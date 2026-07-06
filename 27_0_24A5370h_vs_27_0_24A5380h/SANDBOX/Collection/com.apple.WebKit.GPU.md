## com.apple.WebKit.GPU

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
+		(extension-class "com.apple.mediaserverd.read")
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.sharing.airdrop.readonly")
 		(require-any
 			(extension "com.apple.app-sandbox.read")
 			(extension "com.apple.app-sandbox.read-write")
 			(extension "com.apple.sharing.airdrop.readonly")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(extension "com.apple.assets.read")
-						(require-any
-							(subpath "${HOME}/Library/Assets")
-							(subpath "/private/var/MobileAsset")
-						)
-					)
-					(subpath "/System/Cryptexes/OS/System/Library")
-					(subpath "/System/Library")
-					(subpath "/private/preboot/Cryptexes/OS/System/Library")
-				)
-			)
 		)
 	)
 )

 		(require-not (literal "${HOME}/Library/Preferences/com.apple.mobilemail.plist"))
 		(require-any
 			(literal "/dev/dtracehelper")
+			(literal "/dev/random")
+			(literal "/dev/urandom")
 			(literal "/private/etc/passwd")
 			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
 			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")

 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/preboot/Cryptexes/OS/System/Library")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")

 				(require-not (literal "${HOME}/Library/Preferences/com.apple.mobilemail.plist"))
 				(require-any
 					(literal "/dev/dtracehelper")
+					(literal "/dev/random")
+					(literal "/dev/urandom")
 					(literal "/private/etc/passwd")
 					(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
 					(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")

 				(subpath "/Library/CoreMediaIO/Plug-Ins/DAL")
 				(require-any
 					(extension "com.apple.webkit.camera")
-					(require-all
-						(require-not (literal "${HOME}/Library/Preferences/com.apple.mobilemail.plist"))
-						(require-any
-							(literal "/dev/dtracehelper")
-							(literal "/private/etc/passwd")
-							(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
-							(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-							(literal "/private/var/preferences/com.apple.networkd.plist")
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
-									(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-								)
-							)
-							(require-any
-								(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
-							)
-							(require-any
-								(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-								(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
-								(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-							)
-							(require-any
-								(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
-								(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
-							)
-							(subpath "/")
-							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
-						)
-					)
+					(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
 				)
 			)
 			(require-any

 			(subpath "${HOME}/Library/Fonts")
 			(subpath "/Library/RegionFeatures")
 			(subpath "/System/Library")
-			(subpath "/private/preboot/Cryptexes/OS/System/Library")
 			(subpath "/private/var/db/timezone")
 			(subpath "/private/var/preferences/Logging")
 			(subpath "/usr/lib")

 	(require-all
 		(require-not (xpc-service-name "com.apple.audio.toolbox.reporting.service"))
 		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-any
 			(global-name "com.apple.audio.AudioQueueServer")
 			(global-name "com.apple.logd")
```
