## akd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.coreidvd.proofing"))
 		(require-not (global-name "com.apple.ak.auth.xpc"))
+		(require-not (require-any
+			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
+			(global-name "com.apple.ak.shieldservices.xpc")
+			(global-name "com.apple.appleidsetupd.proximityrepair.authkit.xpc")
+			(global-name "com.apple.appleidsetupd.proximityrepair.xpc")
+		))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.absd"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))

 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.ak.signinwithapple.xpc"))
 		(require-not (global-name "com.apple.appstorecomponentsd.xpc"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))
 		(require-not (global-name "com.apple.absinthed"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))

 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.devicecheckd"))
-		(require-not (require-any
-			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate")
-			(global-name "com.apple.ak.shieldservices.xpc")
-		))
+		(require-not (xpc-service-name "com.apple.SafariFoundation.CredentialProviderExtensionHelper"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.odi.legacySPIService"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
-		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (xpc-service-name "com.apple.SafariFoundation.CredentialProviderExtensionHelper"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
