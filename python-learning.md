# 对 Python 的一些理解

Python 作为解释型语言，它在运行时解释一行行代码并执行，因此通常不需要打包成二进制文件就能直接使用，这使得它的运行速度虽然不如编译语言，但此特性也让它在运行时动态地执行非项目代码成为可能。

# 安装 Python

主要对 Windows 的“安装程序”和“嵌入式包”进行说明。

## 安装程序（installer）

- 包含所有组件，对于使用 Python 进行任何类型项目的开发人员而言，它是最佳选择。

##### 注意

`python` 命令可能会由于环境变量和“应用执行别名”导致问题， 如果你不想详细了解这些问题，可以使用 `py`
命令，后续的所有 `python` **全局**命令中都应该注意此事项。

## 嵌入式包（embeddable package）

- 是一个包含最小 Python 环境的 ZIP 文件。
- 不支持像常规 Python 安装程序那样使用 pip 来管理依赖关系。（所以如果你的电脑中只有嵌入式包，你可能无法正常执行使用了 pip
  模块相关内容的脚本）

# 项目管理

## 虚拟环境

项目之间的环境隔离可以避免很多冲突，隔离环境就可以使用虚拟环境。

Python 推荐使用虚拟环境，虚拟环境的优点：

1. 依赖隔离：虚拟环境为每个项目提供了独立的运行时环境，确保项目之间的依赖不会彼此冲突。每个项目都有自己的库版本，而不会影响到其他项目。
2. 环境一致性：无论是在开发、测试还是生产环境中，虚拟环境可以确保 Python 库的版本一致性。这有助于减少“在我的机器上运行正常”问题。
3. 轻松管理：通过虚拟环境，开发者可以轻松地添加、更新或删除依赖，而不会影响全局 Python 环境或需要管理员权限。
4. 简化部署：虚拟环境可以生成 `requirements.txt` 或相似的文件，以复制或重建相同的环境，简化了项目的部署和迁移。
5. 多 Python 版本：虚拟环境允许在同一台机器上使用多个 Python 版本，适合同时参与使用不同 Python 版本的项目。
6. 开发工作流：它支持现代 Python 工作流程，与诸如 pipenv、poetry 或 conda 等工具紧密集成。

### 创建虚拟环境

使用命令创建虚拟环境：

```cmd
python -m venv <.venv>
```

将 `<.venv>` 替换为你想设置的虚拟环境路径名称，支持路径层级结构（/），如果有空格，可以使用引号 `"` 引住，但推荐的路径名称为 `<.venv>`。

### 激活虚拟环境

什么是激活虚拟环境？

激活虚拟环境会更改当前终端或命令行界面的提示符，通常在开头添加虚拟环境的名称（例如：(.venv)）。

激活虚拟环境使得你可以使用虚拟环境中的 Python 命令。并确保任何 Python 相关的操作（如运行 Python 应用程序、安装或移除 Python 库）都限定在这个环境内完成。

#### Windows 激活

```cmd
<venv-path>\Scripts\activate
```

#### Unix 或 MacOS

```bash
source <venv-path>/bin/activate
```

### 撤销激活虚拟环境

命令行中输入 `deactivate`。

```cmd
deactivate
```

### 为工具模块创建虚拟环境

如果你不太喜欢将一些工具性的模块安装在 Python 的安装路径下，你想维持 Python 原始安装路径的整洁清晰，那你可以为这些第三方工具模块创建一个虚拟环境，以支持这些模块的存放及运行。

这是一个例子：

我将创建一个名为 “tools-env” 的虚拟环境：

```cmd
python -m venv tools-env
```

为了能够快速激活虚拟环境，我在 Python 的安装目录下创建两个文件：

pytool.cmd

```cmd
D:\Python\tools-env\Scripts\activate
```

pytool.ps1

```angular2html
D:\Python\tools-env\Scripts\Activate.ps1
```

