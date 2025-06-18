# 1、破解WiFi的原理是什么？
* 1、暴力破解：用大量常用初始WiFi密码字典，一个一个去尝试，直至破解成功。
评价：操作简单，但是只能处理一些“初级原始”的wifi，密码如果被人为更改后，就很难破解了。
* 2、用 Airodump-ng 和 Aircrack-ng/Hashcat 破解 WPA/WPA2 Wi-Fi 路由器。
* 注：即使现在最新的wpa3安全协议依然可以通过某种技术被破解

# 2、破解WiFi具体工作流程介绍

## 2.1暴力破解
找软件一键点击就行

## 2.2用 Airodump-ng 和 Aircrack-ng/Hashcat 破解 WPA/WPA2 Wi-Fi 路由器。工作流程

### 2.2.1 准备事项：使用命令行具有一般的舒适性
正在运行基于 Debian 的 linux 发行版，最好是 Kali linux（OSX 用户请参阅附录 ）
安装 Aircrack-ng
sudo apt-get install aircrack-ng
拥有支持监控模式的无线网卡（请参阅此处以获取支持的设备列表）

### 2.2.2 破解wifi流程
- 打开监控模式
- 找到你的目标
- 捕获4次握手
- 破解网络密码
相关链接："https://github.com/brannondorsey/wifi-cracking"



