## wifivelocityd

> Group: ⬆️ Updated

```diff

 
 (deny process-exec*
 	(require-all
-		(require-not (literal "/usr/bin/sw_vers"))
 		(require-not (require-any
+			(literal "/sbin/ifconfig")
+			(literal "/sbin/ping")
 			(literal "/sbin/ping6")
 			(literal "/usr/bin/dns-sd")
 			(literal "/usr/bin/footprint")

 			(literal "/usr/sbin/arp")
 			(literal "/usr/sbin/ndp")
 			(literal "/usr/sbin/netstat")
+			(literal "/usr/sbin/scutil")
 			(literal "/usr/sbin/traceroute")
 		))
+		(require-not (require-any
+			(literal "/usr/bin/sw_vers")
+			(literal "/usr/bin/zprint")
+			(literal "/usr/sbin/ioreg")
+		))
 		(require-any
 			(require-all
 				(require-not (literal "/usr/sbin/kextstat"))
-				(require-not (require-any
-					(literal "/sbin/ifconfig")
-					(literal "/sbin/ping")
-					(literal "/usr/sbin/scutil")
-				))
-				(require-not (require-any
-					(literal "/usr/bin/zprint")
-					(literal "/usr/sbin/ioreg")
-				))
 				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/bin/sh"))
 				(require-not (literal "/usr/sbin/tcpdump"))

 					(literal "/usr/local/bin/wifistats")
 					(literal "/usr/local/bin/wl")
 				))
-				(require-not (literal "/usr/local/bin/profilectl"))
-				(require-not (literal "/usr/local/bin/jetsam_priority"))
-				(require-not (literal "/usr/local/bin/apple80211"))
+				(require-not (require-any
+					(literal "/usr/local/bin/jetsam_priority")
+					(literal "/usr/local/bin/profilectl")
+				))
 				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (literal "/usr/local/bin/apple80211"))
 				(require-not (literal "/usr/sbin/kextstat"))
-				(require-not (require-any
-					(literal "/sbin/ifconfig")
-					(literal "/sbin/ping")
-					(literal "/usr/sbin/scutil")
-				))
-				(require-not (require-any
-					(literal "/usr/bin/zprint")
-					(literal "/usr/sbin/ioreg")
-				))
 				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/bin/sh"))
 				(require-not (literal "/usr/sbin/tcpdump"))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
