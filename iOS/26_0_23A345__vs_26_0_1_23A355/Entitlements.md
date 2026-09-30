## 🔑 Entitlements

### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 		<string>com.apple.reminders</string>
 		<string>com.apple.mobileslideshow</string>
 	</array>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.mobilenotes</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```
### com.apple.mobilenotes.QuickLookExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.QuickLookExtension.appex/com.apple.mobilenotes.QuickLookExtension`

```diff

 	<string>com.apple.mobilenotes.QuickLookExtension</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

 	<array>
 		<string>com.apple.mobilenotes</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>508119322</string>
 	<key>platform-application</key>

```
