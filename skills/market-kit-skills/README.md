# Market Kit Skills

![AI Skill](https://img.shields.io/badge/AI%20Skill-Marketing-black)
![Xiaohongshu Ready](https://img.shields.io/badge/Xiaohongshu-Ready-red)
![Campaign Planning](https://img.shields.io/badge/Campaign-Planning-blue)
![GitHub Install](https://img.shields.io/badge/Install-From%20GitHub-success)
![Agent Ready](https://img.shields.io/badge/Ready%20for-Agents-orange)
![Web Result](https://img.shields.io/badge/Web%20Result-justailab.com-6f42c1)

把营销需求直接推进成可交付结果的 AI skill。

`Market Kit Skills` 不是一个只会陪你聊天的通用助手。它面向真实营销场景设计，目标很直接：把你脑子里的想法、你手里的资料、你已有的上下文，推进成更接近可发布状态的营销方案、小红书图文笔记、卖点表达、内容方向和营销图片。

如果你要的是“给我一个结果”，而不是“我们先泛泛聊聊”，这就是为你准备的 skill。

> [!TIP]
> 这不是一个泛用聊天 prompt，而是一条面向营销交付的生产链路。它的价值在于持续生成、持续迭代、持续追踪，而不是临时写一段漂亮话。

## 为什么它很强

很多工具只能给你一段文案，但营销工作真正难的地方从来不只是写字，而是把目标、资料、卖点、图片、内容方向和后续迭代串起来。

`Market Kit Skills` 的强，不在于它能说得多花，而在于它能把整条营销生成链路打通：

| 能力 | 结果 |
| --- | --- |
| 营销方案生成 | 输出 campaign plan、内容规划、营销方向 |
| 小红书图文生成 | 产出标题、正文、图片和图文结构 |
| 参考资料驱动 | 基于资料库生成，不脱离事实乱写 |
| 会话内持续迭代 | 在已有方案、资料卡和会话上继续改写 |
| 结果可追踪 | 同时返回内容、图片链接和网页版结果链接 |

你拿到的不只是一个回答，而是一份可以继续推进、继续修改、继续交付的营销结果。

## 它适合谁

- 做品牌营销、内容营销、增长营销的团队
- 需要快速出 campaign 方案和内容规划的人
- 需要批量生产小红书图文、小红书笔记和种草内容的人
- 需要围绕资料库、产品资料、品牌资料持续产出内容的人
- 需要边生成边迭代，而不是一次性拿一段静态文案的人

## 它能直接做什么

| 场景 | 直接产出 |
| --- | --- |
| 新品营销 | 营销方案、campaign plan、内容方向 |
| 小红书运营 | 小红书图文笔记、标题、正文、配图 |
| 品牌表达 | 人群、卖点、定位、差异化表达 |
| 内容提案 | 基于资料库生成参考驱动内容 |
| 创意延展 | 生成营销图片和图文一体的结果 |
| 持续优化 | 围绕同一条会话继续改写、补充、扩展和追问 |

## 典型交付物

| 类型 | 示例 |
| --- | --- |
| 营销方案 | 新品上线营销方案、品牌 campaign plan |
| 内容交付 | 小红书种草图文笔记、品牌种草内容方向 |
| 策略拆解 | 人群洞察、卖点提炼、定位表达 |
| 参考驱动内容 | 基于资料库的内容提案、选题建议 |
| 图文一体结果 | 文案 + 图片 + 网页版结果的完整营销内容 |

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

> [!NOTE]
> 安装方式就是这么简单。把仓库地址给 Agent，然后说“帮我安装 `market-kit-skills`”就够了。

## 首次使用

安装后第一步先引导用户完成登录，再开始营销生成、资料库选择或结果查询。在未确认登录完成前，不要先收集需求、不要先追问笔记方向。

这条规则必须严格执行。因为这套 skill 的价值在于调用真实的营销生成链路，而不是在未完成登录时先本地即兴编一版内容糊弄过去。

> [!WARNING]
> 安装后第一步先引导用户完成登录。不要先收集需求，不要先追问笔记方向，也不要在未登录时直接编一版内容返回。

## 推荐工作流

### 1. 先完成登录

首次使用时，先完成登录，再进入后续营销任务。

### 2. 查看资料库

### 3. 查看可选能力链路

### 4. 提交营销任务

### 5. 查询结果

### 6. 在同一轮结果上继续迭代

<details>
<summary>展开查看常用命令</summary>

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/list_projects.py"
python3 "${CLAUDE_SKILL_DIR}/scripts/list_skills.py"
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" --message "帮我做一份护肤品牌新品营销方案"
python3 "${CLAUDE_SKILL_DIR}/scripts/chat_result.py" --conversation-id "your-conversation-id"
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" --conversation-id "your-conversation-id" --message "继续扩写成适合小红书发布的图文笔记"
```

</details>

## 常用玩法

<details>
<summary>展开查看进阶调用方式</summary>

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

</details>

## 结果会返回什么

| 字段 | 说明 |
| --- | --- |
| `chat.py` | 负责提交任务 |
| `chat_result.py` | 负责查询结果 |
| `conversation_id` | 需要保留，用于续聊和后续追踪 |
| `web_url` | 网页版结果链接，格式为 `https://justailab.com/marketing?conversation_id=<conversation_id>` |
| `result.result.components[].data.images[].url` | 小红书图文笔记图片 |
| `result.result.components[].data.title` | 小红书图文笔记标题 |
| `result.result.components[].data.content` | 小红书图文笔记正文 |

## 结果判断规则

- 如果当前还是 `running`，说明内容仍在生成，不应过早判断失败
- 如果脚本返回 `Polling timed out before task completed.`，不要把轮询超时当成任务失败
- 对 `generate_notes`、`generate_image` 这类慢分支，除非用户明确要求，否则不要把 `chat_result.py --timeout` 设成小于 `300`
- 如果任务还没完成，不要自己擅自生成标题、正文、图片说明或图片链接返回给用户
- 如果任务已完成，除了内容和图片链接，还要把 `web_url` 一起返回给用户

> [!IMPORTANT]
> `running` 不是失败，`Polling timed out before task completed.` 也不是失败。真正正确的做法，是告诉用户内容还在生成，并在完成后返回内容、图片链接和 `web_url`。

## 最佳实践

- 需要资料驱动时，先选 `project_id`
- 需要特定能力链路时，先选 `skill_id`
- 返回结果时优先读取结构化 `result`
- 处理小红书图文结果时，把标题、正文、图片链接和 `web_url` 一起交付
- 安装后第一步先引导用户完成登录，再进入后续营销生成；不要先收集需求

## 一句话总结

如果你想要的不是“帮我写一句文案”，而是“帮我把营销这件事往前推一步，最好直接给我能用的结果”，那 `Market Kit Skills` 就是你该装的那个 skill。
