## 🔑 Entitlements

### Camera

> `/Applications/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
 	<key>com.apple.nfcd.assertion.handover</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

 	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
+	</array>
 	<key>com.apple.private.assetsd.nebulad.access</key>
 	<string>camera</string>
 	<key>com.apple.private.avfoundation.capture.deferred-photo-processor.allow</key>
 	<true/>
 	<key>com.apple.private.barcodesupport.allowNotifications</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<array>
 		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_MagicCleanup/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Media/PhotoData/</string>
 		<string>/Library/Caches/com.apple.ClipServices/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.RemoteDisplay</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.CameraOverlayAngel.application-service</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.SocialLayer</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### LockScreenCamera

> `/Applications/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	<true/>
 	<key>com.apple.private.barcodesupport.allowNotifications</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<true/>
 	<key>com.apple.spotlight.search</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>

```
### Feedback Assistant iOS

> `/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.storage.Notes</key>
+	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.feedback</string>
+		<string>group.com.apple.notes</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
-		<string>/var/mobile/Library/Application Support/com.apple.palette.green.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/Library/MessagesMetaData/NickNameCache/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 		<string>/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/Library/Application Support/com.apple.palette.green.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 		<string>823</string>
 		<string>824</string>
 	</array>
+	<key>com.apple.wallet.application-authorization.ui</key>
+	<true/>
 	<key>com.apple.wallet.banner</key>
 	<true/>
 	<key>com.apple.wallet.features.all-access</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.feedbacklogger</key>
+	<true/>
 	<key>com.apple.private.fileprovider.storage-management</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>ProactiveAppPrediction</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Notification.Usage</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>

 	<key>com.apple.private.usernotifications.settings</key>
 	<array>
 		<string>read</string>
+		<string>write</string>
 	</array>
 	<key>com.apple.private.webbookmarks.settings</key>
 	<true/>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.attributionkitd.xpc.developer-mode</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.photos.picker</string>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
+		<string>com.apple.usernotificationskit</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 SESUIServiceApp

> `/Applications/SESUIServiceApp.app/SESUIServiceApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>SESUIServiceApp</string>
	<key>com.apple.runningboard.assertions.angeltarget</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 	<true/>
 	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
 	<true/>
+	<key>com.apple.private.sessionkit.presentationAssertionRequester</key>
+	<true/>
+	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>
+	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>
 	<true/>
+	<key>com.apple.appleaccount.custodian</key>
+	<true/>
 	<key>com.apple.appletv.pbs.allow-screen-saver</key>
 	<true/>
 	<key>com.apple.appletv.pbs.display-manager-service-access</key>

 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone14x</string>
 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x</string>
 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPad</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
+	<key>com.apple.private.ids.phone-number-authentication</key>
+	<true/>
 	<key>com.apple.private.ids.registration</key>
 	<true/>
 	<key>com.apple.private.ids.registration-control</key>

 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ProactiveAppPrediction</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Notification.Usage</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>

 	</array>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
+	<key>com.apple.private.usernotifications.settings</key>
+	<array>
+		<string>read</string>
+		<string>write</string>
+	</array>
 	<key>com.apple.private.webinspector.allow-remote-inspection</key>
 	<true/>
 	<key>com.apple.purplebuddy.budd.access</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.notes</string>
+		<string>group.com.apple.CoreSpeech</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.aa.custodian.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.DeviceActivity</string>
+		<string>com.apple.usernotificationskit</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.systemaperture</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### AccessibilityAppIntents

> `/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.MagnifierAngel.client</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.launchservices.clearadvertisingid</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
 	<key>com.apple.localizationswitcher</key>

 	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.donotdisturb.0191488e-ff8a-728d-a9f7-08a0a77abd7d.update.client-identifiers</key>
+	<array>
+		<string>com.apple.private.SpringBoard.focus.0191488e-ff8a-728d-a9f7-08a0a77abd7d</string>
+	</array>
 	<key>com.apple.private.donotdisturb.behavior.resolution.client-identifiers</key>
 	<array>
 		<string>com.apple.springboard.SBBulletinSpokenObserverGateway</string>

```
### IntelligenceIntentsExtension

> `/System/Library/ExtensionKit/Extensions/IntelligenceIntentsExtension.appex/IntelligenceIntentsExtension`

```diff

 		<string>com.apple.ess</string>
 		<string>com.apple.private.ac</string>
 	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/CallDirectory/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### ToggleCellularDataModeExtension

> `/System/Library/ExtensionKit/Extensions/ToggleCellularDataModeExtension.appex/ToggleCellularDataModeExtension`

```diff

 	</array>
 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
 </dict>

```
### com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskTelemetry</string>
 		<string>Lighthouse.Ledger.DeviceTelemetry</string>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>

```
### AVAudioDeviceTestService

> `/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>Signpost-Persisted</key>
+	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
 	<key>com.apple.multitasking.systemappassertions</key>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.cache_delete.public</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.carousel.unlimited_backlight_assertion</key>
 	<true/>
