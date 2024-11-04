## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.AMSEngagementViewService</string>
+	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

 	<string>1445028844</string>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.openai</string>
 		<string>apple</string>
 	</array>
 </dict>

```
### AppDeletionUIHost

> `/Applications/AppDeletionUIHost.app/AppDeletionUIHost`

```diff

 <dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
 </dict>

```
### AuthenticationServicesUI

> `/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 		<string>com.apple.sharingd</string>
 		<string>com.apple.AuthenticationServices.AutoFill</string>
 		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>

```
### BarcodeScanner

> `/Applications/BarcodeScanner.app/BarcodeScanner`

```diff

 	</array>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
-	<key>com.apple.springboard.allowallcallurls</key>
-	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>

```
### Diagnostic-7004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.DiagnosticsKit.diagnosticmanager</key>
+	<true/>
+	<key>com.apple.DiagnosticsKit.extension</key>
+	<true/>
+	<key>com.apple.private.corerepair.xpc</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.corerepair</string>
+		<string>com.apple.diskimagecorerepair</string>
+		<string>com.apple.appleh13camerad</string>
+		<string>com.apple.appleh16camerad</string>
+	</array>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
+</dict>
+</plist>
 

```
### Feedback Assistant iOS

> `/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS`

```diff

 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
-	<key>com.apple.private.photos.service.librarymanagement</key>
-	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.Notes</key>
 	<true/>
-	<key>com.apple.private.security.storage.PhotosLibraries</key>
-	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
-		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.feedback</string>
-		<string>group.com.apple.notes</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.fenceservice</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.coreservices.appleid.authentication</string>
 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.pairingmanager</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.iphone.axserver</string>
 		<string>com.apple.internal.studylogd</string>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
+	<key>com.apple.springboard.openurlswhenlocked</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>

```
### HomeControlService

> `/Applications/HomeControlService.app/HomeControlService`

```diff

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

```
### HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
 	<key>com.apple.idle-timer-services</key>
 	<true/>

 	<array>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.coreduetd.knowledge</string>
-		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.matter.support.xpc</string>

 	<array>
 		<string>com.apple.Home.group</string>
 		<string>com.apple.avfaudio</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.voicetrigger.notbackedup</string>

 	<array>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.coreduetd.knowledge</string>
-		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.matter.support.xpc</string>

 	<array>
 		<string>com.apple.Home.group</string>
 		<string>com.apple.avfaudio</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.voicetrigger.notbackedup</string>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
-	<key>com.apple.developer.healthkit</key>
+	<key>com.apple.developer.calling-app</key>
 	<true/>
-	<key>com.apple.developer.phone-app</key>
+	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.usernotifications.communication</key>
 	<true/>

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceCalendar</string>
+		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>

 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callhistorycontroller</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callhistorymanager</string>
 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.voicememod.xpc</string>
 		<string>com.apple.spotlight.IndexAgent</string>

```
### PCViewService

> `/Applications/PCViewService.app/PCViewService`

```diff

 	<true/>
 	<key>com.apple.MobileAsset.SharingDeviceAssets</key>
 	<true/>
+	<key>com.apple.ProximityControl.ProximityHandoffInteractions</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>

```
### PosterBoard

> `/Applications/PosterBoard.app/PosterBoard`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.PosterPlatformSupportBundleService</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.backboard.display.services</string>

```

### 🆕 PosterPlatformSupportBundleService

> `/Applications/PosterBoard.app/XPCServices/PosterPlatformSupportBundleService.xpc/PosterPlatformSupportBundleService`

- No entitlements *(yet)*
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.bannerkit.post</key>
 	<true/>
+	<key>com.apple.batteryintelligenced.chargetimeestimator-read</key>
+	<true/>
 	<key>com.apple.bluetooth.custom.properties.writable</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

 			<string>1</string>
 		</dict>
 	</dict>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>IAPHistory</string>
+	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.WalletMobileAssets</string>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.lsd.modifydb</string>
+		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.nfcd.session.trust</key>
 	<true/>
+	<key>com.apple.os-eligibility-domain.change.molybdenum</key>
+	<true/>
 	<key>com.apple.passes.add-silently</key>
 	<true/>
 	<key>com.apple.payment.all-access</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage.SetDSLModeEnabled</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.SetDSLStrictModeEnabled</key>
+	<true/>
 	<key>com.apple.private.MobileActivation</key>
 	<array>
 		<string>GetActivationState</string>

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.private.messages.associated-message-extension-bundle-identifiers</key>
+	<array>
+		<string>com.apple.AppleAccountUI.CustodianInviteMessageExtension</string>
+	</array>
 	<key>com.apple.private.mobilestoredemo.enabledemo</key>
 	<array>
 		<string>Enroll</string>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist </string>
 		<string>/private/var/containers/Shared/SystemGroup/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.aa.custodian.xpc</string>
+		<string>com.apple.aa.inheritance.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.biome.access.user</string>

```
### SharingUIService

> `/Applications/SharingUIService.app/SharingUIService`

```diff

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
-	<key>com.apple.springboard.homeScreenIconStyle</key>
-	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 </dict>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.sharing.headphonetutorialcards</string>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>

 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.HRTFEnrollmentService</string>
