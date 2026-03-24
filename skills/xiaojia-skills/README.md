# xiaojia-skills

一个基于 JustAI OpenAPI 的 skill，可以安装到 Claude Code 或 Codex，用来调用线上 Agent 能力，而不是在本地直接推理。

目前主要支持：
- 查询可用资料库
- 查询可用 skill
- 提交异步对话任务
- 轮询查询已有 `conversation_id` 的结果

适合这些场景：
- 营销方案生成
- 小红书图文笔记生成
- 生图
- collect-info / confirm-info 后续推进

## 安装方式

推荐直接使用 `npx skills add`：

```bash
npx skills add https://github.com/qinshimeng18/xiaojia-skills --skill xiaojia-skills
```

安装后重启 Claude Code、Codex 或兼容的 skills 运行环境。

如果当前环境不支持 `npx skills add`，也可以手动复制 `skills/xiaojia-skills` 目录到本地 skills 目录。

## 前置要求

默认会请求生产地址 `https://justailab.com`，所以最少只需要配置：

```bash
export JUSTAI_OPENAPI_API_KEY="your-api-key"
```

可选覆盖：

```bash
export JUSTAI_OPENAPI_BASE_URL="https://justailab.com"
export JUSTAI_OPENAPI_TIMEOUT="300"
```

如果你要切到别的环境，再额外设置：

```bash
export JUSTAI_OPENAPI_BASE_URL="https://your-domain"
```

## 最短使用方式

先查看资料库：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/list_projects.py"
```

再查看可用 skill：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/list_skills.py"
```

然后先发起一次对话任务：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" --message "帮我做一份小红书运营方案"
```

拿到 `conversation_id` 之后，再查询结果：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat_result.py" \
  --conversation-id "your-conversation-id"
```

如果要继续同一轮对话，还是重新调用 `chat.py`，但要带上原来的 `conversation_id`。普通追问时再补新的 `message`：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --conversation-id "your-conversation-id" \
  --message "继续"
```

如果上一轮返回了 `form_id`，网页端那种“点确认后直接继续生成”的模式，对应的是直接带 `form_id` 继续，不需要再补一句确认文案：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --conversation-id "your-conversation-id" \
  --form-id "your-form-id"
```

如果用户改过表单内容，再把更新后的 `form_data` 一起传进去：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --conversation-id "your-conversation-id" \
  --form-id "your-form-id" \
  --form-data-file "/tmp/form_data.json"
```

也可以同时补一句自然语言指令，但不是必须：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --conversation-id "your-conversation-id" \
  --form-id "your-form-id" \
  --form-data-json '{"title":"资料卡","form":[]}' \
  --message "请按更新后的表单继续生成方案"
```

如果要限制到某个资料库或指定 skill，在提交任务时继续传：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/chat.py" \
  --project-id "fld_xxx" \
  --skill-id "skill_xxx" \
  --message "优先参考资料库并使用这个 skill"
```

## 说明

- `chat.py` 只负责 `/openapi/agent/chat_submit`
- `chat_result.py` 只负责 `/openapi/agent/chat_result`
- `conversation_id` 需要自己保留，用于后续续聊
- `confirm_info` 返回 `form_id` 后，默认续跑方式是直接传 `conversation_id + form_id`
- 如果用户改过资料卡，再额外传 `form_data`
- 自然语言续跑仍然可用，但不是“确认后继续生成”的主流程
- 在 Claude Code 中，`${CLAUDE_SKILL_DIR}` 会自动指向当前 skill 目录
