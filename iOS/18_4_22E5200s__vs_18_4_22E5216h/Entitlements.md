## 🔑 Entitlements

### AirPlayReceiver

> `/Applications/AirPlayReceiver.app/AirPlayReceiver`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>com.apple.CompanionLink</key>
 	<true/>
 	<key>com.apple.PairingManager.HomeKit</key>

 	<array>
 		<string>com.apple.private.wifi.driverkit</string>
 	</array>
+	<key>com.apple.private.mediaexperience.systemcontroller.allowappstoinitiateplayback</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.rapport.Client</key>

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.devicesharingd</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 AccountAuthenticationModificationExtensionHelper

> `/Applications/AuthenticationServicesUI.app/PlugIns/AccountAuthenticationModificationExtensionHelper.appex/AccountAuthenticationModificationExtensionHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.authentication-services.coordinate-account-authentication-modification</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.octagon</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.security.octagon</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.cfnetwork</string>
		<string>com.apple.password-manager</string>
	</array>
</dict>
</plist>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 <dict>
 	<key>CanInheritApplicationStateFromOtherProcesses</key>
 	<true/>
+	<key>adi-client</key>
+	<string>3303100823</string>
 	<key>application-identifier</key>
 	<string>com.apple.HeadphoneProxService</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.AudioAccessoryServices</key>
 	<true/>
 	<key>com.apple.BluetoothServices</key>

 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
+	<key>com.apple.payment.card-on-file</key>
+	<true/>
 	<key>com.apple.powerui.smartcharging</key>
 	<true/>
 	<key>com.apple.powerui.smartcharging.AudioAccessory</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceIDData</string>

 	<array>
 		<string>Install</string>
 	</array>
+	<key>com.apple.private.aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>

 		<key>value</key>
 		<string>/Applications/HeadphoneProxService.app</string>
 	</dict>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.productkit.personalization</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.fpsd.client</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>InstallForLaunchServices</string>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMicrophone</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.passd.payment</string>
 		<string>com.apple.HearingModeService</string>
 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.accessories.connection-info-server</string>

 	<key>com.apple.wirelessproxd-disable-scans</key>
 	<true/>
 	<key>fairplay-client</key>
-	<integer>1445028844</integer>
+	<string>1445028844</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### NewDeviceSetupUIService

> `/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService`

```diff

 	<string>com.apple.NewDeviceSetupUIService</string>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.bluetooth.discovery</key>
 	<dict>
 		<key>MacSetup</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.ak.anisette.xpc</string>
+		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.appleidsetupd.setup.xpc</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.distributed_notifications@Uv3</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
+	</array>
 	<key>com.apple.sharing.Client</key>
 	<true/>
 	<key>com.apple.sharing.Session</key>

```

### 🆕 OTEAutomation

> `/Applications/OTEAutomationTest.app/Frameworks/OTEAutomation.framework/OTEAutomation`

- No entitlements *(yet)*

### 🆕 OTEAutomationTest

> `/Applications/OTEAutomationTest.app/OTEAutomationTest`

- No entitlements *(yet)*
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
+	<key>com.apple.private.biometrickit.allow-connect</key>
+	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.background-event-consumption</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<array>
 		<string>com.apple.TextInput</string>
 		<string>com.apple.notes</string>
+		<string>com.apple.productkit.b389personalization</string>
+		<string>com.apple.productkit.personalization</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>

 	<true/>
 	<key>com.apple.private.cloudkit.protectiondata</key>
 	<true/>
+	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
+	<dict>
+		<key>com.apple.productkit.personalization</key>
+		<string>com.apple.productkit.personalization</string>
+	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 		<string>com.apple.usernotificationskit</string>
 		<string>com.apple.messages.critical-messaging.storage</string>
 		<string>com.apple.seserviced.contactlessCredential.settings</string>
+		<string>com.apple.visionproapp.notifications</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<true/>
 	<key>com.apple.usermanagerd.persona.setbundle</key>
 	<true/>
+	<key>com.apple.visioncompaniond.client</key>
+	<true/>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
 	<key>com.apple.voicebanking.services</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.developer.WebKit.ServiceWorkers</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>
 	<true/>
 	<key>com.apple.developer.web-browser</key>

 		<string>com.apple.WebUI</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.account.dca.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>
+	<key>com.apple.private.canGetAppLinkInfo</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

```
### SubcredentialUIService

