# Mnist-test 基于神经网络的手写体识别
* ## 将Mnist_data文件夹与其他测试脚本（.py文件）放在同一文件下，<br/>这样能保证，Mnist_data中的数据被‘.py’文件正确读出；</br>
* ## 或者在执行的‘.py’文件中将“mnist=input_data.read_data_sets('Mnist_data/',one_hot=True)”中的 ‘ Mnist_data/ ’进行修改，修改成手写体数据所在的绝对路径。
