## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.coreidvd.docUpload.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.passd.account</string>

```
### AccessibilityReader_iOS

> `/Applications/AccessibilityReader_iOS.app/AccessibilityReader_iOS`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.iphone.axserver-systemwide</string>
 		<string>com.apple.accessibility.voices</string>
 	</array>
+	<key>com.apple.security.exception.mach-register.local-name</key>
+	<array>
+		<string>com.apple.iphone.axserver</string>
+	</array>
 	<key>com.apple.springboard.homeScreenIconStyle</key>
 	<true/>
 	<key>com.apple.springboard.launchapplications</key>

```
### AuthenticationServicesUI

> `/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI`

```diff

 		<key>appData</key>
 		<array>
 			<string>com.apple.mobilesafari</string>
+			<string>com.apple.Passwords</string>
 		</array>
 	</dict>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.airdrop.settings</key>
 	<true/>
+	<key>com.apple.private.associated-domains</key>
+	<true/>
 	<key>com.apple.private.attribution.explicitly-assumed-identities</key>
 	<array>
 		<string>com.apple.Passwords</string>

 		<string>com.apple.sharingd</string>
 		<string>com.apple.AuthenticationServices.AutoFill</string>
 		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.SharedWebCredentials</string>
 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.ind.cloudfeatures</string>

```
### ContinuitySingShieldUI

> `/Applications/ContinuitySingShieldUI.app/ContinuitySingShieldUI`

```diff

 	<array>
 		<string>background-activities</string>
 	</array>
+	<key>com.apple.wifi.manager-access</key>
+	<true/>
 	<key>fairplay-client</key>
 	<integer>1974055701</integer>
 </dict>

```
### Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

```diff

 	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>EXDisplayPipeUserClient</string>
 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH10CamInUserClient</string>
 		<string>AppleH9CamInUserClient</string>

```
### Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

```diff

 	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>EXDisplayPipeUserClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.backlightd</string>

```
### Diagnostic-8079

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079`

```diff

 	<array>
 		<string>/private/var/Managed Preferences/mobile/com.apple.CoreMotion.plist</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>EXDisplayPipeUserClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.avfaudio.devicetest.service</string>

```
### Diagnostic-8246

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246`

```diff

 	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>EXDisplayPipeUserClient</string>
+	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
 		<string>kern.exclaves_status</string>

```
### Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileSoftwareUpdate/Controller/RepairServices/</string>
-		<string>/private/preboot/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/preboot/</string>
 		<string>/private/var/tmp/VeridianFWImage/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>

```
### Diagnostic-8290-EFD

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8290-EFD.appex/Diagnostic-8290-EFD`

```diff

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXDeviceUserClient</string>
+		<string>EXDisplayPipeUserClient</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleSMCClient</string>
+		<string>EXDisplayPipeUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

 		<string>CLIENT_ENTITLEMENT</string>
 		<string>PURGE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.CoreRepairCore.repairInfo</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>BasebandUniqueId</string>

 		<string>com.apple.ZhuGeService</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.powerui.smartChargeManager</string>
+		<string>com.apple.CoreRepairCoreXPCService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FamilyExtensionHost

> `/Applications/FamilyExtensionHost.app/FamilyExtensionHost`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

```
### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.RepairDevice.access</key>
+	<true/>
+	<key>com.apple.icloud.searchparty.beaconManager.repairdeviceaccess</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.accessorydiscoverysession</key>

 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.findmy.findmylocate.fenceservice</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FMDCFUTheftAndLossReminderExtension

> `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/FMDCFUTheftAndLossReminderExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.RepairDevice.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
+	<key>com.apple.icloud.searchparty.beaconManager.repairdeviceaccess</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.icloud.findmydeviced</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.ak.auth.xpc</string>
 	</array>
 </dict>
 </plist>

```
### GameCenterUIService

> `/Applications/GameCenterUIService.app/GameCenterUIService`

```diff

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.messages.associated-message-extension-bundle-identifiers</key>
+	<array>
+		<string>com.apple.gamecenter.GameCenterUIService.GameCenterMessageExtension</string>
+	</array>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
+	<key>com.apple.private.contactsui.channel-in-process-override</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.xpc-services-enabled</key>
+	<true/>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.persona.write</key>

 	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
+	<key>com.apple.private.security.system-application</key>
+	<true/>
 	<key>com.apple.private.sensitivecontentanalysis.client</key>
 	<array>
 		<string>analysis</string>

```
### PosterBoard