> `/Applications/SubcredentialUIService.app/SubcredentialUIService`

```diff

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.private.barcodesupport.allowNotifications</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>VisualIntelligenceCamera.DetectedLabels</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.canIgnoreAppLinkEnabledProperty</key>

 	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
-	<key>com.apple.sage.summarization</key>
-	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.WritingToolsUIService</string>
+	<key>com.apple.devicesharing.guest-user-mode-client</key>
+	<true/>
 	<key>com.apple.feedbackd.remote-evaluation</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.sage.summarization</string>
 		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```

### 🆕 MobileDevices-0004

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0004.bundle/MobileDevices-0004`

- No entitlements *(yet)*
### ShortcutsTopHitsExtension

> `/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/ActionKit.framework</string>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/CallHistoryDB/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CallHistorySyncHelper</string>
+		<string>com.apple.contactsd</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.siriactionsd.xpc</string>
 	</array>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.SpringBoard.ReadyForRestore</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.purplebuddy.launchMigrationSourceUI</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.donotdisturb.0191488e-ff8a-728d-a9f7-08a0a77abd7d.update.client-identifiers</key>

```
### powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

 	<array>
 		<string>com.apple.powerui.bdcdata</string>
 		<string>com.apple.powerexperienced.resourceusage</string>
+		<string>com.apple.datamigrator</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 ASRFullPayloadCorrection

> `/System/Library/ExtensionKit/Extensions/ASRFullPayloadCorrection.appex/ASRFullPayloadCorrection`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.lighthouse.ASRFullPayloadCorrection</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>ASRFullPayloadCorrection</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Dictation.UserEdit</key>
				<true/>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
	</array>
	<key>com.apple.siri.analytics.assistant</key>
	<true/>
</dict>
</plist>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### DevicePropertiesExtension

> `/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ExperimentationExtension

> `/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
+		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>
 		<string>Device.Wireless.BluetoothGATTSession</string>
 		<string>Media.StreamingStats</string>
 		<string>App.InFocus</string>

 		<string>Autonaming.Messages.AccuracyFedStats</string>
 		<string>Safari.WebsitesBlockingQuit</string>
 		<string>LocalAuthentication.UI.Dialogs</string>
+		<string>VisualIntelligenceCamera.DetectedLabels</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### FindMyIntentsExtension

> `/System/Library/ExtensionKit/Extensions/FindMyIntentsExtension.appex/FindMyIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.intentsession</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>

 		<string>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</string>
 		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 </dict>
 </plist>
 

```
### HomeAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/HomeAppIntentsExtension.appex/HomeAppIntentsExtension`

```diff

 	<array>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.matter.native.xpc</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.matter.native.xpc</string>

```
### LighthouseASRReplay

> `/System/Library/ExtensionKit/Extensions/LighthouseASRReplay.appex/LighthouseASRReplay`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.siri.LighthouseASRReplay</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ASRReplay</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Siri.ASR.ContextualReplayRecord</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/tmp/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.access.user</string>
+	</array>
 </dict>
 </plist>
 

```
### MetricsExtension

> `/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 ODDIPoirotMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/ODDIPoirotMetricsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
		<string>com.apple.poirot.poirot_tool</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```
### QuickLookUIExtension

> `/System/Library/ExtensionKit/Extensions/QuickLookUIExtension.appex/QuickLookUIExtension`

```diff

 	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>

```
### SearchToolDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolDiagnosticExtension.appex/SearchToolDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.omniSearch.SearchToolDiagnosticExtension</string>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>SearchToolExtension</key>

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.spotlight.search.internal</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### SiriTurnRestatementExtension

> `/System/Library/ExtensionKit/Extensions/SiriTurnRestatementExtension.appex/SiriTurnRestatementExtension`

```diff

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SpeakerIdSamplingExtension

> `/System/Library/ExtensionKit/Extensions/SpeakerIdSamplingExtension.appex/SpeakerIdSamplingExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.ssr.rpisamplingservice</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```

### 🆕 TetsuoDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/TetsuoDiagnosticExtension.appex/TetsuoDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.visionproapp.diagnosticextension</string>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.tdg-wb</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.tdg-wb</key>
		<string>com.apple.tdg-wb</string>
	</dict>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.lsd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.visioncompaniond</string>
	</array>
