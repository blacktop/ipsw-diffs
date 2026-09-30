## 🔑 Entitlements

### AXUIViewService

> `/Applications/AXUIViewService.app/AXUIViewService`

```diff

 		<string>com.apple.VoiceOverTouch</string>
 		<string>com.apple.VoiceOverTouch.activities</string>
 		<string>com.apple.ZoomTouch</string>
+		<string>com.apple.keyboard.ContinuousPath</string>
 	</array>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>

```
### ActivityMessagesExtension

> `/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.activitysharingd</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.messages.private.AllowParticipantAddressAccess</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```

### 🆕 AdaptiveMusicApp

> `/Applications/AdaptiveMusicApp.app/AdaptiveMusicApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>628765583</string>
	<key>application-identifier</key>
	<string>com.apple.AdaptiveMusicApp</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.mediaremote.request-bless</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.AdaptiveMusicApp</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Logs/MediaServices/</string>
		<string>/var/mobile/Library/Application Support/com.apple.iTunesCloud/URLBags</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/com.apple.iTunesCloud/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.itunescloud.remote-request-execution-service</string>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
	</array>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```

### 🆕 AdaptiveMusicControl

> `/Applications/AdaptiveMusicApp.app/PlugIns/AdaptiveMusicControl.appex/AdaptiveMusicControl`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>628765583</string>
	<key>application-identifier</key>
	<string>com.apple.AdaptiveMusicApp.AdaptiveMusicControl</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.AdaptiveMusicApp</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Logs/MediaServices/</string>
		<string>/var/mobile/Library/Application Support/com.apple.iTunesCloud/URLBags</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/com.apple.iTunesCloud/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.itunescloud.remote-request-execution-service</string>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
	</array>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```
### AirPlayReceiver

> `/Applications/AirPlayReceiver.app/AirPlayReceiver`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>com.apple.CompanionLink</key>
 	<true/>
 	<key>com.apple.PairingManager.HomeKit</key>

 	<array>
 		<string>com.apple.private.wifi.driverkit</string>
 	</array>
+	<key>com.apple.private.mediaexperience.systemcontroller.allowappstoinitiateplayback</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.rapport.Client</key>

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.devicesharingd</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### AnimojiStickersExtension

> `/Applications/AnimojiStickers.app/PlugIns/AnimojiStickersExtension.appex/AnimojiStickersExtension`

```diff

 <dict>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.messages.private.BypassShelfAccess</key>

```
### AppleIDSetupUIService

> `/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>abs-client</key>
+	<string>1563636331</string>
+	<key>adi-client</key>
+	<string>4127693656</string>
 	<key>application-identifier</key>
 	<string>com.apple.AppleIDSetupUIService</string>
 	<key>com.apple.PairingManager.Read</key>

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.appleidsetup.repair.client</key>

 	<true/>
 	<key>com.apple.frontboard.systemappservices</key>
 	<true/>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>

 	<array>
 		<string>UniqueDeviceID</string>
 		<string>ProvisioningUniqueDeviceID</string>
+		<string>SerialNumber</string>
 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.adid</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.screentime-setup</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.icloud.findmydeviced</string>
+		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.appleidsetupd.repair.xpc</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.PairingManager</string>

 		<string>com.apple.uikit.viewservice.com.apple.AppleIDSetupUIService</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.hsa-authentication-server</string>
+		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.devicecheckd</string>
+		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.adid</string>
+		<string>com.apple.absd</string>
+		<string>com.apple.absinthed</string>
+		<string>com.apple.ak.anisette.xpc</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.AuthKit.AgeRangeSettingsCache</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### AskToMessagesExtension

> `/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension`

```diff

 <dict>
 	<key>com.apple.asktod</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.messages.private.AllowAlertPresentation</key>

```
### Business

> `/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.media-client-id</key>
+	<string>com.apple.CarPlaySetup</string>
+	<key>com.apple.private.appstorecomponents.media-client-version</key>
+	<string>1</string>
 	<key>com.apple.private.carkit.setupPromptDirector</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 		<string>com.apple.carkit.setupPromptDirector.service</string>
 		<string>com.apple.passd.payment</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.AppStoreComponents</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### CoreAuthUI

> `/Applications/CoreAuthUI.app/CoreAuthUI`

```diff

 	<true/>
 	<key>com.apple.private.biometrickit.allow-connect</key>
 	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>

```
### ShareableCredentialsMessagesExtension

> `/Applications/CredentialSharingUIViewService.app/PlugIns/ShareableCredentialsMessagesExtension.appex/ShareableCredentialsMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>
 	<true/>
 	<key>com.apple.internal.seserviced.ptattestation</key>

```
### Diagnostic-8343

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.corerepair</string>
+		<string>com.apple.diskimagecorerepair</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Diagnostic-8357

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8357.appex/Diagnostic-8357`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.DiagnosticsService.Diagnostic-8357</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DiagnosticsPanicEventCollection</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Diagnostics.Panic</key>
+				<true/>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Logs/AppleSupport/</string>
 		<string>/private/var/logs/AppleSupport/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.Diagnostics</string>

```
### Family

> `/Applications/Family.app/Family`

```diff

 	</array>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>

```
### InviteMessageBubbleExtension

> `/Applications/Family.app/PlugIns/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```

### 🆕 BankConnectRefreshReminderNotificationExtension

> `/Applications/FinanceUIService.app/PlugIns/BankConnectRefreshReminderNotificationExtension.appex/BankConnectRefreshReminderNotificationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.finance.private</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.financed.service.coredatastore</string>
		<string>com.apple.financed.service.store</string>
		<string>com.apple.financed.service.financestore</string>
		<string>com.apple.financed.service.bankconnect</string>
	</array>
</dict>
</plist>

```
### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
+	<key>com.apple.appstored.install-apps</key>
+	<true/>
+	<key>com.apple.appstored.install-system-apps</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.accessorydiscoverysession</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>Install</string>
+	</array>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
+	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.accessorydiscoverysession</string>
+		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.appstored.xpc.request</string>
+	</array>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
 	<key>com.apple.springboard.launchapplications</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### FunCameraEmojiStickersExtension

> `/Applications/FunCameraEmojiStickers.app/PlugIns/FunCameraEmojiStickersExtension.appex/FunCameraEmojiStickersExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+</dict>
+</plist>
 

```
### FunCameraShapesExtension

> `/Applications/FunCameraShapes.app/PlugIns/FunCameraShapesExtension.appex/FunCameraShapesExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+</dict>
+</plist>
 

```
### FunCameraTextExtension

> `/Applications/FunCameraText.app/PlugIns/FunCameraTextExtension.appex/FunCameraTextExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+</dict>
+</plist>
 

```
### GameOverlayUI

> `/Applications/GameOverlayUI.app/GameOverlayUI`

```diff

 		<string>Multiplayer</string>
 		<string>TurnBasedMultiplayer</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.gamecenter</string>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
+	<key>com.apple.private.canModifyAppLinkPermissions</key>
+	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.game-center</key>
 	<array>
 		<string>Account</string>

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.iphone.axserver-systemwide</string>
 		<string>com.apple.controlcenter.remoteservice</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 	<array>
 		<string>Removal</string>
 	</array>
+	<key>com.apple.managedconfiguration.profiled.set</key>
+	<array>
+		<string>Passcode</string>
+	</array>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.networkrelay.deviceMonitor</key>

```
### HashtagImages

> `/Applications/HashtagImages.app/HashtagImages`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.messages.private.AllowAlertPresentation</key>
 	<true/>
 	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>

```
### HashtagImagesExtension

> `/Applications/HashtagImages.app/PlugIns/HashtagImagesExtension.appex/HashtagImagesExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.messages.private.AllowAlertPresentation</key>
 	<true/>
 	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 <dict>
 	<key>CanInheritApplicationStateFromOtherProcesses</key>
 	<true/>
+	<key>adi-client</key>
+	<string>3303100823</string>
 	<key>application-identifier</key>
 	<string>com.apple.HeadphoneProxService</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.AudioAccessoryServices</key>
 	<true/>
 	<key>com.apple.BluetoothServices</key>

 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
+	<key>com.apple.payment.card-on-file</key>
+	<true/>
 	<key>com.apple.powerui.smartcharging</key>
 	<true/>
 	<key>com.apple.powerui.smartcharging.AudioAccessory</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceIDData</string>

 	<array>
 		<string>Install</string>
 	</array>
+	<key>com.apple.private.aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>

 		<key>value</key>
 		<string>/Applications/HeadphoneProxService.app</string>
 	</dict>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.productkit.personalization</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.fpsd.client</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>InstallForLaunchServices</string>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMicrophone</string>

 	<array>
 		<string>/private/preboot/</string>
 		<string>/private/var/hardware/FactoryData/System/Library/Caches/com.apple.factorydata/</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
 		<string>/private/var/preferences/FeatureFlags/Settings.plist</string>
 		<string>/System/Library/Caches/com.apple.factorydata/</string>
 	</array>

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+		<string>/Library/UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.passd.payment</string>
 		<string>com.apple.HearingModeService</string>
 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.accessories.connection-info-server</string>

 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.purplebuddy.budd.proximity.source.xpc</string>
 		<string>com.apple.purplebuddy.budd.migration.source.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.sharingd.b332setup</string>

 	<array>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.siri.textinput</string>
+		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<key>com.apple.wirelessproxd-disable-scans</key>
 	<true/>
 	<key>fairplay-client</key>
-	<integer>1445028844</integer>
+	<string>1445028844</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### Animoji

> `/Applications/Jellyfish.app/PlugIns/Animoji.appex/Animoji`

```diff

 <dict>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.idle-timer-services</key>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 	<true/>
 	<key>com.apple.private.avfoundation.capture.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-filter</key>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### MusicUIService

> `/Applications/MusicUIService.app/MusicUIService`

```diff

 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
+	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.springboard.stark.activateBackgroundProvider</key>

```
### NewDeviceSetupUIService

> `/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.NewDeviceSetupUIService</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.bluetooth.discovery</key>
 	<dict>
-		<key>NewDeviceSetupUIService</key>
+		<key>MacSetup</key>
 		<dict>
-			<key>discoveryFlags</key>
+			<key>discoveryTypes</key>
+			<array>
+				<string>MacSetup</string>
+			</array>
+			<key>limitToDeviceClasses</key>
 			<array>
-				<string>macOSSetup</string>
+				<string>iPad</string>
+				<string>iPhone</string>
 			</array>
-			<key>viewControllerClassName</key>
-			<string>FirstAlertViewController</string>
+			<key>sceneIdentifier</key>
+			<string>NewDeviceSetupUIService.NDSUSSceneDelegate</string>
 		</dict>
 	</dict>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.locationd.archived_authorization_decisions</key>
+	<true/>
+	<key>com.apple.locationd.authorizeapplications</key>
+	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
+	<key>com.apple.locationd.status</key>
+	<true/>
+	<key>com.apple.locationd.usage_oracle</key>
+	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.CallerName</key>
+	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
+	<key>com.apple.private.corewifi.internal</key>
+	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceFaceID</string>
+		<string>kTCCServiceCamera</string>
+		<string>kTCCServiceBluetoothAlways</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.ak.anisette.xpc</string>
+		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.hsa-authentication-server</string>
+		<string>com.apple.appleidsetupd.setup.xpc</string>
+		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.PairingManager</string>
+		<string>com.apple.distributed_notifications@Uv3</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
+	</array>
+	<key>com.apple.sharing.Client</key>
+	<true/>
+	<key>com.apple.sharing.Session</key>
+	<true/>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
+	<key>com.apple.springboard.activateRemoteAlert</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert	</key>
+	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>
 	<true/>
 	<key>com.apple.sptingboard.activateRemoteAlert</key>
 	<true/>
+	<key>com.apple.wifi.manager-access</key>
+	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>appleaccount</string>
+		<string>com.apple.certificates</string>
+	</array>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 OTEAutomation

> `/Applications/OTEAutomationTest.app/Frameworks/OTEAutomation.framework/OTEAutomation`

- No entitlements *(yet)*

### 🆕 OTEAutomationTest

> `/Applications/OTEAutomationTest.app/OTEAutomationTest`

- No entitlements *(yet)*
### PCViewService

> `/Applications/PCViewService.app/PCViewService`

```diff

 	<true/>
 	<key>com.apple.proximitycontrol.remoteActivity</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Bundle/Application/</string>

 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.locationd.registration</string>
+		<string>com.apple.mediacontrol.xpc</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.MobileTimer.timerserver</string>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.QuartzCore.system-layers</key>
+	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
 	<key>com.apple.apple-pay-trust.all-access</key>

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
+	<key>com.apple.private.biometrickit.allow-connect</key>
+	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>com.apple.seld.tsmmanager</key>
 	<true/>
 	<key>com.apple.seserviced.key</key>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.QuartzCore.system-layers</key>
+	<true/>
 	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>
 	<array>
 		<string>com.apple.radios.plist</string>

 	<array>
 		<string>Wallet.Transaction</string>
 	</array>
+	<key>com.apple.private.biometrickit.allow-connect</key>
+	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.carkit.headUnitPairingPrompt</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

 		<string>com.apple.Wallet</string>
 		<string>com.apple.Wallet.public</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>com.apple.seld.tsmmanager</key>
 	<true/>
 	<key>com.apple.seserviced.key</key>

 	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.background-event-consumption</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>

```
### PeerPaymentMessagesExtension

> `/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>

```
### PeopleMessagesAskToBuy

> `/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### PeopleMessagesScreenTime

> `/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.DeviceAccess.private</key>
 	<true/>
+	<key>com.apple.Diagnostics.host-view-service</key>
+	<true/>
 	<key>com.apple.DiagnosticsSessionAvailability.client</key>
 	<true/>
 	<key>com.apple.FamilyControls.private-client</key>

 	<true/>
 	<key>com.apple.accessoryupdater.launchauhelper.entitled</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.assistant.domain.system.settings.access</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.attributionkitd.developer-mode</key>

 	<array>
 		<string>com.apple.TextInput</string>
 		<string>com.apple.notes</string>
+		<string>com.apple.productkit.b389personalization</string>
+		<string>com.apple.productkit.personalization</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>

 	<true/>
 	<key>com.apple.hid.manager.user-access-keyboard</key>
 	<true/>
+	<key>com.apple.hidrm</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>

 	<true/>
 	<key>com.apple.locationd.defaults_access</key>
 	<true/>
+	<key>com.apple.locationd.eed_precached_adr</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.status</key>

 	<true/>
 	<key>com.apple.powerui.smartcharging.AudioAccessory</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.CarveoutProperty</key>
+	<true/>
 	<key>com.apple.private.CarPlayServices.icon-layout</key>
 	<true/>
 	<key>com.apple.private.ClassKit.dashboard</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>

 	<true/>
 	<key>com.apple.private.cloudkit.protectiondata</key>
 	<true/>
+	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
+	<dict>
+		<key>com.apple.productkit.personalization</key>
+		<string>com.apple.productkit.personalization</string>
+	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 	<true/>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
+	<key>com.apple.private.locationaccessstore.administer</key>
+	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>com.apple.mobile.lockdown.paired_host_info/NULL</string>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/mobile/Library/Application Support/locationaccessstored/</string>
 		<string>/private/var/mobile/Library/DuetExpertCenter/ModeCaches/</string>
 		<string>/private/var/mobile/Library/DuetExpertCenter/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.locationaccessstored.registration</string>
 		<string>com.apple.softposreaderd</string>
 		<string>com.apple.identityservicesd.nsxpc</string>
 		<string>com.apple.appprotectiond.guard</string>

 		<string>com.apple.usernotificationskit</string>
 		<string>com.apple.messages.critical-messaging.storage</string>
 		<string>com.apple.seserviced.contactlessCredential.settings</string>
+		<string>com.apple.visionproapp.notifications</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 		<string>RootDomainUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
 	</array>
 	<key>com.apple.security.lockdownmode.read</key>
 	<true/>

 	<true/>
 	<key>com.apple.usermanagerd.persona.setbundle</key>
 	<true/>
+	<key>com.apple.visioncompaniond.client</key>
+	<true/>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
 	<key>com.apple.voicebanking.services</key>

 		<string>com.apple.openai</string>
 		<string>com.apple.preferences</string>
 		<string>com.apple.safari.credit-cards</string>
+		<string>com.apple.snowflake</string>
 		<string>com.apple.PassbookUIService</string>
 		<string>com.apple.ProtectedCloudStorage</string>
 		<string>com.apple.PublicCloudStorage</string>

 		<string>com.apple.mail.identities</string>
 		<string>com.apple.AppleCareSupport-Preferences</string>
 		<string>com.apple.cfnetwork</string>
+		<string>com.apple.cfnetwork.testing</string>
 		<string>com.apple.password-manager</string>
+		<string>com.apple.password-manager.testing</string>
 		<string>com.apple.webkit.webauthn</string>
+		<string>com.apple.webkit.webauthn.testing</string>
 		<string>com.apple.cfnetwork-recently-deleted</string>
+		<string>com.apple.cfnetwork-recently-deleted.testing</string>
 		<string>com.apple.password-manager-recently-deleted</string>
+		<string>com.apple.password-manager-recently-deleted.testing</string>
 		<string>com.apple.webkit.webauthn-recently-deleted</string>
+		<string>com.apple.webkit.webauthn-recently-deleted.testing</string>
 		<string>com.apple.password-manager.personal</string>
+		<string>com.apple.password-manager.personal.testing</string>
 		<string>com.apple.password-manager.personal-recently-deleted</string>
+		<string>com.apple.password-manager.personal-recently-deleted.testing</string>
 		<string>com.apple.password-manager.generated-passwords</string>
+		<string>com.apple.password-manager.generated-passwords.testing</string>
 	</array>
 	<key>keychain-cloud-circle</key>
 	<true/>

```
### RemotePaymentPassActionsMessagesExtension

> `/Applications/RemotePaymentPassActionsService.app/PlugIns/RemotePaymentPassActionsMessagesExtension.appex/RemotePaymentPassActionsMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.messages.private.AllowParticipantAddressAccess</key>
 	<true/>
 	<key>com.apple.messages.private.BypassShelfAccess</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.itunesstored.accounts</key>
 	<true/>
 	<key>com.apple.itunesstored.downloads</key>

 		<string>App.WebUsage</string>
 		<string>Discoverability.Signals</string>
 		<string>Discoverability.Usage</string>
+		<string>Safari.Browsing.Assistant</string>
 	</array>
 	<key>com.apple.private.can-load-any-content-blocker</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-dispatch.internal</key>
+	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.in-app-payments</key>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/db/os_eligibility/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>

 		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.email.maild</string>
 		<string>com.apple.webprivacyd</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ak.privateemail.xpc</string>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.datadetectors</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.newscore</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 	</array>

 		<string>com.apple.WebUI</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.ScreenContinuityShell</string>
 		<string>com.apple.RemoteDisplay</string>
 		<string>com.apple.systemstatus</string>
 		<string>com.apple.coremedia.cameraviewfinder</string>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.managedconfiguration.profiled</string>
-		<string>com.apple.screencontinuity.dragserver</string>
-	</array>
-	<key>com.apple.security.exception.mach-register.global-name</key>
-	<array>
-		<string>com.apple.screencontinuity.dragserver</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.accessibility.axctl</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>

 	<true/>
 	<key>com.apple.logd.admin</key>
 	<true/>
+	<key>com.apple.managedconfiguration.mdmd-access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.mdmuserd-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
 	<array>
+		<string>DEPInstallation</string>
 		<string>SilentNonUIInstallation</string>
 		<string>Removal</string>
 	</array>

 	<true/>
 	<key>com.apple.mediastream.mstreamd-access</key>
 	<true/>
+	<key>com.apple.migrationd.client</key>
+	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>

 		<string>Enroll</string>
 		<string>Manage</string>
 	</array>
+	<key>com.apple.private.ndoagent</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.octagon</key>

 	<true/>
 	<key>com.apple.securebackupd.access</key>
 	<true/>
+	<key>com.apple.securesettingsmigration.host</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.notes</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.aa.custodian.xpc</string>
 		<string>com.apple.aa.inheritance.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.fileprovider.enumerate</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<true/>
 	<key>com.apple.geoanalyticsd.telemetry</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
 	<true/>
 	<key>com.apple.intelligenceflow.context</key>

 	<true/>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>
+	<key>com.apple.private.canGetAppLinkInfo</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

 		<string>group.com.apple.Maps</string>
 		<string>group.com.apple.icloud.fm</string>
 		<string>group.com.apple.notes</string>
+		<string>group.com.apple.sports</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<string>com.apple.StickerPickerService</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.VE.CVCalibration.client</key>
+	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.devicesharing.guest-user-mode-client</key>
+	<true/>
 	<key>com.apple.feedbackd.remote-evaluation</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.arkit.authorization</key>
+	<array>
+		<string>worldTracking</string>
+	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

 	</array>
 	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
 	<true/>
+	<key>com.apple.private.security.arkit</key>
+	<array>
+		<string>allowImmersiveExemption</string>
+		<string>allowBackgroundPoseData</string>
+	</array>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.realitysimulation.apps</string>
+		<string>com.apple.ve.cvcalibrationd.xpc</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.devicesharing.guestusermodeservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.surfboard-prevent-linking-for-restoration</key>
 	<true/>
+	<key>com.apple.surfboard.scene-rendering-not-clipped</key>
+	<true/>
 </dict>
 </plist>
 

```
### StickersUltraExtension

> `/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension`

```diff

 <dict>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>

```
### StickersUltra

> `/Applications/StickersUltra.app/StickersUltra`

```diff

 <dict>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>

```
### PassbookSettingsIntentExtension

> `/Applications/SubcredentialUIService.app/Extensions/PassbookSettingsIntentExtension.appex/PassbookSettingsIntentExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.cards.all-access</key>
+	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### SubcredentialInvitationMessagesExtension

> `/Applications/SubcredentialUIService.app/PlugIns/SubcredentialInvitationMessagesExtension.appex/SubcredentialInvitationMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>
 	<true/>
 	<key>com.apple.internal.seserviced.ptattestation</key>

```
### SubcredentialUIService

> `/Applications/SubcredentialUIService.app/SubcredentialUIService`

```diff

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.private.barcodesupport.allowNotifications</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>VisualIntelligenceCamera.DetectedLabels</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.canIgnoreAppLinkEnabledProperty</key>

 	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
-	<key>com.apple.sage.summarization</key>
-	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### Vehicle

> `/Applications/Vehicle.app/Vehicle`

```diff

 	<string>com.apple.AutoSettings</string>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
+	<key>com.apple.bannerkit.post</key>
+	<true/>
 	<key>com.apple.developer.carp</key>
 	<true/>
 	<key>com.apple.private.CarAssetUtils.variants</key>

 		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.CarPlayApp.punch-through-service</string>
 		<string>com.apple.CarAssetUtils.variants</string>
+		<string>com.apple.CarPlayApp.service</string>
 	</array>
 </dict>
 </plist>

```
### WebSheet

> `/Applications/WebSheet.app/WebSheet`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.authentication-services.access-credential-identities</key>
 	<true/>
+	<key>com.apple.authentication-services.allow-authentication-request-any-rpid</key>
+	<true/>
 	<key>com.apple.captive.private</key>
 	<true/>
 	<key>com.apple.developer.web-payments</key>

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.keychain.kcsharing.client</key>
+	<true/>
 	<key>com.apple.private.necp.match</key>
 	<true/>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.mobilesafari-settings</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.email.maild</string>
+		<string>com.apple.security.kcsharing</string>
+		<string>com.apple.security.octagon</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.cfnetwork</string>
+		<string>com.apple.cfnetwork.testing</string>
 		<string>com.apple.mobilesafari</string>
 		<string>com.apple.certificates</string>
 		<string>com.apple.safari.credit-cards</string>
+		<string>com.apple.cfnetwork-recently-deleted</string>
+		<string>com.apple.cfnetwork-recently-deleted.testing</string>
+		<string>com.apple.password-manager</string>
+		<string>com.apple.password-manager.testing</string>
+		<string>com.apple.password-manager-recently-deleted</string>
+		<string>com.apple.password-manager-recently-deleted.testing</string>
+		<string>com.apple.webkit.webauthn</string>
+		<string>com.apple.webkit.webauthn.testing</string>
+		<string>com.apple.webkit.webauthn-recently-deleted</string>
+		<string>com.apple.webkit.webauthn-recently-deleted.testing</string>
+		<string>com.apple.password-manager.personal</string>
+		<string>com.apple.password-manager.personal.testing</string>
+		<string>com.apple.password-manager.personal-recently-deleted</string>
+		<string>com.apple.password-manager.personal-recently-deleted.testing</string>
+		<string>com.apple.password-manager.generated-passwords</string>
+		<string>com.apple.password-manager.generated-passwords.testing</string>
+		<string>com.apple.password-manager.website-metadata</string>
+		<string>com.apple.password-manager.website-metadata.testing</string>
 	</array>
 </dict>
 </plist>

