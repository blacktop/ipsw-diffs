## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Install</string>
+		<string>Queue</string>
 		<string>Library</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>

```
### Camera

> `/Applications/Camera.app/Camera`

```diff

 	<array>
 		<string>com.apple.phoenix</string>
 		<string>com.apple.WallpaperKit</string>
+		<string>com.apple.airplay</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### Diagnostic-4009-iOS-D83-D84

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009-iOS-D83-D84.appex/Diagnostic-4009-iOS-D83-D84`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### FTMInternal-4

> `/Applications/FTMInternal-4.app/FTMInternal-4`

```diff

 	<array>
 		<string>public-cellular-logging</string>
 	</array>
+	<key>com.apple.private.nsurlsession.impersonate</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.basebandd.xpc</string>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.phoneNumberResolver</string>

```
### MobileSafari

> `/Applications/MobileSafari.app/MobileSafari`

```diff

 	<string>com.apple.Safari.SyncedTabs</string>
 	<key>com.apple.developer.web-browser</key>
 	<true/>
-	<key>com.apple.developer.web-browser-engine.host</key>
-	<true/>
 	<key>com.apple.features.all-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.mobilesafari</string>
 		<string>com.apple.tipsd</string>
 	</array>
-	<key>com.apple.private.web-browser-engine.host</key>
-	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>
 	<true/>
+	<key>com.apple.developer.networking.multicast</key>
+	<true/>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>

 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 	</array>
+	<key>com.apple.security.network.server</key>
+	<true/>
 	<key>com.apple.sharesheet.allow-custom-view</key>
 	<true/>
 	<key>com.apple.siri.synapse</key>

```
### MomentsUIService

> `/Applications/MomentsUIService.app/MomentsUIService`

```diff

 		<string>MOFetchEventBundles</string>
 		<string>MOOnboardingAndSettings</string>
 		<string>MOUserNotifications</string>
+		<string>MOAppEntryEngagement</string>
 	</array>
 	<key>com.apple.photoanalysisd</key>
 	<true/>

```
### PASViewService

> `/Applications/PASViewService.app/PASViewService`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.screen-time.persistence</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.security.octagon</string>

 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.icloud.findmydevice.managed</string>
+		<string>systemgroup.com.apple.DeviceActivity</string>
 	</array>
 	<key>com.apple.sharing.Client</key>
 	<true/>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	<true/>
 	<key>com.apple.internal.seserviced.ptattestation</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
+	<key>com.apple.mkb.usersession.keybagopaquedata</key>
+	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
 	<key>com.apple.nfcd.session.ecommerce</key>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
 	<key>com.apple.seld.tsmmanager</key>
 	<true/>

```
### ScreenTimeWidgetExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>1931623171</string>
 	<key>application-identifier</key>
 	<string>com.apple.ScreenTimeWidgetApplication.ScreenTimeWidgetExtension</string>
 	<key>com.apple.chrono.open-urls-direct</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ManagedSettingsAgent</string>

 	<array>
 		<string>systemgroup.com.apple.DeviceActivity</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 </dict>
 </plist>
 

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.datamigrator.deferexit</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	</array>
 	<key>com.apple.private.lockdownmoded.read-write</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.mobilestoredemo.enabledemo</key>
 	<array>
 		<string>Enroll</string>

 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
 	<key>com.apple.private.webinspector.allow-remote-inspection</key>
 	<true/>
 	<key>com.apple.purplebuddy.budd.access</key>

 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/VoiceTrigger/</string>

 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 		<string>RootDomainUserClient</string>
+		<string>AppleParavirtDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.system-container</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
+		<string>systemgroup.com.apple.DeviceActivity</string>
 		<string>systemgroup.com.apple.sharedpclogging</string>
 		<string>systemgroup.com.apple.powerlog</string>
 	</array>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<array>
 		<string>com.apple.ams-identity-verification</string>
 	</array>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>
-	<string>com.apple.productkit.b389personalization</string>
+	<array>
+		<string>com.apple.productkit.b389personalization</string>
+		<string>com.apple.productkit.personalization</string>
+	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.ShortExpiration</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.UI</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>InstallForLaunchServices</string>

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>
 		<string>read</string>

 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.TelephonyUtilities</string>
+		<string>com.apple.sharingd</string>
+		<string>com.apple.DeviceActivity</string>
+	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.DeviceActivity</string>
 	</array>
 	<key>com.apple.sharing.Client</key>
 	<true/>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.mediaremote.remote-control-discovery</key>
+	<true/>
 	<key>com.apple.mobilemail.mailservices</key>
 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.accessibility.HearingMLHelperService-access</key>
 	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.accessibility.axassets</key>

 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
 		<string>hw.cpusubfamily</string>
+		<string>kern.exclaves_status</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### CacheDeleteAppContainerCaches

