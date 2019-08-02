from distutils.core import setup

setup(
    name = "knlp",                # 包名
    version = "0.1.BETA",              # 版本信息
    packages = ['knlp', 'knlp/preprocess'],          # 要打包的项目文件夹
    include_package_data=True,    # 自动打包文件夹内所有数据
    zip_safe=True,                # 设定项目包为安全，不用每次都检测其安全性
    install_requires = [          # 安装依赖的其他包（测试数据）
    #'docutils>=0.3',
    #'requests',
    ],
    package_data={"knlp/preprocess": ["*.dict"]}
)