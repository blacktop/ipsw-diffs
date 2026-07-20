## 🔑 Entitlements

### filesystem

### AAUIViewService

> `/Applications/AAUIViewService.app/AAUIViewService`

```diff

 	</dict>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
 	<key>com.apple.keystore.device</key>

```
### AccessorySetupUI

> `/Applications/AccessorySetupUI.app/AccessorySetupUI`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
 	<key>com.apple.bluetooth.settings</key>

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ProductKitService</string>
 		<string>com.apple.SharingServices</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AuthenticationServicesUI

> `/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

```
### Campo

> `/Applications/Campo.app/Campo`

```diff

 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/preferences/FeatureFlags/</string>
 		<string>/Library/Audio/Tunings/</string>

 		<string>/Library/com.apple.ManagedSettings/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
+		<string>/Library/Caches/com.apple.countryd/</string>
 		<string>/Library/Caches/com.apple.keyboards/</string>
 		<string>/Library/Caches/GeoServices/</string>
 		<string>/Library/WebClips/</string>

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 		<dict>
 			<key>bleRSSIThresholdHint</key>
 			<integer>-48</integer>
-			<key>companionSetupFilters</key>
-			<array>
-				<dict>
-					<key>rssi</key>
-					<integer>-45</integer>
-				</dict>
-			</array>
 			<key>discoveryTypes</key>
 			<array>
 				<string>CompanionSetup</string>

```
### Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

```diff

 	<true/>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
+	<key>com.apple.developer.avfoundation.multitasking-camera-access</key>
+	<true/>
 	<key>com.apple.private.exclaves.kernel-domain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```

### 🆕 Diagnostic-6027

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6027.appex/Diagnostic-6027`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/accessoryupdater/uarpd/sysdiagnose/assets/metrics/</string>
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
### InputUI

> `/Applications/InputUI.app/InputUI`

```diff

 	<true/>
 	<key>com.apple.backboardd.layerTransformLookup</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.generativeexperiences.textcomposition</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
 	<key>com.apple.payment.fpan-card</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.CallerName</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerPID</key>
 	<true/>
 	<key>com.apple.private.SafariServices.PasswordPicker.directlyReceiveCredentials</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
+	</array>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<array>
 		<string>group.com.apple.SuggestedImage.SharedSecureContainer</string>
 	</array>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.stickers</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Audio/Tunings/Generic/Haptics/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/mobile/Library/Application Support/com.apple.VisualGeneration/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.passd.account</string>
 		<string>com.apple.imageplaygroundd.onDemandImageRequesterService</string>
 		<string>com.apple.stickers.api</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.local-name</key>
 	<array>

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.EmojiPreferences</string>
+		<string>com.apple.gms.availability</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.keyboard.preferences</string>
 		<string>com.apple.keyboard</string>
 		<string>com.apple.PencilKit</string>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	</array>
 	<key>com.apple.sharesheet.recipients</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 		<string>analysis-history-read</string>
 		<string>analysis-history-write</string>
 	</array>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.suggestions.events</key>

```
### NewDeviceSetupUIService

> `/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService`

```diff

 	</dict>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
-		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.passd.discovery</string>
 		<string>com.apple.passd.search</string>
 		<string>com.apple.seserviced.kmlXpcService</string>

```
### PhotosUIService

> `/Applications/PhotosUIService.app/PhotosUIService`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.communicationSafetySettings</string>
+		<string>com.apple.mobileslideshow</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.private.AppleProcessorTrace.CarveoutProperty</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read-write</key>
+	<true/>
 	<key>com.apple.private.CarPlayServices.icon-layout</key>
 	<true/>
 	<key>com.apple.private.ClassKit.dashboard</key>

 	</array>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
 	<key>com.apple.private.security.storage.DiagnosticReports.read-only</key>
 	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>

```
### ScreenTimeSettingsShield

> `/Applications/ScreenTimeSettingsShield.app/ScreenTimeSettingsShield`

```diff

 <dict>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.backboardd</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.mobileslideshow</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.systemNotesPresentation</key>
 	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-call-capabilities</string>
+		<string>access-call-providers</string>
+		<string>access-calls</string>
+	</array>
 	<key>com.apple.visualintelligence.private.visual-action-prediction</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### ServicesPaymentAngel

> `/Applications/ServicesPaymentAngel.app/ServicesPaymentAngel`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.payment.externalized-context</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.ServicesPaymentAngel</string>
-		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.PassbookUISceneService.remote-ui</string>
+		<string>com.apple.ServicesPaymentAngel</string>
 		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.jetpackassetd.xpc</string>
+		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
+	<key>com.apple.springboard.biometricUnlockSuppression</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x</string>
 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPad</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
-		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

```
### SupportFlow

> `/Applications/SupportFlow.app/SupportFlow`

```diff

 	<key>com.apple.private.networkextension.configuration</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceFaceID</string>
-	</array>
-	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.tipsd.supportFlowApp</key>
 	<true/>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	</array>
 	<key>com.apple.private.mediaexperience.relativevoiceovervolume.allow</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.setsilentmode.allow</key>
+	<true/>
 	<key>com.apple.private.sociallayer.accessibility</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
+		<string>com.apple.mediaexperience.endpoint.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.gamepolicyd.app.privileged</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
+	<key>com.apple.accessibility.axassets</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

 	</dict>
 	<key>com.apple.private.iokit.battery-gauging-mitigation</key>
 	<true/>
+	<key>com.apple.private.iokit.battery-shipping-charge-limit</key>
+	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.iokit.batteryhealthstate</key>

```
### scrod

> `/System/Library/CoreServices/VoiceOverTouch.app/scrod`