```
### WidgetRenderer_CarPlay

> `/Applications/WidgetRenderer_CarPlay.app/WidgetRenderer_CarPlay`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DuetActivitySchedulerWidgetRefresh</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<dict>
+					<key>Widgets.Viewed</key>
+					<dict>
+						<key>mode</key>
+						<string>read-write</string>
+					</dict>
+				</dict>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.memorystatus</key>

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.chrono.event-service.gamed</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### WidgetRenderer_Default

> `/Applications/WidgetRenderer_Default.app/WidgetRenderer_Default`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DuetActivitySchedulerWidgetRefresh</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<dict>
+					<key>Widgets.Viewed</key>
+					<dict>
+						<key>mode</key>
+						<string>read-write</string>
+					</dict>
+				</dict>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.memorystatus</key>

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.chrono.event-service.gamed</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.WritingToolsUIService</string>
+	<key>com.apple.devicesharing.guest-user-mode-client</key>
+	<true/>
 	<key>com.apple.feedbackd.remote-evaluation</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.sage.summarization</string>
 		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### InviteMessageBubbleExtension

> `/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```

### 🆕 PCSReadingFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/PCSReadingFlowDelegatePlugin.bundle/PCSReadingFlowDelegatePlugin`

- No entitlements *(yet)*

### 🆕 usbaudiodxpc

> `/System/Library/Audio/Plug-Ins/HAL/usbaudiodxpc.driver/usbaudiodxpc`

- No entitlements *(yet)*
### usbaudiod

> `/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod`

```diff

 	<array>
 		<string>com.apple.audio.driver-registrar</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.usbaudiod.defaults</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 </dict>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.backboardd.pointerRepositioning</key>
 	<true/>
+	<key>com.apple.backlight.backlightaccess</key>
+	<true/>
+	<key>com.apple.backlight.disable_wake_gesture_assertion</key>
+	<true/>
+	<key>com.apple.backlight.force_active_assertion</key>
+	<true/>
+	<key>com.apple.backlight.performrequest</key>
+	<true/>
+	<key>com.apple.backlight.prevent_idle_assertion</key>
+	<true/>
+	<key>com.apple.backlight.unlimited_backlight_assertion</key>
+	<true/>
 	<key>com.apple.bannerkit.post</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

 	<true/>
 	<key>com.apple.corespeech.supportheysiriwhenrecord</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.sociallayer.accessibility</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

 		<string>com.apple.locationd</string>
 		<string>com.apple.keyboard.preferences</string>
 		<string>com.apple.preferences.sounds</string>
-		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.AppSupport</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.backboardd</string>

 		<string>com.apple.speech.SpeechRecognitionCommandAndControl</string>
 		<string>com.apple.Accessibility.SwitchControl</string>
 		<string>com.apple.UIKit</string>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.WatchControl</string>
 		<string>com.apple.airplay</string>
 		<string>com.apple.ClarityUI</string>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.mediaexperience.endpoint.xpc</key>
 	<true/>
+	<key>com.apple.modelmanager.assertion</key>
+	<true/>
 	<key>com.apple.private.CarPlayUIServices.status-bar-style</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

 	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
+	<key>com.apple.runningboard.carplay</key>
+	<true/>
 	<key>com.apple.runningboard.hereditarygrantoriginator</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

 		<string>com.apple.siri.audiopowerupdate.xpc</string>
 		<string>com.apple.systemstatus</string>
 		<string>com.apple.caraccessoryframework.nowplaying</string>
+		<string>com.apple.modelmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
+	<key>com.apple.runningboard.carplay</key>
+	<true/>
 	<key>com.apple.runningboard.hereditarygrantoriginator</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

```
### ClarityBoard

> `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<true/>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>
 	<true/>
 	<key>com.apple.systemstatus.domains</key>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.setsilentmode.allow</key>
+	<true/>
 	<key>com.apple.private.sociallayer.accessibility</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

```
### ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

 	</array>
 	<key>com.apple.SubmitDiagInfo.tower-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
+	<key>com.apple.private.MobileContainerManager.lookup</key>
+	<dict>
+		<key>appData</key>
+		<true/>
+	</dict>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	<array>
 		<string>kTCCServiceSystemPolicyAllFiles</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.allowed-complete-urgent-log-submission</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1240</string>
+		<string>1731</string>
 	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>

```
### ReportSystemMemory

> `/System/Library/CoreServices/ReportSystemMemory`

```diff

 	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 </dict>

```
### ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<dict>

```
### ShortcutsTopHitsExtension

> `/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/ActionKit.framework</string>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/CallHistoryDB/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CallHistorySyncHelper</string>
+		<string>com.apple.contactsd</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.siriactionsd.xpc</string>
 	</array>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
+	<key>com.apple.assistant.domain.status.access</key>
+	<true/>
 	<key>com.apple.assistant.domain.system.service</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.deleteContainerContent</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>
 	<true/>
+	<key>com.apple.private.capture-extension-host</key>
+	<true/>
 	<key>com.apple.private.carkit</key>
 	<true/>
 	<key>com.apple.private.carkit.app</key>

 	<true/>
 	<key>com.apple.private.coordination.timers</key>
 	<true/>
+	<key>com.apple.private.coreaudio.borrowaudioapplication.allow</key>
+	<true/>
 	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
 	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.SpringBoard.ReadyForRestore</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.purplebuddy.launchMigrationSourceUI</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.donotdisturb.0191488e-ff8a-728d-a9f7-08a0a77abd7d.update.client-identifiers</key>

 		<string>com.apple.springboard.NCModeManager</string>
 		<string>com.apple.springboard.dndstatemonitor</string>
 		<string>com.apple.springboard.CoverSheetDiscoveryProvider</string>
+		<string>com.apple.UserNotificationCore.SpotlightIndexer</string>
 	</array>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<array>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.matter.native.xpc</string>
+		<string>com.apple.mediacontrol.xpc</string>
+		<string>com.apple.assistant.domain.status.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 		<string>/private/var/MobileAsset/Assets/com_apple_MobileAsset_VoiceServices_VoiceResources/</string>
 		<string>/private/var/MobileAsset/AssetsV2/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Media/DCIM/</string>

```
### osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.osanalytics.factoryproxysync</string>
 		<string>com.apple.osanalytics.OTATaskingAgent</string>
 		<string>com.apple.osanalytics</string>
 		<string>com.apple.softwareupdateservicesd</string>

```
### com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 	<true/>
 	<key>com.apple.developer.driverkit.transport.pci.bridge</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.custom-coredump-location</key>
 	<string>wifi-bcmwlan-dextcrash-%!P(MISSING).%!T(MISSING).core</string>
 	<key>com.apple.private.driverkit.driver-launch-configuration</key>

```

### 🆕 ASRFullPayloadCorrection

> `/System/Library/ExtensionKit/Extensions/ASRFullPayloadCorrection.appex/ASRFullPayloadCorrection`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.lighthouse.ASRFullPayloadCorrection</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>ASRFullPayloadCorrection</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Dictation.UserEdit</key>
				<true/>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
	</array>
	<key>com.apple.siri.analytics.assistant</key>
	<true/>
</dict>
</plist>

```

### 🆕 AdAttributionKitEngagementExtension

> `/System/Library/ExtensionKit/Extensions/AdAttributionKitEngagementExtension.appex/AdAttributionKitEngagementExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.attributionkitd.postback-proxy</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.attributionkitd.xpc.postback-proxy</string>
	</array>
</dict>
</plist>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 AssistantCoreFollowupExtension

> `/System/Library/ExtensionKit/Extensions/AssistantCoreFollowupExtension.appex/AssistantCoreFollowupExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.assistant.domain.system.settings.access</key>
	<true/>
	<key>com.apple.frontboard.shutdown</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.Storage</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.Storage.Preboard</key>
	<true/>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.corefollowup.agent</string>
		<string>com.apple.assistant.domain.system.settings.service</string>
	</array>
</dict>
</plist>

```
### AudiovisualThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/AudiovisualThumbnailExtension.appex/AudiovisualThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```
### BiomeSELFIngestor

> `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor`

```diff

 				<string>IntelligenceFlow.SearchToolTelemetry</string>
 				<string>IntelligenceFlow.ExecutorTelemetry</string>
 				<string>IntelligenceFlow.IFRequestTelemetry</string>
+				<string>IntelligenceFlow.PlanGenerationTelemetry</string>
 			</array>
 		</dict>
 	</dict>

```
### CalendarThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/CalendarThumbnailExtension.appex/CalendarThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```
### CameraMessagesApp

> `/System/Library/ExtensionKit/Extensions/CameraMessagesApp.appex/CameraMessagesApp`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-apac-codec</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.mediastream.mstreamd-access</key>
 	<true/>
 	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>

```
### ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.AppleMediaServicesUI.ComposeReviewExtension</string>
+	</dict>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>

 	<array>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amstoold</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>com_apple_driver_FairPlayIOKitUserClient</string>

```
### ContactThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ContactThumbnailExtension.appex/ContactThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```
### DevicePropertiesExtension

> `/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ExperimentationExtension

> `/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.FedStats.MLHostPlugin</string>
+	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
+		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>
 		<string>Device.Wireless.BluetoothGATTSession</string>
 		<string>Media.StreamingStats</string>
 		<string>App.InFocus</string>

 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>
+		<string>AeroML.RawEvent.PhotosSearchSession</string>
 		<string>CameraCapture.AutoFocusROI</string>
 		<string>Photos.Style</string>
 		<string>WalletPaymentsCommerce.FinancialInsights.RecurringSendSuggestions</string>
 		<string>Safari.Browsing.Assistant</string>
-		<string>GenerativeExperiences.TransparencyLog</string>
 		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
+		<string>GenerativeExperiences.PromptTags</string>
 		<string>AdAttributionKit.AggregatedReporting.Purchase</string>
 		<string>AdAttributionKit.AggregatedReporting.Conversion</string>
 		<string>Siri.ASR.RequestMetricsRecord</string>
 		<string>WalletPaymentsCommerce.UserProofing.Result</string>
+		<string>Autonaming.Messages.AccuracyFedStats</string>
+		<string>Safari.WebsitesBlockingQuit</string>
+		<string>LocalAuthentication.UI.Dialogs</string>
+		<string>VisualIntelligenceCamera.DetectedLabels</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.coreidvd.identity-proofing-data-sharing.xpc</string>
 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>

```
### FindMyIntentsExtension

> `/System/Library/ExtensionKit/Extensions/FindMyIntentsExtension.appex/FindMyIntentsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
+	<key>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</key>
+	<true/>
+	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.intentsession</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.ownersession</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.findmy</string>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.findmy</string>
+	</dict>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+	</array>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+	</array>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 </dict>
 </plist>
 

```
### FontThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/FontThumbnailExtension.appex/FontThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```

### 🆕 GPNonUIExtension

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/GPNonUIExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.ImagePlayground.InlineExtension</string>
	<key>com.apple.VE.CVCalibration.client</key>
	<true/>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.Photos</string>
	</array>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
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
	<key>com.apple.private.arkit.authorization</key>
	<array>
		<string>worldTracking</string>
	</array>
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
		<string>path</string>
		<key>value</key>
		<string>/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension</string>
	</dict>
	<key>com.apple.private.avfoundation.capture.allow</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>GeneratedImageUserInteraction</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
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
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.librarymanagement</key>
	<true/>
	<key>com.apple.private.security.arkit</key>
	<array>
		<string>allowImmersiveExemption</string>
		<string>allowBackgroundPoseData</string>
	</array>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.GenerativePlayground</string>
	</array>
	<key>com.apple.security.device.camera</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
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
		<string>com.apple.generativeexperiences.availabilityService</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.ind.cloudfeatures</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.realitysimulation.apps</string>
		<string>com.apple.ve.cvcalibrationd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp.remoteUIExtension</string>
+	<key>com.apple.VE.CVCalibration.client</key>
+	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.arkit.authorization</key>
+	<array>
+		<string>worldTracking</string>
+	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

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

 	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
+	<key>com.apple.private.security.arkit</key>
+	<array>
+		<string>allowImmersiveExemption</string>
+		<string>allowBackgroundPoseData</string>
+	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.realitysimulation.apps</string>
+		<string>com.apple.ve.cvcalibrationd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### GenerativeAssistantExtension

> `/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension`

```diff

 	<array>
 		<string>/private/var/tmp/VICamera/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/tmp/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>

 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 		<string>/private/var/folders/*/*/*/com.apple.FeatureStore/</string>
 	</array>
+	<key>com.apple.security.ts.tmpdir</key>
+	<array>
+		<string>GenerativeAssistantTools</string>
+	</array>
 	<key>com.apple.sharing.Client</key>
 	<true/>
 	<key>com.apple.shortcuts.background-running</key>

```
### HomeAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/HomeAppIntentsExtension.appex/HomeAppIntentsExtension`

```diff

 	<array>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.matter.native.xpc</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.matter.native.xpc</string>

```
### ImageThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ImageThumbnailExtension.appex/ImageThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```

### 🆕 LighthouseASRReplay

> `/System/Library/ExtensionKit/Extensions/LighthouseASRReplay.appex/LighthouseASRReplay`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.LighthouseASRReplay</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>ASRReplay</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Siri.ASR.ContextualReplayRecord</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/tmp/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```

### 🆕 LighthouseAVExtension

> `/System/Library/ExtensionKit/Extensions/LighthouseAVExtension.appex/LighthouseAVExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.LighthouseAV.LighthouseAVExtension</string>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.coreaudio</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Device.Audio.AdaptiveVolume</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Documents/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
</dict>
</plist>

```

### 🆕 LighthouseServicesAnalyticsExtension

> `/System/Library/ExtensionKit/Extensions/LighthouseServicesAnalyticsExtension.appex/LighthouseServicesAnalyticsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.lighthouse.LighthouseServicesAnalyticsExtension</string>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.internal.Blackbird.DataAccess</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.amsondevicestoraged</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.amsondevicestoraged.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.OnDeviceStorage</string>
	</array>
</dict>
</plist>

```

### 🆕 MessagesAnalyticsWorker

> `/System/Library/ExtensionKit/Extensions/MessagesAnalyticsWorker.appex/MessagesAnalyticsWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.poirot.MessagesAnalyticsWorker</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Messages.Search.Event</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.feedbacklogger</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.poirot.MessagesAnalyticsWorker</string>
		<string>com.apple.poirot.poirot_tool</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.feedbacklogger</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.parsecd</string>
	</array>
</dict>
</plist>

```
### MetricsExtension

> `/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 MobileMailDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/MobileMailDiagnosticExtension.appex/MobileMailDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobilemail.DiagnosticExtension</string>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.email</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.mail</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.mail</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.email.maild</string>
	</array>
</dict>
</plist>

```

### 🆕 ODDIMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIMetricsExtension.appex/ODDIMetricsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.ODDI.MetricsExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.ODDI.MetricsExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
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
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.ODDI.MetricsWorker</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.ODDI.MetricsWorker</string>
	</array>
</dict>
</plist>

```

### 🆕 ODDIPoirotMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/ODDIPoirotMetricsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
		<string>com.apple.poirot.poirot_tool</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### OfficeThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/OfficeThumbnailExtension.appex/OfficeThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```
### PassbookSettingsIntentExtension

> `/System/Library/ExtensionKit/Extensions/PassbookSettingsIntentExtension.appex/PassbookSettingsIntentExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.cards.all-access</key>
+	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### PhotosMessagesApp

> `/System/Library/ExtensionKit/Extensions/PhotosMessagesApp.appex/PhotosMessagesApp`

```diff

 	<array>
 		<string>com.apple.mobileslideshow</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>

```
### PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.priml.pfl.plugins</string>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+	</array>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
+	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeExperiences.PromptTags</string>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>

 			<key>Streams</key>
 			<array>
 				<string>Zeolite.Ledger.Embedding</string>
+				<string>GenerativeExperiences.TransparencyLog</string>
+				<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
+				<string>App.Intent</string>
 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.email.maild</string>
 		<string>com.apple.mlhostd.xpc</string>
 		<string>com.apple.cloudd</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.modelmanager</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.gms.availability</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
 	</array>
 </dict>
 </plist>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.ap.promotedcontent.identifiermanager</string>
+		<string>com.apple.absd</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### QuickLookUIExtension

> `/System/Library/ExtensionKit/Extensions/QuickLookUIExtension.appex/QuickLookUIExtension`

```diff

 	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-read</key>

```

### 🆕 SearchToolDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolDiagnosticExtension.appex/SearchToolDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.omniSearch.SearchToolDiagnosticExtension</string>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SearchToolExtension</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>SearchTool.Transcript</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.spotlight.search.internal</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`

```diff

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.diagnosticpipeline.request</key>
+	<true/>
+	<key>com.apple.fileprovider.enumerate</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/OmniSearch.framework</string>

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>SearchTool.Transcript</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 			</dict>
 		</dict>
 	</dict>

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
+	<key>com.apple.private.security.storage.SiriFeatureStore</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.spotlight.parsec</key>

 	<true/>
 	<key>com.apple.private.suggestions</key>
 	<true/>
+	<key>com.apple.private.suggestions.contacts</key>
+	<true/>
 	<key>com.apple.private.suggestions.events</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Containers/com.apple.managedcorespotlightd/EnabledIndexes</string>
+		<string>/Library/Trial/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/com.apple.FeatureStore/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobileasset.autoasset</string>

 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.dmd.policy</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.managedcorespotlightd</string>
+		<string>com.apple.triald.namespace-management</string>
+		<string>com.apple.diagnosticpipeline.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.spotlightui</string>
 		<string>com.apple.OmniSearch</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.tokengeneration</string>

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.SpotlightResources.Defaults</string>
+		<string>com.apple.siri.morphun</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
 	<key>com.apple.security.personal-information.calendars</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>

 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Containers/com.apple.managedcorespotlightd/EnabledIndexes</string>
+	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>AGXDeviceUserClient</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.managedcorespotlightd</string>
+		<string>com.apple.diagnosticpipeline.service</string>
+	</array>
+	<key>com.apple.security.temporary-exception.sbpl</key>
+	<array>
+		<string>(allow file-issue-extension (extension-class "com.apple.managedcorespotlightd.read-write"))</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.spotlight</string>
 		<string>com.apple.OmniSearch</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.tokengeneration</string>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>337</string>
+		<string>755</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin`

```diff

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppIntent</string>

 	<array>
 		<string>group.com.apple.siri.sirisuggestions</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.siri.inference/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sirisuggestions</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siriinferenced.remembers</string>
 		<string>com.apple.intelligenceplatform.View</string>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.ironwood.support</string>
 	</array>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sirisuggestions</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siriinferenced.remembers</string>
 		<string>com.apple.intelligenceplatform.View</string>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.mobileasset.autoasset</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant.backedup</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siriinferenced</key>
 	<true/>
+	<key>com.apple.sirisuggestions.allow</key>
+	<true/>
+	<key>com.apple.sirisuggestions.application-id</key>
+	<string>com.apple.siri.SiriSuggestionsLightHousePlugin</string>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1343</string>
+		<string>755</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### SiriTurnRestatementExtension

> `/System/Library/ExtensionKit/Extensions/SiriTurnRestatementExtension.appex/SiriTurnRestatementExtension`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.Lighthouse.DeepThought.SiriTurnRestatementExtension</string>
+	<string>com.apple.SiriMetrics.SiriTurnRestatementExtension</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Siri.SELFProcessedEvent</string>

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SpeakerIdSamplingExtension

> `/System/Library/ExtensionKit/Extensions/SpeakerIdSamplingExtension.appex/SpeakerIdSamplingExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.ssr.rpisamplingservice</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.ap.promotedcontent.identifiermanager</string>
+		<string>com.apple.absd</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 TVAppExtension

> `/System/Library/ExtensionKit/Extensions/TVAppExtension.appex/TVAppExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1192613791</string>
	<key>adi-client</key>
	<string>409835401</string>
	<key>application-identifier</key>
	<string>com.apple.VideosUI.TVAppExtension</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.VideosUI.TVAppExtension</string>
	<key>com.apple.asd.client</key>
	<string>9824938448</string>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-access-to-device-list</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.app-tap</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreidvd.spi</key>
	<true/>
	<key>com.apple.coremedia.allow-mpeg4streaming</key>
	<true/>
	<key>com.apple.coremedia.allow-protected-content-playback</key>
	<true/>
	<key>com.apple.coretelephony.Identity.get</key>
	<true/>
	<key>com.apple.developer.associated-domains</key>
	<array/>
	<key>com.apple.developer.group-session</key>
	<true/>
	<key>com.apple.developer.networking.multicast</key>
	<true/>
	<key>com.apple.developer.pass-type-identifiers</key>
	<array>
		<string>*.pass.com.apple.itunes.storecredit</string>
	</array>
	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
	<array>
		<string>com.apple.groupactivities</string>
	</array>
	<key>com.apple.features.all-access</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.itunescloud.in-app-message-service</key>
	<true/>
	<key>com.apple.itunescloudd.private</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.launchservices.receivereferrerrurl</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.passes.add-silently</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.payment.amp-card-enrollment</key>
	<true/>
	<key>com.apple.payment.card-on-file</key>
	<true/>
	<key>com.apple.payment.passbook-secure-ui-service-access</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.userManagedAssets</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Purchase</string>
		<string>IAPHistory</string>
	</array>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.attentionawareness</key>
	<true/>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.cfnetwork.har-capture-amp</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.ids.registration</key>
	<array>
		<string>com.apple.private.alloy.itunes</string>
	</array>
	<key>com.apple.private.ids.remoteurlconnection</key>
	<true/>
	<key>com.apple.private.ids.session</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.in-app-payments</key>
	<true/>
	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>
	<string>*</string>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.tv.sharedcontainer</string>
		<string>group.tvappservices.container</string>
	</array>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.sportskit.client</key>
	<true/>
	<key>com.apple.private.subscriptionservice.internal</key>
	<true/>
	<key>com.apple.private.swc.additional-service-details-consumer</key>
	<true/>
	<key>com.apple.private.swc.system-app</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.tvAppExtension</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.tvappservices.container</string>
		<string>group.com.apple.sports</string>
		<string>group.com.apple.tv.sharedcontainer</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Media/Purchases/</string>
		<string>/private/var/mobile/Media/iTunes_Control/</string>
		<string>/private/var/mobile/Media/ManagedPurchases/TVApp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/com.apple.VideoSubscriberAccount/</string>
		<string>/CTestData/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>com_apple_driver_FairPlayIOKitUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.aa.daemon.xpc</string>
		<string>com.apple.itunescloudd.xpc</string>
		<string>com.apple.coreidvd.proofing</string>
		<string>com.apple.AttentionAwareness</string>
		<string>com.apple.adid</string>
		<string>com.apple.amsaccountsd.security</string>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.atvcached</string>
		<string>com.apple.itunescloud.in-app-message-service</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.hsa-authentication-server</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.medialibraryd.xpc</string>
		<string>com.apple.rtcreportingd</string>
		<string>com.apple.watchlistd.xpc</string>
		<string>com.apple.watchlistd.bulletin-server</string>
		<string>com.apple.mediaartworkd.xpc</string>
		<string>com.apple.atc.xpc</string>
		<string>com.apple.atc.xpc.downloadprogress</string>
		<string>com.apple.routined.registration</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.asd.scoring</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.passd.library</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>
		<string>com.apple.sociallayerd</string>
		<string>com.apple.symptom_analytics</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.itunescloud.remote-request-execution-service</string>
		<string>com.apple.sportsd.xpc</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.ITMLKit</string>
		<string>com.apple.TVMLKit</string>
		<string>com.apple.mobileipod</string>
		<string>com.apple.tv</string>
		<string>com.apple.videos</string>
		<string>com.apple.videos-preferences</string>
		<string>com.apple.homesharing</string>
		<string>com.apple.SocialLayer</string>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.VideosUI.TVAppExtension</string>
	</array>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.tv.api</key>
	<array>
		<string>iTunes</string>
	</array>
	<key>com.apple.tvmlkit.private</key>
	<true/>
	<key>com.apple.wallet.features.all-access</key>
	<true/>
	<key>com.apple.watchlist.private</key>
	<true/>
	<key>com.apple.watchlist.private.playback-report</key>
	<true/>
	<key>com.apple.watchlistd.post-bulletins</key>
	<true/>
	<key>fairplay-client</key>
	<integer>1974055701</integer>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.VideoSubscriberAccount</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 TetsuoDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/TetsuoDiagnosticExtension.appex/TetsuoDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.visionproapp.diagnosticextension</string>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.tdg-wb</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.tdg-wb</key>
		<string>com.apple.tdg-wb</string>
	</dict>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.lsd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.visioncompaniond</string>
	</array>
</dict>
</plist>

```
### TextInputAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/TextInputAppIntentsExtension.appex/TextInputAppIntentsExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict/>
+</plist>
 

