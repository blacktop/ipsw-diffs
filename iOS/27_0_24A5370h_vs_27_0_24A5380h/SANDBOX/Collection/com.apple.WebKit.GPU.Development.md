## com.apple.WebKit.GPU.Development

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

 		(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
 		(literal "/dev/dtracehelper")
+		(literal "/dev/random")
+		(literal "/dev/urandom")
 		(literal "/private/etc/passwd")
 		(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")

 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/preboot/Cryptexes/OS/System/Library")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
 		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
```