```diff

 	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-privileged</key>
+	<true/>
 	<key>com.apple.hid.system.user-access-service</key>
 	<true/>
 	<key>com.apple.hid.transport.user-access</key>

```
### settings

> `/System/Library/DataClassMigrators/PreferencesMigrator.migrator/settings`

```diff

 	<string>*</string>
 	<key>com.apple.private.linkd.observationStatusRegistry</key>
 	<true/>
+	<key>com.apple.private.settings-search-reindex</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

```
### BiomeSELFIngestor

> `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor`

```diff

 		<dict>
 			<key>Streams</key>
 			<array>
-				<string>IntelligenceFlow.Transcript.Datastream</string>
 				<string>IntelligenceFlow.Experimentation</string>
 				<string>IntelligenceFlow.JointResolverTelemetry</string>
 				<string>IntelligenceFlow.PlanResolutionTelemetry</string>

```
### ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension`

```diff

 		<string>com.apple.xpc.amstoold</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
 	</array>
-	<key>com.apple.security.iokit-user-client-class</key>
-	<string>com_apple_driver_FairPlayIOKitUserClient</string>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/FedStatsPluginDynamic`

```diff

 		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
 		<string>HKQuantityTypeIdentifierStepCount</string>
 		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
+		<string>HKCharacteristicTypeIdentifierFitzpatrickSkinType</string>
+		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
 		<string>HKQuantityTypeIdentifierVO2Max</string>
+		<string>HKQuantityTypeIdentifierAppleExerciseTime</string>
 		<string>HKActivitySummaryTypeIdentifier</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Pcc-Recitation-Block-Rate</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>PrivateMLClient.RecitationMetrics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Pegasus-Partial-URLs</key>
 		<dict>
 			<key>Streams</key>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/FedStatsPluginStatic`

```diff

 		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
 		<string>HKQuantityTypeIdentifierStepCount</string>
 		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
+		<string>HKCharacteristicTypeIdentifierFitzpatrickSkinType</string>
+		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
 		<string>HKQuantityTypeIdentifierVO2Max</string>
+		<string>HKQuantityTypeIdentifierAppleExerciseTime</string>
 		<string>HKActivitySummaryTypeIdentifier</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Pcc-Recitation-Block-Rate</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>PrivateMLClient.RecitationMetrics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Pegasus-Partial-URLs</key>
 		<dict>
 			<key>Streams</key>

```
### IntelligencePlatformDataActionsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/IntelligencePlatformDataActionsAppIntentsExtension.appex/IntelligencePlatformDataActionsAppIntentsExtension`

```diff

 		<string>App.InFocus</string>
 		<string>Media.NowPlaying</string>
 		<string>ScreenTime.AppUsage</string>
+		<string>Intelligence.Usage</string>
 		<string>Device.Display.Backlight</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### OBCEngagePlugin

> `/System/Library/ExtensionKit/Extensions/OBCEngagePlugin.appex/OBCEngagePlugin`

```diff

 	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>Location.Semantic</string>
 		<string>Location.MicroLocationVisit</string>
 		<string>Location.Visit</string>
 		<string>Location.SignificantLocation</string>

 		<dict>
 			<key>Streams</key>
 			<array>
+				<string>Location.Semantic</string>
 				<string>Location.MicroLocationVisit</string>
 				<string>Location.Visit</string>
 				<string>Location.SignificantLocation</string>

```
### ODDFeatureDigestsExtension

> `/System/Library/ExtensionKit/Extensions/ODDFeatureDigestsExtension.appex/ODDFeatureDigestsExtension`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
+		<string>Siri.ODDI.ODDAssistantLLMSiriDigests</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

```

### 🆕 PSECollectionExtension

> `/System/Library/ExtensionKit/Extensions/PSECollectionExtension.appex/PSECollectionExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.lighthouse.PSECollectionExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.coreduetd.knowledge</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.lighthouse.PSECollectionExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Photos.Engagement</string>
		<string>Photos.Edit</string>
		<string>Photos.Search</string>
		<string>Photos.Favorite</string>
		<string>Photos.Share</string>
		<string>Photos.Picker</string>
		<string>Photos.Delete</string>
		<string>Photos.Memories.Viewed</string>
		<string>Photos.Memories.Shared</string>
		<string>IntelligenceFlow.Transcript.Datastream</string>
		<string>App.Install</string>
		<string>App.Intent</string>
		<string>Siri.UI</string>
		<string>Media.NowPlaying</string>
		<string>Notification</string>
		<string>Clock.Alarm</string>
		<string>App.InFocus</string>
		<string>App.Intents.Transcript</string>
		<string>Siri.Execution</string>
		<string>HomeKit.Client.AccessoryControl</string>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Siri.PostSiriEngagement</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.coreservices.cangetcurrentactivityinfo</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>LighthouseInference</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>IntelligenceFlow.Transcript.Datastream</string>
			</array>
		</dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Lighthouse.Ledger.TaskCustomEvent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.security.no-sandbox</key>
	<true/>
	<key>com.apple.private.security.storage.CoreKnowledge</key>
	<true/>
	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
	<true/>
	<key>com.apple.rootless.storage.coreknowledge</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/var/mobile/Library/com.apple.internal.ck/</string>
		<string>/private/var/mobile/Library/Logs/com.apple.FeatureStore/biomeStream/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Logs/com.apple.FeatureStore/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.PublicStreamAccessService</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.biome.PublicStreamAccessService</string>
		<string>com.apple.siriknowledged</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.coreduetd.context</string>
		<string>com.apple.coreduetd</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.coreduetd.people</string>
		<string>com.apple.analyticsd</string>
	</array>
	<key>com.apple.siriknowledged</key>
	<true/>
</dict>
</plist>

```
### PhotosAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PhotosAppIntentsExtension.appex/PhotosAppIntentsExtension`

