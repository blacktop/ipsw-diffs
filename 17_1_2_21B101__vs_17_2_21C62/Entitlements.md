## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Library</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
 		<string>com.apple.appstored.xpc</string>

 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.nfcd.hwmanager</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.AppStoreComponents</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.surfboard.chrome-customization</key>

```
### AirDropUI

> `/Applications/AirDropUI.app/AirDropUI`

```diff

 		<string>com.apple.Sharing</string>
 		<string>com.apple.messages.nicknames</string>
 		<string>com.apple.contacts.sharedProfile</string>
+		<string>com.apple.contacts.namedrop</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 		<string>access-calls</string>
 		<string>modify-calls</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 </dict>
 </plist>
 

```
### AirPlayReceiver

> `/Applications/AirPlayReceiver.app/AirPlayReceiver`

```diff

 	</array>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.driverkit.driver-access</key>
+	<array>
+		<string>com.apple.private.wifi.driverkit</string>
+	</array>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.rapport.Client</key>

 	<array>
 		<string>AirPlaySendingDeviceTime</string>
 	</array>
+	<key>com.apple.wifi.events</key>
+	<true/>
+	<key>com.apple.wifi.events.private</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>com.apple.wifip2pd</key>

```
### AirPlaySenderUIApp

> `/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.intelligentrouting.recommendationservice</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.airplay.discoverybroker</string>
 		<string>com.apple.SystemConfiguration.IPMonitorControl</string>
+		<string>com.apple.intelligentroutingd.xpc.media</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.mediaremote</string>
 		<string>com.apple.airplay</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### AppStore

> `/Applications/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.PromotedContentPrediction.APOdmlSearchResultsExtension</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### ProductPageExtension

> `/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.PromotedContentPrediction.APOdmlSearchResultsExtension</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### SubscribePageExtension

> `/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.PromotedContentPrediction.APOdmlSearchResultsExtension</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### AuthenticationServicesUI

> `/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.airdrop.settings</key>

```
### Camera

> `/Applications/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-capture-filter-rendering</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>

```
### CheckerBoard

> `/Applications/CheckerBoard.app/CheckerBoard`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>

 	<true/>
 	<key>com.apple.runningboard.UIKitKeyboardManagement</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.runningboard.primitiveattribute</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.backboard.system-app-server</string>
+		<string>com.apple.wakeboardd.system</string>
+		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.realitysimulation.bounds</string>
+		<string>com.apple.realitysimulation.host</string>
+		<string>com.apple.realitysimulation.scene</string>
 		<string>com.apple.arkit.service.session</string>
 		<string>com.apple.arkit.service.appClipCode</string>
 		<string>com.apple.makod</string>

```
### CoreAuthUI

> `/Applications/CoreAuthUI.app/CoreAuthUI`

```diff

 	<true/>
 	<key>com.apple.bannerkit.post</key>
 	<true/>
+	<key>com.apple.clarityboard.coreAuthUIPresentation</key>
+	<true/>
+	<key>com.apple.developer.usernotifications.time-sensitive</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.device.verify</key>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.tvappservices.container</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/WebClips/</string>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
-	<key>com.apple.springboard.private.feature-a</key>
+	<key>com.apple.springboard.private.ringer-button-events</key>
 	<true/>
 	<key>com.apple.springboard.setVoiceControlEnabled</key>
 	<true/>

```
### Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.private.applesmc.user-access</key>
+	<true/>
 	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>

 	<array>
 		<string>/private/var/tmp/</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>AppleSMCClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.avfaudio.devicetest.service</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleSMCClient</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.DiagnosticsKit</string>

```
### SystemReport-AirPods

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.accessory.Hearing</string>
 		<string>com.apple.springboard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### SystemReport-iOS-D83-D84

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84`

```diff

 		<string>com.apple.springboard</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.enhanced-logging-state</string>
+		<string>com.apple.accessory.Hearing</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### GameCenterRemoteAlert

> `/Applications/GameCenterRemoteAlert.app/GameCenterRemoteAlert`

```diff

 <dict>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.developer.game-center</key>
+	<array>
+		<string>Account</string>
+		<string>Scores</string>
+		<string>Achievements</string>
+		<string>Challenges</string>
+		<string>Multiplayer</string>
+		<string>TurnBasedMultiplayer</string>
+	</array>
 </dict>
 </plist>
 

```
### GameCenterUIService

> `/Applications/GameCenterUIService.app/GameCenterUIService`

```diff

 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.GameOverlayUI</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### HomeCaptiveViewService

> `/Applications/HomeCaptiveViewService.app/HomeCaptiveViewService`

```diff

 	<dict>
 		<key>CNJ</key>
 		<dict>
+			<key>bleRSSIThresholdHint</key>
+			<integer>-70</integer>
 			<key>discoveryFlags</key>
 			<array>
 				<string>CNJ</string>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	<true/>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>collaborations</string>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.mediasafetynet.exception.callbanner</key>
 	<true/>
 	<key>com.apple.private.mediasafetynet.exception.emergency</key>

 	<array>
 		<string>com.apple.Preferences</string>
 	</array>
+	<key>com.apple.rootless.storage.remotemanagementd</key>
+	<true/>
 	<key>com.apple.runningboard.accessibility</key>
 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.containermanagerd</string>
+		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.posterboardservices.data-store</string>
 		<string>com.apple.familycircle.agent</string>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.developer.usernotifications.communication</key>
 	<true/>
+	<key>com.apple.developer.usersafety.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
 	<key>com.apple.facetimemessagestored.service</key>
 	<array>
 		<string>access-facetime-messaging</string>

 	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.persona.write</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.ManagedSettings</string>
+	</array>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

 	<array>
 		<string>com.apple.tipsd</string>
 	</array>
+	<key>com.apple.rootless.storage.remotemanagementd</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.ManagedSettings</string>
 		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 		<string>/Library/Application Support/com.apple.FaceTime/</string>
 		<string>/Media/PhotoData/</string>
 		<string>/Media/Purchases/</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.facetimemessagestored.service</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.siri.activation.service</string>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.CarPlayApp.service</string>

 		<string>com.apple.datamigrator</string>
 		<string>com.apple.transparencyd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.suggestions</string>
 		<string>com.apple.ClarityUI.PhoneFaceTime</string>
 		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.transparency.kt</key>
 	<true/>
+	<key>com.apple.usersafety.service</key>
+	<array>
+		<string>contacts</string>
+	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>
 	<key>com.apple.visualvoicemail.client</key>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/System/Library/PrivateFrameworks/ChatKit.framework</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 		<string>com.apple.sharing.sharesheetrecipients</string>
 		<string>com.apple.coreduetd.people.user</string>
 		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.transparencyd</string>
+		<string>com.apple.transparencyd.ids</string>
 		<string>com.apple.dmd.emergency-mode</string>
 		<string>com.apple.imfoundation.IMRemoteURLConnectionAgent</string>
 		<string>com.apple.Carousel.eligibilityservice</string>

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.dprivacyd</string>
+		<string>com.apple.transparencyd</string>
+		<string>com.apple.transparencyd.ids</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.proactive.experiments.responses</string>
 		<string>com.apple.avatar.service</string>

 		<string>modify-pending-collaboration</string>
 		<string>access-call-providers</string>
 	</array>
+	<key>com.apple.transparency.kt</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>150</string>

```
### MobileSafari

> `/Applications/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceIDData</string>

 		<string>Safari.AutoPlay</string>
 		<string>Safari.WebPagePerformance</string>
 		<string>Safari.Navigations</string>
+		<string>Safari.PageLoad</string>
 	</array>
 	<key>com.apple.private.can-load-any-content-blocker</key>
 	<true/>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>
-		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceFaceID</string>
 	</array>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.allow-prompting</key>
+	<array>
+		<string>kTCCServiceMediaLibrary</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceMediaLibrary</string>
+	</array>
 	<key>com.apple.private.translation</key>
 	<true/>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>

 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.intelligenceplatform.Feedback</string>
 		<string>com.apple.posterboardui.services</string>
+		<string>com.apple.itunescloudd.tcchelper</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### PhotosReliveWidget

> `/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget`

```diff

 		<key>value</key>
 		<string>com.apple.mobileslideshow</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.XPCStoreOptIn</key>

 	</array>
 	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Media/DCIM/</string>

```
### PhotosReliveWidgetIntents

> `/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidgetIntents.appex/PhotosReliveWidgetIntents`

```diff

 		<key>value</key>
 		<string>com.apple.mobileslideshow</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.XPCStoreOptIn</key>

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Media/DCIM/</string>

