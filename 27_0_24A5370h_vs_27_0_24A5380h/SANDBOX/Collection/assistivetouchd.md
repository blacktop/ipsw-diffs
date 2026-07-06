## assistivetouchd

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
 		(extension-class "com.apple.nsurlsessiond.readonly")

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
 		(subpath "${HOME}/Library/Caches/com.apple.assistivetouchd")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.assistivetouchd")
 	)
 )

 		(preference-domain "com.apple.SpeakSelection")
 		(preference-domain "com.apple.UIKit")
 		(preference-domain "com.apple.VideoConference")
+		(preference-domain "com.apple.assistant.public")
 		(preference-domain "com.apple.assistant.support")
 		(preference-domain "com.apple.assistivetouchd")
 		(preference-domain "com.apple.avfaudio")

 		(preference-domain "com.apple.SpeakSelection")
 		(preference-domain "com.apple.UIKit")
 		(preference-domain "com.apple.VideoConference")
+		(preference-domain "com.apple.assistant.public")
 		(preference-domain "com.apple.assistant.support")
 		(preference-domain "com.apple.assistivetouchd")
 		(preference-domain "com.apple.avfaudio")
```
