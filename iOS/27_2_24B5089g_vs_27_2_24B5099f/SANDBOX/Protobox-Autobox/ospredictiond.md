## ospredictiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.milod.xpc.service"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.routined.registration"))

 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
-	(memorystatus-control-command MEMORYSTATUS_CMD_INCREASE_JETSAM_TASK_LIMIT)
+	(memorystatus-control-command
+		MEMORYSTATUS_CMD_GET_PRIORITY_LIST_V2
+		MEMORYSTATUS_CMD_INCREASE_JETSAM_TASK_LIMIT)
 )
 
 (deny system-necp-client-action)
```
