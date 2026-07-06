## photoanalysisd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-					(require-any
-						(subpath "${HOME}/Media/PhotoData/CPLAssets")
-						(subpath "${HOME}/Media/PhotoData/Metadata")
-						(subpath "${HOME}/Media/PhotoData/Mutations")
-						(subpath "${HOME}/Media/PhotoData/Sync")
-						(subpath "${HOME}/Media/PhotoData/Thumbnails")
-					)
-					(subpath "${HOME}/Media/DCIM")
-				)
-			)
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")
-				(subpath "/private/var/tmp/com.apple.photoanalysisd")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")
+			(subpath "/private/var/tmp/com.apple.photoanalysisd")
 		)
 	)
 )

 		(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
 		(subpath "${HOME}/Library/Fonts")
 		(subpath "${HOME}/Media")
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(subpath "${HOME}/Media/PhotoData")
+		(subpath "${HOME}/Media/PhotoData/Caches/GraphService")
+		(subpath "${HOME}/Media/PhotoData/Caches/VisionService")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaanalysisd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")
 		(subpath "/private/var/containers/Data/System/com.apple.geod")

 		(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
 		(subpath "${HOME}/Library/Fonts")
 		(subpath "${HOME}/Media")
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(subpath "${HOME}/Media/PhotoData")
+		(subpath "${HOME}/Media/PhotoData/Caches/GraphService")
+		(subpath "${HOME}/Media/PhotoData/Caches/VisionService")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaanalysisd")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")
 		(subpath "/private/var/containers/Data/System/com.apple.geod")

 		(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
 		(subpath "${HOME}/Media/MediaAnalysis")
 		(subpath "${HOME}/Media/PhotoData")
-		(subpath "${HOME}/Media/PhotoData/Caches/ClientServerTransactions")
 		(subpath "${HOME}/Media/PhotoData/Caches/GraphService")
+		(subpath "${HOME}/Media/PhotoData/Caches/VisionService")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")
 		(subpath "/private/var/tmp/com.apple.photoanalysisd")
 	)

 		(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
 		(subpath "${HOME}/Media/MediaAnalysis")
 		(subpath "${HOME}/Media/PhotoData")
-		(subpath "${HOME}/Media/PhotoData/Caches/ClientServerTransactions")
 		(subpath "${HOME}/Media/PhotoData/Caches/GraphService")
+		(subpath "${HOME}/Media/PhotoData/Caches/VisionService")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")
 		(subpath "/private/var/tmp/com.apple.photoanalysisd")
 	)

 		(subpath "${HOME}/Library/Caches/com.apple.photoanalysisd")
 		(subpath "${HOME}/Media/MediaAnalysis")
 		(subpath "${HOME}/Media/PhotoData")
-		(subpath "${HOME}/Media/PhotoData/Caches/ClientServerTransactions")
 		(subpath "${HOME}/Media/PhotoData/Caches/GraphService")
+		(subpath "${HOME}/Media/PhotoData/Caches/VisionService")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.photoanalysisd")
 		(subpath "/private/var/tmp/com.apple.photoanalysisd")
 	)
```
