## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.appstoreagent.xpc</string>
-		<string>com.apple.appstorecomponentsd.xpc</string>
-		<string>com.apple.passd.payment</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
+		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.askpermissiond</string>
 		<string>com.apple.coreidvd.docUpload.xpc</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.mobileactivationd</string>
-		<string>com.apple.xpc.amsaccountsd</string>
-		<string>com.apple.xpc.amsengagementd</string>
+		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.passd.account</string>
 		<string>com.apple.passd.in-app-payment</string>
-		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.passd.library</string>
-		<string>com.apple.askpermissiond</string>
-		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.passd.payment</string>
+		<string>com.apple.surfboard.scenesessionservice</string>
+		<string>com.apple.xpc.amsengagementd</string>
+		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.surfboard.disable-realitychrome</key>
 	<true/>
+	<key>com.apple.surfboard.scene-state-assertion</key>
+	<true/>
 	<key>com.apple.surfboard.scenesession-updates</key>
 	<true/>
 	<key>com.apple.surfboard.sharing-mode-launch-allowed</key>

```
### AppProtectionUIHost

> `/Applications/AppProtectionUIHost.app/AppProtectionUIHost`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.write.access</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.usernotifications.settings</key>
+	<array>
+		<string>read</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.write</string>
 		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 Diagnostic-6007

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6007.appex/Diagnostic-6007`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.HearingModeService</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.HearingModeService</string>
	</array>
</dict>
</plist>

```

### 🆕 Diagnostic-6008

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6008.appex/Diagnostic-6008`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.HearingModeService</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.HearingModeService</string>
	</array>
</dict>
</plist>

```
### Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileSoftwareUpdate/Controller/RepairServices/</string>
+		<string>/private/preboot/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

 	<array>
 		<string>/private/var/MobileSoftwareUpdate/</string>
 		<string>/private/var/hardware/FactoryData/</string>
-		<string>/private/preboot/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>
 		<string>/usr/local/share/firmware/</string>
-		<string>/usr/standalone/firmware/Savage/</string>
+		<string>/private/preboot/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

```diff

 	<true/>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
+	<key>com.apple.DiagnosticsSupport.HardwareButtonAccess</key>
+	<true/>
 	<key>com.apple.private.corerepair.attestation</key>
 	<true/>
 	<key>com.apple.private.corerepair.xpc</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-filter</key>
+	<true/>
+	<key>com.apple.private.hid.client.event-monitor</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>

```
### Diagnostic-9008

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008`

```diff

 	<true/>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
+	<key>com.apple.DiagnosticsSupport.HardwareButtonAccess</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.corerepair.xpc</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-filter</key>
+	<true/>
+	<key>com.apple.private.hid.client.event-monitor</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>

```
### Diagnostic-9010

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010`

```diff

 	<true/>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
+	<key>com.apple.DiagnosticsSupport.HardwareButtonAccess</key>
+	<true/>
 	<key>com.apple.private.corerepair.xpc</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-filter</key>
+	<true/>
+	<key>com.apple.private.hid.client.event-monitor</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.reboot</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### SystemReport-AirPods

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppleDeviceQueryService</string>
 		<string>com.apple.HearingModeService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppleDeviceQueryService</string>
 		<string>com.apple.HearingModeService</string>
 		<string>com.apple.private.corewifi.mobilewifi-xpc</string>
 		<string>com.apple.wifi.manager</string>

```
### Family

> `/Applications/Family.app/Family`

```diff

 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.contactsd.persistence</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.FamilyCircle</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.DeviceActivity</string>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
 	<true/>
+	<key>com.apple.private.allow-ldm-exempt-webview</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

```
### LimitedAccessPromptView

> `/Applications/LimitedAccessPromptView.app/LimitedAccessPromptView`

```diff

 <dict>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/Applications/LimitedAccessPromptView.app/LimitedAccessPromptView</string>
+	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>
 	<true/>
+	<key>com.apple.coreaudio.allow-apac-codec</key>
+	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 		<string>com.apple.MobileAsset.MediaSupport</string>
 		<string>com.apple.MobileAsset.PhotosCuratedMusicLibraryAsset</string>
 		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 		<string>/Media/PhotoData/</string>
 		<string>/Library/LiveFiles/</string>
 		<string>/Library/Logs/MediaServices/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.posterboardui.services</string>
 		<string>com.apple.itunescloudd.tcchelper</string>
 		<string>com.apple.modelmanager</string>
-		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.assistant.cdm</string>

 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
-		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.siri.uaf.service</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.mediaanalysisd.embeddingstore</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.gms.availability</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.photoanalysisd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.server</key>
 	<true/>
-	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/UnifiedAssetFramework/</string>
-	</array>
-	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.siri.uaf.service</string>
-		<string>com.apple.modelcatalog.catalog</string>
-	</array>
 	<key>com.apple.sharesheet.allow-custom-view</key>
 	<true/>
 	<key>com.apple.siri.synapse</key>

```
### PhotosDestructiveChangeConfirmation

> `/Applications/MobileSlideShow.app/PlugIns/PhotosDestructiveChangeConfirmation.appex/PhotosDestructiveChangeConfirmation`

```diff

 <dict>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.PhotosLibraries</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>

```
### PhotosPicker

> `/Applications/MobileSlideShow.app/PlugIns/PhotosPicker.appex/PhotosPicker`

```diff

 	<array>
 		<string>analysis</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>

 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.duetactivityscheduler</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### com.apple.social.StreamShareService

> `/Applications/MobileSlideShow.app/PlugIns/com.apple.social.StreamShareService.appex/com.apple.social.StreamShareService`

