# 算法进阶：如何让模型更接近标准答案

> 国一和国二的核心差距不在"选了什么算法"，而在"怎么用这个算法"。

## 一、单一算法 → 混合算法

### 1.1 为什么需要混合

| 单一算法 | 优势 | 劣势 |
|---------|------|------|
| GA | 全局搜索能力强 | 局部收敛慢，精度不高 |
| SA | 收敛稳定 | 退火速度难调 |
| PSO | 收敛快 | 容易早熟 |
| 梯度下降 | 局部精度高 | 需要好的初始点，不能处理离散变量 |
| 模式搜索 | 不依赖梯度 | 步长难定，高维效率低 |

**混合策略**：用 GA 找到全局最优区域 → 用梯度下降/模式搜索精修到高精度。

### 1.2 经典混合方案

**GA + 局部搜索 = Memetic Algorithm**：
```python
def memetic_algorithm():
    pop = initialize_population()
    for gen in range(max_gen):
        pop = ga_operators(pop)    # 全局探索
        for ind in pop:
            ind = local_search(ind) # 局部精修（每个个体都做）
        pop = select(pop)
    return best(pop)
```

效果：GA 保证不陷入局部最优，局部搜索保证最终精度。

**SA + 梯度下降 = 两阶段法**：
```python
# 阶段一：SA 全局搜索
best_solution = simulated_annealing(...)
# 阶段二：用 SA 的结果作为梯度下降的初始点
final_solution = gradient_descent(best_solution, ...)
```

效果：SA 的输出精度通常是 95-98%，梯度下降可以推到 99.5%+。

**PSO + 混沌扰动**：
```python
# 标准 PSO 更新
velocity = w * velocity + c1*r1*(pbest - x) + c2*r2*(gbest - x)
x = x + velocity
# 如果检测到停滞（gbest 连续 K 代不变）
if stagnation_counter > K:
    x = x + chaotic_perturbation()  # 混沌映射产生新的搜索方向
    stagnation_counter = 0
```

### 1.3 什么时候混合不值得

- 如果 SA 已经收敛到 <0.1% 精度 → 不需要额外的梯度下降
- 如果约束全是线性的 → 直接用 LP/MILP 求解器，比任何启发式都快
- 如果模型本身有很大不确定性 → 精度 1% 和 0.1% 对结论没区别

## 二、评价类问题的进阶技巧

### 2.1 权重确定：主客观结合

**二等奖**：只用 AHP（纯主观）或只用熵权法（纯客观）
**国一**：AHP + 熵权法，取两种权重的加权平均

```python
# 主观权重（AHP）
w_ahp = ahp(comparison_matrix)
# 客观权重（熵权法）
w_entropy = entropy_weight(data)
# 组合权重（通常 α=0.5，可在 [0.3, 0.7] 做灵敏度）
w_combined = alpha * w_ahp + (1 - alpha) * w_entropy
```

**比单一方法强在哪**：评委看到"主客观结合"就知道你考虑了两种角度的信息，比"我只用了 AHP" 高出至少一个档次。

### 2.2 一致性检验不要只报 CR

**二等奖**：CR = 0.06 < 0.1，通过
**国一**：CR = 0.06 < 0.1，通过。进一步，对判断矩阵做扰动分析——每个元素 ±10%，CR 变化范围 [0.04, 0.08]，均 < 0.1，结论稳健。

### 2.3 TOPSIS 的排名敏感性

```python
# 对原始数据矩阵加入 ±5% 噪声
perturbed_ranks = []
for _ in range(100):
    noisy_data = data * (1 + np.random.uniform(-0.05, 0.05, data.shape))
    ranks = topsis(noisy_data, weights)
    perturbed_ranks.append(ranks)

# 计算每个方案排名的均值和标准差
rank_mean = np.mean(perturbed_ranks, axis=0)
rank_std = np.std(perturbed_ranks, axis=0)

# 如果两个方案的排名差距 < 1σ → 说明排名不稳定，需要讨论
```

## 三、预测类问题的进阶技巧

### 3.1 点预测 → 区间预测

**二等奖**：预测值是 1234
**国一**：预测值 1234，95% 置信区间 [1180, 1288]（Bootstrap 1000 次）

```python
from sklearn.utils import resample
predictions = []
for _ in range(1000):
    X_boot, y_boot = resample(X_train, y_train)
    model.fit(X_boot, y_boot)
    predictions.append(model.predict(X_test))
ci_lower = np.percentile(predictions, 2.5, axis=0)
ci_upper = np.percentile(predictions, 97.5, axis=0)
```

### 3.2 模型可解释性

