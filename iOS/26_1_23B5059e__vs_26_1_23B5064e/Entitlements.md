## 🔑 Entitlements

### AppDistributionLaunchAngel

> `/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.ScreenTimeAgent.ask</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```

### 🆕 AskPermissionUI

> `/Applications/AskPermissionUI.app/AskPermissionUI`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.AskPermissionUI</string>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.AskPermissionUI</string>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.xpc.amsengagementd</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOMobileFramebufferUserClient</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### ContinuitySingShieldUI

> `/Applications/ContinuitySingShieldUI.app/ContinuitySingShieldUI`

```diff

 	<true/>
 	<key>com.apple.springboard.lockDevice</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
 	<key>com.apple.systemstatus.publisher.domains</key>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 	<array>
 		<string>/Library/Caches/com.apple.homedevicesetup/</string>
 		<string>/Library/Logs/CrashReporter/</string>
+		<string>/Library/Logs/MediaServices/HTTPArchives/</string>
 		<string>/Library/Preferences/com.apple.coreaudio.plist</string>
 		<string>/Library/Preferences/com.apple.Sharing.plist</string>
+		<string>/Library/UserConfigurationProfiles/PayloadDependency.plist</string>
 		<string>/Library/VoiceTrigger/</string>
-		<string>/Library/Logs/MediaServices/HTTPArchives/</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.sharingd.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.aa.daemon.xpc</string>
-		<string>com.apple.sharingd</string>
-		<string>com.apple.nfcd.hwmanager</string>
-		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.aa.custodian.xpc</string>
-		<string>com.apple.amsaccountsd.multiuser</string>
-		<string>com.apple.AppleMediaServicesUIDynamicService</string>
+		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.ak.puffin.xpc</string>
+		<string>com.apple.amsaccountsd.multiuser</string>
 		<string>com.apple.analyticsd</string>
-		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.AppleMediaServicesUIDynamicService</string>
 		<string>com.apple.appstored.xpc.request</string>
+		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.awdd</string>
 		<string>com.apple.backlightd</string>

 		<string>com.apple.coreservices.appleid.authentication</string>
 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.extensionkitservice</string>
-		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
-		<string>com.apple.icloud.searchpartyd.pairingmanager</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.pairingmanager</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
-		<string>com.apple.iphone.axserver</string>
 		<string>com.apple.internal.studylogd</string>
+		<string>com.apple.iphone.axserver</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.lsd.installation</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.passd.account</string>
-		<string>com.apple.powerui.audioAccessorySmartChargeManager</string>
 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.passd.library</string>
+		<string>com.apple.powerui.audioAccessorySmartChargeManager</string>
 		<string>com.apple.powerui.smartChargeManager</string>
-		<string>com.apple.private.corewifi.mobilewifi-xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>
-		<string>com.apple.purplebuddy.budd.proximity.source.xpc</string>
+		<string>com.apple.private.corewifi.mobilewifi-xpc</string>
 		<string>com.apple.purplebuddy.budd.migration.source.xpc</string>
+		<string>com.apple.purplebuddy.budd.proximity.source.xpc</string>
 		<string>com.apple.ScreenTimeAgent.persistence</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.sharingd.b332setup</string>
+		<string>com.apple.sharingd</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.soundboardservices.server</string>
 		<string>com.apple.symptom_analytics</string>

 	<true/>
 	<key>com.apple.stereoleader.soundboard</key>
 	<true/>
+	<key>com.apple.symptom_analytics.query</key>
+	<true/>
+	<key>com.apple.symptoms.NetworkOfInterest</key>
+	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.facetimemessagestored.service</string>
-		<string>com.apple.biome.access.user</string>
-		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callhistorymanager</string>
 		<string>com.apple.callintelligenced.service</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.publisher.service.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<array>
 		<string>/System/Library/PrivateFrameworks/Settings.framework</string>
 	</array>
+	<key>com.apple.private.appintents.exception.background-task-allowed</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### Sidecar

> `/Applications/Sidecar.app/Sidecar`

```diff

 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
+	<key>com.apple.springboard.lockDevice</key>
+	<true/>
 	<key>com.apple.springboard.secureAppAssertion</key>
 	<true/>
 </dict>

```
### TVRemoteUIService

> `/Applications/TVRemoteUIService.app/TVRemoteUIService`

```diff

 	<array>
 		<string>Discoverability.Signals</string>
 	</array>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
 	<key>com.apple.private.nearbyinteraction.device-presence</key>

 	<true/>
 	<key>com.apple.springboard.requestAppSwitcherAppearanceForHiddenApp</key>
 	<true/>
+	<key>com.apple.symptom_analytics.query</key>
+	<true/>
+	<key>com.apple.symptoms.NetworkOfInterest</key>
+	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.watchlist.private</key>

```

### 🆕 MobileDevices-0005

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0005.bundle/MobileDevices-0005`

- No entitlements *(yet)*
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>AdvancedPurchase</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