```diff

 	<array>
 		<string>com.apple.suggestd.contacts</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 </dict>

```
### PassbookSecureUIService

> `/Applications/PassbookSecureUIService.app/PassbookSecureUIService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>

 	<array>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.apple-pay-trust.all-access</key>
 	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>

 		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### PeerPaymentMessagesExtension

> `/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.presets</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.SensorKit.effective-bundle</key>
 	<true/>
 	<key>com.apple.SensorKitAppHelper.allow</key>

 	<true/>
 	<key>com.apple.accessibility.AccessibilityPersonalVoiceUsageOverride</key>
 	<true/>
+	<key>com.apple.accessibility.physicalinteraction.client</key>
+	<true/>
 	<key>com.apple.accessoryupdater.launchauhelper.entitled</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

 	<true/>
 	<key>com.apple.springboard.application-removability.proxy</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
 	<key>com.apple.springboard.externaldisplay.displayArrangements</key>
 	<true/>
 	<key>com.apple.springboard.focus-modes-home-screen-settings</key>

 	<true/>
 	<key>com.apple.springboard.private.EA0E3FBF-D56E-4897-B807-A3CA8090EE38</key>
 	<true/>
+	<key>com.apple.springboard.private.capture-button-events</key>
+	<true/>
+	<key>com.apple.springboard.private.capture-button-full-fidelity-events</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.springboard.resetHomeScreenLayout</key>

 		<string>appleaccount</string>
 		<string>com.apple.mobilemail.smime</string>
 		<string>com.apple.preferences</string>
-		<string>com.apple.cfnetwork</string>
 		<string>com.apple.safari.credit-cards</string>
 		<string>com.apple.PassbookUIService</string>
 		<string>com.apple.ProtectedCloudStorage</string>

 		<string>com.apple.passd</string>
 		<string>com.apple.managed.vpn.shared</string>
 		<string>com.apple.mail.identities</string>
-		<string>com.apple.cfnetwork-recently-deleted</string>
 		<string>com.apple.AppleCareSupport-Preferences</string>
+		<string>com.apple.cfnetwork</string>
+		<string>com.apple.password-manager</string>
+		<string>com.apple.webkit.webauthn</string>
+		<string>com.apple.cfnetwork-recently-deleted</string>
+		<string>com.apple.password-manager-recently-deleted</string>
+		<string>com.apple.webkit.webauthn-recently-deleted</string>
+		<string>com.apple.password-manager.personal</string>
+		<string>com.apple.password-manager.personal-recently-deleted</string>
+		<string>com.apple.password-manager.generated-passwords</string>
 	</array>
 	<key>keychain-cloud-circle</key>
 	<true/>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>
 	<true/>
 	<key>com.apple.RemoteDisplay</key>

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
+	<key>com.apple.private.ids.phone-number-authentication</key>
+	<true/>
 	<key>com.apple.private.ids.registration</key>
 	<true/>
 	<key>com.apple.private.ids.registration-control</key>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
-	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
-	<key>com.apple.private.corespotlight.search.internal</key>
-	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.photos.service.multilibrary</key>
 	<true/>
-	<key>com.apple.private.security.storage.Spotlight</key>
-	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>/Library/Spotlight/CoreSpotlight/Priority/index.spotlightV2/Cache/</string>
 		<string>/Library/UserConfigurationProfiles/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CarPlayApp.non-launching-service</string>
 		<string>com.apple.Photos.MultiLibrary</string>
+		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
+		<string>com.apple.backlightd</string>
 		<string>com.apple.bird.token</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
-	<key>com.apple.spotlight.entitledattributes</key>
-	<true/>
 	<key>com.apple.springboard.systemaperture</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 	<array>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.Photos.MultiLibrary</string>
+		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
+		<string>com.apple.backlightd</string>
 		<string>com.apple.bird.token</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
+	<key>com.apple.private.parsec.default-client</key>
+	<string>com.apple.siri</string>
 	<key>com.apple.private.remindd</key>
 	<dict>
 		<key>userInteractive</key>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
-		<string>com.apple.MobileAsset.UAF.FM.com.apple.security.temporaryGenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>

 	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
+	<key>com.apple.private.avfoundation.background-camera-access</key>
+	<true/>
+	<key>com.apple.private.avfoundation.capture.allow</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.device.camera</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Application Support/com.apple.VisualGeneration/</string>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	</array>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<array>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
+		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
 		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.announced.server</string>
+		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>

```
### VideoSubscriberAccountViewService

> `/Applications/VideoSubscriberAccountViewService.app/VideoSubscriberAccountViewService`

```diff

 	<true/>
 	<key>com.apple.private.subscriptionservice.internal</key>
 	<true/>
-	<key>com.apple.private.tcc.manager</key>
-	<true/>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceMSO</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
 	<key>com.apple.private.webinspector.allow-remote-inspection</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 		<string>kTCCServiceListenEvent</string>
 		<string>kTCCServiceMotion</string>
 		<string>kTCCServiceVoiceBanking</string>
+		<string>kTCCServiceMicrophoneInjection</string>
 	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.systemstatus</string>
 		<string>com.apple.voicebanking.services</string>
 		<string>com.apple.voicebanking.store</string>
 		<string>com.apple.shazamd</string>

 	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
+	<key>com.apple.systemstatus.domains</key>
+	<array>
+		<string>media</string>
+	</array>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```
### AccessibilityControlsExtension

> `/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`

```diff

 	<string>com.apple.AccessibilityUIServer.AccessibilityControlsExtension</string>
 	<key>com.apple.AccessibilityControlsExtension</key>
 	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+		<string>carrier-settings</string>
