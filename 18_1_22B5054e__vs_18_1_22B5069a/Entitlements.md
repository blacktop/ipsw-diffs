## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<array>
 		<string>com.apple.AppStoreComponents</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.surfboard-prevent-homeui-from-hiding-when-launching</key>

```
### AppProtectionUIHost

> `/Applications/AppProtectionUIHost.app/AppProtectionUIHost`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appprotectiond.read</string>

```
### Camera

> `/Applications/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
-	<key>com.apple.corespeech.supportheysiriwhenrecord.sae</key>
-	<true/>
 	<key>com.apple.developer.extension-host.photo-editing</key>
 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>

```
### LockScreenCamera

> `/Applications/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
-	<key>com.apple.corespeech.supportheysiriwhenrecord.sae</key>
-	<true/>
 	<key>com.apple.developer.extension-host.photo-editing</key>
 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>

```
### MusicRecognition

> `/Applications/MusicRecognition.app/MusicRecognition`

```diff

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/var/mobile/Library/Application Support/com.apple.iTunesCloud/URLBags/</string>
 		<string>/Library/Logs/MediaServices/</string>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
+		<string>/Library/com.apple.iTunesCloud/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 				<string>Notification.Usage</string>
 			</array>
 		</dict>
+		<key>Tips</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Discoverability.Signals</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>

 	<array>
 		<string>AppleNVMeEANUC</string>
 		<string>AppleAPFSUserClient</string>
+		<string>AppleBiometricServicesUserClient</string>
 		<string>AGXCommandQueue</string>
 		<string>AGXDevice</string>
 		<string>AGXDeviceUserClient</string>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.ind.cloudfeatures</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<string>com.apple.siri</string>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
+	<key>com.apple.springboard.deliveropenurlusingworkspace</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### StickersUltraExtension

> `/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension`

```diff

 		<string>com.apple.AvatarUI.Staryu</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.keyboard.preferences</string>
+		<string>com.apple.EmojiPreferences</string>
 	</array>
 	<key>com.apple.systemstatus.activityattribution</key>
 	<true/>

```
### StickersUltra

> `/Applications/StickersUltra.app/StickersUltra`

```diff

 		<string>com.apple.AvatarUI.Staryu</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.keyboard.preferences</string>
+		<string>com.apple.EmojiPreferences</string>
 	</array>
 	<key>com.apple.systemstatus.activityattribution</key>
 	<true/>

```

### 🆕 AirDropModule

> `/System/Library/ControlCenter/Bundles/AirDropModule.bundle/AirDropModule`

- No entitlements *(yet)*

### 🆕 SatelliteModule

> `/System/Library/ControlCenter/Bundles/SatelliteModule.bundle/SatelliteModule`

- No entitlements *(yet)*
### ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

 		<string>UniqueDeviceID</string>
 		<string>InverseDeviceID</string>
 	</array>
+	<key>com.apple.private.analyticsagent.xpc.allow</key>
+	<true/>
+	<key>com.apple.private.analyticsqueryvalue</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.ReportCrash</string>
 	<key>com.apple.private.biome.read-write</key>

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.analyticsagent</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceBluetoothAlways</string>
 	</array>
+	<key>com.apple.private.tcc.events.subscriber</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceFocusStatus</string>

```
### ContactsButtonXPCService

> `/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.Contacts.database-allow</key>
-	<true/>
 	<key>com.apple.backboardd.eventAuthenticationVerification</key>
 	<true/>
 	<key>com.apple.backboardd.setAuthenticatedTouches</key>

 	</array>
 	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-only</key>
-	<array>
-		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.iconservices.store</string>

```
### shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

 	<true/>
 	<key>com.apple.security.device.microphone</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.locationd.synchronous</string>

