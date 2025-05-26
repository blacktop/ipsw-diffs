## FileProvider.plist

> `Domain/FileProvider.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>D2DMigration</key>
+	<key>DirectoryEviction</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>DirectoryEviction</key>
+	<key>EvictUsingPurgeSingleFile</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>EvictUsingPurgeSingleFile</key>
+	<key>FPCKService</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
+	<key>Helena</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>

```