-		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.icloud.searchpartyd.accessorydiscoverysession</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.pairingmanager</string>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
 		<string>/private/var/mobile/Library/Assistant/AssistantSampled/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/tmp/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.activation.service</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>

 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.siri.activation.service</key>
+	<true/>
 	<key>com.apple.siri.analytics.assistant</key>
 	<array>
 		<string>stream.unifiedMessageStream.readonly</string>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<string>com.apple.StickerPickerService</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>com.apple.animoji</string>
 	</array>
+	<key>com.apple.spotlight.entitledattributes</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.surfboard-prevent-linking-for-restoration</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.parsec.default-client</key>
 	<string>com.apple.VisualIntelligenceCamera</string>
 	<key>com.apple.private.payment.remote-network-payment-initiate</key>

 		<string>586</string>
 		<string>313</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### VideoSubscriberAccountViewService

> `/Applications/VideoSubscriberAccountViewService.app/VideoSubscriberAccountViewService`

```diff

 <dict>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
-	<key>com.apple.VideoSubscriberAccount.AnalyticsService.ReportMetricsEvents</key>
-	<true/>
 	<key>com.apple.VideoSubscriberAccount.DeveloperService</key>
 	<true/>
 	<key>com.apple.VideoSubscriberAccount.PrivacyService</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.VideoSubscriberAccount.AnalyticsService</string>
 		<string>com.apple.VideoSubscriberAccount.PrivacyService</string>
 		<string>com.apple.VideoSubscriberAccount.DeveloperService</string>
 	</array>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/Applications/WritingToolsUIService.app/WritingToolsUIService</string>
+	</dict>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.userprofiles.read</key>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.openai</string>
+	</array>
 </dict>
 </plist>
 

```
### iCloud

> `/Applications/iCloud.app/iCloud`

```diff

 	<string>com.apple.CloudKit.ShareBear</string>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
 	<key>com.apple.developer.icloud-services</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.gamed</string>
 		<string>com.apple.bird</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.appprotectiond.guard</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.backboardd.global-pointer-event-routing</key>
 	<true/>
+	<key>com.apple.backboardd.hitTestContextCategory</key>
+	<true/>
 	<key>com.apple.backboardd.pointerPreferences</key>
 	<true/>
 	<key>com.apple.backboardd.pointerRepositioning</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.mediaremote</string>
 		<string>com.apple.InputModePreferences</string>
 		<string>com.apple.compass</string>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	<true/>
 	<key>com.apple.backboardd.global-pointer-event-routing</key>
 	<true/>
+	<key>com.apple.backboardd.hitTestContextCategory</key>
+	<true/>
 	<key>com.apple.backboardd.launchapplications</key>
 	<true/>
 	<key>com.apple.backboardd.pointerRepositioning</key>

 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
 		<string>com.apple.mediaaccessibility</string>
+		<string>com.apple.springboard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SafariBookmarksSyncAgent

> `/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent`

```diff

 	</array>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.safari</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.spotlight.IndexAgent</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.lsuseractivityd.bestappsuggestion</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```

### 🆕 FindMyPeopleDigitalSeparation

> `/System/Library/DigitalSeparation/SharingSources/FindMyPeopleDigitalSeparation.bundle/FindMyPeopleDigitalSeparation`

- No entitlements *(yet)*
### AutocompleteAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/AutocompleteAppIntentsExtension.appex/AutocompleteAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/System/Library/ExtensionKit/Extensions/AutocompleteAppIntentsExtension.appex/AutocompleteAppIntentsExtension</string>
+	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

```
### BiomeSELFIngestor

> `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor`

```diff

 				<string>IntelligenceFlow.ResponseGeneration</string>
 				<string>IntelligenceFlow.SearchToolTelemetry</string>
 				<string>IntelligenceFlow.ExecutorTelemetry</string>
+				<string>IntelligenceFlow.IFRequestTelemetry</string>
 			</array>
 		</dict>
 	</dict>

```
### BlackPowderInferenceExtension

> `/System/Library/ExtensionKit/Extensions/BlackPowderInferenceExtension.appex/BlackPowderInferenceExtension`

```diff

 	<string>com.apple.anvil</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>GenerativeExperiences.TransparencyLog</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 	</array>

 	<array>
 		<string>com.apple.modelcatalog.catalog</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.anvil</string>
 	</array>

```
### CameraMessagesApp

> `/System/Library/ExtensionKit/Extensions/CameraMessagesApp.appex/CameraMessagesApp`

```diff

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.camera.CameraMessagesApp</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/tmp/</string>

```
### ContactsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ContactsAppIntentsExtension.appex/ContactsAppIntentsExtension`

```diff

 	</array>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.MobileAddressBook</string>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/System/Library/ExtensionKit/Extensions/ContactsAppIntentsExtension.appex/ContactsAppIntentsExtension</string>
+	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```

### 🆕 DefaultAppsSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DefaultAppsSettingsIntents.appex/DefaultAppsSettingsIntents`

- No entitlements *(yet)*
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>Photos.Search</string>
 		<string>Photos.Memories.Viewed</string>
 		<string>Photos.Memories.Shared</string>
