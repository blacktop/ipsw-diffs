## wifivelocityd

> Group: ⬆️ Updated

```diff

 			(literal "/usr/sbin/arp")
 			(literal "/usr/sbin/ndp")
 			(literal "/usr/sbin/netstat")
-			(literal "/usr/sbin/scutil")
 			(literal "/usr/sbin/traceroute")
 		))
 		(require-any
 			(require-all
+				(require-not (require-any
+					(literal "/sbin/ifconfig")
+					(literal "/sbin/ping")
+					(literal "/usr/sbin/scutil")
+				))
 				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (require-any
 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
 				))
 				(require-not (literal "/usr/bin/log"))
-				(require-not (require-any
-					(literal "/sbin/ifconfig")
-					(literal "/sbin/ping")
-				))
 				(require-not (literal "/bin/sh"))
 				(require-not (literal "/usr/sbin/tcpdump"))
 			)

 				(require-not (literal "/usr/local/bin/jetsam_priority"))
 				(require-not (literal "/usr/local/bin/apple80211"))
 				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (require-any
+					(literal "/sbin/ifconfig")
+					(literal "/sbin/ping")
+					(literal "/usr/sbin/scutil")
+				))
 				(require-not (literal "/usr/sbin/kextstat"))
 				(require-not (require-any
 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
 				))
 				(require-not (literal "/usr/bin/log"))
-				(require-not (require-any
-					(literal "/sbin/ifconfig")
-					(literal "/sbin/ping")
-				))
 				(require-not (literal "/bin/sh"))
 				(require-not (literal "/usr/sbin/tcpdump"))
 			)
```