> `/System/Library/CoreServices/CacheDeleteAppContainerCaches`

```diff

 	</array>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileBackupTmp</key>
+	<true/>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

```

### 🆕 MobileDevices-0002

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`

- No entitlements *(yet)*
### osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>
+		<string>SerialNumber</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.osanalyticshelper</string>

```
### AppStoreEvalLighthouseWorker

> `/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.AppleMediaDiscoveryLighthousePlugin</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobileassetd</string>

```

### 🆕 DevicePropertiesExtension

> `/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.metrics.DevicePropertiesExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.metrics.DevicePropertiesExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
		<string>Siri.Metrics.OnDeviceDigestUsageMetrics</string>
		<string>Siri.Metrics.OnDeviceDigestExperimentMetrics</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.assistant.settings</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.assistant.settings</string>
	</array>
</dict>
</plist>

```
### ExperimentationExtension

> `/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension`

```diff

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.SiriExperimentMetricsWorker</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.feedbacklogger</string>

```
### com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

 	<array>
 		<string>com.apple.systemstatus.activityattribution</string>
 	</array>
+	<key>com.apple.security.fatal-exceptions</key>
+	<array>
+		<string>jit</string>
+	</array>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides.coordinator</key>

```
### MercuryPosterExtension

> `/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension`

```diff

 <dict>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.posterkit.enhanced-memory-limits</key>
+	<true/>
 	<key>com.apple.posterkit.provider</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/Library/Wallpaper/Mercury/</string>
+	</array>
 </dict>
 </plist>
 

```
### MetricsExtension

> `/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension`

```diff

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.SiriMetricsWorker</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.feedbacklogger</string>

```
### MusicEngagementExtension

> `/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension`

```diff

 	<string>com.apple.Music.MusicEngagementExtension</string>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
-	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceMediaLibrary</string>
-		<string>kTCCServiceCamera</string>
-		<string>kTCCServicePhotos</string>
-		<string>kTCCServicePhotosAdd</string>
-		<string>kTCCServiceFaceID</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>
 	<true/>
+	<key>com.apple.security.fatal-exceptions</key>
+	<array>
+		<string>jit</string>
+	</array>
 	<key>com.apple.symptom_analytics.configure</key>
 	<true/>
 </dict>

```

### 🆕 PridePosterExtension

> `/System/Library/ExtensionKit/Extensions/PridePosterExtension.appex/PridePosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
</dict>
</plist>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>
 	<true/>
+	<key>com.apple.security.fatal-exceptions</key>
+	<array>
+		<string>jit</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>
 	<true/>
+	<key>com.apple.security.fatal-exceptions</key>
+	<array>
+		<string>jit</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 </dict>

```
### com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

 				<string>Lighthouse.Ledger.TaskError</string>
 				<string>Lighthouse.Ledger.TaskTelemetry</string>
 				<string>Lighthouse.Ledger.DeviceTelemetry</string>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>
 		</dict>
 	</dict>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>com.apple.transparencyd.accounts-support</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.background</key>
 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 		<string>com.apple.private.rupert</string>
 		<string>com.apple.private.rupert.rsa</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>CallData</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>CommCenter.Call.EmergencyVoiceCall</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.darkwake-control</key>
 	<true/>
 	<key>com.apple.private.iokit.powersource-control</key>

 		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.SharedWebCredentials</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.lockdownmode.read</key>
 	<true/>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 		<string>/.b/7/mobile/Library/LiveFiles/</string>
 		<string>/.b/7/mobile/Library/Application Support/FileProvider/</string>
 		<string>/.b/7/mobile/Library/CloudStorage/</string>
+		<string>/.b/0/mobile/Library/Mobile Documents/</string>
+		<string>/.b/0/mobile/Library/LiveFiles/</string>
+		<string>/.b/0/mobile/Library/Application Support/FileProvider/</string>
+		<string>/.b/0/mobile/Library/CloudStorage/</string>
+		<string>/.b/1/mobile/Library/Mobile Documents/</string>
+		<string>/.b/1/mobile/Library/LiveFiles/</string>
+		<string>/.b/1/mobile/Library/Application Support/FileProvider/</string>
+		<string>/.b/1/mobile/Library/CloudStorage/</string>
 		<string>/.b/4/Library/Mobile Documents/</string>
 		<string>/.b/4/Library/LiveFiles/</string>
 		<string>/.b/4/Library/Application Support/FileProvider/</string>

 		<string>/.b/9/Library/LiveFiles/</string>
 		<string>/.b/9/Library/Application Support/FileProvider/</string>
 		<string>/.b/9/Library/CloudStorage/</string>
+		<string>/.b/0/Library/Mobile Documents/</string>
+		<string>/.b/0/Library/LiveFiles/</string>
+		<string>/.b/0/Library/Application Support/FileProvider/</string>
+		<string>/.b/0/Library/CloudStorage/</string>
+		<string>/.b/1/Library/Mobile Documents/</string>
+		<string>/.b/1/Library/LiveFiles/</string>
+		<string>/.b/1/Library/Application Support/FileProvider/</string>
+		<string>/.b/1/Library/CloudStorage/</string>
 		<string>/private/var/mobile/.DocumentRevisions-V100/</string>
 		<string>/var/mobile/.DocumentRevisions-V100/</string>
 	</array>

```