```

### 🆕 MomentsUIServiceCore

> `/Applications/MomentsUIService.app/Frameworks/MomentsUIServiceCore.framework/MomentsUIServiceCore`

- No entitlements *(yet)*

### 🆕 MomentsUIService

> `/Applications/MomentsUIService.app/MomentsUIService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.MomentsUIService</string>
	<key>com.apple.CoreRoutine.LocationOfInterest</key>
	<true/>
	<key>com.apple.CoreRoutine.Visit</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.people</key>
	<true/>
	<key>com.apple.coremedia.compressionsession</key>
	<true/>
	<key>com.apple.coremedia.decompressionsession</key>
	<true/>
	<key>com.apple.coremedia.videocodecd.compressionsession</key>
	<true/>
	<key>com.apple.coremedia.videocodecd.compressionsession.xpc</key>
	<true/>
	<key>com.apple.coremedia.videocodecd.decompressionsession</key>
	<true/>
	<key>com.apple.coremedia.videocodecd.decompressionsession.xpc</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.moments.allowSuggestions</key>
	<true/>
	<key>com.apple.momentsd.internal</key>
	<array>
		<string>MOLogPerformance</string>
		<string>MOLogUsage</string>
		<string>MOLogEngagement</string>
		<string>MOReadPermissions</string>
		<string>MORefreshLight</string>
		<string>MOFetchEventBundles</string>
		<string>MOOnboardingAndSettings</string>
		<string>MOUserNotifications</string>
	</array>
	<key>com.apple.photoanalysisd</key>
	<true/>
	<key>com.apple.powerlog.plxpclogger.xpc</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>NowPlaying</string>
	</array>
	<key>com.apple.private.calendar.allow-suggestions</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.authorization_bypass</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.XPCStoreOptIn</key>
	<true/>
	<key>com.apple.private.photos.storytelling.inferenceSummary</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceReminders</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.momentsd.MOUserNotifications</string>
	</array>
	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.Event</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</key>
	<true/>
	<key>com.apple.runningboard.assertions.angeltarget</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.trustedtarget</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.tipsnext</string>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/HTTPStorages/com.apple.MomentsUIService/</string>
		<string>/Library/Application Support/com.apple.MomentsUIService/</string>
		<string>/Library/Saved Application State/com.apple.MomentsUIService.savedState/</string>
		<string>/Library/Logs/com.apple.MomentsUIService/</string>
		<string>/Library/Caches/com.apple.MomentsUIService/</string>
		<string>/Library/com.apple.momentsd/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>AGXDeviceUserClient</string>
		<string>IOHIDEventServiceFastPathUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.coremedia.admin</string>
		<string>com.apple.audioanalyticsd</string>
		<string>com.apple.SBUserNotification</string>
		<string>com.apple.CoreRoutine.helperservice</string>
		<string>com.apple.routined.registration</string>
		<string>com.apple.routined.internal</string>
		<string>com.apple.biome.PublicStreamAccessService</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.proactive.PersonalizationPortrait.Contact</string>
		<string>com.apple.proactive.PersonalizationPortrait.Event</string>
		<string>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.healthd.server</string>
		<string>com.apple.calaccessd</string>
		<string>com.apple.momentsd</string>
		<string>com.apple.backboard.display.services</string>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.iohideventsystem</string>
		<string>com.apple.CARenderServer</string>
		<string>com.apple.symptom_diagnostics</string>
		<string>com.apple.UIKit.KeyboardManagement.hosted</string>
		<string>com.apple.backboard.hid.services</string>
		<string>com.apple.privacyaccountingd</string>
		<string>com.apple.accountsd.accountmanager</string>
		<string>com.apple.PointerUI.pointeruid.service</string>
		<string>com.apple.iphone.axserver-systemwide</string>
		<string>com.apple.audio.AudioSession</string>
		<string>com.apple.TextInput</string>
		<string>com.apple.audio.hapticd</string>
		<string>com.apple.springboard.services</string>
		<string>com.apple.contactsd</string>
		<string>com.apple.sharing.sharesheet</string>
		<string>com.apple.audio.toolbox.reporting.service</string>
		<string>com.apple.commcenter.coretelephony.xpc</string>
		<string>com.apple.iconservices</string>
		<string>com.apple.commcenter.xpc</string>
		<string>com.apple.Sharing.AirDrop.apple-extension-service</string>
		<string>com.apple.Sharing.AirDrop.viewservice</string>
		<string>com.apple.mobilegestalt</string>
		<string>com.apple.DocumentManagerUICore.SaveToFiles.viewservice</string>
		<string>com.apple.MapKit.SnapshotService</string>
		<string>com.apple.callkit.callcontrollerhost</string>
		<string>com.apple.fontservicesd</string>
		<string>com.apple.iphone.axserver-systemwide</string>
		<string>com.apple.accessibility.AXBackBoardServer</string>
		<string>com.apple.AccessibilityUIServer</string>
		<string>com.apple.SystemConfiguration.NetworkInformation</string>
		<string>com.apple.coremedia.asset.xpc</string>
		<string>com.apple.fairplayd.versioned</string>
		<string>com.apple.usymptomsd</string>
		<string>com.apple.AppSSO.service-xpc</string>
		<string>com.apple.nehelper</string>
		<string>com.apple.itunesstored</string>
		<string>com.apple.locationd.registration</string>
		<string>com.apple.locationd.synchronous</string>
		<string>com.apple.coremedia.systemcontroller.xpc</string>
		<string>com.apple.MediaPlayer.RemotePlayerService</string>
		<string>com.apple.coremedia.routediscoverer.xpc</string>
		<string>com.apple.mediaremoted.xpc</string>
		<string>com.apple.itunescloudd.xpc</string>
		<string>com.apple.coremedia.routingcontext.xpc</string>
		<string>com.apple.medialibraryd.xpc</string>
		<string>com.apple.coremedia.volumecontroller.xpc</string>
		<string>com.apple.coremedia.asset.xpc</string>
		<string>com.apple.MTLCompilerService</string>
		<string>com.apple.coremedia.customurlloader.xpc</string>
		<string>com.apple.coremedia.player.xpc</string>
		<string>com.apple.adid</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.Music.MPMusicPlayerControllerInternal</string>
		<string>com.apple.PowerManagement.control</string>
		<string>com.apple.accessibility.mediaaccessibilityd</string>
		<string>com.apple.backboard.hid-services.xpc</string>
		<string>com.apple.pasteboard.pasted</string>
		<string>com.apple.accounts</string>
		<string>com.apple.WebKit</string>
		<string>com.apple.Safari.SafeBrowsing.Service</string>
		<string>com.apple.coremedia.mutablecomposition.xpc</string>
		<string>com.apple.coremedia.decompressionsession</string>
		<string>com.apple.coremedia.formatreader.xpc</string>
		<string>com.apple.coremedia.mediaplaybackd.asset.xpc</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession.xpc</string>
		<string>com.apple.coremedia.mediaplaybackd.customurlloader.xpc</string>
		<string>com.apple.coremedia.mediaplaybackd.sandboxserver.xpc</string>
		<string>com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc</string>
		<string>com.apple.coremedia.mediaplaybackd.player.xpc</string>
		<string>com.apple.coremedia.mediaplaybackd.formatreader.xpc</string>
		<string>com.apple.coremedia.mediaparserd.formatreader.xpc</string>
		<string>com.apple.FileProvider</string>
		<string>com.apple.photos.VideoConversionService</string>
		<string>com.apple.photos.ImageConversionService</string>
		<string>com.apple.FileCoordination</string>
		<string>com.apple.adid.xpc</string>
		<string>com.apple.hangtracermonitor</string>
		<string>com.apple.coremedia.compressionsession</string>
		<string>com.apple.coremedia.decompressionsession</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession</string>
		<string>com.apple.coremedia.videocodecd.compressionsession</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession.xpc</string>
		<string>com.apple.coremedia.videocodecd.compressionsession.xpc</string>
		<string>com.apple.usernotifications.listener</string>
		<string>com.apple.inputservice.input-ui-host</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.local-name</key>
	<array>
		<string>com.apple.accessibility.gax.backboard</string>
		<string>com.apple.iphone.axserver</string>
	</array>
	<key>com.apple.security.exception.mach-register.local-name</key>
	<array>
		<string>com.apple.iphone.axserver</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.preferences.sounds</string>
		<string>com.apple.mediaaccessibility</string>
		<string>com.apple.mobileipod</string>
		<string>com.apple.camera</string>
		<string>com.apple.coremedia</string>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.itunescloud</string>
		<string>com.apple.amsengagementd</string>
		<string>com.apple.momentsd</string>
		<string>com.apple.MomentsUIService</string>
		<string>com.apple.SocialLayer</string>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.mobilecal</string>
		<string>com.apple.UIKit</string>
		<string>com.apple.coreaudio</string>
		<string>com.apple.keyboard</string>
		<string>com.apple.keyboard.preferences</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.MomentsUIService</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.geoservices</key>
	<true/>
	<key>com.apple.security.ts.mobile-keybag-access</key>
	<true/>
	<key>com.apple.security.ts.render-images</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.MomentsUIService</string>
	<key>com.apple.security.ts.webkit-client</key>
	<true/>
	<key>com.apple.security.ts.xpc-service-name</key>
	<array>
		<string>com.apple.healthd.server</string>
	</array>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>1420</string>
	</array>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 NewDeviceSetupUIService

> `/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.bluetooth.discovery</key>
	<dict>
		<key>NewDeviceSetupUIService</key>
		<dict>
			<key>discoveryFlags</key>
			<array>
				<string>macOSSetup</string>
			</array>
			<key>viewControllerClassName</key>
			<string>FirstAlertViewController</string>
		</dict>
	</dict>
	<key>com.apple.springboard-ui.client</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.springboard.requestScene-daemon</key>
	<true/>
	<key>com.apple.sptingboard.activateRemoteAlert</key>
	<true/>
</dict>
</plist>

```
### PASViewService

> `/Applications/PASViewService.app/PASViewService`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.ShortExpiration</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.Ratchet</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>com.apple.CoreODI</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>com.apple.CoreODI</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache/Library/Caches/com.apple.IconsCache/</string>

```
### PosterBoard

> `/Applications/PosterBoard.app/PosterBoard`

```diff

 		<string>com.apple.chronod</string>
 		<string>com.apple.springboard</string>
 	</array>
+	<key>com.apple.security.system-container</key>
+	<true/>
 	<key>com.apple.springboard.allowIconVisibilityChanges</key>
 	<true/>
 	<key>com.apple.springboard.homeScreenLayout</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.FamilyControls.private-client</key>
 	<true/>
+	<key>com.apple.Maps.tripsharing.sharing</key>
+	<true/>
 	<key>com.apple.MobileInternetSharing.allow</key>
 	<true/>
 	<key>com.apple.ModeEntityScorer</key>

 	<key>com.apple.coreidvd.digital-presentment.merchants</key>
 	<array>
 		<string>com.apple.ams-identity-verification</string>
+		<string>com.apple.asa-identity-verification</string>
 	</array>
 	<key>com.apple.coreidvd.document-upload</key>
 	<true/>

 		<string>CloudDocuments</string>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.in-app-identity-presentment</key>
+	<dict>
+		<key>document-types</key>
+		<array>
+			<string>us-drivers-license</string>
+		</array>
+		<key>elements</key>
+		<array>
+			<string>given-name</string>
+			<string>family-name</string>
+			<string>address</string>
+			<string>issuing-authority</string>
+			<string>document-expiration-date</string>
+			<string>document-issue-date</string>
+			<string>document-number</string>
+			<string>driving-privileges</string>
+			<string>date-of-birth</string>
+		</array>
+	</dict>
+	<key>com.apple.developer.in-app-identity-presentment.merchant-identifiers</key>
+	<array>
+		<string>com.apple.asa-identity-verification</string>
+	</array>
 	<key>com.apple.developer.networking.wifi-info</key>
 	<true/>
 	<key>com.apple.developer.pass-type-identifiers</key>

 	<true/>
 	<key>com.apple.finance.store</key>
 	<true/>
+	<key>com.apple.financekit.financial-connection.host</key>
+	<true/>
 	<key>com.apple.frontboard.delete-application-snapshots</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
