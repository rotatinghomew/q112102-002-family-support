# 跨渠道申请漏斗与表单简化：资料契约

`sessions` 是渠道侧会话，`risk_facts` 为申请人用途及观察截止。`continuations` 的 `confirmed` 是可对上申请键的正式接续，`possible` 只在两边风险事实相容的条件下成为候选，同一旧会话不能同时接到两份独立申请。`visibility` 表知晓的采集盲区；未有轨迹不得判定未做。`actions` 的 `finish` 为正式签收，`stop` 为申请人明确不继续，`rejected` 为实质驳回。只有到期且无继续事实的可观察风险集才报告流失比例。`received` 是真实签收的材料，`permitted` 规则给出可验证替代，不在规则中即不替代。
政策规定 `身份核验` 与 `委托核验` 两个目的必须各保留一份独立证据；签发渠道/用途不适用不得用于当前待审核操作，同一 `proof` 不能同时作为两个目的唯一证据。`proposals` 同一方案可多行，`remove` 移除步骤，`reuse` 指向可替代材料，`defer` 移到正式受理前的末尾。`adoptions` 记录已核准的生效范围；核验目的不因流程简化而作废。日期为本地业务时间，适用区间左闭右开。

## 输入表

- `risk_facts.csv`：`app`、`person`、`purpose`、`started`、`deadline`、`population`
- `sessions.csv`：`session`、`app`、`channel`、`opened`
- `continuations.csv`：`from_session`、`to_session`、`state`、`recognized_on`
- `visibility.csv`：`channel`、`step`、`start`、`end`、`observable`
- `actions.csv`：`session`、`step`、`state`、`at`
- `received.csv`：`proof`、`app`、`kind`、`issuer`、`valid_until`、`signed_on`、`void_on`
- `permitted.csv`：`edition`、`from_date`、`population`、`purpose`、`kind`、`issuer`
- `proposals.csv`：`proposal`、`action`、`step`、`alternate`、`population`
- `adoptions.csv`：`proposal`、`confirmed_on`、`effective_on`、`population`
