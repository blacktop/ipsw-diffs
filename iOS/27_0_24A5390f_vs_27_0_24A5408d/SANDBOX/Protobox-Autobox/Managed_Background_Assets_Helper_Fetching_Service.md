## Managed Background Assets Helper Fetching Service

> Group: ⬆️ Updated

```diff

 (allow default)
 
 (deny file-ioctl)
+(allow file-ioctl
+	(ioctl-command (_IO "h" 4))
+)
 
 (deny generic-issue-extension)
 
```
