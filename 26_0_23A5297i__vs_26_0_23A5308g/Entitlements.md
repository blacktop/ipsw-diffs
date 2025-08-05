## 🔑 Entitlements

### AccessibilityReader_iOS

> `/Applications/AccessibilityReader_iOS.app/AccessibilityReader_iOS`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.runningboard.accessibility</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>

```
### ContinuitySingShieldUI

> `/Applications/ContinuitySingShieldUI.app/ContinuitySingShieldUI`

```diff

 	<array>
 		<string>com.apple.cameracapture</string>
 	</array>
+	<key>com.apple.springboard.hardware-button-service.background-event-consumption</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>

```
### Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

 	<true/>
 	<key>com.apple.private.iokit.rootdomain-set-property</key>
 	<true/>
+	<key>com.apple.private.iokit.system-nvram-allow</key>
+	<true/>
 	<key>com.apple.private.security.no-container</key>
 	<true/>
 	<key>com.apple.private.security.no-sandbox</key>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.Diagnostics</string>
 	<key>com.apple.AppleNVMeEAN.allow</key>
 	<true/>
 	<key>com.apple.AppleServiceToolkit.host</key>

```
### Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```diff

 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>EXDisplayPipeUserClient</string>
 		<string>AppleSMCClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### Family

> `/Applications/Family.app/Family`

```diff

 	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
+	<key>com.apple.family.ageRange</key>
+	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>

```
### FAFollowupExtension

> `/Applications/Family.app/PlugIns/FAFollowupExtension.appex/FAFollowupExtension`

```diff

 	<string>com.apple.family.FAFollowupExtension</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.family.ageRange</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
-	<key>com.apple.icloud.FindMyDevice.RepairDevice.access</key>
-	<true/>
-	<key>com.apple.icloud.searchparty.beaconManager.repairdeviceaccess</key>
-	<true/>
 	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.accessorydiscoverysession</key>

 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.findmy.findmylocate.fenceservice</string>
-		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
-		<string>com.apple.icloud.searchpartyd.ownersession</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FMDCFUTheftAndLossReminderExtension

> `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/FMDCFUTheftAndLossReminderExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.authkit.client.private</key>
-	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
 	<true/>
-	<key>com.apple.icloud.FindMyDevice.RepairDevice.access</key>
-	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
-	<key>com.apple.icloud.searchparty.beaconManager.repairdeviceaccess</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
-	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.icloud.findmydeviced</string>
-		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
-		<string>com.apple.ak.auth.xpc</string>
 	</array>
 </dict>
 </plist>

```
### GameTrampoline

> `/Applications/GameTrampoline.app/GameTrampoline`

```diff

 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GameTrampoline</string>
 	<key>com.apple.developer.associated-domains</key>
-	<array/>
+	<array>
+		<string>applinks:games.apple.com</string>
+	</array>
 	<key>com.apple.developer.game-center</key>
 	<true/>
 	<key>com.apple.private.game-center</key>
 	<array>
 		<string>Account</string>
 	</array>
+	<key>com.apple.private.swc.additional-service-details-consumer</key>
+	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/tmp/APCCaptures/</string>
 		<string>/var/mobile/Library/Caches/com.apple.homedevicesetup/</string>
 	</array>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 		<string>com.apple.tvremotecore.xpc</string>
 		<string>com.apple.mediacontrol.xpc</string>
 		<string>com.apple.intelligentroutingd.xpc.media</string>
+		<string>com.apple.SharingServices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.lightsourcesupport.listener</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.messages.composeclient</key>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
+	<key>com.apple.private.security.storage.MessagesMetaData</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>
 	<true/>
 	<key>com.apple.private.security.storage.PassKit</key>

 		<string>/Library/SMS/</string>
 		<string>/Library/Caches/com.apple.MobileSMS/</string>
 		<string>/Library/CallHistoryDB/</string>
+		<string>/Library/MessagesMetaData/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lightsourcesupport.lightstate</string>
 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.suggestd.events</string>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
-	<key>com.apple.private.contactsui.channel-in-process-override</key>
-	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 			<key>Streams</key>
 			<array>
 				<string>Notification.Usage</string>