由于我已经将 Python 安装目录加入到我的环境变量，因此，不论我是在 cmd 还是 PowerShell 中，我都能通过输入 `pytool`
命令快速激活此虚拟环境，以安装其它 Python 工具模块或使用工具模块。

## 项目结构

项目中应包含完整的项目代码以及有用的信息文档。项目的一般结构如下：

```plaintext
/project-name         # 项目根目录
|-- /venv             # 虚拟环境目录（不加入版本控制）
|-- /project_name     # 项目源码目录
    |-- __init__.py
    |-- module1.py
    |-- module2.py
|-- /tests            # 测试代码
    |-- test_module1.py
    |-- test_module2.py
|-- README.md         # 项目说明文件
|-- requirements.txt  # 项目依赖文件（如果打算使用 pip 安装依赖）
|-- setup.py          # 安装、打包、分发配置文件（如果打算发布项目）
|-- .gitignore        # git忽略文件（忽略非源码文件，如临时文件）
|-- pyproject.toml    # 如果项目使用 Poetry 管理，会有这个文件
```

## Python 发布包（依赖）

Python 发布包不同于项目结构中的模块路径包。在 Python 社区中，发行版通常也称为“包”，但它其实指的是“依赖”。

有关安装 Python 发布包的更多描述请参考：https://packaging.python.org/en/latest/tutorials/installing-packages/

## 包管理工具：pip

pip 的基本使用如下：

### 安装依赖

#### 从 PyPI 安装

使用 `pip install` 命令可以从 PyPI 安装软件包。

```bash
pip install <project_name>[constraints-version]
```

> 通常习惯于使用尖括号 <> 表示一个内容必选，而方括号 [] 则表示内容可选。

#### 批量安装

pip 配合 `requirements.txt` 文件使用，可以批量安装依赖。

```bash
pip install -r requirements.txt
```

#### 从路径源码安装

使用此方式安装，一般希望在开发时同时修改源码，因此可以使用编辑模式安装（加 `-e` 参数）。

如果使用常规安装（没有使用 `-e` 参数），则会将文件复制到虚拟环境目录中，你对引用项目的源码的修改需要重新执行安装，变更才能生效。

```shell
pip install [-e] <path>
```

#### 从本地档案文件安装

如果你从网上下载了别人的模块，这些模块并没有发布在 PyPI 上，你可以执行档案文件安装，只需要指定档案路径即可：

```shell
pip install <archive-path>
```

例如：

```shell
pip install .\archives\test_poetry-0.1.0.tar.gz
```

### 查找包

使用 `pip search` 来搜寻在 PyPI 上的包。

```bash
pip search search_query
```

### 升级包

将依赖升级到最新版。

```bash
pip install --upgrade package_name
```

### 卸载包

你可以使用 pip 来卸载不再需要的包。

```bash
pip uninstall package_name
```

### 冻结依赖

通过 `pip freeze` 命令可以生成当前环境的依赖列表，以保证环境一致性。

```bash
pip freeze > requirements.txt
```

### 列出包

`pip list` 会显示已经安装的包及其版本。

```bash
pip list
```

### 查看包信息

`pip show` 提供了已安装包的信息。

```bash
pip show package_name
```

### 检查包

`pip check` 可以检查已安装的包之间的依赖关系冲突。

```bash
pip check
```

## 项目管理工具：Python-Poetry

Python-Poetry（简称 Poetry）是一个现代的 Python 依赖管理和打包工具，它旨在简化依赖的构建和管理过程。

Poetry 基于项目格式，使用一个简单的 `pyproject.toml` 文件，取代了 `setup.py`，`requirements.txt`，`setup.cfg`，`MANIFEST.in` 和 `Pipfile` 文件。

GitHub 仓库：https://github.com/python-poetry/poetry

### 安装 Poetry

Poetry 工具本身应被安装在全局环境中，而非虚拟环境。

安装教程：https://python-poetry.org/docs/#installation

#### 通过脚本安装

首先下载安装脚本：https://install.python-poetry.org/

> 将会得到 install-poetry.py 文件。

