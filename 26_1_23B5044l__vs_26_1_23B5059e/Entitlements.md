## 🔑 Entitlements

### ContinuitySingShieldUI

> `/Applications/ContinuitySingShieldUI.app/ContinuitySingShieldUI`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.idle-timer-services</key>
+	<true/>
 	<key>com.apple.itunescloud.delegate-account-store</key>
 	<true/>
 	<key>com.apple.itunescloud.delegation-provider</key>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 		<string>com.apple.CheckerBoard</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.AppleServiceToolkit</string>
+		<string>com.apple.backboardd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Diagnostic-8187

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187`

```diff

 	<true/>
 	<key>com.apple.private.powersource-write</key>
 	<true/>
+	<key>com.apple.private.runningboard.Diagnostics</key>
+	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>IOAccessoryManagerUserClient</string>

```
### MomentsUIService

> `/Applications/MomentsUIService.app/MomentsUIService`

```diff

 	<array>
 		<string>Moments.Events.Engagement</string>
 		<string>Moments.Events.EngagementLight</string>
+		<string>Moments.Events.Notifications</string>
 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>

 		<key>Moments</key>
 		<dict>
 			<key>Streams</key>
-			<array>
-				<string>Moments.Events.Engagement</string>
-			</array>
+			<dict>
+				<key>Moments.Events.Engagement</key>
+				<true/>
+				<key>Moments.Events.Notifications</key>
+				<dict>
+					<key>mode</key>
+					<string>write-only</string>
+				</dict>
+			</dict>
 		</dict>
 	</dict>
 	<key>com.apple.private.photoanalysisd.access</key>

```
### PhotosUIService

> `/Applications/PhotosUIService.app/PhotosUIService`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.settings.userchangedpasscode</key>
+	<true/>
 	<key>com.apple.private.dmd.emergency-mode</key>
 	<true/>
 	<key>com.apple.private.dmd.policy</key>

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.homeenergy</key>
+	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>

 		<string>com.apple.migrationd</string>
 		<string>com.apple.alarmkitservices</string>
 		<string>com.apple.seserviced.storage-management-presentation</string>
+		<string>com.apple.homeenergyd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SIMSetupUIService

> `/Applications/SIMSetupUIService.app/SIMSetupUIService`

```diff

 	</dict>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>
+	<key>com.apple.private.ids.registration</key>
+	<array>
+		<string>com.apple.madrid</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	<true/>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.time_zone</key>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.stickers</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### SupportFlow

> `/Applications/SupportFlow.app/SupportFlow`

```diff

 		<string>DeviceExpert.Troubleshooting</string>
 		<string>Discoverability.Signals</string>
 	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>DeviceExpert.Troubleshooting</string>

```
### Trip

> `/Applications/Trip.app/Trip`

```diff

 	<true/>
 	<key>com.apple.developer.carp</key>
 	<true/>
+	<key>com.apple.private.CarAssetUtils.variants</key>
+	<true/>
 	<key>com.apple.private.RequiredVehicleAccessories</key>
 	<array>
 		<string>DriveInformation</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.CarAssetUtils.variants</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 CodeCoverageDelegate

> `/System/ExclaveKit/System/Library/Frameworks/CodeCoverageDelegate.framework/CodeCoverageDelegate`

- No entitlements *(yet)*
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 		<string>com.apple.HearingAids</string>
 		<string>com.apple.SoundDetection</string>
 		<string>com.apple.Accessibility.Magnifier</string>
+		<string>com.apple.Accessibility.FullKeyboardAccess</string>
 		<string>com.apple.Accessibility.GuidedAccess</string>
 		<string>com.apple.Accessibility.TouchAccommodations</string>
 		<string>com.apple.Accessibility.Collection</string>

```
### CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

 	<true/>
 	<key>com.apple.bannerkit.post</key>
 	<true/>
+	<key>com.apple.developer.carp</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.launchservices.clearadvertisingid</key>

 	</dict>
 	<key>com.apple.private.carkit</key>
 	<true/>
+	<key>com.apple.private.carp</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.runningboard.carplay</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.CarPlaySupport.banner-source</string>
+		<string>com.apple.carkit.navigation.service</string>
+		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.CarPlayApp.service</string>
 		<string>com.apple.CarPlayApp.status-bar-service</string>
-		<string>com.apple.carkit.navigation.service</string>
+		<string>com.apple.CarPlaySupport.banner-source</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<array>
 		<string>com.apple.commandandcontrol</string>
 	</array>
+	<key>com.apple.private.voicecontrol.speechrecognition.api</key>
+	<true/>
 	<key>com.apple.realitysimulation.render-on-top-spi</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Ocelot</string>
 		<string>Purchase</string>
 		<string>Library</string>
 		<string>IAPHistory</string>

```

### 🆕 SystemIntents

> `/System/Library/CoreServices/SystemIntents.app/SystemIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CarPlayApp.service</string>
	</array>
	<key>com.apple.springboard.closeApplicationAction</key>
	<true/>
	<key>com.apple.springboard.showHomeScreenAction</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### appplaceholdersyncd

> `/System/Library/CoreServices/appplaceholdersyncd`

```diff

 	</array>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>
+	<key>com.apple.security.ts.read-any-bundle</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/com.apple.DeviceRecovery.entryInfo</string>
 		<string>/System/DriverKit/System/Library/dyld/</string>
 		<string>/System/Cryptexes/OS/System/Library/Caches/com.apple.dyld/</string>
 		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.security.ts.nvram-read</key>
+	<array>
+		<string>device-recovery-boot-reason</string>
+	</array>
 	<key>com.apple.security.ts.read-any-bundle</key>
 	<true/>
 	<key>com.apple.softwareupdateservices.client.allowed</key>

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.priml.allowed-server-model-bundles</key>
+	<array/>
 	<key>com.apple.priml.pfl.Morpheus.allowed</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```

### 🆕 com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.WebKit.GPU</string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.rendering</key>
	<true/>
	<key>com.apple.mediaremote.external-artwork-validation</key>
	<true/>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.mediaremote.ui-control</key>
	<true/>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.attribution.explicitly-assumed-identities</key>
	<array>
		<dict>
			<key>type</key>
			<string>wildcard</string>
		</dict>
	</array>
	<key>com.apple.private.avfoundation.capture.temporary.no-media-environment.allow</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.mediaexperience.processassertionaudittokens.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.recordingWebsite.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>
	<true/>
	<key>com.apple.private.memory.ownership_transfer</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.web-browser-engine.gpu</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.systemstatus.activityattribution</string>
	</array>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
	<key>com.apple.springboard.statusbarstyleoverrides</key>
	<true/>
	<key>com.apple.springboard.statusbarstyleoverrides.coordinator</key>
	<array>
		<string>UIStatusBarStyleOverrideWebRTCAudioCapture</string>
		<string>UIStatusBarStyleOverrideWebRTCCapture</string>
	</array>
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
	<key>com.apple.systemstatus.activityattribution</key>
	<true/>
	<key>com.apple.tcc.delegated-services</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMicrophone</string>
	</array>
</dict>
</plist>