> `/Applications/PosterBoard.app/PosterBoard`

```diff

 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### RemotePaymentPassActionsMessagesExtension

> `/Applications/RemotePaymentPassActionsService.app/PlugIns/RemotePaymentPassActionsMessagesExtension.appex/RemotePaymentPassActionsMessagesExtension`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/PassKit/</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleKeyStoreUserClient</string>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
-	<key>com.apple.coreidvd.web-presentment.internal</key>
-	<true/>
 	<key>com.apple.developer.WebKit.ServiceWorkers</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
-		<string>com.apple.coreidvd.web-presentment.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.cdp.daemon</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>

 	<string>BackgroundShortcutRunner</string>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sessionkit.assertionRequester</key>
 	<true/>
 	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>

 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.VisualIntelligence</string>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>
+	<true/>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.accessibility.local</string>
-		<string>com.apple.private.alloy.accessibility.switchcontrol</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
 		<string>com.apple.private.alloy.accessibility.local</string>
-		<string>com.apple.private.alloy.accessibility.switchcontrol</string>
 	</array>
 	<key>com.apple.private.ids.nearby</key>
 	<true/>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.assistivetouchd</string>
 	<key>com.apple.frontboard.launchapplications</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.coreimage</string>
 		<string>com.apple.ClarityUI</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<true/>
 	<key>com.apple.accessibility.AXSettingsShortcuts</key>
 	<true/>
+	<key>com.apple.accessibility.AccessibilityUIServer</key>
+	<true/>
 	<key>com.apple.accessibility.SpeakThisServices</key>
 	<true/>
 	<key>com.apple.accessibility.api</key>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 		<string>TurnBasedMultiplayer</string>
 		<string>GameStats</string>
 	</array>
+	<key>com.apple.private.imcore.imagent</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>GameOverlaySocialSuggestions</key>

 		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.iconservices.store</string>
 		<string>com.apple.iconservices</string>
+		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.iphone.axserver-systemwide</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.mediaremoted.xpc</string>

```
### MusicKitUI

> `/System/Library/CoreServices/MusicKitUI.app/MusicKitUI`

```diff

 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.mobileactivationd</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>fairplay-client</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
+	<key>com.apple.coremedia.virtualdisplay.allow</key>
+	<true/>
 	<key>com.apple.coremedia.virtualdisplaysession</key>
 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>
 	<true/>
-	<key>com.apple.springboard.windowing-telemetry-personalization</key>
-	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptom_analytics.refresh</key>

```

### 🆕 ClockPosterExtension

> `/System/Library/ExtensionKit/Extensions/ClockPosterExtension.appex/ClockPosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PRWantsLocation</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.ClockPoster.ClockPosterExtension</string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.ClockPoster.ClockPosterExtension</string>
	<key>com.apple.developer.weatherkit</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.locationd.prompt_from_background</key>
	<true/>
	<key>com.apple.locationd.usage_oracle</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.mobiletimerd</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/MappedImageCache/com.apple.ClockKitUI.configurableHands</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.MobileTimer.timerserver</string>
		<string>com.apple.MobileTimer.alarmserver</string>
		<string>com.apple.systemstatus</string>
	</array>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>com.apple.systemstatus.domains</key>
	<array>
		<string>status-bar-overrides</string>
	</array>
</dict>
</plist>

```
### DeveloperSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents`

```diff

 	<array>
 		<string>AppleProcessorTraceUserClient</string>
 	</array>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 </dict>
 </plist>
 

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>GenerativeExperiences.WritingToolsFeatures.ComposeAndAdjust</string>
 		<string>AdAttributionKit.AggregatedReporting.Purchase</string>
 		<string>AdAttributionKit.AggregatedReporting.Conversion</string>
+		<string>AdAttributionKit.AggregatedReporting.SystemReportedPurchase</string>
+		<string>AdAttributionKit.AggregatedReporting.DeveloperReportedPurchase</string>
 		<string>Siri.ASR.RequestMetricsRecord</string>
 		<string>WalletPaymentsCommerce.UserProofing.Result</string>
 		<string>Autonaming.Messages.AccuracyFedStats</string>

```
### FedStatsMLHostPluginClassA

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA`

```diff

 		<string>RegionalSafetyAnalysis.GuardrailResult</string>
 		<string>GenerativeExperiences.GuardrailResult</string>
 		<string>GenerativeExperiences.GeneratedImageFeatures.FailureReason</string>
