# Week 4 Detailed Plan
## AI APIs + Real Coding Challenge

**Dates:** November 3-9, 2025  
**Goal:** Master AI APIs while learning to code WITHOUT copy-paste

---

## 🚨 CRITICAL CHANGE THIS WEEK

### The Problem
Week 3 projects were mostly copy-pasted from ChatGPT.  
Result: Projects done but learning = minimal.

### The Solution
**WEEK 4 = REAL CODING MODE**

**New Rules:**
1. ❌ NO copy-paste from ChatGPT/Claude
2. ✅ TYPE every single line yourself
3. ✅ Use AI to EXPLAIN concepts only
4. ✅ Perplexity for understanding, not code
5. ✅ Messy code = OK
6. ✅ Slow progress = OK
7. ✅ LEARNING > Speed

**Why this matters:**
- Week 4 test coming (no AI help)
- Interview prep needs real skills
- Jan 2026 goal needs actual coding ability

---

## WEEK 4 OVERVIEW

### Learning Focus
- OpenAI ChatGPT API integration
- Anthropic Claude API
- Prompt engineering fundamentals
- LLM response handling
- Building AI-powered applications
- **TYPING CODE MYSELF**

### Weekly Goals
- [ ] Understand LLM APIs deeply
- [ ] Build 3 AI tools (ALL TYPED)
- [ ] Can explain every line of code
- [ ] Comfortable with AI API patterns
- [ ] Ready for Week 4 test
- [ ] 7 consecutive days 🟩×7

---

## DAY 20 - MONDAY, NOV 3

### Morning (6-8 AM)
**OpenAI API Concepts**

**Learn (NO coding yet):**
- Read OpenAI docs: https://platform.openai.com/docs/quickstart
- Understand ChatCompletion API
- Message format (system, user, assistant)
- Parameters (temperature, max_tokens, model)
- Response structure

**Key concepts to understand:**
```
Messages = list of dicts
Each message has: role + content
Roles: system, user, assistant
Response = choices[0].message.content
```

**Don't copy code! Just UNDERSTAND the concepts.**

---

### Afternoon (2-4 PM)
**Build: Simple ChatGPT Caller**

**What to build:**
A simple script that:
1. Takes user question
2. Sends to OpenAI
3. Prints AI response

**Rules for building:**
- Open BLANK Python file ✅
- NO copy-paste ❌
- TYPE from understanding ✅
- If stuck, ask Perplexity: "Explain [concept]" ✅
- NOT: "Give me code" ❌

**Pseudocode (figure out syntax yourself!):**
```
1. Import requests
2. Load API key from .env
3. Get user question
4. Create messages list
5. Make API request
6. Extract response
7. Print it
```

**Expected struggles:**
- Syntax errors ✅ (learning!)
- JSON format confusion ✅ (debug it!)
- API errors ✅ (read error messages!)

**This is GOOD. This is learning.** 💪

---

### Evening (7-9 PM)
**Improve & Test**
- Add error handling (type it!)
- Try different questions
- Test edge cases
- Make it work reliably
- Git push

**Create:** `week4/day20-chatgpt-simple.py`

---

### Day 20 Goals
- [ ] Understand OpenAI API structure
- [ ] Built simple caller (TYPED!)
- [ ] Working end-to-end
- [ ] Can explain every line
- [ ] Git push

---

## DAY 21 - TUESDAY, NOV 4

### Morning (6-8 AM)
**Prompt Engineering Basics**

**Learn:**
- System prompts vs user prompts
- Clear instructions
- Few-shot examples
- Temperature effects
- Token limits

**Read:**
- OpenAI prompt engineering guide
- Anthropic prompt guide

**Practice (type yourself!):**
- Different system prompts
- Temperature variations
- See how responses change

---

### Afternoon (2-4 PM)
**Build: AI Assistant with Personality**

**What to build:**
Simple assistant with specific personality/role.

**Examples:**
- DevOps helper (answers infra questions)
- Python tutor (explains concepts)
- Code reviewer (reviews code snippets)

**Rules:**
- Start from scratch ✅
- Type everything ✅
- Use yesterday's code as REFERENCE only ✅
- Don't copy-paste ❌

