
# サンプルデータ


```python
import numpy as np
import pandas as pd
import matplotlib .pyplot as plt
import seaborn as sns
import scipy.stats as ss
```

## 線形データ


```python
n=20
```


```python
a = np.arange(n).reshape(4, -1); a  # 5列の行列
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])




```python
df = pd.DataFrame(a, columns=list('abcde')); df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>



## ランダムデータ


```python
r = np.random.randn(4, 5); r
```




    array([[-0.76798351,  0.39545824, -0.18938856, -1.34485011,  0.8722842 ],
           [ 0.87813634, -0.80880185,  1.10395955,  2.44202835,  0.04306526],
           [ 0.33626586,  0.29698914,  0.82286026, -1.07663082, -0.3184203 ],
           [-0.34109916, -0.04371998,  0.9267362 , -0.27744202, -0.16861789]])




```python
df = pd.DataFrame(r, columns=list('abcde')); df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.767984</td>
      <td>0.395458</td>
      <td>-0.189389</td>
      <td>-1.344850</td>
      <td>0.872284</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.878136</td>
      <td>-0.808802</td>
      <td>1.103960</td>
      <td>2.442028</td>
      <td>0.043065</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.336266</td>
      <td>0.296989</td>
      <td>0.822860</td>
      <td>-1.076631</td>
      <td>-0.318420</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.341099</td>
      <td>-0.043720</td>
      <td>0.926736</td>
      <td>-0.277442</td>
      <td>-0.168618</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284ea821780>




![png](README_files/README_9_1.png)



```python
df = pd.DataFrame(np.random.randn(n,n))
```


```python
plt.contourf(df, cmap='jet')
```




    <matplotlib.contour.QuadContourSet at 0x284ea934a20>




![png](README_files/README_11_1.png)


等高線表示


```python
plt.pcolor(df, cmap='jet')
```




    <matplotlib.collections.PolyCollection at 0x284ea9ad3c8>




![png](README_files/README_13_1.png)


カラーマップ表示

## sin波


```python
n=100
x = np.linspace(0, 2*np.pi, n)
```


```python
s = pd.Series(np.sin(x), index=x)
s.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284ea8e3fd0>




![png](README_files/README_17_1.png)


sin波


```python
snoise = s + 0.1 * np.random.randn(n)
sdf = pd.DataFrame({'sin wave':s, 'noise wave': snoise})
sdf.plot(color=('r', 'b'))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284ea9f6588>




![png](README_files/README_19_1.png)


ノイズをのせた

## 正規分布


```python
median = x[int(n/2)]  # xの中央値
g = pd.Series(ss.norm.pdf(x, loc=median), x)
g.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284eaa587f0>




![png](README_files/README_22_1.png)



```python
gnoise = g + 0.01 * np.random.randn(n)
df = pd.DataFrame({'gauss wave':g, 'noise wave': gnoise})
df.plot(color=('r', 'b'))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284eab0ef28>




![png](README_files/README_23_1.png)


## log関数


```python
median = x[int(n/2)]  # xの中央値
x1 = x + 10e-3
l = pd.Series(np.log(x1), x1)
l.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284eab426a0>




![png](README_files/README_25_1.png)



```python
lnoise = l + 0.1 * np.random.randn(n)
df = pd.DataFrame({'log wave':l, 'noise wave': lnoise})
df.plot(color=('r', 'b'))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284eabece10>




![png](README_files/README_26_1.png)


## ランダムウォーク


```python
n = 1000
se = pd.Series(np.random.randint(-1, 2, n)).cumsum()
se.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284f3c62c18>




![png](README_files/README_28_1.png)


np.random.randint(-1, 2, n)で(-1, 0, 1)のどれかをランダムにn個生成し、cumsum()で積み上げ合計していくことでランダムウォークを描く。


```python
sma100 = se.rolling(100).mean()
ema100 = se.ewm(span=100).mean()

df = pd.DataFrame({'Chart': se,  'SMA100': sma100, 'EMA100': ema100})
df.plot(style = ['--','-','-'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x284f3cadcc0>




![png](README_files/README_30_1.png)


単純移動平均線(Simple Moving Average)と指数移動平均線(Exponential Moving Average)を同時に描画した。
EMAの方がSMAと比べて一般的に直近の動きを反映しやすく、トレンドに追随しやすいといわれている。