```diff

 <dict>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+	</array>
 </dict>
 </plist>
 

```
### PhotosFileProvider

> `/System/Library/ExtensionKit/Extensions/PhotosFileProvider.appex/PhotosFileProvider`

```diff

 		<string>/Containers/</string>
 		<string>/Media/</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+	</array>
 </dict>
 </plist>
 

```
### PhotosMessagesApp

> `/System/Library/ExtensionKit/Extensions/PhotosMessagesApp.appex/PhotosMessagesApp`

```diff

 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.mediaanalysisd.embeddingstore</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.communicationSafetySettings</string>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<array>
 		<string>systemgroup.com.apple.VideoSubscriberAccount</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.pisco.suinfo</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.symptom_analytics.query</key>

```
### SafariUsageRetentionExtension

> `/System/Library/ExtensionKit/Extensions/SafariUsageRetentionExtension.appex/SafariUsageRetentionExtension`

```diff

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>Unilog.SafariSearch.Stage</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>UnilogInstrumentation.IdentifierProvider</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
 				<key>Unilog.SafariSearch.LongTermAggregationId</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>Unilog.SafariSearch.Stage</key>
+			</dict>
+		</dict>
+		<key>com.apple.aiml.unilog.healthTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Unilog.HealthTelemetry</key>
 				<dict>
 					<key>mode</key>
-					<string>read-only</string>
+					<string>read-write</string>
 				</dict>
 			</dict>
 		</dict>

```
### ScreenTimeAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.usage-tracking</key>

 		<string>com.apple.UsageTrackingAgent.private</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
-		<string>com.apple.MobileAsset.UAF.Siri.AnswerSynthesis</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>

 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_AnswerSynthesis/purpose_auto/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>UAF_AB_ANSWER_SYNTHESIS</string>
-		<string>SEARCH_TOOL_ANSWER_SYNTHESIS</string>
 		<string>337</string>
 		<string>755</string>
 	</array>

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.siri.inference</string>
 		<string>group.com.apple.siri.sirisuggestions</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<array>
 		<string>systemgroup.com.apple.VideoSubscriberAccount</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.pisco.suinfo</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.symptom_analytics.query</key>

```
### TGOnDeviceInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/TGOnDeviceInferenceProviderService.appex/TGOnDeviceInferenceProviderService`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
+		<string>com.apple.MobileAsset.UAF.Translation.MMAssets</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.tgondeviceinferenceproviderservice</string>

```

### 🆕 TVRemoteSettingsAppIntents

> `/System/Library/ExtensionKit/Extensions/TVRemoteSettingsAppIntents.appex/TVRemoteSettingsAppIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 TrackpadAndMouseSettingsIntents

> `/System/Library/ExtensionKit/Extensions/TrackpadAndMouseSettingsIntents.appex/TrackpadAndMouseSettingsIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.UIKit</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
</dict>
</plist>

```
### contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.contacts.provider-host</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```

### 🆕 CardioFitnessDiagnostic

> `/System/Library/Frameworks/CoreMotion.framework/PlugIns/CardioFitnessDiagnostic.appex/CardioFitnessDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.locationd.cardiohealthdata-read</key>
	<true/>
</dict>
</plist>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.cascade.donation-requester</key>
+	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

```
### CommCenterMobileHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper`

```diff

 		<string>Library/HTTPStorages/com.apple.commcentermobilehelper/</string>
 		<string>Library/Preferences/com.apple.lasd.plist</string>
 		<string>Library/Preferences/com.apple.commcenter.shared.plist</string>
+		<string>Library/Preferences/com.apple.CommCenter.plist</string>
 		<string>Library/CallHistoryDB/</string>
 		<string>Library/LASD/</string>
 		<string>Library/Logs/CrashReporter/</string>

 	<array>
 		<string>com.apple.commcentermobilehelper</string>
 		<string>com.apple.commcenter.shared</string>
+		<string>com.apple.CommCenter</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.lasd</string>
 		<string>com.apple.mms_override</string>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
 	<array>
 		<string>com.apple.pay.finance.development</string>
-		<string>com.apple.pay.finance.dropbox.development</string>
 	</array>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.pay.finance</string>
-		<string>com.apple.pay.finance.dropbox</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.fitnesscoachingd</key>
 	<true/>
+	<key>com.apple.fitnessintelligenced</key>
+	<true/>
 	<key>com.apple.frontboard.app-badge-value-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.fitnesscoachingd</string>
+		<string>com.apple.fitnessintelligenced</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.health.RemoteHeartRateStreamService</string>
 		<string>com.apple.healthrecordsd</string>

```
### coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.securestore.upp.config.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.thumbandpay.allow</key>
+	<true/>
 	<key>com.apple.private.biometrickit.allow-connect</key>
 	<true/>
 	<key>com.apple.private.biometrickit.allow-match</key>

```
### MediaPlayerDiagnosticExtension

> `/System/Library/Frameworks/MediaPlayer.framework/PlugIns/MediaPlayerDiagnosticExtension.appex/MediaPlayerDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.musicd</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/MediaServices/</string>

```
### SpeechEncryptedLogsDiagnostic

> `/System/Library/Frameworks/Speech.framework/PlugIns/SpeechEncryptedLogsDiagnostic.appex/SpeechEncryptedLogsDiagnostic`

```diff

 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/</string>

