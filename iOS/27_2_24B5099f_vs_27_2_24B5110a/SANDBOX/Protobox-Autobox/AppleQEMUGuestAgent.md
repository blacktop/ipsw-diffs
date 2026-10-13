## AppleQEMUGuestAgent

> Group: ⬆️ Updated

```diff

 		(require-not (literal "/bin/ls"))
 		(require-not (literal "/usr/bin/sw_vers"))
 		(require-not (literal "/bin/echo"))
+		(require-not (require-any
+			(literal "/bin/cat")
+			(literal "/bin/chmod")
+			(literal "/bin/cp")
+			(literal "/bin/date")
+			(literal "/bin/hostname")
+			(literal "/bin/mkdir")
+			(literal "/sbin/md5")
+			(literal "/usr/bin/false")
+			(literal "/usr/bin/file")
+			(literal "/usr/bin/grep")
+			(literal "/usr/bin/head")
+			(literal "/usr/bin/id")
+			(literal "/usr/bin/llvm-nm")
+			(literal "/usr/bin/llvm-objdump")
+			(literal "/usr/bin/nc")
+			(literal "/usr/bin/notifyutil")
+			(literal "/usr/bin/pgrep")
+			(literal "/usr/bin/printf")
+			(literal "/usr/bin/sqlite3")
+			(literal "/usr/bin/strings")
+			(literal "/usr/bin/tail")
+			(literal "/usr/bin/true")
+			(literal "/usr/bin/which")
+			(literal "/usr/bin/xxd")
+			(literal "/usr/libexec/debugserver")
+		))
 		(require-not (literal "/usr/bin/killall"))
 		(require-not (literal "/bin/bash"))
 		(require-not (require-any

 		(require-not (literal "/sbin/mount"))
 		(require-not (literal "/bin/sh"))
 		(require-not (literal "/usr/bin/defaults"))
-		(require-not (require-any
-			(literal "/bin/cat")
-			(literal "/bin/chmod")
-			(literal "/bin/cp")
-			(literal "/bin/date")
-			(literal "/bin/hostname")
-			(literal "/bin/mkdir")
-			(literal "/sbin/md5")
-			(literal "/usr/bin/false")
-			(literal "/usr/bin/file")
-			(literal "/usr/bin/grep")
-			(literal "/usr/bin/head")
-			(literal "/usr/bin/id")
-			(literal "/usr/bin/llvm-nm")
-			(literal "/usr/bin/llvm-objdump")
-			(literal "/usr/bin/notifyutil")
-			(literal "/usr/bin/pgrep")
-			(literal "/usr/bin/printf")
-			(literal "/usr/bin/sqlite3")
-			(literal "/usr/bin/strings")
-			(literal "/usr/bin/tail")
-			(literal "/usr/bin/true")
-			(literal "/usr/bin/which")
-			(literal "/usr/bin/xxd")
-			(literal "/usr/libexec/debugserver")
-		))
 		(require-any
 			(require-all
 				(require-not (require-any
```
