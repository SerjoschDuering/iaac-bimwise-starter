# Course Introduction: The Startup Simulation

## Welcome -- What This Week Is About

This is a one-week intensive course at IAAC Barcelona. Around 29 students will spend four working days building a real software product together, followed by final presentations on Friday.

### The Basics at a Glance

| Detail | Info |
|--------|------|
| Location | IAAC, Barcelona |
| Duration | 5 days (4 building days + 1 presentation day) |
| Students | ~29 total |
| Daily schedule | ~6 hours, split into 2 blocks of ~3 hours each |
| Theme | Using AI to build software for the architecture industry |

### What Makes This Different

This is not a lecture series. There are no exams. There is no homework you hand in and forget about. Instead, you will build a working product as a team -- a real piece of software that solves a real problem in the architecture industry. By Friday, it needs to work well enough to present to a panel of reviewers.

Each day is split into two sprint blocks of roughly three hours each. Teams build, test, and iterate. At key moments during the week, "board meetings" happen -- the client shows up with new demands that push the company to the next level. These are not scheduled every day; they appear when the stakes need to rise.


---

## The Startup Simulation

### You Are a Company

From the moment the week begins, the class operates as a startup company. On Day 1, students pick a company name. This is not just a fun gimmick -- the entire course is structured around this idea. You have roles, responsibilities, deadlines, and a demanding client.

### The Contract

Your startup has just landed its first contract. A Spanish real estate developer wants an automated platform that checks digital building models against construction regulations. They want to upload a building file, press a button, and get back a clear report showing what passes and what fails. Your job is to build that platform in four days.

### Company Roles

Everyone in the class has a defined role, just like in a real company.

| Role | Who fills it | What they do |
|------|-------------|--------------|
| CEO / Board | The instructors | Set deadlines, drop new requirements mid-week, play the role of an impatient client |
| Captains | 1-2 per team, elected by the team | Own their team's delivery, coordinate with other captains, make technical decisions |
| Engineers | Everyone else | Build features within their assigned team |

**Captains** are elected within each team on Day 1. They act like tech leads at a real company: they do not do all the work themselves, but they unblock their teammates, ensure everyone has tools set up, and coordinate across teams on shared standards and platform decisions.

### Board Meetings

At key points during the week, the "board" (the instructors playing the client) watches a demo of what teams have built. Sometimes they are impressed. Sometimes they say, "Great work, but the client also wants this new feature by tomorrow." These board meetings drive the course forward organically. New requirements appear -- shared standards, deployment, a unified product -- and the company has to adapt, just like a real startup.


---

## No Prior Coding Required (But You Will Learn)

### The Honest Truth

You do not need to know how to code before this week starts. Not a single line. The course is designed around AI coding assistants -- tools that can write code when you describe what you want in plain English.

However, you **will** learn to:

- Read Python code and understand what it does
- Debug problems when something does not work as expected
- Describe what you want clearly enough that an AI assistant can build it
- Test your code against known correct answers

These are practical skills that professionals use every day in 2025. You are learning to work the way the industry actually works now.

### The Support Structure

You are not alone in this process:

- **Your Captain** is your first point of contact when you are stuck
- **Your AI coding assistant** can write code from plain English descriptions
- **The prototype** gives you working examples to learn from
- **The IFC-Bench dataset** lets you verify your code produces correct answers

### AI Coding Tools You Can Use

Students are free to use any AI coding assistant they prefer. Common options include:

- **Claude Code** -- Anthropic's command-line coding assistant
- **Cursor** -- an AI-powered code editor
- **Windsurf** -- another AI-powered code editor
- **GitHub Copilot** -- AI code suggestions inside popular editors
- **Codex** -- OpenAI's coding assistant

The AI writes code fast, but you still need to understand what it wrote, test it, and verify it does the right thing. The AI is a tool, not a replacement for your thinking.


---

## What Is IFC?

### The Simple Explanation

IFC stands for **Industry Foundation Classes**. You can forget the full name immediately. What matters is what it does.

An IFC file is a **digital description of an entire building**. Not a pretty picture. Not a rendering. It is a structured, computer-readable file that contains every detail about a building's elements:

- Every wall, with its thickness and material
- Every door, with its width and height
- Every room, with its area and name
- Every window, with its position and dimensions
- Every floor, every staircase, every column