+				<string>CarPlay.Connected</string>
+				<string>App.InFocus</string>
 			</array>
 		</dict>
 		<key>SiriMontaraSyncedPreferencesBuiltinWrites</key>

```
### ProductKitViewer

> `/Applications/ProductKitViewer.app/ProductKitViewer`

```diff

 	<array>
 		<string>/private/var/mobile/Library/ProductKit/</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.ProductKit</string>
 	</array>

```
### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
+	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
 	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>

 		<string>com.apple.modelmanager</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	</dict>
 	<key>com.apple.private.replay-kit</key>
 	<true/>
+	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>
+	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

```
### SoftwareUpdateUIService

> `/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService`

```diff

 	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.security.no-container</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.softwareupdateservicesd</string>
 		<string>CAREServer</string>

```
### SupportFlow

> `/Applications/SupportFlow.app/SupportFlow`

```diff

 		<key>AppPrediction</key>
 		<dict>
 			<key>Streams</key>
-			<array>
-				<string>DeviceExpert.Troubleshooting</string>
-			</array>
+			<dict>
+				<key>DeviceExpert.Troubleshooting</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Discoverability.Signals</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
 		</dict>
 		<key>FeatureDiscoverability</key>
 		<dict>
 			<key>Streams</key>
-			<array>
-				<string>Discoverability.Signals</string>
-			</array>
+			<dict>
+				<key>Discoverability.Signals</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
 		</dict>
 	</dict>
 	<key>com.apple.private.managedclient.configurationprofiles</key>

 	<array>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tipsd.supportFlowApp</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.SupportFlow</string>

 		<string>com.apple.softwareupdateservicesd</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.tipsd</string>
+		<string>com.apple.tipsd.supportFlow.analytics</string>
 		<string>com.apple.tzlink</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>

 	<array>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.tipsd.supportFlow.analytics</string>
 	</array>
 	<key>com.apple.softwareupdateservices.client.allowed</key>
 	<true/>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>

```
### iMessageAppsViewService

> `/Applications/iMessageAppsViewService.app/iMessageAppsViewService`

```diff

 	<true/>
 	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
 	<true/>
+	<key>com.apple.lightsourcesupport.listener</key>
+	<true/>
 	<key>com.apple.messages.sticker-sharing-level</key>
 	<string>system</string>
 	<key>com.apple.private.avatar.store</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lightsourcesupport.lightstate</string>
 		<string>com.apple.stickers.api</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.systemstatus</string>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.springboard.system-aperture-portaling</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	<true/>
 	<key>com.apple.springboard.activateassistant</key>
 	<true/>
+	<key>com.apple.springboard.menu-bar-service.toggle-visibility</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 			<array>
 				<string>CarPlay.Connected</string>
 				<string>App.InFocus</string>
+				<string>HomeKit.Client.AccessoryControl</string>
 			</array>
 		</dict>
 	</dict>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager</string>
+		<string>com.apple.GameController.system-button-service</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

 		<string>com.apple.avatar.support</string>
 		<string>com.apple.avatar.service</string>
 	</array>
+	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
+	<true/>
 	<key>com.apple.springboard.launchapplications</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### ShortcutsTopHitsExtension

> `/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension`

```diff

 	</array>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/CallHistoryDB/</string>

 	<array>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.contactsd</string>
+		<string>com.apple.contactsd.support</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.siriactionsd.xpc</string>
 	</array>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.HearingModeService</key>
 	<true/>
+	<key>com.apple.LaunchApp</key>
+	<true/>
 	<key>com.apple.MobileInternetSharing.allow</key>
 	<true/>
 	<key>com.apple.ModeEntityScorer</key>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
+	<key>com.apple.springboard.menu-bar-service.toggle-visibility</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>

```
### CoreMotionFoundationModelExtension

> `/System/Library/ExtensionKit/Extensions/CoreMotionFoundationModelExtension.appex/CoreMotionFoundationModelExtension`

```diff

 	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.CoreMotion.IMUFoundationModel</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.CoreMotion.Overrides</string>
+	</array>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel_Overrides/purpose_auto/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>H11ANEInDirectPathClient</string>

