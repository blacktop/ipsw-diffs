## MobileSlideShow

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Media/Debug")
+		(extension-class "com.apple.app-sandbox.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.quicklook.readonly")
-		(subpath "/private/var/tmp")
+		(subpath "${PROCESS_TEMP_DIR}")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+			(literal "${HOME}/Library/SpringBoard")
+			(subpath "${PROCESS_TEMP_DIR}")
+			(subpath "/private/var/MobileAsset/Assets")
+			(subpath "/private/var/tmp")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
+		)
 	)
 )
 (allow file-issue-extension

 						(subpath "/private/var")
 						(require-any
 							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								(subpath "${FRONT_USER_HOME}")
 								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
 										(require-any
 											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(subpath "${HOME}/Library/Cookies")
+											(require-all
+												(subpath "${FRONT_USER_HOME}")
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(subpath "${HOME}/Library/Cookies")
+												)
+											)
 										)
 									)
-									(subpath "${FRONT_USER_HOME}")
 								)
 							)
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
+								(subpath "/private/var/PersonaVolumes")
 								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 									(require-all
-										(subpath "/private/var/PersonaVolumes")
+										(subpath "${FRONT_USER_HOME}")
 										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 											(subpath "${HOME}/Library/Cookies")
 										)
 									)

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(subpath "/private/var/tmp")
-		(extension-class "com.apple.app-sandbox.read-write")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Media/Debug")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.quicklook.readonly")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension "com.apple.sandbox.application-group")
+						(require-any
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									)
+								)
+							)
+						)
+					)
+					(subpath "${HOME}/Library/Cookies")
+				)
+			)
+			(subpath "${HOME}/Library/Cookies")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension "com.apple.sandbox.executable")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Media/PhotoData")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(require-all
+				(subpath "/Library/Ringtones")
+				(extension-class "com.apple.aned.read-only")
+			)
+			(require-all
+				(subpath "/private/var")
+				(subpath "${HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Ringtones.plist$")
+				)
+			)
+			(subpath "${HOME}/Media/Purchases")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.sharing.airdrop.readonly")
+		(subpath "${HOME}/Media")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/MediaCache")
+			(subpath "/private/var/tmp/MediaCache")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Media/Photos")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Media/Purchases")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Media/DCIM")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Media/MediaAnalysis")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Media/Memories")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "${HOME}/Media/Purchases")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 								(require-any
 									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}/Media/DCIM")
+									(subpath "${HOME}/Media/Photos")
 								)
 							)
-							(subpath "${HOME}/Media/DCIM")
+							(subpath "${HOME}/Media/Photos")
 						)
 					)
 					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "${HOME}/Media/DCIM")
+					(subpath "${HOME}/Media/Photos")
 					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
 				)

 				(require-any
 					(require-all
 						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}/Media/Memories")
+								)
+							)
+							(subpath "${HOME}/Media/Memories")
+						)
 					)
+					(subpath "${HOME}/Media/Memories")
 					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 				)
 			)

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Media/Debug")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
 		(subpath "${HOME}/Library/Cookies")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.quicklook.readonly")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
