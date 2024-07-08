## 🔑 Entitlements

### AppStore

> `/Applications/AppStore.app/AppStore`

```diff

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.runningboard.jetengine</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount</string>

```
### ProductPageExtension

> `/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension`

```diff

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.runningboard.jetengine</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount</string>

```
### SubscribePageExtension

> `/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.runningboard.jetengine</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount</string>

```
### CameraMessagesApp

> `/Applications/Camera.app/PlugIns/CameraMessagesApp.appex/CameraMessagesApp`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.healthd</string>
+		<string>com.apple.cameracapture</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### CarPlaySettings

> `/Applications/CarPlaySettings.app/CarPlaySettings`

```diff

 	<array>
 		<string>com.apple.carplay.settings</string>
 	</array>
+	<key>com.apple.private.mediaexperience.setsilentmode.allow</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```

### 🆕 CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
</dict>
</plist>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<true/>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.InFocus</string>
+		<string>App.Install</string>
+		<string>CarPlay.Connected</string>
+		<string>Device.ScreenLocked</string>
+		<string>Media.NowPlaying</string>
+		<string>Motion.Activity</string>
+	</array>
 	<key>com.apple.private.calendar.managedConfigurationBundleIDOverride</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.private.59482219-3102-41D6-BD94-8956D5D52CB6</key>
+	<true/>
+	<key>com.apple.springboard.private.9403EBFD-90B8-4676-84BF-9F38143337E3</key>
+	<true/>
 	<key>com.apple.springboard.private.ringer-button-events</key>
 	<true/>
 	<key>com.apple.springboard.setVoiceControlEnabled</key>

```
### Diagnostic-3939

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CheckerBoard.services</key>
+	<true/>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
 	<key>com.apple.DiagnosticsSupport.HardwareButtonAccess</key>
 	<true/>
 	<key>com.apple.accessibility.AXSBServer.assertions</key>
 	<true/>
+	<key>com.apple.private.hid.client.admin</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-filter</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-monitor</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CheckerBoard.services</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.applesignin</key>
+	<array>
+		<string></string>
+	</array>
+	<key>com.apple.developer.ubiquity-container-identifiers</key>
+	<string></string>
 	<key>com.apple.driver.VADResource.user-access</key>
 	<true/>
 	<key>com.apple.pearl.iokit-user-access</key>
 	<true/>
+	<key>com.apple.private.applepearl.allow</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>

 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>ApplePearlUserClient</string>
 		<string>AppleH10CamInUserClient</string>
 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>

 	<array>
 		<string>com.apple.applecamerad</string>
 		<string>com.apple.appleh13camerad</string>
+		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.appleh16camerad</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.applesignin</key>
+	<array>
+		<string></string>
+	</array>
+	<key>com.apple.developer.ubiquity-container-identifiers</key>
+	<string></string>
 	<key>com.apple.driver.VADResource.user-access</key>
 	<true/>
 	<key>com.apple.pearl.iokit-user-access</key>
 	<true/>
+	<key>com.apple.private.applepearl.allow</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>

 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>ApplePearlUserClient</string>
 		<string>AppleH10CamInUserClient</string>
 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>

 	<array>
 		<string>com.apple.applecamerad</string>
 		<string>com.apple.appleh13camerad</string>
+		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.appleh16camerad</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.applesignin</key>
+	<array>
+		<string></string>
+	</array>
+	<key>com.apple.developer.ubiquity-container-identifiers</key>
+	<string></string>
 	<key>com.apple.driver.VADResource.user-access</key>
 	<true/>
 	<key>com.apple.pearl.iokit-user-access</key>
 	<true/>
+	<key>com.apple.private.applepearl.allow</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>

 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>ApplePearlUserClient</string>
 		<string>AppleH10CamInUserClient</string>
 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>

 	<array>
 		<string>com.apple.applecamerad</string>
 		<string>com.apple.appleh13camerad</string>
+		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.appleh16camerad</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.applesignin</key>
+	<array>
+		<string></string>
+	</array>
+	<key>com.apple.developer.ubiquity-container-identifiers</key>
+	<string></string>
 	<key>com.apple.driver.VADResource.user-access</key>
 	<true/>
 	<key>com.apple.pearl.iokit-user-access</key>
 	<true/>
+	<key>com.apple.private.applepearl.allow</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>

 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>ApplePearlUserClient</string>
 		<string>AppleH10CamInUserClient</string>
 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>

 	<array>
 		<string>com.apple.applecamerad</string>
 		<string>com.apple.appleh13camerad</string>
+		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.appleh16camerad</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.applesignin</key>
+	<array>
+		<string></string>
+	</array>
+	<key>com.apple.developer.ubiquity-container-identifiers</key>
+	<string></string>
 	<key>com.apple.driver.VADResource.user-access</key>
 	<true/>
 	<key>com.apple.pearl.iokit-user-access</key>
 	<true/>
+	<key>com.apple.private.applepearl.allow</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>

 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>ApplePearlUserClient</string>
 		<string>AppleH10CamInUserClient</string>
 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>

 	<array>
 		<string>com.apple.applecamerad</string>
 		<string>com.apple.appleh13camerad</string>
+		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.appleh16camerad</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### EventViewService

> `/Applications/EventViewService.app/EventViewService`

```diff

 	<array/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

```
### Feedback Assistant iOS

> `/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS`

```diff

 	<string>com.apple.appleseed.FeedbackAssistant</string>
 	<key>aps-environment</key>
 	<string>production</string>
+	<key>com.apple.ProactiveSummarization.feedback</key>
+	<true/>
+	<key>com.apple.ProactiveSummarization.model-input</key>
+	<true/>
+	<key>com.apple.ProactiveSummarization.summarization</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

```
### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceMediaLibrary</string>
+		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>

 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callhistorymanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 		<string>com.apple.Accessibility.Assets</string>
 		<string>com.apple.Accessibility.Magnifier</string>
 		<string>com.apple.AccessibilityUIServer</string>
+		<string>com.apple.VoiceOverTouch</string>
 	</array>
 	<key>com.apple.security.ts.ane-client</key>
 	<true/>

```
### Media

> `/Applications/Media.app/Media`