+	</array>
 	<key>com.apple.accessibility.AccessibilityUIServer</key>
 	<true/>
 	<key>com.apple.accessibility.AppIntentExtension</key>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.CarPlayApp.service</string>
+		<string>com.apple.audio.SystemSoundServer-iOS</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
+	<key>com.apple.avfoundation.allows-access-to-device-list</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.camera.iokit-user-access</key>
+	<true/>
 	<key>com.apple.carousel.backlightaccess</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-opus-codec</key>

 		<string>com.apple.MobileAsset.CharacterVoices</string>
 		<string>com.apple.MobileAsset.AXIconVision</string>
 		<string>com.apple.MobileAsset.AXElementVision</string>
+		<string>com.apple.MobileAsset.ImageCaptionModel</string>
 	</array>
+	<key>com.apple.private.avfoundation.background-camera-access</key>
+	<true/>
+	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
+	<true/>
+	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>
+	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
 	<true/>
 	<key>com.apple.private.coreaudio.rpbserver</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceCamera</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceVoiceBanking</string>
 	</array>

```
### powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.PerfPowerTelemetry.data-donation</key>
 	<true/>
 	<key>com.apple.backlight.backlightaccess</key>

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>ContextSync.LOI</string>
-		<string>SemanticLocation</string>
+		<string>Location.Semantic</string>
 		<string>Alarm</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>

```
### AccessibilityControlsExtension

> `/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`

```diff

 	<string>com.apple.AccessibilityUIServer.AccessibilityControlsExtension</string>
 	<key>com.apple.AccessibilityControlsExtension</key>
 	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+		<string>carrier-settings</string>
+	</array>
 	<key>com.apple.accessibility.AccessibilityUIServer</key>
 	<true/>
 	<key>com.apple.accessibility.AppIntentExtension</key>

```
### AudiovisualThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/AudiovisualThumbnailExtension.appex/AudiovisualThumbnailExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
+</dict>
+</plist>
 

```
### CalendarThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/CalendarThumbnailExtension.appex/CalendarThumbnailExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
+</dict>
+</plist>
 

```
### ContactThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ContactThumbnailExtension.appex/ContactThumbnailExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
+</dict>
+</plist>
 

```
### FontThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/FontThumbnailExtension.appex/FontThumbnailExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
+</dict>
+</plist>
 

```
### ImageThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ImageThumbnailExtension.appex/ImageThumbnailExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
+</dict>
+</plist>
 

```
### MKRemoteUI

> `/System/Library/ExtensionKit/Extensions/MKRemoteUI.appex/MKRemoteUI`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.suggestions.contacts</key>
+	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
-	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceAddressBook</string>
-		<string>kTCCServiceCalendar</string>
-		<string>kTCCServiceMediaLibrary</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### MercuryPosterExtension

> `/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>PRWantsLocation</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
+	<key>com.apple.locationd.prompt_behavior</key>
+	<true/>
+	<key>com.apple.locationd.prompt_from_background</key>
+	<true/>
+	<key>com.apple.locationd.usage_oracle</key>
+	<true/>
 	<key>com.apple.posterkit.enhanced-memory-limits</key>
 	<true/>
 	<key>com.apple.posterkit.provider</key>

 	<array>
 		<string>/Library/Wallpaper/Mercury/</string>
 	</array>
+	<key>com.apple.security.personal-information.location</key>
+	<true/>
 </dict>
 </plist>
 

```
### OfficeThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/OfficeThumbnailExtension.appex/OfficeThumbnailExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
+</dict>
+</plist>
 

```

### 🆕 PasscodeSettingsExtension

> `/System/Library/ExtensionKit/Extensions/PasscodeSettingsExtension.appex/PasscodeSettingsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
</dict>
</plist>

```
### QuickLookUIExtension

> `/System/Library/ExtensionKit/Extensions/QuickLookUIExtension.appex/QuickLookUIExtension`

```diff

 	<array>
 		<string>/private/var/mobile/Library/Caches/GeoServices/</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.GEO.plist</string>
+		<string>/private/var/mobile/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.desktopservices.ArchiveService</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 SafetyCheckAppIntents

> `/System/Library/ExtensionKit/Extensions/SafetyCheckAppIntents.appex/SafetyCheckAppIntents`

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
### SearchAnalyticsWorker

> `/System/Library/ExtensionKit/Extensions/SearchAnalyticsWorker.appex/SearchAnalyticsWorker`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.parsecd</string>
 	</array>
 	<key>user-preference-read</key>
 	<true/>

```

### 🆕 SiriTurnRestatementExtension

> `/System/Library/ExtensionKit/Extensions/SiriTurnRestatementExtension.appex/SiriTurnRestatementExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Lighthouse.DeepThought.SiriTurnRestatementExtension</string>
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
			<string>Lighthouse.Ledger.TaskCustomEvent</string>
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
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Lighthouse.DeepThought.SiriTurnRestatementExtension</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Lighthouse.DeepThought.SiriTurnRestatementExtension</string>
	</array>
</dict>
</plist>

```
### SoftwareUpdateSettingsIntents

> `/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsIntents.appex/SoftwareUpdateSettingsIntents`

```diff

 	<string>com.apple.Preferences</string>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.seeding.client</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_SoftwareUpdateDocumentation/</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.seeding.client</string>
 		<string>com.apple.softwareupdateservicesd</string>
 		<string>CAREServer</string>
 	</array>

```

### 🆕 SpotlightSettingsIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SpotlightSettingsIntentsExtension.appex/SpotlightSettingsIntentsExtension`

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

### 🆕 TextInputAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/TextInputAppIntentsExtension.appex/TextInputAppIntentsExtension`

- No entitlements *(yet)*
### TextThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/TextThumbnailExtension.appex/TextThumbnailExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
+</dict>
+</plist>
 

```

### 🆕 TranslateCacheDeleteExtension

> `/System/Library/ExtensionKit/Extensions/TranslateCacheDeleteExtension.appex/TranslateCacheDeleteExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Translate.CacheDeleteExtension</string>
	<key>com.apple.private.translation</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.translationd</string>
	</array>
</dict>
</plist>

```
### VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
-	<key>com.apple.private.tcc.manager</key>
-	<true/>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceMSO</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Bundle/Application/</string>

```
### WebThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/WebThumbnailExtension`

```diff

 <dict>
 	<key>com.apple.private.quicklook-thumbnail.webkit</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.webkit</key>
+	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### iWorkThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/iWorkThumbnailExtension.appex/iWorkThumbnailExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
+</dict>
+</plist>
 

```
### apfs_userfs.util

> `/System/Library/Filesystems/apfs_userfs.fs/apfs_userfs.util`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.security.disk-device-access</key>
+	<true/>
+</dict>
+</plist>
 

```
### ContactsButtonXPCService

> `/System/Library/Frameworks/ContactsUI.framework/XPCServices/ContactsButtonXPCService.xpc/ContactsButtonXPCService`

```diff

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
+	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.iconservices.store</string>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<key>com.apple.private.ids.registration</key>
 	<array>
 		<string>com.apple.madrid</string>
-		<string>com.apple.private.alloy.multiplex1</string>
 	</array>
 	<key>com.apple.private.ids.server.messaging</key>
 	<array>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.depth.divingd</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

```
### coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>
+		<string>UniqueChipID</string>
 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>

 	</array>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/hardware/FactoryData/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.coreauthd</string>
+		<string>com.apple.purplebuddy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 IOHIDSensorPowerLoggingFilter

> `/System/Library/HIDPlugins/ServiceFilters/IOHIDSensorPowerLoggingFilter.plugin/IOHIDSensorPowerLoggingFilter`

- No entitlements *(yet)*
### AXMediaUtilitiesService

> `/System/Library/PrivateFrameworks/AXMediaUtilities.framework/XPCServices/AXMediaUtilitiesService.xpc/AXMediaUtilitiesService`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mediaanalysisd</string>
+		<string>com.apple.Accessibility.Assets</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 		<string>/Library/AppleMediaServices/</string>
 		<string>/Library/Caches/com.apple.amsaccountsd/</string>
 		<string>/Library/HTTPStorages/com.apple.amsaccountsd/</string>
-		<string>/Library/com.apple.AppleMediaServices/PersistedBags/</string>
+		<string>/Library/com.apple.AppleMediaServices/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 		<string>Motion.Activity</string>
 		<string>Location.HashedCoordinates</string>
 		<string>Notification</string>
+		<string>Notification.Usage</string>
 		<string>AppLaunch</string>
+		<string>App.InFocus</string>
 		<string>AppIntent</string>
 		<string>NowPlaying</string>
+		<string>Media.NowPlaying</string>
 		<string>SiriUI</string>
 		<string>SiriExecution</string>
 		<string>Alarm</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>App.Intent</string>
 		<string>CarPlay</string>
 		<string>Clock.Alarm</string>
+		<string>Device.Wireless.Bluetooth</string>
 		<string>HomeKit.Client.AccessoryControl</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification</string>
+		<string>Notification.Usage</string>
 		<string>Sage.Transcript</string>
 		<string>Siri.Metrics.OnDeviceDigestExperimentMetrics</string>
 		<string>Siri.Metrics.OnDeviceDigestSegmentsCohorts</string>

 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.purplebuddy</string>
+		<string>com.apple.SiriCarouselAlert</string>
 		<string>com.apple.SiriViewService</string>
 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.ToneLibrary</string>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.remoteActivityAccessor</key>
 	<true/>
+	<key>com.apple.private.activitykit.unthrottledAPIRequester</key>
+	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
 	<key>com.apple.private.biome.read-only</key>

 		<string>com.apple.apsd</string>
 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### CloudTelemetryService

> `/System/Library/PrivateFrameworks/CloudTelemetry.framework/XPCServices/CloudTelemetryService.xpc/CloudTelemetryService`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudtelemetrylocalbackend</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```
### cdpd

> `/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd`

```diff

 	<true/>
 	<key>com.apple.securebackupd.access</key>
 	<true/>
+	<key>com.apple.security.ts.ipc-posix-sem</key>
+	<string>purplebuddy.sentinel</string>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### parsec-fbf

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf`

```diff

 	<true/>
 	<key>com.apple.mlruntime.host.ondemand</key>
 	<true/>
-	<key>com.apple.mlruntime.host.ondemandplugin</key>
-	<array>
-		<string>com.apple.siri.parsec.CoreParsec.SearchPoirotExtension</string>
-	</array>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.extensionkitservice</string>
-		<string>com.apple.siri.parsec.CoreParsec.SearchPoirotExtension</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 	</array>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>RootDomainUserClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.xpc.amsengagementd</string>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 		<string>com.apple.MobileAsset.VoiceTriggerAssetsMac</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsASMac</string>
 		<string>com.apple.MobileAsset.SpeakerRecognitionAssets</string>
+		<string>com.apple.MobileAsset.SpeakerRecognitionASMacAssets</string>
 		<string>com.apple.MobileAsset.EmbeddedSpeech</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssetsIPad</string>

```
### LeakAgent

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
+	<true/>
 	<key>com.apple.private.iosurfaceinfo</key>
 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

