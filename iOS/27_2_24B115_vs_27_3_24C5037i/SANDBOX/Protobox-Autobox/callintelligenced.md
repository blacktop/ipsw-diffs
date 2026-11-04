## callintelligenced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.SocialHighlight"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.siri.activation.service"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.TextUnderstanding.process"))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