```diff

 	<true/>
 	<key>com.apple.private.CarAssetUtils.variants</key>
 	<true/>
+	<key>com.apple.private.CarPlayUIServices.punch-through</key>
+	<true/>
 	<key>com.apple.private.CarPlayUIServices.status-bar-style</key>
 	<true/>
 	<key>com.apple.private.CarPlayUIServices.volume-notification</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.CarPlayApp.punch-through-service</string>
 		<string>com.apple.CarPlayApp.volume-notification-service</string>
 		<string>com.apple.CarPlayApp.status-bar-service</string>
 		<string>com.apple.CarAssetUtils.variants</string>

```
### MediaRemoteUI

> `/Applications/MediaRemoteUI.app/MediaRemoteUI`

```diff

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.tvremotecore.xpc</string>
 		<string>com.apple.SharingServices</string>
+		<string>com.apple.TVSystemUIService.banners</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.coreduetd.people</key>
+	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

```
### MobileSafari

> `/Applications/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.appattest.spi</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.authentication-services.access-credential-identities</key>

 	<true/>
 	<key>com.apple.diagnosticpipeline.request</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.features.all-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.geoservices.map-subscriptions.size-estimate</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>

 	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>Media.NowPlaying</string>
+		<string>App.InFocus</string>
+		<string>App.Install</string>
+		<string>CarPlay.Connected</string>
+		<string>Motion.Activity</string>
+		<string>Device.ScreenLocked</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>App.WebUsage</string>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>siriRemembers</string>
+	</array>
 	<key>com.apple.private.internal-style-asam</key>
 	<true/>
 	<key>com.apple.private.interstellar.data-access</key>

 	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
+	<key>com.apple.private.parsec.default-client</key>
+	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.rsr-cryptex-access</key>
 	<true/>
 	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>

 		<string>/private/var/db/os_eligibility/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_SafariBrowsingAssistant/purpose_auto/</string>
+		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Safari/AutoFillQuirks.plist</string>
+		<string>/private/var/mobile/Library/com.apple.siri.inference/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.AuthenticationServices.AutoFill</string>
 		<string>com.apple.WebKit.WebContent.Crashy</string>
 		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 		<string>com.apple.MobileAsset.VideoAppsMusicAssets</string>
 		<string>com.apple.MobileAsset.MediaSupport</string>
 		<string>com.apple.MobileAsset.PhotosCuratedMusicLibraryAsset</string>
-		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
-		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_MagicCleanup/purpose_auto/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>

 		<string>/Library/Caches/com.apple.mobileslideshow/</string>
 		<string>/Media/PhotoData/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### MomentsUIService

> `/Applications/MomentsUIService.app/MomentsUIService`

```diff

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Caches/com.apple.momentsd/</string>
 		<string>/Library/HTTPStorages/com.apple.MomentsUIService/</string>
 		<string>/Library/Application Support/com.apple.MomentsUIService/</string>
 		<string>/Library/Saved Application State/com.apple.MomentsUIService.savedState/</string>

```
### PeopleViewService

> `/Applications/PeopleViewService.app/PeopleViewService`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.people</string>
+		<string>com.apple.people.daemon</string>
+		<string>com.apple.people.widget</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### PeopleWidget_iOSExtension

> `/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.people</string>
+		<string>com.apple.people.widget</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.parsec.default-client</key>
+	<string>com.apple.SafariViewService</string>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

```
### SafetyMonitorApp

> `/Applications/SafetyMonitorApp.app/SafetyMonitorApp`

```diff

 	<true/>
 	<key>com.apple.carousel.liveactivities.prevents_smartstack_dismissal</key>
 	<true/>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
+	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.replicator.controller</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.ScreenContinuityServices</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

 		<string>com.apple.RemoteDisplay</string>
 		<string>com.apple.systemstatus</string>
 		<string>com.apple.coremedia.cameraviewfinder</string>
+		<string>com.apple.replicatorservices</string>
 		<string>com.apple.sessionservices</string>
+		<string>com.apple.replicatorservices</string>
 	</array>
 	<key>com.apple.springboard.continuitysession</key>
 	<true/>

```
### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 		<key>value</key>
 		<string>/Applications/ScreenshotServicesService.app/ScreenshotServicesService</string>
 	</dict>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.private.eligibilityd.setInput</key>
 	<true/>
+	<key>com.apple.private.feedbacklogger</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.softposreaderd</string>
 		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.feedbacklogger</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>

```
### ShazamEventsApp

> `/Applications/ShazamEventsApp.app/ShazamEventsApp`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	</dict>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
-		<string>AskToBuy</string>
-		<string>ScreenTimeRequest</string>
-		<string>UserFocusComputedMode</string>
-		<string>Family.ScreenTime.ChildState</string>
 		<string>Accessibility.ReduceMotion</string>
 		<string>Accessibility.ReduceTransparency</string>
 		<string>Accessibility.ColorFilters</string>

 		<string>Accessibility.Contrast</string>
 		<string>Accessibility.ClassicInvert</string>
 		<string>Accessibility.WhitePoint</string>
+		<string>App.InFocus</string>
+		<string>App.Install</string>
+		<string>AskToBuy</string>
+		<string>CarPlay.Connected</string>
 		<string>Clock.Alarm</string>
-		<string>UserFocus.ComputedMode</string>
+		<string>Family.ScreenTime.ChildState</string>
+		<string>Device.Display.AlwaysOn</string>
+		<string>Device.Display.Appearance</string>
+		<string>Device.Display.NightShift</string>
+		<string>Device.ScreenLocked</string>
+		<string>Device.SilentMode</string>
+		<string>Device.Display.TrueTone</string>
 		<string>Device.Power.EnergyMode</string>
 		<string>Device.Wireless.AirplaneMode</string>
-		<string>Device.Display.Appearance</string>
-		<string>Device.Wireless.WiFiAvailabilityStatus</string>
 		<string>Device.Wireless.BluetoothPowerEnabled</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