```
### GenerativeAssistantExtension

> `/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension`

```diff

 	<array>
 		<string>com.apple.generativeassistanttools.GenerativeAssistantExtension</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.familycircle</key>

```

### 🆕 InferenceExtension

> `/System/Library/ExtensionKit/Extensions/InferenceExtension.appex/InferenceExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.lighthouse.InferenceExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.coreduetd.knowledge</key>
	<true/>
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
	<key>com.apple.private.coreservices.cangetcurrentactivityinfo</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
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

### 🆕 LocalCaptureAppIntents

> `/System/Library/ExtensionKit/Extensions/LocalCaptureAppIntents.appex/LocalCaptureAppIntents`

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

### 🆕 com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.WebKit.Networking</string>
	<key>com.apple.das.private.bgtask.continuedprocessing</key>
	<true/>
	<key>com.apple.das.private.bgtask.continuedprocessing.iconBundleIdentifier</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.networking</key>
	<true/>
	<key>com.apple.multitasking.systemappassertions</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.private.accounts.bundleidspoofing</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>InstallWebAttribution</string>
	</array>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.WebContentRestrictions</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.ciphermld.allow</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>
		<string>kTCCServiceUserTracking</string>
	</array>
	<key>com.apple.private.web-browser-engine.network</key>
	<true/>
	<key>com.apple.private.webkit.adattributiond</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.private.webkit.webpush</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
	<key>com.apple.symptom_analytics.configure</key>
	<true/>
</dict>
</plist>

```
### PFLASLAppEmbedding

> `/System/Library/ExtensionKit/Extensions/PFLASLAppEmbedding.appex/PFLASLAppEmbedding`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLASLArcadeRanking

> `/System/Library/ExtensionKit/Extensions/PFLASLArcadeRanking.appex/PFLASLArcadeRanking`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLASLArcadeRetention

> `/System/Library/ExtensionKit/Extensions/PFLASLArcadeRetention.appex/PFLASLArcadeRetention`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLASLExperimental

> `/System/Library/ExtensionKit/Extensions/PFLASLExperimental.appex/PFLASLExperimental`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLCSLAppStore

> `/System/Library/ExtensionKit/Extensions/PFLCSLAppStore.appex/PFLCSLAppStore`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLCSLAppStore2

> `/System/Library/ExtensionKit/Extensions/PFLCSLAppStore2.appex/PFLCSLAppStore2`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PasscodeAndBiometricsSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasscodeAndBiometricsSettingsAppIntentsExtension.appex/PasscodeAndBiometricsSettingsAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.private.sharing.unlock-manager</key>
+	<true/>
 </dict>
 </plist>
 

```
### PhotoPicker

> `/System/Library/ExtensionKit/Extensions/PhotoPicker.appex/PhotoPicker`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

```
### PhotosMessagesApp

> `/System/Library/ExtensionKit/Extensions/PhotosMessagesApp.appex/PhotosMessagesApp`

```diff

 		<key>value</key>
 		<string>com.apple.mobileslideshow</string>
 	</dict>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/PhotosPicker`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Ocelot</string>
 		<string>Purchase</string>
 		<string>Library</string>
 		<string>IAPHistory</string>

```
### SCARemoteView Appex

> `/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/SCARemoteView Appex`

```diff

 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.SensitiveContentAnalysis</string>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Ocelot</string>
 		<string>Purchase</string>
 		<string>Library</string>
 		<string>IAPHistory</string>

```

