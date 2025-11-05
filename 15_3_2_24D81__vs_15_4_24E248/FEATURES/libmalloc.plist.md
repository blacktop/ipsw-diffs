## libmalloc.plist

> `Domain/libmalloc.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>SecureAllocator_ThreadCaching</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>ZeroOnFree</key>
 	<dict>
 		<key>Enabled</key>

```
