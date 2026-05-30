My Experience, Feelings and Understanding About CSC1002:Computational Laboratory  (AI-assisted) 


(Instructed by Professor Kinley Lam, AY2025-26 term2, School of Data Science, CUHKsz)

								
A.Course Syllabus


Phase I: Software Engineering & Best Practices (Weeks 1-4)

	Objective: Transitioning from "Working Code" to "Sustainable Code.

		Week 1: Introduction & Goal Setting
		
			Core Topics: TLC (Think Logically Code), Authentic Tasks, Professional IDE (VS Code).

			Original Keywords: Knowledge Transfer, Problem Decomposition, Python 3 environment.

		Week 2: Clean Code Principles

			Core Topics: The "Dead End" vs. "Sustainable" development.

			Original Keywords: WTFs/Minute, Complexity vs. Productivity, Technical Debt, Meaningful Names.

		Week 3: Software Design Principles

			Core Topics: Foundational rules for software architecture.

			Original Keywords: DRY (Don’t Repeat Yourself), KISS (Keep It Simple), YAGNI (You Ain't Gonna Need It).

		Week 4: Code Smells & Static Analysis

			Core Topics: Identifying weaknesses in code structure.

			Original Keywords: Magic Numbers, Deep Nesting, Long Parameter List, Refactoring potential.


Phase II: Logic Modeling & Professional Standards (Weeks 5-8)

	Objective: Modeling physical systems and establishing industrial coding habits.

		Week 5: Project Case Study I — Water Buckets
		
			Core Topics: Finite State Machine (FSM) implementation.
			
			Original Keywords: Scope, Spec, Design, Implementation, State Transitions, Atomic Operations.
			
		Week 6: Coding Style & Professional Discipline
		
			Core Topics: Adhering to international Python standards.
			
			Original Keywords: Python PEP 8, snake_case, Docstrings, Program Layout (Import/Global/Main).
			
		Week 7: Algorithmic Thinking — Number Flipping (Part I)
		
			Core Topics: Matrix manipulation and search patterns.
			
			Original Keywords: NxN Array, Nested Lists, Base Case, Recursion (DFS pattern).
			
		Week 8: Reusability by Refactoring
		
			Core Topics: Improving design without changing behavior.
			
			Original Keywords: "Call a Spade a Spade," Parameterization, Knowledge Transfer (Digits to Colors).
			

Phase III: Architectural Decoupling & UI (Weeks 9-11)
	
	Objective: Separating Logic from Display and moving to Event-Driven models.
	
		Week 9: Visualization Layer — Turtle Graphics
		
			Core Topics: Graphical mapping and rendering logic.
			
			Original Keywords: XY Drawing Window, Coordinate (0,0), tracer/update (Auto vs. Manual refresh).
			
		Week 10: Advanced Architecture — Decoupling Data Model
		
			Core Topics: Structural stability through MVC-like patterns.
			
			Original Keywords: Separate What Varies, Display Handler, UI Component vs. Engine/Flow.
			
		Week 11: Event-Driven Programming — Flipping Color GUI
		
			Core Topics: Asynchronous user interaction.
			
			Original Keywords: Non-blocking logic, Mainloop, Callback, Lambda functions for state.
			

Phase IV: Modern Tools & Quality Assurance (Week 12)--Writing prompt

	Objective: Leveraging AI and ensuring systemic reliability.
	
		Week 12a: AI-Assisted Programming & Prompt Engineering
		
			Core Topics: LLM as a "Programming Copilot."
			
			Original Keywords: Prompt (CoT, Few-Shot, Role), Context Refinement, Human as "Auditor."
			
		Week 12b: Verification & Robustness — Number Guessing
		
			Core Topics: Unit testing and advanced Python built-ins.
			
			Original Keywords: FIRST Principles (Fast, Independent, etc.), Test Smells, zip(), Typing Hints, random.sample.




B.My Understanding of CSC1002: From Scripting to Software Craftsmanship


I. The Foundational Paradigm: The Sustainability Mandate

	The curriculum of CSC1002 is anchored in a singular, non-negotiable premise: "Working code is not enough." 
	
	This philosophy, established in the "Goals" and "Clean Code" modules,
	
	addresses the Sustainability Crisis in software development.
	

	1.1 The Complexity vs. Productivity Paradox
	
	The course identifies two divergent paths in development:
		
		1.The "Quick and Dirty" Path: Characterized by high initial velocity but a rapid decline in productivity.
			
		As technical debt accumulates,
			
		the code reaches a "Dead End"—a state where the cost of change exceeds the value of the software.

				
		2.The "Thoughtful and Clean" Path: Requires a higher initial investment in design and best practices, 
			
		ensuring a Sustainable lifecycle where complexity is managed and productivity remains constant.
		
				
	1.2 The Objective Measurement of Quality: WTFs/Minute (A really vivid judging level).
		
	Departing from subjective critiques, CSC1002 utilizes the "WTFs/Minute" metric.
		
	Quality is defined by the ease with which a peer reviewer can interpret the code’s intent. 
		
	Code is treated as a "letter written to a human" that a machine happens to execute.
		


II. The Engineering Quality Firewall: Clean Code & Standards

	Weeks 2 through 4 establish the Standards Layer, focusing on the Refinement of Discipline.
	

	2.1 Professional Layout and PEP 8
		
	The course enforces strict adherence to Python PEP 8 and the snake_case naming convention. 
		
	This is not an aesthetic preference but a mechanism to lower the Cognitive Load.
		
		A standardized Program Layout is required:
		
			Imports (standard and third-party).
			
			Global Declarations.
			
			Functions (each documented with a Docstring).
			
			Main Body.
			
			
	2.2 The "Rule of Three": DRY, KISS, and YAGNI

	DRY (Don't Repeat Yourself): Every piece of knowledge must have a single, unambiguous representation.
			
	Redundancy is the primary source of synchronization bugs.

		KISS (Keep It Simple, Stupid): The course discourages over-engineering. Complexity is a liability, not an asset.
			
		YAGNI (You Ain't Gonna Need It): Developers must only implement current requirements, 
		
		avoiding speculative features that complicate the codebase.

			
			
	2.3 Identifying and Eliminating Code Smells
		
	Students are trained to detect "Code Smells"—surface-level indicators of deep-seated architectural issues:
		
		Magic Numbers: Hard-coded literals (e.g., 876) that lack semantic meaning.
			
		Deep Nesting: Excessive if and for blocks that increase cyclomatic complexity.
			
		Long Parameter Lists: Functions that take too many arguments, 
			
		indicating a violation of the Single Responsibility Principle (SRP).



III. Technical Logic Modeling: The "Water Buckets" Framework

	In Weeks 5 and 6, the "Water Buckets" project introduces Problem Decomposition and State Management.
	

	3.1 Finite State Machine (FSM) Design
		
	The game is modeled as a series of State Transitions. The "Board" is represented as a list of capacities and current levels.
		
		Atomic Operations: The logic is decomposed into fill(), empty(), and pour().
			
		Boundary Constraints: The technical crux is the "Pour" logic. 
			
		It requires calculating the exact amount of water to transfer without overflowing the destination or exceeding the source: 
			
		transfer = min(source_water, destination_capacity - destination_water) 
			
		This logic teaches students to program against Invariants and physical constraints.



IV. Advanced Algorithmic Structures: Grid Computation and Recursion

	Weeks 7 and 8 (Flipping Numbers) move from linear lists to 2D Arrays (Nested Lists).
	

	4.1 Matrix Representation and Coordinate Systems
		
	The "NxN" game board requires students to master Index-based Mapping. 
	
	Accessing board[row][col] requires a rigorous understanding of the coordinate relationship 
		
	between the visual display and the underlying Data Model.


	4.2 Recursive Search: The "Connected Neighbors" Algorithm
		
	The course introduces Recursion to solve the problem of cascading effects.
		
		The Spec: Two tiles are "connected" if their values are identical and they are adjacent (North, South, East, West).
			
		The Implementation: A recursive function flip_cell(r, c) calls itself for all four neighbors.
			
		The Safeguards: Students must implement Base Cases (to stop recursion) and Index Checks.
			
		This is a practical application of the Depth-First Search (DFS) pattern.



V. The Architectural Leap: Refactoring and Decoupling

	Weeks 8 and 10 represent the most significant transition: from Flat Scripts to Decoupled Architectures.
	

	5.1 Systematic Refactoring
		
	Refactoring is defined as the process of improving internal structure without altering external behavior.
		
	The course demonstrates this by evolving a "Digit-	Flipping" game into a "Color-Flipping" game.
		
		Generalization: Functions like create_game(dim, digit_range) are refactored into create_game(dim, game_data),
			
		allowing for Knowledge Transfer across different game types.

   
	5.2 The Decoupling Principle: Model vs. UI
		
	Week 10 introduces the Model-View-Controller (MVC) mindset.
		
		Separate What Varies: The UI (Console vs. GUI) varies, but the Game Logic (Flipping rules) is static.
		
		The Display Handler Abstraction: The refresh_screen() function is refactored to accept a Display Handler as an argument.
		
		Technical Implementation: By passing console_txt_handler or console_color_handler as a Callback, 
			
		the game engine becomes "UI-Agnostic." This achieves Structural Stability and high Reusability.
			


VI. Event-Driven Paradigms: Turtle Graphics and GUIs

	Weeks 9, 11, and 12 shift the execution model from sequential to Event-Driven.
	

	6.1 Graphical Mapping
	
	In the GUI mode, students must map logical grid indices to Cartesian (X,Y) Coordinates.
	
			Screen Management: Use of tracer(0) and update() is required to manage manual screen refreshing, preventing flickering during rendering.

			
	6.2 The Event Loop and Callbacks
	
	Instead of input() blocking the program, the system uses a Mainloop.
	
			Non-blocking Execution: The program "waits" for interrupts like onclick().
			
			Lambda Functions: To pass arguments into event handlers (like current board state), 
			
			students must utilize Anonymous (Lambda) Functions: onclick(lambda x, y: handle_click(x, y, game_state)).
			
			This is a critical lesson in Functional Programming within a GUI context.



VII. The Quality Firewall: Verification and Testing

	The curriculum treats Unit Testing as a mechanical necessity, not an option.


	7.1 FIRST Testing Principles
	Tests must be:
	
			Fast: To allow for constant execution.
			
			Independent: No side effects between test cases.
			
			Repeatable: Same results across different machines.
			
			Self-Validating: Binary Pass/Fail output.
			
			Timely: Ideally written during development.

			
	7.2 Test Smells
	
	Students are cautioned against Fragile Tests (which break on any minor code change)
	
	and Over-specified Tests (which test implementation details rather than outcomes). 
	
	The goal is to create a "Quality Firewall" that prevents regressions.



VIII. The Future Frontier: AI-Assisted Programming

	Week 12 introduces the "AI Copilot" paradigm.
	

	8.1 The Shift from Syntax to Auditing
	
	The course acknowledges that AI can generate syntax. Consequently,
	
	the learner's focus shifts toward Design, Coding Structure, and Software Quality.
	
			Prompt Engineering Strategies: Students learn to use Chain-of-Thought (CoT) (step-by-step logic),
			
			Few-Shot Prompting (providing examples), and Role Prompting to guide AI.

			
	8.2 The Human as Auditor
	
	A central theme is that AI produces "Smelly Code." The student must act as an Auditor, 
	
	reviewing AI-generated segments for Magic Numbers, Redundant Logic, and violations of Clean Code. 
	
	AI is used for Bootstrapping, but the human engineer is responsible for the Structural Integrity and Testing.



IX. Summary: The Professional Competency Framework

	Through 12 weeks of Authentic Tasks, CSC1002 builds a specific set of competencies:
	
			1.Decomposition Skills: Breaking a monolithic project into Thin Layers and discrete functions.
			
			2.Architectural Vision: Designing systems with Decoupled Interfaces for future extensibility.
			
			3.Defensive Programming: Using Assertions, Unit Tests, and Boundary Checks to ensure reliability.
			
			4.Refactoring Discipline: Constantly grooming the codebase to maintain Sustainability.





Assessment Arrangement 

	3projects(30% each), 1quiz(10%).


Room for Improvement

	The explanation can be more specific and more logical (it might be due to the time limitation). 
	
	The requirement for coding styles can be further clarified.
	
	The scoring criteria can be further specified.


Conclusion:

The trajectory of CSC1002 is a progression from Discipline (Clean Code) to Logic (State Machines) to Architecture(Decoupling) to Augmentation (AI). After learning this 	course, I have got to know the importance of coding style, and have begun to gradually appreciate the engineering mindset required for programming. Kinley often speaks 	to us with great passion regarding our approach to AI-assisted coding and our responsibilities as developers. From his insights, I have learned a great deal about the 		essential skills and integrity needed to thrive this era of rapid AI advancement. Finally, I would like to express my appreciation to professor Kinley Lam for his 			dedicated work.



HAVE FUN PROGRAMMING!!!







下面是较为正式、自然的中文翻译版本，保留了原文的学术风格与总结性质：

# 我对 CSC1002：计算实验室（AI辅助）课程的体验、感受与理解

**（任课教师：Kinley Lam，2025-26学年第二学期)**

## A. 课程大纲

### 第一阶段：软件工程与最佳实践（第1-4周）

**目标：从“能运行的代码”迈向“可持续发展的代码”**

#### 第1周：课程介绍与目标设定

**核心内容：**

* TLC（Think Logically, Code：逻辑思考后编程）
* 真实任务（Authentic Tasks）
* 专业开发环境（VS Code）

**关键词：**

* 知识迁移（Knowledge Transfer）
* 问题分解（Problem Decomposition）
* Python 3开发环境

#### 第2周：整洁代码原则（Clean Code）

**核心内容：**

* “死胡同式开发”与“可持续开发”

**关键词：**

* WTFs/Minute（每分钟让人困惑的次数）
* 复杂度与生产力
* 技术债务（Technical Debt）
* 有意义的命名（Meaningful Names）

#### 第3周：软件设计原则

**核心内容：**

* 软件架构的基础规则

**关键词：**

* DRY（Don't Repeat Yourself，不要重复自己）
* KISS（Keep It Simple, Stupid，保持简单）
* YAGNI（You Ain't Gonna Need It，你不会需要它）

#### 第4周：代码异味与静态分析

**核心内容：**

* 识别代码结构中的潜在问题

**关键词：**

* 魔法数字（Magic Numbers）
* 深层嵌套（Deep Nesting）
* 过长参数列表（Long Parameter List）
* 重构潜力（Refactoring Potential）

---

### 第二阶段：逻辑建模与专业规范（第5-8周）

**目标：建立物理系统模型并培养工业级编程习惯**

#### 第5周：项目案例研究Ⅰ——水桶问题（Water Buckets）

**核心内容：**

* 有限状态机（Finite State Machine, FSM）的实现

**关键词：**

* 范围（Scope）
* 规格说明（Specification）
* 设计（Design）
* 实现（Implementation）
* 状态转移（State Transitions）
* 原子操作（Atomic Operations）

#### 第6周：编码规范与专业纪律

**核心内容：**

* 遵循国际Python编程标准

**关键词：**

* Python PEP8
* snake_case命名规范
* Docstring文档字符串
* 程序布局（Import / Global / Main）

#### 第7周：算法思维——数字翻转（第一部分）

**核心内容：**

* 矩阵操作与搜索模式

**关键词：**

* NxN数组
* 嵌套列表
* 基础情况（Base Case）
* 递归（DFS模式）

#### 第8周：通过重构实现复用

**核心内容：**

* 在不改变行为的前提下优化设计

**关键词：**

* “名副其实”（Call a Spade a Spade）
* 参数化（Parameterization）
* 知识迁移（从数字到颜色）

---

### 第三阶段：架构解耦与用户界面（第9-11周）

**目标：实现逻辑与显示分离，并进入事件驱动编程**

#### 第9周：可视化层——Turtle Graphics

**核心内容：**

* 图形映射与渲染逻辑

**关键词：**

* XY绘图窗口
* 坐标原点（0,0）
* tracer/update（自动刷新与手动刷新）

#### 第10周：高级架构——数据模型解耦

**核心内容：**

* 通过MVC思想实现结构稳定性

**关键词：**

* Separate What Varies（分离变化部分）
* Display Handler
* UI组件与引擎逻辑分离

#### 第11周：事件驱动编程——颜色翻转GUI

**核心内容：**

* 异步用户交互

**关键词：**

* 非阻塞逻辑
* Mainloop
* Callback
* Lambda表达式

---

### 第四阶段：现代工具与质量保障（第12周）

**目标：利用AI工具并确保系统可靠性**

#### 第12周（上）：AI辅助编程与提示词工程

**核心内容：**

* 大语言模型作为“编程副驾驶”

**关键词：**

* Prompt设计（CoT、Few-Shot、Role Prompting）
* 上下文优化
* 人类作为审计者（Auditor）

#### 第12周（下）：验证与鲁棒性——猜数字游戏

**核心内容：**

* 单元测试与高级Python工具

**关键词：**

* FIRST原则
* 测试异味（Test Smells）
* zip()
* 类型提示（Typing Hints）
* random.sample()

---

# B. 我对CSC1002的理解：从脚本编写到软件工程思维

## 一、基础理念：可持续性至上

CSC1002课程建立在一个明确且不可妥协的前提之上：

> “代码能够运行，并不意味着它已经足够优秀。”

这一理念贯穿于课程目标与Clean Code模块之中，直指软件开发中的“可持续性危机”。

### 1.1 复杂度与生产力悖论

课程指出软件开发存在两条截然不同的发展路径：

**1. 快速但混乱的开发路径**

前期开发速度极快，但随着技术债务不断积累，生产力迅速下降。

最终代码进入“死胡同（Dead End）”状态——修改成本超过软件本身价值。

**2. 深思熟虑的开发路径**

前期需要投入更多时间进行设计与规范建设。

然而长期来看，复杂度得到有效控制，生产力能够保持稳定，实现软件生命周期的可持续发展。

### 1.2 代码质量的客观衡量标准：WTFs/Minute

课程提出了一个极具启发性的指标：

**WTFs/Minute（每分钟产生多少次“这是什么鬼？”的疑惑）**

代码质量不应由作者自我评价，而应由阅读者感受到的理解难度来衡量。

代码本质上是一封写给人类的信件，只是恰好由计算机执行而已。

---

## 二、工程质量防线：整洁代码与标准规范

第2至第4周构建了软件工程的规范层（Standards Layer）。

### 2.1 专业布局与PEP8

课程严格要求遵循Python PEP8标准与snake_case命名规范。

这并非审美要求，而是为了降低阅读代码时的认知负担（Cognitive Load）。

标准程序结构包括：

* Import导入部分
* 全局变量声明
* 函数定义（包含Docstring）
* 主程序入口

### 2.2 三大原则：DRY、KISS与YAGNI

**DRY（Don't Repeat Yourself）**

每一项知识只能有唯一且明确的表示方式。

重复是同步错误的重要来源。

**KISS（Keep It Simple, Stupid）**

避免过度设计。

复杂性是负债，而非资产。

**YAGNI（You Ain't Gonna Need It）**

只实现当前需求。

避免为未来假设需求而提前增加复杂度。

### 2.3 识别并消除代码异味

课程训练学生识别以下典型问题：

* 魔法数字（Magic Numbers）
* 深层嵌套（Deep Nesting）
* 过长参数列表（Long Parameter Lists）

这些往往是更深层架构问题的表面征兆。

---

## 三、技术逻辑建模：Water Buckets框架

第5、6周通过Water Buckets项目引入状态管理与问题分解思想。

### 3.1 有限状态机（FSM）

整个游戏被建模为一系列状态转移。

游戏板由容量与当前水量组成的数据结构表示。

核心操作包括：

* fill()
* empty()
* pour()

其中最关键的是倒水逻辑：

[
transfer = \min(source_water,\ destination_capacity-destination_water)
]

这一设计让学生学会根据不变量（Invariant）和物理约束进行编程。

---

## 四、高级算法结构：网格计算与递归

第7、8周的Flipping Numbers项目引导学生从一维结构进入二维结构。

### 4.1 矩阵表示与坐标系统

NxN棋盘要求学生掌握：

* 二维数组
* 索引映射
* 数据模型与显示界面的对应关系

### 4.2 递归搜索：连通邻居算法

课程通过递归解决连锁翻转问题。

实现方式：

flip_cell(r,c)

会递归访问：

* 北（North）
* 南（South）
* 东（East）
* 西（West）

四个方向的相邻格子。

同时必须实现：

* Base Case
* 边界检查

这实际上是深度优先搜索（DFS）的经典应用。

---

## 五、架构飞跃：重构与解耦

第8周与第10周是课程最重要的转折点之一。

### 5.1 系统化重构

重构被定义为：

> 在不改变外部行为的前提下改善内部结构。

课程通过将数字翻转游戏扩展为颜色翻转游戏展示这一思想。

### 5.2 解耦原则：Model 与 UI

课程引入MVC思想。

核心原则：

**Separate What Varies（分离变化部分）**

UI可能变化，但游戏规则保持不变。

通过Display Handler回调机制：

* console_txt_handler
* console_color_handler

游戏引擎无需知道具体显示方式。

从而实现：

* 高复用性
* 高扩展性
* 结构稳定性

---

## 六、事件驱动范式：Turtle Graphics 与 GUI

### 6.1 图形映射

GUI模式下需要完成：

* 逻辑坐标到屏幕坐标映射
* 手动刷新控制

通过：

* tracer(0)
* update()

避免界面闪烁。

### 6.2 事件循环与回调机制

程序不再依赖阻塞式input()。

而是通过Mainloop等待事件发生。

例如：

onclick(lambda x, y: handle_click(x, y, game_state))

这一部分让学生接触函数式编程思想与GUI开发模式。

---

## 七、质量防火墙：验证与测试

课程强调：

> 单元测试不是可选项，而是工程实践中的必需品。

### 7.1 FIRST测试原则

测试必须满足：

* Fast（快速）
* Independent（独立）
* Repeatable（可重复）
* Self-validating（自验证）
* Timely（及时）

### 7.2 Test Smells

课程提醒学生避免：

* 脆弱测试（Fragile Tests）
* 过度具体化测试（Over-specified Tests）

测试应关注结果，而非实现细节。

其目标是建立能够防止回归错误的“质量防火墙”。

---

## 八、未来前沿：AI辅助编程

### 8.1 从编写代码到审查代码

课程承认AI已经能够生成大量代码。

因此学习重点转向：

* 软件设计
* 架构思维
* 代码质量控制

学生学习：

* Chain-of-Thought（思维链）
* Few-Shot Prompting
* Role Prompting

等提示工程技术。

### 8.2 人类作为审计者

课程的重要观点是：

> AI会生成能够运行但存在问题的代码。

因此开发者必须承担审计职责：

* 检查魔法数字
* 检查重复逻辑
* 检查代码异味
* 完成测试验证

AI负责加速开发，

而人类负责保证系统的结构完整性与可靠性。

---

## 九、总结：专业能力培养框架

通过12周的真实项目实践，CSC1002培养了以下核心能力：

1. **问题分解能力（Decomposition Skills）**
   将复杂项目拆分为多个独立模块。

2. **架构设计能力（Architectural Vision）**
   设计具有良好扩展性的解耦系统。

3. **防御式编程能力（Defensive Programming）**
   使用断言、测试和边界检查保障可靠性。

4. **重构能力（Refactoring Discipline）**
   持续维护代码质量与可持续性。

---

## 考核方式

* 项目（Project）×3：每项30%
* Quiz ×1：10%

---

## 课程改进建议

1. 某些概念的讲解可以更加具体且逻辑更加清晰（这可能与课堂时间限制有关）。

2. 编码规范要求可以进一步明确和细化。

3. 评分标准可以更加透明和具体。

---

# 结语

CSC1002的整体学习路径可以概括为：

**纪律（Clean Code）→ 逻辑（State Machines）→ 架构（Decoupling）→ 增强（AI）**

通过这门课程，我逐渐认识到编码规范的重要性，并开始理解软件开发背后所需要的工程化思维。

Kinley教授经常充满热情地与我们讨论AI辅助编程时代开发者应承担的责任与使命。从他的分享中，我学习到了在这个AI高速发展的时代中，程序员应具备的核心能力、职业素养以及工程师精神。

最后，我衷心感谢Kinley Lam教授在本课程中的辛勤付出与热情！



