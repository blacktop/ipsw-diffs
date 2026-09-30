## maild

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.app-sandbox.read")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.sharing.airdrop.readonly")
+		(require-any
+			(require-all
+				(subpath "${HOME}/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			)
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+					(extension "com.apple.librarian.ubiquity-container")
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+		)
+		(extension "com.apple.odr-assets")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(extension "com.apple.app-sandbox.read-write")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(extension "com.apple.app-sandbox.read-write")
 	)
 )
 (allow file-issue-extension

 		(extension "com.apple.app-sandbox.read-write")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.quicklook.readonly")
+		(subpath "${HOME}/Library/Mail")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.spotlight-indexable")
+		(subpath "${HOME}/Library/Mail")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension "com.apple.sandbox.executable")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
+		(subpath "${HOME}/Media/Purchases")
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
+		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+			(require-all
+				(subpath "/private/var")
+				(subpath "${HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Ringtones.plist$")
+				)
+			)
+			(subpath "${HOME}/Media/Purchases")
 		)
-		(extension "com.apple.odr-assets")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(extension "com.apple.app-sandbox.read-write")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension "com.apple.librarian.ubiquity-container")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Mobile Documents")
-				(extension-class "com.apple.quicklook.readonly")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 			)
 			(require-all
 				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 				(subpath "${FRONT_USER_HOME}")
 				(require-any
-					(extension-class "com.apple.aned.read-only")
-					(extension-class "com.apple.app-sandbox.read")
-					(extension-class "com.apple.app-sandbox.read-write")
-					(extension-class "com.apple.mediaserverd.read")
-					(extension-class "com.apple.mediaserverd.read-write")
-					(extension-class "com.apple.quicklook.readonly")
-					(extension-class "com.apple.sharing.airdrop.readonly")
+					(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+					(extension "com.apple.librarian.ubiquity-container")
 				)
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				(extension-class "com.apple.quicklook.readonly")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				(extension-class "com.apple.quicklook.readonly")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 			)
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.security.exception.files.home-relative-path.read-write")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.app-sandbox.read")
 		(require-any
-			(extension "com.apple.app-sandbox.read-write")
-			(extension "com.apple.security.exception.files.absolute-path.read-only")
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(extension "com.apple.security.exception.files.home-relative-path.read-only")
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
 		)
+		(extension "com.apple.odr-assets")
 	)
 )
 (allow file-issue-extension

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Media/Purchases")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Media/Purchases")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(extension "com.apple.app-sandbox.read-write")
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
-		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(require-all
-				(subpath "/private/var")
-				(subpath "${HOME}")
+				(extension "com.apple.assets.read")
 				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Ringtones.plist$")
 					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
-							(require-all
-								(extension "com.apple.usernotifications.attachments.read-only")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
-								)
-							)
-						)
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 					)
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
-			(subpath "${HOME}/Media/Purchases")
+			(require-all
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			)
 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
-		)
-		(extension "com.apple.odr-assets")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
+		(extension-class "com.apple.quicklook.readonly")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension "com.apple.librarian.ubiquity-container")
 		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Mobile Documents")
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 			(require-all
 				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 				(subpath "${FRONT_USER_HOME}")
 				(require-any
-					(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-					(extension "com.apple.librarian.ubiquity-container")
+					(extension-class "com.apple.aned.read-only")
+					(extension-class "com.apple.app-sandbox.read")
+					(extension-class "com.apple.app-sandbox.read-write")
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
+					(extension-class "com.apple.quicklook.readonly")
+					(extension-class "com.apple.sharing.airdrop.readonly")
 				)
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(extension "com.apple.app-sandbox.read-write")
+			(extension "com.apple.security.exception.files.absolute-path.read-only")
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-only")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension "com.apple.sandbox.application-group")

 				(require-any
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
 					)
 				)
 			)

 				(require-any
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
 					)
 				)
 			)

 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									)