+		<string>AppleIntelligence.Reporting.SafetyGuardrails</string>
+		<string>AppleIntelligence.Reporting.SafetyOverrides</string>
+		<string>Shortcuts.UseModel.Safety</string>
 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>

```
### IntelligencePlatformDataActionsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/IntelligencePlatformDataActionsAppIntentsExtension.appex/IntelligencePlatformDataActionsAppIntentsExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.parsecd</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.DeviceActivity</string>

```

### 🆕 OrderExtractionDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/OrderExtractionDiagnosticExtension.appex/OrderExtractionDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.finance.private</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.finance.OrderExtractionDiagnosticExtension</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>OrderExtractionDiagnosticExtension</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>Wallet.PaymentsCommerce.ExtractedOrder</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
			<key>Streams</key>
			<dict>
				<key>WalletPaymentsCommerce.FoundIn.ClassicOrder</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>WalletPaymentsCommerce.FoundIn.OrderEmail</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>WalletPaymentsCommerce.FoundIn.TrackedOrder</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.financed.service.coredatastore</string>
		<string>com.apple.financed.service.store</string>
		<string>com.apple.financed.service.financestore</string>
	</array>
</dict>
</plist>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>com.apple.WebKit.logPageState</string>
 		<string>com.apple.WebKit.showAllDocuments</string>
 		<string>com.apple.WebKit.showBackForwardCache</string>
+		<string>com.apple.WebKit.dumpAccessibilityTreeToStderr</string>
 		<string>com.apple.WebKit.showGraphicsLayerTree</string>
 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>com.apple.WebKit.logPageState</string>
 		<string>com.apple.WebKit.showAllDocuments</string>
 		<string>com.apple.WebKit.showBackForwardCache</string>
+		<string>com.apple.WebKit.dumpAccessibilityTreeToStderr</string>
 		<string>com.apple.WebKit.showGraphicsLayerTree</string>
 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
-	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
-	<array>
-		<string>com.apple.iCloud.CommCenter</string>
-	</array>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### CommCenterMobileHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
-	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
-	<array>
-		<string>com.apple.iCloud.CommCenter</string>
-	</array>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.email</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.financed</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.WalletBlastDoorService</string>
+		<string>com.apple.email.maild</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```

### 🆕 DirectToVMSettingsBundle

> `/System/Library/PreferenceBundles/DirectToVMSettingsBundle.bundle/DirectToVMSettingsBundle`

- No entitlements *(yet)*

### 🆕 InputAccessoriesBundle

> `/System/Library/PreferenceBundles/InputAccessoriesBundle.bundle/InputAccessoriesBundle`

- No entitlements *(yet)*

### 🆕 KeyboardSettings

> `/System/Library/PreferenceBundles/KeyboardSettings.bundle/KeyboardSettings`

- No entitlements *(yet)*

### 🆕 PasscodeAndBiometricsSettingsPref

> `/System/Library/PreferenceBundles/PasscodeAndBiometricsSettingsPref.bundle/PasscodeAndBiometricsSettingsPref`

- No entitlements *(yet)*

### 🆕 TranslateSettings

> `/System/Library/PreferenceBundles/TranslateSettings.bundle/TranslateSettings`

- No entitlements *(yet)*

### 🆕 iCloudPreferences

> `/System/Library/PreferenceBundles/iCloudPreferences.bundle/iCloudPreferences`

- No entitlements *(yet)*
### com.apple.accounts.dom

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/XPCServices/com.apple.accounts.dom.xpc/com.apple.accounts.dom`

```diff

 	<key>com.apple.private.MobileContainerManager.appGroup.noReference</key>
 	<array>
 		<string>group.com.apple.moments</string>
+		<string>group.com.apple.freeform</string>
 	</array>
 	<key>com.apple.private.MobileContainerManager.deleteContainerContent</key>
 	<true/>

```
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
+		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>
 	<key>com.apple.private.corewifi</key>

```
### AfibBurdenDiagnosticExtension

> `/System/Library/PrivateFrameworks/AfibBurden.framework/PlugIns/AfibBurdenDiagnosticExtension.appex/AfibBurdenDiagnosticExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<string>/Library/Preferences/Logging/Subsystems/</string>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<string>/private/var/mobile/Library/Logs/</string>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>Library/Logs/AfBHIDDiagnostics/</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 AppMigrationKitHelper