### 🆕 com.apple.HealthKit.HealthResearchLogsDiagnosticExtension

> `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension.appex/com.apple.HealthKit.HealthResearchLogsDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.logging.stream</key>
	<true/>
</dict>
</plist>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.backboardd.setAuthenticatedTouches</key>
 	<true/>
+	<key>com.apple.backgroundassets.appstore</key>
+	<true/>
 	<key>com.apple.dmd-access</key>
 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>

 		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.attributionkitd.xpc.token-handoff</string>
+		<string>com.apple.backgroundassets.system</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.symptom_analytics.query</key>

```
### TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

 	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.TrustedPeersHelper</string>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ProgressReporting</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.appleneuralengine</string>

```
### SKAskPermissionExtension

> `/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.StoreKit.SKAskPermissionExtension</string>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
 	<key>com.apple.storekit.client-override</key>

```

### 🆕 NTKPlumeriaFaceBundleCompanion

> `/System/Library/NanoTimeKit/FaceBundles/NTKPlumeriaFaceBundleCompanion.bundle/NTKPlumeriaFaceBundleCompanion`

- No entitlements *(yet)*
### axremoted

> `/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/Support/axremoted`

```diff

 <dict>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.accessibility.BannerServices</key>
+	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.accessibility.physicalinteraction.client</key>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<true/>
 	<key>com.apple.private.launchservices.canchangeupdateavailability</key>
 	<true/>
+	<key>com.apple.private.launchservices.changedefaulthandlers</key>
+	<array>
+		<string>http</string>
+		<string>https</string>
+	</array>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>InstallForLaunchServices</string>

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.AppStore</string>
+		<string>com.apple.Preferences</string>
 	</array>
 	<key>com.apple.remotenotification.preferences</key>
 	<true/>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstoreagent.xpc</string>
+		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.mobileactivationd</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 	</array>

```
### AMSEngagementViewExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementViewExtension.appex/AMSEngagementViewExtension`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Install</string>
+		<string>Queue</string>
 		<string>Library</string>
 	</array>
 	<key>com.apple.private.avfoundation.capture.allow</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.coreidvd.docUpload.xpc</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>HomeKitClientAccessoryControl</string>
 		<string>Notification</string>
 		<string>NowPlaying</string>
+		<string>Siri.Metrics.OnDeviceDigestSegmentsCohorts</string>
 		<string>Siri.SelfTriggerSuppression</string>
 		<string>SiriUI</string>
 	</array>

```
### bookdatastored

> `/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored`

```diff

 		<string>com.apple.kvsd</string>
 		<string>com.apple.medialibraryd.xpc</string>
 		<string>com.apple.nanoprefsync</string>
+		<string>com.apple.ProgressReporting</string>
 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.localizationswitcherd</string>
 		<string>com.apple.sessionservices</string>
+		<string>com.apple.coremedia.admin</string>
 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.coremedia.compressionsession</string>
 		<string>com.apple.coremedia.decompressionsession</string>

```
### cdpd

> `/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

```
### CDPFollowUpExtension

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.Contacts.database-allow</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.adid</key>
+	<true/>
+	<key>com.apple.appleaccount.custodian</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
+	<key>com.apple.coreduetd.allow</key>
+	<true/>
+	<key>com.apple.coreduetd.people</key>
+	<true/>
+	<key>com.apple.coretelephony.Identity.get</key>
+	<true/>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
+	<key>com.apple.imagent</key>
+	<true/>
+	<key>com.apple.imagent.chat</key>
+	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
+	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
+	<key>com.apple.private.hsa-authentication-processing</key>
+	<true/>
+	<key>com.apple.private.ids.idquery-cache</key>
+	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.accounts.representative</string>
+	</array>
+	<key>com.apple.private.ids.messaging.urgent-priority</key>
+	<array>
+		<string>com.apple.private.alloy.accounts.representative</string>
+	</array>
+	<key>com.apple.private.imcore.imagent</key>
+	<true/>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceCamera</string>
+		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/Keychains/Analytics/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/DeviceRegistry.state/ActiveDeviceMiniStore.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.adid</string>
+		<string>com.apple.pearld</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.hsa-authentication-server</string>
+		<string>com.apple.ak.inheritance.xpc</string>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.ak.custodian.xpc</string>
+		<string>com.apple.aa.inheritance.xpc</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.security.octagon</string>
+		<string>com.apple.aa.custodian.xpc</string>
+		<string>com.apple.suggestd.contact</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.corefollowup.agent</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>RootDomainUserClient</string>
+	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 </dict>
 </plist>
 

```
### contextstored

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored`

```diff

 	<array>
 		<string>com.apple.MobileAsset.Duet</string>
 	</array>