```
### GenerativeExperiencesSafetyInferenceProvider

> `/System/Library/ExtensionKit/Extensions/GenerativeExperiencesSafetyInferenceProvider.appex/GenerativeExperiencesSafetyInferenceProvider`

```diff

 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
-		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
-		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
+		<string>AppleIntelligence.Reporting.SafetyOverrides</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.generativemodelsexperiences.safetyinferenceprovider</string>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 Space.metallib

> `/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/Space.metallib`

- No entitlements *(yet)*
### PasscodeAndBiometricsSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasscodeAndBiometricsSettingsAppIntentsExtension.appex/PasscodeAndBiometricsSettingsAppIntentsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
 </dict>

```
### SIDInferenceProvider

> `/System/Library/ExtensionKit/Extensions/SIDInferenceProvider.appex/SIDInferenceProvider`

```diff

 <dict>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.servicesintelligenced</string>

```

### 🆕 ScreenshotServicesAppIntents

> `/System/Library/ExtensionKit/Extensions/ScreenshotServicesAppIntents.appex/ScreenshotServicesAppIntents`

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
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 		<string>com.apple.accessory.Hearing</string>
 		<string>com.apple.private.health.cardio-fitness</string>
 		<string>com.apple.HealthKit.SensitiveLogsTemporaryEnablement</string>
+		<string>com.apple.nanolifestyle.sessiontrackerapp</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 HomeKitCustomerDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitCustomerDiagnosticExtension.appex/HomeKitCustomerDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support</string>
	</array>
</dict>
</plist>

```
### Illustrator_Preview

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/Illustrator_Preview.appex/Illustrator_Preview`

```diff

 		<string>com.apple.MobileAsset.DictionaryServices.dictionary2</string>
 		<string>com.apple.MobileAsset.Font6</string>
 		<string>com.apple.MobileAsset.Font7</string>
+		<string>com.apple.MobileAsset.Font8</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### com.apple.PDFKit.OFD_Preview

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Preview.appex/com.apple.PDFKit.OFD_Preview`

```diff

 		<string>com.apple.MobileAsset.DictionaryServices.dictionary2</string>
 		<string>com.apple.MobileAsset.Font6</string>
 		<string>com.apple.MobileAsset.Font7</string>
+		<string>com.apple.MobileAsset.Font8</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### com.apple.PDFKit.OFD_Thumbnail

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Thumbnail.appex/com.apple.PDFKit.OFD_Thumbnail`

```diff

 		<string>com.apple.MobileAsset.DictionaryServices.dictionary2</string>
 		<string>com.apple.MobileAsset.Font6</string>
 		<string>com.apple.MobileAsset.Font7</string>
+		<string>com.apple.MobileAsset.Font8</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```

### 🆕 VPNPreferences

> `/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences`

- No entitlements *(yet)*
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>

```

### 🆕 BWVideoPIPOverlayNodeCoreImageArchive_bin.metallib

> `/System/Library/PrivateFrameworks/CMCapture.framework/BWVideoPIPOverlayNodeCoreImageArchive_bin.metallib`

- No entitlements *(yet)*
### callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>

 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.speech.localspeechrecognition</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.xpc-service-name</key>
 	<array>

```
### cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
-	<key>com.apple.private.cloudkit.temporary.deviceCapabilities</key>
-	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>

```

### 🆕 CoreMLSegmenter

> `/System/Library/PrivateFrameworks/CoreMLOdie.framework/XPCServices/CoreMLSegmenter.xpc/CoreMLSegmenter`

- No entitlements *(yet)*

### 🆕 E5MLCompiler

> `/System/Library/PrivateFrameworks/CoreMLOdie.framework/XPCServices/E5MLCompiler.xpc/E5MLCompiler`

- No entitlements *(yet)*
### CorePrescriptionService

> `/System/Library/PrivateFrameworks/CorePrescription.framework/XPCServices/CorePrescriptionService.xpc/CorePrescriptionService`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.managedassets.api.deleteall</key>
+	<true/>
 	<key>com.apple.managedassets.api.kvstore.create</key>
 	<array>
 		<string>coreRXNominalGroup/nominalCalibrationData</string>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<array>
 		<string>access-calls</string>
 		<string>access-call-providers</string>
