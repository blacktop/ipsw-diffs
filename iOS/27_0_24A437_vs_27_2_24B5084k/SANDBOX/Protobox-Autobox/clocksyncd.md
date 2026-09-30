## clocksyncd

> Group: ⬆️ Updated

```diff

 
 (deny system-fcntl)
 (allow system-fcntl
-	(fcntl-command F_GETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
+	(fcntl-command F_GETFL F_SETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
 )
 
 (deny system-fsctl)
```
