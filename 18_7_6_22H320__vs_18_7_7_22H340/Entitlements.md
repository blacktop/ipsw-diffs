## 🔑 Entitlements

### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.Preferences.ResetPrivacyWarningsNotification</key>
+	<true/>
 	<key>com.apple.private.dmd.emergency-mode</key>
 	<true/>
 	<key>com.apple.private.dmd.policy</key>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudDocuments</string>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.FindMyDevice.FindMyServiceValidation.access</key>
+	<true/>
 	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>
 	<array>
 		<string>com.apple.radios.plist</string>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.findmydeviced.aoverc</string>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.audioaccessoryd.MuteState</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

```
### mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.network.tcp.info</key>
+	<true/>
 	<key>com.apple.private.network.ultraconstrained</key>
 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>

```