在安装脚本（install-poetry.py）的目录下打开终端（CMD），使用 `python` 命令执行安装脚本，如果需要自定义安装路径，可以通过设置环境变量 `POETRY_HOME` 来指定：

```cmd
set POETRY_HOME=D:\Python\Scripts&& python install-poetry.py
```

你可以替换 `POETRY_HOME` 的值，但注意两端不要有空格，`set POETRY_HOME=D:\Python\Scripts && python install-poetry.py` 与上面的示例是不一样的，它在 `Scripts` 与 `&&` 之间多了空格。
> 如前面提到的，如果 `python` 命令无效，你可以尝试使用 `py`。

安装完成之后，你需要把 Poetry 目录下的 bin 目录加入到你的环境变量中。

#### 检验安装状态

新打开一个 CMD 窗口，输入 `poetry` 如果输出 Poetry 版本以及其它提示信息，说明安装成功。

### Poetry 配置

Poetry 支持很多配置自定义，你可以根据你的习惯爱好更改这些配置，或者更改一些你有强迫症的配置。

#### 查看配置

```shell
poetry config --list
```

#### 配置方式

##### 命令配置

Poetry 可以通过 `config` 命令进行配置，会自动生成 `config.toml` 文件，文件位置：

- macOS: ~/Library/Application Support/pypoetry
- Windows: %APPDATA%\pypoetry

##### 局部配置

Poetry 支持为项目指定配置，通过给 `config` 命令指定 `--local` 参数，将在项目目录下生成 `poetry.toml` 文件，作为项目配置。

```cmd
poetry config virtualenvs.create false --local
```

##### 环境变量配置

Poetry 的所有配置都可以通过环境变量设置，环境变量名必须以 `POETRY_` 开头作为前缀。例如：

```bash
export POETRY_VIRTUALENVS_PATH=/path/to/virtualenvs/directory
```

##### 配置优先级

环境变量配置 > 局部配置 > 命令配置 （只做了粗略验证）

#### 配置变量

##### cache-dir

环境变量值：`POETRY_CACHE_DIR`

描述：Poetry 的缓存目录。

##### virtualenvs.create

环境变量值：`POETRY_VIRTUALENVS_CREATE`

描述：如果设置 `false`，Poetry 将不会创建一个新的虚拟环境。

##### virtualenvs.in-project

环境变量值：`POETRY_VIRTUALENVS_IN_PROJECT`

描述：如果设置 `true`，虚拟环境（目录名称：`.venv`）会被创建在项目的根目录下。

### 使用 Poetry

作为第三方项目管理工具，它通常面临两种情况下的使用：

- 完全由 Poetry 管理：项目一开始就由 Poetry 管理。
- 转换为 Poetry 管理：项目一开始使用其他方式管理，随后加入 Poetry 管理。

需要注意的是，使用 Poetry 管理的项目应该始终通过 Poetry 命令行接口来运行项目和管理依赖（添加、删除等），这样可以保证 Poetry 能够准确地管理项目。

#### 完全由 Poetry 管理

你应该参考官方文档：https://python-poetry.org/docs/

#### 转换为 Poetry 管理

要将一个项目转换为使用 Poetry 进行依赖管理，可以遵循以下步骤：

##### 1. 初始化 Poetry 项目

在项目的根目录中，运行以下命令来初始化 Poetry：

```shell
poetry init
```

`poetry init` 命令将引导你创建一个新的 `pyproject.toml` 文件。在这个过程中，它会询问你关于项目的基本信息，并提供添加依赖的选项。

如果你的项目中已经有 `requirements.txt` 文件，你可以跳过手动添加依赖的部分。如果没有，可以使用一些 Python 工具模块生成这个文件。

##### 2. 项目依赖管理

你应该将项目依赖交由 Poetry 管理，依赖的安装和删除都应该通过 Poetry 操作。

###### 安装依赖

要指定一个依赖（安装依赖），可以使用 `add` 命令：

