## media-device-discovery-extension

> Group: ⬆️ Updated

```diff

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(extension-class "com.apple.aned.read-only")
 						(require-any
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.mediaserverd.read")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									)
 								)
 							)
-							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(extension-class "com.apple.app-sandbox.read")
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
 						)
 					)
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
 						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
 							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 								(extension-class "com.apple.app-sandbox.read")
-							)
-							(require-all
 								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.mediaserverd.read")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									)
 								)
 							)
 						)
 					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-						(require-any
-							(extension-class "com.apple.aned.read-only")
-							(extension-class "com.apple.app-sandbox.read")
-							(extension-class "com.apple.mediaserverd.read")
-						)
-					)
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

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
+		(extension-class "com.apple.quicklook.readonly")
 		(extension "com.apple.sandbox.executable")
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.wcd.readonly")
+		(extension-class "com.apple.sharing.airdrop.readonly")
 		(extension "com.apple.sandbox.executable")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.wcd.readonly")
 		(extension "com.apple.sandbox.executable")
 	)
 )

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(extension-class "com.apple.aned.read-only")
 						(require-any
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.mediaserverd.read")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									)
 								)
 							)
-							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(extension-class "com.apple.app-sandbox.read")
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
 						)
 					)
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
 						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
 							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 								(extension-class "com.apple.app-sandbox.read")
-							)
-							(require-all
 								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.mediaserverd.read")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									)
 								)
 							)
 						)
 					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-						(require-any
-							(extension-class "com.apple.aned.read-only")
-							(extension-class "com.apple.app-sandbox.read")
-							(extension-class "com.apple.mediaserverd.read")
-						)
-					)
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

 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+	)
+)
 (allow file-read*
 	(require-all
 		(extension "com.apple.media-device-discovery.network-client")

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)
 		)
 	)
 )
-(allow file-read*
-	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
-		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
-		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-	)
-)
 (allow file-read*
 	(require-all
 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")

 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(literal "/private/var/preferences/com.apple.security.plist")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 			(%entitlement-is-present "com.apple.developer.media-device-extension")

 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+	)
+)
 (allow file-read-data
 	(require-all
 		(extension "com.apple.media-device-discovery.network-client")

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)
 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
-		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
-		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-	)
-)
 (allow file-read-data
 	(require-all
 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")

 )
 (allow file-read-data
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(literal "/private/var/preferences/com.apple.security.plist")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 )
 (allow file-read-data
 	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 			(%entitlement-is-present "com.apple.developer.media-device-extension")

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
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 			(%entitlement-is-present "com.apple.developer.media-device-extension")

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 )
 (allow file-read-metadata
 	(require-all
-		(literal "${HOME}/Library/Preferences")
+		(literal "${HOME}")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 			(%entitlement-is-present "com.apple.developer.media-device-extension")

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
+		(literal "/private/var/preferences/com.apple.security.plist")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(literal "${HOME}")
+		(literal "${HOME}/Library/Preferences")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
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
-		(global-name "com.apple.AudioAccessoryKit")
+		(global-name "com.apple.server.bluetooth.le.att.xpc")
 		(extension "com.apple.media-device-discovery.audio-smart-routing")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.securityd")
+		(global-name "com.apple.trustd")
+		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.audio.driver-registrar")
+		(%entitlement-is-present "com.apple.developer.media-device-extension")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.symptomsd")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.replayd")
-		(%entitlement-is-present "com.apple.developer.media-device-extension")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.AppSSO.service-xpc")
-		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.SystemConfiguration.helper")
+		(global-name "com.apple.commcenter.xpc")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 		(%entitlement-is-present "com.apple.developer.media-device-extension")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.GSSCred")
-		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.accountsd.accountmanager")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nsurlsessiond")
+		(global-name "com.apple.GSSCred")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cfnetwork.cfnetworkagent")
+		(global-name "com.apple.cfnetwork.AuthBrokerAgent")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.nsurlsessiond")
+		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.usymptomsd")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.SystemConfiguration.NetworkInformation")
+		(global-name "com.apple.symptoms.symptomsd.managed_events")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 		(%entitlement-is-present "com.apple.developer.media-device-extension")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.AppSSO.service-xpc")
+		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.SystemConfiguration.configd")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.commcenter.xpc")
+		(global-name "com.apple.SystemConfiguration.helper")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nesessionmanager")
+		(global-name "com.apple.cfnetwork.cfnetworkagent")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.networkserviceproxy.fetch-token")
+		(global-name "com.apple.SystemConfiguration.DNSConfiguration")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.SystemConfiguration.PPPController")
-		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.trustd")
-		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.symptomsd")
+		(global-name "com.apple.SystemConfiguration.NetworkInformation")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cfnetwork.AuthBrokerAgent")
+		(global-name "com.apple.securityd")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.networkd")
+		(global-name "com.apple.networkserviceproxy.fetch-token")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.symptoms.symptomsd.managed_events")
+		(global-name "com.apple.nesessionmanager")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ak.auth.xpc")
-		(process-attribute is-apple-signed-executable)
+		(global-name "com.apple.SystemConfiguration.PPPController")
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.SystemConfiguration.DNSConfiguration")
+		(global-name "com.apple.ak.auth.xpc")
+		(process-attribute is-apple-signed-executable)
 		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ak.anisette.xpc")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.authkit.client")
-				(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.authkit.client.internal")
-				(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.authkit.client.private")
-				(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-			)
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-			)
-		)
+		(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
+		(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
+		(global-name "com.apple.ak.anisette.xpc")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
-			(%entitlement-is-present "com.apple.developer.media-device-extension")
+			(require-all
+				(%entitlement-is-bool-true "com.apple.authkit.client")
+				(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.authkit.client.internal")
+				(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.authkit.client.private")
+				(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+			)
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.audio.driver-registrar")
+		(global-name "com.apple.replayd")
 		(%entitlement-is-present "com.apple.developer.media-device-extension")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.server.bluetooth.le.att.xpc")
+		(global-name "com.apple.networkd")
 		(require-any
-			(extension "com.apple.media-device-discovery.audio-smart-routing")
-			(require-all
-				(global-name "com.apple.server.bluetooth.le.att.xpc")
-				(require-any
-					(extension "com.apple.media-device-discovery.network-sharing")
-					(require-all
-						(%entitlement-is-present "com.apple.developer.media-device-extension")
-						(require-any
-							(extension "com.apple.media-device-discovery.network-sharing")
-							(extension "com.apple.media-device-extension.bleDiscovery")
-						)
-					)
-				)
-			)
+			(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
+			(%entitlement-is-present "com.apple.developer.media-device-extension")
 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.AudioAccessoryKit")
+		(extension "com.apple.media-device-discovery.audio-smart-routing")
+	)
+)
 (allow mach-lookup
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")

 		(extension "com.apple.media-device-discovery.network-client")
 	)
 )
+(allow sysctl-read
+	(require-all
+		(require-any
+			(sysctl-name "kern.nisdomainname")
+			(sysctl-name "net.statistics")
+		)
+		(extension "com.apple.media-device-discovery.network-client")
+	)
+)
 (allow sysctl-read
 	(require-all
 		(sysctl-name "net.routetable.*")
-		(extension "com.apple.media-device-discovery.network-client")
-	)
-)
-(allow sysctl-read
-	(require-all
-		(sysctl-name "net.statistics")
-		(extension "com.apple.media-device-discovery.network-client")
-	)
-)
-(allow sysctl-read
-	(require-all
-		(sysctl-name "kern.nisdomainname")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 			(%entitlement-is-present "com.apple.developer.media-device-extension")

 
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_GET_DIR_STATS_EXT)
+		(fsctl-command APFSIOC_GET_DIR_STATS)
 		(extension "com.apple.media-device-discovery.network-client")
 	)
 )
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_GET_DIR_STATS)
+		(fsctl-command APFSIOC_GET_DIR_STATS_EXT)
 		(require-any
 			(%entitlement-is-bool-true "com.apple.developer.media-device-discovery-extension")
 			(%entitlement-is-present "com.apple.developer.media-device-extension")
```