+	<array>
+		<string>CloudLockedRemoval</string>
+	</array>
 	<key>com.apple.managedconfiguration.profiled.get</key>
 	<array>
 		<string>MDMInfo</string>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.SetDSLModeEnabled</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

 		<string>CommunicationSafetyResult</string>
 		<string>CommunicationSafetyResultWithoutImage</string>
 		<string>modeConfigurationUIFlowLoggingEvent</string>
+		<string>SystemSettings.GestureEducation.Multitasking</string>
+		<string>SystemSettings.GestureEducation.PillOutcome</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.safetyalerts.spi</key>
+	<true/>
 	<key>com.apple.securebackupd.access</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.maps.virtualgarage.server</string>
 		<string>com.apple.seserviced.sereservation.client</string>
 		<string>com.apple.eyereliefd</string>
+		<string>com.apple.Maps.MapsSync.store</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### RemoteiCloudQuotaUI

> `/Applications/RemoteiCloudQuotaUI.app/RemoteiCloudQuotaUI`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>re6Zb+zwFKJNlkQTUeT+/w</string>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueChipID</string>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.SetDSLModeEnabled</key>
+	<true/>
 	<key>com.apple.private.MobileActivation</key>
 	<array>
 		<string>GetActivationState</string>

 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>SystemSettings.AppearanceSetup</string>
+		<string>SystemSettings.ChildMultitaskingSetup</string>
+		<string>AppleID.ChildSetup</string>
+	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.cloudkit.buddyAccess</key>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.UI</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceCamera</string>
+		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceWillow</string>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.idle-timer-services</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

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
 	<key>com.apple.frontboard.systemappservices</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.caraccessoryframework.gatekeeper</string>
 		<string>com.apple.sirisuggestions</string>
 		<string>com.apple.siriinferenced</string>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
+	<key>com.apple.private.sleepd</key>
+	<true/>
 	<key>com.apple.private.sportskit.client</key>
 	<true/>
 	<key>com.apple.private.subscriptionservice.internal</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.weather.internal</string>
+		<string>group.tvappservices.container</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### TVAccessViewService

> `/Applications/TVAccessViewService.app/TVAccessViewService`

```diff

 	<array>
 		<string>com.apple.tv</string>
 	</array>
+	<key>com.apple.surfboard.chrome-customization</key>
+	<true/>
 	<key>com.apple.watchlist.private</key>
 	<true/>
 	<key>keychain-access-groups</key>

```

### 🆕 JournalDataclassOwner

> `/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner`

- No entitlements *(yet)*

### 🆕 TransparencyAccountNotification

> `/System/Library/Accounts/Notification/TransparencyAccountNotification.bundle/TransparencyAccountNotification`

- No entitlements *(yet)*
### ClarityBoard

> `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/preferences/com.apple.networkd.plist</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
+		<string>/Library/Audio/Tunings/Generic/Haptics/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.iphone.axserver-systemwide</string>
 		<string>com.apple.itunesstored.xpc</string>
+		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.misagent</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 		<string>Device.Display.Appearance</string>
 		<string>Device.Display.AlwaysOn</string>
 		<string>OSAnalytics.Hardware.Reliability</string>
+		<string>SpringBoard.GestureEducation.PillLaunch</string>
 	</array>
 	<key>com.apple.private.biome.realTimeSensorSession</key>
 	<true/>

```

### 🆕 MapsDigitalSeparation

> `/System/Library/DigitalSeparation/SharingSources/MapsDigitalSeparation.bundle/MapsDigitalSeparation`

- No entitlements *(yet)*
### BitacoraWorker

> `/System/Library/ExtensionKit/Extensions/BitacoraWorker.appex/BitacoraWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.LighthouseBitacoraFramework.BitacoraWorker</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.LighthouseBitacoraFramework.BitacoraWorker</string>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
 		<string>Lighthouse.Ledger.DediscoPrivacyEvent</string>
 	</array>
+	<key>com.apple.private.dprivacyd.allow</key>
+	<true/>
+	<key>com.apple.private.dprivacyd.metadata.allow</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.triald.namespace-management </string>
 		<string>com.apple.siri.analytics.assistant</string>
 	</array>

```

### 🆕 MADViewServiceExtension

> `/System/Library/ExtensionKit/Extensions/MADViewServiceExtension.appex/MADViewServiceExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.managed-app-distribution.install-ui</key>
	<array>
		<string>managed-app</string>
	</array>
	<key>com.apple.mdm-view-service-extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.managedappdistributiond.xpc</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
</dict>
</plist>

```

### 🆕 MetricsExtension

> `/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.metrics.MetricsExtension</string>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.metrics.MetricsExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
		<string>Siri.Metrics.OnDeviceDigestUsageMetrics</string>
		<string>Siri.Metrics.OnDeviceDigestSegmentsCohorts</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
</dict>
</plist>

```

### 🆕 PFLHRPeriodPredCK

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLHRPeriodPredCK</string>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.pfl.container</string>
		<string>com.apple.pfl.preprod.container</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.dprivacyd.metadata.allow</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.access</key>
	<array>
		<string>menstrual-cycles-spi</string>
	</array>
	<key>com.apple.private.healthkit.read_authorization_bypass</key>
	<array>
		<string>HKCharacteristicTypeIdentifierUserEnteredMenstrualCycleLength</string>
		<string>HKCharacteristicTypeIdentifierUserEnteredMenstrualPeriodLength</string>
		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
		<string>HKCategoryTypeIdentifierMenstrualFlow</string>
		<string>HKCategoryTypeIdentifierIntermenstrualBleeding</string>
		<string>HKCategoryTypeIdentifierSexualActivity</string>
		<string>HKCategoryTypeIdentifierCervicalMucusQuality</string>
		<string>HKCategoryTypeIdentifierOvulationTestResult</string>
		<string>HKCategoryTypeIdentifierPregnancyTestResult</string>
		<string>HKCategoryTypeIdentifierProgesteroneTestResult</string>
		<string>HKCategoryTypeIdentifierPregnancy</string>
		<string>HKCategoryTypeIdentifierLactation</string>
		<string>HKCategoryTypeIdentifierContraceptive</string>
		<string>HKQuantityTypeIdentifierBasalBodyTemperature</string>
		<string>HKQuantityTypeIdentifierAppleSleepingWristTemperature</string>
		<string>HKQuantityTypeIdentifierHeartRate</string>
		<string>HKCategoryTypeIdentifierProlongedMenstrualPeriods</string>
		<string>HKCategoryTypeIdentifierPersistentIntermenstrualBleeding</string>
		<string>HKCategoryTypeIdentifierIrregularMenstrualCycles</string>
		<string>HKCategoryTypeIdentifierInfrequentMenstrualCycles</string>
		<string>HKCategoryTypeIdentifierAbdominalCramps</string>
		<string>HKCategoryTypeIdentifierAcne</string>
		<string>HKCategoryTypeIdentifierAppetiteChanges</string>
		<string>HKCategoryTypeIdentifierBladderIncontinence</string>
		<string>HKCategoryTypeIdentifierBloating</string>
		<string>HKCategoryTypeIdentifierBreastPain</string>
		<string>HKCategoryTypeIdentifierChills</string>
		<string>HKCategoryTypeIdentifierConstipation</string>
		<string>HKCategoryTypeIdentifierDiarrhea</string>
		<string>HKCategoryTypeIdentifierDrySkin</string>
		<string>HKCategoryTypeIdentifierFatigue</string>
		<string>HKCategoryTypeIdentifierHairLoss</string>
		<string>HKCategoryTypeIdentifierHeadache</string>
		<string>HKCategoryTypeIdentifierHotFlashes</string>
		<string>HKCategoryTypeIdentifierLowerBackPain</string>
		<string>HKCategoryTypeIdentifierMemoryLapse</string>
		<string>HKCategoryTypeIdentifierMoodChanges</string>
		<string>HKCategoryTypeIdentifierNausea</string>
		<string>HKCategoryTypeIdentifierNightSweats</string>
		<string>HKCategoryTypeIdentifierPelvicPain</string>
		<string>HKCategoryTypeIdentifierSleepChanges</string>
		<string>HKCategoryTypeIdentifierVaginalDryness</string>
		<string>HKCategoryTypeIdentifierSleepAnalysis</string>
		<string>HKQuantityTypeIdentifierHeartRateVariabilitySDNN</string>
		<string>HKQuantityTypeIdentifierRestingHeartRate</string>
	</array>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.healthd.server</string>
		<string>com.apple.HealthAlgorithms.HistoricalAnalyzerService</string>
		<string>com.apple.HealthAlgorithms.DayStreamProcessorService</string>
	</array>
</dict>
</plist>

```
### RepackagingWorker

> `/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.RepackagingWorker</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
+	<key>com.apple.private.feedbacklogger</key>
+	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	<array>
 		<string>com.apple.triald.namespace-management </string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.assistant.settings</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```

### 🆕 SiriMASPFLPlugin

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPlugin.appex/SiriMASPFLPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLMLHostPlugins.SiriMASPFLPlugin</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.AppSelection.Music</string>
	</array>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.dprivacyd.metadata.allow</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### com.apple.mlhost.CloudWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.mlhost.CloudWorker</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.mlhost.CloudWorker</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### com.apple.mlhost.QuartzWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.QuartzWorker.appex/com.apple.mlhost.QuartzWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.mlhost.QuartzWorker</string>
-	<key>com.apple.developer.healthkit</key>
+	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
-	<key>com.apple.private.healthkit</key>
+	<key>com.apple.developer.applesignin</key>
+	<array>
+		<string></string>
+	</array>
+	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
-	<key>com.apple.private.healthkit.access</key>
-	<array/>
-	<key>com.apple.private.healthkit.read_authorization_bypass</key>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>lifeEventMap</string>
+		<string>lifeEventSubgraph</string>
+	</array>
+	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>HKQuantityTypeIdentifierVO2Max</string>
-		<string>HKQuantityTypeIdentifierRestingHeartRate</string>
-		<string>HKQuantityTypeIdentifierHeartRateVariabilitySDNN</string>
-		<string>HKWorkoutTypeIdentifier</string>
-		<string>HKQuantityTypeIdentifierDistanceWalkingRunning</string>
-		<string>HKQuantityTypeIdentifierActiveEnergyBurned</string>
-		<string>HKQuantityTypeIdentifierAppleExerciseTime</string>
-		<string>HKQuantityTypeIdentifierAppleMoveTime</string>
-		<string>HKQuantityTypeIdentifierAppleStandTime</string>
-		<string>HKQuantityTypeIdentifierNumberOfTimesFallen</string>
-		<string>HKCategoryTypeIdentifierMindfulSession</string>
-		<string>HKQuantityTypeIdentifierTimeInDaylight</string>
-		<string>HKCategoryTypeIdentifierSleepAnalysis</string>
-		<string>HKCategoryTypeIdentifierSleepChanges</string>
-		<string>HKQuantityTypeIdentifierHeartRate</string>
-		<string>HKQuantityTypeIdentifierStepCount</string>
-		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
-		<string>HKQuantityTypeIdentifierBodyMass</string>
-		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
-		<string>HKQuantityTypeIdentifierHeight</string>
+		<string>kTCCServiceCalendar</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.routined.registration</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.mlhost.SampleWorker</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.mlhost.SampleWorker</string>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MLHostTask</string>

 	<true/>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MLHostTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.mlhost.TelemetryWorker</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.mlhost.TelemetryWorker</string>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>Lighthouse.Ledger.TaskTelemetry</string>

 	</dict>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.mlhost</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 	</array>
-	<key>com.apple.security.ts.application-group-support</key>
-	<true/>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.mlhost</string>
+	</array>
 </dict>
 </plist>
 

```
### ContactViewViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService`