+		<string>Photos.Memories.Curation</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

 		<string>WalletPaymentsCommerce.FinancialInsights.RecurringSendSuggestions</string>
 		<string>Safari.Browsing.Assistant</string>
 		<string>GenerativeExperiences.TransparencyLog</string>
+		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
+		<string>AdAttributionKit.AggregatedReporting.Purchase</string>
+		<string>AdAttributionKit.AggregatedReporting.Conversion</string>
+		<string>Siri.ASR.RequestMetricsRecord</string>
+		<string>WalletPaymentsCommerce.UserProofing.Result</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.aiml.priml.FedStats</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```
### FedStatsMLHostPluginClassA

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.aiml.priml.FedStats</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```
### FedStatsMLHostPluginClassB

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.aiml.priml.FedStats</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```

### 🆕 GMSSELFIngestor

> `/System/Library/ExtensionKit/Extensions/GMSSELFIngestor.appex/GMSSELFIngestor`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.GMSSELFIngestor</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>GMSLogging.StreamMapper</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
	<key>com.apple.siri.analytics.assistant</key>
	<array>
		<string>publish.unordered</string>
	</array>
</dict>
</plist>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.library</key>
+	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceAddressBook</string>
-	</array>
-	<key>com.apple.private.tcc.allow-prompting</key>
-	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
 	<key>com.apple.sage.summarization</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>

```
### GenerativeAssistantExtension

> `/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array>
 		<string>applinks:chatgpt.com</string>

 	<true/>
 	<key>com.apple.intelligenceflow.uiContext</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.generativeassistanttools.GenerativeAssistantExtension</string>
+	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
+	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppIntent</string>

 	<array>
 		<string>com.apple.generativeassistanttools.GenerativeAssistantExtension</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>GenerativeAssistantTools</key>

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.photos.service.mediaconversion</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriFeatureStore</key>

 		<string>kTCCServiceSpeechRecognition</string>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/tmp/VICamera/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/SiriReferenceResolution/</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.shortcuts</string>
+		<string>com.apple.siri.shortcuts</string>
+		<string>group.is.workflow.my.app</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.siri</string>
 		<string>com.apple.generativeassistanttools.GenerativeAssistantExtension</string>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>com.apple.openai</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 GenerativePlaygroundAppIntents

> `/System/Library/ExtensionKit/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.GenerativePlaygroundAppIntents</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.GenerativePlaygroundAppIntents</string>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.Photos</string>
	</array>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.assertion</key>
	<true/>
	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.appintents.attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.GenerativePlaygroundApp</string>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.person</string>
		<string>photos.face</string>
	</array>
	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.GenerativePlaygroundApp</string>
	</dict>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>peopleSubgraph</string>
		<string>inferenceFeaturesECR</string>
		<string>personEntityRelevanceRanking</string>
		<string>entitySimilarityFeatures</string>
	</array>
	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
	<true/>
	<key>com.apple.private.photos.allowassetexpunge</key>
	<true/>
	<key>com.apple.private.photos.allowlibraryupgrade</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.librarymanagement</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.GenerativePlayground</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.photos.ImageConversionService</string>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
</dict>
</plist>

```
### HomeWidgetIntentsExtension

> `/System/Library/ExtensionKit/Extensions/HomeWidgetIntentsExtension.appex/HomeWidgetIntentsExtension`

```diff

 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>
 		<string>com.apple.SoundScapesViewServices.ViewService</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.datamigrator</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.datamigrator</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

```
### IFTranscriptSELFIngestor

> `/System/Library/ExtensionKit/Extensions/IFTranscriptSELFIngestor.appex/IFTranscriptSELFIngestor`

```diff

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
+	<key>com.apple.siri.analytics.assistant</key>
+	<array>
+		<string>publish.unordered</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 SpeakerIdSamplingExtension

> `/System/Library/ExtensionKit/Extensions/SpeakerIdSamplingExtension.appex/SpeakerIdSamplingExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.OnDeviceAnalytics.SpeakerIdSamplingExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.OnDeviceAnalytics.SpeakerIdSamplingExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Lighthouse.Ledger.TaskCustomEvent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Assistant/AssistantSampled/</string>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.ssr.rpisamplingservice</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.voicetrigger</string>
		<string>com.apple.voicetrigger.notbackedup</string>
		<string>com.apple.avfoundation.avvc</string>
		<string>com.apple.coreaudio</string>
		<string>com.apple.speakerrecognition</string>
		<string>com.apple.SpeakerIdWorker</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.ssr.rpisamplingservice</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.SpeakerIdWorker</string>
	</array>
	<key>com.apple.ssr.rpisamplingservice</key>
	<true/>
</dict>
</plist>

```
### VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.VideoSubscriberAccount.AnalyticsService</string>
 		<string>com.apple.VideoSubscriberAccount.PrivacyService</string>
 		<string>com.apple.VideoSubscriberAccount.DeveloperService</string>
 	</array>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>com.apple.accessibility.cache.*</string>
 		<string>com.apple.coreservices.launchservices.session.*</string>
 		<string>user.uid.501.syslog.*</string>
