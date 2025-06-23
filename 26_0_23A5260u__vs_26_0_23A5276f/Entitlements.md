## 🔑 Entitlements


### 🆕 AVKitRoutingIntents

> `/Applications/AVKitRoutingService.app/Extensions/AVKitRoutingIntents.appex/AVKitRoutingIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
</dict>
</plist>

```
### AirPlayReceiver

> `/Applications/AirPlayReceiver.app/AirPlayReceiver`

```diff

 	</array>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.timed</key>

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 	<true/>
 	<key>com.apple.appleidsetup.repair.client</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.appstored.install-apps</key>
 	<true/>
 	<key>com.apple.appstored.install-system-apps</key>

 		<string>com.apple.amsaccountsd.multiuser</string>
 		<string>com.apple.appleidsetupd.repair.xpc</string>
 		<string>com.apple.appleidsetupd.setup.xpc</string>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.appstored.xpc.request</string>
 		<string>com.apple.assistant.multiuser.service</string>

 		<string>com.apple.appleidsetupd.repair.xpc</string>
 		<string>com.apple.appleidsetupd.setup.xpc</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.cdp.daemon</string>

```
### Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

 	<true/>
 	<key>com.apple.backboard.client</key>
 	<true/>
+	<key>com.apple.coretelephony.Identity.get</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

```

### 🆕 Diagnostic-6018

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6018.appex/Diagnostic-6018`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/BatteryLife/Archives/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.Diagnostics</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.DiagnosticsKit</string>
	</array>
</dict>
</plist>

```
### Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

 	<array>
 		<string>com.apple.AppleDeviceQueryService</string>
 		<string>com.apple.corerepair.preflightControl</string>
+		<string>com.apple.diskimagecorerepair.preflightControl</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

 		<string>com.apple.appleh13camerad</string>
 		<string>com.apple.appleh16camerad</string>
 		<string>com.apple.corerepair.preflightControl</string>
+		<string>com.apple.diskimagecorerepair.preflightControl</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

```diff

 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileSoftwareUpdate/</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>

 	<array>
 		<string>com.apple.CoreRepairCoreNetworkXPCService</string>
 		<string>com.apple.corerepair.preflightControl</string>
+		<string>com.apple.diskimagecorerepair.preflightControl</string>
 		<string>com.apple.corerepair</string>
 		<string>com.apple.diskimagecorerepair</string>
 	</array>

```
### Diagnostic-9008

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008`

```diff

 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileSoftwareUpdate/</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>

 	<array>
 		<string>com.apple.CoreRepairCoreNetworkXPCService</string>
 		<string>com.apple.corerepair.preflightControl</string>
+		<string>com.apple.diskimagecorerepair.preflightControl</string>
 		<string>com.apple.corerepair</string>
 		<string>com.apple.diskimagecorerepair</string>
 	</array>

```
### SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

 	<true/>
 	<key>com.apple.private.applemesa.allow</key>
 	<true/>
+	<key>com.apple.private.applesmc.user-access</key>
+	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 		<string>AppleMultitouchDeviceUserClient</string>
 		<string>AppleEmbeddedTouchEEPROMDriverUC</string>
 		<string>AppleNVMeEANUC</string>
+		<string>AppleSMCClient</string>
 		<string>AppleBiometricServicesUserClient</string>
 		<string>IO80211APIUserClient</string>
 		<string>AppleAuthCPUserClient</string>

```

### 🆕 FMDCFUTheftAndLossReminderExtension

> `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/FMDCFUTheftAndLossReminderExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
	<true/>
	<key>com.apple.icloud.findmydeviced.access</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.icloud.findmydeviced</string>
	</array>
</dict>
</plist>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 	<true/>
 	<key>com.apple.private.avfoundation.capture.allow</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.incubation.sideloader</string>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-filter</key>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/assets</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VideoIntelligence/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>

 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.securityd.systemkeychain</string>
 		<string>com.apple.networkserviceproxy</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MediaRemoteUI

> `/Applications/MediaRemoteUI.app/MediaRemoteUI`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.airplay.endpoint.xpc</string>
+		<string>com.apple.mediaexperience.endpoint.xpc</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.itunescloudd.xpc</string>
+		<string>com.apple.itunescloud.contenttaste</string>
+		<string>com.apple.coremedia.endpointpicker.xpc</string>
+		<string>com.apple.coremedia.routediscoverer.xpc</string>
+		<string>com.apple.coremedia.routingcontext.xpc</string>
+		<string>com.apple.coremedia.endpointremotecontrolsession.xpc</string>
+		<string>com.apple.PairingManager</string>
+		<string>com.apple.sessionservices</string>
+		<string>com.apple.tvremotecore.xpc</string>
+		<string>com.apple.SharingServices</string>
+		<string>com.apple.TVSystemUIService.banners</string>
+		<string>com.apple.mediacontrol.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 	</array>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key> com.apple.sharing.Session</key>
+	<true/>
 	<key>CARAppHidden</key>
 	<true/>
 	<key>CARCapableApp</key>

```
### MomentsUIService

> `/Applications/MomentsUIService.app/MomentsUIService`

```diff

 	<true/>
 	<key>com.apple.powerlog.plxpclogger.xpc</key>
 	<true/>
+	<key>com.apple.private.MobileContainerManager.appGroup.noReference</key>
+	<array>
+		<string>group.com.apple.Journal</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<array>
 		<string>group.com.apple.tipsnext</string>
 		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
+		<string>group.com.apple.Journal</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### PCViewService

> `/Applications/PCViewService.app/PCViewService`

```diff

 	<array>
 		<string>App.Intent</string>
 	</array>
-	<key>com.apple.private.coordination.alarms</key>
-	<true/>
-	<key>com.apple.private.coordination.timers</key>
-	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase - 2</key>

 		<string>com.apple.announced.localplaybacksession</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CompanionLink</string>
-		<string>com.apple.coordination.alarms</string>
-		<string>com.apple.coordination.timers</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.coremedia.asset.xpc</string>
 		<string>com.apple.coremedia.customurlloader.xpc</string>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.appleaccount.ageAttestation</key>
 	<true/>
+	<key>com.apple.appleaccount.ageMigration</key>
+	<true/>
 	<key>com.apple.appleaccount.beneficiary</key>
 	<true/>
 	<key>com.apple.appleaccount.custodian</key>

 		<string>com.apple.PassbookUISceneService.remote-ui</string>
 		<string>com.apple.migrationd</string>
 		<string>com.apple.alarmkitservices</string>
+		<string>com.apple.seserviced.storage-management-presentation</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.seserviced.settings.mach</key>
 	<true/>
+	<key>com.apple.seserviced.storage-management</key>
+	<true/>
 	<key>com.apple.settings.private-access-reset</key>
 	<true/>
 	<key>com.apple.sh</key>

```
### RemoteiCloudQuotaUI

> `/Applications/RemoteiCloudQuotaUI.app/RemoteiCloudQuotaUI`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>Library</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.backupd</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.appstored.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SOSBuddy

> `/Applications/SOSBuddy.app/SOSBuddy`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>

 	<true/>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.secureAppAssertion</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 		<key>value</key>
 		<string>/Applications/SafariViewService.app</string>
 	</dict>
+	<key>com.apple.private.backgroundtaskmanagement.manage</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>App.WebApp.InFocus</string>