</dict>
</plist>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>org.WebKit.memoryWarning</string>
 		<string>org.WebKit.memoryWarning.begin</string>
 		<string>org.WebKit.memoryWarning.end</string>
+		<string>org.WebKit.testNotification</string>
 	</array>
 	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
 	<true/>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>org.WebKit.memoryWarning</string>
 		<string>org.WebKit.memoryWarning.begin</string>
 		<string>org.WebKit.memoryWarning.end</string>
+		<string>org.WebKit.testNotification</string>
 	</array>
 	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
 	<true/>

```
### AudioConverterService

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterService.xpc/AudioConverterService`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
 	<true/>
 	<key>com.apple.private.memory.ownership_transfer</key>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
-	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<key>com.apple.developer.hardened-process</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
 	<array>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<array>
 		<string>kTCCServiceFinancialData</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceFinancialData</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceFinancialData</string>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.update-app-attributes</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.get</key>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/MobileIdentityData/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.lsd.installation</string>
 		<string>com.apple.lsd.modifydb</string>
 		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.misagent</string>
 		<string>com.apple.mobile.installd</string>
 		<string>com.apple.pearld</string>
 		<string>com.apple.remotemanagementd.store</string>

```
### ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension`

```diff

 	<array>
 		<string>App.WebUsage</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

```
### com.apple.SensorKit.CHSupportService

> `/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKit.CHSupportService.xpc/com.apple.SensorKit.CHSupportService`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.CognitiveHealth</string>
+	</array>
+</dict>
+</plist>
 

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 	<array>
 		<string>kTCCServiceSpeechRecognition</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.sage.textcomposition</key>

```
### storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>adi-client</key>
 	<string>409835401</string>
 	<key>application-identifier</key>

```

### 🆕 TetsuoNotifications

> `/System/Library/PreferenceBundles/TetsuoNotifications.bundle/TetsuoNotifications`

- No entitlements *(yet)*

### 🆕 VisionCompanionSettings

> `/System/Library/PreferenceBundles/VisionCompanionSettings.bundle/VisionCompanionSettings`

- No entitlements *(yet)*
### motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

```diff

 	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
+	<key>com.apple.private.avfoundation.capture.camera-stolen-interruptor.allow</key>
+	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
 	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<array>
 		<string>com.apple.AppStore</string>
 		<string>com.apple.Preferences</string>
+		<string>com.apple.TVAppStore</string>
 	</array>
 	<key>com.apple.remotenotification.preferences</key>
 	<true/>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.siri.findmy</string>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.siri.userfeedbacklearning</string>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.siri.findmy</string>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.siri.userfeedbacklearning</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 				</dict>
 			</array>
 		</dict>
+		<key>LNActivityProvider</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>App.Intents.Transcript</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>

```
### com.apple.CloudDocs.MobileDocumentsFileProviderUI

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderUI.appex/com.apple.CloudDocs.MobileDocumentsFileProviderUI`

```diff

 	<array>
 		<string>CloudDocuments</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.fileproviderui.display-inline</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 		<string>Siri.SelfTriggerSuppression</string>
 		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
 		<string>Siri.ASR.RequestMetricsRecord</string>
+		<string>Siri.ASR.ContextualReplayRecord</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.siri.recorded-audio</string>
+	</array>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
 	<key>com.apple.private.siri.activation</key>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.triald</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.sage.summarization</key>
 	<true/>
 	<key>com.apple.sage.textcomposition</key>

```
### devicecheckd

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd`

```diff

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
+	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```

### 🆕 TUDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/TUDiagnosticExtension.appex/TUDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
</dict>
</plist>

```
### diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

 	<key>com.apple.diskimages.creator-uc</key>
 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>1</integer>
+	<integer>2</integer>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.vfs.role-account-openfrom</key>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled`

