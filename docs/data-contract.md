# 社区转介与服务补助对账：资料契约

`plans` 记录受助人分项目的需求量，`unit` 是服务本身的计量单位。`authorizations` 指定可接手机构，`proxy` 表明可否直接代为转介。`segments` 是同一人员共同占用的服务区间，`shares` 是其中不同需求的履约证据；`fraction` 用于分配该人员工时，`amount` 用于抵扣服务需求。资助项目以分钟额度核算，工时分摊若产生非整数分钟可用精确比例保留，报表不向上重复取整；只允许在 `backfill_for` 明示对应主项目时补足。补报使用服务日期的授权、项目范围和额度，限额按资金方、自然月执行。
`verified` 为机构及家庭可核实已执行；`no_access` 为未接触；`disputed` 指该份证据与同一记录的现存证据冲突，不影响可独立认定份额。有已核实与待议记录互相重叠时，待议记录不挤占已核实的工时；两个已核实记录仍互相矛盾时，共享时段先挂起。结算候选优先尊重既有实付余额，剩余额度按服务发生时点先后使用，时点相同按份额编号。`changes` 的 `replace` 替代所指份额的资助归属证明，不抹掉其履约事实；`withdraw` 从给定时间起取消指定服务的未履约需求。`payments` 是财务回单，`reversal` 的 `prior` 指原付款，分钟为正数绝对值。示例时间为当地时间，区间左闭右开。

## 输入表

- `plans.csv`：`need`、`resident`、`kind`、`unit`、`required`、`start`、`end`
- `authorizations.csv`：`id`、`need`、`agency`、`start`、`end`、`proxy`
- `referrals.csv`：`id`、`need`、`agency`、`state`、`at`
- `segments.csv`：`id`、`worker`、`agency`、`start`、`end`
- `shares.csv`：`id`、`segment`、`need`、`fraction`、`amount`、`proof`、`primary`
- `funds.csv`：`fund`、`scope`、`start`、`end`、`month_limit_minutes`、`backfill_for`
- `changes.csv`：`id`、`action`、`subject`、`replacement`、`at`
- `payments.csv`：`id`、`share`、`fund`、`kind`、`minutes`、`prior`、`at`