```
### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 		<string>com.apple.proactive.visual-action-prediction</string>
 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>
-		<string>com.apple.sage.summarization</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.modelcatalog.catalog</string>

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
+		<string>com.apple.VisualIntelligence</string>
 	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
+	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
 	<key>com.apple.private.eligibilityd.setInput</key>

 	</array>
 	<key>com.apple.private.lockdownmoded.read-write</key>
 	<true/>
+	<key>com.apple.private.logging.preferences</key>
+	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
 	<key>com.apple.private.managedappdistribution.ddm</key>

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.Preferences</string>
+		<string>com.apple.ThreatNotification.FollowUp</string>
 	</array>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>

 		<string>com.apple.migrationd</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.posterboardservices.dataModel</string>
+		<string>com.apple.seserviced.storage-management-presentation</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>

 		<string>com.apple.DeviceActivity</string>
 		<string>com.apple.usernotificationskit</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.ThreatNotificationUI.FollowUpExtension</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<true/>
 	<key>com.apple.seserviced.kmlXpcService</key>
 	<true/>
+	<key>com.apple.seserviced.storage-management</key>
+	<true/>
 	<key>com.apple.sh</key>
 	<true/>
 	<key>com.apple.sharing.Client</key>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.photos.service.multilibrary</key>

 		<string>com.apple.coremedia.routediscoverer.xpc</string>
 		<string>com.apple.coremedia.routingcontext.xpc</string>
 		<string>com.apple.coremedia.volumecontroller.xpc</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.linkd.autoShortcut</string>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.photos.service.multilibrary</key>

 		<string>com.apple.coremedia.routediscoverer.xpc</string>
 		<string>com.apple.coremedia.routingcontext.xpc</string>
 		<string>com.apple.coremedia.volumecontroller.xpc</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>GeneratedImageUserInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/IntelligencePlatform/Artifacts/visualIdentifier/visualIdentifier.db</string>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### SupportFlow

> `/Applications/SupportFlow.app/SupportFlow`

```diff

 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
-	<key>com.apple.private.accounts.allaccounts </key>
+	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>

 		<string>com.apple.tipsd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.backboardd</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	<true/>
 	<key>com.apple.announced.client</key>
 	<true/>
+	<key>com.apple.assistant.cdm.client</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.corespotlight.search.allow.mail</key>
+	<true/>
+	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
+	<array>
+		<string>com.apple.CalendarUI</string>
+		<string>com.apple.DocumentsApp</string>
+		<string>com.apple.MobileAddressBook</string>
+		<string>com.apple.MobileSMS</string>
+		<string>com.apple.Notes</string>
+		<string>com.apple.Photos</string>
+		<string>com.apple.VoiceMemos</string>
+		<string>com.apple.iCal</string>
+		<string>com.apple.mail</string>
+		<string>com.apple.mobilecal</string>
+		<string>com.apple.mobilemail</string>
+		<string>com.apple.mobilenotes</string>
+		<string>com.apple.mobilesafari</string>
+		<string>com.apple.mobileslideshow</string>
+		<string>com.apple.reminders</string>
+	</array>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.EntityResolution</key>
+	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.corespotlight.search</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>

 	<true/>
 	<key>com.apple.private.homekit.allow-secure-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>appEntityRelevanceRanking</string>
+		<string>entityAliasECR</string>
+		<string>entitySubgraph</string>
+		<string>entitySummary</string>
+		<string>eventSubgraph</string>
+		<string>inferenceFeaturesECR</string>
+		<string>loiEntityRelevanceRanking</string>
+		<string>nerdEmbeddingsPeopleTable</string>
+		<string>peopleAliasECR</string>
+		<string>peopleSubgraph</string>
+		<string>personEntityRelevanceRanking</string>
+		<string>relevance</string>
+		<string>visualIdentifier</string>
+	</array>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingtemporarily</key>

 		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.announced.server</string>
+		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.audio.AudioConverterService</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>

 		<string>com.apple.posterboardservices.services</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.sessionservices</string>
-		<string>com.apple.sharingd</string>
+		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.shortcuts.view-service</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.vocabularyupdates</string>

 	<true/>
 	<key>com.apple.sirittsd.can-dump-audio</key>
 	<true/>
+	<key>com.apple.spotlight.entitledattributes</key>
+	<true/>
+	<key>com.apple.spotlight.photos.entitledattributes</key>
+	<true/>
 	<key>com.apple.springboard.display-lookup</key>
 	<true/>
 	<key>com.apple.springboard.flash-color</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	</array>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/Applications/Tamale.app/Tamale</string>
+	</dict>
 	<key>com.apple.private.barcodesupport.allowNotifications</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.generativepartnerservicesettings</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.VisualIntelligence</string>
 	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>

```
### extensionFilter

> `/Applications/Text Message Filter.app/PlugIns/extensionFilter.appex/extensionFilter`

```diff

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.MTLCompilerService</string>
 		<string>com.apple.system.notification_center</string>
+		<string>com.apple.logd</string>
+		<string>com.apple.logd.events</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.generativeassistantsettings</string>
+		<string>com.apple.generativepartnerservicesettings</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### com.apple.Maps.appremoval

> `/System/Library/AppRemovalServices/com.apple.Maps.appremoval.xpc/com.apple.Maps.appremoval`

```diff

 	<array>
 		<string>com.apple.Maps.offline.*</string>
 	</array>
+	<key>com.apple.geoservices.shrinkdb.force</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>UninstallForLaunchServices</string>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 		<string>/private/var/tmp/</string>
 		<string>/private/var/mobile/DTX/</string>
 		<string>/private/var/mobile/DTX/FalsePositives</string>
+		<string>/private/var/mobile/Library/Accessibility/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.private.homekit.location</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ProactiveAppPrediction</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>CarPlay.Connected</string>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.sessionkit.alertPresenter</key>

 		<string>access-calls</string>
 		<string>modify-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>180</string>
+	</array>
 </dict>
 </plist>
 

```
### CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

 		<string>com.apple.CarPlayApp.status-bar-service</string>
 		<string>com.apple.carkit.navigation.service</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.carplay.internal</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### ClarityBoard

> `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

 	<true/>
 	<key>com.apple.ClarityBoard</key>
 	<true/>
+	<key>com.apple.QuartzCore.display-state</key>
+	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>
 	<true/>
+	<key>com.apple.QuartzCore.flipbook</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.QuartzCore.system-layers</key>

 	<array>
 		<string>com.apple.radios.plist</string>
 	</array>
+	<key>com.apple.accessibility.IDSServices</key>
+	<true/>
 	<key>com.apple.aop.hid-device.user-client</key>
 	<dict>
 		<key>orientation</key>

 	<array>
 		<string>keyboard-flush.boot</string>
 	</array>
-	<key>com.apple.security.ts.ipc-posix-shm</key>
-	<array>
-		<string>/FBW1:com.apple.frontboard.syst</string>
-		<string>/FBW2:com.apple.frontboard.syst</string>
-	</array>
 	<key>com.apple.security.ts.location-services</key>
 	<true/>
 	<key>com.apple.security.ts.mach-task-name</key>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

 		<string>access-call-capabilities</string>
 		<string>modify-calls</string>
 		<string>background-calls</string>
+		<string>register-gft-service</string>
 	</array>
 	<key>fairplay-client</key>
 	<string>465671667</string>

```
### ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.icloud.findmydeviced</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.server.bluetooth.le.att.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AVCPlugin