+		<string>register-gft-service</string>
 	</array>
 	<key>com.apple.trial.client</key>
 	<array>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 				<string>App.InFocus</string>
 			</array>
 		</dict>
+		<key>SmartRepliesFilter</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>CarPlay.Connected</string>
+			</array>
+		</dict>
 		<key>com.apple.personalizationportrait.TextUnderstandingObserver</key>
 		<dict>
 			<key>Streams</key>

```
### DeviceDataResetXPCServiceWorker

> `/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/XPCServices/DeviceDataResetXPCServiceWorker.xpc/DeviceDataResetXPCServiceWorker`

```diff

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.rapport</key>
+	<true/>
+	<key>com.apple.rapport.Client</key>
+	<true/>
+	<key>com.apple.rapport.RegenerateIdentity</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.rapport</string>
 	</array>
 	<key>com.apple.security.exception.mobile-preferences-read-write</key>
 	<array>

```
### FAFollowupExtension

> `/System/Library/PrivateFrameworks/FamilyCircleUI.framework/PlugIns/FAFollowupExtension.appex/FAFollowupExtension`

```diff

 	<string>com.apple.family.FAFollowupExtension</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.family.ageRange</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### fileindexerd

> `/System/Library/PrivateFrameworks/FileIndexerDaemon.framework/Support/fileindexerd`

```diff

 	<true/>
 	<key>com.apple.private.vfs.authorized-access</key>
 	<true/>
+	<key>com.apple.private.vfs.open-by-id</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.FileProvider.LocalStorage</string>

```
### FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
-	<key>com.apple.icloud.searchparty.beaconManager.repairdeviceaccess</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
-	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeExperiences.FailureTracking</string>
+		<string>AppleIntelligence.Reporting.SafetyGuardrails</string>
 	</array>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 <dict>
 	<key>com.apple.timed</key>
 	<true/>
+	<key>com.apple.trustkit.debug.ui</key>
+	<true/>
 	<key>com.apple.proactive.experiments.responses</key>
 	<true/>
 	<key>com.apple.TextUnderstanding.SmartReplies.Inference</key>

```
### intentrecommendd

> `/System/Library/PrivateFrameworks/IntentRecommendRuntime.framework/intentrecommendd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.aeroml.intentrecommend.intentrecommendd</string>
+		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>409835401</string>
 	<key>application-identifier</key>
 	<string>com.apple.backgroundassets.managed.helper.service</string>
 	<key>com.apple.appstored.private</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.backgroundassets.managed.helper.fetching.service</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.xpc.amsaccountsd</string>

 	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 Managed Background Assets Helper Fetching Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssetsHelper.framework/XPCServices/Managed Background Assets Helper Fetching Service.xpc/Managed Background Assets Helper Fetching Service`

- No entitlements *(yet)*
### NFUIService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService`

```diff

 	<true/>
 	<key>com.apple.sharing.Client</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### NewsScoringService

> `/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/NewsScoringService.xpc/NewsScoringService`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.newsd</string>
+		<string>group.com.apple.stocks</string>
 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.newsd</string>
+		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 	<true/>
 	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.notificationcenter-system</key>
 	<array>
 		<dict>

```
### servicesintelligenced

> `/System/Library/PrivateFrameworks/ServicesIntelligence.framework/servicesintelligenced`

```diff

 <dict>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### sleepd

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd`

```diff

 	<array>
 		<string>com.apple.sleep.sleep-mode</string>
 	</array>
+	<key>com.apple.private.health.orchestration.access</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>

 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.proactive.SuggestedPages</string>
+		<string>com.apple.healthappd.orchestration</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.inboxupdaterd</string>
 		<string>com.apple.springboard.blockableservices</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.mobileasset.autoasset</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.backboardd.launchapplications</key>
 	<true/>
 	<key>com.apple.backboardd.proximityDetection</key>

```
### vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.assistant</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.persistentconnection-mcc</string>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
 		<string>/Library/Shortcuts/QuarantineAsset/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.WorkflowKit.BackgroundShortcutRunner</string>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>cellular-plan</string>

 	<true/>
 	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>BackgroundShortcutRunner</string>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.announce/</string>