+		<string>_UUID_.notification</string>
 		<string>CPActiveCountryCodeChanged.Internal</string>
 		<string>MCManagedBooksChanged</string>
 		<string>PINPolicyChangedNotification</string>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>com.apple.accessibility.cache.*</string>
 		<string>com.apple.coreservices.launchservices.session.*</string>
 		<string>user.uid.501.syslog.*</string>
+		<string>_UUID_.notification</string>
 		<string>CPActiveCountryCodeChanged.Internal</string>
 		<string>MCManagedBooksChanged</string>
 		<string>PINPolicyChangedNotification</string>

```
### FullAccessSettingsPromptExtension

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/FullAccessSettingsPromptExtension.appex/FullAccessSettingsPromptExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/System/Library/Frameworks/ContactsUI.framework/PlugIns/FullAccessSettingsPromptExtension.appex/FullAccessSettingsPromptExtension</string>
+	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### com.apple.HealthKit.HealthDiagnosticExtension

> `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthDiagnosticExtension.appex/com.apple.HealthKit.HealthDiagnosticExtension`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.health.orchestration.access</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.feature-availability.read-any</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.sleepd.sleepserver</string>
-		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.appconduitd.device-connection</string>
+		<string>com.apple.bluetooth.xpc</string>
+		<string>com.apple.healthappd.orchestration</string>
+		<string>com.apple.sleepd.sleepserver</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-only</key>
 	<array>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.Carousel.eligibilityservice</key>
 	<true/>
+	<key>com.apple.CommCenter.StormBreaker</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

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
 	<key>com.apple.appstored.octane</key>
 	<true/>
+	<key>com.apple.attributionkitd.token-handoff</key>
+	<true/>
 	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.askpermissiond</string>
+		<string>com.apple.attributionkitd.xpc.token-handoff</string>
 		<string>com.apple.biometrickitd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>

```
### axassetsd

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.Accessibility</string>
+		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.Accessibility.Assets</string>
 		<string>com.apple.voiceservices</string>
 	</array>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<array>
 		<string>com.apple.facetime.bag</string>
 		<string>com.apple.imessage.bag</string>
+		<string>com.apple.AppStore</string>
 	</array>
 	<key>com.apple.security.system-container</key>
 	<true/>

```

### 🆕 CustodianInviteMessageExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/CustodianInviteMessageExtension.appex/CustodianInviteMessageExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.appleaccount.beneficiary</key>
	<true/>
	<key>com.apple.appleaccount.custodian</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.familycircle.agent</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.imagent</key>
	<true/>
	<key>com.apple.messages.private.AllowAlertPresentation</key>
	<true/>
	<key>com.apple.messages.private.AllowParticipantAddressAccess</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.aa.custodian.xpc</string>
		<string>com.apple.aa.inheritance.xpc</string>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.ak.custodian.xpc</string>
		<string>com.apple.ak.inheritance.xpc</string>
		<string>com.apple.corefollowup.agent</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.hsa-authentication-server</string>
		<string>com.apple.security.octagon</string>
	</array>
	<key>com.apple.springboard.activateRemoteAlert</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
</dict>
</plist>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>IAPHistory</string>
 		<string>Library</string>
 		<string>Queue</string>
 		<string>Install</string>
 	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
+	<true/>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.securityd.systemkeychain</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.appstored.xpc</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.securityd.systemkeychain</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstored.xpc</string>

 	<string>1445028844</string>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.openai</string>
 		<string>apple</string>
 	</array>
 </dict>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>Siri.AnalyticsIdentifiers.UserSeed</string>
 		<string>Siri.ContextRefreshTriggers</string>
 		<string>Siri.Execution</string>
+		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>Siri.SELFProcessedEvent</string>
 		<string>Siri.VoiceTriggerStatistics</string>

 	<string>com.apple.siri</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>Assistant</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Device.Wireless.Bluetooth</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Location.MicroLocation.Localization</key>
+				<true/>
+				<key>Notification.Usage</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Siri.Service</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>NLRouterLLMCache</key>
 		<dict>
 			<key>Streams</key>

 	<true/>
 	<key>com.apple.private.siri-morphunassetsupdaterd</key>
 	<true/>
+	<key>com.apple.private.sirittsservice.impersonate-clients</key>
+	<array>
+		<string>com.apple.siri.MultilingualReading</string>
+	</array>
 	<key>com.apple.private.speech-model-training</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

 	<key>com.apple.trial.status.namespace-name.allow</key>
 	<array>
 		<string>MYRIAD_BOOSTS</string>
+		<string>SIRI_AUDIO_APP_SELECTION_HOMEACCESSORY</string>
 		<string>SIRI_AUDIO_APP_SELECTION_HOMEPOD</string>
 		<string>SIRI_AUDIO_DISABLE_MEDIA_ENTITY_SYNC</string>
 		<string>SIRI_AUDIO_LAPSED_MUSIC_USER</string>

 	<array>
 		<string>apple</string>
 		<string>com.apple.assistant</string>
+		<string>com.apple.openai</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/db/biome/</string>
-		<string>/private/var/PersonalDeviceVolumes/</string>
-		<string>/private/var/mobile/Containers/Data/InternalDaemon/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.Biome</string>
 		<string>com.apple.biomed</string>
 	</array>
+	<key>com.apple.security.ts.daemon-container</key>
+	<true/>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### companionmessagesd

> `/System/Library/PrivateFrameworks/ChatKit.framework/companionmessagesd`

```diff

 	<array>
 		<string>NULL/ActivationState</string>
 	</array>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>GetSystemAppMigrationStatus</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>

 		<string>com.apple.securityd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.nanoprefsync</string>