> `/System/Library/ExtensionKit/Extensions/AVCPlugin.appex/AVCPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.priml.PFLMLHostPlugins.AVCPlugin</string>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
+	<key>com.apple.appprotectiond.read</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<string>com.apple.priml.pfl.plugins</string>
 	<key>com.apple.priml.pfl.Morpheus.allowed</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read-write</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.biome.writer</key>

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Caches/com.apple.VideoConference/</string>
+		<string>/private/var/mobile/Library/Logs/CallHistory</string>
+		<string>/private/var/mobile/Library/CallHistoryDB/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mlhostd.xpc</string>
 		<string>com.apple.cloudd</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.CallHistorySyncHelper</string>
 	</array>
 </dict>
 </plist>

```
### AlchemistInferenceProvider

> `/System/Library/ExtensionKit/Extensions/AlchemistInferenceProvider.appex/AlchemistInferenceProvider`

```diff

 		<string>/Library/Caches/com.apple.AlchemistInferenceProvider/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.AlchemistInferenceProvider/</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/examplemodel/</string>
-		<string>/examplemodel/2025_05_06_joint_predictor_637qbu8fw8_100000_full_palette_3mfkv9h744_compression_config_4.0_bpw_universal.mlmodelc/</string>
-	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AGXDeviceUserClient</string>

```

### 🆕 AmbientPhotoFramePosterProvider

> `/System/Library/ExtensionKit/Extensions/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.posterboardservices.data-store</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.suggestion</string>
		<string>photos.face</string>
		<string>photos.memory</string>
		<string>photos.person</string>
		<string>photos.scene</string>
		<string>photos.curation</string>
	</array>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobileslideshow</string>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.XPCStoreOptIn</key>
	<true/>
	<key>com.apple.private.photos.allowcollectionshare</key>
	<true/>
	<key>com.apple.private.photos.allowmemorymutation</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.notification</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/tmp/com.apple.PhotosUIPrivate.PhotosAmbientPosterProvider/</string>
		<string>/private/var/mobile/tmp/com.apple.PhotosUIPrivate.PhotosAmbientPosterProvider/</string>
		<string>/private/var/mobile/Library/SpringBoard/</string>
		<string>/private/var/tmp/com.apple.photoanalysisd/RefreshSessions/</string>
		<string>/private/var/mobile/tmp/com.apple.photoanalysisd/RefreshSessions/</string>
		<string>/private/var/tmp/com.apple.photoanalysisd/UpgradeSessions/</string>
		<string>/private/var/mobile/tmp/com.apple.photoanalysisd/UpgradeSessions/</string>
		<string>/private/var/tmp/com.apple.mediaanalysisd/</string>
		<string>/private/var/mobile/tmp/com.apple.mediaanalysisd/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/DCIM/</string>
		<string>/Media/PhotoStreamsData/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.posterboardservices.services</string>
		<string>com.apple.posterboardservices.dataModel</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### CameraSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 </dict>
 </plist>
 

```
### CoreMotionFoundationModelExtension

> `/System/Library/ExtensionKit/Extensions/CoreMotionFoundationModelExtension.appex/CoreMotionFoundationModelExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.ane.iokit-user-access</key>
-	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
 	<key>com.apple.aned.private.allow</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp.remoteUIExtension</string>
-	<key>com.apple.appprotectiond.guard</key>
-	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
-	<key>com.apple.appprotectiond.read</key>
-	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.assistant.cdm.client</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### GenerativeExperiencesSafetyInferenceProvider

> `/System/Library/ExtensionKit/Extensions/GenerativeExperiencesSafetyInferenceProvider.appex/GenerativeExperiencesSafetyInferenceProvider`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### PhoneAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PhoneAppIntentsExtension.appex/PhoneAppIntentsExtension`

```diff

 	</array>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 	<array>
 		<string>com.apple.TelephonyUtilities</string>
 	</array>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
 	<key>com.apple.springboard.allowallcallurls</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```

### 🆕 PhotosPosterProvider

> `/System/Library/ExtensionKit/Extensions/PhotosPosterProvider.appex/PhotosPosterProvider`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.idle-timer-services</key>
	<true/>
	<key>com.apple.lightsourcesupport.listener</key>
	<true/>
	<key>com.apple.lightsourcesupport.motion</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.posterboardservices.data-store</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.Photos.SpatialPhotosRelive</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.suggestion</string>
		<string>photos.face</string>
		<string>photos.memory</string>
		<string>photos.person</string>
		<string>photos.scene</string>
		<string>photos.locked</string>
	</array>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobileslideshow</string>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.XPCStoreOptIn</key>
	<true/>
	<key>com.apple.private.photos.allowcollectionshare</key>
	<true/>
	<key>com.apple.private.photos.allowmemorymutation</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.messages.access</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.notification</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
	<array>
		<string>com.apple.tipsd</string>
	</array>
	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.tipsnext</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/tmp/com.apple.mobileslideshow.PhotosPosterProvider/</string>
		<string>/private/var/mobile/tmp/com.apple.mobileslideshow.PhotosPosterProvider/</string>
		<string>/private/var/mobile/Library/SpringBoard/</string>
		<string>/private/var/tmp/com.apple.photoanalysisd/RefreshSessions/</string>
		<string>/private/var/mobile/tmp/com.apple.photoanalysisd/RefreshSessions/</string>
		<string>/private/var/tmp/com.apple.photoanalysisd/UpgradeSessions/</string>
		<string>/private/var/mobile/tmp/com.apple.photoanalysisd/UpgradeSessions/</string>
		<string>/private/var/mobile/tmp/com.apple.messages/PFPosterConfigurationImages/</string>
		<string>/private/var/tmp/com.apple.messages/PFPosterConfigurationImages/</string>
		<string>/private/var/tmp/com.apple.photoanalysisd/Spatial3DOnboardingSession/</string>
		<string>/private/var/mobile/tmp/com.apple.photoanalysisd/Spatial3DOnboardingSession/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_SpatialPhotosRelive/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/com.apple.mediaanalysisd/</string>
		<string>/private/var/mobile/tmp/com.apple.mediaanalysisd/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/PhotoData/</string>
		<string>/Media/DCIM/</string>
		<string>/Media/PhotoStreamsData/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.posterboardservices.services</string>
		<string>com.apple.posterboardservices.dataModel</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.lightsourcesupport.lightstate</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.siri.uaf.subscription.service</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.spatialphotosrelive</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.wallpaper.get</key>
	<true/>
</dict>
</plist>

```
### PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`

```diff

 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeExperiences.PromptTags</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
 		<string>/private/var/mobile/Library/Assistant/SiriVocabulary/</string>
+		<string>/Library/Shortcuts/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
+		<string>/Library/Shortcuts/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>

```
### TGOnDeviceInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/TGOnDeviceInferenceProviderService.appex/TGOnDeviceInferenceProviderService`

```diff

 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.foundationmodels</key>
+	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### TVAppExtension

> `/System/Library/ExtensionKit/Extensions/TVAppExtension.appex/TVAppExtension`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceFaceID</string>

```
### WritingToolsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/WritingToolsAppIntentsExtension.appex/WritingToolsAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.sage.summarization</key>

```
### icprefd-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc`

```diff

 	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
+		<string>kTCCServiceExternalCameraMedia</string>
 		<string>kTCCServiceCamera</string>
 	</array>
 	<key>com.apple.private.tcc.override-prompt-policy</key>

```

### 🆕 IOHIDTelemetrySessionFilter

> `/System/Library/HIDPlugins/SessionFilters/IOHIDTelemetrySessionFilter.plugin/IOHIDTelemetrySessionFilter`

- No entitlements *(yet)*

### 🆕 MedicalIDDaemonPlugin

