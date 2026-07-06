## identityservicesd

> Group: ⬆️ Updated

```diff

 		(subpath "${HOME}/Library/IdentityServices")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.identityservicesd")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.nsurlsessiond.readonly")

 )
 (allow file-issue-extension
 	(require-all
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.identityservicesd")
-			(subpath "/private/var/tmp/com.apple.identityservicesd")
-		)
+		(subpath "/private/var/tmp/com.apple.identityservicesd")
 		(require-any
 			(extension-class "com.apple.aned.read-only")
 			(extension-class "com.apple.app-sandbox.read")

 		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+		(literal "/private/var/db/com.apple.countryd/countryCodeCache.plist")
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(literal "/private/var/preferences/SystemConfiguration/com.apple.radios.plist")
 		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")

 		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+		(literal "/private/var/db/com.apple.countryd/countryCodeCache.plist")
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(literal "/private/var/preferences/SystemConfiguration/com.apple.radios.plist")
 		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")

 	(require-all
 		(require-not (sysctl-name "net.link.generic.system.flow_key_trace"))
 		(require-any
+			(require-any
+				(sysctl-name "kern.nisdomainname")
+				(sysctl-name "net.statistics")
+			)
 			(sysctl-name "kern.ipc.maxsockbuf")
-			(sysctl-name "kern.nisdomainname")
 			(sysctl-name "net.routetable.*")
-			(sysctl-name "net.statistics")
 		)
 	)
 )
```