### 🆕 com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.restrict.notifyd</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.imageio.allowabletypes</key>
	<array>
		<string>org.webmproject.webp</string>
		<string>public.jpeg</string>
		<string>public.png</string>
		<string>com.compuserve.gif</string>
	</array>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.pac.shared_region_id</key>
	<string>WebContent</string>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.darwin-notification.introspect</key>
	<array>
		<string>com.apple.accessibility.cache.app.ax</string>
		<string>com.apple.accessibility.cache.ast</string>
		<string>com.apple.accessibility.cache.automation.localized.lookup</string>
		<string>com.apple.accessibility.cache.ax</string>
		<string>com.apple.accessibility.cache.captioning</string>
		<string>com.apple.accessibility.cache.differentiate.without.color</string>
		<string>com.apple.accessibility.cache.enhance.background.contrast</string>
		<string>com.apple.accessibility.cache.enhance.text.legibility</string>
		<string>com.apple.accessibility.cache.enhance.text.legibilitycom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.guided.access</string>
		<string>com.apple.accessibility.cache.guided.access.via.mdm</string>
		<string>com.apple.accessibility.cache.hearing.aid.paired</string>
		<string>com.apple.accessibility.cache.internal.reportvalidationerrors</string>
		<string>com.apple.accessibility.cache.invert.colors</string>
		<string>com.apple.accessibility.cache.invert.colorscom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.loc.caption.mode.enabled</string>
		<string>com.apple.accessibility.cache.mono.audio</string>
		<string>com.apple.accessibility.cache.quick.speak</string>
		<string>com.apple.accessibility.cache.reduce.motion</string>
		<string>com.apple.accessibility.cache.reduce.motion.reduce.slide.transitions</string>
		<string>com.apple.accessibility.cache.reduce.motioncom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.speak.this</string>
		<string>com.apple.accessibility.cache.speech.settings.disabled.by.mc</string>
		<string>com.apple.accessibility.cache.switch.control</string>
		<string>com.apple.accessibility.cache.vot</string>
		<string>com.apple.accessibility.cache.zoom</string>
		<string>com.apple.accessibility.cache.*</string>
		<string>com.apple.system.DirectoryService.InvalidateCache*</string>
		<string>com.apple.coreservices.launchservices.session.*</string>
		<string>user.uid.501.syslog.*</string>
		<string>_AXNotification__UUID_</string>
		<string>_AXNotification_AXMRInvertColors</string>
		<string>_AXNotification_AXMRReduceWhitePoint</string>
		<string>_AXNotification_AXMuseDisplayFiltersEnabled</string>
		<string>_UUID_.notification</string>
		<string>CPActiveCountryCodeChanged.Internal</string>
		<string>MCManagedBooksChanged</string>
		<string>PINPolicyChangedNotification</string>
		<string>com.apple.ManagedConfiguration.diagnosticsCollected</string>
		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
		<string>com.apple.ManagedConfiguration.profileListChanged</string>
		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>
		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
		<string>com.apple.UIKit.InternalPreferences</string>
		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
		<string>com.apple.accessibility.QuickSpeakLocaleForLanguage</string>
		<string>com.apple.accessibility.cache.guided.access</string>
		<string>com.apple.accessibility.haptics.active.status.private</string>
		<string>com.apple.accessibility.internal.reader.changed</string>
		<string>com.apple.coreaudio.audioanalytics.tailspin.defaultsChanged</string>
		<string>com.apple.managedconfiguration._UUID_</string>
		<string>com.apple.managedconfiguration.allowhealthdatasubmissionchanged</string>
		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
		<string>com.apple.managedconfiguration.clearpasscodegenerationcaches</string>
		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
		<string>com.apple.managedconfiguration.defaultsdidchange</string>
		<string>com.apple.managedconfiguration.effectivesettingschanged</string>
		<string>com.apple.managedconfiguration.homescreenlayoutchanged</string>
		<string>com.apple.managedconfiguration.keyboardsettingschanged</string>
		<string>com.apple.managedconfiguration.newssettingschanged</string>
		<string>com.apple.managedconfiguration.passcodechanged</string>
		<string>com.apple.managedconfiguration.restrictionchanged</string>
		<string>com.apple.managedconfiguration.settingschanged</string>
		<string>com.apple.managedconfiguration.webFilterUIActiveDidChange</string>
		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
		<string>com.apple.mobile.keybagd.lock_status</string>
		<string>com.apple.mobile.keybagd.user_changed</string>
		<string>com.apple.system.console_mode_changed</string>
		<string>com.apple.system.thermalpressurelevel</string>
		<string>com.apple.voiceovertouch.screencurtain</string>
		<string>__ABDataBaseChangedByOtherProcessNotification</string>
		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>
		<string>_AXNotification_UseNewAXBundleLoader</string>
		<string>_AXNotification_shouldPerformValidationsAtRuntime</string>
		<string>_NS_ctasd</string>
		<string>AppleCarPlayPreferredContentSizeCategoryChangedNotification</string>
		<string>AppleDatePreferencesChangedNotification</string>
		<string>AppleKeyboardsContinuousPathSettingsChangedNotification</string>
		<string>AppleKeyboardsInputModeChangedNotification</string>
		<string>AppleKeyboardsInternalSettingsChangedNotification</string>
		<string>AppleKeyboardsPreferencesChangedNotification</string>
		<string>AppleKeyboardsSettingsChangedNotification</string>
		<string>AppleLanguagePreferencesChangedNotification</string>
		<string>AppleMeasurementSystemPreferencesChangedNotification</string>
		<string>AppleNumberPreferencesChangedNotification</string>
		<string>ApplePreferredContentSizeCategoryChangedNotification</string>
		<string>AppleTemperatureUnitPreferencesChangedNotification</string>
		<string>AppleTextBehaviorPreferencesChangedNotification</string>
		<string>AppleTimePreferencesChangedNotification</string>
		<string>CPHomeCountryCodeChanged.Internal</string>
		<string>GSEventHardwareKeyboardAttached</string>
		<string>LetterFeedbackEnabled.notification</string>
		<string>PhoneticFeedbackEnabled.notification</string>
		<string>QuickTypePredictionFeedbackEnabled.notification</string>
		<string>WordFeedbackEnabled.notification</string>
		<string>com.apple.AddressBook.PreferenceChanged</string>
		<string>com.apple.CFNetwork.har-capture-update</string>
		<string>com.apple.CFPreferences._domainsChangedExternally</string>
		<string>com.apple.LaunchServices.database</string>
		<string>com.apple.TTS.synthProviderVoicesDidUpdate</string>
		<string>com.apple.UIKit.LoggingPreferences</string>
		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
		<string>com.apple.WebKit.deleteAllCode</string>
		<string>com.apple.WebKit.dumpGCHeap</string>
		<string>com.apple.WebKit.dumpUntrackedMallocs</string>
		<string>com.apple.WebKit.fullGC</string>
		<string>com.apple.WebKit.logMemStats</string>
		<string>com.apple.WebKit.logPageState</string>
		<string>com.apple.WebKit.showAllDocuments</string>
		<string>com.apple.WebKit.showBackForwardCache</string>
		<string>com.apple.WebKit.dumpAccessibilityTreeToStderr</string>
		<string>com.apple.WebKit.showGraphicsLayerTree</string>
		<string>com.apple.WebKit.showLayerTree</string>
		<string>com.apple.WebKit.showLayoutTree</string>
		<string>com.apple.WebKit.showLegacyFlexReasons</string>
		<string>com.apple.WebKit.showMemoryCache</string>
		<string>com.apple.WebKit.showPaintOrderTree</string>
		<string>com.apple.WebKit.showRenderTree</string>
		<string>com.apple.accessibility.api</string>
		<string>com.apple.accessibility.defaultrouteforcall</string>
		<string>com.apple.accessibility.wob.status</string>
		<string>com.apple.analyticsd.running</string>
		<string>com.apple.asl.remote</string>
		<string>com.apple.caulk.alloc.audiodump</string>
		<string>com.apple.caulk.alloc.rtdump</string>
		<string>com.apple.coreaudio.list_components</string>
		<string>com.apple.coreui.statistics</string>
		<string>com.apple.distnote.locale_changed</string>
		<string>com.apple.language.changed</string>
		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
		<string>com.apple.mediaaccessibility.captionAppearanceSettingsChanged</string>
		<string>com.apple.powerlog.state_changed</string>
		<string>com.apple.preferences.sounds.keyboard-audio.changed</string>
		<string>com.apple.runningboard.daemonstartup</string>
		<string>com.apple.system.logging.prefschanged</string>
		<string>com.apple.system.lowpowermode</string>
		<string>com.apple.system.networkd.settings</string>
		<string>com.apple.system.syslog.master</string>
		<string>com.apple.system.timezone</string>
		<string>com.apple.system.timezone./var/db/timezone/zoneinfo/UTC</string>
		<string>com.apple.webinspectord.automatic_inspection_enabled</string>
		<string>com.apple.webinspectord.available</string>
		<string>com.apple.zoomwindow</string>
		<string>kAFPreferencesDidChangeDarwinNotification</string>
		<string>org.WebKit.lowMemory</string>
		<string>org.WebKit.lowMemory.begin</string>
		<string>org.WebKit.lowMemory.end</string>
		<string>org.WebKit.memoryWarning</string>
		<string>org.WebKit.memoryWarning.begin</string>
		<string>org.WebKit.memoryWarning.end</string>
		<string>org.WebKit.testNotification</string>
	</array>
	<key>com.apple.private.disable-log-mach-ports</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
		<string>BlockOpenDirectoryInWebContentSandbox</string>
		<string>BlockMobileAssetInWebContentSandbox</string>
		<string>BlockWebInspectorInWebContentSandbox</string>
		<string>BlockIconServicesInWebContentSandbox</string>
		<string>BlockFontServiceInWebContentSandbox</string>
		<string>UnifiedPDFEnabled</string>
		<string>WebProcessDidNotInjectStoreBundle</string>
		<string>BlockUserInstalledFonts</string>
	</array>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>EnableQuickLookSandboxResources</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
		<string>BlockOpenDirectoryInWebContentSandbox</string>
		<string>BlockMobileAssetInWebContentSandbox</string>
		<string>BlockWebInspectorInWebContentSandbox</string>
		<string>BlockIconServicesInWebContentSandbox</string>
		<string>BlockFontServiceInWebContentSandbox</string>
		<string>UnifiedPDFEnabled</string>
		<string>WebProcessDidNotInjectStoreBundle</string>
		<string>BlockUserInstalledFonts</string>
	</array>
	<key>com.apple.private.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.private.webinspector.allow-remote-inspection</key>
	<true/>
	<key>com.apple.private.webinspector.proxy-application</key>
	<true/>
	<key>com.apple.private.webkit.lockdown-mode</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