+		<string>com.apple.mobile.installd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### com.apple.Photos.CPLDiagnose

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose`

```diff

 	<array>
 		<string>com.apple.PowerManagement.control</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.cache_delete.public</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```

### 🆕 CSFFollowUpExtension

> `/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/PlugIns/CSFFollowUpExtension.appex/CSFFollowUpExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.CloudSubscriptionFeatures.CSFFollowUpExtension</string>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/PlugIns/CSFFollowup.appex/CSFFollowUpExtension</string>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ind.cloudfeatures</string>
		<string>com.apple.ind.xpc</string>
	</array>
</dict>
</plist>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 		<string>Siri.VoiceTriggerStatistics</string>
 		<string>SiriDictation</string>
 		<string>Siri.SelfTriggerSuppression</string>
+		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 	<string>com.apple.corespeechd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>PeopleSuggesterContactPriors</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>PeopleSuggester.ContactPrior</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>SpeechProfile</key>
 		<dict>
 			<key>Sets</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>HomeKit.HomeServiceArea</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Location.SignificantLocation</key>
 				<dict>
 					<key>mode</key>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowmessagescontent</key>
+	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```
### donotdisturbd

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 	<array>
 		<string>Mail.Categorization</string>
 		<string>Mail.Recategorization</string>
+		<string>Mail.CategorizationAnalytics.Receive</string>
+		<string>Mail.CategorizationAnalytics.Read</string>
+		<string>Mail.CategorizationAnalytics.Recategorize</string>
 	</array>
 	<key>com.apple.private.clouddocs.sharing.private-interface</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.dnssd.resolver-override</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.behavior.resolution.client-identifiers</key>
 	<array>
 		<string>com.apple.messageui</string>

```
### FedStatsMLRPlugin

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/FedStatsMLRPlugin`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/FedStats/</string>

```
### FedStatsMLRPluginClassB

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/FedStatsMLRPluginClassB`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/FedStats/</string>

```
### FedStatsMLRPluginNonDnU

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/FedStatsMLRPluginNonDnU`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/FedStats/</string>

```
### FileProviderDiagnosticExtension

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.fileprovider.read-diagnostic-metadata</key>
 	<true/>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.logd.admin</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```

### 🆕 AppleIntelligenceReportDiagnostics

> `/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/PlugIns/AppleIntelligenceReportDiagnostics.appex/AppleIntelligenceReportDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>AppleIntelligenceReportExport</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>GenerativeExperiences.TransparencyLog</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.privatemlclient</string>
		<string>com.apple.AppleIntelligenceReport</string>
	</array>
</dict>
</plist>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.spotlight.SearchAgent</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.mobile.installd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.delete-application-snapshots</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>GetSystemAppMigrationStatus</string>
+		<string>WaitForSystemAppMigrationToComplete</string>
+	</array>
 </dict>
 </plist>
 

```
### IMAutomaticHistoryDeletionAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMAutomaticHistoryDeletionAgent.app/IMAutomaticHistoryDeletionAgent`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>GetSystemAppMigrationStatus</string>
+	</array>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.imagent.desktop.auth</string>
+		<string>com.apple.mobile.installd</string>
 	</array>
 </dict>
 </plist>

```
### installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

 	<string>com.apple.installcoordinationd</string>
 	<key>com.apple.PrivacyDisclosure.consentStore</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.appconduitd.device-connection.connect.allow</key>
 	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>

 	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
-	<key>com.apple.private.ids.registration</key>
-	<array>
-		<string>com.apple.madrid</string>
-	</array>
 	<key>com.apple.private.installcoordinationd.daemon</key>
 	<true/>
 	<key>com.apple.private.managed-settings.override</key>

 		<string>com.apple.nanoprefsync</string>
 		<string>com.apple.managedappdistributiond.installcoordination</string>
 		<string>com.apple.photos.service</string>
+		<string>com.apple.accountsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.madrid</string>
+		<string>com.apple.seserviced.contactlessCredential.settings</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<string>kCFPreferencesAnyApplication</string>
 	<key>com.apple.security.system-groups</key>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.BackupAgent.RestoreEnded</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.BackupAgent.RestoreStarted</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.Drive.RestoreEnded</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.Drive.RestoreStarted</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.backgroundCellularAccessChanged</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.backupStateChanged</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.restoreCompletedAlertStateChanged</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.restoreStateChanged</key>
+	<true/>
 	<key>com.apple.private.fileprovider.backup-restore-plugin</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<true/>
 	<key>com.apple.private.security.storage.MobileBackup</key>
 	<true/>
+	<key>com.apple.private.security.storage.eligibilityd</key>
+	<true/>
 	<key>com.apple.private.security.storage.trustd-private</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```

### 🆕 com.apple.Safari.SandboxBroker