```

### 🆕 NanoControlCenterBridgeSettings

> `/System/Library/NanoPreferenceBundles/General/NanoControlCenterBridgeSettings.bundle/NanoControlCenterBridgeSettings`

- No entitlements *(yet)*

### 🆕 SiriComplication

> `/System/Library/NanoTimeKit/ComplicationBundles/SiriComplication.bundle/SiriComplication`

- No entitlements *(yet)*
### AAUIFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 		<string>/Library/Caches/com.apple.amsaccountsd/</string>
 		<string>/Library/HTTPStorages/com.apple.amsaccountsd/</string>
 		<string>/Library/com.apple.AppleMediaServices/</string>
+		<string>/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.amsaccountsd/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
+	<key>com.apple.private.corewifi.readonly</key>
+	<true/>
 	<key>com.apple.private.domain-extension</key>
 	<true/>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.recovery</key>
+	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
 	<key>com.apple.cdp.walrus</key>

```
### AKFollowUpExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.writer.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>

```
### bookdatastored

> `/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored`

```diff

 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.symptom_analytics</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

```diff

 		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.backupd</string>
 		<string>com.apple.symptom_analytics</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.aggregated.addaily</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.iohideventsystem</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### CDPFollowUpExtension

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.recovery</key>
+	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.telemetry</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### speechmaintenanced

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/speechmaintenanced`

```diff

 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### followupd

> `/System/Library/PrivateFrameworks/CoreFollowUp.framework/followupd`

```diff

 		<string>com.apple.iCloud.FollowUp</string>
 		<string>com.apple.NDO.FollowUp</string>
 		<string>com.apple.ThreatNotification.FollowUp</string>
+		<string>com.apple.Siri.FollowUp</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.AudioAccessorySystemStateService</key>
 	<true/>
+	<key>com.apple.CompanionLink</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.account.AppleAccount</key>

 	<true/>
 	<key>com.apple.corespeech.cat.xpc</key>
 	<true/>
+	<key>com.apple.developer.homekit</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<array>
 		<string>endpoint-read</string>
 	</array>
+	<key>com.apple.private.homekit</key>
+	<true/>
+	<key>com.apple.private.homekit.allow-access-without-prompting</key>
+	<true/>
 	<key>com.apple.private.homekit.siri-audio-connection</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceBluetoothAlways</string>
+		<string>kTCCServiceHomeKit</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Caches/com.apple.HomeKit.configurations</string>
+		<string>/Library/Caches/com.apple.HomeKit</string>
 		<string>/Library/DES/Records/com.apple.siri.speech-dictation-personalization/</string>
 		<string>/Library/VoiceTrigger/</string>
 		<string>/Library/Logs/CrashReporter/Assistant/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.homed.xpc</string>
+		<string>com.apple.CompanionLink</string>
 		<string>com.apple.polaris.cache</string>
 		<string>com.apple.siri.deviceselection</string>
 		<string>com.apple.account.AppleAccount</string>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.accounts.connectbeforemigrationdidfinish</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.appstored.private</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 	<array>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 		<string>kTCCServiceUbiquity</string>
 	</array>
 	<key>com.apple.private.ubiquity-kvstore-access</key>

 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### IMDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/IMDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService`

```diff

 	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.vfs.snapshot</key>
+	<true/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```

### 🆕 ExclavesStats

> `/System/Library/PrivateFrameworks/ExclavesStats.framework/ExclavesStats`

- No entitlements *(yet)*
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled`

```diff

 	<true/>
 	<key>com.apple.authkit.familyDeviceList</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

```
### fileindexerd

> `/System/Library/PrivateFrameworks/FileIndexerDaemon.framework/Support/fileindexerd`

```diff

 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.internal.SpotlightAutomationTester</string>
+		<string>com.apple.revisiond</string>
 	</array>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.skgupdater</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.modelcatalog</string>
+	</array>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer.async</string>
+		<string>com.apple.DeviceConfigurationAgent.publisher</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.frontboard.app-badge-value-access</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
+	<true/>
+	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
+	<true/>
+	<key>com.apple.private.allow-background-haptics</key>
+	<true/>
 	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
 	<array>
 		<string>com.apple.Home</string>

 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.sessionkit.custom-platter-target</key>
+	<true/>
+	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.NetworkInfo.DiagnosticExtension.apple-extension-service</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.ProductKitService</string>
+		<string>com.apple.audio.hapticd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.assistant.backedup</string>
 		<string>HomeKit</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-write</key>
+	<array>
+		<string>kern.memorystatus_vm_pressure_send</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	</array>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.generativeexperiences.agentMediaStore</key>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceScreenCapture</string>
 	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceLiverpool</string>
-		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
-		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceSpeechRecognition</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>
-		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.surfboard.entityinteractionservice</string>
 		<string>com.apple.surfboard.environmentservice</string>

 		<string>1760</string>
 		<string>INTELLIGENCE_FLOW_QUERY_DECORATOR</string>
 		<string>SIRI_SECURITY_IPI</string>
+		<string>SIRI_INTELLIGENCE_FLOW_PLANNER</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### IntelligencePlatformComputeService

> `/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService`

```diff

 	</dict>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
-	<key>com.apple.private.photos.XPCStoreOptIn</key>
-	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.IntelligencePlatform</key>

```
### intelligenceplatformd

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd`

```diff

 		<string>App.MediaUsage</string>
 		<string>Media.NowPlaying</string>
 		<string>ScreenTime.AppUsage</string>
+		<string>Intelligence.Usage</string>
 		<string>WalletPaymentsCommerce.FoundIn.OrderEmail</string>
 		<string>WalletPaymentsCommerce.FoundIn.ClassicOrder</string>
 		<string>WalletPaymentsCommerce.FoundIn.Transaction</string>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 		<string>Device.Display.Backlight</string>
 		<string>Media.NowPlaying</string>
 		<string>ScreenTime.AppUsage</string>
