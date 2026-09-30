## com.apple.assistant.assistantd

> Group: ⬆️ Updated

```diff

 		(extension "com.apple.sandbox.executable")
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/Cookies")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")

 								(subpath "${FRONT_USER_HOME}")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(subpath "${HOME}/Library/Cookies")
-										)
-									)
+									(subpath "${HOME}/Library/Cookies")
 								)
 							)
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
 								(require-any
 									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(subpath "${HOME}/Library/Cookies")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(subpath "${HOME}/Library/Cookies")
+										)
+									)
 								)
 							)
 							(subpath "${HOME}/Library/Cookies")

 						(subpath "${FRONT_USER_HOME}")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(subpath "${HOME}/Library/Cookies")
-								)
-							)
+							(subpath "${HOME}/Library/Cookies")
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
 						(require-any
 							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(subpath "${HOME}/Library/Cookies")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(subpath "${HOME}/Library/Cookies")
+								)
+							)
 						)
 					)
 					(subpath "${HOME}/Library/Cookies")

 												(subpath "${FRONT_USER_HOME}")
 												(require-any
 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(subpath "${HOME}/Library/Cookies")
-														)
-													)
+													(subpath "${HOME}/Library/Cookies")
 												)
 											)
 										)
 									)
 								)
 							)
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(subpath "${HOME}/Library/Cookies")
-										)
-									)
-								)
-							)
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
 								(require-any

 												(subpath "/private/var/PersonaVolumes")
 												(require-any
 													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(subpath "${HOME}/Library/Cookies")
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
+														(require-any
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(subpath "${HOME}/Library/Cookies")
+														)
+													)
 												)
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
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(subpath "${HOME}/Library/Cookies")
+										)
+									)
+								)
+							)
 						)
 					)
 					(subpath "${HOME}/Library/Cookies")

 														(subpath "${FRONT_USER_HOME}")
 														(require-any
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(require-any
-																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(subpath "${HOME}/Library/Cookies")
-																)
-															)
+															(subpath "${HOME}/Library/Cookies")
 														)
 													)
 												)
 											)
 										)
 									)
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(subpath "${HOME}/Library/Cookies")
-												)
-											)
-										)
-									)
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
 										(require-any

 														(subpath "/private/var/PersonaVolumes")
 														(require-any
 															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(subpath "${HOME}/Library/Cookies")
+															(require-all
+																(subpath "${FRONT_USER_HOME}")
+																(require-any
+																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	(subpath "${HOME}/Library/Cookies")
+																)
+															)
 														)
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
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(subpath "${HOME}/Library/Cookies")
+												)
+											)
+										)
+									)
 								)
 							)
 							(subpath "${HOME}/Library/Cookies")

 																(subpath "${FRONT_USER_HOME}")
 																(require-any
 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(require-any
-																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(subpath "${HOME}/Library/Cookies")
-																		)
-																	)
+																	(subpath "${HOME}/Library/Cookies")
 																)
 															)
 														)
 													)
 												)
 											)
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(subpath "${HOME}/Library/Cookies")
-														)
-													)
-												)
-											)
 											(require-all
 												(subpath "/private/var/PersonaVolumes")
 												(require-any

 																(subpath "/private/var/PersonaVolumes")
 																(require-any
 																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(subpath "${HOME}/Library/Cookies")
+																	(require-all
+																		(subpath "${FRONT_USER_HOME}")
+																		(require-any
+																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			(subpath "${HOME}/Library/Cookies")
+																		)
+																	)
 																)
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
+														(require-any
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(subpath "${HOME}/Library/Cookies")
+														)
+													)
+												)
+											)
 										)
 									)
 									(subpath "${HOME}/Library/Cookies")

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
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
 		(subpath "${HOME}/Library/Caches/com.apple.assistantd")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "${HOME}/Library/Caches/com.apple.assistantd")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(subpath "${HOME}/Library/Caches/com.apple.assistantd")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(subpath "${HOME}/Library/Caches/com.apple.AssistantServices")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
-			(subpath "${HOME}/Library/Cookies")
+			(subpath "${HOME}/Library/Caches/com.apple.assistantd")
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Caches/com.apple.assistantd")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.AssistantServices")
+			(require-all
+				(subpath "${HOME}/Library/Caches/com.apple.AssistantServices")
+				(extension-class "com.apple.aned.read-only")
+			)
 			(subpath "${HOME}/Library/Caches/com.apple.assistantd")
 		)
-		(require-any
-			(extension-class "com.apple.aned.read-only")
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.app-sandbox.read-write")
-			(extension-class "com.apple.mediaserverd.read")
-			(extension-class "com.apple.mediaserverd.read-write")
-		)
 	)
 )
 (deny file-issue-extension

 								(subpath "${FRONT_USER_HOME}")
 								(require-any
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(subpath "${HOME}/Library/Cookies")
-										)
-									)
+									(subpath "${HOME}/Library/Cookies")
 								)
 							)
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
 								(require-any
 									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(subpath "${HOME}/Library/Cookies")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(subpath "${HOME}/Library/Cookies")
+										)
+									)
 								)
 							)
 							(subpath "${HOME}/Library/Cookies")

 						(subpath "${FRONT_USER_HOME}")
 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(subpath "${HOME}/Library/Cookies")
-								)
-							)
+							(subpath "${HOME}/Library/Cookies")
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
 						(require-any
 							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(subpath "${HOME}/Library/Cookies")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(subpath "${HOME}/Library/Cookies")
+								)
+							)
 						)
 					)
 					(subpath "${HOME}/Library/Cookies")

 												(subpath "${FRONT_USER_HOME}")
 												(require-any
 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(subpath "${HOME}/Library/Cookies")
-														)
-													)
+													(subpath "${HOME}/Library/Cookies")
 												)
 											)
 										)
 									)
 								)
 							)
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(subpath "${HOME}/Library/Cookies")
-										)
-									)
-								)
-							)
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
 								(require-any

 												(subpath "/private/var/PersonaVolumes")
 												(require-any
 													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(subpath "${HOME}/Library/Cookies")
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
+														(require-any
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(subpath "${HOME}/Library/Cookies")
+														)
+													)
 												)
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
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(subpath "${HOME}/Library/Cookies")
+										)
+									)
+								)
+							)
 						)
 					)
 					(subpath "${HOME}/Library/Cookies")

 														(subpath "${FRONT_USER_HOME}")
 														(require-any
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(require-any
-																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(subpath "${HOME}/Library/Cookies")
-																)
-															)
+															(subpath "${HOME}/Library/Cookies")
 														)
 													)
 												)
 											)
 										)
 									)
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(subpath "${HOME}/Library/Cookies")
-												)
-											)
-										)
-									)
 									(require-all
 										(subpath "/private/var/PersonaVolumes")
 										(require-any

 														(subpath "/private/var/PersonaVolumes")
 														(require-any
 															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(subpath "${HOME}/Library/Cookies")
+															(require-all
+																(subpath "${FRONT_USER_HOME}")
+																(require-any
+																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	(subpath "${HOME}/Library/Cookies")
+																)
+															)
 														)
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
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(subpath "${HOME}/Library/Cookies")
+												)
+											)
+										)
+									)
 								)
 							)
 							(subpath "${HOME}/Library/Cookies")

 																(subpath "${FRONT_USER_HOME}")
 																(require-any
 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(require-any
-																			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																			(subpath "${HOME}/Library/Cookies")
-																		)
-																	)
+																	(subpath "${HOME}/Library/Cookies")
 																)
 															)
 														)
 													)
 												)
 											)
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(subpath "${HOME}/Library/Cookies")
-														)
-													)
-												)
-											)
 											(require-all
 												(subpath "/private/var/PersonaVolumes")
 												(require-any

 																(subpath "/private/var/PersonaVolumes")
 																(require-any
 																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(subpath "${HOME}/Library/Cookies")
+																	(require-all
+																		(subpath "${FRONT_USER_HOME}")
+																		(require-any
+																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																			(subpath "${HOME}/Library/Cookies")
+																		)
+																	)
 																)
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
+														(require-any
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(subpath "${HOME}/Library/Cookies")
+														)
+													)
+												)
+											)
 										)
 									)
 									(subpath "${HOME}/Library/Cookies")

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
