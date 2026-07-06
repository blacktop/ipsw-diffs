## afcd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/Caches/com.apple.afc")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.afc")
+		(require-not (extension-class "com.apple.mediaserverd.read-write"))
+		(require-any
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(subpath "${HOME}/Library/Caches/com.apple.afc")
+			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read")
+				(subpath "${HOME}/Library/Caches/com.apple.afc")
+			)
+			(require-all
+				(extension-class "com.apple.app-sandbox.read-write")
+				(subpath "${HOME}/Library/Caches/com.apple.afc")
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(subpath "${HOME}/Library/Caches/com.apple.afc")
+			)
+		)
 	)
 )
 (allow file-issue-extension

 		(require-any
 			(extension-class "com.apple.mediaserverd.read")
 			(extension-class "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.app-sandbox.read-write")
+				(subpath "${HOME}/Library/Caches/com.apple.afc")
+			)
 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/Caches/com.apple.afc")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.afc")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(subpath "${HOME}/Library/Caches/com.apple.afc")
-	)
-)
 
 (allow file-link)
 

 
 (allow file-ungraft)
 
-(allow file-write*
-	(with report)
-	(require-all
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(extension "com.apple.afc.root")
-	)
-)
 (allow file-write*
 	(with report)
 	(require-all

 		(extension "com.apple.afc.root")
 	)
 )
+(allow file-write*
+	(with report)
+	(require-all
+		(subpath "${HOME}/Media/MediaAnalysis")
+		(extension "com.apple.afc.root")
+	)
+)
 (allow file-write*
 	(require-any
 		(subpath "${HOME}/Media/Photos/Sync")

 	)
 )
 
-(allow file-write-create
-	(with report)
-	(require-all
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(extension "com.apple.afc.root")
-	)
-)
 (allow file-write-create
 	(with report)
 	(require-all

 		(extension "com.apple.afc.root")
 	)
 )
+(allow file-write-create
+	(with report)
+	(require-all
+		(subpath "${HOME}/Media/MediaAnalysis")
+		(extension "com.apple.afc.root")
+	)
+)
 (allow file-write-create
 	(require-any
 		(subpath "${HOME}/Media/Photos/Sync")

 
 (deny file-write-setugid)
 
-(allow file-write-unlink
-	(with report)
-	(require-all
-		(subpath "${HOME}/Media/MediaAnalysis")
-		(extension "com.apple.afc.root")
-	)
-)
 (allow file-write-unlink
 	(with report)
 	(require-all

 		(extension "com.apple.afc.root")
 	)
 )
+(allow file-write-unlink
+	(with report)
+	(require-all
+		(subpath "${HOME}/Media/MediaAnalysis")
+		(extension "com.apple.afc.root")
+	)
+)
 (allow file-write-unlink
 	(require-all
 		(extension "com.apple.sandbox.oopjit")
```