```diff

 	<true/>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	</dict>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.managed-settings.apply</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screentime-setup</key>

 		<string>com.apple.ScreenTimeAgent.private</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.identityservicesd.pds</string>
+		<string>com.apple.ManagedSettingsAgent</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>com.apple.appstored.xpc.request</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.containermanagerd</string>
+		<string>com.apple.controlcenter.remoteservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

 	<array>
 		<string>App.InFocus</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 		<string>VasUgeSzVyHdB27g2XpN0g</string>
 		<string>iyfxmLogGVIaH7aEgqwcIA</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<array>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>HomeKit</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app</string>
 	</dict>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
 	<key>com.apple.private.cloudkit.buddyAccess</key>
 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

 	<true/>
 	<key>com.apple.private.imcore.imtransferservice</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DuetActivitySchedulerPairedSystemContext</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>

 		<string>com.apple.StatusKit.publish</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.biomesyncd.sync</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### IntelligenceFlowDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics`

```diff

 	<array>
 		<string>Sage.Transcript</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
+		<string>IntelligenceEngine.Interaction.Donation</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>

 			<array>
 				<string>Sage.Transcript</string>
 				<string>IntelligenceFlow.Transcript.Datastream</string>
+				<string>IntelligenceEngine.Interaction.Donation</string>
 			</array>
 		</dict>
 	</dict>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 		<string>1170</string>
 		<string>1180</string>
 		<string>1760</string>
-		<string>1761</string>
+		<string>INTELLIGENCE_FLOW_QUERY_DECORATOR</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### com.apple.MLKit.MLModelPreview

> `/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

```
### com.apple.MLKit.MLPackagePreview

> `/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	</dict>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>
+		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
 		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 	</array>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	</dict>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>
+		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
 		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 	</array>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.application-identifier</key>
+	<string>AAPLPHOTOS.com.apple.mstreamd</string>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.migrationd</string>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
 	<key>com.apple.appprotectiond.read</key>

 	<array>
 		<string>group.com.apple.FileProvider.LocalStorage</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/CallHistoryDB/</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleJPEGDriverUserClient</string>

```
### accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### medialibraryd

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.medialibraryd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<array>
 		<string>Wallet.Transaction</string>
 	</array>
-	<key>com.apple.private.bmk.allow</key>
+	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.biometricUnlockSuppression</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### schooltimed

> `/System/Library/PrivateFrameworks/SchoolTime.framework/Support/schooltimed`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### budd

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/budd`

```diff

 	<true/>
 	<key>com.apple.account.dca.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.purplebuddy.launchMigrationSourceUI</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.setInput</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<array>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	</array>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siriinference-dodml-plugin</key>
 	<true/>
+	<key>com.apple.private.SiriSuggestionsBookkeepingService.xpc</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.symptom_diagnostics</string>
-		<string>com.apple.coremedia.samplebufferaudiorenderer.xpc</string>
-		<string>com.apple.coremedia.samplebufferrendersynchronizer.xpc</string>
+		<string>com.apple.appleneuralengine</string>
+		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.audio.AudioQueueServer</string>
 		<string>com.apple.audio.AudioSession</string>
+		<string>com.apple.audioanalyticsd</string>
+		<string>com.apple.coremedia.samplebufferaudiorenderer.xpc</string>
+		<string>com.apple.coremedia.samplebufferrendersynchronizer.xpc</string>
+		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>
-		<string>com.apple.audio.AudioComponentRegistrar</string>
+		<string>com.apple.homed.xpc</string>
+		<string>com.apple.homehubd.manage</string>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
-		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.siri.uaf.service</string>
-		<string>com.apple.appleneuralengine</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.coremedia.systemcontroller.xpc</string>
-		<string>com.apple.homehubd.manage</string>
-		<string>com.apple.homed.xpc</string>
-		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.sirittsd</string>
+		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.triald.namespace-management</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### StatusKitAgent

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent`

```diff

 	</dict>
 	<key>com.apple.private.cloudkit.spi</key>
 	<true/>
+	<key>com.apple.private.ids.firewall</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.status.keysharing</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.audio.hapticd</string>
+		<string>com.apple.accessories.externalaccessory-server</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### TranslationUIService

> `/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService`

```diff

 	<string>com.apple.TranslationUIServices.TranslationUIService</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
-	<key>com.apple.developer.default-translation-app</key>
-	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	</array>
 	<key>com.apple.private.translation</key>
 	<true/>
+	<key>com.apple.private.translation.uiprovider.host</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.replicator.replication</string>
 		<string>com.apple.replicatorservices</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### WiFiLogConfigDiagnosticExtension_iOS

