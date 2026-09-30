## routined

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.routined")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.CoreRoutine.helperservice")
+			(subpath "${HOME}/Library/Caches/com.apple.routined")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.routined")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.routined")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.CoreRoutine.helperservice")
+			(subpath "${HOME}/Library/Caches/com.apple.routined")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.routined")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.CoreRoutine.helperservice")
+			(subpath "${HOME}/Library/Caches/com.apple.routined")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.CoreRoutine.helperservice")
+			(subpath "${HOME}/Library/Caches/com.apple.routined")
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
-				(extension-class "com.apple.mediaserverd.read")
 				(subpath "${HOME}/Library/Cookies")
+				(extension-class "com.apple.aned.read-only")
 			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.CoreRoutine.helperservice")

 		(subpath "/Developer")
 		(subpath "/Library/Audio/Plug-Ins")
 		(subpath "/System")
-		(subpath "/System/Developer/Applications")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Maps")
 		(subpath "/private/var/containers/Bundle")
 		(subpath "/private/var/containers/Data/System/com.apple.geod")

 		(subpath "/Developer")
 		(subpath "/Library/Audio/Plug-Ins")
 		(subpath "/System")
-		(subpath "/System/Developer/Applications")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Maps")
 		(subpath "/private/var/containers/Bundle")
 		(subpath "/private/var/containers/Data/System/com.apple.geod")

 		(subpath "/Developer")
 		(subpath "/Library/Audio/Plug-Ins")
 		(subpath "/System")
-		(subpath "/System/Developer/Applications")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Maps")
 		(subpath "/private/var/containers/Bundle")
 		(subpath "/private/var/containers/Data/System/com.apple.geod")

 )
 (allow file-write*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")

 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")
+			)
 		)
 	)
 )

 )
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")
+			)
 		)
 	)
 )

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CoreRoutine.helperservice")
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.routined")
+			)
 		)
 	)
 )
```