> `/System/Library/PrivateFrameworks/AppMigrationKit.framework/XPCServices/AppMigrationKitHelper.xpc/AppMigrationKitHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.app-migration-host</key>
	<true/>
	<key>com.apple.private.container.access</key>
	<dict>
		<key>appData</key>
		<dict>
			<key>*</key>
			<dict>
				<key>systemData</key>
				<dict>
					<key>access</key>
					<string>read-write</string>
					<key>domains</key>
					<array>
						<string>com.apple.appmigrationkit</string>
					</array>
					<key>operations</key>
					<array>
						<string>lookup</string>
					</array>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.appmigrationkit.staged-migration-data</string>
	</array>
</dict>
</plist>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	<true/>
 	<key>com.apple.private.cfnetwork.har-capture-amp</key>
 	<true/>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.applemediaservices.multiuser</key>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.amsengagementd</string>
 	<key>com.apple.appstored.private</key>

 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.watchnotificationsui.alertservice</string>
+		<string>com.apple.PineBoardServices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	</array>
 	<key>com.apple.trial.status.namespace-name.allow</key>
 	<array>
+		<string>COREOS_GMPOWER_VM_TUNING_PAGE_SHORTAGE_THRESHOLDS</string>
 		<string>INTELLIGENCE_FLOW_PLAN_RESOLUTION</string>
 		<string>MYRIAD_BOOSTS</string>
 		<string>SIRI_AUDIO_APP_SELECTION_HOMEACCESSORY</string>

 		<string>SIRI_SUGGESTIONS_DOMAIN_GROUP_A</string>
 		<string>SIRI_SUGGESTIONS_DOMAIN_GROUP_B</string>
 		<string>SIRI_SUGGESTIONS_PLATFORM</string>
-		<string>SIRI_TTS_AB_DEVICE</string>
+		<string>SIRI_TTS_UAF_AB_DEVICE</string>
 		<string>SIRI_UI_RESPONSES_SETTINGS</string>
 		<string>SIRI_UNDERSTANDING_CLASSIC_DEPRECATION</string>
 		<string>SIRI_UNDERSTANDING_NL</string>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.mdmd-access</key>
 	<true/>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
+	<key>com.apple.mkb.usersession.keybagopaquedata</key>
+	<true/>
 	<key>com.apple.mobileactivationd.bridge</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

```

### 🆕 BWPreviewStitcherNodeCoreImageArchive_bin.metallib

> `/System/Library/PrivateFrameworks/CMCapture.framework/BWPreviewStitcherNodeCoreImageArchive_bin.metallib`

- No entitlements *(yet)*
### cloudd

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd`

```diff

 		<string>com.apple.cloudkit.partlycloudd</string>
 		<string>com.apple.cloudkit.partlycloudd.debug</string>
 	</array>
-	<key>com.apple.security.personal-information.addressbook</key>
-	<true/>
 	<key>com.apple.spaceattribution.private</key>
 	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>

```
### CMFSyncAgent

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.cmfsyncagent</string>
-	<key>com.apple.Contacts.database-allow</key>
-	<true/>
 	<key>com.apple.StatusKit.publish.types</key>
 	<array>
 		<string>com.apple.focus.status</string>
 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.cmfsyncagent</string>
-	<key>com.apple.private.contacts</key>
-	<true/>
 	<key>com.apple.private.dark-wake-network-reachability</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile</key>

```
### devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

 	<true/>
 	<key>com.apple.private.osanalytics.SubmitLogs.allow</key>
 	<true/>
-	<key>com.apple.private.security.storage.erm</key>
-	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>

```
### LocationDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LocationDiagnosticExtension.appex/LocationDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/Logs/location_log_keys/</string>
 		<string>/Library/Logs/CrashReporter/gpsd/</string>
 		<string>/Library/Logs/CrashReporter/raven/</string>
 		<string>/Library/Logs/CrashReporter/pipelined/</string>

```
### FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.icloud.searchparty.beaconManager.repairdeviceaccess</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### IRNDiagnosticExtension

