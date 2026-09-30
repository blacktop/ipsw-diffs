## AppleQEMUGuestAgent

> Group: ⬆️ Updated

```diff

 
 (deny process-exec*
 	(require-all
-		(require-not (literal "/bin/bash"))
-		(require-not (literal "/usr/bin/find"))
 		(require-not (literal "/bin/ls"))
 		(require-not (literal "/usr/bin/sw_vers"))
-		(require-not (literal "/bin/sh"))
 		(require-not (require-any
 			(literal "/bin/cat")
 			(literal "/bin/chmod")
+			(literal "/sbin/md5")
+			(literal "/usr/bin/file")
+			(literal "/usr/bin/pgrep")
 			(literal "/usr/bin/sqlite3")
+			(literal "/usr/bin/xxd")
 		))
-		(require-not (literal "/bin/zsh"))
 		(require-not (literal "/bin/echo"))
-		(require-not (literal "/usr/bin/log"))
-		(require-not (literal "/usr/bin/defaults"))
-		(require-not (literal "/usr/sbin/nvram"))
 		(require-not (literal "/usr/bin/killall"))
+		(require-not (literal "/bin/bash"))
+		(require-not (require-any
+			(literal "/bin/sleep")
+			(literal "/usr/sbin/nvram")
+		))
+		(require-not (literal "/usr/bin/defaults"))
+		(require-not (literal "/sbin/ping"))
+		(require-not (literal "/bin/sh"))
+		(require-not (literal "/usr/bin/log"))
+		(require-not (literal "/bin/zsh"))
+		(require-not (literal "/usr/bin/find"))
 		(require-any
 			(require-all
-				(require-not (literal "/usr/local/bin/recap"))
 				(require-not (require-any
 					(literal "/usr/local/bin/axctl")
 					(literal "/usr/local/bin/capturectl")

 					(literal "/usr/local/bin/suiatool")
 					(literal "/usr/local/bin/swifter")
 					(literal "/usr/local/bin/xctitool")
+					(literal "/usr/local/bin/xctspawn")
 					(literal "/usr/local/sbin/sshd")
 				))
+				(require-not (require-any
+					(literal "/usr/local/bin/amstool")
+					(literal "/usr/local/bin/homeutil")
+				))
 				(require-not (literal "/usr/local/bin/darwinup"))
-				(require-not (literal "/usr/local/bin/homeutil"))
+				(require-not (literal "/usr/local/bin/recap"))
 				(require-not (literal "/usr/local/bin/profilectl"))
 				(require-not (literal "/AppleInternal/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9"))
 			)

 			task_get_special_port_from_user
 			task_set_special_port
 			semaphore_create
+			semaphore_destroy
 			task_set_exc_guard_behavior
 			vm_remap_external
 			mach_make_memory_entry_64

 					mach_exception_raise_state
 					mach_exception_raise_state_identity
 					mach_port_get_context_from_user))
+				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine task_restartable_ranges_register))
 				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine mach_vm_reallocate))
+				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine io_service_open_extended))
 				(require-not (kernel-mig-routine vm_reallocate))
 			)
```