</dict>
</plist>

```

### 🆕 com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.cs.allow-jit</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.restrict.notifyd</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.pac.shared_region_id</key>
	<string>WebContent</string>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.darwin-notification.introspect</key>
	<array>
		<string>com.apple.accessibility.cache.app.ax</string>
		<string>com.apple.accessibility.cache.ast</string>
		<string>com.apple.accessibility.cache.automation.localized.lookup</string>
		<string>com.apple.accessibility.cache.ax</string>
		<string>com.apple.accessibility.cache.captioning</string>
		<string>com.apple.accessibility.cache.differentiate.without.color</string>
		<string>com.apple.accessibility.cache.enhance.background.contrast</string>
		<string>com.apple.accessibility.cache.enhance.text.legibility</string>
		<string>com.apple.accessibility.cache.enhance.text.legibilitycom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.guided.access</string>
		<string>com.apple.accessibility.cache.guided.access.via.mdm</string>
		<string>com.apple.accessibility.cache.hearing.aid.paired</string>
		<string>com.apple.accessibility.cache.internal.reportvalidationerrors</string>
		<string>com.apple.accessibility.cache.invert.colors</string>
		<string>com.apple.accessibility.cache.invert.colorscom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.loc.caption.mode.enabled</string>
		<string>com.apple.accessibility.cache.mono.audio</string>
		<string>com.apple.accessibility.cache.quick.speak</string>
		<string>com.apple.accessibility.cache.reduce.motion</string>
		<string>com.apple.accessibility.cache.reduce.motion.reduce.slide.transitions</string>
		<string>com.apple.accessibility.cache.reduce.motioncom.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.cache.speak.this</string>
		<string>com.apple.accessibility.cache.speech.settings.disabled.by.mc</string>
		<string>com.apple.accessibility.cache.switch.control</string>
		<string>com.apple.accessibility.cache.vot</string>
		<string>com.apple.accessibility.cache.zoom</string>
		<string>com.apple.accessibility.cache.*</string>
		<string>com.apple.system.DirectoryService.InvalidateCache*</string>
		<string>com.apple.coreservices.launchservices.session.*</string>
		<string>user.uid.501.syslog.*</string>
		<string>_AXNotification__UUID_</string>
		<string>_AXNotification_AXMRInvertColors</string>
		<string>_AXNotification_AXMRReduceWhitePoint</string>
		<string>_AXNotification_AXMuseDisplayFiltersEnabled</string>
		<string>_UUID_.notification</string>
		<string>CPActiveCountryCodeChanged.Internal</string>
		<string>MCManagedBooksChanged</string>
		<string>PINPolicyChangedNotification</string>
		<string>com.apple.ManagedConfiguration.diagnosticsCollected</string>
		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
		<string>com.apple.ManagedConfiguration.profileListChanged</string>
		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>
		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
		<string>com.apple.UIKit.InternalPreferences</string>
		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
		<string>com.apple.accessibility.QuickSpeakLocaleForLanguage</string>
		<string>com.apple.accessibility.cache.guided.access</string>
		<string>com.apple.accessibility.haptics.active.status.private</string>
		<string>com.apple.accessibility.internal.reader.changed</string>
		<string>com.apple.coreaudio.audioanalytics.tailspin.defaultsChanged</string>
		<string>com.apple.managedconfiguration._UUID_</string>
		<string>com.apple.managedconfiguration.allowhealthdatasubmissionchanged</string>
		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
		<string>com.apple.managedconfiguration.clearpasscodegenerationcaches</string>
		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
		<string>com.apple.managedconfiguration.defaultsdidchange</string>
		<string>com.apple.managedconfiguration.effectivesettingschanged</string>
		<string>com.apple.managedconfiguration.homescreenlayoutchanged</string>
		<string>com.apple.managedconfiguration.keyboardsettingschanged</string>
		<string>com.apple.managedconfiguration.newssettingschanged</string>
		<string>com.apple.managedconfiguration.passcodechanged</string>
		<string>com.apple.managedconfiguration.restrictionchanged</string>
		<string>com.apple.managedconfiguration.settingschanged</string>
		<string>com.apple.managedconfiguration.webFilterUIActiveDidChange</string>
		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
		<string>com.apple.mobile.keybagd.lock_status</string>
		<string>com.apple.mobile.keybagd.user_changed</string>
		<string>com.apple.system.console_mode_changed</string>
		<string>com.apple.system.thermalpressurelevel</string>
		<string>com.apple.voiceovertouch.screencurtain</string>
		<string>__ABDataBaseChangedByOtherProcessNotification</string>
		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>
		<string>_AXNotification_UseNewAXBundleLoader</string>
		<string>_AXNotification_shouldPerformValidationsAtRuntime</string>
		<string>_NS_ctasd</string>
		<string>AppleCarPlayPreferredContentSizeCategoryChangedNotification</string>
		<string>AppleDatePreferencesChangedNotification</string>
		<string>AppleKeyboardsContinuousPathSettingsChangedNotification</string>
		<string>AppleKeyboardsInputModeChangedNotification</string>
		<string>AppleKeyboardsInternalSettingsChangedNotification</string>
		<string>AppleKeyboardsPreferencesChangedNotification</string>
		<string>AppleKeyboardsSettingsChangedNotification</string>
		<string>AppleLanguagePreferencesChangedNotification</string>
		<string>AppleMeasurementSystemPreferencesChangedNotification</string>
		<string>AppleNumberPreferencesChangedNotification</string>
		<string>ApplePreferredContentSizeCategoryChangedNotification</string>
		<string>AppleTemperatureUnitPreferencesChangedNotification</string>
		<string>AppleTextBehaviorPreferencesChangedNotification</string>
		<string>AppleTimePreferencesChangedNotification</string>
		<string>CPHomeCountryCodeChanged.Internal</string>
		<string>GSEventHardwareKeyboardAttached</string>
		<string>LetterFeedbackEnabled.notification</string>
		<string>PhoneticFeedbackEnabled.notification</string>
		<string>QuickTypePredictionFeedbackEnabled.notification</string>
		<string>WordFeedbackEnabled.notification</string>
		<string>com.apple.AddressBook.PreferenceChanged</string>
		<string>com.apple.CFNetwork.har-capture-update</string>
		<string>com.apple.CFPreferences._domainsChangedExternally</string>
		<string>com.apple.LaunchServices.database</string>
		<string>com.apple.TTS.synthProviderVoicesDidUpdate</string>
		<string>com.apple.UIKit.LoggingPreferences</string>
		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
		<string>com.apple.WebKit.deleteAllCode</string>
		<string>com.apple.WebKit.dumpGCHeap</string>
		<string>com.apple.WebKit.dumpUntrackedMallocs</string>
		<string>com.apple.WebKit.fullGC</string>
		<string>com.apple.WebKit.logMemStats</string>
		<string>com.apple.WebKit.logPageState</string>
		<string>com.apple.WebKit.showAllDocuments</string>
		<string>com.apple.WebKit.showBackForwardCache</string>
		<string>com.apple.WebKit.dumpAccessibilityTreeToStderr</string>
		<string>com.apple.WebKit.showGraphicsLayerTree</string>
		<string>com.apple.WebKit.showLayerTree</string>
		<string>com.apple.WebKit.showLayoutTree</string>
		<string>com.apple.WebKit.showLegacyFlexReasons</string>
		<string>com.apple.WebKit.showMemoryCache</string>
		<string>com.apple.WebKit.showPaintOrderTree</string>
		<string>com.apple.WebKit.showRenderTree</string>
		<string>com.apple.accessibility.api</string>
		<string>com.apple.accessibility.defaultrouteforcall</string>
		<string>com.apple.accessibility.wob.status</string>
		<string>com.apple.analyticsd.running</string>
		<string>com.apple.asl.remote</string>
		<string>com.apple.caulk.alloc.audiodump</string>
		<string>com.apple.caulk.alloc.rtdump</string>
		<string>com.apple.coreaudio.list_components</string>
		<string>com.apple.coreui.statistics</string>
		<string>com.apple.distnote.locale_changed</string>
		<string>com.apple.language.changed</string>
		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
		<string>com.apple.mediaaccessibility.captionAppearanceSettingsChanged</string>
		<string>com.apple.powerlog.state_changed</string>
		<string>com.apple.preferences.sounds.keyboard-audio.changed</string>
		<string>com.apple.runningboard.daemonstartup</string>
		<string>com.apple.system.logging.prefschanged</string>
		<string>com.apple.system.lowpowermode</string>
		<string>com.apple.system.networkd.settings</string>
		<string>com.apple.system.syslog.master</string>
		<string>com.apple.system.timezone</string>
		<string>com.apple.system.timezone./var/db/timezone/zoneinfo/UTC</string>
		<string>com.apple.webinspectord.automatic_inspection_enabled</string>
		<string>com.apple.webinspectord.available</string>
		<string>com.apple.zoomwindow</string>
		<string>kAFPreferencesDidChangeDarwinNotification</string>
		<string>org.WebKit.lowMemory</string>
		<string>org.WebKit.lowMemory.begin</string>
		<string>org.WebKit.lowMemory.end</string>
		<string>org.WebKit.memoryWarning</string>
		<string>org.WebKit.memoryWarning.begin</string>
		<string>org.WebKit.memoryWarning.end</string>
		<string>org.WebKit.testNotification</string>
	</array>
	<key>com.apple.private.disable-log-mach-ports</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
		<string>BlockOpenDirectoryInWebContentSandbox</string>
		<string>BlockMobileAssetInWebContentSandbox</string>
		<string>BlockWebInspectorInWebContentSandbox</string>
		<string>BlockIconServicesInWebContentSandbox</string>
		<string>BlockFontServiceInWebContentSandbox</string>
		<string>UnifiedPDFEnabled</string>
		<string>WebProcessDidNotInjectStoreBundle</string>
		<string>BlockUserInstalledFonts</string>
	</array>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
		<string>EnableQuickLookSandboxResources</string>
		<string>ParentProcessCanEnableQuickLookStateFlag</string>
		<string>BlockOpenDirectoryInWebContentSandbox</string>
		<string>BlockMobileAssetInWebContentSandbox</string>
		<string>BlockWebInspectorInWebContentSandbox</string>
		<string>BlockIconServicesInWebContentSandbox</string>
		<string>BlockFontServiceInWebContentSandbox</string>
		<string>UnifiedPDFEnabled</string>
		<string>WebProcessDidNotInjectStoreBundle</string>
		<string>BlockUserInstalledFonts</string>
	</array>
	<key>com.apple.private.verified-jit</key>
	<true/>
	<key>com.apple.private.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.private.webinspector.allow-remote-inspection</key>
	<true/>
	<key>com.apple.private.webinspector.proxy-application</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
</dict>
</plist>

```
### WritingToolsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/WritingToolsAppIntentsExtension.appex/WritingToolsAppIntentsExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.generativepartnerservicesettings</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.gms.availability</string>
 	</array>
 </dict>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.mobile.keybagd.UserManager.logout</key>
 	<true/>