> `/System/Library/PrivateFrameworks/MobileSafari.framework/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobilesafari</string>
	</dict>
	<key>com.apple.private.imcore.spi.database-access</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleJPEGDriverUserClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
</dict>
</plist>

```
### NewsScoringService

> `/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/NewsScoringService.xpc/NewsScoringService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.ane.iokit-user-access</key>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.hid.client.admin</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.assistant.cdm</string>
+		<string>com.apple.mediaanalysisd.embeddingstore</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### AmbientPhotoFramePosterProvider

> `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/AmbientPhotoFramePosterProvider.appex/AmbientPhotoFramePosterProvider`

```diff

 		<key>value</key>
 		<string>com.apple.mobileslideshow</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.XPCStoreOptIn</key>

```
### PhotosPosterProvider

> `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider`

```diff

 		<key>value</key>
 		<string>com.apple.mobileslideshow</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.XPCStoreOptIn</key>

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

```diff

 	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>

```
### budd

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/budd`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.MobileActivation</key>
 	<array>
 		<string>GetActivationState</string>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 				<string>Device.ScreenLocked</string>
 			</array>
 		</dict>
+		<key>SiriSuggestions</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.Intent</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.itunesstored.private</key>
 	<true/>

```

### 🆕 STSDiagnostic

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/PlugIns/STSDiagnostic.appex/STSDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/Logs/CrashReporter/VoiceServices/</string>
		<string>/private/var/mobile/Library/Logs/SiriTTSService/</string>
	</array>
</dict>
</plist>

```
### syncdefaultsd

> `/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
+		<key>com.apple.KeyValueService.Encrypted</key>
+		<string>com.apple.KeyValueService.Encrypted</string>
 		<key>com.apple.KeyValueService.EndToEndEncrypted</key>
 		<string>com.apple.KeyValueService.EndToEndEncrypted</string>
 		<key>com.apple.KeyValueService.EndToEndEncrypted.AllPlatforms</key>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 		<string>synchronize-extensions</string>
 		<string>compact-store</string>
 		<string>query-identification-entries</string>
+		<string>query-extension-priorities</string>
 	</array>
 	<key>com.apple.CallKit.call-directory.extension-host</key>
 	<true/>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```

### 🆕 WalletBlastDoorService

> `/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/XPCServices/WalletBlastDoorService.xpc/WalletBlastDoorService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.pac.shared_region_id</key>
	<string>BlastDoor</string>
	<key>com.apple.private.pac.exception</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>blastdoor-messages</string>
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
### WidgetConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension`

```diff

 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Applications/</string>
+		<string>/Library/Preferences/com.apple.networkd.plist</string>
 		<string>/private/var/containers/Bundle/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### ind

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/ind`

```diff

 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.CloudSubscriptionFeatures</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.cache</string>
+		<string>com.apple.CloudSubscriptionFeatures.diagnostic</string>
 		<string>com.apple.CloudSubscriptionFeatures.geoCache</string>
 		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>

```
### ICQFollowup

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup`

```diff

 	<true/>
 	<key>com.apple.coreidvd.spi</key>
 	<true/>
-	<key>com.apple.frontboard.launchapplications</key>
-	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.payment.all-access</key>

 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
-	<key>com.apple.private.coreservices.canmaplsdatabase</key>
-	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

```
### itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

 	<true/>
 	<key>com.apple.private.fpsd.client</key>
 	<true/>
+	<key>com.apple.private.homekit</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.itunescloudd</string>

 		<string>com.apple.amsaccountsd.multiuser</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.homed.xpc</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	</array>
 	<key>com.apple.private.ids.nearby</key>
 	<true/>
+	<key>com.apple.private.ids.phone-number-authentication</key>
+	<true/>
 	<key>com.apple.private.ids.registration</key>
 	<array>
 		<string>com.apple.madrid</string>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 <dict>
 	<key>CanInheritApplicationStateFromOtherProcesses</key>
 	<true/>
+	<key>NSExtension</key>
+	<dict>
+		<key>NSExtensionFileProviderDocumentGroup</key>
+		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
+		<key>NSExtensionPointIdentifier</key>
+		<string>com.apple.fileprovider-nonui</string>
+		<key>NSExtensionPrincipalClass</key>
+		<string>PhotosFileProvider</string>
+	</dict>
 	<key>application-identifier</key>
 	<string>com.apple.camera</string>
 	<key>checklessPersistentURLTranslation</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 <dict>
 	<key>CanInheritApplicationStateFromOtherProcesses</key>
 	<true/>
+	<key>NSExtension</key>
+	<dict>
+		<key>NSExtensionFileProviderDocumentGroup</key>
+		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
+		<key>NSExtensionPointIdentifier</key>
+		<string>com.apple.fileprovider-nonui</string>
+		<key>NSExtensionPrincipalClass</key>
+		<string>PhotosFileProvider</string>
+	</dict>
 	<key>application-identifier</key>
 	<string>com.apple.camera.lockscreen</string>
 	<key>checklessPersistentURLTranslation</key>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
-	<key>com.apple.developer.healthkit</key>
+	<key>com.apple.developer.calling-app</key>
 	<true/>
-	<key>com.apple.developer.phone-app</key>
+	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.usernotifications.communication</key>
 	<true/>

```
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-call-capabilities</string>
+		<string>access-call-providers</string>
+	</array>
 	<key>fairplay-client</key>
 	<string>511712240</string>
 	<key>platform-application</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.usernotifications.critical-alerts</key>