-	<key>com.apple.private.biome.puner</key>
+	<key>com.apple.private.biome.pruner</key>
 	<array>
 		<string>App.InFocus</string>
 		<string>App.Intent</string>

 		<string>Media.NowPlaying</string>
 		<string>Motion.Activity</string>
 		<string>Screen.Sharing</string>
+		<string>ScreenTime.AppUsage</string>
 		<string>UserFocus.InferredMode</string>
 	</array>
 	<key>com.apple.private.carkit</key>

```
### FollowUpSampleExtension

> `/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/PlugIns/FollowUpSampleExtension.appex/FollowUpSampleExtension`

```diff

 	<array>
 		<string>com.apple.corefollowup.agent</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
+	<key>com.apple.assistant.dictation</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.assistant.multiuser.service</key>

 	<true/>
 	<key>com.apple.private.corespeechd.activation</key>
 	<true/>
+	<key>com.apple.private.exclaves.conclave-host</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>

 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.isusingbuiltinmicforrecording.allow</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.microphoneattribution.allow</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.usesecuresession</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.homepodaccessorysettings.server</string>
 		<string>com.apple.audio.isolated.client.service</string>
+		<string>com.apple.assistant.dictation</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
+		<string>kern.stackshot_stats</string>
 		<string>net.routetable.0.0.3.0</string>
 		<string>kern.exclaves_status</string>
 		<string>kern.task_conclave</string>

```
### diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

 	<true/>
 	<key>com.apple.diskimages.creator-uc</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.vfs.role-account-openfrom</key>

```
### com.apple.DocumentManager.Service

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.storagekitd</string>
 		<string>com.apple.FileProvider.ArchiveService</string>
 		<string>com.apple.desktopservices.ArchiveService</string>
 		<string>com.apple.searchd</string>

```
### facetimemessagestored

> `/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored`

```diff

 	<string>serverPreferred</string>
 	<key>com.apple.CallHistory.sync.allow</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.facetimemessagestored</string>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.facetime</string>

```
### FinHealthXPCServices

> `/System/Library/PrivateFrameworks/FinHealth.framework/XPCServices/FinHealthXPCServices.xpc/FinHealthXPCServices`

```diff

 		<string>com.apple.photos.service</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.proactive.PersonalizationPortrait.Event</string>
+		<string>com.apple.calaccessd</string>
 		<string>com.apple.geod</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 		<string>com.apple.wpantund.xpc</string>
 		<string>com.apple.sleepd.sleepserver</string>
 		<string>com.apple.StatusKit.presence</string>
+		<string>com.apple.wifi.manager-access</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### IMAutomaticHistoryDeletionAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMAutomaticHistoryDeletionAgent.app/IMAutomaticHistoryDeletionAgent`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.MobileSMS</string>
+	</dict>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.service.client</key>
 	<true/>
 	<key>com.apple.messages.supportsattachments</key>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.service.client</key>
 	<true/>
 	<key>com.apple.messages.supportsattachments</key>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 		<string>com.apple.airplay.apsynccontroller.xpc</string>
 		<string>com.apple.airplay.receiver.mediaremote.services</string>
 		<string>com.apple.audio.AudioSession</string>
+		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.BluetoothServices</string>
 		<string>com.apple.callkit.callcontrollerhost</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.CoreDuet</string>
+		<string>com.apple.duetexpertd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.lockscreen.shared</string>
-		<string>com.apple.duetexpertd</string>
+		<string>com.apple.purplebuddy</string>
 		<string>com.apple.spotlightui</string>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.TelephonyUtilities.sharePlayAppPolicies</string>

```
### UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID`

```diff

 		<string>com.apple.UARPUpdaterServiceHID</string>
 		<string>com.apple.MobileAccessoryUpdater</string>
 		<string>com.apple.UARPHIDUpdater.database</string>
+		<string>com.apple.mobileaccessoryupdater</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### MobileBackupCacheDeleteService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>MobileBackup</string>
+	<key>com.apple.private.security.storage.MobileBackupTmp</key>
+	<true/>
 	<key>com.apple.private.vfs.open-by-id</key>
 	<true/>
 	<key>com.apple.private.vfs.snapshot</key>

```
### NewDeviceOutreachExtension

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension`

```diff

 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.surfboard.applicationservice</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.surfboard.application-service-client</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>505792035</string>
 	<key>keychain-access-groups</key>

```

### 🆕 ANFDecoder

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/XPCServices/ANFDecoder.xpc/ANFDecoder`

