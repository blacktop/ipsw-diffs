## wifivelocityd

> Group: ⬆️ Updated

```diff

 		))
 		(require-any
 			(require-all
+				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (require-any
 					(literal "/sbin/ifconfig")
 					(literal "/sbin/ping")
 					(literal "/usr/sbin/scutil")
 				))
-				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (require-any
 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")

 				(require-not (literal "/usr/local/bin/jetsam_priority"))
 				(require-not (literal "/usr/local/bin/apple80211"))
 				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (require-any
 					(literal "/sbin/ifconfig")
 					(literal "/sbin/ping")
 					(literal "/usr/sbin/scutil")
 				))
-				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (require-any
 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
```