```
### TextThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/TextThumbnailExtension.appex/TextThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```
### VisualGenerationInference

> `/System/Library/ExtensionKit/Extensions/VisualGenerationInference.appex/VisualGenerationInference`

```diff

 	<string>com.apple.VisualGeneration.inference</string>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.ane.memoryUnwiringOptOutAccess.allow</key>
+	<true/>
 	<key>com.apple.aned.private.adapterWeight.allow</key>
 	<true/>
 	<key>com.apple.aned.private.allow</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>com.apple.accessibility.cache.vot</string>
 		<string>com.apple.accessibility.cache.zoom</string>
 		<string>com.apple.accessibility.cache.*</string>
+		<string>com.apple.system.DirectoryService.InvalidateCache*</string>
 		<string>com.apple.coreservices.launchservices.session.*</string>
 		<string>user.uid.501.syslog.*</string>
+		<string>_AXNotification__UUID_</string>
+		<string>_AXNotification_AXMRInvertColors</string>
+		<string>_AXNotification_AXMRReduceWhitePoint</string>
+		<string>_AXNotification_AXMuseDisplayFiltersEnabled</string>
 		<string>_UUID_.notification</string>
 		<string>CPActiveCountryCodeChanged.Internal</string>
 		<string>MCManagedBooksChanged</string>
 		<string>PINPolicyChangedNotification</string>
+		<string>com.apple.ManagedConfiguration.diagnosticsCollected</string>
 		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
 		<string>com.apple.ManagedConfiguration.profileListChanged</string>
 		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>

 		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
 		<string>com.apple.UIKit.InternalPreferences</string>
 		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
+		<string>com.apple.accessibility.QuickSpeakLocaleForLanguage</string>
+		<string>com.apple.accessibility.cache.guided.access</string>
 		<string>com.apple.accessibility.haptics.active.status.private</string>
+		<string>com.apple.accessibility.internal.reader.changed</string>
 		<string>com.apple.managedconfiguration._UUID_</string>
+		<string>com.apple.managedconfiguration.allowhealthdatasubmissionchanged</string>
 		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
 		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
+		<string>com.apple.managedconfiguration.clearpasscodegenerationcaches</string>
 		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
 		<string>com.apple.managedconfiguration.defaultsdidchange</string>
 		<string>com.apple.managedconfiguration.effectivesettingschanged</string>
+		<string>com.apple.managedconfiguration.homescreenlayoutchanged</string>
 		<string>com.apple.managedconfiguration.keyboardsettingschanged</string>
 		<string>com.apple.managedconfiguration.newssettingschanged</string>
 		<string>com.apple.managedconfiguration.passcodechanged</string>
 		<string>com.apple.managedconfiguration.restrictionchanged</string>
 		<string>com.apple.managedconfiguration.settingschanged</string>
 		<string>com.apple.managedconfiguration.webFilterUIActiveDidChange</string>
+		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
 		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
 		<string>com.apple.mobile.keybagd.lock_status</string>
 		<string>com.apple.mobile.keybagd.user_changed</string>
 		<string>com.apple.system.thermalpressurelevel</string>
+		<string>com.apple.voiceovertouch.screencurtain</string>
 		<string>__ABDataBaseChangedByOtherProcessNotification</string>
 		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
 		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>

 		<string>com.apple.CFNetwork.har-capture-update</string>
 		<string>com.apple.CFPreferences._domainsChangedExternally</string>
 		<string>com.apple.LaunchServices.database</string>
+		<string>com.apple.TTS.synthProviderVoicesDidUpdate</string>
 		<string>com.apple.UIKit.LoggingPreferences</string>
 		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
 		<string>com.apple.WebKit.deleteAllCode</string>

 		<string>com.apple.WebKit.showGraphicsLayerTree</string>
 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>
+		<string>com.apple.WebKit.showLegacyFlexReasons</string>
 		<string>com.apple.WebKit.showMemoryCache</string>
 		<string>com.apple.WebKit.showPaintOrderTree</string>
 		<string>com.apple.WebKit.showRenderTree</string>

 		<string>org.WebKit.memoryWarning</string>
 		<string>org.WebKit.memoryWarning.begin</string>
 		<string>org.WebKit.memoryWarning.end</string>
+		<string>org.WebKit.testNotification</string>
 	</array>
 	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
 	<true/>

 		<string>BlockIOKitInWebContentSandbox</string>
 		<string>local:WebContentProcessLaunched</string>
 		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>BlockOpenDirectoryInWebContentSandbox</string>
+		<string>BlockMobileAssetInWebContentSandbox</string>
+		<string>BlockMobileGestaltInWebContentSandbox</string>
+		<string>BlockWebInspectorInWebContentSandbox</string>
+		<string>BlockIconServicesInWebContentSandbox</string>
+		<string>BlockFontServiceInWebContentSandbox</string>
 	</array>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>

 		<string>local:WebContentProcessLaunched</string>
 		<string>EnableQuickLookSandboxResources</string>
 		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>BlockOpenDirectoryInWebContentSandbox</string>
+		<string>BlockMobileAssetInWebContentSandbox</string>
+		<string>BlockMobileGestaltInWebContentSandbox</string>
+		<string>BlockWebInspectorInWebContentSandbox</string>
+		<string>BlockIconServicesInWebContentSandbox</string>
+		<string>BlockFontServiceInWebContentSandbox</string>
 	</array>
 	<key>com.apple.private.web-browser-engine.webcontent</key>
 	<true/>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>com.apple.accessibility.cache.vot</string>
 		<string>com.apple.accessibility.cache.zoom</string>
 		<string>com.apple.accessibility.cache.*</string>
+		<string>com.apple.system.DirectoryService.InvalidateCache*</string>
 		<string>com.apple.coreservices.launchservices.session.*</string>
 		<string>user.uid.501.syslog.*</string>
+		<string>_AXNotification__UUID_</string>
+		<string>_AXNotification_AXMRInvertColors</string>
+		<string>_AXNotification_AXMRReduceWhitePoint</string>
+		<string>_AXNotification_AXMuseDisplayFiltersEnabled</string>
 		<string>_UUID_.notification</string>
 		<string>CPActiveCountryCodeChanged.Internal</string>
 		<string>MCManagedBooksChanged</string>
 		<string>PINPolicyChangedNotification</string>
+		<string>com.apple.ManagedConfiguration.diagnosticsCollected</string>
 		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
 		<string>com.apple.ManagedConfiguration.profileListChanged</string>
 		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>

 		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
 		<string>com.apple.UIKit.InternalPreferences</string>
 		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
+		<string>com.apple.accessibility.QuickSpeakLocaleForLanguage</string>
+		<string>com.apple.accessibility.cache.guided.access</string>
 		<string>com.apple.accessibility.haptics.active.status.private</string>
+		<string>com.apple.accessibility.internal.reader.changed</string>
 		<string>com.apple.managedconfiguration._UUID_</string>
+		<string>com.apple.managedconfiguration.allowhealthdatasubmissionchanged</string>
 		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
 		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
+		<string>com.apple.managedconfiguration.clearpasscodegenerationcaches</string>
 		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
 		<string>com.apple.managedconfiguration.defaultsdidchange</string>
 		<string>com.apple.managedconfiguration.effectivesettingschanged</string>
+		<string>com.apple.managedconfiguration.homescreenlayoutchanged</string>
 		<string>com.apple.managedconfiguration.keyboardsettingschanged</string>
 		<string>com.apple.managedconfiguration.newssettingschanged</string>
 		<string>com.apple.managedconfiguration.passcodechanged</string>
 		<string>com.apple.managedconfiguration.restrictionchanged</string>
 		<string>com.apple.managedconfiguration.settingschanged</string>
 		<string>com.apple.managedconfiguration.webFilterUIActiveDidChange</string>
+		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
 		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
 		<string>com.apple.mobile.keybagd.lock_status</string>
 		<string>com.apple.mobile.keybagd.user_changed</string>
 		<string>com.apple.system.thermalpressurelevel</string>
+		<string>com.apple.voiceovertouch.screencurtain</string>
 		<string>__ABDataBaseChangedByOtherProcessNotification</string>
 		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
 		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>

 		<string>com.apple.CFNetwork.har-capture-update</string>
 		<string>com.apple.CFPreferences._domainsChangedExternally</string>
 		<string>com.apple.LaunchServices.database</string>
+		<string>com.apple.TTS.synthProviderVoicesDidUpdate</string>
 		<string>com.apple.UIKit.LoggingPreferences</string>
 		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
 		<string>com.apple.WebKit.deleteAllCode</string>

 		<string>com.apple.WebKit.showGraphicsLayerTree</string>
 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>
+		<string>com.apple.WebKit.showLegacyFlexReasons</string>
 		<string>com.apple.WebKit.showMemoryCache</string>
 		<string>com.apple.WebKit.showPaintOrderTree</string>
 		<string>com.apple.WebKit.showRenderTree</string>

 		<string>org.WebKit.memoryWarning</string>
 		<string>org.WebKit.memoryWarning.begin</string>
 		<string>org.WebKit.memoryWarning.end</string>
+		<string>org.WebKit.testNotification</string>
 	</array>
 	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
 	<true/>

 		<string>BlockIOKitInWebContentSandbox</string>
 		<string>local:WebContentProcessLaunched</string>
 		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>BlockOpenDirectoryInWebContentSandbox</string>
+		<string>BlockMobileAssetInWebContentSandbox</string>
+		<string>BlockMobileGestaltInWebContentSandbox</string>
+		<string>BlockWebInspectorInWebContentSandbox</string>
+		<string>BlockIconServicesInWebContentSandbox</string>
+		<string>BlockFontServiceInWebContentSandbox</string>
 	</array>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>

 		<string>local:WebContentProcessLaunched</string>
 		<string>EnableQuickLookSandboxResources</string>
 		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>BlockOpenDirectoryInWebContentSandbox</string>
+		<string>BlockMobileAssetInWebContentSandbox</string>
+		<string>BlockMobileGestaltInWebContentSandbox</string>
+		<string>BlockWebInspectorInWebContentSandbox</string>
+		<string>BlockIconServicesInWebContentSandbox</string>
+		<string>BlockFontServiceInWebContentSandbox</string>
 	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>

```
### WebThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/WebThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.quicklook-thumbnail.webkit</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>

```
### ZeoliteExtension

> `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension`

```diff

 	<array>
 		<string>Zeolite.Ledger.Embedding</string>
 	</array>
+	<key>com.apple.private.biome.read</key>
+	<array>
+		<string>App.Intent</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

 		<dict>
 			<key>Streams</key>
 			<array>
+				<string>App.Intent</string>
 				<string>GenerativeExperiences.TransparencyLog</string>
 				<string>Zeolite.Ledger.Embedding</string>
 				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.mlhost.allowedDictionaryGroups</key>
+	<array>
+		<string>com.apple.zeolite.ZeoliteExtension</string>
+	</array>
+	<key>com.apple.private.mlhost.dictionaryRead</key>
+	<true/>
+	<key>com.apple.private.mlhost.dictionaryWrite</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mlhostd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mlhostd.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### com.apple.mlhost.CloudWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.mlhost.allowedTasks</key>
+	<array>
+		<string>*</string>
+	</array>
 	<key>com.apple.private.mlhost.configRead</key>
 	<true/>
+	<key>com.apple.private.mlhost.taskDelete</key>
+	<true/>
 	<key>com.apple.private.mlhost.taskRead</key>
 	<true/>
 	<key>com.apple.private.mlhost.taskWrite</key>

```
### com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.mlhost.allowedDictionaryGroups</key>
+	<array>
+		<string>SampleWorker</string>
+	</array>
+	<key>com.apple.private.mlhost.dictionaryDelete</key>
+	<true/>
+	<key>com.apple.private.mlhost.dictionaryRead</key>
+	<true/>
+	<key>com.apple.private.mlhost.dictionaryWrite</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mlhostd.xpc</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mobileasset.autoasset</string>

```
### iWorkThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/iWorkThumbnailExtension.appex/iWorkThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```
### apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.early_boot_mount</key>
 	<true/>
+	<key>com.apple.rootless.volume.Preboot</key>
+	<true/>
 	<key>com.apple.rootless.volume.Recovery</key>
 	<true/>
+	<key>com.apple.rootless.volume.iSCPreboot</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>AppleAPFSUserClient</string>
 </dict>

```
### apfs_stats

> `/System/Library/Filesystems/apfs.fs/apfs_stats`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.apfs.get-graft-info</key>
-	<true/>
 	<key>com.apple.private.apfs.omm.ctl</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### acdiagnose

> `/System/Library/Frameworks/Accounts.framework/Support/acdiagnose`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>AAACCOUNTS.com.apple.acdiagnose</string>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<array>
 		<string>com.apple.accounts.exists.plist</string>
 	</array>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.connectbeforemigrationdidfinish</key>
 	<true/>
 	<key>com.apple.accounts.inactive.fullaccess</key>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Photos/</string>

```
### AudioConverterService

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterService.xpc/AudioConverterService`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
 	<true/>
 	<key>com.apple.private.memory.ownership_transfer</key>

```
### BrowserEngineKit.Intermediary

> `/System/Library/Frameworks/BrowserEngineKit.framework/XPCServices/BrowserEngineKit.Intermediary.xpc/BrowserEngineKit.Intermediary`

```diff

 <dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.DocumentManagerCore.Downloads</string>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<true/>
 	<key>com.apple.mobileassetd.v2</key>
 	<true/>
+	<key>com.apple.private.ciphermld.allow</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ciphermld</string>
 		<string>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.intelligenceplatform.View</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
+		<string>com.apple.linkd.registry</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
 	<array>
 		<string>com.apple.iCloud.CommCenter</string>

 	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
+	<key>com.apple.migrationd.client</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

 	<true/>
 	<key>com.apple.networkd_privileged</key>
 	<true/>
+	<key>com.apple.networkrelay.deviceMonitor</key>
+	<true/>
 	<key>com.apple.networkrelay.retryConnections</key>
 	<true/>
 	<key>com.apple.nfcd.assertion.dontreset</key>

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.CoreTelephony.Slicing.Interfaces.Active.State</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.CoreTelephony.Slicing.LLPHS.State</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.abm.cellularcert</string>
 		<string>com.apple.telephony.control-msg.xpc</string>
-		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
-		<string>com.apple.devicecheckd</string>
 	</array>
 	<key>com.apple.security.lockdownmode.read</key>
 	<true/>

```
### CommCenterMobileHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper`

```diff

 		<string>spi</string>
 		<string>internal</string>
 	</array>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
 	<array>
 		<string>com.apple.iCloud.CommCenter</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callhistorymanager</string>

```
### CommCenterRootHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.debug_port</key>
 	<true/>
 	<key>com.apple.private.logging.admin</key>

```
### FamilyControlsAgent

> `/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent`

```diff

 	<string>serverPreferred</string>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.private.managed-settings.apply</key>
 	<true/>
-	<key>com.apple.private.sandbox.profile</key>
+	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.tcc.allow</key>
 	<array>

 	<true/>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

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

 	<true/>
 	<key>com.apple.private.vfs.skip-mtime-updates</key>
 	<true/>
+	<key>com.apple.private.vfs.support-long-paths</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.fileprovider</key>
 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.FileProvider.DomainCaching</string>
+	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	<array>
 		<string>com.apple.iconservices</string>
 		<string>com.apple.assertiond.applicationstateconnection</string>
-		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.FileProviderDaemon.AppStoreService</string>
 		<string>com.apple.FileProviderDaemon.FPCKService</string>
 		<string>com.apple.cloudd</string>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<array>
 		<string>kTCCServiceFinancialData</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceFinancialData</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceFinancialData</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceFinancialData</string>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Finance/</string>
+		<string>/Library/FinanceBackup/</string>
 		<string>/Library/Caches/Finance/</string>
 		<string>/Library/Caches/com.apple.financed/</string>
 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>

 		<string>com.apple.passd.library</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.passd.payment</string>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.financed</string>
+	<key>com.apple.springboard.CFUserNotification</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### GroupSessionService

> `/System/Library/Frameworks/GroupActivities.framework/XPCServices/GroupSessionService.xpc/GroupSessionService`

```diff

 	<true/>
 	<key>com.apple.StatusKit.presence.clientID</key>
 	<string>groupsessionservice</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.groupRemoteControl.session</string>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### intents_helper

> `/System/Library/Frameworks/Intents.framework/XPCServices/intents_helper.xpc/intents_helper`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.backgroundassets.appstore</key>
 	<true/>
+	<key>com.apple.devicemanagementclient.managedappsd.appconfig</key>
+	<true/>
 	<key>com.apple.dmd-access</key>
 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>
 	<true/>
-	<key>com.apple.dmd.operation.set-app-allow-user-to-hide</key>
-	<true/>
-	<key>com.apple.dmd.operation.set-app-allow-user-to-lock</key>
-	<true/>
-	<key>com.apple.dmd.operation.set-app-associated-domains</key>
-	<true/>
-	<key>com.apple.dmd.operation.set-app-associated-domains-enable-direct-downloads</key>
+	<key>com.apple.dmd.operation.start-managing-app</key>
 	<true/>
-	<key>com.apple.dmd.operation.set-app-extension-uuids</key>
+	<key>com.apple.dmd.operation.stop-managing-app</key>
 	<true/>
-	<key>com.apple.dmd.operation.set-app-removability</key>
+	<key>com.apple.dmd.operation.update-app</key>
 	<true/>
-	<key>com.apple.dmd.operation.set-app-tap-to-pay-screen-lock</key>
+	<key>com.apple.dmd.operation.update-app-attributes</key>
 	<true/>
-	<key>com.apple.dmd.operation.start-managing-app</key>
-	<true/>
-	<key>com.apple.dmd.operation.update-app</key>
+	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.get</key>

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreAppProtection</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.ignoreRemovability</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreRestrictions</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.uninstall</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
+	<key>com.apple.private.remotemanagement.subscriber</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/MobileIdentityData/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
+		<string>com.apple.devicemanagementclient.managedappsd</string>
+		<string>com.apple.dmd</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.fontservicesd</string>

 		<string>com.apple.lsd.installation</string>
 		<string>com.apple.lsd.modifydb</string>
 		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.misagent</string>
 		<string>com.apple.mobile.installd</string>
 		<string>com.apple.pearld</string>
+		<string>com.apple.remotemanagementd.store</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.xpc.amsaccountsd</string>
-		<string>com.apple.dmd</string>
 		<string>com.apple.xpc.amsuniversallinks</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>

```

### 🆕 managedsettingsdiagnoticstool

> `/System/Library/Frameworks/ManagedSettings.framework/managedsettingsdiagnoticstool`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.team-identifier</key>
	<string>Apple</string>
	<key>com.apple.private.managed-settings.diagnostics</key>
	<true/>
</dict>
</plist>

```
### RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
+	<true/>
 	<key>com.apple.private.coreaudio.viewInterruptorName.allow</key>
 	<true/>
 	<key>com.apple.private.coremedia.pidinheritance.allow</key>

```
### MTLCompilerService

> `/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>MTLCompilerService</string>

```
### com.apple.PDFKit.OFD_Preview

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Preview.appex/com.apple.PDFKit.OFD_Preview`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.DictionaryServices.dictionary2</string>

```
### com.apple.PDFKit.OFD_Thumbnail

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Thumbnail.appex/com.apple.PDFKit.OFD_Thumbnail`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.DictionaryServices.dictionary2</string>

```
### com.apple.quicklook.extension.previewUI

> `/System/Library/Frameworks/QuickLook.framework/PlugIns/com.apple.quicklook.extension.previewUI.appex/com.apple.quicklook.extension.previewUI`

```diff

 	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-read</key>

```
### com.apple.quicklook.ThumbnailsAgent

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent`

```diff

 	<string>com.apple.quicklook.ThumbnailsAgent</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.quicklook.ThumbnailsAgent</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>

```
### ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>App.WebUsage</string>
+	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.SensorKit.CHSupportService

> `/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKit.CHSupportService.xpc/com.apple.SensorKit.CHSupportService`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.CognitiveHealth</string>
+	</array>
+</dict>
+</plist>
 

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.speech.localspeechrecognition</string>
+	<key>com.apple.generativeexperiences.textcomposition</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.EmbeddedSpeech</string>

 	<array>
 		<string>kTCCServiceSpeechRecognition</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.sage.textcomposition</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/MobileAsset/</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/PersonalDeviceVolumes/</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/ASRAssetOverrides/</string>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.FileCoordination</string>
+		<string> com.apple.generativeexperiences.textcomposition</string>
+		<string>com.apple.sage.textcomposition</string>
+		<string>com.apple.uservault</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>adi-client</key>
 	<string>409835401</string>
 	<key>application-identifier</key>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>StoreKitMessages</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.kvs.ignore-quota</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```

### 🆕 get-network-info

> `/System/Library/Frameworks/SystemConfiguration.framework/get-network-info`

- No entitlements *(yet)*

### 🆕 HIDRMServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/HIDRMServiceFilter.plugin/HIDRMServiceFilter`

- No entitlements *(yet)*

### 🆕 HIDRMSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/HIDRMSessionFilter.plugin/HIDRMSessionFilter`

- No entitlements *(yet)*

### 🆕 LocationHarvest

> `/System/Library/LocationBundles/LocationHarvest.bundle/LocationHarvest`

- No entitlements *(yet)*

### 🆕 AdAttributionKitDeveloperSettings

> `/System/Library/PreferenceBundles/AdAttributionKitDeveloperSettings.bundle/AdAttributionKitDeveloperSettings`

- No entitlements *(yet)*

### 🆕 PaymentContactlessSettingsUIPlugin

> `/System/Library/PreferenceBundles/PaymentContactlessSettingsUIPlugin.bundle/PaymentContactlessSettingsUIPlugin`

- No entitlements *(yet)*

### 🆕 TetsuoNotifications

> `/System/Library/PreferenceBundles/TetsuoNotifications.bundle/TetsuoNotifications`

- No entitlements *(yet)*

### 🆕 VisionCompanionSettings

> `/System/Library/PreferenceBundles/VisionCompanionSettings.bundle/VisionCompanionSettings`

- No entitlements *(yet)*
### abm-helper

> `/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper`

```diff

 <dict>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.driver.AppleBasebandPCI.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleBasebandPCIControl.user-access</key>

```
### motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

```diff

 	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
+	<key>com.apple.private.avfoundation.capture.camera-stolen-interruptor.allow</key>
+	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
 	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>

```
### com.apple.accounts.dom

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/XPCServices/com.apple.accounts.dom.xpc/com.apple.accounts.dom`

```diff

 	<string>AAACCOUNTS.com.apple.accounts.dom</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 	<array>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.moments</string>
+		<string>group.com.apple.freeform</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### activitysharingd

> `/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 			<string>com.apple.Fitness</string>
 		</dict>
 	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

```
### AppStoreEventServiceExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/AppStoreEventServiceExtension.appex/AppStoreEventServiceExtension`

