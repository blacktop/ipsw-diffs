## com.apple.WebKit.WebContent.Development

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

 		(literal "${HOME}/Library/Preferences/com.apple.voiceservices.logging.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.voiceservices.plist")
 		(literal "/dev/null")
+		(literal "/dev/random")
+		(literal "/dev/urandom")
 		(literal "/dev/zero")
 		(literal "/private/etc/fstab")
 		(literal "/private/etc/group")

 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/preboot/Cryptexes/OS/System/Library")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
 		(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")

 		(literal "${HOME}/Library/Preferences/com.apple.voiceservices.logging.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.voiceservices.plist")
 		(literal "/dev/null")
+		(literal "/dev/random")
+		(literal "/dev/urandom")
 		(literal "/dev/zero")
 		(literal "/private/etc/fstab")
 		(literal "/private/etc/group")

 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/preboot/Cryptexes/OS/System/Library")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
 		(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")

 
 (allow file-write-data
 	(with report)
-	(require-any
-		(extension "com.apple.app-sandbox.read-write")
-		(literal "/dev/null")
-		(literal "/dev/zero")
+	(extension "com.apple.app-sandbox.read-write")
+)
+(allow file-write-data
+	(with report)
+	(require-all
+		(require-any
+			(literal "/dev/null")
+			(literal "/dev/zero")
+		)
+		(require-not (literal "/dev/dtracehelper"))
 	)
 )
 

 )
 (allow syscall-unix
 	(require-all
-		(syscall-number SYS_kdebug_trace_string SYS_kdebug_typefilter)
+		(syscall-number SYS_kdebug_trace64 SYS_kdebug_typefilter)
 		(system-attribute developer-mode)
 	)
 )

 )
 (allow syscall-unix
 	(require-all
-		(syscall-number SYS_kdebug_trace64)
+		(syscall-number SYS_kdebug_trace_string)
 		(require-any
 			(require-not (state-flag "local:WebContentProcessLaunched"))
 			(system-attribute developer-mode)
```
