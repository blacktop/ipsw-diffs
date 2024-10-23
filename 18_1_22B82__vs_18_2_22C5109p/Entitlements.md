## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 	<key>com.apple.surfboard-prevent-homeui-from-hiding-when-launching</key>
 	<true/>
 	<key>com.apple.surfboard.chrome-customization</key>

```
### AirDropUI

> `/Applications/AirDropUI.app/AirDropUI`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.ProximityControl.ProximityHandoffInteractions</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

 		<string>com.apple.sociallayerd</string>
 		<string>com.apple.posterboardservices.data-store</string>
 		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.ProximityControl.ProximityHandoffInteractions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### AirPlayReceiver

> `/Applications/AirPlayReceiver.app/AirPlayReceiver`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.devicesharingd.client</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.private.MobileActivation</key>
 	<array>
 		<string>GetActivationState</string>
 	</array>
+	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.driverkit.driver-access</key>

 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.wifip2pd</string>
+		<string>com.apple.devicesharingd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 AppDeletionUIHost

> `/Applications/AppDeletionUIHost.app/AppDeletionUIHost`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
</dict>
</plist>

```
### AppDistributionLaunchAngel

> `/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.AppDistributionLaunchAngel</string>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
+	<key>com.apple.developer.browser.app-installation</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
+	<key>com.apple.payment.card-on-file</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
+	<key>com.apple.runningboard.jetengine</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/JetPackCache/</string>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>fairplay-client</key>
+	<true/>
 </dict>
 </plist>
 

```
### AppProtectionUIHost

> `/Applications/AppProtectionUIHost.app/AppProtectionUIHost`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.write.access</key>
 	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### CoreAuthUI

> `/Applications/CoreAuthUI.app/CoreAuthUI`

```diff

 <dict>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.QuartzCore.system-layers</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.assertiond.app-state-monitor</key>

 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.tvappservices.container</string>
+		<string>group.com.apple.sports</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### Diagnostic-7004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004`

```diff

-<?xml version="1.0" encoding="UTF-8"?>
-<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
-<plist version="1.0">
-<dict>
-	<key>com.apple.DiagnosticsKit.diagnosticmanager</key>
-	<true/>
-	<key>com.apple.DiagnosticsKit.extension</key>
-	<true/>
-	<key>com.apple.private.corerepair.xpc</key>
-	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.corerepair</string>
-		<string>com.apple.diskimagecorerepair</string>
-		<string>com.apple.appleh13camerad</string>
-		<string>com.apple.appleh16camerad</string>
-	</array>
-	<key>com.apple.system.diagnostics.iokit-properties</key>
-	<true/>
-</dict>
-</plist>
 

```
### Diagnostic-8343

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`

```diff

 	<array>
 		<string>com.apple.corerepair</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Diagnostic-8343</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 </dict>

```
### FTMInternal-4

> `/Applications/FTMInternal-4.app/FTMInternal-4`

```diff

 		<string>phone</string>
 		<string>carrier-settings</string>
 	</array>
+	<key>com.apple.Pasteboard.background-access</key>
+	<true/>
 	<key>com.apple.cellular-logging.internal</key>
 	<true/>
 	<key>com.apple.developer.cellular-logging.allow</key>

```
### Feedback Assistant iOS

> `/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.siri</key>
+	<true/>
 	<key>com.apple.diagnosticextensionsd.xpcclient</key>
 	<true/>
 	<key>com.apple.feedbackd.admin</key>

```
### GameCenterUIService

> `/Applications/GameCenterUIService.app/GameCenterUIService`

```diff

 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.GameOverlayUI</string>
+		<string>com.apple.GameOverlayUIInternal</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 GuestUserHandoverSetup

> `/Applications/GuestUserHandoverSetup.app/GuestUserHandoverSetup`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.PairingManager.Read</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.devicesharingd.client</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.devicesharingd</string>
	</array>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
</dict>
</plist>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>
 	</array>
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
 	<key>com.apple.locationd.status</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
+	<array>
+		<string>Removal</string>
+	</array>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.networkrelay.deviceMonitor</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

 	</array>
 	<key>com.apple.purplebuddy.budd.access</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.homedevicesetup.diagnostics</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/mobile/Library/Preferences/</string>
 		<string>/private/preboot/</string>
+		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/</string>
 		<string>/private/var/hardware/FactoryData/System/Library/Caches/com.apple.factorydata/</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/PayloadManifest.plist</string>
+		<string>/private/var/mobile/Library/Preferences/</string>
 		<string>/private/var/preferences/FeatureFlags/Settings.plist</string>
 		<string>/System/Library/Caches/com.apple.factorydata/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/var/mobile/Library/Caches/com.apple.homedevicesetup/</string>
 		<string>/private/var/tmp/APCCaptures/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
-		<string>/private/var/mobile/Library/Preferences/com.apple.sharingd.plist</string>
+		<string>/Library/Caches/com.apple.homedevicesetup/</string>
 		<string>/Library/Logs/CrashReporter/</string>
-		<string>/Library/VoiceTrigger/</string>
 		<string>/Library/Preferences/com.apple.coreaudio.plist</string>
 		<string>/Library/Preferences/com.apple.Sharing.plist</string>
+		<string>/Library/VoiceTrigger/</string>
 		<string>/Library/Logs/MediaServices/HTTPArchives/</string>
+		<string>/private/var/mobile/Library/Preferences/com.apple.sharingd.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.sharingd</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.coreservices.appleid.authentication</string>
 		<string>com.apple.corespeech.voicetriggerservice</string>
+		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>

 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.ak.auth.xpc</string>
 	</array>

```

### 🆕 HDSDiagnostic

> `/Applications/HDSViewService.app/PlugIns/HDSDiagnostic.appex/HDSDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.homedevicesetup.diagnostics</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/</string>
		<string>/Library/Caches/com.apple.homedevicesetup/</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
</dict>
</plist>

```
### HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.Home.group</string>
+		<string>group.com.apple.CoreSpeech</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.matter.support.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.matter.support.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

```
### MediaRemoteUI

> `/Applications/MediaRemoteUI.app/MediaRemoteUI`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.mediacontrol</string>
 		<string>com.apple.CoreDuet</string>
 		<string>com.apple.lockscreen.shared</string>
 		<string>com.apple.duetexpertd</string>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.mediacontrol</string>
 		<string>com.apple.CoreDuet</string>
 		<string>com.apple.lockscreen.shared</string>
 		<string>com.apple.duetexpertd</string>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
+	<key>com.apple.developer.phone-app</key>
+	<true/>
 	<key>com.apple.developer.usernotifications.communication</key>
 	<true/>
 	<key>com.apple.developer.usersafety.client</key>

```
### PCViewService

> `/Applications/PCViewService.app/PCViewService`

```diff

 		<string>com.apple.PairingManager</string>
 		<string>com.apple.PointerUI.pointeruid.service</string>
 		<string>com.apple.ProximityControl.HandoffViewServiceHost</string>
+		<string>com.apple.ProximityControl.ProximityHandoffInteractions</string>
 		<string>com.apple.ProximityControl.server</string>
 		<string>com.apple.ProximityControl.server.launching</string>
 		<string>com.apple.security.sfkeychainserver</string>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.financekit.financial-connection.host</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.fitcore</key>
 	<true/>
 	<key>com.apple.frontboard.delete-application-snapshots</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.geoservices.map-subscriptions</key>
 	<array>
 		<string>*</string>

 	<true/>
 	<key>com.apple.private.launchservices.changedefaulthandlers</key>
 	<array>
+		<string>*</string>
 		<string>https</string>
 		<string>http</string>
 		<string>mailto</string>

 	<key>com.apple.private.messages.associated-message-extension-bundle-identifiers</key>
 	<array>
 		<string>com.apple.PassbookUIService.PeerPaymentMessagesExtension</string>
+		<string>com.apple.AppleAccountUI.CustodianInviteMessageExtension</string>
 	</array>
 	<key>com.apple.private.mis.online_auth_agent</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.networkextension.configuration</key>
 	<string>super</string>
 	<key>com.apple.private.networkserviceproxy</key>

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceSpeechRecognition</string>
+		<string>kTCCServiceMicrophoneInjection</string>
 		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>
 		<string>kTCCServiceExposureNotification</string>
 	</array>

 		<string>/private/var/mobile/Library/DuetExpertCenter/ModeCaches/</string>
 		<string>/private/var/mobile/Library/DuetExpertCenter/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Media/PhotoData/Caches/PhotosPickerLogs/</string>
 		<string>/Library/DoNotDisturb/DB/IconCache</string>
 		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.SharedWebCredentials</string>
 		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.CarPlayApp.service</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.pairingmanager</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.anvil</string>
 		<string>com.apple.springboard</string>
 		<string>com.apple.momentsd</string>
-		<string>com.apple.seserviced.contactlessCredential.settings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
 		<string>com.apple.usernotificationskit</string>
+		<string>com.apple.messages.critical-messaging.storage</string>
+		<string>com.apple.seserviced.contactlessCredential.settings</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.hearing-test-mode</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.largeIconLayout</key>
 	<true/>
 	<key>com.apple.springboard.lowDensityIconLayout</key>

 		<string>com.apple.identities</string>
 		<string>appleaccount</string>
 		<string>com.apple.mobilemail.smime</string>
+		<string>com.apple.openai</string>
 		<string>com.apple.preferences</string>
 		<string>com.apple.safari.credit-cards</string>
 		<string>com.apple.PassbookUIService</string>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<dict>
 		<key>appData</key>
 		<array>
+			<string>com.apple.mobilesafari</string>
 			<string>com.apple.Passwords</string>
 		</array>
 	</dict>

 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Clip</string>
+		<string>Install</string>
+		<string>Library</string>
 	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>

 		<string>UIStatusBarStyleOverrideFullScreenWebRTCCapture</string>
 		<string>UIStatusBarStyleOverrideFullScreenWebRTCAudioCapture</string>
 	</array>
+	<key>com.apple.springboard.webClipService</key>
+	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

 		<string>com.apple.webkit.webauthn-recently-deleted</string>
 		<string>com.apple.password-manager.personal-recently-deleted</string>
 		<string>com.apple.password-manager.generated-passwords</string>
+		<string>com.apple.cfnetwork.testing</string>
+		<string>com.apple.password-manager.testing</string>
+		<string>com.apple.webkit.webauthn.testing</string>
 		<string>com.apple.password-manager.website-metadata</string>
+		<string>com.apple.password-manager.website-metadata.testing</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### SafetyMonitorApp

> `/Applications/SafetyMonitorApp.app/SafetyMonitorApp`

```diff

 	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
+	<key>com.apple.private.imcore.imagent</key>
+	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>
 	<true/>
 	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>

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
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 		<string>com.apple.coremedia.routingcontext.xpc</string>
 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 		<string>com.apple.coremedia.routediscoverer.xpc</string>
 		<string>com.apple.coremedia.routingcontext.xpc</string>
 		<string>com.apple.coremedia.volumecontroller.xpc</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```

### 🆕 TypeToSiriWidgetExtension

> `/Applications/Siri.app/PlugIns/TypeToSiriWidgetExtension.appex/TypeToSiriWidgetExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.TypeToSiriWidget</string>
	<key>com.apple.private.appintents-attribution-override</key>
	<string>YES</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.activation.service</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri</string>
	</array>
	<key>com.apple.siri.activation.service</key>
	<true/>
</dict>
</plist>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents.media-client-id</key>

 	<array>
 		<string>read</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.private.xpc.domain-extension</key>
 	<true/>
 	<key>com.apple.private.xpc.domain-extension.proxy</key>

 	<true/>
 	<key>com.apple.runningboard.primitiveattribute</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
 	<key>com.apple.screenshotservices.ssuiservice.showscreenshotui</key>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>

 		<string>com.apple.siri.client_lite</string>
 		<string>com.apple.siri.location</string>
 		<string>com.apple.corespeech.voicetriggerservice</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.siri.CarBluetooth</string>
 		<string>com.apple.Accessibility</string>
 		<string>com.apple.mobilenotes</string>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.StickerPickerService</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.assistant.cdm.client</key>

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 	<string>system</string>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
+	<key>com.apple.modelmanager.assertion</key>
+	<true/>
 	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```

### 🆕 DiagnosticExtension

> `/Applications/Tamale.app/PlugIns/DiagnosticExtension.appex/DiagnosticExtension`

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

### 🆕 TamaleWidgetExtension

> `/Applications/Tamale.app/PlugIns/TamaleWidgetExtension.appex/TamaleWidgetExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.VisualIntelligenceCamera.WidgetExtension</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.activation.service</string>
	</array>
	<key>com.apple.siri.activation.service</key>
	<true/>
</dict>
</plist>

```

### 🆕 Tamale

> `/Applications/Tamale.app/Tamale`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.VisualIntelligenceCamera</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>public-cellular-plan</string>
		<string>public-esim-qr-code</string>
	</array>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.RemoteDisplay</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.ane.iokit-user-access</key>
	<true/>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.VisualIntelligenceCamera</string>
	<key>com.apple.argos.availibility-bypass</key>
	<true/>
	<key>com.apple.arkit</key>
	<true/>
	<key>com.apple.assistant.dictation.prerecorded</key>
	<true/>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.allow-opus-codec</key>
	<true/>
	<key>com.apple.developer.applesignin</key>
	<array>
		<string></string>
	</array>
	<key>com.apple.developer.networking.HotspotConfiguration</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.pegasus.context</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.BarcodeSupport.can-suppress-app-clip-code-url-authorization</key>
	<true/>
	<key>com.apple.private.ClipServices</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.barcodesupport.allowNotifications</key>
	<true/>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.canIgnoreAppLinkEnabledProperty</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.corespeech.audioinjection.xpc</key>
	<true/>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.parsec.default-client</key>
	<string>com.apple.VisualIntelligenceCamera</string>
	<key>com.apple.private.payment.remote-network-payment-initiate</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>container</string>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.stickers</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceLocation</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServicePhotosAdd</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.rapport.SessionPaired</key>
	<true/>
	<key>com.apple.runningboard.trustedtarget</key>
	<true/>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.VisualIntelligenceCamera</string>
	</array>
	<key>com.apple.security.device.camera</key>
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
		<string>/private/var/Managed Preferences/mobile/com.apple.CoreMotion.plist</string>
		<string>/private/var/preferences/com.apple.networkd.plist</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/tmp/</string>
		<string>/private/var/tmp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.ClipServices/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOHIDEventServiceFastPathUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.sirireaderd</string>
		<string>com.apple.private.assistant.settings</string>
		<string>com.apple.sirittsd</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.geod</string>
		<string>com.apple.parsecd</string>
		<string>com.apple.stickers.api</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.siri.activation</string>
		<string>com.apple.siri.activation.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.usymptomsd</string>
		<string>com.apple.commcenter.coretelephony.xpc</string>
		<string>com.apple.nehelper</string>
		<string>com.apple.ClipServices.clipserviced</string>
		<string>com.apple.iconservices</string>
		<string>com.apple.pasteboard.pasted</string>
		<string>com.apple.BarcodeSupport.ParsingService</string>
		<string>com.apple.BarcodeSupport.BarcodeNotificationService</string>
		<string>com.apple.SharedWebCredentials</string>
		<string>com.apple.RemoteDisplay</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.parsecd</string>
		<string>com.apple.anvil</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.spotlightui</string>
		<string>com.apple.visualintelligence</string>
		<string>com.apple.gms.availability</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.generativeassistantsettings</string>
	</array>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
	<array>
		<string>/Library/Logs/DiagnosticReports/</string>
		<string>/tmp/</string>
	</array>
	<key>com.apple.siri.activation</key>
	<true/>
	<key>com.apple.siri.activation.service</key>
	<true/>
	<key>com.apple.sirittsd.can-dump-audio</key>
	<true/>
	<key>com.apple.springboard.activateRemoteAlert</key>
	<true/>
	<key>com.apple.springboard.allowallcallurls</key>
	<true/>
	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
	<key>com.apple.springboard.openurlswhenlocked</key>
	<true/>
	<key>com.apple.springboard.private.capture-button-events</key>
	<true/>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>581</string>
		<string>582</string>
		<string>583</string>
		<string>584</string>
		<string>585</string>
		<string>586</string>
		<string>313</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### Web

> `/Applications/Web.app/Web`

```diff

 	<array>
 		<string>com.apple.installcoordinationd</string>
 	</array>
+	<key>com.apple.springboard.webClipService</key>
+	<true/>
 </dict>
 </plist>
 

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<string>com.apple.WritingToolsUIService</string>
 	<key>com.apple.feedbackd.remote-evaluation</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
 	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>
 	<true/>
 	<key>com.apple.generativeexperiences.textcomposition</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
 	<key>com.apple.sage.summarization</key>

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Shortcuts/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.extensionkitservice</string>

 		<string>com.apple.sage.summarization</string>
 		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
-		<string>com.apple.siri.activation.service</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
-	<key>com.apple.siri.activation.service</key>
+	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>
 </plist>

```

### 🆕 MobileAssetExclaveComponent

> `/System/ExclaveKit/System/Library/Frameworks/MobileAssetExclaveComponent.framework/MobileAssetExclaveComponent`

- No entitlements *(yet)*

### 🆕 CoreANSTKit

> `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreANSTKit.framework/CoreANSTKit`

- No entitlements *(yet)*

### 🆕 CoreERClientKit

> `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreERClientKit.framework/CoreERClientKit`

- No entitlements *(yet)*

### 🆕 CoreMDClientKit

> `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreMDClientKit.framework/CoreMDClientKit`

- No entitlements *(yet)*

### 🆕 CoreMedia

> `/System/ExclaveKit/System/Library/PrivateFrameworks/CoreMedia.framework/CoreMedia`

- No entitlements *(yet)*

### 🆕 SISP_EK_AlgoModels

> `/System/ExclaveKit/System/Library/PrivateFrameworks/SISP_EK_AlgoModels.framework/SISP_EK_AlgoModels`

- No entitlements *(yet)*

### 🆕 SpeakerRecognitionKit

> `/System/ExclaveKit/System/Library/PrivateFrameworks/SpeakerRecognitionKit.framework/SpeakerRecognitionKit`

- No entitlements *(yet)*

### 🆕 libcorecrypto.dylib

> `/System/ExclaveKit/usr/lib/system/libcorecrypto.dylib`

- No entitlements *(yet)*

### 🆕 GameCenterAccountAuthenticationPlugin

> `/System/Library/Accounts/Authentication/GameCenterAccountAuthenticationPlugin.bundle/GameCenterAccountAuthenticationPlugin`

- No entitlements *(yet)*

### 🆕 GenerativeAssistantEnablementFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/GenerativeAssistantEnablementFlowPlugin.bundle/GenerativeAssistantEnablementFlowPlugin`

- No entitlements *(yet)*

### 🆕 IFFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/IFFlowPlugin.bundle/IFFlowPlugin`

- No entitlements *(yet)*
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.backboardd.pointerRepositioning</key>
 	<true/>
+	<key>com.apple.bannerkit.post</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.coreaudio.CanTapTelephony</key>

 		<string>com.apple.accessibility.livespeech</string>
 		<string>com.apple.speech.SpeechRecognitionCommandAndControl</string>
 		<string>com.apple.Accessibility.SwitchControl</string>
+		<string>com.apple.UIKit</string>
 		<string>com.apple.WatchControl</string>
 		<string>com.apple.airplay</string>
 		<string>com.apple.ClarityUI</string>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.CarPlayApp.service</string>
 		<string>com.apple.audio.SystemSoundServer-iOS</string>
+		<string>com.apple.CarPlayApp.service</string>
+	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>IOHIDResourceDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>

```

### 🆕 MediaMLExtension

> `/System/Library/CoreServices/MediaMLPluginApp.app/Extensions/MediaMLExtension.appex/MediaMLExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.MediaMLPluginApp.MediaMLExtension</string>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/com.apple.coremedia/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/MediaML/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.rtcreportingd</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
</dict>
</plist>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 		<string>com.apple.usernotificationsvendor.listener</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.matter.native.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

 	<true/>
 	<key>com.apple.private.CoreAnalytics.RolloverEvents.allow</key>
 	<true/>
+	<key>com.apple.private.CoreAnalytics.Tasking.notify</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```

### 🆕 AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.metrics.AssetMetricsExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.metrics.AssetMetricsExtension</string>
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
</dict>
</plist>

```
### AutocompleteAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/AutocompleteAppIntentsExtension.appex/AutocompleteAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
-	<key>com.apple.private.appintents-attribution-override</key>
-	<true/>
-	<key>com.apple.private.appintents-bundle-absolute-paths</key>
-	<array>
-		<string>/System/Library/PrivateFrameworks/ContactsAutocomplete.framework</string>
-	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCalendar</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.contacts.intents</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```

### 🆕 BiomeSELFIngestor

> `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.lighthouse.BiomeSELFIngestor</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.lighthouse.BiomeSELFIngestor</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>DillSELFMapper</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>IntelligenceFlow.Transcript.Datastream</string>
				<string>IntelligenceFlow.Experimentation</string>
				<string>IntelligenceFlow.JointResolverTelemetry</string>
				<string>IntelligenceFlow.PlanResolutionTelemetry</string>
				<string>IntelligenceFlow.QueryDecorationTelemetry</string>
				<string>IntelligenceFlow.ResponseGeneration</string>
				<string>IntelligenceFlow.SearchToolTelemetry</string>
				<string>IntelligenceFlow.ExecutorTelemetry</string>
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
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.lighthouse.dill.BiomeSELFIngestor</string>
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

### 🆕 BlackPowderInferenceExtension

> `/System/Library/ExtensionKit/Extensions/BlackPowderInferenceExtension.appex/BlackPowderInferenceExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.anvil</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
	</array>
	<key>com.apple.private.network.system-token-fetch</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.modelcatalog.catalog</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.anvil</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.openai</string>
	</array>
</dict>
</plist>

```

### 🆕 CameraMessagesApp

> `/System/Library/ExtensionKit/Extensions/CameraMessagesApp.appex/CameraMessagesApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.camera.CameraMessagesApp</string>
	<key>checklessPersistentURLTranslation</key>
	<true/>
	<key>com.apple.PencilKit.allowsSnapToShape</key>
	<true/>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.avfoundation.allow-capture-filter-rendering</key>
	<true/>
	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.allow-apac-codec</key>
	<true/>
	<key>com.apple.mediastream.mstreamd-access</key>
	<true/>
	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>
	<true/>
	<key>com.apple.messages.private.AllowParticipantAddressAccess</key>
	<true/>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.assetsd.nebulad.access</key>
	<string>camera</string>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.MobileSMS</string>
	</dict>
	<key>com.apple.private.avatar.store</key>
	<true/>
	<key>com.apple.private.avfoundation.capture.deferred-photo-processor.allow</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.lockdown.finegrained-get</key>
	<array>
		<string>NULL/ActivationPrivateKey</string>
		<string>NULL/DeviceCertificate</string>
	</array>
	<key>com.apple.private.photos.service.mediaconversion</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/tmp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Media/</string>
		<string>/Library/Caches/com.apple.MobileSMS/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assetsd.nebulad</string>
		<string>com.apple.systemstatus.activityattribution</string>
		<string>com.apple.CameraOverlayAngel.application-service</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.healthd</string>
		<string>com.apple.cameracapture</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.camera</string>
		<string>com.apple.MobileSMS</string>
	</array>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>com.apple.systemstatus.activityattribution</key>
	<true/>
</dict>
</plist>

```
### ContactsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ContactsAppIntentsExtension.appex/ContactsAppIntentsExtension`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.contacts.intents</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>WalletPaymentsCommerce.FinancialInsights.Search</string>
 		<string>WalletPaymentsCommerce.FinancialInsights.PaymentRingSuggestions</string>
 		<string>Photos.UserAnalytics</string>
-		<string>Moments.Stats.EventData</string>
 		<string>Keyboard.TokenFrequency</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Location.Semantic</string>

 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>MediaAnalysis.PEC.Processing</string>
 		<string>Safari.PageLoad</string>
 		<string>Siri.Health.Federated</string>
 		<string>AppleID.ChildSetup</string>

 		<string>Safari.WindowProxy</string>
 		<string>Siri.AssistantSuggestionFeatures</string>
 		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
-		<string>Photos.Delete</string>
-		<string>Photos.Memories.Curation</string>
+		<string>CommCenter.Call.EmergencyVoiceCall</string>
+		<string>Location.Emergency.SessionStart</string>
+		<string>Safari.MemoryFootprint</string>
+		<string>Mail.Recategorization</string>
 		<string>Photos.MemoryCreation</string>