```diff

 <dict>
 	<key>com.apple.appstored-services.event</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ap.promotedcontent.metrics</string>
+	</array>
 </dict>
 </plist>
 

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.developer.pass-type-identifiers</key>
 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>

 	<true/>
 	<key>com.apple.private.appinstallationmetrics</key>
 	<true/>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.cfnetwork.har-capture-amp</key>
 	<true/>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
+	<key>com.apple.private.cloudkit.systemService</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

 	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>appstored</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.storekit</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceFaceID</string>
+		<string>kTCCServiceLiverpool</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.AppStore</string>
 		<string>com.apple.Preferences</string>
+		<string>com.apple.TVAppStore</string>
 	</array>
 	<key>com.apple.remotenotification.preferences</key>
 	<true/>

 		<string>com.apple.idsremoteurlconnectionagent.desktop.auth</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.chronoservices</string>
+		<string>com.apple.cloudd</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.dmd.policy</string>

 		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.storekitd</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.attributionkitd</string>
 		<string>com.apple.amsengagementd</string>
 		<string>com.apple.coremedia</string>
+		<string>com.apple.CloudKit</string>
 		<string>com.apple.registration</string>
 		<string>com.apple.backgroundassets</string>
 		<string>com.apple.gamecenter</string>

 	</array>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>appstored</string>
-	</array>
 </dict>
 </plist>
 

```
### AAUIFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension`

```diff

 	<string>2036825899</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.appleaccount.beneficiary</key>
 	<true/>
 	<key>com.apple.appleaccount.custodian</key>

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
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	<array>
 		<string>monitor</string>
 	</array>
+	<key>com.apple.companion-authentication.store-purchase</key>
+	<true/>
 	<key>com.apple.coreidvd.spi</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
-	<key>com.apple.private.bmk.allow</key>
+	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
 	<key>com.apple.private.cfnetwork.har-capture-amp</key>
 	<true/>

 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.ts</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.AppleMediaServicesUI.engagement.notifications</string>
 		<string>com.apple.AppleMediaServicesUI.engagement.notifications.macOS</string>
 		<string>com.apple.AppStore</string>
+		<string>com.apple.iCloudSettingsNotification</string>
 		<string>com.apple.Music</string>
 		<string>com.apple.tv</string>
 		<string>com.apple.Fitness</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.amsondevicestoraged.xpc</string>
+		<string>com.apple.companiond.xpc</string>
 		<string>com.apple.locationd.registration</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.asd.scoring</string>

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.passd.library</string>
+		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.xpc.amsengagementd</string>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.amsaccountsd</string>
+		<string>com.apple.OnDeviceStorage</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>com_apple_driver_FairPlayIOKitUserClient</string>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.ts</key>
+	<true/>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.amsengagementd.analytics</string>

 	<array>
 		<string>com.apple.AppStore</string>
 		<string>com.apple.Fitness</string>
+		<string>com.apple.iCloudSettingsNotification</string>
 		<string>com.apple.iBooks</string>
 		<string>com.apple.Music</string>
 		<string>com.apple.news</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.engagementd</string>
+		<string>com.apple.OnDeviceStorage</string>
 	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>

```
### apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.gizmoappd.appmanager.allow</key>

```
### ASVAssetThumbnail

> `/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetThumbnail.appex/ASVAssetThumbnail`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.lsd.advertisingidentifiers</string>

```
### ASVAssetViewer

> `/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/ASVAssetViewer.appex/ASVAssetViewer`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>adi-client</key>
 	<string>628765583</string>
 	<key>application-identifier</key>

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.intelligenceflow.uiContext</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

 		<string>SiriPrivateLearningSELFEvent</string>
 		<string>SiriIntentEvents</string>
 		<string>Siri.AppSelection.Music</string>
+		<string>App.Intent</string>
 	</array>
 	<key>com.apple.private.calendar.allow-integrations</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.siri.findmy</string>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.siri.userfeedbacklearning</string>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.siri.findmy</string>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.siri.userfeedbacklearning</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.orchestration.configuration</string>
+		<string>com.apple.intelligenceflow.uiContext</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager</string>
 		<string>com.apple.siri.orchestration.intelligencesession</string>
 		<string>com.apple.facetimemessagestored.service</string>
 		<string>com.apple.NeighborhoodActivityConduitService</string>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.write</string>
 		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.location</key>
 	<true/>
+	<key>com.apple.siri.orchestration.configuration</key>
+	<true/>
 	<key>com.apple.siri.orchestration.intelligencesession</key>
 	<true/>
 	<key>com.apple.siri.pommes_search_xpc_service</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>
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

 		<string>Media.NowPlaying</string>
 		<string>Notification</string>
 		<string>Notification.Usage</string>
+		<string>Photos.Delete</string>
+		<string>Photos.Edit</string>
+		<string>Photos.Engagement</string>
+		<string>Photos.Favorite</string>
+		<string>Photos.Memories.Shared</string>
+		<string>Photos.Memories.Viewed</string>
+		<string>Photos.Picker</string>
+		<string>Photos.Search</string>
+		<string>Photos.Share</string>
 		<string>Siri.Metrics.OnDeviceDigestExperimentMetrics</string>
 		<string>Siri.Metrics.OnDeviceDigestSegmentsCohorts</string>
 		<string>Siri.Metrics.OnDeviceDigestUsageMetrics</string>

 	<true/>
 	<key>com.apple.private.networkserviceproxy</key>
 	<true/>
+	<key>com.apple.private.power.notifications</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.assistant.shared</string>
 		<string>group.com.apple.weather</string>
 	</array>
 	<key>com.apple.private.security.storage.CallHistory</key>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.assistant.shared</string>
 		<string>group.com.apple.weather</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/Library/Audio/Tunings/Generic/Haptics/Patterns/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/MobileIdentityData/Indeterminates.plist</string>
 		<string>/private/var/db/MobileIdentityData/Version.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.availability.internal</string>

 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.misagent</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.MobileTimer.alarmserver</string>

 		<string>com.apple.siri.shared_flow_plugin_service</string>
 		<string>com.apple.siri.siriaudio-helper</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.siri.UnifiedSiriTest.BridgeService</string>
 		<string>com.apple.siri.UnifiedSiriTest.TestingEventService</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>

 		<string>com.apple.assistantd</string>
 		<string>com.apple.WorkflowKit.BackgroundShortcutRunner</string>
 		<string>HeadGestures</string>
+		<string>SiriMessages</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
 	<key>com.apple.appletv.pbs.user-presentation-service-access</key>

 	</array>
 	<key>com.apple.private.authentication-services.internal-authorization-requests</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.managedconfiguration.mdmdservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.AppStoreComponents</string>
+		<string>com.apple.aaa.serverbackoff</string>
+		<string>com.apple.AuthKit.AgeRangeSettingsCache</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.aaa.serverbackoff</string>
+	</array>
 	<key>com.apple.security.ts.ipc-posix-sem</key>
 	<true/>
 	<key>com.apple.security.ts.ipc-posix-shm</key>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>
+		<string>ichat</string>
 		<string>com.apple.akd</string>
 		<string>com.apple.cfnetwork</string>
 		<string>com.apple.akd.pcsauth</string>

```
### MemojiImageRenderService

> `/System/Library/PrivateFrameworks/AvatarUI.framework/XPCServices/MemojiImageRenderService.xpc/MemojiImageRenderService`

```diff

 	<true/>
 	<key>com.apple.backboard.client</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>
 	<true/>
 	<key>com.apple.private.avatar.store</key>

```
### com.apple.BarcodeSupport.Helper

> `/System/Library/PrivateFrameworks/BarcodeSupport.framework/XPCServices/com.apple.BarcodeSupport.Helper.xpc/com.apple.BarcodeSupport.Helper`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.BarcodeScanner.BarcodeSupportHelper</string>
 	<key>com.apple.private.controlcenter.service.moduleidentifiers</key>
 	<array>
 		<string>com.apple.control-center.QRCodeModule</string>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.intelligenceplatform</string>
 		<string>com.apple.suggestions</string>

```
### BreathingDisturbanceAnalyzerDiagnosticExtension

> `/System/Library/PrivateFrameworks/BreathingAlgorithms.framework/PlugIns/BreathingDisturbanceAnalyzerDiagnosticExtension.appex/BreathingDisturbanceAnalyzerDiagnosticExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.BreathingAlgorithms.BDADiagnosticExtension</string>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
-	<key>com.apple.private.healthkit.authorization_bypass</key>
-	<true/>
 	<key>com.apple.private.healthkit.feature-availability.read</key>
 	<array>
 		<string>SleepApneaNotifications</string>
 	</array>
+	<key>com.apple.private.healthkit.read_authorization_bypass</key>
+	<array>
+		<string>HKQuantityTypeIdentifierAppleSleepingBreathingDisturbances</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<string>/private/var/mobile/Library/Logs/HealthAlgorithms/BreathingAlgorithms/</string>
 	<key>com.apple.security.ts.tmpdir</key>

```
### businessservicesd

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd`

```diff

 		<string>spi</string>
 		<string>sim-authentication</string>
 	</array>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.businessservicesd</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Development</string>
 	<key>com.apple.developer.icloud-services</key>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<array>
 		<string>com.apple.private.alloy.widgets</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DuetActivitySchedulerWidgetRefresh</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<dict>
+					<key>Widgets.Refresh</key>
+					<dict>
+						<key>mode</key>
+						<string>read-write</string>
+					</dict>
+					<key>Widgets.Viewed</key>
+					<dict>
+						<key>mode</key>
+						<string>read-only</string>
+					</dict>
+				</dict>
+			</array>
+		</dict>
+		<key>LNActivityProvider</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>App.Intents.Transcript</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.logging.admin</key>

 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```

### 🆕 PrivacyDisclosure

> `/System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/PlugIns/PrivacyDisclosure.appex/PrivacyDisclosure`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### ScreenshotService

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/XPCServices/ScreenshotService.xpc/ScreenshotService`

```diff

 	<string>com.apple.ClassroomKit.ScreenshotService</string>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### com.apple.CloudDocs.MobileDocumentsFileProviderUI

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderUI.appex/com.apple.CloudDocs.MobileDocumentsFileProviderUI`

```diff

 	<array>
 		<string>CloudDocuments</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.fileproviderui.display-inline</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### CloudTelemetryService

> `/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.osanalytics.defaults.allow</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>Library/OSAnalytics/Preferences</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Caches/</string>

```
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.assistant_cdmd</string>
-	<key>com.apple.TapToRadarKit.service-access</key>
-	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 		<string>com.apple.coreservices.quarantine-resolver</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.symptom_diagnostics</string>
-		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>

```
### accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.driver.AppleAuthCP.user-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 	<true/>
 	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
 	<true/>
+	<key>com.apple.private.osanalytics.defaults.allow</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 	<array>
 		<string>Device.ScreenLocked</string>
 		<string>OSAnalytics.CA.HighEngagementDevices</string>
+		<string>Trial.Experiment.NamespaceUpdates</string>
 	</array>
 	<key>com.apple.private.corewifi</key>
 	<true/>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/tmp/com.apple.siri-distributed-evaluation/</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/PersonalDeviceVolumes/</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/ASRAssetOverrides/</string>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<true/>
 	<key>com.apple.datadetectors.source-write.system</key>
 	<true/>
-	<key>com.apple.developer.networking.multipath</key>
-	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.da</string>
 		<string>com.apple.UnifiedAssetFramework</string>

```
### CoreSpeechXPC

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/CoreSpeechXPC.xpc/CoreSpeechXPC`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.corespeech.cat.xpc</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.hid.system.user-access-fast-path</key>
 	<true/>
 	<key>com.apple.homepodaccessorysettings.client</key>
 	<true/>
+	<key>com.apple.intelligenceflow.context</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

 		<string>Siri.SelfTriggerSuppression</string>
 		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
 		<string>Siri.ASR.RequestMetricsRecord</string>
+		<string>Siri.ASR.ContextualReplayRecord</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.corespeech.xpc.remote</key>
 	<true/>
+	<key>com.apple.private.corespeech_launchagent.xpc</key>
+	<true/>
 	<key>com.apple.private.corespeechd.activation</key>
 	<true/>
 	<key>com.apple.private.exclaves.conclave-host</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>App.Intents.IndexedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.Intents.IndexedEnum</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>App.Shortcut.Entity</key>
 				<dict>
 					<key>mode</key>

 	</array>
 	<key>com.apple.private.iokit.darkwake-control</key>
 	<true/>
+	<key>com.apple.private.isolated.audio.coreaudioclient</key>
+	<true/>
+	<key>com.apple.private.isolated.audio.coreaudioclient.shareddsp</key>
+	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.siri.recorded-audio</string>
+	</array>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
 	<key>com.apple.private.siri.activation</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/Library/Audio/Tunings/</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/PersonalDeviceVolumes/</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/ASRAssetOverrides/</string>

 		<string>com.apple.assistant.dictation</string>
 		<string>com.apple.audio.AudioSession</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.assistant.domain.status.service</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceflow.context</string>
+		<string>com.apple.intelligenceflow.querydecoration</string>
 		<string>com.apple.assistant.domain.validation.service</string>
 		<string>com.apple.assistant.domain.system.settings.service</string>
 		<string>com.apple.feedbacklogger</string>

 		<string>756</string>
 		<string>757</string>
 		<string>1701</string>
+		<string>1441</string>
 	</array>
 	<key>com.apple.trial.status.namespace-name.allow</key>
 	<array>

```
### speechmodeltrainingd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<true/>
 	<key>com.apple.private.canmodifyanyuseractivity</key>
 	<true/>
+	<key>com.apple.private.ciphermld.allow</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.CoreSuggestions.PseudoEvents</key>

 	<true/>
 	<key>com.apple.rootless.storage.triald</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.sage.summarization</key>
 	<true/>
 	<key>com.apple.sage.textcomposition</key>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.ciphermld</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.driverkit.communicates-with-drivers</key>
+	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.iokit.powerdxpc</key>
 	<false/>
 	<key>com.apple.private.ckks</key>

 		<string>com.apple.threadradiodeMACDB</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
-	<string>AppleFillmoreUserClient</string>
+	<array>
+		<string>AppleFillmoreUserClient</string>
+		<string>IOUserUserClient</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### DTServiceHub

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
+	<true/>
 	<key>com.apple.frontboard.debugapplications</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.odr.devtools</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
 	<key>com.apple.private.ClipServices.request-install-clips</key>

 	<true/>
 	<key>com.apple.private.dt.instrumentsxpc.allowed</key>
 	<true/>
+	<key>com.apple.private.game-center</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>

 		<string>/private/var/mobile/Containers/Data/Application/</string>
 		<string>/private/var/mobile/Containers/Data/PluginKitPlugin/</string>
 		<string>/private/var/root/Library/Caches/com.apple.DTServiceHub/</string>
+		<string>/private/var/root/Library/Caches/com.apple.hwtrace/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>ApplePMPUserClient</string>
 		<string>ApplePMPv2UserClient</string>
 		<string>AppleHWAccessUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.trustd</string>
 		<string>com.apple.MTLCompilerService</string>
 		<string>com.apple.iconservices</string>
+		<string>com.apple.gamed</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleHWAccessUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
 	</array>
 	<key>com.apple.security.network.server</key>
 	<true/>

```
### com.apple.dt.instruments.dtsecurity

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
+	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.host-exception-port-override</key>
 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleHWAccessUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
 	</array>
 	<key>com.apple.system-task-ports</key>
 	<true/>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.securebackupd.access</key>
 	<true/>
+	<key>com.apple.securesettingsmigration.host</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.stocks</string>

```
### devicecheckd

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
+	<key>com.apple.mobileactivationd.eda</key>
+	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
+	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 	</array>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.PlatformSSO.auth</string>
 		<string>lockdown-identities</string>
 		<string>2bit-identity</string>
 		<string>com.apple.appattest.identities</string>
+		<string>appattest-webauthn</string>
+		<string>appattest-device</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

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
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.coremedia.endpoint.xpc</string>
		<string>com.apple.coremedia.routediscoverer.xpc</string>
		<string>com.apple.coremedia.routingcontext.xpc</string>
		<string>com.apple.airplay.endpoint.xpc</string>
		<string>com.apple.mediaexperience.endpoint.xpc</string>
	</array>
</dict>
</plist>

```

### 🆕 TUDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/TUDiagnosticExtension.appex/TUDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
</dict>
</plist>

```
### diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

 	<key>com.apple.diskimages.creator-uc</key>
 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>1</integer>
+	<integer>2</integer>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.vfs.role-account-openfrom</key>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 	<true/>
 	<key>com.apple.dataaccess.dataaccessd.PersistentPush</key>
 	<string>com.apple.email.maild</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.triald.namespace-management</string>

 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.icloudmailagent.secret.xpc</string>
 		<string>com.apple.businessservicesd</string>
+		<string>com.apple.backboard.hid.services</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 EnergyKitService

> `/System/Library/PrivateFrameworks/EnergyKit.framework/XPCServices/EnergyKitService.xpc/EnergyKitService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.EnergyKitService</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.developer.homekit</key>
	<true/>
	<key>com.apple.energykit.store</key>
	<true/>
	<key>com.apple.homekit.private-spi-access</key>
	<true/>
	<key>com.apple.locationd.authorizeapplications</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.private.homekit</key>
	<true/>
	<key>com.apple.private.homekit.home-location</key>
	<true/>
	<key>com.apple.private.homekit.location</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.security.exception.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Application Support/com.apple.homeenergyd/</string>
		<string>/private/var/mobile/Library/homeenergyd/</string>
		<string>/private/var/mobile/Library/homeenergyd/com.apple.homeenergyd/</string>
		<string>/private/var/mobile/Library/Weather/</string>
		<string>/private/var/mobile/Library/Caches/com.apple.EnergyKitService/</string>
		<string>/private/var/mobile/Library/Caches/com.apple.wpc.energyservices.gridservices/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/com.apple.homeenergyd/</string>
		<string>/Library/Application Support/homeenergyd/</string>
		<string>/Library/Application Support/homeenergyd/com.apple.homeenergyd/</string>
		<string>/Library/homeenergyd/</string>
		<string>/Library/homeenergyd/com.apple.homeenergyd/</string>
		<string>/Library/Caches/com.apple.wpc.homeservices.energyservices/</string>
		<string>/Library/Caches/com.apple.wpc.energyservices.utilityservices/</string>
		<string>/Library/Caches/com.apple.HomeKit.configurations/</string>
		<string>/Library/Caches/com.apple.HomeKit/</string>
		<string>/Library/Caches/com.apple.homeenergyd/</string>
		<string>/Library/HTTPStorages/com.apple.homeenergyd/</string>
		<string>/Library/HTTPStorages/com.apple.EnergyKitService/</string>
		<string>/Library/Caches/com.apple.EnergyKitService/</string>
		<string>/Library/Weather/</string>
		<string>/Library/Caches/com.apple.wpc.energyservices.gridservices/</string>
		<string>/Containers/Data/Application/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.homed.xpc</string>
		<string>com.apple.containermanagerd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.EnergyKit</string>
		<string>com.apple.Home</string>
		<string>com.apple.homeenergyd</string>
		<string>com.apple.wpc.homeservices.energyservices</string>
		<string>com.apple.wpc.energyservices.utilityservices</string>
		<string>com.apple.wpc.energyservices.gridservices</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.EnergyKitService</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### facetimemessagestored

> `/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored`

```diff

 	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled`

```diff

 	<true/>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	</dict>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.managed-settings.apply</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screentime-setup</key>

 		<string>com.apple.ScreenTimeAgent.private</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.identityservicesd.pds</string>
+		<string>com.apple.ManagedSettingsAgent</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### DraftingExtension-iOS

> `/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS`

```diff

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.feedback</string>

 		<string>com.apple.ist.ds.appleconnect2.service.agent</string>
 		<string>com.apple.ist.ds.service.rlogd</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Feedback.DraftingExtension</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 </dict>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.corefollowup</key>
 	<true/>
+	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
+	<true/>
 	<key>com.apple.intelligenceflow.context</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.modelmanager.query</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	</array>
 	<key>com.apple.private.assistant.settings</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>GenerativeExperiences.FailureTracking</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

 				<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 			</array>
 		</dict>
+		<key>com.apple.GenerativeFunctions.PeriodicTasks.ReportAvailabilityTask</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Availability</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.GenerativeModelsFoundation.FailureTracking</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>GenerativeExperiences.FailureTracking</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/UnifiedAssetFramework/</string>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.GenerativeFunctions.generativeexperiencesd/</string>
 		<string>/Library/AppleIntelligencePlatform/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.GenerativeFunctions.generativeexperiencesd/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.compute.publisher.service</string>
+		<string>com.apple.biome.compute.publisher.service.user</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.intelligenceflow.context</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.nsurlsessiond</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.generativeexperiences.corefollowup</string>
 		<string>com.apple.appstored.xpc.request</string>
+		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.containermanagerd</string>
 		<string>com.apple.controlcenter.remoteservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.SummarizationKit</string>
 		<string>com.apple.EmojiPreferences</string>
 		<string>com.apple.AppSupport</string>

 		<string>com.apple.CloudSubscriptionFeatures.ticket.cache</string>
 		<string>com.apple.CloudSubscriptionFeatures.cache</string>
 		<string>com.apple.CloudSubscriptionFeatures.gmCache</string>
-		<string>com.apple.icloud.gm</string>
+		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
+		<string>com.apple.CloudSubscriptionFeatures.waitlist</string>
 		<string>com.apple.csf.gm.bypass</string>
+		<string>com.apple.icloud.gm</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.Accessibility</string>
-		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
 		<string>com.apple.applicationaccess</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### geod

> `/System/Library/PrivateFrameworks/GeoServices.framework/geod`

```diff

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/GeoServices.framework/geod</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.geoservices</string>

```

### 🆕 HIDRMUICFUNUIExtension

> `/System/Library/PrivateFrameworks/HIDRMUI.framework/PlugIns/HIDRMUICFUNUIExtension.appex/HIDRMUICFUNUIExtension`

- No entitlements *(yet)*
### HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.hangtracer.collect-logs</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.HangTracer.HangLogsDiagnosticExtension</string>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.InFocus</string>
+	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 		<string>VasUgeSzVyHdB27g2XpN0g</string>
 		<string>iyfxmLogGVIaH7aEgqwcIA</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.hearing</string>
+		<string>com.apple.private.alloy.accessibility.switchcontrol</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
 		<string>com.apple.private.alloy.hearing</string>
+		<string>com.apple.private.alloy.accessibility.switchcontrol</string>
 	</array>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>

```
### homeenergyd

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

 		<string>/Library/homeenergyd/com.apple.homeenergyd/</string>
 		<string>/Library/Caches/com.apple.wpc.homeservices.energyservices/</string>
 		<string>/Library/Caches/com.apple.wpc.energyservices.utilityservices/</string>
+		<string>/Library/Caches/com.apple.wpc.energyservices.gridservices/</string>
 		<string>/Library/Caches/com.apple.HomeKit.configurations/</string>
 		<string>/Library/Caches/com.apple.HomeKit/</string>
 		<string>/Library/Caches/com.apple.homeenergyd/</string>

 		<string>com.apple.homeenergyd</string>
 		<string>com.apple.wpc.homeservices.energyservices</string>
 		<string>com.apple.wpc.energyservices.utilityservices</string>
+		<string>com.apple.wpc.energyservices.gridservices</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

 	</array>
 	<key>com.apple.private.carkit</key>
 	<true/>
+	<key>com.apple.private.ckks</key>
+	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.securityd.ckks</string>
 		<string>com.apple.srp-mdns-proxy.proxy</string>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.ThreadNetwork.xpc</string>

 		<string>com.apple.wifi.manager-access</string>
 		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.seserviced</string>
 		<string>com.apple.SetStoreUpdateService</string>
+		<string>com.apple.linkd.autoShortcut</string>
+		<string>com.apple.mobileactivationd</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.MobileStoreDemo.test</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>HomeKit</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### iapd

> `/System/Library/PrivateFrameworks/IAP.framework/Support/iapd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>

```
### identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app</string>
 	</dict>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
 	<key>com.apple.private.cloudkit.buddyAccess</key>
 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

 	</dict>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.cloudtelemetry</key>
+	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
 	<key>com.apple.private.dark-wake-push</key>

 	<true/>
 	<key>com.apple.private.imcore.imtransferservice</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DuetActivitySchedulerPairedSystemContext</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>

 		<string>com.apple.StatusKit.publish</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.biomesyncd.sync</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### IDSBlastDoorService

> `/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<false/>
 	<key>com.apple.coregraphics.disableinmemoryfonts</key>
 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.imageio.allowabletypes</key>
 	<array/>
 	<key>com.apple.pac.shared_region_id</key>

 	<array/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>blastdoor-ids</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>blastdoor-ids</string>
-	</array>
 </dict>
 </plist>
 

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.imagent</string>
 	<key>aps-connection-initiate</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+    <key>com.apple.private.CloudSharing.SPI</key>
