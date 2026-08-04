# workforge_discord_bot

## What This Does

Automates onboarding for the WorkForge AI apprenticeship program.

When someone joins the Discord server, the bot:
1. Sends a DM asking "What's your skill level?"
2. User replies: beginner / intermediate / advanced
3. Bot assigns a role and moves them to #web-dev
4. Bot sends welcome message with first project details

That's it.

---

## Tech Stack

**Backend (Python):**
- Discord.py
- Handles DM logic, role assignment, message routing

**Frontend (JavaScript):**
- Discord.js
- Bot initialization, command handling, Discord integration

---

## Timeline

3 weeks to MVP (basic sorting + assignment).

**Week 1:** Setup + planning
**Week 2-3:** Build + ship

---

## Tasks

- [ ] Python: DM handler + role assignment logic
- [ ] JavaScript: Bot commands + Discord setup
- [ ] Testing: Verify bot responds and assigns roles correctly
- [ ] Deployment: Get bot live and responding

---

## Getting Started

1. Clone repo
2. Install deps: `pip install discord.py` (Python) + `npm install discord.js` (JS)
3. Create `.env` with Discord token
4. Push commits to respective branches

---

## Contributors

- Loveday(Happylove32c) (JavaScript, project lead)
- VoidNitro12 (Python backend)

---

Made for WorkForge AI apprenticeship pilot.
