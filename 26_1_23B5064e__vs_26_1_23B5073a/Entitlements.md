## 🔑 Entitlements

### AirDropUI

> `/Applications/AirDropUI.app/AirDropUI`

```diff

 	<true/>
 	<key>com.apple.private.messages.collaboration-initiate-send</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

 		<string>com.apple.posterboardservices.data-store</string>
 		<string>com.apple.posterboardservices.services</string>
 		<string>com.apple.ProximityControl.ProximityHandoffInteractions</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Media

> `/Applications/Media.app/Media`

```diff

 	<true/>
 	<key>com.apple.private.carp.wake</key>
 	<true/>
-	<key>com.apple.private.externalaccessory.showallaccessories</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.caraccessoryframework.cardata</string>

```
### PhotosUIService

> `/Applications/PhotosUIService.app/PhotosUIService`

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
 		<string>com.apple.restrictionspassword</string>
 		<string>com.apple.springboard</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### ReplayKitAngel

> `/Applications/ReplayKitAngel.app/ReplayKitAngel`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.private.corespeech.audioinjection.xpc</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.siri.sirireaderd</string>
 		<string>com.apple.private.assistant.settings</string>
 		<string>com.apple.sirittsd</string>

```

### 🆕 MobileDevices-0002

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`

- No entitlements *(yet)*
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>

```
### PhotoPicker

> `/System/Library/ExtensionKit/Extensions/PhotoPicker.appex/PhotoPicker`

```diff

 		<string>com.apple.restrictionspassword</string>
 		<string>com.apple.springboard</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
+	</array>
 	<key>com.apple.sensitivecontentanalysis.service</key>
 	<array>
 		<string>photos</string>

```
### PhotosMessagesApp

> `/System/Library/ExtensionKit/Extensions/PhotosMessagesApp.appex/PhotosMessagesApp`

```diff

 	<true/>
 	<key>com.apple.private.privacy.accounting.write</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/PhotosPicker`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.photos.picker</string>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
+	<key>com.apple.private.nsurlsession.set-discretionary-override-value</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.allowcollectionshare</key>

 	<true/>
 	<key>com.apple.private.privacy.accounting.write</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.private.security.storage.Notes</key>

 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.itunescloud.internal</string>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.siri.koa.donate.internal</key>
 	<true/>

```

### 🆕 CallHapticsSettingsBundle

> `/System/Library/PreferenceBundles/CallHapticsSettingsBundle.bundle/CallHapticsSettingsBundle`

- No entitlements *(yet)*
### AudioAccessoryAssetManagementXPCService

> `/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/XPCServices/AudioAccessoryAssetManagementXPCService.xpc/AudioAccessoryAssetManagementXPCService`

```diff

 	<true/>
 	<key>com.apple.das.private.bgtask.continuedprocessing.iconBundleIdentifier</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.translation</key>

```
### mobiletimerd

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/Applications/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>NSBonjourServices</key>
+	<array>
+		<string>_wallet._tcp</string>
+	</array>
 	<key>adi-client</key>
 	<integer>4201635476</integer>
 	<key>application-identifier</key>

 		<string>CloudKit</string>
 		<string>CloudDocuments</string>
 	</array>
+	<key>com.apple.developer.networking.multicast</key>
+	<true/>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.network.server</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>

```
### Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```diff

 		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.anvil</string>
+		<string>com.apple.EmojiPreferences</string>
 	</array>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>

```
### PassbookLockedWidgetsExtension

> `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/PassKit/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.iconservices</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.passd.payment</string>

```
### PhotosNotificationsUpdates

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.notification</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<array>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### com.apple.social.StreamShareService

> `/private/var/staged_system_apps/Photos.app/PlugIns/com.apple.social.StreamShareService.appex/com.apple.social.StreamShareService`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.appleaccount.custodian</string>
 	<key>com.apple.frontboard.debugapplications</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.usymptomsd</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.kvsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### avconferenced

> `/usr/libexec/avconferenced`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.sensitivecontentanalysis.client</key>
 	<array>
 		<string>analysis</string>

 		<string>com.apple.privacyaccountingd</string>
 		<string>com.apple.realitysimulation.renderedcontentservice</string>
 		<string>com.apple.royad</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.systemstatus.activityattribution</string>
 		<string>com.apple.timesync.expositor</string>
 		<string>com.apple.timesync.manager</string>

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.avfoundation</string>
 		<string>com.apple.conference</string>
+		<string>com.apple.communicationSafetySettings</string>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.coreanimation</string>
 		<string>com.apple.coremedia</string>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.UIKit</string>
 		<string>com.apple.gms.availability</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.InFocus</string>
+		<string>App.Intent</string>
 		<string>AppLaunch</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Discoverability.Signals</string>

```
