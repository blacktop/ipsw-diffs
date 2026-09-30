## Security.plist

> `Domain/Security.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>EarlyAnchorExpiration</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>EnableSecureObjectSync</key>
 	<dict>
 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>KCSharingCKSyncEngineTransition</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
+	<key>KCSharingCloudCoreAdoption</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>RootConstraints</key>
 	<dict>
 		<key>DevelopmentPhase</key>
 		<string>FeatureComplete</string>
 	</dict>
+	<key>SEPBasedICSCHealingEnabled</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>TTROnCRKRemoval</key>
 	<dict>
 		<key>Enabled</key>

```
