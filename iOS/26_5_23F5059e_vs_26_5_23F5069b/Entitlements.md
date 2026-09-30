## 🔑 Entitlements

### ctkd

> `/System/Library/Frameworks/CryptoTokenKit.framework/ctkd`

```diff

 	<true/>
 	<key>com.apple.nfcd.session.reader.internal</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.audit.user</key>

```
### adattributiond

> `/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
+	<key>com.apple.private.networkserviceproxy</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>com.apple.WebKit.adattributiond</string>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<dict>
+		<key>0</key>
+		<string>com.apple.networkserviceproxy</string>
+	</dict>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### IMTranscoderAgent

> `/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent`

```diff

 		<string>com.apple.MobileSMSPreview</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
+		<string>com.apple.imessage.bag</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 		<string>AGXDeviceUserClient</string>
 		<string>AppleHPMARM</string>
 		<string>IOUSBDeviceInterfaceUserClient</string>
+		<string>IOAccessoryManagerUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### ProductKitService

> `/System/Library/PrivateFrameworks/ProductKitCore.framework/XPCServices/ProductKitService.xpc/ProductKitService`

```diff

 	<key>application-identifier</key>
 	<string>com.apple.ProductKitService</string>
 	<key>com.apple.developer.icloud-container-environment</key>
-	<string>Development</string>
+	<string>production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.productkit.b389personalization</string>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 		<string>com.apple.audio.piper</string>
 		<string>com.apple.coreaudio.device</string>
 		<string>com.apple.coreaudio</string>
+		<string>com.apple.coreaudio.private</string>
 		<string>com.apple.celestial</string>
 		<string>com.apple.coremedia.bag.airplay</string>
 		<string>com.apple.mediaexperience</string>

```
