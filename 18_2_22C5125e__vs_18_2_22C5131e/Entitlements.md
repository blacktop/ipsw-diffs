## 🔑 Entitlements

### AppDeletionUIHost

> `/Applications/AppDeletionUIHost.app/AppDeletionUIHost`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CommCenter.StormBreaker</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.springboard.homeScreenIconStyle</key>

```
### FinanceUIService

> `/Applications/FinanceUIService.app/FinanceUIService`

```diff

 		<string>com.apple.financed.service.coredatastore</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.WalletBlastDoorService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SharingUIService

> `/Applications/SharingUIService.app/SharingUIService`

```diff

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 </dict>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.nanoregistryd</string>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.TouchRemote</string>
 		<string>com.apple.siri.textinput</string>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	<array>
 		<string>/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice</string>
-		<string>/Library/VoiceServices/Assets</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.announce/</string>

 	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>
 	<true/>
+	<key>com.apple.sirittsd.can-dump-audio</key>
+	<true/>
 	<key>com.apple.springboard.display-lookup</key>
 	<true/>
 	<key>com.apple.springboard.flash-color</key>

 		<string>access-call-providers</string>
 		<string>access-calls</string>
 	</array>
-	<key>com.apple.voiced.can-dump-audio</key>
-	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>fairplay-client</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 		<string>com.apple.RemoteDisplay</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-calls</string>
+	</array>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>581</string>

```
### iCloud+

> `/Applications/iCloud+.app/iCloud+`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### appplaceholdersyncd

> `/System/Library/CoreServices/appplaceholdersyncd`

```diff

 <dict>
 	<key>com.apple.appplaceholdersyncd.replicatorclient</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>InstallForInstallCoordination</string>

 	<array>
 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.mobile.installd</string>
+		<string>com.apple.appprotectiond.read</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.appplaceholdersyncd</string>
 	</array>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension`

```diff

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.AssetMetricsWorker</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.feedbacklogger</string>

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.AssetMetricsWorker</string>
+	</array>
 </dict>
 </plist>
 

```
### DefaultAppsSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DefaultAppsSettingsIntents.appex/DefaultAppsSettingsIntents`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
+	<string>com.apple.Preferences</string>
+	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
+	<string>com.apple.Preferences</string>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
+</dict>
+</plist>
 

```

### 🆕 SoundAndHapticsControls

> `/System/Library/ExtensionKit/Extensions/SoundAndHapticsControls.appex/SoundAndHapticsControls`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
</dict>
</plist>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<true/>
 	<key>com.apple.mobileassetd.v2</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.WalletBlastDoorService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.mdmd-access</key>
+	<true/>
 	<key>com.apple.mobileactivationd.bridge</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.managedconfiguration.mdmdservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.CacheDelete</key>
+	<array>
+		<string>CLIENT_ENTITLEMENT</string>
+		<string>PURGE_ENTITLEMENT</string>
+	</array>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.asr</key>
 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.borealis</key>

 		<string>SiriDictation</string>
 		<string>Siri.SelfTriggerSuppression</string>
 		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
+		<string>Siri.ASR.RequestMetricsRecord</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 	</array>
 	<key>com.apple.private.iokit.darkwake-control</key>
 	<true/>
+	<key>com.apple.private.kernel.global-proc-info</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.isusingbuiltinmicforrecording.allow</key>

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.uservault</string>
 		<string>com.apple.assistant.domain.audio.level.service</string>
+		<string>com.apple.cache_delete</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.ironwood.support</string>

 		<string>com.apple.UIKit</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.assistant.domain.preferences</string>
+		<string>com.apple.keyboard.preferences</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>kern.exclaves_status</string>
 		<string>kern.task_conclave</string>
 	</array>
+	<key>com.apple.security.get-task-allow</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.server.bluetooth</string>

 	<true/>
 	<key>com.apple.siri.external_request</key>
 	<true/>
+	<key>com.apple.system-task-ports.name.safe</key>
+	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>
 	<true/>
 	<key>com.apple.systemstatus.publisher.domains</key>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 		<string>/Library/Caches/PassKit/</string>
 		<string>/Library/UserConfigurationProfiles/</string>
 		<string>/Library/Preferences/com.apple.purplebuddy.plist</string>
+		<string>/Library/Caches/com.apple.businessservicesd/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.icloudmailagent.secret.xpc</string>
+		<string>com.apple.businessservicesd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	<array>
 		<string>Library/Photos/Libraries/Syndication.photoslibrary/private/com.apple.mediaanalysisd/</string>
 		<string>Library/Caches/com.apple.HomeKit/com.apple.mediaanalysisd/</string>
+		<string>Library/Caches/com.apple.VisualIntelligence/</string>
 		<string>Library/MediaAnalysis/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	<array>
 		<string>Library/Photos/Libraries/Syndication.photoslibrary/private/com.apple.mediaanalysisd/</string>
 		<string>Library/Caches/com.apple.HomeKit/com.apple.mediaanalysisd/</string>
+		<string>Library/Caches/com.apple.VisualIntelligence/</string>
 		<string>Library/MediaAnalysis/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 		<string>com.apple.private.alloy.applepay</string>
 		<string>com.apple.private.alloy.applepay.sharing</string>
 	</array>
+	<key>com.apple.private.ids.phone-number-authentication</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.passd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice</string>
 		<string>/Library/UserConfigurationProfiles/</string>
-		<string>/Library/VoiceServices/Assets</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.sirittsd</string>
 		<string>com.apple.speech.localspeechrecognition</string>
 		<string>com.apple.translationd</string>
-		<string>com.apple.voiceservices.keepalive</string>
-		<string>com.apple.voiceservices.tts</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.sirittsd.can-dump-audio</key>
+	<true/>
 	<key>com.apple.springboard.display-lookup</key>
 	<true/>
 	<key>com.apple.springboard.flash-color</key>

 		<string>access-call-providers</string>
 		<string>access-calls</string>
 	</array>
-	<key>com.apple.voiced.can-dump-audio</key>
-	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>fairplay-client</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<array>
 		<string>/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice</string>
-		<string>/Library/VoiceServices/Assets</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.announce/</string>

 	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>
 	<true/>
+	<key>com.apple.sirittsd.can-dump-audio</key>
+	<true/>
 	<key>com.apple.springboard.display-lookup</key>
 	<true/>
 	<key>com.apple.springboard.flash-color</key>

 		<string>access-call-providers</string>
 		<string>access-calls</string>
 	</array>
-	<key>com.apple.voiced.can-dump-audio</key>
-	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>fairplay-client</key>

```
### ind

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/ind`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>PURGEABLE_ENTITLEMENT</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 		<string>com.apple.Wallet</string>
 		<string>com.apple.HearingAids</string>
 		<string>com.apple.NanoHome</string>
+		<string>com.apple.Sharing</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Calculator

> `/private/var/staged_system_apps/Calculator.app/Calculator`

```diff

 	<string>com.apple.calculator</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<array>
 		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.appprotectiond.read</string>
