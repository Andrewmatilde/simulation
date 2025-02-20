import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import time

class QueueSimulation:
    def __init__(self, arrival_rate, num_queues, service_rates, simulation_time):
        self.arrival_rate = arrival_rate  # 总体到达率
        self.num_queues = num_queues  # 队列数量
        self.service_rates = service_rates  # 每种服务率的处理速度
        self.simulation_time = simulation_time  # 模拟时间
        self.queues = defaultdict(list)  # 存储每个队列的长度随时间变化
        self.current_lengths = np.zeros(num_queues)  # 当前每个队列的长度
        
    def generate_arrivals(self):
        # 生成泊松到达的时间点
        arrivals = []
        t = 0
        while t < self.simulation_time:
            # 生成下一个到达间隔
            interval = np.random.exponential(1/self.arrival_rate)
            t += interval
            if t < self.simulation_time:
                arrivals.append(t)
        return arrivals
    
    def assign_service_rates(self):
        # 为每个队列随机分配处理速率
        return np.random.choice(self.service_rates, size=self.num_queues)
    
    def run_simulation(self):
        arrivals = self.generate_arrivals()
        queue_service_rates = self.assign_service_rates()
        
        # 对每个队列，计算在模拟时间内能处理的请求数
        processed_per_queue = queue_service_rates * self.simulation_time
        
        # 随机分配到达请求到队列
        queue_assignments = np.random.randint(0, self.num_queues, size=len(arrivals))
        
        # 计算每个队列的最终长度（到达数 - 处理数）
        arrivals_per_queue = np.bincount(queue_assignments, minlength=self.num_queues)
        final_lengths = np.maximum(arrivals_per_queue - processed_per_queue, 0)
        
        return final_lengths
    
    def plot_results(self, final_lengths):
        plt.figure(figsize=(12, 6))
        
        # 绘制队列长度的直方图
        plt.hist(final_lengths, bins=50, density=True, alpha=0.7)
        plt.xlabel('队列长度')
        plt.ylabel('频率')
        plt.title(f'队列长度分布 (到达率={self.arrival_rate}, {self.num_queues}个队列)')
        plt.grid(True, alpha=0.3)
        
        # 添加统计信息
        plt.text(0.98, 0.95, 
                f'平均长度: {np.mean(final_lengths):.2f}\n'
                f'最大长度: {np.max(final_lengths):.2f}\n'
                f'标准差: {np.std(final_lengths):.2f}',
                transform=plt.gca().transAxes,
                verticalalignment='top',
                horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        plt.show()

# 运行模拟
if __name__ == "__main__":
    # 设置参数
    ARRIVAL_RATE = 6400  # 总体到达率
    NUM_QUEUES = 64    # 队列数量
    SERVICE_RATES = [100]  # 可能的服务速率
    SIMULATION_TIME = 3600  # 模拟1小时
    
    # 创建并运行模拟
    sim = QueueSimulation(ARRIVAL_RATE, NUM_QUEUES, SERVICE_RATES, SIMULATION_TIME)
    final_lengths = sim.run_simulation()
    
    # 显示结果
    sim.plot_results(final_lengths) 