> `/System/Library/PrivateFrameworks/HeartRhythmAlgorithms.framework/PlugIns/IRNDiagnosticExtension.appex/IRNDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<string>/private/var/mobile/Library/Logs/</string>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<string>Library/Logs/IRNDiagnostics/</string>
 </dict>
 </plist>
 

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.homecommsd.xpc</string>
+		<string>com.apple.uarp.endpoint.transport</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
+	<key>com.apple.uarp</key>
+	<true/>
+	<key>com.apple.uarp.endpoint.transport</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>com.apple.videoconference.allow-conferencing</key>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 		<string>com.apple.ProgressReporting</string>
 		<string>com.apple.searchd</string>
 		<string>com.apple.omniSearch.search</string>
+		<string>com.apple.omniSearch.answerSynthesis</string>
 		<string>com.apple.siri.flowtools_xpc_service</string>
 		<string>com.apple.corespeech.corespeechd.xpc</string>
 		<string>com.apple.siri.localspeechrecognitionbridge.xpc</string>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
-		<string>com.apple.backgroundassets.managed</string>
 		<string>com.apple.backgroundassets.managed.helper.service</string>
 		<string>com.apple.itunesstored</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.backgroundassets.managed</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-container</key>

```
### destinationd

> `/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd`

```diff

 	<array>
 		<string>group.com.apple.Maps</string>
 	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.suggestions.events</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/System/Library/Preferences/Logging/</string>
 		<string>/AppleInternal/Library/Preferences/Logging/</string>

```
### navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

 	<array>
 		<string>group.com.apple.Maps</string>
 	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 		<string>/Library/Preferences/Logging/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/db/MobileIdentityData/Version.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.assistant.backedup.plist</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.assistant.plist</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.assistant.support.plist</string>

 		<string>com.apple.callkit.callcontrollerhost</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.navd.commuteroute</string>
+		<string>com.apple.navd.commutewindow</string>
 		<string>com.apple.coreautomationd.xpc.mobile</string>
 		<string>com.apple.coremedia.admin</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
+		<string>com.apple.MobileAsset.UAF.Photos.SpatialPhotosRelive</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_SpatialPhotosRelive/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.spatialphotosrelive</string>
 		<string>com.apple.spotlightui</string>
 		<string>com.apple.CloudKit</string>
 		<string>com.apple.purplebuddy</string>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
+		<string>com.apple.MobileAsset.UAF.Photos.SpatialPhotosRelive</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_SpatialPhotosRelive/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.spatialphotosrelive</string>
 		<string>com.apple.spotlightui</string>
 		<string>com.apple.CloudKit</string>
 		<string>com.apple.purplebuddy</string>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.rtcreportingd</key>
+	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>
 	<true/>
 	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.networkrelay.deviceMonitor</key>
 	<true/>
 	<key>com.apple.networkrelay.devices.read</key>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.d2d.transferProgress</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.manualBackupStarted</key>
+	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.restoreCompletedAlertStateChanged</key>
 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.restoreStateChanged</key>

```
### NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.nanosystemsettings</key>
 	<array>
 		<string>accounts</string>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/DeviceRegistry/</string>
+		<string>/Library/NanoPreferencesSync/</string>
 		<string>/Library/Passes/</string>
 		<string>/tmp/com.apple.Passbook/</string>
 		<string>/Library/HTTPStorages/com.apple.NPKCompanionAgent/</string>

```

### 🆕 NUNICalliopeShadersCompanion.metallib

> `/System/Library/PrivateFrameworks/NanoUniverse.framework/NUNICalliopeShadersCompanion.metallib`

- No entitlements *(yet)*
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```

### 🆕 PerfPowerServicesSignpostService

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostService.xpc/PerfPowerServicesSignpostService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PerfPowerServicesSignpostService</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.PerfPowerServicesSignpostService</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Production</string>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.MobileContainerManager.allowed</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
	</array>
	<key>com.apple.private.kernel.override-cpumon</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.powerlog</string>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.trial.status.deployment-environment.allow</key>
	<array>
		<integer>0</integer>
	</array>
</dict>
</plist>

```
### com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.suppressrecordingstatetosystemstatus</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.useindependentinputaudioresourcesession</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### TrialArchivingService

