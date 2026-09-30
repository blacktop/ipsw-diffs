## quicklookd

> Group: ⬆️ Updated

```diff

 				(require-any
 					(extension "com.apple.odr-assets")
 					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 					)
 				)
 			)

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.quicklook.readonly")
+		(extension-class "com.apple.mediaserverd.read")
 		(extension "com.apple.sandbox.executable")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(require-all
+				(extension "com.apple.assets.read")
+				(require-any
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+					)
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			)
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.wcd.readonly")
 		(extension "com.apple.sandbox.executable")
 	)
 )

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.wcd.readonly")
-		(extension "com.apple.sandbox.executable")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 	)
 )
 (allow file-issue-extension

 		(extension "com.apple.sandbox.executable")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
+			(extension "com.apple.quicklook.readonly")
+			(extension "com.apple.security.exception.files.absolute-path.read-only")
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-only")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
 			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
+				(extension "com.apple.assets.read")
 				(require-any
 					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
+			(require-all
+				(require-any
+					(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+				)
+				(require-any
+					(extension "com.apple.odr-assets")
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+								)
+								(require-any
+									(extension "com.apple.odr-assets")
+									(require-all
+										(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+										(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+									)
+								)
+							)
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+									(extension "com.apple.librarian.ubiquity-container")
+								)
+							)
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
+						)
+						(require-any
+							(extension "com.apple.odr-assets")
+							(require-all
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+								(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+							)
+						)
+					)
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
+		(extension-class "com.apple.quicklook.readonly")
+		(extension "com.apple.sandbox.executable")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(require-all
+				(subpath "${HOME}/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			)
+			(require-all
+				(subpath "/private/var")
+				(subpath "${FRONT_USER_HOME}")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
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
 		)
 	)
 )

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(extension "com.apple.sandbox.container")
+				(subpath "/private/var")
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(extension "com.apple.sandbox.container")
+				(subpath "/private/var")
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(extension "com.apple.sandbox.container")
+				(subpath "/private/var")
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.quicklook.readonly")
+				(extension "com.apple.sandbox.container")
+				(subpath "/private/var")
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.sharing.airdrop.readonly")
+				(extension "com.apple.sandbox.container")
+				(subpath "/private/var")
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(require-any
+					(require-all
+						(extension "com.apple.sandbox.container")
+						(subpath "/private/var")
+						(extension-class "com.apple.app-sandbox.read")
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
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(require-any
+											(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
+							(require-all
+								(extension "com.apple.sandbox.container")
+								(subpath "/private/var")
+								(extension-class "com.apple.app-sandbox.read")
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+											(require-all
+												(extension-class "com.apple.app-sandbox.read")
+												(require-any
+													(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension-class "com.apple.app-sandbox.read")
+						(extension "com.apple.sandbox.container")
+						(subpath "/private/var")
+						(extension-class "com.apple.app-sandbox.read")
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
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(require-any
+											(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(extension-class "com.apple.app-sandbox.read-write")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+								)
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+										)
+									)
+								)
+							)
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(require-any
+							(require-all
+								(extension-class "com.apple.app-sandbox.read-write")
+								(require-any
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+										)
+									)
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+												)
+											)
+										)
+									)
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+								)
+							)
+							(require-all
+								(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
+								(require-any
+									(extension-class "com.apple.app-sandbox.read-write")
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(extension "com.apple.sandbox.container")
+										(subpath "/private/var")
+										(extension-class "com.apple.app-sandbox.read")
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(require-any
+													(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+													(require-all
+														(extension-class "com.apple.app-sandbox.read")
+														(require-any
+															(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+															(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+															(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+														)
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$")
+								(extension-class "com.apple.app-sandbox.read-write")
+							)
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(require-all
+										(extension-class "com.apple.app-sandbox.read-write")
+										(require-any
+											(require-all
+												(require-any
+													(subpath "${FRONT_USER_HOME}")
+													(subpath "${HOME}")
+												)
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+												)
+											)
+											(require-all
+												(subpath "/private/var/PersonaVolumes")
+												(require-any
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+													(require-all
+														(require-any
+															(subpath "${FRONT_USER_HOME}")
+															(subpath "${HOME}")
+														)
+														(require-any
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
+															(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+														)
+													)
+												)
+											)
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+										)
+									)
+									(require-all
+										(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
+										(require-any
+											(extension-class "com.apple.app-sandbox.read-write")
+											(require-all
+												(extension-class "com.apple.app-sandbox.read")
+												(extension "com.apple.sandbox.container")
+												(subpath "/private/var")
+												(extension-class "com.apple.app-sandbox.read")
+												(subpath "/private/var/PersonaVolumes")
+												(require-any
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+													(require-all
+														(require-any
+															(subpath "${FRONT_USER_HOME}")
+															(subpath "${HOME}")
+														)
+														(require-any
+															(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+															(require-all
+																(extension-class "com.apple.app-sandbox.read")
+																(require-any
+																	(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+																	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+																	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+																)
+															)
+														)
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+						)
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.quicklook.readonly")

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-					)
-				)
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-					)
-				)
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-					)
-				)
-			)
-			(require-all
-				(extension-class "com.apple.quicklook.readonly")
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-					)
-				)
-			)
-			(require-all
-				(extension-class "com.apple.sharing.airdrop.readonly")
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(subpath "/private/var")
-						(extension-class "com.apple.quicklook.readonly")
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(subpath "/private/var")
-								(extension-class "com.apple.quicklook.readonly")
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
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension-class "com.apple.app-sandbox.read-write")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-										)
-									)
-								)
-							)
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-						)
-					)
-					(require-all
-						(extension-class "com.apple.quicklook.readonly")
-						(extension "com.apple.sandbox.container")
-						(subpath "/private/var")
-						(extension-class "com.apple.quicklook.readonly")
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(require-all
-								(extension-class "com.apple.app-sandbox.read-write")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-										)
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-												)
-											)
-										)
-									)
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-								)
-							)
-							(require-all
-								(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
-								(require-any
-									(extension-class "com.apple.app-sandbox.read-write")
-									(require-all
-										(extension-class "com.apple.quicklook.readonly")
-										(extension "com.apple.sandbox.container")
-										(subpath "/private/var")
-										(extension-class "com.apple.quicklook.readonly")
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$")
-								(extension-class "com.apple.app-sandbox.read-write")
-							)
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(require-all
-										(extension-class "com.apple.app-sandbox.read-write")
-										(require-any
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-												)
-											)
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-													(require-all
-														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$")
-															(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-														)
-													)
-												)
-											)
-											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-										)
-									)
-									(require-all
-										(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
-										(require-any
-											(extension-class "com.apple.app-sandbox.read-write")
-											(require-all
-												(extension-class "com.apple.quicklook.readonly")
-												(extension "com.apple.sandbox.container")
-												(subpath "/private/var")
-												(extension-class "com.apple.quicklook.readonly")
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-													(require-all
-														(require-any
-															(subpath "${FRONT_USER_HOME}")
-															(subpath "${HOME}")
-														)
-														(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-													)
-												)
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(extension "com.apple.quicklook.readonly")
-			(extension "com.apple.security.exception.files.absolute-path.read-only")
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(extension "com.apple.security.exception.files.home-relative-path.read-only")
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
-			(require-all
-				(extension "com.apple.assets.read")
-				(require-any
-					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-					)
-					(subpath "${HOME}/Library/Assets")
-					(subpath "/private/var/MobileAsset")
-				)
-			)
 			(require-all
 				(require-any
 					(subpath "${HOME}/Library/OnDemandResources/AssetPacks")

 				(require-any
 					(extension "com.apple.odr-assets")
 					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 					)
 				)
 			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.sharing.airdrop.readonly")
+		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Mobile Documents")
 				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 			)
 			(require-all
 				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+				(subpath "${FRONT_USER_HOME}")
 				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
-								)
-								(require-any
-									(extension "com.apple.odr-assets")
-									(require-all
-										(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-										(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-									)
-								)
-							)
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-									(extension "com.apple.librarian.ubiquity-container")
-								)
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
-						)
-						(require-any
-							(extension "com.apple.odr-assets")
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-							)
-						)
-					)
+					(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+					(extension "com.apple.librarian.ubiquity-container")
 				)
 			)
 			(require-all

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(require-any
-					(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
-				)
-				(require-any
-					(extension "com.apple.odr-assets")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 			(extension "com.apple.security.exception.files.absolute-path.read-write")
 			(extension "com.apple.security.exception.files.home-relative-path.read-write")
 			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 			)
 		)
 	)

 		(require-any
 			(extension "com.apple.quicklook.readonly")
 			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 			)
 		)
 	)

 			(require-all
 				(extension "com.apple.sandbox.container")
 				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.app-sandbox.read")
 				(subpath "/private/var/PersonaVolumes")
 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
 					)
 				)
 			)

 				(extension-class "com.apple.app-sandbox.read")
 				(extension "com.apple.sandbox.container")
 				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.app-sandbox.read")
 				(subpath "/private/var/PersonaVolumes")
 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
 					)
 				)
 			)

 				(extension-class "com.apple.mediaserverd.read")
 				(extension "com.apple.sandbox.container")
 				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.app-sandbox.read")
 				(subpath "/private/var/PersonaVolumes")
 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
 					)
 				)
 			)

 				(extension-class "com.apple.quicklook.readonly")
 				(extension "com.apple.sandbox.container")
 				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.app-sandbox.read")
 				(subpath "/private/var/PersonaVolumes")
 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
 					)
 				)
 			)

 				(extension-class "com.apple.sharing.airdrop.readonly")
 				(extension "com.apple.sandbox.container")
 				(subpath "/private/var")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.app-sandbox.read")
 				(subpath "/private/var/PersonaVolumes")
 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+						(require-any
+							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+							(require-all
+								(extension-class "com.apple.app-sandbox.read")
+								(require-any
+									(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+								)
+							)
+						)
 					)
 				)
 			)
 			(require-all
-				(subpath "/private/var")
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
 				(require-any
 					(require-all
 						(extension "com.apple.sandbox.container")
 						(subpath "/private/var")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.app-sandbox.read")
 						(subpath "/private/var/PersonaVolumes")
 						(require-any
 							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 									(subpath "${FRONT_USER_HOME}")
 									(subpath "${HOME}")
 								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+								(require-any
+									(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(require-any
+											(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+										)
+									)
+								)
 							)
 						)
 					)
 					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
+						(subpath "/private/var")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)")
 							(require-all
 								(extension "com.apple.sandbox.container")
 								(subpath "/private/var")
-								(extension-class "com.apple.quicklook.readonly")
+								(extension-class "com.apple.app-sandbox.read")
 								(subpath "/private/var/PersonaVolumes")
 								(require-any
 									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+										(require-any
+											(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+											(require-all
+												(extension-class "com.apple.app-sandbox.read")
+												(require-any
+													(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+													(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+												)
+											)
+										)
 									)
 								)
 							)

 			(require-all
 				(subpath "/private/var")
 				(require-any
+					(require-all
+						(extension-class "com.apple.app-sandbox.read")
+						(extension "com.apple.sandbox.container")
+						(subpath "/private/var")
+						(extension-class "com.apple.app-sandbox.read")
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
+									(require-all
+										(extension-class "com.apple.app-sandbox.read")
+										(require-any
+											(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+											(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+										)
+									)
+								)
+							)
+						)
+					)
 					(require-all
 						(extension-class "com.apple.app-sandbox.read-write")
 						(require-any

 							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 						)
 					)
-					(require-all
-						(extension-class "com.apple.quicklook.readonly")
-						(extension "com.apple.sandbox.container")
-						(subpath "/private/var")
-						(extension-class "com.apple.quicklook.readonly")
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							)
-						)
-					)
 					(require-all
 						(require-any
 							(subpath "${FRONT_USER_HOME}")

 								(require-any
 									(extension-class "com.apple.app-sandbox.read-write")
 									(require-all
-										(extension-class "com.apple.quicklook.readonly")
+										(extension-class "com.apple.app-sandbox.read")
 										(extension "com.apple.sandbox.container")
 										(subpath "/private/var")
-										(extension-class "com.apple.quicklook.readonly")
+										(extension-class "com.apple.app-sandbox.read")
 										(subpath "/private/var/PersonaVolumes")
 										(require-any
 											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+												(require-any
+													(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+													(require-all
+														(extension-class "com.apple.app-sandbox.read")
+														(require-any
+															(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+															(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+															(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+														)
+													)
+												)
 											)
 										)
 									)

 										(require-any
 											(extension-class "com.apple.app-sandbox.read-write")
 											(require-all
-												(extension-class "com.apple.quicklook.readonly")
+												(extension-class "com.apple.app-sandbox.read")
 												(extension "com.apple.sandbox.container")
 												(subpath "/private/var")
-												(extension-class "com.apple.quicklook.readonly")
+												(extension-class "com.apple.app-sandbox.read")
 												(subpath "/private/var/PersonaVolumes")
 												(require-any
 													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")

 															(subpath "${FRONT_USER_HOME}")
 															(subpath "${HOME}")
 														)
-														(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+														(require-any
+															(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+															(require-all
+																(extension-class "com.apple.app-sandbox.read")
+																(require-any
+																	(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/iTunesArtwork")
+																	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+																	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/System")
+																)
+															)
+														)
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
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+		(require-any
+			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+		)
+		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
 (allow file-read*
 	(require-all
-		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
-		)
-		(extension "com.apple.odr-assets")
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
 (allow file-read*

 )
 (allow file-read*
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
 (allow file-read*

 )
 (allow file-read*
 	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
-			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-			(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
 		)
-		(extension "com.apple.librarian.ubiquity-revision")
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
 (allow file-read-data
 	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+		(require-any
+			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+		)
+		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
 (allow file-read-data
 	(require-all
-		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
-		)
-		(extension "com.apple.odr-assets")
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
 (allow file-read-data

 )
 (allow file-read-data
 	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
-			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-			(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
 		)
-		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
 (allow file-read-data

 )
 (allow file-read-data
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
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+		(require-any
+			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+		)
+		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
 (allow file-read-xattr
 	(require-all
-		(require-any
-			(subpath "${HOME}/Library/OnDemandResources/AssetPacks")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.ondemandresources/Library/AssetPacks")
-		)
-		(extension "com.apple.odr-assets")
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
 (allow file-read-xattr

 )
 (allow file-read-xattr
 	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
-			(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-			(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
 		)
-		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
 (allow file-read-xattr

 )
 (allow file-read-xattr
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

 	(require-all
 		(extension "com.apple.sandbox.container")
 		(require-any
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

 	(require-all
 		(extension "com.apple.sandbox.container")
 		(require-any
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

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
 		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
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
```
