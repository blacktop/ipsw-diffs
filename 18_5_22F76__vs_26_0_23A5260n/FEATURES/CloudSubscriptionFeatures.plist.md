## CloudSubscriptionFeatures.plist

> `Domain/CloudSubscriptionFeatures.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>disableStaleFeatureFallback</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>imageGenerationBypass</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```