+		<string>/Library/CallHistoryDB/</string>
 		<string>/Library/Cookies/</string>
 		<string>/Library/HTTPStorages/</string>
 		<string>/Library/WebKit/com.apple.WorkflowKit.BackgroundShortcutRunner/</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.CARenderServer</string>
+		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MapKit.SnapshotService</string>
 		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.contactsd</string>
+		<string>com.apple.contactsd.support</string>
 		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>
 		<string>com.apple.coremedia.routediscoverer.xpc</string>

```
### bird

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/bird`

```diff

 		<string>performModifyWebSharingOperation:withBlock:</string>
 		<string>getNewWebSharingIdentity:</string>
 	</array>
-	<key>com.apple.private.cloudkit.temporary.deviceCapabilities</key>
-	<true/>
 	<key>com.apple.private.cloudkit.usePublicAPSToken</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.itunescloudd</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.atc.private</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 	<true/>
 	<key>com.apple.developer.networking.multipath</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
+	<key>com.apple.locationd.usage_oracle</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.networkd.set_source_application</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.cfnetwork.har-capture-amp</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 	<array>
 		<string>com.apple.Music</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.aps.itunescloudd</string>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```

### 🆕 com.apple.osintelligence.notifications

> `/System/Library/UserNotifications/Bundles/com.apple.osintelligence.notifications.bundle/com.apple.osintelligence.notifications`

- No entitlements *(yet)*
### Books

> `/private/var/staged_system_apps/Books.app/Books`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
-	<key>com.apple.private.contactsui.channel-in-process-override</key>
-	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
 	<true/>
-	<key>com.apple.icloud.FindMyDevice.RepairDevice.access</key>
-	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.FitnessIntelligence.VoiceAssetCache</string>
+		<string>com.apple.FitnessIntelligence.VoiceAssetSettings</string>
 		<string>com.apple.FitnessIntelligence</string>
 		<string>com.apple.fitnessplus</string>
 		<string>com.apple.nanolifestyle</string>

```
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 	<true/>
 	<key>com.apple.private.metadata.exattrs</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.shortcuts.IntentsAvailableDuringBuddy</key>

 	<array>
 		<string>group.com.apple.freeform</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Logs/AppAnalytics/</string>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.swc.additional-service-details-consumer</key>
+	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 		<string>com.apple.journal.xpc</string>
 		<string>com.apple.LinkPresentation.LinkSnapshotGeneratorService</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.stickers.recency</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.stickers.recency</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.MagnifierAngel.client</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/MagnifierSupport.framework</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.accessibility.MagnifierAngel.mach</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>CloudDocuments</string>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.networking.carrier-constrained.app-optimized</key>
+	<true/>
+	<key>com.apple.developer.networking.carrier-constrained.appcategory</key>
+	<string>messaging-8001</string>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.lightsourcesupport.listener</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lightsourcesupport.lightstate</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.surfboard.applicationservice</string>
 		<string>com.apple.biome.access.user</string>

```
### MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.lightsourcesupport.listener</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lightsourcesupport.lightstate</string>
 		<string>com.apple.dmd.emergency-mode</string>
 		<string>com.apple.dmd.policy</string>
 		<string>com.apple.ScreenTimeAgent</string>

```
### MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.lightsourcesupport.listener</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lightsourcesupport.lightstate</string>
 		<string>com.apple.dmd.emergency-mode</string>
 		<string>com.apple.dmd.policy</string>
 		<string>com.apple.ScreenTimeAgent</string>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
-	<key>com.apple.private.fpsd.client</key>
-	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Caches/com.apple.businessservicesd/</string>
+		<string>/Library/DeviceRegistry/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### RemindersSharingExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

```
### Reminders

> `/private/var/staged_system_apps/Reminders.app/Reminders`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

```
### SequoiaTranslator

> `/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.hid.system.user-access-service</key>
 	<true/>
 	<key>com.apple.locationd.asmanager</key>

 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.AudioAccessoryAssetManagementXPCService</string>
 		<string>com.apple.feedbackd.xpc</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 	<string>production</string>
 	<key>com.apple.MobileAsset.SearchAds.AppVector</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 	<true/>
 	<key>com.apple.airplay.receiver.agent.allow</key>
 	<true/>
