# TensorFlow-Rasberry-pai

    1.树莓派和TensorFlow syste version不匹配
        树莓派system “version 2018-11-13-raspbian-stretch.zip” 
        TensorFlow systemversion “tensorflow-1.11.0-cp35-none-linux_armv7l.whl”
        这样在安装时出现错误      File "/usr/share/python-wheels/urllib3-1.19.1-py2.py3-none-any.whl/urllib3/util/retry.py", line 315, in increment total -= 1TypeError: unsupported operand type(s) for -=: 'Retry' and 'int'
    2.已知安装成功
        树莓派system “version 2018-11-13-raspbian-stretch.zip” 
        TensorFlow systemversion “tensorflow-1.9.0-cp35-none-linux_armv7l.whl”
    3.安装tensorflow

        首先安装tensorflow所需要的依赖库和工具

            sudo apt-get update
             
            # For Python 2.7
            sudo apt-get install python-pip python-dev
             
            # For Python 3.3+
            sudo apt-get install python3-pip python3-dev

        然受按装tensorflow：

        如果之前没有安装过其他版本的tensorflow，直接：

            # For Python 2.7
            sudo pip install tensorflow-1.8.0-cp27-none-linux_armv7l.whl
             
            # For Python 3.4
            sudo pip3 install tensorflow-1.8.0-cp35-none-linux_armv7l.whl

        如果之前安装过其他版本的tensorflow，先卸载，再安装

            sudo pip3 uninstall tensorflow
            sudo pip3 install --upgrade tensorflow-1.8.0-cp35-none-linux_armv7l.whl

        完成！


    4.测试


        pi@raspberrypi:~ $ python3
        Python 3.5.3 (default, Sep 27 2018, 17:25:39)
        [GCC 6.3.0 20170516] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import tensorflow as tf

        >>>
        >>> tf.__version__
        '1.9.0'

        欢迎来到TensorFlow