> `/System/Library/PrivateFrameworks/WiFiLogCapture.framework/PlugIns/WiFiLogConfigDiagnosticExtension_iOS.appex/WiFiLogConfigDiagnosticExtension_iOS`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.private.wifivelocity</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/Logs/</string>
+		<string>/Library/Logs/</string>
+		<string>/Library/Preferences/</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/Managed Preferences/mobile/</string>
+		<string>/private/var/run/com.apple.wifivelocity/</string>
+		<string>/private/var/log/com.apple.wifivelocity/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Preferences/</string>
 	</array>
-	<key>seatbelt-profiles</key>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>MegaWiFiDE</string>
+		<string>com.apple.wifivelocityd</string>
 	</array>
 </dict>
 </plist>

```
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>adi-client</key>
 	<string>409835401</string>
 	<key>application-identifier</key>

```

### 🆕 AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.BluetoothServices.cloud</key>
	<true/>
	<key>com.apple.BluetoothServices</key>
	<true/>
	<key>adi-client</key>
	<string>143531244</string>
	<key>application-identifier</key>
	<string>com.apple.visionproapp</string>
	<key>aps-environment</key>
	<string>development</string>
	<key>com.apple.authkit.client</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.spatialshowcase.userdata</string>
		<string>com.apple.tdg-wb</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstorecomponents.media-client-id</key>
	<string>com.apple.visionproapp</string>
	<key>com.apple.private.appstorecomponents.media-client-version</key>
	<string>1</string>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.spatialshowcase.userdata</key>
		<string>com.apple.spatialshowcase.userdata</string>
		<key>com.apple.tdg-wb</key>
		<string>com.apple.tdg-wb</string>
	</dict>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.fairplay.FPDI</key>
	<dict>
		<key>capabilities</key>
		<array>
			<integer>4014732562</integer>
		</array>
		<key>client-identifier</key>
		<string>amstool</string>
	</dict>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.metadata.private</key>
	<true/>
	<key>com.apple.private.healthkit.read_authorization_bypass</key>
	<array>
		<string>HKVisionPrescriptionTypeIdentifier</string>
	</array>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.storekit</key>
	<array>
		<string>RemoteDownloadIdentifiers</string>
		<string>Articles</string>
	</array>
	<key>com.apple.private.tvAppExtension</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.countryd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.BluetoothCloudServices</string>
		<string>com.apple.visioncompaniond</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.visioncompaniond</string>
		<string>com.apple.visionproapp.notifications</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.visioncompaniond.client</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>com.apple.itunesstored.private</key>
	<true/>
</dict>
</plist>

```
### BooksThumbnail

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksThumbnail.appex/BooksThumbnail`

```diff

 	<string>com.apple.iBooks.BooksThumbnail</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.iBooks.BooksThumbnail</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### FindMyNotificationsService

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>

```
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.handwritingd.allowBackgroundRecognition</key>
+	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
 	<key>com.apple.private.CloudSharing.SPI</key>

```
### GenerativePlaygroundMessagesAppExtension

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceCamera</string>
 	</array>
 	<key>com.apple.private.tcc.allow-prompting</key>
 	<array>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.textcomposition</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 		<string>com.apple.proactive.PersonalizationPortrait.Contact</string>
 		<string>com.apple.icloudmailagent.secret.xpc</string>
 		<string>com.apple.backboard.hid.services</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

 	<array>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.parsecd</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MailNotificationContentExtension

> `/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension`

```diff

 	<string>com.apple.mobilemail.MailNotificationContentExtension</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.businessservicesd.businessmetadata</key>
+	<true/>
+	<key>com.apple.icloudmailagent.secret.xpc</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>

 	<array>
 		<string>group.com.apple.mail</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Caches/com.apple.businessservicesd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.email.maild</string>
+		<string>com.apple.icloudmailagent.secret.xpc</string>
+		<string>com.apple.businessservicesd</string>
 	</array>
 </dict>
 </plist>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 		<string>com.apple.reminders</string>
 		<string>com.apple.mobileslideshow</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<string>Notes</string>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mobilenotes</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### com.apple.mobilenotes.QuickLookExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.QuickLookExtension.appex/com.apple.mobilenotes.QuickLookExtension`