+    <true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

 		<string>com.apple.madrid.lite</string>
 		<string>com.apple.ess</string>
 		<string>com.apple.private.ac</string>
+		<string>com.apple.private.alloy.biz</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>

 		<string>apple</string>
 		<string>lockdown-identities</string>
 		<string>com.apple.apsd</string>
+		<string>trustkit</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.mobile.installd</string>
-        <string>com.apple.sysdiagnose.service.xpc</string>
+		<string>com.apple.sysdiagnose.service.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>GetSystemAppMigrationStatus</string>
 		<string>WaitForSystemAppMigrationToComplete</string>
 	</array>
-    <key>com.apple.private.sysdiagnose</key>
-    <true/>
-    <key>com.apple.security.exception.process-info</key>
-    <true/>
+	<key>com.apple.private.sysdiagnose</key>
+	<true/>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 </dict>
 </plist>
 

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 	<true/>
 	<key>com.apple.datadetectors.source-read.user</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.developer.usernotifications.communication</key>

```
### IMTranscoderAgent

> `/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.pac.shared_region_id</key>

```
### IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent`

```diff

 	</array>
 	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>
 	<string>YES</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	<true/>
 	<key>com.apple.locationd.place_inference</key>
 	<true/>
+	<key>com.apple.mediaremote.device-info</key>
+	<true/>
+	<key>com.apple.mediaremote.remote-control-discovery</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MorphunData</string>

 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.siri.morphunassetsupdaterd</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.location</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.coremedia.videocodecd.decompressionsession</string>
 		<string>com.apple.coremedia.videocodecd.compressionsession</string>

 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.naturallanguaged</string>
 		<string>com.apple.dmd.policy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.mobilecal</string>
 		<string>com.apple.siri.morphun</string>
 		<string>com.apple.assistant</string>
+		<string>com.apple.mediaremote</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.inference.EntityMatcher.useSensitiveLogging</key>
 	<true/>
+	<key>com.apple.siri.location</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>755</string>

```
### IntelligenceFlowDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics`

```diff

 	<array>
 		<string>Sage.Transcript</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
+		<string>IntelligenceEngine.Interaction.Donation</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>

 			<array>
 				<string>Sage.Transcript</string>
 				<string>IntelligenceFlow.Transcript.Datastream</string>
+				<string>IntelligenceEngine.Interaction.Donation</string>
 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.storage.SiriFeatureStore</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Logs/com.apple.FeatureStore/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
 	<true/>
+	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

 		<string>IntelligenceFlow.ResponseGeneration</string>
 		<string>IntelligenceFlow.Experimentation</string>
 		<string>IntelligenceFlow.IFRequestTelemetry</string>
+		<string>IntelligenceFlow.PlanGenerationTelemetry</string>
 		<string>PostSiriEngagement</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>Siri.Remembers.InteractionHistory</string>

 	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.XPCStoreOptIn</key>

 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
+	<key>com.apple.private.security.storage.Spotlight</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.shazamkit.allow-external-audio-recording</key>

 	<true/>
 	<key>com.apple.private.shazamkit.allow-signature-generation</key>
 	<true/>
+	<key>com.apple.private.suggestions.contacts</key>
+	<true/>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.sharingd</string>
 		<string>com.apple.shortcuts.view-service</string>
+		<string>com.apple.siri.location</string>
 		<string>com.apple.siri.vocabularyupdates</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.speech.localspeechrecognition</string>

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.assistant.backedup</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.siri.location</key>
+	<true/>
 	<key>com.apple.siriknowledged.koa.donate.internal</key>
 	<true/>
 	<key>com.apple.spotlight.entitledattributes</key>

 		<string>1170</string>
 		<string>1180</string>
 		<string>1760</string>
-		<string>1761</string>
+		<string>INTELLIGENCE_FLOW_QUERY_DECORATOR</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### intelligenceplatformd

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd`

```diff

 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.intelligenceplatform.IntelligencePlatformCore.ERMLRuntimePlugin</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
+	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>
 		<string>photos.scene</string>

 		<string>Motion.Activity</string>
 		<string>Location.Semantic</string>
 		<string>UserFocus.ComputedMode</string>
+		<string>IntelligencePlatform.Views.Updated</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Trial/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.siri-distributed-evaluation</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.NPKCompanionAgent.library</string>
 		<string>com.apple.payment.all-access</string>
 		<string>com.apple.passd.library</string>

 		<string>com.apple.AppSupport</string>
 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.parsecd</string>
+		<string>com.apple.siri.morphun</string>
+		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>1161</string>
 		<string>1170</string>
 		<string>1180</string>
+		<string>755</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Autonaming.Messages.AccuracyFedStats</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>Autonaming.Messages.Inferences</key>
 				<dict>
 					<key>mode</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Trial/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
 		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
 		<string>/Media/PhotoData/Caches/GraphService/PhotosGraph/photosgraph.kgdb-shm</string>
 		<string>/Media/PhotoData/Caches/GraphService/PhotosGraph/photosgraph.kgdb-wal</string>

 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.proactive.sports.xpc</string>
 		<string>com.apple.healthd.server</string>

 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.SoftwareUpdate</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.siri.morphun</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>

 		<string>1180</string>
 		<string>1190</string>
 		<string>1191</string>
+		<string>755</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### com.apple.MLKit.MLModelPreview

> `/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLModelPreview.appex/com.apple.MLKit.MLModelPreview`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

```
### com.apple.MLKit.MLPackagePreview

> `/System/Library/PrivateFrameworks/MLKit.framework/PlugIns/com.apple.MLKit.MLPackagePreview.appex/com.apple.MLKit.MLPackagePreview`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

```
### mapspushd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.VehicleLocation</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.Maps</string>
 	<key>com.apple.geoservices.manifestrequesttoken</key>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	</dict>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>
+		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
 		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 	</array>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	</dict>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>
+		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
 		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 	</array>

```
### MediaAnalysisBlastDoorService

> `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.posterboardservices.disallowArchivingAppleArchive</key>
 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>blastdoor-messages</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>
-		<string>blastdoor-hubble</string>
 	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>
-		<string>blastdoor-hubble</string>
-	</array>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>blastdoor-messages</string>
 	</array>
 </dict>
 </plist>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.application-identifier</key>
+	<string>AAPLPHOTOS.com.apple.mstreamd</string>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### MessagesAirlockService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.private.pac.exception</key>

```
### MessagesBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.posterboardservices.disallowArchivingAppleArchive</key>
 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>blastdoor-messages</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>

 	</array>
 	<key>com.apple.private.security.storage.PassKit</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>blastdoor-messages</string>
-	</array>
 </dict>
 </plist>
 

```

### 🆕 migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.migrationd</string>
	<key>com.apple.CallHistory.sync.allow</key>
	<true/>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.appprotectiond.read</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.bluetooth.internal</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.contacts</key>
	<true/>
	<key>com.apple.contacts.keys.pronouns</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.networkrelay.deviceMonitor</key>
	<true/>
	<key>com.apple.networkrelay.devices.read</key>
	<true/>
	<key>com.apple.networkrelay.devices.write</key>
	<true/>
	<key>com.apple.networkrelay.pairing</key>
	<true/>
	<key>com.apple.private.CallHistory.read</key>
	<true/>
	<key>com.apple.private.CallHistory.read-write</key>
	<true/>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.app-migration-host</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.corewifi.bssid</key>
	<true/>
	<key>com.apple.private.corewifi.internal</key>
	<true/>
	<key>com.apple.private.corewifi.keychain</key>
	<true/>
	<key>com.apple.private.imcore.imdpersistence.database-access</key>
	<true/>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.security.storage.AppDataContainers</key>
	<true/>
	<key>com.apple.private.security.storage.CallHistory</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.MessagesMetaData</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceBluetoothAlways</string>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.FileProvider.LocalStorage</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/CallHistoryDB/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleJPEGDriverUserClient</string>
		<string>AGXDeviceUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.installcoordinationd</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.CallHistorySyncHelper</string>
		<string>com.apple.accountsd.accountmanager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.mobilephone.speeddial</string>
	</array>
	<key>com.apple.security.personal-information.addressbook</key>
	<true/>
	<key>com.apple.springboard.osMigrationHomeScreenLayout</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
</dict>
</plist>

```
### accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.apfs.get-crypto-file-info</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Restore</string>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
-	<key>com.apple.private.followup</key>
-	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>AppleIntelligence.Availability</string>
+	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>ModelCatalog.Subscriptions.Decisions</string>
+		<string>GenerativeExperiences.FailureTracking</string>
+	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ModelCatalogSubscriptionEvaluation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Availability</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>ModelCatalog.Subscriptions.Decisions</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>ModelCatalog.Subscriptions.ExplicitRequests</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/UnifiedAssetFramework/</string>

 		<string>com.apple.modelcatalogd</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
 	</array>
 </dict>
 </plist>

```
### medialibraryd

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.medialibraryd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
 	</array>
-	<key>com.apple.siri.koa.donate.internal</key>
-	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>fairplay-client</key>

```
### NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

 	<string>com.apple.NPKCompanionAgent</string>
 	<key>com.apple.seserviced.kmlXpcService</key>
 	<true/>
+	<key>com.apple.seserviced.session.acwg</key>
+	<true/>
 	<key>com.apple.seserviced.session.dck</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```

### 🆕 NetworkInfoDiagnosticExtension

> `/System/Library/PrivateFrameworks/NetworkInfo.framework/PlugIns/NetworkInfoDiagnosticExtension.appex/NetworkInfoDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CompanionLink</key>
	<true/>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.networking.multipath</key>
	<true/>
	<key>com.apple.locationd.activity</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.status</key>
	<true/>
	<key>com.apple.private.network.interface-control</key>
	<true/>
	<key>com.apple.private.network.statistics</key>
	<true/>
	<key>com.apple.private.networkQuality</key>
	<true/>
	<key>com.apple.private.networking.elevated-logging</key>
	<true/>
	<key>com.apple.private.pcapd-local</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/networkinfodiagext/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.pcapd-local</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-write</key>
	<array>
		<string>net.route.verbose</string>
		<string>net.inet6.icmp6.nd6_debug</string>
		<string>net.inet6.ip6.select_srcaddr_debug</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
</dict>
</plist>

```
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### IPSExtension

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/PlugIns/IPSExtension.appex/IPSExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

```

### 🆕 amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.amsondevicestoraged</string>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.amsondevicestoraged</string>
	</array>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.sqlite.sqlite-encryption</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.amsondevicestoraged</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Application Support/CrashReporter/DiagnosticMessagesHistory.plist</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.amsondevicestoraged/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/com.apple.AppleMediaServices/</string>
		<string>/Library/HTTPStorages/com.apple.amsondevicestoraged/</string>
		<string>/Library/HTTPStorages/amsondevicestoraged/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.SBUserNotification</string>
		<string>com.apple.usernotifications.usernotificationservice</string>
	</array>
	<key>com.apple.security.exception.mach-register.global-name</key>
	<array>
		<string>com.apple.chrono.event-service.amsondevicestoraged</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.amsondevicestoraged</string>
		<string>com.apple.AppleMediaServices.notbackedup</string>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.OnDeviceStorage</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.OnDeviceStorage</string>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>

 	<true/>
 	<key>com.apple.private.activitykit.activityAuthorizer</key>
 	<true/>
+	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
+	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<array>
 		<string>Wallet.Transaction</string>
 	</array>
-	<key>com.apple.private.bmk.allow</key>
+	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.seserviced.passd.private.jpki</key>

 	<true/>
 	<key>com.apple.springboard.biometricUnlockSuppression</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

 		<string>com.apple.PassbookUIService</string>
 		<string>com.apple.Passbook.PeerPayment</string>
 		<string>apple</string>
+		<string>com.apple.pay.merchant-tokens</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest.ExtendLifetime</key>
 	<true/>
+	<key>com.apple.CoreRoutine.Visit</key>
+	<true/>
 	<key>com.apple.PersonalizedSensingService</key>
 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>

```

### 🆕 PhotosSearchDiagnostics

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosSearchDiagnostics.appex/PhotosSearchDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PhotoLibraryServices.PhotosSearchDiagnostics</string>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
	</array>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.service.debug</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/PhotoData/internal/searchdiagnostics/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.photoanalysisd</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
</dict>
</plist>

```
### PerfPowerServicesSignpostReader

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
-		<string>GenerativeModels.GenerativeFunctions.SystemInstrumenetation</string>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 	</array>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>

```

### 🆕 PerfPowerTelemetryClientRegistrationService

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/PerfPowerTelemetryClientRegistrationService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.powerlog</string>
	</array>
</dict>
</plist>

```

### 🆕 PromotedContentJetService

> `/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/XPCServices/PromotedContentJetService.xpc/PromotedContentJetService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/JetPackCache/</string>
		<string>/Library/HTTPStorages/com.apple.ap.PromotedContentJetService/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Caches/com.apple.ap.PromotedContentJetService/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.itunesstored</string>
		<string>com.apple.AppleMediaServices</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AdPlatforms</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.ap.PromotedContentJetService</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### RTTNotificationContentExtension

> `/System/Library/PrivateFrameworks/RTTUI.framework/PlugIns/RTTNotificationContentExtension.appex/RTTNotificationContentExtension`

```diff

 	</array>
 	<key>com.apple.backboardd.proximityDetection</key>
 	<true/>
+	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.mobilephone</string>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### ManagedAppsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.remotemanagement.ManagedAppsSubscriber</string>
+	<key>com.apple.devicemanagementclient.managedappsd.appconfig</key>
+	<true/>
 	<key>com.apple.dmd-access</key>
 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>

```

### 🆕 ManagedSettingsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedSettingsSubscriber.xpc/ManagedSettingsSubscriber`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.remotemanagement.ManagedSettingsSubscriber</string>
	<key>com.apple.private.managed-settings.apply</key>
	<true/>
	<key>com.apple.private.remotemanagement.subscriber</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.remotemanagementd.store</string>
		<string>com.apple.RemoteManagementAgent.store</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.remotemanagement.ManagedSettingsSubscriber</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<array>
		<string>com.apple.remotemanagement.ManagedSettingsSubscriber</string>
	</array>
</dict>
</plist>

```
### SoftwareUpdateSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber`

```diff

 		<string>com.apple.softwareupdateservicesd</string>
 		<string>com.apple.remoted</string>
 		<string>com.apple.seeding.client</string>
+		<string>com.apple.tvosupdate</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.softwareupdateservices.client.allowed</key>
 	<true/>
+	<key>com.apple.tvosupdate.client</key>
+	<true/>
 </dict>
 </plist>
 

```
### schooltimed

> `/System/Library/PrivateFrameworks/SchoolTime.framework/Support/schooltimed`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### budd

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/budd`

```diff

 	<true/>
 	<key>com.apple.VideoSubscriberAccount.DeveloperService</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.purplebuddy.launchMigrationSourceUI</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.setInput</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<array>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 SeymourDaemonDiagnosticExtension

> `/System/Library/PrivateFrameworks/SeymourServices.framework/PlugIns/SeymourDaemonDiagnosticExtension.appex/SeymourDaemonDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.Fitness</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/Seymour/seymour_b.sqlite</string>
		<string>/private/var/mobile/Library/Seymour/AirPlayKit/</string>
		<string>/private/var/mobile/Library/Seymour/Blackbeard/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.fitnessplus</string>
	</array>
</dict>
</plist>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.link-extension</string>
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

 	</array>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siriinference-dodml-plugin</key>
 	<true/>
+	<key>com.apple.private.SiriSuggestionsBookkeepingService.xpc</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.SiriInferenceHolidays</string>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>Photos.Engagement</string>
+		<string>Photos.Edit</string>
+		<string>Photos.Search</string>
+		<string>Photos.Favorite</string>
+		<string>Photos.Share</string>
+		<string>Photos.Picker</string>
+		<string>Photos.Delete</string>
+		<string>Photos.Memories.Viewed</string>
+		<string>Photos.Memories.Shared</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>UserFocus.ComputedMode</string>
 		<string>Location.Semantic</string>

 		<string>Siri.Remembers.AssistantSuggestions</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>Siri.Audio.CompanionContext</string>
+		<string>IntelligenceEngine.Interaction.Donation</string>
 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/mobile/Library/DuetExpertCenter/UICaches/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.suggestions</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.springboard.backgroundappservices</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>

 		<string>com.apple.intelligenceflow.context</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.mobilephone.speeddial</string>
 		<string>com.apple.mediaremote</string>
+		<string>com.apple.siri.audio</string>
 		<string>com.apple.siri.homeAutomation</string>
 		<string>com.apple.assistant.backedup</string>
-		<string>com.apple.siri.inference.SiriSignals</string>
 		<string>com.apple.voicetrigger</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

 		<string>com.apple.siri.sirisuggestions</string>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
 		<string>com.apple.siriinferenced.AppOrdering</string>
+		<string>com.apple.siri.inference.SiriSignals</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsBookkeepingService.xpc/SiriSuggestionsBookkeepingService`

```diff

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppIntent</string>

 	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.HomeKit/com.apple.siriinferenced/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sirisuggestions</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.linkd.registry</string>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.settings</string>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

 	<true/>
 	<key>com.apple.siriinferenced</key>
 	<true/>
+	<key>com.apple.sirisuggestions.allow</key>
+	<true/>
+	<key>com.apple.sirisuggestions.application-id</key>
+	<string>com.apple.siri.SuggestionsBookkeepingService</string>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1343</string>
+		<string>755</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

```
### com.apple.SiriTTSService.TrialProxy

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/com.apple.SiriTTSService.TrialProxy`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.coremedia.samplebufferaudiorenderer.xpc</string>
-		<string>com.apple.coremedia.samplebufferrendersynchronizer.xpc</string>
+		<string>com.apple.appleneuralengine</string>
+		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.audio.AudioQueueServer</string>
 		<string>com.apple.audio.AudioSession</string>
+		<string>com.apple.audioanalyticsd</string>
+		<string>com.apple.coremedia.samplebufferaudiorenderer.xpc</string>
+		<string>com.apple.coremedia.samplebufferrendersynchronizer.xpc</string>
+		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>
-		<string>com.apple.audio.AudioComponentRegistrar</string>
+		<string>com.apple.homed.xpc</string>
+		<string>com.apple.homehubd.manage</string>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
-		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.siri.analytics.assistant</string>
-		<string>com.apple.appleneuralengine</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.coremedia.systemcontroller.xpc</string>
-		<string>com.apple.homehubd.manage</string>
-		<string>com.apple.homed.xpc</string>
-		<string>com.apple.audioanalyticsd</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.sirittsd</string>
+		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.triald.namespace-management</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### sociallayerd

> `/System/Library/PrivateFrameworks/SocialLayer.framework/sociallayerd.app/sociallayerd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.imdpersistence.IMDPersistenceAgent-Syndication</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```
### subridged

> `/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/Support/subridged`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.subridged</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<string>/private/var/code_coverage/</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

 	<true/>
 	<key>com.apple.apfs.spec_telemetry</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>TEST_ENTITLEMENT</string>

 		<string>PURGEABLE_ENTITLEMENT</string>
 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.MobileContainerManager.allowed</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.softwareupdateservicesd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### StatusKitAgent

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	</dict>
 	<key>com.apple.private.cloudkit.spi</key>
 	<true/>
+	<key>com.apple.private.ids.firewall</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.status.keysharing</string>

```
### TelephonyBlastDoorService

> `/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/XPCServices/TelephonyBlastDoorService.xpc/TelephonyBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
+	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
+	<false/>
 	<key>com.apple.coregraphics.disableinmemoryfonts</key>
 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.imageio.allowabletypes</key>
+	<array/>
+	<key>com.apple.pac.shared_region_id</key>
+	<string>BlastDoor</string>
+	<key>com.apple.private.coremedia.allowabletypecategories</key>
+	<array/>
+	<key>com.apple.private.pac.exception</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>blastdoor-ids</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.private.security.message-filter</key>
+	<true/>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>

```
### com.apple.FTLivePhotoService

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService`

```diff

 		<string>com.apple.telephonyutilities.callservicesdaemon.usernotificationprovider</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
-		<string>com.apple.telephonyutilities.callservicesdaemon.reportingcontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.businessservicesd.businessmetadata</key>
 	<true/>
+	<key>com.apple.conversation-recording.required-host-entitlement</key>
+	<true/>
 	<key>com.apple.coreaudio.private.HasMicrophoneInjectionAccess</key>
 	<true/>
 	<key>com.apple.coreaudio.private.MicrophoneInjectionCanBypassMicMute</key>

 	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<string>com.apple.facetime</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 		<string>com.apple.FTLivePhotoService</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.audio.hapticd</string>
+		<string>com.apple.accessories.externalaccessory-server</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.ClarityUI</string>
 		<string>com.apple.SOS</string>
 		<string>com.apple.purplebuddy.notbackedup</string>
+		<string>com.apple.preferences.sounds</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### TranslationUIService

> `/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService`

```diff

 	</array>
 	<key>com.apple.private.translation</key>
 	<true/>
+	<key>com.apple.private.translation.uiprovider.host</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

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
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.replicator.replication</string>
 		<string>com.apple.replicatorservices</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```

### 🆕 TVProductPageExtension

> `/System/Library/PrivateFrameworks/VideosUI.framework/PlugIns/TVProductPageExtension.appex/TVProductPageExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1192613791</string>
	<key>adi-client</key>
	<string>409835401</string>
	<key>application-identifier</key>
	<string>com.apple.VideosUI.TVProductPageExtension</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.VideosUI.TVProductPageExtension</string>
	<key>com.apple.asd.client</key>
	<string>9824938448</string>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-access-to-device-list</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.app-tap</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreidvd.spi</key>
	<true/>
	<key>com.apple.coremedia.allow-mpeg4streaming</key>
	<true/>
	<key>com.apple.coremedia.allow-protected-content-playback</key>
	<true/>
	<key>com.apple.coretelephony.Identity.get</key>
	<true/>
	<key>com.apple.developer.associated-domains</key>
	<array/>
	<key>com.apple.developer.group-session</key>
	<true/>
	<key>com.apple.developer.networking.multicast</key>
	<true/>
	<key>com.apple.developer.pass-type-identifiers</key>
	<array>
		<string>*.pass.com.apple.itunes.storecredit</string>
	</array>
	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
	<array>
		<string>com.apple.groupactivities</string>
	</array>
	<key>com.apple.features.all-access</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.itunescloud.in-app-message-service</key>
	<true/>
	<key>com.apple.itunescloudd.private</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.launchservices.receivereferrerrurl</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.passes.add-silently</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.payment.amp-card-enrollment</key>
	<true/>
	<key>com.apple.payment.card-on-file</key>
	<true/>
	<key>com.apple.payment.passbook-secure-ui-service-access</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.userManagedAssets</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Purchase</string>
		<string>IAPHistory</string>
	</array>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.attentionawareness</key>
	<true/>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.cfnetwork.har-capture-amp</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.ids.registration</key>
	<array>
		<string>com.apple.private.alloy.itunes</string>
	</array>
	<key>com.apple.private.ids.remoteurlconnection</key>
	<true/>
	<key>com.apple.private.ids.session</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.in-app-payments</key>
	<true/>
	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>
	<string>*</string>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.tv.sharedcontainer</string>
		<string>group.tvappservices.container</string>
	</array>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.sportskit.client</key>
	<true/>
	<key>com.apple.private.subscriptionservice.internal</key>
	<true/>
	<key>com.apple.private.swc.additional-service-details-consumer</key>
	<true/>
	<key>com.apple.private.swc.system-app</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.tvappservices.container</string>
		<string>group.com.apple.sports</string>
		<string>group.com.apple.tv.sharedcontainer</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Media/Purchases/</string>
		<string>/private/var/mobile/Media/iTunes_Control/</string>
		<string>/private/var/mobile/Media/ManagedPurchases/TVApp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/com.apple.VideoSubscriberAccount/</string>
		<string>/CTestData/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>com_apple_driver_FairPlayIOKitUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.aa.daemon.xpc</string>
		<string>com.apple.itunescloudd.xpc</string>
		<string>com.apple.coreidvd.proofing</string>
		<string>com.apple.AttentionAwareness</string>
		<string>com.apple.adid</string>
		<string>com.apple.amsaccountsd.security</string>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.atvcached</string>
		<string>com.apple.itunescloud.in-app-message-service</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.hsa-authentication-server</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.medialibraryd.xpc</string>
		<string>com.apple.rtcreportingd</string>
		<string>com.apple.watchlistd.xpc</string>
		<string>com.apple.watchlistd.bulletin-server</string>
		<string>com.apple.mediaartworkd.xpc</string>
		<string>com.apple.atc.xpc</string>
		<string>com.apple.atc.xpc.downloadprogress</string>
		<string>com.apple.routined.registration</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.asd.scoring</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.passd.library</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>
		<string>com.apple.sociallayerd</string>
		<string>com.apple.symptom_analytics</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.itunescloud.remote-request-execution-service</string>
		<string>com.apple.sportsd.xpc</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.ITMLKit</string>
		<string>com.apple.TVMLKit</string>
		<string>com.apple.mobileipod</string>
		<string>com.apple.tv</string>
		<string>com.apple.videos</string>
		<string>com.apple.videos-preferences</string>
		<string>com.apple.homesharing</string>
		<string>com.apple.SocialLayer</string>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.VideosUI.TVProductPageExtension</string>
	</array>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.tv.api</key>
	<array>
		<string>iTunes</string>
	</array>
	<key>com.apple.tvmlkit.private</key>
	<true/>
	<key>com.apple.wallet.features.all-access</key>
	<true/>
	<key>com.apple.watchlist.private</key>
	<true/>
	<key>com.apple.watchlist.private.playback-report</key>
	<true/>
	<key>com.apple.watchlistd.post-bulletins</key>
	<true/>
	<key>fairplay-client</key>
	<integer>1974055701</integer>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.VideoSubscriberAccount</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

 	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.imagent.av</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

```
### WalletBlastDoorService

