## 🔑 Entitlements

### filesystem

### AccessorySetupUI

> `/Applications/AccessorySetupUI.app/AccessorySetupUI`

```diff

 	<true/>
 	<key>com.apple.DeviceAccess.private</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
 	<key>com.apple.bluetooth.settings</key>

 		<string>com.apple.private.corewifi.wifi-network-sharing-ui-xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ProductKitService</string>
+		<string>com.apple.SharingServices</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.accessorysetupkit</string>
 	</array>
+	<key>com.apple.sharing.Client</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### SCARemoteView Appex

> `/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/SCARemoteView Appex`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.family.ageRange</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.ManagedSettingsAgent</string>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.ManagedSettingsAgent</string>

```

### 🆕 NearFieldPrivateServiceLocation

> `/System/Library/LocationBundles/NearFieldPrivateServiceLocation.bundle/NearFieldPrivateServiceLocation`

- No entitlements *(yet)*

### 🆕 TVNotificationSettings

> `/System/Library/PreferenceBundles/TVNotificationSettings.bundle/TVNotificationSettings`

- No entitlements *(yet)*

### 🆕 appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/appleaccounttransparencyd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.cdp.telemetry</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.appleaccounttransparencyd</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.transparencyd.aet</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.appleaccounttransparency</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppleMediaServices</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

```
### deleted_helper

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper`

```diff

 	<true/>
 	<key>com.apple.private.osanalytics.SubmitLogs.allow</key>
 	<true/>
+	<key>com.apple.private.security.datavault.controller</key>
+	<true/>
 	<key>com.apple.private.vfs.entitled-reserve-access</key>
 	<true/>
 </dict>

```
### remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Alarm</string>
+		<string>App.InFocus</string>
 		<string>App.Intent</string>
 		<string>App.Intents.Transcript</string>
 		<string>CarPlay</string>
+		<string>ContextSync.Health.Workout</string>
 		<string>ContextSync.WalletTransaction</string>
 		<string>Device.Power.BatteryLevel</string>
 		<string>Device.Power.LowPowerMode</string>

 		<string>Device.Wireless.Bluetooth</string>
 		<string>Device.Wireless.NFCTag</string>
 		<string>Device.Wireless.WiFi</string>
+		<string>Health.Workout</string>
 		<string>MediaSuggester.SuggestionFeedback</string>
 		<string>SleepMode</string>
 		<string>SoundDetection</string>

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>App.InFocus</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Clock.Alarm</key>
 				<dict>
 					<key>mode</key>

```
### NotesAppMigrationExtension

> `/private/var/staged_system_apps/MobileNotes.app/Extensions/NotesAppMigrationExtension.appex/NotesAppMigrationExtension`

```diff

 	<string>notes</string>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.notes.import</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Shortcuts/</string>
+	</array>
+	<key>com.apple.shortcuts.stepwise-execution</key>
+	<true/>
+	<key>com.apple.shortcuts.variable-injection</key>
+	<true/>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 </dict>
 </plist>
 

```
### Tips

> `/private/var/staged_system_apps/Tips.app/Tips`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.tips</string>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceFaceID</string>

```


### SystemOS

### com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>

```
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.sqlite.defensive</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```