```
### AirPlayDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.avfoundation.allow-system-wide-context</key>
+	<true/>
+	<key>com.apple.avfoundation.allows-set-output-device</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.coremedia.endpoint.xpc</string>

```
### LocationDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LocationDiagnosticExtension.appex/LocationDiagnosticExtension`

```diff

 		<string>/Library/Logs/CrashReporter/raven/</string>
 		<string>/Library/Logs/CrashReporter/pipelined/</string>
 		<string>/Library/Logs/CrashReporter/vision/</string>
-		<string>/Library/Logs/CrashReporter/locationd/</string>
+		<string>/Library/Logs/CrashReporter/com.apple.locationd/</string>
 		<string>/Library/Logs/gpsd/</string>
 		<string>/Library/Logs/locationd/</string>
 		<string>/Library/Logs/raven/</string>

```
### SaveToFiles

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.developer.auto-elect-plugin</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.bluetooth.xpc</string>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 	<true/>
 	<key>com.apple.audio.adam.xpc</key>
 	<true/>
+	<key>com.apple.avfoundation.allow-system-wide-context</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.bluetooth.xpc</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<string>WILLOWSYNC.com.apple.willowd</string>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
 	<key>com.apple.assistant.security</key>

```
### installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

 	<true/>
 	<key>com.apple.appconduitd.device-connection.connect.allow</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 	<string>AppleKeyStoreUserClient</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.mobile.installd</string>
 		<string>com.apple.lsd.installation</string>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	<string>com.apple.intelligenceflow.intelligencecontextd</string>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.Knosis</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 	<true/>
 	<key>com.apple.private.contextkit.request-external-content</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>ContextRetrieval</key>

 	<string>com.apple.intelligenceflow.intelligencecontextd</string>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.siri.inference.EntityMatcher.useSensitiveLogging</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>755</string>

```
### IntelligenceFlowDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics`

```diff

 	<string>com.apple.intelligenceflow.IntelligenceFlowRuntime.IntelligenceFlowDiagnostics</string>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.intelligenceflow.context</key>
+	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Sage.Transcript</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.intelligenceflow.context</string>
 	</array>
 </dict>
 </plist>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	</dict>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 	</array>
 	<key>com.apple.private.ciphermld.allow</key>

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.library</key>
+	<true/>
 	<key>com.apple.private.psid.allow</key>
 	<true/>
 	<key>com.apple.private.security.storage.HomeAI</key>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	</dict>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 	</array>
 	<key>com.apple.private.ciphermld.allow</key>

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.library</key>
+	<true/>
 	<key>com.apple.private.psid.allow</key>
 	<true/>
 	<key>com.apple.private.security.storage.HomeAI</key>

```
### nanosystemsettingsd

> `/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd`

```diff

 		<string>com.apple.animoji</string>
 		<string>com.apple.AvatarUI.Staryu</string>
 		<string>com.apple.Bridge</string>
+		<string>com.apple.nanosystemsettings</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

```
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 	<string>com.apple.newsd</string>
 	<key>aps-environment</key>
 	<string>production</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	<array>
 		<string>com.apple.newscore2</string>
 	</array>
+	<key>com.apple.security.ts.power-assertions</key>
+	<true/>
 	<key>com.apple.sessionkit.broadcastPush</key>
 	<true/>
 	<key>fairplay-client</key>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.coreidvd.identity-proofing</key>
+	<true/>
 	<key>com.apple.coreidvd.identity-provisioning</key>
 	<true/>
 	<key>com.apple.coreidvd.spi</key>

 	<true/>
 	<key>com.apple.private.activitykit.activityAuthorizer</key>
 	<true/>
+	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.applesse.allow</key>

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
+	<key>com.apple.private.seserviced.passd.private.jpki</key>
+	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>
 	<true/>
 	<key>com.apple.private.seserviced.sesprivacykey</key>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 		<string>Photos.MemoryCreation</string>
 		<string>Photos.Curation</string>
 		<string>Photos.Delete</string>
+		<string>Photos.Search</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 		<string>Photos.MemoryCreation</string>
 		<string>Photos.Curation</string>
 		<string>Photos.Delete</string>
+		<string>Photos.Search</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 		<string>Photos.MemoryCreation</string>
 		<string>Photos.Curation</string>
 		<string>Photos.Delete</string>
+		<string>Photos.Search</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```

### 🆕 MathSettingsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/MathSettingsSubscriber.xpc/MathSettingsSubscriber`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.remotemanagement.MathSettingsSubscriber</string>
	<key>com.apple.managedconfiguration.profiled.set</key>
	<array>
		<string>ClientRestrictions</string>
	</array>
	<key>com.apple.private.remotemanagement.subscriber</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/UserConfigurationProfiles/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.remotemanagementd.store</string>
		<string>com.apple.RemoteManagementAgent.store</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.remotemanagement.MathSettingsSubscriber</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.configurationprofiles</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<array>
		<string>com.apple.remotemanagement.MathSettingsSubscriber</string>
	</array>
</dict>
</plist>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 		<string>com.apple.siri.homeAutomation</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.siri.inference.SiriSignals</string>
+		<string>com.apple.voicetrigger</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SiriSuggestionsInternalXPCServices

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsInternalXPCServices.xpc/SiriSuggestionsInternalXPCServices`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.MobileAsset.SoftwareUpdate</key>
+	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
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
 	<key>com.apple.linkd.registry</key>
 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>

 		<string>AppIntent</string>
 		<string>siriRemembers</string>
 		<string>App.InFocus</string>
+		<string>UserFocus.ComputedMode</string>
+		<string>Media.NowPlaying</string>
+		<string>Motion.Activity</string>
+		<string>CarPlay.Connected</string>
+		<string>Location.Semantic</string>
+		<string>Device.ScreenLocked</string>
+	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Siri.Remembers.MessageHistory</string>
+		<string>Siri.Remembers.CallHistory</string>
+		<string>Siri.Remembers.InteractionHistory</string>
+		<string>Siri.Remembers.AudioHistory</string>
+		<string>Siri.Remembers.AssistantSuggestions</string>
+		<string>Siri.PostSiriEngagement</string>
+		<string>Siri.Audio.CompanionContext</string>
 	</array>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>siriRemembers</string>
+	</array>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.siri.userfeedbacklearning</string>
+	</array>
 	<key>com.apple.private.security.storage.SiriInference</key>
 	<true/>
+	<key>com.apple.private.sqlite.sqlite-encryption</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Caches/com.apple.HomeKit/com.apple.siriinferenced/</string>
+		<string>/Library/Caches/com.apple.siriinferenced/</string>
 		<string>/Library/com.apple.siri.inference/</string>
+		<string>/Library/srtest/</string>
+		<string>/Library/AddressBook/</string>
+		<string>/Library/Preferences/com.apple.suggestions.plist</string>
+		<string>/Library/IntelligencePlatform/</string>
 		<string>/Library/Shortcuts/ToolKit/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.settings</string>
+		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.siriinferenced</string>
+		<string>com.apple.siri.PostSiriEngagement</string>
+		<string>com.apple.siriinference-dodml-plugin</string>
+		<string>com.apple.siri.DialogEngine</string>
+		<string>com.apple.assistant</string>
 		<string>com.apple.siri.sirisuggestions</string>
+		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
+		<string>com.apple.siriinferenced.AppOrdering</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>

 	<array>
 		<string>1343</string>
 	</array>
+	<key>seatbelt-profiles</key>
+	<array>
+		<string>temporary-sandbox</string>
+	</array>
 </dict>
 </plist>
 

```
### sleepd

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>
 	<true/>
-	<key>com.apple.private.healthkit.feature-availability.read</key>
-	<array>
-		<string>SleepCoaching</string>
-		<string>SleepTracking</string>
-	</array>
+	<key>com.apple.private.healthkit.feature-availability.read-any</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.private.health.localdevice</string>

```
### StocksKitService

> `/System/Library/PrivateFrameworks/StocksKit.framework/XPCServices/StocksKitService.xpc/StocksKitService`

```diff

 	<string>ZL6BUSYGB3.com.apple.StocksKitService</string>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### systemstatusd

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd`

```diff

 	<true/>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.systemstatus</string>
+	</array>
 	<key>com.apple.security.ts.read-any-bundle</key>
 	<true/>
 	<key>platform-application</key>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>development</string>
+	<key>com.apple.AudioAccessoryServices</key>
+	<true/>
 	<key>com.apple.CallHistory.sync.allow</key>
 	<true/>
 	<key>com.apple.CallKit.call-directory</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceWillow</string>
+		<string>kTCCServiceMicrophoneInjection</string>
 	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.facetimemessagestored.service</string>
 		<string>com.apple.carkit.service</string>
+		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>

```
### MauiAUSP

> `/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/PlugIns/MauiAUSP.appex/MauiAUSP`

```diff

 <dict>
 	<key>com.apple.accessibility.systemvoiceprovider</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.TTSAXResourceModelAssets</string>
+	</array>
 	<key>com.apple.private.sirittsservice.modify-proxy-assets</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.audio.AudioConverterService</string>
 		<string>com.apple.logd</string>
 		<string>com.apple.system.notification_center</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.audio.AudioConverterService</string>
 		<string>com.apple.logd</string>
 		<string>com.apple.system.notification_center</string>

```
### VideoSubscriberAccountAuthenticationExtension

> `/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/PlugIns/VideoSubscriberAccountAuthenticationExtension.appex/VideoSubscriberAccountAuthenticationExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
-	<key>com.apple.private.tcc.manager</key>
-	<true/>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceMSO</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
 	<key>com.apple.private.webinspector.allow-remote-inspection</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
-	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
-	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

 		<string>Device.Wireless.Bluetooth</string>
 		<string>Device.Wireless.NFCTag</string>
 		<string>Device.Wireless.WiFi</string>
-		<string>Sleep.ScheduleState</string>
 		<string>SleepMode</string>
 		<string>SoundDetection</string>
 		<string>SpringBoard.ExternalDisplay.DisplayConnected</string>
 		<string>SpringBoard.WindowManagement.StageManagerMode</string>
-		<string>UserFocus.SleepMode</string>
 		<string>UserFocusComputedMode</string>
 		<string>Wallet.Transaction</string>
 	</array>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 		<string>com.apple.CarPlayApp.service</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.Photos.MultiLibrary</string>
+		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
 		<string>com.apple.WebBookmarks.webbookmarksd</string>
 		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.accountsd.accountmanager</string>

 		<string>com.apple.audio.AudioQueueServer</string>
 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.backlightd</string>
+		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
-	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
-	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MapKit.SnapshotService</string>
+		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
 		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.announced.server</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.write</string>
+		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 	<array>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
+		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
+		<string>com.apple.backlightd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>

```
### kbd

> `/System/Library/TextInput/kbd`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-container-identifiers</key>
 	<array>
-		<string>com.apple.TextInput</string>
+		<string>$(TeamIdentifierPrefix)com.apple.TextInput</string>
 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.TextInput</string>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
 	<key>com.apple.private.security.storage.kbd</key>

 	<array>
 		<string>com.apple.keyboard.TypoTracker</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.private.xpc.domain-extension</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Connections</key>

 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.email.maild</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>170</string>
 	</array>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.TextInput</string>

```
### Books

> `/private/var/staged_system_apps/Books.app/Books`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.iBooks</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### BooksThumbnail

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksThumbnail.appex/BooksThumbnail`

```diff

 	<string>com.apple.iBooks.BooksThumbnail</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.iBooks.BooksThumbnail</string>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array>
+		<string>iCloud.com.apple.iBooks</string>
+		<string>iCloud.com.apple.iBooks.iTunesU</string>
+	</array>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudDocuments</string>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.iBooks</string>

```
### Calculator

> `/private/var/staged_system_apps/Calculator.app/Calculator`

```diff

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### HealthBalanceWidgetExtension

> `/private/var/staged_system_apps/Health.app/PlugIns/HealthBalanceWidgetExtension.appex/HealthBalanceWidgetExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.companionappd.connect.allow</key>
+	<true/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionComplete</string>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>VasUgeSzVyHdB27g2XpN0g</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.appconduitd.device-connection</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.health.shared</string>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 		<string>/private/var/mobile/Library/Caches/com.apple.navd/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.Maps/ARTraces/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.Maps/</string>
+		<string>/private/var/mobile/Library/Caches/com.apple.maps/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.Maps/DiagnosticLogs/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.navd/NavTraces/</string>
 		<string>/private/var/mobile/Library/Weather/</string>

```
### CalendarIntentsExtension

> `/private/var/staged_system_apps/MobileCal.app/Extensions/CalendarIntentsExtension.appex/CalendarIntentsExtension`

```diff

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCalendar</string>
+		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceReminders</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.surfboard.scenesessionservice</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
+		<string>com.apple.backlightd</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.apple-pay-trust.all-access</key>
 	<true/>
 	<key>com.apple.asd.allow</key>

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.private.corewifi.internal-xpc</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-only</key>
 	<string>com.apple.stockholm</string>

 	<true/>
 	<key>com.apple.sharing.Client</key>
 	<true/>
-	<key>com.apple.softposreaderd</key>
-	<true/>
 	<key>com.apple.softposreaderd.provision</key>
 	<true/>
 	<key>com.apple.springboard.allowIconVisibilityChanges</key>

```
### PassbookLockedWidgetsExtension

> `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
-	<key>com.apple.private.appintents-bundle-absolute-paths</key>
-	<array>
-		<string>/System/Library/Frameworks/FinanceKitUI.framework</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/PassKit/</string>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
+	<key>com.apple.private.appstorecomponents.media-client-id</key>
+	<string>com.apple.Passwords</string>
+	<key>com.apple.private.appstorecomponents.media-client-version</key>
+	<string>1</string>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 		<string>com.apple.private.email</string>
 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.cdp.daemon</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.AppStoreComponents</string>
+	</array>
 	<key>com.apple.security.files.user-selected.read-write</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

 	</array>
 	<key>com.apple.sharing.Services</key>
 	<true/>
-	<key>com.apple.springboard.appbackgroundstyle</key>
-	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
-	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
-	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
-	<key>com.apple.private.security.storage.Spotlight</key>
-	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 		<string>/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice</string>
 		<string>/Library/DuetExpertCenter/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
-		<string>/Library/Spotlight/CoreSpotlight/Priority/index.spotlightV2/Cache/</string>
 		<string>/Library/UserConfigurationProfiles/</string>
 		<string>/Library/VoiceServices/Assets</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>

 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MobileTimer.alarmserver</string>
+		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.amsaccountsd.multiuser</string>

 		<string>com.apple.audio.AudioComponentPrefs</string>
 		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.audio.AudioQueueServer</string>
+		<string>com.apple.backlightd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.coreduetd.knowledge</string>

 	<true/>
 	<key>com.apple.soundscapes.picker</key>
 	<true/>
-	<key>com.apple.spotlight.entitledattributes</key>
-	<true/>
 	<key>com.apple.springboard.addWebClipToHomeScreen</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### Stocks

> `/private/var/staged_system_apps/Stocks.app/Stocks`

```diff

 		<string>/System/Library/PrivateFrameworks/StocksUI.framework</string>
 		<string>/System/Library/PrivateFrameworks/StocksCore.framework</string>
 	</array>
-	<key>com.apple.private.appintents-bundle-relative-paths</key>
-	<array>
-		<string>/PlugIns/StocksWidget.appex</string>
-	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### mount

> `/sbin/mount`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.fskit.mount</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.fskit.mount</string>
 	<key>com.apple.private.LiveFS.connection</key>
 	<true/>
 	<key>com.apple.private.bindfs-allow</key>

```
### ReportMemoryException

> `/usr/libexec/ReportMemoryException`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
+	<true/>
 	<key>com.apple.diagnosticpipeline.request</key>
 	<true/>
 	<key>com.apple.private.get-system-corpse</key>

```
### amfid

> `/usr/libexec/amfid`

```diff

 	</array>
 	<key>com.apple.private.amfi.developer-mode-control</key>
 	<true/>
+	<key>com.apple.private.amfi.set-demo</key>
+	<true/>
 	<key>com.apple.private.iokit.nvram-read-access</key>
 	<true/>
 	<key>com.apple.private.iokit.nvram-write-access</key>

```
### aned