-		<string>Device.Display.TrueTone</string>
-		<string>Device.Display.NightShift</string>
-		<string>Device.Display.AlwaysOn</string>
-		<string>Device.SilentMode</string>
+		<string>Device.Wireless.WiFiAvailabilityStatus</string>
+		<string>Media.NowPlaying</string>
+		<string>Motion.Activity</string>
+		<string>ScreenTimeRequest</string>
+		<string>UserFocus.ComputedMode</string>
+		<string>UserFocusComputedMode</string>
 	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>

 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>siriRemembers</string>
+		<string>visualIdentifier</string>
 		<string>nerdSummary</string>
 		<string>behavioralPopularitySignals</string>
 		<string>nerdEmbeddingsPeopleTable</string>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<array>
 		<string>.GlobalPreferences</string>
 		<string>com.apple.animoji</string>
+		<string>com.apple.EmojiPreferences</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### TVRemoteUIService

> `/Applications/TVRemoteUIService.app/TVRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.TVRemoteUIService</string>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
 	<key>com.apple.private.nearbyinteraction.device-presence</key>

```
### com.apple.podcasts.appremoval

> `/System/Library/AppRemovalServices/com.apple.podcasts.appremoval.xpc/com.apple.podcasts.appremoval`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<string>com.apple.podcasts</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>243LU875E5.groups.com.apple.podcasts</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.accessibility.local</string>
+		<string>com.apple.private.alloy.accessibility.switchcontrol</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
 		<string>com.apple.private.alloy.accessibility.local</string>
+		<string>com.apple.private.alloy.accessibility.switchcontrol</string>
 	</array>
 	<key>com.apple.private.ids.nearby</key>
 	<true/>

```
### AccessibilityControlsExtension

> `/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`

```diff

 	<string>com.apple.Preferences</string>
 	<key>com.apple.frontboard.launchapplications</key>
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

 	<array>
 		<string>com.apple.SoundScapesViewServices.ViewService</string>
 	</array>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.fileprovider.acl-write</key>
 	<true/>
 	<key>com.apple.fileprovider.enumerate</key>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
 	<key>com.apple.hid.system.user-access-service</key>

```
### AccessibilityControlsExtension

> `/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`

```diff

 	<string>com.apple.Preferences</string>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.MagnifierAngel.client</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
+	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension</string>
+	</dict>
 	<key>com.apple.private.avfoundation.capture.allow</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
-	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
-	<array>
-		<string>/private/var/db/os_eligibility/eligibility.plist</string>
-		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
-		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
-		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
-	</array>
-	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
-	<array>
-		<string>AppleNVMeEANUC</string>
-	</array>
-	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.assistant.cdm</string>
-		<string>com.apple.modelmanager</string>
-		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.photoanalysisd</string>
-		<string>com.apple.photos.service</string>
-		<string>com.apple.mediaanalysisd.service.public</string>
-		<string>com.apple.sage.summarization</string>
-		<string>com.apple.generativeexperiences.summarization</string>
-		<string>com.apple.feedbackd.centralized-feedback</string>
-		<string>com.apple.extensionkitservice</string>
-		<string>com.apple.intelligenceplatform.EntityResolution</string>
-		<string>com.apple.intelligenceplatform.View</string>
-		<string>com.apple.appprotectiond.read</string>
-		<string>com.apple.appprotectiond.guard</string>
-	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
-	<array>
-		<string>com.apple.UnifiedAssetFramework</string>
-		<string>com.apple.modelcatalog.ajax</string>
-		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
-		<string>com.apple.gms.availability</string>
-		<string>kCFPreferencesAnyApplication</string>
-	</array>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`

```diff

 	<true/>
 	<key>com.apple.intelligenceflow.orchestrator</key>
 	<true/>
-	<key>com.apple.intelligenceflow.search</key>
-	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.KnowledgeConstruction</key>

```

### 🆕 SettingsSOSAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SettingsSOSAppIntentsExtension.appex/SettingsSOSAppIntentsExtension`

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
### apfs_checkdigest

> `/System/Library/Filesystems/apfs.fs/apfs_checkdigest`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.dataless-manipulation</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.dataless-manipulation</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.dataless-manipulation</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.dataless-manipulation</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.dataless-manipulation</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### fsck_apfs

> `/System/Library/Filesystems/apfs_userfs.fs/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.dataless-manipulation</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 		<string>com.apple.mediaanalysisd.embeddingstore</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.shortcutitems.fullaccess</key>
 	<true/>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>394</string>

```
### ContactsButtonXPCService

> `/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService`

```diff

 	<true/>
 	<key>com.apple.backboardd.setAuthenticatedTouches</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService</string>
+	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile</key>

```
### maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict/>
+<dict>
+	<key>com.apple.geoservices.restricted-tiles</key>
+	<array>
+		<string>offline</string>
+	</array>
+</dict>
 </plist>
 

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
-	<key>com.apple.financekit.financial-insights.host</key>
-	<true/>
 	<key>com.apple.financekit.image-processing.host</key>
 	<true/>
+	<key>com.apple.financekit.maps-insights.host</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

```
### translationd

> `/System/Library/Frameworks/Translation.framework/translationd`

```diff

 		<string>com.apple.coreaudio</string>
 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.coremedia</string>
+		<string>com.apple.assistant.support</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### activitysharingd