```diff

 	<true/>
 	<key>com.apple.developer.ubiquity-container-identifiers</key>
 	<true/>
+	<key>com.apple.developer.usersafety.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	</dict>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>
 	<true/>
+	<key>com.apple.private.communicationsfilter</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

 	<array>
 		<string>/Media/PhotoData/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
+		<string>/Library/com.apple.ManagedSettings/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.contacts.donation.agent</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
+		<string>com.apple.transparencyd</string>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<array>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<array>
 		<string>access-call-providers</string>
 	</array>
+	<key>com.apple.transparency.kt</key>
+	<true/>
+	<key>com.apple.usersafety.service</key>
+	<string>contacts</string>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### ContactsViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService`

```diff

 	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
+	<key>com.apple.developer.usersafety.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	</dict>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>
 	<true/>
+	<key>com.apple.private.communicationsfilter</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

 	<array>
 		<string>/Media/PhotoData/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
+		<string>/Library/com.apple.ManagedSettings/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.privacyaccountingd</string>
+		<string>com.apple.transparencyd</string>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<array>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<array>
 		<string>access-call-providers</string>
 	</array>
+	<key>com.apple.transparency.kt</key>
+	<true/>
+	<key>com.apple.usersafety.service</key>
+	<string>contacts</string>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.fileprovider.extension-host</key>

 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.OTATaskingAgent</string>
+		<string>com.apple.duetactivityscheduler</string>
 	</array>
 	<key>com.apple.spaceattribution.private</key>
 	<true/>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.financekit.financial-insights.host</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.NPKCompanionAgent.library</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### com.apple.HealthKit.HealthDiagnosticExtension

> `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthDiagnosticExtension.appex/com.apple.HealthKit.HealthDiagnosticExtension`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.Carousel</string>
+		<string>com.apple.private.health.age-gating</string>
+		<string>com.apple.private.health.feature-availability-requirement-overrides</string>
+		<string>com.apple.nanolifestyle.privacy</string>
+		<string>com.apple.private.health.respiratory</string>
 	</array>
 </dict>
 </plist>

```
### ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

 	<string>OOPCocoa</string>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>autobox</string>
 	<key>com.apple.security.exception.files.absolute-path.read</key>
 	<array>
 		<string>/private/var/mobile/Library/Preferences/.GlobalPreferences.plist</string>

```
### coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CoreRoutine.AuthorizedLocation</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

 	<true/>
 	<key>com.apple.keystore.device.verify</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.capturecredential.allow</key>

 	<true/>
 	<key>com.apple.private.applecredentialmanager.securestore.macbuddy.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.securestore.ratchet.config.allow</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.securestore.ratchet.reset.allow</key>
 	<true/>
 	<key>com.apple.private.bmk.allow</key>

 	<array>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.CoreAuthUI</string>
+	</array>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 	<array>
 		<string>com.apple.springboard.services</string>
 		<string>com.apple.iohideventsystem</string>
+		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.routined.registration</string>
+		<string>com.apple.locationd.synchronous</string>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```

### 🆕 managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>409835401</string>
	<key>application-identifier</key>
	<string>com.apple.managedappdistributiond</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.dmd-access</key>
	<true/>
	<key>com.apple.dmd.operation.fetch-apps</key>
	<true/>
	<key>com.apple.dmd.operation.set-app-associated-domains</key>
	<true/>
	<key>com.apple.dmd.operation.set-app-associated-domains-enable-direct-downloads</key>
	<true/>
	<key>com.apple.dmd.operation.set-app-extension-uuids</key>
	<true/>
	<key>com.apple.dmd.operation.set-app-removability</key>
	<true/>
	<key>com.apple.dmd.operation.set-app-tap-to-pay-screen-lock</key>
	<true/>
	<key>com.apple.dmd.operation.start-managing-app</key>
	<true/>
	<key>com.apple.dmd.operation.update-app</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled.get</key>
	<array>
		<string>MDMInfo</string>
	</array>
	<key>com.apple.networkd.set_source_application</key>
	<true/>
	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
	<true/>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.private.InstallCoordination.ignoreRemovability</key>
	<true/>
	<key>com.apple.private.InstallCoordination.uninstall</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
		<string>UniqueDeviceIDData</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.nsurlsession.impersonate</key>
	<true/>
	<key>com.apple.private.nsurlsession.set-task-priority</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/com.apple.AppleMediaServices/</string>
		<string>/Library/Application Support/managedappdistributiond/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Caches/com.apple.managedappdistributiond/</string>
		<string>/Library/HTTPStorages/com.apple.managedappdistributiond/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.apsd</string>
		<string>com.apple.AssetCacheLocatorService</string>
		<string>com.apple.cache_delete.public</string>
		<string>com.apple.commcenter.coretelephony.xpc</string>
		<string>com.apple.fairplayd.versioned</string>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.installcoordinationd</string>
		<string>com.apple.lsd.installation</string>
		<string>com.apple.lsd.modifydb</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.mobile.installd</string>
		<string>com.apple.pearld</string>
		<string>com.apple.SBUserNotification</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.dmd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.appstored</string>
		<string>com.apple.itunesstored</string>
		<string>com.apple.amsengagementd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.managedappdistributiond</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.system-container</key>
	<true/>
	<key>com.apple.security.ts.mobile-keybag-access</key>
	<true/>
	<key>com.apple.security.ts.power-assertions</key>
	<true/>
	<key>com.apple.security.ts.read-any-bundle</key>
	<true/>
	<key>com.apple.security.ts.springboard-services</key>
	<true/>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.usermanagerd.persona.setbundle</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.SiriVocabulary</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceSpeechRecognition</string>

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/Assistant/SiriVocabulary/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```

### 🆕 JournalSettings

> `/System/Library/PreferenceBundles/JournalSettings.bundle/JournalSettings`

- No entitlements *(yet)*

### 🆕 NameAndPhotoSettingsBundle

> `/System/Library/PreferenceBundles/NameAndPhotoSettingsBundle.bundle/NameAndPhotoSettingsBundle`

- No entitlements *(yet)*
### axauditd

> `/System/Library/PrivateFrameworks/AccessibilityAudit.framework/Support/axauditd`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.accessibility.AXMossdeepServer</string>
+		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.iconservices</string>
+		<string>com.apple.containermanagerd.system</string>
+		<string>com.apple.royad</string>
+		<string>com.apple.accessibility.AXMossdeepServer</string>
+		<string>com.apple.accessibility.AXSurfBoardServer</string>
+		<string>com.apple.realitysimulation.apps</string>
+		<string>com.apple.realitysystemsupport.hid_server_backboard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 appinstallationmetricsd

> `/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.appinstallationmetricsd</string>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.keystore.absinthe</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.lookup</key>
	<dict>
		<key>appData</key>
		<true/>
	</dict>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<true/>
	<key>com.apple.private.ProvInfoIOKitUserClient.access</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/com.apple.AppleMediaServices/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.xpc.amsengagementd</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>com_apple_driver_FairPlayIOKitUserClient</string>
		<string>IOAESAccelerator</string>
		<string>IOAESAcceleratorUserClient</string>
		<string>ProvInfoIOKitUserClient</string>
	</array>
	<key>com.apple.security.iokit-user-client-class entitlement</key>
	<true/>
	<key>com.apple.security.system-container</key>
	<true/>
</dict>
</plist>

```
### appstorecomponentsd

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd`

```diff

 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.Carousel.authAlertXPCService</string>
 		<string>com.apple.appconduitd.application-manager</string>
+		<string>com.apple.storekitd</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<string>com.apple.appstorecomponentsd</string>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.storekit.client-override</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appinstallationmetrics</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.adid</string>
+		<string>com.apple.appinstallationmetrics.xpc</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.ak.authorizationservices.xpc</string>

```
### AAUIFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### AMSFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/PlugIns/AMSFollowUpExtension.appex/AMSFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Library</string>
 		<string>Queue</string>
 		<string>Install</string>
 	</array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.xpc.amsaccountsd</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 	</array>
 	<key>com.apple.symptom_analytics.query</key>