+		<string>Photos.Curation</string>
+		<string>Photos.Delete</string>
+		<string>Photos.Search</string>
+		<string>Photos.Memories.Viewed</string>
+		<string>Photos.Memories.Shared</string>
+		<string>AeroML.Insights.PhotosSearchInsights</string>
+		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
+		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>
+		<string>CameraCapture.AutoFocusROI</string>
+		<string>Photos.Style</string>
+		<string>WalletPaymentsCommerce.FinancialInsights.RecurringSendSuggestions</string>
+		<string>Safari.Browsing.Assistant</string>
+		<string>GenerativeExperiences.TransparencyLog</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```

### 🆕 FindMyIntentsExtension

> `/System/Library/ExtensionKit/Extensions/FindMyIntentsExtension.appex/FindMyIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.findmy</string>
</dict>
</plist>

```
### com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.WebKit.GPU</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.QuartzCore.webkit-end-points</key>

 	<true/>
 	<key>com.apple.mediaremote.set-playback-state</key>
 	<true/>
+	<key>com.apple.mediaremote.ui-control</key>
+	<true/>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>
 	<true/>
 	<key>com.apple.private.attribution.explicitly-assumed-identities</key>

```

### 🆕 GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.GenerativePlaygroundApp.remoteUIExtension</string>
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
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
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

### 🆕 GenerativeAssistantExtension

> `/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.associated-domains</key>
	<array>
		<string>applinks:chatgpt.com</string>
	</array>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
	<true/>
	<key>com.apple.intelligenceflow.uiContext</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.generativeassistanttools.GenerativeAssistantExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>AppIntent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>com.apple.generativeassistanttools.GenerativeAssistantExtension</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>GenerativeAssistantTools</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>mode</key>
				<string>read-write</string>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.photos.service.mediaconversion</key>
	<true/>
	<key>com.apple.private.security.storage.SiriFeatureStore</key>
	<true/>
	<key>com.apple.private.security.storage.SiriReferenceResolution</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceMotion</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServicePhotosAdd</string>
		<string>kTCCServiceReminders</string>
		<string>kTCCServiceSpeechRecognition</string>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Assistant/SiriReferenceResolution/</string>
		<string>/Library/Shortcuts/</string>
		<string>/Media/iTunes_Control/iTunes/</string>
		<string>/Library/ACMEPrompts/</string>
		<string>/Library/Logs/com.apple.FeatureStore/</string>
		<string>/private/var/folders/*/*/*/com.apple.FeatureStore/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.SharingServices</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.calaccessd</string>
		<string>com.apple.controlcenter.remoteservice</string>
		<string>com.apple.coreduetd.context</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.itunescloudd.xpc</string>
		<string>com.apple.medialibraryd.xpc</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.securityd</string>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.trustd</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
		<string>com.apple.intelligenceflow.uiContext</string>
		<string>com.apple.symptom_diagnostics</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.generativeassistantsettings</string>
		<string>com.apple.siri</string>
		<string>com.apple.generativeassistanttools.GenerativeAssistantExtension</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
	<array>
		<string>/Library/Logs/com.apple.FeatureStore/</string>
		<string>/private/var/folders/*/*/*/com.apple.FeatureStore/</string>
	</array>
	<key>com.apple.sharing.Client</key>
	<true/>
	<key>com.apple.shortcuts.background-running</key>
	<true/>
	<key>com.apple.shortcuts.stepwise-execution</key>
	<true/>
	<key>com.apple.shortcuts.variable-injection</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 GenerativeAssistantSettingsExtension

> `/System/Library/ExtensionKit/Extensions/GenerativeAssistantSettingsExtension.appex/GenerativeAssistantSettingsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 HomeAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/HomeAppIntentsExtension.appex/HomeAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.homekit</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/HomeAppIntents.framework</string>
	</array>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Home</string>
	<key>com.apple.private.homekit</key>
	<true/>
	<key>com.apple.private.homekit.allow-secure-access</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.matter.native.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.matter.native.xpc</string>
	</array>
</dict>
</plist>

```
### HomeWidgetIntentsExtension

> `/System/Library/ExtensionKit/Extensions/HomeWidgetIntentsExtension.appex/HomeWidgetIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.Home.group</string>
+		<string>group.com.apple.CoreSpeech</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 		<string>com.apple.itunescloud.in-app-message-service</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.pearld</string>
 		<string>com.apple.private.corewifi.readonly-xpc</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

 		<string>com.apple.itunescloud.in-app-message-service</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.pearld</string>
 		<string>com.apple.private.corewifi.readonly-xpc</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

```

### 🆕 IFTranscriptSELFIngestor

> `/System/Library/ExtensionKit/Extensions/IFTranscriptSELFIngestor.appex/IFTranscriptSELFIngestor`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.lighthouse.IFTranscriptSELFIngestor</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>LighthouseDataProcessor</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>IntelligenceFlow.Transcript.Datastream</string>
				<string>IntelligenceFlow.IFRequestTelemetry</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### InferenceProviderService

> `/System/Library/ExtensionKit/Extensions/InferenceProviderService.appex/InferenceProviderService`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.CodeLM</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>

```

### 🆕 IntelligenceFlowAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/IntelligenceFlowAppIntentsExtension.appex/IntelligenceFlowAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.intelligenceflow.IntelligenceFlowAppIntentsExtension</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.intelligenceflow.IntelligenceFlowAppIntentsExtension</string>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Caches/com.apple.intelligenceflow.IntelligenceFlowAppIntentsExtension/</string>
		<string>/private/var/containers/Bundle/Application/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.apsd</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.CompanionLink</string>
		<string>com.apple.locationd.synchronous</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 MediaMLExtension

> `/System/Library/ExtensionKit/Extensions/MediaMLExtension.appex/MediaMLExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.MediaMLPluginApp.MediaMLExtension</string>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/com.apple.coremedia/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/MediaML/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.rtcreportingd</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
</dict>
</plist>

```
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.WebKit.Networking</string>
+	<key>com.apple.das.private.bgtask.continuedprocessing</key>
+	<true/>
+	<key>com.apple.das.private.bgtask.continuedprocessing.iconBundleIdentifier</key>
+	<true/>
 	<key>com.apple.developer.gpu-restricted</key>
 	<true/>
 	<key>com.apple.developer.web-browser-engine.networking</key>

```

### 🆕 PhotoPicker

> `/System/Library/ExtensionKit/Extensions/PhotoPicker.appex/PhotoPicker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobileslideshow.photo-picker</string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
	</array>
	<key>com.apple.developer.auto-elect-plugin</key>
	<true/>
	<key>com.apple.developer.sensitivecontentanalysis.client</key>
	<array>
		<string>analysis</string>
	</array>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobileslideshow.photo-picker</string>
	</dict>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>SensitiveContentAnalysis.UIInteraction</string>
		<string>SensitiveContentAnalysis.MediaAnalysis</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>inferenceFeaturesECR</string>
		<string>entitySubgraph</string>
		<string>entitySummary</string>
		<string>eventSubgraph</string>
		<string>peopleSubgraph</string>
		<string>appEntityRelevanceRanking</string>
		<string>personEntityRelevanceRanking</string>
		<string>loiEntityRelevanceRanking</string>
		<string>hasAssociationSubgraph</string>
	</array>
	<key>com.apple.private.keychain.sysbound</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.service.debug</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.mediaconversion</key>
	<true/>
	<key>com.apple.private.privacy.accounting.write</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screentime-communication</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
		<string>group.com.apple.Photos.PhotosFileProvider</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Media/PhotoData/Caches/</string>
		<string>/Media/PhotoData/PhotoCloudSharingData/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.compute.source</string>
		<string>com.apple.ScreenTimeAgent.communication</string>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.ManagedSettingsAgent.publisher</string>
		<string>com.apple.ManagedSettingsAgent</string>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.photoanalysisd</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.photos.picker</string>
		<string>com.apple.restrictionspassword</string>
		<string>com.apple.springboard</string>
	</array>
	<key>com.apple.sensitivecontentanalysis.service</key>
	<array>
		<string>photos</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.surfboard.allow-any-custom-shader</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```

### 🆕 PhotosDestructiveChangeConfirmation

> `/System/Library/ExtensionKit/Extensions/PhotosDestructiveChangeConfirmation.appex/PhotosDestructiveChangeConfirmation`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
</dict>
</plist>

```

### 🆕 PhotosEngagementExtension

> `/System/Library/ExtensionKit/Extensions/PhotosEngagementExtension.appex/PhotosEngagementExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 PhotosFileProvider

> `/System/Library/ExtensionKit/Extensions/PhotosFileProvider.appex/PhotosFileProvider`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.service.mediaconversion</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Containers/</string>
		<string>/Media/</string>
	</array>
</dict>
</plist>

```

### 🆕 PhotosMessagesApp

> `/System/Library/ExtensionKit/Extensions/PhotosMessagesApp.appex/PhotosMessagesApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
	</array>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.messages.private.AllowAllPresentationStyles</key>
	<true/>
	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>
	<true/>
	<key>com.apple.messages.private.AllowParticipantAddressAccess</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobileslideshow</string>
	</dict>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>inferenceFeaturesECR</string>
		<string>entitySubgraph</string>
		<string>entitySummary</string>
		<string>eventSubgraph</string>
		<string>peopleSubgraph</string>
		<string>appEntityRelevanceRanking</string>
		<string>personEntityRelevanceRanking</string>
		<string>loiEntityRelevanceRanking</string>
		<string>hasAssociationSubgraph</string>
	</array>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.mediaconversion</key>
	<true/>
	<key>com.apple.private.privacy.accounting.write</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
		<string>group.com.apple.Photos.PhotosFileProvider</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/PhotoData/</string>
		<string>/Media/DCIM/</string>
		<string>/Media/PhotoStreamsData/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Media/PhotoData/OutgoingTemp/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.photoanalysisd</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.surfboard.allow-any-custom-shader</key>
	<true/>
</dict>
</plist>

```

### 🆕 PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/PhotosPicker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobileslideshow.photospicker</string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
	</array>
	<key>com.apple.developer.auto-elect-plugin</key>
	<true/>
	<key>com.apple.developer.sensitivecontentanalysis.client</key>
	<array>
		<string>analysis</string>
	</array>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobileslideshow.photospicker</string>
	</dict>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>SensitiveContentAnalysis.UIInteraction</string>
		<string>SensitiveContentAnalysis.MediaAnalysis</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>inferenceFeaturesECR</string>
		<string>entitySubgraph</string>
		<string>entitySummary</string>
		<string>eventSubgraph</string>
		<string>peopleSubgraph</string>
		<string>appEntityRelevanceRanking</string>
		<string>personEntityRelevanceRanking</string>
		<string>loiEntityRelevanceRanking</string>
		<string>hasAssociationSubgraph</string>
	</array>
	<key>com.apple.private.keychain.sysbound</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.service.debug</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.mediaconversion</key>
	<true/>
	<key>com.apple.private.privacy.accounting.write</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screentime-communication</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
		<string>group.com.apple.Photos.PhotosFileProvider</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Media/PhotoData/Caches/</string>
		<string>/Media/PhotoData/PhotoCloudSharingData/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.compute.source</string>
		<string>com.apple.ScreenTimeAgent.communication</string>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.ManagedSettingsAgent.publisher</string>
		<string>com.apple.ManagedSettingsAgent</string>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.duetactivityscheduler</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.photos.picker</string>
		<string>com.apple.restrictionspassword</string>
		<string>com.apple.springboard</string>
	</array>
	<key>com.apple.sensitivecontentanalysis.service</key>
	<array>
		<string>photos</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.surfboard.allow-any-custom-shader</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```

### 🆕 PhotosTCCNotificationExtension

> `/System/Library/ExtensionKit/Extensions/PhotosTCCNotificationExtension.appex/PhotosTCCNotificationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
</dict>
</plist>

```
### PnROnDeviceWorker

> `/System/Library/ExtensionKit/Extensions/PnROnDeviceWorker.appex/PnROnDeviceWorker`

```diff

 		<dict>
 			<key>Streams</key>
 			<array>
+				<string>IntelligenceFlow.Transcript.Datastream</string>
 				<string>IntelligenceFlow.Telemetry</string>
-				<string>Sage.Transcript</string>
 			</array>
 		</dict>
 	</dict>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.analyticsd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
-		<string>com.apple.private.feedbacklogger</string>
+		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.siri.analytics.assistant</string>
 	</array>
 </dict>

```
### PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.email</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>MLHostTelemetry</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.email.maild</string>
 		<string>com.apple.mlhostd.xpc</string>
 		<string>com.apple.cloudd</string>
 	</array>

```
### PrivateMLClientInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService`

```diff

 	</array>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
-	<key>com.apple.privatecloudcompute.admin</key>
-	<true/>
 	<key>com.apple.privatecloudcompute.bundleIdentifierOverride</key>
 	<true/>
 	<key>com.apple.privatecloudcompute.prefetchRequest</key>

```

### 🆕 ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>379332956</string>
	<key>application-identifier</key>
	<string>com.apple.AppStore.ProductPageExtension</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.CoreTelephony.DataUsageInfo.allow</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.appleaccount.custodian</key>
	<true/>
	<key>com.apple.appstored.install-apps</key>
	<true/>
	<key>com.apple.appstored.private</key>
	<true/>
	<key>com.apple.appstored.update-apps</key>
	<true/>
	<key>com.apple.appstored.xpc.updates</key>
	<true/>
	<key>com.apple.attributionkitd.impression-intake</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.cdp.recoverykey</key>
	<true/>
	<key>com.apple.corerecents.recentsd</key>
	<true/>
	<key>com.apple.developer.associated-domains</key>
	<array/>
	<key>com.apple.developer.usernotifications.time-sensitive</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.itunescloud.in-app-message-service</key>
	<true/>
	<key>com.apple.itunesstored.metrics</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.absinthe</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.launchservices.receivereferrerrurl</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.passd.account</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.payment.amp-card-enrollment</key>
	<true/>
	<key>com.apple.payment.card-on-file</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.APODMLDESPlugin</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.PromotedContentPrediction.APOdmlSearchResultsExtension</key>
	<true/>
	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.accounts.customaccesssinfo</key>
	<true/>
	<key>com.apple.private.ap.idmanager</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstorecomponents.build-lockup-from-mapi-response</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Purchase</string>
		<string>Library</string>
		<string>IAPHistory</string>
		<string>Personalization</string>
		<string>Update</string>
		<string>PurchaseHistory</string>
		<string>AppCapabilities</string>
	</array>
	<key>com.apple.private.avatar.store</key>
	<true/>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.calendar.has-adopted-modern-request-access-methods</key>
	<true/>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.canIgnoreAppLinkOpenStrategy</key>
	<true/>
	<key>com.apple.private.cfnetwork.har-capture-amp</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.game-center</key>
	<array>
		<string>Account</string>
		<string>Authenticate</string>
		<string>Profile</string>
		<string>Friends</string>
		<string>Games</string>
		<string>Scores</string>
		<string>Achievements</string>
		<string>Challenges</string>
		<string>Multiplayer</string>
		<string>TurnBasedMultiplayer</string>
		<string>GameStats</string>
	</array>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.hsa-authentication-processing</key>
	<true/>
	<key>com.apple.private.iad.news-client</key>
	<true/>
	<key>com.apple.private.iad.opt-in-control</key>
	<true/>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.ids.remoteurlconnection</key>
	<true/>
	<key>com.apple.private.in-app-payments</key>
	<true/>
	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>
	<string>*</string>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.security.storage.triald</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.swc.additional-service-details-consumer</key>
	<true/>
	<key>com.apple.private.swc.system-app</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount</string>
		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>
		<string>/Library/Trial/NamespaceDescriptors/</string>
		<string>/Library/Trial/Treatments/511/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.storeservices/</string>
		<string>/Library/com.apple.itunesstored/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Logs/com.apple.StoreServices/</string>
		<string>/Library/Caches/JetPackCache/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.attributionkitd.xpc.impression-intake</string>
		<string>com.apple.ap.promotedcontent.pcinterface</string>
		<string>com.apple.ap.promotedcontent.mescalinterface</string>
		<string>com.apple.appstored.xpc.storequeue</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.ap.promotedcontent.metrics</string>
		<string>com.apple.ap.promotedcontent.supportinterface</string>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.corerecents.recentsd</string>
		<string>com.apple.appstored.xpc.jobmanager</string>
		<string>com.apple.appstored.xpc.request</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.appstored.xpc.updates</string>
		<string>com.apple.symptom_analytics</string>
		<string>com.apple.ap.adprivacyd.idmanager</string>
		<string>com.apple.ap.adprivacyd.opt-out</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.itunescloud.in-app-message-service</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.hsa-authentication-server</string>
		<string>com.apple.ap.adprivacyd.store</string>
		<string>com.apple.aa.custodian.xpc</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.payment.all-access</string>
		<string>com.apple.cards.all-access</string>
		<string>com.apple.passd.account</string>
		<string>com.apple.xpc.amsserverdatacacheservice</string>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.symptom_diagnostics</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.appstored</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AdLib</string>
		<string>com.apple.gamecenter</string>
		<string>com.apple.AppStore</string>
		<string>com.apple.AppStore.ProductPageExtension</string>
		<string>com.apple.AppStore.SubscribePageExtension</string>
		<string>com.apple.Fitness</string>
		<string>com.apple.itunesstored</string>
		<string>com.apple.springboard</string>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.AdPlatforms</string>
	</array>
	<key>com.apple.security.system-group-containers</key>
	<array>
		<string>systemgroup.com.apple.VideoSubscriberAccount</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.telephony.cupolicy-rw-access</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>511</string>
		<string>512</string>
	</array>
	<key>fairplay-client</key>
	<string>1699554724</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.VideoSubscriberAccount</string>
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
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.intelligenceflow.internal</key>

 		<string>com.apple.MobileAsset.UAF.FM.com.apple.security.temporaryGenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
 	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>SearchToolExtension</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>IntelligenceFlow.SearchToolTelemetry</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>peopleSubgraph</string>

 	<true/>
 	<key>com.apple.private.security.no-container</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.siri.referenceResolution</string>
+	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.app-server</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.siri.referenceResolution</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

 		<string>AGXDevice</string>
 		<string>H11ANEInDirectPathClient</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.personal-information.calendars</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/System/Library/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/purpose_auto/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>337</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>appleaccount</string>
+		<string>apple</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 SensitiveContentAnalysisConfigurationExtension

> `/System/Library/ExtensionKit/Extensions/SensitiveContentAnalysisConfigurationExtension.appex/SensitiveContentAnalysisConfigurationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.sensitivecontentanalysis.client</key>
	<array>
		<string>analysis</string>
	</array>
</dict>
</plist>

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin`

```diff

 	<string>com.apple.siri.SiriSuggestionsLightHousePlugin</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siri.SiriSuggestionsLightHousePlugin</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
 	<key>com.apple.linkd.registry</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siriinferenced.remembers</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.siriinferenced</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siriinferenced.remembers</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.siriinferenced</string>

```

### 🆕 SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>379332956</string>
	<key>application-identifier</key>
	<string>com.apple.AppStore.SubscribePageExtension</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.CoreTelephony.DataUsageInfo.allow</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.appleaccount.custodian</key>
	<true/>
	<key>com.apple.appstored.install-apps</key>
	<true/>
	<key>com.apple.appstored.private</key>
	<true/>
	<key>com.apple.appstored.update-apps</key>
	<true/>
	<key>com.apple.appstored.xpc.updates</key>
	<true/>
	<key>com.apple.attributionkitd.impression-intake</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.cdp.recoverykey</key>
	<true/>
	<key>com.apple.corerecents.recentsd</key>
	<true/>
	<key>com.apple.developer.associated-domains</key>
	<array/>
	<key>com.apple.developer.usernotifications.time-sensitive</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.itunescloud.in-app-message-service</key>
	<true/>
	<key>com.apple.itunesstored.metrics</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.absinthe</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.launchservices.receivereferrerrurl</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.passd.account</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.payment.amp-card-enrollment</key>
	<true/>
	<key>com.apple.payment.card-on-file</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.APODMLDESPlugin</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.PromotedContentPrediction.APOdmlSearchResultsExtension</key>
	<true/>
	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.accounts.customaccesssinfo</key>
	<true/>
	<key>com.apple.private.ap.idmanager</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstorecomponents.build-lockup-from-mapi-response</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Purchase</string>
		<string>Library</string>
		<string>IAPHistory</string>
		<string>Personalization</string>
		<string>Update</string>
		<string>PurchaseHistory</string>
		<string>AppCapabilities</string>
	</array>
	<key>com.apple.private.avatar.store</key>
	<true/>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.calendar.has-adopted-modern-request-access-methods</key>
	<true/>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.canIgnoreAppLinkOpenStrategy</key>
	<true/>
	<key>com.apple.private.cfnetwork.har-capture-amp</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.game-center</key>
	<array>
		<string>Account</string>
		<string>Authenticate</string>
		<string>Profile</string>
		<string>Friends</string>
		<string>Games</string>
		<string>Scores</string>
		<string>Achievements</string>
		<string>Challenges</string>
		<string>Multiplayer</string>
		<string>TurnBasedMultiplayer</string>
		<string>GameStats</string>
	</array>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.hsa-authentication-processing</key>
	<true/>
	<key>com.apple.private.iad.news-client</key>
	<true/>
	<key>com.apple.private.iad.opt-in-control</key>
	<true/>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.ids.remoteurlconnection</key>
	<true/>
	<key>com.apple.private.in-app-payments</key>
	<true/>
	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>
	<string>*</string>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.security.storage.triald</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.swc.additional-service-details-consumer</key>
	<true/>
	<key>com.apple.private.swc.system-app</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount</string>
		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>
		<string>/Library/Trial/NamespaceDescriptors/</string>
		<string>/Library/Trial/Treatments/511/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.storeservices/</string>
		<string>/Library/com.apple.itunesstored/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Logs/com.apple.StoreServices/</string>
		<string>/Library/Caches/JetPackCache/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.attributionkitd.xpc.impression-intake</string>
		<string>com.apple.ap.promotedcontent.pcinterface</string>
		<string>com.apple.ap.promotedcontent.mescalinterface</string>
		<string>com.apple.appstored.xpc.storequeue</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.ap.promotedcontent.metrics</string>
		<string>com.apple.ap.promotedcontent.supportinterface</string>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.corerecents.recentsd</string>
		<string>com.apple.appstored.xpc.jobmanager</string>
		<string>com.apple.appstored.xpc.request</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.appstored.xpc.updates</string>
		<string>com.apple.symptom_analytics</string>
		<string>com.apple.ap.adprivacyd.idmanager</string>
		<string>com.apple.ap.adprivacyd.opt-out</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.itunescloud.in-app-message-service</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.hsa-authentication-server</string>
		<string>com.apple.ap.adprivacyd.store</string>
		<string>com.apple.aa.custodian.xpc</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.payment.all-access</string>
		<string>com.apple.cards.all-access</string>
		<string>com.apple.passd.account</string>
		<string>com.apple.xpc.amsserverdatacacheservice</string>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.symptom_diagnostics</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.appstored</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AdLib</string>
		<string>com.apple.gamecenter</string>
		<string>com.apple.AppStore</string>
		<string>com.apple.AppStore.ProductPageExtension</string>
		<string>com.apple.AppStore.SubscribePageExtension</string>
		<string>com.apple.Fitness</string>
		<string>com.apple.itunesstored</string>
		<string>com.apple.springboard</string>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.AdPlatforms</string>
	</array>
	<key>com.apple.security.system-group-containers</key>
	<array>
		<string>systemgroup.com.apple.VideoSubscriberAccount</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.telephony.cupolicy-rw-access</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>511</string>
		<string>512</string>
	</array>
	<key>fairplay-client</key>
	<string>1699554724</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.VideoSubscriberAccount</string>
	</array>
</dict>
</plist>

