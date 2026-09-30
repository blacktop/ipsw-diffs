## sharingd

> Group: ⬆️ Updated

```diff

 
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
-		(subpath "${HOME}/Media")
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "${HOME}/Media/Purchases")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Media/Debug")
+		(extension-class "com.apple.mediaserverd.read-write")
+		(subpath "${HOME}/Media/Photos")
 	)
 )
 (allow file-issue-extension

 		(subpath "${HOME}/Downloads/com.apple.AirDrop")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.sharing.airdrop.readonly")
+		(subpath "${HOME}/Media")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.sharingd")
+			(subpath "${HOME}/Library/Caches/com.apple.sharingd")
+		)
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
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "${HOME}/Media/Photos")
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
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(extension "com.apple.security.exception.files.absolute-path.read-only")
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-only")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			)
+			(require-all
+				(extension "com.apple.librarian.ubiquity-container")
+				(require-any
+					(require-all
+						(extension "com.apple.sharing.airdrop.readonly")
+						(require-any
+							(extension-class "com.apple.mediaserverd.read")
+							(require-all
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+								(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var")
+						(require-any
+							(require-all
+								(extension "com.apple.sharing.airdrop.readonly")
+								(require-any
+									(extension-class "com.apple.mediaserverd.read")
+									(require-all
+										(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+										(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+									)
+								)
+							)
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+								(require-any
+									(require-all
+										(extension "com.apple.sharing.airdrop.readonly")
+										(require-any
+											(extension-class "com.apple.mediaserverd.read")
+											(require-all
+												(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+												(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+											)
+										)
+									)
+									(subpath "${FRONT_USER_HOME}")
+								)
+							)
+						)
+					)
+					(subpath "${HOME}/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+				)
+			)
+			(require-all
+				(extension "com.apple.sharing.airdrop.readonly")
+				(require-any
+					(extension-class "com.apple.mediaserverd.read")
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+					)
+				)
+			)
+			(subpath "${HOME}/Downloads/com.apple.AirDrop")
+			(subpath "${HOME}/Media/PhotoStreamsData")
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Media/Debug")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.sharingd")
+			(subpath "${HOME}/Library/Caches/com.apple.sharingd")
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
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(require-all
+				(subpath "${HOME}/Media/PhotoStreamsData")
+				(extension-class "com.apple.aned.read-only")
+			)
+			(subpath "${HOME}/Media/DCIM")
+			(subpath "${HOME}/Media/Debug")
+			(subpath "${HOME}/Media/MediaAnalysis")
+			(subpath "${HOME}/Media/Memories")
+			(subpath "${HOME}/Media/PhotoData")
+			(subpath "${HOME}/Media/Photos")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "${HOME}/Media/Photos")
 	)
 )
 (allow file-issue-extension

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Media/Debug")
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
-		(extension-class "com.apple.nsurlsessiond.readonly")
-		(extension "com.apple.sandbox.executable")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Media/Debug")
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
-		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.sharingd")
-			(subpath "/private/var/tmp/com.apple.sharingd")
+			(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.sharingd")
+			(subpath "${HOME}/Library/Caches/com.apple.sharingd")
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.sharingd")
-			(subpath "/private/var/tmp/com.apple.sharingd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.sharingd")
-			(subpath "/private/var/tmp/com.apple.sharingd")
+			(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.sharingd")
+			(subpath "${HOME}/Library/Caches/com.apple.sharingd")
 		)
 	)
 )

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes")
-				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
 			)
 		)
 	)

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									)
+								)
 							)
-							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(subpath "/private/var/PersonaVolumes")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
 						)
 					)

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.sharingd")
-			(subpath "/private/var/tmp/com.apple.sharingd")
+			(require-all
+				(extension "com.apple.sandbox.application-group")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(subpath "${FRONT_USER_HOME}")
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.sharingd")
+				(subpath "${HOME}/Library/Caches/com.apple.sharingd")
+			)
+			(require-any
+				(subpath "${PROCESS_TEMP_DIR}/com.apple.sharingd")
+				(subpath "/private/var/tmp/com.apple.sharingd")
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
+			(subpath "${HOME}/Library/Caches/com.apple.HomeKit.configurations")
+			(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Media/Photos")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(require-all
-				(subpath "${HOME}/Media/PhotoStreamsData")
-				(extension-class "com.apple.mediaserverd.read")
-			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension "com.apple.app-sandbox.read-write")
 		(require-any
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
+			(extension-class "com.apple.app-sandbox.read")
+			(extension-class "com.apple.app-sandbox.read-write")
+			(extension-class "com.apple.mediaserverd.read")
+			(extension-class "com.apple.mediaserverd.read-write")
+			(extension-class "com.apple.sharing.airdrop.readonly")
 		)
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
+		(extension-class "com.apple.quicklook.readonly")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
 			(require-all

 )
 (allow file-issue-extension
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
-		(require-any
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.app-sandbox.read-write")
-			(extension-class "com.apple.mediaserverd.read")
-			(extension-class "com.apple.mediaserverd.read-write")
-			(extension-class "com.apple.sharing.airdrop.readonly")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(extension "com.apple.sandbox.application-group")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}/Library/Caches/com.apple.HomeKit.configurations")
-								)
-							)
-							(subpath "${HOME}/Library/Caches/com.apple.HomeKit.configurations")
-						)
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.HomeKit.configurations")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-				)
-			)
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.sharingd")
-				(subpath "${HOME}/Library/Caches/com.apple.sharingd")
-			)
-			(require-any
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.sharingd")
-				(subpath "/private/var/tmp/com.apple.sharingd")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
-			(subpath "${HOME}/Library/Caches/com.apple.HomeKit.configurations")
-			(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.quicklook.readonly")
+		(extension-class "com.apple.spotlight-indexable")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
 			(require-all

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.sharing.airdrop.readonly")
+		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(extension "com.apple.security.exception.files.absolute-path.read-only")
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(extension "com.apple.security.exception.files.home-relative-path.read-only")
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
 			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
 			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(extension "com.apple.sharing.airdrop.readonly")
-						(require-any
-							(extension-class "com.apple.mediaserverd.read")
-							(require-all
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-								(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var")
-						(require-any
-							(require-all
-								(extension "com.apple.sharing.airdrop.readonly")
-								(require-any
-									(extension-class "com.apple.mediaserverd.read")
-									(require-all
-										(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-										(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-									)
-								)
-							)
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-								(require-any
-									(require-all
-										(extension "com.apple.sharing.airdrop.readonly")
-										(require-any
-											(extension-class "com.apple.mediaserverd.read")
-											(require-all
-												(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-												(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-											)
-										)
-									)
-									(subpath "${FRONT_USER_HOME}")
-								)
-							)
-						)
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-			(require-all
-				(extension "com.apple.sharing.airdrop.readonly")
-				(require-any
-					(extension-class "com.apple.mediaserverd.read")
-					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-					)
-				)
-			)
-			(subpath "${HOME}/Downloads/com.apple.AirDrop")
-			(subpath "${HOME}/Media/PhotoStreamsData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
 		)
 	)
 )

 		)
 	)
 )
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
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.wcd.readonly")

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 									(require-all
-										(subpath "/private/var/PersonaVolumes")
+										(subpath "/private/var")
 										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(require-all
+												(extension "com.apple.sandbox.application-group")
+												(require-any
+													(require-all
+														(extension-class "com.apple.mediaserverd.read")
+														(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+													)
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
+														(require-any
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(require-all
+																(extension-class "com.apple.mediaserverd.read")
+																(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+															)
+														)
+													)
+													(require-all
+														(subpath "/private/var/PersonaVolumes")
+														(require-any
+															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(require-all
+																(subpath "${FRONT_USER_HOME}")
+																(require-any
+																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	(require-all
+																		(extension-class "com.apple.mediaserverd.read")
+																		(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+																	)
+																)
+															)
+														)
+													)
+												)
+											)
 											(require-all
 												(extension-class "com.apple.mediaserverd.read")
 												(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")

 								)
 							)
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
+								(subpath "/private/var")
 								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 									(require-all
-										(subpath "/private/var/PersonaVolumes")
+										(extension "com.apple.sandbox.application-group")
 										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(require-all
+												(extension-class "com.apple.mediaserverd.read")
+												(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+											)
 											(require-all
 												(subpath "${FRONT_USER_HOME}")
 												(require-any
 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 													(require-all
-														(subpath "/private/var/PersonaVolumes")
+														(extension-class "com.apple.mediaserverd.read")
+														(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+													)
+												)
+											)
+											(require-all
+												(subpath "/private/var/PersonaVolumes")
+												(require-any
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
 														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 															(require-all
 																(extension-class "com.apple.mediaserverd.read")
 																(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")

 											)
 										)
 									)
+									(require-all
+										(extension-class "com.apple.mediaserverd.read")
+										(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+									)
 								)
 							)
 							(require-all

 										(require-any
 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 											(require-all
-												(subpath "/private/var/PersonaVolumes")
+												(subpath "/private/var")
 												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(extension "com.apple.sandbox.application-group")
+														(require-any
+															(require-all
+																(extension-class "com.apple.mediaserverd.read")
+																(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+															)
+															(require-all
+																(subpath "${FRONT_USER_HOME}")
+																(require-any
+																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	(require-all
+																		(extension-class "com.apple.mediaserverd.read")
+																		(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+																	)
+																)
+															)
+															(require-all
+																(subpath "/private/var/PersonaVolumes")
+																(require-any
+																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	(require-all
+																		(subpath "${FRONT_USER_HOME}")
+																		(require-any
+																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			(require-all
+																				(extension-class "com.apple.mediaserverd.read")
+																				(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")
+																			)
+																		)
+																	)
+																)
+															)
+														)
+													)
 													(require-all
 														(extension-class "com.apple.mediaserverd.read")
 														(subpath "${HOME}/Library/Caches/com.apple.SensorKitDataExport")

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								)
+							)
+						)
 					)
 				)
 			)

 )
 (allow file-read*
 	(require-all
-		(process-attribute is-apple-signed-executable)
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-read*
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(process-attribute is-apple-signed-executable)
+		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 	)
 )
 (allow file-read*

 )
 (allow file-read*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 )
 (allow file-read-data
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type DIRECTORY SYMLINK)
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
-				(extension "com.apple.revisiond.revision")
+				(extension "com.apple.revisiond.staging")
 			)
 		)
 	)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								)
+							)
+						)
 					)
 				)
 			)

 )
 (allow file-read-data
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
-				(extension "com.apple.revisiond.revision")
+				(require-any
+					(extension "com.apple.revisiond.revision")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
 			)
 			(require-all
 				(require-any

 					(subpath "/private/var/.DocumentRevisions-V100/staging")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(extension "com.apple.revisiond.revision")
-					)
-				)
+				(extension "com.apple.revisiond.staging")
 			)
 		)
 	)

 		(subpath "${FRONT_USER_HOME}")
 	)
 )
+(allow file-read-data
+	(require-all
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
+	)
+)
 (allow file-read-data
 	(require-all
 		(require-any

 		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
-(allow file-read-data
-	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
-	)
-)
 (allow file-read-data
 	(require-all
 		(subpath "/AppleInternal")

 )
 (allow file-read-data
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type DIRECTORY SYMLINK)
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
-				(extension "com.apple.revisiond.revision")
+				(extension "com.apple.revisiond.staging")
 			)
 		)
 	)

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
-				(extension "com.apple.revisiond.revision")
+				(require-any
+					(extension "com.apple.revisiond.revision")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
 			)
 			(require-all
 				(require-any

 					(subpath "/private/var/.DocumentRevisions-V100/staging")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(extension "com.apple.revisiond.revision")
-					)
-				)
+				(extension "com.apple.revisiond.staging")
 			)
 		)
 	)

 			)
 			(require-all
 				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
 				(require-any
-					(extension "com.apple.revisiond.staging")
+					(extension "com.apple.revisiond.revision")
 					(require-all
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
-						(extension "com.apple.revisiond.revision")
+						(extension "com.apple.revisiond.staging")
 					)
 				)
 			)

 						(require-any
 							(require-all
 								(require-any
-									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-									(subpath "/private/var/.DocumentRevisions-V100/staging")
-									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 								)
 								(require-any
-									(extension "com.apple.revisiond.staging")
+									(extension "com.apple.revisiond.revision")
 									(require-all
 										(require-any
-											(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-											(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-											(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+											(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+											(subpath "/private/var/.DocumentRevisions-V100/staging")
+											(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 										)
-										(extension "com.apple.revisiond.revision")
+										(extension "com.apple.revisiond.staging")
 									)
 								)
 							)

 					)
 					(require-all
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)
 						(require-any
-							(extension "com.apple.revisiond.staging")
+							(extension "com.apple.revisiond.revision")
 							(require-all
 								(require-any
-									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 								)
-								(extension "com.apple.revisiond.revision")
+								(extension "com.apple.revisiond.staging")
 							)
 						)
 					)

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "/System/Library/Carrier Bundles")
+		(require-any
+			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.sandbox.application-group")

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								)
+							)
+						)
 					)
 				)
 			)

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(require-any
-			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 		(literal "${HOME}/Library/Mobile Documents")
 		(literal "${HOME}/Library/PPTDevice")
 		(literal "${HOME}/Library/Preferences")
+		(literal "${HOME}/Media/MediaAnalysis")
+		(literal "${HOME}/Media/Memories")
 		(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
 		(literal "/private")
 		(literal "/private/var")

 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type DIRECTORY SYMLINK)
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
-				(extension "com.apple.revisiond.revision")
+				(extension "com.apple.revisiond.staging")
 			)
 		)
 	)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+								)
+							)
+						)
 					)
 				)
 			)

 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
-				(extension "com.apple.revisiond.revision")
+				(require-any
+					(extension "com.apple.revisiond.revision")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
 			)
 			(require-all
 				(require-any

 					(subpath "/private/var/.DocumentRevisions-V100/staging")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(extension "com.apple.revisiond.revision")
-					)
-				)
+				(extension "com.apple.revisiond.staging")
 			)
 		)
 	)

 		(subpath "${FRONT_USER_HOME}")
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(require-any

 		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(subpath "/AppleInternal")

 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 							(require-all
 								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
+							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${HOME}")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+								(subpath "${HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
 						)
 					)

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 )
 (allow file-write*
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-write*

 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 							(require-all
 								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
+							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${HOME}")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+								(subpath "${HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
 						)
 					)

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 )
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-write-create

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

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

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 							(require-all
 								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
+							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${HOME}")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+								(subpath "${HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
 						)
 					)

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 )
 (allow file-write-flags
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-write-flags

 )
 (allow file-write-flags
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 							(require-all
 								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
+							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${HOME}")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+								(subpath "${HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
 						)
 					)

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 )
 (allow file-write-mode
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-write-mode

 )
 (allow file-write-mode
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 							(require-all
 								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
+							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${HOME}")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+								(subpath "${HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
 						)
 					)

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 )
 (allow file-write-owner
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-write-owner

 )
 (allow file-write-owner
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 							(require-all
 								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
+							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${HOME}")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+								(subpath "${HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
 						)
 					)

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 )
 (allow file-write-times
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-write-times

 )
 (allow file-write-times
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 							(require-all
 								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
+							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${HOME}")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+								(subpath "${HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
 						)
 					)

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-write-unlink

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 							(require-all
 								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
+							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
-						(subpath "${HOME}")
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+								(subpath "${HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 							)
 						)
 					)

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/com\.apple\.sharing($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 )
 (allow file-write-xattr
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.SensorKitDataExport")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.sharingd")
-		)
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 	)
 )
 (allow file-write-xattr

 )
 (allow file-write-xattr
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.sharingd")
```