+	<key>com.apple.airplay.receiver.mediaremote.agent.services.allow</key>
+	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-set-output-device</key>

 		<string>com.apple.accessories.transport-server</string>
 		<string>com.apple.airplay.agent.services</string>
 		<string>com.apple.airplay.receiver.agent</string>
+		<string>com.apple.airplay.receiver.mediaremote.agent.services</string>
 		<string>com.apple.analyticsd</string>
 		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.audio.AudioComponentRegistrar</string>

```
### asktod

> `/usr/libexec/asktod`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.asktod/</string>
+		<string>/Library/Caches/com.apple.asktod/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.gasgauge.user-access-device</key>
 	<true/>
+	<key>com.apple.hid.heartrate-access</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-custom-queue-size</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>

 	<true/>
 	<key>com.apple.private.xpc.launchd.app-server</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.reboot</key>
+	<true/>
 	<key>com.apple.runningboard.primitiveattribute</key>
 	<true/>
 	<key>com.apple.runningboard.terminatemanagedprocesses</key>

```
### carkitd

> `/usr/libexec/carkitd`

```diff

 		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.sysdiagnose.service.xpc</string>
 		<string>com.apple.carkit.sessionBoost.service</string>
+		<string>com.apple.iap2d.xpc</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### coreidvd

> `/usr/libexec/coreidvd`

```diff

 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
-		<string>com.apple.coreidv.service-messages</string>
 		<string>com.apple.coreidv.idv-data</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>

 	<dict>
 		<key>com.apple.coreidv.idv-data</key>
 		<string>com.apple.coreidv.idv-data</string>
-		<key>com.apple.coreidv.server-messages</key>
-		<string>com.apple.coreidv.service-messages</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>

```
### demod

> `/usr/libexec/demod`

```diff

 		<string>com.apple.mobilestoredemod</string>
 		<string>appleaccount</string>
 		<string>com.apple.bluetooth</string>
+		<string>com.apple.rapport</string>
+		<string>com.apple.continuity.encryption</string>
 	</array>
 </dict>
 </plist>

```
### diagnosticextensionsd

> `/usr/libexec/diagnosticextensionsd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/preferences/com.apple.networkextension.control.plist</string>
+		<string>/private/preboot/Cryptexes/System/Library/Diagnostics/DiagnosticsEncryptionPublicKey</string>
+		<string>/private/var/RPSupport/System/Library/Diagnostics/DiagnosticsEncryptionPublicKey</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
-	<key>com.apple.frontboard.launchapplications</key>
-	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceBTDiscoveryXPCService.access</key>
 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceEraseXPCService.access</key>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
-	<key>com.apple.springboard.remote-alert</key>
-	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.wifi.manager-access</key>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 		<string>com.apple.inputAnalytics.IASSRAnalyzer</string>
 		<string>com.apple.inputAnalytics.IASGenmojiAnalyzer</string>
 		<string>com.apple.inputAnalytics.IASGenmojiUsageAnalyzer</string>
+		<string>com.apple.inputAnalytics.IASImageGenerationCreationAnalyzer</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>

```
### languageassetd

> `/usr/libexec/languageassetd`

```diff

 	<string>com.apple.languageassetd</string>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.DictionaryServices.dictionary3iOS</string>
 		<string>com.apple.MobileAsset.DictionaryServices.dictionary2</string>
+		<string>com.apple.MobileAsset.Font8</string>
+		<string>com.apple.MobileAsset.Font7</string>
 		<string>com.apple.MobileAsset.Font6</string>
 		<string>com.apple.MobileAsset.Font5</string>
 		<string>com.apple.MobileAsset.Font4</string>

```
### mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

 	<true/>
 	<key>com.apple.private.applesepmanager.allow</key>
 	<true/>
+	<key>com.apple.private.erm.preboot</key>
+	<true/>
 	<key>com.apple.private.findmymac.locking</key>
 	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>

```
### mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 	<true/>
 	<key>com.apple.private.security.bootpolicy</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.corerepair</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.Preferences</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.corerepair</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleMobileApNonceUserClient</string>