- No entitlements *(yet)*
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.domain-extension</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.parsecd</string>
+		<string>com.apple.news.ANFDecoder</string>
 		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.news.TodayFeedConfigDecoder</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 TodayFeedConfigDecoder

> `/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/TodayFeedConfigDecoder.xpc/TodayFeedConfigDecoder`

- No entitlements *(yet)*
### com.apple.PrintKit.PrinterTool

> `/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array>
+		<string>com.apple.PrintKit.PrinterTool</string>
+	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.PrintKit.PrinterTool</string>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.printing.bandservice</key>
 	<true/>
+	<key>com.apple.private.necp.match</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.dp.PrivateFederatedLearning.DPMLRuntimePlugin</string>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
-	<key>com.apple.intelligenceplatform.View</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>UserProofing</string>
 		<string>Photos.UserAnalytics</string>
 		<string>Moments.Stats.EventData</string>
+		<string>Moments.Events.Engagement</string>
 		<string>Keyboard.TokenFrequency</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Location.Semantic</string>

 		<string>Siri.AssistantSuggestionFeatures</string>
 		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
 		<string>IntelligencePlatform.EntityTagging.PersonInference</string>
+		<string>CommCenter.Call.EmergencyVoiceCall</string>
+		<string>Location.Emergency.SessionStart</string>
+		<string>Safari.MemoryFootprint</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
-	<key>com.apple.private.intelligenceplatform.views.read-only</key>
-	<array>
-		<string>visualIdentifier</string>
-	</array>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
-		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.dp.PrivateFederatedLearning.DPMLRuntimePlugin</string>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
-	<key>com.apple.intelligenceplatform.View</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>UserProofing</string>
 		<string>Photos.UserAnalytics</string>
 		<string>Moments.Stats.EventData</string>
+		<string>Moments.Events.Engagement</string>
 		<string>Keyboard.TokenFrequency</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Location.Semantic</string>

 		<string>Siri.AssistantSuggestionFeatures</string>
 		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
 		<string>IntelligencePlatform.EntityTagging.PersonInference</string>
+		<string>CommCenter.Call.EmergencyVoiceCall</string>
+		<string>Location.Emergency.SessionStart</string>
+		<string>Safari.MemoryFootprint</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
-	<key>com.apple.private.intelligenceplatform.views.read-only</key>
-	<array>
-		<string>visualIdentifier</string>
-	</array>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
-		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.dp.PrivateFederatedLearning.DPMLRuntimePlugin</string>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
-	<key>com.apple.intelligenceplatform.View</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>UserProofing</string>
 		<string>Photos.UserAnalytics</string>
 		<string>Moments.Stats.EventData</string>
+		<string>Moments.Events.Engagement</string>
 		<string>Keyboard.TokenFrequency</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Location.Semantic</string>

 		<string>Siri.AssistantSuggestionFeatures</string>
 		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
 		<string>IntelligencePlatform.EntityTagging.PersonInference</string>
+		<string>CommCenter.Call.EmergencyVoiceCall</string>
+		<string>Location.Emergency.SessionStart</string>
+		<string>Safari.MemoryFootprint</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
-	<key>com.apple.private.intelligenceplatform.views.read-only</key>
-	<array>
-		<string>visualIdentifier</string>
-	</array>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
-		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.set-declarations</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.eyerelief.distancesampling</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.chronoservices</string>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.FamilyControlsAgent</string>
 		<string>com.apple.FamilyControlsAgent.private</string>
 		<string>com.apple.people.agent</string>

```
### liveactivitiesd

> `/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd`

```diff

 	<string>com.apple.liveactivitiesd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.coreduetd.context</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.mobile.keybagd.lock_status</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 	<array>
 		<string>com.apple.private.alloy.sessionkit</string>
 	</array>
+	<key>com.apple.private.iokit.batterydataprecise</key>
+	<true/>
 	<key>com.apple.private.security.storage.sessionkitd</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 		<string>/Applications/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/sessionkitd/</string>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.coreduetd.context</string>
+		<string>com.apple.iokit.powerdxpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
+	<key>com.apple.icloud.fmfd.access</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.Maps.xpc.SharedTrip</string>
 		<string>com.apple.siriknowledged</string>
+		<string>com.apple.icloud.fmfd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.apfs.spec_telemetry</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>TEST_ENTITLEMENT</string>

```
### com.apple.SpeechRecognitionCore.brokerd

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd`

```diff

 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
-	<key>com.apple.private.contacts</key>
-	<true/>
-	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceMicrophone</string>
-		<string>kTCCServiceAddressBook</string>
-	</array>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>372</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>
+	<key>com.apple.private.ids.report-spam-message</key>
+	<true/>
 	<key>com.apple.private.ids.self-session</key>
 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>