-			)
-			(subpath "${HOME}/Library/Cookies")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/Cookies")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.application-group")
-						(require-any
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(subpath "${HOME}/Library/Cookies")
-														)
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(subpath "${HOME}/Library/Cookies")
-										)
-									)
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(subpath "${HOME}/Library/Cookies")
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-					(subpath "${HOME}/Library/Cookies")
-				)
-			)
-			(subpath "${HOME}/Library/Cookies")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/MediaCache")
-			(subpath "/private/var/tmp/MediaCache")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(subpath "${HOME}/Library/Cookies")
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-					(subpath "${HOME}/Library/Cookies")
-				)
-			)
-			(subpath "${HOME}/Library/Cookies")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
-		(extension "com.apple.sandbox.executable")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Media/Debug")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(extension-class "com.apple.mediaserverd.read-write")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
-		(subpath "${HOME}/Media")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(subpath "/Library/Ringtones")
-				(extension-class "com.apple.mediaserverd.read")
-			)
-			(require-all
-				(subpath "/private/var")
-				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Ringtones.plist$")
-				)
-			)
-			(subpath "${HOME}/Media/Purchases")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Media/Purchases")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(subpath "${HOME}/Media/PhotoData")
-		(extension-class "com.apple.mediaserverd.read-write")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(subpath "${HOME}/Media/Memories")
-		(extension-class "com.apple.mediaserverd.read-write")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Media/Purchases")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(subpath "${HOME}/Media/DCIM")
-		(extension-class "com.apple.mediaserverd.read-write")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
-			(literal "${HOME}/Library/SpringBoard")
-			(subpath "${PROCESS_TEMP_DIR}")
-			(subpath "/private/var/MobileAsset/AssetsV2")
-			(subpath "/private/var/tmp")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.camera")
-			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.spotlight-indexable")
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(require-all
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-				)
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
+			(extension-class "com.apple.aned.read-only")
+			(extension-class "com.apple.app-sandbox.read")
+			(extension-class "com.apple.app-sandbox.read-write")
+			(extension-class "com.apple.mediaserverd.read")
+			(extension-class "com.apple.mediaserverd.read-write")
 		)
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(subpath "${HOME}/Media/PhotoStreamsData")
+		(extension-class "com.apple.sharing.airdrop.readonly")
 		(require-any
-			(extension-class "com.apple.aned.read-only")
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.mediaserverd.read")
+			(subpath "${PROCESS_TEMP_DIR}")
+			(subpath "/private/var/tmp")
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(require-any
+					(extension "com.apple.security.exception.files.absolute-path.read-write")
+					(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(subpath "${HOME}/Library/Cookies")
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(subpath "${HOME}/Library/Cookies")
+								)
+							)
+						)
+					)
+					(subpath "${HOME}/Library/Cookies")
+				)
+			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(subpath "${HOME}/Library/Cookies")
+						)
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(subpath "${HOME}/Library/Cookies")
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.wcd.readonly")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
 			(require-all

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.wcd.readonly")
+		(extension-class "com.apple.sharing.airdrop.readonly")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
 			(require-all

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(subpath "${HOME}/Library/Cookies")
-		(require-any
-			(extension-class "com.apple.aned.read-only")
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.app-sandbox.read-write")
-			(extension-class "com.apple.mediaserverd.read")
-			(extension-class "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(subpath "${PROCESS_TEMP_DIR}")
-		(require-any
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.app-sandbox.read-write")
-			(extension-class "com.apple.mediaserverd.read")
-			(extension-class "com.apple.mediaserverd.read-write")
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.quicklook.readonly")

 )
 (allow file-issue-extension
 	(require-all
-		(subpath "${HOME}/Media/Photos")
+		(extension-class "com.apple.spotlight-indexable")
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.camera")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileslideshow")
+		)
 		(require-any
 			(extension-class "com.apple.mediaserverd.read")
 			(extension-class "com.apple.mediaserverd.read-write")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
+		(subpath "/private/var/tmp")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}")
-			(subpath "/private/var/tmp")
+			(extension-class "com.apple.app-sandbox.read")
+			(extension-class "com.apple.app-sandbox.read-write")
+			(extension-class "com.apple.mediaserverd.read")
+			(extension-class "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Media/Debug")
+		(require-any
+			(extension-class "com.apple.mediaserverd.read")
+			(extension-class "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Media/PhotoStreamsData")
+		(require-any
+			(extension-class "com.apple.aned.read-only")
+			(extension-class "com.apple.app-sandbox.read")
+			(extension-class "com.apple.mediaserverd.read")
 		)
 	)
 )

 					(require-all
 						(extension-class "com.apple.aned.read-only")
 						(require-any
-							(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+							(require-all
+								(process-attribute is-apple-signed-executable)
+								(require-any
+									(require-all
+										(extension-class "com.apple.mediaserverd.read")
+										(extension "com.apple.sandbox.executable")
+									)
+									(require-all
+										(extension-class "com.apple.webkit.map-executable")
+										(extension "com.apple.sandbox.executable")
+									)
+								)
+							)
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(require-all
+										(process-attribute is-apple-signed-executable)
+										(require-any
+											(require-all
+												(extension-class "com.apple.mediaserverd.read")
+												(extension "com.apple.sandbox.executable")
+											)
+											(require-all
+												(extension-class "com.apple.webkit.map-executable")
+												(extension "com.apple.sandbox.executable")
+											)
+										)
+									)
+									(require-all
+										(subpath "/private/var")
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
+											(require-all
+												(process-attribute is-apple-signed-executable)
+												(require-any
+													(require-all
+														(extension-class "com.apple.mediaserverd.read")
+														(extension "com.apple.sandbox.executable")
+													)
+													(require-all
+														(extension-class "com.apple.webkit.map-executable")
+														(extension "com.apple.sandbox.executable")
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+							(require-any
+								(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+							)
 						)
 					)
 					(require-all

 					(require-all
 						(extension-class "com.apple.mediaserverd.read")
 						(require-any
-							(require-all
-								(process-attribute is-apple-signed-executable)
-								(require-any
-									(require-all
-										(extension-class "com.apple.quicklook.readonly")
-										(extension "com.apple.sandbox.executable")
-									)
-									(require-all
-										(extension-class "com.apple.webkit.map-executable")
-										(extension "com.apple.sandbox.executable")
-									)
-								)
-							)
-							(require-all
-								(subpath "/private/var")
-								(require-any
-									(require-all
-										(process-attribute is-apple-signed-executable)
-										(require-any
-											(require-all
-												(extension-class "com.apple.quicklook.readonly")
-												(extension "com.apple.sandbox.executable")
-											)
-											(require-all
-												(extension-class "com.apple.webkit.map-executable")
-												(extension "com.apple.sandbox.executable")
-											)
-										)
-									)
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-											(require-all
-												(process-attribute is-apple-signed-executable)
-												(require-any
-													(require-all
-														(extension-class "com.apple.quicklook.readonly")
-														(extension "com.apple.sandbox.executable")
-													)
-													(require-all
-														(extension-class "com.apple.webkit.map-executable")
-														(extension "com.apple.sandbox.executable")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-							(require-any
-								(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
-							)
+							(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
 						)
 					)
 					(require-all
 						(process-attribute is-apple-signed-executable)
 						(require-any
 							(require-all
-								(extension-class "com.apple.quicklook.readonly")
+								(extension-class "com.apple.mediaserverd.read")
 								(extension "com.apple.sandbox.executable")
 							)
 							(require-all

 							)
 							(require-all
 								(extension-class "com.apple.spotlight-indexable")
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+									)
+								)
+							)
+							(require-all
+								(extension-class "com.apple.wcd.readonly")
 								(require-any
 									(require-all
 										(require-any

 									)
 								)
 							)
-							(require-all
-								(extension-class "com.apple.wcd.readonly")
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
 						)
 					)
 				)

 				(process-attribute is-apple-signed-executable)
 				(require-any
 					(require-all
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read")
 						(extension "com.apple.sandbox.executable")
 					)
 					(require-all

 			(extension-class "com.apple.mediaserverd.read")
 			(extension-class "com.apple.quicklook.readonly")
 			(extension-class "com.apple.sharing.airdrop.readonly")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
+			)
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(extension-class "com.apple.quicklook.readonly")
+					(extension-class "com.apple.app-sandbox.read")
 					(require-all
 						(extension-class "com.apple.app-sandbox.read-write")
 						(require-any

 							(require-all
 								(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
 								(require-any
+									(extension-class "com.apple.app-sandbox.read")
 									(extension-class "com.apple.app-sandbox.read-write")
-									(extension-class "com.apple.quicklook.readonly")
 								)
 							)
 						)

 									(require-all
 										(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
 										(require-any
+											(extension-class "com.apple.app-sandbox.read")
 											(extension-class "com.apple.app-sandbox.read-write")
-											(extension-class "com.apple.quicklook.readonly")
 										)
 									)
 								)

 					)
 				)
 			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 		)
 	)

 
 (allow file-map-executable
 	(require-all
-		(signing-identifier "com.apple.mobileslideshow")
+		(signing-identifier "com.apple.camera")
 		(%entitlement-is-bool-true "get-task-allow")
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 )
 (allow file-map-executable
 	(require-all
-		(signing-identifier "com.apple.camera")
+		(signing-identifier "com.apple.mobileslideshow")
 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")

 		(extension "com.apple.sandbox.container")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/Snapshots")

 		(extension "com.apple.sandbox.container")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/Snapshots")

 			(require-all
 				(extension "com.apple.sandbox.oopjit")
 				(subpath "/private/var/OOPJit")
-				(require-any
-					(extension "com.apple.app-sandbox.read")
-					(extension "com.apple.app-sandbox.read-write")
-				)
+				(extension "com.apple.app-sandbox.read")
 			)
 		)
 	)

 )
 
 (define (_g0 _)
-	(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist"))
+	(require-any
+	(literal "${HOME}/Library/Logs/MobileSlideShow.log")
+	(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
+	(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
+	(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
+	(subpath "${HOME}/Library/Application Support/MobileSlideShow")
+	(subpath "${HOME}/Library/Application Support/iLifePageLayout")
+	(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
+	(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
+	(subpath "${HOME}/Library/Siri")
+))
 (define (_g1 _)
-	(literal "/AppleInternal/Library/Preferences/com.apple.airplay.dashboard.plist"))
+	(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache"))
 (define (_g2 _)
-	(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist"))
+	(require-any
+	(literal "${HOME}/Library/Logs/MobileSlideShow.log")
+	(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
+	(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
+	(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
+	(subpath "${HOME}/Library/Application Support/MobileSlideShow")
+	(subpath "${HOME}/Library/Application Support/iLifePageLayout")
+	(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
+	(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
+	(subpath "${HOME}/Library/Siri")
+))
 (define (_g3 _)
-	(literal "/AppleInternal/Library/Preferences/com.apple.airplay.dashboard.plist"))
+	(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache"))
 (define (_g4 _)
-	(literal "${HOME}/Library/SpringBoard"))
+	(require-any
+	(literal "${HOME}/Library/Logs/MobileSlideShow.log")
+	(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
+	(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
+	(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
+	(subpath "${HOME}/Library/Application Support/MobileSlideShow")
+	(subpath "${HOME}/Library/Application Support/iLifePageLayout")
+	(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
+	(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
+	(subpath "${HOME}/Library/Siri")
+))
 (define (_g5 _)
-	(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist"))
+	(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache"))
 (define (_g6 _)
-	(literal "/private/var/preferences/com.apple.networkd.plist"))
+	(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist"))
 (define (_g7 _)
 	(require-all
 	(extension "com.apple.sandbox.application-group")

 	)
 ))
 (define (_g8 _)
-	(literal "/AppleInternal/Library/Preferences/com.apple.airplay.dashboard.plist"))
-(define (_g9 _)
 	(require-all
 	(signing-identifier "com.apple.camera.lockscreen")
 	(require-any
-		(_g8 "")
+		(_g4 "")
 		(require-all
 			(extension "com.apple.sandbox.container")
 			(require-any
-				(_g8 "")
+				(_g4 "")
 				(require-all
 					(subpath "/private/var")
 					(require-any

 		)
 	)
 ))
-(define (_g10 _)
+(define (_g9 _)
 	(require-all
 	(require-any
-		(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-		(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-		(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+		(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+		(subpath "/private/var/.DocumentRevisions-V100/staging")
+		(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 	)
 	(require-any
-		(_g9 "")
-		(extension "com.apple.revisiond.revision")
+		(_g8 "")
+		(extension "com.apple.revisiond.staging")
 	)
 ))
+(define (_g10 _)
+	(require-any
+	(_g9 "")
+	(extension "com.apple.revisiond.revision")
+))
 (define (_g11 _)
-	(require-any
-	(_g10 "")
-	(extension "com.apple.revisiond.staging")
-))
-(define (_g12 _)
 	(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)"))
-(define (_g13 _)
+(define (_g12 _)
 	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/iTunes Library.itlp(/|$)"))
-(define (_g14 _)
+(define (_g13 _)
 	(require-all
 	(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 	(require-any

 		)
 	)
 ))
-(define (_g15 _)
+(define (_g14 _)
 	(require-all
-	(vnode-type REGULAR-FILE)
+	(vnode-type DIRECTORY)
 	(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.photos.peopleImageCache")
 ))
-(define (_g16 _)
+(define (_g15 _)
 	(require-all
 	(subpath "/private/var/PersonaVolumes")
 	(require-any
-		(_g15 "")
+		(_g14 "")
 		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 	)
 ))
-(define (_g17 _)
+(define (_g16 _)
 	(require-all
 	(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 	(require-any
-		(_g15 "")
+		(_g14 "")
 		(process-attribute is-apple-signed-executable)
 	)
 ))
-(define (_g18 _)
+(define (_g17 _)
 	(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin"))
-(define (_g19 _)
+(define (_g18 _)
 	(require-all
 	(subpath "/private/var")
 	(require-any
-		(_g18 "")
+		(_g17 "")
 		(require-all
 			(subpath "${HOME}")
 			(require-any
-				(_g18 "")
+				(_g17 "")
 				(require-all
 					(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 					(require-any
-						(_g18 "")
+						(_g17 "")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Artwork(/|$)")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 					)

 		)
 	)
 ))
-(define (_g20 _)
+(define (_g19 _)
 	(require-all
 	(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 ))
-(define (_g21 _)
+(define (_g20 _)
 	(require-all
 	(extension "com.apple.fileprovider.read-write")
 	(require-any
-		(_g20 "")
+		(_g19 "")
 		(require-all
 			(subpath "/private/var")
 			(require-any
-				(_g20 "")
+				(_g19 "")
 				(require-all
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 					(require-any
-						(_g20 "")
+						(_g19 "")
 						(subpath "${FRONT_USER_HOME}")
 					)
 				)

 		)
 	)
 ))
-(define (_g22 _)
+(define (_g21 _)
 	(require-all
 	(extension "com.apple.classkit.read-write")
 	(require-any
-		(_g21 "")
+		(_g20 "")
 		(require-all
-			(subpath "/private/var")
 			(require-any
-				(_g21 "")
+				(subpath "${FRONT_USER_HOME}")
+				(subpath "${HOME}")
+			)
+			(require-any
+				(_g20 "")
 				(require-all
+					(subpath "/private/var")
 					(require-any
-						(subpath "${FRONT_USER_HOME}")
-						(subpath "${HOME}")
-					)
-					(require-any
-						(_g21 "")
+						(_g20 "")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
 					)
 				)

 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
 	)
 ))
-(define (_g23 _)
-	(require-all
-	(extension "com.apple.assets.read")
-	(require-any
-		(_g22 "")
-		(subpath "${HOME}/Library/Assets")
-		(subpath "/private/var/MobileAsset")
-	)
-))
-(define (_g24 _)
+(define (_g22 _)
 	(require-all
 	(require-any
 		(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
 		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
 	)
 	(require-any
-		(_g23 "")
+		(_g21 "")
 		(extension "com.apple.odr-assets")
 	)
 ))
-(define (_g25 _)
+(define (_g23 _)
 	(require-all
 	(require-any
 		(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")

 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
 	)
 	(require-any
-		(_g24 "")
+		(_g22 "")
 		(extension "com.apple.librarian.ubiquity-revision")
 	)
 ))
+(define (_g24 _)
+	(require-all
+	(extension "com.apple.assets.read")
+	(require-any
+		(_g23 "")
+		(subpath "${HOME}/Library/Assets")
+		(subpath "/private/var/MobileAsset")
+	)
+))
+(define (_g25 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.Pasteboard")
+	(require-any
+		(_g24 "")
+		(extension "com.apple.Pasteboard-readonly")
+	)
+))
 (define (_g26 _)
 	(require-all
-	(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.Pasteboard")
+	(subpath "${HOME}/Library/ReplayKit")
 	(require-any
 		(_g25 "")
-		(extension "com.apple.Pasteboard-readonly")
+		(extension "com.apple.replayd.read-only")
 	)
 ))
 (define (_g27 _)
 	(require-all
-	(subpath "${HOME}/Library/ReplayKit")
+	(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 	(require-any
 		(_g26 "")
-		(extension "com.apple.replayd.read-only")
+		(process-attribute is-apple-signed-executable)
 	)
 ))
 (define (_g28 _)
 	(require-all
-	(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+	(%entitlement-is-present "com.apple.private.networkextension.configuration")
 	(require-any
-		(_g27 "")
-		(process-attribute is-apple-signed-executable)
+		(_g26 "")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
 	)
 ))
 (define (_g29 _)
-	(require-all
-	(%entitlement-is-present "com.apple.private.networkextension.configuration")
-	(require-any
-		(_g27 "")
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-	)
-))
-(define (_g30 _)
 	(require-all
 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
 	(extension "com.apple.clouddocs.version")
 ))
-(define (_g31 _)
+(define (_g30 _)
 	(require-all
 	(literal "/Library/Audio/Tunings/AID*")
 	(require-any
-		(_g30 "")
+		(_g29 "")
 		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
 	)
 ))
-(define (_g32 _)
+(define (_g31 _)
 	(require-all
 	(subpath "/System/Library/Carrier Bundles")
 	(require-any

 		(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 	)
 ))
-(define (_g33 _)
+(define (_g32 _)
 	(require-any
-	(_g32 "")
+	(_g31 "")
 	(extension "com.apple.clouddocs.version")
 ))
-(define (_g34 _)
+(define (_g33 _)
 	(require-all
 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
 	(require-any
-		(_g32 "")
+		(_g31 "")
 		(require-all
 			(vnode-type REGULAR-FILE)
-			(_g33 "")
+			(_g32 "")
 		)
 	)
 ))
-(define (_g35 _)
+(define (_g34 _)
 	(require-all
 	(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
 	(vnode-type REGULAR-FILE)
-	(_g33 "")
+	(_g32 "")
 ))
+(define (_g35 _)
+	(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist"))
 (define (_g36 _)
-	(literal "/private/var/preferences/com.apple.networkd.plist"))
-(define (_g37 _)
 	(require-all
 	(literal "${HOME}/Media/PhotoData/Photos.sqlite*")
 	(process-attribute is-platform-binary)
 	(extension "com.apple.tcc.kTCCServicePhotos")
 ))
-(define (_g38 _)
+(define (_g37 _)
 	(require-all
 	(extension "com.apple.tcc.kTCCServicePhotos")
 	(require-any
-		(_g37 "")
+		(_g36 "")
 		(literal "${HOME}/Media/PhotoData/syncInfo.plist")
 		(require-any
 			(subpath "${HOME}/Media/PhotoData/CPLAssets")

 		(subpath "${HOME}/Media/PhotoStreamsData")
 	)
 ))
+(define (_g38 _)
+	(subpath "${HOME}/Library/Fonts"))
 (define (_g39 _)
-	(require-all
-	(vnode-type REGULAR-FILE)
-	(require-any
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
-	)
-))
+	(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist"))
 (define (_g40 _)
-	(require-all
-	(subpath "${FRONT_USER_HOME}")
-	(require-any
-		(_g39 "")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-	)
-))
-(define (_g41 _)
 	(require-all
 	(subpath "${HOME}")
 	(require-any
-		(_g40 "")
+		(_g39 "")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/SyncedPreferences/com.apple.camera-.+\.plist")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/SyncedPreferences/com.apple.mobileslideshow-.+\.plist")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Ringtones.plist$")
 	)
 ))
+(define (_g41 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g40 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
+	)
+))
 (define (_g42 _)
-	(subpath "${HOME}/Library/Caches/Snapshots/com.apple.camera"))
+	(require-all
+	(extension "com.apple.security.exception.files.home-relative-path.read-write")
+	(extension "com.apple.app-sandbox.read")
+))
 (define (_g43 _)
-	(extension "com.apple.app-sandbox.read"))
-(define (_g44 _)
 	(require-all
 	(subpath "/private/var")
 	(require-any
-		(_g43 "")
+		(_g42 "")
 		(require-all
 			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
 			(require-any
-				(_g43 "")
+				(_g42 "")
 				(subpath "${FRONT_USER_HOME}")
 			)
 		)
 		(require-all
 			(subpath "${FRONT_USER_HOME}")
 			(require-any
-				(_g43 "")
+				(_g42 "")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
 			)
 		)
 	)
 ))
-(define (_g45 _)
+(define (_g44 _)
 	(require-all
 	(subpath "/System/Library/Carrier Bundles")
 	(require-any
-		(_g44 "")
+		(_g43 "")
 		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
 		(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 	)
 ))
-(define (_g46 _)
+(define (_g45 _)
 	(require-all
 	(subpath "${FRONT_USER_HOME}")
 	(require-any
-		(_g45 "")
+		(_g44 "")
 		(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
 	)
 ))
+(define (_g46 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes")
+	(require-any
+		(_g45 "")
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+	)
+))
 (define (_g47 _)
 	(require-all
-	(subpath "/private/var/PersonaVolumes")
+	(subpath "/private/var")
 	(require-any
-		(_g46 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+		(_g44 "")
+		(_g45 "")
 	)
 ))
 (define (_g48 _)
-	(require-all
-	(subpath "/private/var")
-	(require-any
-		(_g45 "")
-		(_g46 "")
-	)
-))
-(define (_g49 _)
-	(extension "com.apple.security.exception.files.absolute-path.read-only"))
+	(extension "com.apple.security.exception.files.absolute-path.read-write"))
 (allow file-read-data
 	(require-any
 	(require-all

 			(signing-identifier "com.apple.camera.lockscreen")
 			(signing-identifier "com.apple.photos.Memoryscape")
 		)
-		(vnode-type REGULAR-FILE)
+		(vnode-type SYMLINK)
 		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+			(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+			(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 		)
 		(require-any
-			(extension "com.apple.revisiond.staging")
+			(extension "com.apple.revisiond.revision")
 			(require-all
 				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 				)
 				(require-any
-					(extension "com.apple.revisiond.revision")
+					(extension "com.apple.revisiond.staging")
 					(require-all
 						(signing-identifier "com.apple.camera.lockscreen")
 						(require-any
-							(_g3 "")
+							(_g0 "")
 							(require-all
 								(extension "com.apple.sandbox.container")
 								(require-any
-									(_g3 "")
+									(_g0 "")
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(extension "com.apple.sandbox.application-group")
 												(require-any
-													(_g2 "")
+													(_g1 "")
 													(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
 													(require-all
 														(subpath "/private/var")
 														(require-any
-															(literal "/private/var/preferences/com.apple.networkd.plist")
+															(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 															(require-all
 																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
 																(require-any
-																	(_g2 "")
+																	(_g1 "")
 																	(subpath "${FRONT_USER_HOME}")
 																)
 															)

 													(subpath "${HOME}")
 												)
 												(require-any
-													(literal "${HOME}/Library/SpringBoard")
+													(_g0 "")
 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
 												)
 											)

 	)
 	(require-all
 		(signing-identifier "com.apple.camera")
+		(vnode-type SYMLINK)
 		(require-any
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+			(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+			(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+		)
+		(require-any
+			(extension "com.apple.revisiond.revision")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(signing-identifier "com.apple.camera.lockscreen")
+						(require-any
+							(_g2 "")
+							(require-all
+								(extension "com.apple.sandbox.container")
+								(require-any
+									(_g2 "")
+									(require-all
+										(subpath "/private/var")
+										(require-any
+											(require-all
+												(extension "com.apple.sandbox.application-group")
+												(require-any
+													(_g3 "")
+													(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+													(require-all
+														(subpath "/private/var")
+														(require-any
+															(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+															(require-all
+																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+																(require-any
+																	(_g3 "")
+																	(subpath "${FRONT_USER_HOME}")
+																)
+															)
+														)
+													)
+												)
+											)
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(require-any
+													(_g2 "")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
+												)
+											)
+										)
+									)
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/Snapshots")
+								)
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+	(require-all
+		(signing-identifier "com.apple.mobileslideshow")
+		(require-any
+			(_g13 "")
 			(_g14 "")
-			(_g15 "")
+			(_g16 "")
 			(_g17 "")
 			(_g18 "")
 			(_g19 "")

 			(_g24 "")
 			(_g25 "")
 			(_g26 "")
-			(_g27 "")
+			(_g29 "")
 			(_g30 "")
 			(_g31 "")
-			(_g32 "")
+			(_g33 "")
 			(_g34 "")
 			(_g35 "")
 			(_g36 "")

 			(_g42 "")
 			(_g43 "")
 			(_g44 "")
-			(_g45 "")
+			(_g47 "")
 			(_g48 "")
-			(_g49 "")
 			(_g5 "")
 			(_g6 "")
 			(_g7 "")
 			(_g8 "")
-			(_g9 "")
+			(extension "com.apple.app-sandbox.read")
 			(extension "com.apple.app-sandbox.read-write")
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
-			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
+			(extension "com.apple.app-sandbox.read-write")
+			(extension "com.apple.security.exception.files.absolute-path.read-only")
 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Library/Caches/DateFormats.plist")
 			(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
 			(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
+			(literal "${HOME}/Library/Caches/com.apple.pep.configuration.plist")
 			(literal "${HOME}/Library/Logs/awd")
 			(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
+			(literal "${HOME}/Library/SpringBoard")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+			(literal "/AppleInternal/Library/Preferences/com.apple.airplay.dashboard.plist")
 			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 			(literal "/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist")
 			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")

 			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
 			(literal "/private/var/preferences/com.apple.security.plist")
 			(literal "/private/var/preferences/com.apple.security.plist")
 			(literal "/private/var/preferences/com.apple.security.plist")
 			(require-all
 				(%entitlement-is-present "com.apple.private.networkextension.configuration")
 				(require-any
-					(_g15 "")
+					(_g14 "")
 					(literal "/private/var/preferences/com.apple.networkextension.plist")
 				)
 			)
 			(require-all
 				(%entitlement-is-present "com.apple.private.networkextension.configuration")
 				(require-any
-					(_g38 "")
+					(_g37 "")
 					(literal "/private/var/preferences/com.apple.networkextension.plist")
 				)
 			)
 			(require-all
 				(extension "com.apple.librarian.ubiquity-container")
 				(require-any
-					(_g31 "")
+					(_g30 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g31 "")
+							(_g30 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 								(require-any
-									(_g31 "")
+									(_g30 "")
 									(subpath "${FRONT_USER_HOME}")
 								)
 							)

 			(require-all
 				(extension "com.apple.sandbox.application-group")
 				(require-any
-					(_g15 "")
+					(_g14 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
+							(_g15 "")
 							(_g16 "")
-							(_g17 "")
 							(require-all
 								(subpath "${FRONT_USER_HOME}")
 								(require-any
-									(_g16 "")
+									(_g15 "")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 								)

 			)
 			(require-all
 				(extension "com.apple.sandbox.executable")
-				(extension "com.apple.security.exception.files.absolute-path.read-only")
+				(extension "com.apple.security.exception.files.absolute-path.read-write")
 			)
 			(require-all
 				(extension "com.apple.security.exception.files.home-relative-path.read-only")
-				(extension "com.apple.app-sandbox.read-write")
-			)
-			(require-all
-				(extension "com.apple.security.exception.files.home-relative-path.read-write")
-				(extension "com.apple.app-sandbox.read-write")
+				(extension "com.apple.app-sandbox.read")
 			)
 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(_g36 "")
+					(_g35 "")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)
 			(require-all
 				(signing-identifier "com.apple.camera.lockscreen")
 				(require-any
-					(_g48 "")
+					(_g47 "")
 					(require-all
 						(extension "com.apple.sandbox.container")
 						(require-any
-							(_g45 "")
+							(_g44 "")
 							(require-all
 								(subpath "/private/var")
 								(require-any
+									(_g46 "")
 									(_g47 "")
-									(_g48 "")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
 										(require-any
-											(_g47 "")
+											(_g46 "")
 											(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+$")
 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")

 			(require-all
 				(subpath "/private/var")
 				(require-any
+					(_g26 "")
 					(_g27 "")
 					(_g28 "")
-					(_g29 "")
 					(require-all
 						(process-attribute is-apple-signed-executable)
 						(require-any
-							(_g29 "")
+							(_g28 "")
 							(literal "/private/var/preferences/SystemConfiguration/com.apple.accounts.exists.plist")
 						)
 					)
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(_g28 "")
+							(_g27 "")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")

 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g35 "")
+					(_g34 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
 						(require-any
-							(_g34 "")
+							(_g33 "")
 							(require-all
 								(require-any
 									(subpath "${FRONT_USER_HOME}")

 					(require-all
 						(subpath "${HOME}")
 						(require-any
+							(_g12 "")
 							(_g13 "")
-							(_g14 "")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/SpringBoard/.*(Lock|Home).+")
 							(require-all
 								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 								(require-any
+									(_g11 "")
 									(_g12 "")
-									(_g13 "")
 									(require-all
 										(vnode-type DIRECTORY)
 										(require-any
-											(_g12 "")
+											(_g11 "")
 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
 										)
 									)

 						(extension "com.apple.sandbox.oopjit")
 						(subpath "/private/var/OOPJit")
 						(require-any
-							(_g49 "")
+							(_g48 "")
 							(extension "com.apple.app-sandbox.read")
-							(extension "com.apple.app-sandbox.read-write")
 						)
 					)
 				)

 			(require-all
 				(system-attribute carrier-build)
 				(require-any
-					(_g43 "")
+					(_g42 "")
 					(subpath "/AppleInternal")
 					(subpath "/usr/local/lib")
 				)

 			(require-all
 				(vnode-type DIRECTORY)
 				(require-any
-					(_g19 "")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.photos.peopleImageCache")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
+				(_g10 "")
 			)
 			(require-all
 				(vnode-type DIRECTORY)
 				(require-any
-					(_g42 "")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
+				)
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(_g18 "")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.photos.peopleImageCache")
+				)
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(_g38 "")
 					(require-any
 						(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.camera")
 						(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileslideshow")
 					)
 				)
 			)
-			(require-all
-				(vnode-type DIRECTORY)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(_g11 "")
-			)
 			(require-all
 				(vnode-type REGULAR-FILE)
 				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+					(_g8 "")
+					(_g9 "")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+						)
+						(_g10 "")
+					)
 				)
-				(_g11 "")
 			)
 			(require-all
 				(vnode-type SOCKET)
 				(require-any
-					(_g9 "")
+					(_g8 "")
 					(literal "${FRONT_USER_HOME}/Library/ExternalAccessory/ea*")
 				)
 			)
 			(require-all
 				(vnode-type SYMLINK)
 				(require-any
-					(_g10 "")
-					(_g9 "")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-						)
-						(_g11 "")
-					)
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
+				(_g10 "")
 			)
 			(require-any
 				(literal "${HOME}/Library/Caches/Snapshots/com.apple.camera-*")

 				(subpath "${HOME}/Library/WebKit")
 				(subpath "${HOME}/Media/Safari")
 			)
-			(require-any
-				(literal "${HOME}/Library/Logs/MobileSlideShow.log")
-				(literal "${HOME}/Library/Logs/awd/awd-Camera.log")
-				(literal "${HOME}/Library/Logs/awd/awd-MobileSlideShow.log")
-				(literal "${HOME}/Library/Logs/awd/awdComponent0x19.log")
-				(subpath "${HOME}/Library/Application Support/MobileSlideShow")
-				(subpath "${HOME}/Library/Application Support/iLifePageLayout")
-				(subpath "${HOME}/Library/Caches/com.apple.legacycamera")
-				(subpath "${HOME}/Library/Caches/com.apple.springboard.sharedimagecache/Wallpaper")
-				(subpath "${HOME}/Library/Siri")
-			)
 			(require-any
 				(literal "${HOME}/Library/SyncedPreferences/com.apple.camera.plist*")
 				(literal "${HOME}/Library/SyncedPreferences/com.apple.mobileslideshow.plist*")

 			(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
 			(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
 			(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
+			(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
+			(subpath "${HOME}/Library/Caches/Snapshots/com.apple.camera")
 			(subpath "${HOME}/Library/Caches/Snapshots/com.apple.camera")
 			(subpath "${HOME}/Library/Caches/com.apple.UIStatusBar")
 			(subpath "${HOME}/Library/Caches/com.apple.keyboards")
-			(subpath "${HOME}/Library/Caches/com.apple.photos.peopleImageCache")
 			(subpath "${HOME}/Library/Carrier Bundles")
 			(subpath "${HOME}/Library/Cookies")
 			(subpath "${HOME}/Library/Cookies")
 			(subpath "${HOME}/Library/Cookies")
 			(subpath "${HOME}/Library/Fonts")
-			(subpath "${HOME}/Library/Fonts")
 			(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CloudPhotoLibrary.aslgroup")
 			(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
 			(subpath "${HOME}/Library/SMS")

 			(subpath "/private/var/tmp/MediaCache")
 		)
 	)
-	(require-all
-		(signing-identifier "com.apple.mobileslideshow")
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-		)
-		(require-any
-			(extension "com.apple.revisiond.staging")
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(extension "com.apple.revisiond.revision")
-					(require-all
-						(signing-identifier "com.apple.camera.lockscreen")
-						(require-any
-							(_g1 "")
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(_g1 "")
-									(require-all
-										(subpath "/private/var")
-										(require-any
-											(require-all
-												(extension "com.apple.sandbox.application-group")
-												(require-any
-													(_g0 "")
-													(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
-													(require-all
-														(subpath "/private/var")
-														(require-any
-															(literal "/private/var/preferences/com.apple.networkd.plist")
-															(require-all
-																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-																(require-any
-																	(_g0 "")
-																	(subpath "${FRONT_USER_HOME}")
-																)
-															)
-														)
-													)
-												)
-											)
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(require-any
-													(literal "${HOME}/Library/SpringBoard")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
-												)
-											)
-										)
-									)
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/Snapshots")
-								)
-							)
-						)
-					)
-				)
-			)
-		)
-	)
 )
 )
 (deny file-read-data

 		(require-any
 			(require-all
 				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 				(subpath "${FRONT_USER_HOME}")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 			)
 			(require-any
 				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")

 		(subpath "${HOME}/Media/Photos")
 		(subpath "${HOME}/Media/Safari")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "${PROCESS_TEMP_DIR}/MediaCache")
 		(subpath "/private/var/tmp")
 	)
 )

 )
 (deny file-write*
 	(require-all
-		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
 		(require-not (extension "com.apple.app-sandbox.read"))
-		(require-not (extension "com.apple.app-sandbox.read-write"))
 		(require-not (extension "com.apple.sandbox.executable"))
 		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-write"))
+		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
+		(require-not (extension "com.apple.app-sandbox.read-write"))
 		(require-any
 			(subpath "${ANY_USER_HOME}/Containers")
 			(subpath "/private/var/containers")

 		(require-any
 			(require-all
 				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 				(subpath "${FRONT_USER_HOME}")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 			)
 			(require-any
 				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")

 		(subpath "${HOME}/Media/Photos")
 		(subpath "${HOME}/Media/Safari")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "${PROCESS_TEMP_DIR}/MediaCache")
 		(subpath "/private/var/tmp")
 	)
 )

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+					)
+				)
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
-					)
-				)
+				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 			)
 		)
 	)

 )
 (deny file-write-create
 	(require-all
-		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
 		(require-not (extension "com.apple.app-sandbox.read"))
-		(require-not (extension "com.apple.app-sandbox.read-write"))
 		(require-not (extension "com.apple.sandbox.executable"))
 		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-write"))
+		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
+		(require-not (extension "com.apple.app-sandbox.read-write"))
 		(require-any
 			(subpath "${ANY_USER_HOME}/Containers")
 			(subpath "/private/var/containers")

 		(require-any
 			(require-all
 				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 				(subpath "${FRONT_USER_HOME}")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 			)
 			(require-any
 				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")

 		(subpath "${HOME}/Media/Photos")
 		(subpath "${HOME}/Media/Safari")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "${PROCESS_TEMP_DIR}/MediaCache")
 		(subpath "/private/var/tmp")
 	)
 )

 )
 (deny file-write-data
 	(require-all
-		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
 		(require-not (extension "com.apple.app-sandbox.read"))
-		(require-not (extension "com.apple.app-sandbox.read-write"))
 		(require-not (extension "com.apple.sandbox.executable"))
 		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-write"))
+		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
+		(require-not (extension "com.apple.app-sandbox.read-write"))
 		(require-any
 			(subpath "${ANY_USER_HOME}/Containers")
 			(subpath "/private/var/containers")

 		(require-any
 			(require-all
 				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 				(subpath "${FRONT_USER_HOME}")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
 			)
 			(require-any
 				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")

 				(signing-identifier "com.apple.camera.lockscreen")
 				(require-any
 					(require-all
-						(subpath "/private/var")
 						(require-any
 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
+						(subpath "/private/var")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 					)
 					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")

 										(signing-identifier "com.apple.camera.lockscreen")
 										(require-any
 											(require-all
-												(subpath "/private/var")
 												(require-any
 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
+												(subpath "/private/var")
 												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 											)
 											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")

 												(signing-identifier "com.apple.camera.lockscreen")
 												(require-any
 													(require-all
-														(subpath "/private/var")
 														(require-any
 															(subpath "${FRONT_USER_HOME}")
 															(subpath "${HOME}")
 														)
+														(subpath "/private/var")
 														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 													)
 													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")

 		(subpath "${HOME}/Media/Photos")
 		(subpath "${HOME}/Media/Safari")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "${PROCESS_TEMP_DIR}/MediaCache")
 		(subpath "/private/var/mnt")
 		(subpath "/private/var/tmp")
 	)

 				(signing-identifier "com.apple.camera.lockscreen")
 				(require-any
 					(require-all
-						(subpath "/private/var")
 						(require-any
 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
+						(subpath "/private/var")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 					)
 					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")

 										(signing-identifier "com.apple.camera.lockscreen")
 										(require-any
 											(require-all
-												(subpath "/private/var")
 												(require-any
 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
+												(subpath "/private/var")
 												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 											)
 											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")

 												(signing-identifier "com.apple.camera.lockscreen")
 												(require-any
 													(require-all
-														(subpath "/private/var")
 														(require-any
 															(subpath "${FRONT_USER_HOME}")
 															(subpath "${HOME}")
 														)
+														(subpath "/private/var")
 														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 													)
 													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")

 )
 (deny file-write-unlink
 	(require-all
-		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
 		(require-not (extension "com.apple.app-sandbox.read"))
-		(require-not (extension "com.apple.app-sandbox.read-write"))
 		(require-not (extension "com.apple.sandbox.executable"))
 		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-write"))
+		(require-not (extension "com.apple.security.exception.files.home-relative-path.read-only"))
+		(require-not (extension "com.apple.app-sandbox.read-write"))
 		(require-any
 			(subpath "${ANY_USER_HOME}/Containers")
 			(subpath "/private/var/containers")

 (allow mach-lookup
 	(with report)
 	(require-all
-		(signing-identifier "com.apple.camera")
+		(signing-identifier "com.apple.mobileslideshow")
 		(require-any
 			(extension "com.apple.sandbox.application-group")
 			(global-name "PurplePPTServer")

 			(global-name "com.apple.locationd.registration")
 			(global-name "com.apple.locationd.spi")
 			(global-name "com.apple.locationd.synchronous")
-			(global-name "com.apple.lsd.advertisingidentifiers")
-			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.lsd.xpc")
 			(global-name "com.apple.marco")
 			(global-name "com.apple.mediaanalysisd.analysis")

 			(global-name "com.apple.siri.VoiceShortcuts.xpc")
 			(global-name "com.apple.siri.vocabularyupdates")
 			(global-name "com.apple.sociallayerd")
+			(global-name "com.apple.speech.localspeechrecognition")
 			(global-name "com.apple.spotlight.IndexAgent")
 			(global-name "com.apple.spotlight.IndexDelegateAgent")
 			(global-name "com.apple.spotlight.SearchAgent")

 				(global-name "com.apple.ExposureNotification")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.exposure-notification")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.ServicesPaymentAngel")
 				(require-any
 					(%entitlement-is-present "com.apple.private.applemediaservices")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 					(%entitlement-is-bool-true "com.apple.authkit.client.internal")
 					(%entitlement-is-bool-true "com.apple.authkit.client.private")
 					(process-attribute is-apple-signed-executable)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.assessmentagent")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.coreidvd.digital-presentment.xpc")
 				(require-any
 					(require-all
-						(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+						(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 						(require-any
-							(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
-							(xpc-service-name "com.apple.ImageIOXPCService")
+							(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+							(xpc-service-name ".viewservice")
 						)
 					)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.family.ageRange.xpc")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.declared-age-range")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(require-any
 					(%entitlement-is-present "com.apple.developer.financekit")
 					(%entitlement-is-present "com.apple.finance.private")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.gputools.service")
 				(require-any
 					(system-attribute developer-mode)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 			)
 			(require-all
 				(global-name "com.apple.merchantd.identity")
-				(%entitlement-is-present "com.apple.developer.proximity-reader.identity.display")
+				(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
 			)
 			(require-all
 				(global-name "com.apple.merchantd.storage")

 				(global-name "com.apple.messages.critical-messaging")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.odi.assessmentService")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.trustinsights.base")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.seserviced.credential.manager")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.secure-element-credential")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.seserviced.session")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.carkey.session")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				)
 				(require-any
 					(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 						(global-name "com.apple.seserviced.session")
 						(require-any
 							(%entitlement-is-present "com.apple.developer.carkey.session")
-							(xpc-service-name "com.apple.ImageIOXPCService")
+							(xpc-service-name ".viewservice")
 						)
 					)
 				)

 				(global-name "com.apple.airplaydiagnostics.server")
 				(global-name "com.apple.dictationd.recognition")
 				(global-name "com.apple.ondemandd.client")
-				(global-name "com.apple.speech.localspeechrecognition")
 			)
 			(require-any
 				(global-name "com.apple.AccessorySetupUI")

 				(global-name "com.apple.iap2d.xpc")
 				(global-name "com.apple.iapd.xpc")
 			)
+			(require-any
+				(global-name "com.apple.lsd.advertisingidentifiers")
+				(global-name "com.apple.lsd.openurl")
+			)
 			(require-any
 				(global-name "com.apple.timesync.expositor")
 				(global-name "com.apple.timesync.manager")

 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.mobileslideshow")
-		(global-name "com.apple.securityd")
+		(signing-identifier "com.apple.camera")
+		(global-name "com.apple.storekitd")
 	)
 )
 (allow mach-lookup

 			(signing-identifier "com.apple.camera.lockscreen")
 			(signing-identifier "com.apple.photos.Memoryscape")
 		)
-		(global-name "com.apple.securityd")
+		(global-name "com.apple.storekitd")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.camera")
+		(signing-identifier "com.apple.mobileslideshow")
 		(require-any
 			(extension "com.apple.sandbox.application-group")
 			(global-name "PurplePPTServer")

 			(global-name "com.apple.locationd.registration")
 			(global-name "com.apple.locationd.spi")
 			(global-name "com.apple.locationd.synchronous")
-			(global-name "com.apple.lsd.advertisingidentifiers")
-			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.lsd.xpc")
 			(global-name "com.apple.marco")
 			(global-name "com.apple.mediaanalysisd.analysis")

 			(global-name "com.apple.siri.VoiceShortcuts.xpc")
 			(global-name "com.apple.siri.vocabularyupdates")
 			(global-name "com.apple.sociallayerd")
+			(global-name "com.apple.speech.localspeechrecognition")
 			(global-name "com.apple.spotlight.IndexAgent")
 			(global-name "com.apple.spotlight.IndexDelegateAgent")
 			(global-name "com.apple.spotlight.SearchAgent")

 				(global-name "com.apple.ExposureNotification")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.exposure-notification")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.ServicesPaymentAngel")
 				(require-any
 					(%entitlement-is-present "com.apple.private.applemediaservices")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 					(%entitlement-is-bool-true "com.apple.authkit.client.internal")
 					(%entitlement-is-bool-true "com.apple.authkit.client.private")
 					(process-attribute is-apple-signed-executable)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.assessmentagent")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.coreidvd.digital-presentment.xpc")
 				(require-any
 					(require-all
-						(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+						(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 						(require-any
-							(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
-							(xpc-service-name "com.apple.ImageIOXPCService")
+							(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+							(xpc-service-name ".viewservice")
 						)
 					)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.family.ageRange.xpc")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.declared-age-range")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(require-any
 					(%entitlement-is-present "com.apple.developer.financekit")
 					(%entitlement-is-present "com.apple.finance.private")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.gputools.service")
 				(require-any
 					(system-attribute developer-mode)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 			)
 			(require-all
 				(global-name "com.apple.merchantd.identity")
-				(%entitlement-is-present "com.apple.developer.proximity-reader.identity.display")
+				(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
 			)
 			(require-all
 				(global-name "com.apple.merchantd.storage")

 				(global-name "com.apple.messages.critical-messaging")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.odi.assessmentService")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.trustinsights.base")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.seserviced.credential.manager")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.secure-element-credential")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.seserviced.session")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.carkey.session")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				)
 				(require-any
 					(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 						(global-name "com.apple.seserviced.session")
 						(require-any
 							(%entitlement-is-present "com.apple.developer.carkey.session")
-							(xpc-service-name "com.apple.ImageIOXPCService")
+							(xpc-service-name ".viewservice")
 						)
 					)
 				)

 				(global-name "com.apple.airplaydiagnostics.server")
 				(global-name "com.apple.dictationd.recognition")
 				(global-name "com.apple.ondemandd.client")
-				(global-name "com.apple.speech.localspeechrecognition")
 			)
 			(require-any
 				(global-name "com.apple.AccessorySetupUI")

 				(global-name "com.apple.iap2d.xpc")
 				(global-name "com.apple.iapd.xpc")
 			)
+			(require-any
+				(global-name "com.apple.lsd.advertisingidentifiers")
+				(global-name "com.apple.lsd.openurl")
+			)
 			(require-any
 				(global-name "com.apple.timesync.expositor")
 				(global-name "com.apple.timesync.manager")

 (deny mach-lookup)
 (deny mach-lookup
 	(require-all
-		(signing-identifier "com.apple.camera")
+		(signing-identifier "com.apple.mobileslideshow")
 		(require-any
 			(extension "com.apple.sandbox.application-group")
 			(global-name "PurplePPTServer")

 			(global-name "com.apple.locationd.registration")
 			(global-name "com.apple.locationd.spi")
 			(global-name "com.apple.locationd.synchronous")
-			(global-name "com.apple.lsd.advertisingidentifiers")
-			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.lsd.xpc")
 			(global-name "com.apple.marco")
 			(global-name "com.apple.mediaanalysisd.analysis")

 			(global-name "com.apple.siri.VoiceShortcuts.xpc")
 			(global-name "com.apple.siri.vocabularyupdates")
 			(global-name "com.apple.sociallayerd")
+			(global-name "com.apple.speech.localspeechrecognition")
 			(global-name "com.apple.spotlight.IndexAgent")
 			(global-name "com.apple.spotlight.IndexDelegateAgent")
 			(global-name "com.apple.spotlight.SearchAgent")

 				(global-name "com.apple.ExposureNotification")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.exposure-notification")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.ServicesPaymentAngel")
 				(require-any
 					(%entitlement-is-present "com.apple.private.applemediaservices")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 					(%entitlement-is-bool-true "com.apple.authkit.client.internal")
 					(%entitlement-is-bool-true "com.apple.authkit.client.private")
 					(process-attribute is-apple-signed-executable)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.assessmentagent")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.coreidvd.digital-presentment.xpc")
 				(require-any
 					(require-all
-						(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+						(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 						(require-any
-							(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
-							(xpc-service-name "com.apple.ImageIOXPCService")
+							(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+							(xpc-service-name ".viewservice")
 						)
 					)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.family.ageRange.xpc")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.declared-age-range")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(require-any
 					(%entitlement-is-present "com.apple.developer.financekit")
 					(%entitlement-is-present "com.apple.finance.private")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.gputools.service")
 				(require-any
 					(system-attribute developer-mode)
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 			)
 			(require-all
 				(global-name "com.apple.merchantd.identity")
-				(%entitlement-is-present "com.apple.developer.proximity-reader.identity.display")
+				(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
 			)
 			(require-all
 				(global-name "com.apple.merchantd.storage")

 				(global-name "com.apple.messages.critical-messaging")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				(global-name "com.apple.odi.assessmentService")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.trustinsights.base")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.seserviced.credential.manager")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.secure-element-credential")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all
 				(global-name "com.apple.seserviced.session")
 				(require-any
 					(%entitlement-is-present "com.apple.developer.carkey.session")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 				)
 				(require-any
 					(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
-					(xpc-service-name "com.apple.ImageIOXPCService")
+					(xpc-service-name ".viewservice")
 				)
 			)
 			(require-all

 						(global-name "com.apple.seserviced.session")
 						(require-any
 							(%entitlement-is-present "com.apple.developer.carkey.session")
-							(xpc-service-name "com.apple.ImageIOXPCService")
+							(xpc-service-name ".viewservice")
 						)
 					)
 				)

 				(global-name "com.apple.airplaydiagnostics.server")
 				(global-name "com.apple.dictationd.recognition")
 				(global-name "com.apple.ondemandd.client")
-				(global-name "com.apple.speech.localspeechrecognition")
 			)
 			(require-any
 				(global-name "com.apple.AccessorySetupUI")

 				(global-name "com.apple.iap2d.xpc")
 				(global-name "com.apple.iapd.xpc")
 			)
+			(require-any
+				(global-name "com.apple.lsd.advertisingidentifiers")
+				(global-name "com.apple.lsd.openurl")
+			)
 			(require-any
 				(global-name "com.apple.timesync.expositor")
 				(global-name "com.apple.timesync.manager")

 
 (allow user-preference-read
 	(require-all
-		(signing-identifier "com.apple.mobileslideshow")
-		(preference-domain "com.apple.appleaccount")
+		(signing-identifier "com.apple.camera")
+		(preference-domain "com.apple.CoreMotion")
 	)
 )
 (allow user-preference-read

 			(signing-identifier "com.apple.camera.lockscreen")
 			(signing-identifier "com.apple.photos.Memoryscape")
 		)
-		(preference-domain "com.apple.appleaccount")
+		(preference-domain "com.apple.CoreMotion")
 	)
 )
 (allow user-preference-read
 	(require-all
-		(signing-identifier "com.apple.camera")
+		(signing-identifier "com.apple.mobileslideshow")
 		(require-any
 			(preference-domain "com.apple.AOSNotification.public.notbackedup")
 			(preference-domain "com.apple.Accessibility")

 			(preference-domain "com.apple.airplay")
 			(preference-domain "com.apple.appleaccount")
 			(preference-domain "com.apple.assistant")
+			(preference-domain "com.apple.assistant.backedup")
 			(preference-domain "com.apple.assistant.logging")
+			(preference-domain "com.apple.assistant.public")
 			(preference-domain "com.apple.assistant.support")
 			(preference-domain "com.apple.avfoundation")
 			(preference-domain "com.apple.avkit")

 				(preference-domain "com.apple.WebKit")
 				(preference-domain "com.apple.act")
 			)
-			(require-any
-				(preference-domain "com.apple.assistant.backedup")
-				(preference-domain "com.apple.assistant.public")
-			)
 			(require-any
 				(preference-domain "com.apple.cloud.quota")
 				(preference-domain "com.apple.legacycamera")

 
 (allow managed-preference-read
 	(require-all
-		(signing-identifier "com.apple.mobileslideshow")
-		(preference-domain "com.apple.appleaccount")
+		(signing-identifier "com.apple.camera")
+		(preference-domain "com.apple.CoreMotion")
 	)
 )
 (allow managed-preference-read

 			(signing-identifier "com.apple.camera.lockscreen")
 			(signing-identifier "com.apple.photos.Memoryscape")
 		)
-		(preference-domain "com.apple.appleaccount")
+		(preference-domain "com.apple.CoreMotion")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(signing-identifier "com.apple.camera")
+		(signing-identifier "com.apple.mobileslideshow")
 		(require-any
 			(preference-domain "com.apple.AOSNotification.public.notbackedup")
 			(preference-domain "com.apple.Accessibility")

 			(preference-domain "com.apple.airplay")
 			(preference-domain "com.apple.appleaccount")
 			(preference-domain "com.apple.assistant")
+			(preference-domain "com.apple.assistant.backedup")
 			(preference-domain "com.apple.assistant.logging")
+			(preference-domain "com.apple.assistant.public")
 			(preference-domain "com.apple.assistant.support")
 			(preference-domain "com.apple.avfoundation")
 			(preference-domain "com.apple.avkit")

 				(preference-domain "com.apple.WebKit")
 				(preference-domain "com.apple.act")
 			)
-			(require-any
-				(preference-domain "com.apple.assistant.backedup")
-				(preference-domain "com.apple.assistant.public")
-			)
 			(require-any
 				(preference-domain "com.apple.cloud.quota")
 				(preference-domain "com.apple.legacycamera")

 
 (allow user-preference-write
 	(require-all
-		(signing-identifier "com.apple.mobileslideshow")
-		(preference-domain "com.apple.appleaccount")
+		(signing-identifier "com.apple.camera")
+		(require-any
+			(preference-domain "com.apple.cloud.quota")
+			(preference-domain "com.apple.legacycamera")
+			(preference-domain "com.apple.nanocamera")
+			(preference-domain "com.apple.videouploadplugins")
+			(preference-domain "com.apple.youtubeframework.notbackedup")
+		)
 	)
 )
 (allow user-preference-write

 			(signing-identifier "com.apple.camera.lockscreen")
 			(signing-identifier "com.apple.photos.Memoryscape")
 		)
-		(preference-domain "com.apple.appleaccount")
+		(require-any
+			(preference-domain "com.apple.cloud.quota")
+			(preference-domain "com.apple.legacycamera")
+			(preference-domain "com.apple.nanocamera")
+			(preference-domain "com.apple.videouploadplugins")
+			(preference-domain "com.apple.youtubeframework.notbackedup")
+		)
 	)
 )
 (allow user-preference-write
 	(require-all
-		(signing-identifier "com.apple.camera")
+		(signing-identifier "com.apple.mobileslideshow")
 		(require-any
 			(preference-domain "com.apple.Preferences")
 			(preference-domain "com.apple.WebFoundation")
```