> `/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/XPCServices/WalletBlastDoorService.xpc/WalletBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
+	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
+	<false/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.private.pac.exception</key>

```
### watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

 		<string>ClientRestrictions</string>
 		<string>UserSettings</string>
 	</array>
+	<key>com.apple.mediaremote.now-playing-read-access</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```

### 🆕 WiFiLogConfigDiagnosticExtension_iOS

> `/System/Library/PrivateFrameworks/WiFiLogCapture.framework/PlugIns/WiFiLogConfigDiagnosticExtension_iOS.appex/WiFiLogConfigDiagnosticExtension_iOS`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.wifivelocity</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/Logs/</string>
		<string>/Library/Logs/</string>
		<string>/Library/Preferences/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/Managed Preferences/mobile/</string>
		<string>/private/var/run/com.apple.wifivelocity/</string>
		<string>/private/var/log/com.apple.wifivelocity/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Preferences/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.wifivelocityd</string>
	</array>
</dict>
</plist>

```
### DiagnosticExtension

> `/System/Library/PrivateFrameworks/WiFiVelocity.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### wirelessinsightsd

> `/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.wirelessinsightsd</string>
 	<key>com.apple.CommCenter.StormBreaker</key>
 	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>

 	<array>
 		<string>com.apple.AutoWake.xml</string>
 	</array>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.wirelessinsightsd</string>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
 	<key>com.apple.geoservices.restricted-tiles</key>
 	<array>
 		<string>cellcoverage</string>
 	</array>
+	<key>com.apple.locationd.authorizeapplications</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.slv_configurer</key>
 	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
+	<key>com.apple.locationd.usage_oracle</key>
+	<true/>
+	<key>com.apple.maps.model-access</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>

 	</array>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceLiverpool</string>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/var/mobile/Library/Caches/GeoServices/</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.routined.registration</string>
+		<string>com.apple.duet.expertcenter</string>
+		<string>com.apple.Maps.IPC</string>
+		<string>com.apple.wirelessinsightsd</string>
+		<string>com.apple.Maps.MapsSync.store</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.unrestrictedPersona</key>
	<true/>
	<key>com.apple.private.clouddocs.read-diagnostic-metadata</key>
	<true/>
	<key>com.apple.private.clouddocs.spi</key>
	<array>
		<string>dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:</string>
	</array>
	<key>com.apple.private.pluginkit.persona</key>
	<string>system</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.iCloudDrive</string>
	</array>
	<key>com.apple.private.security.storage.CloudDocsDB</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.iCloudDrive</string>
	</array>
	<key>com.apple.security.enterprise-volume-access</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/CloudDocs/session/db/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/CloudDocs/session/db/</string>
	</array>
</dict>
</plist>

```

### 🆕 bird

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/bird`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>allow-softwareupdated</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.bird</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>aps-environment</key>
	<string>serverPreferred</string>
	<key>com.apple.DiagnosticExtensions.extensionHost</key>
	<true/>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.and.client</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.bird</string>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.developer.aps-environment</key>
	<string>serverPreferred</string>
	<key>com.apple.developer.default-data-protection</key>
	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.fileprovider.migration-import-progress</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboard.shutdown</key>
	<true/>
	<key>com.apple.internal.fileprovider.fpck</key>
	<true/>
	<key>com.apple.internal.fileprovider.sync-root-management</key>
	<true/>
	<key>com.apple.mobile.keybagd.UserManager.sync</key>
	<true/>
	<key>com.apple.multitasking.termination</key>
	<true/>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>PURGE_ENTITLEMENT</string>
		<string>CLIENT_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.aps-connection-initiate</key>
	<true/>
	<key>com.apple.private.clouddocs.bundle-service</key>
	<true/>
	<key>com.apple.private.clouddocs.telemetry-disk-checker</key>
	<true/>
	<key>com.apple.private.cloudkit.accountDetailAccess</key>
	<true/>
	<key>com.apple.private.cloudkit.assetBoundaryKey</key>
	<true/>
	<key>com.apple.private.cloudkit.customAccounts</key>
	<true/>
	<key>com.apple.private.cloudkit.displaysSystemAcceptPrompt</key>
	<true/>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.packages</key>
	<true/>
	<key>com.apple.private.cloudkit.participant-pii</key>
	<true/>
	<key>com.apple.private.cloudkit.protectiondata</key>
	<true/>
	<key>com.apple.private.cloudkit.publishAssets</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<array>
		<string>performModifyWebSharingOperation:withBlock:</string>
		<string>getNewWebSharingIdentity:</string>
	</array>
	<key>com.apple.private.cloudkit.temporary.deviceCapabilities</key>
	<true/>
	<key>com.apple.private.cloudkit.usePublicAPSToken</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.desktopservices.home-folder.set-path</key>
	<true/>
	<key>com.apple.private.desktopservices.icloud-desktop.move-and-merge</key>
	<true/>
	<key>com.apple.private.foundation.fileprovider-any-path</key>
	<true/>
	<key>com.apple.private.foundation.fileprovideridentifier</key>
	<string>com.apple.bird</string>
	<key>com.apple.private.iaaccounts</key>
	<true/>
	<key>com.apple.private.kernel.global-proc-info</key>
	<true/>
	<key>com.apple.private.launchservices.allowopenwithanyhandler</key>
	<true/>
	<key>com.apple.private.librarian.can-reclaim-space</key>
	<true/>
	<key>com.apple.private.mobileinstall.allowedSPI</key>
	<array>
		<string>InstallForLaunchServices</string>
		<string>UninstallForLaunchServices</string>
	</array>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>com.apple.bird</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.CloudDocs</string>
		<string>group.com.apple.iCloudDrive</string>
	</array>
	<key>com.apple.private.security.scoped-bookmark-key</key>
	<true/>
	<key>com.apple.private.security.storage.CloudDocsDB</key>
	<true/>
	<key>com.apple.private.security.storage.CloudKit</key>
	<true/>
	<key>com.apple.private.security.storage.DocumentRevisions</key>
	<true/>
	<key>com.apple.private.security.storage.MobileDocuments</key>
	<true/>
	<key>com.apple.private.security.storage.iCloudDrive</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
		<string>kTCCServiceSystemPolicyDesktopFolder</string>
		<string>kTCCServiceSystemPolicyDocumentsFolder</string>
		<string>kTCCServiceFileProviderDomain</string>
	</array>
	<key>com.apple.private.tcc.manager.access.delete</key>
	<array>
		<string>kTCCServiceUbiquity</string>
	</array>
	<key>com.apple.private.tcc.manager.access.modify</key>
	<array>
		<string>kTCCServiceUbiquity</string>
	</array>
	<key>com.apple.private.tcc.manager.access.read</key>
	<array>
		<string>kTCCServiceAll</string>
	</array>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceUbiquity</string>
		<string>kTCCServiceSystemPolicyAllFiles</string>
	</array>
	<key>com.apple.private.tcc.manager.compute-designated-requirement</key>
	<true/>
	<key>com.apple.private.tcc.override-prompt-policy</key>
	<true/>
	<key>com.apple.private.vfs.authorized-access</key>
	<true/>
	<key>com.apple.private.vfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.vfs.open-by-id</key>
	<true/>
	<key>com.apple.private.vfs.snapshot</key>
	<true/>
	<key>com.apple.private.vfs.snapshot.user</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.CloudDocs</string>
		<string>group.com.apple.iCloudDrive</string>
	</array>
	<key>com.apple.security.enterprise-volume-access</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.shortcutitems.fullaccess</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>255</string>
	</array>
	<key>com.apple.usermanagerd.persona.fetch</key>
	<true/>
</dict>
</plist>

```
### ind

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/ind`

```diff

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.iCloud.FollowUp</string>
+		<string>com.apple.iCloudSettingsNotification</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 iCloudSettingsNotificationContentExtension

> `/System/Library/PrivateFrameworks/iCloudSettings.framework/PlugIns/iCloudSettingsNotificationContentExtension.appex/iCloudSettingsNotificationContentExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/UserNotifications/</string>
	</array>
</dict>
</plist>

```

### 🆕 AppInstallation

> `/System/Library/Settings/DefaultApps/AppInstallation.plugin/AppInstallation`

- No entitlements *(yet)*

### 🆕 CallFiltering

> `/System/Library/Settings/DefaultApps/CallFiltering.plugin/CallFiltering`

- No entitlements *(yet)*

### 🆕 ContactlessPayment

> `/System/Library/Settings/DefaultApps/ContactlessPayment.plugin/ContactlessPayment`

- No entitlements *(yet)*

### 🆕 DefaultAppsPasswordManagerSettings

> `/System/Library/Settings/DefaultApps/DefaultAppsPasswordManagerSettings.plugin/DefaultAppsPasswordManagerSettings`

- No entitlements *(yet)*

### 🆕 DefaultContactlessAppSettingsUIPlugin

> `/System/Library/Settings/DefaultApps/DefaultContactlessAppSettingsUIPlugin.plugin/DefaultContactlessAppSettingsUIPlugin`

- No entitlements *(yet)*

### 🆕 Keyboards

> `/System/Library/Settings/DefaultApps/Keyboards.plugin/Keyboards`

- No entitlements *(yet)*
### kbd

> `/System/Library/TextInput/kbd`

```diff

 	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assertiond.applicationstateconnection</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 		<string>com.apple.email.maild</string>
 		<string>com.apple.userprofiles</string>
 		<string>com.apple.uservault</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 CPUTrace

> `/System/Library/Trace/Providers/CPUTrace.bundle/CPUTrace`

- No entitlements *(yet)*

### 🆕 com.apple.iCloudSettingsNotification

> `/System/Library/UserNotifications/Bundles/com.apple.iCloudSettingsNotification.bundle/com.apple.iCloudSettingsNotification`

- No entitlements *(yet)*
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.ap.promotedcontent.identifiermanager</string>
+		<string>com.apple.absd</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>adi-client</key>
 	<string>409835401</string>
 	<key>application-identifier</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.visioncompaniond</string>
 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.AttentionAwareness</string>

 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.absd</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.tvmlkit.private</key>
 	<true/>
+	<key>com.apple.visioncompaniond.client</key>
+	<true/>
 	<key>com.apple.watchlist.private</key>
 	<true/>
 	<key>com.apple.watchlist.private.playback-report</key>

```

### 🆕 AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.BluetoothServices.cloud</key>
	<true/>
	<key>com.apple.BluetoothServices</key>
	<true/>
	<key>adi-client</key>
	<string>143531244</string>
	<key>application-identifier</key>
	<string>com.apple.visionproapp</string>
	<key>aps-environment</key>
	<string>development</string>
	<key>com.apple.authkit.client</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.spatialshowcase.userdata</string>
		<string>com.apple.tdg-wb</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstorecomponents.media-client-id</key>
	<string>com.apple.visionproapp</string>
	<key>com.apple.private.appstorecomponents.media-client-version</key>
	<string>1</string>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.spatialshowcase.userdata</key>
		<string>com.apple.spatialshowcase.userdata</string>
		<key>com.apple.tdg-wb</key>
		<string>com.apple.tdg-wb</string>
	</dict>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.fairplay.FPDI</key>
	<dict>
		<key>capabilities</key>
		<array>
			<integer>4014732562</integer>
		</array>
		<key>client-identifier</key>
		<string>amstool</string>
	</dict>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.metadata.private</key>
	<true/>
	<key>com.apple.private.healthkit.read_authorization_bypass</key>
	<array>
		<string>HKVisionPrescriptionTypeIdentifier</string>
	</array>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.storekit</key>
	<array>
		<string>RemoteDownloadIdentifiers</string>
		<string>Articles</string>
	</array>
	<key>com.apple.private.tvAppExtension</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.countryd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.BluetoothCloudServices</string>
		<string>com.apple.visioncompaniond</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.visioncompaniond</string>
		<string>com.apple.visionproapp.notifications</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.visioncompaniond.client</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>com.apple.itunesstored.private</key>
	<true/>
</dict>
</plist>

```
### BooksThumbnail

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksThumbnail.appex/BooksThumbnail`

```diff

 	<string>com.apple.iBooks.BooksThumbnail</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.iBooks.BooksThumbnail</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.CoreTelephony.DataUsageInfo.allow</key>
 	<true/>
+	<key>com.apple.Diagnostics.host-view-service</key>
+	<true/>
 	<key>com.apple.NPKCompanionAgent.client</key>
 	<true/>
 	<key>com.apple.PassKit.issuer-provisioning.consumer</key>

 	<array>
 		<string>com.apple.ams-identity-verification</string>
 	</array>
+	<key>com.apple.coreidvd.identity-proofing</key>
+	<true/>
 	<key>com.apple.coreidvd.identity-proofing-ui</key>
 	<true/>
 	<key>com.apple.coreidvd.report-a-concern</key>

 	<true/>
 	<key>com.apple.energykit.spi</key>
 	<true/>
+	<key>com.apple.finance.private</key>
+	<true/>
 	<key>com.apple.findmylocaldevice-playsounds</key>
 	<true/>
 	<key>com.apple.fitcore</key>

 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceFaceID</string>
+		<string>kTCCServiceWillow</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.coreidvd.identity-proofing.xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.passd.sharing-channel</string>
 		<string>com.apple.passd.device-registration</string>

 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.softposreaderd</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.financed.service.coredatastore</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.RemoteDisplay</key>
 	<true/>
-	<key>com.apple.UIKit.vends-view-services</key>
-	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.nfcd.assertion.handover</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.modelmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.LockedContentServices.allowWarmLaunch</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>

 	<true/>
 	<key>com.apple.RemoteDisplay</key>
 	<true/>
-	<key>com.apple.UIKit.vends-view-services</key>
-	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.nfcd.assertion.handover</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.cache_delete</string>
 		<string>com.apple.spotlight.IndexDelegateAgent</string>
+		<string>com.apple.modelmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<array>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.suggestions</string>
+		<string>com.apple.conference</string>
 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.communicationSafetySettings</string>
 	</array>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<dict>
 		<key>appData</key>
 		<true/>
+		<key>appGroup</key>
+		<array>
+			<string>group.com.apple.FileProvider.DomainCaching</string>
+		</array>
 	</dict>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>

```
### FindMyNotificationsService

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>

```
### FindMyWidgetItems

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems`

```diff

 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
 		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
+		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyuseragent.beaconmanager.simplebeacon</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### FindMyWidgetPeople

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople`

```diff

 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
 		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
+		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyuseragent.beaconmanager.simplebeacon</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.weather</string>
+		<string>group.com.apple.Fitness</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```

### 🆕 FitnessDiagnosticExtension

> `/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessDiagnosticExtension.appex/FitnessDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.Fitness</string>
	</array>
</dict>
</plist>

```
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.handwritingd.allowBackgroundRecognition</key>
+	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>0000000000.com.apple.Health</string>
 	<key>com.apple.appstored.install-apps</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.avfaudio.devicetest</key>

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.recoverykey</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.set</key>
+	<array>
+		<string>Passcode</string>
+	</array>
 	<key>com.apple.media.ringtones.read-only</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry</key>

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>UniqueDeviceID</string>
 		<string>VasUgeSzVyHdB27g2XpN0g</string>
 		<string>re6Zb+zwFKJNlkQTUeT+/w</string>
 		<string>hiHut/WR+B9Lx/vd0WyeNg</string>

 	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
+	<key>com.apple.private.hsa-authentication-processing</key>
+	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.Health</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.developer.homekit.background-mode</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	</array>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
+		<key>com.apple.homekit.camera.clips</key>
+		<string>com.apple.homekit</string>
 		<key>com.apple.homekit.events</key>
 		<string>com.apple.homekit</string>
 	</dict>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 	<string>com.apple.GenerativePlaygroundAppIntents</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GenerativePlaygroundAppIntents</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>

 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.Photos</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
+	<key>com.apple.generativeexperiences.summarization</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
-	<key>com.apple.private.appintents.attribution-override</key>
-	<true/>
-	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.GenerativePlaygroundApp</string>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
-	<dict>
-		<key>type</key>
-		<string>bundleID</string>
-		<key>value</key>
-		<string>com.apple.GenerativePlaygroundApp</string>
-	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-dispatch.internal</key>
+	<true/>
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

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.library</key>
+	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tcc.allow-prompting</key>
-	<array>
-		<string>kTCCServiceCamera</string>
-	</array>
+	<key>com.apple.sage.summarization</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/MobileAsset/AssetsV2/</string>
-		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
-		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
+		<string>/System/Library/PreinstalledAssetsV2/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.sage.summarization</string>
 		<string>com.apple.generativeexperiences.summarization</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.duetactivityscheduler</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.gms.availability</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
+	</array>
+	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
+	<array>
+		<string>AppleNVMeEANUC</string>
+	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.assistant.cdm</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.photos.service</string>
+		<string>com.apple.mediaanalysisd.service.public</string>
+		<string>com.apple.sage.summarization</string>
+		<string>com.apple.generativeexperiences.summarization</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>com.apple.gms.availability</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp</string>
+	<key>com.apple.VE.CVCalibration.client</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp</string>
 	<key>com.apple.appprotectiond.guard.access</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.arkit.authorization</key>
+	<array>
+		<string>worldTracking</string>
+	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
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

 	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
+	<key>com.apple.private.security.arkit</key>
+	<array>
+		<string>allowImmersiveExemption</string>
+		<string>allowBackgroundPoseData</string>
+	</array>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.realitysimulation.apps</string>
+		<string>com.apple.ve.cvcalibrationd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.gms.availability</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>

 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### GenerativePlaygroundMessagesAppExtension

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp.remoteUIExtension</string>
+	<key>com.apple.VE.CVCalibration.client</key>
+	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.arkit.authorization</key>
+	<array>
+		<string>worldTracking</string>
+	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

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

 	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
+	<key>com.apple.private.security.arkit</key>
+	<array>
+		<string>allowImmersiveExemption</string>
+		<string>allowBackgroundPoseData</string>
+	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceCamera</string>
 	</array>
 	<key>com.apple.private.tcc.allow-prompting</key>
 	<array>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.realitysimulation.apps</string>
+		<string>com.apple.ve.cvcalibrationd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
-	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
-	<array>
-		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
-		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
-		<string>/private/var/db/os_eligibility/eligibility.plist</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
-		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
-	</array>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.developer.extension-host.widget-extension</key>
 	<true/>
+	<key>com.apple.developer.navigation-app</key>
+	<true/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.duet.expertcenter.consumer</key>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.textcomposition</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 	</array>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>

 		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.proactive.PersonalizationPortrait.Contact</string>
 		<string>com.apple.icloudmailagent.secret.xpc</string>
+		<string>com.apple.backboard.hid.services</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

 	<array>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.parsecd</string>
+		<string>com.apple.gms.availability</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### MailNotificationContentExtension

> `/private/var/staged_system_apps/MobileMail.app/PlugIns/MailNotificationContentExtension.appex/MailNotificationContentExtension`

```diff

 	<string>com.apple.mobilemail.MailNotificationContentExtension</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.businessservicesd.businessmetadata</key>
+	<true/>
+	<key>com.apple.icloudmailagent.secret.xpc</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>

 	<array>
 		<string>group.com.apple.mail</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Caches/com.apple.businessservicesd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.email.maild</string>
+		<string>com.apple.icloudmailagent.secret.xpc</string>
+		<string>com.apple.businessservicesd</string>
 	</array>
 </dict>
 </plist>

```
### MailQuickLookExtension

> `/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension`

```diff

 	<string>com.apple.mobilemail.MailQuickLookExtension</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
 	<key>com.apple.private.networkserviceproxy</key>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 		<string>com.apple.reminders</string>
 		<string>com.apple.mobileslideshow</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<string>Notes</string>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.sessionkit.custom-platter-target</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.private.shortcuts.IntentsAvailableDuringBuddy</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mobilenotes</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### com.apple.mobilenotes.QuickLookExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.QuickLookExtension.appex/com.apple.mobilenotes.QuickLookExtension`

```diff

 	<string>com.apple.mobilenotes.QuickLookExtension</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<string></string>
 	<key>com.apple.NanoTimeKit.userphotofaceclient</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.ProactiveSummarization.feedback</key>
 	<true/>
 	<key>com.apple.ProactiveSummarization.model-input</key>

 	<array/>
 	<key>com.apple.developer.carplay-communication</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>

 		<string>CommunicationSafetyResultWithoutImage</string>
 		<string>Discoverability.Signals</string>
 		<string>Discoverability.Usage</string>
+		<string>Messages.Search.Event</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MessagesAssistantExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension`

```diff

 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.commcenter.coretelephony.xpc</string>
+		<string>com.apple.commcenter.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>
 	<true/>
 	<key>com.apple.geoservices.map-subscriptions.check-existence</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.tipsnext</string>
+		<string>group.com.apple.sports</string>
 		<string>group.com.apple.safari</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>

 	<array>
 		<string>/private/var/db/MobileIdentityData/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/Applications/</string>
 		<string>/private/var/db/os_eligibility/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_SafariBrowsingAssistant/purpose_auto/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.webprivacyd</string>
 		<string>com.apple.trial.status</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.BrowserEngineKit.Intermediary</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.datadetectors</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.UnifiedAssetFramework</string>

 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.newscore</string>
 		<string>com.apple.suggestions</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.Passwords</string>
 	</array>
 	<key>com.apple.security.system-groups</key>

```
### com.apple.mobilesafari.SafariDiagnosticExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SafariBookmarksSyncAgent</string>
+		<string>com.apple.Safari.History.Service</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 <dict>
 	<key>CARCapableApp</key>
 	<true/>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>SBStarkCapable</key>
 	<true/>
 	<key>adi-client</key>

 		<string>com.apple.surfboard.scenesessionservice</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.backlightd</string>
+		<string>com.apple.absd</string>
+		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.timed.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.MusicKit</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.SocialLayer</string>

 	<true/>
 	<key>com.apple.telephony.cupolicy-rw-access</key>
 	<true/>
+	<key>com.apple.timed</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>MUSIC_PLAYBACK_PERFORMANCE_STEREO_HLS</string>

```
### MediaPicker

> `/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker`

```diff

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.itunescloud.media-app-banner-service</string>
 		<string>com.apple.itunescloud.remote-request-execution-service</string>
+		<string>com.apple.absd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### MusicMessagesApp

> `/private/var/staged_system_apps/Music.app/PlugIns/MusicMessagesApp.appex/MusicMessagesApp`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
-		<string></string>
 		<string>/System/Library/PrivateFrameworks/NewsArticles.framework/</string>
 		<string>/System/Library/PrivateFrameworks/NewsUI2.framework/</string>
+		<string>/System/Library/PrivateFrameworks/CookingSupport.framework</string>
+	</array>
+	<key>com.apple.private.appintents-bundle-relative-paths</key>
+	<array>
+		<string>Frameworks/NewsArticles.framework/</string>
+		<string>Frameworks/NewsUI2.framework/</string>
+		<string>Frameworks/CookingSupport.framework</string>
 	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>

 	</dict>
 	<key>com.apple.private.mobileinstall.upgrade-enabled</key>
 	<true/>