```
### UnityPosterExtension

> `/System/Library/PrivateFrameworks/UnityPoster.framework/PlugIns/UnityPosterExtension.appex/UnityPosterExtension`

```diff

 <dict>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.posterkit.enhanced-memory-limits</key>
+	<true/>
 	<key>com.apple.posterkit.provider</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/preferences/com.apple.networkd.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.apsd</string>
 		<string>com.apple.conference</string>
 		<string>com.apple.CloudKit</string>
 		<string>com.apple.DeviceActivity</string>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.Photos.MultiLibrary</string>
 		<string>com.apple.WebBookmarks.webbookmarksd</string>
+		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.amsaccountsd.multiuser</string>
 		<string>com.apple.announced.server</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MapKit.SnapshotService</string>
+		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.announced.server</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### CatalystContentExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/CatalystContentExtension.appex/CatalystContentExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### SystemActionConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### TelemetryDiskChecker

> `/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/TelemetryDiskChecker.xpc/TelemetryDiskChecker`

```diff

 	</dict>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.CloudDocsDB</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.CloudDocs</string>
+		<string>group.com.apple.iCloudDrive</string>
+	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.phoneNumberResolver</string>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.btFinding.access</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.localFindableConnectionMaterialMonitor</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.pairingmanager</key>

 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
+	<key>com.apple.private.nearbyinteraction.device-presence</key>
+	<true/>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
 	<true/>
 	<key>com.apple.private.notificationcenter-system</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.searchparty.btfindingsession</string>
+		<string>com.apple.accessories.connection-info-server</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>

 		<string>com.apple.nearbyd.xpc.BTRanging</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.icloud.searchpartyd.accessorydiscoverysession</string>
+		<string>com.apple.icloud.searchpartyd.localFindableConnectionMaterialSession</string>
 		<string>com.apple.icloud.searchpartyd.unknowndiscoverysession</string>
 		<string>com.apple.icloud.findmydeviced.app-support</string>
 		<string>com.apple.ak.auth.xpc</string>

 		<string>com.apple.findmy.fmfcore.notbackedup</string>
 		<string>com.apple.findmy</string>
 		<string>com.apple.findmy.findmylocated</string>
+		<string>com.apple.sharingd</string>
 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 		<string>com.apple.SharePlay.GroupSessionService</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
+		<string>com.apple.surfboard.immersionservice</string>
+		<string>com.apple.surfboard.environmentservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.systemNotesScreenshot</key>
 	<true/>
+	<key>com.apple.surfboard.environment-client</key>
+	<true/>
+	<key>com.apple.surfboard.immersion-client</key>
+	<true/>
+	<key>com.apple.surfboard.scene-state-assertion</key>
+	<true/>
 	<key>com.apple.synapse.allowAddLinkContextRequests</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

```
### MobileStore

> `/private/var/staged_system_apps/MobileStore.app/MobileStore`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>Library</string>
+	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 		<string>com.apple.passd.library</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.appstored.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	<array/>
 	<key>com.apple.developer.carplay-audio</key>
 	<true/>
+	<key>com.apple.developer.game-center</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.ap.adservicesd.server</string>
 		<string>com.apple.nanonews.service.companion</string>
+		<string>com.apple.news.ANFDecoder</string>
 		<string>com.apple.coreduetd</string>
 		<string>com.apple.ap.adprivacyd.opt-out</string>
 		<string>com.apple.coreduetd.knowledge</string>
+		<string>com.apple.news.TodayFeedConfigDecoder</string>
 		<string>com.apple.newsd.analytics</string>
 		<string>com.apple.newsd.download</string>
+		<string>com.apple.newsd.today-feed</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.routined.internal</string>
 		<string>com.apple.SafariLaunchAgent</string>

```
### NewsToday2

> `/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2`

```diff

 		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
 		<string>com.apple.newsd.analytics</string>
 		<string>com.apple.newsd.download</string>
+		<string>com.apple.newsd.today-feed</string>
 		<string>com.apple.parsecd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.social.facebook.like</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Preferences/com.apple.restrictionspassword.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### AutomationNotificationContent

> `/private/var/staged_system_apps/Shortcuts.app/PlugIns/AutomationNotificationContent.appex/AutomationNotificationContent`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### ShortcutsActionExtension

> `/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsActionExtension.appex/ShortcutsActionExtension`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### ShortcutsWidgetExtension

> `/private/var/staged_system_apps/Shortcuts.app/PlugIns/ShortcutsWidgetExtension.appex/ShortcutsWidgetExtension`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 		<string>group.com.apple.tipsnext</string>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<array>
 		<string>com.apple.powerlog.proactivenotifications</string>
 	</array>
+	<key>com.apple.private.xpc.allowed-get-service-name</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.service-stats</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```
### IOMFB_bics_daemon

> `/usr/libexec/IOMFB_bics_daemon`

```diff

 <dict>
 	<key>com.apple.AppleNVMeEAN.allow</key>
 	<true/>