**Add:**
- Custom system prompt
- Multiple user questions
- Conversation history (simple list)

---

### Evening (7-9 PM)
**Test & Polish**
- Try different personalities
- Test conversation flow
- Handle errors properly
- Git push

**Create:** `week4/day21-ai-assistant.py`

---

### Day 21 Goals
- [ ] Understand prompt engineering
- [ ] Built personality-based assistant
- [ ] Maintains conversation context
- [ ] All typed myself!

---

## DAY 22 - WEDNESDAY, NOV 5

### Morning (6-8 AM)
**Anthropic Claude API**

**Learn:**
- Claude vs ChatGPT differences
- Anthropic API format
- Message structure
- Best practices

**Read:**
- Anthropic docs: https://docs.anthropic.com/

**Note differences:**
- Different API endpoint
- Different message format
- Different parameters

---

### Afternoon (2-4 PM)
**Build: Dual AI Comparer**

**What to build:**
Send same question to both OpenAI and Claude.
Compare responses.

**Challenge:**
- Handle 2 different APIs ✅
- Type both integrations ✅
- No copy-paste ❌

**Structure (figure out yourself!):**
```
1. Get user question
2. Send to OpenAI → get response
3. Send to Claude → get response
4. Display both
5. Let user compare
```

---

### Evening (7-9 PM)
**Enhance**
- Add response timing
- Show token usage
- Handle errors for both
- Git push

**Create:** `week4/day22-ai-comparer.py`

---

### Day 22 Goals
- [ ] Understand Claude API
- [ ] Compare OpenAI vs Claude
- [ ] Both working (typed!)
- [ ] See real differences

---

## DAY 23 - THURSDAY, NOV 6

### Morning (6-8 AM)
**Streaming Responses**

**Learn:**
- Why streaming matters
- SSE (Server-Sent Events)
- Chunk handling
- Real-time display

**Understand:**
- stream=True parameter
- Iterating response chunks
- Displaying incrementally

---

### Afternoon (2-4 PM)
**Build: Streaming AI Chat**

**What to build:**
Chat that shows AI response word-by-word (like ChatGPT interface).

**Challenge:**
- Handle streaming ✅
- Print chunks as they arrive ✅
- Type the streaming logic yourself ✅

**This will be tricky!**
- But you'll learn deeply ✅

---

### Evening (7-9 PM)
**Polish streaming**
- Smooth display
- Handle errors
- Test reliability
- Git push

**Create:** `week4/day23-streaming-chat.py`

---

### Day 23 Goals
- [ ] Understand streaming
- [ ] Working real-time display
- [ ] Smooth UX
- [ ] Typed myself!

---

## DAY 24 - FRIDAY, NOV 7

### Morning (6-8 AM)
**Review Week 4 So Far**

**Rebuild ONE project from Week 3:**
Choose simplest (Weather or GitHub extractor).

**Rules:**
- From complete scratch ✅
- No looking at old code ✅
- Type from memory/understanding ✅
- Prove you can actually code ✅

**This is the test!**
Can you rebuild without copy-paste?

---

### Afternoon (2-4 PM)
**Continue rebuild**
- Make it work
- Handle errors
- Test thoroughly
- Compare to old version

**If you can do this:**
- You're actually learning ✅
- Ready for test ✅

**If you can't:**
- Need more practice ✅
- That's OK, we adjust ✅

---

### Evening (7-9 PM)
**Git push rebuild**
- Document what you learned
- Note what was hard
- Celebrate what worked

---

### Day 24 Goals
- [ ] Rebuilt one project completely
- [ ] From memory/understanding
- [ ] Working code
- [ ] REAL confidence boost!

---

## WEEKEND - DAYS 25-26 (NOV 8-9)

### Saturday - Week 4 Project

**Build: AI-Powered Tool**

**Choose ONE:**

**Option 1: DevOps AI Assistant**
- Ask infrastructure questions
- Get AI-powered solutions
- Save conversation history
- Export recommendations

**Option 2: Code Explainer**
- Paste any code
- AI explains what it does
- Line-by-line breakdown
- Suggests improvements

**Option 3: Document Summarizer**
- Paste long text/docs
- AI summarizes key points
- Different summary lengths
- Extract action items