```shell
poetry add <package-name>
```

它会自动找到合适的版本并安装依赖及其子依赖项。

可以结合 PowerShell 循环遍历 `requirements.txt` 文件内容，将依赖依次添加到 Poetry 中：

```PowerShell
foreach ($dependency in Get-Content -Path "requirements.txt") { `
    if ($dependency.Trim() -ne "") { `
        poetry add $dependency.Trim() `
    } `
}
```

> PowerShell 通过使用反引号（`）可以将每一行指令连接到下一行，从而形成一个多行指令。

###### 移除依赖

要从项目中移除一个依赖，可以使用 `remove` 命令：

```shell
poetry remove <package-name>
```

##### 3. 检查虚拟环境

在运行项目之前，你应该检查项目当前虚拟环境信息，使用以下命令检查：

```shell
poetry env info
```

##### 4. 运行项目

确认当前虚拟环境后，使用以下命令激活虚拟环境以运行和开发项目：

```shell
poetry shell
```

这会创建一个新的 shell 窗口，要撤销激活且退出新 shell 窗口，使用 `exit` 命令，`deactivate` 命令仅撤销激活，但不会退出新 shell 窗口。

##### 5. 版本控制

如果你的项目在版本控制中（如 git）你应将 `pyproject.toml` 和 `poetry.lock` 文件提交到版本控制系统中。

##### 6. 构建项目

构建命令：

```bash
poetry build
```

这会生成 dist 文件夹并生成用于发布的 `.whl` 和 `.tar.gz` 文件。

使用 Poetry 构建项目应遵循它的项目结构，否则会构建失败。

> 如果项目名称使用连字符 `-` 连接单词，项目源码目录需要转为下划线 `_` 连接（包名不应该使用连字符等特殊符号）。

### 题外话

#### 一些主观偏好

##### 创建虚拟环境

对于创建虚拟环境，如果你不想用 Poetry 提供的策略，你可以使用 Python 提供的工具模块（venv）在项目根目录下创建虚拟环境（.venv），因为 Poetry 同样优先使用此目录。

#### 什么时候 Poetry 会创建虚拟环境？

当 Poetry 需要使用到虚拟环境时，它会根据当前环境和参数配置（`virtualenvs.in-project`、`cache-dir` 等）决定是否以及在哪创建虚拟环境。

## 将 Python 项目打包成可执行文件

现代 Python 项目越来越倾向于作为模块或包进行管理和分发，而不是传统的可执行文件。

当然，这不意味着将 Python 项目打包成单个可执行文件没有其场景和优势。例如，对于需要简化部署、易于分发的桌面应用或在特定环境（如某些限制访问的服务器）中执行的脚本， 打包为可执行文件依然有其价值。然而，对于库、模块，或者依赖强大生态系统的应用，直接作为模块运行和分发更加符合 Python 的设计哲学和实践。

# 工具模块

如前面提到的，你可以为工具模块创建一个虚拟环境，专门用于存放这些 Python 工具模块，作为全局使用。

## pipreqs

用于为导入的项目生成 `requirements.txt` 文件。

GitHub：https://github.com/bndr/pipreqs

### 使用方式

1. 在项目目录下打开 shell 窗口（CMD 或 PowerShell）。
2. 激活工具模块虚拟环境。
3. 使用 pipreqs 扫描项目生成 `requirements.txt` 文件。

语法：

```shell
pipreqs [options] [<path>]
```

默认路径为当前 shell 工作目录，所以你可以省略，但 pipreqs 默认扫描所有 Python 模块，如果你的项目根路径下存在虚拟环境（如 .venv），你需要将它排除：

```shell
pipreqs --ignore .venv
```

如果你的项目根目录下只有项目源码目录（标准的项目结构也是这样的），你可以直接指定扫描项目源码目录（这就不需要排除虚拟环境目录），然后会在源码目录下生成 `requirements.txt` 文件，把它复制到项目根目录即可：

```shell
pipreqs ./project_name
```
