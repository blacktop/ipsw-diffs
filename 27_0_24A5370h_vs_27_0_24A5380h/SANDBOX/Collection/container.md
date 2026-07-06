## container

> Group: ⬆️ Updated

```diff

 (define (_g6 _)
 	(require-any
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com\.apple\.HomeKit/com\.apple\.Home/com\.apple\.HomeKit\.SoftwareUpdate/SoftwareUpdateDocumentation(/|$)")
 	)
 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.HomeKit/com.apple.Home/com.apple.HomeKit.SoftwareUpdate/SoftwareUpdateDocumentation")

 	(require-any
 		(_g7 "")
 		(require-all
-			(subpath "/private/var")
+			(require-any
+				(subpath "${FRONT_USER_HOME}")
+				(subpath "${HOME}")
+			)
 			(require-any
 				(_g7 "")
 				(require-all
-					(require-any
-						(subpath "${FRONT_USER_HOME}")
-						(subpath "${HOME}")
-					)
+					(subpath "/private/var")
 					(require-any
 						(_g7 "")
 						(require-all

 	(require-all
 		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
+				)
+			)
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+			)
 		)
 	)
 	(require-all

 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-				)
-			)
-			(require-any
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
-			)
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
 		)
 	)
 	(require-all

 					(_g5 "")
 					(require-all
 						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 				)
 			)

 ))
 (define (_g10 _)
 	(require-all
-	(extension-class "com.apple.quicklook.readonly")
+	(extension-class "com.apple.app-sandbox.read")
 	(extension "com.apple.sandbox.container")
 	(_g9 "")
 ))

 		)
 		(require-all
 			(signing-identifier "com.apple.mobilesafari")
-			(extension-class "com.apple.app-sandbox.read-write")
+			(extension-class "com.apple.mediaserverd.read-write")
 		)
 		(require-all
 			(signing-identifier "com.apple.safarifetcherd")
-			(extension-class "com.apple.app-sandbox.read-write")
+			(extension-class "com.apple.mediaserverd.read-write")
 		)
 		(require-all
 			(signing-identifier "com.apple.webbookmarksd")
-			(extension-class "com.apple.app-sandbox.read-write")
+			(extension-class "com.apple.mediaserverd.read-write")
 		)
 	)
 ))

 	(subpath "${HOME}/Library/CallServices/Ringtones")
 	(require-any
 		(require-all
-			(signing-identifier "com.apple.fileindexerd")
+			(signing-identifier "com.apple.FileProvider.LocalStorage")
 			(require-any
 				(require-all
-					(subpath "/private/var")
 					(require-any
 						(subpath "${FRONT_USER_HOME}")
 						(subpath "${HOME}")
 					)
+					(subpath "/private/var")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 				)
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 (define (_g24 _)
 	(require-all
 	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-	(signing-identifier "com.apple.fileindexerd")
+	(signing-identifier "com.apple.FileProvider.LocalStorage")
 ))
 (define (_g25 _)
 	(require-all

 		(require-all
 			(extension-class "com.apple.spotlight-indexable")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-			(signing-identifier "com.apple.fileindexerd")
+			(signing-identifier "com.apple.FileProvider.LocalStorage")
 		)
 		(signing-identifier "com.apple.CloudDocs.MobileDocumentsFileProvider")
 	)

 	)
 ))
 (define (_g27 _)
-	(require-all
-	(signing-identifier "com.apple.MobileSMS")
-	(require-any
-		(require-all
-			(extension-class "com.apple.quicklook.readonly")
-			(signing-identifier "com.apple.mobilecal")
-			(require-any
-				(require-all
-					(extension-class "com.apple.sharing.airdrop.readonly")
-					(require-any
-						(require-all
-							(signing-identifier "com.apple.ReplayKit.RPVideoEditorExtension")
-							(subpath "${HOME}/Library/ReplayKit")
-						)
-						(require-all
-							(signing-identifier "com.apple.SharingUI.ShareSheet")
-							(extension "com.apple.sharing.airdrop.readonly")
-						)
-					)
-				)
-				(subpath "${HOME}/Library/Calendar")
-			)
-		)
-		(subpath "${HOME}/Library/SMS/Attachments")
-	)
-))
-(define (_g28 _)
 	(require-all
 	(extension-class "com.apple.sharing.airdrop.readonly")
 	(require-any

 		)
 	)
 ))
-(define (_g29 _)
+(define (_g28 _)
 	(require-any
-	(_g28 "")
+	(_g27 "")
 	(subpath "${HOME}/Library/Calendar")
 ))
-(define (_g30 _)
+(define (_g29 _)
 	(require-all
 	(extension-class "com.apple.quicklook.readonly")
 	(signing-identifier "com.apple.mobilecal")
-	(_g29 "")
+	(_g28 "")
+))
+(define (_g30 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+	(extension-class "com.apple.mediaserverd.read-write")
 ))
 (define (_g31 _)
 	(require-all
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-	(extension-class "com.apple.quicklook.readonly")
+	(subpath "${FRONT_USER_HOME}")
+	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 ))
 (define (_g32 _)
 	(require-all
 	(subpath "/private/var/PersonaVolumes")
-	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	(require-any
+		(_g31 "")
+		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
 ))
 (define (_g33 _)
 	(require-all

 	)
 ))
 (define (_g34 _)
-	(require-all
-	(subpath "/private/var/PersonaVolumes")
-	(require-any
-		(_g33 "")
-		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
-))
-(define (_g35 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any

 		(require-all
 			(subpath "/private/var")
 			(require-any
+				(_g32 "")
 				(_g33 "")
-				(_g34 "")
 				(require-all
-					(subpath "${FRONT_USER_HOME}")
+					(subpath "/private/var/PersonaVolumes")
 					(require-any
-						(_g34 "")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+						(_g33 "")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 					)
 				)
 			)
 		)
 	)
 ))
-(define (_g36 _)
+(define (_g35 _)
 	(require-any
+	(_g31 "")
 	(_g32 "")
-	(_g33 "")
+))
+(define (_g36 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+	(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 ))
 (define (_g37 _)
 	(require-all

 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(extension-class "com.apple.quicklook.readonly")
+		(extension-class "com.apple.mediaserverd.read-write")
 	)
 	(require-all
 		(extension "com.apple.app-sandbox.read-write")

 		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Mobile Documents")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 			(require-all
 				(subpath "/private/var")

 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 			(require-all
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 		)
 	)
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(_g31 "")
-			(_g35 "")
+			(_g30 "")
+			(_g34 "")
 			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
 			(require-all
 				(extension-class "com.apple.aned.read-only")
 				(subpath "/private/var")
-				(_g36 "")
+				(_g35 "")
 			)
 			(require-all
 				(extension-class "com.apple.app-sandbox.read")
 				(subpath "/private/var")
-				(_g36 "")
+				(_g35 "")
 			)
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g31 "")
+					(_g30 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
 						(require-any
-							(_g31 "")
+							(_g30 "")
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)

 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g35 "")
+					(_g34 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(_g35 "")
+							(_g34 "")
 							(require-all
 								(subpath "${FRONT_USER_HOME}")
 								(require-any

 			(_g11 "")
 			(_g15 "")
 			(require-all
-				(extension-class "com.apple.app-sandbox.read")
+				(extension-class "com.apple.mediaserverd.read")
 				(extension "com.apple.sandbox.container")
 				(_g9 "")
 			)
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.quicklook.readonly")
 				(extension "com.apple.sandbox.container")
 				(_g9 "")
 			)

 				(extension "com.apple.sandbox.container")
 				(_g9 "")
 			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(require-any
+					(_g15 "")
+					(require-all
+						(subpath "/private/var")
+						(require-any
+							(_g15 "")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
+						)
+					)
+				)
+			)
 			(require-all
 				(subpath "/private/var")
 				(require-any

 					)
 				)
 			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(_g15 "")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(_g15 "")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-						)
-					)
-				)
-			)
 		)
 	)
 	(require-all

 	)
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(extension "com.apple.sandbox.executable")
-			(require-all
-				(signing-identifier "com.apple.mobilemail")
-				(subpath "${HOME}/Media/Purchases")
-			)
-		)
-	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(signing-identifier "com.apple.fileindexerd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(signing-identifier "com.apple.mobilemail")
-		(subpath "${HOME}/Media/Purchases")
-	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/Mail")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
-				)
-				(signing-identifier "com.apple.PosterBoard")
-			)
-			(signing-identifier "com.apple.mobilemail")
-		)
-	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.FileProvider.LocalStorage")
-	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")
-		(signing-identifier "com.apple.SafariViewService")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(extension "com.apple.app-sandbox.read-write")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
-		)
-		(extension "com.apple.odr-assets")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(signing-identifier "com.apple.fileindexerd")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(signing-identifier "com.apple.mobilemail")
-		(subpath "${HOME}/Media/Purchases")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/Mail")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
-				)
-				(signing-identifier "com.apple.PosterBoard")
-			)
-			(signing-identifier "com.apple.mobilemail")
-		)
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Media/Purchases")
-		(%entitlement-is-bool-true "com.apple.media.ringtones.read-write")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.FileProvider.LocalStorage")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")
-		(signing-identifier "com.apple.SafariViewService")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(extension "com.apple.app-sandbox.read-write")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/Mail")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
-				)
-				(signing-identifier "com.apple.PosterBoard")
-			)
-			(signing-identifier "com.apple.mobilemail")
-		)
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Media/Purchases")
-		(%entitlement-is-bool-true "com.apple.media.ringtones.read-write")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.FileProvider.LocalStorage")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")
-		(signing-identifier "com.apple.SafariViewService")
-	)
-	(require-all
-		(extension-class "com.apple.identityservices.send")
-		(require-any
-			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
-				(require-any
-					(require-any
-						(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-						(signing-identifier "com.apple.shortcuts.watch")
-					)
-					(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
-					(signing-identifier "com.apple.shortcuts")
-				)
-			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.shortcuts")
-			)
-		)
-	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(_g16 "")
 			(require-all

 		)
 	)
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(_g17 "")
 			(_g19 "")

 		)
 	)
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(_g21 "")
-			(require-all
-				(signing-identifier "com.apple.mobilemail")
-				(require-any
-					(_g21 "")
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-				)
-			)
-		)
-	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(_g22 "")
 			(_g23 "")

 			)
 		)
 	)
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(_g36 "")
+			(require-all
+				(extension "com.apple.assets.read")
+				(require-any
+					(_g36 "")
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(extension "com.apple.sandbox.executable")
+			(require-all
+				(signing-identifier "com.apple.mobilemail")
+				(subpath "${HOME}/Media/Purchases")
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.aned.read-only")
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
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(extension "com.apple.app-sandbox.read-write")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(require-any
+			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+		)
+		(extension "com.apple.odr-assets")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(signing-identifier "com.apple.mobilemail")
+		(subpath "${HOME}/Media/Purchases")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "${HOME}/Library/Mail")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
+				)
+				(signing-identifier "com.apple.PosterBoard")
+			)
+			(signing-identifier "com.apple.mobilemail")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "${HOME}/Media/Purchases")
+		(%entitlement-is-bool-true "com.apple.media.ringtones.read-write")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")
+		(signing-identifier "com.apple.SafariViewService")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(extension "com.apple.app-sandbox.read-write")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "${HOME}/Library/Mail")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
+				)
+				(signing-identifier "com.apple.PosterBoard")
+			)
+			(signing-identifier "com.apple.mobilemail")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "${HOME}/Media/Purchases")
+		(%entitlement-is-bool-true "com.apple.media.ringtones.read-write")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")
+		(signing-identifier "com.apple.SafariViewService")
+	)
+	(require-all
+		(extension-class "com.apple.identityservices.send")
+		(require-any
+			(require-all
+				(subpath "${PROCESS_TEMP_DIR}")
+				(require-any
+					(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+					(signing-identifier "com.apple.shortcuts.watch")
+				)
+			)
+			(require-all
+				(subpath "/private/var/tmp")
+				(require-any
+					(require-any
+						(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+						(signing-identifier "com.apple.shortcuts.watch")
+					)
+					(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+					(signing-identifier "com.apple.shortcuts")
+				)
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(_g21 "")
+			(require-all
+				(signing-identifier "com.apple.mobilemail")
+				(require-any
+					(_g21 "")
+					(extension "com.apple.security.exception.files.absolute-path.read-only")
+					(extension "com.apple.security.exception.files.absolute-path.read-write")
+					(extension "com.apple.security.exception.files.home-relative-path.read-only")
+					(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				)
+			)
+		)
+	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any

 			(extension "com.apple.security.exception.files.home-relative-path.read-write")
 		)
 	)
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
-			)
-		)
-	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any

 			)
 		)
 	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(signing-identifier "com.apple.FileProvider.LocalStorage")
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-				(signing-identifier "com.apple.FileProvider.LocalStorage")
-			)
-		)
-	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any

 	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
-		(signing-identifier "com.apple.fileindexerd")
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
 		)
 	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(signing-identifier "com.apple.mobilemail")
+		(subpath "${HOME}/Media/Purchases")
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Mail")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
+				)
+				(signing-identifier "com.apple.PosterBoard")
+			)
+			(signing-identifier "com.apple.mobilemail")
+		)
+	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(subpath "/private/var")

 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
 	)
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.security.exception.files.home-relative-path.read-write")
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")
+		(signing-identifier "com.apple.SafariViewService")
 	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 			)
 		)
 	)
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+		)
+	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any

 	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/Mail")
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
 		(require-any
 			(require-all
 				(require-any
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
 				)
-				(signing-identifier "com.apple.PosterBoard")
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
-			(signing-identifier "com.apple.mobilemail")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
 		)
 	)
 	(require-all

 		(subpath "${HOME}/Media/Purchases")
 		(%entitlement-is-bool-true "com.apple.media.ringtones.read-write")
 	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.FileProvider.LocalStorage")
-	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")

 		(extension-class "com.apple.sharing.airdrop.readonly")
 		(extension "com.apple.app-sandbox.read-write")
 	)
+	(require-all
+		(extension-class "com.apple.sharing.airdrop.readonly")
+		(require-any
+			(_g29 "")
+			(require-all
+				(extension-class "com.apple.sharing.airdrop.readonly")
+				(require-any
+					(_g27 "")
+					(require-all
+						(signing-identifier "com.apple.mobilecal")
+						(_g28 "")
+					)
+				)
+			)
+			(require-all
+				(signing-identifier "com.apple.MobileSMS")
+				(require-any
+					(_g29 "")
+					(subpath "${HOME}/Library/SMS/Attachments")
+				)
+			)
+		)
+	)
 	(require-all
 		(extension-class "com.apple.sharing.airdrop.readonly")
 		(require-any

 			)
 		)
 	)
-	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
-		(signing-identifier "com.apple.MobileSMS")
-		(require-any
-			(require-all
-				(extension-class "com.apple.quicklook.readonly")
-				(signing-identifier "com.apple.mobilecal")
-				(require-any
-					(require-all
-						(extension-class "com.apple.sharing.airdrop.readonly")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.ReplayKit.RPVideoEditorExtension")
-								(subpath "${HOME}/Library/ReplayKit")
-							)
-							(require-all
-								(signing-identifier "com.apple.SharingUI.ShareSheet")
-								(extension "com.apple.sharing.airdrop.readonly")
-							)
-						)
-					)
-					(subpath "${HOME}/Library/Calendar")
-				)
-			)
-			(subpath "${HOME}/Library/SMS/Attachments")
-		)
-	)
 	(require-all
 		(extension-class "com.apple.spotlight-indexable")
 		(process-attribute is-apple-signed-executable)

 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
-						(signing-identifier "com.apple.fileindexerd")
-					)
-				)
-			)
-		)
-	)
-	(require-all
-		(extension-class "com.apple.spotlight-indexable")
-		(require-any
-			(_g27 "")
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(_g27 "")
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
+							(extension-class "com.apple.aned.read-only")
+							(signing-identifier "com.apple.FileProvider.LocalStorage")
 						)
-						(signing-identifier "com.apple.FileProvider.LocalStorage")
 					)
 				)
 			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-				(signing-identifier "com.apple.FileProvider.LocalStorage")
-			)
 		)
 	)
 	(require-all
 		(extension-class "com.apple.spotlight-indexable")
+		(signing-identifier "com.apple.MobileSMS")
 		(require-any
-			(_g30 "")
 			(require-all
-				(extension-class "com.apple.sharing.airdrop.readonly")
+				(extension-class "com.apple.quicklook.readonly")
+				(signing-identifier "com.apple.mobilecal")
 				(require-any
-					(_g28 "")
 					(require-all
-						(signing-identifier "com.apple.mobilecal")
-						(_g29 "")
+						(extension-class "com.apple.sharing.airdrop.readonly")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.ReplayKit.RPVideoEditorExtension")
+								(subpath "${HOME}/Library/ReplayKit")
+							)
+							(require-all
+								(signing-identifier "com.apple.SharingUI.ShareSheet")
+								(extension "com.apple.sharing.airdrop.readonly")
+							)
+						)
 					)
+					(subpath "${HOME}/Library/Calendar")
 				)
 			)
-			(require-all
-				(signing-identifier "com.apple.MobileSMS")
-				(require-any
-					(_g30 "")
-					(subpath "${HOME}/Library/SMS/Attachments")
-				)
-			)
+			(subpath "${HOME}/Library/SMS/Attachments")
 		)
 	)
 	(require-all

 	)
 	(require-all
 		(subpath "${HOME}/Media/Books")
-		(extension-class "com.apple.quicklook.readonly")
-		(signing-identifier "com.apple.itunesu")
-	)
-	(require-all
-		(subpath "${HOME}/Media/Podcasts")
 		(require-any
 			(require-all
 				(extension-class "com.apple.app-sandbox.read")

 			)
 		)
 	)
+	(require-all
+		(subpath "${HOME}/Media/Podcasts")
+		(extension-class "com.apple.app-sandbox.read")
+		(signing-identifier "com.apple.itunesu")
+	)
 	(require-all
 		(subpath "/Library/Ringtones")
 		(require-any

 		)
 	)
 )
+(allow file-map-executable
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-map-executable
+	(require-all
+		(signing-identifier "com.apple.MobileSMS")
+		(subpath "/Applications/AppStore.app/Frameworks")
+	)
+)
 (allow file-map-executable
 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")

 		)
 	)
 )
-(allow file-map-executable
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
-(allow file-map-executable
-	(require-all
-		(signing-identifier "com.apple.MobileSMS")
-		(require-any
-			(subpath "/Applications/AppStore.app/Frameworks")
-			(subpath "/usr/appleinternal/lib/sanitizers")
-		)
-	)
-)
 (allow file-map-executable
 	(require-all
 		(system-attribute carrier-build)

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

 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(%entitlement-is-present "com.apple.private.oop-jit.loader")
+		(subpath "/private/var/OOPJit/${ENTITLEMENT:com.apple.private.oop-jit.loader}")
 	)
 )
 (allow file-read*
 	(require-all
-		(%entitlement-is-present "com.apple.private.oop-jit.loader")
-		(subpath "/private/var/OOPJit/${ENTITLEMENT:com.apple.private.oop-jit.loader}")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
 	)
 )
 (allow file-read*

 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-							(require-any
-								(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-								(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-							)
 						)
 					)
 					(require-all

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-									(require-any
-										(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-										(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-									)
 								)
 							)
 						)
 					)
-					(require-any
-						(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-						(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-					)
 				)
 			)
 			(require-any

 )
 (allow file-read*
 	(require-all
-		(subpath "${HOME}/Media/Books")
+		(subpath "${HOME}/Media/Podcasts")
 		(signing-identifier "com.apple.itunesu")
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "${HOME}/Media/Podcasts")
+		(subpath "${HOME}/Media/Books")
 		(signing-identifier "com.apple.itunesu")
 	)
 )

 		(extension "com.apple.clouddocs.version")
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService(/|$)")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(signing-identifier "com.apple.SafariViewService")
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")

 		)
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService(/|$)")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(signing-identifier "com.apple.SafariViewService")
-	)
-)
 (allow file-read*
 	(require-all
 		(extension "com.apple.librarian.ubiquity-container")

 			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
 			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
 		)
-		(signing-identifier "com.apple.mobilemail")
+		(signing-identifier "com.apple.mobilenotes")
 	)
 )
 (allow file-read*

 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.CloudDocs.MobileDocumentsFileProvider")
-		(subpath "${HOME}/Library/Mobile Documents/com~apple~CloudDocs")
+		(subpath "${HOME}/Library/CallServices/Ringtones")
+		(signing-identifier "com.apple.InCallService")
 	)
 )
 (allow file-read*

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "${HOME}/Library/Mail")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${HOME}/Library/Logs/Mail")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "/private/var")

 )
 (allow file-read*
 	(require-all
-		(subpath "${HOME}/Library/Mail")
+		(subpath "${HOME}/Library/DataAccess")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
+			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
+		)
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${HOME}/Library/Calendar")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(subpath "${HOME}/Library/Logs/Mail")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/Calendar")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/DataAccess")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/CallServices/Ringtones")
-		(signing-identifier "com.apple.InCallService")
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
-			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
-		)
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 		(signing-identifier "com.apple.PreviewShell")
 	)
 )
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.iStreamer")
-		(literal "/AppleInternal/Library/Frameworks/CoreAutomation*")
-	)
-)
 (allow file-read*
 	(require-all
 		(subpath "/private/var")

 		(subpath "${HOME}/Library/DeviceRegistry")
 	)
 )
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.iStreamer")
+		(literal "/AppleInternal/Library/Frameworks/CoreAutomation*")
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "${HOME}/Library/BulletinDistributor/Attachments")

 )
 (allow file-read*
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
-			(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-			(subpath "${HOME}/Library/AddressBook")
-			(subpath "${HOME}/Library/AddressBook/Delegates")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAppPopover")
-			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAvocado")
-			(signing-identifier "com.apple.DocumentManagerUICore.SaveToFiles")
-		)
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
+			(signing-identifier "com.apple.DocumentManagerUICore.Service")
+			(signing-identifier "com.apple.DocumentsApp")
 		)
+		(subpath "/AppleInternal/Applications")
 	)
 )
 (allow file-read*

 		)
 	)
 )
+(allow file-read*
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
 (allow file-read*
 	(require-all
 		(subpath "/private/var")

 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		(signing-identifier "com.apple.CloudDocs.MobileDocumentsFileProvider")
+		(subpath "${HOME}/Library/Mobile Documents/com~apple~CloudDocs")
 	)
 )
 (allow file-read*

 )
 (allow file-read*
 	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+		(literal "/Library/Audio/Tunings/AID*")
+		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
 	)
 )
 (allow file-read*
 	(require-all
-		(literal "/Library/Audio/Tunings/AID*")
-		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(extension "com.apple.clouddocs.version")
 	)
 )
 (allow file-read*

 		(extension "com.apple.clouddocs.version")
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/com.apple.wifi.plist")
-		(process-attribute is-apple-signed-executable)
-	)
-)
 (allow file-read*
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
 (allow file-read*
 	(require-all
-		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.tcc.kTCCServicePhotos")
-		(require-any
-			(literal "${HOME}/Media/PhotoData/syncInfo.plist")
-			(require-any
-				(subpath "${HOME}/Media/PhotoData/CPLAssets")
-				(subpath "${HOME}/Media/PhotoData/Metadata")
-				(subpath "${HOME}/Media/PhotoData/Mutations")
-				(subpath "${HOME}/Media/PhotoData/Sync")
-				(subpath "${HOME}/Media/PhotoData/Thumbnails")
-			)
-			(subpath "${HOME}/Media/DCIM")
-			(subpath "${HOME}/Media/PhotoData/PhotoCloudSharingData")
-			(subpath "${HOME}/Media/PhotoStreamsData")
+			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
 		)
+		(extension "com.apple.odr-assets")
 	)
 )
 (allow file-read*

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.tcc.kTCCServicePhotos")
+		(require-any
+			(literal "${HOME}/Media/PhotoData/syncInfo.plist")
+			(require-any
+				(subpath "${HOME}/Media/PhotoData/CPLAssets")
+				(subpath "${HOME}/Media/PhotoData/Metadata")
+				(subpath "${HOME}/Media/PhotoData/Mutations")
+				(subpath "${HOME}/Media/PhotoData/Sync")
+				(subpath "${HOME}/Media/PhotoData/Thumbnails")
+			)
+			(subpath "${HOME}/Media/DCIM")
+			(subpath "${HOME}/Media/PhotoData/PhotoCloudSharingData")
+			(subpath "${HOME}/Media/PhotoStreamsData")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/SystemConfiguration/com.apple.wifi.plist")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read*
 	(require-all
 		(system-attribute internal-build)

 )
 (allow file-read*
 	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
 		)
-		(extension "com.apple.odr-assets")
 	)
 )
 (allow file-read*

 		(subpath "${HOME}/Library/Safari")
 		(require-any
 			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilenotes")
 			(signing-identifier "com.apple.mobilesafari")
 			(signing-identifier "com.apple.safarifetcherd")
 			(signing-identifier "com.apple.webbookmarksd")

 )
 (allow file-read*
 	(require-all
-		(literal "${HOME}/Library/SpringBoard/OriginalLockVideo.mov")
+		(literal "${HOME}/Library/SpringBoard/OriginalHomeVideo.mov")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.system.get-wallpaper")
 			(signing-identifier "com.apple.itunesu")
 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.mobilemail")
+		(require-any
+			(literal "${HOME}/Library/Preferences/com.apple.AOSNotification.launchd")
+			(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.mobilemail*")
+				(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.mobilemail*")
+			)
+			(require-any
+				(literal "/System/Library/PairedSyncServices/com.apple.pairedsync.mail.plist")
+				(literal "/private/var/preferences/SystemConfiguration/com.apple.AutoWake.plist")
+				(subpath "/Library/Application Support/Mail/Plugins")
+			)
+			(subpath "${HOME}/Library/Caches/DataAccess")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${HOME}/Media/Safari")
+		(require-any
+			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilesafari")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${HOME}/Library/WebClips")
+		(require-any
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.webapp")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAppPopover")
+			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAvocado")
+			(signing-identifier "com.apple.DocumentManagerUICore.SaveToFiles")
+		)
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Bundle/Application")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${HOME}/Library/Notes")
+		(require-any
+			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilenotes")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.PosterBoard")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/(SystemData|tmp)/com.apple.posterkit.provider(/|$)")
+			)
+			(require-any
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.chrono.WidgetRenderer-*")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com.apple.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))")
+			)
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+			)
+		)
+	)
+)
+(allow file-read*
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
 (allow file-read*
 	(require-all
 		(literal "${HOME}/Library/Cookies/com.apple.itunesstored*")

 )
 (allow file-read*
 	(require-all
-		(subpath "/System/Library/Carrier Bundles")
+		(subpath "${HOME}/Library/Cookies")
 		(require-any
-			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.Service")
-			(signing-identifier "com.apple.DocumentsApp")
-		)
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Bundle/Application")
-			(subpath "/private/var/containers/Bundle")
+			(signing-identifier "com.apple.Safari.SocialHelper")
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.safarifetcherd")
+			(signing-identifier "com.apple.webbookmarksd")
 		)
 	)
 )

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.iBooks")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 									(require-all
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 										(subpath "${HOME}")

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.iBooks")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+								)
+							)
 							(require-all
 								(signing-identifier "com.apple.mobilemail")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 						)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.iBooks")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 								(subpath "${HOME}")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.iBooks")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+						)
+					)
 					(require-all
 						(signing-identifier "com.apple.mobilemail")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 				)

 		)
 	)
 )
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.chrono.WidgetRenderer-*")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com.apple.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))")
-			)
-			(require-any
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-			)
-		)
-	)
-)
-(allow file-read*
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
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/WebClips")
-		(require-any
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.webapp")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Media/Safari")
-		(require-any
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.mobilesafari")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/Cookies")
-		(require-any
-			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.safarifetcherd")
-			(signing-identifier "com.apple.webbookmarksd")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.mobilemail")
-		(require-any
-			(literal "${HOME}/Library/Preferences/com.apple.AOSNotification.launchd")
-			(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection/com.apple.mobilemail*")
-				(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection/com.apple.mobilemail*")
-			)
-			(require-any
-				(literal "/System/Library/PairedSyncServices/com.apple.pairedsync.mail.plist")
-				(literal "/private/var/preferences/SystemConfiguration/com.apple.AutoWake.plist")
-				(subpath "/Library/Application Support/Mail/Plugins")
-			)
-			(subpath "${HOME}/Library/Caches/DataAccess")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/Notes")
-		(require-any
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.mobilenotes")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.PosterBoard")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/(SystemData|tmp)/com.apple.posterkit.provider(/|$)")
-			)
-			(require-any
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
-			)
-		)
-	)
-)
 (allow file-read*
 	(require-all
 		(process-attribute is-apple-signed-executable)

 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.FileProvider.LocalStorage")
+		(subpath "/System/Library/Carrier Bundles")
 		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 		)
 	)
 )

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.iBooks")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 									(require-all
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 										(subpath "${HOME}")

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.iBooks")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+								)
+							)
 							(require-all
 								(signing-identifier "com.apple.mobilemail")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 						)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.iBooks")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 								(subpath "${HOME}")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.iBooks")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+						)
+					)
 					(require-all
 						(signing-identifier "com.apple.mobilemail")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 				)

 )
 (allow file-read-data
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(%entitlement-is-present "com.apple.private.oop-jit.loader")
+		(subpath "/private/var/OOPJit/${ENTITLEMENT:com.apple.private.oop-jit.loader}")
 	)
 )
 (allow file-read-data
 	(require-all
-		(%entitlement-is-present "com.apple.private.oop-jit.loader")
-		(subpath "/private/var/OOPJit/${ENTITLEMENT:com.apple.private.oop-jit.loader}")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
 	)
 )
 (allow file-read-data

 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-							(require-any
-								(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-								(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-							)
 						)
 					)
 					(require-all

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-									(require-any
-										(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-										(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-									)
 								)
 							)
 						)
 					)
-					(require-any
-						(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-						(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-					)
 				)
 			)
 			(require-any

 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Media/Books")
+		(subpath "${HOME}/Media/Podcasts")
 		(signing-identifier "com.apple.itunesu")
 	)
 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Media/Podcasts")
+		(subpath "${HOME}/Media/Books")
 		(signing-identifier "com.apple.itunesu")
 	)
 )

 		(extension "com.apple.clouddocs.version")
 	)
 )
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService(/|$)")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(signing-identifier "com.apple.SafariViewService")
+	)
+)
 (allow file-read-data
 	(require-all
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")

 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService(/|$)")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(signing-identifier "com.apple.SafariViewService")
-	)
-)
 (allow file-read-data
 	(require-all
 		(extension "com.apple.librarian.ubiquity-container")

 			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
 			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
 		)
-		(signing-identifier "com.apple.mobilemail")
+		(signing-identifier "com.apple.mobilenotes")
 	)
 )
 (allow file-read-data

 )
 (allow file-read-data
 	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		(signing-identifier "com.apple.CloudDocs.MobileDocumentsFileProvider")
+		(subpath "${HOME}/Library/Mobile Documents/com~apple~CloudDocs")
 	)
 )
 (allow file-read-data

 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.Maps")
-		(require-any
-			(literal "/private/var/containers/Bundle/[^/]+/[-A-Z0-9]")
-			(regex #"/private/var/containers/Bundle/[^/]+/([-A-Z0-9])+/GeoJSON")
-		)
-	)
-)
 (allow file-read-data
 	(require-all
 		(subpath "/private/var")

 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Library/CallServices/Ringtones")
-		(signing-identifier "com.apple.InCallService")
+		(subpath "${HOME}/Library/Mail")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.Maps")
+		(require-any
+			(literal "/private/var/containers/Bundle/[^/]+/[-A-Z0-9]")
+			(regex #"/private/var/containers/Bundle/[^/]+/([-A-Z0-9])+/GeoJSON")
+		)
 	)
 )
 (allow file-read-data

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(subpath "${HOME}/Library/Calendar")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
 (allow file-read-data
 	(require-all
 		(subpath "${HOME}/Library/DataAccess")

 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Library/Logs/Mail")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.CloudDocs.MobileDocumentsFileProvider")
-		(subpath "${HOME}/Library/Mobile Documents/com~apple~CloudDocs")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "${HOME}/Library/Calendar")
-		(signing-identifier "com.apple.mobilemail")
+		(subpath "${HOME}/Library/CallServices/Ringtones")
+		(signing-identifier "com.apple.InCallService")
 	)
 )
 (allow file-read-data

 		(require-any
 			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
 			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		)
 		(signing-identifier "com.apple.mobilemail")
 	)
 )
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
 (allow file-read-data
 	(require-all
 		(subpath "${HOME}/Media")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.iStreamer")
-		(literal "/AppleInternal/Library/Frameworks/CoreAutomation*")
-	)
-)
 (allow file-read-data
 	(require-all
 		(subpath "/private/var")

 		(subpath "${HOME}/Library/DeviceRegistry")
 	)
 )
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.iStreamer")
+		(literal "/AppleInternal/Library/Frameworks/CoreAutomation*")
+	)
+)
 (allow file-read-data
 	(require-all
 		(subpath "${HOME}/Library/BulletinDistributor/Attachments")

 )
 (allow file-read-data
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
-			(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-			(subpath "${HOME}/Library/AddressBook")
-			(subpath "${HOME}/Library/AddressBook/Delegates")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAppPopover")
-			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAvocado")
-			(signing-identifier "com.apple.DocumentManagerUICore.SaveToFiles")
-		)
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
+			(signing-identifier "com.apple.DocumentManagerUICore.Service")
+			(signing-identifier "com.apple.DocumentsApp")
 		)
+		(subpath "/AppleInternal/Applications")
 	)
 )
 (allow file-read-data

 		)
 	)
 )
+(allow file-read-data
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
 (allow file-read-data
 	(require-all
 		(subpath "/private/var")

 )
 (allow file-read-data
 	(require-all
-		(signing-identifier "com.apple.SharingUI.ShareSheet")
-		(extension "com.apple.sharing.airdrop.readonly")
+		(subpath "${HOME}/Library/ReplayKit")
+		(extension "com.apple.replayd.read-only")
 	)
 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Library/ReplayKit")
-		(extension "com.apple.replayd.read-only")
+		(signing-identifier "com.apple.SharingUI.ShareSheet")
+		(extension "com.apple.sharing.airdrop.readonly")
 	)
 )
 (allow file-read-data

 )
 (allow file-read-data
 	(require-all
-		(literal "/Library/Audio/Tunings/AID*")
-		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(extension "com.apple.clouddocs.version")
 	)
 )
 (allow file-read-data
 	(require-all
-		(subpath "/AppleInternal")
+		(subpath "/usr/local/lib")
 		(system-attribute carrier-build)
 	)
 )
 (allow file-read-data
 	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
-		(extension "com.apple.clouddocs.version")
+		(extension "com.apple.tcc.kTCCServicePhotos")
+		(require-any
+			(literal "${HOME}/Media/PhotoData/syncInfo.plist")
+			(require-any
+				(subpath "${HOME}/Media/PhotoData/CPLAssets")
+				(subpath "${HOME}/Media/PhotoData/Metadata")
+				(subpath "${HOME}/Media/PhotoData/Mutations")
+				(subpath "${HOME}/Media/PhotoData/Sync")
+				(subpath "${HOME}/Media/PhotoData/Thumbnails")
+			)
+			(subpath "${HOME}/Media/DCIM")
+			(subpath "${HOME}/Media/PhotoData/PhotoCloudSharingData")
+			(subpath "${HOME}/Media/PhotoStreamsData")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.classkit.read-write")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
+		)
 	)
 )
 (allow file-read-data

 )
 (allow file-read-data
 	(require-all
-		(extension "com.apple.fileprovider.read-write")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(require-any
-				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
-				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
+		(literal "/Library/Audio/Tunings/AID*")
+		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
 	)
 )
 (allow file-read-data

 )
 (allow file-read-data
 	(require-all
-		(extension "com.apple.tcc.kTCCServicePhotos")
-		(require-any
-			(literal "${HOME}/Media/PhotoData/syncInfo.plist")
-			(require-any
-				(subpath "${HOME}/Media/PhotoData/CPLAssets")
-				(subpath "${HOME}/Media/PhotoData/Metadata")
-				(subpath "${HOME}/Media/PhotoData/Mutations")
-				(subpath "${HOME}/Media/PhotoData/Sync")
-				(subpath "${HOME}/Media/PhotoData/Thumbnails")
-			)
-			(subpath "${HOME}/Media/DCIM")
-			(subpath "${HOME}/Media/PhotoData/PhotoCloudSharingData")
-			(subpath "${HOME}/Media/PhotoStreamsData")
-		)
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
 	)
 )
 (allow file-read-data
 	(require-all
-		(extension "com.apple.classkit.read-write")
+		(extension "com.apple.fileprovider.read-write")
 		(require-any
 			(require-all
 				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/ClassKit(/|$)")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Data/[^/]+/[^/]+/Library/Application Support/Collaboration/com.apple.iWork/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(require-any
+				(subpath "${ANY_USER_HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd")
+				(subpath "${ANY_USER_HOME}/tmp/com.apple.fileproviderd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.fileproviderd")
 			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit")
 		)
 	)
 )

 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Library/Mail")
+		(subpath "${HOME}/Library/Logs/Mail")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Library/Notes")
 		(require-any
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.mobilenotes")
+			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAppPopover")
+			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAvocado")
+			(signing-identifier "com.apple.DocumentManagerUICore.SaveToFiles")
+		)
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Bundle/Application")
+			(subpath "/private/var/containers/Bundle")
 		)
 	)
 )

 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Library/Cookies")
+		(subpath "/System/Library/Carrier Bundles")
 		(require-any
-			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.safarifetcherd")
-			(signing-identifier "com.apple.webbookmarksd")
+			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 		)
 	)
 )
 (allow file-read-data
 	(require-all
-		(subpath "${HOME}/Library/WebClips")
+		(signing-identifier "com.apple.PosterBoard")
 		(require-any
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.webapp")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "${HOME}/Library/Cookies/com.apple.itunesstored*")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.container2")
-			(signing-identifier "com.apple.iBooks")
-			(signing-identifier "com.apple.itunesu")
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.webbookmarksd")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/(SystemData|tmp)/com.apple.posterkit.provider(/|$)")
+			)
+			(require-any
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
+			)
 		)
 	)
 )

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.iBooks")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 									(require-all
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 										(subpath "${HOME}")

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.iBooks")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+								)
+							)
 							(require-all
 								(signing-identifier "com.apple.mobilemail")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 						)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.iBooks")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 								(subpath "${HOME}")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.iBooks")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+						)
+					)
 					(require-all
 						(signing-identifier "com.apple.mobilemail")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 				)

 )
 (allow file-read-data
 	(require-all
-		(signing-identifier "com.apple.FileProvider.LocalStorage")
+		(subpath "${HOME}/Library/Notes")
 		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.Service")
-			(signing-identifier "com.apple.DocumentsApp")
-		)
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Bundle/Application")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.chrono.WidgetRenderer-*")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com.apple.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))")
-			)
-			(require-any
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "${HOME}/Library/Safari")
-		(require-any
-			(signing-identifier "com.apple.Safari.SocialHelper")
 			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.safarifetcherd")
-			(signing-identifier "com.apple.webbookmarksd")
+			(signing-identifier "com.apple.mobilenotes")
 		)
 	)
 )
 (allow file-read-data
 	(require-all
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
-(allow file-read-data
-	(require-all
-		(literal "${HOME}/Library/SpringBoard/OriginalLockVideo.mov")
+		(literal "${HOME}/Library/SpringBoard/OriginalHomeVideo.mov")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.system.get-wallpaper")
 			(signing-identifier "com.apple.itunesu")

 )
 (allow file-read-data
 	(require-all
-		(signing-identifier "com.apple.PosterBoard")
+		(literal "${HOME}/Library/Cookies/com.apple.itunesstored*")
 		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/(SystemData|tmp)/com.apple.posterkit.provider(/|$)")
-			)
-			(require-any
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.posterkit.provider")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.posterkit.provider")
-			)
+			(%entitlement-is-bool-true "com.apple.container2")
+			(signing-identifier "com.apple.iBooks")
+			(signing-identifier "com.apple.itunesu")
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.webbookmarksd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "${HOME}/Library/Cookies")
+		(require-any
+			(signing-identifier "com.apple.Safari.SocialHelper")
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.safarifetcherd")
+			(signing-identifier "com.apple.webbookmarksd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "${HOME}/Library/Safari")
+		(require-any
+			(signing-identifier "com.apple.Safari.SocialHelper")
+			(signing-identifier "com.apple.mobilenotes")
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.safarifetcherd")
+			(signing-identifier "com.apple.webbookmarksd")
 		)
 	)
 )

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(subpath "${HOME}/Library/WebClips")
+		(require-any
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.webapp")
+		)
+	)
+)
 (allow file-read-data
 	(require-all
 		(signing-identifier "com.apple.mobilemail")

 		)
 	)
 )
+(allow file-read-data
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
+(allow file-read-data
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
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.chrono.WidgetRenderer-*")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com.apple.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))")
+			)
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+			)
+		)
+	)
+)
 (allow file-read-data
 	(require-all
 		(process-attribute is-apple-signed-executable)

 )
 (allow file-read-data
 	(require-all
-		(subpath "/System/Library/Carrier Bundles")
+		(signing-identifier "com.apple.FileProvider.LocalStorage")
 		(require-any
-			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
 		)
 	)
 )

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

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.iBooks")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 									(require-all
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 										(subpath "${HOME}")

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.iBooks")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+								)
+							)
 							(require-all
 								(signing-identifier "com.apple.mobilemail")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 						)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.iBooks")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 								(subpath "${HOME}")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.iBooks")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+						)
+					)
 					(require-all
 						(signing-identifier "com.apple.mobilemail")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 				)

 )
 (allow file-read-metadata
 	(require-all
-		(%entitlement-is-present "com.apple.private.oop-jit.loader")
-		(subpath "/private/var/OOPJit/${ENTITLEMENT:com.apple.private.oop-jit.loader}")
+		(%entitlement-is-present "com.apple.developer.cellular-logging.allow")
+		(literal "/AppleInternal/Library/Frameworks/CellularLogging.framework*")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "${HOME}/Media/Books")
+		(subpath "${HOME}/Media/Podcasts")
 		(signing-identifier "com.apple.itunesu")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "${HOME}/Media/Podcasts")
+		(subpath "${HOME}/Media/Books")
 		(signing-identifier "com.apple.itunesu")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(%entitlement-is-present "com.apple.developer.cellular-logging.allow")
-		(literal "/AppleInternal/Library/Frameworks/CellularLogging.framework*")
+		(%entitlement-is-present "com.apple.private.oop-jit.loader")
+		(subpath "/private/var/OOPJit/${ENTITLEMENT:com.apple.private.oop-jit.loader}")
 	)
 )
 (allow file-read-metadata

 		(signing-identifier "com.apple.Music")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Library/Calendar")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/(NanoMail|PairedSyncServiceRestrictions)($|/)")
+		(subpath "${FRONT_USER_HOME}")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
+			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
+		)
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Library/Logs/Mail")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "${HOME}/Library/DataAccess")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(require-any
+			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
+			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
+		)
+		(signing-identifier "com.apple.mobilenotes")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Media")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(signing-identifier "com.apple.Maps")

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "${HOME}/Library/Calendar")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read-metadata
-	(require-all
+		(signing-identifier "com.apple.mobilesafari")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
-			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+			(subpath "${HOME}/Library/Caches/com.apple.parsecd/CustomFeedback/SafariAutoFill")
+			(subpath "${HOME}/Library/Caches/com.apple.parsecd/CustomFeedback/SafariAutoPlay")
 		)
-		(signing-identifier "com.apple.mobilemail")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/(NanoMail|PairedSyncServiceRestrictions)($|/)")
-		(subpath "${FRONT_USER_HOME}")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Library/Logs/Mail")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Media")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(require-any
-			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
-			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
-		)
-		(signing-identifier "com.apple.mobilemail")
+		(signing-identifier "com.apple.SharingUI.ShareSheet")
+		(extension "com.apple.sharing.airdrop.readonly")
 	)
 )
 (allow file-read-metadata

 		(signing-identifier "com.apple.InCallService")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.mobilesafari")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.parsecd/CustomFeedback/SafariAutoFill")
-			(subpath "${HOME}/Library/Caches/com.apple.parsecd/CustomFeedback/SafariAutoPlay")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(signing-identifier "com.apple.MobileSMS")
 		(subpath "/Applications/AppStore.app/Frameworks")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.SharingUI.ShareSheet")
-		(extension "com.apple.sharing.airdrop.readonly")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 )
 (allow file-read-metadata
 	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
 		)
-		(extension "com.apple.odr-assets")
 	)
 )
 (allow file-read-metadata

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
-		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
+			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
 		)
+		(extension "com.apple.odr-assets")
 	)
 )
 (allow file-read-metadata

 		(process-attribute is-apple-signed-executable)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/AppleInternal")

 		(extension "com.apple.clouddocs.version")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Library/BulletinDistributor/Attachments")
-		(extension "com.apple.bulletindistributor.attachments.read-only")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(signing-identifier "com.apple.Bridge")

 (allow file-read-metadata
 	(require-all
 		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAppPopover")
-			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAvocado")
-			(signing-identifier "com.apple.DocumentManagerUICore.SaveToFiles")
-		)
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
+			(signing-identifier "com.apple.DocumentManagerUICore.Service")
+			(signing-identifier "com.apple.DocumentsApp")
 		)
+		(subpath "/AppleInternal/Applications")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Library/BulletinDistributor/Attachments")
+		(extension "com.apple.bulletindistributor.attachments.read-only")
 	)
 )
 (allow file-read-metadata

 		(extension "com.apple.Pasteboard-readonly")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.iStreamer")
-		(literal "/AppleInternal/Library/Frameworks/CoreAutomation*")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.sandbox.container")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(signing-identifier "com.apple.iStreamer")
+		(literal "/AppleInternal/Library/Frameworks/CoreAutomation*")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Library/Safari")
+		(require-any
+			(signing-identifier "com.apple.Safari.SocialHelper")
+			(signing-identifier "com.apple.mobilenotes")
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.safarifetcherd")
+			(signing-identifier "com.apple.webbookmarksd")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(require-any

 		(signing-identifier "com.apple.chrono.WidgetRenderer-*")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com.apple.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))")
 			)
 			(require-any

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(literal "${HOME}/Library/SpringBoard/OriginalLockVideo.mov")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.system.get-wallpaper")
-			(signing-identifier "com.apple.itunesu")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(literal "${HOME}/Library/Cookies/com.apple.itunesstored*")

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Library/WebClips")
-		(require-any
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.webapp")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.Service")
-			(signing-identifier "com.apple.DocumentsApp")
-		)
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Bundle/Application")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Media/Safari")
-		(require-any
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.mobilesafari")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(extension "com.apple.tcc.kTCCServicePhotos")
-		(require-any
-			(literal "${HOME}/Media/PhotoData/syncInfo.plist")
-			(require-any
-				(subpath "${HOME}/Media/PhotoData/CPLAssets")
-				(subpath "${HOME}/Media/PhotoData/Metadata")
-				(subpath "${HOME}/Media/PhotoData/Mutations")
-				(subpath "${HOME}/Media/PhotoData/Sync")
-				(subpath "${HOME}/Media/PhotoData/Thumbnails")
-			)
-			(subpath "${HOME}/Media/DCIM")
-			(subpath "${HOME}/Media/PhotoData/PhotoCloudSharingData")
-			(subpath "${HOME}/Media/PhotoStreamsData")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Library/Cookies")
-		(require-any
-			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.safarifetcherd")
-			(signing-identifier "com.apple.webbookmarksd")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Library/Safari")
-		(require-any
-			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.safarifetcherd")
-			(signing-identifier "com.apple.webbookmarksd")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-							(require-any
-								(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-								(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-									(require-any
-										(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-										(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-									)
-								)
-							)
-						)
-					)
-					(require-any
-						(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-						(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-					)
-				)
-			)
-			(require-any
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-				(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-			)
-			(require-any
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
-			)
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Library/Cookies")
+		(require-any
+			(signing-identifier "com.apple.Safari.SocialHelper")
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.safarifetcherd")
+			(signing-identifier "com.apple.webbookmarksd")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Media/Safari")
+		(require-any
+			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilesafari")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Library/WebClips")
+		(require-any
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.webapp")
+		)
+	)
+)
+(allow file-read-metadata
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
+(allow file-read-metadata
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
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.iBooks")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 									(require-all
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 										(subpath "${HOME}")

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.iBooks")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+								)
+							)
 							(require-all
 								(signing-identifier "com.apple.mobilemail")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 						)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.iBooks")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 								(subpath "${HOME}")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.iBooks")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+						)
+					)
 					(require-all
 						(signing-identifier "com.apple.mobilemail")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 				)

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.swift-playgrounds.executable")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.developer.swift-playgrounds-app.development-build")
+			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "${HOME}/Library/SpringBoard/OriginalHomeVideo.mov")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.system.get-wallpaper")
+			(signing-identifier "com.apple.itunesu")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(require-any
+			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAppPopover")
+			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAvocado")
+			(signing-identifier "com.apple.DocumentManagerUICore.SaveToFiles")
+		)
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Bundle/Application")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
+				(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
+			)
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+			)
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(signing-identifier "com.apple.mobilemail")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")
+			(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection")
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "${HOME}/Library/Caches")
+		(require-any
+			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilenotes")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(process-attribute is-apple-signed-executable)

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type SYMLINK)
+		(extension "com.apple.tcc.kTCCServicePhotos")
 		(require-any
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
-(allow file-read-metadata
-	(require-all
-		(vnode-type DIRECTORY)
-		(require-any
-			(require-all
-				(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")
-				(signing-identifier "com.apple.mobilemail")
-			)
-			(require-all
-				(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection")
-				(signing-identifier "com.apple.mobilemail")
-			)
-			(require-all
-				(literal "${HOME}/Library/Caches")
-				(require-any
-					(require-all
-						(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")
-						(signing-identifier "com.apple.mobilemail")
-					)
-					(signing-identifier "com.apple.mobilemail")
-					(signing-identifier "com.apple.mobilenotes")
-				)
+			(literal "${HOME}/Media/PhotoData/syncInfo.plist")
+			(require-any
+				(subpath "${HOME}/Media/PhotoData/CPLAssets")
+				(subpath "${HOME}/Media/PhotoData/Metadata")
+				(subpath "${HOME}/Media/PhotoData/Mutations")
+				(subpath "${HOME}/Media/PhotoData/Sync")
+				(subpath "${HOME}/Media/PhotoData/Thumbnails")
 			)
+			(subpath "${HOME}/Media/DCIM")
+			(subpath "${HOME}/Media/PhotoData/PhotoCloudSharingData")
+			(subpath "${HOME}/Media/PhotoStreamsData")
 		)
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(require-all
+				(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")
+				(signing-identifier "com.apple.mobilemail")
+			)
+			(require-all
+				(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection")
+				(signing-identifier "com.apple.mobilemail")
+			)
+			(require-all
+				(literal "${HOME}/Library/Caches")
+				(require-any
+					(require-all
+						(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")
+						(signing-identifier "com.apple.mobilemail")
+					)
+					(signing-identifier "com.apple.mobilemail")
+					(signing-identifier "com.apple.mobilenotes")
+				)
+			)
 		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(extension "com.apple.revisiond.staging")
 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
-				(extension "com.apple.revisiond.revision")
-			)
-		)
-	)
-)
-(allow file-read-metadata
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
-(allow file-read-metadata
-	(require-all
-		(literal "${HOME}/Library/Caches")
-		(require-any
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.mobilenotes")
-		)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(signing-identifier "com.apple.mobilemail")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")
-			(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection")
-		)
-	)
-)
-(allow file-read-metadata
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
 				(require-any
-					(literal "/private/var/preferences/SystemConfiguration/com.apple.accounts.exists.plist")
+					(extension "com.apple.revisiond.revision")
 					(require-all
-						(%entitlement-is-present "com.apple.private.networkextension.configuration")
-						(literal "/private/var/preferences/com.apple.networkextension.plist")
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(extension "com.apple.revisiond.staging")
 					)
 				)
 			)
 			(require-all
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
-				(subpath "${HOME}")
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
 				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/\.GlobalPreferences$")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/GameKit/Data/[^/]+.gcdata$")
-						(subpath "${HOME}")
-					)
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 				)
+				(extension "com.apple.revisiond.staging")
 			)
 		)
 	)

 )
 (allow file-read-metadata
 	(require-all
-		(extension "com.apple.swift-playgrounds.executable")
+		(vnode-type DIRECTORY SYMLINK)
 		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.swift-playgrounds-app.development-build")
-			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
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
 		)
 	)
 )

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.iBooks")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 									(require-all
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 										(subpath "${HOME}")

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.iBooks")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+								)
+							)
 							(require-all
 								(signing-identifier "com.apple.mobilemail")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 						)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.iBooks")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 								(subpath "${HOME}")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.iBooks")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+						)
+					)
 					(require-all
 						(signing-identifier "com.apple.mobilemail")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 				)

 )
 (allow file-read-xattr
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(%entitlement-is-present "com.apple.private.oop-jit.loader")
+		(subpath "/private/var/OOPJit/${ENTITLEMENT:com.apple.private.oop-jit.loader}")
 	)
 )
 (allow file-read-xattr
 	(require-all
-		(%entitlement-is-present "com.apple.private.oop-jit.loader")
-		(subpath "/private/var/OOPJit/${ENTITLEMENT:com.apple.private.oop-jit.loader}")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
 	)
 )
 (allow file-read-xattr

 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-							(require-any
-								(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-								(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-							)
 						)
 					)
 					(require-all

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/System(/|$)")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/iTunesArtwork$")
-									(require-any
-										(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-										(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-									)
 								)
 							)
 						)
 					)
-					(require-any
-						(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-						(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-					)
 				)
 			)
 			(require-any

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "${HOME}/Media/Books")
+		(subpath "${HOME}/Media/Podcasts")
 		(signing-identifier "com.apple.itunesu")
 	)
 )
 (allow file-read-xattr
 	(require-all
-		(subpath "${HOME}/Media/Podcasts")
+		(subpath "${HOME}/Media/Books")
 		(signing-identifier "com.apple.itunesu")
 	)
 )

 		(extension "com.apple.clouddocs.version")
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService(/|$)")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(signing-identifier "com.apple.SafariViewService")
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService")

 		)
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.SafariViewService(/|$)")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(signing-identifier "com.apple.SafariViewService")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(extension "com.apple.librarian.ubiquity-container")

 			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
 			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
 		)
-		(signing-identifier "com.apple.mobilemail")
+		(signing-identifier "com.apple.mobilenotes")
 	)
 )
 (allow file-read-xattr

 )
 (allow file-read-xattr
 	(require-all
-		(signing-identifier "com.apple.CloudDocs.MobileDocumentsFileProvider")
-		(subpath "${HOME}/Library/Mobile Documents/com~apple~CloudDocs")
+		(subpath "${HOME}/Library/CallServices/Ringtones")
+		(signing-identifier "com.apple.InCallService")
 	)
 )
 (allow file-read-xattr

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/(NanoMail|PairedSyncServiceRestrictions)($|/)")
-		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}/Library/Mail")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 )
 (allow file-read-xattr
 	(require-all
-		(signing-identifier "com.apple.Maps")
-		(require-any
-			(literal "/private/var/containers/Bundle/[^/]+/[-A-Z0-9]")
-			(regex #"/private/var/containers/Bundle/[^/]+/([-A-Z0-9])+/GeoJSON")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "${HOME}/Library/Logs/Mail")
-		(signing-identifier "com.apple.mobilemail")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "${HOME}/Library/Calendar")
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/(NanoMail|PairedSyncServiceRestrictions)($|/)")
+		(subpath "${FRONT_USER_HOME}")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "${HOME}/Library/CallServices/Ringtones")
-		(signing-identifier "com.apple.InCallService")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
+			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
+		)
+		(signing-identifier "com.apple.mobilemail")
 	)
 )
 (allow file-read-xattr
 	(require-all
+		(subpath "${HOME}/Library/Calendar")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.Maps")
 		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
-			(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+			(literal "/private/var/containers/Bundle/[^/]+/[-A-Z0-9]")
+			(regex #"/private/var/containers/Bundle/[^/]+/([-A-Z0-9])+/GeoJSON")
 		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 		(signing-identifier "com.apple.PreviewShell")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.iStreamer")
-		(literal "/AppleInternal/Library/Frameworks/CoreAutomation*")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(subpath "/private/var")

 		(subpath "${HOME}/Library/DeviceRegistry")
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.iStreamer")
+		(literal "/AppleInternal/Library/Frameworks/CoreAutomation*")
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(subpath "${HOME}/Library/BulletinDistributor/Attachments")

 )
 (allow file-read-xattr
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
-			(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-			(subpath "${HOME}/Library/AddressBook")
-			(subpath "${HOME}/Library/AddressBook/Delegates")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAppPopover")
-			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAvocado")
-			(signing-identifier "com.apple.DocumentManagerUICore.SaveToFiles")
-		)
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
+			(signing-identifier "com.apple.DocumentManagerUICore.Service")
+			(signing-identifier "com.apple.DocumentsApp")
 		)
+		(subpath "/AppleInternal/Applications")
 	)
 )
 (allow file-read-xattr

 		)
 	)
 )
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
 		(subpath "/private/var")

 )
 (allow file-read-xattr
 	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		(signing-identifier "com.apple.CloudDocs.MobileDocumentsFileProvider")
+		(subpath "${HOME}/Library/Mobile Documents/com~apple~CloudDocs")
 	)
 )
 (allow file-read-xattr

 )
 (allow file-read-xattr
 	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+		(literal "/Library/Audio/Tunings/AID*")
+		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
 	)
 )
 (allow file-read-xattr
 	(require-all
-		(literal "/Library/Audio/Tunings/AID*")
-		(regex #"^/Library/Audio/Tunings/AID[0-9]+/Haptics(/.*)?$")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(extension "com.apple.clouddocs.version")
 	)
 )
 (allow file-read-xattr

 		(extension "com.apple.clouddocs.version")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/com.apple.wifi.plist")
-		(process-attribute is-apple-signed-executable)
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
 (allow file-read-xattr
 	(require-all
-		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(extension "com.apple.tcc.kTCCServicePhotos")
-		(require-any
-			(literal "${HOME}/Media/PhotoData/syncInfo.plist")
-			(require-any
-				(subpath "${HOME}/Media/PhotoData/CPLAssets")
-				(subpath "${HOME}/Media/PhotoData/Metadata")
-				(subpath "${HOME}/Media/PhotoData/Mutations")
-				(subpath "${HOME}/Media/PhotoData/Sync")
-				(subpath "${HOME}/Media/PhotoData/Thumbnails")
-			)
-			(subpath "${HOME}/Media/DCIM")
-			(subpath "${HOME}/Media/PhotoData/PhotoCloudSharingData")
-			(subpath "${HOME}/Media/PhotoStreamsData")
+			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
 		)
+		(extension "com.apple.odr-assets")
 	)
 )
 (allow file-read-xattr

 		)
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(extension "com.apple.tcc.kTCCServicePhotos")
+		(require-any
+			(literal "${HOME}/Media/PhotoData/syncInfo.plist")
+			(require-any
+				(subpath "${HOME}/Media/PhotoData/CPLAssets")
+				(subpath "${HOME}/Media/PhotoData/Metadata")
+				(subpath "${HOME}/Media/PhotoData/Mutations")
+				(subpath "${HOME}/Media/PhotoData/Sync")
+				(subpath "${HOME}/Media/PhotoData/Thumbnails")
+			)
+			(subpath "${HOME}/Media/DCIM")
+			(subpath "${HOME}/Media/PhotoData/PhotoCloudSharingData")
+			(subpath "${HOME}/Media/PhotoStreamsData")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/SystemConfiguration/com.apple.wifi.plist")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(system-attribute internal-build)

 )
 (allow file-read-xattr
 	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
 		)
-		(extension "com.apple.odr-assets")
 	)
 )
 (allow file-read-xattr

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "${HOME}/Library/Mail")
+		(subpath "${HOME}/Library/Logs/Mail")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 		(subpath "${HOME}/Library/Safari")
 		(require-any
 			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilenotes")
 			(signing-identifier "com.apple.mobilesafari")
 			(signing-identifier "com.apple.safarifetcherd")
 			(signing-identifier "com.apple.webbookmarksd")

 		)
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(literal "${HOME}/Library/SpringBoard/OriginalHomeVideo.mov")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.system.get-wallpaper")
+			(signing-identifier "com.apple.itunesu")
+		)
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(subpath "${HOME}/Library/Cookies")

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "/System/Library/Carrier Bundles")
+		(subpath "${HOME}/Media/Safari")
 		(require-any
-			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilesafari")
+		)
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(require-any
+			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAppPopover")
+			(signing-identifier "com.apple.DocumentManagerUICore.RecentsAvocado")
+			(signing-identifier "com.apple.DocumentManagerUICore.SaveToFiles")
+		)
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Bundle/Application")
+			(subpath "/private/var/containers/Bundle")
 		)
 	)
 )

 		)
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
+		(subpath "${HOME}/Library/WebClips")
+		(require-any
+			(signing-identifier "com.apple.mobilesafari")
+			(signing-identifier "com.apple.webapp")
+		)
+	)
+)
+(allow file-read-xattr
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
 (allow file-read-xattr
 	(require-all
 		(subpath "/private/var")

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.iBooks")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 									(require-all
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 										(subpath "${HOME}")

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.iBooks")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+								)
+							)
 							(require-all
 								(signing-identifier "com.apple.mobilemail")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 						)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.iBooks")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 								(subpath "${HOME}")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.iBooks")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+						)
+					)
 					(require-all
 						(signing-identifier "com.apple.mobilemail")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 				)

 		)
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.Service")
-			(signing-identifier "com.apple.DocumentsApp")
-		)
-		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Bundle/Application")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
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
 (allow file-read-xattr
 	(require-all
 		(literal "${HOME}/Library/Cookies/com.apple.itunesstored*")

 		)
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(subpath "${HOME}/Media/Safari")
-		(require-any
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.mobilesafari")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(subpath "${HOME}/Library/WebClips")
-		(require-any
-			(signing-identifier "com.apple.mobilesafari")
-			(signing-identifier "com.apple.webapp")
-		)
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "${HOME}/Library/SpringBoard/OriginalLockVideo.mov")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.system.get-wallpaper")
-			(signing-identifier "com.apple.itunesu")
-		)
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(subpath "${HOME}/Library/Notes")

 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(subpath "/System/Library/Carrier Bundles")
 		(require-any
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
-(allow file-read-xattr
-	(require-all
-		(signing-identifier "com.apple.chrono.WidgetRenderer-*")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com.apple.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))")
-			)
-			(require-any
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-			)
-		)
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
+			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 		)
 	)
 )

 		(signing-identifier "com.apple.FileProvider.LocalStorage")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
 		)
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(signing-identifier "com.apple.chrono.WidgetRenderer-*")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com.apple.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com.apple.chrono(/|$))")
+			)
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
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
 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-								)
-							)
-							(require-all
-								(signing-identifier "com.apple.iBooks")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 									(require-all
 										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 										(subpath "${HOME}")

 									)
 								)
 							)
+							(require-all
+								(signing-identifier "com.apple.iBooks")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+								)
+							)
 							(require-all
 								(signing-identifier "com.apple.mobilemail")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 							(require-all

 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+									(require-all
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+										(subpath "${HOME}")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(%entitlement-is-bool-true "com.apple.container2")
+									)
 								)
 							)
 						)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.Carousel$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.iBooks")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 								(subpath "${HOME}")

 							)
 						)
 					)
+					(require-all
+						(signing-identifier "com.apple.iBooks")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMusicSync$")
+						)
+					)
 					(require-all
 						(signing-identifier "com.apple.mobilemail")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.NanoMail")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.bulletinboard\.apps$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 					(require-all

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.stocks\.bridge$")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+								(subpath "${HOME}")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(%entitlement-is-bool-true "com.apple.container2")
+							)
 						)
 					)
 				)

 			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
 			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
 		)
-		(signing-identifier "com.apple.mobilemail")
+		(signing-identifier "com.apple.mobilenotes")
 	)
 	(require-all
 		(signing-identifier "com.apple.Bridge")

 		(signing-identifier "com.apple.FileProvider.LocalStorage")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(signing-identifier "com.apple.PosterBoard")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/(SystemData|tmp)/com.apple.posterkit.provider(/|$)")
 			)
 			(require-any

 		(subpath "${HOME}/Library/Safari")
 		(require-any
 			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilenotes")
 			(signing-identifier "com.apple.mobilesafari")
 			(signing-identifier "com.apple.safarifetcherd")
 			(signing-identifier "com.apple.webbookmarksd")

 	(require-any
 		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")
 		(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection")
-		(literal "${HOME}/Library/Preferences/com.apple.AOSNotification.launchd")
+		(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
 	)
 ))
 (define (_g3 _)
 	(require-all
-	(subpath "${FRONT_USER_HOME}")
-	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+	(subpath "/private/var/PersonaVolumes")
+	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 	(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 	(vnode-type DIRECTORY)
 	(literal "${HOME}/Library/Caches/com.apple.DictionaryServices")

 			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
 			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
 		)
-		(signing-identifier "com.apple.mobilemail")
+		(signing-identifier "com.apple.mobilenotes")
 	)
 	(require-all
 		(require-any

 				(require-any
 					(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")
 					(literal "${FRONT_USER_HOME}/Library/Logs/PersistentConnection")
-					(literal "${HOME}/Library/Preferences/com.apple.AOSNotification.launchd")
+					(literal "${HOME}/Library/Preferences/com.apple.dataaccess.launchd")
 				)
 			)
 			(signing-identifier "com.apple.Music")

 		(signing-identifier "com.apple.FileProvider.LocalStorage")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(signing-identifier "com.apple.PosterBoard")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/(SystemData|tmp)/com.apple.posterkit.provider(/|$)")
 			)
 			(require-any

 		(subpath "${HOME}/Library/Safari")
 		(require-any
 			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilenotes")
 			(signing-identifier "com.apple.mobilesafari")
 			(signing-identifier "com.apple.safarifetcherd")
 			(signing-identifier "com.apple.webbookmarksd")

 		(require-any
 			(_g3 "")
 			(require-all
-				(subpath "/private/var/PersonaVolumes")
+				(subpath "${FRONT_USER_HOME}")
 				(require-any
 					(_g3 "")
 					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 						(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 						(vnode-type DIRECTORY)
 						(literal "${HOME}/Library/Caches/com.apple.DictionaryServices")

 					(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
 					(signing-identifier "com.apple.shortcuts.watch")
 				)
+				(subpath "${PROCESS_TEMP_DIR}")
+			)
+			(require-all
+				(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+				(subpath "${PROCESS_TEMP_DIR}")
+			)
+			(require-all
+				(signing-identifier "com.apple.shortcuts")
 				(require-any
 					(subpath "${PROCESS_TEMP_DIR}")
 					(subpath "/private/var/tmp")
 				)
 			)
-			(require-all
-				(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
-				(subpath "/private/var/tmp")
-			)
-			(require-all
-				(signing-identifier "com.apple.shortcuts")
-				(subpath "/private/var/tmp")
-			)
 		)
 	)
 	(require-all

 			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
 			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
 		)
-		(signing-identifier "com.apple.mobilemail")
+		(signing-identifier "com.apple.mobilenotes")
 	)
 	(require-all
 		(signing-identifier "com.apple.Bridge")

 		(signing-identifier "com.apple.FileProvider.LocalStorage")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(signing-identifier "com.apple.PosterBoard")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/(SystemData|tmp)/com.apple.posterkit.provider(/|$)")
 			)
 			(require-any

 		(subpath "${HOME}/Library/Safari")
 		(require-any
 			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilenotes")
 			(signing-identifier "com.apple.mobilesafari")
 			(signing-identifier "com.apple.safarifetcherd")
 			(signing-identifier "com.apple.webbookmarksd")

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

 			)
 		)
 	)
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+		)
+	)
 	(require-all
 		(extension "com.apple.sandbox.container")
 		(require-any

 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")
 		)
 	)
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-		)
-	)
 	(require-all
 		(extension "com.apple.sandbox.oopjit")
 		(subpath "/private/var/OOPJit")

 			(literal "${HOME}/Library/Caches/com.apple.notes.objectcreation.lock")
 			(literal "${HOME}/Library/Caches/com.apple.notes.sharedstore.lock")
 		)
-		(signing-identifier "com.apple.mobilemail")
+		(signing-identifier "com.apple.mobilenotes")
 	)
 	(require-all
 		(signing-identifier "com.apple.Bridge")

 		(signing-identifier "com.apple.FileProvider.LocalStorage")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")

 		(signing-identifier "com.apple.PosterBoard")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/(SystemData|tmp)/com.apple.posterkit.provider(/|$)")
 			)
 			(require-any

 		(subpath "${HOME}/Library/Safari")
 		(require-any
 			(signing-identifier "com.apple.Safari.SocialHelper")
-			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.mobilenotes")
 			(signing-identifier "com.apple.mobilesafari")
 			(signing-identifier "com.apple.safarifetcherd")
 			(signing-identifier "com.apple.webbookmarksd")

 		(require-any
 			(require-all
 				(subpath "${PROCESS_TEMP_DIR}")
-				(signing-identifier "com.apple.shortcuts")
+				(require-any
+					(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+					(signing-identifier "com.apple.shortcuts.watch")
+				)
 			)
 			(require-all
 				(subpath "/private/var/tmp")
-				(signing-identifier "com.apple.shortcuts")
+				(require-any
+					(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+					(signing-identifier "com.apple.shortcuts.watch")
+				)
 			)
 		)
 	)

 	)
 )
 
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "ane-type")
+		(require-any
+			(iokit-registry-entry-class "AppleARMIODevice")
+			(iokit-registry-entry-class "IOPlatformExpertDevice")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(require-any
+			(iokit-property "BatteryData")
+			(iokit-property "Serial")
+			(iokit-property "battery-data")
+		)
+		(%entitlement-is-bool-true "com.apple.system.get-hardware-identifiers")
+		(iokit-connection "IOPMPowerSource")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "supports-apt")
+		(iokit-registry-entry-class "AppleARMIODevice")
+	)
+)
 (allow iokit-get-properties
 	(require-all
 		(iokit-registry-entry-class "IOPlatformDevice")
 		(require-any
-			(iokit-property "compatible")
-			(iokit-property "function-button_ringerab")
-			(iokit-property "home-button-type")
+			(iokit-property "device-colors")
+			(iokit-property "dictation")
+			(iokit-property "display-corner-radius")
+			(iokit-property "front-cam-offset-from-center")
 			(iokit-property "iommu-present")
+			(iokit-property "product-id")
+			(require-any
+				(iokit-property "artwork-device-idiom")
+				(iokit-property "artwork-device-subtype")
+				(iokit-property "artwork-display-gamut")
+				(iokit-property "artwork-dynamic-displaymode")
+				(iokit-property "artwork-scale-factor")
+				(iokit-property "compatible-device-fallback")
+				(iokit-property "device-perf-memory-class")
+				(iokit-property "graphics-featureset-class")
+				(iokit-property "graphics-featureset-fallbacks")
+				(iokit-property "product-description")
+			)
+			(require-any
+				(iokit-property "assistant")
+				(iokit-property "bluetooth-le")
+				(iokit-property "car-integration")
+				(iokit-property "front-cam-rotation-isp")
+				(iokit-property "function-button_ringerab")
+				(iokit-property "gps-capable")
+				(iokit-property "horseman")
+				(iokit-property "location-reminders")
+				(iokit-property "magnetometer")
+				(iokit-property "offline-dictation")
+				(iokit-property "rear-cam-offset-from-center")
+				(iokit-property "side-button-location")
+				(iokit-property "supports-maps-optical-heading")
+				(iokit-property "unique-model")
+				(iokit-property "watch-companion")
+			)
+			(require-any
+				(iokit-property "compatible")
+				(iokit-property "oled-display")
+				(iokit-property "ui-pip")
+			)
+			(require-any
+				(iokit-property "compatible-app-variant")
+				(iokit-property "external-hdr")
+			)
+			(require-any
+				(iokit-property "home-button-type")
+				(iokit-property "ptp-large-files")
+			)
+			(require-any
+				(iokit-property "large-format-phone")
+				(iokit-property "thin-bezel")
+			)
 		)
 	)
 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-property "DeviceProperties")
+		(iokit-registry-entry-class "IOAcceleratorES")
 		(require-any
-			(iokit-registry-entry-class "H11ANEIn")
-			(iokit-registry-entry-class "H1xANELoadBalancer")
+			(iokit-property "BaseAddressAlignmentRequirement")
+			(iokit-property "PerformanceStatistics")
+			(require-any
+				(iokit-property "AGXParameterBufferMaxSize*")
+				(iokit-property "IOGLES*")
+				(iokit-property "InternalStatisticsAccm")
+				(iokit-property "MetalStatisticsName")
+				(iokit-property "PerformanceStatisticsAccum")
+			)
+			(require-any
+				(iokit-property "MetalPluginClassName")
+				(iokit-property "MetalPluginName")
+			)
 		)
 	)
 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-registry-entry-class "AppleSPUHIDDriver")
 		(require-any
-			(iokit-property "SupportAlwaysOnCompass")
-			(iokit-property "SupportHDRCompass")
+			(iokit-property "nfcWithRadio")
+			(iokit-property "supports-nfc-reader-mode")
+		)
+		(require-any
+			(iokit-registry-entry-class "AppleSimpleUARTSync")
+			(iokit-registry-entry-class "AppleStockholmControlConfig")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(require-any
+			(iokit-property "disable-globe-map")
+			(iokit-property "multiuser-sessions")
+		)
+		(iokit-registry-entry-class "IOPlatformDevice")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "als-colorCfg")
+		(require-any
+			(iokit-registry-entry-class "AppleARMIICDevice")
+			(iokit-registry-entry-class "AppleSPUInterface")
 		)
 	)
 )

 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-registry-entry-class "IOPlatformDevice")
 		(require-any
-			(iokit-property "artwork-scale-factor")
-			(iokit-property "device-colors")
-			(iokit-property "dictation")
-			(iokit-property "display-corner-radius")
-			(iokit-property "front-cam-offset-from-center")
-			(iokit-property "product-id")
-			(iokit-property "ptp-large-files")
+			(iokit-property "Product Name")
+			(iokit-property "idProduct")
+			(iokit-property "idVendor")
+			(iokit-property "kUSBProductString")
+		)
+		(iokit-connection "AppleSynopsysOTGDevice")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-registry-entry-class "IOMedia")
+		(signing-identifier "com.apple.SharingViewService")
+		(require-any
+			(iokit-property "BSD Name")
 			(require-any
-				(iokit-property "artwork-device-idiom")
-				(iokit-property "artwork-device-subtype")
-				(iokit-property "artwork-display-gamut")
-				(iokit-property "artwork-dynamic-displaymode")
-				(iokit-property "compatible-device-fallback")
-				(iokit-property "device-perf-memory-class")
-				(iokit-property "graphics-featureset-class")
-				(iokit-property "graphics-featureset-fallbacks")
-				(iokit-property "product-description")
-			)
-			(require-any
-				(iokit-property "assistant")
-				(iokit-property "bluetooth-le")
-				(iokit-property "car-integration")
-				(iokit-property "front-cam-rotation-isp")
-				(iokit-property "gps-capable")
-				(iokit-property "horseman")
-				(iokit-property "location-reminders")
-				(iokit-property "magnetometer")
-				(iokit-property "offline-dictation")
-				(iokit-property "rear-cam-offset-from-center")
-				(iokit-property "side-button-location")
-				(iokit-property "supports-maps-optical-heading")
-				(iokit-property "unique-model")
-				(iokit-property "watch-companion")
-			)
-			(require-any
-				(iokit-property "compatible-app-variant")
-				(iokit-property "external-hdr")
-			)
-			(require-any
-				(iokit-property "large-format-phone")
-				(iokit-property "thin-bezel")
-			)
-			(require-any
-				(iokit-property "oled-display")
-				(iokit-property "ui-pip")
+				(iokit-property "Content")
+				(iokit-property "Role")
+				(iokit-property "UUID")
 			)
 		)
 	)
 )
+(allow iokit-get-properties
+	(require-all
+		(iokit-registry-entry-class "IONetworkController")
+		(require-any
+			(iokit-property "IOClass")
+			(require-any
+				(iokit-property "CFBundleIdentifier")
+				(iokit-property "IOLinkSpeed")
+				(iokit-property "IOLinkStatus")
+				(iokit-property "IOMaxPacketSize")
+				(iokit-property "IOMinPacketSize")
+				(iokit-property "IOPropertyMatch")
+			)
+			(require-any
+				(iokit-property "IOFeatures")
+				(iokit-property "IOProviderClass")
+			)
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-registry-entry-class "AppleSPUHIDDriver")
+		(require-any
+			(iokit-property "SupportAlwaysOnCompass")
+			(iokit-property "SupportHDRCompass")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-registry-entry-class "AppleAVD")
+		(require-any
+			(iokit-property "AVCSupported")
+			(iokit-property "HEVCCanDecodeTileToCanvas")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(require-any
+			(iokit-registry-entry-class "IOHIDDevice")
+			(iokit-registry-entry-class "IOHIDInterface")
+		)
+		(iokit-property "MaxInputReportSize")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-registry-entry-class "IOMobileFramebuffer")
+		(require-any
+			(iokit-property "PerformanceStatistics")
+			(iokit-property "ext-display-subsystem")
+			(iokit-property "external")
+			(require-any
+				(iokit-property "AppleTV")
+				(iokit-property "appleTV-VID0")
+				(iokit-property "appleTV-VID1")
+			)
+			(require-any
+				(iokit-property "DisplayPipePlaneBaseAlignment")
+				(iokit-property "DisplayPipeStrideRequirements")
+				(iokit-property "dfr")
+				(iokit-property "hdcp-hoover-protocol")
+			)
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "HEVCSupported")
+		(iokit-registry-entry-class "AppleD5500")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(require-any
+			(iokit-property "BatteryInstalled")
+			(iokit-property "ExternalConnected")
+		)
+		(iokit-connection "IOPMPowerSource")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "Size")
+		(iokit-registry-entry-class "IOMedia")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "noMultiColorSupport")
+		(require-any
+			(iokit-registry-entry-class "AppleARMIICDevice")
+			(iokit-registry-entry-class "AppleSPUInterface")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(require-any
+			(iokit-property "ForceSupported")
+			(iokit-property "SupportTapToWake")
+		)
+		(require-any
+			(iokit-registry-entry-class "AppleMultitouchDevice")
+			(iokit-registry-entry-class "AppleMultitouchSPI")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-registry-entry-class "IOPlatformExpertDevice")
+		(require-any
+			(iokit-property "region-info")
+			(require-any
+				(iokit-property "model")
+				(iokit-property "model-number")
+			)
+			(require-any
+				(iokit-property "platform-name")
+				(iokit-property "regulatory-model-number")
+			)
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-registry-entry-class "AppleJPEGDriver")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+			(iokit-property "AppleJPEGNumCores")
+			(iokit-property "AppleJPEGSupportsAppleInterchangeFormats")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "DeviceProperties")
+		(require-any
+			(iokit-registry-entry-class "H11ANEIn")
+			(iokit-registry-entry-class "H1xANELoadBalancer")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-registry-entry-class "AppleAPFSVolume")
+		(require-any
+			(signing-identifier "com.apple.DocumentManagerUICore.Service")
+			(signing-identifier "com.apple.DocumentsApp")
+		)
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "soc-generation")
+		(iokit-registry-entry-class "IOPlatformDevice")
+	)
+)
 (allow iokit-get-properties
 	(require-all
 		(iokit-registry-entry-class "IONetworkInterface")

 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-property "noMultiColorSupport")
-		(require-any
-			(iokit-registry-entry-class "AppleARMIICDevice")
-			(iokit-registry-entry-class "AppleSPUInterface")
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "supports-apt")
-		(iokit-registry-entry-class "AppleARMIODevice")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "Size")
-		(iokit-registry-entry-class "IOMedia")
+		(iokit-property "client")
+		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
 	)
 )
 (allow iokit-get-properties
 	(require-all
 		(require-any
-			(iokit-property "Product Name")
-			(iokit-property "idProduct")
-			(iokit-property "idVendor")
-			(iokit-property "kUSBProductString")
-		)
-		(iokit-connection "AppleSynopsysOTGDevice")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "IONetworkController")
-		(require-any
-			(iokit-property "IOClass")
-			(require-any
-				(iokit-property "CFBundleIdentifier")
-				(iokit-property "IOLinkSpeed")
-				(iokit-property "IOLinkStatus")
-				(iokit-property "IOMaxPacketSize")
-				(iokit-property "IOMinPacketSize")
-				(iokit-property "IOPropertyMatch")
-			)
-			(require-any
-				(iokit-property "IOFeatures")
-				(iokit-property "IOProviderClass")
-			)
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "IOMedia")
-		(signing-identifier "com.apple.SharingViewService")
-		(require-any
-			(iokit-property "BSD Name")
-			(require-any
-				(iokit-property "Content")
-				(iokit-property "Role")
-				(iokit-property "UUID")
-			)
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(require-any
-			(iokit-property "nfcWithRadio")
-			(iokit-property "supports-nfc-reader-mode")
-		)
-		(require-any
-			(iokit-registry-entry-class "AppleSimpleUARTSync")
-			(iokit-registry-entry-class "AppleStockholmControlConfig")
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "AppleAVD")
-		(require-any
-			(iokit-property "AVCSupported")
-			(iokit-property "HEVCCanDecodeTileToCanvas")
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "ane-type")
-		(require-any
-			(iokit-registry-entry-class "AppleARMIODevice")
-			(iokit-registry-entry-class "IOPlatformExpertDevice")
+			(iokit-registry-entry-class "AppleOscarNub")
+			(iokit-registry-entry-class "AppleSPUHIDInterface")
 		)
+		(iokit-property "gyro-interrupt-calibration")
 	)
 )
 (allow iokit-get-properties

 )
 (allow iokit-get-properties
 	(require-all
+		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
 		(require-any
-			(iokit-property "ForceSupported")
-			(iokit-property "SupportTapToWake")
-		)
-		(require-any
-			(iokit-registry-entry-class "AppleMultitouchDevice")
-			(iokit-registry-entry-class "AppleMultitouchSPI")
+			(iokit-property "QueueSize")
+			(require-any
+				(iokit-property "interval")
+				(iokit-property "mode")
+				(iokit-property "useMag")
+			)
 		)
 	)
 )

 		(iokit-registry-entry-class "AppleJPEGDriver")
 	)
 )
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "als-colorCfg")
-		(require-any
-			(iokit-registry-entry-class "AppleARMIICDevice")
-			(iokit-registry-entry-class "AppleSPUInterface")
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(require-any
-			(iokit-registry-entry-class "AppleOscarNub")
-			(iokit-registry-entry-class "AppleSPUHIDInterface")
-		)
-		(iokit-property "gyro-interrupt-calibration")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(require-any
-			(iokit-registry-entry-class "IOHIDDevice")
-			(iokit-registry-entry-class "IOHIDInterface")
-		)
-		(iokit-property "MaxInputReportSize")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "IOAcceleratorES")
-		(require-any
-			(iokit-property "BaseAddressAlignmentRequirement")
-			(iokit-property "PerformanceStatistics")
-			(require-any
-				(iokit-property "AGXParameterBufferMaxSize*")
-				(iokit-property "IOGLES*")
-				(iokit-property "InternalStatisticsAccm")
-				(iokit-property "MetalStatisticsName")
-				(iokit-property "PerformanceStatisticsAccum")
-			)
-			(require-any
-				(iokit-property "MetalPluginClassName")
-				(iokit-property "MetalPluginName")
-			)
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(require-any
-			(iokit-property "BatteryInstalled")
-			(iokit-property "ExternalConnected")
-		)
-		(iokit-connection "IOPMPowerSource")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "AppleJPEGDriver")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-			(iokit-property "AppleJPEGNumCores")
-			(iokit-property "AppleJPEGSupportsAppleInterchangeFormats")
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(require-any
-			(iokit-property "BatteryData")
-			(iokit-property "Serial")
-			(iokit-property "battery-data")
-		)
-		(%entitlement-is-bool-true "com.apple.system.get-hardware-identifiers")
-		(iokit-connection "IOPMPowerSource")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "AppleAPFSVolume")
-		(require-any
-			(signing-identifier "com.apple.DocumentManagerUICore.Service")
-			(signing-identifier "com.apple.DocumentsApp")
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "soc-generation")
-		(iokit-registry-entry-class "IOPlatformDevice")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(require-any
-			(iokit-property "disable-globe-map")
-			(iokit-property "multiuser-sessions")
-		)
-		(iokit-registry-entry-class "IOPlatformDevice")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "IOPlatformExpertDevice")
-		(require-any
-			(iokit-property "region-info")
-			(require-any
-				(iokit-property "model")
-				(iokit-property "model-number")
-			)
-			(require-any
-				(iokit-property "platform-name")
-				(iokit-property "regulatory-model-number")
-			)
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "client")
-		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
-		(require-any
-			(iokit-property "QueueSize")
-			(require-any
-				(iokit-property "interval")
-				(iokit-property "mode")
-				(iokit-property "useMag")
-			)
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-registry-entry-class "IOMobileFramebuffer")
-		(require-any
-			(iokit-property "PerformanceStatistics")
-			(iokit-property "ext-display-subsystem")
-			(iokit-property "external")
-			(require-any
-				(iokit-property "AppleTV")
-				(iokit-property "appleTV-VID0")
-				(iokit-property "appleTV-VID1")
-			)
-			(require-any
-				(iokit-property "DisplayPipePlaneBaseAlignment")
-				(iokit-property "DisplayPipeStrideRequirements")
-				(iokit-property "dfr")
-				(iokit-property "hdcp-hoover-protocol")
-			)
-		)
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(%entitlement-is-present "fairplay-client")
-		(%entitlement-is-present "com.apple.private.MobileGestalt.AllowedProtectedKeys")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "HEVCSupported")
-		(iokit-registry-entry-class "AppleD5500")
-	)
-)
 (allow iokit-get-properties
 	(require-any
 		(%entitlement-is-bool-true "com.apple.system.get-hardware-identifiers")
 		(%entitlement-is-bool-true "com.apple.wifi.manager-access")
+		(%entitlement-is-present "fairplay-client")
 		(iokit-property "IOCFPlugInTypes")
 		(iokit-property "IOClass")
 		(iokit-property "IOClassNameOverride")

 	(extension-class "com.apple.webkit.extension.iokit")
 )
 
-(allow iokit-open-user-client
-	(require-all
-		(iokit-registry-entry-class "RootDomainUserClient")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-				(signing-identifier "com.apple.shortcuts.watch")
-			)
-			(signing-identifier "com.apple.Bridge")
-			(signing-identifier "com.apple.Maps")
-			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.shortcuts")
-		)
-	)
-)
 (allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AppleMobileFileIntegrityUserClient")

 		(iokit-registry-entry-class "IOHIDLibUserClient")
 	)
 )
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "RootDomainUserClient")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+				(signing-identifier "com.apple.shortcuts.watch")
+			)
+			(signing-identifier "com.apple.Bridge")
+			(signing-identifier "com.apple.Maps")
+			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.shortcuts")
+		)
+	)
+)
 (allow iokit-open-user-client
 	(require-all
 		(system-attribute virtual-device)

 			(%entitlement-is-bool-true "com.apple.developer.arkit.main-camera-access.allow")
 			(%entitlement-is-bool-true "com.apple.developer.arkit.object-tracking-parameter-adjustment.allow")
 			(%entitlement-is-bool-true "com.apple.developer.arkit.shared-coordinate-space.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.visual-fidelity-monitoring.allow")
 			(%entitlement-is-bool-true "com.apple.developer.avfoundation.uvc-device-access")
 			(%entitlement-is-bool-true "com.apple.developer.coreml.neural-engine-access")
 			(%entitlement-is-bool-true "com.apple.developer.protected-content")

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.powerlog.plxpclogger.xpc")
-		(signing-identifier "com.apple.shortcuts")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
 	)
 )
 (allow mach-lookup

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.PowerManagement.control")
-		(signing-identifier "com.apple.shortcuts")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
 	)
 )
 (allow mach-lookup

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.iokit.powerdxpc")
-		(signing-identifier "com.apple.shortcuts")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
 	)
 )
 (allow mach-lookup

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.nanoprefsync")
-		(require-any
-			(signing-identifier "com.apple.Health")
-			(signing-identifier "com.apple.PassbookUIService")
-		)
+		(signing-identifier "com.apple.iBooks")
 	)
 )
 (allow mach-lookup

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.merchantd.identity")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.display")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
 	)
 )
 (allow mach-lookup

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
 		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.aps.alertprovider.xpc")
+		(global-name "com.apple.mobile.keybagd.UserManager.xpc")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(require-any
-			(global-name "com.apple.lskdd")
-			(global-name "com.apple.lskdd.xpc")
-			(global-name "com.apple.unfreed")
-		)
+		(global-name "com.apple.mobile.keybagd.xpc")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.mobile.keybagd.xpc")
+		(require-any
+			(global-name "com.apple.lskdd")
+			(global-name "com.apple.lskdd.xpc")
+			(global-name "com.apple.unfreed")
+		)
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.aps.alertprovider.xpc")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 		(process-attribute is-apple-signed-executable)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.coreduetd")
-		(process-attribute is-apple-signed-executable)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.odi.assessmentService")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.mobile.keybagd.UserManager.xpc")
+		(xpc-service-name "com.apple.Gestures.tracing.service.xpc")
 		(process-attribute is-apple-signed-executable)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.Gestures.tracing.service.xpc")
+		(global-name "com.apple.coreduetd")
 		(process-attribute is-apple-signed-executable)
 	)
 )

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

 					(sysctl-name "vm.all_map_ranges")
 					(sysctl-name "vm.vm_map_user_range_debug")
 				)
-				(%entitlement-is-bool-true "com.apple.security.developer-tools.thread-sanitizer")
+				(%entitlement-is-bool-true "com.apple.security.developer-tools.address-sanitizer")
 			)
 			(require-all
 				(sysctl-name "hw.pagesize_compat")
-				(%entitlement-is-bool-true "com.apple.security.developer-tools.thread-sanitizer")
+				(%entitlement-is-bool-true "com.apple.security.developer-tools.address-sanitizer")
 			)
 			(require-all
 				(sysctl-name "kern.osrelease")
-				(%entitlement-is-bool-true "com.apple.security.developer-tools.thread-sanitizer")
+				(%entitlement-is-bool-true "com.apple.security.developer-tools.address-sanitizer")
 			)
 		)
 	)

 )
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_GET_PURGEABLE_FILE_FLAGS APFSIOC_MAINTAIN_DIR_STATS)
-		(require-any
-			(signing-identifier "com.apple.TVMusic")
-			(signing-identifier "com.apple.nowplaying")
-		)
+		(fsctl-command APFSIOC_MAINTAIN_DIR_STATS APFSIOC_MARK_PURGEABLE)
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow system-fsctl

 )
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_MARK_PURGEABLE)
+		(fsctl-command APFSIOC_GET_PURGEABLE_FILE_FLAGS)
 		(require-any
 			(require-all
 				(fsctl-command APFSIOC_GET_DIR_STATS_EXT)
-				(require-any
-					(signing-identifier "com.apple.FileProvider.LocalStorage")
-					(signing-identifier "com.apple.fileindexerd")
-				)
+				(signing-identifier "com.apple.FileProvider.LocalStorage")
 			)
 			(require-all
 				(fsctl-command APFSIOC_MAINTAIN_DIR_STATS)
-				(signing-identifier "com.apple.fileindexerd")
+				(signing-identifier "com.apple.FileProvider.LocalStorage")
 			)
 			(require-any
 				(signing-identifier "com.apple.TVMusic")

 (allow system-necp-client-action)
 
 (allow system-package-check
-	(require-all
-		(signing-identifier "com.apple.FileProvider.LocalStorage")
-		(require-not (signing-identifier "com.apple.FileProvider.FileIndexerDaemonTests"))
-	)
-)
-(allow system-package-check
-	(signing-identifier "com.apple.fileindexerd")
+	(signing-identifier "com.apple.FileProvider.LocalStorage")
 )
 
 (allow system-privilege)

 		)
 	)
 )
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.springboard")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.media.ringtones.read-only")
-			(%entitlement-is-bool-true "com.apple.system.get-wallpaper")
-			(%entitlement-is-bool-true "com.apple.system.set-alert-tone")
-			(signing-identifier "com.apple.itunesu")
-			(signing-identifier "com.apple.mobilemail")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.ids")
-		(signing-identifier "com.apple.shortcuts")
-	)
-)
 (allow user-preference-read
 	(require-all
 		(preference-domain "com.apple.corevideo")

 (allow user-preference-read
 	(require-all
 		(preference-domain "com.apple.conference")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.avfoundation")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.ids")
 		(require-any
 			(require-all
 				(signing-identifier "com.apple.Bridge")
-				(preference-domain "com.apple.conference")
+				(preference-domain "com.apple.ids")
 			)
 			(require-any
 				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.marco")
+		(preference-domain "com.apple.coremedia")
+		(signing-identifier "com.apple.mobilemail")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.logging")
 		(require-any
 			(require-any
 				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")

 		)
 	)
 )
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.cloud.quota")
-		(require-any
-			(signing-identifier "com.apple.iCloudDriveApp")
-			(signing-identifier "com.apple.mobilemail")
-		)
-	)
-)
 (allow user-preference-read
 	(require-all
 		(preference-domain "com.apple.OTASyncState")

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.coreaudio")
-		(signing-identifier "com.apple.mobilemail")
+		(preference-domain "com.apple.homesharing")
+		(signing-identifier "com.apple.mobilesafari")
 	)
 )
 (allow user-preference-read

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.homesharing")
+		(preference-domain "com.apple.itunesstored")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.container2")
 			(signing-identifier "com.apple.iBooks")

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.avfoundation")
+		(preference-domain "com.apple.coreaudio")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.medialibrary")
-		(signing-identifier "com.apple.mobilesafari")
+		(preference-domain "com.apple.cloud.quota")
+		(require-any
+			(signing-identifier "com.apple.iCloudDriveApp")
+			(signing-identifier "com.apple.mobilemail")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.springboard")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.media.ringtones.read-only")
+			(%entitlement-is-bool-true "com.apple.system.get-wallpaper")
+			(%entitlement-is-bool-true "com.apple.system.set-alert-tone")
+			(signing-identifier "com.apple.itunesu")
+			(signing-identifier "com.apple.mobilemail")
+		)
 	)
 )
 (allow user-preference-read

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.itunesstored")
+		(preference-domain "com.apple.medialibrary")
 		(signing-identifier "com.apple.mobilesafari")
 	)
 )

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.logging")
-		(signing-identifier "com.apple.shortcuts")
+		(preference-domain "com.apple.marco")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
 	)
 )
 (allow user-preference-read

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.coremedia")
-		(signing-identifier "com.apple.mobilemail")
+		(%entitlement-is-bool-true "com.apple.posterkit.provider")
+		(require-any
+			(preference-domain "com.apple.mobilecal")
+			(preference-domain "com.apple.mobilecal.alarmengine")
+		)
 	)
 )
 (allow user-preference-read

 		(preference-domain "com.apple.icloud.findmydeviced.postwipe")
 		(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
 		(preference-domain "com.apple.iclouddrive.features")
-		(preference-domain "com.apple.imagent")
 		(preference-domain "com.apple.imdsmsrecordstore")
 		(preference-domain "com.apple.imessage")
 		(preference-domain "com.apple.indigo")

 
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.coremedia")
+		(preference-domain "com.apple.corevideo")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.ids")
-		(signing-identifier "com.apple.shortcuts")
+		(preference-domain "com.apple.conference")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
 	)
 )
 (allow managed-preference-read

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.avfoundation")
+		(preference-domain "com.apple.homesharing")
+		(signing-identifier "com.apple.mobilesafari")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.coreaudio")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.corevideo")
+		(preference-domain "com.apple.avfoundation")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.coreaudio")
+		(preference-domain "com.apple.coremedia")
 		(signing-identifier "com.apple.mobilemail")
 	)
 )

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.itunesstored")
-		(signing-identifier "com.apple.mobilesafari")
+		(preference-domain "com.apple.cloud.quota")
+		(require-any
+			(signing-identifier "com.apple.iCloudDriveApp")
+			(signing-identifier "com.apple.mobilemail")
+		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.homesharing")
+		(preference-domain "com.apple.itunesstored")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.container2")
 			(signing-identifier "com.apple.iBooks")

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.cloud.quota")
-		(require-any
-			(signing-identifier "com.apple.iCloudDriveApp")
-			(signing-identifier "com.apple.mobilemail")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.marco")
+		(preference-domain "com.apple.logging")
 		(require-any
 			(require-any
 				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.logging")
-		(signing-identifier "com.apple.shortcuts")
+		(preference-domain "com.apple.coreidv.public")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.identity.display")
+			(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
+		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.conference")
+		(preference-domain "com.apple.marco")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.ids")
 		(require-any
 			(require-all
 				(signing-identifier "com.apple.Bridge")
-				(preference-domain "com.apple.conference")
+				(preference-domain "com.apple.ids")
 			)
 			(require-any
 				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")

 		)
 	)
 )
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.coreidv.public")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.identity.display")
-			(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
-		)
-	)
-)
 (allow managed-preference-read
 	(require-all
 		(require-any

 		)
 	)
 )
+(allow managed-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.posterkit.provider")
+		(require-any
+			(preference-domain "com.apple.mobilecal")
+			(preference-domain "com.apple.mobilecal.alarmengine")
+		)
+	)
+)
 (allow managed-preference-read
 	(require-all
 		(process-attribute is-apple-signed-executable)

 		(preference-domain "com.apple.icloud.findmydeviced.postwipe")
 		(preference-domain "com.apple.icloud.findmydeviced.public.notbackedup")
 		(preference-domain "com.apple.iclouddrive.features")
-		(preference-domain "com.apple.imagent")
 		(preference-domain "com.apple.imdsmsrecordstore")
 		(preference-domain "com.apple.imessage")
 		(preference-domain "com.apple.indigo")

 
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.mobileipod")
+		(preference-domain "com.apple.itunesstored")
 		(signing-identifier "com.apple.itunesu")
 	)
 )

 )
 (allow user-preference-write
 	(require-all
-		(preference-domain "com.apple.itunesstored")
+		(preference-domain "com.apple.mobileipod")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.container2")
 			(signing-identifier "com.apple.iBooks")
```