> `/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
-		<string>/private/var/mobile</string>
 		<string>/private/var/mobile/Library/DeviceRegistry.state/</string>
 		<string>/private/var/mobile/Library/Health/ActivitySharing</string>
 		<string>/private/var/mobile/Library/Health/ActivitySharing/ContactsCache/</string>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<array>
 		<string>com.apple.donotdisturb.siri.assistant</string>
 	</array>
+	<key>com.apple.private.email</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.access</key>

 		<string>1327</string>
 		<string>1328</string>
 		<string>1631</string>
+		<string>1750</string>
 	</array>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availability.internal</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.geoservices.navigation_info</key>

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.generativeexperiences.availability.internal</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.geod</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.iap2d.ExternalAccessory.distributednotification.server</string>

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.GEO</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.HeadGestures</string>
 		<string>com.apple.homed</string>
 		<string>com.apple.homed.notbackedup</string>
 		<string>com.apple.itunescloud</string>

 		<string>com.apple.pairedsyncd</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.pommes</string>
+		<string>com.apple.preferences.sounds</string>
 		<string>com.apple.raisetospeak</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.siri.cdm</string>

 		<string>SIRI_DATA_INTEGRATION_TEST1</string>
 		<string>SIRI_DATA_INTEGRATION_TEST2</string>
 		<string>SIRI_DICTATION_ASSETS</string>
+		<string>SIRI_HEARABLES_VOX</string>
 		<string>SIRI_INFORMATION_CACHING</string>
 		<string>SIRI_MEMORY_SYNC_CONFIG</string>
 		<string>SIRI_MESSAGES_ANNOUNCE_HINT_EDUCATION</string>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.intelligenceplatform</string>
 		<string>com.apple.suggestions</string>
-		<string>com.apple.tokengeneration</string>
+		<string>com.apple.AppleIntelligenceReport</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>Carousel.Connection.Companion</string>
+	</array>
 	<key>com.apple.private.chrono-extension-host</key>
 	<true/>
 	<key>com.apple.private.coreaudio.initiatetemporarybackgroundplayback.allow</key>

```
### com.apple.CloudDocs.MobileDocumentsFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProvider.appex/com.apple.CloudDocs.MobileDocumentsFileProvider`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.security.files.user-selected.executable</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>

```
### com.apple.CloudDocs.MobileDocumentsFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.appex/com.apple.CloudDocs.MobileDocumentsFileProviderManaged`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.security.files.user-selected.executable</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### com.apple.CloudDocs.MobileDocumentsFileProviderUI

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderUI.appex/com.apple.CloudDocs.MobileDocumentsFileProviderUI`

```diff

 	</array>
 	<key>com.apple.private.fileproviderui.display-inline</key>
 	<true/>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### com.apple.CloudDocs.iCloudDriveFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.security.files.user-selected.executable</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>

```
### com.apple.CloudDocs.iCloudDriveFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.security.files.user-selected.executable</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic`

```diff

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/db/</string>
 	</array>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### bird

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/bird`

