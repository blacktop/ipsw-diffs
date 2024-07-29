## 🔑 Entitlements

### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 		<string>com.apple.dprivacyd</string>
 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.CloudSubscriptionFeatures.datadetectors</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 	<true/>
 	<key>com.apple.Pasteboard.paste-unchecked</key>
 	<true/>
+	<key>com.apple.ProactiveSummarization.feedback</key>
+	<true/>
 	<key>com.apple.SystemConfiguration.SCPreferences-read-access</key>
 	<array>
 		<string>com.apple.radios.plist</string>

 		<string>com.apple.foundationmodels.languagemodelservice</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.nanoprefsync</string>
+		<string>com.apple.ProactiveSummarization.server</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-write</key>
 	<string>com.apple.NanoHomeScreen.RelevantWidgetDefaults</string>

```