```

### 🆕 TGOnDeviceInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/TGOnDeviceInferenceProviderService.appex/TGOnDeviceInferenceProviderService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.tgondeviceinferenceproviderservice</string>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.aned.private.adapterWeight.allow</key>
	<true/>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.aned.private.processModelShare.allow</key>
	<true/>
	<key>com.apple.appattest.spi</key>
	<true/>
	<key>com.apple.developer.ane.increased-model-size-limit</key>
	<true/>
	<key>com.apple.devicecheck.extension-client</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.private.ane.allow-set-client-hints</key>
	<true/>
	<key>com.apple.private.ane.allow-share-coalition-hints</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.CodeLM</string>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
	</array>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.tgondeviceinferenceproviderservice</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
		<string>GenerativeExperiences.TransparencyLog</string>
	</array>
	<key>com.apple.private.memory.ownership_transfer</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/compiled/e5bundlecache/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.InferenceProviderService/</string>
		<string>/private/var/mobile/Library/Caches/com.apple.InferenceProviderService/</string>
		<string>/private/var/mobile/tmp/</string>
		<string>/private/var/tmp/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>ANEClientHintsUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appleneuralengine</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.tokengeneration</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>IOSurfaceAcceleratorClient</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.mobileactivationd</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/db/com.apple.modelcatalog/protected/compiled/e5bundlecache/</string>
		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/Library/Preferences/com.apple.tokengeneration.plist</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appleneuralengine</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.mediaanalysisd.service.public</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.tokengeneration</string>
	</array>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
</dict>
</plist>

```

### 🆕 TelemetryAggregator

> `/System/Library/ExtensionKit/Extensions/TelemetryAggregator.appex/TelemetryAggregator`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.DifferentialPrivacy.TelemetryAggregator</string>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.dprivacyd.metadata.allow</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Lighthouse.Ledger.DediscoPrivacyEvent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.mlhost</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.mlhost</string>
	</array>
</dict>
</plist>

```

### 🆕 VisualGenerationInference

> `/System/Library/ExtensionKit/Extensions/VisualGenerationInference.appex/VisualGenerationInference`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.VisualGeneration.inference</string>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.aned.private.adapterWeight.allow</key>
	<true/>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.aned.private.processModelShare.allow</key>
	<true/>
	<key>com.apple.developer.ane.increased-model-size-limit</key>
	<true/>
	<key>com.apple.devicecheck.extension-client</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
		<string>SerialNumber</string>
		<string>UniqueChipID</string>
	</array>
	<key>com.apple.private.ane.allow-set-client-hints</key>
	<true/>
	<key>com.apple.private.ane.allow-share-coalition-hints</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
	</array>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.VisualGeneration.inference</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
		<string>GenerativeExperiences.TransparencyLog</string>
	</array>
	<key>com.apple.private.memory.ownership_transfer</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/mobile/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/compiled/e5bundlecache/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.VisualGeneration.inference/</string>
		<string>/private/var/mobile/Library/Caches/com.apple.VisualGeneration.inference/</string>
		<string>/private/var/mobile/tmp/</string>
		<string>/private/var/tmp/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>ANEClientHintsUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appleneuralengine</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.tests.callbackService</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>ANEClientHintsUserClient</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.mobileactivationd</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/db/com.apple.modelcatalog/protected/compiled/e5bundlecache/</string>
		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.VisualGeneration.inference/</string>
		<string>/Library/Caches/com.apple.modelmanager.homedirworkaround/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appleneuralengine</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.mediaanalysisd.service.public</string>
	</array>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
</dict>
</plist>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>com.apple.accessibility.cache.*</string>
 		<string>com.apple.coreservices.launchservices.session.*</string>
 		<string>user.uid.501.syslog.*</string>
+		<string>CPActiveCountryCodeChanged.Internal</string>
+		<string>MCManagedBooksChanged</string>
+		<string>PINPolicyChangedNotification</string>
+		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
 		<string>com.apple.ManagedConfiguration.profileListChanged</string>
+		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>
 		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
 		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
 		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
 		<string>com.apple.UIKit.InternalPreferences</string>
+		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
+		<string>com.apple.managedconfiguration._UUID_</string>
+		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
 		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
 		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
 		<string>com.apple.managedconfiguration.defaultsdidchange</string>

 		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
 		<string>com.apple.mobile.keybagd.lock_status</string>
 		<string>com.apple.mobile.keybagd.user_changed</string>
+		<string>com.apple.system.thermalpressurelevel</string>
 		<string>__ABDataBaseChangedByOtherProcessNotification</string>
 		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
 		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>

 		<string>com.apple.CFNetwork.har-capture-update</string>
 		<string>com.apple.CFPreferences._domainsChangedExternally</string>
 		<string>com.apple.LaunchServices.database</string>
+		<string>com.apple.UIKit.LoggingPreferences</string>
 		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
 		<string>com.apple.WebKit.deleteAllCode</string>
 		<string>com.apple.WebKit.dumpGCHeap</string>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>com.apple.accessibility.cache.*</string>
 		<string>com.apple.coreservices.launchservices.session.*</string>
 		<string>user.uid.501.syslog.*</string>
+		<string>CPActiveCountryCodeChanged.Internal</string>
+		<string>MCManagedBooksChanged</string>
+		<string>PINPolicyChangedNotification</string>
+		<string>com.apple.ManagedConfiguration.managedAppsChanged</string>
 		<string>com.apple.ManagedConfiguration.profileListChanged</string>
+		<string>com.apple.ManagedConfiguration.removedSystemAppsChanged</string>
 		<string>com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.LinguisticDataAuto^ASSET_VERSION_DOWNLOADED</string>
 		<string>com.apple.MobileAsset.LinguisticData.dds.assets-updated</string>
 		<string>com.apple.MobileAsset.LinguisticData.new-asset-installed</string>
 		<string>com.apple.UIKit.InternalPreferences</string>
+		<string>com.apple.WebKit.WebContent.showUntrackedDerefs</string>
+		<string>com.apple.managedconfiguration._UUID_</string>
+		<string>com.apple.managedconfiguration.allowpasscodemodificationchanged</string>
 		<string>com.apple.managedconfiguration.appwhitelistdidchange</string>
 		<string>com.apple.managedconfiguration.clientrestrictionschanged</string>
 		<string>com.apple.managedconfiguration.defaultsdidchange</string>

 		<string>com.apple.mobile.usermanagerd.foregrounduser_changed</string>
 		<string>com.apple.mobile.keybagd.lock_status</string>
 		<string>com.apple.mobile.keybagd.user_changed</string>
+		<string>com.apple.system.thermalpressurelevel</string>
 		<string>__ABDataBaseChangedByOtherProcessNotification</string>
 		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
 		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>

 		<string>com.apple.CFNetwork.har-capture-update</string>
 		<string>com.apple.CFPreferences._domainsChangedExternally</string>
 		<string>com.apple.LaunchServices.database</string>
+		<string>com.apple.UIKit.LoggingPreferences</string>
 		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
 		<string>com.apple.WebKit.deleteAllCode</string>
 		<string>com.apple.WebKit.dumpGCHeap</string>

```
### ZeoliteExtension

> `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.lighthouse.ZeoliteExtension</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.lighthouse.ZeoliteExtension</string>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MLHostTask</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 	<array>
 		<string>Zeolite.Ledger.Embedding</string>
 	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>Zeolite.Ledger.Embedding</string>

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
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
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.mlhost</string>
+		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>com.apple.gms.availability</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.zeolite</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/System/Library/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.email.maild</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
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
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.photos.service.librarymanagement</key>
+	<true/>
 	<key>com.apple.private.protectedcloudstorage.keysyncing</key>
 	<true/>
 	<key>com.apple.private.rsr-cryptex-access</key>

```
### attributionkitd

> `/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd`

```diff

 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.attributionkitd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>AggregatedReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AdAttributionKit.AggregatedReporting.Conversion</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>AdAttributionKit.AggregatedReporting.Purchase</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.fileprovider.enumerate</key>
+	<true/>
 	<key>com.apple.imdpersistence.IMDPersistenceAgent-Syndication</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```

### 🆕 BrowserEngineKit.Intermediary

> `/System/Library/Frameworks/BrowserEngineKit.framework/XPCServices/BrowserEngineKit.Intermediary.xpc/BrowserEngineKit.Intermediary`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.DocumentManagerCore.Downloads</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.DocumentManager.defaults</string>
		<string>com.apple.iclouddrive.features</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.BrowserEngineKit.Intermediary</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.spotlightknowledged</string>
+	<key>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</key>
+	<true/>
 	<key>com.apple.apfs.unlock</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.private.spotlight.openjournal</key>
 	<true/>
+	<key>com.apple.private.suggestions.spotlightknowledged</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.SetStoreUpdateService</string>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
+	<key>com.apple.private.coreservices.appmarketplace.read</key>
+	<true/>
+	<key>com.apple.private.coreservices.appmarketplace.write</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.install.can-set-install-requestor</key>
+	<true/>
 	<key>com.apple.private.install.distributor-info-source</key>
 	<true/>
 	<key>com.apple.private.marketplace-extension-host</key>

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.runningboard.jetengine</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

```
### com.apple.SafariServices.ContentBlockerLoader

> `/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader`

```diff

 	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Applications/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Safari/</string>

```
### shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

 	<true/>
 	<key>com.apple.security.device.microphone</key>
 	<true/>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/com.apple.PrivacyDisclosure/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.locationd.synchronous</string>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/ASRAssetOverrides/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 		<string>/Library/Assistant/SiriVocabulary/</string>
 	</array>

```

### 🆕 CoreRCPlugin

> `/System/Library/HIDPlugins/SessionFilters/CoreRCPlugin.plugin/CoreRCPlugin`

- No entitlements *(yet)*

### 🆕 HealthAppDiagnosticExtensionPlugin

> `/System/Library/Health/DiagnosticExtensionPlugins/HealthAppDiagnosticExtensionPlugin.bundle/HealthAppDiagnosticExtensionPlugin`

- No entitlements *(yet)*

### 🆕 DefaultAppsSettingsUIPlugin

> `/System/Library/PreferenceBundles/DefaultAppsSettingsUIPlugin.bundle/DefaultAppsSettingsUIPlugin`

- No entitlements *(yet)*

### 🆕 VolumeLimitSettings

> `/System/Library/PreferenceBundles/VolumeLimitSettings.bundle/VolumeLimitSettings`

- No entitlements *(yet)*
### com.apple.AVConference.Diagnostic

> `/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/com.apple.AVConference.Diagnostic`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.VideoConference/</string>
+		<string>/var/mobile/Library/Caches/com.apple.VideoConference/logs</string>
+		<string>/var/mobile/Library/Logs/CrashReporter/</string>
+		<string>/var/mobile/Library/Logs/RTCReporting/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/avconference/</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/Logs/RTCReporting/</string>
-	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/var/root/Library/RTCReporting</string>
 		<string>/private/var/root/Library/Logs/RTCReporting</string>
+		<string>/Library/Logs/DiagnosticReports/</string>
+		<string>/Library/Logs/DiagnosticReports/Retired</string>
+		<string>/private/var/tmp</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>/Library/Caches/com.apple.VideoConference/</string>
-		<string>/Library/Logs/DiagnosticReports/</string>
+		<string>/Library/Caches/com.apple.VideoConference/logs</string>
 	</array>
 </dict>
 </plist>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<true/>
 	<key>com.apple.springboard.setbadgestring</key>
 	<true/>
+	<key>com.apple.springboard.swapIconsInProminentPositions</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	<array>
 		<string>apple</string>
 		<string>com.apple.asd</string>
+		<string>com.apple.applemediaservices.multiuser</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.MobileInternetSharing.allow</key>
 	<true/>
+	<key>com.apple.NeighborhoodActivityConduitService</key>
+	<true/>
 	<key>com.apple.PairingManager.Read</key>
 	<true/>
 	<key>com.apple.PairingManager.Write</key>

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.locationd.absolute_altimeter</key>
+	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 		<string>Siri.Health.Federated</string>
 		<string>SiriExecution</string>
 		<string>PostSiriEngagement</string>
+		<string>Siri.Orchestration.RequestContext</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>SiriPrivateLearningSELFEvent</string>
 		<string>SiriIntentEvents</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.orchestration.intelligencesession</string>
 		<string>com.apple.facetimemessagestored.service</string>
+		<string>com.apple.NeighborhoodActivityConduitService</string>
 		<string>com.apple.siri.location</string>
 		<string>com.apple.tipsd.assistant</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>

 	<true/>
 	<key>com.apple.siri.location</key>
 	<true/>
+	<key>com.apple.siri.orchestration.intelligencesession</key>
+	<true/>
 	<key>com.apple.siri.pommes_search_xpc_service</key>
 	<true/>
 	<key>com.apple.siriinferenced</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.atvcached.client</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>

 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.borealis</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<array>
 		<string>App.InFocus</string>
 		<string>App.Intent</string>
+		<string>App.Intents.Transcript</string>
 		<string>CarPlay</string>
 		<string>Clock.Alarm</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>HomeKit.Client.AccessoryControl</string>
+		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification</string>
 		<string>Notification.Usage</string>
-		<string>Sage.Transcript</string>
 		<string>Siri.Metrics.OnDeviceDigestExperimentMetrics</string>
 		<string>Siri.Metrics.OnDeviceDigestSegmentsCohorts</string>
 		<string>Siri.Metrics.OnDeviceDigestUsageMetrics</string>

 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Application Support/com.apple.FaceTime/</string>
+		<string>/Library/ASRAssetOverrides/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/SyncedIntentDefinitions/</string>
 		<string>/Library/Trial/</string>

 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.purplebuddy</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.SiriCarouselAlert</string>
 		<string>com.apple.SiriViewService</string>
 		<string>com.apple.TelephonyUtilities</string>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.network.server</key>
+	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.system-group-containers</key>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.Biome</key>
 	<true/>
 	<key>com.apple.private.security.storage.IntelligencePlatform</key>

 	<true/>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>
 	<true/>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/db/biome/</string>
+		<string>/private/var/PersonalDeviceVolumes/</string>
+		<string>/private/var/mobile/Containers/Data/InternalDaemon/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.spaceattributiond</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<array>
 		<string>1152</string>
 	</array>
+	<key>com.apple.uservault</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### SetStoreUpdateService

> `/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/tmp/com.apple.biomesyncd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.cascade.SetChangeRelayService</string>

```
### CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic`

```diff

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/db/</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>kCFPreferencesAnyApplication</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 		<string>AppleKeyStoreUserClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>
-	<key>com.apple.security.network.client</key>
-	<true/>
 	<key>com.apple.shortcuts.library-read-access</key>
 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>

 		<string>755</string>
 		<string>1630</string>
 	</array>
+	<key>com.apple.uservault</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Config</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>

 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/tmp/com.apple.siri-distributed-evaluation/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/PersonalDeviceVolumes/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/ASRAssetOverrides/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.uservault</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<true/>
 	<key>com.apple.datadetectors.source-write.system</key>
 	<true/>
+	<key>com.apple.developer.networking.multipath</key>
+	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```

### 🆕 CoreRCHIDService

> `/System/Library/PrivateFrameworks/CoreRC.framework/PlugIns/CoreRCHIDService.plugin/CoreRCHIDService`

- No entitlements *(yet)*

### 🆕 CECIOCECInterfaceListener

> `/System/Library/PrivateFrameworks/CoreRC.framework/PlugIns/InterfacePlugins/CECIOCECInterfaceListener.plugin/CECIOCECInterfaceListener`

- No entitlements *(yet)*
### CoreRepairCoreXPCService

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/XPCServices/CoreRepairCoreXPCService.xpc/CoreRepairCoreXPCService`

```diff

 	<true/>
 	<key>com.apple.private.vfs.snapshot</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ctkd.token-client</string>

```
### CoreRoutineHelperService

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.security.storage.CoreRoutine</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>routined</string>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.assistant.domain.audio.level.client.provider</key>
+	<true/>
 	<key>com.apple.assistant.domain.preferences.notifier</key>
 	<true/>
 	<key>com.apple.assistant.domain.status.access</key>

 					<string>read-only</string>
 				</dict>
 			</dict>
+			<key>Streams</key>
+			<dict>
+				<key>CarPlay.Connected</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
 		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

 		<string>/private/var/MobileAsset/</string>
 		<string>/Library/Audio/Tunings/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/PersonalDeviceVolumes/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/ASRAssetOverrides/</string>
 		<string>/Library/CoreDuet/</string>
 		<string>/Library/PeopleSuggester/</string>
 		<string>/Library/Caches/com.apple.corespeech.cat.xpc/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.perceptiond.entitykit</string>
 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.server.bluetooth</string>
 		<string>com.apple.server.bluetooth.general.xpc</string>

 		<string>com.apple.assistant.domain.validation.service</string>
 		<string>com.apple.assistant.domain.system.settings.service</string>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.uservault</string>
+		<string>com.apple.assistant.domain.audio.level.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### suggest_tool

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool`

```diff

 	<true/>
 	<key>com.apple.private.suggestions.reminders</key>
 	<true/>
+	<key>com.apple.private.suggestions.spotlightknowledged</key>
+	<true/>
 	<key>com.apple.private.suggestions.urls</key>
 	<true/>
 	<key>com.apple.private.tcc.allow.overridable</key>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<true/>
 	<key>com.apple.private.suggestions.reminders</key>
 	<true/>
+	<key>com.apple.private.suggestions.spotlightknowledged</key>
+	<true/>
 	<key>com.apple.private.suggestions.urls</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

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

### 🆕 EventKitSyncDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/EventKitSyncDiagnosticExtension.appex/EventKitSyncDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/EventKitSyncServices/Diagnostics/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.EventKitSyncServices.server</string>
	</array>
</dict>
</plist>

```
### donotdisturbd

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd`

```diff

 		<string>com.apple.link-extension</string>
 		<string>com.apple.appintents-extension</string>
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
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.linkd.registry</key>

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
-		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

 		<string>com.apple.conference</string>
 		<string>com.apple.AppSupport</string>
 		<string>com.apple.SiriViewService</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.registration</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### textunderstandingd

> `/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/Support/textunderstandingd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.textunderstandingd</string>
 	<key>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</key>
 	<true/>
 	<key>com.apple.TextUnderstanding.DocumentUpdateHandler</key>

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>
 		<string>photos.person</string>

 		<string>TextUnderstanding.DocumentUnderstanding.PoemBuffer</string>
 		<string>TextUnderstanding.DocumentUnderstanding.Poem</string>
 		<string>TextUnderstanding.DocumentUnderstanding.PoemAnalytics</string>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
 	<key>com.apple.private.corespotlight.bundleid</key>
 	<string>com.apple.FileProvider.LocalStorage</string>

 		<string>appEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
 	</array>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.TextUnderstanding</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<true/>
 	<key>com.apple.proactive.experiments.responses</key>
 	<true/>
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
 		<string>com.apple.TextUnderstanding.SmartReplies.Inference</string>

 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.mediaanalysisd.client</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.biome.access.user</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 		<string>AGXDevice</string>
 		<string>H11ANEInDirectPathClient</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.modelmanager</string>
+	</array>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>SMART_REPLY_EN</string>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled`

```diff

 	</dict>
 	<key>com.apple.private.followup</key>
 	<true/>
-	<key>com.apple.private.groupkit.allgroups</key>
-	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screentime-setup</key>

 		<string>com.apple.ScreenTimeAgent.private</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.identityservicesd.pds</string>
-		<string>com.apple.groupkitd.xpc.groupservice</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### FedStatsMLRPlugin

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/FedStatsMLRPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStats.Plugin</string>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>WalletPaymentsCommerce.FinancialInsights.Search</string>
 		<string>WalletPaymentsCommerce.FinancialInsights.PaymentRingSuggestions</string>
 		<string>Photos.UserAnalytics</string>
-		<string>Moments.Stats.EventData</string>
 		<string>Keyboard.TokenFrequency</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Location.Semantic</string>

 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>MediaAnalysis.PEC.Processing</string>
 		<string>Safari.PageLoad</string>
 		<string>Siri.Health.Federated</string>
 		<string>AppleID.ChildSetup</string>

 		<string>Safari.WindowProxy</string>
 		<string>Siri.AssistantSuggestionFeatures</string>
 		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
+		<string>CommCenter.Call.EmergencyVoiceCall</string>
+		<string>Location.Emergency.SessionStart</string>
+		<string>Safari.MemoryFootprint</string>
+		<string>Mail.Recategorization</string>
 		<string>Photos.MemoryCreation</string>
-		<string>Photos.Memories.Curation</string>
+		<string>Photos.Curation</string>
 		<string>Photos.Delete</string>
+		<string>Photos.Search</string>
+		<string>Photos.Memories.Shared</string>
+		<string>Photos.Memories.Viewed</string>
+		<string>AeroML.Insights.PhotosSearchInsights</string>
+		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
+		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>
+		<string>CameraCapture.AutoFocusROI</string>
+		<string>Photos.Style</string>
+		<string>WalletPaymentsCommerce.FinancialInsights.RecurringSendSuggestions</string>
+		<string>Safari.Browsing.Assistant</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>1549</string>
 		<string>1550</string>
 		<string>1551</string>
+		<string>1552</string>
+		<string>1555</string>
+		<string>1557</string>
+		<string>1850</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### FedStatsMLRPluginClassB

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/FedStatsMLRPluginClassB`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStats.PluginClassB</string>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### FedStatsMLRPluginNonDnU

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/FedStatsMLRPluginNonDnU`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStatsPlugin.NonDnU</string>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

```
### DraftingExtension-iOS

> `/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.siri</key>
+	<true/>
 	<key>com.apple.diagnosticextensionsd.xpcclient</key>
 	<true/>
 	<key>com.apple.feedbackd.admin</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	</array>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
+	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 		<string>com.apple.MobileAsset.LinguisticData</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 	</array>
 	<key>com.apple.private.assistant.settings</key>
 	<true/>

 	<array>
 		<string>/private/var/mobile/Library/UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_Planner/purpose_auto/</string>

 		<string>com.apple.SummarizationKit</string>
 		<string>com.apple.EmojiPreferences</string>
 		<string>com.apple.AppSupport</string>
+		<string>com.apple.CloudSubscriptionFeatures</string>
 		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>

```
### homeenergyd

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.energykit</string>
+	<key>com.apple.developer.weatherkit</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
+	<key>com.apple.private.homekit.home-location</key>
+	<true/>
+	<key>com.apple.private.homekit.location</key>
+	<true/>
 	<key>com.apple.private.homekit.messaging</key>
 	<true/>
 	<key>com.apple.private.homekit.modern-messaging</key>

 		<string>com.apple.Home</string>
 		<string>com.apple.HomeEnergyDaemon</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.weather</string>
+	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Application Support/com.apple.homeenergyd/</string>
+		<string>/private/var/mobile/Library/Caches/EnergyKit/</string>
 		<string>/private/var/mobile/Library/homeenergyd/</string>
 		<string>/private/var/mobile/Library/homeenergyd/com.apple.homeenergyd/</string>
+		<string>/private/var/mobile/Library/Weather/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>/Library/Caches/com.apple.HomeKit.configurations/</string>
 		<string>/Library/Caches/com.apple.HomeKit/</string>
 		<string>/Library/Caches/com.apple.homeenergyd/</string>
+		<string>/Library/Caches/EnergyKit/</string>
 		<string>/Library/HTTPStorages/com.apple.homeenergyd/</string>
+		<string>/Library/Weather/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.weatherkit.authservice</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.homekit.background-mode</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.private.homeenergy</key>
 	<true/>
+	<key>com.apple.private.homekit</key>
+	<true/>
 	<key>com.apple.private.ids.activity.monitor</key>
 	<array>
 		<string>com.apple.private.alloy.willow-com.apple.HomeKit</string>

 	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.homed</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>HomeServiceAreaDonation</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>HomeKit.HomeServiceArea</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.octagon</key>

 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceWillow</string>
 	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>

 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.StatusKit.presence</string>
 		<string>com.apple.wifi.manager-access</string>
+		<string>com.apple.matter.native.xpc</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.SetStoreUpdateService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 HomeKitEventsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HomeKitEvents.framework/PlugIns/HomeKitEventsDiagnosticExtension.appex/HomeKitEventsDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.home.hindsight.utility</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/com.apple.homeeventsd/diagnostics/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.homekitevents.xpc</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.HomeKitEvents.HomeKitEventsDiagnosticExtension</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### IDSBlastDoorService

> `/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
+	<false/>
+	<key>com.apple.coregraphics.disableinmemoryfonts</key>
+	<true/>
+	<key>com.apple.coregraphics.disablepdf</key>
+	<true/>
+	<key>com.apple.imageio.allowabletypes</key>
+	<array/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>IDSBlastDoor</string>
+	<key>com.apple.private.coremedia.allowabletypecategories</key>
+	<array/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
 	<key>com.apple.private.security.enable-state-flags</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.kvsd</string>
 		<string>com.apple.aps.kvsd</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

 		<string>com.apple.transparencyd</string>
 		<string>com.apple.spotlight.SearchAgent</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.lsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.nanobuddy</string>
 		<string>com.apple.communicationSafetySettings</string>
+		<string>com.apple.MobileSMS.CKDNDList</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.conference</string>
 		<string>com.apple.ClarityUI.Messages</string>
+		<string>com.apple.messages.critical-messaging.storage</string>
+		<string>com.apple.Messages.InstallationState</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### IMTranscoderAgent

> `/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent`

```diff

 		<string>com.apple.geod</string>
 		<string>com.apple.commcenter.xpc</string>
 		<string>com.apple.coremedia.decompressionsession</string>