-	<key>com.apple.photos.asset-resource-background-upload</key>
+	<key>com.apple.photos.background-upload</key>
 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>

 	</dict>
 	<key>com.apple.private.avfoundation.capture.deferred-photo-processor.allow</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+	</array>
 	<key>com.apple.private.cloudkit.spi</key>
 	<true/>
 	<key>com.apple.private.cloudphotod.access</key>

 	<true/>
 	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
 	<true/>
+	<key>com.apple.private.nsurlsession.impersonate</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.allowcollectionshare</key>

```
### AudioConverterHardenedService

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterHardenedService.xpc/AudioConverterHardenedService`

```diff

 	<key>com.apple.private.memory.ownership_transfer</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
-	<string>autobox</string>
+	<string>AudioConverterService</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Preferences/com.apple.coreaudio.plist</string>

```
### ContactViewViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService`

```diff

 	<true/>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 	</array>

```
### ContactsViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService`

```diff

 	<true/>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 	</array>

```
### CommCenterMobileHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.ids.remotecredentials</key>
+	<true/>
+	<key>com.apple.private.imcore.imremoteurlconnection</key>
+	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

```
### com.apple.accessibility.mediaaccessibilityd

> `/System/Library/Frameworks/MediaAccessibility.framework/XPCServices/com.apple.accessibility.mediaaccessibilityd.xpc/com.apple.accessibility.mediaaccessibilityd`

```diff

 		<string>com.apple.mediaaccessibility</string>
 		<string>com.apple.mediaaccessibility.public</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```

### 🆕 PassKitWrapperXPCServiceUI

> `/System/Library/Frameworks/PassKit.framework/XPCServices/PassKitWrapperXPCServiceUI.xpc/PassKitWrapperXPCServiceUI`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PassKitWrapperXPCServiceUI</string>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.developer.kernel.increased-memory-limit</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.peerpayment.all-access</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>Library/Caches/com.apple.PassKitWrapperXPCServiceUI/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOGPUDeviceUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.linkd.autoShortcut</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.passd.peer-payment</string>
		<string>com.apple.containermanagerd.system</string>
		<string>com.apple.containermanagerd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UIKit</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXDeviceUserClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 SafariServices

> `/System/Library/Frameworks/SafariServices.framework/PlugIns/SafariServices.wkbundle/SafariServices`

- No entitlements *(yet)*

### 🆕 com.apple.SafariServices.ContentBlockerLoader

> `/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.can-load-any-content-blocker</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.private.security.storage.Safari</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.safari</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/Applications/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Safari/</string>
	</array>
</dict>
</plist>

```

### 🆕 adattributiond

> `/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile</key>
	<string>com.apple.WebKit.adattributiond</string>
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
</dict>
</plist>