**Rules:**
- Pick the one most useful to YOU ✅
- Build from scratch ✅
- Type everything ✅
- Make it production-quality ✅

**Morning (9 AM-12 PM):**
- Plan structure
- Build core functionality
- Test basic flow

**Afternoon (2-5 PM):**
- Add features
- Error handling
- Polish UX

---

### Sunday - Polish & Document

**Morning (9 AM-12 PM):**
- Add README with usage
- Test edge cases
- Make it reliable

**Afternoon (2-4 PM):**
- Create demo video/screenshots
- Document learning
- Week 4 reflection
- Git push

**Evening (7-8 PM):**
- Prepare for Week 4 TEST (Monday?)
- Review key concepts
- Be honest about what you know

---

## WEEK 4 TEST (End of Week?)

**Format:**
- 3-5 coding problems
- 2 hours
- NO AI help ❌
- Just you + code editor ✅

**Topics:**
- Python basics (functions, loops, conditionals)
- API calls (GET/POST)
- JSON handling
- Error handling
- Simple LLM integration

**Purpose:**
- See what you actually know
- Find gaps
- Adjust remaining weeks

**This will be uncomfortable.**  
**That's the point.** 💪

---

## API SETUP NEEDED

**Before Week 4 starts:**

**OpenAI:**
- Sign up: https://platform.openai.com/
- Get API key
- $5 free credit (enough for week)

**Anthropic (Claude):**
- Sign up: https://console.anthropic.com/
- Get API key
- Free tier available

**Store keys in `.env`:**
```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

**Add `.env` to `.gitignore`!** ⚠️

---

## RESOURCES (CONCEPTS ONLY!)

**OpenAI:**
- Docs: https://platform.openai.com/docs
- Quickstart: https://platform.openai.com/docs/quickstart
- API Reference: https://platform.openai.com/docs/api-reference

**Anthropic:**
- Docs: https://docs.anthropic.com/
- API Guide: https://docs.anthropic.com/claude/reference/getting-started-with-the-api

**Prompt Engineering:**
- OpenAI guide: https://platform.openai.com/docs/guides/prompt-engineering
- Anthropic guide: https://docs.anthropic.com/claude/docs/intro-to-prompting

**Use these to UNDERSTAND, not copy code!**

---

## SUCCESS METRICS

By Nov 9:

**Knowledge:**
- [ ] Understand LLM API structure deeply
- [ ] Can explain prompts, temperature, tokens
- [ ] Know streaming vs non-streaming
- [ ] Comfortable with both OpenAI & Claude

**Skills:**
- [ ] Can integrate AI APIs WITHOUT copy-paste
- [ ] Type code from understanding
- [ ] Debug API errors independently
- [ ] Build functional AI tools

**Output:**
- [ ] 7 days coded 🟩×7
- [ ] 4-5 AI tools built (ALL TYPED)
- [ ] Week 3 project rebuilt from scratch
- [ ] Week 4 test ready

**Mindset:**
- [ ] Can actually CODE (not just copy)
- [ ] Understand what I'm doing
- [ ] Ready for honest assessment
- [ ] Confident in fundamentals

---

## WEEK 4 MOTIVATION

**This is the uncomfortable week.**

**The week you:**
- Stop pretending ✅
- Start actually learning ✅
- Type every character ✅
- Build real skills ✅

**It will be slower.**  
**It will be messier.**  
**It will be frustrating.**

**But it will be REAL.**

**And in 6 more weeks:**
- You'll actually be ready ✅
- You'll pass interviews ✅
- You'll build real AI apps ✅
- Jan 2026 will happen ✅

**This week = The foundation of everything after.**

**Let's do this RIGHT.** 💪🔥

---

## DAILY REFLECTION TEMPLATE

**End of each day, answer honestly:**

**What I built today:**
- 

**Did I copy-paste:** Yes / No
- If yes, from where:
- How much:

**What I understood:**
- 

**What confused me:**
- 

**Can I rebuild this from scratch tomorrow:** Yes / No / Maybe

**Honest self-assessment (1-10):** ___

**Tomorrow's focus:**
- 

---

*Week 4: The week I stopped copy-pasting and started LEARNING* 🎯