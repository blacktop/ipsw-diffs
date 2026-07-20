## AppleQEMUGuestAgent

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 	)
 )
 
+(deny iokit-open-user-client)
+
 (deny iokit-open-service)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(ipc-posix-name "apple.shm.notification_center")
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.notification_center"))

 	)
 )
 
+(deny process-codesigning
+	(require-all
+		(require-not (literal "/bin/ls"))
+		(require-not (literal "/usr/bin/sw_vers"))
+		(require-not (require-any
+			(literal "/bin/cat")
+			(literal "/bin/chmod")
+			(literal "/sbin/md5")
+			(literal "/usr/bin/file")
+			(literal "/usr/bin/pgrep")
+			(literal "/usr/bin/sqlite3")
+			(literal "/usr/bin/strings")
+			(literal "/usr/bin/xxd")
+		))
+		(require-not (literal "/bin/echo"))
+		(require-not (literal "/usr/bin/killall"))
+		(require-not (literal "/usr/bin/defaults"))
+		(require-not (literal "/bin/bash"))
+		(require-not (require-any
+			(literal "/bin/sleep")
+			(literal "/usr/sbin/nvram")
+		))
+		(require-not (literal "/usr/bin/find"))
+		(require-not (literal "/sbin/ping"))
+		(require-not (literal "/usr/bin/plutil"))
+		(require-not (literal "/bin/sh"))
+		(require-not (literal "/usr/bin/log"))
+		(require-not (literal "/bin/zsh"))
+		(require-any
+			(require-all
+				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (require-any
+					(literal "/usr/local/bin/amstool")
+					(literal "/usr/local/bin/assistant_tool")
+					(literal "/usr/local/bin/csfctl")
+					(literal "/usr/local/bin/homeutil")
+				))
+				(require-not (require-any
+					(literal "/usr/local/bin/LaunchApp")
+					(literal "/usr/local/bin/axctl")
+					(literal "/usr/local/bin/capturectl")
+					(literal "/usr/local/bin/fcq")
+					(literal "/usr/local/bin/pairtool")
+					(literal "/usr/local/bin/suiatool")
+					(literal "/usr/local/bin/swifter")
+					(literal "/usr/local/bin/xctitool")
+					(literal "/usr/local/bin/xctspawn")
+					(literal "/usr/local/sbin/sshd")
+				))
+				(require-not (literal "/usr/local/bin/recap"))
+				(require-not (literal "/usr/local/bin/profilectl"))
+				(require-not (literal "/AppleInternal/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9"))
+			)
+			(require-not (system-attribute internal-build))
+		)
+	)
+)
+
 (deny process-exec*
 	(require-all
 		(require-not (literal "/bin/ls"))

 			(literal "/usr/bin/file")
 			(literal "/usr/bin/pgrep")
 			(literal "/usr/bin/sqlite3")
+			(literal "/usr/bin/strings")
 			(literal "/usr/bin/xxd")
 		))
 		(require-not (literal "/bin/echo"))
 		(require-not (literal "/usr/bin/killall"))
+		(require-not (literal "/usr/bin/defaults"))
 		(require-not (literal "/bin/bash"))
 		(require-not (require-any
 			(literal "/bin/sleep")
 			(literal "/usr/sbin/nvram")
 		))
-		(require-not (literal "/usr/bin/defaults"))
+		(require-not (literal "/usr/bin/find"))
 		(require-not (literal "/sbin/ping"))
+		(require-not (literal "/usr/bin/plutil"))
 		(require-not (literal "/bin/sh"))
 		(require-not (literal "/usr/bin/log"))
 		(require-not (literal "/bin/zsh"))
-		(require-not (literal "/usr/bin/find"))
 		(require-any
 			(require-all
+				(require-not (literal "/usr/local/bin/darwinup"))
 				(require-not (require-any
+					(literal "/usr/local/bin/amstool")
+					(literal "/usr/local/bin/assistant_tool")
+					(literal "/usr/local/bin/csfctl")
+					(literal "/usr/local/bin/homeutil")
+				))
+				(require-not (require-any
+					(literal "/usr/local/bin/LaunchApp")
 					(literal "/usr/local/bin/axctl")
 					(literal "/usr/local/bin/capturectl")
 					(literal "/usr/local/bin/fcq")

 					(literal "/usr/local/bin/xctspawn")
 					(literal "/usr/local/sbin/sshd")
 				))
-				(require-not (require-any
-					(literal "/usr/local/bin/amstool")
-					(literal "/usr/local/bin/homeutil")
-				))
-				(require-not (literal "/usr/local/bin/darwinup"))
 				(require-not (literal "/usr/local/bin/recap"))
 				(require-not (literal "/usr/local/bin/profilectl"))
 				(require-not (literal "/AppleInternal/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9"))
```
