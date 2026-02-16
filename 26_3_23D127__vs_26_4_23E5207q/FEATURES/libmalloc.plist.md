## libmalloc.plist

> `Domain/libmalloc.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>SecureAllocator_Nano</key>
-	<dict>
-		<key>DevelopmentPhase</key>
-		<string>FeatureComplete</string>
-	</dict>
-	<key>SecureAllocator_SystemWide</key>
+	<key>SecureAllocator_GuardObjects</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>

```
