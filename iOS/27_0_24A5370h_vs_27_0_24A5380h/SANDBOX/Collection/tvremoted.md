## tvremoted

> Group: ⬆️ Updated

```diff

 
 (allow file-graft)
 
+(allow file-issue-extension
+	(require-all
+		(subpath "/private/var/tmp/com.apple.tvremoted")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.nsurlsessiond.readonly")

 )
 (allow file-issue-extension
 	(require-all
+		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.tvremoted")
-			(subpath "/private/var/tmp/com.apple.tvremoted")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
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
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
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
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension-class "com.apple.aned.read-only")
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
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
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
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(require-all
+								(extension-class "com.apple.mediaserverd.read")
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
 		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.tvremoted")
 		(require-any
 			(extension-class "com.apple.aned.read-only")
 			(extension-class "com.apple.app-sandbox.read")

 		)
 	)
 )
+(deny file-issue-extension
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
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
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
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
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension-class "com.apple.aned.read-only")
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
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension-class "com.apple.mediaserverd.read")
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
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(require-all
+								(extension-class "com.apple.mediaserverd.read")
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
 
 (allow file-link)
 

 		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
+(allow file-map-executable
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+					(%entitlement-is-bool-true "get-task-allow")
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				(%entitlement-is-bool-true "get-task-allow")
+			)
+		)
+	)
+)
 (allow file-map-executable
 	(require-all
 		(system-attribute carrier-build)

 
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
 		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
 	)
 )
 (allow file-read*

 		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
+(allow file-read*
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "/AppleInternal")

 		(subpath "/private/var/tmp/com.apple.tvremoted")
 	)
 )
+(deny file-read*
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
 (deny file-read*
 	(require-any
 		(literal "/System/Library/Caches/apticket.der")

 
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
 		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
 	)
 )
 (allow file-read-metadata

 		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "/AppleInternal")

 		(subpath "/private/var/tmp/com.apple.tvremoted")
 	)
 )
+(deny file-read-metadata
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
 (deny file-read-metadata
 	(require-any
 		(literal "/System/Library/Caches/apticket.der")

 
 (allow file-ungraft)
 
+(allow file-write*
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
 (allow file-write*
 	(require-any
 		(subpath "${HOME}/Library/Caches/com.apple.HomeKit.configurations/tvremoted")

 		(subpath "/private/var/tmp/com.apple.tvremoted")
 	)
 )
+(deny file-write*
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
 
+(allow file-write-create
+	(require-all
+		(vnode-type DIRECTORY)
+		(subpath "/private/var/tmp/com.apple.tvremoted")
+	)
+)
+(allow file-write-create
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(allow file-write-create
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(extension "com.apple.sandbox.application-group")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+					)
+					(subpath "/private/var/tmp/com.apple.tvremoted")
+				)
+			)
+			(subpath "/private/var/tmp/com.apple.tvremoted")
+		)
+	)
+)
 (allow file-write-create
 	(require-any
 		(subpath "${HOME}/Library/Caches/com.apple.HomeKit.configurations/tvremoted")
 		(subpath "${HOME}/Library/Caches/com.apple.HomeKit/tvremoted")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.tvremoted")
-		(subpath "/private/var/tmp/com.apple.tvremoted")
 	)
 )
 (deny file-write-create
 	(with no-report)
 	(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")
 )
+(deny file-write-create
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(deny file-write-create
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(extension "com.apple.sandbox.application-group")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/Library|/Library/Preferences)$")
+					)
+					(subpath "/private/var/tmp/com.apple.tvremoted")
+				)
+			)
+			(subpath "/private/var/tmp/com.apple.tvremoted")
+		)
+	)
+)
 
 (deny file-write-setugid)
 

 		(subpath "/private/var/OOPJit")
 	)
 )
+(allow file-write-unlink
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
 (allow file-write-unlink
 	(require-any
 		(subpath "${HOME}/Library/Caches/com.apple.HomeKit.configurations/tvremoted")

 		(subpath "/private/var/tmp/com.apple.tvremoted")
 	)
 )
+(deny file-write-unlink
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/.com.apple.*")
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/\.com\.apple\.")
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						)
+					)
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
 
 (allow fs-info)
 

 	)
 )
 
+(allow ipc-posix-sem*
+	(extension "com.apple.sandbox.application-group")
+)
+
+(allow ipc-posix-shm*
+	(extension "com.apple.sandbox.application-group")
+)
+
 (allow ipc-posix-shm-read-data
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
-		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
+		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
 	)
 )
 (allow ipc-posix-shm-read-data
-	(ipc-posix-name "/com.apple.AppSSO.version")
+	(require-any
+		(extension "com.apple.sandbox.application-group")
+		(ipc-posix-name "/com.apple.AppSSO.version")
+	)
 )
 
 (deny job-creation)

 )
 (allow mach-lookup
 	(require-any
+		(extension "com.apple.sandbox.application-group")
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")
 		(global-name "com.apple.AppSSO.service-xpc")

 )
 
 (allow mach-register
-	(extension "com.apple.security.exception.mach-register.global-name")
+	(require-any
+		(extension "com.apple.sandbox.application-group")
+		(extension "com.apple.security.exception.mach-register.global-name")
+	)
 )
 
 (allow mach-task-exception-port-set)
```