```
### nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.nesessionmanager.url-filter-fail-closed</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.nesessionmanager.url-prefilter-ready</key>
+	<true/>
 	<key>com.apple.private.neagent-client</key>
 	<true/>
 	<key>com.apple.private.necp.match</key>

```
### ospredictiond

> `/usr/libexec/ospredictiond`

```diff

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.osintelligence.inactivity.notifications</string>
+		<string>com.apple.osintelligence.notifications</string>
 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>

```
### remindd

> `/usr/libexec/remindd`

```diff

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/db/com.apple.naturallanguaged/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array/>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.locationd.harvest.contribute</key>
 	<true/>
+	<key>com.apple.locationd.natalimetry</key>
+	<true/>
 	<key>com.apple.locationd.private_info</key>
 	<true/>
 	<key>com.apple.locationd.routine</key>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-calls</string>
+		<string>access-call-capabilities</string>
+	</array>
 	<key>com.apple.timed</key>
 	<true/>
 	<key>com.apple.wifi.manager-access</key>

```
### securityd

> `/usr/libexec/securityd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.SFAnalytics</key>
 	<true/>
+	<key>com.apple.private.securityd.get-derived-entropy</key>
+	<true/>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### securityresearchdevice-init

> `/usr/libexec/securityresearchdevice-init`

```diff

 	<true/>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.erm.nvram</key>
+	<true/>
 	<key>com.apple.private.img4.nonce.cryptex1.generic.erm</key>
 	<true/>
 	<key>com.apple.private.security-research-device</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.Accessibility</string>
 		<string>com.apple.appletvservices</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.AppleMediaServices</string>

```
### swtransparencyd

> `/usr/libexec/swtransparencyd`

```diff

 	<array>
 		<string>group.com.apple.swtransparency</string>
 	</array>
+	<key>com.apple.private.security.storage.SFAnalytics</key>
+	<true/>
 	<key>com.apple.privatecloudcompute.serverEnvironment</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	<true/>
 	<key>com.apple.intelligenceplatform.Sysdiagnose</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.profile</key>
+	<true/>
 	<key>com.apple.nearbyd.diagnostics</key>
 	<true/>
 	<key>com.apple.networkrelay.diagnostic</key>

 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
+	<key>com.apple.private.managedclient.configurationprofiles</key>
+	<true/>
 	<key>com.apple.private.notificationcenter-system</key>
 	<array>
 		<dict>

 	<array>
 		<string>systemgroup.com.apple.powerlog</string>
 		<string>systemgroup.com.apple.ReportMemoryException</string>
+		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
 	<key>com.apple.springboard.statedump</key>
 	<true/>

```
### terminusd

> `/usr/libexec/terminusd`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.countrycode</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.networkrelay.endpointcache</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.networkrelay.launch</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.networkrelay.referencesChanged</key>
+	<true/>
 	<key>com.apple.private.ids.continuity</key>
 	<true/>
 	<key>com.apple.private.ids.localpairing-api</key>

```
### textcomposerd

> `/usr/libexec/textcomposerd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.textcomposerd</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.TextUnderstanding.SmartReplies.Inference</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### textunderstandingd

> `/usr/libexec/textunderstandingd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.textunderstandingd</string>
-	<key>com.apple.TapToRadarKit.service-access</key>
-	<true/>
 	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-read</key>

 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>
 	<true/>
+	<key>com.apple.finance.private</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 			<dict>
 				<key>App.InFocus</key>
 				<dict/>
+				<key>App.Intent</key>
+				<dict/>
 				<key>AppLaunch</key>
 				<dict/>
 				<key>Device.Wireless.Bluetooth</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict/>
 				<key>UserFocusComputedMode</key>
 				<dict/>
 			</dict>

```
### videosubscriptionsd

> `/usr/libexec/videosubscriptionsd`

```diff

 	<array>
 		<string>SerialNumber</string>
 		<string>UserAssignedDeviceName</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 		<string>com.apple.icloud.searchpartyd</string>
 		<string>com.apple.da</string>
 		<string>com.apple.carplay</string>
+		<string>com.apple.corecapture.configure.bt</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>systemgroup.com.apple.osanalytics</string>
 		<string>systemgroup.com.apple.managedsettings</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/Managed Preferences/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>IOUserUserClient</string>

```