+		<string>com.apple.uservault</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>com.apple.uservault</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>IMTranscoderAgent</string>

```
### installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

 	<true/>
 	<key>com.apple.private.MobileInstallationHelperService.allowed</key>
 	<true/>
+	<key>com.apple.private.coreservices.appmarketplace.read</key>
+	<true/>
 	<key>com.apple.private.coreservices.can-send-install-notifications</key>
 	<true/>
 	<key>com.apple.private.domain-extension</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
+	<key>com.apple.private.ids.registration</key>
+	<array>
+		<string>com.apple.madrid</string>
+	</array>
 	<key>com.apple.private.installcoordinationd.daemon</key>
 	<true/>
 	<key>com.apple.private.managed-settings.override</key>

 		<string>UpdateSinfForInstallCoordination</string>
 		<string>UpdateiTunesMetadataForInstallCoordination</string>
 	</array>
+	<key>com.apple.private.photos.service.internal.cloud</key>
+	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServicePhotos</string>
+	</array>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
 		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>

 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.nanoprefsync</string>
 		<string>com.apple.managedappdistributiond.installcoordination</string>
+		<string>com.apple.photos.service</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	<string>com.apple.intelligenceflow.intelligencecontextd</string>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
+	<key>com.apple.QuartzCore.global-capture</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.Knosis</key>

 			<key>Streams</key>
 			<array>
 				<string>App.InFocus</string>
-				<true/>
 				<string>Siri.Orchestration.RequestContext</string>
-				<true/>
 				<string>Siri.ContextRefreshTriggers</string>
-				<true/>
 			</array>
 		</dict>
 	</dict>

 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screencapturekit.noprompt</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.intelligenceflow</string>

 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceScreenCapture</string>
+	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
 		<string>kTCCServiceCalendar</string>

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.intelligenceflow</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.naturallanguaged/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/SiriReferenceResolution/</string>

 		<string>/Library/Caches/com.apple.intelligenceflow.intelligencecontextd/</string>
 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 		<string>/Library/Assistant/SiriVocabulary/</string>
+		<string>/Library/Shortcuts/</string>
+	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>AppleAVEUserClient</string>
+		<string>AppleAVE2UserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.siri.morphunassetsupdaterd</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.lsd.mapdb</string>
+		<string>com.apple.coremedia.videocodecd.decompressionsession</string>
+		<string>com.apple.coremedia.videocodecd.compressionsession</string>
+		<string>com.apple.coremedia.admin</string>
+		<string>com.apple.FileCoordination</string>
+		<string>com.apple.CARenderServer</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.dmd.policy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.siri.morphun</string>
 		<string>com.apple.assistant</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>H11ANEInDirectPathClient</string>
+		<string>AppleJPEGDriverUserClient</string>
+		<string>IOSurfaceRootUserClient</string>
+		<string>IOSurfaceAcceleratorClient</string>
+		<string>IOGPUDeviceUserClient</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.calendars</key>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.intelligenceflow.intelligencecontextd</string>
+	<key>com.apple.shortcuts.stepwise-execution</key>
+	<true/>
+	<key>com.apple.shortcuts.variable-injection</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siri.inference.EntityMatcher.useSensitiveLogging</key>

 		<string>753</string>
 		<string>1630</string>
 	</array>
+	<key>com.apple.videotoolbox.hardwarevideodecoder</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 		<string>IntelligenceFlow.Telemetry</string>
 		<string>IntelligenceFlow.ResponseGeneration</string>
 		<string>IntelligenceFlow.Experimentation</string>
+		<string>IntelligenceFlow.IFRequestTelemetry</string>
 		<string>PostSiriEngagement</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>Siri.Remembers.InteractionHistory</string>

 		<string>Sage.Transcript</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>IntelligenceFlow.ExecutorTelemetry</string>
 	</array>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>

```
### mapssyncd

> `/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
-	<key>com.apple.application-identifier</key>
-	<string>com.apple.Maps</string>
-	<key>com.apple.developer.aps-environment</key>
-	<string>serverPreferred</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.coreservices.launchservicesd</string>
+		<string>com.apple.coreservices.quarantine-resolver</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 		<string>com.apple.MobileAsset.AXElementVision</string>
 		<string>com.apple.MobileAsset.VCPMobileAssets</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 		<string>com.apple.MobileAsset.AXElementVision</string>
 		<string>com.apple.MobileAsset.VCPMobileAssets</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### MediaAnalysisBlastDoorService

> `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
+	<key>com.apple.coregraphics.disableinmemoryfonts</key>
+	<true/>
+	<key>com.apple.coregraphics.disablepdf</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.posterboardservices.disallowArchivingAppleArchive</key>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.mediacontrol</string>
 		<string>com.apple.mediaremote</string>
 		<string>com.apple.mediaremoted</string>
 		<string>com.apple.airplay</string>

```
### MessagesAirlockService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
+	<key>com.apple.coregraphics.disableinmemoryfonts</key>
+	<true/>
+	<key>com.apple.coregraphics.disablepdf</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.private.pac.exception</key>

```
### MessagesBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
+	<key>com.apple.coregraphics.disableinmemoryfonts</key>
+	<true/>
+	<key>com.apple.coregraphics.disablepdf</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.posterboardservices.disallowArchivingAppleArchive</key>

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

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.chronoservices</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.ClockAngel.mach</string>
 	</array>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
+		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

```
### medialibraryd

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd`

```diff

 		<dict>
 			<key>Sets</key>
 			<dict>
-				<key>Media.Entity</key>
+				<key>MediaLibrary.Media</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>

 	<array>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.FSEvents</string>

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 	<string>628765583</string>
 	<key>application-identifier</key>
 	<string>com.apple.newsd</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>aps-environment</key>
 	<string>production</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array>
+		<string>com.apple.news.private.secure</string>
+		<string>com.apple.news.private.secure.staging</string>
+		<string>com.apple.news.private.secure.qa</string>
+		<string>com.apple.news.private.secure.sandbox</string>
+		<string>com.apple.news.private.secure.demo1</string>
+		<string>com.apple.news.private.secure.demo2</string>
+	</array>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
+	<dict>
+		<key>com.apple.news.private.secure</key>
+		<string>com.apple.news.private.secure2</string>
+		<key>com.apple.news.private.secure.qa</key>
+		<string>com.apple.news.private.secure2</string>
+		<key>com.apple.news.private.secure.staging</key>
+		<string>com.apple.news.private.secure2</string>
+	</dict>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<array>
+		<string>true</string>
+	</array>
+	<key>com.apple.private.cloudkit.systemService</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>

 	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.news</string>
+	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.news.ScoringService</string>
+		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.apsd</string>
+		<string>com.apple.cloudd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 NewsScoringService

> `/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/NewsScoringService.xpc/NewsScoringService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.ane.iokit-user-access</key>
	<true/>
	<key>com.apple.aned.private.ANEAccess.allow</key>
	<true/>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.hid.manager.user-access-device</key>
	<true/>
	<key>com.apple.private.hid.client.admin</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.newsd</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.newsd</string>
		<string>group.com.apple.news</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/News/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOHIDLibUserClient</string>
		<string>AppleSPUHIDDeviceUserClient</string>
		<string>IOReportUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>AGXDeviceUserClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.newscore</string>
		<string>com.apple.newscore2</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOHIDLibUserClient</string>
		<string>AppleSPUHIDDeviceUserClient</string>
		<string>IOReportUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>AGXDeviceUserClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
</dict>
</plist>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
-	<key>com.apple.private.tcc.manager.access.delete</key>
-	<array>
-		<string>kTCCServiceFinancialData</string>
-	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

 	<array>
 		<string>com.apple.Passbook</string>
 		<string>com.apple.NanoPassbook</string>
+		<string>com.apple.PassbookUIService</string>
 	</array>
 	<key>com.apple.runningboard.assertions.PassbookUIService</key>
 	<true/>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 		<string>/Library/Trial/</string>
 		<string>/Library/Photos/PrivateEncryptedComputeStore.json</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Shortcuts/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleJPEGDriverUserClient</string>

```
### PerfPowerServicesSignpostReader

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumenetation</string>
+	</array>
+	<key>com.apple.private.kernel.override-cpumon</key>
+	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

```diff

 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.private.osanalytics.defaults.allow</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>

```
### RemoteManagementAgent

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent`

```diff

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.mdmd-access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.set</key>

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.ctkd.token-client</string>
+		<string>com.apple.managedconfiguration.mdmdservice</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.managedconfiguration.teslad</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

```
### remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.mdmd-access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.set</key>

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.ctkd.token-client</string>
+		<string>com.apple.managedconfiguration.mdmdservice</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.managedconfiguration.teslad</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

```
### replicatord

> `/System/Library/PrivateFrameworks/ReplicatorCore.framework/Support/replicatord`

```diff

 	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
 	<true/>
-	<key>com.apple.chrono.event-service-publisher</key>
-	<true/>
 	<key>com.apple.coreduet.knowledge</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
-	<key>com.apple.linkd.registry.waitforready</key>
-	<true/>
-	<key>com.apple.localizationswitcher</key>
-	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.networkd.allow_bootstrap_cellular_service_request</key>

 	<true/>
 	<key>com.apple.private.skywalk.register-user-pipe</key>
 	<true/>
-	<key>com.apple.private.tcc.events.subscriber</key>
+	<key>com.apple.private.userprofiles.read</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>

 	<string>group.com.apple.replicatord</string>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/Applications/</string>
-		<string>/System/Library/CoreServices/</string>
-		<string>/AppleInternal/Applications/</string>
-		<string>/private/var/containers/Bundle/Application/</string>
-		<string>/private/var/mobile/Library/SpringBoard/</string>
 		<string>/System/Library/replicatord/</string>
 		<string>/System/Library/replicatord/clientDescriptors/</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/Fonts/AddedFontCache.plist</string>
-		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/replicatord/</string>

 	<string>IOHIDLibUserClient</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.backboard.display.services</string>
-		<string>com.apple.iohideventsystem</string>
-		<string>com.apple.frontboard.systemappservices</string>
-		<string>com.apple.CARenderServer</string>
-		<string>com.apple.UIKit.KeyboardManagement.hosted</string>
 		<string>com.apple.duetactivityscheduler</string>
-		<string>com.apple.iphone.axserver-systemwide</string>
-		<string>com.apple.accessibility.AXBackBoardServer</string>
-		<string>com.apple.proactive.infoSuggestion.xpc</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
-		<string>com.apple.locationd.registration</string>
-		<string>com.apple.PointerUI.pointeruid.service</string>
-		<string>com.apple.fontservicesd</string>
 		<string>com.apple.backboard.hid-services.xpc</string>
-		<string>com.apple.springboard.services</string>
-		<string>com.apple.locationd.synchronous</string>
-		<string>com.apple.backlightd</string>
 		<string>com.apple.symptom_diagnostics</string>
-		<string>com.apple.localizationswitcherd</string>
-		<string>com.apple.sessionservices</string>
-		<string>com.apple.coremedia.systemcontroller.xpc</string>
-		<string>com.apple.coremedia.compressionsession</string>
-		<string>com.apple.coremedia.decompressionsession</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.networkd_privileged</string>
 		<string>com.apple.private.corewifi-xpc</string>
-		<string>com.apple.iconservices</string>
-		<string>com.apple.siri.VoiceShortcuts.xpc</string>
-		<string>com.apple.linkd.registry</string>
-		<string>com.apple.linkd.extension</string>
-		<string>com.apple.linkd.transcript</string>
-		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.StatusKit.local</string>
 		<string>com.apple.chronod.replicator</string>
 		<string>com.apple.identityservicesd.nsxpc</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.local-name</key>
-	<array>
-		<string>com.apple.iphone.axserver</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>
 		<string>com.apple.replicatorservices</string>
 	</array>
-	<key>com.apple.security.exception.mach-register.local-name</key>
-	<array>
-		<string>com.apple.iphone.axserver</string>
-	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
-		<string>com.apple.Preferences</string>
-		<string>com.apple.coremedia</string>
-		<string>com.apple.UIKit</string>
-		<string>com.apple.keyboard</string>
-		<string>com.apple.da</string>
-		<string>com.apple.SpeakSelection</string>
-		<string>com.apple.coreanimation</string>
 		<string>com.apple.duetexpertd</string>
-		<string>com.apple.frontboardservices.device_emulation</string>
 		<string>com.apple.ids</string>
 		<string>com.apple.conference</string>
 	</array>

```
### sosd

> `/System/Library/PrivateFrameworks/SOS.framework/sosd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

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
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
-		<string>Sage.Transcript</string>
+		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>UserFocus.ComputedMode</string>
 		<string>Location.Semantic</string>
 		<string>SiriIntentEvents</string>

```
### SettingsIntentExtension

> `/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/PlugIns/SettingsIntentExtension.appex/SettingsIntentExtension`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict>
-	<key>com.apple.CommCenter.fine-grained</key>
-	<array>
-		<string>spi</string>
-		<string>phone</string>
-	</array>
-	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>
-	<array>
-		<string>com.apple.radios.plist</string>
-	</array>
-	<key>com.apple.assistant.settings</key>
-	<true/>
-	<key>com.apple.avfoundation.allow-system-wide-context</key>
-	<true/>
-	<key>com.apple.backboard.displaybrightness</key>
-	<true/>
-	<key>com.apple.bluetooth.system</key>
-	<true/>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
-	<key>com.apple.coreduetd.batterysaver.allow</key>
-	<true/>
-	<key>com.apple.homepodaccessorysettings.client</key>
-	<true/>
-	<key>com.apple.homepodaccessorysettings.server</key>
-	<true/>
-	<key>com.apple.locationd.authorizeapplications</key>
-	<true/>
-	<key>com.apple.private.coreservices.canmaplsdatabase</key>
-	<true/>
-	<key>com.apple.private.usernotifications.settings</key>
-	<array>
-		<string>read</string>
-		<string>write</string>
-	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.assistant.settings</string>
-		<string>com.apple.coreduetd.batterysaver</string>
-		<string>com.apple.backlightd</string>
-		<string>com.apple.coremedia.flashlight</string>
-		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
-		<string>com.apple.homepodaccessorysettings.server</string>
-		<string>com.apple.homepodaccessorysettings.client</string>
-	</array>
-	<key>com.apple.security.exception.mach-register.global-name</key>
-	<array>
-		<string>com.apple.homepodaccessorysettings.server</string>
-		<string>com.apple.homepodaccessorysettings.client</string>
-	</array>
-	<key>com.apple.security.exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.Accessibility</string>
-		<string>com.apple.mediaaccessibility</string>
-		<string>com.apple.springboard</string>
-		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
-		<string>com.apple.backboardd</string>
-		<string>com.apple.voicetrigger</string>
-		<string>com.apple.audio.puffin</string>
-	</array>
-	<key>com.apple.voicetrigger</key>
-	<true/>
-	<key>com.apple.wifi.manager-access</key>
-	<true/>
-</dict>
+<dict/>
 </plist>
 

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsBookkeepingService.xpc/SiriSuggestionsBookkeepingService`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.assistant.settings</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### TelephonyBlastDoorService

> `/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/XPCServices/TelephonyBlastDoorService.xpc/TelephonyBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.coregraphics.disableinmemoryfonts</key>
+	<true/>
+	<key>com.apple.coregraphics.disablepdf</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>blastdoor-ids</string>
 	<key>com.apple.private.security.enable-state-flags</key>

```
### PhoneIntentHandler

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler`

```diff

 		<string>spi</string>
 		<string>cellular-plan</string>
 	</array>
+	<key>com.apple.NeighborhoodActivityConduitService</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.NeighborhoodActivityConduitService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.facetimemessagestored.service</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

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

```
### vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/preferences/SystemConfiguration/com.apple.wifi.plist</string>
+		<string>/private/var/preferences/SystemConfiguration/com.apple.radios.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.coremedia.mediaplaybackd.remaker.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.remaker</string>
 		<string>com.apple.coremedia.mediaparserd.formatreader.xpc</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>
+		<string>access-call-capabilities</string>
 	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>ToolKit.ToolDefinition</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
 				<key>ToolKitToolDefinition</key>
 				<dict>
 					<key>mode</key>

 		<string>com.apple.shortcuts</string>
 		<string>com.apple.shortcuts.AutomationLockscreenNotifications</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.proactive.ActionPrediction.predictions</key>
 	<true/>
 	<key>com.apple.proactive.AppPrediction.predictions</key>

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

 		<string>com.apple.shortcuts.view-service</string>
 		<string>com.apple.siri.vocabularyupdates</string>
 		<string>com.apple.spotlight.SearchAgent</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.shortcuts.background-running</key>
 	<true/>
+	<key>com.apple.shortcuts.daemon</key>
+	<true/>
 	<key>com.apple.shortcuts.dialogpresentation</key>
 	<true/>
 	<key>com.apple.shortcuts.stepwise-execution</key>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### FocusConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### SystemActionConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension`

```diff

 		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.itunescloudd.xpc</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### WidgetConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.WorkflowUI.WidgetConfigurationExtension</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.coreduetd.allow</key>
+	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array>
+		<string>iCloud.is.workflow.my.workflows</string>
+	</array>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudDocuments</string>
+		<string>CloudKit</string>
+	</array>
+	<key>com.apple.developer.ubiquity-container-identifiers</key>
+	<array>
+		<string>iCloud.is.workflow.my.workflows</string>
+	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
+	<key>com.apple.private.controlcenter.service.moduleidentifiers</key>
+	<array>
+		<string>com.apple.control-center.QRCodeModule</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceCalendar</string>
+		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
+	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.shortcuts</string>
+		<string>group.is.workflow.my.app</string>
+		<string>group.is.workflow.shortcuts</string>
 		<string>group.com.apple.weather</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/Applications/</string>
+		<string>/private/var/containers/Bundle/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/UserConfigurationProfiles/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Shortcuts/</string>
+		<string>/Media/iTunes_Control/iTunes/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.calaccessd</string>
+		<string>com.apple.controlcenter.remoteservice</string>
+		<string>com.apple.coreduetd.knowledge</string>
+		<string>com.apple.itunescloudd.xpc</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.medialibraryd.xpc</string>
+		<string>com.apple.photos.service</string>
+		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siriactionsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.logging</string>
+		<string>com.apple.medialibrary</string>
 		<string>com.apple.stocks</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

 		<string>com.apple.siri.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.configurationprofiles</string>
+	</array>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>V568VXD5P8.is.workflow.my.app</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### ICQFollowup

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup`

```diff

 	<true/>
 	<key>com.apple.coreidvd.spi</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.payment.all-access</key>

 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

```

### 🆕 EmergencyUIPlugin

> `/System/Library/Snippets/UIPlugins/EmergencyUIPlugin.bundle/EmergencyUIPlugin`

- No entitlements *(yet)*

### 🆕 GenerativeAssistantUIPlugin

> `/System/Library/Snippets/UIPlugins/GenerativeAssistantUIPlugin.bundle/GenerativeAssistantUIPlugin`

- No entitlements *(yet)*

### 🆕 SearchToolUIPlugin

> `/System/Library/Snippets/UIPlugins/SearchToolUIPlugin.bundle/SearchToolUIPlugin`

- No entitlements *(yet)*

### 🆕 SiriInformationUIPlugin

> `/System/Library/Snippets/UIPlugins/SiriInformationUIPlugin.bundle/SiriInformationUIPlugin`

- No entitlements *(yet)*

### 🆕 AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>379332956</string>
	<key>application-identifier</key>
	<string>com.apple.AppStore</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.CoreTelephony.DataUsageInfo.allow</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.appleaccount.custodian</key>
	<true/>
	<key>com.apple.appstored.install-apps</key>
	<true/>
	<key>com.apple.appstored.private</key>
	<true/>
	<key>com.apple.appstored.update-apps</key>
	<true/>
	<key>com.apple.appstored.xpc.updates</key>
	<true/>
	<key>com.apple.attributionkitd.impression-intake</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.cdp.recoverykey</key>
	<true/>
	<key>com.apple.corerecents.recentsd</key>
	<true/>
	<key>com.apple.developer.associated-domains</key>
	<array/>
	<key>com.apple.developer.usernotifications.time-sensitive</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.itunescloud.in-app-message-service</key>
	<true/>
	<key>com.apple.itunesstored.metrics</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.absinthe</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.launchservices.receivereferrerrurl</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.passd.account</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.payment.amp-card-enrollment</key>
	<true/>
	<key>com.apple.payment.card-on-file</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.APODMLDESPlugin</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.ap.PromotedContentPrediction.APOdmlSearchResultsExtension</key>
	<true/>
	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.accounts.customaccesssinfo</key>
	<true/>
	<key>com.apple.private.ap.idmanager</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstorecomponents.build-lockup-from-mapi-response</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Purchase</string>
		<string>Library</string>
		<string>IAPHistory</string>
		<string>Personalization</string>
		<string>Update</string>
		<string>PurchaseHistory</string>
		<string>AppCapabilities</string>
	</array>
	<key>com.apple.private.avatar.store</key>
	<true/>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.calendar.has-adopted-modern-request-access-methods</key>
	<true/>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.canIgnoreAppLinkOpenStrategy</key>
	<true/>
	<key>com.apple.private.cfnetwork.har-capture-amp</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.game-center</key>
	<array>
		<string>Account</string>
		<string>Authenticate</string>
		<string>Profile</string>
		<string>Friends</string>
		<string>Games</string>
		<string>Scores</string>
		<string>Achievements</string>
		<string>Challenges</string>
		<string>Multiplayer</string>
		<string>TurnBasedMultiplayer</string>
		<string>GameStats</string>
	</array>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.hsa-authentication-processing</key>
	<true/>
	<key>com.apple.private.iad.news-client</key>
	<true/>
	<key>com.apple.private.iad.opt-in-control</key>
	<true/>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.ids.remoteurlconnection</key>
	<true/>
	<key>com.apple.private.in-app-payments</key>
	<true/>
	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>
	<string>*</string>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.security.storage.triald</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.swc.additional-service-details-consumer</key>
	<true/>
	<key>com.apple.private.swc.system-app</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount</string>
		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>
		<string>/Library/Trial/NamespaceDescriptors/</string>
		<string>/Library/Trial/Treatments/511/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.storeservices/</string>
		<string>/Library/com.apple.itunesstored/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Logs/com.apple.StoreServices/</string>
		<string>/Library/Caches/JetPackCache/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.attributionkitd.xpc.impression-intake</string>
		<string>com.apple.ap.promotedcontent.pcinterface</string>
		<string>com.apple.ap.promotedcontent.mescalinterface</string>
		<string>com.apple.appstored.xpc.storequeue</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.ap.promotedcontent.metrics</string>
		<string>com.apple.ap.promotedcontent.supportinterface</string>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.corerecents.recentsd</string>
		<string>com.apple.appstored.xpc.jobmanager</string>
		<string>com.apple.appstored.xpc.request</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.appstored.xpc.updates</string>
		<string>com.apple.symptom_analytics</string>
		<string>com.apple.ap.adprivacyd.idmanager</string>
		<string>com.apple.ap.adprivacyd.opt-out</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.itunescloud.in-app-message-service</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.hsa-authentication-server</string>
		<string>com.apple.ap.adprivacyd.store</string>
		<string>com.apple.aa.custodian.xpc</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.payment.all-access</string>
		<string>com.apple.cards.all-access</string>
		<string>com.apple.passd.account</string>
		<string>com.apple.xpc.amsserverdatacacheservice</string>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.symptom_diagnostics</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.appstored</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AdLib</string>
		<string>com.apple.gamecenter</string>
		<string>com.apple.AppStore</string>
		<string>com.apple.AppStore.ProductPageExtension</string>
		<string>com.apple.AppStore.SubscribePageExtension</string>
		<string>com.apple.Fitness</string>
		<string>com.apple.itunesstored</string>
		<string>com.apple.springboard</string>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.AdPlatforms</string>
	</array>
	<key>com.apple.security.system-group-containers</key>
	<array>
		<string>systemgroup.com.apple.VideoSubscriberAccount</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.telephony.cupolicy-rw-access</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>511</string>
		<string>512</string>
	</array>
	<key>fairplay-client</key>
	<string>1699554724</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.VideoSubscriberAccount</string>
	</array>
