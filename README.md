My Experience, Feelings and Understanding About CSC1002:Computational Laboratory  (AI-assisted) 
                (Instructed by Professor Kinley Lam, AY2025-26 term2)

								
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




==========================================================================================================================================================================
B.My Understanding of CSC1002: From Scripting to Software Craftsmanship


I. The Foundational Paradigm: The Sustainability Mandate

The curriculum of CSC1002 is anchored in a singular, non-negotiable premise: "Working code is not enough." This philosophy, established in the "Goals" and "Clean Code" modules, addresses the Sustainability Crisis in software development.

1.1 The Complexity vs. Productivity Paradox
The course identifies two divergent paths in development:
				1.The "Quick and Dirty" Path: Characterized by high initial velocity but a rapid decline in productivity. As technical debt accumulates, the code reaches a "Dead 	End"—a state where the cost of change exceeds the value of the software.
				2.The "Thoughtful and Clean" Path: Requires a higher initial investment in design and best practices, ensuring a Sustainable lifecycle where complexity is managed and productivity remains constant.
				
1.2 The Objective Measurement of Quality: WTFs/Minute (A really vivid judging level).
Departing from subjective critiques, CSC1002 utilizes the "WTFs/Minute" metric. Quality is defined by the ease with which a peer reviewer can interpret the code’s intent. Code is treated as a "letter written to a human" that a machine happens to execute.



II. The Engineering Quality Firewall: Clean Code & Standards

Weeks 2 through 4 establish the Standards Layer, focusing on the Refinement of Discipline.

2.1 Professional Layout and PEP 8
The course enforces strict adherence to Python PEP 8 and the snake_case naming convention. This is not an aesthetic preference but a mechanism to lower the Cognitive Load.

A standardized Program Layout is required:
			Imports (standard and third-party).
			Global Declarations.
			Functions (each documented with a Docstring).
			Main Body.
			
