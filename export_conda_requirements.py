import subprocess
import os

# 创建 requirements 文件夹，如果不存在的话
if not os.path.exists("requirements"):
    os.makedirs("requirements")

# 获取所有 Conda 环境的名称
try:
    result = subprocess.run(["conda", "env", "list"], capture_output=True, text=True, check=True)
    lines = result.stdout.split("\n")[2:]  # 跳过前两行标题
    envs = [line.split()[0] for line in lines if line.strip()]

    # 遍历每个环境
    for env in envs:
        print(f"Exporting requirements for environment: {env}")
        # 构建保存文件的完整路径
        output_file = os.path.join("requirements", f"{env}-requirements.txt")
        # 构建 PowerShell 命令
        command = f'conda activate {env}; if ($?) {{ pip freeze > "{output_file}" }}'
        subprocess.run(["powershell", "-Command", command], shell=False)
except subprocess.CalledProcessError as e:
    print(f"Error occurred while getting conda environments: {e}")
