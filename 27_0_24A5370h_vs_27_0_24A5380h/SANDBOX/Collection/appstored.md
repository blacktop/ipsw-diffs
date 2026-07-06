## appstored

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.AppleMediaServices")
-			(subpath "${HOME}/Library/Caches/com.apple.appstored")
-			(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.appstored")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.AppleMediaServices")
-			(subpath "${HOME}/Library/Caches/com.apple.appstored")
-			(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.appstored")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.AppleMediaServices")
-			(subpath "${HOME}/Library/Caches/com.apple.appstored")
-			(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.appstored")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.AppleMediaServices")
-			(subpath "${HOME}/Library/Caches/com.apple.appstored")
-			(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.appstored")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.AppleMediaServices")
-			(subpath "${HOME}/Library/Caches/com.apple.appstored")
-			(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.appstored")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
 	)
 )
 (allow file-issue-extension

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.AppleMediaServices")
+				(subpath "${HOME}/Library/Caches/com.apple.appstored")
+				(subpath "${HOME}/Library/HTTPStorages/com.apple.appstored")
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.iTunesStore")
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.nsurlsessiond.readonly")

 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
 				)
 			)
 			(require-all

 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
 				)
 			)
 			(require-all

 			(require-all
 				(subpath "${FRONT_USER_HOME}")
 				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
 				)
 			)
 			(require-all

 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(require-all
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
 						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					)
 				)
 			)

 			(require-all
 				(subpath "${FRONT_USER_HOME}")
 				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
 				)
 			)
 			(require-all

 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(require-all
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
 						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					)
 				)
 			)

 			(require-all
 				(subpath "${FRONT_USER_HOME}")
 				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
 				)
 			)
 			(require-all

 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(require-all
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
 						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					)
 				)
 			)

 			(require-all
 				(subpath "${FRONT_USER_HOME}")
 				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
 				)
 			)
 			(require-all

 				(require-any
 					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					(require-all
+						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.appstored")
 						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
 					)
 				)
 			)
```
