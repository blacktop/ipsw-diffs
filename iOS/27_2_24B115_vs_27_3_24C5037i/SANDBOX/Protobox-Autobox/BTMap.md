## BTMap

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.dmd.emergency-mode"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.SocialHighlight"))
 		(require-not (global-name "com.apple.geod"))

 		(require-not (global-name "com.apple.synapse.backlink-service"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.awdd"))
-		(require-not (xpc-service-name "com.apple.AudioAccessoryAssetManagementXPCService"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
 		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.private"))

 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (xpc-service-name "com.apple.imdpersistence.IMDPersistenceAgent"))
+		(require-not (xpc-service-name "com.apple.AudioAccessoryAssetManagementXPCService"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
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
