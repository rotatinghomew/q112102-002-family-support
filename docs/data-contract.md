# 漏登居民估计与独立补访：资料契约

`overlap` 对每期同片区同一定义的三张名册 A/B/C 给出互斥的出现组合 `abc`，1 表示出现，0 表示不出现；000 未观测。`verified=0` 或空值为数字未核清，不按 0 处理，后续补核用较晚时间覆盖同一单元。上界来自 `regions` 的可登记居民数上界。`dependence` 标注哪些期间的来源共享登记入口或存在转介；这些是可检验的适用条件而不是给定的独立性。分析可比较有依据的多名单模型及依赖敏感度；没有可识别支持时保留可证明的界限。不使用姓名等个人数据。
`address_frame` 每个 `frame` 是地址框之一，两个框的相同 `dwelling` 是同一住宅，不可当两个抽访机会。`independent=0` 表示地址仅由原名册转介，不计入新增的独立抽访覆盖。`access_windows` 为本月地址可访问时段（含开始不含结束），`staff_slots` 每席位一户。`observations` 的 `unanswered` 有访问机会但无人回答；`covered` 或 `new` 表示有效完成、分别确认已登记或新发现。政策覆盖使用符合资格的独立住宅框中有效完成计数；抽查来自 `sample_plan` 中冻结的不同纳入概率的片区住宅名单，估计时区分在框和有效应答、两者不能直接相除作漏登估计。`commitments` 是已通知住户的席位。`adjustments` 为已确认的服务名额调整，记录原统计截止；`changes` 追加观察作废、许可撤回或班次取消。各日期为当地时间。

## 输入表

- `regions.csv`：`period`、`area`、`eligible_upper`
- `overlap.csv`：`period`、`area`、`abc`、`people`、`verified`、`reported_on`
- `dependence.csv`：`period`、`area`、`sources`、`basis`
- `address_frame.csv`：`period`、`area`、`frame`、`dwelling`、`independent`
- `sample_plan.csv`：`period`、`area`、`dwelling`、`probability`、`frozen_on`
- `observations.csv`：`id`、`dwelling`、`state`、`observed_on`、`reported_on`
- `access_windows.csv`：`dwelling`、`start`、`end`
- `staff_slots.csv`：`slot`、`start`、`end`、`areas`
- `commitments.csv`：`id`、`slot`、`dwelling`、`notified_on`
- `changes.csv`：`id`、`kind`、`target`、`at`
- `policy.csv`：`area`、`minimum_independent_interviews`、`minimum_missing_share`
- `adjustments.csv`：`id`、`area`、`effective_period`、`extra_slots`、`confirmed_on`、`evidence_cutoff`