```
### scrod

> `/System/Library/CoreServices/VoiceOverTouch.app/scrod`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.coreaudio.CanTapTelephony</key>
+	<true/>
 	<key>com.apple.coreaudio.app-tap</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.audio.AudioQueueServer</string>
 		<string>com.apple.AccessibilityUIServer</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
+		<string>com.apple.commcenter.coretelephony.xpc</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.TelephonyUtilities</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>IOMobileFramebufferUserClient</string>
 		<string>AppleJPEGDriverUserClient</string>
 	</array>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-calls</string>
+		<string>modify-calls</string>
+	</array>
 	<key>com.apple.voicebanking.services</key>
 	<true/>
 </dict>

```

### 🆕 ADAskForExceptionExtension

> `/System/Library/ExtensionKit/Extensions/ADAskForExceptionExtension.appex/ADAskForExceptionExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.asktod</string>
		<string>com.apple.managedappdistributiond.xpc</string>
	</array>
</dict>
</plist>

```
### ChallengesMessageExtension

> `/System/Library/ExtensionKit/Extensions/ChallengesMessageExtension.appex/ChallengesMessageExtension`

```diff

 	</array>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>AdvancedPurchase</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### FedStatsMLHostPluginClassB

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.triald.namespace-management</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
 	</array>
 </dict>
 </plist>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>AdvancedPurchase</string>
+	</array>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>AdvancedPurchase</string>
+	</array>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.app-distribution.private</key>
 	<true/>
+	<key>com.apple.asktod</key>
+	<true/>
 	<key>com.apple.attributionkitd.token-handoff</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 		<string>com.apple.backgroundassets.system</string>
 		<string>com.apple.StreamingUnzipService</string>
 		<string>com.apple.storekitd</string>
+		<string>com.apple.asktod</string>
+		<string>com.apple.askpermissiond</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```

### 🆕 askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.askpermissiond</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.askpermissiond</string>
	<key>com.apple.askto.responseui.host</key>
	<true/>
	<key>com.apple.asktod</key>
	<true/>
	<key>com.apple.asktod.updateMessageBubble</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.familycircle.agent</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>AskToBuy</string>
	</array>
	<key>com.apple.private.people</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.askpermission.notifications</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.usernotifications.usernotificationservice</string>
		<string>com.apple.AskPermissionUI</string>
		<string>com.apple.biome.PublicStreamAccessService</string>
		<string>com.apple.biome.compute.source</string>
		<string>com.apple.people.agent</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.ScreenTimeAgent.exception</string>
		<string>com.apple.asktod</string>
	</array>
	<key>com.apple.security.ts.springboard-services</key>
	<true/>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
</dict>
</plist>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 		<string>SiriDictation</string>
 		<string>Siri.SelfTriggerSuppression</string>
 		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
+		<string>Siri.OnDeviceAnalytics.attentionAndInvocationSampling</string>
 		<string>Siri.ASR.RequestMetricsRecord</string>
 		<string>Siri.ASR.ContextualReplayRecord</string>
 	</array>

```
### devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

 	<true/>
 	<key>com.apple.private.osanalytics.SubmitLogs.allow</key>
 	<true/>
+	<key>com.apple.private.osanalytics.dre-opt-in.allow</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>
 		<string>AppleCredentialManagerUserClient</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.osanalytics</string>
+	</array>
 </dict>
 </plist>
 

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
+	<array>
+		<string>com.apple.accounts.sync.suggestion</string>
+	</array>
 	<key>com.apple.private.voicememod.client</key>
 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.ctkd.token-client</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.securityd.xpc</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>

```
### liveactivitiesd

> `/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
+	<key>com.apple.carousel.nonmatchingsessions</key>
+	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.carousel.sessionservice</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### StatusKitAgent

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
-	<key>com.apple.SystemConfiguration.SCPreferences-read-access</key>
-	<array>
-		<string>com.apple.radios.plist</string>
-	</array>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

```
### ind

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/ind`

```diff

 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>

```
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>AdvancedPurchase</string>
+	</array>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

```
### AppStoreWidgetsExtension

> `/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>AdvancedPurchase</string>
+	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>AdvancedPurchase</string>
+	</array>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 		<string>com.apple.private.corewifi.readonly-xpc</string>
 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.routined.registration</string>
+		<string>com.apple.security.octagon</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.siri.uaf.service</string>

 		<string>com.apple.private.corewifi.readonly-xpc</string>
 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.routined.registration</string>
+		<string>com.apple.security.octagon</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.siri.uaf.service</string>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>com.apple.asktod</string>
 		<string>com.apple.communicationtrustd.service</string>
 		<string>com.apple.jetpackassetd.xpc</string>
+		<string>com.apple.ScreenTimeAgent.exception</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### gamed

> `/usr/libexec/gamed`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/usr/local/bin/</string>
+		<string>/Library/com.apple.AppleMediaServices/PersistedBags/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<true/>
 	<key>com.apple.diagnostics.launcher-service</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.frontboard.shutdown</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<array>
 		<string>private/var/db/eligibilityd/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.sysdiagnose_helper</string>
+	<key>com.apple.aiml.rapidresourcedelivery.read-config</key>
+	<true/>
 	<key>com.apple.centaurid.xpc</key>
 	<true/>
 	<key>com.apple.corecapture.manager-access</key>

```