> `/usr/libexec/aned`

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
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>AvpFairPlayUserClient.access</key>
+	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.appleaccountd</string>
 	<key>aps-connection-initiate</key>

 		<string>com.apple.appleaccountd</string>
 		<string>com.apple.appleaccount</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AvpFairPlayUserClient</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```
### appprotectiond

> `/usr/libexec/appprotectiond`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.UI</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<true/>
 	<key>com.apple.springboard.externaldisplay.displayArrangements</key>
 	<true/>
+	<key>com.apple.springboard.home-screen-configuration</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
+	<key>com.apple.modelmanager.assertion</key>
+	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.modelmanager</string>
 		<string>com.apple.realitycamerad.RCXPCProvider</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.figcpecryptor.xpc</string>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>com.apple.systemstatus.domains</key>
+	<array>
+		<string>media</string>
+	</array>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.cameracaptured</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.homehubd</key>
+	<array>
+		<string>endpoint-read</string>
+	</array>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.homekit.messaging</key>

 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.homehubd.manage</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.MobileTimer.alarmserver</string>
 		<string>com.apple.MobileTimer.timerserver</string>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 	</array>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.backboard.client</key>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### cryptexd

> `/usr/libexec/cryptexd`

```diff

 	</array>
 	<key>com.apple.private.vfs.graftdmg</key>
 	<true/>
+	<key>com.apple.private.xpc.allowed-launch-types</key>
+	<array>
+		<integer>1</integer>
+	</array>
 	<key>com.apple.private.xpc.cryptex.terminate</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.deviceaccessd</string>
+	<key>com.apple.bluetooth.custom.properties.writable</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>

```
### diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```diff

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
-	<key>com.apple.private.usernotifications.bundle-identifiers</key>
-	<array>
-		<string>com.apple.Diagnostics</string>
-		<string>com.apple.EnhancedLogging</string>
-		<string>com.apple.supportapp.notifications</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.usernotifications.usernotificationservice</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.diagnosticspushd</string>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 	<true/>
 	<key>com.apple.Pasteboard.paste-unchecked</key>
 	<true/>
+	<key>com.apple.ProactiveSummarization.feedback</key>
+	<true/>
 	<key>com.apple.SystemConfiguration.SCPreferences-read-access</key>
 	<array>
 		<string>com.apple.radios.plist</string>

 		<string>group.com.apple.mail</string>
 		<string>group.com.apple.iBooks</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Caches/com.apple.chrono/widget-relevance-cache/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.proactive.UserEducationSuggestion.client-listener.xpc</string>

 		<string>com.apple.foundationmodels.languagemodelservice</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.nanoprefsync</string>
+		<string>com.apple.ProactiveSummarization.server</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-write</key>
 	<string>com.apple.NanoHomeScreen.RelevantWidgetDefaults</string>

```
### merchantd

> `/usr/libexec/merchantd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>

```
### mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.modelmanager.assertion</key>
 	<true/>
 	<key>com.apple.modelmanager.query</key>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 		<string>spi</string>
 		<string>cellular-plan</string>
 	</array>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.keystore.dsme_access</key>

 		<string>com.apple.apsd</string>
 		<string>com.apple.cache_delete</string>
 		<string>com.apple.cache_delete.public</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### ospredictiond

> `/usr/libexec/ospredictiond`

```diff

 		<string>Device.ScreenLocked</string>
 		<string>Device.TimeZone</string>
 		<string>Device.Power.BatteryLevel</string>
+		<string>Location.MicroLocationVisit</string>
 	</array>
 	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
 	<string>ospredictiond</string>

 	<true/>
 	<key>com.apple.private.sleepd</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceCalendar</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.osintelligence.inactivity.notifications</string>

 		<string>com.apple.locationd.synchronous</string>
 		<string>com.apple.geod</string>
 	</array>
+	<key>com.apple.security.personal-information.calendars</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>251</string>

```
### otpaird

> `/usr/libexec/otpaird`

```diff

 <dict>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.octagon</string>

```
### photosfaced

> `/usr/libexec/photosfaced`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.AXMediaUtilitiesService-access</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.ap.idmanager</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.replayd</string>
 		<string>group.com.apple.portrait.BackgroundReplacement</string>
 	</array>
 	<key>com.apple.private.skylight.expanse</key>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.replayd</string>
 		<string>group.com.apple.portrait.BackgroundReplacement</string>
 	</array>
 	<key>com.apple.security.device.audio-input</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
+	<key>com.apple.networkrelay.deviceMonitor</key>
+	<true/>
+	<key>com.apple.networkrelay.devices.read</key>
+	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
 	<key>com.apple.nfcd.session.lpemConfig</key>

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.terminusd</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-container</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.ownersession</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.imagent.chat</key>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.icloud.searchpartyd.accessorydiscoverysession</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.iconservices</string>
 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>

```
### thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.avfoundation.allow-system-wide-context</key>
+	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
 	<key>com.apple.carousel.onWristMonitor.actions</key>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.tvremoted</string>
 	<key>com.apple.CompanionLink</key>
 	<true/>
 	<key>com.apple.PairingManager.Read</key>

 		<string>/Library/Caches/com.apple.tvremoted/</string>
 		<string>/Library/Caches/tvapp_bag/</string>
 		<string>/Library/HTTPStorages/com.apple.tvremoted/</string>
+		<string>/Library/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<array>
 		<string>com.apple.icloud.searchpartyd</string>
 		<string>com.apple.da</string>
+		<string>com.apple.carplay</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<array>
 		<string>StoreDemoMode</string>
 	</array>
-	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
-	<true/>
-	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
-	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.wifid</string>
 	<key>com.apple.private.biome.read-write</key>

```
