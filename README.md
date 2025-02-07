# conda-req-batch-exporter
Conda 环境依赖批量导出工具

输出所有conda env 的依赖，依次生成requirements.txt文件, 方便环境迁移

部分conda环境因读写权限问题，可能无法导出

## notebook

![cmd](./assets/notebook.png)

## bash

```cmd
python export_conda_requirements.py
```

![cmd](./assets/cmd.png)