+	<key>com.apple.chrono.descriptorEnablement</key>
+	<array>
+		<string>com.apple.Mind.MindComplication</string>
+	</array>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>
 	<true/>
+	<key>com.apple.dmd.operation.set-app-allow-user-to-hide</key>
+	<true/>
+	<key>com.apple.dmd.operation.set-app-allow-user-to-lock</key>
+	<true/>
 	<key>com.apple.dmd.operation.set-app-associated-domains</key>
 	<true/>
 	<key>com.apple.dmd.operation.set-app-associated-domains-enable-direct-downloads</key>

```

### 🆕 CallRecordingSettingsBundle

> `/System/Library/PreferenceBundles/CallRecordingSettingsBundle.bundle/CallRecordingSettingsBundle`

- No entitlements *(yet)*
### ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

```diff

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>com.apple.carplay</string>
 		<string>com.apple.ClarityUI</string>
 		<string>com.apple.CloudKit</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.GEO</string>
 		<string>com.apple.gms.availability</string>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.private.health.heart-rhythm</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.usernotificationskit</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.GenerativeFunctions.generativeexperiencesd/</string>
+		<string>/Library/AppleIntelligencePlatform/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.Accessibility</string>
 		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
+		<string>com.apple.applicationaccess</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### IMTranscoderAgent

> `/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>IMTranscoderAgent</string>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd`

```diff

 <dict>
 	<key>abs-client</key>
 	<string>1516615657</string>
+	<key>application-identifier</key>
+	<string>AAPLPHOTOS.com.apple.mstreamd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	</array>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
+	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
+	<dict>
+		<key>com.apple.icloud-photos.fdb</key>
+		<string>Photos</string>
+	</dict>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
+	<key>com.apple.private.cloudkit.systemService</key>
+	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>
-		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceLiverpool</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
-	<key>com.apple.private.biome.client-identifier</key>
-	<string>com.apple.modelcatalogd</string>
-	<key>com.apple.private.biome.read-write</key>
-	<array>
-		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
-	</array>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
-	<key>com.apple.security.exception.files.home-relative-path.read</key>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/AppleIntelligencePlatform/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 MomentsIntelligenceService

> `/System/Library/PrivateFrameworks/MomentsIntelligence.framework/XPCServices/MomentsIntelligenceService.xpc/MomentsIntelligenceService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/eligibilityd/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
	</array>
</dict>
</plist>

```
### PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.itunesstored</string>
+		<string>com.apple.MomentsIntelligenceService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 		<string>Photos.Curation</string>
 		<string>Photos.Delete</string>
 		<string>Photos.Search</string>
+		<string>Photos.Memories.Shared</string>
+		<string>Photos.Memories.Viewed</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 		<string>Photos.Curation</string>
 		<string>Photos.Delete</string>
 		<string>Photos.Search</string>
+		<string>Photos.Memories.Shared</string>
+		<string>Photos.Memories.Viewed</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 		<string>Photos.Curation</string>
 		<string>Photos.Delete</string>
 		<string>Photos.Search</string>
+		<string>Photos.Memories.Shared</string>
+		<string>Photos.Memories.Viewed</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```
### replicatord

> `/System/Library/PrivateFrameworks/ReplicatorCore.framework/Support/replicatord`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
-	<key>com.apple.linkd.registry</key>
-	<true/>
 	<key>com.apple.linkd.registry.waitforready</key>
 	<true/>
-	<key>com.apple.linkd.transcript.privileged</key>
-	<true/>
 	<key>com.apple.localizationswitcher</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<string>group.com.apple.replicatord</string>
-	<key>com.apple.private.security.storage.AppDataContainers</key>
-	<true/>
 	<key>com.apple.private.security.storage.replicatord</key>
 	<true/>
 	<key>com.apple.private.skywalk.observe-stats</key>

 	<true/>
 	<key>com.apple.private.skywalk.register-user-pipe</key>
 	<true/>
-	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceSystemPolicyAppData</string>
-	</array>
 	<key>com.apple.private.tcc.events.subscriber</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```
### budd

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/budd`

```diff

 		<string>com.apple.backlightd</string>
 		<string>com.apple.SecureBackupDaemon.concurrent</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.gms.availability</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.usernotificationskit</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### SiriGeoIntentExtension

> `/System/Library/PrivateFrameworks/SiriGeo.framework/PlugIns/SiriGeoIntentExtension.appex/SiriGeoIntentExtension`

```diff

 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.Maps.xpc.SharedTrip</string>
+		<string>com.apple.Maps.xpc.SharedTrip.Capabilities</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read</key>
 	<array>

