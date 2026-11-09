## 🔑 Entitlements

### filesystem

### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-keyboard</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>AppleIntelligenceReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.Buddy</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>ProactiveAppPrediction</key>
 		<dict>
 			<key>Streams</key>

```


