## BackgroundShortcutRunner

> Group: ⬆️ Updated

```diff

 
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
-			(require-all
-				(subpath "${HOME}/Library/Caches/com.apple.WorkflowKit.BackgroundShortcutRunner")
-				(extension-class "com.apple.mediaserverd.read")
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
+			(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")
 		)
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
-				(extension "com.apple.shortcuts.access.internet")
-				(require-any
-					(require-all
-						(literal "${HOME}/Library/Cookies/com.apple.WorkflowKit.BackgroundShortcutRunner.binarycookies*")
-						(extension-class "com.apple.mediaserverd.read")
-					)
-					(subpath "${HOME}/Library/HTTPStorages/com.apple.WorkflowKit.BackgroundShortcutRunner")
-				)
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-				)
-			)
-			(require-any
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
-				(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")
+				(subpath "${HOME}/Library/Caches/com.apple.WorkflowKit.BackgroundShortcutRunner")
+				(extension-class "com.apple.aned.read-only")
 			)
+			(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
 		)
 	)
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
-		(extension-class "com.apple.app-sandbox.read")
+		(extension-class "com.apple.app-sandbox.read-write")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
 			(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Mobile Documents")

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
-			(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
-			(require-all
-				(extension-class "com.apple.aned.read-only")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(require-any
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
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
-				)
-			)
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-					)
-				)
-			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(require-any
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
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
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
-										)
-									)
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
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
-								)
-							)
-						)
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
-				)
-			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(require-all
-								(subpath "/private/var")
-								(require-any
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
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "${FRONT_USER_HOME}")
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															)
-														)
-													)
-												)
-											)
-										)
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
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
-										)
-									)
-								)
-							)
-							(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
-						)
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-						(require-any
-							(require-all
-								(extension-class "com.apple.mediaserverd.read")
-								(require-any
-									(require-all
-										(subpath "/private/var")
-										(require-any
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
-											(require-all
-												(subpath "${FRONT_USER_HOME}")
-												(require-any
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "/private/var/PersonaVolumes")
-														(require-any
-															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "${FRONT_USER_HOME}")
-																(require-any
-																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	(require-all
-																		(subpath "/private/var/PersonaVolumes")
-																		(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-																	)
-																)
-															)
-														)
-													)
-												)
-											)
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(require-any
-													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-													(require-all
-														(subpath "${FRONT_USER_HOME}")
-														(require-any
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-															(require-all
-																(subpath "/private/var/PersonaVolumes")
-																(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-															)
-														)
-													)
-												)
-											)
-										)
-									)
-									(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
-								)
-							)
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.app-sandbox.read-write")
-									(extension-class "com.apple.mediaserverd.read")
-									(extension-class "com.apple.mediaserverd.read-write")
-									(extension-class "com.apple.nsurlsessiond.readonly")
-									(extension-class "com.apple.quicklook.readonly")
-									(extension-class "com.apple.sharing.airdrop.readonly")
-									(extension-class "com.apple.spotlight-indexable")
-									(extension-class "com.apple.wcd.readonly")
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
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(extension-class "com.apple.quicklook.readonly")
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(extension-class "com.apple.quicklook.readonly")
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-				(extension-class "com.apple.quicklook.readonly")
-			)
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(require-all
+				(extension "com.apple.shortcuts.access.internet")
+				(require-any
+					(require-all
+						(literal "${HOME}/Library/Cookies/com.apple.WorkflowKit.BackgroundShortcutRunner.binarycookies*")
+						(extension-class "com.apple.aned.read-only")
+					)
+					(subpath "${HOME}/Library/HTTPStorages/com.apple.WorkflowKit.BackgroundShortcutRunner")
+				)
+			)
+			(require-any
+				(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
+				(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension "com.apple.app-sandbox.read-write")
+		(require-any
+			(extension-class "com.apple.app-sandbox.read")
+			(extension-class "com.apple.app-sandbox.read-write")
+			(extension-class "com.apple.mediaserverd.read")
+			(extension-class "com.apple.mediaserverd.read-write")
+			(extension-class "com.apple.sharing.airdrop.readonly")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
 			(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(require-all
+				(extension-class "com.apple.mediaserverd.read-write")
+				(subpath "${HOME}/Library/Caches/com.apple.WorkflowKit.BackgroundShortcutRunner")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
 		(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
+		(extension-class "com.apple.app-sandbox.read-write")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
+		(extension-class "com.apple.app-sandbox.read")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
 			(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")
 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(extension "com.apple.assets.read")
+		(require-any
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.identityservices.send")

 )
 (allow file-issue-extension
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
-		(require-any
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.app-sandbox.read-write")
-			(extension-class "com.apple.mediaserverd.read")
-			(extension-class "com.apple.mediaserverd.read-write")
-			(extension-class "com.apple.sharing.airdrop.readonly")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(require-any
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
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
+						)
+					)
+					(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
+				)
+			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(require-any
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
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
+								)
+							)
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
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
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
+										)
+									)
+								)
+							)
+						)
+					)
+					(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
+						(require-any
+							(require-all
+								(subpath "/private/var")
+								(require-any
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
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
+										)
+									)
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
+									(require-all
+										(subpath "/private/var/PersonaVolumes")
+										(require-any
+											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+											(require-all
+												(subpath "${FRONT_USER_HOME}")
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(subpath "/private/var/PersonaVolumes")
+														(require-any
+															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(require-all
+																(subpath "${FRONT_USER_HOME}")
+																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															)
+														)
+													)
+												)
+											)
+										)
+									)
+								)
+							)
+							(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
+						)
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(require-all
+								(extension-class "com.apple.mediaserverd.read")
+								(require-any
+									(require-all
+										(subpath "/private/var")
+										(require-any
+											(require-all
+												(subpath "${FRONT_USER_HOME}")
+												(require-any
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(subpath "/private/var/PersonaVolumes")
+														(require-any
+															(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(require-all
+																(subpath "${FRONT_USER_HOME}")
+																(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															)
+														)
+													)
+												)
+											)
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
+											(require-all
+												(subpath "/private/var/PersonaVolumes")
+												(require-any
+													(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+													(require-all
+														(subpath "${FRONT_USER_HOME}")
+														(require-any
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+															(require-all
+																(subpath "/private/var/PersonaVolumes")
+																(require-any
+																	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	(require-all
+																		(subpath "${FRONT_USER_HOME}")
+																		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+																	)
+																)
+															)
+														)
+													)
+												)
+											)
+										)
+									)
+									(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
+								)
+							)
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(require-any
+									(extension-class "com.apple.aned.read-only")
+									(extension-class "com.apple.app-sandbox.read")
+									(extension-class "com.apple.app-sandbox.read-write")
+									(extension-class "com.apple.mediaserverd.read")
+									(extension-class "com.apple.mediaserverd.read-write")
+									(extension-class "com.apple.nsurlsessiond.readonly")
+									(extension-class "com.apple.quicklook.readonly")
+									(extension-class "com.apple.sharing.airdrop.readonly")
+									(extension-class "com.apple.spotlight-indexable")
+									(extension-class "com.apple.wcd.readonly")
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
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(require-all
+								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(extension-class "com.apple.mediaserverd.read-write")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(extension-class "com.apple.mediaserverd.read-write")
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
 		(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
 	)
 )

 		(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/Caches/com.apple.siri.flowtools")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.sharing.airdrop.readonly")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 	)

 			)
 			(require-all
 				(extension-class "com.apple.aned.read-only")
-				(subpath "${HOME}/Media/PhotoStreamsData")
+				(require-any
+					(subpath "${HOME}/Media/PhotoStreamsData")
+					(subpath "/Library/Ringtones")
+				)
 			)
 			(require-all
 				(extension-class "com.apple.app-sandbox.read")
-				(subpath "${HOME}/Media/Debug")
+				(subpath "${HOME}/Media/Photos")
 			)
 			(require-all
 				(extension-class "com.apple.app-sandbox.read")
-				(subpath "${HOME}/Media/PhotoStreamsData")
+				(subpath "/Library/Ringtones")
 			)
 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
-				(subpath "${HOME}/Media/Debug")
+				(subpath "${HOME}/Media/Photos")
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
 				(require-any
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(require-any
-								(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
-								(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")
-							)
-							(subpath "${HOME}/Media/PhotoStreamsData")
-						)
-					)
-					(require-any
-						(subpath "${PROCESS_TEMP_DIR}/com.apple.WorkflowKit.BackgroundShortcutRunner")
-						(subpath "/private/var/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner")
-					)
 					(subpath "${HOME}/Media/DCIM")
 					(subpath "${HOME}/Media/Debug")
 					(subpath "${HOME}/Media/MediaAnalysis")

 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(subpath "${HOME}/Media/PhotoStreamsData")
-					(subpath "/Library/Ringtones")
-				)
+				(subpath "${HOME}/Media/Photos")
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(subpath "/Library/Ringtones")
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
-				(subpath "${HOME}/Media/Debug")
+				(subpath "${HOME}/Media/Photos")
 			)
 			(require-all
 				(extension-class "com.apple.sharing.airdrop.readonly")

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

 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "/System/Library/Carrier Bundles")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 																		(require-any
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																			(require-all
 																				(subpath "${HOME}")

 																							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																							(require-all
 																								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																								(extension "com.apple.shortcuts.access.location")
+																								(require-any
+																									(extension "com.apple.shortcuts.access.location")
+																									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																								)
 																							)
 																						)
 																					)
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)

 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "/private/var")
 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 		(extension "com.apple.librarian.ubiquity-revision")
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/AddressBook")
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-	)
-)
 (allow file-read*
 	(require-all
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read*

 		(extension "com.apple.clouddocs.version")
 	)
 )
+(allow file-read*
+	(require-all
+		(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
+	)
+)
 (allow file-read*
 	(require-all
 		(extension "com.apple.shortcuts.access.photos")
 		(require-any
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/usr/sbin/fairplayd")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-							(subpath "${HOME}/Library/FairPlay")
+							(require-any
+								(literal "/usr/sbin/fairplayd")
+								(subpath "${HOME}/Library/FairPlay")
+							)
 						)
 					)
-					(subpath "${HOME}/Library/FairPlay")
+					(require-any
+						(literal "/usr/sbin/fairplayd")
+						(subpath "${HOME}/Library/FairPlay")
+					)
 				)
 			)
-			(subpath "${HOME}/Library/FairPlay")
+			(require-any
+				(literal "/usr/sbin/fairplayd")
+				(subpath "${HOME}/Library/FairPlay")
+			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

 )
 (allow file-read*
 	(require-all
-		(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+		(subpath "${HOME}/Library/AddressBook")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read*

 		(require-any
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 						)
 					)
 					(require-all
 						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-						(extension "com.apple.shortcuts.access.location")
+						(require-any
+							(extension "com.apple.shortcuts.access.location")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+						)
 					)
 					(require-all
 						(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "${HOME}")

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 					)
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		)
 	)
 )

 		(subpath "/Developer/Applications")
 		(subpath "/System/Developer/Applications")
 		(subpath "/private/var/containers/Bundle")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")
 		(subpath "/private/var/personalized_debug/Applications")

 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "/System/Library/Carrier Bundles")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 																		(require-any
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																			(require-all
 																				(subpath "${HOME}")

 																							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																							(require-all
 																								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																								(extension "com.apple.shortcuts.access.location")
+																								(require-any
+																									(extension "com.apple.shortcuts.access.location")
+																									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																								)
 																							)
 																						)
 																					)
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)

 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "/private/var")
 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 		(require-any
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/usr/sbin/fairplayd")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-							(subpath "${HOME}/Library/FairPlay")
+							(require-any
+								(literal "/usr/sbin/fairplayd")
+								(subpath "${HOME}/Library/FairPlay")
+							)
 						)
 					)
-					(subpath "${HOME}/Library/FairPlay")
+					(require-any
+						(literal "/usr/sbin/fairplayd")
+						(subpath "${HOME}/Library/FairPlay")
+					)
 				)
 			)
-			(subpath "${HOME}/Library/FairPlay")
+			(require-any
+				(literal "/usr/sbin/fairplayd")
+				(subpath "${HOME}/Library/FairPlay")
+			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

 		(require-any
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 						)
 					)
 					(require-all
 						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-						(extension "com.apple.shortcuts.access.location")
+						(require-any
+							(extension "com.apple.shortcuts.access.location")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+						)
 					)
 					(require-all
 						(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "${HOME}")

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 					)
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		)
 	)
 )

 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "/System/Library/Carrier Bundles")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 																		(require-any
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																			(require-all
 																				(subpath "${HOME}")

 																							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																							(require-all
 																								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																								(extension "com.apple.shortcuts.access.location")
+																								(require-any
+																									(extension "com.apple.shortcuts.access.location")
+																									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																								)
 																							)
 																						)
 																					)
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)

 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "/private/var")
 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 		(extension "com.apple.shortcuts.access.location")
 	)
 )
-(allow file-read-data
-	(require-all
-		(subpath "${HOME}/Library/AddressBook")
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-	)
-)
 (allow file-read-data
 	(require-all
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read-data

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(subpath "${HOME}/Library/AddressBook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
+	)
+)
 (allow file-read-data
 	(require-all
 		(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read-data

 		(require-any
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/usr/sbin/fairplayd")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-							(subpath "${HOME}/Library/FairPlay")
+							(require-any
+								(literal "/usr/sbin/fairplayd")
+								(subpath "${HOME}/Library/FairPlay")
+							)
 						)
 					)
-					(subpath "${HOME}/Library/FairPlay")
+					(require-any
+						(literal "/usr/sbin/fairplayd")
+						(subpath "${HOME}/Library/FairPlay")
+					)
 				)
 			)
-			(subpath "${HOME}/Library/FairPlay")
+			(require-any
+				(literal "/usr/sbin/fairplayd")
+				(subpath "${HOME}/Library/FairPlay")
+			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

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

 		(require-any
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 						)
 					)
 					(require-all
 						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-						(extension "com.apple.shortcuts.access.location")
+						(require-any
+							(extension "com.apple.shortcuts.access.location")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+						)
 					)
 					(require-all
 						(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "${HOME}")

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 					)
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		)
 	)
 )

 		(subpath "/Developer/Applications")
 		(subpath "/System/Developer/Applications")
 		(subpath "/private/var/containers/Bundle")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")
 		(subpath "/private/var/personalized_debug/Applications")

 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "/System/Library/Carrier Bundles")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 																		(require-any
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																			(require-all
 																				(subpath "${HOME}")

 																							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																							(require-all
 																								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																								(extension "com.apple.shortcuts.access.location")
+																								(require-any
+																									(extension "com.apple.shortcuts.access.location")
+																									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																								)
 																							)
 																						)
 																					)
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)

 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "/private/var")
 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 		(require-any
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/usr/sbin/fairplayd")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-							(subpath "${HOME}/Library/FairPlay")
+							(require-any
+								(literal "/usr/sbin/fairplayd")
+								(subpath "${HOME}/Library/FairPlay")
+							)
 						)
 					)
-					(subpath "${HOME}/Library/FairPlay")
+					(require-any
+						(literal "/usr/sbin/fairplayd")
+						(subpath "${HOME}/Library/FairPlay")
+					)
 				)
 			)
-			(subpath "${HOME}/Library/FairPlay")
+			(require-any
+				(literal "/usr/sbin/fairplayd")
+				(subpath "${HOME}/Library/FairPlay")
+			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

 		(require-any
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 						)
 					)
 					(require-all
 						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-						(extension "com.apple.shortcuts.access.location")
+						(require-any
+							(extension "com.apple.shortcuts.access.location")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+						)
 					)
 					(require-all
 						(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "${HOME}")

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 					)
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		)
 	)
 )

 
 (allow file-read-metadata
 	(require-all
-		(subpath "${HOME}/Media/Debug")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Media/PhotoData")
+		(extension "com.apple.shortcuts.access.photos")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "${HOME}/Media/Photos")
 		(extension "com.apple.shortcuts.access.photos")
 	)
 )

 		(extension "com.apple.shortcuts.access.photos")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "${HOME}/Media/Memories")
-		(extension "com.apple.shortcuts.access.photos")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.WorkflowKit.BackgroundShortcutRunner")

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "${HOME}/Media/Photos")
+		(subpath "${HOME}/Media/Debug")
 		(extension "com.apple.shortcuts.access.photos")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
+		(extension "com.apple.clouddocs.version")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "${HOME}/Library/Mobile Documents")

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "${HOME}/Media/PhotoData")
+		(subpath "${HOME}/Media/DCIM")
 		(extension "com.apple.shortcuts.access.photos")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(subpath "${HOME}/Media/DCIM")
+		(subpath "${HOME}/Media/Memories")
 		(extension "com.apple.shortcuts.access.photos")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "${HOME}/Library/AddressBook")
+		(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+		(subpath "${HOME}/Library/AddressBook")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read-metadata

 	(require-all
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read-metadata

 		(extension "com.apple.shortcuts.access.location")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.Pasteboard")
-		(extension "com.apple.Pasteboard-readonly")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")

 		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.Pasteboard")
+		(extension "com.apple.Pasteboard-readonly")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "/System/Library/Carrier Bundles")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 																		(require-any
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																			(require-all
 																				(subpath "${HOME}")

 																							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																							(require-all
 																								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																								(extension "com.apple.shortcuts.access.location")
+																								(require-any
+																									(extension "com.apple.shortcuts.access.location")
+																									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																								)
 																							)
 																						)
 																					)
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)

 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "/private/var")
 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 		(require-any
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/usr/sbin/fairplayd")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-							(subpath "${HOME}/Library/FairPlay")
+							(require-any
+								(literal "/usr/sbin/fairplayd")
+								(subpath "${HOME}/Library/FairPlay")
+							)
 						)
 					)
-					(subpath "${HOME}/Library/FairPlay")
+					(require-any
+						(literal "/usr/sbin/fairplayd")
+						(subpath "${HOME}/Library/FairPlay")
+					)
 				)
 			)
-			(subpath "${HOME}/Library/FairPlay")
+			(require-any
+				(literal "/usr/sbin/fairplayd")
+				(subpath "${HOME}/Library/FairPlay")
+			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

 		(require-any
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 						)
 					)
 					(require-all
 						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-						(extension "com.apple.shortcuts.access.location")
+						(require-any
+							(extension "com.apple.shortcuts.access.location")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+						)
 					)
 					(require-all
 						(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "${HOME}")

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 					)
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
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

 		(subpath "/Developer/Applications")
 		(subpath "/System/Developer/Applications")
 		(subpath "/private/var/containers/Bundle")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")
 		(subpath "/private/var/personalized_debug/Applications")

 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "/System/Library/Carrier Bundles")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 																		(require-any
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																			(require-all
 																				(subpath "${HOME}")

 																							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																							(require-all
 																								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																								(extension "com.apple.shortcuts.access.location")
+																								(require-any
+																									(extension "com.apple.shortcuts.access.location")
+																									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																								)
 																							)
 																						)
 																					)
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)

 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "/private/var")
 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 		(require-any
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/usr/sbin/fairplayd")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-							(subpath "${HOME}/Library/FairPlay")
+							(require-any
+								(literal "/usr/sbin/fairplayd")
+								(subpath "${HOME}/Library/FairPlay")
+							)
 						)
 					)
-					(subpath "${HOME}/Library/FairPlay")
+					(require-any
+						(literal "/usr/sbin/fairplayd")
+						(subpath "${HOME}/Library/FairPlay")
+					)
 				)
 			)
-			(subpath "${HOME}/Library/FairPlay")
+			(require-any
+				(literal "/usr/sbin/fairplayd")
+				(subpath "${HOME}/Library/FairPlay")
+			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

 		(require-any
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 						)
 					)
 					(require-all
 						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-						(extension "com.apple.shortcuts.access.location")
+						(require-any
+							(extension "com.apple.shortcuts.access.location")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+						)
 					)
 					(require-all
 						(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "${HOME}")

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 					)
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		)
 	)
 )

 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "/System/Library/Carrier Bundles")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 																		(require-any
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																			(require-all
 																				(subpath "${HOME}")

 																							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																							(require-all
 																								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																								(extension "com.apple.shortcuts.access.location")
+																								(require-any
+																									(extension "com.apple.shortcuts.access.location")
+																									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																								)
 																							)
 																						)
 																					)
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)

 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "/private/var")
 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 		(extension "com.apple.shortcuts.access.location")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(subpath "${HOME}/Library/AddressBook")
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
-		(extension "com.apple.tcc.kTCCServiceAddressBook")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read-xattr

 		)
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(subpath "${HOME}/Library/AddressBook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-read-xattr

 		(require-any
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/usr/sbin/fairplayd")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-							(subpath "${HOME}/Library/FairPlay")
+							(require-any
+								(literal "/usr/sbin/fairplayd")
+								(subpath "${HOME}/Library/FairPlay")
+							)
 						)
 					)
-					(subpath "${HOME}/Library/FairPlay")
+					(require-any
+						(literal "/usr/sbin/fairplayd")
+						(subpath "${HOME}/Library/FairPlay")
+					)
 				)
 			)
-			(subpath "${HOME}/Library/FairPlay")
+			(require-any
+				(literal "/usr/sbin/fairplayd")
+				(subpath "${HOME}/Library/FairPlay")
+			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

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

 		(require-any
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 						)
 					)
 					(require-all
 						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-						(extension "com.apple.shortcuts.access.location")
+						(require-any
+							(extension "com.apple.shortcuts.access.location")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+						)
 					)
 					(require-all
 						(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "${HOME}")

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 					)
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		)
 	)
 )

 		(subpath "/Developer/Applications")
 		(subpath "/System/Developer/Applications")
 		(subpath "/private/var/containers/Bundle")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")
 		(subpath "/private/var/personalized_debug/Applications")

 			(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "/System/Library/Carrier Bundles")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 																		(require-any
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																			(require-all
 																				(subpath "${HOME}")

 																							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																							(require-all
 																								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																								(extension "com.apple.shortcuts.access.location")
+																								(require-any
+																									(extension "com.apple.shortcuts.access.location")
+																									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																								)
 																							)
 																						)
 																					)
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)

 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "/private/var")
 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 																(require-any
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																	(require-all
 																		(subpath "${HOME}")

 																					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																					(require-all
 																						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																						(extension "com.apple.shortcuts.access.location")
+																						(require-any
+																							(extension "com.apple.shortcuts.access.location")
+																							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																						)
 																					)
 																				)
 																			)
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)

 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "/private/var")
 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 														(require-any
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 															(require-all
 																(subpath "${HOME}")

 																			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																			(require-all
 																				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																				(extension "com.apple.shortcuts.access.location")
+																				(require-any
+																					(extension "com.apple.shortcuts.access.location")
+																					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																				)
 																			)
 																		)
 																	)
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)

 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "/private/var")
 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 		(require-any
 			(literal "${HOME}/Library/Caches/Checkpoint.plist")
 			(literal "${HOME}/Media/Vibrations/UserGeneratedVibrationPatterns.plist")
-			(literal "/usr/sbin/fairplayd")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com\.apple\.ToneLibrary$")
-							(subpath "${HOME}/Library/FairPlay")
+							(require-any
+								(literal "/usr/sbin/fairplayd")
+								(subpath "${HOME}/Library/FairPlay")
+							)
 						)
 					)
-					(subpath "${HOME}/Library/FairPlay")
+					(require-any
+						(literal "/usr/sbin/fairplayd")
+						(subpath "${HOME}/Library/FairPlay")
+					)
 				)
 			)
-			(subpath "${HOME}/Library/FairPlay")
+			(require-any
+				(literal "/usr/sbin/fairplayd")
+				(subpath "${HOME}/Library/FairPlay")
+			)
 			(subpath "${HOME}/Media/DCIM")
 			(subpath "${HOME}/Media/Debug")
 			(subpath "${HOME}/Media/MediaAnalysis")

 		(require-any
 			(require-all
 				(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-				(extension "com.apple.shortcuts.access.location")
+				(require-any
+					(extension "com.apple.shortcuts.access.location")
+					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+				)
 			)
 			(require-all
 				(subpath "${HOME}")

 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 								)
 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 						)
 					)
 					(require-all
 						(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-						(extension "com.apple.shortcuts.access.location")
+						(require-any
+							(extension "com.apple.shortcuts.access.location")
+							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+						)
 					)
 					(require-all
 						(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 							)
 							(require-all
 								(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-								(extension "com.apple.shortcuts.access.location")
+								(require-any
+									(extension "com.apple.shortcuts.access.location")
+									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+								)
 							)
 							(require-all
 								(subpath "/private/var")
 								(require-any
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "${HOME}")

 													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 										)
 									)

 												(require-any
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 													(require-all
 														(subpath "${HOME}")

 																	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 																	(require-all
 																		(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																		(extension "com.apple.shortcuts.access.location")
+																		(require-any
+																			(extension "com.apple.shortcuts.access.location")
+																			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																		)
 																	)
 																)
 															)
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)

 									)
 									(require-all
 										(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-										(extension "com.apple.shortcuts.access.location")
+										(require-any
+											(extension "com.apple.shortcuts.access.location")
+											(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+										)
 									)
 									(require-all
 										(subpath "/private/var")
 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 										(require-any
 											(require-all
 												(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-												(extension "com.apple.shortcuts.access.location")
+												(require-any
+													(extension "com.apple.shortcuts.access.location")
+													(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+												)
 											)
 											(require-all
 												(subpath "${HOME}")

 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes(/|$)")
 															(require-all
 																(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-																(extension "com.apple.shortcuts.access.location")
+																(require-any
+																	(extension "com.apple.shortcuts.access.location")
+																	(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+																)
 															)
 														)
 													)
 													(require-all
 														(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-														(extension "com.apple.shortcuts.access.location")
+														(require-any
+															(extension "com.apple.shortcuts.access.location")
+															(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
+														)
 													)
 												)
 											)

 					)
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles")
 		)
 	)
 )

 		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/AddressBook")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-write*
 	(require-all
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-write*

 	(require-all
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-write-create

 		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/AddressBook")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-write-create

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 							(require-all
-								(vnode-type DIRECTORY)
+								(subpath "/private/var/PersonaVolumes")
 								(require-any
-									(literal "${HOME}/Library/Caches")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 									(require-all
-										(subpath "/private/var")
-										(subpath "${HOME}")
-										(extension "com.apple.shortcuts.access.music-library")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(vnode-type DIRECTORY)
 										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(literal "${HOME}/Library/Caches")
 											(require-all
-												(vnode-type DIRECTORY)
+												(subpath "/private/var")
+												(subpath "${HOME}")
+												(extension "com.apple.shortcuts.access.music-library")
+												(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 												(require-any
 													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+														)
+													)
 												)
 											)
 										)

 						(require-any
 							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
+								(vnode-type DIRECTORY)
 								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+									(literal "${HOME}/Library/Caches")
 									(require-all
-										(vnode-type DIRECTORY)
+										(subpath "/private/var")
+										(subpath "${HOME}")
+										(extension "com.apple.shortcuts.access.music-library")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 										(require-any
-											(literal "${HOME}/Library/Caches")
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 											(require-all
-												(subpath "/private/var")
-												(subpath "${HOME}")
-												(extension "com.apple.shortcuts.access.music-library")
-												(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+												(vnode-type DIRECTORY)
 												(require-any
 													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-														)
-													)
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
 												)
 											)
 										)

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 							(require-all
-								(vnode-type DIRECTORY)
+								(subpath "/private/var/PersonaVolumes")
 								(require-any
-									(literal "${HOME}/Library/Caches")
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 									(require-all
-										(subpath "/private/var")
-										(subpath "${HOME}")
-										(extension "com.apple.shortcuts.access.music-library")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(vnode-type DIRECTORY)
 										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(literal "${HOME}/Library/Caches")
 											(require-all
-												(vnode-type DIRECTORY)
+												(subpath "/private/var")
+												(subpath "${HOME}")
+												(extension "com.apple.shortcuts.access.music-library")
+												(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 												(require-any
 													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+													(require-all
+														(vnode-type DIRECTORY)
+														(require-any
+															(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+														)
+													)
 												)
 											)
 										)

 						(require-any
 							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
 							(require-all
-								(subpath "${FRONT_USER_HOME}")
+								(vnode-type DIRECTORY)
 								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+									(literal "${HOME}/Library/Caches")
 									(require-all
-										(vnode-type DIRECTORY)
+										(subpath "/private/var")
+										(subpath "${HOME}")
+										(extension "com.apple.shortcuts.access.music-library")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 										(require-any
-											(literal "${HOME}/Library/Caches")
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
 											(require-all
-												(subpath "/private/var")
-												(subpath "${HOME}")
-												(extension "com.apple.shortcuts.access.music-library")
-												(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+												(vnode-type DIRECTORY)
 												(require-any
 													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(require-all
-														(vnode-type DIRECTORY)
-														(require-any
-															(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-														)
-													)
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
 												)
 											)
 										)

 	(require-all
 		(subpath "${HOME}/Library/AddressBook/Delegates")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-write-unlink

 		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/AddressBook")
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-		(extension "com.apple.shortcuts.access.contacts")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
+		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
 (allow file-write-unlink

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cmfsyncagent.embedded.auth")
+		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
 		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.spotlight.IndexDelegateAgent")
-		(extension "com.apple.shortcuts.access.contacts")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.locationd.spi")
-		(extension "com.apple.shortcuts.access.location")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.spotlight.IndexAgent")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.medialibraryd.xpc")
+		(global-name "com.apple.itunescloudd.xpc")
 		(extension "com.apple.shortcuts.access.music-library")
 	)
 )

 		(extension "com.apple.shortcuts.access.contacts")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.locationd.spi")
+		(extension "com.apple.shortcuts.access.location")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.spotlight.IndexDelegateAgent")
+		(extension "com.apple.shortcuts.access.contacts")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.homed.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.healthd.server")
+		(global-name "com.apple.healthd.restriction")
 		(extension "com.apple.shortcuts.access.health")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.itunescloudd.xpc")
+		(global-name "com.apple.medialibraryd.xpc")
 		(extension "com.apple.shortcuts.access.music-library")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
+		(global-name "com.apple.cmfsyncagent.embedded.auth")
 		(extension "com.apple.shortcuts.access.contacts")
 	)
 )

 		(extension "com.apple.shortcuts.access.photos")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.remindd")
+		(extension "com.apple.shortcuts.access.calendar")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.calaccessd.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.remindd")
-		(extension "com.apple.shortcuts.access.calendar")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.healthd.restriction")
+		(global-name "com.apple.healthd.server")
 		(extension "com.apple.shortcuts.access.health")
 	)
 )

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(extension "com.apple.shortcuts.access.music-library")
-		(require-any
-			(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
-			(global-name "com.apple.fairplay.xpc")
-			(global-name "com.apple.fairplayd")
-			(global-name "com.apple.fairplayd.versioned")
-		)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(extension "com.apple.shortcuts.access.photos")

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(extension "com.apple.shortcuts.access.music-library")
+		(require-any
+			(global-name "com.apple.Music.MPMusicPlayerControllerInternal")
+			(global-name "com.apple.fairplay.xpc")
+			(global-name "com.apple.fairplayd")
+			(global-name "com.apple.fairplayd.versioned")
+		)
+	)
+)
 (allow mach-lookup
 	(require-all
 		(require-not (xpc-service-name "*"))

 			(global-name "com.apple.itunescloudd.xpc")
 			(global-name "com.apple.itunesstored.xpc")
 			(global-name "com.apple.librariand")
-			(global-name "com.apple.lsd.advertisingidentifiers")
-			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.marco")
 			(global-name "com.apple.mediaremoted.xpc")
 			(global-name "com.apple.mediaserverd")

 				(global-name "com.apple.cvmsServ")
 				(global-name "com.apple.gpumemd.source")
 			)
+			(require-any
+				(global-name "com.apple.lsd.advertisingidentifiers")
+				(global-name "com.apple.lsd.openurl")
+			)
 			(require-any
 				(global-name "com.apple.timesync.expositor")
 				(global-name "com.apple.timesync.manager")

 			(global-name "com.apple.itunescloudd.xpc")
 			(global-name "com.apple.itunesstored.xpc")
 			(global-name "com.apple.librariand")
-			(global-name "com.apple.lsd.advertisingidentifiers")
-			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.marco")
 			(global-name "com.apple.mediaremoted.xpc")
 			(global-name "com.apple.mediaserverd")

 				(global-name "com.apple.cvmsServ")
 				(global-name "com.apple.gpumemd.source")
 			)
+			(require-any
+				(global-name "com.apple.lsd.advertisingidentifiers")
+				(global-name "com.apple.lsd.openurl")
+			)
 			(require-any
 				(global-name "com.apple.timesync.expositor")
 				(global-name "com.apple.timesync.manager")

 	(require-all
 		(extension "com.apple.shortcuts.access.internet")
 		(require-any
+			(require-any
+				(sysctl-name "kern.nisdomainname")
+				(sysctl-name "net.statistics")
+			)
 			(sysctl-name "kern.ipc.maxsockbuf")
-			(sysctl-name "kern.nisdomainname")
 			(sysctl-name "net.routetable.*")
-			(sysctl-name "net.statistics")
 		)
 	)
 )

 		(extension "com.apple.shortcuts.access.photos")
 	)
 )
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.CFNetwork")
+		(extension "com.apple.shortcuts.access.internet")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.GEO")
+		(extension "com.apple.shortcuts.access.location")
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.carrier")
+		(extension "com.apple.shortcuts.access.location")
+	)
+)
 (allow user-preference-read
 	(require-all
 		(extension "com.apple.shortcuts.access.location")

 			(preference-domain "com.apple.AppSupport")
 			(preference-domain "com.apple.GEO")
 			(preference-domain "com.apple.locationd")
-			(require-all
-				(preference-domain "com.apple.carrier")
-				(extension "com.apple.shortcuts.access.location")
-			)
 		)
 	)
 )
 (allow user-preference-read
 	(require-all
-		(require-not (preference-domain "com.apple.GEO"))
+		(preference-domain "com.apple.itunesstored")
+		(process-attribute is-apple-signed-executable)
+		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
+	)
+)
+(allow user-preference-read
+	(require-all
+		(extension "com.apple.shortcuts.access.calendar")
 		(require-any
-			(require-all
-				(extension "com.apple.shortcuts.access.calendar")
-				(require-any
-					(preference-domain "com.apple.mobilecal")
-					(preference-domain "com.apple.mobilecal.alarmengine")
-					(require-all
-						(preference-domain "com.apple.itunesstored")
-						(process-attribute is-apple-signed-executable)
-						(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
-					)
-				)
-			)
-			(require-all
-				(preference-domain "com.apple.CFNetwork")
-				(extension "com.apple.shortcuts.access.internet")
-			)
-			(require-all
-				(preference-domain "com.apple.carrier")
-				(extension "com.apple.shortcuts.access.location")
-			)
-			(require-all
-				(preference-domain "com.apple.itunesstored")
-				(process-attribute is-apple-signed-executable)
-				(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
-			)
+			(preference-domain "com.apple.mobilecal")
+			(preference-domain "com.apple.mobilecal.alarmengine")
 		)
 	)
 )

 		(extension "com.apple.shortcuts.access.photos")
 	)
 )
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.CFNetwork")
+		(extension "com.apple.shortcuts.access.internet")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.GEO")
+		(extension "com.apple.shortcuts.access.location")
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.carrier")
+		(extension "com.apple.shortcuts.access.location")
+	)
+)
 (allow managed-preference-read
 	(require-all
 		(extension "com.apple.shortcuts.access.location")

 			(preference-domain "com.apple.AppSupport")
 			(preference-domain "com.apple.GEO")
 			(preference-domain "com.apple.locationd")
-			(require-all
-				(preference-domain "com.apple.carrier")
-				(extension "com.apple.shortcuts.access.location")
-			)
 		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(require-not (preference-domain "com.apple.GEO"))
+		(preference-domain "com.apple.itunesstored")
+		(process-attribute is-apple-signed-executable)
+		(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(extension "com.apple.shortcuts.access.calendar")
 		(require-any
-			(require-all
-				(extension "com.apple.shortcuts.access.calendar")
-				(require-any
-					(preference-domain "com.apple.mobilecal")
-					(preference-domain "com.apple.mobilecal.alarmengine")
-					(require-all
-						(preference-domain "com.apple.itunesstored")
-						(process-attribute is-apple-signed-executable)
-						(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
-					)
-				)
-			)
-			(require-all
-				(preference-domain "com.apple.CFNetwork")
-				(extension "com.apple.shortcuts.access.internet")
-			)
-			(require-all
-				(preference-domain "com.apple.carrier")
-				(extension "com.apple.shortcuts.access.location")
-			)
-			(require-all
-				(preference-domain "com.apple.itunesstored")
-				(process-attribute is-apple-signed-executable)
-				(require-not (%entitlement-is-bool-true "com.apple.itunesstored.private"))
-			)
+			(preference-domain "com.apple.mobilecal")
+			(preference-domain "com.apple.mobilecal.alarmengine")
 		)
 	)
 )
```