+	<key>com.apple.private.mobiletimerd</key>
+	<true/>
 	<key>com.apple.private.networkextension.configuration</key>
 	<true/>
 	<key>com.apple.private.safari.can-use-launch-agent</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.news.ScoringService</string>
+		<string>com.apple.MobileTimer.timerserver</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### NewsNotificationServiceExtension

> `/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### NewsTag

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag`

```diff

 	</array>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### NewsToday2

> `/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2`

```diff

 	</array>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.news</string>
+		<string>group.com.apple.newsd</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### NewsTodayIntents

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTodayIntents.appex/NewsTodayIntents`

```diff

 	</array>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<array>
 		<string>Wallet.Transaction</string>
 	</array>
-	<key>com.apple.private.bmk.allow</key>
+	<key>com.apple.private.biometrickit.allow-connect</key>
+	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
 	<key>com.apple.private.carkit.headUnitPairingPrompt</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.seserviced.passd.private.jpki</key>
+	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

 		<string>com.apple.FinanceKit</string>
 		<string>com.apple.Sharing</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>H11ANEInDirectPathClient</string>

 	<true/>
 	<key>com.apple.springboard.allowallcallurls</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.keychain</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-dispatch.internal</key>
+	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.internal.resource</key>
 	<true/>
+	<key>com.apple.private.photos.service.librarymanagement</key>
+	<true/>
 	<key>com.apple.private.photos.service.multilibrary</key>
 	<true/>
 	<key>com.apple.private.photos.service.notification</key>

```
### PodcastsWidget

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.podcasts</string>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>243LU875E5.groups.com.apple.podcasts</string>

 	<array>
 		<string>243LU875E5.groups.com.apple.podcasts</string>
 	</array>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 </dict>
 </plist>
 

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 		<string>com.apple.timesync.expositor</string>
 		<string>com.apple.timesync.manager</string>
 		<string>com.apple.timesync.ptp.manager</string>
-		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.passd.library</string>

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.absd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.chrono.avocadocontrollerconnection</string>
 		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.xpc.amsengagementd</string>
-		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>

 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.iTunes</string>
 	</array>
-	<key>com.apple.siri.koa.donate.internal</key>
-	<true/>
 	<key>com.apple.springboard.activateassistant</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### QuickLookExtension

> `/private/var/staged_system_apps/Shortcuts.app/PlugIns/QuickLookExtension.appex/QuickLookExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.shortcuts.QuickLookExtension</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### ThumbnailExtension

> `/private/var/staged_system_apps/Shortcuts.app/PlugIns/ThumbnailExtension.appex/ThumbnailExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.shortcuts.ThumbnailExtension</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
-	<key>com.apple.sharesheet.allow-custom-view</key>
-	<true/>
 	<key>com.apple.sharing.Client</key>
 	<true/>
 	<key>com.apple.shortcuts.background-running</key>

```
### StocksWidget

> `/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget`

```diff

 	<string>com.apple.stocks</string>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	<array>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.stocks-news</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### Stocks

> `/private/var/staged_system_apps/Stocks.app/Stocks`

```diff

 	<array>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.stocks-news</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### VoiceMemosIntentsExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.place_inference</key>

 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<string>/private/var/mobile/Media/Recordings/</string>
 		<string>/private/var/mobile/Library/Recordings/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/AppAnalytics/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### VoiceMemosShareExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.place_inference</key>

 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<string>/private/var/mobile/Media/Recordings/</string>
 		<string>/private/var/mobile/Library/Recordings/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/AppAnalytics/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### VoiceMemos

> `/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.place_inference</key>

 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<string>/private/var/mobile/Media/Recordings/</string>
 		<string>/private/var/mobile/Library/Recordings/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/AppAnalytics/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### WeatherAppIntents

> `/private/var/staged_system_apps/Weather.app/Extensions/WeatherAppIntents.appex/WeatherAppIntents`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.weather</string>
+	<key>com.apple.CoreRoutine.LocationOfInterest</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.chronoservices</string>
+		<string>com.apple.routined.registration</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Weather

> `/private/var/staged_system_apps/Weather.app/Weather`

```diff

 		<string>com.apple.weatherd.weatherkit</string>
 		<string>com.apple.weatherd.notifications</string>
 		<string>com.apple.weatherkit.authservice</string>
+		<string>com.apple.weatherd.summary-strings</string>
 		<string>com.apple.ap.promotedcontent.pcinterface</string>
 		<string>com.apple.ap.promotedcontent.mescalinterface</string>
 		<string>com.apple.ap.promotedcontent.metrics</string>

```

### 🆕 ifconfig

> `/sbin/ifconfig`

- No entitlements *(yet)*
### launchd

> `/sbin/launchd`

```diff

 <dict>
 	<key>com.apple.apfs.get-dev-by-role</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.private.amfi.can-allow-non-platform</key>
 	<true/>
+	<key>com.apple.private.delegate-signals</key>
+	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>
 	<true/>
 	<key>com.apple.private.kernel.darkboot</key>

```

### 🆕 route

> `/sbin/route`

- No entitlements *(yet)*
### csfdiagnose

> `/usr/bin/csfdiagnose`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

 	<true/>
 	<key>com.apple.private.vfs.snapshot</key>
 	<true/>
+	<key>com.apple.private.vfs.support-long-paths</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/</string>

```
### modelcatalogdump

> `/usr/bin/modelcatalogdump`

```diff

 	<string>com.apple.modelcatalogtool</string>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
+	<key>com.apple.modelcatalog.subscriptions</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>AppleIntelligence.Availability</string>
+		<string>ModelCatalog.Subscriptions.ExplicitRequests</string>
+	</array>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.modelcatalogtool</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ModelCatalogSubscriptionEvaluation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Availability</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>ModelCatalog.Subscriptions.ExplicitRequests</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/mobile/Library/UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.modelcatalog.subscriptions</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.compute.source.user</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### modelmanagerdump

> `/usr/bin/modelmanagerdump`

```diff

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOReportUserClient</string>
+		<string>AGXDeviceUserClient</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.debug</key>

```

### 🆕 libramrod.dylib

> `/usr/lib/libramrod.dylib`

- No entitlements *(yet)*
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.nfcd.session.reader.internal</key>
 	<true/>
+	<key>com.apple.private.AuthenticationServicesAgent</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>

 		<string>com.apple.cfnetwork</string>
 		<string>com.apple.webkit.webauthn</string>
 		<string>com.apple.password-manager</string>
+		<string>com.apple.cfnetwork.testing</string>
+		<string>com.apple.webkit.webauthn.testing</string>
+		<string>com.apple.password-manager.testing</string>
 		<string>com.apple.password-manager.personal</string>
+		<string>com.apple.password-manager.personal.testing</string>
 		<string>com.apple.cfnetwork-recently-deleted</string>
+		<string>com.apple.cfnetwork-recently-deleted.testing</string>
 		<string>com.apple.password-manager-recently-deleted</string>
+		<string>com.apple.password-manager-recently-deleted.testing</string>
 		<string>com.apple.webkit.webauthn-recently-deleted</string>
+		<string>com.apple.webkit.webauthn-recently-deleted.testing</string>
 		<string>com.apple.password-manager.personal-recently-deleted</string>
+		<string>com.apple.password-manager.personal-recently-deleted.testing</string>
 		<string>com.apple.managed.passkey.attestation</string>
+		<string>com.apple.managed.passkey.attestation.testing</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### DumpPanic

> `/usr/libexec/DumpPanic`

```diff

 	</array>
 	<key>com.apple.private.coredump-encryption-key</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.DumpPanic</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>PanicPatternMatching</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Diagnostics.Panic</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>
 	<key>com.apple.private.security.disk-device-access</key>

 	<true/>
 	<key>com.apple.rootless.volume.VM</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>AppleNVMeNamespaceUC</string>
 	<key>com.apple.security.system-groups</key>

```
### MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

 	<true/>
 	<key>com.apple.private.apfs.allocate_contig</key>
 	<true/>
+	<key>com.apple.private.apfs.get-graft-info</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.apfs.trim-active-file</key>
 	<true/>
 	<key>com.apple.private.oop-jit.dir-manager</key>
 	<true/>
+	<key>com.apple.private.security.bootpolicy</key>
+	<true/>
 	<key>com.apple.private.security.disk-device-access</key>
 	<true/>
+	<key>com.apple.private.vfs.exclave-fs-register</key>
+	<true/>
+	<key>com.apple.private.vfs.graftdmg</key>
+	<true/>
 	<key>com.apple.private.vfs.snapshot</key>
 	<true/>
 	<key>com.apple.rootless.install</key>

```
### MobileStorageMounter

> `/usr/libexec/MobileStorageMounter`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileStorageMounter</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.job-manager</key>
+	<string>com.apple.mobile.storage_mounter</string>
 	<key>com.apple.private.xpc.launchd.storage-mounter</key>
 	<true/>
 	<key>com.apple.rootless.storage.MobileStorageMounter</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.debug</key>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.kernel.get-kext-info</key>
+	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/TrustedHostAttached</string>

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>application-identifier</key>
 	<string>com.apple.iad-cloudkit</string>
 	<key>aps-connection-initiate</key>

```
### amfid

> `/usr/libexec/amfid`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.managedconfiguration.feature-setting.trustedCodeSigningIdentities</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.BackgroundUI</key>

```
### announced

> `/usr/libexec/announced`

```diff

 		<string>com.apple.assistant.multiuser.service.remora</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.announced.toneplayer</string>
+		<string>com.apple.mobileactivationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.Sharing</string>
 		<string>com.apple.TelephonyUtilities</string>
+		<string>com.apple.MobileStoreDemo.test</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

 			<dict/>
 		</dict>
 	</dict>
+	<key>com.apple.geoservices.navigation_info</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-privileged</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access-protected</key>

 		<string>com.apple.sos</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.locationd.registration</string>
+		<string>com.apple.navigationListener</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.safetyalerts</string>
+	</array>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>
 	<key>com.apple.security.ts.identity-services-client</key>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<string></string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.appleaccountd</string>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.cdp.recoverykey</key>

 	<true/>
 	<key>com.apple.cdp.walrus.pcskeys</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>
-	<key>com.apple.private.security.storage.IntelligencePlatform</key>
-	<true/>
 	<key>com.apple.private.security.storage.appleaccountd</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

 	<true/>
 	<key>com.apple.PairingManager.Write</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
 	<key>com.apple.appleidsetup.repair.client</key>

 	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
 	<array>
 		<string>Removal</string>

 		<key>value</key>
 		<string>/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService</string>
 	</dict>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.game-center</key>
 	<array>
 		<string>Account</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.icloud.findmydeviced</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.frontboard.systemappservices</string>

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.userprofiles</string>
-		<string>com.apple.PineBoardRiseServices</string>
+		<string>com.apple.corefollowup.agent</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### asktod

> `/usr/libexec/asktod`

```diff

 <dict>
 	<key>com.apple.askto.extension.host</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.people.legacy.service.extension</key>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.assessmentagent/</string>

 		<string>com.apple.assessmentmode</string>
 		<string>com.apple.springboard</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.configurationprofiles</string>
+	</array>
 	<key>com.apple.springboard.application-restriction-monitoring</key>
 	<true/>
 	<key>com.apple.springboard.externaldisplay.displayArrangements</key>

```
### atcrtcomm

> `/usr/libexec/atcrtcomm`

```diff

 <dict>
 	<key>com.apple.driver.AppleTypeCRetimer.user-access</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleTypeCRetimerUserClient</string>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	<array>
 		<string>BluetoothAddress</string>
 		<string>SysCfg</string>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+		<string>SerialNumber</string>
+		<string>UniqueChipID</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.SkyLight.displaycontrol</key>
 	<true/>

 		<string>kTCCServiceBluetoothPeripheral</string>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceMotion</string>
+		<string>kTCCServiceBluetoothAlways</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

 		<string>com.apple.ShareAudioNotifications</string>
 		<string>com.apple.AudioAccessoryUserNotifications</string>
 		<string>com.apple.HearingModeUserNotifications</string>
+		<string>com.apple.SleepDetectionUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.relatived.public</string>
 		<string>com.apple.healthd.server</string>
+		<string>com.apple.BTAudioHALPluginAccessories</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.private.health.feature-availability-requirement-overrides</string>
+		<string>com.apple.assistant.domain.preferences</string>
 		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

 	<true/>
 	<key>com.apple.siri.external_request</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.systemstatus.domains</key>
 	<array>
 		<string>media</string>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.AudioAccessoryServices</key>
 	<true/>
+	<key>com.apple.BTAudioHALPluginAccessories</key>
+	<true/>
 	<key>com.apple.BTServer.le</key>
 	<true/>
 	<key>com.apple.BluetoothServices</key>

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.networking.multipath</key>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.private.allow-ext_paniclog</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
+	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>
+	<true/>
 	<key>com.apple.private.applepearl.allow</key>
 	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
+	<key>com.apple.private.attentionawareness.continuousFaceDetect</key>
+	<true/>
+	<key>com.apple.private.attentionawareness.poll</key>
+	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
 	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>

```
### biometrickitd

> `/usr/libexec/biometrickitd`

```diff

 		<string>AppleSPUHIDDeviceUserClient</string>
 		<string>AppleSPUHIDDriverUserClient</string>
 	</array>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### bluetoothuserd

> `/usr/libexec/bluetoothuserd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	</array>
 	<key>com.apple.private.ids.identityservicesd</key>
 	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.icloudpairing</string>
+	</array>
+	<key>com.apple.private.ids.messaging.high-priority</key>
+	<array>
+		<string>com.apple.private.alloy.icloudpairing</string>
+	</array>
 	<key>com.apple.private.ids.registration</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### carkitd

> `/usr/libexec/carkitd`

```diff

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.CarDDPAssets</string>
+		<string>com.apple.MobileAsset.CarDDPAssetsPreflight</string>
 		<string>com.apple.MobileAsset.CarExperienceAssets</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>

 	<true/>
 	<key>com.apple.private.carkit.app</key>
 	<true/>
+	<key>com.apple.private.carkit.appClips</key>
+	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
 	<key>com.apple.private.carkit.sessionRequest</key>

```
### ciphermld

> `/usr/libexec/ciphermld`

```diff

 	<string>com.apple.ciphermld</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.pegasus.context</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.PegasusConfiguration</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.ciphermld/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.networkserviceproxy</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.kvsd</string>
 		<string>com.apple.CipherMLService</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.parsecd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.parsecd</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.jett.switch-itms</string>
 	</array>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<true/>
 	<key>com.apple.appletv.pbs.user-profiles</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authentication-services-core.allow-authentication-request-proxying</key>
 	<true/>
 	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.carousel.wakegesturemonitor</key>
 	<true/>
 	<key>com.apple.companionuiservice.client</key>

 	<string>production</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
+	<key>com.apple.locationd.effective-bundle</key>
+	<true/>
+	<key>com.apple.locationd.usage-oracle</key>
+	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
 	<key>com.apple.payment.card-on-file</key>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.bmk.allow</key>

 	</array>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Applications/</string>

 		<string>/Library/Preferences/SystemConfiguration/preferences.plist</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Application Support/com.apple.DistributedTimers/</string>

 	<array>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.ak.authorizationservices.xpc</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent</string>
+		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.carousel.wakegesturemonitor</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.CompanionLink</string>

 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.homehubd.manage</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.MobileTimer.alarmserver</string>
 		<string>com.apple.MobileTimer.timerserver</string>
 		<string>com.apple.PineBoardServices</string>

```
### configd

> `/usr/libexec/configd`

```diff

 	<true/>
 	<key>com.apple.carousel.modalappservice</key>
 	<true/>
-	<key>com.apple.developer.driverkit.userclient-access</key>
-	<array>
-		<string>com.apple.DriverKit-AppleBCMWLAN</string>
-	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.multitasking.systemappassertions</key>

```
### corecaptured

> `/usr/libexec/corecaptured`

```diff

 	<true/>
 	<key>com.apple.corecaptured.remoteservice-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.diagnosticpipeline.request</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.gizmoappd.appmanager.allow</key>

 	<string>com.apple.coreduetd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>PeopleSuggesterContactPriors</key>
+		<key>ShareSheetFeedback</key>
 		<dict>
-			<key>Sets</key>
-			<dict>
-				<key>Contacts.Contact</key>
-				<dict>
-					<key>mode</key>
-					<string>read-only</string>
-				</dict>
-				<key>PeopleSuggester.ContactPrior</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
+			<key>Streams</key>
+			<array>
+				<string>ShareSheet.Feedback</string>
+			</array>
 		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
+		<string>visualIdentifier</string>
 		<string>photosAutonamingView</string>
 	</array>
 	<key>com.apple.private.kernel.override-cpumon</key>

```
### coreidvd

> `/usr/libexec/coreidvd`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.NPKCompanionAgent.client</key>
+	<true/>
 	<key>com.apple.NanoPassbook.IDVRemoteDeviceService.extendedReviewNotification</key>
 	<true/>
 	<key>com.apple.NanoPassbook.IDVRemoteDeviceService.session.client</key>

 		<string>com.apple.iconservices</string>
 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.NPKCompanionAgent.library</string>
+		<string>com.apple.NPKCompanionAgent.Server</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.managedappdistributiond.xpc</string>

```
### cryptexd

> `/usr/libexec/cryptexd`

```diff

 	<array>
 		<string>kTCCServiceSystemPolicySysAdminFiles</string>
 	</array>
+	<key>com.apple.private.unload-trust-cache</key>
+	<true/>
 	<key>com.apple.private.vfs.graftdmg</key>
 	<true/>
 	<key>com.apple.private.xpc.allowed-launch-types</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.computesafeguards.managing.allow</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 		<string>Activity.Level</string>
 		<string>ContextSync.DeviceActivityLevel</string>
 		<string>App.InFocus</string>
+		<string>App.Install</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>ActivityScheduler.Dependency.Completion</string>
 		<string>ActivityScheduler.Dependency.Result</string>
+		<string>Device.Thermals.BatteryTemperature</string>
 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>AppResumeBiomeUseCase</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Device.Power.PluggedIn</string>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
+		<key>DuetActivitySchedulerAppPredictions</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
 		<key>PhotosIntentSyncRemoteDeviceActivity</key>
 		<dict>
 			<key>Streams</key>

 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.commcenter.carrierspace.xpc</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
+		<string>com.apple.computesafeguards.managing</string>
 		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.coremedia.cameraviewfinder</string>

```
### demod

> `/usr/libexec/demod`

```diff

 	<true/>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
+	<key>com.apple.backlight.disable_always_on_assertion</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.cdp.recoverykey</key>

 	<true/>
 	<key>com.apple.private.airdrop.settings</key>
 	<true/>
+	<key>com.apple.private.allow-SUController</key>
+	<true/>
 	<key>com.apple.private.allow-subridge</key>
 	<true/>
 	<key>com.apple.private.amfi.set-demo</key>

 	<true/>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.InFocus</string>

```
### demod_helper

> `/usr/libexec/demod_helper`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.demo_backup</key>
 	<true/>
+	<key>com.apple.private.sysdiagnose</key>
+	<true/>
 	<key>com.apple.private.vfs.snapshot</key>
 	<true/>
 	<key>com.apple.rootless.storage.siriremembers</key>

```
### devicesharingd

> `/usr/libexec/devicesharingd`

```diff

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biometrickitd.oyster</string>
 		<string>com.apple.devicesharingd.guestuserremoteunlockservice</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.iconservices</string>

```
### diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

 	<false/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<string>AppleAPFSUserClient</string>
 </dict>
 </plist>
 

```
### dmd

> `/usr/libexec/dmd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
 	<string>com.apple.dmd</string>
 	<key>com.apple.private.lockdown.finegrained-get</key>

```
### feedbackd

> `/usr/libexec/feedbackd`

```diff

 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.appleseed.FeedbackAssistant</string>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.surfboard.application-service-client</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.private.ckks</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 	<string>com.apple.findmy.findmylocated</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.CommCenter.StormBreaker</key>
+	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>data-allowed-write</string>
+		<string>spi</string>
+	</array>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.pairedInfoSecurity</key>
+	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
+	<key>com.apple.chrono.invalidate-timelines</key>
+	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.securelocations</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry</key>
+	<true/>
 	<key>com.apple.nearbyinteraction.background</key>
 	<true/>
 	<key>com.apple.nearbyinteraction.finding.local-device</key>
 	<true/>
 	<key>com.apple.nearbyinteraction.finding.session</key>
 	<true/>
+	<key>com.apple.networkrelay.deviceMonitor</key>
+	<true/>
+	<key>com.apple.networkrelay.devices.read</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>ArrowChipID</string>

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>FindMy.ContactActivity</string>
+		<string>FindMy.LocationChange</string>
 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>

 	<array>
 		<string>com.apple.private.alloy.fmf.local</string>
 		<string>com.apple.private.alloy.fmf</string>
+		<string>com.apple.private.alloy.fmd</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
 		<string>com.apple.private.alloy.fmf</string>
 		<string>com.apple.private.alloy.fmf.local</string>
+		<string>com.apple.private.alloy.fmd</string>
 	</array>
 	<key>com.apple.private.ids.registration</key>
 	<true/>

 	<key>com.apple.private.ids.session</key>
 	<array>
 		<string>com.apple.private.alloy.fmf</string>
+		<string>com.apple.private.alloy.fmd</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>
 	<array>
 		<string>com.apple.private.alloy.fmf</string>
+		<string>com.apple.private.alloy.fmd</string>
 	</array>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.geod</string>
+		<string>com.apple.icloud.findmydeviced</string>
 		<string>com.apple.icloud.searchpartyd.securelocations</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.identityservicesd.idquery.embedded.auth</string>

 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.chronoservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>systemgroup.com.apple.icloud.searchpartyd.sharedsettings</string>
 		<string>com.apple.ids</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

 	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.icloud.searchpartyd.sharedsettings</string>
+	</array>
 	<key>com.apple.security.ts.application-group-support</key>
 	<true/>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.findmy.findmylocated</string>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.timed</key>
 	<true/>
 	<key>platform-application</key>

```
### finish_demo_restore

> `/usr/libexec/finish_demo_restore`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.security.storage.HomeKit</key>
+	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>
 	<true/>
 	<key>com.apple.private.security.storage.demo_backup</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>Library/homed/</string>
+	</array>
 </dict>
 </plist>
 

```
### fskitd

> `/usr/libexec/fskitd`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.filesystems.fskitd</string>
+	<string>com.apple.fskitd</string>
 	<key>com.apple.application-identifier</key>
-	<string>com.apple.filesystems.fskitd</string>
+	<string>com.apple.fskitd</string>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.private.LiveFS.connection</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.containermanagerd</string>
 		<string>com.apple.fskit.fskit_agent</string>
+		<string>com.apple.fskit.fskit_helper</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>AppleLIFSUserClient</string>
+	<key>notYet.com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GameController.gamecontrollerd</string>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 		<string>com.apple.iaptransportd.ExternalAccessory.distributednotification.server</string>
 		<string>com.apple.ExternalAccessory.distributednotification.server</string>
 		<string>com.apple.accessories.externalaccessory-server</string>
-		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.replayd</string>
+		<string>com.apple.bluetooth.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gamecenter</string>
-		<string>com.apple.mediaremote</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### gamed

> `/usr/libexec/gamed`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GameCenterLibraryRecentlyPlayed</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
 		<key>GameCenterSuggestionFeedback</key>
 		<dict>
 			<key>Streams</key>

```
### handwritingd

> `/usr/libexec/handwritingd`

```diff

 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keyboardservices.textreplacement.allow</key>
 	<true/>
 	<key>com.apple.modelcatalog.full-access</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.modelcatalog.catalog</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### hostapd

> `/usr/libexec/hostapd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.driverkit.driver-access</key>
 	<array>
 		<string>com.apple.private.wifi.driverkit</string>

```
### icloudmailagent

> `/usr/libexec/icloudmailagent`

```diff

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.mail</string>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.bluetooth.softwareupdate</key>
+	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
+	<key>com.apple.developer.networking.multicast</key>
+	<true/>
 	<key>com.apple.diagnostics.launcher-service</key>
 	<true/>
 	<key>com.apple.frontboard.shutdown</key>

 	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>
 	<true/>
