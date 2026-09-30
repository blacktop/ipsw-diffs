## AppleQEMUGuestAgent

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		(require-not (require-any
 			(literal "/bin/cat")
 			(literal "/bin/chmod")
+			(literal "/bin/date")
 			(literal "/sbin/md5")
 			(literal "/usr/bin/file")
+			(literal "/usr/bin/head")
+			(literal "/usr/bin/id")
+			(literal "/usr/bin/llvm-nm")
+			(literal "/usr/bin/llvm-objdump")
 			(literal "/usr/bin/pgrep")
 			(literal "/usr/bin/sqlite3")
 			(literal "/usr/bin/strings")
+			(literal "/usr/bin/true")
+			(literal "/usr/bin/which")
 			(literal "/usr/bin/xxd")
 		))
 		(require-not (literal "/bin/echo"))

 		(require-not (literal "/bin/bash"))
 		(require-not (require-any
 			(literal "/bin/sleep")
+			(literal "/usr/bin/uptime")
 			(literal "/usr/sbin/nvram")
 		))
-		(require-not (literal "/usr/bin/find"))
-		(require-not (literal "/sbin/ping"))
-		(require-not (literal "/usr/bin/plutil"))
-		(require-not (literal "/bin/sh"))
 		(require-not (literal "/usr/bin/log"))
+		(require-not (require-any
+			(literal "/sbin/ifconfig")
+			(literal "/sbin/ping")
+		))
+		(require-not (literal "/bin/sh"))
+		(require-not (literal "/usr/bin/pkill"))
+		(require-not (literal "/bin/launchctl"))
 		(require-not (literal "/bin/zsh"))
+		(require-not (literal "/usr/bin/find"))
+		(require-not (literal "/usr/bin/login"))
+		(require-not (literal "/usr/bin/plutil"))
 		(require-any
 			(require-all
-				(require-not (literal "/usr/local/bin/darwinup"))
 				(require-not (require-any
 					(literal "/usr/local/bin/amstool")
 					(literal "/usr/local/bin/assistant_tool")
 					(literal "/usr/local/bin/csfctl")
 					(literal "/usr/local/bin/homeutil")
+					(literal "/usr/local/bin/iftool")
+					(literal "/usr/local/bin/imtool")
+					(literal "/usr/local/bin/switchcl")
 				))
+				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (literal "/usr/local/bin/hkctl"))
 				(require-not (require-any
 					(literal "/usr/local/bin/LaunchApp")
 					(literal "/usr/local/bin/axctl")
 					(literal "/usr/local/bin/capturectl")
 					(literal "/usr/local/bin/fcq")
+					(literal "/usr/local/bin/ifrunner")
 					(literal "/usr/local/bin/pairtool")
+					(literal "/usr/local/bin/ps")
+					(literal "/usr/local/bin/snapshottool")
+					(literal "/usr/local/bin/ssutil")
 					(literal "/usr/local/bin/suiatool")
 					(literal "/usr/local/bin/swifter")
+					(literal "/usr/local/bin/untool")
 					(literal "/usr/local/bin/xctitool")
 					(literal "/usr/local/bin/xctspawn")
 					(literal "/usr/local/sbin/sshd")
```
