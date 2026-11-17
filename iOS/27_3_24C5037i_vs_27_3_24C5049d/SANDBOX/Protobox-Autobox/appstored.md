## appstored

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.AssetCacheLocatorService"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
+		(require-not (global-name "com.apple.lsd.appprotection"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.lsd.modifydb"))
 		(require-not (global-name "com.apple.carousel.connectionstatusservice"))

 		(require-not (global-name "com.apple.spotlight.IndexDelegateAgent"))
 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
-		(require-not (xpc-service-name "com.apple.ServicesPaymentPresentationService.xpc"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.ServicesPaymentPresentationService.xpc")
+			(xpc-service-name "com.apple.TestFlight.ServiceExtension")
+		))
 		(require-not (xpc-service-name "com.apple.MobileInstallationHelperService"))
 		(require-not (xpc-service-name "com.apple.VideoSubscriberAccount.DeveloperService"))
 		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
