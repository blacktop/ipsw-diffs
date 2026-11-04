## com.apple.WebKit.Networking

> Group: ⬆️ Updated

```diff

 (version 1)
 (deny default)
 
+(deny asr-parser-enter)
+(allow asr-parser-enter
+	(require-any
+		(asr-parser-name "com.apple.imageio.png")
+		(require-not (asr-parser-domain ASR_DOMAIN_IMAGES))
+	)
+)
+
 (deny darwin-notification-post)
 (allow darwin-notification-post
 	(require-any

 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
 		(require-any
+			(extension "com.apple.app-sandbox.read")
 			(extension "com.apple.app-sandbox.read-write")
 			(extension "com.apple.sandbox.executable")
 			(subpath "/Library/RegionFeatures")

 			(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
+				(require-any
+					(literal "/private/var/preferences/com.apple.networkextension.plist")
+					(require-all
+						(require-any
+							(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+							(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+						)
+						(extension "com.apple.sandbox.container")
+						(require-not (process-attribute is-apple-signed-executable))
+					)
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+				)
+				(extension "com.apple.sandbox.container")
+				(require-not (process-attribute is-apple-signed-executable))
 			)
 			(require-any
 				(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")

 			(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
+				(require-any
+					(literal "/private/var/preferences/com.apple.networkextension.plist")
+					(require-all
+						(require-any
+							(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+							(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+						)
+						(extension "com.apple.sandbox.container")
+						(require-not (process-attribute is-apple-signed-executable))
+					)
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+				)
+				(extension "com.apple.sandbox.container")
+				(require-not (process-attribute is-apple-signed-executable))
 			)
 			(require-any
 				(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")

 (allow file-write*
 	(extension "com.apple.app-sandbox.read-write")
 )
+(allow file-write*
+	(require-all
+		(require-any
+			(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+			(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+		)
+		(extension "com.apple.sandbox.container")
+		(require-not (process-attribute is-apple-signed-executable))
+	)
+)
 
 (allow file-write-create
-	(extension "com.apple.app-sandbox.read-write")
-)
-(deny file-write-create
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
+		(require-not (vnode-type SYMLINK))
+		(require-not (literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*"))
 		(require-any
-			(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
-			(vnode-type SYMLINK)
+			(extension "com.apple.app-sandbox.read-write")
+			(require-all
+				(require-any
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+					(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+				)
+				(extension "com.apple.sandbox.container")
+				(require-not (process-attribute is-apple-signed-executable))
+			)
 		)
 	)
 )
 
+(allow file-write-data
+	(require-all
+		(require-any
+			(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/Library/Caches")
+			(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
+		)
+		(extension "com.apple.sandbox.container")
+		(require-not (process-attribute is-apple-signed-executable))
+	)
+)
 (allow file-write-data
 	(require-any
 		(extension "com.apple.app-sandbox.read-write")

 
 (allow sysctl-read
 	(require-all
+		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
 		(require-any
 			(sysctl-name "kern.proc.*")
 			(sysctl-name "kern.procargs2.*")
 		)
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
 	)
 )
 (allow sysctl-read
```