-								)
-							)
 							(require-all
 								(subpath "${FRONT_USER_HOME}")
 								(require-any

 											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 											(require-all
 												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													)
-												)
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 											)
 										)
 									)
 								)
 							)
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
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
 								(require-any

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 											(require-all
 												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+												(require-any
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
+														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													)
+												)
 											)
 										)
 									)

 							(require-all
 								(subpath "/private/var")
 								(require-any
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											)
-										)
-									)
 									(require-all
 										(subpath "${FRONT_USER_HOME}")
 										(require-any

 													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 													(require-all
 														(subpath "${FRONT_USER_HOME}")
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															)
-														)
+														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 													)
 												)
 											)
 										)
 									)
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(require-all
+												(subpath "${FRONT_USER_HOME}")
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											)
+										)
+									)
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
 										(require-any

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 													(require-all
 														(subpath "/private/var/PersonaVolumes")
-														(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+														(require-any
+															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(require-all
+																(subpath "${FRONT_USER_HOME}")
+																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															)
+														)
 													)
 												)
 											)

 									(require-all
 										(subpath "/private/var")
 										(require-any
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													)
-												)
-											)
 											(require-all
 												(subpath "${FRONT_USER_HOME}")
 												(require-any

 															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 															(require-all
 																(subpath "${FRONT_USER_HOME}")
-																(require-any
-																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	)
-																)
+																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 															)
 														)
 													)
 												)
 											)
+											(require-all
+												(subpath "/private/var/PersonaVolumes")
+												(require-any
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
+														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													)
+												)
+											)
 											(require-all
 												(subpath "/private/var/PersonaVolumes")
 												(require-any

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 															(require-all
 																(subpath "/private/var/PersonaVolumes")
-																(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																(require-any
+																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	(require-all
+																		(subpath "${FRONT_USER_HOME}")
+																		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	)
+																)
 															)
 														)
 													)

 						(require-any
 							(require-all
 								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(extension-class "com.apple.quicklook.readonly")
+								(extension-class "com.apple.mediaserverd.read-write")
 							)
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 				)
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-				(extension-class "com.apple.quicklook.readonly")
-			)
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.spotlight-indexable")
-		(subpath "${HOME}/Library/Mail")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.quicklook.readonly")
-		(subpath "${HOME}/Library/Mail")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(extension-class "com.apple.quicklook.readonly")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(subpath "${HOME}/Library/Mobile Documents")
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-			)
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-					(extension "com.apple.librarian.ubiquity-container")
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 		)
 	)

 				(require-any
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
 					)
 				)
 			)

 				(require-any
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
 					)
 				)
 			)

 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									)
-								)
-							)
 							(require-all
 								(subpath "${FRONT_USER_HOME}")
 								(require-any

 											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 											(require-all
 												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													)
-												)
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 											)
 										)
 									)
 								)
 							)
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
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
 								(require-any

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 											(require-all
 												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+												(require-any
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
+														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													)
+												)
 											)
 										)
 									)

 							(require-all
 								(subpath "/private/var")
 								(require-any
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											)
-										)
-									)
 									(require-all
 										(subpath "${FRONT_USER_HOME}")
 										(require-any

 													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 													(require-all
 														(subpath "${FRONT_USER_HOME}")
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															)
-														)
+														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 													)
 												)
 											)
 										)
 									)
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(require-all
+												(subpath "${FRONT_USER_HOME}")
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											)
+										)
+									)
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
 										(require-any

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 													(require-all
 														(subpath "/private/var/PersonaVolumes")
-														(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+														(require-any
+															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(require-all
+																(subpath "${FRONT_USER_HOME}")
+																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															)
+														)
 													)
 												)
 											)

 									(require-all
 										(subpath "/private/var")
 										(require-any
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													)
-												)
-											)
 											(require-all
 												(subpath "${FRONT_USER_HOME}")
 												(require-any

 															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 															(require-all
 																(subpath "${FRONT_USER_HOME}")
-																(require-any
-																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	)
-																)
+																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 															)
 														)
 													)
 												)
 											)
