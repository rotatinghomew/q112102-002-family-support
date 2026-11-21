# 数据说明

家庭支持需求、转介、服务发生与回访的合成资料。

下列文件仅包含合成记录。空值按 CSV 空单元格保存；时间字段使用当地业务记录时间，不预设统计结论。

## `needs.csv`

字段：`need_id`、`family_ref`、`group_code`、`need_type`、`valid_from`、`valid_to`、`status`。当前演练样本 4 条。

## `referrals.csv`

字段：`referral_id`、`need_id`、`service_code`、`sent_at`、`state`、`reason`。当前演练样本 4 条。

## `service_events.csv`

字段：`event_id`、`referral_id`、`occurred_at`、`event_type`、`staff_ref`。当前演练样本 3 条。
