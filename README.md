准备：
1、找到rk3588 npu官方文档（本项目基于2.0版本，下载时应下载2.0版本，不然模型不能正常加载，推理），并下载（链接：https://github.com/rockchip-linux/rknpu2）

2、找到 rknn-toolkit2-master\rknn-toolkit2-master\rknn-toolkit2\packages 下的txt文件，找到对应版本的txt文件，文件名cp XY 即表示python的版本是X.Y

3、将文件复制到rk3588平台，本项目基于香橙派，系统是ubuntu，远程将文件下载某一路径，打开终端，输入pip install -r 文件名.txt


4、找到\rknn-toolkit2-master\rknn-toolkit-lite2\packages 下的文件，找到对应版本的whl文件，与上一步类似，在终端输入pip install 文件名.whl

5、rknn即安装好

![image](https://github.com/deeper-roots/rk3588example/assets/61220762/59d2ee16-eb8a-41db-b90c-b8f077cd767c)










pycharm远程连接
0、在windows系统打开本项目文件
1、找到如下图所示，点击ON SHH

![屏幕截图 2024-07-11 211557](https://github.com/deeper-roots/rk3588example/assets/61220762/3b88194d-00e5-4373-8baa-b9f564350168)

2、输入rk2588平台的ip（填写在host那一栏），username那一栏填写linux的用户名

![屏幕截图 2024-07-11 211730](https://github.com/deeper-roots/rk3588example/assets/61220762/0b4653dc-6d2a-448a-ad97-8929358af6b9)


3、输入用户名对应的密码

![屏幕截图 2024-07-11 211857](https://github.com/deeper-roots/rk3588example/assets/61220762/02b48200-d8a2-4232-91a9-85c5ab1cc172)

4、完成连接后，选择python解释器（一定要找安装好rk3588包对应的解释器，如果是直接安装，则默认即可，如果是通过conda创建的虚拟环境，需要找到对应的python.exe的路径）

![image](https://github.com/deeper-roots/rk3588example/assets/61220762/90777ca3-a70d-4ba9-8182-b8f9c1345929)

5、Sync folders 填写你想在rk3588平台上放置项目的路径，点击创建，既可以远程调试


6、右击项目文件夹，找到deployment，选择第一个upload to  XXXXXXXX

![image](https://github.com/deeper-roots/rk3588example/assets/61220762/23a27442-ece4-411e-8a66-34140b3dea08)

 7、点击运行，即可在rk3588平台运行程序
