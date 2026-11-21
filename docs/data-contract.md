# 热线分类风险与人工复核容量：资料契约

`messages` 一行是一份当时可见的来件描述；`origin` 是原始来件，`item` 是独立事项，`replaces` 表示同项描述补充，不能增加样本。`history` 给旧接单事实；`labels` 给已核实真类，`review` 为 `random` 或 `complaint`。标签更正用更晚的 `confirmed_on`，仅在决定时点已收到的标签可用。规则表 `audit_strata` 给原随机抽样策略的纳入概率（0 代表未获支持），每个来源层和月份可不同。`maturity` 给每个核实窗口和最长等待；材料未落入成熟期不作负样本。`loss` 给真实类被派错的代价，相同类代价为零，直派政策的可接受错派风险上限为 `policy.max_risk`。样例是合成数据，不能据来源名假定分析结论。
`intake` 是本班待判事项：到期按 `deadline`，时间为当地当班分钟，`priority=urgent` 可使用紧急专席。`review_slots` 中各编号各能核实一件，类为空表示全类；一项涉及多个尚未消歧的候选类时，该席位应能判别全部候选类。`commitments.review_held` 占指定席位；`dept_accepted` 表示旧派单已被接单。`new_facts` 在所列分钟进入，缺岗自当笔事实起生效。超时升级记录未移交或未核实的范围，不得算作已办。`loss` 与 `policy` 均为办公室规则，不从相同记录里反推。

## 输入表

- `messages.csv`：`item`、`origin`、`source`、`text`、`at`、`replaces`
- `history.csv`：`item`、`old_destination`、`accepted_at`
- `labels.csv`：`item`、`review`、`actual`、`confirmed_on`
- `audit_strata.csv`：`month`、`source`、`probability`
- `loss.csv`：`actual`、`destination`、`cost`
- `maturity.csv`：`minimum_label_days`、`max_review_minutes`
- `policy.csv`：`max_risk`、`minimum_random_per_source`
- `intake.csv`：`item`、`source`、`text`、`priority`、`arrive`、`deadline`
- `review_slots.csv`：`slot`、`staff`、`categories`、`start`、`end`、`urgent_only`
- `commitments.csv`：`id`、`item`、`status`、`assignment`、`at`
- `new_facts.csv`：`id`、`kind`、`target`、`value`、`at`
