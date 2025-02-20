import socket
import random

def send_empty_udp():
    # 创建UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 目标地址和端口
    server_address = ('165.154.96.229', 22)
    
    try:
        # 发送空数据包
        print(f"正在向 {server_address} 发送空UDP包...")
        sock.sendto(b"", server_address)
        print("发送成功！")
    except Exception as e:
        print(f"发送失败: {e}")
    finally:
        sock.close()

def send_malformed_udp():
    # 创建UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 目标地址和端口
    server_address = ('165.154.96.229', 22)
    
    try:
        # 创建畸形数据包（随机字节）
        malformed_data = bytes([random.randint(0, 255) for _ in range(1024)])
        
        # 发送畸形数据包
        print(f"正在向 {server_address} 发送畸形UDP包...")
        sock.sendto(malformed_data, server_address)
        print("发送成功！")
    except Exception as e:
        print(f"发送失败: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    # send_empty_udp()
    send_malformed_udp() 