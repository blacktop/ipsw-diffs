## dataaccessd

> Group: ⬆️ Updated

```diff

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.dataaccess.dataaccessd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.exchangesyncd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Caches/com.apple.dataaccess.exchangesyncd")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
-		(subpath "${HOME}/Library/Caches/com.apple.dataaccess.exchangesyncd")
+		(require-any
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.dataaccess.dataaccessd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.exchangesyncd")
+		)
 	)
 )
 (allow file-issue-extension

 						(require-any
 							(require-all
 								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
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
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.dataaccess.dataaccessd")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.exchangesyncd")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.dataaccess.exchangesyncd")
 		)
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.dataaccess.exchangesyncd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.dataaccess.dataaccessd")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.exchangesyncd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Cookies")
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
 			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.dataaccess.dataaccessd")

 						(require-any
 							(require-all
 								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									)
-								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
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

 	(require-all
 		(subpath "/private/var")
 		(require-any
+			(literal "/private/var/preferences/com.apple.security.plist")
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				(require-any
+					(literal "/private/var/preferences/com.apple.security.plist")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 							(subpath "${FRONT_USER_HOME}")
 						)
 					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
-										(require-any
-											(require-all
-												(subpath "/private/var")
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-												)
-											)
-											(subpath "${FRONT_USER_HOME}")
-										)
-									)
-								)
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
-										(require-any
-											(require-all
-												(subpath "/private/var")
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-												)
-											)
-											(subpath "${FRONT_USER_HOME}")
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 							(require-all
 								(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
 								(require-any

 							)
 						)
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+									(require-all
+										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
+										(require-any
+											(require-all
+												(subpath "/private/var")
+												(subpath "${FRONT_USER_HOME}")
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+												)
+											)
+											(subpath "${FRONT_USER_HOME}")
+										)
+									)
+								)
+							)
+						)
+					)
 				)
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")

 )
 (allow file-read*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.exchangesyncd")

 )
 (allow file-read*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")

 		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(literal "/private/var/preferences/com.apple.security.plist")
 		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
 		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/PersistentConnection")

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.exchangesyncd")

 							(subpath "${FRONT_USER_HOME}")
 						)
 					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
-										(require-any
-											(require-all
-												(subpath "/private/var")
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-												)
-											)
-											(subpath "${FRONT_USER_HOME}")
-										)
-									)
-								)
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
-										(require-any
-											(require-all
-												(subpath "/private/var")
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-												)
-											)
-											(subpath "${FRONT_USER_HOME}")
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 							(require-all
 								(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
 								(require-any

 							)
 						)
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+									(require-all
+										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
+										(require-any
+											(require-all
+												(subpath "/private/var")
+												(subpath "${FRONT_USER_HOME}")
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+												)
+											)
+											(subpath "${FRONT_USER_HOME}")
+										)
+									)
+								)
+							)
+						)
+					)
 				)
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")

 	(require-all
 		(subpath "/private/var")
 		(require-any
+			(literal "/private/var/preferences/com.apple.security.plist")
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				(require-any
+					(literal "/private/var/preferences/com.apple.security.plist")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(literal "/private/var/preferences/com.apple.security.plist")
 		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles")
 		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
 		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")

 	(require-all
 		(subpath "/private/var")
 		(require-any
+			(literal "/private/var/preferences/com.apple.security.plist")
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				(require-any
+					(literal "/private/var/preferences/com.apple.security.plist")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
 		)
 	)

 							(subpath "${FRONT_USER_HOME}")
 						)
 					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
-										(require-any
-											(require-all
-												(subpath "/private/var")
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-												)
-											)
-											(subpath "${FRONT_USER_HOME}")
-										)
-									)
-								)
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
-										(require-any
-											(require-all
-												(subpath "/private/var")
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-												)
-											)
-											(subpath "${FRONT_USER_HOME}")
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 							(require-all
 								(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
 								(require-any

 							)
 						)
 					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+									(require-all
+										(regex #"(((((^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$)|^/private/var/(mobile|euser[0-9]+)/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/[-0-9A-F]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle($|/Info\.plist$))|^/private/var/Users/[^/]+/Library/Carrier Bundles/.*\.bundle/([^/])*\.lproj(/|$))")
+										(require-any
+											(require-all
+												(subpath "/private/var")
+												(subpath "${FRONT_USER_HOME}")
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+												)
+											)
+											(subpath "${FRONT_USER_HOME}")
+										)
+									)
+								)
+							)
+						)
+					)
 				)
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")

 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.exchangesyncd")

 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")

 		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(literal "/private/var/preferences/com.apple.security.plist")
 		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
 		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles")
 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+					(subpath "/private/var/tmp")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
+			(subpath "/private/var/tmp")
 		)
 	)
 )
 (allow file-write*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.exchangesyncd")

 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")

 		(subpath "${HOME}/Library/Notes")
 		(subpath "${PROCESS_TEMP_DIR}")
 		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
-		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write*

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+					(subpath "/private/var/tmp")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
+			(subpath "/private/var/tmp")
 		)
 	)
 )
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.exchangesyncd")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")

 		(subpath "${HOME}/Library/Notes")
 		(subpath "${PROCESS_TEMP_DIR}")
 		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
-		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write-create

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

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
+					(subpath "/private/var/tmp")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?DataAccess($|/)")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/com.apple.notes..+.lock$")
 			)
+			(subpath "/private/var/tmp")
 		)
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.exchangesyncd")

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.dataaccess.dataaccessd")

 		(subpath "${HOME}/Library/Notes")
 		(subpath "${PROCESS_TEMP_DIR}")
 		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
-		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write-unlink
```
