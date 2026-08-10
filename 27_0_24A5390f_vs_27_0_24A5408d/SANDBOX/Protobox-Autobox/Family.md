## Family

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.naturallanguaged"))
 		(require-not (global-name "com.apple.icloud.fmfd"))
 		(require-not (global-name "com.apple.webinspector"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.assetcacheinspector.xpc"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.lsd.icons"))

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (global-name "com.apple.translation.text"))
-		(require-not (require-any
-			(global-name "com.apple.appprotectiond.viewsubjectinfo")
-			(global-name "com.apple.appprotectiond.viewsubjectmonitor")
-		))
 		(require-not (global-name "com.apple.bird.token"))
 		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))

 		(require-not (global-name "com.apple.internal.studylogd"))
 		(require-not (global-name "com.apple.intelligenceplatform.Feedback"))
 		(require-not (global-name "com.apple.contactsd.launch-services-proxy"))
+		(require-not (global-name "com.apple.appprotectiond.viewsubjectmonitor"))
 		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.synapse.backlink-service"))
 		(require-not (global-name "com.apple.containermanagerd"))

 			(global-name "com.apple.iMessageAppsViewService.warmup-connection")
 			(global-name "com.apple.uikit.viewservice.com.apple.iMessageAppsViewService")
 		))
+		(require-not (global-name "com.apple.appprotectiond.viewsubjectinfo"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.itunescloudd.xpc"))

 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
+		(require-not (global-name "UIASTNotificationCenter"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fchmodat
 		SYS_fstatat
```