```

### 🆕 HomePrivacySettings

> `/System/Library/PreferenceBundles/HomePrivacySettings.bundle/HomePrivacySettings`

- No entitlements *(yet)*

### 🆕 ReplayKitInternalSettings

> `/System/Library/PreferenceBundles/ReplayKitInternalSettings.bundle/ReplayKitInternalSettings`

- No entitlements *(yet)*

### 🆕 ReplayKitLocalCaptureSettings

> `/System/Library/PreferenceBundles/ReplayKitLocalCaptureSettings.bundle/ReplayKitLocalCaptureSettings`

- No entitlements *(yet)*
### AppStoreEventServiceExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/AppStoreEventServiceExtension.appex/AppStoreEventServiceExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.ap.promotedcontent.metrics</string>
 	</array>
 </dict>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.fitcore</key>
 	<true/>
+	<key>com.apple.fitnessintelligenced</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboard.shutdown</key>

 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.fitnessintelligenced</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

```diff

 		<string>com.apple.voiceservices</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.facetime.bag</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 DeviceRecoveryBrainSupport

> `/System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport`

- No entitlements *(yet)*
### RecentsAvocado

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado`

```diff

 		<key>appData</key>
 		<true/>
 	</dict>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
 	<key>com.apple.private.clouddocs.can-grant-access-to-document</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
+	<key>com.apple.private.parsec.default-client</key>
+	<string>com.apple.email.maild</string>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.personas.propagate</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
-	<key>com.apple.private.assets.accessible-asset-types</key>
-	<array>
-		<string>com.apple.MobileAsset.LinguisticData</string>
-		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
-		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
-		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
-		<string>com.apple.MobileAsset.CN.Guardrail</string>
-	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
 	<key>com.apple.private.assistant.settings</key>
 	<true/>
 	<key>com.apple.private.biome.read-only</key>

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_Planner/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_SummarizationKitConfiguration/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_DialogAssets/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_UnderstandingASRHammer/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_FindMyConfigurationFiles/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_UnderstandingNLOverrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_TextToSpeech/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/purpose_auto/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
-		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.generativeexperiences.corefollowup</string>
-		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.appleintelligencereporting</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 		<string>com.apple.compass.cellular-waypoints</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.contacts.poster.api</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ManifestStorageService

> `/System/Library/PrivateFrameworks/MobileAsset.framework/XPCServices/ManifestStorageService.xpc/ManifestStorageService`

```diff

 <dict>
 	<key>com.apple.private.image4.dfu.mobile-asset</key>
 	<true/>
+	<key>com.apple.private.img4.nonce.cryptex1.mobile-asset.code-install</key>
+	<true/>
+	<key>com.apple.private.img4.nonce.cryptex1.mobile-asset.code-load</key>
+	<true/>
 	<key>com.apple.private.security.AppleImage4.user-client</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetManifestStorage</key>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.install.distributor-info-source</key>
 	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>

```

### 🆕 BrowsingDataImport

> `/System/Library/PrivateFrameworks/MobileSafari.framework/XPCServices/BrowsingDataImport.xpc/BrowsingDataImport`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.ArchiveService.XPC</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.desktopservices.ArchiveService</string>
		<string>com.apple.Safari.CredentialExtractionHelper</string>
	</array>
</dict>
</plist>

```
### mobiletimerd

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd`

```diff

 	<array>
 		<string>group.com.apple.mobiletimerd</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/Library/Ringtones/</string>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.coreidvd.identity-proofing</key>
 	<true/>
+	<key>com.apple.coreidvd.identity-proofing-ui</key>
+	<true/>
 	<key>com.apple.coreidvd.identity-provisioning</key>
 	<true/>
 	<key>com.apple.coreidvd.spi</key>

```

### 🆕 PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

- No entitlements *(yet)*

### 🆕 AutoFillHelper

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/AutoFillHelper.xpc/AutoFillHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authentication-services.access-credential-identities</key>
	<true/>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.octagon</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assertiond.applicationstateconnection</string>
		<string>com.apple.SharedWebCredentials</string>
		<string>com.apple.securityd</string>
		<string>com.apple.security.octagon</string>
		<string>com.apple.accountsd.accountmanager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.WebUI</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.cfnetwork</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>AutoFillHelper</string>
	</array>
</dict>
</plist>

```

### 🆕 CredentialProviderExtensionHelper

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/CredentialProviderExtensionHelper.xpc/CredentialProviderExtensionHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.authentication-services.access-credential-identities</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>CredentialProviderExtensionHelper</string>
	</array>
</dict>
</plist>

```

### 🆕 SafariConfigurationSubscriber

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/XPCServices/SafariConfigurationSubscriber.xpc/SafariConfigurationSubscriber`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.SafariShared.SafariConfigurationSubscriber</string>
	<key>com.apple.private.remotemanagement.subscriber</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.private.security.storage.Safari</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.remotemanagementd.store</string>
		<string>com.apple.RemoteManagementAgent.store</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.remotemanagement.SafariSubscriber</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<array>
		<string>com.apple.SafariShared.SafariConfigurationSubscriber</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.Safari.CredentialExtractionHelper

> `/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.CredentialExtractionHelper.xpc/com.apple.Safari.CredentialExtractionHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile</key>
	<string>temporary-sandbox</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 com.apple.Safari.SearchHelper

> `/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile</key>
	<string>SafariSearchHelper</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceMicrophone</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceMicrophone</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### com.apple.SpeechRecognitionCore.brokerd

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd`

```diff

 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.voicecontrol.speechrecognition.api</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>372</string>

```

### 🆕 ThumbnailsBlastDoorService

> `/System/Library/PrivateFrameworks/ThumbnailsBlastDoorSupport.framework/XPCServices/ThumbnailsBlastDoorService.xpc/ThumbnailsBlastDoorService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
	<true/>
	<key>com.apple.coregraphics.disableinmemoryfonts</key>
	<true/>
	<key>com.apple.coregraphics.disablepdf</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.hardened-process.hardened-heap</key>
	<true/>
	<key>com.apple.pac.shared_region_id</key>
	<string>BlastDoor</string>
	<key>com.apple.posterboardservices.disallowArchivingAppleArchive</key>
	<true/>
	<key>com.apple.private.pac.exception</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>blastdoor-thumbnails</string>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>blastdoor-post-launch</string>
	</array>
	<key>com.apple.private.security.message-filter</key>
	<true/>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>blastdoor-post-launch</string>
	</array>
</dict>
</plist>

```

### 🆕 VisualTestKit

> `/System/Library/PrivateFrameworks/VisualTestKit.framework/VisualTestKit`

- No entitlements *(yet)*
### CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic`

```diff

 	<array>
 		<string>dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:</string>
 	</array>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
 	<key>com.apple.private.pluginkit.persona</key>
 	<string>system</string>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/db/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.logd.admin</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>kCFPreferencesAnyApplication</string>

```
### ICQFollowup

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup`

```diff

 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

```

### 🆕 com.apple.corewifi.usernotifications

> `/System/Library/UserNotifications/Bundles/com.apple.corewifi.usernotifications.bundle/com.apple.corewifi.usernotifications`

- No entitlements *(yet)*
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Ocelot</string>
 		<string>Purchase</string>
 		<string>Library</string>
 		<string>IAPHistory</string>

```
### AppStoreWidgetsExtension

> `/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Ocelot</string>
 		<string>Purchase</string>
 		<string>Library</string>
 		<string>IAPHistory</string>

```
### AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.visioncompaniond</string>
 		<string>com.apple.wifip2pd</string>
