## AppleQEMUGuestAgent

> Group: ⬆️ Updated

```diff

 			(literal "/usr/sbin/nvram")
 		))
 		(require-not (literal "/bin/ls"))
+		(require-not (literal "/usr/bin/sw_vers"))
+		(require-not (literal "/bin/echo"))
+		(require-not (literal "/usr/bin/killall"))
+		(require-not (literal "/bin/bash"))
 		(require-not (require-any
 			(literal "/sbin/ifconfig")
 			(literal "/sbin/ping")
 			(literal "/usr/sbin/scutil")
 		))
-		(require-not (literal "/usr/bin/sw_vers"))
-		(require-not (literal "/bin/echo"))
-		(require-not (literal "/usr/bin/killall"))
-		(require-not (literal "/bin/bash"))
 		(require-not (require-any
 			(literal "/bin/kill")
 			(literal "/bin/rm")

 		(require-not (literal "/usr/bin/find"))
 		(require-not (literal "/sbin/mount"))
 		(require-not (literal "/bin/sh"))
+		(require-not (literal "/usr/bin/defaults"))
 		(require-not (require-any
 			(literal "/bin/cat")
 			(literal "/bin/chmod")
 			(literal "/bin/cp")
 			(literal "/bin/date")
+			(literal "/bin/hostname")
 			(literal "/bin/mkdir")
 			(literal "/sbin/md5")
 			(literal "/usr/bin/false")

 			(literal "/usr/bin/xxd")
 			(literal "/usr/libexec/debugserver")
 		))
-		(require-not (literal "/usr/bin/defaults"))
 		(require-any
 			(require-all
-				(require-not (literal "/usr/local/bin/darwinup"))
-				(require-not (require-any
-					(literal "/usr/local/bin/amstool")
-					(literal "/usr/local/bin/assistant_tool")
-					(literal "/usr/local/bin/csfctl")
-					(literal "/usr/local/bin/ffctl")
-					(literal "/usr/local/bin/homeutil")
-					(literal "/usr/local/bin/iftool")
-					(literal "/usr/local/bin/imtool")
-					(literal "/usr/local/bin/switchcl")
-				))
 				(require-not (require-any
 					(literal "/usr/local/bin/DumpDisplay")
 					(literal "/usr/local/bin/IOMFBDebug")

 					(literal "/usr/local/bin/captureIOMFBLayer")
 					(literal "/usr/local/bin/capturectl")
 					(literal "/usr/local/bin/ckctl")
+					(literal "/usr/local/bin/eligibility_util")
 					(literal "/usr/local/bin/fcq")
 					(literal "/usr/local/bin/ifrunner")
 					(literal "/usr/local/bin/loctool")

 					(literal "/usr/local/bin/ssutil")
 					(literal "/usr/local/bin/suiatool")
 					(literal "/usr/local/bin/swifter")
+					(literal "/usr/local/bin/uaftool")
 					(literal "/usr/local/bin/untool")
 					(literal "/usr/local/bin/uxautomationctl")
 					(literal "/usr/local/bin/xctitool")
 					(literal "/usr/local/bin/xctspawn")
 					(literal "/usr/local/sbin/sshd")
 				))
+				(require-not (require-any
+					(literal "/usr/local/bin/amstool")
+					(literal "/usr/local/bin/assistant_tool")
+					(literal "/usr/local/bin/csfctl")
+					(literal "/usr/local/bin/ffctl")
+					(literal "/usr/local/bin/homeutil")
+					(literal "/usr/local/bin/iftool")
+					(literal "/usr/local/bin/imtool")
+					(literal "/usr/local/bin/switchcl")
+				))
+				(require-not (literal "/usr/local/bin/profilectl"))
+				(require-not (literal "/usr/local/bin/recap"))
+				(require-not (literal "/usr/local/bin/darwinup"))
 				(require-not (require-any
 					(literal "/usr/local/bin/gestalt_query")
 					(literal "/usr/local/bin/hkctl")
 				))
-				(require-not (literal "/usr/local/bin/recap"))
-				(require-not (literal "/usr/local/bin/profilectl"))
 				(require-not (literal "/AppleInternal/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9"))
 			)
 			(require-not (system-attribute internal-build))
```
