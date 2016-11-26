
# coding: utf-8

# # サンプルデータ

# ## 線形データ

# In[1]:

n=20


# In[2]:

a = np.arange(n).reshape(4, -1); a  # 5列の行列


# In[3]:

df = pd.DataFrame(a, columns=list('abcde')); df


# ## ランダムデータ

# In[4]:

r = np.random.randn(4, 5); r


# In[5]:

df = pd.DataFrame(r, columns=list('abcde')); df


# In[6]:

df.plot()


# In[7]:

df = pd.DataFrame(np.random.randn(n,n))


# In[8]:

plt.contourf(df, cmap='jet')


# 等高線表示

# In[9]:

plt.pcolor(df, cmap='jet')


# カラーマップ表示

# ## sin波

# In[10]:

n=100
x = np.linspace(0, 2*np.pi, n)


# In[11]:

s = pd.Series(np.sin(x), index=x)
s.plot()


# sin波

# In[12]:

snoise = s + 0.1 * np.random.randn(n)
sdf = pd.DataFrame({'sin wave':s, 'noise wave': snoise})
sdf.plot(color=('r', 'b'))


# ノイズをのせた

# ## 正規分布

# In[13]:

from  scipy import stats as ss


# In[14]:

median = x[int(n/2)]  # xの中央値
g = pd.Series(ss.norm.pdf(x, loc=median), x)
g.plot()


# In[15]:

gnoise = g + 0.01 * np.random.randn(n)
df = pd.DataFrame({'gauss wave':g, 'noise wave': gnoise})
df.plot(color=('r', 'b'))


# ## log関数

# In[16]:

median = x[int(n/2)]  # xの中央値
x1 = x + 10e-3
l = pd.Series(np.log(x1), x1)
l.plot()


# In[17]:

lnoise = l + 0.1 * np.random.randn(n)
df = pd.DataFrame({'log wave':l, 'noise wave': lnoise})
df.plot(color=('r', 'b'))


# In[ ]:



