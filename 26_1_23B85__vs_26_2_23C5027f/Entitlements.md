## 🔑 Entitlements

### AirDropUI

> `/Applications/AirDropUI.app/AirDropUI`

```diff

 	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.sharingd</string>
+	</array>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.sharingd</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Audio/Tunings/Generic/Haptics/</string>

```

### 🆕 AppleCashStickerPackHost

> `/Applications/AppleCashStickerPackHost.app/AppleCashStickerPackHost`

- No entitlements *(yet)*

### 🆕 AppleCashStickerPackExtension

> `/Applications/AppleCashStickerPackHost.app/PlugIns/AppleCashStickerPackExtension.appex/AppleCashStickerPackExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.WalletMobileAssets</string>
	</array>
</dict>
</plist>

```
### AppleIDSetupUIService

> `/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.authkit.writer.internal</key>
+	<true/>
 	<key>com.apple.bluetooth.discovery</key>
 	<dict>
 		<key>AppleIDSignIn</key>

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>

 		<string>com.apple.absd</string>
 		<string>com.apple.absinthed</string>
 		<string>com.apple.ak.anisette.xpc</string>
+		<string>com.apple.corefollowup.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Diagnostic-8259

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8259.appex/Diagnostic-8259`

```diff

 <dict>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
+	<key>com.apple.security.network.client</key>
+	<true/>
 </dict>
 </plist>
 

```
### Diagnostic-8262

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262`

```diff

 	<array>
 		<string>com.apple.MobileAsset.RepairUpdate</string>
 	</array>
+	<key>com.apple.private.assets.change-daemon-config</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.img4.nonce.pdi</key>

```
### Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

 	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
+	<key>com.apple.private.corerepair.prebootremount</key>
+	<true/>
 	<key>com.apple.private.corerepair.xpc</key>
 	<true/>
 	<key>com.apple.private.gasgauge-update</key>

 	<true/>
 	<key>com.apple.private.security.AppleImage4.user-client</key>
 	<true/>
+	<key>com.apple.rootless.volume.iSCPreboot</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileSoftwareUpdate/Controller/RepairServices/</string>

```
### DockFolderViewService

> `/Applications/DockFolderViewService.app/DockFolderViewService`

```diff

 	<true/>
 	<key>com.apple.private.pluginkit.persona</key>
 	<string>system</string>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.trust-ubiquity-kvstore-identifier</key>

```
### Family

> `/Applications/Family.app/Family`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

 		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
 		<string>group.com.apple.people</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### FamilyOutOfProcessUIExtension

> `/Applications/FamilyExtensionHost.app/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.AppleMediaServices</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.familycircled</string>

```
### HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

 	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
+	<key>com.apple.private.homekit.diagnostics</key>
+	<true/>
 	<key>com.apple.private.homekit.person-manager</key>
 	<true/>
 	<key>com.apple.private.homekit.wallet-key</key>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.wallet.features.all-access</key>
 	<true/>
+	<key>fairplay-client</key>
+	<integer>87750944</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.PassbookUIService</string>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 		<string>com.apple.businessservicesd</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.private.corewifi.internal-xpc</string>
+		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### PosterBoard

> `/Applications/PosterBoard.app/PosterBoard`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.allowed</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>Library</string>
+		<string>Install</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.PosterPlatformSupportBundleService</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>

 	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.installcoordinationd</string>
+	</array>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
 	<key>com.apple.springboard.allowIconVisibilityChanges</key>
 	<true/>
+	<key>com.apple.springboard.application-removability.proxy</key>
+	<true/>
 	<key>com.apple.springboard.homeScreenLayout</key>
 	<true/>
 	<key>com.apple.springboard.homeScreenSilhouetteLayout</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	</array>
 	<key>com.apple.managedconfiguration.profiled.set</key>
 	<array>
+		<string>ClientRestrictions</string>
 		<string>Passcode</string>
 	</array>
 	<key>com.apple.managedconfiguration.teslad-access</key>

 	<true/>
 	<key>com.apple.mediastream.mstreamd-access</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.migrationd.client</key>
 	<true/>
 	<key>com.apple.mkb.usersession.delete</key>

 	</array>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.fetchNewestPolicies</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.internalState</key>
 	<true/>
 	<key>com.apple.private.eligibilityd.setInput</key>

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.tips</string>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 	</array>
 	<key>com.apple.private.security.storage-exempt.heritable</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.tipsd</string>
 		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
 		<string>com.apple.audio.AudioSession</string>
 		<string>com.apple.locationaccessstored.registration</string>

 	</array>
 	<key>com.apple.timed</key>
 	<true/>
+	<key>com.apple.tipsd.access</key>
+	<true/>
 	<key>com.apple.transparency.kt</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>
 	<true/>
+	<key>com.apple.developer.networking.slicing.appcategory</key>
+	<string>Browser-9003</string>
+	<key>com.apple.developer.networking.slicing.trafficcategory</key>
+	<string>video-2</string>
 	<key>com.apple.developer.web-browser</key>
 	<true/>
 	<key>com.apple.dmd.policy</key>
 	<true/>
+	<key>com.apple.familycircle.agent</key>
+	<true/>
 	<key>com.apple.features.all-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.WebClips.read-write</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appinstall.install-webkit-push-placeholder</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.parsec.default-client</key>
 	<string>com.apple.SafariViewService</string>
+	<key>com.apple.private.safari.automatic-strong-passwords.can-override-application-identifier</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.runningboard.trustedtarget</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.safari</string>
+		<string>group.com.apple.BrowserKit</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

 		<string>com.apple.email.maild</string>
 		<string>com.apple.webprivacyd</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.lsd.modifydb</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.security.kcsharing</string>
-		<string>com.apple.lsd.modifydb</string>
 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.UserNotifications.OneTimeCodeService</string>
 		<string>com.apple.lsd.xpc</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.AppStoreComponents</string>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
+		<string>com.apple.BrowserKit</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.tips</string>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 	</array>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.tipsd</string>
 		<string>com.apple.seserviced.sereservation.client</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.asd.scoring</string>

 	<true/>
 	<key>com.apple.timed</key>
 	<true/>
+	<key>com.apple.tipsd.access</key>
+	<true/>
 	<key>com.apple.tvhomesharingd.client</key>
 	<true/>
 	<key>com.apple.tzlink.allow</key>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.sharingd</string>
+	</array>
 	<key>com.apple.private.sharing.all-access</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

 	</array>
 	<key>com.apple.purplebuddy.budd.access</key>
 	<true/>
+	<key>com.apple.rapport.Client</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.runningboard.sharingviewservice</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.sharingd</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/preboot/</string>

 		<string>com.apple.purplebuddy.budd.migration.source.xpc</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.sharing.airdrop.service</string>
+		<string>com.apple.sharing.pinpairing</string>
 		<string>com.apple.sharingd.b332setup</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.sirittsd</string>

```
### SleepWidgetExtension

> `/Applications/SleepWidgetContainer.app/PlugIns/SleepWidgetExtension.appex/SleepWidgetExtension`

```diff

 	<array>
 		<string>com.apple.sleepd.sleepserver</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.health.shared</string>
+	</array>
 </dict>
 </plist>
 

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/mobile/Library/Trial/</string>
 		<string>/private/var/mobile/Library/Application Support/com.apple.VisualGeneration/</string>
 		<string>/private/var/mobile/Media/PhotoData/Caches/VisionService/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

```
### StickersUltraExtension

> `/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.private.BypassShelfAccess</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.uninstall</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.WalletMobileAssets</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Caches/PassKit/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Avatar/</string>

```
### StickersUltra

> `/Applications/StickersUltra.app/StickersUltra`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.private.BypassShelfAccess</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.uninstall</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.WalletMobileAssets</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Caches/PassKit/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Avatar/</string>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
-		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcutsProd</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.private.corespeech.audioinjection.xpc</key>
 	<true/>
-	<key>com.apple.private.familycircle</key>
-	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.siri.sirireaderd</string>
 		<string>com.apple.private.assistant.settings</string>
 		<string>com.apple.sirittsd</string>

```

### 🆕 AMSMediaServiceOwnerUIProvider

> `/System/Library/AppleMediaServices/AMSMediaServiceOwner/PlugIns/AMSMediaServiceOwnerUIProvider.bundle/AMSMediaServiceOwnerUIProvider`

- No entitlements *(yet)*
### AccessibilityControlsExtension

> `/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`

```diff

 	<true/>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 		<string>com.apple.AccessibilityUIServer</string>
 		<string>com.apple.UIKit.KeyboardManagement.hosted</string>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.server.bluetooth.general.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.backboard.watchdog</string>
 		<string>com.apple.accessibility.voices</string>
 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.pasteboard.pasted</string>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.mediaexperience.endpoint.xpc</key>
 	<true/>
+	<key>com.apple.mediaremote.send-commands</key>
+	<true/>
 	<key>com.apple.modelmanager.assertion</key>
 	<true/>
 	<key>com.apple.private.CarAssetUtils.variants</key>

```
### OTACrashCopier

> `/System/Library/CoreServices/OTACrashCopier`

```diff

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.osanalytics</string>
 </dict>
 </plist>
 

```
### SafariBookmarksSyncAgent

> `/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent`

```diff

 	<array>
 		<string>com.apple.mobilesafarishared</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.Safari.WBSDevice</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.BrowserKit</string>
 		<string>group.com.apple.weather</string>
 		<string>group.com.apple.stocks</string>
 		<string>com.apple.Home.group</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.BrowserKit</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.appstored</string>
 		<string>com.apple.itunesstored</string>

```
### osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

 	</array>
 	<key>com.apple.security.ts.read-any-bundle</key>
 	<true/>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.osanalytics</string>
 	<key>com.apple.softwareupdateservices.client.allowed</key>
 	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>

```
### ADAskForExceptionExtension

> `/System/Library/ExtensionKit/Extensions/ADAskForExceptionExtension.appex/ADAskForExceptionExtension`

```diff

 <dict>
 	<key>com.apple.app-distribution.private</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

```

### 🆕 ASDAgeAssuranceExtension

> `/System/Library/ExtensionKit/Extensions/ASDAgeAssuranceExtension.appex/ASDAgeAssuranceExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.asktod</string>
		<string>com.apple.managedappdistributiond.xpc</string>
		<string>com.apple.familycircle.agent</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```
### AskToViewExtension

> `/System/Library/ExtensionKit/Extensions/AskToViewExtension.appex/AskToViewExtension`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.askto.responseui.host</key>
+	<true/>
 	<key>com.apple.asktod</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<array>
 		<string>com.apple.AskToMessagesHost.AskToMessagesExtension</string>
 	</array>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### FamilyOutOfProcessUIExtension

> `/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.AppleMediaServices</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.familycircled</string>

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowmessagescontent</key>
+	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.usernotifications.settings</key>
+	<array>
+		<string>read</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Messages/Attachments/</string>
+		<string>/Library/SMS/Attachments/</string>
+		<string>/Library/Mail/AttachmentData/</string>
+		<string>/Library/UserNotifications/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.email.maild</string>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelmanager</string>
+		<string>com.apple.spotlight.IndexAgent</string>
+		<string>com.apple.spotlight.SearchAgent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.spotlight.IndexAgent</string>
+		<string>com.apple.spotlight.SearchAgent</string>
+	</array>
 </dict>
 </plist>
 

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>RegionalSafetyAnalysis.Eligibility</string>
 		<string>TrustKit.Decisioning.TKModelMessages</string>
 		<string>CommApps.CallIntelligence.HoldAssistFedStats</string>
+		<string>Device.Networking.TLS</string>
+		<string>App.EventEngagement</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides.coordinator</key>

```
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
-	<key>com.apple.private.security.enable-state-flags</key>
-	<array>
-		<string>BlockNetworkAccess</string>
-	</array>
-	<key>com.apple.private.security.mutable-state-flags</key>
-	<array>
-		<string>BlockNetworkAccess</string>
-	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 	<key>com.apple.symptom_analytics.configure</key>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.attributionkitd.impression-intake</key>
 	<true/>
+	<key>com.apple.attributionkitd.trusted-publisher-intake</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.AppStore.ProductPageExtension</string>
+	</dict>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.attributionkitd.xpc.trusted-publisher-intake</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.attributionkitd.xpc.impression-intake</string>
 		<string>com.apple.ap.promotedcontent.pcinterface</string>
 		<string>com.apple.ap.promotedcontent.mescalinterface</string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>AD_PLATFORMS_SEARCH_RESULTS_PAGE</string>
+		<string>AD_PLATFORMS_APPSTORE_ALL_PLACEMENTS</string>
 		<string>511</string>
 		<string>512</string>
 	</array>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.attributionkitd.impression-intake</key>
 	<true/>
+	<key>com.apple.attributionkitd.trusted-publisher-intake</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.AppStore.SubscribePageExtension</string>
+	</dict>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.attributionkitd.xpc.trusted-publisher-intake</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.attributionkitd.xpc.impression-intake</string>
 		<string>com.apple.ap.promotedcontent.pcinterface</string>
 		<string>com.apple.ap.promotedcontent.mescalinterface</string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>AD_PLATFORMS_SEARCH_RESULTS_PAGE</string>
+		<string>AD_PLATFORMS_APPSTORE_ALL_PLACEMENTS</string>
 		<string>511</string>
 		<string>512</string>
 	</array>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```

### 🆕 com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/ExtensionKit/Extensions/WebContentEnhancedSecurityExtension.appex/com.apple.WebKit.WebContent.EnhancedSecurity`

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
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.restrict.notifyd</key>
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
	<key>com.apple.private.webinspector.allow-remote-inspection</key>
	<true/>
	<key>com.apple.private.webinspector.proxy-application</key>
	<true/>
	<key>com.apple.private.webkit.enhanced-security</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.fatal-exceptions</key>
	<array>
		<string>jit</string>
	</array>
	<key>com.apple.security.hardened-process.containment.ipc</key>
	<true/>
	<key>com.apple.sqlite.defensive</key>
	<integer>1</integer>
</dict>
</plist>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### BrowserEngineKit.Intermediary

> `/System/Library/Frameworks/BrowserEngineKit.framework/XPCServices/BrowserEngineKit.Intermediary.xpc/BrowserEngineKit.Intermediary`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.WebContentRestrictions</string>
+	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
+	<key>com.apple.private.ciphermld.allow</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.DocumentManagerCore.Downloads</string>
+		<string>com.apple.ciphermld</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### CoreSpotlightTestImporter

> `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTestImporter.appex/CoreSpotlightTestImporter`

```diff

 	<string>com.apple.CoreSpotlight.TestImporter</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
-	<key>com.apple.security.files.user-selected.read-only</key>
-	<true/>
 </dict>
 </plist>
 

```
### CoreSpotlightTextImporter

> `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTextImporter.appex/CoreSpotlightTextImporter`

```diff

 	<string>com.apple.CoreSpotlight.TextImporter</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
-	<key>com.apple.security.files.user-selected.read-only</key>
-	<true/>
 </dict>
 </plist>
 

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.securemessagingagent.delivery</key>
+	<array>
+		<string>encryptedRCS</string>
+	</array>
+	<key>com.apple.securemessagingagent.registration</key>
+	<array>
+		<string>encryptedRCS</string>
+	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.tipsnext</string>

```
### LocalStorageFileProvider

> `/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>
 	<true/>
 	<key>com.apple.private.vfs.authorized-access</key>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DocumentRevisions</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
 	<key>com.apple.private.security.storage.iCloudDrive</key>

```

### 🆕 ServicesAccountLinkingService

> `/System/Library/Frameworks/ServicesAccountLinking.framework/XPCServices/ServicesAccountLinkingService.xpc/ServicesAccountLinkingService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.authkit.client.internal</key>
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
	<key>com.apple.private.fairplay.FPDI</key>
	<dict>
		<key>capabilities</key>
		<array>
			<integer>4014732562</integer>
		</array>
		<key>client-identifier</key>
		<string>ServicesAccountLinkingService</string>
	</dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.read-any-bundle</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

 	<true/>
 	<key>com.apple.appstored.octane</key>
 	<true/>
+	<key>com.apple.attributionkitd.postback-proxy</key>
+	<true/>
 	<key>com.apple.attributionkitd.token-handoff</key>
 	<true/>
 	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>

 		<string>com.apple.misagent</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.watchnotificationsui.alertservice</string>
+		<string>com.apple.attributionkitd.xpc.postback-proxy</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### adattributiond

> `/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond`

```diff

 <dict>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>com.apple.WebKit.adattributiond</string>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```

### 🆕 AccessorySetupDeveloperSettings

> `/System/Library/PreferenceBundles/AccessorySetupDeveloperSettings.bundle/AccessorySetupDeveloperSettings`

- No entitlements *(yet)*
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
-		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcutsProd</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>

```
### AMDEngagementExtension

> `/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/PlugIns/AMDEngagementExtension.appex/AMDEngagementExtension`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>App.LanguageConsumption</string>
+		<string>App.EventEngagement</string>
 	</array>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.AppleMediaServices</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.pisco.suinfo/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>fairplay-client</key>

```
### askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.askpermissiond</string>
 	<key>com.apple.askto.responseui.host</key>

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>Library</string>
+		<string>Install</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>AskToBuy</string>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ScreenTimeAgent.exception</string>
 		<string>com.apple.asktod</string>
+		<string>com.apple.appstored.xpc.request</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.lsd.open</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 </dict>

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

### 🆕 GestureDiagnostic

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/GestureDiagnostic.appex/GestureDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Logs/CrashReporter/com.apple.locationd/</string>
		<string>/Library/Logs/locationd/MslLogger/Gesture/</string>
	</array>
</dict>
</plist>

```

### 🆕 MediaSuggesterDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/MediaSuggesterDiagnosticExtension.appex/MediaSuggesterDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>App.Intent</string>
		<string>App.Intents.Transcript</string>
		<string>Media.NowPlaying</string>
		<string>MediaSuggester.SuggestionFeedback</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support</string>
	</array>
</dict>
</plist>

```
### com.apple.DocumentManagerCore.Downloads

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Downloads.xpc/com.apple.DocumentManagerCore.Downloads`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>
 	<true/>
 	<key>com.apple.private.trust-ubiquity-kvstore-identifier</key>

```
### com.apple.DocumentManagerCore.Rename

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>
 	<true/>
 	<key>com.apple.private.trust-ubiquity-kvstore-identifier</key>

```
### RecentsAvocado

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado`

```diff

 	<true/>
 	<key>com.apple.private.pluginkit.persona</key>
 	<string>system</string>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.trust-ubiquity-kvstore-identifier</key>
 	<true/>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>

 		<string>com.apple.UIKit</string>
 		<string>com.apple.desktopservices</string>
 	</array>
+	<key>com.apple.springboard.app-drag</key>
+	<true/>
 	<key>com.apple.springboard.homeScreenIconStyle</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### SaveToFiles

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles`

```diff

 	<true/>
 	<key>com.apple.private.metadata.exattrs</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceFaceID</string>

```
### com.apple.DocumentManager.Service

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service`

```diff

 	<true/>
 	<key>com.apple.private.pluginkit.persona</key>
 	<string>system</string>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<true/>
 	<key>com.apple.private.screentime-setup</key>
 	<true/>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.familycircled</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/preferences/com.apple.networkd.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.familycircled.settings</string>
 		<string>com.apple.familycircled.sharing</string>
+		<string>com.apple.familycircled.testing</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.AppleMediaServices</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.appleaccount</string>

 	<true/>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
+	<key>com.apple.security.ts.daemon-container</key>
+	<true/>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### FitnessIntelligenceSnapshotService

> `/System/Library/PrivateFrameworks/FitnessIntelligenceDaemonCore.framework/XPCServices/FitnessIntelligenceSnapshotService.xpc/FitnessIntelligenceSnapshotService`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.source_override</key>
 	<string>com.apple.private.health.localdevice</string>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/var/mobile/tmp</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.FitnessIntelligenceSnapshotService</string>
 		<string>com.apple.seymour</string>
 		<string>com.apple.healthd.server</string>
 	</array>
+	<key>com.apple.security.temporary-exception.sbpl</key>
+	<array>
+		<string>(allow syscall-unix
+            (syscall-number SYS_open_dprotected_np
+            SYS_rmdir
+            SYS_getattrlistbulk
+            SYS_listxattr
+            ))
+        </string>
+	</array>
 </dict>
 </plist>
 

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.cloudtelemetry</key>
+	<true/>
 	<key>com.apple.private.controlcenter.service.moduleidentifiers</key>
 	<array>
 		<string>com.apple.Home.ControlCenter</string>

```
### jetpackassetd

> `/System/Library/PrivateFrameworks/JetCore.framework/Support/jetpackassetd`

```diff

 	<array>
 		<string>/Library/Application Support/CrashReporter/DiagnosticMessagesHistory.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/tmp/com.apple.jetpackassetd/overrides/</string>
+		<string>/private/var/tmp/com.apple.CoreDevice/jetpack-cli/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```

### 🆕 SearchPersonalization

> `/System/Library/PrivateFrameworks/MapsIntelligence.framework/IntelligenceBundles/SearchPersonalization.bundle/SearchPersonalization`

- No entitlements *(yet)*
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<array>
 		<string>NULL/DeviceName</string>
 	</array>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.musicd.client</key>
 	<true/>
 	<key>com.apple.private.octagon</key>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 	</dict>
 	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### replicatord

> `/System/Library/PrivateFrameworks/ReplicatorCore.framework/Support/replicatord`

```diff

 	</array>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
 	<true/>
 	<key>com.apple.authkit.client</key>

 	<string>IOHIDLibUserClient</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.backboard.display.services</string>
 		<string>com.apple.duetactivityscheduler</string>

```
### com.apple.Safari.SearchHelper

> `/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>SafariSearchHelper</string>
 	<key>com.apple.private.security.daemon-container</key>

```

### 🆕 genSafetyAlertsUI

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/PlugIns/genSafetyAlertsUI.appex/genSafetyAlertsUI`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.safetyalerts.spi</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.safetyalerts</string>
	</array>
</dict>
</plist>

```
### AirDrop

> `/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDrop.appex/AirDrop`

```diff

 	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.sharingd</string>
+	</array>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.rapport.nearfield</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.sharingd</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Applications/</string>

```
### StatusKitAgent

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.SystemConfiguration.SCPreferences-read-access</key>
+	<array>
+		<string>com.apple.radios.plist</string>
+	</array>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.statuskit</string>
+	<key>com.apple.wifi.manager-access</key>
+	<true/>
 </dict>
 </plist>
 

```
### StocksKitService

> `/System/Library/PrivateFrameworks/StocksKit.framework/XPCServices/StocksKitService.xpc/StocksKitService`

```diff

 	<array>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.adid</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### com.apple.StreamingUnzipService.privileged

> `/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.privileged.xpc/com.apple.StreamingUnzipService.privileged`

```diff

 <dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>StreamingUnzipService</string>
+	<key>com.apple.private.vfs.entitled-reserve-access</key>
+	<true/>
 	<key>com.apple.rootless.storage.MobileAssetDownload</key>
 	<true/>
 	<key>com.apple.rootless.volume.Update</key>

```
### com.apple.StreamingUnzipService

> `/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService`

```diff

 <dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>StreamingUnzipService</string>
+	<key>com.apple.private.vfs.entitled-reserve-access</key>
+	<true/>
 </dict>
 </plist>
 

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>re6Zb+zwFKJNlkQTUeT+/w</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
-	<key>com.apple.developer.icloud-container-identifiers</key>
-	<array>
-		<string>com.apple.facetime</string>
-	</array>
-	<key>com.apple.developer.icloud-services</key>
-	<array>
-		<string>CloudDocuments</string>
-	</array>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<string>com.apple.facetime</string>
 		<string>com.apple.Photos</string>
 	</array>
-	<key>com.apple.developer.ubiquity-container-identifiers</key>
-	<array>
-		<string>com.apple.facetime</string>
-	</array>
 	<key>com.apple.duet.expertcenter.consumer</key>
 	<true/>
 	<key>com.apple.facetimemessagestored.service</key>

 	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
-	<key>com.apple.private.clouddocs.auto-accept-share</key>
-	<true/>
-	<key>com.apple.private.clouddocs.sharing.private-interface</key>
-	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

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

 	<array>
 		<string>com.apple.default-app.phone</string>
 	</array>
-	<key>com.apple.private.librarian.container-proxy</key>
-	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/ActivationState</string>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
-	<key>com.apple.private.security.storage.MobileDocuments</key>
-	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

```
### TrialArchivingService

> `/System/Library/PrivateFrameworks/TrialServer.framework/XPCServices/TrialArchivingService.xpc/TrialArchivingService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.trial.TrialArchivingService</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.geoservices.experiments.bucket-id.read</key>
 	<true/>
 	<key>com.apple.private.modelPurgeInAllPartitions.allow</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.ap.promotedcontent.trialbucketid</string>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.geod</string>
 		<string>com.apple.appleneuralengine.private</string>

```
### UserNotificationsThumbnailProvider

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/PlugIns/UserNotificationsThumbnailProvider.appex/UserNotificationsThumbnailProvider`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+</dict>
+</plist>
 

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
-		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcutsProd</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.appleaccount</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.mediaaccessibility</string>
 		<string>kCFPreferencesAnyApplication</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
-		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcutsProd</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
-		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcutsProd</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>

```
### SystemActionConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.shortcuts</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.siri.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>V568VXD5P8.is.workflow.my.app</string>
+		<string>com.apple.openai</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### WidgetConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.shortcuts</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.siri.shortcuts</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>V568VXD5P8.is.workflow.my.app</string>
+		<string>com.apple.openai</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### kbd

> `/System/Library/TextInput/kbd`

```diff

 		<string>/private/var/mobile/Library/Preferences/com.apple.WebUI.plist</string>
 		<string>/private/var/.DocumentRevisions-V100/PerUID</string>
 		<string>/private/var/mobile/Library/Safari/AutoFillQuirks.plist</string>
+		<string>/private/var/mobile/Library/Trial/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```

### 🆕 com.apple.safetyalerts.gen

> `/System/Library/UserNotifications/Bundles/com.apple.safetyalerts.gen.bundle/com.apple.safetyalerts.gen`

- No entitlements *(yet)*
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.attributionkitd.impression-intake</key>
 	<true/>
+	<key>com.apple.attributionkitd.trusted-publisher-intake</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.AppStore</string>
+	</dict>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.attributionkitd.xpc.trusted-publisher-intake</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.attributionkitd.xpc.impression-intake</string>
 		<string>com.apple.ap.promotedcontent.pcinterface</string>
 		<string>com.apple.ap.promotedcontent.mescalinterface</string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>AD_PLATFORMS_SEARCH_RESULTS_PAGE</string>
+		<string>AD_PLATFORMS_APPSTORE_ALL_PLACEMENTS</string>
 		<string>511</string>
 		<string>512</string>
 	</array>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 		<string>com.apple.nanobackup</string>
 		<string>com.apple.nanotimekit.facesnapshotserver</string>
 		<string>com.apple.nanotimekit.facesupportserver</string>
+		<string>com.apple.nanofacegallery.allassertions.server</string>
+		<string>com.apple.nanofacegallery.librarybroker.server</string>
+		<string>com.apple.nanofacegallery.gallerybroker.server</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.atc.xpc.sessions</string>
 		<string>com.apple.iBooks.BookDataStoreService</string>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.rapport.Client</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.safetycheckd</string>
 		<string>com.apple.contacts.poster.api</string>
+		<string>com.apple.sharingd.pairedcontactmanager</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<true/>
 	<key>com.apple.media.ringtones.read-only</key>
 	<true/>
+	<key>com.apple.mediaanalysisd.client</key>
+	<true/>
 	<key>com.apple.mobilemail.mailservices</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.safetycheckd</string>
+		<string>com.apple.mediaanalysisd.analysis</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<key>com.apple.usersafety.service</key>
 	<array>
 		<string>contacts</string>
+		<string>videoVoiceMail</string>
 	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<true/>
 	<key>com.apple.private.personas.propagate</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.shortcuts.IntentsAvailableDuringBuddy</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	<true/>
 	<key>com.apple.dropin</key>
 	<true/>
+	<key>com.apple.dropin.audiomanagement</key>
+	<true/>
 	<key>com.apple.energykit.client</key>
 	<true/>
 	<key>com.apple.energykit.spi</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.home.home-extension</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceWillow</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceEnergyKitGuidance</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceWillow</string>
+	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.tipsd</string>

 		<string>/private/var/preferences/SystemConfiguration/</string>
 		<string>/private/var/tmp/siriBC</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Containers/Data/Application/</string>
+		<string>/private/var/mobile/Library/Caches/</string>
+		<string>/private/var/mobile/home_ecosystems_liveon/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Containers/Shared/AppGroup/</string>

 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.apsd</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.cdp.daemon</string>

 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.apsd</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.cdp.daemon</string>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<true/>
+	<string>/Library/Logs/AppAnalytics/</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobileassetd.v2</string>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
-	<true/>
+	<string>/Library/Logs/AppAnalytics/</string>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.modelcatalog.catalog</string>

```
### JournalShareExtension

> `/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.auto-elect-plugin</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.Journal</string>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>
 	<true/>
+	<key>com.apple.developer.networking.slicing.appcategory</key>
+	<string>Browser-9003</string>
+	<key>com.apple.developer.networking.slicing.trafficcategory</key>
+	<string>video-2</string>
 	<key>com.apple.developer.web-browser</key>
 	<true/>
 	<key>com.apple.diagnosticpipeline.request</key>

 	<true/>
 	<key>com.apple.private.parsec.default-client</key>
 	<string>com.apple.mobilesafari</string>
+	<key>com.apple.private.rating-rank-eligibility-domain</key>
+	<integer>8</integer>
 	<key>com.apple.private.rsr-cryptex-access</key>
 	<true/>
 	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/Applications/</string>
-		<string>/private/var/MobileDevice/ProvisioningProfiles/</string>
 		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/MobileDevice/ProvisioningProfiles/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_SafariBrowsingAssistant/purpose_auto/</string>

 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.BrowserEngineKit.Intermediary</string>
 		<string>com.apple.timed.xpc</string>
+		<string>com.apple.securityd.xpc</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

 	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>

 		<string>com.apple.webkit.webauthn</string>
 		<string>apple</string>
 		<string>lockdown-identities</string>
+		<string>com.apple.Safari.WBSDevice</string>
 		<string>com.apple.password-manager</string>
 		<string>com.apple.password-manager.personal</string>
 		<string>com.apple.cfnetwork-recently-deleted</string>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.springboard.activateassistant</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.launchapplications</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.ak.privateemail.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.password-manager.personal-recently-deleted.testing</string>
 		<string>com.apple.password-manager.generated-passwords</string>
 		<string>com.apple.password-manager.generated-passwords.testing</string>
+		<string>com.apple.password-manager.password-evaluations</string>
+		<string>com.apple.password-manager.password-evaluations.testing</string>
 	</array>
 </dict>
 </plist>

```
### RemindersWidgetExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.sessionkit.listener</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### Reminders

> `/private/var/staged_system_apps/Reminders.app/Reminders`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.activitykit.bypassAuthorizationUI</key>
+	<true/>
+	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
+	<true/>
+	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/RemindersAppIntents.framework</string>

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.sessionkit.custom-platter-target</key>
+	<true/>
+	<key>com.apple.private.sessionkit.listener</key>
+	<true/>
+	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.suggestions.reminders</key>

 		<string>com.apple.tipsd</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.alarmkitservices</string>
+		<string>com.apple.sessionservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Weather

> `/private/var/staged_system_apps/Weather.app/Weather`

```diff

 		<string>com.apple.news.public.demo2</string>
 		<string>com.apple.news.private.demo2</string>
 		<string>com.apple.news.private.secure.demo2</string>
+		<string>com.apple.weather.fallback</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>

```
### ProxiedCrashCopier

> `/usr/libexec/ProxiedCrashCopier`

```diff

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.osanalytics</string>
 </dict>
 </plist>
 

```
### aonsensed

> `/usr/libexec/aonsensed`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/Library/Managed Preferences/mobile/com.apple.bluetooth.plist</string>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 	</array>

```
### asktod

> `/usr/libexec/asktod`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
+	<key>com.apple.family.ageRange</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.imagent</key>

 	<true/>
 	<key>com.apple.private.screentime-ask</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 	</array>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.asktod/</string>

 		<string>com.apple.messages.nicknames</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.AppSupport</string>
+		<string>com.apple.AppleMediaServices</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.SoundProfileAsset</key>
 	<true/>
-	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
-	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>

 		<string>/usr/libexec</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.mediaremote.plist</string>
 		<string>/private/var/db/com.apple.countryd/</string>
-		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

 <dict>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
+	<key>com.apple.carkit.app.service</key>
+	<true/>
 	<key>com.apple.developer.carp</key>
 	<true/>
 	<key>com.apple.private.CarPlayUIServices.cluster-theme</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.carkit.app.service</string>
 		<string>com.apple.CarPlayApp.cluster-theme-service</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
 	</array>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.deviceaccessd</string>
+	<key>com.apple.DeviceAccess.private</key>
+	<true/>
 	<key>com.apple.bluetooth.custom.properties.writable</key>
 	<true/>
+	<key>com.apple.bluetooth.pairedInfoSecurity</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>systemgroup.com.apple.accessorysetupkit</string>

 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.wifip2pd</string>
