## facetimemessagestored

> Group: ⬆️ Updated

```diff

 
 (allow default)
 
-(deny asr-parser-enter
-	(require-any
-		(require-not (asr-parser-domain ASR_DOMAIN_IMAGES))
-		(require-not (asr-parser-name "com.apple.imageio.atx"))
-	)
-)
+(deny asr-parser-enter)
 
 (deny file-ioctl)
 (allow file-ioctl

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
