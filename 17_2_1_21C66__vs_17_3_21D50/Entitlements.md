## 🔑 Entitlements

### AuthKitUIService

> `/Applications/AuthKitUIService.app/AuthKitUIService`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

```
### Camera

> `/Applications/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
-	<key>com.apple.authkit.client.private</key>
-	<true/>
 	<key>com.apple.avfoundation.allow-capture-filter-rendering</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>

```

### 🆕 Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.avfaudio.devicetest</key>
	<true/>
	<key>com.apple.avfaudio.devicetest.service</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.private.applesmc.user-access</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleSMCClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.avfaudio.devicetest.service</string>
		<string>com.apple.audioanalyticsd</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleSMCClient</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.DiagnosticsKit</string>
	</array>
</dict>
</plist>

```
### GameCenterWidgets

> `/Applications/GameCenterWidgets.app/GameCenterWidgets`

```diff

 	<array>
 		<string>com.apple.AppStoreComponents</string>
 	</array>
+	<key>com.apple.security.lockdownmode.read</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```
### GCWidgets

> `/Applications/GameCenterWidgets.app/PlugIns/GCWidgets.appex/GCWidgets`

```diff

 	<array>
 		<string>com.apple.AppStoreComponents</string>
 	</array>
+	<key>com.apple.security.lockdownmode.read</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.osanalytics.SubmitLogs.allow</key>
 	<true/>
 	<key>com.apple.private.persona.read</key>

 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceBluetoothAlways</string>
+		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.webinspector.allow-remote-inspection</key>
 	<true/>

```
### SafariBookmarksSyncAgent

> `/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent`

```diff

 	</array>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.spotlight.IndexAgent</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mobilesafarishared</string>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<array>
 		<string>com.apple.intelligenceplatform.View</string>
 	</array>
+	<key>com.apple.spotlight.entitledattributes</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>333</string>

```
### ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

 <dict>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>OOPCocoa</string>
+	<key>com.apple.private.memory.ownership_transfer</key>
+	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

 		<string>com.apple.locationd.synchronous</string>
 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<array>
 		<string>com.apple.coreauthd</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.coreauthd</string>
+	</array>
 	<key>com.apple.security.ts.read-any-bundle</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>

```
### appconduitd

> `/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd`

```diff

 	<array>
 		<string>systemgroup.com.apple.installcoordinationd</string>
 	</array>
+	<key>com.apple.springboard.application-removability.proxy</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<array>
 		<string>bridge:</string>
 	</array>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>appconduitd</string>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.ShortExpiration</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage.BiometricLivenessFlag</key>

 	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceFaceID</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.Preferences</string>

```
### AKFollowUpExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceFaceID</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.payment.configuration</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
 	<key>com.apple.private.Safari.History</key>

 		<string>UpdateSystemAppState</string>
 		<string>SetSystemAppMigrationComplete</string>
 	</array>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.photos.service.migration</key>
 	<true/>
 	<key>com.apple.private.safari.cloudtabs</key>

```
### com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.NeighborhoodActivityConduitService</string>
+		<string>com.apple.TelephonyUtilities</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 		<string>Safari.PageLoad</string>
-		<string>Siri.Health.federated</string>
+		<string>Siri.Health.Federated</string>
 		<string>AppleID.ChildSetup</string>
 		<string>SystemSettings.AppearanceSetup</string>
 		<string>SystemSettings.ChildMultitaskingSetup</string>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 		<string>Safari.PageLoad</string>
-		<string>Siri.Health.federated</string>
+		<string>Siri.Health.Federated</string>
 		<string>AppleID.ChildSetup</string>
 		<string>SystemSettings.AppearanceSetup</string>
 		<string>SystemSettings.ChildMultitaskingSetup</string>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 		<string>Safari.PageLoad</string>
-		<string>Siri.Health.federated</string>
+		<string>Siri.Health.Federated</string>
 		<string>AppleID.ChildSetup</string>
 		<string>SystemSettings.AppearanceSetup</string>
 		<string>SystemSettings.ChildMultitaskingSetup</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.private.ids.firewall</key>
 	<true/>
+	<key>com.apple.private.ids.force-query-send-option-allowed</key>
+	<array>
+		<string>com.apple.private.alloy.facetime.multi</string>
+	</array>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>

```

### 🆕 RhizomePoster

> `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/RhizomePoster.appex/RhizomePoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.WatchFacesWallpaperSupport.RhizomePoster</string>
	</array>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```
### FocusConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension`

```diff

 		<string>/Applications/</string>
 		<string>/private/var/containers/Bundle/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.linkd.extension</string>

```
### WidgetConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension`

```diff

 	<array>
 		<string>group.com.apple.weather</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.linkd.extension</string>

```

### 🆕 BooksSpotlightExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/BooksSpotlightExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.spotlight.IndexAgent</string>
		<string>com.apple.spotlight.SearchAgent</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
</dict>
</plist>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceCalendar</string>
+		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	<true/>
 	<key>com.apple.nearbyinteraction.finding.session</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>ArrowChipID</string>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	</array>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

 	<true/>
 	<key>com.apple.private.suggestions.reminders</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceFaceID</string>
+	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### MailNotificationContentExtension

> `/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension`

```diff

 	<array>
 		<string>group.com.apple.mail</string>
 	</array>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceFaceID</string>
+	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### NewsDiagnosticExtension

> `/private/var/staged_system_apps/News.app/PlugIns/NewsDiagnosticExtension.appex/NewsDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.news</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 </dict>

```
### hidutil

> `/usr/bin/hidutil`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.hid.client.alpha-numeric-remapping</key>
+	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>
 	<true/>
 </dict>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>258</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.springboard</string>

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

 		<string>com.apple.private.corewifi.internal-xpc</string>
 		<string>com.apple.symptoms.symptomsd.managed_events</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>kCFPreferencesAnyApplication</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOUserUserClient</string>

 		<string>IOUserUserClient</string>
 		<string>IO80211APIUserClient</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>kCFPreferencesAnyApplication</string>
+	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.wifi.manager-access</key>

```