+	<true/>
 	<key>com.apple.dropin</key>
 	<true/>
 	<key>com.apple.energykit.client</key>

 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>
 		<string>com.apple.SoundScapesViewServices.ViewService</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>com.apple.datamigrator</string>
 		<string>com.apple.dropin.xpc</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homeenergyd.xpc</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

 		<string>com.apple.datamigrator</string>
 		<string>com.apple.dropin.xpc</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homeenergyd.xpc</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

```
### HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homeenergyd.xpc</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

 		<string>com.apple.datamigrator</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

```
### HomeWidgetLockScreen

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen`

```diff

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>com.apple.datamigrator</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

 		<string>com.apple.datamigrator</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

```
### HomeWidgetSingleAccessoryIntent

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent`

```diff

 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>
 		<string>com.apple.SoundScapesViewServices.ViewService</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.datamigrator</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homeenergyd.xpc</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

 		<string>com.apple.datamigrator</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>

 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>
 		<string>com.apple.homed</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.message</string>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.GenerativePlaygroundAppIntents</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.GenerativePlaygroundAppIntents</string>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>

 		<string>kTCCServiceCamera</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
-	<false/>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.GenerativePlayground</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>

```
### Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.library</key>
+	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>

```
### GenerativePlaygroundMessagesAppExtension

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.library</key>
+	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
-	<key>com.apple.geoanalyticsd.analytics</key>
+	<key>com.apple.geoanalyticsd.eval</key>
 	<true/>
 	<key>com.apple.geod.allow-user-initiated-request</key>
 	<true/>

```
### com.apple.mobilenotes.SharingExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.personas.propagate</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<array/>
 	<key>com.apple.developer.carplay-communication</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudDocuments</string>

```
### MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.developer.usersafety.client</key>

```
### MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.developer.usersafety.client</key>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
+		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.sage.summarization</string>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.tvappservices.container</string>
+	</array>
 	<key>com.apple.private.security.storage.News</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

```
### NewsTodayIntents

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents`

```diff

 	<string>ZL6BUSYGB3.com.apple.news.widgetintents</string>
 	<key>aps-environment</key>
 	<string>development</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<array>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.coreduetd.people.user</string>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.AppStoreComponents</string>
+		<string>com.apple.AuthenticationServices.Developer</string>
 	</array>
 	<key>com.apple.security.files.user-selected.read-write</key>
 	<true/>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.mediaanalysisd.embeddingstore</string>
+		<string>com.apple.tailspind</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>com.apple.tailspin.config-apply</key>
+	<true/>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-call-capabilities</string>
+		<string>access-call-providers</string>
+	</array>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>391</string>

```
### csfdiagnose

> `/usr/bin/csfdiagnose`

```diff

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.cloud.quota</string>
 		<string>com.apple.mobileslideshow</string>
+		<string>com.apple.CloudSubscriptionFeatures</string>
 		<string>com.apple.CloudSubscriptionFeatures.cache</string>
+		<string>com.apple.CloudSubscriptionFeatures.diagnostic</string>
 		<string>com.apple.CloudSubscriptionFeatures.geoCache</string>
 		<string>com.apple.CloudSubscriptionFeatures.ticket.cache</string>
 		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.WebUI</string>
+		<string>com.apple.AuthenticationServices.Developer</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.BackupAgent.RestoreEnded</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.BackupAgent.RestoreStarted</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.Drive.RestoreEnded</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.Drive.RestoreStarted</key>
+	<true/>
 	<key>com.apple.private.fileprovider.backup-restore-plugin</key>
 	<true/>
 	<key>com.apple.private.keychain-backup-client</key>

 	<true/>
 	<key>com.apple.private.security.storage.MobileBackup</key>
 	<true/>
+	<key>com.apple.private.security.storage.eligibilityd</key>
+	<true/>
 	<key>com.apple.private.security.storage.trustd-private</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### FinishRestoreFromBackup

> `/usr/libexec/FinishRestoreFromBackup`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.ciconia</key>
 	<true/>
+	<key>com.apple.private.security.storage.eligibilityd</key>
+	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>
 	<true/>
 	<key>com.apple.rootless.install</key>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.EnabledState</key>
+	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>

```
### announced

> `/usr/libexec/announced`

