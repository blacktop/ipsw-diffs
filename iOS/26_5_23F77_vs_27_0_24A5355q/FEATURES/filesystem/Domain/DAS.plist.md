## DAS.plist

> `Domain/DAS.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>Enabled</key>
-	<false/>
+	<key>AllowRunsDuringDeviceActivityOnCharger</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>EnhancedDYLDClosureBuild</key>
 	<dict>
 		<key>Enabled</key>

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>use_ml_freezer_recommender</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 </dict>
 </plist>
 

```