+	</array>
 	<key>file-read-data</key>
 	<true/>
 	<key>file-write-data</key>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.HearingModeService</string>
 		<string>com.apple.AudioAccessoryServices</string>
+		<string>com.apple.controlcenter.remoteservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.icloudmailagent.secret.xpc</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 		<string>com.apple.generativeexperiences.textcomposition</string>
 		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.proactive.PersonalizationPortrait.Contact</string>
+		<string>com.apple.icloudmailagent.secret.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	<string>ZL6BUSYGB3.com.apple.news</string>
 	<key>com.apple.appstored.manage-iap</key>
 	<true/>
+	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.fileprovider.extension-host</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice</string>
 		<string>/Library/DuetExpertCenter/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
 		<string>/Library/UserConfigurationProfiles/</string>
-		<string>/Library/VoiceServices/Assets</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Media/PhotoData/</string>
 	</array>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>

 		<string>com.apple.sleepd.sleepserver</string>
 		<string>com.apple.systemactions</string>
 		<string>com.apple.translationd</string>
-		<string>com.apple.voiceservices.keepalive</string>
-		<string>com.apple.voiceservices.tts</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.sirittsd.can-dump-audio</key>
+	<true/>
 	<key>com.apple.soundscapes.picker</key>
 	<true/>
 	<key>com.apple.springboard.addWebClipToHomeScreen</key>

 	<array>
 		<string>180</string>
 	</array>
-	<key>com.apple.voiced.can-dump-audio</key>
-	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.inputAnalytics.serverStats</string>
 		<string>com.apple.inputAnalytics.IASWTAnalyzer</string>
 		<string>com.apple.inputAnalytics.IASSRAnalyzer</string>
+		<string>com.apple.inputAnalytics.IASGenmojiAnalyzer</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.inputanalyticsd</string>
 	<key>com.apple.security.ts.xpc-service-name</key>
 	<string>com.apple.duetactivityscheduler</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.openai</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### mdmuserd

> `/usr/libexec/mdmuserd`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.launchservices.changedefaulthandlers</key>
+	<array>
+		<string>http</string>
+		<string>https</string>
+	</array>
 	<key>com.apple.private.remotemanagement.enrollment</key>
 	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
+		<string>/private/var/run/MobileAssetCritialDomainsUpdated.plist</string>
 		<string>/private/var/code_coverage/</string>
 		<string>/private/var/run/com.apple.mobileassetd-AutoAsset-DeviceBoot-UUID</string>
 	</array>

```
### nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.NanoRegistryPairingCompatibilityIndex</string>
+	</array>
 	<key>com.apple.private.controlcenter.service.moduleidentifiers</key>
 	<array>
 		<string>com.apple.PingMyWatchControlCenterUI</string>

```