```
### AppleMediaServicesUIDynamicService

> `/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/XPCServices/AppleMediaServicesUIDynamicService.xpc/AppleMediaServicesUIDynamicService`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>Library</string>
 		<string>Queue</string>
 		<string>Install</string>
 	</array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.xpc.amsaccountsd</string>

 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 	</array>
 	<key>com.apple.symptom_analytics.query</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<string>com.apple.weather</string>
 	<key>com.apple.duet.expertcenter.consumer</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.fitcore</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.siri.pommes_search_xpc_service</string>
 		<string>com.apple.routined.safetyMonitor</string>
 		<string>com.apple.TextUnderstanding.SmartReplies.Inference</string>

 		<string>871</string>
 		<string>872</string>
 		<string>873</string>
+		<string>874</string>
 		<string>910</string>
 		<string>961</string>
 		<string>353</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<array>
 		<string>PostSiriEngagement</string>
 		<string>Siri.PostSiriEngagement</string>
+		<string>Siri.SELFProcessedEvent</string>
 		<string>Siri.VoiceTriggerStatistics</string>
 		<string>SiriExecution</string>
 		<string>SiriPrivateLearningSELFEvent</string>

 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
-	<string>com.apple.assistantd</string>
+	<array>
+		<string>com.apple.assistantd</string>
+		<string>com.apple.WorkflowKit.BackgroundShortcutRunner</string>
+	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siri.acousticsignature</key>

 	<array>
 		<string>1000</string>
 		<string>1220</string>
+		<string>1221</string>
 		<string>1230</string>
 		<string>1570</string>
 		<string>1571</string>

 		<string>SIRI_DATA_INTEGRATION_TEST1</string>
 		<string>SIRI_DATA_INTEGRATION_TEST2</string>
 		<string>SIRI_DICTATION_ASSETS</string>
+		<string>SIRI_INFORMATION_CACHING</string>
 		<string>SIRI_MEMORY_SYNC_CONFIG</string>
 		<string>SIRI_MESSAGES_ANNOUNCE_HINT_EDUCATION</string>
 		<string>SIRI_MESSAGES_APP_SELECTION</string>

 		<string>SIRI_REFERENCE_RESOLUTION_LIGHTHOUSE_PLUGIN</string>
 		<string>SIRI_REFERENCE_RESOLUTION_LIGHTHOUSE_PLUGIN_FOR_SHADOW_LOGGING</string>
 		<string>SIRI_SPEECH_SV_SPEECH_PROFILE</string>
+		<string>SIRI_SUGGESTIONS_DOMAIN_GROUP_A</string>
+		<string>SIRI_SUGGESTIONS_DOMAIN_GROUP_B</string>
 		<string>SIRI_SUGGESTIONS_PLATFORM</string>
 		<string>SIRI_UI_RESPONSES_SETTINGS</string>
 		<string>SIRI_UNDERSTANDING_CLASSIC_DEPRECATION</string>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.BiometricLivenessFlag</key>
+	<true/>
 	<key>com.apple.private.MobileActivation</key>
 	<array>
 		<string>RequestActivationState</string>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
 	<true/>
+	<key>com.apple.carousel.nonmatchingsessions</key>
+	<true/>
 	<key>com.apple.chrono.event-service-publisher</key>
 	<true/>
 	<key>com.apple.coreduet.knowledge</key>

 	<array>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.StatusKit.local</string>
+		<string>com.apple.carousel.sessionservice</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```

### 🆕 EasyMAIDSignInPicker

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/Extensions/EasyMAIDSignInPicker.appex/EasyMAIDSignInPicker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.developer.ClassKit-environment</key>
	<string>production</string>
	<key>com.apple.private.ClassKit.dashboard</key>
	<true/>
	<key>com.apple.private.ClassKit.register-dashboard</key>
	<true/>
	<key>com.apple.private.ClassKit.search</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.studentd</string>
		<string>com.apple.bluetooth.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.easymaidsignin</string>
	</array>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.studentd</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.easymaidsignin</string>
	</array>
	<key>com.apple.studentd-access</key>
	<true/>
	<key>com.apple.usermanagerd.persona.fetch</key>
	<true/>
</dict>
</plist>

```
### cloudd

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd`

```diff

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.octagon.walrus</key>
+	<true/>
 	<key>com.apple.private.protectedcloudstorage.keysyncing</key>
 	<true/>
 	<key>com.apple.private.rtcreportingd</key>

```
### accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.timed.accessory-timesync</string>
+		<string>com.apple.sysdiagnose.service.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### CDPFollowUpExtension

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceFaceID</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/Keychains/Analytics/</string>

```
### parsec-fbf

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.PegasusConfiguration</string>
+		<string>group.com.apple.feedbacklogger</string>
 	</array>
 	<key>com.apple.rootless.storage.coreparsec_uploadables</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.PegasusConfiguration</string>
+		<string>group.com.apple.feedbacklogger</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.purplebuddy</string>
+		<string>com.apple.da</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
-		<string>com.apple.da</string>
 	</array>
 	<key>com.apple.security.system-group-containers</key>
 	<array>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.phs</key>
 	<true/>
+	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siri.speech-dictation-personalization</key>
+	<true/>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<string>Dictation.UserEdit</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>Emoji.Engagement</string>
+		<string>Dictation.UserEdit</string>
 		<string>Siri.VoiceTriggerStatistics</string>
+		<string>SiriDictation</string>
 		<string>Siri.SelfTriggerSuppression</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/DES/Records/com.apple.siri.speech-dictation-personalization/</string>
 		<string>/Library/VoiceTrigger/</string>
 		<string>/Library/Logs/CrashReporter/Assistant/</string>
 		<string>/Library/Logs/CrashReporter/VoiceTrigger/</string>

```

### 🆕 threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.iokit.powerdxpc</key>
	<false/>
	<key>com.apple.private.ckks</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.corewifi-xpc</key>
	<true/>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.private.iokit.darkwake-control</key>
	<false/>
	<key>com.apple.private.iokit.powersource-control</key>
	<false/>
	<key>com.apple.private.keychain.performance_impacting_api</key>
	<true/>
	<key>com.apple.private.nehelper.privileged</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>wpantund</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.WirelessCoexManager</string>
		<string>com.apple.SBUserNotification</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.homed</string>
		<string>com.apple.ccmapping_ios</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.threadradiodData</string>
		<string>com.apple.threadradiodeMACDB</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>AppleFillmoreUserClient</string>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.srp-mdns-proxy.proxy</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.thread.network</string>
		<string>com.apple.thread.dataset</string>
		<string>com.apple.preferred.network</string>
		<string>com.apple.frozen.network</string>
		<string>apple</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.migration</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper</string>
 	</dict>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>SystemSettings.AppearanceSetup</string>
+		<string>SystemSettings.ChildMultitaskingSetup</string>
+	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.calendar.migration</key>

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceWillow</string>
 	</array>
-	<key>com.apple.private.tcc.manager</key>
-	<true/>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceLiverpool</string>
+		<string>kTCCServiceUbiquity</string>
+	</array>
 	<key>com.apple.private.ubiquity-kvstore-access</key>
 	<array>
 		<string>com.apple.springboard</string>

```

### 🆕 AirPlayDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.coremedia.endpoint.xpc</string>
		<string>com.apple.coremedia.routediscoverer.xpc</string>
		<string>com.apple.coremedia.routingcontext.xpc</string>
	</array>
</dict>
</plist>

```
### AudioDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AudioDiagnosticExtension.appex/AudioDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/var/mobile/tmp/AudioCapture/</string>
+		<string>/private/var/mobile/tmp/com.apple.audiomxd/AudioCapture/</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/Assistant/AVVCCapture/</string>
 		<string>/private/var/tmp/AudioStateDump/</string>
-		<string>/private/var/mobile/tmp/com.apple.audiomxd/AudioCapture/</string>
-		<string>/private/var/mobile/tmp/AudioCapture/</string>
+		<string>/private/var/mobile/tmp/AudioCapture/DiagnosticExtensionFiles/</string>
+		<string>/private/var/mobile/tmp/com.apple.audiomxd/AudioCapture/DiagnosticExtensionFiles</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Audio/</string>
+		<string>/private/var/mobile/Library/Logs/CrashReporter/AudioDiagnosticExtension/</string>
 	</array>
 </dict>
 </plist>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.keystore.allow.background-processing-assertions</key>
+	<true/>
 	<key>com.apple.mobile.keybagd.UserManager.sync</key>
 	<true/>
 	<key>com.apple.mobilemail.mailservices</key>

 	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
+	<key>com.apple.private.corerecents</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.bundleid</key>

```
### GameCenterAuthenticateExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterAuthenticateExtension.appex/GameCenterAuthenticateExtension`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.avatar.store</key>

 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### GameCenterDashboardExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterDashboardExtension.appex/GameCenterDashboardExtension`

```diff

 	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.private.corewifi-xpc</key>
 	<true/>
+	<key>com.apple.private.fillmore.getTriggerStats</key>
+	<true/>
+	<key>com.apple.private.fillmore.provideEmac</key>
+	<true/>
+	<key>com.apple.private.fillmore.startPairing</key>
+	<true/>
+	<key>com.apple.private.fillmore.stopPairing</key>
+	<true/>
+	<key>com.apple.private.fillmore.threadLeave</key>
+	<true/>
+	<key>com.apple.private.fillmore.threadStart</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.get-system-corpse</key>

 		<string>com.apple.coreautomationd.xpc.root</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.nanoprefsync</string>
-		<string>com.apple.security.octagon</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.wpantund.xpc</string>
 		<string>com.apple.sleepd.sleepserver</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.timed.xpc</string>
+        <string>com.apple.transparencyd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.private.ids.report-spam-message</key>
 	<true/>
+    <key>com.apple.transparency.kt</key>
+    <true/>
 </dict>
 </plist>
 

```
### IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent`

```diff

 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 		<string>UserFocusComputedMode</string>
 		<string>AppIntent</string>
 		<string>TextUnderstanding.DocumentUnderstanding.Poem</string>
+		<string>Motion.Activity</string>
 	</array>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>

```
### LighthouseBitacoraPlugin

> `/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/PlugIns/LighthouseBitacoraPlugin.appex/LighthouseBitacoraPlugin`

```diff

 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
 		<string>Lighthouse.Ledger.DediscoPrivacyEvent</string>
 	</array>
+	<key>com.apple.private.dprivacyd.metadata.allow</key>
+	<string>YES</string>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

 	<array>
 		<string>com.apple.triald.namespace-management </string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.private.dprivacyd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd</string>
 	</dict>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>MediaAnalysis.VisualSearch.Processing</string>
+	</array>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

 		<string>585</string>
 		<string>586</string>
 		<string>588</string>
+		<string>589</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd</string>
 	</dict>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>MediaAnalysis.VisualSearch.Processing</string>
+	</array>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

 		<string>585</string>
 		<string>586</string>
 		<string>588</string>
+		<string>589</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 		<string>com.apple.distributed_notifications@Uv3</string>
 		<string>com.apple.SharePlay.NearbyInvitationsService</string>
 		<string>com.apple.StatusKit.presence</string>
-		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.NeighborhoodActivityConduitService</string>

 	<true/>
 	<key>com.apple.security.ts.mach-task-name</key>
 	<true/>
+	<key>com.apple.security.ts.springboard-services</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.mediaremoted</string>
 	<key>com.apple.sharing.ProximityClient</key>

```
### accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

 		<string>/private/var/firmware/AOP/</string>
 		<string>/private/var/firmware/IPD/</string>
 		<string>/private/var/Managed Preferences/mobile/</string>
