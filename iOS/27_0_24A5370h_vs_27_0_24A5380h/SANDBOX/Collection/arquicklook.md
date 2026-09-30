## arquicklook

> Group: ⬆️ Updated

```diff

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
 )
 
+(allow file-write-data
+	(require-any
+		(literal "/dev/null")
+		(literal "/dev/zero")
+	)
+)
 (allow file-write-data
 	(require-all
 		(literal "/dev/dtracehelper")

 	(require-all
 		(extension "com.apple.sandbox.container")
 		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
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
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-				)
-			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/Snapshots")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")
 		)
 	)
 )
-(allow file-write-data
-	(require-any
-		(literal "/dev/null")
-		(literal "/dev/zero")
-	)
-)
 (deny file-write-data
 	(require-all
 		(extension "com.apple.sandbox.container")
 		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
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
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-						)
-					)
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-				)
-			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/Snapshots")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/SyncedPreferences")

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

 	(extension-class "com.apple.webkit.mach-bootstrap")
 )
 
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "platform-name")
-		(iokit-registry-entry-class "IOPlatformExpertDevice")
-	)
-)
 (allow iokit-get-properties
 	(require-all
 		(iokit-registry-entry-class "IOService")

 		)
 	)
 )
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "platform-name")
+		(iokit-registry-entry-class "IOPlatformExpertDevice")
+	)
+)
 (allow iokit-get-properties
 	(require-all
 		(iokit-registry-entry-class "IOPlatformDevice")
 		(require-any
-			(iokit-property "artwork-scale-factor")
 			(iokit-property "front-cam-offset-from-center")
 			(iokit-property "is-muse")
 			(iokit-property "product-id")

 				(iokit-property "artwork-device-subtype")
 				(iokit-property "artwork-display-gamut")
 				(iokit-property "artwork-dynamic-displaymode")
+				(iokit-property "artwork-scale-factor")
 				(iokit-property "compatible-device-fallback")
 				(iokit-property "device-perf-memory-class")
 				(iokit-property "graphics-featureset-class")
```