```diff

 	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird</string>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.shortcutitems.fullaccess</key>

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.CoreAnalytics</key>
 	<true/>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/private/var/mobile/Library/Trial/Treatments/</string>
-		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SystemConfiguration.configd</string>

 	</array>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>1000</string>
-		<string>1010</string>
-		<string>1020</string>
-		<string>1030</string>
-		<string>1040</string>
-		<string>1041</string>
-		<string>1042</string>
-		<string>1043</string>
-		<string>1090</string>
-		<string>1100</string>
-		<string>1101</string>
-		<string>1110</string>
-		<string>1120</string>
-		<string>1130</string>
-		<string>1140</string>
-		<string>1150</string>
-		<string>1151</string>
-		<string>1152</string>
-		<string>1153</string>
-		<string>1154</string>
-		<string>1160</string>
-		<string>1161</string>
-		<string>1162</string>
-		<string>1170</string>
-		<string>1180</string>
-		<string>1190</string>
-		<string>1191</string>
-		<string>1200</string>
-		<string>1201</string>
-		<string>1202</string>
-		<string>1210</string>
-		<string>1220</string>
-		<string>1221</string>
-		<string>1230</string>
-		<string>1231</string>
-		<string>1240</string>
-		<string>1241</string>
-		<string>1250</string>
-		<string>1251</string>
-		<string>1252</string>
-		<string>1260</string>
-		<string>1261</string>
-		<string>1262</string>
-		<string>1270</string>
-		<string>1280</string>
-		<string>1290</string>
-		<string>1291</string>
-		<string>1292</string>
-		<string>1300</string>
-		<string>1310</string>
-		<string>1321</string>
-		<string>1320</string>
-		<string>1322</string>
-		<string>1323</string>
-		<string>1324</string>
-		<string>1325</string>
-		<string>1326</string>
-		<string>1327</string>
-		<string>1328</string>
-		<string>1329</string>
-		<string>1330</string>
-		<string>1331</string>
-		<string>1340</string>
-		<string>1341</string>
-		<string>1342</string>
-		<string>1350</string>
-		<string>1360</string>
-		<string>1370</string>
-		<string>1380</string>
-		<string>1390</string>
-		<string>1400</string>
-		<string>1410</string>
-		<string>1411</string>
-		<string>1420</string>
-		<string>1430</string>
-		<string>1431</string>
-		<string>1440</string>
-		<string>1441</string>
-		<string>1450</string>
-		<string>1460</string>
-		<string>1470</string>
-		<string>1480</string>
-		<string>1490</string>
-		<string>1491</string>
-		<string>1500</string>
-		<string>1510</string>
-		<string>1511</string>
-		<string>1512</string>
-		<string>1513</string>
-		<string>1520</string>
-		<string>1521</string>
-		<string>1530</string>
-		<string>1540</string>
-		<string>1541</string>
-		<string>1542</string>
-		<string>1543</string>
-		<string>1544</string>
-		<string>1545</string>
-		<string>1546</string>
-		<string>1547</string>
-		<string>1548</string>
-		<string>1549</string>
-		<string>1550</string>
-		<string>1551</string>
-		<string>1560</string>
-		<string>1570</string>
-		<string>1571</string>
-		<string>1580</string>
-		<string>1590</string>
-		<string>1600</string>
-		<string>1601</string>
-		<string>1602</string>
-		<string>1603</string>
-		<string>1610</string>
-		<string>1620</string>
-		<string>1630</string>
-		<string>1631</string>
-		<string>1632</string>
-		<string>1640</string>
-		<string>1650</string>
-		<string>1660</string>
-		<string>1670</string>
-		<string>1680</string>
-		<string>1690</string>
-		<string>1700</string>
-		<string>1701</string>
-		<string>1702</string>
-		<string>1710</string>
-		<string>1720</string>
-		<string>1730</string>
-		<string>1740</string>
-		<string>100</string>
-		<string>101</string>
-		<string>102</string>
-		<string>103</string>
-		<string>104</string>
-		<string>105</string>
-		<string>106</string>
-		<string>107</string>
-		<string>108</string>
-		<string>109</string>
-		<string>110</string>
-		<string>120</string>
-		<string>130</string>
-		<string>150</string>
-		<string>151</string>
-		<string>152</string>
-		<string>153</string>
-		<string>154</string>
-		<string>155</string>
-		<string>156</string>
-		<string>157</string>
-		<string>158</string>
-		<string>159</string>
-		<string>160</string>
-		<string>161</string>
-		<string>162</string>
-		<string>163</string>
-		<string>164</string>
-		<string>165</string>
-		<string>166</string>
-		<string>167</string>
-		<string>168</string>
-		<string>169</string>
-		<string>170</string>
-		<string>171</string>
-		<string>180</string>
-		<string>181</string>
-		<string>190</string>
-		<string>191</string>
-		<string>200</string>
-		<string>201</string>
-		<string>210</string>
-		<string>211</string>
-		<string>212</string>
-		<string>213</string>
-		<string>214</string>
-		<string>215</string>
-		<string>251</string>
-		<string>252</string>
-		<string>253</string>
-		<string>254</string>
-		<string>255</string>
-		<string>256</string>
-		<string>257</string>
-		<string>258</string>
-		<string>301</string>
-		<string>311</string>
-		<string>312</string>
-		<string>313</string>
-		<string>314</string>
-		<string>321</string>
-		<string>322</string>
-		<string>331</string>
-		<string>332</string>
-		<string>333</string>
-		<string>334</string>
-		<string>335</string>
-		<string>336</string>
-		<string>337</string>
-		<string>341</string>
-		<string>342</string>
-		<string>351</string>
-		<string>352</string>
-		<string>353</string>
-		<string>354</string>
-		<string>361</string>
-		<string>371</string>
-		<string>372</string>
-		<string>373</string>
-		<string>374</string>
-		<string>375</string>
-		<string>381</string>
-		<string>391</string>
-		<string>392</string>
-		<string>393</string>
-		<string>394</string>
-		<string>395</string>
-		<string>401</string>
-		<string>402</string>
-		<string>403</string>
-		<string>404</string>
-		<string>405</string>
-		<string>406</string>
-		<string>407</string>
-		<string>408</string>
-		<string>409</string>
-		<string>411</string>
-		<string>412</string>
-		<string>413</string>
-		<string>414</string>
-		<string>415</string>
-		<string>416</string>
-		<string>417</string>
-		<string>421</string>
-		<string>422</string>
-		<string>423</string>
-		<string>424</string>
-		<string>425</string>
-		<string>426</string>
-		<string>431</string>
-		<string>501</string>
-		<string>502</string>
-		<string>511</string>
-		<string>512</string>
-		<string>513</string>
-		<string>514</string>
-		<string>515</string>
-		<string>521</string>
-		<string>522</string>
-		<string>531</string>
-		<string>532</string>
-		<string>541</string>
-		<string>551</string>
-		<string>561</string>
-		<string>562</string>
-		<string>563</string>
-		<string>564</string>
-		<string>565</string>
-		<string>566</string>
-		<string>567</string>
-		<string>568</string>
-		<string>569</string>
-		<string>571</string>
-		<string>581</string>
-		<string>582</string>
-		<string>583</string>
-		<string>584</string>
-		<string>585</string>
-		<string>586</string>
-		<string>587</string>
-		<string>588</string>
-		<string>589</string>
-		<string>591</string>
-		<string>592</string>
-		<string>593</string>
-		<string>601</string>
-		<string>602</string>
-		<string>603</string>
-		<string>604</string>
-		<string>605</string>
-		<string>611</string>
-		<string>621</string>
-		<string>631</string>
-		<string>641</string>
-		<string>642</string>
-		<string>651</string>
-		<string>700</string>
-		<string>701</string>
-		<string>702</string>
-		<string>703</string>
-		<string>704</string>
-		<string>705</string>
-		<string>750</string>
-		<string>751</string>
-		<string>752</string>
-		<string>753</string>
-		<string>754</string>
-		<string>755</string>
-		<string>756</string>
-		<string>757</string>
-		<string>758</string>
-		<string>759</string>
-		<string>760</string>
-		<string>761</string>
-		<string>762</string>
-		<string>763</string>
-		<string>800</string>
-		<string>801</string>
-		<string>802</string>
-		<string>803</string>
-		<string>804</string>
-		<string>805</string>
-		<string>810</string>
-		<string>811</string>
-		<string>812</string>
-		<string>813</string>
-		<string>814</string>
-		<string>815</string>
-		<string>816</string>
-		<string>817</string>
-		<string>818</string>
-		<string>819</string>
-		<string>820</string>
-		<string>821</string>
-		<string>822</string>
-		<string>823</string>
-		<string>824</string>
-		<string>825</string>
-		<string>830</string>
-		<string>831</string>
-		<string>832</string>
-		<string>833</string>
-		<string>834</string>
-		<string>835</string>
-		<string>836</string>
-		<string>837</string>
-		<string>838</string>
-		<string>839</string>
-		<string>840</string>
-		<string>841</string>
-		<string>842</string>
-		<string>843</string>
-		<string>844</string>
-		<string>845</string>
-		<string>846</string>
-		<string>847</string>
-		<string>848</string>
-		<string>849</string>
-		<string>850</string>
-		<string>851</string>
-		<string>852</string>
-		<string>860</string>
-		<string>861</string>
 		<string>862</string>
-		<string>863</string>
-		<string>870</string>
-		<string>871</string>
-		<string>872</string>
-		<string>873</string>
-		<string>874</string>
-		<string>880</string>
-		<string>890</string>
-		<string>900</string>
-		<string>910</string>
-		<string>920</string>
-		<string>921</string>
-		<string>922</string>
-		<string>923</string>
-		<string>924</string>
-		<string>930</string>
-		<string>940</string>
-		<string>950</string>
-		<string>960</string>
-		<string>961</string>
-		<string>962</string>
-		<string>963</string>
-		<string>970</string>
-		<string>980</string>
-		<string>990</string>
-		<string>11</string>
-		<string>12</string>
-		<string>13</string>
-		<string>14</string>
-		<string>20</string>
-		<string>30</string>
-		<string>31</string>
-		<string>40</string>
-		<string>41</string>
-		<string>50</string>
-		<string>51</string>
-		<string>52</string>
-		<string>53</string>
-		<string>54</string>
-		<string>60</string>
-		<string>61</string>
-		<string>62</string>
-		<string>71</string>
-		<string>0</string>
-		<string>1</string>
 	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>

```
### contextstored

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored`

```diff

 		<string>Siri.Remembers.InteractionHistory</string>
 		<string>Siri.Remembers.MessageHistory</string>
 		<string>IntelligenceEngine.Interaction.Donation</string>
