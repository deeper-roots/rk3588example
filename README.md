准备：
1、找到rk3588 npu官方文档（本项目基于2.0版本，下载时应下载2.0版本，不然模型不能正常加载，推理），并下载（链接：https://github.com/rockchip-linux/rknpu2）

2、找到 rknn-toolkit2-master\rknn-toolkit2-master\rknn-toolkit2\packages 下的txt文件，找到对应版本的txt文件，文件名cp XY 即表示python的版本是X.Y

![屏幕截图 2024-07-11 213256](https://github.com/deeper-roots/rk3588example/assets/61220762/9f8bec42-9764-4c60-a8d6-849a6e75fdda)

3、将文件复制到rk3588平台，本项目基于香橙派，系统是ubuntu，远程将文件下载某一路径，打开终端，输入pip install -r 文件名.txt


4、找到\rknn-toolkit2-master\rknn-toolkit-lite2\packages 下的文件，找到对应版本的whl文件，与上一步类似，在终端输入pip install 文件名.whl

5、rknn即安装好












pycharm远程连接
0、在windows系统打开本项目文件
1、找到如下图所示，点击ON SHH

![屏幕截图 2024-07-11 211557](https://github.com/deeper-roots/rk3588example/assets/61220762/79f5d06c-c77f-49b4-90c8-f2da0d05541c)


2、输入rk2588平台的ip（填写在host那一栏），username那一栏填写linux的用户名

![屏幕截图 2024-07-11 211730](https://github.com/deeper-roots/rk3588example/assets/61220762/dfb79772-c645-4374-bc8c-5e9ad398bb5c)


3、输入用户名对应的密码

![屏幕截图 2024-07-11 211857](https://github.com/deeper-roots/rk3588example/assets/61220762/e89a57d1-d1a8-40c9-b3b7-700af6c745aa)


4、完成连接后，选择python解释器（一定要找安装好rk3588包对应的解释器，如果是直接安装，则默认即可，如果是通过conda创建的虚拟环境，需要找到对应的python.exe的路径）

![屏幕截图 2024-07-11 212431](https://github.com/deeper-roots/rk3588example/assets/61220762/fbd8f977-2f10-4283-96c7-833d186cc176)


5、Sync folders 填写你想在rk3588平台上放置项目的路径，点击创建，既可以远程调试


6、右击项目文件夹，找到deployment，选择第一个upload to  XXXXXXXX

![屏幕截图 2024-07-11 212845](https://github.com/deeper-roots/rk3588example/assets/61220762/33cd3ad5-0b26-4eff-baec-9192b1f1976d)


 7、点击运行，即可在rk3588平台运行程序
