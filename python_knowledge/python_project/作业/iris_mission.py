import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap

# 假设 'Iris.csv' 文件与此脚本位于同一目录下。
# 如果文件不在当前目录，请修改为正确的路径。
FILE_PATH = 'Iris.csv'
TARGET_COLUMN = 'species'
FEATURES = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

print("--- 1. 数据加载与探索性分析 (EDA) ---")
try:
    # 任务 1: 加载数据
    # 🚨 尝试使用 'gbk' 编码来解决 UnicodeDecodeError
    try:
        df = pd.read_csv(FILE_PATH, encoding='gbk')
    except UnicodeDecodeError:
        # 如果 gbk 失败，尝试 'latin-1' (或 'iso-8859-1')
        df = pd.read_csv(FILE_PATH, encoding='latin-1')
    
    # 将列名统一转为小写，以防数据集中列名格式不统一 (如 SepalLengthCm)
    df.columns = df.columns.str.lower().str.replace('[^a-z0-9_]', '', regex=True)
    
    # 确保所需特征和目标列存在
    # 假设 'sepal_width' 和 'petal_width' 在预期的 FEATURES 列表中
    df = df.rename(columns={'sepallengthcm': 'sepal_length', 'sepalwidthcm': 'sepal_width', 
                            'petallengthcm': 'petal_length', 'petalwidthcm': 'petal_width',
                            'species': 'species'})
    
    # 检查并打印数据概览
    print(f"成功加载数据集，共 {len(df)} 条记录。")
    print("\n数据集前 5 行:")
    print(df.head())
    print("-" * 50)

except FileNotFoundError:
    print(f"错误: 文件 '{FILE_PATH}' 未找到。请确保文件路径正确。")
    exit()
except Exception as e:
    # 捕获其他可能的异常，包括最终的 UnicodeDecodeError（如果两种编码都不对）
    print(f"加载数据时发生错误: {e}")
    exit()
# --- 任务 1: 线性回归模型预测 ---
# 目标：预测花瓣宽度 (petal_width) 基于花萼宽度 (sepal_width)
print("\n--- 2. 任务 1: 线性回归模型 ---")

# 准备数据
X_reg = df[['sepal_width']]  # 自变量 (特征)
y_reg = df['petal_width']    # 因变量 (目标)

# 训练线性回归模型
model_reg = LinearRegression()
model_reg.fit(X_reg, y_reg)

# 进行预测
y_pred_reg = model_reg.predict(X_reg)

# 计算 R (相关系数)
# 使用 numpy 计算皮尔逊相关系数
r_value = np.corrcoef(X_reg['sepal_width'], y_reg)[0, 1]

# 计算 r_score (R-squared)
r_score = r2_score(y_reg, y_pred_reg)

print(f"相关系数 (R): {r_value:.4f}")
print(f"决定系数 (r_score / R^2): {r_score:.4f}")
print(f"线性模型方程: Petal_Width = {model_reg.coef_[0]:.4f} * Sepal_Width + {model_reg.intercept_:.4f}")

# 可视化散点图和回归线
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_width', y='petal_width', data=df, hue='species', palette='viridis')
plt.plot(X_reg, y_pred_reg, color='red', linewidth=2, label=f'回归线 (R^2={r_score:.4f})')
plt.title('任务 1: 花瓣宽度 vs. 花萼宽度 的线性回归')
plt.xlabel('花萼宽度 (sepal_width)')
plt.ylabel('花瓣宽度 (petal_width)')
plt.legend()
plt.grid(True)
plt.show()
print("-" * 50)


# --- 任务 2: 分类器训练与测试 ---
# 使用 K-近邻 (KNN) 作为示例分类器
print("\n--- 3. 任务 2: 分类器 (K-NN) ---")

# 准备数据：使用所有四个特征
X_cls = df[FEATURES]
y_cls = df['species']

# 准备训练集和测试集 (任务要求: 前 140 行训练，后 10 行测试)
# 通常做法是使用 train_test_split，但为了严格符合任务要求，手动切分
X_train = X_cls.iloc[:140]
y_train = y_cls.iloc[:140]
X_test = X_cls.iloc[140:]
y_test = y_cls.iloc[140:]

print(f"训练集大小: {len(X_train)} (前 140 行)")
print(f"测试集大小: {len(X_test)} (后 10 行)")

# 算法训练：使用 K-近邻分类器 (K=5)
model_cls = KNeighborsClassifier(n_neighbors=5)
model_cls.fit(X_train, y_train)

# 进行预测
y_pred_cls = model_cls.predict(X_test)

# 统计预测正确数和准确率
correct_predictions = (y_pred_cls == y_test).sum()
total_predictions = len(y_test)
accuracy = model_cls.score(X_test, y_test)

print("\n测试集预测结果:")
test_results = pd.DataFrame({
    '实际类别': y_test, 
    '预测类别': y_pred_cls, 
    '是否正确': (y_pred_cls == y_test)
})
print(test_results)

print(f"\n预测正确数: {correct_predictions} / {total_predictions}")
print(f"测试集预测准确率: {accuracy:.4f}")
print("-" * 50)


# 可视化训练集散点图和决策边界 (仅使用两个特征以方便可视化)
print("\n--- 4. 任务 2: 可视化训练集散点图和决策边界 ---")

# 为了可视化，我们只使用 'petal_length' 和 'petal_width'
X_vis = X_train[['petal_length', 'petal_width']].values
y_vis = y_train.factorize()[0] # 将字符串类别编码为数字 (0, 1, 2)

# 重新训练一个仅包含两个特征的分类器用于决策边界绘制
model_vis = KNeighborsClassifier(n_neighbors=5)
model_vis.fit(X_vis, y_vis)

# 创建绘图网格
h = 0.02 # 网格步长
x_min, x_max = X_vis[:, 0].min() - 0.5, X_vis[:, 0].max() + 0.5
y_min, y_max = X_vis[:, 1].min() - 0.5, X_vis[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# 预测网格上的点以绘制决策边界
Z = model_vis.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 获取原始的类别名称用于图例
target_names = y_train.unique()
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

plt.figure(figsize=(10, 6))
# 绘制决策边界
plt.pcolormesh(xx, yy, Z, cmap=cmap_light, shading='auto')

# 绘制训练集散点图
scatter = plt.scatter(X_vis[:, 0], X_vis[:, 1], c=y_vis, cmap=cmap_bold,
                      edgecolor='k', s=20)

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("任务 2: K-NN 分类器决策边界 (基于花瓣长/宽)")
plt.xlabel('花瓣长度 (petal_length)')
plt.ylabel('花瓣宽度 (petal_width)')

# 创建自定义图例
legend_elements = [plt.scatter([], [], color=cmap_bold(i), label=name) 
                   for i, name in enumerate(target_names)]
plt.legend(handles=legend_elements, title="类别")

plt.show()

print("--- 任务完成 ---")