import heapq
from dataclasses import dataclass
from typing import Any, Callable, Dict
from enum import Enum
import random
import math
import statistics

def generate_job_rate(mean: float) -> float:
    """生成作业速率,服从指数分布
        
    Args:
        mean: 分布的均值
    Returns:
        float: 生成的作业速率
    """
        
    return mean


def cpu_rate(num:int, task_rate:float) -> float:
    """计算cpu速率
    
    Args:
        num: cpu数量
        task_rate: 任务速率
    """
    return task_rate / num

class Cluster:
    def __init__(self, init_nodes: int):
        self.running_nodes = init_nodes
        self.pending_nodes = 0
        self.creating_nodes = 0
        self.deleting_nodes = 0
        self.target = init_nodes
class Monitoring:
    def __init__(self, alpha_rate: float):
        self.total_cpu_rate = []
        self.running_cpu_rate = []
        self.pending_task_rate = []
        self.alpha_rate = alpha_rate

    def update(self, job_rate: float, node_num: int, pending_node: int):
        total = job_rate / (node_num + pending_node)
        running = total

        self.total_cpu_rate.append(total)
        self.running_cpu_rate.append(running)

class TimeLine:
    def __init__(self, timeline: list[int]):
        self.taks_line: list[float] = [generate_job_rate(timeline[i]) for i in range(len(timeline))]

    def loop(self, cluster: Cluster, target: float, alpha_rate: float) -> float:
        loss = [0 for _ in range(len(self.taks_line))]
        monitoring = Monitoring(alpha_rate)
        action_line = {}
        target_line = []
        for i in range(len(self.taks_line)):
            job_rate = self.taks_line[i]
            monitoring.update(job_rate, cluster.running_nodes, cluster.pending_nodes)
            if i % 2 == 0:
                diff = sum(monitoring.running_cpu_rate[-2:])/(2 if len(monitoring.running_cpu_rate) > 2 else 1) - target
                if diff > 0.1:
                    cluster.target = cluster.running_nodes + math.ceil(diff*cluster.running_nodes)
                elif diff < -0.1:
                    cluster.target = cluster.running_nodes + math.floor(diff*cluster.running_nodes)
            cluster_future = cluster.running_nodes + cluster.pending_nodes + cluster.creating_nodes - cluster.deleting_nodes
            if cluster.target != cluster_future:
                if i+4 not in action_line:
                    action_line[i+2] = []
                if cluster.target > cluster_future:
                    creating_nodes = cluster.target - cluster_future
                    cluster.creating_nodes += creating_nodes
                    action_line[i+2].append(("add_pending", creating_nodes))
                else:
                    deleting_nodes = cluster_future - cluster.target
                    cluster.deleting_nodes += deleting_nodes
                    action_line[i+2].append(("remove_node", deleting_nodes))
            if i in action_line:
                for action in action_line[i]:
                    if action[0] == "add_pending":
                        cluster.pending_nodes += action[1]
                        if i + 1 not in action_line:
                            action_line[i + 1] = []
                        cluster.creating_nodes -= action[1]
                        action_line[i + 1].append(("add_running", action[1]))
                    elif action[0] == "remove_node":
                        cluster.deleting_nodes -= action[1]
                        cluster.running_nodes -= action[1]
                    elif action[0] == "add_running":
                        cluster.running_nodes += action[1]
                        cluster.pending_nodes -= action[1]
            loss[i] = (cluster.running_nodes + cluster.pending_nodes) / 2 - job_rate
            target_line.append(cluster.target)
        print(action_line)

        print(target_line)
        return loss
    

if __name__ == "__main__":
    timeline = [10 + i if i < 40 else (40 - i) for i in range(80)]
    print(timeline)
    cluster = Cluster(20)
    timeline = TimeLine(timeline)
    loss = timeline.loop(cluster, 0.5, 0.6)
    print(sum(loss)/len(loss))