> `/System/Library/Health/Plugins/MedicalIDDaemonPlugin.bundle/MedicalIDDaemonPlugin`

- No entitlements *(yet)*

### 🆕 FilterAsNewCallersSettingsBundle

> `/System/Library/PreferenceBundles/FilterAsNewCallersSettingsBundle.bundle/FilterAsNewCallersSettingsBundle`

- No entitlements *(yet)*

### 🆕 HoldAssistSettingsBundle

> `/System/Library/PreferenceBundles/HoldAssistSettingsBundle.bundle/HoldAssistSettingsBundle`

- No entitlements *(yet)*
### AirPlaySenderService

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/XPCServices/AirPlaySenderService.xpc/AirPlaySenderService`

```diff

 	<array>
 		<string>com.apple.airplay</string>
 		<string>com.apple.airplay.pairing</string>
+		<string>com.apple.pairing</string>
 	</array>
 </dict>
 </plist>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	</array>
 	<key>com.apple.companion-authentication.store-purchase</key>
 	<true/>
-	<key>com.apple.coreidvd.spi</key>
-	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
 	<key>com.apple.developer.aps-environment</key>

 		<string>com.apple.adid.xpc</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.commcenter.xpc</string>
-		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.eligibilityd</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.mobileactivationd</string>

```
### apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

 	<true/>
 	<key>com.apple.networkd_privileged</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Device.Wireless.APSDInterfaceStatus</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>SIRI_SUGGESTIONS_DOMAIN_GROUP_A</string>
 		<string>SIRI_SUGGESTIONS_DOMAIN_GROUP_B</string>
 		<string>SIRI_SUGGESTIONS_PLATFORM</string>
+		<string>SIRI_TTS_AB_DEVICE</string>
 		<string>SIRI_UI_RESPONSES_SETTINGS</string>
 		<string>SIRI_UNDERSTANDING_CLASSIC_DEPRECATION</string>
 		<string>SIRI_UNDERSTANDING_NL</string>

```
### callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

```diff

 	</array>
 	<key>com.apple.security.personal-information.calendars</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Trial/</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.callintelligenced</string>
 	<key>com.apple.siri.activation.service</key>

 		<string>modify-simulated-conversations</string>
 		<string>smart-holding</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>WIRELESS_DATA_ANALYTICS_CALLINTELLIGENCE_EXPERIMENTATION</string>
+	</array>
 	<key>com.apple.usernotifications.listener</key>
 	<true/>
 	<key>com.apple.videoconference.allow-conferencing</key>

```

### 🆕 FRSVCoreImageArchive_bin.metallib

> `/System/Library/PrivateFrameworks/CameraUI.framework/FRSVCoreImageArchive_bin.metallib`

- No entitlements *(yet)*
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
-		<string>com.apple.MobileAsset.AutoAssetNotification</string>
-		<string>com.apple.MobileAsset.MAAutoAsset</string>
+		<string>com.apple.MobileAsset.UAF.IF.PlannerOverrides</string>
+		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNL</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNLOverrides</string>

```
### parsec-fbf

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf`

```diff

 	<true/>
 	<key>com.apple.developer.networking.multipath_extended</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.mlruntime.extension-point-ondemand</string>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 		<string>com.apple.gms.availability</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.SiriViewService</string>
+		<string>com.apple.spotlightui</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### RecentsAppPopover

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAppPopover.appex/RecentsAppPopover`

```diff

 		<string>com.apple.UIKit</string>
 		<string>com.apple.desktopservices</string>
 	</array>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### RecentsAvocado

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado`

```diff

 		<string>com.apple.UIKit</string>
 		<string>com.apple.desktopservices</string>
 	</array>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.temporary.files-widget-transparency</key>

```
### SaveToFiles

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles`

```diff

 	</array>
 	<key>com.apple.shortcuts.background-running</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### com.apple.DocumentManager.Service

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service`

```diff

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.private.diskarbitrationd.access</string>
 		<string>com.apple.CloudSharing.SPIHelper-iOS</string>
+		<string>com.apple.DiskArbitration.diskarbitrationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.fileStackIconList</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### DeviceDataResetXPCServiceWorker

> `/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/XPCServices/DeviceDataResetXPCServiceWorker.xpc/DeviceDataResetXPCServiceWorker`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.devicedatareset.devicedataresetxpcserviceworker</string>
 	<key>com.apple.CommCenter.Preferences-delete</key>
 	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
-	<key>com.apple.private.biome.writer</key>
-	<array>
-		<string>Discoverability.Signals</string>
-	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.ids.registration-reset</key>
 	<true/>
 	<key>com.apple.private.ids.resetstate</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>FeatureDiscoverability</key>
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
+	</dict>
 	<key>com.apple.private.lockdown.finegrained-remove</key>
 	<array>
 		<string>com.apple.mobile.data_sync/Bookmarks</string>

 	<array>
 		<string>/Library/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 	<key>com.apple.security.exception.mobile-preferences-read-write</key>
 	<array>
 		<string>com.apple.ids</string>

```
### FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.ndoagent</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### fitnessintelligenced

> `/System/Library/PrivateFrameworks/FitnessIntelligenceDaemonCore.framework/fitnessintelligenced`

```diff

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.fitnessintelligence.inference</key>
+	<true/>
+	<key>com.apple.private.fitnessintelligence.snapshot</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>

```
### revisiond

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond`

```diff

 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
 	</array>
+	<key>com.apple.private.vfs.authorized-access</key>
+	<true/>
 	<key>com.apple.private.vfs.fsevents-watcher</key>
 	<true/>
 	<key>com.apple.private.vfs.open-by-id</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
 	</array>
+	<key>com.apple.private.nsurlsession.impersonate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.openai</string>
+		<string>com.apple.openai.xcode</string>
 	</array>
 </dict>
 </plist>

```
### HealthFollowUpExtension

> `/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex/HealthFollowUpExtension`

```diff

 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>path</string>
+		<string>bundleID</string>
 		<key>value</key>
-		<string>/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/HealthFollowUpExtension.appex</string>
+		<string>com.apple.Health</string>
 	</dict>
 	<key>com.apple.private.avfoundation.capture.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>
 	<true/>
+	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
 		<string>kTCCServiceCamera</string>

```
### HRCDiagnosticExtension

> `/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/PlugIns/HRCDiagnosticExtension.appex/HRCDiagnosticExtension`

```diff

 	<array>
 		<string>group.com.apple.heartratecoordinatord</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>Library/Logs/Bluetooth/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.bluetoothuser.xpc</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.HeartRateCoordinator</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 homeeventsd

> `/System/Library/PrivateFrameworks/HomeKitEvents.framework/Support/homeeventsd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.homeeventsd</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Development</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.homekit.events</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.homekit.events</key>
		<string>com.apple.homekit</string>
	</dict>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.storage.HomeKit</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>Library/homed/homeeventsd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.SystemConfiguration.configd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.homeeventsd</string>
	</array>
	<key>com.apple.security.ts.cloudkit-client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.homeeventsd</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 	<true/>
 	<key>com.apple.private.CloudSharing.SPI</key>
 	<true/>
-    <key>com.apple.developer.icloud-extended-share-access</key>
-    <array>
-        <string>InProcessShareOwnerParticipantInfo</string>
-    </array>
+	<key>com.apple.developer.icloud-extended-share-access</key>
+	<array>
+		<string>InProcessShareOwnerParticipantInfo</string>
+	</array>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

 		<string>com.apple.nanobuddy</string>
 		<string>com.apple.communicationSafetySettings</string>
 		<string>com.apple.MobileSMS.CKDNDList</string>