```diff

 	<string>com.apple.mobilenotes.QuickLookExtension</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>CommunicationSafetyResultWithoutImage</string>
 		<string>Discoverability.Signals</string>
 		<string>Discoverability.Usage</string>
+		<string>Messages.Search.Event</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_SafariBrowsingAssistant/purpose_auto/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>

 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.newscore</string>
 		<string>com.apple.suggestions</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.Passwords</string>
 	</array>
 	<key>com.apple.security.system-groups</key>

```
### MusicMessagesApp

> `/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.news.ScoringService</string>
 		<string>com.apple.MobileTimer.timerserver</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<array>
 		<string>Wallet.Transaction</string>
 	</array>
-	<key>com.apple.private.bmk.allow</key>
+	<key>com.apple.private.biometrickit.allow-connect</key>
+	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
 	<key>com.apple.private.carkit.headUnitPairingPrompt</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.allowallcallurls</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.internal.resource</key>
 	<true/>
+	<key>com.apple.private.photos.service.librarymanagement</key>
+	<true/>
 	<key>com.apple.private.photos.service.multilibrary</key>
 	<true/>
 	<key>com.apple.private.photos.service.notification</key>

```
### PodcastsWidget

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.podcasts</string>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>243LU875E5.groups.com.apple.podcasts</string>

```
### QuickLookExtension

> `/private/var/staged_system_apps/Shortcuts.app/PlugIns/QuickLookExtension.appex/QuickLookExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.shortcuts.QuickLookExtension</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<array>
 		<string>com.apple.sharing.appleidauthentication</string>
 	</array>
-	<key>om.apple.developer.hardened-process</key>
-	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### ThumbnailExtension

> `/private/var/staged_system_apps/Shortcuts.app/PlugIns/ThumbnailExtension.appex/ThumbnailExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.shortcuts.ThumbnailExtension</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### VoiceMemosIntentsExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension`

```diff

 		<string>/private/var/mobile/Media/Recordings/</string>
 		<string>/private/var/mobile/Library/Recordings/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/AppAnalytics/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

```
### VoiceMemosShareExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension`

```diff

 		<string>/private/var/mobile/Media/Recordings/</string>
 		<string>/private/var/mobile/Library/Recordings/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/AppAnalytics/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

```
### VoiceMemos

> `/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos`

```diff

 		<string>/private/var/mobile/Media/Recordings/</string>
 		<string>/private/var/mobile/Library/Recordings/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/AppAnalytics/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>
-	<key>com.apple.private.security.storage.IntelligencePlatform</key>
-	<true/>
 	<key>com.apple.private.security.storage.appleaccountd</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.assessmentagent/</string>

 		<string>com.apple.assessmentmode</string>
 		<string>com.apple.springboard</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.configurationprofiles</string>
+	</array>
 	<key>com.apple.springboard.application-restriction-monitoring</key>
 	<true/>
 	<key>com.apple.springboard.externaldisplay.displayArrangements</key>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 	<string>com.apple.coreduetd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>PeopleSuggesterContactPriors</key>
+		<key>ShareSheetFeedback</key>
 		<dict>
-			<key>Sets</key>
-			<dict>
-				<key>Contacts.Contact</key>
-				<dict>
-					<key>mode</key>
-					<string>read-only</string>
-				</dict>
-				<key>PeopleSuggester.ContactPrior</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
+			<key>Streams</key>
+			<array>
+				<string>ShareSheet.Feedback</string>
+			</array>
 		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>AppResumeBiomeUseCase</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Device.Power.PluggedIn</string>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
 		<key>DuetActivitySchedulerAppPredictions</key>
 		<dict>
 			<key>Streams</key>

```
### diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

 	<false/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<string>AppleAPFSUserClient</string>
 </dict>
 </plist>
 

```
### dmd

> `/usr/libexec/dmd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
 	<string>com.apple.dmd</string>
 	<key>com.apple.private.lockdown.finegrained-get</key>

```
### feedbackd

> `/usr/libexec/feedbackd`

```diff

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.surfboard.application-service-client</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.findmy.findmylocated</string>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.timed</key>
 	<true/>
 	<key>platform-application</key>

```
### icloudmailagent

> `/usr/libexec/icloudmailagent`

```diff

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.mail</string>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleMobileApNonceUserClient</string>

