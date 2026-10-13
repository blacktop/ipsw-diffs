## SpringBoard

> Group: ⬆️ Updated

```diff

 (deny system-memorystatus-control)
 (allow system-memorystatus-control
 	(memorystatus-control-command
+		40
 		MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOT
 		MEMORYSTATUS_CMD_GET_PRIORITY_LIST
 		MEMORYSTATUS_CMD_GET_PROCESS_IS_FROZEN
```