+		<string>com.apple.TelephonyUtilities</string>
 	</array>
 	<key>com.apple.private.translation</key>
 	<true/>

 		<string>com.apple.ClarityUI.Messages</string>
 		<string>com.apple.messages.critical-messaging.storage</string>
 		<string>com.apple.Messages.InstallationState</string>
+		<string>com.apple.nanosystemsettings</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

 	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
+		<string>SERVICE_ENTITLEMENT</string>
 		<string>CLIENT_ENTITLEMENT</string>
 		<string>PURGEABLE_ENTITLEMENT</string>
 		<string>PURGE_ENTITLEMENT</string>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.corespeech.corespeechd.xpc</key>
+	<true/>
 	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
 	<true/>
 	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>

 		<string>com.apple.searchd</string>
 		<string>com.apple.omniSearch.search</string>
 		<string>com.apple.siri.flowtools_xpc_service</string>
+		<string>com.apple.siri.localspeechrecognitionbridge.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.flowtools_xpc_service</key>
 	<true/>
+	<key>com.apple.siri.localspeechrecognitionbridge.xpc</key>
+	<true/>
 	<key>com.apple.siri.location</key>
 	<true/>
 	<key>com.apple.siriknowledged.koa.donate.internal</key>

```
### lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
-		<string>kCFPreferencesAnyApplication</string>
-		<string>com.apple.lockdownmoded</string>
+		<string>com.apple.ThreatNotificationUI.FollowUpExtension</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.mediaanalysisd</string>
+	<key>com.apple.springboard.wallpaper.get</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.mediaanalysisd</string>
+	<key>com.apple.springboard.wallpaper.get</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
-		<string>com.apple.MobileAsset.OSMigration</string>
+		<string>com.apple.MobileAsset.MigrationKit</string>
 	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.BackupAgent.RestoreStarted</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.BackupOverCellularEnabledState</key>
+	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.Drive.RestoreEnded</key>
 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.Drive.RestoreStarted</key>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/searchtoold`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
 		<string>/private/var/mobile/Library/Assistant/SiriVocabulary/</string>
+		<string>/Library/Shortcuts/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Shortcuts/</string>
 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
+		<string>/Library/Shortcuts/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Containers/com.apple.managedcorespotlightd/EnabledIndexes</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Shortcuts/</string>
+		<string>/Library/Logs/com.apple.FeatureStore/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>AGXDeviceUserClient</string>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 	<true/>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
+	<key>com.apple.private.photos.managedspotlightindex.read-write</key>
+	<true/>
 	<key>com.apple.private.photos.messages.access</key>
 	<true/>
 	<key>com.apple.private.photos.service.debug</key>

 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>

 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.mediaanalysisd.embeddingstore</string>
 		<string>com.apple.shazamd.events</string>
+		<string>com.apple.TapToRadarKit.service</string>
+		<string>com.apple.managedcorespotlightd</string>
+	</array>
+	<key>com.apple.security.temporary-exception.sbpl</key>
+	<array>
+		<string>(allow file-issue-extension (require-all (extension "com.apple.app-sandbox.read-write") (extension-class "com.apple.photos.managedspotlightindex")))</string>
+		<string>(allow file-issue-extension (require-all (extension "com.apple.photos.managedspotlightindex") (extension-class "com.apple.managedcorespotlightd.read-write")))</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### sosd

> `/System/Library/PrivateFrameworks/SOS.framework/sosd`

```diff

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/SOS.framework/sosd</string>
 	</dict>
+	<key>com.apple.private.exclaves.conclave-host</key>
+	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriTextToSpeech</string>

 		<string>com.apple.sirittsd</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.triald.namespace-management</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.modelcatalog.catalog</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.callintelligenced.service</string>
 		<string>com.apple.translationd</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.remindd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### voicebankingd

> `/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.voicebankingd</string>
+	<key>com.apple.assistant.dictation.prerecorded</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
 	<key>com.apple.developer.icloud-container-environment</key>

```
### ThreatNotificationCFU

> `/System/Library/PrivateFrameworks/ThreatNotificationUI.framework/Extensions/ThreatNotificationCFU.appex/ThreatNotificationCFU`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
-		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.ThreatNotificationUI.FollowUpExtension</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 	<true/>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>
+		<string>write</string>
 		<string>read</string>
 	</array>
 	<key>com.apple.private.usernotifications.systemservice</key>

```
### TVProductPageExtension

> `/System/Library/PrivateFrameworks/VideosUI.framework/PlugIns/TVProductPageExtension.appex/TVProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceFaceID</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.announced.client</key>
 	<true/>
+	<key>com.apple.assistant.cdm.client</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.corespotlight.search.allow.mail</key>
+	<true/>
+	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
+	<array>
+		<string>com.apple.CalendarUI</string>
+		<string>com.apple.DocumentsApp</string>
+		<string>com.apple.MobileAddressBook</string>
+		<string>com.apple.MobileSMS</string>
+		<string>com.apple.Notes</string>
+		<string>com.apple.Photos</string>
+		<string>com.apple.VoiceMemos</string>
+		<string>com.apple.iCal</string>
+		<string>com.apple.mail</string>
+		<string>com.apple.mobilecal</string>
+		<string>com.apple.mobilemail</string>
+		<string>com.apple.mobilenotes</string>
+		<string>com.apple.mobilesafari</string>
+		<string>com.apple.mobileslideshow</string>
+		<string>com.apple.reminders</string>
+	</array>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.EntityResolution</key>
+	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.corespotlight.search</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>

 	<array>
 		<string>com.apple.private.alloy.shortcuts</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>appEntityRelevanceRanking</string>
+		<string>entityAliasECR</string>
+		<string>entitySubgraph</string>
+		<string>entitySummary</string>
+		<string>eventSubgraph</string>
+		<string>inferenceFeaturesECR</string>
+		<string>loiEntityRelevanceRanking</string>
+		<string>nerdEmbeddingsPeopleTable</string>
+		<string>peopleAliasECR</string>
+		<string>peopleSubgraph</string>
+		<string>personEntityRelevanceRanking</string>
+		<string>relevance</string>
+		<string>visualIdentifier</string>
+	</array>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingtemporarily</key>

 		<string>com.apple.amsaccountsd.multiuser</string>
 		<string>com.apple.announced.server</string>
 		<string>com.apple.appleneuralengine</string>
+		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.assistant.dictation</string>
 		<string>com.apple.audio.AURemoteIOServer</string>
 		<string>com.apple.audio.AudioComponentPrefs</string>

 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.safarifetcherd</string>
 		<string>com.apple.sessionservices</string>
-		<string>com.apple.sharingd</string>
+		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.shazamd</string>
 		<string>com.apple.shortcuts.dialogpresentation</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>

 	<true/>
 	<key>com.apple.sirittsd.can-dump-audio</key>
 	<true/>
+	<key>com.apple.spotlight.entitledattributes</key>
+	<true/>
+	<key>com.apple.spotlight.photos.entitledattributes</key>
+	<true/>
 	<key>com.apple.springboard.display-lookup</key>
 	<true/>
 	<key>com.apple.springboard.flash-color</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.write.access</key>
 	<true/>
+	<key>com.apple.assistant.cdm.client</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.corespotlight.search.allow.mail</key>
+	<true/>
+	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
+	<array>
+		<string>com.apple.CalendarUI</string>
+		<string>com.apple.DocumentsApp</string>
+		<string>com.apple.MobileAddressBook</string>
+		<string>com.apple.MobileSMS</string>
+		<string>com.apple.Notes</string>
+		<string>com.apple.Photos</string>
+		<string>com.apple.VoiceMemos</string>
+		<string>com.apple.iCal</string>
+		<string>com.apple.mail</string>
+		<string>com.apple.mobilecal</string>
+		<string>com.apple.mobilemail</string>
+		<string>com.apple.mobilenotes</string>
+		<string>com.apple.mobilesafari</string>
+		<string>com.apple.mobileslideshow</string>
+		<string>com.apple.reminders</string>
+	</array>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.EntityResolution</key>
+	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.corespotlight.search</key>
+	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>appEntityRelevanceRanking</string>
+		<string>entityAliasECR</string>
+		<string>entitySubgraph</string>
+		<string>entitySummary</string>
+		<string>eventSubgraph</string>
+		<string>inferenceFeaturesECR</string>
+		<string>loiEntityRelevanceRanking</string>
+		<string>nerdEmbeddingsPeopleTable</string>
+		<string>peopleAliasECR</string>
+		<string>peopleSubgraph</string>
+		<string>personEntityRelevanceRanking</string>
+		<string>relevance</string>
+		<string>visualIdentifier</string>
+	</array>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingtemporarily</key>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.write</string>
+		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.audio.AudioConverterService</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>

 		<string>com.apple.remindd</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.sessionservices</string>
-		<string>com.apple.sharingd</string>
+		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.shortcuts.view-service</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.vocabularyupdates</string>

 	<true/>
 	<key>com.apple.sirittsd.can-dump-audio</key>
 	<true/>
+	<key>com.apple.spotlight.entitledattributes</key>
+	<true/>
+	<key>com.apple.spotlight.photos.entitledattributes</key>
+	<true/>
 	<key>com.apple.springboard.display-lookup</key>
 	<true/>
 	<key>com.apple.springboard.flash-color</key>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>

```
### RemoteiCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>Library</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.backupd</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.appstored.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### itunesstored

