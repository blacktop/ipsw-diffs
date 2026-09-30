## duetexpertd

> Group: ⬆️ Updated

```diff

 
 (allow file-graft)
 
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.security.exception.files.home-relative-path.read-write")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension "com.apple.sandbox.application-group")

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.mediaserverd.read")
-								)
-							)
-							(subpath "${FRONT_USER_HOME}")
+							(extension-class "com.apple.aned.read-only")
+							(extension-class "com.apple.app-sandbox.read")
+							(extension-class "com.apple.mediaserverd.read")
 						)
 					)
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-								(extension-class "com.apple.aned.read-only")
-							)
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.mediaserverd.read")
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+										(extension-class "com.apple.mediaserverd.read")
+									)
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+										(require-any
+											(extension-class "com.apple.aned.read-only")
+											(extension-class "com.apple.app-sandbox.read")
+											(extension-class "com.apple.mediaserverd.read")
+										)
+									)
 								)
 							)
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 						(require-any
-							(extension-class "com.apple.aned.read-only")
-							(extension-class "com.apple.app-sandbox.read")
-							(extension-class "com.apple.mediaserverd.read")
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(extension-class "com.apple.mediaserverd.read")
+							)
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(require-any
+									(extension-class "com.apple.aned.read-only")
+									(extension-class "com.apple.app-sandbox.read")
+									(extension-class "com.apple.mediaserverd.read")
+								)
+							)
 						)
 					)
 				)

 				(subpath "/private/var")
 				(require-any
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(subpath "${FRONT_USER_HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.mediaserverd.read")
-								)
-							)
-							(subpath "${FRONT_USER_HOME}")
+							(extension-class "com.apple.aned.read-only")
+							(extension-class "com.apple.app-sandbox.read")
+							(extension-class "com.apple.mediaserverd.read")
 						)
 					)
 					(require-all
 						(subpath "${FRONT_USER_HOME}")
 						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-								(extension-class "com.apple.aned.read-only")
-							)
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
 							(require-all
 								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 								(require-any
-									(extension-class "com.apple.aned.read-only")
-									(extension-class "com.apple.app-sandbox.read")
-									(extension-class "com.apple.mediaserverd.read")
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+										(extension-class "com.apple.mediaserverd.read")
+									)
+									(require-all
+										(subpath "${FRONT_USER_HOME}")
+										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+										(require-any
+											(extension-class "com.apple.aned.read-only")
+											(extension-class "com.apple.app-sandbox.read")
+											(extension-class "com.apple.mediaserverd.read")
+										)
+									)
 								)
 							)
 						)
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 						(require-any
-							(extension-class "com.apple.aned.read-only")
-							(extension-class "com.apple.app-sandbox.read")
-							(extension-class "com.apple.mediaserverd.read")
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(extension-class "com.apple.mediaserverd.read")
+							)
+							(require-all
+								(subpath "${FRONT_USER_HOME}")
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+								(require-any
+									(extension-class "com.apple.aned.read-only")
+									(extension-class "com.apple.app-sandbox.read")
+									(extension-class "com.apple.mediaserverd.read")
+								)
+							)
 						)
 					)
 				)

 (allow file-write*
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
 		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write*
 	(require-all
 		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
-			)
-			(subpath "/private/var/tmp")
-		)
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write*

 		(subpath "${HOME}/Library/Logs/CallHistory")
 		(subpath "${HOME}/Library/Logs/com.apple.duetexpertd")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write*

 (allow file-write-create
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
 		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-create
 	(require-all
 		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
-			)
-			(subpath "/private/var/tmp")
-		)
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-create

 		(subpath "${HOME}/Library/Logs/CallHistory")
 		(subpath "${HOME}/Library/Logs/com.apple.duetexpertd")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write-create

 (allow file-write-mode
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
 		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-mode
 	(require-all
 		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
-			)
-			(subpath "/private/var/tmp")
-		)
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-mode

 		(subpath "${HOME}/Library/Logs/CallHistory")
 		(subpath "${HOME}/Library/Logs/com.apple.duetexpertd")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write-mode

 (allow file-write-owner
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
 		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-owner
 	(require-all
 		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
-			)
-			(subpath "/private/var/tmp")
-		)
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-owner

 		(subpath "${HOME}/Library/Logs/CallHistory")
 		(subpath "${HOME}/Library/Logs/com.apple.duetexpertd")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write-owner

 (allow file-write-unlink
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
 		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-unlink
 	(require-all
 		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
-			)
-			(subpath "/private/var/tmp")
-		)
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-unlink

 		(subpath "${HOME}/Library/Logs/CallHistory")
 		(subpath "${HOME}/Library/Logs/com.apple.duetexpertd")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write-unlink

 (allow file-write-xattr
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
 		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-xattr
 	(require-all
 		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.apppredictionsync")
-			)
-			(subpath "/private/var/tmp")
-		)
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?proactive_")
+		(subpath "${FRONT_USER_HOME}")
 	)
 )
 (allow file-write-xattr

 		(subpath "${HOME}/Library/Logs/CallHistory")
 		(subpath "${HOME}/Library/Logs/com.apple.duetexpertd")
 		(subpath "${PROCESS_TEMP_DIR}")
+		(subpath "/private/var/tmp")
 	)
 )
 (deny file-write-xattr
```