+		<string>/usr/standalone/firmware/accessoryupdater/UARP/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### MBPrebuddyFollowUpExtension

> `/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension`

```diff

 	<string>com.apple.backupd</string>
 	<key>backupd-connection-initiate</key>
 	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+	</array>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

```
### companionfindlocallyd

> `/System/Library/PrivateFrameworks/NanoLeash.framework/companionfindlocallyd`

```diff

 	</array>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
+	<key>com.apple.private.coremedia.interruptions.phonecallpriority.allow</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.findmylocaldevice</string>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerPID</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>om.apple.CoreODI</string>
+	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.photos.kvstore</string>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 		<string>Siri.AppSelection.Music</string>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>Siri.PostSiriEngagement</string>
+		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>Safari.PageLoad</string>
+		<string>Siri.Health.federated</string>
+		<string>AppleID.ChildSetup</string>
+		<string>SystemSettings.AppearanceSetup</string>
+		<string>SystemSettings.ChildMultitaskingSetup</string>
+		<string>SpringBoard.GestureEducation.PillLaunch</string>
+		<string>SystemSettings.GestureEducation.PillOutcome</string>
+		<string>SystemSettings.GestureEducation.Multitasking</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>com.apple.photos.geoanalytics.sent</string>
 		<string>com.apple.photos.geoanalytics</string>
+		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

 		<string>847</string>
 		<string>1541</string>
 		<string>1542</string>
+		<string>1545</string>
+		<string>1543</string>
+		<string>1544</string>
+		<string>841</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 		<string>Siri.AppSelection.Music</string>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>Siri.PostSiriEngagement</string>
+		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>Safari.PageLoad</string>
+		<string>Siri.Health.federated</string>
+		<string>AppleID.ChildSetup</string>
+		<string>SystemSettings.AppearanceSetup</string>
+		<string>SystemSettings.ChildMultitaskingSetup</string>
+		<string>SpringBoard.GestureEducation.PillLaunch</string>
+		<string>SystemSettings.GestureEducation.PillOutcome</string>
+		<string>SystemSettings.GestureEducation.Multitasking</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>com.apple.photos.geoanalytics.sent</string>
 		<string>com.apple.photos.geoanalytics</string>
+		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

 		<string>847</string>
 		<string>1541</string>
 		<string>1542</string>
+		<string>1545</string>
+		<string>1543</string>
+		<string>1544</string>
+		<string>841</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 		<string>Siri.AppSelection.Music</string>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>Siri.PostSiriEngagement</string>
+		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>Safari.PageLoad</string>
+		<string>Siri.Health.federated</string>
+		<string>AppleID.ChildSetup</string>
+		<string>SystemSettings.AppearanceSetup</string>
+		<string>SystemSettings.ChildMultitaskingSetup</string>
+		<string>SpringBoard.GestureEducation.PillLaunch</string>
+		<string>SystemSettings.GestureEducation.PillOutcome</string>
+		<string>SystemSettings.GestureEducation.Multitasking</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>com.apple.photos.geoanalytics.sent</string>
 		<string>com.apple.photos.geoanalytics</string>
+		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

 		<string>847</string>
 		<string>1541</string>
 		<string>1542</string>
+		<string>1545</string>
+		<string>1543</string>
+		<string>1544</string>
+		<string>841</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### ManagedAppsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>
 	<true/>
+	<key>com.apple.dmd.operation.remove-app</key>
+	<true/>
+	<key>com.apple.private.managedappdistribution.ddm</key>
+	<true/>
 	<key>com.apple.private.remotemanagement.subscriber</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	<string>com.apple.siriinferenced</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.Maps.tripsharing.sharing</key>
+	<true/>
+	<key>com.apple.MobileAsset.SoftwareUpdate</key>
+	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siriinferenced</string>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
+	<key>com.apple.internal.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>SiriIntelligencePlatform</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+				<string>Device.ScreenLocked</string>
+			</array>
+		</dict>
+	</dict>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.linkd.registry</key>
 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>UserFocus.ComputedMode</string>
+		<string>Location.Semantic</string>
 		<string>SiriIntentEvents</string>
 		<string>App.Install</string>
 		<string>Device.Wireless.WiFi</string>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.Maps</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/DuetExpertCenter/UICaches/</string>

 		<string>com.apple.linkd.suggestions</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.springboard.backgroundappservices</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.audio.AudioSession</string>
+		<string>com.apple.backlightd</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.Maps.xpc.SharedTrip</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.assistant</string>
 		<string>com.apple.siri.sirisuggestions</string>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
+		<string>com.apple.siriinferenced.AppOrdering</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.siri.uaf.service</string>

 		<string>1326</string>
 		<string>1327</string>
 		<string>1328</string>
+		<string>1340</string>
+		<string>1341</string>
+		<string>1342</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### MusicAppSelectionPFLPlugin

> `/System/Library/PrivateFrameworks/SiriSignals.framework/PlugIns/MusicAppSelectionPFLPlugin.appex/MusicAppSelectionPFLPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.siri.SiriSignals.MusicAppSelectionPFLPlugin</string>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>Siri.AppSelection.Music</string>
+	</array>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.proactive.eventtracker</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/DES/</string>
+		<string>mas/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>1329</string>
 	</array>
 </dict>
 </plist>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.homehubd.manage</string>
+		<string>com.apple.homed.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.coremedia</string>
 		<string>com.apple.triald</string>
 		<string>com.apple.siri.audio</string>
+		<string>com.apple.SpeakSelection</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.homed.xpc</string>
+		<string>com.apple.homehubd.manage</string>
+	</array>
 	<key>com.apple.security.ts.play-media</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### SiriHeadlessService

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService`

```diff

 	<true/>
 	<key>com.apple.siri.client_lite</key>
 	<true/>
+	<key>com.apple.soundboard.system</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1230</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.NeighborhoodActivityConduitService</key>
 	<true/>
+	<key>com.apple.RemoteDisplay</key>
+	<true/>
 	<key>com.apple.appletv.pbs.mediaremote</key>
 	<true/>
 	<key>com.apple.appletv.pbs.user-profiles</key>

 		<string>com.apple.accessibility.heard</string>
 		<string>com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc</string>
 		<string>com.apple.intelligentroutingd.xpc.media</string>
+		<string>com.apple.RemoteDisplay</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MauiAUSP

> `/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/PlugIns/MauiAUSP.appex/MauiAUSP`

```diff

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VoiceServices_CustomVoice/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_TTSAXResourceModelAssets/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VoiceServices_VoiceResources/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VoiceServices_CombinedVocalizerVoices/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### translationd

> `/System/Library/PrivateFrameworks/Translation.framework/translationd`

```diff

 	<true/>
 	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
 	<true/>
+	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
+	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```

### 🆕 TransparencyFollowUpExtension

> `/System/Library/PrivateFrameworks/TransparencyUI.framework/PlugIns/TransparencyFollowUpExtension.appex/TransparencyFollowUpExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.corefollowup.agent</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.corefollowup.agent</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.mode.assertion.user-requested.client-identifiers</key>

```
### watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.tv.sharedcontainer</string>
+		<string>group.tvappservices.container</string>
 	</array>
 	<key>com.apple.private.sportskit.session.client</key>
 	<true/>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.tv.sharedcontainer</string>
+		<string>group.tvappservices.container</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### ICQFollowup

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>re6Zb+zwFKJNlkQTUeT+/w</string>

```
### RemoteiCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>re6Zb+zwFKJNlkQTUeT+/w</string>

```
### itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.symptom_analytics.query</key>
+	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
 	<key>com.apple.telephony.cupolicy-rw-access</key>

```
### itunesstored

> `/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored`

```diff

 	<array>
 		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceMediaLibrary</string>
+		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>
+		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>

```

### 🆕 SiriGeoSuggestions

> `/System/Library/Siri/DM/SiriSuggestions/Owners/SiriGeoSuggestions.bundle/SiriGeoSuggestions`

- No entitlements *(yet)*
### kbd

> `/System/Library/TextInput/kbd`

```diff

 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.TextInput.TypingDESPlugin</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### Books

> `/private/var/staged_system_apps/Books.app/Books`

```diff

 		<string>/Library/Logs/MobileBackup/MobileBackup.log</string>
 		<string>/Library/Preferences/com.apple.Preferences.plist</string>
 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
+		<string>/Media/ManagedPurchases/Books/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 BooksProductPageExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksProductPageExtension.appex/BooksProductPageExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.iBooks.iBooksProductPageExtension</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
	<array>
		<string>iCloud.com.apple.iBooks</string>
		<string>iCloud.com.apple.iBooks.iTunesU</string>
	</array>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Development</string>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudDocuments</string>
		<string>CloudKit</string>
	</array>
	<key>com.apple.iBooks.BDSService.private</key>
	<true/>
	<key>com.apple.ibooks.BLService.private</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.iBooks</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Media/Books/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.backlightd</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.ibooks.BLService</string>
		<string>com.apple.iBooks.BookDataStoreService</string>
		<string>com.apple.xpc.amsaccountsd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AppleMediaServices</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.media.shared.books</string>
		<string>systemgroup.com.apple.media.books.managed</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>fairplay-client</key>
	<string>1328318286</string>
</dict>
</plist>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.passd.device-registration</string>
 		<string>com.apple.WorkoutKitXPCService</string>
 		<string>com.apple.coreidvd.digital-presentment.xpc</string>
 		<string>com.apple.ak.puffin.xpc</string>

 		<string>com.apple.NanoTimeKit.face</string>
 		<string>com.apple.tincan</string>
 		<string>com.apple.Mind</string>
+		<string>com.apple.nanolifestyle.sessiontrackerapp</string>
 		<string>com.apple.DeepBreathing</string>
 		<string>com.apple.Carousel</string>
 		<string>com.apple.SOS</string>

 		<string>com.apple.health.shared</string>
 		<string>com.apple.nanolifestyle</string>
 		<string>com.apple.iBooks</string>