> `/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored`

```diff

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
-	<key>com.apple.coreidvd.spi</key>
-	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.asd.scoring</string>
-		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.backupd</string>

```

### 🆕 FamilyRemoteUINavigationProxy

> `/System/Library/RemoteUI/Plugins/FamilyRemoteUINavigationProxy.bundle/FamilyRemoteUINavigationProxy`

- No entitlements *(yet)*
### AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```diff

 	</dict>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
-    <key>com.apple.devicesharing.enrollmentassetservice.client</key>
-    <true/>
-    <key>com.apple.private.bmk.allow</key>
-    <true/>
+	<key>com.apple.devicesharing.enrollmentassetservice.client</key>
+	<true/>
+	<key>com.apple.private.bmk.allow</key>
+	<true/>
 	<key>com.apple.private.healthkit.metadata.private</key>
 	<true/>
 	<key>com.apple.private.healthkit.read_authorization_bypass</key>

 	</array>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
-    <key>com.apple.private.sharing.unlock-manager</key>
-    <true/>
+	<key>com.apple.private.sharing.unlock-manager</key>
+	<true/>
 	<key>com.apple.private.storekit</key>
 	<array>
 		<string>RemoteDownloadIdentifiers</string>

 	<array>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.BluetoothCloudServices</string>
-        <string>com.apple.devicesharingd.enrollmentassetservice</string>
+		<string>com.apple.devicesharingd.enrollmentassetservice</string>
 		<string>com.apple.visioncompaniond</string>
 	</array>
-    <key>com.apple.security.exception.shared-preference.read-only</key>
-    <array>
-        <string>com.apple.devicesharingd</string>
-    </array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.devicesharingd</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.visioncompaniond</string>
 		<string>com.apple.visionproapp.notifications</string>
+		<string>com.apple.TetsuoUITests</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.intents.intents-helper</key>
 	<true/>
+	<key>com.apple.lightsourcesupport.listener</key>
+	<true/>
+	<key>com.apple.lightsourcesupport.motion</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.mediastream.mstreamd-access</key>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.MapKit.SnapshotService</string>
+		<string>com.apple.lightsourcesupport.lightstate</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.coreimage</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	<true/>
 	<key>com.apple.intents.intents-helper</key>
 	<true/>
+	<key>com.apple.lightsourcesupport.listener</key>
+	<true/>
+	<key>com.apple.lightsourcesupport.motion</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.mediastream.mstreamd-access</key>

 		<string>com.apple.spotlight.IndexDelegateAgent</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.MapKit.SnapshotService</string>
+		<string>com.apple.lightsourcesupport.lightstate</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<true/>
 	<key>com.apple.springboard.fileStackIconList</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.shortcutitems.customimage</key>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	<key>com.apple.developer.associated-domains</key>
 	<array>
 		<string>applinks:find.apple.com</string>
+		<string>applinks:find.apple.com.cn</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>

```
### FitnessWidget

> `/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.companionappd.connect.allow</key>
+	<true/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionComplete</string>
+	<key>com.apple.fitnessintelligenced</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 	<array>
 		<string>/private/var/mobile/Library/DeviceRegistry/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fitnessintelligenced</string>
+		<string>com.apple.heartratecoordinatord.observer</string>
+		<string>com.apple.CompanionLink</string>
+		<string>com.apple.AudioAccessoryServices</string>
+		<string>com.apple.appconduitd.device-connection</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.nanolifestyle</string>
 		<string>com.apple.nanolifestyle.sessiontrackerapp</string>
+		<string>com.apple.FitnessIntelligence</string>
+	</array>
+	<key>com.apple.security.ts.nano-preference.read-write</key>
+	<array>
+		<string>com.apple.nanolifestyle.sessiontrackerapp</string>
 	</array>
 </dict>
 </plist>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.facetime.bag</string>
+		<string>com.apple.ids</string>
 		<string>com.apple.AdLib</string>
 		<string>com.apple.AdPlatforms</string>
 		<string>com.apple.AppleMediaServices</string>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
+	<key>com.apple.intelligentrouting.recommendationservice</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.internal.studylogd</string>
 		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.internal.studylogd</string>
 		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>

```
### HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
+	<key>com.apple.intelligentrouting.recommendationservice</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.internal.studylogd</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>
 		<string>com.apple.linkd.registry</string>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.internal.studylogd</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>
 		<string>com.apple.lsd.xpc</string>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-filter</key>

 		<string>com.apple.securityd.systemkeychain</string>
 		<string>com.apple.networkserviceproxy</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.private.9403EBFD-90B8-4676-84BF-9F38143337E3</key>
 	<true/>
 	<key>platform-application</key>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 		<string>com.apple.financed.service.financestore</string>
 		<string>com.apple.financed.service.store </string>
 		<string>com.apple.financed.service.coredatastore</string>
-		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.proactive.PersonalizationPortrait.Event</string>
 		<string>com.apple.online-auth-agent.xpc</string>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<string>collaborations</string>
 	<key>com.apple.private.iosmac</key>
 	<true/>
+	<key>com.apple.private.jetpackassetd</key>
+	<true/>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.asktod</string>
 		<string>com.apple.communicationtrustd.service</string>
+		<string>com.apple.jetpackassetd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.ClarityUI.Messages</string>
 		<string>com.apple.IMCoreSpotlight</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
+		<string>com.apple.nanosystemsettings</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.backgroundtaskmanagement.manage</key>
+	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Media.NowPlaying</string>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.financed.service.bankconnect</string>
+		<string>com.apple.finhealthd.service</string>
 		<string>com.apple.seserviced.storage-management-presentation</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.softposreaderd</string>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<string>1</string>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.backgroundtaskmanagement.manage</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.assistant.cdm.client</key>

 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>

 		<string>com.apple.MapKit.SnapshotService</string>
 		<string>com.apple.lightsourcesupport.lightstate</string>
 		<string>com.apple.internal.xctestinternalangel.sessions</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### PhotosNotificationsUpdates

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.mobileslideshow.photosnotifications-updates</string>
+	<key>com.apple.SensitiveContentAnalysis.intervention.host</key>
+	<true/>
+	<key>com.apple.developer.sensitivecontentanalysis.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
 	<key>com.apple.mediastream.mstreamd-access</key>
 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.photos.allowcollectionshare</key>
 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>

 	<array>
 		<string>com.apple.photos.kvstore</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Media/PhotoData/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/AppleInternal/Library/Jet/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.symptom_analytics</string>
+		<string>com.apple.commcenter.coretelephony.xpc</string>
+		<string>com.apple.appstoreagent.xpc</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.cache_delete</string>
+		<string>com.apple.jetpackassetd.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### Preview

> `/private/var/staged_system_apps/Preview.app/Preview`

```diff

 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.metadata.exattrs</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