> `/System/Library/PrivateFrameworks/TrialServer.framework/XPCServices/TrialArchivingService.xpc/TrialArchivingService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.geoservices.experiments.bucket-id.read</key>
+	<true/>
 	<key>com.apple.private.modelPurgeInAllPartitions.allow</key>
 	<true/>
 	<key>com.apple.private.security.storage.triald</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/AppleInternal/Library/Trial/NamespaceKeys/</string>
+		<string>/private/var/mobile/Library/Caches/GeoServices/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appleneuralengine</string>
+		<string>com.apple.geod</string>
 		<string>com.apple.appleneuralengine.private</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 		<string>com.apple.sharing.handoff.scanning</string>
 		<string>com.apple.CarPlayApp.non-launching-service</string>
 		<string>com.apple.server.bluetooth.general.xpc</string>
+		<string>com.apple.tccd</string>
+		<string>com.apple.tccd.system</string>
 	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
+		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>

 	<string>siriactionsd</string>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.sessionkit.assertionRequester</key>

```

### 🆕 NTKKaleidoscopeShaders.metallib

> `/System/Library/PrivateFrameworks/WatchFacesWallpaperSupport.framework/PlugIns/KaleidoscopePoster.appex/NTKKaleidoscopeShaders.metallib`

- No entitlements *(yet)*
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>

 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sessionkit.assertionRequester</key>
 	<true/>
 	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/containers/Bundle/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.homed.xpc</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.assistant</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.mobilenotes</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.voiceservices</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 		<string>Device.SilentMode</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>Shortcuts.UseModel.Safety</string>
 		<string>ToolKit.Transcript</string>
 	</array>
 	<key>com.apple.private.calendar.daemon.access-level.testing</key>

 	<string>BackgroundShortcutRunner</string>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sessionkit.assertionRequester</key>
 	<true/>
 	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>

 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MapKit.SnapshotService</string>
 		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
+		<string>com.apple.TextInput.rdt</string>
 		<string>com.apple.accessibility.AXBackBoardServer</string>
+		<string>com.apple.accessibility.voices</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.announced.server</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.write</string>
 		<string>com.apple.assistant.cdm</string>
+		<string>com.apple.audio.AURemoteIOServer</string>
 		<string>com.apple.audio.AudioConverterService</string>
+		<string>com.apple.audio.AudioUnitServer</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.user</string>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 		<string>com.apple.HearingAids</string>
 		<string>com.apple.NanoHome</string>
 		<string>com.apple.Sharing</string>
+		<string>com.apple.FitnessIntelligence</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-capture-filter-rendering</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.assetsd.nebulad</string>
 		<string>com.apple.assetsd.keepDaemonAlive</string>
 		<string>com.apple.siri-distributed-evaluation</string>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
+	<key>com.apple.private.contactsui.channel-in-process-override</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.RepairDevice.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.intents.extension.discovery</key>
+	<true/>
 	<key>com.apple.ios.StoreKit.account-page</key>
 	<true/>
 	<key>com.apple.itunescloud.in-app-message-service</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/preferences/SystemConfiguration/</string>
 		<string>/private/var/tmp/siriBC</string>
 	</array>

 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/preferences/SystemConfiguration/</string>
 		<string>/private/var/tmp/siriBC</string>
 	</array>

```
### HomeNotification

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification`

```diff

 		<key>value</key>
 		<string>com.apple.Home</string>
 	</dict>
+	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
+	<dict>
+		<key>com.apple.homekit.camera.clips</key>
+		<string>com.apple.homekit</string>
+	</dict>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
+	<key>com.apple.private.cloudkit.systemService</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

```
### MagnifierExtension

> `/private/var/staged_system_apps/Magnifier.app/Extensions/MagnifierExtension.appex/MagnifierExtension`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceAddressBook</string>

 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.securityd.systemkeychain</string>
 		<string>com.apple.networkserviceproxy</string>
+		<string>com.apple.speech.localspeechrecognition</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### GeneralMapsWidget

> `/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget`

```diff

 	<array>
 		<string>group.com.apple.Maps</string>
 	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.suggestions.events</key>
 	<true/>
 	<key>com.apple.private.tcc.allow.overridable</key>

 	<array>
 		<string>group.com.apple.Maps</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.Maps.Suggestions/</string>

 		<string>com.apple.maps.destinationd.predictions</string>
 		<string>com.apple.navigationService</string>
 		<string>com.apple.navd.commuteroute</string>
+		<string>com.apple.navd.commutewindow</string>
 		<string>com.apple.geoanalyticsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.argos.availibility-bypass</key>
 	<true/>
+	<key>com.apple.asktod</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>

```
### MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.runningboard.posterkit.host</key>
+	<true/>
 	<key>com.apple.sage.textcomposition</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>