```
### storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
+	<true/>
 	<key>com.apple.appstored.octane</key>
 	<true/>
 	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	<true/>
 	<key>com.apple.private.cfnetwork.har-capture-amp</key>
 	<true/>
+	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
+	<dict>
+		<key>New item</key>
+		<string></string>
+	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.ids.remoteurlconnection</key>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.kvs.ignore-quota</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.nsurlsession-allow-override-connection-pool</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceFaceID</string>
+		<string>kTCCServiceLiverpool</string>
+	</array>
+	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
+	<array>
+		<string>com.apple.storekit.externalPurchaseTokensV2</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

 		<string>com.apple.idsremoteurlconnectionagent.desktop.auth</string>
 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.itunesstored.xpc</string>
+		<string>com.apple.kvsd</string>
 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.passd.payment</string>

 		<string>com.apple.xpc.amstreatmentstoreservice</string>
 		<string>com.apple.misagent</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.watchnotificationsui.alertservice</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>ExternalGateway</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceFaceID</string>

 		<string>com.apple.attributionkitd.xpc.token-handoff</string>
 		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
+		<string>com.apple.storekitd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.watchnotificationsui.alertservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<key>abs-client</key>
 	<string>143531244</string>
 	<key>adi-client</key>
-	<string>572356293</string>
+	<string>347420559</string>
 	<key>application-identifier</key>
 	<string>com.apple.akd</string>
 	<key>aps-connection-initiate</key>

```

### 🆕 analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.generativeexperiences.availabilityService</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.analyticsagent</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
+	<key>com.apple.private.analyticsqueryvalue</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.analyticsd</string>
 	<key>com.apple.private.biome.read-only</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.analyticsagent</string>
 		<string>com.apple.SystemConfiguration.configd</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.aggregated.addaily</string>

```
### cdpd

> `/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd`

```diff

 	<true/>
 	<key>com.apple.securebackupd.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.ts.ipc-posix-sem</key>
 	<string>purplebuddy.sentinel</string>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceFinancialData</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>com.apple.systemstatus.domains</key>
+	<array>
+		<string>media</string>
+	</array>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>332</string>

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.frontboard.disable-watchdog</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.chrono.controls</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.chrono.widgetcenterconnection</string>
+		<string>com.apple.chronoservices</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.extensionkitservice</string>

```
### matd

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/matd`

```diff

 	</array>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.inactive.fullaccess</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	<array>
 		<string>PopInstallationQueue</string>
 	</array>
+	<key>com.apple.managedconfiguration.profiled.set</key>
+	<array>
+		<string>Passcode</string>
+	</array>
 	<key>com.apple.mediaremote.device-info</key>
 	<true/>
 	<key>com.apple.mediaremote.remote-control-discovery</key>

 	<true/>
 	<key>com.apple.private.homekit.wallet-key</key>
 	<true/>
+	<key>com.apple.private.hsa-authentication-processing</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.home</string>

 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.rtcreportingd</key>

```

### 🆕 MeasureWidgetExtension

> `/private/var/staged_system_apps/Measure.app/PlugIns/MeasureWidgetExtension.appex/MeasureWidgetExtension`

- No entitlements *(yet)*
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.webinspector.allow-remote-inspection</key>
-	<true/>
 	<key>com.apple.private.xpc.domain-extension</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Config</key>

```
### SequoiaTranslator

> `/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator`

```diff

 	<key>application-identifier</key>
 	<string>com.apple.Translate</string>
 	<key>aps-environment</key>
-	<string>development</string>
+	<string>production</string>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

```
### appprotectiond

> `/usr/libexec/appprotectiond`

```diff

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleKeyStoreUserClient</string>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.networkextension.configuration</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.runningboard.process-state</key>

```
### demod

> `/usr/libexec/demod`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
+	<key>com.apple.private.assets.change-daemon-config</key>
+	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.InFocus</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### dmd

> `/usr/libexec/dmd`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreAppProtection</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.ignoreRemovability</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreRestrictions</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<true/>
 	<key>com.apple.feedbackd.remote-evaluation</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>private/var/db/eligibilityd/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.gms.availability</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.inputAnalytics.serverStats</string>
+		<string>com.apple.inputAnalytics.IASWTAnalyzer</string>
+		<string>com.apple.inputAnalytics.IASSRAnalyzer</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.inputanalyticsd</string>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.keystore.escrow.create</key>
 	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>

```
### mdmuserd

> `/usr/libexec/mdmuserd`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.remove-profile</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.keystore.escrow.create</key>
 	<true/>
 	<key>com.apple.managedconfiguration.mdmd-access</key>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
 	<key>com.apple.VE.CVCalibration.client</key>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<string>com.apple.intelligenceplatform.Sysdiagnose</string>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.voicetrigger.notbackedup</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleNVMeUpdateUC</string>

```