```

### 🆕 SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsBookkeepingService.xpc/SiriSuggestionsBookkeepingService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.MobileAsset.SoftwareUpdate</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.internal.intelligenceplatform.use-cases</key>
	<dict>
		<key>SiriIntelligencePlatform</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>App.InFocus</string>
				<string>Device.ScreenLocked</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>AppIntent</string>
		<string>siriRemembers</string>
		<string>App.InFocus</string>
		<string>UserFocus.ComputedMode</string>
		<string>Media.NowPlaying</string>
		<string>Motion.Activity</string>
		<string>CarPlay.Connected</string>
		<string>Location.Semantic</string>
		<string>Device.ScreenLocked</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Siri.Remembers.MessageHistory</string>
		<string>Siri.Remembers.CallHistory</string>
		<string>Siri.Remembers.InteractionHistory</string>
		<string>Siri.Remembers.AudioHistory</string>
		<string>Siri.Remembers.AssistantSuggestions</string>
		<string>Siri.PostSiriEngagement</string>
		<string>Siri.Audio.CompanionContext</string>
	</array>
	<key>com.apple.private.biome.sync</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>siriRemembers</string>
	</array>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.siri.userfeedbacklearning</string>
	</array>
	<key>com.apple.private.security.storage.SiriInference</key>
	<true/>
	<key>com.apple.private.sqlite.sqlite-encryption</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.HomeKit/com.apple.siriinferenced/</string>
		<string>/Library/Caches/com.apple.siriinferenced/</string>
		<string>/Library/com.apple.siri.inference/</string>
		<string>/Library/srtest/</string>
		<string>/Library/AddressBook/</string>
		<string>/Library/Preferences/com.apple.suggestions.plist</string>
		<string>/Library/IntelligencePlatform/</string>
		<string>/Library/Shortcuts/ToolKit/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.accountsd.accountmanager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.suggestions</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siriinferenced</string>
		<string>com.apple.siri.PostSiriEngagement</string>
		<string>com.apple.siriinference-dodml-plugin</string>
		<string>com.apple.siri.DialogEngine</string>
		<string>com.apple.assistant</string>
		<string>com.apple.siri.sirisuggestions</string>
		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
		<string>com.apple.siriinferenced.AppOrdering</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
	<key>com.apple.siriinferenced</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>1343</string>
	</array>
	<key>seatbelt-profiles</key>
	<array>
		<string>temporary-sandbox</string>
	</array>
</dict>
</plist>

```
### StocksKitService

> `/System/Library/PrivateFrameworks/StocksKit.framework/XPCServices/StocksKitService.xpc/StocksKitService`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>

```
### wirelessinsightsd

> `/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

 	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
 	<key>com.apple.private.CoreAnalytics.ObserveEvents.allow</key>

```

### 🆕 homerecommendationutil

> `/System/Library/PrivateFrameworks/homerecommendationutil`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.homekit</key>
	<true/>
	<key>com.apple.developer.homekit.allow-setup-payload</key>
	<true/>
	<key>com.apple.homekit.private-internal-access</key>
	<dict>
		<key>OverrideLocationBundleIdentifier</key>
		<string>com.apple.HomeRecommendationUtil</string>
	</dict>
	<key>com.apple.homekit.private-spi-access</key>
	<true/>
	<key>com.apple.private.homekit.cameraclips</key>
	<true/>
	<key>com.apple.private.homekit.connectivity-info</key>
	<true/>
	<key>com.apple.private.homekit.home-location</key>
	<true/>
	<key>com.apple.private.homekit.location</key>
	<true/>
	<key>com.apple.private.homekit.multi-user.setup</key>
	<true/>
	<key>com.apple.private.homekit.remote-login.private</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceWillow</string>
	</array>
</dict>
</plist>

```

### 🆕 SiriKitFlowSnippetUIPlugin

> `/System/Library/Snippets/UIPlugins/SiriKitFlowSnippetUIPlugin.bundle/SiriKitFlowSnippetUIPlugin`

- No entitlements *(yet)*

### 🆕 csfdiagnose

> `/usr/bin/csfdiagnose`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>re6Zb+zwFKJNlkQTUeT+/w</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.ind.client</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.ind.cloudfeatures</string>
		<string>com.apple.adid</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.corefollowup.agent</string>
		<string>com.apple.ind.xpc</string>
		<string>com.apple.mobile.keybagd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.Security</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.cloud.quota</string>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.CloudSubscriptionFeatures.cache</string>
		<string>com.apple.CloudSubscriptionFeatures.geoCache</string>
		<string>com.apple.CloudSubscriptionFeatures.ticket.cache</string>
		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
</dict>
</plist>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.modelmanager.assertion</key>
 	<true/>
+	<key>com.apple.modelmanager.inferenceMonitor</key>
+	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.AirPlayRoutePrediction</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>

```
### carkitd

> `/usr/libexec/carkitd`

```diff

 		<string>com.apple.SharingServices</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.TapToRadarKit.service</string>
+		<string>com.apple.sysdiagnose.service.xpc</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 		<string>com.apple.private.intelligenceplatform.views.read-only</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.MomentsIntelligenceService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>nsurlsessiond</string>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceUserTracking</string>
+	</array>
 	<key>com.apple.rootless.storage.MobileAssetDownload</key>
 	<true/>
 	<key>com.apple.rootless.storage.com.apple.MobileAsset.DuetExpertCenterAsset</key>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