```
### MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.runningboard.posterkit.host</key>
+	<true/>
 	<key>com.apple.sage.textcomposition</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.coreduetd.knowledge</key>
 	<true/>
-	<key>com.apple.coreidvd.web-presentment.internal</key>
-	<true/>
 	<key>com.apple.developer.WebKit.ServiceWorkers</key>
 	<true/>
 	<key>com.apple.developer.browser.app-installation</key>

 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
-		<string>com.apple.coreidvd.web-presentment.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.finhealthd</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.fpsd.client</key>

```
### PodcastsWidget

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/PodcastsWidget`

```diff

 	<array>
 		<string>243LU875E5.groups.com.apple.podcasts</string>
 	</array>
+	<key>com.apple.runningboard.assertions.coredata</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.coredata</key>
+	<true/>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### SequoiaTranslator

> `/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator`

```diff

 		<string>com.apple.AudioAccessoryAssetManagementXPCService</string>
 		<string>com.apple.feedbackd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOHIDLibUserClient</string>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.businessservicesd.businessmetadata</key>
+	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.InternalBiome</key>

 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/containers/Bundle/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/Caches/com.apple.businessservicesd/</string>
 		<string>/Library/DuetExpertCenter/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
 		<string>/Library/UserConfigurationProfiles/</string>

 		<string>com.apple.audio.AudioQueueServer</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.businessservicesd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.coreduetd.knowledge</string>

 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.HearingAids</string>
 		<string>com.apple.SoundDetection</string>
 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.spotlightui</string>
 		<string>com.apple.voiceservices</string>
 		<string>com.apple.voicetrigger</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### VoiceMemosIntentsExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceMemos.shared</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.private.security.system-application</key>
 	<true/>

```
### VoiceMemosShareExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceMemos.shared</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.private.security.system-application</key>
 	<true/>

```
### VoiceMemos

> `/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceMemos.shared</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.private.security.system-application</key>
 	<true/>

```
### announced

> `/usr/libexec/announced`

```diff

 		<string>com.apple.Sharing</string>
 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.MobileStoreDemo.test</string>
+		<string>com.apple.UIKit</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
 	<key>com.apple.account.dca.fullaccess</key>
-	<string></string>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.appleaccountd</string>
 	<key>com.apple.authkit.birthday</key>

 	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

```
### assetsubscriptiond

> `/usr/libexec/assetsubscriptiond`

```diff

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>/Library/Caches/UnifiedAssetFramework/</string>
 		<string>/Library/Trial/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/UnifiedAssetFramework/</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleKeyStoreUserClient</string>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	</array>
 	<key>com.apple.private.ids.registration</key>
 	<true/>
-	<key>com.apple.private.power.notifications-temp</key>
+	<key>com.apple.private.power.notifications</key>
 	<true/>
 	<key>com.apple.private.security.storage.SoundProfileAsset</key>
 	<true/>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.PairingManager.Write</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

 		<string>com.apple.audio.AUHostingService.arm64e</string>
 		<string>com.apple.BluetoothCloudServices</string>
 		<string>com.apple.corespeech.assistant.activation.xpc</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.usbaudiod</string>
 		<string>com.apple.HearingModeService</string>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceMotion</string>
 		<string>kTCCServiceMediaLibrary</string>
+		<string>kTCCServiceExternalCameraMedia</string>
 	</array>
 	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
 	<true/>

```
### corecaptured

> `/usr/libexec/corecaptured`

```diff

 		<string>CCDataPipeUserClient</string>
 		<string>IOUserUserClient</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/Managed Preferences/mobile/</string>
+		<string>/private/var/tmp/com.apple.corecaptured/</string>
+	</array>
 </dict>
 </plist>
 

```
### coreidvd

> `/usr/libexec/coreidvd`

```diff

 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
-	<string>YES</string>
+	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### deferredmediad

> `/usr/libexec/deferredmediad`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>deferredmediad</string>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceExternalCameraMedia</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.camera</string>

```
### facemetricsd

> `/usr/libexec/facemetricsd`

```diff

 	</dict>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
-		<string>AppLaunch</string>
+		<string>App.InFocus</string>
 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceBTDiscoveryXPCService.access</key>
 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceEraseXPCService.access</key>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.wifi.manager-access</key>

```
### frauddefensed

> `/usr/libexec/frauddefensed`

```diff

 	</array>
 	<key>com.apple.trustkit.frauddefensed</key>
 	<true/>
