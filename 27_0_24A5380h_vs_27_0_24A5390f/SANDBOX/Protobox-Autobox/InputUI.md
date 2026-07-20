## InputUI

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
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleANS3NVMeController")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
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
 		(require-not (global-name "com.apple.storekitd"))

 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
+		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (global-name "com.apple.assistant.settings"))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))
 		(require-not (global-name "com.apple.PrototypeTools.domainserver"))

 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (require-any
+			(global-name "UIASTNotificationCenter")
 			(global-name "com.apple.MercuryPoster.viewservice")
 			(global-name "com.apple.inputservice.keyboarduis")
 			(global-name "com.apple.inputservice.keyboarduiz")

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.handwritingd.remoterecognition"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.modelmanager"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.accessibility.voices"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.springboard.services"))
 		(require-not (global-name "com.apple.backboard.display.services"))
+		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
 		(require-not (global-name "com.apple.pasteboard.pasted"))

 		(require-not (global-name "com.apple.passd.payment"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.email.maild"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.dmd.policy"))
 		(require-not (global-name "com.apple.handwritingd.pkanalytics"))
-		(require-not (global-name "com.apple.spotlight.SearchAgent"))
-		(require-not (global-name "com.apple.ABDatabaseDoctor"))
-		(require-not (global-name "com.apple.AccessibilityUIServer"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (system-attribute developer-mode))
 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
