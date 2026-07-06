## social-services

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.facebook.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.flickr.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.tencentweibo.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.twitter.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.vimeo.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.weibo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.facebook.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.tencentweibo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.twitter.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.vimeo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.weibo.xpc")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.facebook.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.flickr.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.tencentweibo.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.twitter.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.vimeo.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.weibo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.facebook.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.tencentweibo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.twitter.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.vimeo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.weibo.xpc")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.facebook.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.flickr.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.tencentweibo.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.twitter.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.vimeo.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.weibo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.facebook.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.tencentweibo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.twitter.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.vimeo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.weibo.xpc")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.facebook.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.flickr.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.tencentweibo.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.twitter.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.vimeo.xpc")
+			(subpath "${HOME}/Library/Caches/com.apple.weibo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.facebook.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.tencentweibo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.twitter.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.vimeo.xpc")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.weibo.xpc")
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
+				(extension-class "com.apple.aned.read-only")
 				(require-any
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(extension "com.apple.security.exception.files.absolute-path.read-only")
-							(extension "com.apple.security.exception.files.absolute-path.read-write")
-							(extension "com.apple.security.exception.files.home-relative-path.read-only")
-							(extension "com.apple.security.exception.files.home-relative-path.read-write")
-						)
-					)
 					(require-all
 						(subpath "/private/var")
+						(subpath "${HOME}")
 						(require-any
-							(require-all
-								(extension-class "com.apple.mediaserverd.read")
-								(require-any
-									(extension "com.apple.security.exception.files.absolute-path.read-only")
-									(extension "com.apple.security.exception.files.absolute-path.read-write")
-									(extension "com.apple.security.exception.files.home-relative-path.read-only")
-									(extension "com.apple.security.exception.files.home-relative-path.read-write")
-								)
-							)
-							(require-all
-								(subpath "${HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Ringtones.plist$")
-									(require-all
-										(extension-class "com.apple.mediaserverd.read")
-										(require-any
-											(extension "com.apple.security.exception.files.absolute-path.read-only")
-											(extension "com.apple.security.exception.files.absolute-path.read-write")
-											(extension "com.apple.security.exception.files.home-relative-path.read-only")
-											(extension "com.apple.security.exception.files.home-relative-path.read-write")
-										)
-									)
-								)
-							)
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/Ringtones(/|$)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Ringtones.plist$")
 						)
 					)
 					(subpath "${HOME}/Media/Purchases")

 				(subpath "${HOME}/Library/Caches/com.apple.vimeo.xpc")
 				(subpath "${HOME}/Library/Caches/com.apple.weibo.xpc")
 				(subpath "${HOME}/Library/HTTPStorages/com.apple.facebook.xpc")
+				(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
 				(subpath "${HOME}/Library/HTTPStorages/com.apple.tencentweibo.xpc")
 				(subpath "${HOME}/Library/HTTPStorages/com.apple.twitter.xpc")
 				(subpath "${HOME}/Library/HTTPStorages/com.apple.vimeo.xpc")
 				(subpath "${HOME}/Library/HTTPStorages/com.apple.weibo.xpc")
 			)
 			(subpath "${HOME}/Library/Cookies")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.flickr.xpc")
 		)
 	)
 )
```