+		<string>App.LocationActivity</string>
 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>

```
### FollowUpSampleExtension

> `/System/Library/PrivateFrameworks/CoreFollowUpUI.framework/PlugIns/FollowUpSampleExtension.appex/FollowUpSampleExtension`

```diff

 	<array>
 		<string>com.apple.corefollowup.agent</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<string>com.apple.corespeechd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>__Koa__</key>
+		<key>SpeechProfile</key>
 		<dict>
 			<key>Sets</key>
 			<dict>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
-				<key>HomeKit.Entity</key>
+				<key>HomeKit.Home</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
-				<key>Media.Entity</key>
+				<key>MediaLibrary.Media</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
-				<key>Podcasts.Entity</key>
+				<key>Podcasts.Podcast</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
-				<key>Siri.PrivateLearning.MediaEntity</key>
+				<key>Siri.PrivateLearning.Media</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.ironwood.support</string>
 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.nano</string>
 		<string>com.apple.raisetospeak</string>

```
### speechmodeltrainingd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd`

```diff

 	<array>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
-	<key>com.apple.privatefederatedlearning.allowed</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreRemovability</key>
+	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreRestrictions</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>

```
### DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

 	<string>com.apple.DPSubmissionService</string>
 	<key>aps-environment</key>
 	<string>development</string>
-	<key>com.apple.application-identifier</key>
-	<string>com.apple.DPSubmissionService</string>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 	<true/>
 	<key>com.apple.bulletindistributord.server</key>
 	<true/>
+	<key>com.apple.businessservicesd.businessmetadata</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

```

### 🆕 SyncDiagnostics

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/PlugIns/SyncDiagnostics.appex/SyncDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/Managed Preferences/mobile/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/CrashReporter/DataAccess/</string>
	</array>
</dict>
</plist>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.assistant.settings</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.intelligenceflow.context</key>

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
+	<key>com.apple.private.assistant.settings</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

 		<string>com.apple.modelmanager</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.assistant.settings</string>
+		<string>com.apple.private.assistant.settings</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>

 		<string>com.apple.SummarizationKit</string>
 		<string>com.apple.EmojiPreferences</string>
 		<string>com.apple.AppSupport</string>
+		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
 		<string>com.apple.CloudSubscriptionFeatures.ticket.cache</string>
 		<string>com.apple.CloudSubscriptionFeatures.cache</string>
+		<string>com.apple.CloudSubscriptionFeatures.gmCache</string>
 		<string>com.apple.csf.gm.bypass</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>WILLOWSYNC.com.apple.willowd</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
 	<key>com.apple.assistant.security</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
+		<string>com.apple.Messages.diagnostics.usernotifications</string>
 		<string>com.apple.MobileSMS</string>
 	</array>
 	<key>com.apple.springboard.launchapplications</key>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
+		<string>com.apple.Messages.diagnostics.usernotifications</string>
 		<string>com.apple.MobileSMS</string>
 	</array>
 	<key>com.apple.proactive.experiments.responses</key>

```

### 🆕 com.apple.ImagePlayground.DiagnosticExtension

> `/System/Library/PrivateFrameworks/ImagePlayground.framework/PlugIns/com.apple.ImagePlayground.DiagnosticExtension.appex/com.apple.ImagePlayground.DiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### installcoordination_proxy

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordination_proxy`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.overridePlaceholderDisposition</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.uninstall</key>
 	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 		<string>com.apple.intelligenceflow</string>
 		<string>com.apple.mobilecal</string>
 		<string>com.apple.siri.morphun</string>
+		<string>com.apple.assistant</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### MetricMeasurementHelper

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/XPCServices/MetricMeasurementHelper.xpc/MetricMeasurementHelper`

```diff

 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.sysmond</string>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.modelcatalogd</string>
-	<key>com.apple.aned.private.processModelShare.allow</key>
-	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
-	<key>com.apple.modelcatalog.compilationService</key>
-	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

```
### nanosystemsettingsd

> `/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd`

```diff

 	<array>
 		<string>com.apple.animoji</string>
 		<string>com.apple.AvatarUI.Staryu</string>
+		<string>com.apple.Bridge</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

```
### com.apple.NanoTimeKit.CreateWatchFace

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/com.apple.NanoTimeKit.CreateWatchFace.appex/com.apple.NanoTimeKit.CreateWatchFace`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.photosface</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<string>/private/var/mobile/Library/NanoTimeKit/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<string>/Media/PhotoData/</string>
+	<array>
+		<string>/Library/PhotosFace/</string>
+		<string>/Media/PhotoData/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/MappedImageCache/</string>

```
### PassKitServicesXPCService

> `/System/Library/PrivateFrameworks/PassKitServices.framework/XPCServices/PassKitServicesXPCService.xpc/PassKitServicesXPCService`

```diff

 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
-	<key>com.apple.passd.peer-payment</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.passd.peer-payment</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### peopled

> `/System/Library/PrivateFrameworks/People.framework/peopled`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.people</string>
+		<string>com.apple.people.daemon</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.messages</string>
 	</array>

```
### PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 		<string>/Library/Caches/com.apple.momentsd/</string>
 		<string>/Library/com.apple.momentsd/ </string>
 		<string>/Library/com.apple.momentsd/personalizedSensing/</string>
+		<string>/Library/Caches/com.apple.PersonalizedSensingService/</string>
+		<string>/Library/HTTPStorages/com.apple.PersonalizedSensingService/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.momentsd</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.itunesstored</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	</array>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siriinference-dodml-plugin</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.coreservices.useractivityd</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceUbiquity</string>

 	</array>
 	<key>com.apple.runningboard.assertions.useractivityd</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.coreservices.useractivityd</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 		<string>Device.Wireless.Bluetooth</string>
 		<string>Device.Wireless.NFCTag</string>
 		<string>Device.Wireless.WiFi</string>
+		<string>Sleep.ScheduleState</string>
 		<string>SleepMode</string>
 		<string>SoundDetection</string>
 		<string>SpringBoard.ExternalDisplay.DisplayConnected</string>
 		<string>SpringBoard.WindowManagement.StageManagerMode</string>
+		<string>UserFocus.SleepMode</string>
 		<string>UserFocusComputedMode</string>
 		<string>Wallet.Transaction</string>
 	</array>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>
+		<string>com.apple.calaccessd</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.contactsd</string>

```
### ContainerMetadataExtractor

