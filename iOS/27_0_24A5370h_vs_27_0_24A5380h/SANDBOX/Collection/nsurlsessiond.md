## nsurlsessiond

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.nsurlsessiond")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.nsurlsessiond")
-			(subpath "/private/var/tmp/com.apple.nsurlsessiond")
-		)
+		(subpath "/private/var/tmp/com.apple.nsurlsessiond")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.nsurlsessiond")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.nsurlsessiond")
-			(subpath "/private/var/tmp/com.apple.nsurlsessiond")
-		)
+		(subpath "/private/var/tmp/com.apple.nsurlsessiond")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(subpath "/private/var/tmp/com.apple.nsurlsessiond")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "/private/var/tmp/com.apple.nsurlsessiond")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.nsurlsessiond")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.nsurlsessiond")
-			(subpath "/private/var/tmp/com.apple.nsurlsessiond")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.nsurlsessiond")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.nsurlsessiond")
-			(subpath "/private/var/tmp/com.apple.nsurlsessiond")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(require-any
-			(extension-class "com.apple.STExtractionService")
-			(extension-class "com.apple.StreamingUnzipService")
-		)
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.nsurlsessiond*")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/Library/Caches/com.apple.nsurlsessiond*")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/Library/com.apple.UserManagedAssets*")
-			(subpath "/private/var/MobileAsset/AssetsV2/downloadDir")
-			(subpath "/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/downloadDir")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(subpath "${HOME}")
-						(require-any
-							(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Media/([^/]+/)?(Downloads|MotionAssets)(/|$)|^/private/var/(mobile|euser[0-9]+)/Media/([^/]+/)?(Managed)?Purchases(/|$))|^/private/var/[-0-9A-F]+/Media/([^/]+/)?(Downloads|MotionAssets)(/|$))|^/private/var/[-0-9A-F]+/Media/([^/]+/)?(Managed)?Purchases(/|$))|^/private/var/Users/[^/]+/Media/([^/]+/)?(Downloads|MotionAssets)(/|$))|^/private/var/Users/[^/]+/Media/([^/]+/)?(Managed)?Purchases(/|$))")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?Music/(Cache|Downloads)(/|$)")
-							(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond")
-						)
-					)
-					(require-any
-						(literal "${FRONT_USER_HOME}/tmp/AirTraffic*")
-						(literal "/private/var/tmp/AirTraffic*")
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond")
-				)
-			)
 			(require-any
 				(subpath "${HOME}/Library/HTTPStorages/com.apple.nsurlsessiond")
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.nsurlsessiond")
-				(subpath "/private/var/tmp/com.apple.nsurlsessiond")
 			)
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond")
+			(subpath "/private/var/tmp/com.apple.nsurlsessiond")
 		)
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(extension-class "com.apple.STExtractionService")
+			(extension-class "com.apple.StreamingUnzipService")
+		)
 		(require-any
 			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/com.apple.UserManagedAssets*")
 			(require-all

 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?Music/(Cache|Downloads)(/|$)")
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Caches/com\.apple\.nsurlsessiond")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Cookies/[^/]+\.binarycookies(([^/])*\.dat)?$")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")

 					)
 				)
 			)
+			(subpath "/private/var/tmp/com.apple.nsurlsessiond")
 		)
 	)
 )

 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?Music/(Cache|Downloads)(/|$)")
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Caches/com\.apple\.nsurlsessiond")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Cookies/[^/]+\.binarycookies(([^/])*\.dat)?$")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")

 				(subpath "${FRONT_USER_HOME}")
 				(require-any
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library$|/Library/Caches$)")
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library$|/Library/Caches$)")
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library$|/Library/Caches$)")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library$|/Library/Caches$)")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library$|/Library/Caches$)")
-					)
+					(subpath "/private/var/tmp/com.apple.nsurlsessiond")
 				)
 			)
 			(require-all

 						(subpath "${FRONT_USER_HOME}")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library$|/Library/Caches$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library$|/Library/Caches$)")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library$|/Library/Caches$)")
-									)
-								)
-							)
+							(subpath "/private/var/tmp/com.apple.nsurlsessiond")
 						)
 					)
 				)
 			)
+			(subpath "/private/var/tmp/com.apple.nsurlsessiond")
 		)
 	)
 )

 					)
 					(require-all
 						(vnode-type DIRECTORY)
+						(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
+					)
+					(require-all
+						(vnode-type REGULAR-FILE)
 						(require-any
 							(require-all
 								(subpath "/private/var/PersonaVolumes")

 							(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
 						)
 					)
-					(require-all
-						(vnode-type REGULAR-FILE)
-						(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
-					)
 				)
 			)
 			(require-all

 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?Music/(Cache|Downloads)(/|$)")
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Caches/com\.apple\.nsurlsessiond")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Cookies/[^/]+\.binarycookies(([^/])*\.dat)?$")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")

 					)
 					(require-all
 						(vnode-type DIRECTORY)
+						(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
+					)
+					(require-all
+						(vnode-type REGULAR-FILE)
 						(require-any
 							(require-all
 								(subpath "/private/var/PersonaVolumes")

 							(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
 						)
 					)
-					(require-all
-						(vnode-type REGULAR-FILE)
-						(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
-					)
 				)
 			)
 			(require-all

 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?Music/(Cache|Downloads)(/|$)")
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Caches/com\.apple\.nsurlsessiond")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Cookies/[^/]+\.binarycookies(([^/])*\.dat)?$")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")

 					)
 					(require-all
 						(vnode-type DIRECTORY)
+						(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
+					)
+					(require-all
+						(vnode-type REGULAR-FILE)
 						(require-any
 							(require-all
 								(subpath "/private/var/PersonaVolumes")

 							(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
 						)
 					)
-					(require-all
-						(vnode-type REGULAR-FILE)
-						(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nsurlsessiond")
-					)
 				)
 			)
 			(require-all

 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?Music/(Cache|Downloads)(/|$)")
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Caches/com\.apple\.nsurlsessiond")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/Library/Cookies/[^/]+\.binarycookies(([^/])*\.dat)?$")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
```