```
### RemindersWidgetExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension`

```diff

 	<array>
 		<string>kTCCServiceReminders</string>
 	</array>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.reminders</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>Library/Shortcuts/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.remindd</string>

 	</array>
 	<key>com.apple.shortcuts.background-running</key>
 	<true/>
+	<key>com.apple.shortcuts.stepwise-execution</key>
+	<true/>
+	<key>com.apple.shortcuts.variable-injection</key>
+	<true/>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 </dict>
 </plist>
 

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.feature-availability.read</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>

```

### 🆕 WeatherPoster

> `/private/var/staged_system_apps/Weather.app/Extensions/WeatherPoster.appex/WeatherPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.weather</string>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.storage.Weather</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.weather</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.countryd/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Weather/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.weather</string>
		<string>com.apple.weather.internal</string>
		<string>com.apple.weather.sensitive</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```
### perfpowermetricd

> `/usr/bin/perfpowermetricd`

```diff

 	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
+	<key>com.apple.batteryintelligenced.batteryanalysis-read</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.computesafeguards.managing.allow</key>

 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
+	<key>com.apple.private.iokit.charging-iconography</key>
+	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>
 	<true/>
 	<key>com.apple.private.ioreporting.access</key>

 		<string>com.apple.computesafeguards.managing</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
+	<key>com.apple.batteryintelligenced.batteryanalysis-read</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.computesafeguards.managing.allow</key>

 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
+	<key>com.apple.private.iokit.charging-iconography</key>
+	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>
 	<true/>
 	<key>com.apple.private.ioreporting.access</key>

 		<string>com.apple.computesafeguards.managing</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.surfboard.CFUserNotification</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### DumpPanic

> `/usr/libexec/DumpPanic`

```diff

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
-	<key>com.apple.trial.client</key>
-	<array>
-		<string>1730</string>
-	</array>
 </dict>
 </plist>
 

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
+	<key>com.apple.batteryintelligenced.batteryanalysis-read</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.computesafeguards.managing.allow</key>

 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
+	<key>com.apple.private.iokit.charging-iconography</key>
+	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>
 	<true/>
 	<key>com.apple.private.ioreporting.access</key>

 		<string>com.apple.computesafeguards.managing</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
+	<key>com.apple.batteryintelligenced.batteryanalysis-read</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.computesafeguards.managing.allow</key>

 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
+	<key>com.apple.private.iokit.charging-iconography</key>
+	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>
 	<true/>
 	<key>com.apple.private.ioreporting.access</key>

 		<string>com.apple.computesafeguards.managing</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 	<array>
 		<string>com.apple.airplay</string>
 		<string>com.apple.airplay.pairing</string>
+		<string>com.apple.pairing</string>
 	</array>
 	<key>lskdd-client</key>
 	<string>898061433</string>

```
### aned

> `/usr/libexec/aned`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.triald</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/tmp/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### appleh16camerad

> `/usr/libexec/appleh16camerad`

```diff

 	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/CrashReporter/appleh16camerad/</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

 	<array>
 		<string>media</string>
 	</array>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
 </dict>
 </plist>
 

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.locationd.activity</key>
+	<true/>
 	<key>com.apple.locationd.pedestrianfencemanager</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 		<string>com.apple.iconservices.store</string>
 		<string>com.apple.powerui.audioAccessorySmartChargeManager</string>
 		<string>com.apple.AttentionAwareness</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 		<string>com.apple.accessories.connection-info-server</string>
 		<string>com.apple.carkit.layer-metadata</string>
 		<string>com.apple.chronoservices</string>
+		<string>com.apple.powerexperienced.powermitigationsmanager.service</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.cascade.Maintenance</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### biometrickitd

> `/usr/libexec/biometrickitd`

```diff

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.locationd.activity</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.USBCEntitlement</key>
+	<true/>
 	<key>com.apple.VE.CVCalibration.client</key>
 	<true/>
 	<key>com.apple.ane.memoryUnwiringOptOutAccess.allow</key>

 		<string>com.apple.RelativeMotion</string>
 		<string>com.apple.SoundAnalysis</string>
 		<string>com.apple.sensitivecontentanalysis.testing</string>
+		<string>com.apple.SensitiveContentAnalysis</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.CarPlayUIServices.cluster-theme</key>
 	<true/>
+	<key>com.apple.private.carkit.sessionBoost</key>
+	<true/>
 	<key>com.apple.private.carp</key>
 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>

```
### carkitd

> `/usr/libexec/carkitd`

```diff

 	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
+	<key>com.apple.private.carkit.sessionBoost</key>
+	<true/>
 	<key>com.apple.private.carkit.sessionRequest</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.sysdiagnose.service.xpc</string>
+		<string>com.apple.carkit.sessionBoost.service</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### coreidvd

> `/usr/libexec/coreidvd`

```diff

 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.businessservicesd</string>
 	</array>
-	<key>com.apple.security.network.client</key>
-	<true/>
-	<key>com.apple.security.network.server</key>
-	<true/>
 	<key>com.apple.security.system-group-containers</key>
 	<array>
 		<string>systemgroup.com.apple.mobileactivationd</string>

```
### countryd

> `/usr/libexec/countryd`

```diff

 	<true/>
 	<key>com.apple.rapport.StatusUpdates</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/Caches/com.apple.countryd/</string>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.eligibilityd</string>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>com.apple.MobileInternetSharing</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.photos.service</string>
+		<string>com.apple.powerexperienced.powermitigationsmanager.service</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.purplebuddy.budd.cloud.xpc</string>

```
### deferredmediad

> `/usr/libexec/deferredmediad`

```diff

 	<array>
 		<string>com.apple.camera</string>
 	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.modelmanager</string>
-		<string>com.apple.usernotifications.usernotificationservice</string>
-		<string>com.apple.usernotifications.listener</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.cameracapture</string>

```
### diskimagesiod

> `/usr/libexec/diskimagesiod`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.disk-device-access</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyAllFiles</string>

```
### dmd

> `/usr/libexec/dmd`