> `/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/ContainerMetadataExtractor`

```diff

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/containers/</string>
 	</array>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.security.ts.mach-lookup</key>
 	<array>
 		<string>com.apple.frontboard.systemappservices</string>

```
### TelemetryDiskChecker

> `/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/TelemetryDiskChecker.xpc/TelemetryDiskChecker`

```diff

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/telemetry-db/</string>
 	</array>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Application Support/CloudDocs/session/telemetry-db/</string>

```
### eapolclient

> `/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient`

```diff

 	<true/>
 	<key>com.apple.private.mobileinboxupdater.xpc</key>
 	<true/>
+	<key>com.apple.private.otadaemon.eapCredentialEnabled</key>
+	<true/>
+	<key>com.apple.private.otadaemon.xpc</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### TVWidgetExtension

> `/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension`

```diff

 	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
-	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
-	<dict>
-		<key>type</key>
-		<string>bundleID</string>
-		<key>value</key>
-		<string>com.apple.tv</string>
-	</dict>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.tv.sharedcontainer</string>

```
### Books

> `/private/var/staged_system_apps/Books.app/Books`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
-	<key>com.apple.coreduetd.context</key>
-	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
 	<key>com.apple.developer.ClassKit-environment</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tipsd.discoverability</key>
-	<true/>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.backupd</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.appstored.xpc.updates</string>
-		<string>com.apple.tipsd</string>
-		<string>com.apple.coreduetd.context</string>
-		<string>com.apple.coreduetd</string>
-		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.UIKit.ShareUI.apple-extension-service</string>
 		<string>com.apple.UIKit.ShareUI.viewservice</string>
 		<string>com.apple.absd</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.frontboard.shutdown</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.iBooks.BDSService.private</key>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
+	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.GenerativePlaygroundApp</string>
+	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

```
### GenerativePlaygroundMessagesAppExtension

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
+	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.GenerativePlaygroundApp</string>
+	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 		<string>com.apple.MomentsUIService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.journal.xpc</string>
+		<string>com.apple.LinkPresentation.LinkSnapshotGeneratorService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MagnifierExtension

> `/private/var/staged_system_apps/Magnifier.app/Extensions/MagnifierExtension.appex/MagnifierExtension`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>H15ANEInDirectPathClient</string>
 		<string>IOSurfaceAcceleratorClient</string>
+		<string>H11ANEInDirectPathClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.CameraOverlayAngel.application-service</string>
+		<string>com.apple.appleneuralengine</string>
+		<string>com.apple.appleneuralengine.private</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.businessservicesd.businessmetadata</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

```
### MobileTimer

> `/private/var/staged_system_apps/MobileTimer.app/MobileTimer`

```diff

 	<array>
 		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/Ringtones/</string>
+		<string>/private/var/mobile/Media/Purchases/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### PassbookLockedWidgetsExtension

> `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.Passbook.PassbookWidgets</string>
+	<string>com.apple.Passbook.PassbookLockedWidgets</string>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>

 	<array>
 		<string>/System/Library/Frameworks/FinanceKitUI.framework</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/PassKit/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>

```
### PassbookWidgetsExtension-iPhone

> `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookWidgetsExtension-iPhone.appex/PassbookWidgetsExtension-iPhone`

```diff

 		<string>com.apple.passd.payment</string>
 		<string>com.apple.financed.service.coredatastore</string>
 		<string>com.apple.financed.service.store</string>
+		<string>com.apple.financed.service.bankconnect</string>
 		<string>com.apple.passd.account</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.passd.library</string>

```
### PodcastsClassKitExtension

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/PodcastsClassKitExtension`

```diff

 <dict>
 	<key>com.apple.developer.ClassKit-environment</key>
 	<string>production</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>243LU875E5.groups.com.apple.podcasts</string>
+	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>243LU875E5.groups.com.apple.podcasts</string>

```
### PodcastsNotificationExtension

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsNotificationExtension.appex/PodcastsNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>243LU875E5.groups.com.apple.podcasts</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### PodcastsWidget

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>243LU875E5.groups.com.apple.podcasts</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### com.apple.podcasts.DiagnosticExtension

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.DiagnosticExtension.appex/com.apple.podcasts.DiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>243LU875E5.groups.com.apple.podcasts</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

```
### com.apple.podcasts.SpotlightIndexExtension

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>243LU875E5.groups.com.apple.podcasts</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>243LU875E5.groups.com.apple.podcasts</string>
+	</array>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

```
### fsck_apfs

> `/sbin/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.dataless-manipulation</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### brctl

> `/usr/bin/brctl`

```diff

 	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
-	<key>com.apple.security.exception.ts.tmpdir</key>
-	<array>
-		<string>com.apple.bird.codecoverage</string>
-	</array>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 </dict>

```
### modelmanagerdump

> `/usr/bin/modelmanagerdump`

```diff

 	<true/>
 	<key>com.apple.modelmanager.dumpState</key>
 	<true/>
+	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.modelmanager.loadBundle</key>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>backupd-connection-initiate</key>
 	<true/>
+	<key>com.apple.AssistiveTouch</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.ioaccelmemoryinfo</key>
 	<true/>
 	<key>com.apple.private.iokit.BDCDataCopy</key>
 	<true/>
+	<key>com.apple.private.iokit.battery-gauging-mitigation</key>
+	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.ind.xpc</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.preferences.sounds</string>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.iokit.BDCDataCopy</key>
 	<true/>
+	<key>com.apple.private.iokit.battery-gauging-mitigation</key>
+	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.ind.xpc</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.preferences.sounds</string>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>backupd-connection-initiate</key>
 	<true/>
+	<key>com.apple.AssistiveTouch</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.ioaccelmemoryinfo</key>
 	<true/>
 	<key>com.apple.private.iokit.BDCDataCopy</key>
 	<true/>
+	<key>com.apple.private.iokit.battery-gauging-mitigation</key>
+	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.ind.xpc</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.preferences.sounds</string>

```
### SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

 	<true/>
 	<key>com.apple.RemoteDisplay</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.sidecarRelay</key>

 	<array>
 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.RemoteDisplay</string>