```diff

 	<true/>
 	<key>com.apple.announced.clientid</key>
 	<string>com.apple.announced</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.assistant.multiuser.service</key>

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.locationd.effective-bundle</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.locationd.usage-oracle</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<array>
 		<string>com.apple.private.alloy.intercom</string>

 	</array>
 	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.homehubd</key>
 	<array>
 		<string>endpoint-read</string>

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Caches/GeoServices/</string>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.corespeech.corespeechd.ssv.service</string>
 		<string>com.apple.assistant.dictation</string>
 		<string>com.apple.SharingServices</string>
-		<string>com.apple.voiceservices.tts</string>
 		<string>com.apple.homehubd.manage</string>
 		<string>com.apple.audio.SystemSoundServer-iOS</string>
 		<string>com.apple.coremedia.asset.xpc</string>

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.assistant.multiuser.service</string>
 		<string>com.apple.assistant.multiuser.service.remora</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.announced.toneplayer</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.mediaremote</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
-		<string>com.apple.voiceservices</string>
 		<string>com.apple.Sharing</string>
 		<string>com.apple.TelephonyUtilities</string>
 	</array>

 	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>
-	<key>com.apple.voiced.can-dump-audio</key>
-	<true/>
-	<key>com.apple.voiceservices.tts</key>
-	<true/>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 		<string>com.apple.AppSSO.service-xpc</string>
 		<string>com.apple.usymptomsd</string>
 		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.lsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.private.health.feature-availability-requirement-overrides</string>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

 	<array>
 		<string>com.apple.batteryintelligence-notifications</string>
 	</array>
+	<key>com.apple.proactive.eventtracker</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/usr/libexec/</string>

 	<array>
 		<string>com.apple.batteryintelligence.internal</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
+	<string>/Library/Trial/</string>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>1910</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### devicesharingd

> `/usr/libexec/devicesharingd`

```diff

 	<true/>
 	<key>com.apple.managedassets.api.usermode</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>

 		<string>com.apple.devicesharingd.guestuserremoteunlockservice</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.iconservices</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.managedassetsd</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.surfboard.authenticationservice</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.devicesharingd</string>
+	<key>com.apple.springboard.CFUserNotification</key>
+	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
 	<key>com.apple.surfboard.authentication-client</key>

```
### diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```
### eligibilityd

> `/usr/libexec/eligibilityd`

```diff

 	</array>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.security.storage.eligibilityd</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readwrite</key>
 	<true/>
 	<key>com.apple.security.system-container</key>

```
### eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.private.calendar.allow-birthday-modification</key>

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceReminders</string>
 	</array>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.eventkitsync.notifications</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.EventKitSyncServices.server</string>
+		<string>com.apple.lsd.open</string>
+		<string>com.apple.usernotifications.listener</string>
 	</array>
 </dict>
 </plist>

```
### handwritingd

> `/usr/libexec/handwritingd`

```diff

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Handwriting_Synthesis/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### linkd

> `/usr/libexec/linkd`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.homed</string>
 		<string>com.apple.linkd</string>
 		<string>com.apple.assistant.backedup</string>
 	</array>
+	<key>com.apple.security.exception.user-preference-read</key>
+	<array>
+		<string>com.apple.homed</string>
+	</array>
 	<key>com.apple.security.system-container</key>
 	<true/>
 	<key>com.apple.security.ts.mobile-keybag-access</key>

```
### locationd

> `/usr/libexec/locationd`

```diff

 			<dict/>
 		</dict>
 	</dict>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.safetyalerts</string>

```
### lockdownd

> `/usr/libexec/lockdownd`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceFaceID</string>
 		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.private.webinspector.allow-remote-inspection</key>

```
### nanomediaremotelinkagent

> `/usr/libexec/nanomediaremotelinkagent`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.mediaremote.device-info</key>
+	<true/>
+	<key>com.apple.mediaremote.remote-control-discovery</key>
+	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

```
### remoteappintentsd

> `/usr/libexec/remoteappintentsd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.remoteappintentsd</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.diagnosticpipeline.request</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<array>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.diagnosticpipeline.service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.observationStatusRegistry</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 	</array>
 	<key>com.apple.security.exception.user-preference.read</key>
 	<array>

```
### restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleBasebandPCIUserClient</string>
+		<string>AppleBasebandUserClient</string>
 		<string>AppleGasGaugeUpdateUserClient</string>
 		<string>AppleH10CamInUserClient</string>
 		<string>AppleH13CamInUserClient</string>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	</array>
 	<key>com.apple.sharing.DurianTapPromptClient</key>
 	<true/>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	</array>
 	<key>com.apple.fileprovider.enumerate</key>
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
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.HearingModeService</string>
 		<string>com.apple.homed.xpc</string>
-		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.icloud.searchpartyd.accessorydiscoverysession</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.iconservices</string>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.ids.event-reporting</key>
+	<true/>
 	<key>com.apple.private.ids.key-transparency.cache-clear-request</key>
 	<true/>
 	<key>com.apple.private.ids.key-transparency.optin-check</key>

```
### videosubscriptionsd

> `/usr/libexec/videosubscriptionsd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>production</string>
-	<key>com.apple.VideoSubscriberAccount.AnalyticsService.ReportAMSMetricsEvents</key>
-	<true/>
 	<key>com.apple.VideoSubscriberAccount.DeveloperService</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.VideoSubscriberAccount.AnalyticsService</string>
 		<string>com.apple.watchlistd.xpc</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.cloudd</string>

```
### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>WaitForSystemAppMigrationToComplete</string>
+	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>

 	</array>
 	<key>com.apple.remotemanagementd.management-state</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/installd/Library/MobileInstallation/MigrationInfo.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobile.keybagd.xpc</string>

 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.Safari.BrowsingDataImport</string>
+		<string>com.apple.lsd.xpc</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>

```
