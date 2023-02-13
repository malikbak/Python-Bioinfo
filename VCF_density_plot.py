#!/usr/bin/env python
# coding: utf-8

# In[5]:


import allel


# In[16]:


callset = allel.read_vcf('chr02.vcf')


# In[7]:


sorted(callset.keys())


# In[8]:


callset['samples']


# In[9]:


callset['variants/CHROM']


# In[10]:


callset['variants/POS']


# In[11]:


callset['calldata/GT']


# In[12]:


gt = allel.GenotypeArray(callset['calldata/GT'])
gt


# In[13]:


callset['variants/ALT']


# In[18]:


df = allel.vcf_to_dataframe('chr02.vcf', fields='*', alt_number=2)
df


# In[19]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[23]:


import zarr
allel.vcf_to_zarr('chr02.vcf', 'example.zarr', fields='*', overwrite=True)


# In[26]:


zarr_path = 'example.zarr'
vcf_path = 'chr02.vcf'


# In[29]:


import sys
import numcodecs
allel.vcf_to_zarr(vcf_path, zarr_path, group='22',
                  fields='*', alt_number=8, log=sys.stdout,
                  compressor=numcodecs.Blosc(cname='zstd', clevel=1, shuffle=False))


# In[31]:


callset_h1k = zarr.open_group(zarr_path, mode='r')
callset_h1k


# In[34]:


import ipytree
callset_h1k.tree(expand=True)


# In[35]:


pos = allel.SortedIndex(callset_h1k['22/variants/POS'])
pos


# In[36]:


def plot_windowed_variant_density(pos, window_size, title=None):
    
    # setup windows 
    bins = np.arange(0, pos.max(), window_size)
    
    # use window midpoints as x coordinate
    x = (bins[1:] + bins[:-1])/2
    
    # compute variant density in each window
    h, _ = np.histogram(pos, bins=bins)
    y = h / window_size
    
    # plot
    fig, ax = plt.subplots(figsize=(12, 3))
    sns.despine(ax=ax, offset=10)
    ax.plot(x, y)
    ax.set_xlabel('Chromosome position (bp)')
    ax.set_ylabel('Variant density (bp$^{-1}$)')
    if title:
        ax.set_title(title)


# In[38]:


import numpy as np
plot_windowed_variant_density(pos, window_size=100000, title='Variant density')


# In[ ]:




