## tipsd

> Group: ⬆️ Updated

```diff

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

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.tipsd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.TipsDaemon")
-			(subpath "${HOME}/Library/Caches/com.apple.tipsd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.TipsDaemon")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.TipsDaemon")
+					(subpath "${HOME}/Library/Caches/com.apple.tipsd")
+				)
+			)
 			(subpath "${HOME}/Library/Caches/com.apple.tipsd")
 		)
 	)

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.TipsDaemon")
+			(subpath "${HOME}/Library/Caches/com.apple.tipsd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.TipsCore")
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
 			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.TipsDaemon")

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
 	(require-any
+		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/Truth.plist")
 		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/UserSettings.plist")
+		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/Truth.plist")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/UserSettings.plist")
 		(literal "${HOME}/Library/Cookies/com.apple.tipsd.binarycookies*")
 		(literal "${HOME}/Library/SyncedPreferences/com.apple.tipsd.plist")
 		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/Truth.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")

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
 (allow file-read-metadata
 	(require-any
+		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/Truth.plist")
 		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/UserSettings.plist")
+		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/Truth.plist")
 		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/UserSettings.plist")
 		(literal "${HOME}")
 		(literal "${HOME}/Library/Caches")

 		(literal "${HOME}/Library/Preferences")
 		(literal "${HOME}/Library/SyncedPreferences/com.apple.tipsd.plist")
 		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/Truth.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")

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
```