+		<string>Intelligence.Usage</string>
 		<string>WalletPaymentsCommerce.FoundIn.OrderEmail</string>
 		<string>WalletPaymentsCommerce.FoundIn.ClassicOrder</string>
 		<string>WalletPaymentsCommerce.FoundIn.Transaction</string>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>
+		<string>/private/var/mobile/Containers/Data/Application/*/tmp/com.apple.backgroundassets.managed.helper.service/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	<array>
 		<string>com.apple.backgroundassets.managed.helper.fetching.service</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.spaceattributiond</string>
+		<string>com.apple.userprofiles</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fpsd</string>
+	</array>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>
 	<key>com.apple.spaceattribution.private</key>

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```

### 🆕 Managed Background Assets Relay Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Relay Service.xpc/Managed Background Assets Relay Service`

- No entitlements *(yet)*
### destinationd

> `/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd`

```diff

 		<string>com.apple.coremedia</string>
 		<string>com.apple.MapsSuggestions</string>
 		<string>com.apple.mobilecal</string>
+		<string>com.apple.NanoHomeScreen.SmartStackSuggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### nanomapscd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/nanomapscd`

```diff

 	<array>
 		<string>group.com.apple.Maps</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.Maps</string>

```
### navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

 	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
+	<key>com.apple.private.appintents.live-entities.read</key>
+	<true/>
+	<key>com.apple.private.appintents.live-entities.write</key>
+	<array>
+		<string>maps.parkedCar</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appintents.LiveEntityService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.accessories.externalaccessory-server</string>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Bundle/</string>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MigrationKit.resumeBackgroundActivity</key>
 	<true/>
+	<key>com.apple.private.ids.idquery-device-flush</key>
+	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.storage.nandtaskscheduler</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.usermanagerd.persona.background</key>

```
### NFUIService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService`

```diff

 <dict>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
+	<false/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.seserviced.presentment-authorization</string>
+	</array>
+	<key>com.apple.seserviced.presentment-authorization</key>
 	<true/>
 	<key>com.apple.sharing.Client</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/searchtoold`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.omniSearch.searchtoold</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.carousel.notificationservice</key>

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
-		<string>com.apple.MobileAsset.UAF.Siri.AnswerSynthesis</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>

 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_AnswerSynthesis/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>

 		<string>com.apple.mediaanalysisd.embeddingstore</string>
 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.tccd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.managedcorespotlightd</string>
 		<string>com.apple.diagnosticpipeline.service</string>
+		<string>com.apple.tccd</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>UAF_AB_ANSWER_SYNTHESIS</string>
 		<string>337</string>
 		<string>755</string>
 	</array>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.utility</key>
 	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>

```
### PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 		<dict>
 			<key>Sets</key>
 			<dict>
-				<key>Fitness.Guest</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
 				<key>SensedUserContext.Event</key>
 				<dict>
 					<key>mode</key>

```
### privacyaccountingd

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd`

```diff

 	</array>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/PrivacyAccounting/</string>

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

```diff

 	</array>
 	<key>com.apple.private.cloudtelemetry</key>
 	<true/>
+	<key>com.apple.private.container.access</key>
+	<dict>
+		<key>daemon</key>
+		<dict>
+			<key>com.apple.privatecloudcomputed</key>
+			<dict>
+				<key>data</key>
+				<dict>
+					<key>access</key>
+					<string>path-only</string>
+					<key>operations</key>
+					<array>
+						<string>delete</string>
+					</array>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>TransparencyLogging</key>

 	<true/>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SBUserNotification</string>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.settings-search-reindex</key>
+	<true/>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 		<string>com.apple.FamilyControlsAgent.private</string>
 		<string>com.apple.iconservices</string>
 		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.SettingsServices.SearchReindexService</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>

```
### servicesintelligenced

> `/System/Library/PrivateFrameworks/ServicesIntelligence.framework/servicesintelligenced`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.servicesintelligenced</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.servicesintelligenced</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.developer.healthkit.background-delivery</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 		<string>com.apple.ciphermld</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.healthd.server</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 SettingsSearchReindexService

> `/System/Library/PrivateFrameworks/SettingsServices.framework/XPCServices/SettingsSearchReindexService.xpc/SettingsSearchReindexService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SettingsServices.Reindexer</string>
	</array>
</dict>
</plist>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 		<string>/private/var/mobile/Library/Trial/</string>
 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/mobile/models/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	</array>
 	<key>com.apple.private.allow-sucore-helper-service</key>
 	<true/>
+	<key>com.apple.private.allow-susd-helper-service</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.SplatSoftwareUpdate</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.powerd.coresmartpowernap</string>
 		<string>com.apple.tipsd</string>
 		<string>com.apple.inboxupdaterd</string>
 		<string>com.apple.springboard.blockableservices</string>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.healthd.server</string>
 		<string>com.apple.sucore.SUCoreHelperService</string>
+		<string>com.apple.sus.SUDaemonHelperService</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 SUDaemonHelperService

> `/System/Library/PrivateFrameworks/SoftwareUpdateServicesDaemonFramework.framework/XPCServices/SUDaemonHelperService.xpc/SUDaemonHelperService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileSoftwareUpdate/asu_trial/</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>APPLE_SOFTWARE_UPDATE_SUSAU</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### STExtractionService.privileged

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.privileged.xpc/STExtractionService.privileged`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobilegestalt.xpc</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### systemstatusd

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.rootless.critical</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.systemstatusd</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.exception.process-info</key>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.CoreTelephony.CommCenterHelper.allow</key>
 	<true/>
+	<key>com.apple.DeviceAccess.private</key>
+	<true/>
 	<key>com.apple.FTLivePhotoService</key>
 	<array>
 		<string>modify-moments</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.facetimed.service</string>
+		<string>com.apple.DeviceAccess.xpc</string>
 		<string>com.apple.accessibility.voices</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>

```

### 🆕 FollowUp

> `/System/Library/Settings/FollowUp.settings/FollowUp`

- No entitlements *(yet)*

### 🆕 Headphones

> `/System/Library/Settings/Headphones.settings/Headphones`

- No entitlements *(yet)*

### 🆕 TVRemoteSettings

> `/System/Library/Settings/TVRemoteSettings.settings/TVRemoteSettings`

- No entitlements *(yet)*

### 🆕 com.apple.Siri.FollowUp

> `/System/Library/UserNotifications/Bundles/com.apple.Siri.FollowUp.bundle/com.apple.Siri.FollowUp`

- No entitlements *(yet)*
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<array>
 		<string>systemgroup.com.apple.VideoSubscriberAccount</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.pisco.suinfo</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.symptom_analytics.query</key>

```
### Books

> `/private/var/staged_system_apps/Books.app/Books`

```diff

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>CrashReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>OSAnalytics.Stability.Crash</key>
+				<true/>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.librarian.can-get-application-info</key>
 	<true/>
 	<key>com.apple.private.mobileinstall.upgrade-enabled</key>

```
### BooksNotificationContentExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksNotificationContentExtension.appex/BooksNotificationContentExtension`

```diff

 	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>CrashReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>OSAnalytics.Stability.Crash</key>
+				<true/>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

```
### BooksProductPageExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension`

```diff

 	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>CrashReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>OSAnalytics.Stability.Crash</key>
+				<true/>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.odi.legacySPIService</string>
+		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.arkit</key>
 	<true/>
+	<key>com.apple.assistant.cdm.client</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 	<true/>
 	<key>com.apple.locationd.dynamic_accuracy_reduction</key>
 	<true/>
+	<key>com.apple.locationd.prompt_content_control</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.mediastream.mstreamd-access</key>

```
### LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	<true/>
 	<key>com.apple.arkit</key>
 	<true/>
+	<key>com.apple.assistant.cdm.client</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 	<true/>
 	<key>com.apple.locationd.dynamic_accuracy_reduction</key>
 	<true/>
+	<key>com.apple.locationd.prompt_content_control</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.mediastream.mstreamd-access</key>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 		<string>spi</string>
 		<string>data-allowed-write</string>
 		<string>data-usage</string>
+		<string>cellular-plan</string>
 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
+	<key>com.apple.findmy.secureenvironment.client</key>
+	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService.access</key>
 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>

 		<string>com.apple.chrono.widgetcenterconnection</string>
 		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>
 		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+		<string>com.apple.findmy.FindMySecureEnvironmentXPCService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
 	<key>com.apple.developer.declared-age-range</key>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
-	<key>com.apple.developer.in-app-payments</key>
-	<array/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>INTERNAL.com.apple.Health</string>
 	<key>com.apple.developer.usernotifications.critical-alerts</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.rapport.Client</key>
+	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>

```
### HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
-	<key>com.apple.developer.declared-age-range</key>
-	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
-	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
-	<string>com.apple.Home</string>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>

```
### HomeWidgetLockScreen

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
-	<key>com.apple.developer.declared-age-range</key>
-	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
-	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
-	<string>com.apple.Home</string>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.maps.model-access</key>
 	<true/>
+	<key>com.apple.maps.suggestions.signalpipeline</key>
+	<true/>
 	<key>com.apple.maps.virtualgarage.vehicles</key>
 	<true/>
 	<key>com.apple.media.ringtones.read-only</key>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.businessservicesd.businessmetadata</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.springboard.delete-application-snapshots</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>

```
### MessagesPluginNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 </dict>
 </plist>
 

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 		<string>Safari.Navigations</string>
 		<string>Safari.PageLoad</string>
 		<string>Safari.WindowProxy</string>
+		<string>Unilog.SafariSearch.Stage</string>
 		<string>Safari.Browsing.Assistant</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.Events</string>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.people</key>

```
### PhotosNotificationsUpdates

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.communicationSafetySettings</string>
+		<string>com.apple.mobileslideshow</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### SequoiaTranslator

> `/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.aop.hid-driver.user-client</key>
 	<dict>
 		<key>eclipse</key>

 	</dict>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

 	<true/>
 	<key>com.apple.developer.team-identifier</key>
 	<string>96VJNMX6ZP</string>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Translate</string>
 	<key>com.apple.feedbackd.client-forms</key>
 	<array>
 		<string>:framework-translation-survey</string>

 	<true/>
 	<key>com.apple.locationd.asmanager</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>

```

### 🆕 TVRemoteSettingsAppIntents

> `/private/var/staged_system_apps/TVRemote.app/PlugIns/TVRemoteSettingsAppIntents.appex/TVRemoteSettingsAppIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### TVRemote

> `/private/var/staged_system_apps/TVRemote.app/TVRemote`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.tipsnext</string>
+		<string>group.com.apple.TVRemote</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### VoiceMemosIntentsExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
 	<key>com.apple.developer.siri</key>
 	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.VoiceMemos</string>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### VoiceMemosShareExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
 	<key>com.apple.developer.siri</key>
 	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.VoiceMemos</string>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### VoiceMemos

> `/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
 	<key>com.apple.developer.siri</key>
 	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.VoiceMemos</string>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### launchd

> `/sbin/launchd`

```diff

 	<true/>
 	<key>com.apple.private.set-atm-diagnostic-flag</key>
 	<true/>
+	<key>com.apple.private.shared-region.config</key>
+	<true/>
 	<key>com.apple.private.spawn-panic-crash-behavior</key>
 	<true/>
 	<key>com.apple.private.spawn-subsystem-root</key>

```
### BatteryDischargeService

> `/usr/libexec/BatteryDischargeService`

```diff

 <dict>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
-	<key>com.apple.powerui.smartcharging</key>
-	<true/>
 	<key>com.apple.private.iokit.battery-shipping-charge-limit</key>
 	<true/>
 	<key>com.apple.private.iokit.powermanagement</key>

```
### announced

> `/usr/libexec/announced`

```diff

 	<true/>
 	<key>com.apple.assistant.multiuser.service.remora</key>
 	<true/>
-	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
-	<true/>
 	<key>com.apple.coreaudio.allow-opus-codec</key>
 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.recovery</key>
+	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.cdp.walrus.pcskeys</key>

```
### appprotectiond

> `/usr/libexec/appprotectiond`

```diff

 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
 		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>

```
### atc

> `/usr/libexec/atc`

```diff

 	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.nanomediasync</string>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 		<string>kTCCServiceSensorKitWatchOnWristState</string>
 		<string>kTCCServiceSensorKitWatchHeartRate</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
 	<key>com.apple.private.ubiquity-kvstore-access</key>
 	<array>
 		<string>com.apple.springboard</string>

 	<array>
 		<string>kern.task_conclave</string>
 		<string>kern.bootargs</string>
+		<string>kern.darkboot</string>
 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>

```
### batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.powerui.smartcharging</key>
 	<true/>
 	<key>com.apple.private.alloy.batteryintelligence</key>

 		<string>com.apple.appleneuralengine.private</string>
 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.mobileactivationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 		<key>value</key>
 		<string>/usr/libexec/cameracaptured</string>
 	</dict>
+	<key>com.apple.private.audio.client-audit-token-override</key>
+	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.clpc.policy</key>

```
### caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.carkit.sessionBoost</key>
 	<true/>
+	<key>com.apple.private.carkit.statisticsPublisher</key>
+	<true/>
 	<key>com.apple.private.carp</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

```

### 🆕 chassisplatformhostd

> `/usr/libexec/chassisplatformhostd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.chassisplatformhostd.cpk.gov.remote</key>
	<true/>
	<key>com.apple.private.RemoteServiceDiscovery.compute-platform</key>
	<true/>
	<key>com.apple.private.RemoteServiceDiscovery.device-admin</key>
	<true/>
	<key>com.apple.private.network.management.data</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleUSBHostDeviceUserClient</string>
		<string>AppleUSBHostInterfaceUserClient</string>
	</array>
</dict>
</plist>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>

```
### frauddefensed

> `/usr/libexec/frauddefensed`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.frauddefensed</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>TrustKit.Decisioning.TKWalletOrderExtractionDomains</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 			</dict>
 		</dict>
 	</dict>

```
### gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
-	<key>com.apple.developer.game-center</key>
-	<true/>
 	<key>com.apple.gamepolicyd.tool.privileged.xpc</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access</key>

 	</array>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
-	<key>com.apple.private.game-center</key>
-	<array>
-		<string>Account</string>
-	</array>
 	<key>com.apple.private.game-controller.dynamic-device-manager</key>
 	<true/>
 	<key>com.apple.private.gamecontroller.config.client</key>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
-	<string>Development</string>
+	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.mobileinboxupdater.personalization</string>

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.nfcd.hce</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.diagnosticscheckupd.launch</key>
+	<true/>
 	<key>com.apple.private.iokit.limitedpower-wakerequest</key>
 	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>

 	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>

 	<true/>
 	<key>com.apple.rootless.volume.iSCHardware</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>
 		<string>com.apple.MIBULoopbackServerHelper</string>
 		<string>com.apple.cloudd</string>
+		<string>com.apple.diagnosticscheckupd</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### linkd

> `/usr/libexec/linkd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.linkd</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.biome.PublicStreamAccessService</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.dmd.policy</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.linkd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

```
### logd

> `/usr/libexec/logd`

```diff

 	<true/>
 	<key>com.apple.private.power.notifications</key>
 	<true/>
+	<key>com.apple.private.security.storage.LogdPreferencesCache</key>
+	<true/>
 	<key>com.apple.private.set-atm-diagnostic-flag</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.ios-system-session</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/secureconfig/</string>
+	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
 		<string>kern.exclaves_status</string>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<array>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.vfs.snapshot</key>
+	<true/>
+	<key>com.apple.private.vfs.snapshot.user</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.reboot</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.userspace-reboot</key>

```
### nexusd

> `/usr/libexec/nexusd`

```diff

 	<array>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.event-monitor</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Ringtones/</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	</array>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 	<key>com.apple.private.skywalk.observe-all</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.geoanalyticsd.telemetry</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.localfindable</key>

 	<true/>
 	<key>com.apple.icloud.searchpartyd.advertisementcache.write</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.btFinding.access</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.scheduler.access</key>
 	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>

 	<true/>
 	<key>com.apple.locationd.Proximity.TagManagement</key>
 	<true/>
+	<key>com.apple.locationd.activity</key>
+	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 	<array>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.terminusd</string>
+		<string>com.apple.findmydeviced.btfindingsession</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### securityd

> `/usr/libexec/securityd`

```diff

 	<true/>
 	<key>com.apple.authkit.devicelist.server-only</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

```
### softposreaderd

> `/usr/libexec/softposreaderd`

```diff

 	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
+	<key>com.apple.security.ts.ipc-posix-sem</key>
+	<string>purplebuddy.sentinel</string>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.softposreaderd</string>
 	<key>com.apple.seld.tsmmanager</key>

```
### soundanalysisd

> `/usr/libexec/soundanalysisd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/tmp/AudioCapture</string>
+		<string>/dev/exfiltration-adc-soundanalys</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.cascade.donation-requester</key>
+	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

```
### spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.cascade.donation-requester</key>
+	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

```
### symptomsd

> `/usr/libexec/symptomsd`

```diff

 	<array>
 		<string>com.apple.private.alloy.autobugcapture</string>
 	</array>
+	<key>com.apple.private.iokit.powermanagement.read-assertions</key>
+	<true/>
 	<key>com.apple.private.logging.admin</key>
 	<true/>
 	<key>com.apple.private.nehelper.privileged</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.wirelessinsightsd.xpc</string>
+		<string>com.apple.iohideventsystem</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### symptomsd-helper

> `/usr/libexec/symptomsd-helper`

```diff

 	<array>
 		<string>com.apple.private.alloy.autobugcapture</string>
 	</array>
+	<key>com.apple.private.iokit.powermanagement.read-assertions</key>
+	<true/>
 	<key>com.apple.private.logging.admin</key>
 	<true/>
 	<key>com.apple.private.nehelper.privileged</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.wirelessinsightsd.xpc</string>
+		<string>com.apple.iohideventsystem</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	<true/>
 	<key>com.apple.private.appmanagedfeatures.configuration</key>
 	<true/>
+	<key>com.apple.private.container.debug</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.dumpSysdiagnoseDataToDir</key>
 	<true/>
 	<key>com.apple.private.endpoint-security.xpc</key>

```

### 🆕 trustdFileHelper

> `/usr/libexec/trustdFileHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.security.storage.SFAnalytics</key>
	<true/>
	<key>com.apple.private.security.storage.trustd</key>
	<true/>
	<key>com.apple.private.security.storage.trustd-private</key>
	<true/>
</dict>
</plist>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 		<string>/private/var/preferences/SystemConfiguration/com.apple.wifi.plist</string>
 		<string>/usr/libexec/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/tvremoted/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
-		<string>/Library/Caches/com.apple.HomeKit.configurations/tvremoted/</string>
-		<string>/Library/Caches/com.apple.HomeKit/tvremoted/</string>
+		<string>/Library/Caches/com.apple.HomeKit/com.apple.tvremoted/</string>
 		<string>/Library/Caches/com.apple.tvremoted/</string>
 		<string>/Library/Caches/tvapp_bag/</string>
 		<string>/Library/HTTPStorages/com.apple.tvremoted/</string>
-		<string>/Library/tvremoted/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
-		<string>IOHIDUserDeviceCreate</string>
-		<string>IOHIDResourceDeviceUserClient</string>
-		<string>IOHIDUserClient</string>
 		<string>IO80211APIUserClient</string>
 		<string>IOHIDLibUserClient</string>
+		<string>IOHIDResourceDeviceUserClient</string>
+		<string>IOHIDUserClient</string>
+		<string>IOHIDUserDeviceCreate</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.coreaudio</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.homesharing</string>
+		<string>com.apple.rapport</string>
 		<string>com.apple.Sharing</string>
+		<string>com.apple.TVRemoteCore</string>
 		<string>com.apple.videos-preferences</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### xpcproxy

> `/usr/libexec/xpcproxy`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.driverkitd</key>
 	<true/>
+	<key>com.apple.private.shared-region.config</key>
+	<true/>
 	<key>com.apple.private.spawn-driver</key>
 	<true/>
 	<key>com.apple.private.spawn-panic-crash-behavior</key>

```
### BTLEServer

> `/usr/sbin/BTLEServer`

```diff

 	<true/>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	</array>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
+	<key>com.apple.developer.homekit</key>
+	<true/>
 	<key>com.apple.driver.AppleBluetoothModule.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleConvergedIPC.user-access</key>

 	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
+	<key>com.apple.homekit.private-spi-access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.access</key>

 	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
+	<key>com.apple.private.homekit.beacon-keybag</key>
+	<true/>
 	<key>com.apple.private.iokit.nvram-bluetooth</key>
 	<true/>
 	<key>com.apple.private.iokit.powersource-control</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceBluetoothPeripheral</string>
+		<string>kTCCServiceWillow</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>

 		<string>com.apple.backboard.display.services</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.matter.support.xpc</string>
+		<string>com.apple.homed.beacon-keybag</string>
 		<string>com.apple.UXMAssertionService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.ProductKitService</string>

```


### SystemOS

### com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile</key>
+	<string>com.apple.WebKit.GPU</string>
 	<key>com.apple.private.web-browser-engine.gpu</key>
 	<true/>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>

```
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile</key>
+	<string>com.apple.WebKit.Networking</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>BlockNetworkAccess</string>

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.sqlite.defensive</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile</key>
+	<string>com.apple.WebKit.WebContent</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>EnableExperimentalSandbox</string>

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/ExtensionKit/Extensions/WebContentEnhancedSecurityExtension.appex/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile</key>
+	<string>com.apple.WebKit.WebContent</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>EnableExperimentalSandbox</string>

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile</key>
+	<string>com.apple.WebKit.WebContent</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>EnableExperimentalSandbox</string>

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### AutoFillHelper

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/AutoFillHelper.xpc/AutoFillHelper`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.mobilesafari</string>
 		<string>com.apple.WebUI</string>
 	</array>
 	<key>keychain-access-groups</key>

```


### AppOS

### SafariBookmarksSyncAgent

> `/usr/libexec/SafariBookmarksSyncAgent`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>*</string>
 	<key>com.apple.private.security.container-required</key>

```
### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Unilog.SafariSearch.Stage</string>
+	</array>
 	<key>com.apple.private.can-import-browsing-data-to-Safari</key>
 	<true/>
 	<key>com.apple.private.can-load-any-content-blocker</key>

 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.securityd</string>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.lsd.xpc</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>

```


