## 🔑 Entitlements

### CMFSyncAgent

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.cmfsyncagent</string>
-	<key>com.apple.Contacts.database-allow</key>
-	<true/>
 	<key>com.apple.StatusKit.publish.types</key>
 	<array>
 		<string>com.apple.focus.status</string>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/tmp/</string>
-		<string>/private/var/mobile/Library/AddressBook/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.StatusKit.publish</string>

 	<array>
 		<string>com.apple.cmfsyncagent</string>
 	</array>
-	<key>com.apple.security.ts.addressbook</key>
-	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 </dict>

```
