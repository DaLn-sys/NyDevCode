import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, LSTM, Dropout
from tensorflow.keras.callbacks import ReduceLROnPlateau
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('data.csv')
load_data = data['load'].values

# 归一化
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(load_data.reshape(-1, 1))

# 创建训练集和测试集
train_size = int(len(scaled_data) * 0.8)
train_data, test_data = scaled_data[:train_size], scaled_data[train_size:]

# 创建序列数据
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 10
X_train, y_train = create_dataset(train_data, look_back)
X_test, y_test = create_dataset(test_data, look_back)

# Reshape input to be [samples, time steps, features]
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# 创建 RNN 模型
model_rnn = Sequential()
model_rnn.add(SimpleRNN(50, input_shape=(look_back, 1)))
model_rnn.add(Dropout(0.2))
model_rnn.add(Dense(1))
model_rnn.compile(loss='mean_squared_error', optimizer='adam')

# 创建 LSTM 模型
model_lstm = Sequential()
model_lstm.add(LSTM(50, input_shape=(look_back, 1)))
model_lstm.add(Dropout(0.2))
model_lstm.add(Dense(1))
model_lstm.compile(loss='mean_squared_error', optimizer='adam')

# 回调函数
reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.5, patience=5, min_lr=0.00001)

# 训练模型并保存每个epoch的损失
history_rnn = model_rnn.fit(X_train, y_train, epochs=50, batch_size=64, verbose=2, callbacks=[reduce_lr])
history_lstm = model_lstm.fit(X_train, y_train, epochs=50, batch_size=64, verbose=2, callbacks=[reduce_lr])

# 预测
train_predict_rnn = model_rnn.predict(X_train)
test_predict_rnn = model_rnn.predict(X_test)
train_predict_lstm = model_lstm.predict(X_train)
test_predict_lstm = model_lstm.predict(X_test)

# 反归一化
train_predict_rnn = scaler.inverse_transform(train_predict_rnn)
test_predict_rnn = scaler.inverse_transform(test_predict_rnn)
train_predict_lstm = scaler.inverse_transform(train_predict_lstm)
test_predict_lstm = scaler.inverse_transform(test_predict_lstm)

y_train_inv = scaler.inverse_transform(y_train.reshape(-1, 1))
y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))

# 计算 RMSE
train_score_rnn = np.sqrt(np.mean((train_predict_rnn - y_train_inv)**2))
test_score_rnn = np.sqrt(np.mean((test_predict_rnn - y_test_inv)**2))
train_score_lstm = np.sqrt(np.mean((train_predict_lstm - y_train_inv)**2))
test_score_lstm = np.sqrt(np.mean((test_predict_lstm - y_test_inv)**2))

print(f'RNN Train Score: {train_score_rnn:.2f} RMSE')
print(f'RNN Test Score: {test_score_rnn:.2f} RMSE')
print(f'LSTM Train Score: {train_score_lstm:.2f} RMSE')
print(f'LSTM Test Score: {test_score_lstm:.2f} RMSE')

# 可视化结果
plt.figure(figsize=(18, 6))

# 训练数据的预测
plt.subplot(1, 3, 1)
plt.plot(scaler.inverse_transform(scaled_data[:train_size]), label='True Data')
plt.plot(np.arange(look_back, len(train_predict_rnn) + look_back), train_predict_rnn, label='RNN Predict')
plt.plot(np.arange(look_back, len(train_predict_lstm) + look_back), train_predict_lstm, label='LSTM Predict')
plt.xlabel('Time')
plt.ylabel('Load')
plt.title('Train Data Prediction')
plt.legend()

# 测试数据的预测
plt.subplot(1, 3, 2)
plt.plot(scaler.inverse_transform(scaled_data[train_size:]), label='True Data')
plt.plot(np.arange(look_back, len(test_predict_rnn) + look_back), test_predict_rnn, label='RNN Predict')
plt.plot(np.arange(look_back, len(test_predict_lstm) + look_back), test_predict_lstm, label='LSTM Predict')
plt.xlabel('Time')
plt.ylabel('Load')
plt.title('Test Data Prediction')
plt.legend()

# 绘制损失图
plt.subplot(1, 3, 3)
plt.plot(history_rnn.history['loss'], label='RNN Loss')
plt.plot(history_lstm.history['loss'], label='LSTM Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Model Loss')
plt.legend()

plt.tight_layout()
plt.show()