2.2 The "Rule of Three": DRY, KISS, and YAGNI
			DRY (Don't Repeat Yourself): Every piece of knowledge must have a single, unambiguous representation. Redundancy is the primary source of synchronization bugs.
			KISS (Keep It Simple, Stupid): The course discourages over-engineering. Complexity is a liability, not an asset.
			YAGNI (You Ain't Gonna Need It): Developers must only implement current requirements, avoiding speculative features that complicate the codebase.
			
2.3 Identifying and Eliminating Code Smells
Students are trained to detect "Code Smells"—surface-level indicators of deep-seated architectural issues:
			Magic Numbers: Hard-coded literals (e.g., 876) that lack semantic meaning.
			Deep Nesting: Excessive if and for blocks that increase cyclomatic complexity.
			Long Parameter Lists: Functions that take too many arguments, indicating a violation of the Single Responsibility Principle (SRP).



III. Technical Logic Modeling: The "Water Buckets" Framework

In Weeks 5 and 6, the "Water Buckets" project introduces Problem Decomposition and State Management.

3.1 Finite State Machine (FSM) Design
The game is modeled as a series of State Transitions. The "Board" is represented as a list of capacities and current levels.
			Atomic Operations: The logic is decomposed into fill(), empty(), and pour().
			Boundary Constraints: The technical crux is the "Pour" logic. It requires calculating the exact amount of water to transfer without overflowing the destination or 	exceeding the source: transfer = min(source_water, destination_capacity - destination_water) This logic teaches students to program against Invariants and physical constraints.



IV. Advanced Algorithmic Structures: Grid Computation and Recursion

Weeks 7 and 8 (Flipping Numbers) move from linear lists to 2D Arrays (Nested Lists).

4.1 Matrix Representation and Coordinate Systems
The "NxN" game board requires students to master Index-based Mapping. Accessing board[row][col] requires a rigorous understanding of the coordinate relationship between the visual display and the underlying Data Model.

4.2 Recursive Search: The "Connected Neighbors" Algorithm
The course introduces Recursion to solve the problem of cascading effects.
			The Spec: Two tiles are "connected" if their values are identical and they are adjacent (North, South, East, West).
			The Implementation: A recursive function flip_cell(r, c) calls itself for all four neighbors.
			The Safeguards: Students must implement Base Cases (to stop recursion) and Index Checks (to prevent IndexErrorat the grid boundaries). This is a practical application of the Depth-First Search (DFS) pattern.



V. The Architectural Leap: Refactoring and Decoupling

Weeks 8 and 10 represent the most significant transition: from Flat Scripts to Decoupled Architectures.

5.1 Systematic Refactoring
Refactoring is defined as the process of improving internal structure without altering external behavior. The course demonstrates this by evolving a "Digit-Flipping" game into a "Color-Flipping" game.
			Generalization: Functions like create_game(dim, digit_range) are refactored into create_game(dim, game_data), allowing for Knowledge Transfer across different game types.
   
5.2 The Decoupling Principle: Model vs. UI
Week 10 introduces the Model-View-Controller (MVC) mindset.
			Separate What Varies: The UI (Console vs. GUI) varies, but the Game Logic (Flipping rules) is static.
			The Display Handler Abstraction: The refresh_screen() function is refactored to accept a Display Handler as an argument.
			Technical Implementation: By passing console_txt_handler or console_color_handler as a Callback, the game engine becomes "UI-Agnostic." This achieves Structural Stability and high Reusability.



VI. Event-Driven Paradigms: Turtle Graphics and GUIs

Weeks 9, 11, and 12 shift the execution model from sequential to Event-Driven.

6.1 Graphical Mapping
In the GUI mode, students must map logical grid indices to Cartesian (X,Y) Coordinates.
			Screen Management: Use of tracer(0) and update() is required to manage manual screen refreshing, preventing flickering during rendering.
			
6.2 The Event Loop and Callbacks
Instead of input() blocking the program, the system uses a Mainloop.
			Non-blocking Execution: The program "waits" for interrupts like onclick().
			Lambda Functions: To pass arguments into event handlers (like current board state), students must utilize Anonymous (Lambda) Functions: onclick(lambda x, y: 			handle_click(x, y, game_state)). This is a critical lesson in Functional Programming within a GUI context.



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
Students are cautioned against Fragile Tests (which break on any minor code change) and Over-specified Tests (which test implementation details rather than outcomes). The goal is to create a "Quality Firewall" that prevents regressions.



VIII. The Future Frontier: AI-Assisted Programming

Week 12 introduces the "AI Copilot" paradigm.

8.1 The Shift from Syntax to Auditing
The course acknowledges that AI can generate syntax. Consequently, the learner's focus shifts toward Design, Coding Structure, and Software Quality.
			Prompt Engineering Strategies: Students learn to use Chain-of-Thought (CoT) (step-by-step logic), Few-Shot Prompting (providing examples), and Role Prompting to guide AI.
8.2 The Human as Auditor
A central theme is that AI produces "Smelly Code." The student must act as an Auditor, reviewing AI-generated segments for Magic Numbers, Redundant Logic, and violations of Clean Code. AI is used for Bootstrapping, but the human engineer is responsible for the Structural Integrity and Testing.



IX. Summary: The Professional Competency Framework

Through 12 weeks of Authentic Tasks, CSC1002 builds a specific set of competencies:
			1.Decomposition Skills: Breaking a monolithic project into Thin Layers and discrete functions.
			2.Architectural Vision: Designing systems with Decoupled Interfaces for future extensibility.
			3.Defensive Programming: Using Assertions, Unit Tests, and Boundary Checks to ensure reliability.
			4.Refactoring Discipline: Constantly grooming the codebase to maintain Sustainability.





=========================================================================================================================================================================
Assessment Arrangement 

3projects(30% each), 1quiz(10%).


==========================================================================================================================================================================
Room for Improvement

The explanation can be more specific and more logical (it might be due to the time limitation). 
The requirement for coding styles can be further clarified.
The scoring criteria can be further specified.


=========================================================================================================================================================================
Conclusion
The trajectory of CSC1002 is a progression from Discipline (Clean Code) to Logic (State Machines) to Architecture(Decoupling) to Augmentation (AI). After learning this course, I have got to know the importance of coding style, and have begun to gradually appreciate the engineering mindset required for programming. Kinley often speaks to us with great passion regarding our approach to AI-assisted coding and our responsibilities as developers. From his insights, I have learned a great deal about the essential skills and integrity needed to thrive this era of rapid AI advancement. Finally, I would like to express my appreciation to professor Kinley Lam for his dedicated work.



HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!
HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!
HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!
HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!
HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!
HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!
HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!HAVE FUN PROGRAMMING!!!