Think of it this way: if a blueprint is a photograph of a building, an IFC file is more like the building's DNA -- every measurement and relationship encoded in a format that software can read and analyze.

### Why IFC Matters

IFC is an **open standard**. That means no single company owns it. It works across all major architecture software:

| Software | Can export to IFC? |
|----------|-------------------|
| Autodesk Revit | Yes |
| ArchiCAD | Yes |
| Tekla Structures | Yes |
| Many others | Yes |

When you export a building model from any of these programs to IFC, all the building data comes with it. This makes IFC the common language that different software tools can share.


---

## What Is Compliance Checking?

### The Problem

Before any building gets constructed, inspectors review the design to make sure it follows the rules. These rules cover things like minimum room sizes, door widths for accessibility, wall thicknesses for safety, and much more.

Traditionally, a human inspector checks these things by hand -- measuring dimensions on drawings, cross-referencing against regulation books, writing reports. This is slow, tedious, and easy to get wrong.

### The Solution

Automated compliance checking means a computer reads the IFC file and checks the rules automatically. Instead of a person measuring every door width by hand, software scans the entire building in seconds and produces a clear report.

### Examples of Automated Checks

The starter kit includes sample regulations -- both basic numeric rules (like minimum door width, room area, wall thickness) and more advanced ones that require reasoning. You will write the check functions yourself, starting on Day 1. Here are examples of the kinds of checks you will build:

| Check | Rule | What it looks for |
|-------|------|-------------------|
| Minimum room area | Every room must be at least 9 m² | Flags any room smaller than 9 square meters |
| Minimum door width | Every door must be at least 800 mm wide | Flags any door narrower than 800 millimeters (accessibility requirement) |
| Window per room | Every room must have at least one window | Flags any room that has no window at all |

These are simple examples, but the same approach scales to much more complex regulations.


---

## The Prototype: Your Day 1 Starting Point

### What You Get on Day 1

You will not start from an empty screen. There is already a working application waiting for you. This is your prototype -- the foundation you will build on all week.

### What the Starter Kit Includes

- **Built with Python + Gradio** -- Python is the programming language; Gradio is a tool that makes it easy to create simple web interfaces without much code
- **A skeleton checker** -- the app framework is ready, you write the check functions that plug into it
- **A 3D viewer** -- you can see the building model right in the browser; elements that fail a check turn red, elements that pass turn gray
- **Upload and check** -- you upload an IFC file, click "Run Checks," and see results instantly
- **Exercise notebooks** -- Jupyter notebooks that walk you through IFC basics, calling LLMs, getting structured output, and building agents

### Your First Exercise

On Day 1, your first task is straightforward:

1. Explore the IFC file in a notebook -- understand what's inside
2. Read the sample regulations
3. Write your first check function and wire it into the app

If you can describe a rule in a sentence -- like "every door must be at least 800mm wide" -- your AI assistant can help you turn that sentence into working code.


---

## How the Week Evolves

### The Day-by-Day Arc

| Day | Theme | What Happens |
|-----|-------|--------------|
| **Day 1** | "Make It Work" | Learn IFC basics, write your first compliance checks, see results in the app |
| **Day 2** | "Make It Talk" | Add AI-powered reasoning to checks, agree on shared standards across teams |
| **Day 3** | "Make It Connect" | Deploy agents to the cloud, add RAG so agents can look up regulations, platform architecture emerges |
| **Day 4** | "Make It Real" | Integration sprint -- frontend, orchestrator, and team agents all connect. Rehearse the pitch. |
| **Day 5** | Presentations | Final demos to "investors" / jury panel |

### The Pivot

Early on, every team does the same kind of work -- writing compliance checks, learning the tools, building confidence. Then the board drops new requirements and things get real. The client wants a unified product. Teams have to specialize and coordinate:

- Some people focus on the **frontend** (what users see on screen)
- Some people deepen the **compliance checks** and add AI reasoning
- Some people work on **deployment and infrastructure**
- Captains coordinate the **platform architecture** that ties everything together

This mirrors exactly how real startups work. Early on, everyone is a generalist. As the product matures and requirements grow, people specialize.


---

## The Shared Result Schema: The Contract Between Teams

### Why It Exists

When five different teams are all writing compliance checks, there is one critical question: how do all those checks produce results that the rest of the system can understand?

