## progressd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/tmp/com.apple.progressd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/ClassKit")
+			(subpath "${HOME}/Library/Caches/com.apple.progressd")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/tmp/com.apple.progressd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/tmp/com.apple.progressd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/ClassKit")
+			(subpath "${HOME}/Library/Caches/com.apple.progressd")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "/private/var/tmp/com.apple.progressd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/ClassKit")
+			(subpath "${HOME}/Library/Caches/com.apple.progressd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/ClassKit")
+			(subpath "${HOME}/Library/Caches/com.apple.progressd")
+		)
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 				(require-any
 					(require-all
 						(subpath "/private/var")
-						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
-								)
-							)
-							(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
-						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+						(subpath "${FRONT_USER_HOME}")
 					)
-					(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 					(subpath "${HOME}/Library/Mobile Documents")
 					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
 				)
 			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-							)
-							(require-all
-								(extension "com.apple.librarian.ubiquity-container")
-								(require-any
-									(require-all
-										(subpath "/private/var")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-										(subpath "${FRONT_USER_HOME}")
-									)
-									(subpath "${HOME}/Library/Mobile Documents")
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-								)
-							)
-						)
-					)
-				)
-			)
 			(require-any
-				(subpath "${HOME}/Library//private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+				(subpath "${HOME}/Library//private/var/tmp/com.apple.progressd")
 				(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd")
-				(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+				(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/tmp/com.apple.progressd")
 				(subpath "${HOME}/Library/Mobile Documents/iCloud~com~apple~homeroom")
-				(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+				(subpath "${HOME}/private/var/tmp/com.apple.progressd")
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.progressd")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+				(subpath "/private/var/tmp/com.apple.progressd")
 			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/ClassKit")
 				(subpath "${HOME}/Library/Caches/com.apple.progressd")
 			)
 			(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
-			(subpath "/private/var/tmp/com.apple.progressd")
 		)
 	)
 )

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/ClassKit")
-			(subpath "${HOME}/Library/Caches/com.apple.progressd")
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.nsurlsessiond.readonly")

 )
 (allow file-read*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")

 )
 (allow file-read*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")

 		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/private/var/preferences/com.apple.security.plist")
 		(subpath "${FRONT_USER_HOME}/Library/ClassKit")
-		(subpath "${HOME}/Library//private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library//private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Caches/ClassKit")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 		(subpath "${HOME}/Library/Caches/com.apple.progressd")
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Mobile Documents/iCloud~com~apple~homeroom")
-		(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/private/var/tmp/com.apple.progressd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.progressd")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
 		(subpath "/private/var/tmp/com.apple.progressd")

 )
 (allow file-read-data
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")

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
 )
 (allow file-read-data
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")

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

 		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/private/var/preferences/com.apple.security.plist")
 		(subpath "${FRONT_USER_HOME}/Library/ClassKit")
-		(subpath "${HOME}/Library//private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library//private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Caches/ClassKit")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 		(subpath "${HOME}/Library/Caches/com.apple.progressd")
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Mobile Documents/iCloud~com~apple~homeroom")
-		(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/private/var/tmp/com.apple.progressd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.progressd")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
 		(subpath "/private/var/tmp/com.apple.progressd")

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
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")

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
 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")

 		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/private/var/preferences/com.apple.security.plist")
 		(subpath "${FRONT_USER_HOME}/Library/ClassKit")
-		(subpath "${HOME}/Library//private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library//private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Caches/ClassKit")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 		(subpath "${HOME}/Library/Caches/com.apple.progressd")
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Mobile Documents/iCloud~com~apple~homeroom")
-		(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/private/var/tmp/com.apple.progressd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.progressd")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
 		(subpath "/private/var/tmp/com.apple.progressd")

 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")

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
 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")

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

 		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/private/var/preferences/com.apple.security.plist")
 		(subpath "${FRONT_USER_HOME}/Library/ClassKit")
-		(subpath "${HOME}/Library//private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library//private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Caches/ClassKit")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 		(subpath "${HOME}/Library/Caches/com.apple.progressd")
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Mobile Documents/iCloud~com~apple~homeroom")
-		(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/private/var/tmp/com.apple.progressd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.progressd")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
 		(subpath "/private/var/tmp/com.apple.progressd")

 )
 (allow file-write*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type SYMLINK)
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 		)
+		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write*

 )
 (allow file-write*
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type DIRECTORY)
 		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")
 		)
-		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any

 		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/.ClassKit*")
 		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit*")
 		(subpath "${FRONT_USER_HOME}/Library/ClassKit")
-		(subpath "${HOME}/Library//private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library//private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Caches/ClassKit")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 		(subpath "${HOME}/Library/Caches/com.apple.progressd")
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Mobile Documents/iCloud~com~apple~homeroom")
-		(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/private/var/tmp/com.apple.progressd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.progressd")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
 		(subpath "/private/var/tmp/com.apple.progressd")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type SYMLINK)
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 		)
+		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write-create

 )
 (allow file-write-create
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type DIRECTORY)
 		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")
 		)
-		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any

 		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/.ClassKit*")
 		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit*")
 		(subpath "${FRONT_USER_HOME}/Library/ClassKit")
-		(subpath "${HOME}/Library//private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library//private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Caches/ClassKit")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 		(subpath "${HOME}/Library/Caches/com.apple.progressd")
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Mobile Documents/iCloud~com~apple~homeroom")
-		(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/private/var/tmp/com.apple.progressd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.progressd")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
 		(subpath "/private/var/tmp/com.apple.progressd")

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type SYMLINK)
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 		)
+		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write-unlink

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type DIRECTORY)
 		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/ClassKit")
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.progressd")
 		)
-		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any

 		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/.ClassKit*")
 		(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/ClassKit*")
 		(subpath "${FRONT_USER_HOME}/Library/ClassKit")
-		(subpath "${HOME}/Library//private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library//private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Caches/ClassKit")
 		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 		(subpath "${HOME}/Library/Caches/com.apple.progressd")
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.progressd/private/var/tmp/com.apple.progressd")
 		(subpath "${HOME}/Library/Mobile Documents/iCloud~com~apple~homeroom")
-		(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
+		(subpath "${HOME}/private/var/tmp/com.apple.progressd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.progressd")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents/iCloud~com~apple~homeroom")
 		(subpath "/private/var/tmp/com.apple.progressd")
```