+		<string>com.apple.watchlistd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.visioncompaniond.client</key>
 	<true/>
+	<key>com.apple.watchlist.private</key>
+	<true/>
 	<key>com.apple.wifi.events</key>
 	<true/>
 	<key>com.apple.wifi.events.private</key>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<array>
 		<string>Discoverability.Signals</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.calendar.allow-integrations</key>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>

```
### FindMyWidgetItems

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### FindMyWidgetPeople

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<key>com.apple.developer.group-session</key>
 	<true/>
 	<key>com.apple.developer.networking.carrier-constrained.app-optimized</key>
-	<true/>
+	<false/>
 	<key>com.apple.developer.networking.carrier-constrained.appcategory</key>
 	<string>hiking-8003</string>
 	<key>com.apple.developer.pass-type-identifiers</key>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.recovery</key>
+	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.launchservices.receivereferrerrurl</key>
+	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
 	<key>com.apple.passd.account</key>

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Ocelot</string>
 		<string>Purchase</string>
 		<string>Library</string>
 		<string>IAPHistory</string>

 	</array>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>com.apple.passd.payment</string>
 		<string>com.apple.payment.all-access</string>
 		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.ScreenTimeAgent.exception</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceEnergyKitGuidance</string>
+	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.tipsd</string>

```
### Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```diff

 	<array>
 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.Photos</string>
+		<string>com.apple.Stickers</string>
 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.carp</key>
+	<true/>
 	<key>com.apple.developer.corelocation.learned-routes-access</key>
 	<true/>
 	<key>com.apple.developer.corelocation.visit-history-access</key>

 	<true/>
 	<key>com.apple.private.carkit</key>
 	<true/>
+	<key>com.apple.private.carp</key>
+	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

 		<string>com.apple.kvsd</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.MFAAuthentication.MFAANetwork</string>
+		<string>com.apple.caraccessoryframework.cardata</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>

 		<string>com.apple.reminders</string>
 		<string>com.apple.mobileslideshow</string>
 	</array>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.mobilenotes</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```
### com.apple.mobilenotes.EditorExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.EditorExtension.appex/com.apple.mobilenotes.EditorExtension`

```diff

 	<string>com.apple.mobilenotes.EditorExtension</string>
 	<key>com.apple.PencilKit.allowsSnapToShape</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.systemstatus.activityattribution</string>
 		<string>com.apple.LinkPresentation.LinkSnapshotGeneratorService</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.mobilenotes.QuickLookExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.QuickLookExtension.appex/com.apple.mobilenotes.QuickLookExtension`

```diff

 	<string>com.apple.mobilenotes.QuickLookExtension</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

 	<array>
 		<string>com.apple.mobilenotes</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>508119322</string>
 	<key>platform-application</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.QuickboardViewService.textFieldDidInputText</key>
 	<true/>
 	<key>com.apple.StatusKit.publish.types</key>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/Applications/</string>
+		<string>/private/var/MobileDevice/ProvisioningProfiles/</string>
 		<string>/private/var/db/os_eligibility/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>

 		<string>com.apple.trial.status</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.BrowserEngineKit.Intermediary</string>
+		<string>com.apple.timed.xpc</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 				<true/>
 			</dict>
 		</dict>
+		<key>CrashReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>OSAnalytics.Stability.Crash</key>
+				<true/>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.mobileinstall.upgrade-enabled</key>
 	<true/>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 		<string>Discoverability.Signals</string>
 		<string>Discoverability.Usage</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.cloudphotod.access</key>

```
### PhotosNotificationsUpdates

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates`

```diff

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
 	<key>com.apple.private.photos.allowcollectionshare</key>

```
### com.apple.social.StreamShareService

> `/private/var/staged_system_apps/Photos.app/PlugIns/com.apple.social.StreamShareService.appex/com.apple.social.StreamShareService`

```diff

 		<key>value</key>
 		<string>com.apple.mobileslideshow</string>
 	</dict>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.contactsui</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

```
### RemindersSharingExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension`

```diff

 	<true/>
 	<key>com.apple.private.avfoundation.capture.allow</key>
 	<true/>
+	<key>com.apple.private.canGetAppLinkInfo</key>
+	<true/>
 	<key>com.apple.private.cloudkit.customAccounts</key>
 	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>

```
### VoiceMemosIntentsExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension`

```diff

 	</array>
 	<key>fairplay-client</key>
 	<string>511712240</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>group.com.apple.VoiceMemos.shared</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### VoiceMemosShareExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension`

```diff

 	</array>
 	<key>fairplay-client</key>
 	<string>511712240</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>group.com.apple.VoiceMemos.shared</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### VoiceMemos

> `/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos`

```diff

 	</array>
 	<key>fairplay-client</key>
 	<string>511712240</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>group.com.apple.VoiceMemos.shared</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

- No entitlements *(yet)*

### 🆕 libMTLHud.dylib

> `/usr/lib/libMTLHud.dylib`

- No entitlements *(yet)*

### 🆕 libffi-trampolines.dylib

> `/usr/lib/libffi-trampolines.dylib`

- No entitlements *(yet)*

### 🆕 libglInterpose.dylib

> `/usr/lib/libglInterpose.dylib`

- No entitlements *(yet)*

### 🆕 libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

- No entitlements *(yet)*

### 🆕 libobjc-trampolines.dylib

> `/usr/lib/libobjc-trampolines.dylib`

- No entitlements *(yet)*

### 🆕 libramrod.dylib

> `/usr/lib/libramrod.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.6.0.9.dylib

> `/usr/lib/libstdc++.6.0.9.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.6.dylib

> `/usr/lib/libstdc++.6.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.dylib

> `/usr/lib/libstdc++.dylib`

- No entitlements *(yet)*
### DumpPanic

> `/usr/libexec/DumpPanic`

```diff

 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
+	<key>com.apple.private.ApplePMGRUserClient.access</key>
+	<true/>
+	<key>com.apple.private.ApplePMGRUserClient.get-bpr</key>
+	<true/>
+	<key>com.apple.private.AppleSoCMiscUserClient.access</key>
+	<true/>
+	<key>com.apple.private.AppleSoCMiscUserClient.get-bpr</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>InverseDeviceID</string>

 		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
-	<string>AppleNVMeNamespaceUC</string>
+	<array>
+		<string>AppleSoCMiscUserClient</string>
+		<string>ApplePMGRUserClient</string>
+		<string>AppleNVMeNamespaceUC</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### MobileAssetEarlyBootTask

> `/usr/libexec/MobileAssetEarlyBootTask`

```diff

 	<true/>
 	<key>com.apple.private.vfs.graftdmg</key>
 	<true/>
+	<key>com.apple.rootless.storage.MobileAsset</key>
+	<true/>
 	<key>com.apple.rootless.volume.Update</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 		<string>com.apple.powerui.lowpowermode</string>
 		<string>com.apple.powerui.thermalmonitor</string>
 		<string>com.apple.powerui.smartcharging</string>
+		<string>com.apple.osintelligence.notifications</string>
 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>

```
### assetsubscriptiond

