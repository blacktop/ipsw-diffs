## wifivelocityd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(require-not (literal "/usr/bin/sw_vers"))
 		(require-not (require-any
-			(literal "/sbin/ifconfig")
 			(literal "/sbin/ping6")
 			(literal "/usr/bin/dns-sd")
 			(literal "/usr/bin/footprint")

 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
 				))
-				(require-not (literal "/sbin/ping"))
 				(require-not (literal "/usr/bin/log"))
+				(require-not (require-any
+					(literal "/sbin/ifconfig")
+					(literal "/sbin/ping")
+				))
 				(require-not (literal "/bin/sh"))
 				(require-not (literal "/usr/sbin/tcpdump"))
 			)

 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
 				))
-				(require-not (literal "/sbin/ping"))
 				(require-not (literal "/usr/bin/log"))
+				(require-not (require-any
+					(literal "/sbin/ifconfig")
+					(literal "/sbin/ping")
+				))
 				(require-not (literal "/bin/sh"))
 				(require-not (literal "/usr/sbin/tcpdump"))
 			)
```
