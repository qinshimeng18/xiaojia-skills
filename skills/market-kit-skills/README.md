# Market Kit Skills

把营销需求直接推进成可交付结果的 AI skill。

`Market Kit Skills` 不是一个只会陪你聊天的通用助手。它面向真实营销场景设计，目标很直接：把你脑子里的想法、你手里的资料、你已有的上下文，推进成更接近可发布状态的营销方案、小红书图文笔记、卖点表达、内容方向和营销图片。

如果你要的是“给我一个结果”，而不是“我们先泛泛聊聊”，这就是为你准备的 skill。

## 为什么它很强

很多工具只能给你一段文案，但营销工作真正难的地方从来不只是写字，而是把目标、资料、卖点、图片、内容方向和后续迭代串起来。

`Market Kit Skills` 的强，不在于它能说得多花，而在于它能把整条营销生成链路打通：

- 能出营销方案，也能出内容方向和 campaign plan
- 能出小红书图文笔记，不只是标题，还包括正文和配图
- 能基于资料库生成参考驱动内容，而不是脱离事实乱写
- 能在已有方案、资料卡和会话上继续迭代，不用每次从头来
- 能同时返回内容、图片链接和网页版结果链接，方便继续追踪和复用

你拿到的不只是一个回答，而是一份可以继续推进、继续修改、继续交付的营销结果。

## 它适合谁

- 做品牌营销、内容营销、增长营销的团队
- 需要快速出 campaign 方案和内容规划的人
- 需要批量生产小红书图文、小红书笔记和种草内容的人
- 需要围绕资料库、产品资料、品牌资料持续产出内容的人
- 需要边生成边迭代，而不是一次性拿一段静态文案的人

## 它能直接做什么

- 生成营销方案、内容规划和 campaign plan
- 生成小红书图文笔记、标题、正文和配图
- 提炼人群、卖点、定位和差异化表达
- 基于资料库生成参考驱动的营销内容
- 生成营销图片，以及图文一体的结果
- 围绕同一条会话继续改写、补充、扩展和追问

## 典型交付物

- 新品上线营销方案
- 品牌种草内容方向
- 小红书种草图文笔记
- 人群与卖点拆解
- 资料驱动的内容提案
- 文案 + 图片 + 网页版结果的完整营销内容

## 为什么和普通 AI 不一样

普通 AI 更像“即时回答器”，擅长当场给你一段文字。

`Market Kit Skills` 更像一条营销生产链路：

- 前面可以收集和确认必要信息
- 中间可以走明确的营销生成能力
- 后面可以继续轮询、继续迭代、继续扩写
- 结果既有结构化内容，也有图片链接和网页落地页

这意味着它更适合真实业务，而不是只适合演示。

## 安装方式

安装方式很简单：把这个 GitHub 仓库地址发给你的 Agent，然后告诉它帮你安装 `market-kit-skills` 就可以。

```text
请帮我安装这个 skill：
https://github.com/qinshimeng18/xiaojia-skills

skill 名称：
market-kit-skills
```

## 首次使用

安装后第一步先引导用户完成登录，再开始营销生成、资料库选择或结果查询。在未确认登录完成前，不要先收集需求、不要先追问笔记方向。

这条规则必须严格执行。因为这套 skill 的价值在于调用真实的营销生成链路，而不是在未完成登录时先本地即兴编一版内容糊弄过去。

## 推荐工作流

### 1. 先完成登录

首次使用时，先完成登录，再进入后续营销任务。

### 2. 查看资料库

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/list_projects.py"
```

### 3. 查看可选能力链路

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/list_skills.py"
```

### 4. 提交营销任务

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" --message "帮我做一份护肤品牌新品营销方案"
```

### 5. 查询结果

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat_result.py" \
  --conversation-id "your-conversation-id"
```

### 6. 在同一轮结果上继续迭代

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --conversation-id "your-conversation-id" \
  --message "继续扩写成适合小红书发布的图文笔记"
```

## 常用玩法

限定资料库，做参考驱动内容：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --project-id "fld_xxx" \
  --message "参考资料库内容，生成一篇留学种草图文"
```

限定能力链路，强制走某条营销能力：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --skill-id "skill_xxx" \
  --message "使用这个营销 skill 继续生成内容"
```

在确认信息卡后继续生成：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --conversation-id "your-conversation-id" \
  --message "这些信息没问题，继续生成方案"
```

## 结果会返回什么

- `chat.py` 负责提交任务
- `chat_result.py` 负责查询结果
- `conversation_id` 需要保留，用于续聊和后续追踪
- `web_url` 是网页版结果链接，格式为 `https://justailab.com/marketing?conversation_id=<conversation_id>`
- 小红书图文笔记图片通常在 `result.result.components[].data.images[].url`
- 小红书图文笔记标题通常在 `result.result.components[].data.title`
- 小红书图文笔记正文通常在 `result.result.components[].data.content`

## 结果判断规则

- 如果当前还是 `running`，说明内容仍在生成，不应过早判断失败
- 如果脚本返回 `Polling timed out before task completed.`，不要把轮询超时当成任务失败
- 对 `generate_notes`、`generate_image` 这类慢分支，除非用户明确要求，否则不要把 `chat_result.py --timeout` 设成小于 `300`
- 如果任务还没完成，不要自己擅自生成标题、正文、图片说明或图片链接返回给用户
- 如果任务已完成，除了内容和图片链接，还要把 `web_url` 一起返回给用户

## 最佳实践

- 需要资料驱动时，先选 `project_id`
- 需要特定能力链路时，先选 `skill_id`
- 返回结果时优先读取结构化 `result`
- 处理小红书图文结果时，把标题、正文、图片链接和 `web_url` 一起交付
- 安装后第一步先引导用户完成登录，再进入后续营销生成；不要先收集需求

## 一句话总结

如果你想要的不是“帮我写一句文案”，而是“帮我把营销这件事往前推一步，最好直接给我能用的结果”，那 `Market Kit Skills` 就是你该装的那个 skill。