+	<key>com.apple.QuartzCore.display-state</key>
+	<true/>
 	<key>com.apple.afk.user</key>
 	<true/>
 	<key>com.apple.private.applesepmanager.allow</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceExposureNotification</string>
 	</array>
+	<key>com.apple.private.xpc.allowed-get-service-name</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.service-stats</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<array>
 		<string>com.apple.powerlog.proactivenotifications</string>
 	</array>
+	<key>com.apple.private.xpc.allowed-get-service-name</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.service-stats</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>ContextSync.LOI</string>
-		<string>SemanticLocation</string>
+		<string>Location.Semantic</string>
 		<string>Device.Power.BatteryLevel</string>
 		<string>Device.Power.PluggedIn</string>
 		<string>Device.Networking.EdgeSelection</string>

```
### anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

 			<key>read</key>
 			<dict/>
 		</dict>
+		<key>MagFp</key>
+		<dict>
+			<key>read</key>
+			<dict/>
+		</dict>
 		<key>PressureFp</key>
 		<dict>
 			<key>read</key>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<string>com.apple.appleaccountd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.Contacts.database-allow</key>
+	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.imagent</key>
+	<true/>
+	<key>com.apple.imagent.chat</key>
+	<true/>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<array>
 		<string>com.apple.private.alloy.accounts.representative</string>
 	</array>
+	<key>com.apple.private.imcore.imagent</key>
+	<true/>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>
 	<key>com.apple.private.notificationcenter-system</key>

```
### asktod

> `/usr/libexec/asktod`

```diff

 	<array>
 		<string>ScreenTimeRequest</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.askto</string>

 		<string>com.apple.ScreenTimeAgent.ask</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.iconservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.ScreenTimeAgent.ask</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.iconservices</string>
 	</array>
 	<key>com.apple.security.ts.identity-services-client</key>
 	<true/>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allows-set-output-device</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.mediaremote.restrict-command-clients</key>
 	<true/>
+	<key>com.apple.private.automatic-assessment-configuration.restrictor</key>
+	<true/>
 	<key>com.apple.private.neagent</key>
 	<true/>
 	<key>com.apple.private.necp.policies</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.assessment-mode-restriction</string>
 		<string>com.apple.pasteboard.pasted</string>
 		<string>com.apple.coremedia.routingcontext.xpc</string>
 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.nehelper</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mediaremoted.xpc</string>
+		<string>com.apple.frontboard.systemappservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.assessmentmode</string>
+		<string>com.apple.springboard</string>
 	</array>
+	<key>com.apple.springboard.application-restriction-monitoring</key>
+	<true/>
+	<key>com.apple.springboard.externaldisplay.displayArrangements</key>
+	<true/>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.diagnosticpipeline.request</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.launchservices.MoveDocumentOnOpen</key>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 		<string>/Library/Audio/Tunings/</string>
 		<string>/private/var/preferences/SystemConfiguration/com.apple.radios.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/dev/exfiltration-audio_capture</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>Library/AirPlayRoutePrediction/correlations.archive</string>

```
### configd

> `/usr/libexec/configd`

```diff

 	<true/>
 	<key>com.apple.private.network.management.data</key>
 	<true/>
+	<key>com.apple.private.route.iflist.include-clat46</key>
+	<true/>
 	<key>com.apple.private.snhelper</key>
 	<true/>
 	<key>com.apple.private.usbdevice.setdescription</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>com.apple.gridDataServices.config</string>
 		<string>com.apple.duetactivityscheduler.trial</string>
 		<string>com.apple.duetactivityscheduler.policydatacollection</string>
+		<string>com.apple.dasd.barMetricRecorder</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### dietapplecamerad

> `/usr/libexec/dietapplecamerad`

```diff

 	<true/>
 	<key>com.apple.pearl.iokit-user-access</key>
 	<true/>
-	<key>com.apple.private.tcc.manager</key>
-	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### eligibilityd

> `/usr/libexec/eligibilityd`

```diff

 	<false/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
-		<string>com.apple.MobileAsset.os_eligibility_parameters</string>
+		<string>com.apple.MobileAsset.OSEligibility.Parameters</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

```
### findmybeaconingd

> `/usr/libexec/findmybeaconingd`

```diff

 	<array>
 		<string>/private/var/db/com.apple.findmy.findmybeaconingd/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/com.apple.findmy.findmybeaconingd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.nfcd.hwmanager</string>

```
### init_exclavekit

> `/usr/libexec/init_exclavekit`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.exclaves.conclave-boot</key>
+	<true/>
+</dict>
+</plist>
 

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
-	<key>com.apple.momentsd.internal</key>
-	<array>
-		<string>MOOnboardingAndSettings</string>
-	</array>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.geoanalyticsd</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.spaceattributiond</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.sos.trigger</key>
 	<true/>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.springboard.launchapplications</key>

