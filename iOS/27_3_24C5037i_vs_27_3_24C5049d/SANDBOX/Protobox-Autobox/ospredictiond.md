## ospredictiond

> Group: ⬆️ Updated

```diff

 		SYS_access
 		SYS_chflags
 		SYS_fchflags
+		SYS_kill
 		SYS_crossarch_trap
 		SYS_dup
 		SYS_getegid

 		F_SINGLE_WRITER
 		F_BARRIERFSYNC
 		F_OFD_SETLK
+		F_OFD_GETLK
 		F_SETCONFINED
+		F_GETCONFINED
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )

 (deny system-memorystatus-control)
 (allow system-memorystatus-control
 	(memorystatus-control-command
+		MEMORYSTATUS_CMD_GET_PRIORITY_LIST
 		MEMORYSTATUS_CMD_GET_PRIORITY_LIST_V2
 		MEMORYSTATUS_CMD_GRP_SET_PROPERTIES
 		MEMORYSTATUS_CMD_INCREASE_JETSAM_TASK_LIMIT)
```