</dict>
</plist>

```

### 🆕 AppStoreWidgetsExtension

> `/private/var/staged_system_apps/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.AppStore.Widgets</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.appstored.private</key>
	<true/>
	<key>com.apple.appstored.xpc.updates</key>
	<true/>
	<key>com.apple.chrono.event-service</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.accounts.customaccessinfo</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Purchase</string>
		<string>Library</string>
		<string>IAPHistory</string>
		<string>Personalization</string>
		<string>Update</string>
		<string>PurchaseHistory</string>
		<string>AppCapabilities</string>
	</array>
	<key>com.apple.private.ids.remoteurlconnection</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.storeservices/</string>
		<string>/Library/com.apple.itunesstored/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Logs/com.apple.StoreServices/</string>
		<string>/Library/Caches/JetPackCache/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.corerecents.recentsd</string>
		<string>com.apple.appstored.xpc.jobmanager</string>
		<string>com.apple.appstored.xpc.request</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.appstored.xpc.updates</string>
		<string>com.apple.symptom_analytics</string>
		<string>com.apple.ap.adprivacyd.idmanager</string>
		<string>com.apple.ap.adprivacyd.opt-out</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.itunescloud.in-app-message-service</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.hsa-authentication-server</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AdLib</string>
		<string>com.apple.AppStore</string>
		<string>com.apple.AppStore.Widgets</string>
		<string>com.apple.Fitness</string>
		<string>com.apple.itunesstored</string>
		<string>com.apple.springboard</string>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.AppStoreComponents</string>
	</array>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>fairplay-client</key>
	<string>1699554724</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.VideoSubscriberAccount</string>
	</array>
</dict>
</plist>

```
### TVWidgetExtension

> `/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension`

```diff

 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
-	<array>
-		<true/>
-	</array>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.homesharing</string>
 		<string>com.apple.videos</string>
 		<string>com.apple.videos-preferences</string>
 		<string>com.apple.TVWatchList</string>

```
### Books

> `/private/var/staged_system_apps/Books.app/Books`

```diff

 		<string>systemgroup.com.apple.media.shared.books</string>
 		<string>systemgroup.com.apple.media.books.managed</string>
 	</array>
+	<key>com.apple.sharesheet.userdefaults</key>
+	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>
 	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.passd.sharing-channel</string>
 		<string>com.apple.passd.device-registration</string>
 		<string>com.apple.WorkoutKitXPCService</string>

```

### 🆕 Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CanInheritApplicationStateFromOtherProcesses</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.camera</string>
	<key>checklessPersistentURLTranslation</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>public-cellular-plan</string>
		<string>public-esim-qr-code</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.RemoteDisplay</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.avfoundation.allow-capture-filter-rendering</key>
	<true/>
	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.allow-apac-codec</key>
	<true/>
	<key>com.apple.coremedia.cameraviewfinder</key>
	<true/>
	<key>com.apple.developer.extension-host.photo-editing</key>
	<true/>
	<key>com.apple.developer.networking.HotspotConfiguration</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.excludes-extensions</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.intents.intents-helper</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.mediastream.mstreamd-access</key>
	<true/>
	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.nfcd.assertion.handover</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.BarcodeSupport.can-suppress-app-clip-code-url-authorization</key>
	<true/>
	<key>com.apple.private.ClipServices</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.acg.autoloops</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
	</array>
	<key>com.apple.private.assetsd.nebulad.access</key>
	<string>camera</string>
	<key>com.apple.private.avfoundation.capture.deferred-photo-processor.allow</key>
	<true/>
	<key>com.apple.private.barcodesupport.allowNotifications</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Discoverability.Signals</string>
	</array>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.imagecapturecore.authorization_bypass</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.ind.client</key>
	<true/>
	<key>com.apple.private.lockdown.finegrained-get</key>
	<array>
		<string>NULL/ActivationPrivateKey</string>
		<string>NULL/DeviceCertificate</string>
	</array>
	<key>com.apple.private.payment.remote-network-payment-initiate</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.allowassetexpunge</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.internal.resource</key>
	<true/>
	<key>com.apple.private.photos.service.multilibrary</key>
	<true/>
	<key>com.apple.private.photos.smartsharing.cache.read</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>MobileSlideShow</string>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.translation</key>
	<true/>
	<key>com.apple.private.xpc.domain-extension</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.rapport.SessionPaired</key>
	<true/>
	<key>com.apple.rapport.people</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_MagicCleanup/purpose_auto/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/PhotoData/</string>
		<string>/Library/Caches/com.apple.ClipServices/</string>
		<string>/Library/UnifiedAssetFramework/</string>
		<string>/Library/com.apple.modelcatalog/sideload/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.WebKit.Networking/</string>
		<string>/Library/LiveFiles/com.apple.filesystems.userfsd/</string>
		<string>/Library/Caches/com.apple.DocumentCamera/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.assetsd.nebulad</string>
		<string>com.apple.assetsd.keepDaemonAlive</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.rapport.people</string>
		<string>com.apple.SharingServices</string>
		<string>com.apple.translationd</string>
		<string>com.apple.RemoteDisplay</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.CameraOverlayAngel.application-service</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SocialLayer</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.gms.availability</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.phoenix</string>
		<string>com.apple.WallpaperKit</string>
		<string>com.apple.cameracapture</string>
		<string>com.apple.airplay</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.geoanalyticsd</string>
	</array>
	<key>com.apple.sharesheet.allow-custom-view</key>
	<true/>
	<key>com.apple.sharing.DeviceDiscovery</key>
	<true/>
	<key>com.apple.springboard.activateawayviewplugins</key>
	<true/>
	<key>com.apple.springboard.allowallcallurls</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
	<key>com.apple.springboard.setWantsLockButtonEvents</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>313</string>
	</array>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>fairplay</key>
	<integer>1615507317</integer>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.youtube.credentials</string>
		<string>com.apple.videouploadplugins.credentials</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CanInheritApplicationStateFromOtherProcesses</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.camera.lockscreen</string>
	<key>checklessPersistentURLTranslation</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>public-cellular-plan</string>
		<string>public-esim-qr-code</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.RemoteDisplay</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.avfoundation.allow-capture-filter-rendering</key>
	<true/>
	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coremedia.cameraviewfinder</key>
	<true/>
	<key>com.apple.developer.extension-host.photo-editing</key>
	<true/>
	<key>com.apple.developer.networking.HotspotConfiguration</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.excludes-extensions</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.intents.intents-helper</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.mediastream.mstreamd-access</key>
	<true/>
	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
	<true/>
	<key>com.apple.nfcd.assertion.handover</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.BarcodeSupport.can-suppress-app-clip-code-url-authorization</key>
	<true/>
	<key>com.apple.private.ClipServices</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.acg.autoloops</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
	<true/>
	<key>com.apple.private.assetsd.nebulad.access</key>
	<string>camera</string>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.camera</string>
	</dict>
	<key>com.apple.private.avfoundation.capture.allow</key>
	<true/>
	<key>com.apple.private.avfoundation.capture.deferred-photo-processor.allow</key>
	<true/>
	<key>com.apple.private.barcodesupport.allowNotifications</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Discoverability.Signals</string>
	</array>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.imagecapturecore.authorization_bypass</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.ind.client</key>
	<true/>
	<key>com.apple.private.lockdown.finegrained-get</key>
	<array>
		<string>NULL/ActivationPrivateKey</string>
		<string>NULL/DeviceCertificate</string>
	</array>
	<key>com.apple.private.payment.remote-network-payment-initiate</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.allowassetexpunge</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.internal.resource</key>
	<true/>
	<key>com.apple.private.photos.service.mediaconversion</key>
	<true/>
	<key>com.apple.private.photos.service.multilibrary</key>
	<true/>
	<key>com.apple.private.photos.smartsharing.cache.read</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>MobileSlideShow</string>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.translation</key>
	<true/>
	<key>com.apple.private.xpc.domain-extension</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.rapport.SessionPaired</key>
	<true/>
	<key>com.apple.rapport.people</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/PhotoData/</string>
		<string>/Library/Caches/com.apple.ClipServices/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Media/PhotoData/</string>
		<string>/Media/DCIM/</string>
		<string>/Library/Caches/com.apple.WebKit.Networking/</string>
		<string>/Library/LiveFiles/com.apple.filesystems.userfsd/</string>
		<string>/Library/Caches/com.apple.DocumentCamera/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.assetsd.nebulad</string>
		<string>com.apple.assetsd.keepDaemonAlive</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.rapport.people</string>
		<string>com.apple.SharingServices</string>
		<string>com.apple.translationd</string>
		<string>com.apple.RemoteDisplay</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.CameraOverlayAngel.application-service</string>
		<string>com.apple.companion.camera</string>
		<string>com.apple.coremedia.cameraviewfinder</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.cache_delete</string>
		<string>com.apple.spotlight.IndexDelegateAgent</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SocialLayer</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.camera</string>
		<string>com.apple.phoenix</string>
		<string>com.apple.WallpaperKit</string>
		<string>com.apple.camera.lockscreen</string>
		<string>com.apple.airplay</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.geoanalyticsd</string>
	</array>
	<key>com.apple.sharesheet.allow-custom-view</key>
	<true/>
	<key>com.apple.sharing.DeviceDiscovery</key>
	<true/>
	<key>com.apple.springboard.activateawayviewplugins</key>
	<true/>
	<key>com.apple.springboard.allowallcallurls</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
	<key>com.apple.springboard.setWantsLockButtonEvents</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>313</string>
	</array>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>fairplay</key>
	<integer>1615507317</integer>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.youtube.credentials</string>
		<string>com.apple.videouploadplugins.credentials</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 LauncherControlExtension

> `/private/var/staged_system_apps/Camera.app/PlugIns/LauncherControlExtension.appex/LauncherControlExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.camera</string>
</dict>
</plist>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 		<string>com.apple.SOS</string>
 		<string>com.apple.messages.nicknames</string>
 		<string>com.apple.contacts.sharedProfile</string>
+		<string>com.apple.contacts.intents</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
+	<key>com.apple.developer.phone-app</key>
+	<true/>
 	<key>com.apple.developer.usernotifications.communication</key>
 	<true/>
 	<key>com.apple.developer.usersafety.client</key>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	</array>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.fenceservice</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>

```

### 🆕 FindMyIntentsExtension

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyIntentsExtension.appex/FindMyIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.findmy</string>
</dict>
</plist>

```
### FindMyNotificationsContent

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsContent.appex/FindMyNotificationsContent`

```diff

 <dict>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.icloud.fmf.FMFMapXPCService.access</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 	<array>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.icloud.FMF.FMFMapXPCService</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>

```
### FindMyNotificationsService

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService`

```diff

 <dict>
 	<key>com.apple.developer.usernotifications.filtering</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>

 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 	</array>
 </dict>
 </plist>

```
### FindMyWidgetItems

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetItems.appex/FindMyWidgetItems`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.authkit.client.internal</key>
-	<true/>
-	<key>com.apple.authkit.client.private</key>
-	<true/>
+	<key>application-identifier</key>
+	<string>com.apple.findmy</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>

 	<true/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionComplete</string>
-	<key>com.apple.developer.siri</key>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
-	<key>com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService.access</key>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
 	<true/>
-	<key>com.apple.icloud.findmydeviced.access</key>
+	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
+	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
 	<true/>
-	<key>com.apple.icloud.searchpartyd.ownersession</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.securelocations</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
 	<true/>
-	<key>com.apple.intents.extension.discovery</key>
-	<true/>
-	<key>com.apple.intents.uiextension.discovery</key>
+	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
-	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
-	<array>
-		<string>UniqueDeviceID</string>
-	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<key>value</key>
 		<string>com.apple.findmy</string>
 	</dict>
-	<key>com.apple.private.hsa-authentication-processing</key>
-	<true/>
-	<key>com.apple.private.network.socket-delegate</key>
-	<true/>
-	<key>com.apple.private.security.storage.FindMy</key>
-	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute</key>
-	<array>
-		<string>/tmp/findmydeviced-sandbox-violation</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_SharingDeviceAssets/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.chronoservices</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
-		<string>com.apple.icloud.findmydeviced.app-support</string>
-		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
-		<string>com.apple.chronoservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.dnssd.service</string>
-	</array>
-	<key>com.apple.security.exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.findmy.fmipcore.notbackedup</string>
-		<string>com.apple.findmy.fmfcore.notbackedup</string>
-		<string>com.apple.findmy</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
-	<key>com.apple.security.network.client</key>
+	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
-	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/</string>
-	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.icloud.searchparty.locationfetch.items</string>
-		<string>com.apple.icloud.findmydeviced.app-support</string>
-		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
-		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
-		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.chronoservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.dnssd.service</string>
-	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.findmy.fmipcore.notbackedup</string>
-		<string>com.apple.findmy.fmfcore.notbackedup</string>
-		<string>com.apple.findmy</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### FindMyWidgetPeople

> `/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.authkit.client.internal</key>
-	<true/>
-	<key>com.apple.authkit.client.private</key>
-	<true/>
+	<key>application-identifier</key>
+	<string>com.apple.findmy</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>

 	<true/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionComplete</string>
-	<key>com.apple.developer.siri</key>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
-	<key>com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService.access</key>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
 	<true/>
-	<key>com.apple.icloud.findmydeviced.access</key>
+	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
+	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
 	<true/>
-	<key>com.apple.icloud.searchpartyd.ownersession</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.securelocations</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
 	<true/>
-	<key>com.apple.intents.extension.discovery</key>
-	<true/>
-	<key>com.apple.intents.uiextension.discovery</key>
+	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
-	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
-	<array>
-		<string>UniqueDeviceID</string>
-	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<key>value</key>
 		<string>com.apple.findmy</string>
 	</dict>
-	<key>com.apple.private.hsa-authentication-processing</key>
-	<true/>
-	<key>com.apple.private.network.socket-delegate</key>
-	<true/>
-	<key>com.apple.private.security.storage.FindMy</key>
-	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute</key>
-	<array>
-		<string>/tmp/findmydeviced-sandbox-violation</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_SharingDeviceAssets/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.chronoservices</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
-		<string>com.apple.icloud.findmydeviced.app-support</string>
-		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
-		<string>com.apple.chronoservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.dnssd.service</string>
-	</array>
-	<key>com.apple.security.exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.findmy.fmipcore.notbackedup</string>
-		<string>com.apple.findmy.fmfcore.notbackedup</string>
-		<string>com.apple.findmy</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
-	<key>com.apple.security.network.client</key>
+	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
-	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/</string>
-	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.icloud.searchparty.locationfetch.items</string>
-		<string>com.apple.icloud.findmydeviced.app-support</string>
-		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
-		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
-		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.chronoservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.dnssd.service</string>
-	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.findmy.fmipcore.notbackedup</string>
-		<string>com.apple.findmy.fmfcore.notbackedup</string>
-		<string>com.apple.findmy</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 	<array>
 		<string>group.com.apple.freeform</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/AppAnalytics/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.coreduetd.knowledge</string>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.Home.group</string>
+		<string>group.com.apple.CoreSpeech</string>
 		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>

 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.pearld</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.pearld</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

```
### HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.Home.group</string>
+		<string>group.com.apple.CoreSpeech</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.pearld</string>
 		<string>com.apple.private.corewifi.readonly-xpc</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.pearld</string>
 		<string>com.apple.private.corewifi.readonly-xpc</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

```
### HomeWidgetLockScreen

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.Home.group</string>
+		<string>group.com.apple.CoreSpeech</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

```
### HomeWidgetSingleAccessoryIntent

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.Home.group</string>
+		<string>group.com.apple.CoreSpeech</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>

```

### 🆕 GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
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
	<false/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.GenerativePlayground</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
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

### 🆕 Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.GenerativePlaygroundApp</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.GenerativePlaygroundApp</string>
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
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
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
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
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
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.ind.cloudfeatures</string>
		<string>com.apple.duetactivityscheduler</string>
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
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
	</array>
	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
	<array>
		<string>AppleNVMeEANUC</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.mobileasset.autoasset</string>
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
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.ind.cloudfeatures</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```

### 🆕 GenerativePlaygroundMessagesAppExtension

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.GenerativePlaygroundApp.remoteUIExtension</string>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
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
	<key>com.apple.messages.private.AllowConversationContextAccess</key>
	<false/>
	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>
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
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
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
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
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
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
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
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.ind.cloudfeatures</string>
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
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
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
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### MagnifierExtension

> `/private/var/staged_system_apps/Magnifier.app/Extensions/MagnifierExtension.appex/MagnifierExtension`

```diff

 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.CameraOverlayAngel.application-service</string>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.appleneuralengine.private</string>
 		<string>com.apple.pluginkit.pkd</string>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.CameraOverlayAngel.application-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	</array>
 	<key>com.apple.geoservices.map-subscriptions.manage-downloads</key>
 	<true/>
+	<key>com.apple.geoservices.map-subscriptions.watch-sync</key>
+	<true/>
 	<key>com.apple.geoservices.navd.clientIdentifier</key>
 	<string></string>
 	<key>com.apple.geoservices.navd.recentLocations</key>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>
 	<true/>
 	<key>com.apple.generativeexperiences.textcomposition</key>

 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>

 	<array>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.notes.import</string>
+		<string>group.com.apple.GenerativePlayground</string>
 	</array>
 	<key>com.apple.security.device.audio-input</key>
 	<true/>

 		<string>/private/var/MobileAsset/AssetsV2/</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```

### 🆕 MessagesActionExtension

> `/private/var/staged_system_apps/MobileSMS.app/Extensions/MessagesActionExtension.appex/MessagesActionExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.MobileSMS</string>
	</array>
</dict>
</plist>