```diff

 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 		<string>/Library/InstallCoordination/removability.plist</string>
 		<string>/Library/UserConfigurationProfiles/</string>
+		<string>/Library/Logs/CrashReporter/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
+		<string>group.com.apple.icloud.findmydevice.followup</string>
 	</array>
 	<key>com.apple.private.system-keychain</key>
 	<true/>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.communicationsfilter</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.fmf.local</string>

```
### gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

 		<string>com.apple.GameController.gamecontrollerd.app</string>
 		<string>com.apple.situational-awareness.game-pad-controller</string>
 		<string>com.apple.gamepolicyd.tool.privileged</string>
+		<string>com.apple.surfboard.launcherservice</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.applibrary.openpod</key>
 	<true/>
+	<key>com.apple.surfboard.launcherservice.client</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### gamepolicyd

> `/usr/libexec/gamepolicyd`

```diff

 	<string>com.apple.gamepolicyd</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.gamepolicyd</string>
+	<key>com.apple.backboardd.globalDeferringChainObserver</key>
+	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.modelmanager.assertion</key>
 	<true/>
 	<key>com.apple.private.clpc.policy</key>

 	<array>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.GameOverlayUI</string>
+		<string>com.apple.backboard.hid-services.xpc</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### idcredd

> `/usr/libexec/idcredd`

```diff

 	<true/>
 	<key>com.apple.sts.xpchelperclient.transceive.proxy.listener</key>
 	<true/>
-	<key>com.apple.timed</key>
-	<true/>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.healthlite.spi</key>
 	<true/>
+	<key>com.apple.heartratecoordinator.spi.heartrate</key>
+	<true/>
 	<key>com.apple.hid.heartrate-access</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access-protected</key>

 	<array>
 		<string>/private/var/db/accessoryupdater/DurianUpdaterService/</string>
 		<string>/private/var/mobile/Library/CLEEDMediaService/</string>
+		<string>/private/var/db/location_log_keys/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<string>/Library/UnifiedAssetFramework</string>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>PurpleSystemEventPort</string>
 		<string>com.apple.coremedia.nerotransportconnectionxpc</string>
-		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.timesync.expositor</string>
 		<string>com.apple.timesync.manager</string>
 		<string>com.apple.timesync.ptp.manager</string>

```
### ospredictiond

> `/usr/libexec/ospredictiond`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.coremedia.cameraviewfinder</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>251</string>
+		<string>364</string>
 		<string>1200</string>
 	</array>
 </dict>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<array>
 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
 	</array>
-	<key>com.apple.private.coordination.alarms</key>
-	<true/>
-	<key>com.apple.private.coordination.timers</key>
-	<true/>
 	<key>com.apple.private.coreservices.cangetcurrentactivityinfo</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 		<string>com.apple.coremedia.mediaplaybackd.player.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.sandboxserver.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.videoqueue</string>
-		<string>com.apple.coordination.alarms</string>
-		<string>com.apple.coordination.timers</string>
 		<string>com.apple.coreaudio.device</string>
 		<string>com.apple.coremedia.admin</string>
 		<string>com.apple.coremedia.asset.xpc</string>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.private.audio.suppress-mic-indicator</key>
 	<true/>
+	<key>com.apple.private.avfoundation.audio-format-override</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>ScreenSharing</string>

```

### 🆕 securityresearchdevice-init

> `/usr/libexec/securityresearchdevice-init`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.assets.change-daemon-config</key>
	<true/>
	<key>com.apple.private.img4.nonce.cryptex1.generic.erm</key>
	<true/>
	<key>com.apple.private.security-research-device</key>
	<true/>
	<key>com.apple.private.security.AppleImage4.user-client</key>
	<true/>
	<key>com.apple.private.security.cryptex.install</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleImage4UserClient</string>
	</array>
</dict>
</plist>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 		<string>/usr/standalone/firmware/SLAM/</string>
 		<string>/private/preboot/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/db/nearbyd</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.siri.findmy</string>
+	</array>
 	<key>com.apple.private.security.storage.CoreKnowledge</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 	<true/>
 	<key>com.apple.rootless.storage.coreknowledge</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.siri.findmy</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>

 		<string>com.apple.carpd.xpc</string>
 		<string>com.apple.caraccessoryframework.gatekeeper</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.ak.anisette.xpc</string>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.medialibraryd.xpc</string>

 		<string>com.apple.IntelligenceTasks</string>
 		<string>com.apple.SiriEntityMatcher</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```
### sportsd

> `/usr/libexec/sportsd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>Production</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.private.activitykit.activityAuthorizationListener</key>
 	<true/>
 	<key>com.apple.private.activitykit.activityAuthorizer</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	<array>
 		<string>group.com.apple.sports</string>
 	</array>
+	<key>com.apple.private.sessionkit.assertionRequester</key>
+	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>
 	<true/>
 	<key>com.apple.private.sessionkit.customPushProcessIdentifier</key>
 	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.sports</string>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/</string>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+		<string>/Library/Shortcuts/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.watchlistd.xpc</string>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.sessionservices</string>
 	</array>
 	<key>com.apple.watchlist.private.suppression</key>
 	<true/>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 			<string>com.apple.sysdiagnose_helper</string>
 		</dict>
 	</array>
+	<key>com.apple.private.osanalytics.defaults.allow</key>
+	<true/>
 	<key>com.apple.private.psg.internal</key>
 	<true/>
 	<key>com.apple.private.tcc.allow-prompting</key>

```
### textcomposerd

> `/usr/libexec/textcomposerd`

```diff

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.textcomposerd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.modelmanager</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.AppSupport</string>
 		<string>com.apple.EmojiPreferences</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.tipsd</string>
+	<key>com.apple.developer.usernotifications.time-sensitive</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>

```
### triald

> `/usr/libexec/triald`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/Managed Preferences/mobile/</string>
 		<string>/private/var/MobileAsset/</string>
-		<string>/private/var/mobile/Library/OSAnalytics/Preferences/</string>
-		<string>/private/var/mobile/Library/Caches/GeoServices/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	<array>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
-		<string>com.apple.softwareupdateservicesd</string>
-		<string>com.apple.keyboard.preferences</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### usermanagerd

> `/usr/libexec/usermanagerd`

```diff

 <dict>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.keystore.device.verify</key>
+	<true/>
 	<key>com.apple.mkb.usersession.ops</key>
 	<true/>
 	<key>com.apple.private.CacheDelete</key>

```
### wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

 	<true/>
 	<key>com.apple.private.wifivelocity</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/preferences/com.apple.networkd.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>

 		<string>com.apple.SystemConfiguration.configd</string>
 		<string>com.apple.private.corewifi.internal-xpc</string>
 		<string>com.apple.symptoms.symptomsd.managed_events</string>
+		<string>com.apple.networkd</string>
+		<string>com.apple.mdns</string>
+		<string>com.apple.networkserviceproxy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>wifianalyticsd</string>
 		<string>apple</string>
 		<string>com.apple.identities</string>
 		<string>com.apple.certificates</string>

```
### wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lsd.mapdb</string>
+		<string>com.apple.coreservices.quarantine-resolver</string>
 		<string>com.apple.networkd_privileged</string>
 		<string>com.apple.private.skywalk.observe-stats</string>
 		<string>com.apple.private.nehelper.privileged</string>

```
### wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

 		<string>group.com.apple.wifi</string>
 		<string>group.com.apple.wifi.logs</string>
 	</array>
+	<key>com.apple.private.security.storage.wifi</key>
+	<true/>
 	<key>com.apple.private.sysdiagnose</key>
 	<true/>
 	<key>com.apple.private.ubiquity-kvstore-access</key>

```
### appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

 	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/CrashReporter/appleh16camerad/</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

 	<array>
 		<string>media</string>
 	</array>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
 </dict>
 </plist>
 

```
