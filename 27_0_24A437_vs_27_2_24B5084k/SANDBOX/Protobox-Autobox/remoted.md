## remoted

> Group: ⬆️ Updated

```diff

 
 (allow default)
 
+(deny asr-parser-enter)
+
 (deny file-ioctl)
 (allow file-ioctl
 	(ioctl-command (_IO "h" 4) TIOCSCTTY)
```