```

### 🆕 MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Siri</key>
	<true/>
	<key>abs-client</key>
	<string>833127088</string>
	<key>adi-client</key>
	<string>559326803</string>
	<key>application-identifier</key>
	<string>com.apple.MobileSMS</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.Carousel.eligibilityservice</key>
	<true/>
	<key>com.apple.CommCenter.StormBreaker</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>preferences-write</string>
		<string>spi</string>
		<string>cellular-plan</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.CoreRoutine.SafetyMonitor</key>
	<true/>
	<key>com.apple.IdentityLookup.MessageFilter</key>
	<string></string>
	<key>com.apple.NanoTimeKit.userphotofaceclient</key>
	<true/>
	<key>com.apple.ProactiveSummarization.feedback</key>
	<true/>
	<key>com.apple.ProactiveSummarization.model-input</key>
	<true/>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.StatusKit.publish.types</key>
	<array>
		<string>com.apple.availability</string>
		<string>com.apple.focus.status</string>
		<string>com.apple.offgrid.status</string>
	</array>
	<key>com.apple.StatusKit.subscribe.types</key>
	<array>
		<string>com.apple.availability</string>
		<string>com.apple.focus.status</string>
		<string>com.apple.offgrid.status</string>
	</array>
	<key>com.apple.TextUnderstanding.SmartReplies.Inference</key>
	<true/>
	<key>com.apple.accountsd.accountmanager</key>
	<true/>
	<key>com.apple.activityawardsd</key>
	<true/>
	<key>com.apple.activitysharingd</key>
	<true/>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.appstored.install-apps</key>
	<true/>
	<key>com.apple.appstored.xpc.updates</key>
	<true/>
	<key>com.apple.assistant.dictation.prerecorded</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.avfoundation.allow-capture-filter-rendering</key>
	<true/>
	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
	<true/>
	<key>com.apple.backboardd.touchDeliveryObservation</key>
	<true/>
	<key>com.apple.carousel.backlightaccess</key>
	<true/>
	<key>com.apple.cdp.statemachine</key>
	<true/>
	<key>com.apple.clarityboard.chromeVisibility</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-encode</key>
	<true/>
	<key>com.apple.coreaudio.allow-apac-codec</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.coreduetd.people</key>
	<true/>
	<key>com.apple.coretelephony.Identity.get</key>
	<true/>
	<key>com.apple.developer.associated-domains</key>
	<array/>
	<key>com.apple.developer.carplay-communication</key>
	<true/>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudDocuments</string>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.siri</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.messages.pinning</string>
	<key>com.apple.developer.usernotifications.communication</key>
	<true/>
	<key>com.apple.developer.usernotifications.critical-alerts</key>
	<true/>
	<key>com.apple.developer.usernotifications.time-sensitive</key>
	<true/>
	<key>com.apple.developer.usersafety.client</key>
	<array>
		<string>analysis</string>
	</array>
	<key>com.apple.developer.workoutkit</key>
	<true/>
	<key>com.apple.diagnosticpipeline.request</key>
	<true/>
	<key>com.apple.duet.expertcenter.consumer</key>
	<true/>
	<key>com.apple.feedbackd.remote-evaluation</key>
	<true/>
	<key>com.apple.fileprovider.share</key>
	<true/>
	<key>com.apple.finance.private</key>
	<true/>
	<key>com.apple.findmy.findmylocate.friendshipservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.locationservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.settings</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.geoservices.navigation_info</key>
	<true/>
	<key>com.apple.icloud.fmfd.access</key>
	<true/>
	<key>com.apple.identitylookup.classification-ui.extension-host</key>
	<string></string>
	<key>com.apple.imagent.chat</key>
	<true/>
	<key>com.apple.intents.intents-helper</key>
	<true/>
	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>
	<true/>
	<key>com.apple.ios.StoreKit.store-page</key>
	<true/>
	<key>com.apple.itunescloudd.private</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled-access</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>
	<true/>
	<key>com.apple.media.ringtones.read-only</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.messages.sticker-sharing-level</key>
	<string>messages</string>
	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.multitasking.systemappassertions</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.nanopassd.connect</key>
	<true/>
	<key>com.apple.passd.peer-payment</key>
	<true/>
	<key>com.apple.passes.add-silently</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.peerpayment.all-access</key>
	<true/>
	<key>com.apple.pegasus.context</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.CallHistory.read</key>
	<true/>
	<key>com.apple.private.ClipServices</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/ChatKit.framework</string>
	</array>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Purchase</string>
		<string>Library</string>
		<string>IAPInfo</string>
		<string>Personalization</string>
		<string>Update</string>
		<string>PurchaseHistory</string>
	</array>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.Activity.Achievements</string>
	</array>
	<key>com.apple.private.assetsd.nebulad.access</key>
	<string>camera</string>
	<key>com.apple.private.avatar.store</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>InferredMode</string>
		<string>UserFocusComputedMode</string>
		<string>NowPlaying</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>CommunicationSafetyResult</string>
		<string>CommunicationSafetyResultWithoutImage</string>
		<string>Discoverability.Signals</string>
		<string>Discoverability.Usage</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>SensitiveContentAnalysis.UIInteraction</string>
		<string>SensitiveContentAnalysis.MediaAnalysis</string>
	</array>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.clouddocs.sharing-proxy</key>
	<true/>
	<key>com.apple.private.clouddocs.sharing.private-interface</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.communicationsfilter</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.dmd.emergency-mode</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.donotdisturb.modeconfiguration.availability.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.donotdisturb.settings.modify.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.donotdisturb.settings.request.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.dprivacyd.metadata.allow</key>
	<true/>
	<key>com.apple.private.emergency-mode</key>
	<true/>
	<key>com.apple.private.game-center</key>
	<array>
		<string>Account</string>
	</array>
	<key>com.apple.private.game-center.bypass-authentication</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.medicaliddata</key>
	<true/>
	<key>com.apple.private.healthkit.read_authorization_override</key>
	<array>
		<string>HKQuantityTypeIdentifierHeartRate</string>
	</array>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.ids.idquery-cache</key>
	<true/>
	<key>com.apple.private.ids.messaging</key>
	<array>
		<string>com.apple.private.alloy.nameandphoto</string>
		<string>com.apple.madrid</string>
		<string>com.apple.madrid.lite</string>
		<string>com.apple.private.alloy.biz</string>
	</array>
	<key>com.apple.private.ids.messaging.urgent-priority</key>
	<array>
		<string>com.apple.private.alloy.nameandphoto</string>
	</array>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.ids.registration</key>
	<array>
		<string>com.apple.private.alloy.nameandphoto</string>
		<string>com.apple.private.alloy.biz</string>
	</array>
	<key>com.apple.private.ignore-preferences-size-limits</key>
	<true/>
	<key>com.apple.private.imcore.imdpersistence.database-access</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.imcore.imtranscoderservice</key>
	<true/>
	<key>com.apple.private.interstellar.data-access</key>
	<string>collaborations</string>
	<key>com.apple.private.iosmac</key>
	<true/>
	<key>com.apple.private.librarian.container-proxy</key>
	<true/>
	<key>com.apple.private.managed-settings.effective-read</key>
	<true/>
	<key>com.apple.private.mobileinstall.allowedSPI</key>
	<array>
		<string>UninstallForLaunchServices</string>
	</array>
	<key>com.apple.private.persona.read</key>
	<true/>
	<key>com.apple.private.persona.write</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.pluginkit.manager</key>
	<true/>
	<key>com.apple.private.remindd</key>
	<array>
		<string>peopleInteraction</string>
		<string>store</string>
	</array>
	<key>com.apple.private.safari.safebrowsing.useallproviders</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screentime-communication</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.storage.CallHistory</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.MessagesMetaData</key>
	<true/>
	<key>com.apple.private.security.storage.PassKit</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.shared-with-you.on-screen-content</key>
	<true/>
	<key>com.apple.private.sociallayer.collaboration-handshake</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.sociallayer.shareable-content</key>
	<true/>
	<key>com.apple.private.stickers</key>
	<true/>
	<key>com.apple.private.suggestions</key>
	<true/>
	<key>com.apple.private.suggestions.contacts</key>
	<true/>
	<key>com.apple.private.suggestions.events</key>
	<true/>
	<key>com.apple.private.suggestions.messages</key>
	<true/>
	<key>com.apple.private.suggestions.reminders</key>
	<true/>
	<key>com.apple.private.suggestions.searchtoshare</key>
	<true/>
	<key>com.apple.private.swc.system-app</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServicePhotosAdd</string>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.private.tipsd.discoverability</key>
	<true/>
	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
	<array>
		<string>com.apple.tipsd</string>
		<string>com.apple.MobileSMS</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.proactive.experiments.responses</key>
	<true/>
	<key>com.apple.rootless.storage.triald</key>
	<true/>
	<key>com.apple.runningboard.posterkit.host</key>
	<true/>
	<key>com.apple.sage.textcomposition</key>
	<true/>
	<key>com.apple.samples.cloudkit.sharing</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.safari</string>
		<string>group.com.apple.PegasusConfiguration</string>
		<string>group.com.apple.hashtagImages</string>
		<string>group.com.apple.tipsnext</string>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
	</array>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.countryd/</string>
		<string>/AppleInternal/Library/Madrid/</string>
		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist</string>
		<string>/private/var/MobileAsset/Assets/com_apple_MobileAsset_LinguisticData/</string>
		<string>/Library/Audio/Tunings/Generic/AU/aufx-epvd-appl.plist</string>
		<string>/Library/Audio/Plug-Ins/RemoteInput/</string>
		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
		<string>/private/var/mobile/Library/Trial/Treatments/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/com.apple.messages/</string>
		<string>/private/var/mobile/tmp/com.apple.messages/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/</string>
		<string>/Library/Caches/CloudKit/com.apple.imagent/</string>
		<string>/Library/PPTDevice</string>
		<string>/Library/CallHistoryDB/com.apple.callhistory.databaseInfo.plist</string>
		<string>/Library/Caches/PassKit/</string>
		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
		<string>/Library/com.apple.itunesstored/kvs.sqlitedb</string>
		<string>/Containers/Data/PluginKitPlugin/</string>
		<string>/Library/CallHistoryDB/</string>
		<string>/Library/Caches/com.apple.ClipServices/</string>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
		<string>/Library/DeviceRegistry.state/ActiveDeviceMiniStore.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/ResponseKit/</string>
		<string>/Library/SMS/</string>
		<string>/Library/Caches/com.apple.MobileSMS/</string>
		<string>/Library/CoreDuet/People/interactionC.db-shm</string>
		<string>/Library/com.apple.itunesstored/kvs.sqlitedb-shm</string>
		<string>/Library/Caches/com.apple.keyboards/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Caches/com.apple.storeservices/</string>
		<string>/Library/com.apple.itunesstored/</string>
		<string>/Library/MessagesMetaData/</string>
		<string>/Library/Avatar/</string>
		<string>/Library/ContactsMetadata/</string>
		<string>/Library/Caches/com.apple.AvatarUI/</string>
		<string>/Media/PhotoData/</string>
		<string>/Library/NanoPhotos/</string>
		<string>/Library/Caches/com.apple.NanoTimeKit/</string>
		<string>/Library/Caches/PassKit/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>RootDomainUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.surfboard.applicationservice</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.compute.source</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.suggestd.events</string>
		<string>com.apple.webprivacyd</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.sharing.sharesheetrecipients</string>
		<string>com.apple.coreduetd.people.user</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.transparencyd</string>
		<string>com.apple.transparencyd.ids</string>
		<string>com.apple.dmd.emergency-mode</string>
		<string>com.apple.imfoundation.IMRemoteURLConnectionAgent</string>
		<string>com.apple.Carousel.eligibilityservice</string>
		<string>com.apple.appstored.xpc.updates</string>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.sage.textcomposition</string>
		<string>com.apple.suggestd.contacts</string>
		<string>com.apple.suggestd.messages</string>
		<string>com.apple.suggestd.reminders</string>
		<string>com.apple.appstored.xpc.request</string>
		<string>com.apple.private.healthd.server-extended</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.passd.peer-payment</string>
		<string>com.apple.NPKInAppPaymentServer</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.tipsd</string>
		<string>com.apple.icloud.fmfd</string>
		<string>com.apple.findmy.findmylocate.friendshipservice</string>
		<string>com.apple.findmy.findmylocate.locationservice</string>
		<string>com.apple.findmy.findmylocate.settings</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.assetsd.nebulad</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.Safari.SafeBrowsing.Service</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.StatusKit.subscribe</string>
		<string>com.apple.StatusKit.publish</string>
		<string>com.apple.donotdisturb.service</string>
		<string>com.apple.donotdisturb.service.non-launching</string>
		<string>com.apple.donotdisturb.appconfiguration.service</string>
		<string>com.apple.installcoordinationd</string>
		<string>com.apple.CellularPlanDaemon.xpc</string>
		<string>com.apple.IdentityLookup.MessageFilter</string>
		<string>com.apple.remindd</string>
		<string>com.apple.imtranscoding.IMTranscoderAgent</string>
		<string>com.apple.proactive.experiments.responses</string>
		<string>com.apple.triald</string>
		<string>com.apple.avatar.service</string>
		<string>com.apple.avatar.support</string>
		<string>com.apple.NPKNanoPassDaemonConnection.XPC</string>
		<string>com.apple.ClipServices.clipserviced</string>
		<string>com.apple.siri.activation.service</string>
		<string>com.apple.nanophotos.progress</string>
		<string>com.apple.NanoTimeKit.userphotofaceserver</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.itunescloud.remote-request-execution-service</string>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.ScreenTimeAgent.communication</string>
		<string>com.apple.seserviced</string>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.sociallayerd</string>
		<string>com.apple.uikit.viewservice.com.apple.NanoMessageUIViewService</string>
		<string>com.apple.uikit.viewservice.com.apple.NanoMailComposeService</string>
		<string>com.apple.uikit.viewservice.com.apple.WorkoutRemoteViewService</string>
		<string>com.apple.surfboard.applicationservice</string>
		<string>com.apple.CloudSharing.SPIHelper-iOS</string>
		<string>com.apple.siriknowledged.koa.donate</string>
		<string>com.apple.MemojiImageRenderService</string>
		<string>com.apple.MessagesBlastDoorService</string>
		<string>com.apple.voicememod.xpc</string>
		<string>com.apple.dprivacyd</string>
		<string>com.apple.financed.service.financestore</string>
		<string>com.apple.routined.safetyMonitor</string>
		<string>com.apple.CoreRoutine.SafetyMonitor</string>
		<string>com.apple.WorkoutKitXPCService</string>
		<string>com.apple.TextUnderstanding.SmartReplies.Inference</string>
		<string>com.apple.ManagedSettingsAgent</string>
		<string>com.apple.ManagedSettingsAgent.publisher</string>
		<string>com.apple.stickers.api</string>
		<string>com.apple.passd.device-registration</string>
		<string>com.apple.activityawardsd</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.activitysharingd</string>
		<string>com.apple.watchnotificationsui.alertservice</string>
		<string>com.apple.surfboard.scenesessionservice</string>
		<string>com.apple.ProactiveSummarization.server</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.mobileactivationd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.WatchListKit</string>
		<string>com.apple.healthd</string>
		<string>com.apple.imessage.bag</string>
		<string>com.apple.conference</string>
		<string>com.apple.LanguageModeling</string>
		<string>com.apple.ids</string>
		<string>com.apple.ids.debug</string>
		<string>com.apple.CoreNLP</string>
		<string>com.apple.avfaudio</string>
		<string>com.apple.frontboardservices.device_emulation</string>
		<string>com.apple.registration</string>
		<string>com.apple.assistant</string>
		<string>UITextInputContextIdentifiers</string>
		<string>com.apple.ResponseKit</string>
		<string>com.apple.voicetrigger</string>
		<string>com.apple.ImageIO</string>
		<string>com.apple.nanolifestyle.privacy</string>
		<string>PUICNPSPreferences</string>
		<string>com.apple.proactive.experiments.responses</string>
		<string>com.apple.messages.ordering-automation</string>
		<string>com.apple.suggestions</string>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.ScreenTimeAgent.private</string>
		<string>com.apple.NanoSettings.internal</string>
		<string>com.apple.nanobuddy</string>
		<string>com.apple.wallet</string>
		<string>com.apple.Wallet.public</string>
		<string>com.apple.appstored</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.communicationSafetySettings</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.camera</string>
		<string>com.apple.MobileSMS</string>
		<string>com.apple.madrid</string>
		<string>com.apple.handwriting</string>
		<string>com.apple.MobileSMS.CKDNDList</string>
		<string>com.apple.MobileSMSPreview</string>
		<string>com.apple.messages</string>
		<string>UITextInputContextIdentifiers</string>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.imessage.bag</string>
		<string>com.apple.facetime.bag</string>
		<string>PUICNPSPreferences</string>
		<string>com.apple.EmojiCache</string>
		<string>com.apple.messages.nicknames</string>
		<string>com.apple.messages.pinning</string>
		<string>com.apple.messages.text</string>
		<string>com.apple.ScreenTimeAgent.conversation</string>
		<string>com.apple.SocialLayer</string>
		<string>com.apple.keyboard.preferences</string>
		<string>com.apple.messages.commsafety</string>
		<string>com.apple.contacts.sharedProfile</string>
		<string>com.apple.ClarityUI.Messages</string>
		<string>com.apple.IMCoreSpotlight</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>H11ANEInDirectPathClient</string>
		<string>AppleVirtIONeuralEngineDeviceUserClient</string>
	</array>
	<key>com.apple.security.personal-information.addressbook</key>
	<true/>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.configurationprofiles</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.dprivacyd</string>
		<string>com.apple.transparencyd</string>
		<string>com.apple.transparencyd.ids</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
		<string>com.apple.proactive.experiments.responses</string>
		<string>com.apple.avatar.service</string>
		<string>com.apple.avatar.support</string>
		<string>com.apple.stickers.api</string>
		<string>com.apple.mobileactivationd</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.parsecd</string>
	</array>
	<key>com.apple.seserviced.key</key>
	<true/>
	<key>com.apple.seserviced.kmlXpcService</key>
	<true/>
	<key>com.apple.sharesheet.allow-suggestions</key>
	<true/>
	<key>com.apple.sharesheet.recipients</key>
	<true/>
	<key>com.apple.siri.activation.service</key>
	<true/>
	<key>com.apple.siri.task</key>
	<true/>
	<key>com.apple.spotlight.documentunderstanding.entitledattributes</key>
	<true/>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.activateassistant</key>
	<true/>
	<key>com.apple.springboard.allowallcallurls</key>
	<true/>
	<key>com.apple.springboard.delete-application-snapshots</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.proximity-active-bypass</key>
	<true/>
	<key>com.apple.springboard.shortcutitems.customimage</key>
	<true/>
	<key>com.apple.springboard.topButtonFrames</key>
	<true/>
	<key>com.apple.surfboard.always-discard-last-scene</key>
	<true/>
	<key>com.apple.surfboard.prevent-scene-restoration</key>
	<true/>
	<key>com.apple.surfboard.scenesession-updates</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>com.apple.tailspin.dump-output</key>
	<true/>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>modify-calls</string>
		<string>access-calls</string>
		<string>modify-pending-collaboration</string>
		<string>access-call-providers</string>
	</array>
	<key>com.apple.transparency.kt</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>150</string>
		<string>151</string>
		<string>152</string>
		<string>153</string>
		<string>154</string>
		<string>155</string>
		<string>156</string>
		<string>157</string>
		<string>158</string>
		<string>159</string>
		<string>160</string>
		<string>161</string>
		<string>162</string>
		<string>163</string>
		<string>164</string>
		<string>165</string>
		<string>166</string>
		<string>167</string>
		<string>168</string>
		<string>169</string>
		<string>700</string>
		<string>701</string>
		<string>702</string>
		<string>703</string>
		<string>704</string>
		<string>705</string>
	</array>
	<key>com.apple.triald.client</key>
	<true/>
	<key>com.apple.trustkit.orca</key>
	<true/>
	<key>com.apple.usersafety.service</key>
	<string>messages</string>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>fairplay-client</key>
	<string>1025382176</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.TextInput</string>
		<string>trustkit</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 MessagesAssistantExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>cellular-plan</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-encode</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.developer.usersafety.client</key>
	<array>
		<string>analysis</string>
	</array>
	<key>com.apple.imagent</key>
	<true/>
	<key>com.apple.locationd.usage_oracle</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.private.CallHistory.read</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.MobileSMS</string>
	</dict>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Discoverability.Signals</string>
		<string>Discoverability.Usage</string>
	</array>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.dmd.emergency-mode</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.ids.idquery-cache</key>
	<true/>
	<key>com.apple.private.ids.messaging</key>
	<array>
		<string>com.apple.private.alloy.biz</string>
		<string>com.apple.madrid</string>
		<string>com.apple.madrid.lite</string>
	</array>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.imcore.imagent</key>
	<true/>
	<key>com.apple.private.imcore.imdpersistence.data-detection-access</key>
	<true/>
	<key>com.apple.private.imcore.imdpersistence.database-access</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.imcore.spi.database-access</key>
	<true/>
	<key>com.apple.private.intents.extension</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screentime-communication</key>
	<true/>
	<key>com.apple.private.security.storage.CallHistory</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
	<array>
		<string>com.apple.tipsd</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.tipsnext</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/SMS/</string>
		<string>/private/var/tmp/</string>
		<string>/private/var/mobile/tmp/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/com.apple.messages/</string>
		<string>/private/var/mobile/tmp/com.apple.messages/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/CallHistoryDB/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.dmd.emergency-mode</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
		<string>com.apple.CellularPlanDaemon.xpc</string>
		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.imfoundation.IMRemoteURLConnectionAgent</string>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.ScreenTimeAgent.private</string>
		<string>com.apple.dmd.policy</string>
		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.ScreenTimeAgent.communication</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
		<string>com.apple.CallHistorySyncHelper</string>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.ManagedSettingsAgent.publisher</string>
		<string>com.apple.appprotectiond.read</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.ScreenTimeAgent</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.ScreenTimeAgent.conversation</string>
		<string>com.apple.MobileSMS</string>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.security.personal-information.addressbook</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.imagent.embedded.auth</string>
	</array>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>access-calls</string>
		<string>access-call-providers</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>351</string>
	</array>
	<key>com.apple.usersafety.service</key>
	<string>messages</string>
</dict>
</plist>

```

### 🆕 MessagesAssistantUIExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantUIExtension.appex/MessagesAssistantUIExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.IdentityLookup.MessageFilter</key>
	<string></string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.backboardd.proximityDetection</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-encode</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.icloud.fmfd.access</key>
	<true/>
	<key>com.apple.imagent</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.emergency-mode</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.imcore.imdpersistence.database-access</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceMicrophone</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceReminders</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.private.ubiquity-kvstore-identifier</key>
	<string>com.apple.MobileSMS</string>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Audio/Tunings/Generic/AU/</string>
		<string>/Library/Audio/Tunings/Generic/AU/aufx-epvd-appl.plist</string>
		<string>/private/var/tmp/</string>
		<string>/private/var/mobile/tmp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/SMS/</string>
		<string>/Library/Caches/com.apple.MobileSMS/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.dmd.emergency-mode</string>
		<string>com.apple.suggestd.contacts</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.MobileSMS</string>
		<string>com.apple.mobilephone</string>
		<string>com.apple.ScreenTimeAgent.conversation</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.dprivacyd</string>
		<string>com.apple.siri.vocabularyupdates</string>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.ScreenTimeAgent.private</string>
		<string>com.apple.dmd.policy</string>
		<string>com.apple.imfoundation.IMRemoteURLConnectionAgent</string>
	</array>
	<key>com.apple.wifi.manager-access</key>
	<true/>
</dict>
</plist>

```

### 🆕 MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.IdentityLookup.MessageFilter</key>
	<string></string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.StatusKit.publish.types</key>
	<array>
		<string>com.apple.availability</string>
		<string>com.apple.focus.status</string>
		<string>com.apple.offgrid.status</string>
	</array>
	<key>com.apple.StatusKit.subscribe.types</key>
	<array>
		<string>com.apple.availability</string>
		<string>com.apple.focus.status</string>
		<string>com.apple.offgrid.status</string>
	</array>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.backboardd.proximityDetection</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-encode</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.developer.siri</key>
	<true/>
	<key>com.apple.developer.usersafety.client</key>
	<array>
		<string>analysis</string>
	</array>
	<key>com.apple.findmy.findmylocate.friendshipservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.locationservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.settings</key>
	<true/>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.icloud.fmfd.access</key>
	<true/>
	<key>com.apple.imagent</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.MobileSMS</string>
	</dict>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.emergency-mode</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.donotdisturb.modeconfiguration.availability.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.donotdisturb.settings.request.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.ids.idquery-cache</key>
	<true/>
	<key>com.apple.private.ids.messaging</key>
	<array>
		<string>com.apple.private.alloy.biz</string>
		<string>com.apple.madrid</string>
		<string>com.apple.madrid.lite</string>
	</array>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.imcore.imdpersistence.database-access</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.imcore.imtranscoderservice</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screentime-communication</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.MessagesMetaData</key>
	<true/>
	<key>com.apple.private.security.storage.PassKit</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceReminders</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.sage.textcomposition</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Audio/Tunings/Generic/AU/</string>
		<string>/Library/Audio/Tunings/Generic/AU/aufx-epvd-appl.plist</string>
		<string>/private/var/tmp/</string>
		<string>/private/var/mobile/tmp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/SMS/</string>
		<string>/Library/Caches/com.apple.MobileSMS/</string>
		<string>/Library/MessagesMetaData/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.dmd.emergency-mode</string>
		<string>com.apple.dmd.policy</string>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.ScreenTimeAgent.private</string>
		<string>com.apple.ScreenTimeAgent.communication</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.sage.textcomposition</string>
		<string>com.apple.StatusKit.subscribe</string>
		<string>com.apple.StatusKit.publish</string>
		<string>com.apple.donotdisturb.service</string>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.suggestd.contacts</string>
		<string>com.apple.dprivacyd</string>
		<string>com.apple.MessagesBlastDoorService</string>
		<string>com.apple.siri.vocabularyupdates</string>
		<string>com.apple.imtranscoding.IMTranscoderAgent</string>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.ManagedSettingsAgent</string>
		<string>com.apple.ManagedSettingsAgent.publisher</string>
		<string>com.apple.findmy.findmylocate.friendshipservice</string>
		<string>com.apple.findmy.findmylocate.locationservice</string>
		<string>com.apple.findmy.findmylocate.settings</string>
		<string>com.apple.mobileactivationd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.springboard</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.MobileSMS</string>
		<string>com.apple.MobileSMSPreview</string>
		<string>com.apple.madrid</string>
		<string>com.apple.mobilephone</string>
		<string>UITextInputContextIdentifiers</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.trustkit.orca</key>
	<true/>
	<key>com.apple.usernotifications.legacy-extension</key>
	<true/>
	<key>com.apple.usersafety.service</key>
	<string>messages</string>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.TextInput</string>
		<string>trustkit</string>
	</array>
</dict>
</plist>

```

### 🆕 MessagesPluginNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.asktod</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
	<true/>
	<key>com.apple.imagent</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceReminders</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.asktod</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
</dict>
</plist>

```

### 🆕 MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.IdentityLookup.MessageFilter</key>
	<string></string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.StatusKit.publish.types</key>
	<array>
		<string>com.apple.availability</string>
		<string>com.apple.focus.status</string>
		<string>com.apple.offgrid.status</string>
	</array>
	<key>com.apple.StatusKit.subscribe.types</key>
	<array>
		<string>com.apple.availability</string>
		<string>com.apple.focus.status</string>
		<string>com.apple.offgrid.status</string>
	</array>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.backboardd.proximityDetection</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-encode</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.developer.siri</key>
	<true/>
	<key>com.apple.developer.usersafety.client</key>
	<array>
		<string>analysis</string>
	</array>
	<key>com.apple.findmy.findmylocate.friendshipservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.locationservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.settings</key>
	<true/>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.icloud.fmfd.access</key>
	<true/>
	<key>com.apple.imagent</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.MobileSMS</string>
	</dict>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.emergency-mode</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.donotdisturb.modeconfiguration.availability.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.donotdisturb.settings.request.client-identifiers</key>
	<array>
		<string>com.apple.messages</string>
	</array>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.ids.idquery-cache</key>
	<true/>
	<key>com.apple.private.ids.messaging</key>
	<array>
		<string>com.apple.private.alloy.biz</string>
		<string>com.apple.madrid</string>
		<string>com.apple.madrid.lite</string>
	</array>
	<key>com.apple.private.ids.phone-number-authentication</key>
	<true/>
	<key>com.apple.private.imcore.imdpersistence.database-access</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.imcore.imtranscoderservice</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screentime-communication</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.MessagesMetaData</key>
	<true/>
	<key>com.apple.private.security.storage.PassKit</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceReminders</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.sage.textcomposition</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Audio/Tunings/Generic/AU/</string>
		<string>/Library/Audio/Tunings/Generic/AU/aufx-epvd-appl.plist</string>
		<string>/private/var/tmp/</string>
		<string>/private/var/mobile/tmp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/SMS/</string>
		<string>/Library/Caches/com.apple.MobileSMS/</string>
		<string>/Library/MessagesMetaData/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.dmd.emergency-mode</string>
		<string>com.apple.dmd.policy</string>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.ScreenTimeAgent.private</string>
		<string>com.apple.ScreenTimeAgent.communication</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.sage.textcomposition</string>
		<string>com.apple.StatusKit.subscribe</string>
		<string>com.apple.StatusKit.publish</string>
		<string>com.apple.donotdisturb.service</string>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.suggestd.contacts</string>
		<string>com.apple.dprivacyd</string>
		<string>com.apple.MessagesBlastDoorService</string>
		<string>com.apple.siri.vocabularyupdates</string>
		<string>com.apple.imtranscoding.IMTranscoderAgent</string>
		<string>com.apple.mediaanalysisd.analysis</string>
		<string>com.apple.ManagedSettingsAgent</string>
		<string>com.apple.ManagedSettingsAgent.publisher</string>
		<string>com.apple.findmy.findmylocate.friendshipservice</string>
		<string>com.apple.findmy.findmylocate.locationservice</string>
		<string>com.apple.findmy.findmylocate.settings</string>
		<string>com.apple.mobileactivationd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.ScreenTimeAgent</string>
		<string>com.apple.springboard</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.MobileSMS</string>
		<string>com.apple.MobileSMSPreview</string>
		<string>com.apple.madrid</string>
		<string>com.apple.mobilephone</string>
		<string>UITextInputContextIdentifiers</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.trustkit.orca</key>
	<true/>
	<key>com.apple.usernotifications.legacy-extension</key>
	<true/>
	<key>com.apple.usersafety.service</key>
	<string>messages</string>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.TextInput</string>
		<string>trustkit</string>
	</array>
</dict>
</plist>

```

### 🆕 SafariLinkExtension

> `/private/var/staged_system_apps/MobileSafari.app/Extensions/SafariLinkExtension.appex/SafariLinkExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.Safari.History</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/MobileSafari.framework</string>
	</array>
	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.SafariBookmarksSyncAgent</string>
		<string>com.apple.Safari.History.Service</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.mobilesafarishared</string>
		<string>com.apple.WebUI</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
</dict>
</plist>

```