+		<string>com.apple.accessibility.livespeech</string>
 	</array>
 	<key>com.apple.seld.tsmmanager</key>
 	<true/>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<true/>
 	<key>com.apple.developer.ubiquity-container-identifiers</key>
 	<true/>
+	<key>com.apple.developer.usersafety.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<true/>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>
 	<true/>
+	<key>com.apple.private.communicationsfilter</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>

 	<array>
 		<string>/Media/PhotoData/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
+		<string>/Library/com.apple.ManagedSettings/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
+		<string>com.apple.transparencyd</string>
 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.dprivacyd</string>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.ContactsBackgroundColorService</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<array>
 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.suggestions</string>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<array>
 		<string>access-call-providers</string>
 	</array>
+	<key>com.apple.transparency.kt</key>
+	<true/>
+	<key>com.apple.usersafety.service</key>
+	<string>contacts</string>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<true/>
 	<key>com.apple.developer.usernotifications.communication</key>
 	<true/>
+	<key>com.apple.developer.usersafety.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
 	<key>com.apple.facetimemessagestored.service</key>
 	<array>
 		<string>access-facetime-messaging</string>

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.persona.write</key>

 	<array>
 		<string>com.apple.tipsd</string>
 	</array>
+	<key>com.apple.rootless.storage.remotemanagementd</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.containermanagerd</string>
+		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.tipsd</string>

 		<string>access-call-capabilities</string>
 		<string>modify-call-capabilities</string>
 	</array>
+	<key>com.apple.usersafety.service</key>
+	<array>
+		<string>contacts</string>
+	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>
 	<key>com.apple.visualvoicemail.client</key>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
-	<key>com.apple.spaceattribution.private</key>
-	<true/>
+	<key>com.apple.security.ts.system-info</key>
+	<array>
+		<string>net.link.addr</string>
+	</array>
 	<key>com.apple.springboard.allowIconVisibilityChanges</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.Health.Medications</string>
+		<string>com.apple.health.[any-device-uuid]</string>
 	</array>
 	<key>com.apple.private.healthkit.sync</key>
 	<array>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>
 	<key>com.apple.voicetrigger.voicetriggerservice</key>

```
### HomeEnergyWidgetsExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
 	<key>com.apple.private.homeenergy</key>
 	<true/>
 	<key>com.apple.private.homekit.allow-secure-access</key>

```

### 🆕 Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.journal</string>
	<key>aps-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.journal.test</string>
		<string>com.apple.journal</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.journal.allow</key>
	<array>
		<string>suggestions</string>
	</array>
	<key>com.apple.developer.moments.allow</key>
	<array>
		<string>suggestions</string>
	</array>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.journal</string>
	<key>com.apple.moments.allowSuggestions</key>
	<true/>
	<key>com.apple.momentsd.internal</key>
	<array>
		<string>MOAppEntryEngagement</string>
		<string>MOUserNotifications</string>
		<string>MOOnboardingAndSettings</string>
	</array>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.journal</key>
		<string>com.apple.journal</string>
	</dict>
	<key>com.apple.private.cloudkit.systemService</key>
	<false/>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.momentsd.MOUserNotifications</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.Journal</string>
		<string>group.com.apple.moments</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.momentsd</string>
		<string>com.apple.MomentsUIService</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.momentsd</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
</dict>
</plist>

```

### 🆕 JournalShareExtension

> `/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.Journal</string>
		<string>group.com.apple.moments</string>
	</array>
</dict>
</plist>

```
### MobileStore

> `/private/var/staged_system_apps/MobileStore.app/MobileStore`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.MobileStore</string>
+		<string>com.apple.AppStoreComponents</string>
 	</array>
 	<key>com.apple.springboard.launchapplications</key>
 	<true/>

```

### 🆕 MusicFocusFilters

> `/private/var/staged_system_apps/Music.app/Extensions/MusicFocusFilters.appex/MusicFocusFilters`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.mediaplaybackcore</string>
	</array>
</dict>
</plist>

```
### MusicWidgets

> `/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets`

```diff

 		<key>value</key>
 		<string>com.apple.Music</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>
 	<true/>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.newsd</string>
+		<string>group.tvappservices.container</string>
 		<string>group.com.apple.news</string>
 		<string>group.com.apple.weather</string>
 		<string>group.com.apple.stocks-news</string>

 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.AdPlatforms</string>
 	</array>
+	<key>com.apple.sessionkit.broadcastPush</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### NewsTag

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag`

```diff

 	<string>ZL6BUSYGB3.com.apple.news.tag</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.chrono.invalidatesOnStorefrontChange</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### NewsToday2

> `/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2`

```diff

 	<string>ZL6BUSYGB3.com.apple.news.widget</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.chrono.invalidatesOnStorefrontChange</key>
+	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>com.apple.CoreODI</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache/Library/Caches/com.apple.IconsCache/</string>

 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.Wallet</string>
 		<string>com.apple.Wallet.public</string>
+		<string>com.apple.FinanceKit</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### SequoiaTranslator

> `/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator`

```diff

 	<string>com.apple.Translate</string>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.cards.all-access</key>

 	<true/>
 	<key>com.apple.developer.networking.multipath_extended</key>
 	<true/>
+	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
+	<true/>
+	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.DictionaryServices.dictionary2</string>

 	</array>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.sessionkit.custom-platter-target</key>
+	<true/>
+	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.private.suggestions.internal</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.sessionservices</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### StocksWidget

> `/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.chrono.invalidatesOnStorefrontChange</key>
+	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### Stocks

> `/private/var/staged_system_apps/Stocks.app/Stocks`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>821141022</string>
 	<key>application-identifier</key>
 	<string>ZL6BUSYGB3.com.apple.stocks</string>
 	<key>aps-environment</key>

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.developer.applesignin</key>
+	<array>
+		<string></string>
+	</array>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
 	<key>com.apple.developer.icloud-container-environment</key>

 	<true/>
 	<key>com.apple.mediaremote.set-playback-state</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.notificationcenter.widgetcontrollerhascontent</key>
 	<true/>
+	<key>com.apple.payment.card-on-file</key>
+	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	</array>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.bmk.allow</key>
+	<true/>
 	<key>com.apple.private.calendar.has-adopted-modern-request-access-methods</key>
 	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>

 	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceFaceID</string>
+	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.askpermissiond</string>
+		<string>com.apple.passd.payment</string>
+		<string>com.apple.passd.in-app-payment</string>
+		<string>com.apple.passd.library</string>
+		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>fairplay-client</key>
 	<string>1417937365</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 </dict>
 </plist>
 

```
### Tips

> `/private/var/staged_system_apps/Tips.app/Tips`

```diff

 		<string>UniqueDeviceID</string>
 		<string>RearFacingCameraSuperWideCameraCapability</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>

```
### WeatherIntents

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherIntents.appex/WeatherIntents`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.weather.internal</string>
+		<string>com.apple.weather.sensitive</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### WeatherPoster

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherPoster.appex/WeatherPoster`

```diff

 	<array>
 		<string>com.apple.weather</string>
 		<string>com.apple.weather.internal</string>
+		<string>com.apple.weather.sensitive</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### WeatherWidget

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget`

```diff

 	<true/>
 	<key>com.apple.locationd.prompt_from_background</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<array>
 		<string>com.apple.weather</string>
 		<string>com.apple.weather.internal</string>
+		<string>com.apple.weather.sensitive</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```
### Weather

> `/private/var/staged_system_apps/Weather.app/Weather`

```diff

 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
-	<true/>
+	<false/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.weather.internal</string>
+		<string>com.apple.weather.sensitive</string>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.newscore</string>
 		<string>com.apple.newscore2</string>

```
### launchd

> `/sbin/launchd`

```diff

 	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>
 	<true/>
+	<key>com.apple.private.kernel.darkboot</key>
+	<true/>
 	<key>com.apple.private.kernel.system-override</key>
 	<true/>
 	<key>com.apple.private.persona-mgmt</key>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.associated-domains</key>

```

### 🆕 ChassisAttestationd

> `/usr/libexec/ChassisAttestationd`

- No entitlements *(yet)*
### MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.afu.userclientaccess</key>
+	<true/>
 	<key>com.apple.private.apfs.allocate_contig</key>
 	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>

 	<true/>
 	<key>com.apple.rootless.install</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleFirmwareUpdateUserClient</string>
+	</array>
 </dict>
 </plist>
 

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 	<array>
 		<string>com.apple.ap.promotedcontent.supportinterface</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.amsengagementd</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.AdPlatforms</string>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.keystore.lockassertion</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### continuitycaptured

> `/usr/libexec/continuitycaptured`

```diff

 <dict>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.NeighborhoodActivityConduitService</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.RemoteDisplay</key>

 		<string>com.apple.dockaccessoryd</string>
 		<string>com.apple.dockaccessoryd.debug</string>
 		<string>com.apple.lsd.open</string>
+		<string>com.apple.NeighborhoodActivityConduitService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### coordinated

> `/usr/libexec/coordinated`

```diff

 	<string>coordinated</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.coordinated</string>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.private.coordination.messaging</key>

 	<array>
 		<string>com.apple.private.alloy.alarms-timers</string>
 	</array>
+	<key>com.apple.private.ids.remotecredentials</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.coordination.messaging</string>
 		<string>com.apple.coordination.role</string>
+		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.coordinated</string>
+		<string>com.apple.facetime.bag</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<true/>
 	<key>com.apple.MobileInternetSharing.allow</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.bulletinboard.dataprovider</key>
 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
+	<array>
+		<string>photos.suggestion</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppIntent</string>

 	<array>
 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceExposureNotification</string>
+		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.MobileInternetSharing</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.photos.service</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.purplebuddy.budd.cloud.xpc</string>
 		<string>com.apple.PowerManagement.control</string>

 		<string>com.apple.gridDataServices</string>
 		<string>com.apple.nanobuddy</string>
 		<string>com.apple.purplebuddy</string>
+		<string>com.apple.cloudphotod</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### dockaccessoryd