+											(require-all
+												(subpath "/private/var/PersonaVolumes")
+												(require-any
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
+														(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													)
+												)
+											)
 											(require-all
 												(subpath "/private/var/PersonaVolumes")
 												(require-any

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 															(require-all
 																(subpath "/private/var/PersonaVolumes")
-																(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																(require-any
+																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	(require-all
+																		(subpath "${FRONT_USER_HOME}")
+																		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	)
+																)
 															)
 														)
 													)

 						(require-any
 							(require-all
 								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(extension-class "com.apple.quicklook.readonly")
+								(extension-class "com.apple.mediaserverd.read-write")
 							)
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 				)
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 		)
 	)

 		(extension "com.apple.classkit.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/Library/Audio/Tunings/AID*")
+		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(require-any
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Artwork(/|$)")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+	)
+)
 (allow file-read*
 	(require-all
 		(extension "com.apple.sandbox.application-group")

 		)
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Artwork(/|$)")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
-		)
-	)
-)
 (allow file-read*
 	(require-all
 		(extension "com.apple.fileprovider.read-write")

 		)
 	)
 )
-(allow file-read*
-	(require-all
-		(literal "/Library/Audio/Tunings/AID*")
-		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
-	)
-)
 (allow file-read*
 	(require-all
 		(require-any

 		(extension "com.apple.usernotifications.attachments.read-only")
 	)
 )
-(allow file-read*
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/AppleInternal")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read*
-	(require-all
-		(process-attribute is-apple-signed-executable)
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
 (allow file-read*
 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")

 		(literal "${FRONT_USER_HOME}/Library/ExternalAccessory/ea*")
 	)
 )
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(%entitlement-is-present "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-all
+				(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/private/var/preferences/SystemConfiguration/com.apple.accounts.exists.plist")
+					(require-all
+						(%entitlement-is-present "com.apple.private.networkextension.configuration")
+						(literal "/private/var/preferences/com.apple.networkextension.plist")
+					)
+				)
+			)
+			(require-all
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
+				(subpath "${HOME}")
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/\.GlobalPreferences$")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
+						(subpath "${HOME}")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
+		(subpath "${HOME}")
+		(extension "com.apple.usernotifications.attachments.read-only")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(subpath "${HOME}")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(require-any
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Artwork(/|$)")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
+		)
+	)
+)
 (allow file-read-data
 	(require-all
 		(extension "com.apple.fileprovider.read-write")

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+	)
+)
 (allow file-read-data
 	(require-all
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")

 )
 (allow file-read-data
 	(require-all
-		(subpath "/private/var")
-		(subpath "${HOME}")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(literal "/Library/Audio/Tunings/AID*")
+		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
+	)
+)
+(allow file-read-data
+	(require-all
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Artwork(/|$)")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
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
+			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
 		)
 	)
 )
 (allow file-read-data
 	(require-all
-		(literal "/Library/Audio/Tunings/AID*")
-		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
+		(vnode-type DIRECTORY SYMLINK)
+		(require-any
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
+				(extension "com.apple.revisiond.staging")
+			)
+		)
 	)
 )
 (allow file-read-data

 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(%entitlement-is-present "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
-			)
-			(require-all
-				(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-				(process-attribute is-apple-signed-executable)
-			)
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(require-any
-					(literal "/private/var/preferences/SystemConfiguration/com.apple.accounts.exists.plist")
-					(require-all
-						(%entitlement-is-present "com.apple.private.networkextension.configuration")
-						(literal "/private/var/preferences/com.apple.networkextension.plist")
-					)
-				)
-			)
-			(require-all
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
-				(subpath "${HOME}")
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/\.GlobalPreferences$")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
-						(subpath "${HOME}")
-					)
-				)
-			)
-		)
-	)
-)
 (allow file-read-data
 	(require-all
 		(extension "com.apple.tcc.kTCCServicePhotos")

 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
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
-				(extension "com.apple.revisiond.revision")
-			)
-		)
-	)
-)
 (allow file-read-data
 	(require-all
 		(extension "com.apple.classkit.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
-		(subpath "${HOME}")
-		(extension "com.apple.usernotifications.attachments.read-only")
-	)
-)
-(allow file-read-data
-	(require-all
-		(vnode-type SYMLINK)
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(extension "com.apple.revisiond.revision")
-			)
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
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
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/AppleInternal")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read-data
-	(require-all
-		(process-attribute is-apple-signed-executable)
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
 (allow file-read-data
 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")

 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")
-		(subpath "${HOME}")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Artwork(/|$)")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
 		)
 	)
 )
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Artwork(/|$)")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 		)
 	)
 )

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

 		(extension "com.apple.classkit.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")

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
 (allow file-read-xattr
 	(require-all
-		(extension "com.apple.fileprovider.read-write")
+		(subpath "/private/var")
 		(require-any
 			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(%entitlement-is-present "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-all
+				(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+				(process-attribute is-apple-signed-executable)
+			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/private/var/preferences/SystemConfiguration/com.apple.accounts.exists.plist")
+					(require-all
+						(%entitlement-is-present "com.apple.private.networkextension.configuration")
+						(literal "/private/var/preferences/com.apple.networkextension.plist")
+					)
+				)
+			)
+			(require-all
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
+				(subpath "${HOME}")
+			)
+			(require-all
 				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/\.GlobalPreferences$")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
+						(subpath "${HOME}")
+					)
+				)
 			)
-			(require-any
-				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-		(require-any
-			(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-			(subpath "${HOME}/Library/AddressBook")
-			(subpath "${HOME}/Library/AddressBook/Delegates")
 		)
 	)
 )

 		)
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/Library/Audio/Tunings/AID*")
+		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.fileprovider.read-write")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(require-any
+				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(require-any
+			(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+			(subpath "${HOME}/Library/AddressBook")
+			(subpath "${HOME}/Library/AddressBook/Delegates")
+		)
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(process-attribute is-apple-signed-executable)
 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(vnode-type REGULAR-FILE)
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
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
+			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(extension "com.apple.revisiond.staging")
+			)
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(vnode-type DIRECTORY SYMLINK)
+		(require-any
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
+				(extension "com.apple.revisiond.staging")
+			)
+		)
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(extension "com.apple.librarian.ubiquity-container")

 		)
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(literal "/Library/Audio/Tunings/AID*")
-		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(require-any

 		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
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
-				(extension "com.apple.revisiond.revision")
-			)
-		)
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(extension "com.apple.classkit.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
 		)
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(vnode-type SYMLINK)
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(extension "com.apple.revisiond.revision")
-			)
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
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
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/AppleInternal")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(%entitlement-is-present "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
-			)
-			(require-all
-				(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-				(process-attribute is-apple-signed-executable)
-			)
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(require-any
-					(literal "/private/var/preferences/SystemConfiguration/com.apple.accounts.exists.plist")
-					(require-all
-						(%entitlement-is-present "com.apple.private.networkextension.configuration")
-						(literal "/private/var/preferences/com.apple.networkextension.plist")
-					)
-				)
-			)
-			(require-all
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
-				(subpath "${HOME}")
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/\.GlobalPreferences$")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
-						(subpath "${HOME}")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
 (allow file-read-xattr
 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")

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

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.merchantd.identity")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.display")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
 	)
 )
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
 		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
 	)
 )
 (allow mach-lookup

 	(require-all
 		(require-not (xpc-service-name "*"))
 		(require-any
-			(global-name "com.apple.lsd.advertisingidentifiers")
-			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.tccd")
 			(require-all
 				(global-name "com.apple.system.notification_center")
 				(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 			)
+			(require-any
+				(global-name "com.apple.lsd.advertisingidentifiers")
+				(global-name "com.apple.lsd.openurl")
+			)
 		)
 	)
 )
```