+	<key>com.apple.trustkit.ui</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>trustkit</string>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>

 	<array>
 		<string>com.apple.MobileAsset.CoreLocationConfig</string>
 		<string>com.apple.MobileAsset.UAF.AONSenseConfiguration</string>
+		<string>com.apple.MobileAsset.UAF.CoreMotion.IMUFoundationModel</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_AONSenseConfiguration/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel_Overrides/purpose_auto/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/db/accessoryupdater/DurianUpdaterService/</string>
 		<string>/private/var/mobile/Library/CLEEDMediaService/</string>
-		<string>/private/var/db/location_log_keys/</string>
+		<string>/private/var/mobile/Library/Logs/location_log_keys/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<string>/Library/UnifiedAssetFramework</string>

 		<string>com.apple.carkit.app.service</string>
 		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.modelmanager</string>
+		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>

```
### lsd

> `/usr/libexec/lsd`

```diff

 <dict>
 	<key>com.apple.MobileDataTransit.allow</key>
 	<true/>
+	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
+	<true/>
 	<key>com.apple.coreservices.lsd</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.launchservices.clearadvertisingid</key>

 	<true/>
 	<key>com.apple.springboard.launchapplications</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
+	<key>com.apple.surfboard.application-service-client</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>com.apple.usermanagerd.persona.fetchbundle</key>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
 	<true/>
+	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
+	<array>
+		<string>com.apple.devicemanagementclient.DMCTools</string>
+	</array>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>

```
### mdmuserd

> `/usr/libexec/mdmuserd`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
+	<array>
+		<string>com.apple.devicemanagementclient.DMCTools</string>
+	</array>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.launchservices.changedefaulthandlers</key>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 		<string>fromMe</string>
 		<string>internal</string>
 	</array>
+	<key>com.apple.private.managed-settings.apply</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>

 		<string>com.apple.apsd</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.ManagedSettingsAgent</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### remindd

> `/usr/libexec/remindd`

```diff

 		<string>210</string>
 		<string>1380</string>
 	</array>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>temporary-sandbox</string>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.ReplayKitAngel.mach</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.controlcenter.remoteservice</string>

 		<string>media</string>
 		<string>background-activities</string>
 	</array>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-call-providers</string>
+		<string>access-calls</string>
+	</array>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>replayd</string>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.locationd.status</key>
 	<true/>
+	<key>com.apple.locationd.time_zone</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.maps.model-access</key>

```
### softposreaderd

> `/usr/libexec/softposreaderd`

```diff

 	<true/>
 	<key>com.apple.seserviced.storage-management</key>
 	<true/>
+	<key>com.apple.timed</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.softposreader</string>

```
### symptomsd

> `/usr/libexec/symptomsd`

```diff

 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>com.apple.symptomsd.distributed.NDF</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>862</string>

```
### symptomsd-helper

> `/usr/libexec/symptomsd-helper`

```diff

 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>com.apple.symptomsd.distributed.NDF</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>862</string>

```
### tailspind

> `/usr/libexec/tailspind`

```diff

 	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.powerexperienced.powermitigationsmanager.service</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleProcessorTraceUserClient</string>

```
### textunderstandingd

> `/usr/libexec/textunderstandingd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.textunderstandingd</string>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-read</key>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>UserFocusComputedMode</key>
+				<dict/>
 			</dict>
 		</dict>
 	</dict>

```
### triald

> `/usr/libexec/triald`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/Managed Preferences/mobile/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### triald_system

> `/usr/libexec/triald_system`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.triald.system</string>
+	<key>com.apple.TrialArchivingService.internal</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.triald.system</string>
 	<key>com.apple.developer.icloud-services</key>

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
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
 	<key>com.apple.private.security.storage.triald</key>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.ExposureNotification</key>
 	<true/>
+	<key>com.apple.private.sessionkit.listener</key>
+	<true/>
 	<key>com.apple.private.skywalk.register-user-pipe</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sessionservices</string>
 		<string>com.apple.carkit.reconnectiontime.service</string>
 		<string>com.apple.bluetoothaudiod</string>
 		<string>com.apple.icloud.findmydeviced</string>

```
### mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.dnssd.cache-only</key>
+	<true/>
 	<key>com.apple.private.ip-domain-table</key>
 	<true/>
 	<key>com.apple.private.necp.match</key>

```
