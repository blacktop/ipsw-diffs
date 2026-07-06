## quicklook-thumbnail-secure

> Group: ⬆️ Updated

```diff

 
 (define (_g0 _)
 	(require-all
-	(subpath "/private/var/PersonaVolumes")
-	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+	(subpath "${FRONT_USER_HOME}")
+	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 ))
 (define (_g1 _)
 	(require-any
 	(_g0 "")
-	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 ))
 (define (_g2 _)
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

 			)
 			(require-all
 				(extension-class "com.apple.spotlight-indexable")
+				(subpath "/private/var/PersonaVolumes")
+				(_g4 "")
+			)
+			(require-all
+				(extension-class "com.apple.wcd.readonly")
 				(require-any
 					(_g2 "")
 					(_g3 "")

 					)
 				)
 			)
-			(require-all
-				(extension-class "com.apple.wcd.readonly")
-				(subpath "/private/var/PersonaVolumes")
-				(_g4 "")
-			)
 		)
 	)
 ))

 	(require-any
 	(_g7 "")
 	(require-all
-		(subpath "/private/var")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
 		(require-any
 			(_g7 "")
 			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
+				(subpath "/private/var")
 				(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 				(extension "com.apple.sandbox.container")
 				(_g6 "")

 		(require-all
 			(regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)")
 			(require-not (extension-class "com.apple.app-sandbox.read-write"))
-			(extension-class "com.apple.quicklook.readonly")
+			(extension-class "com.apple.app-sandbox.read")
 			(extension "com.apple.sandbox.container")
 			(_g6 "")
 		)

 ))
 (define (_g12 _)
 	(require-all
-	(extension-class "com.apple.quicklook.readonly")
+	(extension-class "com.apple.app-sandbox.read")
 	(extension "com.apple.sandbox.container")
 	(_g6 "")
 ))
 (define (_g13 _)
-	(extension-class "com.apple.quicklook.readonly"))
+	(extension-class "com.apple.mediaserverd.read"))
 (allow file-issue-extension
 	(require-any
 	(require-all

 		(require-any
 			(require-all
 				(extension-class "com.apple.aned.read-only")
-				(subpath "${FRONT_USER_HOME}")
-				(_g1 "")
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(subpath "${FRONT_USER_HOME}")
-				(_g1 "")
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
 				(require-any
 					(_g0 "")
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
+						(subpath "/private/var/PersonaVolumes")
 						(_g1 "")
 					)
 				)
 			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var/PersonaVolumes")
+				(_g1 "")
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(subpath "/private/var/PersonaVolumes")
+				(_g1 "")
+			)
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
 				(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\."))
 				(extension-class "com.apple.app-sandbox.read")
-				(subpath "${FRONT_USER_HOME}")
+				(subpath "/private/var/PersonaVolumes")
 				(_g1 "")
 			)
 		)

 			(_g12 "")
 			(_g9 "")
 			(require-all
-				(extension-class "com.apple.app-sandbox.read")
+				(extension-class "com.apple.mediaserverd.read")
 				(extension "com.apple.sandbox.container")
 				(_g6 "")
 			)
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.quicklook.readonly")
 				(extension "com.apple.sandbox.container")
 				(_g6 "")
 			)

 							(require-all
 								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$")
 								(require-not (extension-class "com.apple.app-sandbox.read-write"))
-								(extension-class "com.apple.quicklook.readonly")
+								(extension-class "com.apple.app-sandbox.read")
 								(extension "com.apple.sandbox.container")
 								(_g6 "")
 							)

 		(require-any
 			(_g13 "")
 			(extension-class "com.apple.aned.read-only")
-			(extension-class "com.apple.mediaserverd.read")
+			(extension-class "com.apple.quicklook.readonly")
 			(extension-class "com.apple.sharing.airdrop.readonly")
 			(extension-class "com.apple.wcd.readonly")
 			(require-all

 )
 (allow file-read*
 	(require-all
-		(literal "/private")
+		(literal "/private/preboot")
 		(process-attribute is-apple-signed-executable)
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

 										(require-any
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

 								(require-any
 									(require-all
 										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											)
-										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 									)
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(require-all
+												(subpath "${FRONT_USER_HOME}")
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											)
+										)
 									)
 								)
 							)

 )
 (allow file-read*
 	(require-all
-		(literal "/private/preboot")
+		(literal "/private")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 		(extension "com.apple.sandbox.container")
 		(require-not (subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/Snapshots"))
 		(require-any
-			(literal "/dev/null")
+			(literal "/private/etc/passwd")
 			(require-all
 				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots(/|$)")

 			(extension "com.apple.sandbox.executable")
 			(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
 			(literal "/dev/dtracehelper")
-			(literal "/dev/null")
 			(literal "/dev/random")
 			(literal "/dev/urandom")
-			(literal "/dev/zero")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 								(extension "com.apple.sandbox.container")
 								(require-any
 									(require-all
-										(literal "/private")
+										(literal "/private/preboot")
 										(process-attribute is-apple-signed-executable)
 									)
 									(require-all

 																(require-any
 																	(require-all
 																		(subpath "${FRONT_USER_HOME}")
-																		(require-any
-																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(subpath "/private/var/PersonaVolumes")
-																				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			)
-																		)
+																		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 																	)
 																	(require-all
 																		(subpath "/private/var/PersonaVolumes")
-																		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																		(require-any
+																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			(require-all
+																				(subpath "${FRONT_USER_HOME}")
+																				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			)
+																		)
 																	)
 																)
 															)

 												(require-any
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

 														(require-any
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

 								(extension "com.apple.sandbox.container")
 								(require-any
 									(require-all
-										(literal "/private")
+										(literal "/private/preboot")
 										(process-attribute is-apple-signed-executable)
 									)
 									(require-all

 																(require-any
 																	(require-all
 																		(subpath "${FRONT_USER_HOME}")
-																		(require-any
-																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(subpath "/private/var/PersonaVolumes")
-																				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			)
-																		)
+																		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 																	)
 																	(require-all
 																		(subpath "/private/var/PersonaVolumes")
-																		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																		(require-any
+																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			(require-all
+																				(subpath "${FRONT_USER_HOME}")
+																				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			)
+																		)
 																	)
 																)
 															)

 												(require-any
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

 														(require-any
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

 				(extension "com.apple.sandbox.container")
 				(require-any
 					(require-all
-						(literal "/private")
+						(literal "/private/preboot")
 						(process-attribute is-apple-signed-executable)
 					)
 					(require-all

 												(require-any
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

 								(require-any
 									(require-all
 										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											)
-										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 									)
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(require-all
+												(subpath "${FRONT_USER_HOME}")
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											)
+										)
 									)
 								)
 							)

 										(require-any
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

 										(extension "com.apple.sandbox.container")
 										(require-any
 											(require-all
-												(literal "/private")
+												(literal "/private/preboot")
 												(process-attribute is-apple-signed-executable)
 											)
 											(require-all

 																		(require-any
 																			(require-all
 																				(subpath "${FRONT_USER_HOME}")
-																				(require-any
-																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																					(require-all
-																						(subpath "/private/var/PersonaVolumes")
-																						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																					)
-																				)
+																				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 																			)
 																			(require-all
 																				(subpath "/private/var/PersonaVolumes")
-																				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																				(require-any
+																					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																					(require-all
+																						(subpath "${FRONT_USER_HOME}")
+																						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																					)
+																				)
 																			)
 																		)
 																	)

 														(require-any
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
 																		(subpath "${FRONT_USER_HOME}")
-																		(require-any
-																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(subpath "/private/var/PersonaVolumes")
-																				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			)
-																		)
+																		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 																	)
 																	(require-all
 																		(subpath "/private/var/PersonaVolumes")
-																		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																		(require-any
+																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			(require-all
+																				(subpath "${FRONT_USER_HOME}")
+																				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			)
+																		)
 																	)
 																)
 															)

 										(extension "com.apple.sandbox.container")
 										(require-any
 											(require-all
-												(literal "/private")
+												(literal "/private/preboot")
 												(process-attribute is-apple-signed-executable)
 											)
 											(require-all

 																		(require-any
 																			(require-all
 																				(subpath "${FRONT_USER_HOME}")
-																				(require-any
-																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																					(require-all
-																						(subpath "/private/var/PersonaVolumes")
-																						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																					)
-																				)
+																				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 																			)
 																			(require-all
 																				(subpath "/private/var/PersonaVolumes")
-																				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																				(require-any
+																					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																					(require-all
+																						(subpath "${FRONT_USER_HOME}")
+																						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																					)
+																				)
 																			)
 																		)
 																	)

 														(require-any
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
 																		(subpath "${FRONT_USER_HOME}")
-																		(require-any
-																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(require-all
-																				(subpath "/private/var/PersonaVolumes")
-																				(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			)
-																		)
+																		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 																	)
 																	(require-all
 																		(subpath "/private/var/PersonaVolumes")
-																		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																		(require-any
+																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			(require-all
+																				(subpath "${FRONT_USER_HOME}")
+																				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			)
+																		)
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
+			(require-any
+				(literal "/dev/null")
+				(literal "/dev/zero")
+			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

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

 										(require-any
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

 								(require-any
 									(require-all
 										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											)
-										)
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 									)
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(require-all
+												(subpath "${FRONT_USER_HOME}")
+												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											)
+										)
 									)
 								)
 							)

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private")
+		(literal "/private/preboot")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/preboot")
+		(literal "/private")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 							(subpath "${FRONT_USER_HOME}")
 							(subpath "${HOME}")
 						)
+						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)"))
 						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
-						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")

 							(subpath "${HOME}")
 						)
 						(require-not (regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
+						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)"))
 						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
-						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
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

 									(subpath "${FRONT_USER_HOME}")
 									(subpath "${HOME}")
 								)
+								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)"))
 								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
-								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 							)
 							(require-all
 								(subpath "/private/var/PersonaVolumes")

 									(subpath "${HOME}")
 								)
 								(require-not (regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
+								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)"))
 								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
-								(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
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

 											(subpath "${FRONT_USER_HOME}")
 											(subpath "${HOME}")
 										)
+										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)"))
 										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
-										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 									)
 									(require-all
 										(subpath "/private/var/PersonaVolumes")

 											(subpath "${HOME}")
 										)
 										(require-not (regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
+										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences(/|$)"))
 										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Preferences/\.GlobalPreferences\.plist|/Library/Preferences/com\.apple\.PeoplePicker\.plist)$"))
-										(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox(/|$)"))
 									)
 								)
 							)

 						)
 						(extension "com.apple.sandbox.container")
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-						(require-not (regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)"))
 						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$"))
+						(require-not (regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)"))
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")

 						)
 						(extension "com.apple.sandbox.container")
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox")
-						(require-not (regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$"))
 						(require-not (regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$"))
-						(require-not (regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)"))
+						(require-not (regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$"))
 						(require-not (regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Documents|/Documents/Inbox)$"))
+						(require-not (regex #"((((((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((((/Library|/Library/Caches)|/Library/Caches/Snapshots)|/Library/Preferences)|/Library/SyncedPreferences)$|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library|/Library/Caches)$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/Snapshots$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/SyncedPreferences$)"))
 					)
 				)
 			)

 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "artwork-scale-factor")
-		(iokit-registry-entry-class "IOPlatformDevice")
-	)
-)
 (allow iokit-get-properties
 	(require-all
 		(require-any

 			(iokit-property "artwork-device-subtype")
 			(iokit-property "artwork-display-gamut")
 			(iokit-property "artwork-dynamic-displaymode")
+			(iokit-property "artwork-scale-factor")
 			(iokit-property "compatible-device-fallback")
 			(iokit-property "device-perf-memory-class")
 			(iokit-property "graphics-featureset-class")
```
