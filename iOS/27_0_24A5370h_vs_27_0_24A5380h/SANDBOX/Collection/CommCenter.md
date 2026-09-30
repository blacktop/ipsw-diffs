## CommCenter

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${HOME}/Library/Caches/CommCenterClassic")
 			(subpath "${HOME}/Library/Caches/com.apple.CommCenter")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(subpath "${HOME}/Library/Caches/CommCenterClassic")
 			(subpath "${HOME}/Library/Caches/com.apple.CommCenter")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
+				(extension "com.apple.assets.read")
 				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
 			(require-all
 				(subpath "/Library/Ringtones")
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
 			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/CommCenterClassic")

 		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(literal "/private/var/db/os_eligibility/eligibility.plist")
 		(literal "/private/var/installd/Library/MobileInstallation/MigrationInfo.plist")
-		(literal "/private/var/preferences/SystemConfiguration/com.apple.eapol.sim.generation.plist")
 		(literal "/private/var/preferences/SystemConfiguration/com.apple.radios.plist")
 		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(literal "/private/var/preferences/com.apple.networkd.plist")

 		(subpath "${PROCESS_TEMP_DIR}")
 		(subpath "/Library/Ringtones")
 		(subpath "/private/preboot")
-		(subpath "/private/var/Managed Preferences/mobile/com.apple.managedCarrier.plist${FRONT_USER_HOME}/Library/CountryBundles")
 		(subpath "/private/var/db/com.apple.countryd")
 		(subpath "/private/var/hardware/FactoryData")
 		(subpath "/private/var/logs/BBUpdater")
 		(subpath "/private/var/logs/WirelessLibraryLogs")
+		(subpath "/private/var/preferences/SystemConfiguration/com.apple.eapol.sim.generation.plist${FRONT_USER_HOME}/Library/CountryBundles")
 		(subpath "/private/var/tmp")
 		(subpath "/private/var/wireless")
-		(subpath "/private/var/wireless/Library/Images")
 		(subpath "/usr/local/standalone/firmware/Baseband")
 		(subpath "/usr/sbin")
 	)

 		(extension "com.apple.identityservices.deliver")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")
 		(require-any
-			(literal "/private/var/preferences/SystemConfiguration/com.apple.eapol.sim.generation.plist")
-			(literal "/private/var/preferences/SystemConfiguration/com.apple.radios.plist")
-			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 			(require-all
 				(regex #"((((((((((^/private/var/(mobile|euser[0-9]+)(/Library((((/CallHistory)?|/(Carrier|Operator) Bundle.bundle)|/Voicemail)|/Preferences))?$|^/private/var/[-0-9A-F]+/Library(/CallHistory)?$)|^/private/var/[-0-9A-F]+/Library/(Carrier|Operator) Bundle.bundle$)|^/private/var/[-0-9A-F]+/Library/Voicemail$)|^/private/var/[-0-9A-F]+/Library/Preferences$)|^/private/var/[-0-9A-F]+$)|^/private/var/Users/[^/]+/Library(/CallHistory)?$)|^/private/var/Users/[^/]+/Library/(Carrier|Operator) Bundle.bundle$)|^/private/var/Users/[^/]+/Library/Voicemail$)|^/private/var/Users/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+$)")
 				(subpath "${FRONT_USER_HOME}")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 		(literal "${HOME}/Library/Preferences")
 		(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
 		(literal "/dev/cu.debug")
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(literal "/private/var/db/os_eligibility/eligibility.plist")
 		(literal "/private/var/installd/Library/MobileInstallation/MigrationInfo.plist")
+		(literal "/private/var/preferences/SystemConfiguration/com.apple.radios.plist")
 		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/private/var/preferences/com.apple.networkextension*")
 		(literal "/private/var/preferences/com.apple.security.plist")
 		(literal "/usr/local/lib/CarrierBundleDevKey.dylib")

 		(subpath "${PROCESS_TEMP_DIR}")
 		(subpath "/Library/Ringtones")
 		(subpath "/private/preboot")
-		(subpath "/private/var/Managed Preferences/mobile/com.apple.managedCarrier.plist${FRONT_USER_HOME}/Library/CountryBundles")
 		(subpath "/private/var/db/com.apple.countryd")
 		(subpath "/private/var/hardware/FactoryData")
 		(subpath "/private/var/logs/BBUpdater")
 		(subpath "/private/var/logs/WirelessLibraryLogs")
+		(subpath "/private/var/preferences/SystemConfiguration/com.apple.eapol.sim.generation.plist${FRONT_USER_HOME}/Library/CountryBundles")
 		(subpath "/private/var/tmp")
 		(subpath "/private/var/wireless")
 		(subpath "/private/var/wireless/Library/Images")
```