```
### keychainsharingmessagingd

> `/usr/libexec/keychainsharingmessagingd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.kcsharing.invite</string>

```
### locationd

> `/usr/libexec/locationd`

```diff

 		<string>road-tiles</string>
 		<string>building-tiles</string>
 	</array>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 		<string>com.apple.nearbyd.xpc.nearbyinteraction.observer</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.countryd.update</string>
+		<string>com.apple.eligibilityd</string>
 		<string>com.apple.CarPlayApp.user-alerts-service</string>
 		<string>com.apple.rapport.people</string>
 		<string>com.apple.locationpushd.pushregistration</string>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>

```
### mediaparserd

> `/usr/libexec/mediaparserd`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-vorbis-decode</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 	<true/>
 	<key>com.apple.coremedia.nerotransportconnectionxpc.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.idle-timer-services</key>

```
### merchantd

> `/usr/libexec/merchantd`

```diff

 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>
 	<true/>
+	<key>com.apple.nfcd.hwmanager</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

```
### mlhostd

> `/usr/libexec/mlhostd`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.mlhost</string>

 	<true/>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<array>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 		<string>/private/var/run/MobileAssetCritialDomainsUpdated.plist</string>
+		<string>/private/var/run/MobileAssetSuspendSystemOptionalForSoftwareUpdate.nonce</string>
 		<string>/private/var/code_coverage/</string>
 		<string>/private/var/run/com.apple.mobileassetd-AutoAsset-DeviceBoot-UUID</string>
 	</array>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.coreduetd.context</key>
+	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.feedbackd.client-forms</key>
 	<array>
 		<string>:framework-journalingsuggestions-onboarding</string>

 	<array>
 		<string>group.com.apple.Journal</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>NowPlaying</string>
+		<string>App.MediaUsage</string>
+		<string>App.WebUsage</string>
+		<string>Device.Display.Backlight</string>
+		<string>Media.NowPlaying</string>
+		<string>Notification.Usage</string>
+		<string>ScreenTime.AppUsage</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.momentsd.MOUserNotifications</string>

 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.MomentsIntelligenceService</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>
 	<key>com.apple.security.ts.springboard-services</key>

```
### pcapd

> `/usr/libexec/pcapd`

```diff

-<?xml version="1.0" encoding="UTF-8"?>
-<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
-<plist version="1.0">
-<dict>
-	<key>com.apple.security.ts.bpf</key>
-	<true/>
-</dict>
-</plist>
 

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.ids.registration</key>

```
### relatived

> `/usr/libexec/relatived`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-protected</key>
+	<true/>
 	<key>com.apple.hid.system.fast-path-motion-event-privileged</key>
 	<true/>
 	<key>com.apple.hid.system.user-access-fast-path</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.fmd.local</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.fmd.local</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>

 	<true/>
 	<key>com.apple.private.ids.session</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.orchestration.capabilities</string>
 		<string>com.apple.SystemConfiguration.configd</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.locationd.registration</string>

 	</array>
 	<key>com.apple.siri.embeddedspeech</key>
 	<true/>
+	<key>com.apple.siri.orchestration.capabilities</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### videocodecd

> `/usr/libexec/videocodecd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.private.FairPlayIOKitUserClient.access</key>

```

### 🆕 visioncompaniond

> `/usr/libexec/visioncompaniond`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.visioncompaniond</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.appstored.install-apps</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.tdg-wb</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.private.InstallCoordination.uninstall</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>DeviceName</string>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.tdg-wb</key>
		<string>com.apple.tdg-wb</string>
	</dict>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_SoftwareUpdateDocumentation/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstored.xpc.request</string>
		<string>com.apple.apsd</string>
		<string>com.apple.installcoordinationd</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.softwareupdateservicesd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.softwareupdateservicesd</string>
		<string>com.apple.visioncompaniond</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.visioncompaniond</string>
	<key>com.apple.softwareupdateservices</key>
	<true/>
	<key>com.apple.softwareupdateservices.client.allowed</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### BTLEServer

> `/usr/sbin/BTLEServer`

```diff

 		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
 		<string>HKQuantityTypeIdentifierHeight</string>
 	</array>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.CallHistory</key>

```

### 🆕 skywalkctl

> `/usr/sbin/skywalkctl`

- No entitlements *(yet)*