**XGBoost/LightGBM 的特征重要性**：
```python
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)
shap.summary_plot(shap_values, X)  # SHAP 蜂群图
```

**线性模型的系数解释**：
```
销售额 = 2.34 × 广告投入 + 0.87 × 促销天数 - 1.23 × 竞品价格 + 156
        (p<0.001)          (p=0.003)          (p<0.001)
解释：广告投入每增加 1 万元，销售额增加 2.34 万元（95%CI [1.98, 2.70]）
```

## 四、微分方程/物理题的进阶技巧

### 4.1 参数辨识

题目给了测量数据，要反推模型参数 → **最小二乘 + 优化**

```python
from scipy.optimize import least_squares

def residuals(params, t, y_observed):
    """ODE 模型预测值与观测值的残差"""
    k1, k2, k3 = params  # 待辨识参数
    y_predicted = solve_ode([k1, k2, k3], t)
    return y_predicted - y_observed

result = least_squares(residuals, x0=[0.1, 0.1, 0.1], args=(t_data, y_data))
```

### 4.2 数值解精度验证

- 步长减半：步长从 dt 减到 dt/2，结果变化 < 0.1% → 数值解可信
- 守恒量检查：如果系统有守恒量（能量/质量），检验每一步是否守恒
- 解析解对照：如果简化版本有解析解，用数值解与之比较

### 4.3 刚性系统处理

如果时间尺度差异大（如快反应 + 慢扩散）→ 用刚性求解器：

```python
from scipy.integrate import solve_ivp
# method='Radau' 或 'BDF' 处理刚性问题
sol = solve_ivp(ode_func, [t0, tf], y0, method='Radau', rtol=1e-8, atol=1e-10)
```

## 五、统计类问题的进阶技巧

### 5.1 不只是 Pearson 相关系数

- Pearson：线性关系
- Spearman：单调关系（不要求线性）
- 距离相关系数：任何形式的关系（包括非线性、非单调）
- MIC（最大信息系数）：探测任何函数关系

### 5.2 假设检验不只是 p < 0.05

```
t = 3.42, df = 198, p = 0.0008
效应量 Cohen's d = 0.48（中等效应）
95% CI of difference: [2.3, 8.1]
```

**p 值 + 效应量 + 置信区间** → 完整统计报告

## 六、通用的"让结果更好"技巧

### 6.1 数据预处理直接影响结果质量

- 缺失值：不要无脑填充均值。先画缺失模式热力图 → 判断是 MCAR/MAR/MNAR → 选择对应方法
- 异常值：IQR 法阈值 1.5 → 对正态数据 ok；对偏态数据用调整后箱线图
- 标准化：对优化问题用 Min-Max（保持边界）；对统计问题用 Z-score（保持分布形状）

### 6.2 交叉验证不是做一次就完

```python
from sklearn.model_selection import RepeatedKFold
# 5 折 × 10 次重复 → 50 个评估结果 → 报告均值 ± 标准差
rkf = RepeatedKFold(n_splits=5, n_repeats=10, random_state=42)
scores = cross_val_score(model, X, y, cv=rkf, scoring='neg_mean_squared_error')
print(f"MSE = {-scores.mean():.4f} ± {scores.std():.4f}")
```

### 6.3 回归结果必须检查残差

```python
import scipy.stats as stats
residuals = y_true - y_pred
# 1. 正态性
_, p_norm = stats.shapiro(residuals)
# 2. 异方差性（Breusch-Pagan test）
# 3. 自相关性（Durbin-Watson test for time series）
# 4. 残差图：残差 vs 拟合值
```

残差不满足假设 → 模型有系统性偏差 → 需要改进模型，不是忽略残差。

## 七、模型选择总结表

| 题目特征 | 基线（快速） | 主模型（标准） | 冲刺（国一） |
|---------|------------|-------------|------------|
| 连续优化 | 线性规划 | GA/SA | **混合算法 + 多起点 + 局部精修** |
| 离散优化 | 贪心 | GA（整数编码） | **分支定界 + GA 混合** |
| 多目标 | 加权和 | NSGA-II | **ε-约束法 + 理想点法** |
| 时间序列预测 | 指数平滑 | ARIMA/LSTM | **Ensemble + Bootstrap 区间** |
| 回归预测 | 线性回归 | XGBoost | **Stacking + SHAP 解释** |
| 综合评价 | AHP | 熵权+TOPSIS | **主客观结合 + 排名敏感性** |
| 分类 | 逻辑回归 | RF/SVM | **Soft voting ensemble + 概率校准** |
| 微分方程 | Euler 法 | RK4 | **刚性求解器 + 参数辨识** |
| 仿真 | 简单 MC | LHS 抽样 | **Sobol 序列 + 方差缩减** |