> `/usr/libexec/dockaccessoryd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-device</key>
+	<true/>
+	<key>com.apple.hid.manager.user-access-protected</key>
+	<true/>
 	<key>com.apple.idle-timer-services</key>
 	<true/>
 	<key>com.apple.private.accessories.showallconnections</key>
 	<true/>
+	<key>com.apple.private.allow-background-haptics</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothAlways</string>

 	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
-	<key>com.apple.security.iokit-user-client-class</key>
-	<array>
-		<string>IOHIDEventServiceFastPathUserClient</string>
-	</array>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 		<string>com.apple.healthd.server</string>
 		<string>com.apple.sessionservices</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.purplebuddy.notbackedup</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.SpotlightFoundation</string>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.nfcd.session.se</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileActivation</key>
 	<array>
 		<string>RequestActivationState</string>

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAccessibility</string>
+		<string>kTCCServiceFaceID</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.nanoprefsync</string>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 	<array>
 		<string>com.apple.findmy</string>
 	</array>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/usr/libexec/findmylocated</string>

```
### gamed

> `/usr/libexec/gamed`

```diff

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.GameOverlayUI</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### intelligentroutingd

> `/usr/libexec/intelligentroutingd`

```diff

 <dict>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.airplay.endpoint.xpc</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>

 	<true/>
 	<key>com.apple.locationd.pedestrianfencemanager</key>
 	<true/>
+	<key>com.apple.mediaexperience.endpoint.xpc</key>
+	<true/>
 	<key>com.apple.nearbyinteraction.background</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<array>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction.observer</string>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
+		<string>com.apple.lsd.mapdb</string>
 	</array>
 </dict>
 </plist>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.momentsd.internal</key>
+	<array>
+		<string>MOOnboardingAndSettings</string>
+	</array>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry</key>

 		<string>com.apple.CarPlayApp.user-alerts-service</string>
 		<string>com.apple.rapport.people</string>
 		<string>com.apple.locationpushd.pushregistration</string>
+		<string>com.apple.momentsd</string>
 		<string>com.apple.nearbyd.xpc.diagnostics</string>
 		<string>com.apple.accessoryupdater.uarp</string>
 		<string>com.apple.cloudd</string>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 		<string>com.apple.ve.cvcalibrationd.xpc</string>
 		<string>com.apple.UXMAssertionService</string>
 		<string>com.apple.litehudd.xpc</string>
+		<string>com.apple.carousel.connectionstatusservice</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### mediasetupd

> `/usr/libexec/mediasetupd`

```diff

 	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

```
### mlhostd

> `/usr/libexec/mlhostd`

```diff

 	<string>com.apple.mlhostd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.mlhostd</string>
 	<key>com.apple.mlhost.worker-host-entitlement</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.biome.pruner</key>
 	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 		<string>Lighthouse.Ledger.TaskStatus</string>
 		<string>Lighthouse.Ledger.TaskError</string>
 		<string>Lighthouse.Ledger.TaskTelemetry</string>

 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 		<string>Lighthouse.Ledger.TaskStatus</string>
 		<string>Lighthouse.Ledger.TaskError</string>
 		<string>Lighthouse.Ledger.TaskTelemetry</string>

 				<string>Lighthouse.Ledger.TaskError</string>
 				<string>Lighthouse.Ledger.TaskTelemetry</string>
 				<string>Lighthouse.Ledger.DeviceTelemetry</string>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>
 		</dict>
 	</dict>

 	<array>
 		<string>/usr/libexec/mlhostd</string>
 		<string>/System/Library/MLHost/</string>
-		<string>/AppleInternal/System/Library/</string>
+		<string>/AppleInternal/Library/MLHost/</string>
+		<string>/AppleInternal/System/Library/MLHost/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
+	<key>com.apple.locationd.time_zone</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.momentsd.internal</key>
 	<array>
+		<string>MODataExportService</string>
 		<string>MOFetchEventBundles</string>
 	</array>
 	<key>com.apple.photoanalysisd</key>

 	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
+	<key>com.apple.private.healthkit.authorization_bypass</key>
+	<true/>
 	<key>com.apple.private.healthkit.metadata.private</key>
 	<true/>
 	<key>com.apple.private.healthkit.read_authorization_bypass</key>
 	<array>
 		<string>HKWorkoutRouteTypeIdentifier</string>
 		<string>HKWorkoutTypeIdentifier</string>
-		<string>HKQuantityTypeIdentifierWalkingSpeed</string>
 		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
 		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
 		<string>HKCategoryTypeIdentifierMindfulSession</string>

 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
+	<key>com.apple.private.photos.storytelling.inferenceSummary</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.MomentsDataExportService</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.contactsd</string>

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.locationd.adpd</string>
 		<string>com.apple.locationd.registration</string>
+		<string>com.apple.locationd.synchronous</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.sociallayerd</string>

```
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 	<true/>
 	<key>com.apple.runningboard.targetidentities</key>
 	<true/>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>RootDomainUserClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.nano.nanoregistry.paireddeviceregistry</string>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.AdLib</string>
 		<string>com.apple.springboard</string>
 		<string>com.apple.ap.promotedcontentd</string>
 		<string>com.apple.security</string>
 		<string>com.apple.CFNetwork</string>
 		<string>com.apple.itunesstored</string>
+		<string>com.apple.amsengagementd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### remindd

> `/usr/libexec/remindd`

```diff

 	<array>
 		<string>Library/Caches/com.apple.itunesstored/url-resolution.plist</string>
 		<string>Library/Caches/com.apple.AppleAccount/</string>
+		<string>Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.triald.namespace-management</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.kvsd</string>
 	</array>

 		<string>com.apple.persistentconnection</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.DataAccess.BehaviorOptions</string>
+		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### routined

> `/usr/libexec/routined`

```diff

 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>AppLaunch</string>
+		<string>AppIntent</string>
+	</array>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>
 	<key>com.apple.private.calendar.watchos-mutable-database</key>

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.safetyalerts.spi</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<string>/private/var/db/com.apple.countryd/</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.dmd.emergency-mode</string>
 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.timed.xpc</string>
+		<string>com.apple.safetyalerts</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 		<string>apple-safety-alert</string>
 		<string>spi</string>
 	</array>
+	<key>com.apple.CoreRoutine.PeopleDiscovery</key>
+	<true/>
 	<key>com.apple.CoreRoutine.StoredLocation</key>
 	<true/>
 	<key>com.apple.aps.incoming-message-interface</key>
 	<true/>
 	<key>com.apple.apsd.ios-device-push-token</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.driver.AppleConvergedIPCBB.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleConvergedIPCBBControl.user-access</key>

 	<true/>
 	<key>com.apple.driver.AppleConvergedIPCICEBBControl.user-access</key>
 	<true/>
+	<key>com.apple.locationd.activity</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.spectator</key>

 		<string>Device.Wireless.WiFi</string>
 		<string>Device.Wireless.WiFiAvailabilityStatus</string>
 		<string>Device.Wireless.WakeOnWiFiStatus</string>
-		<string>Device.Wireless.CellularAvailabilityStatus</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
 	</array>
 	<key>com.apple.private.followup</key>

```
### security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

```diff

 		<string>com.apple.hap.metadata</string>
 		<string>com.apple.continuity.unlock</string>
 		<string>com.apple.rapport</string>
+		<string>group.com.apple.notes</string>
 	</array>
 	<key>keychain-cloud-circle</key>
 	<true/>

```
### sportsd

> `/usr/libexec/sportsd`

```diff

 	</array>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>
 	<true/>
+	<key>com.apple.private.sessionkit.customPushProcessIdentifier</key>
+	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```

### 🆕 srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.srp-mdns-proxy</string>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.keystore.access-keychain-keys</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.mDNSResponder_Helper</key>
	<true/>
	<key>com.apple.networkd_privileged</key>
	<true/>
	<key>com.apple.pf.allow</key>
	<true/>
	<key>com.apple.private.fillmore.prefix.modification</key>
	<true/>
	<key>com.apple.private.fillmore.service.add</key>
	<true/>
	<key>com.apple.private.fillmore.service.remove</key>
	<true/>
	<key>com.apple.private.nehelper.privileged</key>
	<true/>
	<key>com.apple.private.network.reserved-port</key>
	<true/>
	<key>com.apple.private.wpantund.service.xpc</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/usr/libexec</string>
		<string>/dev/fd</string>
		<string>/private/var/Managed Preferences/mobile/com.apple.srp-mdns-proxy.plist</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/</string>
		<string>/private/var/preferences/SystemConfiguration/preferences.plist</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.wpantund.xpc</string>
		<string>com.apple.network.IPConfiguration</string>
		<string>com.apple.pfd</string>
		<string>com.apple.mDNSResponder_Helper</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.srp-mdns-proxy.preferences</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-write</key>
	<array>
		<string>net.inet6.ip6.forwarding</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.srp-mdns-proxy</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>temporary-sandbox</string>
	</array>
</dict>
</plist>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.ids.key-transparency.cache-clear-request</key>
+	<true/>
 	<key>com.apple.private.ids.key-transparency.optin-check</key>
 	<true/>
-	<key>com.apple.private.ids.messaging</key>
-	<array>
-		<string>com.apple.private.alloy.keytransparency.accountkey.pinning</string>
-	</array>
-	<key>com.apple.private.ids.messaging.urgent-priority</key>
+	<key>com.apple.private.ids.registration</key>
 	<array>
-		<string>com.apple.private.alloy.keytransparency.accountkey.pinning</string>
+		<string>com.apple.madrid</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>
-	<key>com.apple.private.ids.session</key>
-	<array>
-		<string>com.apple.private.alloy.keytransparency.accountkey.pinning</string>
-	</array>
-	<key>com.apple.private.ids.session-private</key>
-	<array>
-		<string>com.apple.private.alloy.keytransparency.accountkey.pinning</string>
-	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>
 	<true/>
 	<key>com.apple.private.octagon</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>transparencyd</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.transparency</string>
+	</array>
 	<key>com.apple.private.security.storage.SFAnalytics</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceContacts</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.transparency</string>
+	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### tzinit

> `/usr/libexec/tzinit`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.vfs.allow-low-space-writes</key>
+	<true/>
+</dict>
+</plist>
 

```
### WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.geoanalyticsd.telemetry</key>
+	<true/>
 	<key>com.apple.geoservices.restricted-tiles</key>
 	<array>
 		<string>smartdata</string>

 		<string>com.apple.wpantund.xpc</string>
 		<string>com.apple.geoanalyticsd</string>
 		<string>com.apple.wifip2pd</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.private.network-performance-tester</key>
 	<true/>
+	<key>com.apple.private.networkextension.configuration</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.ppm.client</key>

 	<array>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
 	<key>com.apple.private.ubiquity-kvstore-access</key>
 	<array>
 		<string>com.apple.wifid</string>

```
