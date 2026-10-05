## generativeexperiencesd

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.private.GenerativeAgentsTransport.runtime.com.apple.gms.clientexamplesd")
 			(global-name "com.apple.private.GenerativeAgentsTransport.runtime.mach.com.apple.freeform.FreeformAgentService")
 			(global-name "com.apple.private.GenerativeAgentsTransport.runtime.mach.com.apple.gms.clientexamplesd")
+			(global-name "com.apple.toolkitd.xpc")
 		))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.spotlightknowledged"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))

 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.siriactionsd.xpc"))
 		(require-not (global-name "com.apple.adid"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.diagd"))

 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))

 		SYS_sigpending
 		SYS_sigaltstack
 		SYS_ioctl
+		SYS_symlink
 		SYS_readlink
 		SYS_umask
 		SYS_msync
```