The answer is the **shared result schema** -- a fixed format that every single check must follow when reporting its results. Think of it as a contract between teams. No matter who wrote the check, no matter how simple or complex it is, the output always looks the same.

### The Format

Every check result contains these fields:

| Field | What it is | Example |
|-------|-----------|---------|
| `element_id` | A unique identifier for the building element being checked | `"3x4F..."` |
| `element_type` | What kind of building element it is | `"IfcDoor"` |
| `element_name` | A human-readable name | `"Door #42"` |
| `rule` | Which check was run | `"Door Width"` |
| `requirement` | What the regulation demands | `">= 800 mm"` |
| `actual` | What was actually found in the model | `"700 mm"` |
| `passed` | Did the element pass the check? | `true`, `false`, or `null` (if data is missing) |

### Why This Matters

This schema is locked on Day 1, before any team starts building. That way:

- The **frontend team** knows exactly what data format to expect and can build the interface accordingly
- The **compliance checking teams** know exactly what their code needs to output
- **New checks** written on Day 4 work with the same interface that was built on Day 2
- **Everything plugs together** without anyone having to rewrite or translate anything

If the schema is the glue that holds the platform together, respecting it is not optional. It is the most important engineering discipline the startup will practice.


---

## Agent Skills: The Company Handbook

### What It Is

Every real company has engineering standards -- documents that say things like "this is how we structure data," "this is how we build checks," and "this is the architecture we follow." At your startup, these standards live in a shared **Agent Skills** repository that your AI coding assistant can read.

Agent Skills is an open standard for giving AI coding assistants domain knowledge. It is a separate repository with a `SKILL.md` entry point and reference files that describe your company's conventions, schemas, and patterns.

### What It Contains

- The shared result schema (the output format every check must follow)
- Architecture conventions (how to structure your project, how to name things)
- Agent patterns (how to build PydanticAI agents with tools and chains)

### The Special Power of Agent Skills

Here is what makes this different from a normal handbook: **your AI coding assistant reads it automatically**.

When you install the skills repo into your AI assistant (VS Code, Cursor, Claude Code -- whatever you use), it picks up the company standards. When you ask it to write a new compliance check, it already knows the expected output format, the naming conventions, and the coding patterns everyone else is using. This means that even if 29 different people are writing code in 29 different corners of the room, the code all follows the same patterns.

### How It Stays Up to Date

1. After a board meeting, new standards get added to the skills repo
2. Everyone pulls the update
3. Every AI assistant immediately picks up the new rules
4. All new code automatically follows the updated standards

This solves one of the biggest problems in group projects: inconsistency. Without shared standards, five teams writing five different things in five different styles means someone has to spend hours stitching it all together at the end. With Agent Skills, consistency is baked into the process from the start.


---

## Why This Matters Beyond the Course

### The Industry Is Changing

The construction and architecture industry is going through a digital transformation. Building Information Modeling (BIM) -- the broader category that IFC files belong to -- is becoming mandatory in more and more countries. Automated compliance checking is actively being developed by companies and governments worldwide. This is not a futuristic concept. It is happening now.

### Skills You Will Build This Week

| Skill | Why it matters |
|-------|---------------|
| Working with IFC / digital building models | BIM is becoming the standard in architecture worldwide |
| Writing and understanding automated checks | Compliance automation is a growing field with real demand |
| Using AI coding assistants effectively | This is how professional software development works in 2025 |
| Reading and debugging code | Even non-programmers increasingly need to understand what code does |
| Collaborating in cross-functional teams | Every technology project involves people with different specializations working together |
| Working under startup-style pressure | Deadlines, pivots, and teamwork under constraint are universal professional skills |

### The Bigger Picture

You are not just building a course project. You are practicing the exact workflow that modern software teams use: define a problem, break it into pieces, assign teams, agree on standards, build in parallel, integrate, test, and ship. The fact that you are doing it with AI assistance and building models makes it directly relevant to where the architecture profession is heading.

The course is designed to be challenging but not overwhelming, practical but not shallow. By Friday, you will have built something real, learned skills you did not have on Monday, and experienced what it feels like to ship a product as a team. That experience -- the rhythm of building, the pressure of deadlines, the satisfaction of seeing your work come together -- is something no lecture can replicate.