```
### mlhostd

> `/usr/libexec/mlhostd`

```diff

 	<array>
 		<string>group.com.apple.mlhost</string>
 	</array>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.mlhost</string>

```
### online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

 	<array>
 		<string>com.apple.MobileAsset.MobileIdentityService.DenyList</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 	</array>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

```
### remindd

> `/usr/libexec/remindd`

```diff

 	<array>
 		<string>/usr/libexec</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array/>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
+	<key>com.apple.locationd.adpd_gathering</key>
+	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 		<string>Device.Wireless.WiFiAvailabilityStatus</string>
 		<string>Motion.Activity</string>
 	</array>
+	<key>com.apple.private.bmk.allow</key>
+	<true/>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>
 	<key>com.apple.private.calendar.watchos-mutable-database</key>

 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.safetyalerts</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 	</array>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.safetyalerts</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.usernotifications.listener</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.pairedInfoSecurity</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>

 		<string>UserAssignedDeviceName</string>
 		<string>SerialNumber</string>
 	</array>
+	<key>com.apple.private.accessories.showallconnections</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
+		<key>com.apple.findmy.localfindable</key>
+		<string>com.apple.findmy.localfindable</string>
 		<key>com.apple.icloud.searchparty</key>
 		<string>com.apple.icloud.searchparty</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
 	<key>com.apple.private.communicationsfilter</key>

 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.cmfsyncagent.embedded.auth</string>
+		<string>com.apple.accessories.connection-info-server</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>
 	<true/>
-	<key>com.apple.private.tcc.manager.access.read</key>
-	<array>
-		<string>kTCCServiceAll</string>
-	</array>
-	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
-	<array>
-		<string>kTCCServiceSecureElementAccess</string>
-	</array>
+	<key>com.apple.private.tcc.manager</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.secureelementservice.aapp</string>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.CacheDelete</key>
+	<array>
+		<string>CLIENT_ENTITLEMENT</string>
+		<string>PURGEABLE_ENTITLEMENT</string>
+		<string>SERVICE_ENTITLEMENT</string>
+		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
+		<string>PURGE_ENTITLEMENT</string>
+	</array>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.cache_delete.public</string>
+		<string>com.apple.cache_delete</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### soundanalysisd

> `/usr/libexec/soundanalysisd`

```diff

 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.enrollmentmode.allow</key>
+	<true/>
+	<key>com.apple.private.mediaexperience.usesecuresession</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.tcc.allow</key>

```
### storagekitd

> `/usr/libexec/storagekitd`

```diff

 		<string>com.apple.DiskArbitration.diskarbitrationd</string>
 		<string>com.apple.storagekitfsrunner</string>
 		<string>com.apple.cache_delete</string>
+		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.filesystems.livefileproviderd</string>
 		<string>com.apple.filesystems.fskitd</string>
 	</array>

```
### thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

 	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
+	<key>com.apple.private.clpc.policy</key>
+	<true/>
 	<key>com.apple.private.clpc.seeding</key>
 	<true/>
 	<key>com.apple.private.getprivatesysid</key>

```
### usermanagerd

> `/usr/libexec/usermanagerd`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
+	<key>com.apple.private.kernel.panic</key>
+	<true/>
 	<key>com.apple.private.migrate-musr-system-keychain</key>
 	<true/>
 	<key>com.apple.private.mis.profiles.write</key>

```
### videosubscriptionsd

> `/usr/libexec/videosubscriptionsd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>production</string>
+	<key>com.apple.VideoSubscriberAccount.AnalyticsService.ReportAMSMetricsEvents</key>
+	<true/>
 	<key>com.apple.VideoSubscriberAccount.DeveloperService</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.VideoSubscriberAccount.AnalyticsService</string>
 		<string>com.apple.watchlistd.xpc</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.cloudd</string>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.purplebuddy</string>
+		<string>com.apple.TVWatchList</string>
 		<string>com.apple.VideoSubscriberAccount</string>
+		<string>com.apple.videos-preferences</string>
 	</array>
 	<key>com.apple.security.temporary-exception.*</key>
 	<array>

```
### wcd

> `/usr/libexec/wcd`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appconduitd.application-manager</string>
+		<string>com.apple.ProgressReporting</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

```
### xpcproxy

> `/usr/libexec/xpcproxy`

```diff

 <dict>
 	<key>com.apple.private.coreservices.canmanagebackgroundtasks</key>
 	<true/>
+	<key>com.apple.private.exclaves.conclave-spawn</key>
+	<true/>
 	<key>com.apple.private.security.storage.driverkitd</key>
 	<true/>
 	<key>com.apple.private.spawn-driver</key>

```