### 🆕 MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobilesafari</string>
	<key>aps-environment</key>
	<string>production</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>public-cellular-plan</string>
		<string>public-esim-qr-code</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.appattest.spi</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.assistant.dictation.prerecorded</key>
	<true/>
	<key>com.apple.authentication-services.access-credential-identities</key>
	<true/>
	<key>com.apple.authentication-services.allow-authentication-request-any-rpid</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.bluetooth.internal</key>
	<true/>
	<key>com.apple.chrono.invalidate-timelines</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.coreduetd.knowledge</key>
	<true/>
	<key>com.apple.developer.WebKit.ServiceWorkers</key>
	<true/>
	<key>com.apple.developer.browser.app-installation</key>
	<true/>
	<key>com.apple.developer.default-data-protection</key>
	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>iCloud.com.apple.mobilesafari</string>
		<string>com.apple.SafariShared.History</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudDocuments</string>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.networking.HotspotConfiguration</key>
	<true/>
	<key>com.apple.developer.web-browser</key>
	<true/>
	<key>com.apple.diagnosticpipeline.request</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.features.all-access</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.geoservices.map-subscriptions.check-existence</key>
	<true/>
	<key>com.apple.geoservices.map-subscriptions.size-estimate</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.intents.uiextension.discovery</key>
	<true/>
	<key>com.apple.itunesstored.accounts</key>
	<true/>
	<key>com.apple.itunesstored.downloads</key>
	<true/>
	<key>com.apple.itunesstored.kvs</key>
	<true/>
	<key>com.apple.itunesstored.lookup</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.itunesstored.software-library</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.locationd.authorizeapplications</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.time_zone</key>
	<true/>
	<key>com.apple.managedconfiguration.feature-setting.allowPasswordAutoFill</key>
	<true/>
	<key>com.apple.managedconfiguration.feature-setting.safariAcceptCookies</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
	<array>
		<string>UIInstallation</string>
	</array>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.multitasking.systemappassertions</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.nfcd.session.reader.internal</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.private.BarcodeSupport.can-suppress-app-clip-code-url-authorization</key>
	<true/>
	<key>com.apple.private.ClipServices</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.lookup</key>
	<dict>
		<key>appData</key>
		<array>
			<string>com.apple.Passwords</string>
		</array>
	</dict>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceIDData</string>
		<string>UniqueChipID</string>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
		<string>ProvisioningUniqueDeviceID</string>
	</array>
	<key>com.apple.private.Safari.History</key>
	<true/>
	<key>com.apple.private.Safari.PasswordBreachHelper</key>
	<true/>
	<key>com.apple.private.WebClips.read-write</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/MobileSafari.framework</string>
	</array>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstorecomponents.media-client-id</key>
	<string>com.apple.searchui</string>
	<key>com.apple.private.appstorecomponents.media-client-version</key>
	<string>1</string>
	<key>com.apple.private.appstorecomponents.media-clients</key>
	<dict>
		<key>SmartAppBanner</key>
		<dict>
			<key>id</key>
			<string>com.apple.mobilesafari.SmartAppBanner</string>
			<key>version</key>
			<string>1</string>
		</dict>
	</dict>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Clip</string>
	</array>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.SafariCloudHistoryConfiguration</string>
		<string>com.apple.MobileAsset.CoreSuggestions</string>
		<string>com.apple.MobileAsset.SafariBackgroundImage</string>
		<string>com.apple.MobileAsset.UAF.SafariBrowsingAssistant</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Media.NowPlaying</string>
		<string>App.InFocus</string>
		<string>App.Install</string>
		<string>CarPlay.Connected</string>
		<string>Motion.Activity</string>
		<string>Device.ScreenLocked</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>App.WebUsage</string>
		<string>Discoverability.Signals</string>
		<string>Discoverability.Usage</string>
		<string>Safari.AutoPlay</string>
		<string>Safari.WebPagePerformance</string>
		<string>Safari.Navigations</string>
		<string>Safari.PageLoad</string>
		<string>Safari.WindowProxy</string>
		<string>Safari.Browsing.Assistant</string>
	</array>
	<key>com.apple.private.can-load-any-content-blocker</key>
	<true/>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.canModifyAppLinkPermissions</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.SafariShared.History</key>
		<string>com.apple.SafariShared.History</string>
	</dict>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.copresence</key>
	<true/>
	<key>com.apple.private.copresence.stable-app-identifier</key>
	<string>com.apple.Safari</string>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.coreservices.lsuseractivityd.bestappsuggestion</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.email</key>
	<true/>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.imcore.imagent</key>
	<true/>
	<key>com.apple.private.in-app-payments</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>siriRemembers</string>
	</array>
	<key>com.apple.private.internal-style-asam</key>
	<true/>
	<key>com.apple.private.interstellar.data-access</key>
	<string>*</string>
	<key>com.apple.private.keychain.kcsharing.client</key>
	<true/>
	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>
	<string>*</string>
	<key>com.apple.private.mobileinstall.xpc-services-enabled</key>
	<true/>
	<key>com.apple.private.networkserviceproxy</key>
	<true/>
	<key>com.apple.private.octagon</key>
	<true/>
	<key>com.apple.private.osanalytics.defaults.allow</key>
	<true/>
	<key>com.apple.private.parsec.default-client</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.private.rsr-cryptex-access</key>
	<true/>
	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>
	<true/>
	<key>com.apple.private.safari.can-use-history-push-agent</key>
	<true/>
	<key>com.apple.private.safari.can-use-search-helper</key>
	<true/>
	<key>com.apple.private.safari.offlinereadinglist</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>EnableQuickLookSandboxResources</string>
	</array>
	<key>com.apple.private.security.storage.Safari</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.sportskit.client</key>
	<true/>
	<key>com.apple.private.subscriptionservice.web-sources.read-write</key>
	<true/>
	<key>com.apple.private.suggestions.events</key>
	<true/>
	<key>com.apple.private.suggestions.urls</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceListenEvent</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotosAdd</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceCalendar</string>
	</array>
	<key>com.apple.private.translation</key>
	<true/>
	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
	<array>
		<string>com.apple.mobilesafari</string>
		<string>com.apple.tipsd</string>
	</array>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.Passwords</string>
	</array>
	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.remotemanagementd.ask-for-time</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.tipsnext</string>
		<string>group.com.apple.safari</string>
	</array>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.device.usb</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/MobileIdentityData/</string>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/Applications/</string>
		<string>/private/var/db/os_eligibility/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_SafariBrowsingAssistant/purpose_auto/</string>
		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.storeservices/</string>
		<string>/Library/Caches/com.apple.ClipServices/</string>
		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
		<string>/Library/UnifiedAssetFramework/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Safari/AutoFillQuirks.plist</string>
		<string>/private/var/mobile/Library/com.apple.siri.inference/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.DocumentManagerCore.Downloads</string>
		<string>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</string>
		<string>com.apple.coreservices.lsbestappsuggestionmanager.xpc</string>
		<string>com.apple.suggestd.urls</string>
		<string>com.apple.LORemoteUIPinService</string>
		<string>com.apple.remotemanagementd.management-state</string>
		<string>com.apple.SafariBookmarksSyncAgent</string>
		<string>com.apple.Safari.SafeBrowsing.Service</string>
		<string>com.apple.SafariCloudHistoryPushAgent</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.parsecd</string>
		<string>com.apple.parsec-fbf</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.internal.safaricyclerd</string>
		<string>com.apple.watchlistd.xpc</string>
		<string>com.apple.Safari.SandboxBroker</string>
		<string>com.apple.BarcodeSupport.ParsingService</string>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.ManagedSettingsAgent</string>
		<string>com.apple.Safari.History</string>
		<string>com.apple.SharingServices</string>
		<string>com.apple.SharedWebCredentials</string>
		<string>com.apple.dmd.policy</string>
		<string>com.apple.UsageTrackingAgent</string>
		<string>com.apple.UsageTrackingAgent.private</string>
		<string>com.apple.remotemanagementd.ask</string>
		<string>com.apple.passd.account</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.AppSSO.service-xpc</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.translationd</string>
		<string>com.apple.ClipServices.clipserviced</string>
		<string>com.apple.security.octagon</string>
		<string>com.apple.WebKit.WebAuthn</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.datamigrator</string>
		<string>com.apple.online-auth-agent.xpc</string>
		<string>com.apple.Safari.SearchHelper</string>
		<string>com.apple.misagent</string>
		<string>com.apple.sportsd.xpc</string>
		<string>com.apple.email.maild</string>
		<string>com.apple.AuthenticationServices.AutoFill</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.webprivacyd</string>
		<string>com.apple.trial.status</string>
		<string>com.apple.Safari.History.Service</string>
		<string>com.apple.Safari.PasswordBreachHelper</string>
		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>
		<string>com.apple.sociallayerd</string>
		<string>com.apple.networkserviceproxy</string>
		<string>com.apple.synapse.contentlinkingd</string>
		<string>com.apple.synapse.link-context-service</string>
		<string>com.apple.ind.cloudfeatures</string>
		<string>com.apple.ak.privateemail.xpc</string>
		<string>com.apple.donotdisturb.appconfiguration.service</string>
		<string>com.apple.security.kcsharing</string>
		<string>com.apple.SharePlay.GroupSessionService</string>
		<string>com.apple.siri.sirireaderd</string>
		<string>com.apple.sirittsd</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.managedappdistributiond.xpc</string>
		<string>com.apple.AppDistributionLaunchAngel</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.ManagedSettingsAgent.publisher</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.ak.signinwithapple.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.CloudSubscriptionFeatures.datadetectors</string>
		<string>com.apple.suggestions</string>
		<string>com.apple.SocialLayer</string>
		<string>com.apple.UnifiedAssetFramework</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.mobilesafarishared</string>
		<string>com.apple.WebUI</string>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.webinspectord</string>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.newscore</string>
		<string>com.apple.suggestions</string>
		<string>com.apple.Passwords</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.mobileactivationd</string>
	</array>
	<key>com.apple.sharing.Client</key>
	<true/>
	<key>com.apple.sharing.DeviceDiscovery</key>
	<true/>
	<key>com.apple.sharing.Services</key>
	<true/>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.addWebClipToHomeScreen</key>
	<true/>
	<key>com.apple.springboard.appbackgroundstyle</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.statusbarstyleoverrides</key>
	<true/>
	<key>com.apple.springboard.statusbarstyleoverrides.coordinator</key>
	<array>
		<string>UIStatusBarStyleOverrideWebRTCCapture</string>
		<string>UIStatusBarStyleOverrideWebRTCAudioCapture</string>
	</array>
	<key>com.apple.springboard.systemNotesPresentation</key>
	<true/>
	<key>com.apple.springboard.wallpaperAnimationSuspension</key>
	<true/>
	<key>com.apple.springboard.webClipService</key>
	<true/>
	<key>com.apple.symptom_analytics.configure</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.synapse.allowLinkContextRequests</key>
	<true/>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>access-call-providers</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>342</string>
	</array>
	<key>com.apple.trial.status.deployment-environment.allow</key>
	<array>
		<integer>2</integer>
	</array>
	<key>com.apple.watchlist.private</key>
	<true/>
	<key>fairplay-client</key>
	<integer>965772570</integer>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.cfnetwork</string>
		<string>com.apple.identities</string>
		<string>com.apple.mobilesafari</string>
		<string>com.apple.certificates</string>
		<string>com.apple.safari.credit-cards</string>
		<string>com.apple.safari.history</string>
		<string>com.apple.safari.WebCrypto.master</string>
		<string>com.apple.ProtectedCloudStorage</string>
		<string>com.apple.webkit.webauthn</string>
		<string>apple</string>
		<string>lockdown-identities</string>
		<string>com.apple.password-manager</string>
		<string>com.apple.password-manager.personal</string>
		<string>com.apple.cfnetwork-recently-deleted</string>
		<string>com.apple.password-manager-recently-deleted</string>
		<string>com.apple.webkit.webauthn-recently-deleted</string>
		<string>com.apple.password-manager.personal-recently-deleted</string>
		<string>com.apple.password-manager.generated-passwords</string>
		<string>com.apple.cfnetwork.testing</string>
		<string>com.apple.password-manager.testing</string>
		<string>com.apple.webkit.webauthn.testing</string>
		<string>com.apple.password-manager.website-metadata</string>
		<string>com.apple.password-manager.website-metadata.testing</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>vm-pressure-level</key>
	<true/>
</dict>
</plist>

```

### 🆕 SafariWidgetExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobilesafari.SafariWidgetExtension</string>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.private.security.storage.Safari</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.safari</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Safari/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.SafariBookmarksSyncAgent</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.mobilesafarishared</string>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.WebUI</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 com.apple.mobilesafari.SafariDiagnosticExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.can-load-any-content-blocker</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.private.security.storage.Safari</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/CrashReporter/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Safari/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.SafariBookmarksSyncAgent</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.Safari.SandboxBroker

> `/private/var/staged_system_apps/MobileSafari.app/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker`

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
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.news.ScoringService</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### NewsNotificationServiceExtension

> `/private/var/staged_system_apps/News.app/PlugIns/NewsNotificationServiceExtension.appex/NewsNotificationServiceExtension`

```diff

 		<string>/Library/UserNotifications/</string>
 		<string>/Library/News/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.news.ScoringService</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.newscore</string>

```
### NewsTag

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag`

```diff

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.newsd.analytics</string>
+		<string>com.apple.news.ScoringService</string>
 	</array>
 </dict>
 </plist>

```
### NewsToday2

> `/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2`

```diff

 		<string>com.apple.newsd.analytics</string>
 		<string>com.apple.newsd.download</string>
 		<string>com.apple.newsd.today-feed</string>
+		<string>com.apple.news.ScoringService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.Passbook</string>
+		<string>com.apple.PassbookUIService</string>
 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.cfnetwork</string>
+		<string>com.apple.cfnetwork.testing</string>
 		<string>com.apple.password-manager</string>
+		<string>com.apple.password-manager.testing</string>
 		<string>com.apple.webkit.webauthn</string>
+		<string>com.apple.webkit.webauthn.testing</string>
 		<string>com.apple.password-manager.website-metadata</string>
+		<string>com.apple.password-manager.website-metadata.testing</string>
 		<string>com.apple.sharing.safaripasswordsharing</string>
+		<string>com.apple.sharing.safaripasswordsharing.testing</string>
 		<string>com.apple.safari.history</string>
+		<string>com.apple.safari.history.testing</string>
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
 		<string>com.apple.password-manager.generated-passwords</string>
+		<string>com.apple.password-manager.generated-passwords.testing</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobileslideshow</string>
	<key>backupd-connection-initiate</key>
	<true/>
	<key>checklessPersistentURLTranslation</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>public-cellular-plan</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.CoreRoutine.LocationOfInterest</key>
	<true/>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-access-to-device-list</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.coreaudio.allow-amr-decode</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.coreduetd.people</key>
	<true/>
	<key>com.apple.developer.associated-domains</key>
	<array/>
	<key>com.apple.developer.extension-host.photo-editing</key>
	<true/>
	<key>com.apple.developer.networking.HotspotConfiguration</key>
	<true/>
	<key>com.apple.developer.networking.multicast</key>
	<true/>
	<key>com.apple.developer.siri</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.photos.kvstore</string>
	<key>com.apple.excludes-extensions</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.Feedback</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.intents.intents-helper</key>
	<true/>
	<key>com.apple.itunescloud.in-app-message-service</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.mediastream.mstreamd-access</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.multitasking.systemappassertions</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.photos.intelligence.mcDefaultOverwrite</key>
	<true/>
	<key>com.apple.posterboardservices.data-store</key>
	<true/>
	<key>com.apple.posterboardui.externalEditing</key>
	<true/>
	<key>com.apple.private.BarcodeSupport.can-suppress-app-clip-code-url-authorization</key>
	<true/>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>CLIENT_ENTITLEMENT</string>
		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
		<string>PURGE_ENTITLEMENT</string>
		<string>CANCEL_PURGE_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.ClipServices</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.acg.autoloops</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.accounts.bypassguestmoderestrictions</key>
	<true/>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.allow-external-storage</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/PhotosUIPrivate.framework</string>
		<string>/System/Library/PrivateFrameworks/PhotosUICore.framework</string>
	</array>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.VideoAppsMusicAssets3</string>
		<string>com.apple.MobileAsset.VideoAppsMusicAssets</string>
		<string>com.apple.MobileAsset.MediaSupport</string>
		<string>com.apple.MobileAsset.PhotosCuratedMusicLibraryAsset</string>
		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.assetsd.nebulad.access</key>
	<string>photos</string>
	<key>com.apple.private.avatar.store</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Photos.Search</string>
		<string>Photos.Map</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>Discoverability.Signals</string>
		<string>Discoverability.Usage</string>
	</array>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.cloudphotod.access</key>
	<string>management</string>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.feedback.centralized-feedback</key>
	<true/>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.imagecapturecore.authorization_bypass</key>
	<true/>
	<key>com.apple.private.imcore.imagent</key>
	<true/>
	<key>com.apple.private.ind.client</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>Photos</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AeroML.RawEvent.PhotosSearchSession</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Delete</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Edit</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Engagement</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Favorite</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Memories.Curation</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Memories.MoviePlayed;</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Memories.Notification</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Memories.Shared</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Memories.Viewed</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.MemoryCreation</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Photos.Share</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>photosAutonamingView</string>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>inferenceFeaturesECR</string>
		<string>entitySubgraph</string>
		<string>entitySummary</string>
		<string>eventSubgraph</string>
		<string>peopleSubgraph</string>
		<string>appEntityRelevanceRanking</string>
		<string>personEntityRelevanceRanking</string>
		<string>loiEntityRelevanceRanking</string>
		<string>hasAssociationSubgraph</string>
	</array>
	<key>com.apple.private.lockdown.finegrained-get</key>
	<array>
		<string>NULL/ActivationPrivateKey</string>
		<string>NULL/DeviceCertificate</string>
	</array>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.mediaanalysisd.datamanagement.embedding</key>
	<true/>
	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
	<true/>
	<key>com.apple.private.messages.associated-message-extension-bundle-identifiers</key>
	<array>
		<string>com.apple.mobileslideshow.PhotosMessagesApp</string>
	</array>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.allowassetexpunge</key>
	<true/>
	<key>com.apple.private.photos.allowmemorymutation</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.allow</key>
	<true/>
	<key>com.apple.private.photos.cpanalytics.cache.read</key>
	<true/>
	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
	<true/>
	<key>com.apple.private.photos.service.debug</key>
	<true/>
	<key>com.apple.private.photos.service.diagnostics</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.internal.resource</key>
	<true/>
	<key>com.apple.private.photos.service.multilibrary</key>
	<true/>
	<key>com.apple.private.photos.service.notification</key>
	<true/>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
		<string>group.com.apple.tipsnext</string>
	</array>
	<key>com.apple.private.security.storage.MessagesMetaData</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.suggestions.contacts</key>
	<true/>
	<key>com.apple.private.swc.system-app</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.private.tcc.manager.access.delete</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.private.translation</key>
	<true/>
	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
	<array>
		<string>com.apple.tipsd</string>
	</array>
	<key>com.apple.private.xpc.domain-extension</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite</key>
	<true/>
	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.posterkit.host</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
		<string>group.com.apple.tipsnext</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_MagicCleanup/purpose_auto/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/var/mobile/Library/Caches/com.apple.ShareNameAndPhoto</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.ClipServices/</string>
		<string>/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>
		<string>/Library/Caches/com.apple.mobileslideshow/</string>
		<string>/Media/PhotoData/</string>
		<string>/Library/MessagesMetaData/NickNameCache/</string>
		<string>/Library/UnifiedAssetFramework/</string>
		<string>/Library/com.apple.modelcatalog/sideload/</string>
		<string>/Library/Application Support/com.apple.palette.green.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Media/PhotoData/</string>
		<string>/Library/LiveFiles/</string>
		<string>/Library/Logs/MediaServices/</string>
		<string>/Library/UnifiedAssetFramework/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceAcceleratorParavirtClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.coreduetd.context</string>
		<string>com.apple.coreduetd</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
		<string>com.apple.rtcreportingd</string>
		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>
		<string>com.apple.itunescloud.in-app-message-service</string>
		<string>com.apple.xpc.amsengagementd</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.translationd</string>
		<string>com.apple.geoanalyticsd</string>
		<string>com.apple.posterboardservices.dataModel</string>
		<string>com.apple.posterboardservices.services</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.intelligenceplatform.Feedback</string>
		<string>com.apple.posterboardui.services</string>
		<string>com.apple.itunescloudd.tcchelper</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.generativeexperiences.availabilityService</string>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.itunescloud.remote-request-execution-service</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.mediaanalysisd.embeddingstore</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SocialLayer</string>
		<string>com.apple.Music</string>
		<string>com.apple.parsecd</string>
		<string>com.apple.avfoundation.videoperformancehud</string>
		<string>com.apple.OmniSearch</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.gms.availability</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.photoanalysisd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.WallpaperKit</string>
		<string>com.apple.springboard</string>
		<string>com.apple.itunescloud</string>
		<string>com.apple.itunescloud.internal</string>
		<string>com.apple.coreimage</string>
		<string>com.apple.tokengeneration</string>
		<string>com.apple.trustedmlclient</string>
		<string>com.apple.trustedcloudcompute</string>
	</array>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.sharesheet.allow-custom-view</key>
	<true/>
	<key>com.apple.siri.synapse</key>
	<true/>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.allowallcallurls</key>
	<true/>
	<key>com.apple.springboard.externaldisplay.displayArrangements</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
	<key>com.apple.springboard.topButtonFrames</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>391</string>
		<string>392</string>
		<string>393</string>
		<string>394</string>
	</array>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>com.apple.wlan.authentication</key>
	<true/>
	<key>fairplay</key>
	<integer>1615507317</integer>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.youtube.credentials</string>
		<string>com.apple.videouploadplugins.credentials</string>
		<string>apple</string>
		<string>com.apple.airplay</string>
		<string>com.apple.social.oauthurl</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>MobileSlideShow</string>
	</array>
</dict>
</plist>

```

### 🆕 PhotosMemoriesNotificationUpdates

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosMemoriesNotificationUpdates.appex/PhotosMemoriesNotificationUpdates`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobileslideshow.photosmemoriesnotificationupdates</string>
	<key>com.apple.private.photos.service.notification</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/PhotoData/</string>
	</array>
</dict>
</plist>

```

### 🆕 PhotosNotificationsUpdates

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosNotificationsUpdates.appex/PhotosNotificationsUpdates`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobileslideshow.photosnotifications-updates</string>
	<key>com.apple.mediastream.mstreamd-access</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.notification</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
	<array>
		<string>com.apple.photos.kvstore</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Media/PhotoData/</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```

### 🆕 PhotosReliveWidget

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobileslideshow.PhotosReliveWidget</string>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.suggestion</string>
		<string>photos.face</string>
		<string>photos.memory</string>
		<string>photos.person</string>
		<string>photos.scene</string>
	</array>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobileslideshow</string>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.XPCStoreOptIn</key>
	<true/>
	<key>com.apple.private.photos.allowmemorymutation</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.notification</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/DCIM/</string>
		<string>/Media/PhotoStreamsData/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
		<string>com.apple.chronoservices</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.social.StreamShareService

> `/private/var/staged_system_apps/Photos.app/PlugIns/com.apple.social.StreamShareService.appex/com.apple.social.StreamShareService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.developer.auto-elect-plugin</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobileslideshow</string>
	</dict>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.security.storage.Photos</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/PhotoData/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.suggestd.contacts</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
</dict>
</plist>

```

### 🆕 PodcastsTranscripts

> `/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts`

- No entitlements *(yet)*
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
-	<key>com.apple.private.appintents-bundle-absolute-paths</key>
-	<array>
-		<string>/System/Library/PrivateFrameworks/PodcastsUI.framework</string>
-	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<dict>
 			<key>Sets</key>
 			<dict>
-				<key>Podcasts.Entity</key>
+				<key>Podcasts.Podcast</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### StocksWidget

> `/private/var/staged_system_apps/Stocks.app/PlugIns/StocksWidget.appex/StocksWidget`

```diff

 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.companionappd</string>
 		<string>com.apple.chronoservices</string>
+		<string>com.apple.news.ScoringService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### VoiceMemosIntentsExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension`

```diff

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
+	<array>
+		<string>com.apple.tipsd</string>
+	</array>
 	<key>com.apple.private.voicememod.client</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceMemos.shared</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### VoiceMemosShareExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension`

