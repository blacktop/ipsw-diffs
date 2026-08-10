## HomeUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.springboard.services"))
 		(require-not (global-name "com.apple.backboard.display.services"))
+		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))

 		(require-not (global-name "com.apple.internal.studylogd"))
 		(require-not (global-name "com.apple.contactsd.launch-services-proxy"))
 		(require-not (global-name "com.apple.exchangesyncd"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))

 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
-		(require-not (global-name "com.apple.AccessibilityUIServer"))
+		(require-not (global-name "UIASTNotificationCenter"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (global-name "AccessibilityDebuggerServices"))
 		(require-not (system-attribute developer-mode))

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