+		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.situational-awareness.breakthrough-shape</string>
 		<string>com.apple.surfboard.sharingmodeservice</string>
 		<string>com.apple.timesync.expositor</string>

```
### anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.Preferences</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<key>com.apple.systemstatus.domains</key>
 	<array>
 		<string>calling</string>
+		<string>media</string>
 	</array>
 	<key>com.apple.systemstatus.publisher.domains</key>
 	<string>media</string>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 		<string>com.apple.server.bluetooth</string>
 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.timed.xpc</string>
-		<string>com.apple.wifi.manager</string>
 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.wirelessproxd</string>
 	</array>

```
### caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.carp</key>
 	<true/>
+	<key>com.apple.private.externalaccessory.showallaccessories</key>
+	<true/>
 	<key>com.apple.runningboard.caraccessoryd</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### carkitd

> `/usr/libexec/carkitd`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>DoNotDisturbWhileDriving</string>
-		<string>UserFocusComputedMode</string>
+		<string>UserFocus.ComputedMode</string>
 	</array>
 	<key>com.apple.private.carkit</key>
 	<true/>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 		<string>Siri.Remembers.InteractionHistory</string>
 		<string>Siri.Remembers.MessageHistory</string>
 		<string>IntelligenceEngine.Interaction.Donation</string>
+		<string>App.LocationActivity</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>com.apple.duetactivityscheduler.plugin</string>
 		<string>com.apple.das.fairscheduling</string>
 		<string>com.apple.dasd.dailyPeriodic</string>
+		<string>com.apple.dasd.issueDetector</string>
 		<string>com.apple.dasd.swapkills</string>
 		<string>com.apple.dasd.widgetRefreshBudgets</string>
 		<string>com.apple.mt</string>

```
### demod

> `/usr/libexec/demod`

```diff

 	<true/>
 	<key>com.apple.PairingManager.Read</key>
 	<true/>
+	<key>com.apple.PairingManager.RemovePeer</key>
+	<true/>
 	<key>com.apple.PairingManager.Write</key>
 	<true/>
 	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>

```
### hangtracerd

> `/usr/libexec/hangtracerd`

```diff

 	<array>
 		<string>com.apple.HangHUD</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.ReportMemoryException</string>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<array>
 		<string>com.apple.preview-shell.user-alerts</string>
 	</array>
+	<key>com.apple.accessibility.api</key>
+	<true/>
 	<key>com.apple.accessoryupdater.uarp</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

 		<string>com.apple.kvsd</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.carkit.app.service</string>
+		<string>com.apple.accessibility.AXBackBoardServer</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.modelmanager.query</key>
+	<true/>
 	<key>com.apple.private.kernel.darkboot</key>
 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 	<true/>
 	<key>com.apple.powerlog.plxpclogger.xpc</key>
 	<true/>
+	<key>com.apple.private.MobileContainerManager.appGroup.noReference</key>
+	<array>
+		<string>group.com.apple.Journal</string>
+	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>

 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.mobilecal</string>
+		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### passcodenagd

> `/usr/libexec/passcodenagd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.managedconfiguration.profiled</string>
-		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.securityd</string>
+		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.securityd</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.private.logging.admin</key>
 	<true/>
-	<key>com.apple.private.managed-settings.apply</key>
+	<key>com.apple.private.managed-settings.blame</key>
 	<true/>
 	<key>com.apple.private.mis.online_auth_agent</key>
 	<true/>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.MobileAsset.SharingDeviceAssets</key>
 	<true/>
+	<key>com.apple.PCAngel.HandoffUI</key>
+	<true/>
 	<key>com.apple.PairingManager.Read</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

 	<true/>
 	<key>com.apple.private.coordination.timers</key>
 	<true/>
+	<key>com.apple.private.coreservices.cangetcurrentactivityinfo</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

 		<string>com.apple.MobileTimer.alarmserver</string>
 		<string>com.apple.nanoprefsync</string>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
+		<string>com.apple.PCAngel.xpc</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.PointerUI.pointeruid.service</string>
 		<string>com.apple.PowerManagement.control</string>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.private.audio.interprocess-tap</key>
 	<true/>
+	<key>com.apple.private.audio.suppress-mic-indicator</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>ScreenSharing</string>

 	<array>
 		<string>UIStatusBarStyleOverrideScreenReplayRecording</string>
 	</array>
+	<key>com.apple.systemstatus.domains</key>
+	<array>
+		<string>media</string>
+	</array>
+	<key>com.apple.systemstatus.publisher.domains</key>
+	<array>
+		<string>media</string>
+	</array>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>replayd</string>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.backboardd.lastUserEventTime</key>
 	<true/>
+	<key>com.apple.backlight.allowsActivationObservation</key>
+	<true/>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.mobilecal</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>351</string>
 		<string>401</string>
 		<string>406</string>
 		<string>409</string>

 		<string>961</string>
 		<string>1000</string>
 		<string>1210</string>
+		<string>1630</string>
 		<string>1701</string>
 	</array>
 	<key>platform-application</key>

```
### uarppersonalizationd

> `/usr/libexec/uarppersonalizationd`

```diff

 	<true/>
 	<key>com.apple.uarppersonalization</key>
 	<true/>
+	<key>com.apple.uarppersonalization.btleserver</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Device.Wireless.CellularAvailabilityStatus</string>
+		<string>Device.Wireless.ConnectivityContext</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<array>
 		<string>StoreDemoMode</string>
 	</array>
+	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
+	<true/>
+	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.wifid</string>
 	<key>com.apple.private.biome.read-write</key>

```