+	<key>com.apple.private.security.no-sandbox</key>
+	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceBluetoothPeripheral</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleMobileApNonceUserClient</string>

 	<array>
 		<string>systemgroup.com.apple.powerlog</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/tmp/</string>
+		<string>/usr/local/bin/</string>
+		<string>/usr/local/bin/suServer.py</string>
+		<string>/usr/local/bin/python3</string>
+	</array>
+	<key>com.apple.wifi_nan.event_monitor</key>
+	<true/>
+	<key>com.apple.wifip2p.daemon_monitor</key>
+	<true/>
+	<key>com.apple.wifip2pd</key>
+	<true/>
 </dict>
 </plist>
 

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 		<string>com.apple.inputAnalytics.IASWTAnalyzer</string>
 		<string>com.apple.inputAnalytics.IASSRAnalyzer</string>
 		<string>com.apple.inputAnalytics.IASGenmojiAnalyzer</string>
+		<string>com.apple.inputAnalytics.IASGenmojiUsageAnalyzer</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.inputanalyticsd</string>

```
### keychainsharingmessagingd

> `/usr/libexec/keychainsharingmessagingd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.kcsharing.invite</string>

```
### linkd

> `/usr/libexec/linkd`

```diff

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.remoteappintentsd.appevent</string>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.linkd</string>
-	<key>com.apple.siri.koa.donate.internal</key>
-	<true/>
 	<key>com.apple.siri.process-donates-vocabulary-on-behalf-of-apps</key>
 	<true/>
 	<key>platform-application</key>

```

### 🆕 locationaccessstored

> `/usr/libexec/locationaccessstored`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.status</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.locationd.synchronous</string>
		<string>com.apple.duetactivityscheduler</string>
	</array>
</dict>
</plist>

```
### locationd

> `/usr/libexec/locationd`

```diff

 		<string>road-tiles</string>
 		<string>building-tiles</string>
 	</array>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>
 	<true/>
+	<key>com.apple.private.healthkit.feature-availability.read</key>
+	<array>
+		<string>CardioFitness</string>
+		<string>WalkingSteadinessClassifications</string>
+	</array>
 	<key>com.apple.private.healthkit.local-device-source</key>
 	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>

 	<true/>
 	<key>com.apple.private.security.storage.containers</key>
 	<true/>
+	<key>com.apple.private.security.storage.locationd-private</key>
+	<true/>
 	<key>com.apple.private.security.storage.pipelined</key>
 	<true/>
 	<key>com.apple.private.sessionkit.listener</key>

 		<string>com.apple.locationd.LocationNotificationBundle</string>
 		<string>com.apple.FindMySafetyAlertsNotifications</string>
 	</array>
+	<key>com.apple.private.usernotifications.settings</key>
+	<array>
+		<string>write</string>
+		<string>read</string>
+	</array>
 	<key>com.apple.private.vfs.allow-low-space-writes</key>
 	<true/>
 	<key>com.apple.proactive.hero.AppPrediction.predictions</key>

 		<string>com.apple.nearbyd.xpc.nearbyinteraction.observer</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.countryd.update</string>
+		<string>com.apple.eligibilityd</string>
 		<string>com.apple.CarPlayApp.user-alerts-service</string>
 		<string>com.apple.rapport.people</string>
 		<string>com.apple.locationpushd.pushregistration</string>

```
### lockdownd

> `/usr/libexec/lockdownd`

```diff

 		<string>AppleARMIICUserClient</string>
 		<string>IOThunderboltFamilyUserClient</string>
 		<string>AppleAstrisGpioProbeUserClient</string>
+		<string>IOUserUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### logd

> `/usr/libexec/logd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.notify.root_access</key>
 	<true/>
 	<key>com.apple.private.exclaves.kernel-domain</key>

```

### 🆕 managedappsd

> `/usr/libexec/managedappsd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.devicemanagementclient.managedappsd</string>
	<key>com.apple.private.remotemanagement.subscriber</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/Managed Preferences/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.devicemanagementclient.managedappsd</string>
	</array>
	<key>com.apple.security.system-container</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<array>
		<string>com.apple.devicemanagementclient.managedappsd</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.managedappsd</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### mc_mobile_tunnel

> `/usr/libexec/mc_mobile_tunnel`

```diff

 	<true/>
 	<key>com.apple.keystore.escrow.create</key>
 	<true/>
+	<key>com.apple.managedconfiguration.mdmd-access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.mdmd.push</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profileconnection.mdm-access</key>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.validate-applications</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.shutdown</key>
 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService.access</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>

 	<array>
 		<string>http</string>
 		<string>https</string>
+		<string>*</string>
+		<string>im</string>
+		<string>Messages</string>
+		<string>iChat</string>
+		<string>imessage</string>
+		<string>tel</string>
 	</array>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>

```
### mdmuserd

> `/usr/libexec/mdmuserd`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.remove-profile</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.escrow.create</key>

```
### mediaparserd

> `/usr/libexec/mediaparserd`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
+	<key>com.apple.coreaudio.allow-vorbis-decode</key>
+	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>mediaparserd</string>
 	<key>com.apple.security.exception.iokit-user-client-class</key>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 	<true/>
 	<key>com.apple.coremedia.nerotransportconnectionxpc.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.idle-timer-services</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>com.apple.coremedia.mediaparserd.steeringparser.xpc</string>
 		<string>com.apple.coremedia.mediaparserd.playlistfileparser.xpc</string>
 		<string>com.apple.coremedia.mediaparserd.streamplaylistparser.xpc</string>
+		<string>com.apple.coremedia.mediaparserd.jsonparser.xpc</string>
 		<string>com.apple.coremedia.videocodecd.decompressionsession.xpc</string>
 		<string>com.apple.coremedia.videocodecd.decompressionsession</string>
 		<string>com.apple.coremedia.videocodecd.compressionsession</string>

 	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
+	<key>com.apple.wirelessinsightsd.manager-access</key>
+	<true/>
 	<key>fairplay-client</key>
 	<integer>883412483</integer>
 	<key>keychain-access-groups</key>

```

### 🆕 memoryanalyticsd

> `/usr/libexec/memoryanalyticsd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.memoryanalyticsd</string>
	<key>com.apple.diagnosticpipeline.request</key>
	<true/>
	<key>com.apple.private.AuthorizationServices</key>
	<array>
		<string>system.preferences.nvram</string>
	</array>
	<key>com.apple.private.osanalytics.defaults.allow </key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.ReportMemoryException</string>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.system-task-ports.read</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>appleaccount</string>
	</array>
</dict>
</plist>

```
### merchantd

> `/usr/libexec/merchantd`

```diff

 	<true/>
 	<key>com.apple.coreidvd.mobile-document-reader.internal</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>
 	<true/>
+	<key>com.apple.nfcd.hwmanager</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.proxreader.uis-mach</string>
+		<string>com.apple.duetactivityscheduler</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.merchantd.prod</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.merchantd</string>

```
### mlhostd

> `/usr/libexec/mlhostd`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.mlhost</string>

 	<true/>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

```
### mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>2010</string>
 		<string>551</string>
+		<string>260</string>
 	</array>
 </dict>
 </plist>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<array>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 		<string>/private/var/run/MobileAssetCritialDomainsUpdated.plist</string>
+		<string>/private/var/run/MobileAssetSuspendSystemOptionalForSoftwareUpdate.nonce</string>
 		<string>/private/var/code_coverage/</string>
 		<string>/private/var/run/com.apple.mobileassetd-AutoAsset-DeviceBoot-UUID</string>
 	</array>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 	<string>com.apple.thimble.thtool</string>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.ane.memoryUnwiringOptOutAccess.allow</key>
+	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
 	<key>com.apple.developer.ane.increased-model-size-limit</key>

 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
+		<string>com.apple.MobileAsset.CN.Guardrail</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.modelmanagerd</string>

 	<key>com.apple.private.extensionkit.host.unsandboxed-extensions-for-extension-points</key>
 	<array>
 		<string>com.apple.modelmanager.inferenceprovider</string>
+		<string>com.apple.modelmanager.inferenceprovider.safety</string>
 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.coreduetd.context</key>
+	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.feedbackd.client-forms</key>
 	<array>
 		<string>:framework-journalingsuggestions-onboarding</string>

 	<array>
 		<string>group.com.apple.Journal</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>NowPlaying</string>
+		<string>App.MediaUsage</string>
+		<string>App.WebUsage</string>
+		<string>Device.Display.Backlight</string>
+		<string>Media.NowPlaying</string>
+		<string>Notification.Usage</string>
+		<string>ScreenTime.AppUsage</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.momentsd.MOUserNotifications</string>

 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.MomentsIntelligenceService</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>
 	<key>com.apple.security.ts.springboard-services</key>

```
### nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboard.app-badge-value-access</key>
 	<true/>
 	<key>com.apple.keystore.lockassertion</key>

```
### naturallanguaged

> `/usr/libexec/naturallanguaged`

```diff

 	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
+	<key>com.apple.generativeexperiences.textcomposition</key>
+	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/db/com.apple.naturallanguaged/</string>

 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.TextInput.rdt</string>
+		<string>com.apple.generativeexperiences.textcomposition</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.biome.access.user</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preferences.read-write</key>
 	<string>com.apple.naturallanguaged</string>

```
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.security.storage.Location</key>
 	<true/>
+	<key>com.apple.private.sessionkit.listener</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.coremedia.mediaplaybackd.player.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.remaker.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.sandboxserver.xpc</string>
+		<string>com.apple.sessionservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### nfcd

> `/usr/libexec/nfcd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.hammerfest.kext.entitlement</key>

```
### nptocompaniond

> `/usr/libexec/nptocompaniond`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.lsd.mapdb</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry</key>

```
### powerexperienced

> `/usr/libexec/powerexperienced`

```diff

 		<string>AppleCLPCUserClient</string>
 		<string>AppleSMCClient</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>364</string>
+	</array>
 </dict>
 </plist>
 

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.ids.registration</key>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.ProximityControl</string>
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
+	<key>com.apple.icloud.fmfd.access</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 	<true/>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
 	<true/>
+	<key>com.apple.private.safari.proximity-handoff</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.sociallayer.shareable-content</key>

 		<string>com.apple.fontservicesd</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.iconservices</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.iohideventsystem</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	<string>com.apple.rapportd</string>
 	<key>com.apple.CompanionLink</key>
 	<true/>
-	<key>com.apple.Contacts.database-allow</key>
-	<true/>
 	<key>com.apple.PairingManager.HomeKit</key>
 	<true/>
 	<key>com.apple.PairingManager.Read</key>

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Development</string>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
+	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
+	<array>
+		<string>com.apple.network.application-service</string>
+	</array>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.debugapplications</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.ckks</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
+	<key>com.apple.private.cloudkit.systemService</key>
+	<true/>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmapbundleidtouuid</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceBluetoothPeripheral</string>
 		<string>kTCCServiceWillow</string>

 	<array>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.CompanionLink</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.rapport</string>
 		<string>com.apple.rapport.NearbyInvitation</string>
 		<string>com.apple.securityd.ckks</string>
 		<string>com.apple.SharedWebCredentials</string>
 		<string>com.apple.SiriVOXService.client</string>
+		<string>com.apple.StatusKit.local</string>
+		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>

 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.SBUserNotification</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.cloudd</string>
+		<string>com.apple.contactsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>com.apple.wifi.awdl</key>

```
### relatived

> `/usr/libexec/relatived`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-protected</key>
+	<true/>
 	<key>com.apple.hid.system.fast-path-motion-event-privileged</key>
 	<true/>
 	<key>com.apple.hid.system.user-access-fast-path</key>

```
### remoted

> `/usr/libexec/remoted`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 		<string>IOThunderboltFamilyUserClient</string>
 		<string>IODPDeviceUserClient</string>
 		<string>IOAVDeviceUserClient</string>
+		<string>IOUserUserClient</string>
 	</array>
 </dict>
 </plist>

```
### retimerd

> `/usr/libexec/retimerd`

```diff

 <dict>
 	<key>com.apple.driver.AppleTypeCRetimer.user-access</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleTypeCRetimerUserClient</string>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
+	<key>com.apple.aonsensed.xpc</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

```
### runningboardd

> `/usr/libexec/runningboardd`

```diff

 	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.pluginkit.manager</key>
 	<true/>
 	<key>com.apple.private.process.suspend-resume.any</key>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.safetyalerts</string>
+	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	</array>
 	<key>com.apple.findmy.findmybeaconingd.push</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.fenceservice</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
+	<key>com.apple.nearbyinteraction.background</key>
+	<true/>
 	<key>com.apple.networkrelay.deviceMonitor</key>
 	<true/>
 	<key>com.apple.networkrelay.devices.read</key>

 	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.fmd.local</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.fmd.local</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>

 	<true/>
 	<key>com.apple.private.ids.session</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>
 	<true/>
+	<key>com.apple.private.nearbyinteraction.auth-ranging</key>
+	<true/>
+	<key>com.apple.private.nearbyinteraction.auto-tech-selection</key>
+	<true/>
+	<key>com.apple.private.nearbyinteraction.device-presence</key>
+	<true/>
+	<key>com.apple.private.nearbyinteraction.privileged</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.security.storage.SearchParty</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.terminusd</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```
### seld

> `/usr/libexec/seld`

```diff

 	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>
 	<true/>
+	<key>com.apple.internal.seserviced.fido</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.seserviced.key</key>
+	<true/>
 	<key>com.apple.seserviced.seendpoints</key>
 	<true/>
 </dict>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	<array>
 		<string>analysis</string>
 	</array>
+	<key>com.apple.devicesharing.guest-user-mode-client</key>
+	<true/>
+	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
+	<array>
+		<string>com.apple.share-services</string>
+		<string>com.apple.ui-services</string>
+		<string>com.apple.services</string>
+	</array>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>

 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 		<string>PURGE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.HUD-application</key>

 	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
+	<key>com.apple.private.security.storage-exempt</key>
+	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
 	<key>com.apple.private.security.storage.DiagnosticReports.read-only</key>

 		<string>/private/var/mobile/Library/CoreBehavior/BehaviorMiner.sqlite</string>
 		<string>/private/var/mobile/Library/CoreBehavior/BehaviorMiner.sqlite-shm</string>
 		<string>/private/var/mobile/Library/CoreBehavior/BehaviorMiner.sqlite-wal</string>
+		<string>/private/var/mobile/Library/com.apple.sharingd/ShareSheetTestingSnapshots/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
+		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.DocumentManagerCore.Downloads</string>
 		<string>com.apple.diagnosticextensionsd.sharing-wakeup</string>
 		<string>com.apple.distributed_notifications@Uv3</string>

 		<string>com.apple.cache_delete</string>
 		<string>com.apple.userprofiles</string>
 		<string>com.apple.uservault</string>
+		<string>com.apple.ClipServices.clipserviced</string>
+		<string>com.apple.containermanagerd</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 	<string>production</string>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
-	<key>com.apple.accounts.appleaccount.fullaccess</key>
-	<true/>
 	<key>com.apple.assistant.multiuser.service</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.orchestration.capabilities</string>
 		<string>com.apple.SystemConfiguration.configd</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.locationd.registration</string>

 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.medialibraryd.xpc</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.corefollowup.agent</string>

 		<string>com.apple.mobilecal</string>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.siri.inference.EntityMatcher</string>
+		<string>com.apple.siri.vocabulary</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.siri.embeddedspeech</key>
 	<true/>
+	<key>com.apple.siri.orchestration.capabilities</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### softposreaderd

> `/usr/libexec/softposreaderd`

```diff

 		<string>NDEF</string>
 		<string>TAG</string>
 	</array>
+	<key>com.apple.devicecheck.daemon-client</key>
+	<true/>
+	<key>com.apple.devicecheck.private.api</key>
+	<true/>
+	<key>com.apple.devicecheck.private.certificate.validity</key>
+	<integer>48960</integer>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.feedbackd.client-forms</key>
+	<array>
+		<string>framework-tap-to-pay</string>
+	</array>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.devicecheckd</string>
+		<string>com.apple.feedbackd.xpc</string>
 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.seld.tsmmanager</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.mobileactivationd</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.merchantd.prod</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.softposreaderd</string>
 		<string>com.apple.softposreader</string>
 		<string>com.apple.softposreader.daily</string>
+		<string>com.apple.AppAttest.client</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### soundanalysisd

> `/usr/libexec/soundanalysisd`

```diff

 	<true/>
 	<key>com.apple.private.exclaves.conclave-host</key>
 	<true/>
+	<key>com.apple.private.isolated.audio.coreaudioclient</key>
+	<true/>
+	<key>com.apple.private.isolated.audio.coreaudioclient.shareddsp</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.enrollmentmode.allow</key>

```
### srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

 	<true/>
 	<key>com.apple.pf.allow</key>
 	<true/>
+	<key>com.apple.private.ctr.thread</key>
+	<true/>
 	<key>com.apple.private.fillmore.AccessoryInfo.modification</key>
 	<true/>
 	<key>com.apple.private.fillmore.prefix.modification</key>

```
### swtransparencyd

> `/usr/libexec/swtransparencyd`

```diff

 	<array>
 		<string>group.com.apple.swtransparency</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.osanalytics</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 systemservicemonitord

> `/usr/libexec/systemservicemonitord`

- No entitlements *(yet)*
### terminusd

> `/usr/libexec/terminusd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.networkrelayTransport</key>
 	<true/>
+	<key>com.apple.bluetooth.pairedInfoSecurity</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

```

### 🆕 textunderstandingd

> `/usr/libexec/textunderstandingd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.textunderstandingd</string>
	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
	<true/>
	<key>com.apple.fileprovider.acl-read</key>
	<true/>
	<key>com.apple.fileprovider.acl-write</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.fileprovider.extension-host</key>
	<true/>
	<key>com.apple.fileprovider.fetch-url</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.analysis</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.person</string>
		<string>photos.face</string>
	</array>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.textunderstandingd</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>TextUnderstanding.DocumentUnderstanding.PoemBuffer</string>
		<string>TextUnderstanding.DocumentUnderstanding.Poem</string>
		<string>TextUnderstanding.DocumentUnderstanding.PoemAnalytics</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.corespotlight.bundleid</key>
	<string>com.apple.FileProvider.LocalStorage</string>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>entitySummary</string>
		<string>eventSubgraph</string>
		<string>peopleSubgraph</string>
		<string>inferenceFeaturesECR</string>
		<string>personEntityRelevanceRanking</string>
		<string>appEntityRelevanceRanking</string>
		<string>loiEntityRelevanceRanking</string>
	</array>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.TextUnderstanding</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.proactive.experiments.responses</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/db/com.apple.naturallanguaged/com.apple.e5rt.e5bundlecache/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.proactive.experiments.responses</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.mediaanalysisd.client</string>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.naturallanguaged</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.AppSupport</string>
		<string>com.apple.tokengeneration</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXDeviceUserClient</string>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>H11ANEInDirectPathClient</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>SMART_REPLY_EN</string>
		<string>UNDERSTANDING_PLATFORM_DOCUMENT_UNDERSTANDING</string>
		<string>UNDERSTANDING_PLATFORM_FOUND_IN</string>
		<string>UNDERSTANDING_PLATFORM_POEM</string>
	</array>
	<key>com.apple.webkit-client</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### transparencyStaticKey

> `/usr/libexec/transparencyStaticKey`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.transparencyStaticKey</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.cdp.utility</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.transparency.transparencyd</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.ProtectedCloudStorage.KTAccountKey</string>

```
### triald

> `/usr/libexec/triald`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>

 	<array>
 		<string>Siri.AnalyticsIdentifiers.UserAggregationId</string>
 	</array>
-	<key>com.apple.private.biome.read-write</key>
-	<string>Lighthouse.Ledger.TrialdEvent</string>
 	<key>com.apple.private.cloudkit.buddyAccess</key>
 	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>NamespaceUpdates</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Trial.Experiment.NamespaceUpdates</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.cache_delete</string>
 		<string>com.apple.mobileasset.autoasset</string>

```
### triald_system

> `/usr/libexec/triald_system`

```diff

 	<string>com.apple.triald.system</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.triald.system</string>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriResponseFrameworkFiles</string>

```
### videocodecd

> `/usr/libexec/videocodecd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```

### 🆕 visioncompaniond

> `/usr/libexec/visioncompaniond`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.visioncompaniond</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.appstored.install-apps</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.tdg-wb</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.private.InstallCoordination.uninstall</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>DeviceName</string>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.tdg-wb</key>
		<string>com.apple.tdg-wb</string>
	</dict>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_SoftwareUpdateDocumentation/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstored.xpc.request</string>
		<string>com.apple.apsd</string>
		<string>com.apple.installcoordinationd</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.softwareupdateservicesd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.softwareupdateservicesd</string>
		<string>com.apple.visioncompaniond</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.visioncompaniond</string>
	<key>com.apple.softwareupdateservices</key>
	<true/>
	<key>com.apple.softwareupdateservices.client.allowed</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### wapic

> `/usr/libexec/wapic`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.developer.driverkit.userclient-access</key>
+	<key>com.apple.private.driverkit.driver-access</key>
 	<array>
-		<string>com.apple.DriverKit-AppleBCMWLAN</string>
+		<string>com.apple.private.wifi.driverkit</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### watchdogd

> `/usr/libexec/watchdogd`

```diff

 	<true/>
 	<key>com.apple.private.apfs.key_migration</key>
 	<true/>
+	<key>com.apple.private.endpoint-security.client</key>
+	<true/>
+	<key>com.apple.private.endpoint-security.default-muter</key>
+	<true/>
+	<key>com.apple.private.endpoint-security.embeddedclient</key>
+	<true/>
 	<key>com.apple.private.iowatchdog.user-access</key>
 	<true/>
 	<key>com.apple.private.security.storage.spindump</key>

 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>
 	<string>com.apple.watchdogd</string>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>EndpointSecurityExternalClient</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>

```
### wifiFirmwareLoader

> `/usr/libexec/wifiFirmwareLoader`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>

```
### wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>

```
### wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
 	<array>
 		<string>Inspection</string>

```
### wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>

```
### BTAvrcp

> `/usr/sbin/BTAvrcp`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.mediaplayer.radio.private</key>

```
### BTLEServer

> `/usr/sbin/BTLEServer`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.devicesharing.guest-user-mode-client</key>

 		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
 		<string>HKQuantityTypeIdentifierHeight</string>
 	</array>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.CallHistory</key>

```
### BTMap

> `/usr/sbin/BTMap`

```diff

 <dict>
 	<key>com.apple.contacts.database-allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

```

### 🆕 arp

> `/usr/sbin/arp`

- No entitlements *(yet)*
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 		<string>com.apple.driver.driverkit.serial</string>
 		<string>com.apple.IOUserBluetoothSerialDriver</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.driver.AppleBluetoothModule.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleConvergedIPC.user-access</key>

 	<array>
 		<string>Device.Wireless.BluetoothGATTSession</string>
 		<string>Device.Wireless.BluetoothPowerEnabled</string>
+		<string>Device.Wireless.Bluetooth</string>
 	</array>
 	<key>com.apple.private.carkit</key>
 	<true/>

```
### fairplayd.H2

> `/usr/sbin/fairplayd.H2`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.fpsd</key>
 	<true/>
+    <key>com.apple.TapToRadarKit.service-access</key>
+    <true/>
+	<key>com.apple.timed</key>
+	<true/>
 </dict>
 </plist>
 

```
### filecoordinationd

> `/usr/sbin/filecoordinationd`

```diff

 	<true/>
 	<key>com.apple.private.vfs.dataless-resolver</key>
 	<true/>
+	<key>com.apple.private.vfs.support-long-paths</key>
+	<true/>
 </dict>
 </plist>
 

```
### mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.iokit.wakerequest</key>
 	<true/>
 	<key>com.apple.mDNSResponder_Helper</key>

```

### 🆕 ndp

> `/usr/sbin/ndp`

- No entitlements *(yet)*

### 🆕 netstat

> `/usr/sbin/netstat`

- No entitlements *(yet)*
### notifyd

> `/usr/sbin/notifyd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.ios-system-session</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```

### 🆕 skywalkctl

> `/usr/sbin/skywalkctl`

- No entitlements *(yet)*
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.diagnosticpipeline.request</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.geoanalyticsd.telemetry</key>

 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
+	<key>com.apple.private.CarPlayServices.app-history</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>StoreDemoMode</string>
 	</array>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.CoreWiFi</string>
+	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.wifid</string>
 	<key>com.apple.private.biome.read-write</key>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