```diff

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
+	<array>
+		<string>com.apple.tipsd</string>
+	</array>
 	<key>com.apple.private.voicememod.client</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceMemos.shared</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### VoiceMemos

> `/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos`

```diff

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
+	<array>
+		<string>com.apple.tipsd</string>
+	</array>
 	<key>com.apple.private.voicememod.client</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceMemos.shared</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### appprotectiondiagnose

> `/usr/bin/appprotectiondiagnose`

```diff

 <dict>
 	<key>com.apple.appprotectiond.maintenance.access</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 </dict>
 </plist>
 

```
### csfdiagnose

> `/usr/bin/csfdiagnose`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.icloud.gm</string>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.cloud.quota</string>
 		<string>com.apple.mobileslideshow</string>

```
### SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

 	<true/>
 	<key>com.apple.private.sidecarRelay</key>
 	<true/>
-	<key>com.apple.private.situational-awareness.breakthrough-shape</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.RemoteDisplay</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.private.corewifi-xpc</string>
-		<string>com.apple.situational-awareness.breakthrough-shape</string>
-		<string>com.apple.surfboard.sharingmodeservice</string>
 		<string>com.apple.timesync.expositor</string>
 		<string>com.apple.timesync.ptp.manager</string>
 		<string>com.apple.timesync.manager</string>

 	<true/>
 	<key>com.apple.springboard.secureAppAssertion</key>
 	<true/>
-	<key>com.apple.surfboard.immersion-client</key>
-	<true/>
-	<key>com.apple.surfboard.scenesession-updates</key>
-	<true/>
-	<key>com.apple.surfboard.sharing-mode-client</key>
-	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>com.apple.wifi.peer_traffic_registration</key>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	<true/>
 	<key>com.apple.hid.transport.user-access</key>
 	<true/>
+	<key>com.apple.iokit.IOPort.TRM.user-access</key>
+	<true/>
 	<key>com.apple.iokit.IOPort.user-access</key>
 	<true/>
 	<key>com.apple.iokit.IOPortFamily</key>

```
### announced

> `/usr/libexec/announced`

```diff

 	<true/>
 	<key>com.apple.FaceTime.NoPrompt</key>
 	<true/>
+	<key>com.apple.announced.client</key>
+	<true/>
+	<key>com.apple.announced.clientid</key>
+	<string>com.apple.announced</string>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.assistant.multiuser.service</key>
+	<true/>
+	<key>com.apple.assistant.multiuser.service.remora</key>
+	<true/>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-opus-codec</key>

 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 	<array>
 		<string>DeviceClassNumber</string>
 	</array>
+	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
+	<true/>
+	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<array>
 		<string>com.apple.private.alloy.intercom</string>

 	<true/>
 	<key>com.apple.private.security.storage.SiriReferenceResolution</key>
 	<true/>
+	<key>com.apple.private.sessionkit.custom-platter-target</key>
+	<true/>
+	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.Home</string>
 		<string>com.apple.NanoHome</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/usr/libexec/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.announced.localplaybacksession</string>
+		<string>com.apple.announced.reachability</string>
+		<string>com.apple.announced.remoteplaybacksession</string>
+		<string>com.apple.announced.server</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.contactsd</string>

 		<string>com.apple.videoconference.camera</string>
 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.sessionservices</string>
+		<string>com.apple.assistant.multiuser.service</string>
+		<string>com.apple.assistant.multiuser.service.remora</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<string>com.apple.appleaccountd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
-	<key>com.apple.Contacts.database-allow</key>
-	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 		<string>com.apple.appleaccount.custodian</string>
 		<string>com.apple.appleaccount.beneficiary</string>
 		<string>com.apple.appleaccount.beneficiary.private</string>
-		<string>com.apple.appleaccount.identity</string>
-		<string>com.apple.appleaccount.identity.private</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>

 	<true/>
 	<key>com.apple.imagent.chat</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

 		<string>com.apple.appleaccount.beneficiary</string>
 		<key>com.apple.appleaccount.custodian.private</key>
 		<string>com.apple.appleaccount.custodian</string>
-		<key>com.apple.appleaccount.identity.private</key>
-		<string>com.apple.appleaccount.identity.private</string>
 	</dict>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	</array>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>entityTagging</string>
+		<string>visualIdentifier</string>
+		<string>hasAssociationSubgraph</string>
+		<string>phPersonIdentifierMap</string>
+	</array>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>
 	<key>com.apple.private.notificationcenter-system</key>

 	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.storage.IntelligencePlatform</key>
+	<true/>
 	<key>com.apple.private.security.storage.appleaccountd</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.AppSSO.service-xpc</string>
 		<string>com.apple.usymptomsd</string>
+		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 appleh16camerad

> `/usr/libexec/appleh16camerad`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.driver.VADResource.user-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.photondetector.iokit-user-access</key>
	<true/>
	<key>com.apple.private.CoreRepairCore.repairInfo</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.cmio.extension.configuration</key>
	<true/>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>AGXDeviceUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AppleH16CamInUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>H1xANELoadBalancerDirectPathClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelContext2</string>
		<string>IOAccelDevice</string>
		<string>IOAccelDevice2</string>
		<string>IOAccelSharedUserClient</string>
		<string>IOAccelSharedUserClient2</string>
		<string>IOAccelSubmitter2</string>
		<string>IOSurfaceRootUserClient</string>
		<string>VADResourceArbiterUserClient</string>
		<string>AppleH16PhotonDetectorUserClient</string>
		<string>IOUserClient</string>
	</array>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.systemstatus.publisher.domains</key>
	<array>
		<string>media</string>
	</array>
</dict>
</plist>

```
### appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

 <dict>
 	<key>abs-client</key>
 	<string>143531244</string>
+	<key>adi-client</key>
+	<string>4127693656</string>
 	<key>application-identifier</key>
 	<string>com.apple.appleidsetupd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.AppSSO.service-xpc</key>
+	<true/>
 	<key>com.apple.CompanionLink</key>
 	<true/>
 	<key>com.apple.PairingManager.Read</key>

 	<true/>
 	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
 	<true/>
-	<key>com.apple.appletv.pbs.user-profile-application</key>
-	<true/>
-	<key>com.apple.appletv.pbs.user-profiles</key>
-	<true/>
-	<key>com.apple.appletv.pbs.user-profiles.account-notification</key>
-	<true/>
-	<key>com.apple.appletv.pbs.user-profiles.edit</key>
-	<true/>
-	<key>com.apple.appletv.pbs.user-profiles.group-recommendations-consent.edit</key>
-	<true/>
-	<key>com.apple.appletv.pbs.user-profiles.select</key>
-	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.owner</key>

 	<array>
 		<string>com.apple.appleidsetup.notifications</string>
 	</array>
+	<key>com.apple.private.userprofiles.assertion-domains</key>
+	<array>
+		<string>SuppressAccountChangeEventHandling</string>
+	</array>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>
 	<key>com.apple.private.userprofiles.read-write</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/</string>
+		<string>/Library/Preferences/com.apple.networkd.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.absinthed</string>

 	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/Library/Preferences/com.apple.networkd.plist</string>
+	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ak.anisette.xpc</string>
+	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
 	<key>com.apple.security.ts.identity-services-client</key>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	</dict>
 	<key>com.apple.aop.hid-driver.user-client</key>
 	<dict>
-		<key>gesture</key>
+		<key>cma</key>
 		<dict>
+			<key>historical-memory</key>
+			<dict/>
 			<key>send-command</key>
 			<dict/>
 		</dict>

 	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-privileged</key>
+	<true/>
 	<key>com.apple.hid.system.user-access-fast-path</key>
 	<true/>
 	<key>com.apple.iaptransportd.clientport</key>

 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceMicrophoneInjection</string>
 		<string>kTCCServiceMotion</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>

 		<string>com.apple.iconservices</string>
 		<string>com.apple.audio.AUHostingService.arm64e</string>
 		<string>com.apple.BluetoothCloudServices</string>
+		<string>com.apple.corespeech.assistant.activation.xpc</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.usbaudiod</string>
 		<string>com.apple.HearingModeService</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>

 		<string>com.apple.audio.earcplayer</string>
 		<string>com.apple.siri.CarBluetooth</string>
 		<string>com.apple.system.prefs</string>
+		<string>com.apple.assistant.domain.preferences</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### avconferenced

> `/usr/libexec/avconferenced`

```diff

 		<string>/private/var/tmp/com.apple.audiomxd/AudioCapture/</string>
 		<string>/private/var/tmp/vp/</string>
 		<string>/private/var/mobile/tmp/com.apple.audiomxd/AudioCapture/</string>
+		<string>/private/var/mobile/Library/Logs/CrashReporter/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<string>com.apple.backboardd</string>
 	<key>com.apple.diagnosticpipeline.request</key>
 	<true/>
+	<key>com.apple.driver.I2C.device.user-access</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
-		<string>kern.exclaves_status</string>
 		<string>kern.task_conclave</string>
-		<string>machdep.wake_abstime</string>
-		<string>machdep.wake_conttime</string>
-		<string>security.codesigning.security_boot_mode_complete</string>
 		<string>kern.bootargs</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.data-read-xpc</key>
 	<true/>
+	<key>com.apple.coreduetd.context</key>
+	<true/>
 	<key>com.apple.private.powersource-read</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.appleneuralengine.private</string>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.accountsd.accountmanager</string>

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.biomesyncd</string>
+	<key>com.apple.uservault</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>platform-application</key>

```
### biometrickitd

> `/usr/libexec/biometrickitd`

```diff

 	<true/>
 	<key>com.apple.private.applepearl.allow</key>
 	<true/>
+	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
+	<true/>
+	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Discoverability.Signals</string>

 	<true/>
 	<key>com.apple.private.mobilerepair.xpc</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceCamera</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.Preferences</string>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.avfoundation</string>
 		<string>com.apple.camera</string>
 		<string>com.apple.coreanimation</string>
 		<string>com.apple.coreimage</string>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<true/>
 	<key>com.apple.carousel.wakegesturemonitor</key>
 	<true/>
+	<key>com.apple.companionuiservice.client</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

 	<array>
 		<string>com.apple.CompanionNotifications</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Applications/</string>

 		<string>com.apple.carousel.wakegesturemonitor</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.CompanionLink</string>
+		<string>com.apple.CompanionUIService.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.homehubd.manage</string>

 		<string>com.apple.tvremotecore.xpc</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.userprofiles</string>
 		<string>com.apple.watchnotificationsui.alertservice</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.askpermissiond</string>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.coreduetd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>PeopleSuggesterContactPriors</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Contacts.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>PeopleSuggester.ContactPrior</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>photosAutonamingView</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
 		<string>com.apple.siri.uaf.service</string>

```

### 🆕 corercd

> `/usr/libexec/corercd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOCECUserClient</string>
		<string>IOHIDLibUserClient</string>
		<string>RootDomainUserClient</string>
	</array>
</dict>
</plist>

```
### corerepaird

> `/usr/libexec/corerepaird`

```diff

 	<true/>
 	<key>com.apple.private.vfs.snapshot</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ctkd.token-client</string>

```

### 🆕 devicesharingd

> `/usr/libexec/devicesharingd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.devicesharingd</string>
	<key>com.apple.PairingManager.Read</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-access-to-device-list</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.devicesharing.guest-user-mode-client</key>
	<true/>
	<key>com.apple.devicesharingd.client</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.managedassets.api.import</key>
	<true/>
	<key>com.apple.managedassets.api.serialize</key>
	<true/>
	<key>com.apple.managedassets.api.usermode</key>
	<true/>
	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
	<true/>
	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
	<true/>
	<key>com.apple.private.application-service-browse</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.networkextension.configuration</key>
	<string>super</string>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.sessionkit.custom-platter-target</key>
	<true/>
	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>
	<true/>
	<key>com.apple.private.sessionkit.sessionRequest</key>
	<true/>
	<key>com.apple.private.sharing.unlock-manager</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.guestData</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.devicesharingd.guestuserremoteunlockservice</string>
		<string>com.apple.devicesharing.guestusermodeservice</string>
		<string>com.apple.iconservices</string>
		<string>com.apple.managedassetsd</string>
		<string>com.apple.sessionservices</string>
		<string>com.apple.surfboard.authenticationservice</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.airplay</string>
		<string>com.apple.devicesharingd</string>
		<string>com.apple.RealityGuestSetup</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.devicesharingd</string>
	<key>com.apple.springboard.activateRemoteAlert</key>
	<true/>
	<key>com.apple.surfboard.authentication-client</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```diff

 <dict>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 	<array>
 		<string>com.apple.diagnosticspushd</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.TapToRadarKit.service</string>
+	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 </dict>

```

### 🆕 dietappleh16camerad

> `/usr/libexec/dietappleh16camerad`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.driver.VADResource.user-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.photondetector.iokit-user-access</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>AGXDeviceUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AppleH16CamInUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>H1xANELoadBalancerDirectPathClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelContext2</string>
		<string>IOAccelDevice</string>
		<string>IOAccelDevice2</string>
		<string>IOAccelSharedUserClient</string>
		<string>IOAccelSharedUserClient2</string>
		<string>IOAccelSubmitter2</string>
		<string>IOSurfaceRootUserClient</string>
		<string>VADResourceArbiterUserClient</string>
		<string>AppleH16PhotonDetectorUserClient</string>
		<string>IOUserClient</string>
	</array>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.systemstatus.publisher.domains</key>
	<array>
		<string>media</string>
	</array>
</dict>
</plist>

```
### eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceReminders</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.EventKitSyncServices.server</string>
+	</array>
 </dict>
 </plist>
 

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceBTDiscoveryXPCService.access</key>
 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceEraseXPCService.access</key>

 		<string>com.apple.security.octagon</string>
 		<string>com.apple.securityd.ckks</string>
 		<string>com.apple.icloud.searchpartyd.securelocations</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### fmfd

> `/usr/libexec/fmfd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
-	<key>com.apple.findmy.findmylocate.fenceservice</key>
-	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

```
### fmflocatord

> `/usr/libexec/fmflocatord`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
-	<key>com.apple.findmy.findmylocate.fenceservice</key>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.PowerManagement.control</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### gamed

> `/usr/libexec/gamed`

```diff

 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
-	<key>com.apple.private.ids.messaging</key>
-	<array>
-		<string>com.apple.private.alloy.gamecenter</string>
-	</array>
-	<key>com.apple.private.ids.messaging.high-priority</key>
-	<array>
-		<string>com.apple.private.alloy.gamecenter</string>
-	</array>
 	<key>com.apple.private.ids.registration</key>
 	<array>
 		<string>com.apple.private.alloy.arcade</string>

 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>
-	<key>com.apple.private.ids.session</key>
-	<array>
-		<string>com.apple.private.alloy.gamecenter</string>
-	</array>
-	<key>com.apple.private.ids.session-private</key>
-	<array>
-		<string>com.apple.private.alloy.gamecenter</string>
-	</array>
-	<key>com.apple.private.ids.urgent-priority</key>
-	<array>
-		<string>com.apple.private.alloy.gamecenter</string>
-	</array>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.GameOverlayUI</string>
+		<string>com.apple.GameOverlayUIInternal</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### installd

> `/usr/libexec/installd`

```diff

 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
+	<key>com.apple.usermanagerd.persona.setbundle</key>
+	<true/>
 	<key>fairplay-client</key>
 	<integer>2033844765</integer>
 	<key>keychain-cloud-circle</key>

```
### linkd

> `/usr/libexec/linkd`

```diff

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.remoteappintentsd.appevent</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>

 	<array>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.linkd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.siriknowledged.koa.donate</string>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.remoteappintentsd.appevent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.driver.AppleBasebandPCIControl.user-access</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.geoanalyticsd.telemetry</key>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>
+	<key>com.apple.private.launchservices.changedefaulthandlers</key>
+	<array>
+		<string>http</string>
+		<string>https</string>
+	</array>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/DeviceName</string>

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
### milod

> `/usr/libexec/milod`

```diff

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.spaceattributiond</string>
+		<string>com.apple.PowerManagement.control</string>
 	</array>
 	<key>com.apple.spaceattribution.private</key>
 	<true/>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	</array>
 	<key>com.apple.private.diskimages.kext.user-client-access</key>
 	<true/>
+	<key>com.apple.private.exclaves.conclave-host</key>
+	<true/>
 	<key>com.apple.private.image4.nonce.propose.mobile-asset</key>
 	<true/>
 	<key>com.apple.private.img4.nonce.cryptex1.asset</key>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.CodeLM</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>

```
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.avfoundation.multitasking-camera-access</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 	<true/>
 	<key>com.apple.private.accessories.showallconnections</key>
 	<true/>
+	<key>com.apple.private.avfoundation.capture.allow</key>
+	<true/>
+	<key>com.apple.private.avfoundation.capture.hidden-cameras.allow</key>
+	<true/>
+	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.corewifi.countrycode</key>

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceCamera</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceNearbyInteraction</string>

 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Caches/com.apple.nearbyd/</string>
 		<string>/Library/Caches/com.apple.CoreMotionAlgorithms/</string>
+		<string>Documents/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.privacyaccountingd</string>
 		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.audioanalyticsd</string>
+		<string>com.apple.coremedia.mediaplaybackd.player.xpc</string>
+		<string>com.apple.coremedia.mediaplaybackd.remaker.xpc</string>
+		<string>com.apple.coremedia.mediaplaybackd.sandboxserver.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### nehelper

> `/usr/libexec/nehelper`

```diff

 	<true/>
 	<key>com.apple.networkextension.keychain</key>
 	<true/>
+	<key>com.apple.networkrelay.identityProxy</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.network</string>

 	<array>
 		<string>/private/var/db/com.apple.networkextension.tracker-info.temp</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.terminusd</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

 		<string>com.apple.identities</string>
 		<string>com.apple.certificates</string>
 		<string>com.apple.managed.vpn.shared</string>
+		<string>com.apple.terminusd.local-identity</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.NeighborhoodActivityConduitService</key>
 	<true/>
-	<key>com.apple.PCAngel.HandoffUI</key>
-	<true/>
 	<key>com.apple.PairingManager.Read</key>
 	<true/>
+	<key>com.apple.ProximityControlUI.HandoffUI</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.SiriVOXService.client</key>

 	<true/>
 	<key>com.apple.announced.client</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>

 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
+	<key>com.apple.developer.shared-with-you</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.ProximityControl</string>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.mediaremote.device-info</key>
 	<true/>
 	<key>com.apple.mediaremote.group-sessions</key>

 	<true/>
 	<key>com.apple.private.allow-background-haptics</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.sociallayer.shareable-content</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.Home</string>
 		<string>com.apple.Home.HomeControlService</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.proximitycontrol</key>
 	<true/>
 	<key>com.apple.proximitycontrol.remoteActivity</key>

 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
+	<key>com.apple.runningboard.sharing.airdrop</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Bundle/Application/</string>

 		<string>/usr/libexec</string>
 		<string>/usr/local/lib/log</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Application Support/com.apple.Home</string>

 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.locationd.registration</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.mediaremoted.xpc</string>

 		<string>com.apple.nanoprefsync</string>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.NeighborhoodActivityConduitService</string>
-		<string>com.apple.PCAngel.xpc</string>
+		<string>com.apple.perceptiond.entitykit</string>
+		<string>com.apple.ProximityControlUI.xpc</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.PointerUI.pointeruid.service</string>
 		<string>com.apple.PowerManagement.control</string>

 		<string>com.apple.ProximityControl.server.launching</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.security.sfkeychainserver</string>
+		<string>com.apple.sharing.airdrop.service</string>
+		<string>com.apple.sharing.airdropui.services</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.SiriVOXService.client</string>
+		<string>com.apple.sociallayerd</string>
 		<string>com.apple.soundboardservices.server</string>
 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.springboard.services</string>

 		<string>com.apple.TextInput</string>
 		<string>com.apple.tvremotecore.xpc</string>
 		<string>com.apple.UIKit.KeyboardManagement.hosted</string>
+		<string>com.apple.usermanagerd.persona.fetch</string>
+		<string>com.apple.userprofiles</string>
 		<string>com.apple.usymptomsd</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>

 		<string>com.apple.ProximityControl</string>
 		<string>com.apple.ProximityControlPreferencesSync</string>
 		<string>com.apple.purplebuddy</string>
+		<string>com.apple.rapport</string>
 		<string>com.apple.Sharing</string>
 		<string>com.apple.springboard</string>
 		<string>com.apple.spotlightui</string>

 	<true/>
 	<key>com.apple.sharing.Services</key>
 	<true/>
+	<key>com.apple.sharing.airdrop.service</key>
+	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
+	<key>com.apple.frontboard.debugapplications</key>
+	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

```

### 🆕 remoteappintentsd

> `/usr/libexec/remoteappintentsd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.remoteappintentsd</string>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.usage_oracle</key>
	<true/>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.application-service-browse</key>
	<true/>
	<key>com.apple.private.linkd.observationStatusRegistry</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.mediator</string>
		<string>com.apple.linkd.observationStatusRegistry</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
	</array>
	<key>com.apple.security.exception.user-preference.read</key>
	<array>
		<string>com.apple.appintentssservices</string>
	</array>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.system-container</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.remoteappintentsd</string>
	<key>platform-application</key>
	<true/>
	<key>user-preference-read</key>
	<true/>
</dict>
</plist>

```
### routined

> `/usr/libexec/routined`

```diff

 	</array>
 	<key>com.apple.carousel.session.backgroundLaunch</key>
 	<true/>
+	<key>com.apple.chrono.descriptorEnablement</key>
+	<array>
+		<string>com.apple.SafetyMonitorApp.SuggestionWidget</string>
+	</array>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

```
### runningboardd

> `/usr/libexec/runningboardd`

```diff

 	<true/>
 	<key>com.apple.private.jetsam.modify-priority</key>
 	<integer>100</integer>
+	<key>com.apple.private.kernel.jetsam</key>
+	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.kernel.setpriority-darwin-role</key>

 	<true/>
 	<key>com.apple.private.vfs.allow-low-space-writes</key>
 	<true/>
+	<key>com.apple.private.write-kr-experiment-factors</key>
+	<true/>
 	<key>com.apple.private.xpc.allowed-launch-types</key>
 	<array>
 		<integer>3</integer>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 	<array>
 		<string>kTCCServiceWillow</string>
 	</array>
-	<key>com.apple.private.tcc.manager</key>
-	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
 	<key>com.apple.runningboard.private.se.credential</key>
 	<true/>
 	<key>com.apple.runningboard.process-state</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.soundboardservices.server</string>
 		<string>com.apple.springboard.blockableservices</string>
+		<string>com.apple.StatusKit.local</string>
 		<string>com.apple.sysdiagnose.service.xpc</string>
 		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.tailspind</string>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

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

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.CoreKnowledge</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Config</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>1630</string>
 		<string>1701</string>
 	</array>
+	<key>com.apple.uservault</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### soundanalysisd

> `/usr/libexec/soundanalysisd`

```diff

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.audio.adam.xpc</string>
+		<string>com.apple.shareddspd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### symptomsd-diag

> `/usr/libexec/symptomsd-diag`

```diff

 		<string>com.apple.cache_delete</string>
 		<string>com.apple.diagnosticpipeline.service</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
+		<string>com.apple.lsd.modifydb</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### terminusd

> `/usr/libexec/terminusd`

```diff

 		<string>lockdown-identities</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.srp-mdns-proxy</string>
+		<string>com.apple.terminusd.local-identity</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 		<string>SiriPassThrough</string>
 		<string>TVPairing</string>
 	</array>
-	<key>com.apple.mediaremote.external-artwork-validation</key>
-	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.can-import-browsing-data-to-Safari</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.SafariShared.History</key>

 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.security.octagon</string>
+		<string>com.apple.Safari.BrowsingDataImport</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>

```
### webpushd

> `/usr/libexec/webpushd`

```diff

 <dict>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.private.launchservices.allowopenwithanyhandler</key>
 	<true/>
 	<key>com.apple.private.launchservices.canspecifysourceapplication</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>com.apple.WebKit.webpushd</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.private.usernotifications.app-management-domain.proxy</key>
+	<string>com.apple.WebKit.PushBundles</string>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.uikitservices.app.value-access</key>
+	<true/>
+	<key>com.apple.usernotification.notificationschedulerproxy</key>
+	<true/>
 </dict>
 </plist>
 

```
### wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

 	<true/>
 	<key>com.apple.private.wifivelocity</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/log/com.apple.wifi.analytics/</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>IOUserUserClient</string>

```
