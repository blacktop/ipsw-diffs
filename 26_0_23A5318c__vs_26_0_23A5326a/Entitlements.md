## 🔑 Entitlements

### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x</string>
 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPad</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
-		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction.iPhone</string>
-		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction.iPad</string>
+		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.ExposureNotification</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sessionkit.listener</key>
 	<true/>
 	<key>com.apple.private.skywalk.register-user-pipe</key>

 		<string>/usr/sbin/BTLEServer/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/log/CoreCapture/com.apple.KalBluetooth_driver/FwLogs/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