+		<string>com.apple.AccessorySetupUI</string>
+		<string>com.apple.AccessorySetupUI.services.presenter</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.GameController</string>
+		<string>com.apple.SpatialAccessorySettings</string>
 		<string>com.apple.GameController.gamecontrollerd</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```
### locationd

> `/usr/libexec/locationd`

```diff

 			<key>read</key>
 			<dict/>
 		</dict>
+		<key>DmQuaternionFp</key>
+		<dict>
+			<key>read</key>
+			<dict/>
+		</dict>
 	</dict>
 	<key>com.apple.aop.hid-device.user-client</key>
 	<dict>

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_AONSenseConfiguration/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel_Overrides/purpose_auto/</string>
+		<string>/private/var/db/eligibilityd/eligibility_allowlists.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

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
### mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

 	</array>
 	<key>com.apple.timed</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>MOBILE_ACTIVATION_CARRY</string>
+	</array>
 	<key>fairplay-client</key>
 	<integer>1209439590</integer>
 	<key>keychain-access-groups</key>

```
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>com.apple.locationd.inertialodometry</key>
 	<true/>
+	<key>com.apple.locationd.slv_configurer</key>
+	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

```
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 	<array>
 		<string>kTCCServiceUserTracking</string>
 	</array>
+	<key>com.apple.private.vfs.entitled-reserve-access</key>
+	<true/>
 	<key>com.apple.rootless.storage.MobileAssetDownload</key>
 	<true/>
 	<key>com.apple.rootless.storage.com.apple.MobileAsset.DuetExpertCenterAsset</key>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<array>
 		<string>/usr/libexec</string>
 		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Library/Trial/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	<array>
 		<string>513</string>
 		<string>514</string>
+		<string>AD_PLATFORMS_TODAY_TAB</string>
+		<string>AD_PLATFORMS_SEARCH_RESULTS_PAGE</string>
+		<string>AD_PLATFORMS_SEARCH_LANDING_PAGE</string>
+		<string>AD_PLATFORMS_PRODUCT_PAGE</string>
+		<string>AD_PLATFORMS_APPSTORE_ALL_PLACEMENTS</string>
 	</array>
 	<key>fairplay-client</key>
 	<string>700802717</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 		<string>com.apple.cloudd</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.rapport.RPPairing</string>
+		<string>com.apple.sharingd.pairedcontactmanager</string>
+		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.sharing.Session</key>
 	<true/>
+	<key>com.apple.sharing.airdrop.service</key>
+	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### remindd

> `/usr/libexec/remindd`

```diff

 	<array>
 		<string>framework-reminders-grocerylist</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

```
### restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleTCONControlUserClient</string>
 		<string>AppleBasebandPCIUserClient</string>
 		<string>AppleBasebandUserClient</string>
 		<string>AppleGasGaugeUpdateUserClient</string>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 	<array>
 		<string>com.apple.safetyalerts</string>
 		<string>com.apple.safetyalerts.aw</string>
+		<string>com.apple.safetyalerts.gen</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 		<string>com.apple.containermanagerd</string>
 		<string>com.apple.DDUI.UserAcceptService</string>
 		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.sharing.pinpairing</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### visionhwserverd

> `/usr/libexec/visionhwserverd`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>
+		<string>AppleCameraUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appleh13camerad</string>
 		<string>com.apple.appleh16camerad</string>
+		<string>com.apple.cameraispd</string>
 		<string>com.apple.iohideventsystem</string>
 		<string>com.apple.locationd.synchronous</string>
 	</array>

```
### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 	<true/>
 	<key>com.apple.private.can-import-browsing-data-to-Safari</key>
 	<true/>
+	<key>com.apple.private.can-load-any-content-blocker</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.SafariShared.History</key>

 	<array>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.SafariBookmarksSyncAgent</string>
+		<string>com.apple.Safari.BrowsingDataImport</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.security.octagon</string>
-		<string>com.apple.Safari.BrowsingDataImport</string>
 		<string>com.apple.lsd.xpc</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>

 	<key>com.apple.springboard.opensensitiveurl</key>
 	<array>
 		<string>settings-navigation://com.apple.Settings.Apps/com.apple.mobilesafari?action=showExportSheet</string>
+		<string>settings-navigation://com.apple.Settings.Apps/com.apple.mobilesafari/WEB_EXTENSIONS</string>
 	</array>
 	<key>com.apple.springboard.shortcutitems.fullaccess</key>
 	<true/>

 		<string>com.apple.webkit.webauthn-recently-deleted</string>
 		<string>com.apple.password-manager.personal</string>
 		<string>com.apple.password-manager.personal-recently-deleted</string>
+		<string>com.apple.Safari.WBSDevice</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### webpushd

> `/usr/libexec/webpushd`

```diff

 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.sqlite.defensive</key>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.mediaremote.critical-section-monitor</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.pairunpairobliterate</key>
 	<true/>
 	<key>com.apple.networkd_privileged</key>

```