> `/usr/libexec/assetsubscriptiond`

```diff

 	<string>com.apple.assetsubscriptiond</string>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.keystore.lockassertion</key>
+	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.AppleIntelligence.Reporting.AssetDeliveryLog.UnifiedAssetFramework</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.UnifiedAssetFramework</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.backboardd</string>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>CarPlay.Connected</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Device.Display.TrueTone</string>

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>AttentionAwarenessCarPlayConnection</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>CarPlay.Connected</key>
+				<true/>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.iokit.rootdomain-set-property</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	</dict>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
+	<key>com.apple.private.kernel.read-write-trial-experiment-factors</key>
+	<true/>
 	<key>com.apple.private.kernel.selective-forced-idle</key>
 	<true/>
 	<key>com.apple.private.launchservices.allowedtolaunchinothersessions</key>

 	<array>
 		<string>com.apple.dasd-notifications</string>
 	</array>
+	<key>com.apple.private.write-kr-experiment-factors</key>
+	<true/>
 	<key>com.apple.purplebuddy.budd.access</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
-	<key>com.apple.developer.accessory-extension</key>
-	<true/>
 	<key>com.apple.developer.accessory-setup-discovery-extension</key>
 	<true/>
 	<key>com.apple.developer.accessory-transport-extension</key>

```
### gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GameController.gamecontrollerd</string>
+	<key>com.apple.backboardd.globalDeferringChainObserver</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### gamed

> `/usr/libexec/gamed`

```diff

 	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.GameOverlayUI</string>
+		<string>com.apple.ScreenTimeAgent.exception</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.shortcutitems.fullaccess</key>
 	<true/>
+	<key>com.apple.surfboard.CFUserNotification</key>
+	<true/>
 	<key>com.apple.telephony.cupolicy-monitor-access</key>
 	<true/>
 	<key>com.apple.telephony.cupolicy-rw-access</key>

```
### installd

> `/usr/libexec/installd`

```diff

 	<true/>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
+	</array>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>com.apple.usermanagerd.persona.grantSandboxExtension</key>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<true/>
 	<key>com.apple.keystore.dsme_access</key>
 	<true/>
+	<key>com.apple.keystore.lockassertion</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

 		<string>PURGEABLE_ENTITLEMENT</string>
 		<string>PURGE_SPECIAL_CASE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.InstallCoordination.OSModuleOperations</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileAsset.ManifestStorageService</key>

 	<true/>
 	<key>com.apple.private.img4.nonce.cryptex1.asset</key>
 	<true/>
+	<key>com.apple.private.img4.nonce.cryptex1.mobile-asset.code-install</key>
+	<true/>
+	<key>com.apple.private.img4.nonce.cryptex1.mobile-asset.code-load</key>
+	<true/>
 	<key>com.apple.private.img4.nonce.pdi</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

 	<key>com.apple.private.pmap.load-trust-cache</key>
 	<array>
 		<string>personalized.mobile-asset-brain</string>
+		<string>personalized.mobile-asset-code</string>
 	</array>
 	<key>com.apple.private.security.AppleImage4.user-client</key>
 	<true/>

 	<true/>
 	<key>com.apple.rootless.volume.Update</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleKeyStoreUserClient</string>
 		<string>AppleImage4UserClient</string>
 		<string>IOHDIXControllerUserClient</string>
 	</array>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/System/Library/CoreServices/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_GuardrailFramework/</string>
+		<string>/AppleInternal/Assets/SecureMobileAssets/com.apple.MobileAsset.CN.GuardrailFramework/com.apple.rsa.wrapperapp.generic/Source/Applications/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.rapportd</string>
+	</array>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>

 	<true/>
 	<key>com.apple.runningboard.assertions.rapportd</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.rapportd</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>IOHIDLibUserClient</string>

```
### replayd

> `/usr/libexec/replayd`

```diff

 		<string>group.com.apple.replayd</string>
 		<string>group.com.apple.portrait.BackgroundReplacement</string>
 	</array>
+	<key>com.apple.private.security.storage.AppDataContainers</key>
+	<true/>
 	<key>com.apple.private.skylight.expanse</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<true/>
 	<key>com.apple.security.device.microphone</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/Mobile Documents/</string>
+		<string>/private/var/mobile/Containers/Shared/AppGroup/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

 		<string>com.apple.applicationaccess</string>
 		<string>com.apple.camera</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-write</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.selectivesharing.session_system</key>

```
### routined

> `/usr/libexec/routined`

```diff

 	</array>
 	<key>com.apple.timed</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>LOMO_CHECK_IN</string>
+	</array>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 		<string>apple-safety-alert</string>
 		<string>spi</string>
 	</array>
+	<key>com.apple.CoreRoutine.LocationOfInterest</key>
+	<true/>
 	<key>com.apple.CoreRoutine.PeopleDiscovery</key>
 	<true/>
 	<key>com.apple.CoreRoutine.StoredLocation</key>

 	<true/>
 	<key>com.apple.driver.AppleConvergedIPCICEBBControl.user-access</key>
 	<true/>
+	<key>com.apple.geoservices.map-subscriptions</key>
+	<array>
+		<string>com.apple.safetyalertsd.*</string>
+	</array>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 		<string>/private/var/mobile/Library/CoreBehavior/BehaviorMiner.sqlite</string>
 		<string>/private/var/mobile/Library/CoreBehavior/BehaviorMiner.sqlite-shm</string>
 		<string>/private/var/mobile/Library/CoreBehavior/BehaviorMiner.sqlite-wal</string>
-		<string>/private/var/mobile/Library/com.apple.sharingd/ShareSheetTestingSnapshots/</string>
 		<string>/private/var/tmp/MRQL</string>
 		<string>/private/var/tmp/MRQL/AirDrop/</string>
+		<string>/private/var/tmp/ShareSheetTestingSnapshots/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled.profile</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.nearbyd.diagnostics</key>
 	<true/>
 	<key>com.apple.networkrelay.diagnostic</key>

```
### uarpd

> `/usr/libexec/uarpd`

```diff

 	<string>com.apple.uarpd</string>
 	<key>com.apple.corespeech.xpc</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+	</array>
 	<key>com.apple.private.osanalytics.write-logs.allow</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.SBUserNotification</string>
-		<string>com.apple.installerauthagent</string>
 		<string>com.apple.AppSSO.service-xpc</string>
+		<string>com.apple.geod</string>
+		<string>com.apple.installerauthagent</string>
+		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.uarpassetmanager.uarp</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.GEO</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.ist.ds.appleconnect.mobile.external</string>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
 	<key>com.apple.private.corewifi.keychain</key>

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.wifid.usernotification</string>
+		<string>com.apple.corewifi.usernotifications</string>
 	</array>
 	<key>com.apple.private.wifianalytics</key>
 	<true/>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.centaurid.xpc</string>
+		<string>com.apple.AccessorySetupUI</string>
+		<string>com.apple.AccessorySetupUI.services.presenter</string>
+		<string>com.apple.lsd.mapdb</string>
+		<string>com.apple.lsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
