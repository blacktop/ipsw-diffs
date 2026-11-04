## deleted_helper

> Group: ⬆️ Updated

```diff

 (deny system-fsctl)
 (allow system-fsctl
 	(fsctl-command
+		(_IO "J" 138)
 		APFSIOC_CLONEGROUP_ITERATE
 		APFSIOC_DIR_STATS_OP
 		APFSIOC_GET_CLONE_INFO

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
