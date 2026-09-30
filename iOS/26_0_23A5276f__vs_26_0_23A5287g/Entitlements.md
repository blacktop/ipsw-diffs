## 🔑 Entitlements

### AccessibilityReader_iOS

> `/Applications/AccessibilityReader_iOS.app/AccessibilityReader_iOS`

```diff

 	<key>com.apple.developer.user-fonts</key>
 	<array>
 		<string>app-usage</string>
+		<string>font-enumeration</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<array>
 		<string>com.apple.accessibility.voices</string>
 	</array>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.launchapplications</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### ActivityProgressUI

> `/Applications/ActivityProgressUI.app/ActivityProgressUI`

```diff

 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
 	<key>com.apple.systemstatus.publisher.domains</key>

```

### 🆕 AirPlay Receiver

> `/Applications/AirPlay Receiver.app/AirPlay Receiver`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>FairPlay-Classic-Client</key>
	<true/>
	<key>com.apple.CompanionLink</key>
	<true/>
	<key>com.apple.PairingManager.HomeKit</key>
	<true/>
	<key>com.apple.PairingManager.Read</key>
	<true/>
	<key>com.apple.PairingManager.Write</key>
	<true/>
	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
	<true/>
	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>
	<array>
		<string>preferences.plist</string>
	</array>
	<key>com.apple.airplay.receiver.mediaremote.services</key>
	<true/>
	<key>com.apple.airplay.receiverservices</key>
	<true/>
	<key>com.apple.avfoundation.allows-access-to-device-list</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.coremedia.allow-mpeg4streaming</key>
	<true/>
	<key>com.apple.coremedia.allow-protected-content-playback</key>
	<true/>
	<key>com.apple.coremedia.salplayer</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.devicesharingd.client</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.MobileActivation</key>
	<array>
		<string>GetActivationState</string>
	</array>
	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.driverkit.driver-access</key>
	<array>
		<string>com.apple.private.wifi.driverkit</string>
	</array>
	<key>com.apple.private.mediaexperience.systemcontroller.allowappstoinitiateplayback</key>
	<true/>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.rapport.Client</key>
	<true/>
	<key>com.apple.runningboard.airplayreceiver</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOTimeSyncClockManagerUserClient</string>
		<string>IOTimeSyncgPTPManagerUserClient</string>
		<string>IOTimeSyncDomainUserClient</string>
		<string>IOTimeSyncNetworkPortUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.PairingManager</string>
		<string>com.apple.bluetooth.xpc</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.wifip2pd</string>
		<string>com.apple.devicesharingd</string>
		<string>com.apple.fairplayd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.airplay</string>
	</array>
	<key>com.apple.springboard.appbackgroundstyle</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>com.apple.timed</key>
	<true/>
	<key>com.apple.timed.sources</key>
	<array>
		<string>AirPlaySendingDeviceTime</string>
	</array>
	<key>com.apple.wifi.events</key>
	<true/>
	<key>com.apple.wifi.events.private</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>com.apple.wifip2pd</key>
	<true/>
	<key>com.apple.wlan.authentication</key>
	<true/>
	<key>fairplay-client</key>
	<integer>938689383</integer>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.airplay</string>
		<string>com.apple.airplay.pairing</string>
		<string>com.apple.pairing</string>
	</array>
</dict>
</plist>

```
### AppDistributionLaunchAngel

> `/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel`

```diff

 	<true/>
 	<key>com.apple.payment.card-on-file</key>
 	<true/>
+	<key>com.apple.payment.externalized-context</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### CoreAuthUI

> `/Applications/CoreAuthUI.app/CoreAuthUI`

```diff

 	<true/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.device.verify</key>

 		<string>com.apple.LocalAuthentication.RemoteUIHost</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.sharingd.nsxpc</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### CredentialSharingUIViewService

> `/Applications/CredentialSharingUIViewService.app/CredentialSharingUIViewService`

```diff

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.security.storage.coreduet_knowledge_store</key>

```
### Diagnostic-6017

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6017.appex/Diagnostic-6017`

```diff

 <dict>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/accessoryupdater/uarp/sysdiagnose/</string>

```
### DockFolderViewService

> `/Applications/DockFolderViewService.app/DockFolderViewService`

```diff

 	<array>
 		<string>com.apple.finder</string>
 	</array>
+	<key>com.apple.runningboard.assertions.desktopserviceshelper</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.DocumentManager</string>

```
### FamilyOutOfProcessUIExtension

> `/Applications/FamilyExtensionHost.app/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.family.ageRange.xpc</string>

 		<string>com.apple.ScreenTimeAgent.Contacts</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.familycircled</string>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.HeadphoneProxFeatureService</string>
+		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
 	</array>
 	<key>com.apple.sharing.Client</key>
 	<true/>

```
### HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
+	<key>com.apple.energykit.client</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.homeenergy</key>
+	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.homekit.person-manager</key>

```
### LocalAuthenticationUIService

> `/Applications/LocalAuthenticationUIService.app/LocalAuthenticationUIService`

```diff

 	<true/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.device.verify</key>

 		<string>com.apple.LocalAuthentication.RemoteUIHost</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.sharingd.nsxpc</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### MomentsUIService

> `/Applications/MomentsUIService.app/MomentsUIService`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.Visit</key>
 	<true/>
+	<key>com.apple.QuartzCore.displayable-context</key>
+	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 		<string>com.apple.momentsui</string>
 		<string>com.apple.momentsd</string>
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
 	<key>com.apple.security.ts.geoservices</key>

```
### NetworkEndpointPickerUI

> `/Applications/NetworkEndpointPickerUI.app/NetworkEndpointPickerUI`

```diff

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/Applications/NetworkEndpointPickerUI.app/NetworkEndpointPickerUI</string>
+	</dict>
 	<key>com.apple.private.avfoundation.background-camera-access</key>
 	<true/>
 	<key>com.apple.private.avfoundation.capture.hidden-cameras.allow</key>

```
### PeerPaymentMessagesExtension

> `/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.messages.private.AllowAlertPresentation</key>
 	<true/>
+	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>
+	<true/>
 	<key>com.apple.messages.private.AllowParticipantAddressAccess</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.feedbackd.client-forms</key>
 	<array>
+		<string>framework-autocorrect_S04_vi</string>
 		<string>framework-autocorrect_S03_fr</string>
 		<string>framework-autocorrect_S03_es</string>
 	</array>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>

 		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>
 		<string>kTCCServiceExposureNotification</string>
 	</array>
+	<key>com.apple.private.tcc.icons_for_prompts</key>
+	<true/>
 	<key>com.apple.private.tcc.manager</key>
 	<true/>
 	<key>com.apple.private.timezoneupdates.tzd.access</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
 		<string>com.apple.audio.AudioSession</string>
 		<string>com.apple.locationaccessstored.registration</string>
 		<string>com.apple.softposreaderd</string>

 		<string>com.apple.identities</string>
 		<string>appleaccount</string>
 		<string>com.apple.mobilemail.smime</string>
-		<string>com.apple.openai</string>
 		<string>com.apple.preferences</string>
 		<string>com.apple.safari.credit-cards</string>
-		<string>com.apple.snowflake</string>
 		<string>com.apple.PassbookUIService</string>
 		<string>com.apple.ProtectedCloudStorage</string>
 		<string>com.apple.PublicCloudStorage</string>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 		<key>value</key>
 		<string>/Applications/SafariViewService.app</string>
 	</dict>
-	<key>com.apple.private.backgroundtaskmanagement.manage</key>
-	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>App.WebApp.InFocus</string>

```
### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 	<true/>
 	<key>com.apple.argos.availibility-bypass</key>
 	<true/>
+	<key>com.apple.assistant.settings</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.siri.sirireaderd</string>
 		<string>com.apple.parsecd</string>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.springboard.wallpaper-access</key>
 	<true/>
+	<key>com.apple.springboard.windowing-telemetry-personalization</key>
+	<true/>
 	<key>com.apple.telephony.cupolicy-monitor-access</key>
 	<true/>
 	<key>com.apple.timed</key>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.email</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 		<string>com.apple.SharingServices</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.bird.token</string>

 		<string>com.apple.coremedia.routediscoverer.xpc</string>
 		<string>com.apple.coremedia.routingcontext.xpc</string>
 		<string>com.apple.coremedia.volumecontroller.xpc</string>
+		<string>com.apple.email.maild</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.email</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 		<string>com.apple.coremedia.routediscoverer.xpc</string>
 		<string>com.apple.coremedia.routingcontext.xpc</string>
 		<string>com.apple.coremedia.volumecontroller.xpc</string>
+		<string>com.apple.email.maild</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.geoanalyticsd.telemetry</key>

 		<string>com.apple.siri.location</string>
 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
+		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### SupportFlow

> `/Applications/SupportFlow.app/SupportFlow`

```diff

 		<string>com.apple.softwareupdateservicesd</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.tipsd</string>
+		<string>com.apple.tzlink</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<true/>
 	<key>com.apple.tipsd.access</key>
 	<true/>
+	<key>com.apple.tzlink.allow</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>com.apple.wifi.manager-reset-settings</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
+	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
 	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>VisualIntelligenceCamera.DetectedLabels</string>
+		<string>VisualIntelligenceCamera.Lookup.Event</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>

 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
+		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
+	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
 	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>

 		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
+		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```

### 🆕 CodeCoverageDelegate

> `/System/ExclaveKit/System/Library/Frameworks/CodeCoverageDelegate.framework/CodeCoverageDelegate`

- No entitlements *(yet)*
### ClarityBoard

> `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

 	<true/>
 	<key>com.apple.private.biometrickit.allow-match</key>
 	<true/>
+	<key>com.apple.private.dmd.policy</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.behavior.resolution.client-identifiers</key>
 	<array>
 		<string>com.apple.private.ClarityBoard.dnd</string>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<true/>
 	<key>com.apple.idle-timer-services</key>
 	<true/>
+	<key>com.apple.multitasking.termination</key>
+	<true/>
 	<key>com.apple.private.CarPlayServices.icon-layout</key>
 	<true/>
 	<key>com.apple.private.accessories.showallconnections</key>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.default-data-protection</key>
+	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
 	<key>com.apple.developer.game-center</key>
 	<array>
 		<string>Account</string>

 	<array>
 		<string>com.apple.iphone.axserver</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.suggestions</string>
+		<string>com.apple.spotlightui</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.GameOverlayUI</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 		<string>App.Intent</string>
 		<string>MediaSuggester.SuggestionFeedback</string>
 		<string>App.Intents.Transcript</string>
+		<string>Device.Display.Appearance</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ApplicationSnapshot</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Device.Display.Appearance</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.battery-gauging-mitigation</key>
 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>

 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 		<string>com.apple.PerformanceTrace.ptpassivecollectiond.collectionconfig</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>
 	<true/>
+	<key>com.apple.springboard.windowing-telemetry-personalization</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptom_analytics.refresh</key>

 		<string>modify-calls</string>
 		<string>access-call-providers</string>
 		<string>access-moments</string>
+		<string>access-screen-calls</string>
+		<string>smart-holding</string>
 	</array>
 	<key>com.apple.timed</key>
 	<true/>

```

### 🆕 AAKPriMLPlugin

> `/System/Library/ExtensionKit/Extensions/AAKPriMLPlugin.appex/AAKPriMLPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.adattributionkit.AAKPriMLPlugin</string>
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
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.priml.pfl.plugins</string>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>AdAttributionKit.AggregatedReporting.Purchase</string>
		<string>AdAttributionKit.AggregatedReporting.Conversion</string>
		<string>AdAttributionKit.AggregatedReporting.SystemReportedPurchase</string>
		<string>AdAttributionKit.AggregatedReporting.DeveloperReportedPurchase</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.cloudkit.masquerade</key>
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
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.biomed</string>
		<string>com.apple.biome.PublicStreamAccessService</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.aiml.priml.FedStats</string>
	</array>
</dict>
</plist>

```
### BiomeSELFIngestor

> `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/BiomeSELFIngestor`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.lighthouse.dill.BiomeSELFIngestor</string>
+		<string>com.apple.lighthouse.dill.BiomeUploadProcessor</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### DeveloperSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.AppleProcessorTrace.CarveoutProperty</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleProcessorTraceUserClient</string>
+	</array>
 </dict>
 </plist>
 

```
### DynamicBackgroundPosterExtension

> `/System/Library/ExtensionKit/Extensions/DynamicBackgroundPosterExtension.appex/DynamicBackgroundPosterExtension`

```diff

 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.messages.transcriptBackgroundPoster</string>

```
### FamilyOutOfProcessUIExtension

> `/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.family.ageRange.xpc</string>

 		<string>com.apple.ScreenTimeAgent.Contacts</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.familycircled</string>

```

### 🆕 FitnessSettingsIntents

> `/System/Library/ExtensionKit/Extensions/FitnessSettingsIntents.appex/FitnessSettingsIntents`

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
### GradientBackgroundPosterExtension

> `/System/Library/ExtensionKit/Extensions/GradientBackgroundPosterExtension.appex/GradientBackgroundPosterExtension`

```diff

 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.messages.transcriptBackgroundPoster</string>

```
### PhotosAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PhotosAppIntentsExtension.appex/PhotosAppIntentsExtension`

```diff

 <dict>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 </dict>
 </plist>
 

```
### PhotosPFLPlugin

> `/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin`

```diff

 	</array>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mlhostd.xpc</string>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/PhotosPicker`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 		<string>com.apple.ap.promotedcontent.configurationsystem</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.ScreenTimeAgent.exception</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SiriAttentionAndInvocationExtension

> `/System/Library/ExtensionKit/Extensions/SiriAttentionAndInvocationExtension.appex/SiriAttentionAndInvocationExtension`

```diff

 	<array>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
 		<string>Siri.OnDeviceAnalytics.attentionAndInvocationSampling</string>
+		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>

 		<string>com.apple.coreaudio</string>
 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.corespeechdatacollection</string>
+		<string>com.apple.SpeakerIdWorker</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin`

```diff

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Logs/com.apple.FeatureStore/</string>
 		<string>/Library/com.apple.siri.inference/</string>
 		<string>/Library/Shortcuts/ToolKit/</string>
 	</array>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 		<string>com.apple.ap.promotedcontent.configurationsystem</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.ScreenTimeAgent.exception</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 VisualIntelligenceCameraAnalytics

> `/System/Library/ExtensionKit/Extensions/VisualIntelligenceCameraAnalytics.appex/VisualIntelligenceCameraAnalytics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.VisualIntelligenceCameraAnalytics</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>VisualIntelligenceCamera.Lookup.Event</string>
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
		<string>group.com.apple.VisualIntelligenceCameraAnalytics</string>
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
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.notes</string>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 		<string>802</string>
 		<string>800</string>
 		<string>801</string>
+		<string>862</string>
 	</array>
 	<key>com.apple.triald.namespace-management</key>
 	<true/>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	<true/>
 	<key>com.apple.private.MobileContainerManager.unrestrictedPersona</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### com.apple.HealthKit.HealthDiagnosticExtension

> `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthDiagnosticExtension.appex/com.apple.HealthKit.HealthDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.hkctl</key>
 	<true/>
+	<key>com.apple.private.healthkit.sync</key>
+	<array>
+		<string>context-sync</string>
+	</array>
 	<key>com.apple.private.security.storage.Health</key>
 	<true/>
 	<key>com.apple.private.sleepd</key>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	</array>
 	<key>com.apple.devicesharing.guest-user-mode-client</key>
 	<true/>
+	<key>com.apple.diagnosticpipeline.request</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.fitnesscoachingd</key>

```

### 🆕 HealthFeaturesDiagnosticExtensionPlugin

> `/System/Library/Health/DiagnosticExtensionPlugins/HealthFeaturesDiagnosticExtensionPlugin.bundle/HealthFeaturesDiagnosticExtensionPlugin`

- No entitlements *(yet)*

### 🆕 FilterSpamSettingsBundle

> `/System/Library/PreferenceBundles/FilterSpamSettingsBundle.bundle/FilterSpamSettingsBundle`

- No entitlements *(yet)*

### 🆕 WISDeveloperSettings

> `/System/Library/PreferenceBundles/WISDeveloperSettings.bundle/WISDeveloperSettings`

- No entitlements *(yet)*
### activitysharingd

> `/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd`

```diff

 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
 	<key>com.apple.private.communicationsfilter</key>

```
### ASDAskPermissionExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/ASDAskPermissionExtension`

```diff

 	<string>com.apple.AppStoreDaemon.ASDAskPermissionExtension</string>
 	<key>com.apple.appstored.private</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Purchase</string>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
-	<key>com.apple.coreidvd.spi</key>
-	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.corefollowup.agent</string>
-		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.dmd.policy</string>
 		<string>com.apple.gamed</string>
 		<string>com.apple.homed.xpc</string>

```
### AMSEngagementViewExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementViewExtension.appex/AMSEngagementViewExtension`

```diff

 		<string>com.apple.AppleMediaServicesUI.engagement.notifications</string>
 		<string>com.apple.AppleMediaServicesUI.engagement.notifications.macOS</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appstoreagent.xpc</string>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.aaa.serverbackoff</string>
 		<string>com.apple.AuthKit.AgeRangeSettingsCache</string>
+		<string>com.apple.AuthKit</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

```diff

 		<string>com.apple.containermanagerd</string>
 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.speech.localspeechrecognition</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.xpc-service-name</key>
 	<array>

 		<string>access-collaboration</string>
 		<string>modify-simulated-conversations</string>
 		<string>smart-holding</string>
+		<string>access-screen-calls</string>
 	</array>
 	<key>com.apple.trial.client</key>
 	<array>

```
### CreateiCloudLinkExtension

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/CreateiCloudLinkExtension.appex/CreateiCloudLinkExtension`

```diff

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.icloud.drive.access-gater</string>

```
### CMFSyncAgent

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.cmfsyncagent</string>
+	<key>com.apple.Contacts.database-allow</key>
+	<true/>
 	<key>com.apple.StatusKit.publish.types</key>
 	<array>
 		<string>com.apple.focus.status</string>
 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.cmfsyncagent</string>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.dark-wake-network-reachability</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile</key>

 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.cmfsyncagent</string>
 	</array>
+	<key>com.apple.springboard.CFUserNotification</key>
+	<true/>
 </dict>
 </plist>
 

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	</array>
 	<key>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</key>
 	<true/>
-	<key>com.apple.TextUnderstanding.process</key>
-	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.ciphermld</string>
-		<string>com.apple.TextUnderstanding.process</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

 	<true/>
 	<key>com.apple.private.CoreAnalytics.RolloverEvents.allow</key>
 	<true/>
+	<key>com.apple.private.DeviceRecovery.BrainController</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.osanalytics.SubmitLogs.allow</key>
 	<true/>
+	<key>com.apple.private.security.storage.erm</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>

```
### IMDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/IMDiagnosticExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.DiagnosticExtensions.IMDiagnosticExtension</string>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.DiagnosticExtensions.IMDiagnosticExtension</string>
+	<key>com.apple.private.imcore.imagent</key>
+	<true/>
+	<key>com.apple.private.imcore.imdpersistence.database-access</key>
+	<true/>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.IMCoreSpotlight</string>
+	</array>
 </dict>
 </plist>
 

```
### FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService`

```diff

 	</array>
 	<key>com.apple.private.apfs.attribution-tags</key>
 	<true/>
+	<key>com.apple.private.apfs.clonegroup</key>
+	<true/>
 	<key>com.apple.private.apfs.get_purgeable_bulk_info</key>
 	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>

```
### com.apple.DocumentManager.Service

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service`

```diff

 		<string>com.apple.private.diskarbitrationd.access</string>
 		<string>com.apple.CloudSharing.SPIHelper-iOS</string>
 		<string>com.apple.DiskArbitration.diskarbitrationd</string>
+		<string>com.apple.lsd.modifydb</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

 	<array>
 		<string>com.apple.nanoprefsync</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.icloud.findmydevice.managed</string>
+	</array>
 </dict>
 </plist>
 

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>com.apple.containermanagerd</string>
 		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.timed.xpc</string>
+		<string>com.apple.securityd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.support</string>
 		<string>com.apple.SummarizationKit</string>
 		<string>com.apple.EmojiPreferences</string>
 		<string>com.apple.AppSupport</string>

```

### 🆕 IntelligenceFlowInternalDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowInternalDiagnostics.appex/IntelligenceFlowInternalDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.intelligenceflow.IntelligenceFlowRuntime.IntelligenceFlowInternalDiagnostics</string>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.intelligenceflow.context</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Sage.Transcript</string>
		<string>IntelligenceFlow.Transcript.Datastream</string>
		<string>IntelligenceEngine.Interaction.Donation</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>com.apple.intelligenceflow.IntelligenceFlowRuntime.IntelligenceFlowInternalDiagnostics</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Sage.Transcript</string>
				<string>IntelligenceFlow.Transcript.Datastream</string>
				<string>IntelligenceEngine.Interaction.Donation</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.security.storage.SiriFeatureStore</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/com.apple.FeatureStore/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.intelligenceflow.context</string>
	</array>
</dict>
</plist>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 		<string>visualIdentifier</string>
 		<string>bundleIdMap</string>
 		<string>entitySimilarityFeatures</string>
+		<string>siriRemembers</string>
 	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>

 		<string>com.apple.searchd</string>
 		<string>com.apple.omniSearch.search</string>
 		<string>com.apple.siri.flowtools_xpc_service</string>
+		<string>com.apple.corespeech.corespeechd.xpc</string>
 		<string>com.apple.siri.localspeechrecognitionbridge.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 	<true/>
 	<key>com.apple.intelligenceplatform.Coordination</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.EntityResolution</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EventLog</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.Internal</key>

 		<string>com.apple.intelligenceplatform.Coordination</string>
 		<string>com.apple.intelligenceplatform.AssetRegistry</string>
 		<string>com.apple.intelligenceplatform.EventLog</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.siri.uaf.service</string>

```
### lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.airplay</string>
+		<string>com.apple.Sharing</string>
+		<string>com.apple.sharingd</string>
+		<string>com.apple.coremedia</string>
+		<string>com.apple.controlcenter</string>
+		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.ThreatNotificationUI.FollowUpExtension</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleVideoToolboxParavirtualizationUserClient</string>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.appletv.pbs.volume-control</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
+	<key>com.apple.locationd.usage_oracle</key>
+	<true/>
 	<key>com.apple.managedconfiguration.feature-setting.allowRemoteAppPairing</key>
 	<true/>
 	<key>com.apple.mediaremote.group-sessions</key>

 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>

 		<string>com.apple.private.alloy.facetime.mw</string>
 		<string>com.apple.private.alloy.groupRemoteControl.messaging</string>
 		<string>com.apple.private.alloy.itunes</string>
+		<string>com.apple.private.alloy.status.keysharing</string>
 	</array>
 	<key>com.apple.private.ids.session</key>
 	<array>

 		<string>com.apple.private.alloy.itunes</string>
 		<string>com.apple.private.alloy.avconference.avctester</string>
 		<string>com.apple.private.alloy.groupRemoteControl.messaging</string>
+		<string>com.apple.private.alloy.status.keysharing</string>
 	</array>
 	<key>com.apple.private.lockdown.finegrained-set</key>
 	<array>

 	</array>
 	<key>com.apple.private.usernotifications.forwarding</key>
 	<true/>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.proximitycontrol</key>
 	<true/>
 	<key>com.apple.proximitycontrol.lockscreenControls</key>

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/MediaRemote/</string>

 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.cmfsyncagent.embedded.auth</string>
 		<string>com.apple.duetactivityscheduler</string>
 	</array>
-	<key>com.apple.security.network.client</key>
-	<true/>
-	<key>com.apple.security.personal-information.addressbook</key>
-	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.cmfsyncagent.auth</string>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.MobileTimer.alarmserver</string>
 		<string>com.apple.posterboardservices.dataModel</string>
+		<string>com.apple.passd.library</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.backupStateChanged</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.d2d.transferMinutesRemaining</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.d2d.transferProgress</key>
+	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.restoreCompletedAlertStateChanged</key>
 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MobileBackup.restoreStateChanged</key>

```
### com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

 	<array>
 		<string>com.apple.MobileAsset.MobileSoftwareUpdate.MacUpdateBrain</string>
 		<string>com.apple.MobileAsset.MobileSoftwareUpdate.UpdateBrain</string>
+		<string>com.apple.MobileAsset.DeviceRecoveryBrain</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

```
### mobiletimerd

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd`

```diff

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.containermanagerd</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.spatialphotosrelive</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>SIML_ADM_PERSONALIZATION_GP</string>
+		<string>SIML_ADM_PERSONALIZATION</string>
+	</array>
 </dict>
 </plist>
 

```
### NPTCellularDiagnosticsExtension

> `/System/Library/PrivateFrameworks/NPTKit.framework/PlugIns/NPTCellularDiagnosticsExtension.appex/NPTCellularDiagnosticsExtension`

```diff

 	<true/>
 	<key>com.apple.private.network-performance-tester</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.wifivelocityd</string>

```
### NPTWiFiDiagnosticsExtension

> `/System/Library/PrivateFrameworks/NPTKit.framework/PlugIns/NPTWiFiDiagnosticsExtension.appex/NPTWiFiDiagnosticsExtension`

```diff

 	<true/>
 	<key>com.apple.private.network-performance-tester</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.wifivelocityd</string>

```
### PhotoAnalysisLighthousePlugin

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/PlugIns/PhotoAnalysisLighthousePlugin.appex/PhotoAnalysisLighthousePlugin`

```diff

 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/var/mobile/Library/Trial/</string>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
-	<key>com.apple.security.assets.pictures.read-write</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

 	</array>
 	<key>com.apple.security.files.bookmarks.app-scope</key>
 	<true/>
-	<key>com.apple.security.network.client</key>
-	<true/>
-	<key>com.apple.security.personal-information.addressbook</key>
-	<true/>
-	<key>com.apple.security.personal-information.calendars</key>
-	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Trial/</string>

```
### PhotosDiagnostics

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosDiagnostics.appex/PhotosDiagnostics`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.sbextensions</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Logs/CrashReporter/DiagnosticLogs/photos/</string>

```
### PhotosSearchDiagnostics

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosSearchDiagnostics.appex/PhotosSearchDiagnostics`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Media/PhotoData/internal/searchdiagnostics/</string>

```
### PhotosStoryDiagnostics

> `/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PlugIns/PhotosStoryDiagnostics.appex/PhotosStoryDiagnostics`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 </dict>
 </plist>
 

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

```diff

 	<string>com.apple.privatecloudcomputed</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>PrivateCloudCompute.RequestLog</string>

```
### replicatord

> `/System/Library/PrivateFrameworks/ReplicatorCore.framework/Support/replicatord`

```diff

 	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
 	<true/>
+	<key>com.apple.authkit.client</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.coreduet.knowledge</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.application-service-browse</key>

 		<string>com.apple.chronod.replicator</string>
 		<string>com.apple.identityservicesd.nsxpc</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.ak.auth.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### AppLaunchIntentExtension

> `/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension`

```diff

 	<string>com.apple.siri.SiriAppLaunchIntents.AppLaunchIntentExtension</string>
 	<key>com.apple.appletv.pbs.app-info-service-access</key>
 	<true/>
+	<key>com.apple.appletv.pbs.person-monitor-service-access</key>
+	<true/>
+	<key>com.apple.appletv.pbs.person-monitor-service-access.write</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsBookkeepingService.xpc/SiriSuggestionsBookkeepingService`

```diff

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Logs/com.apple.FeatureStore/</string>
 		<string>/Library/Caches/com.apple.HomeKit/com.apple.siriinferenced/</string>
 		<string>/Library/Caches/com.apple.siriinferenced/</string>
 		<string>/Library/com.apple.siri.inference/</string>

```
### SiriTTSTrainingAgent

> `/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>
+		<string>/private/var/mobile/Library/Caches/SiriTTS/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Logs/SiriTTSTrainer/</string>
 		<string>/Library/Trial/</string>
 		<string>/Library/com.apple.SiriTTSTrainingAgent/</string>
+		<string>/Library/Caches/SiriTTS/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### VideoIntentExtension

> `/System/Library/PrivateFrameworks/SiriVideoIntents.framework/PlugIns/VideoIntentExtension.appex/VideoIntentExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.appletv.pbs.person-monitor-service-access</key>
+	<true/>
+	<key>com.apple.appletv.pbs.person-monitor-service-access.write</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	<true/>
 	<key>com.apple.private.mobile.releasevalidation.tests</key>
 	<true/>
+	<key>com.apple.private.mobileinboxupdater.xpc</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.springboard.blockableservices</string>
+		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.surfboard.scenesessionservice</string>
 		<string>com.apple.surfboard.applicationservice</string>

```
### com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
 	<true/>
-	<key>com.apple.private.mediaexperience.suppressrecordingstatetosystemstatus</key>
-	<true/>
 	<key>com.apple.private.mediaexperience.useindependentinputaudioresourcesession</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### MauiAUSP

> `/System/Library/PrivateFrameworks/TextToSpeechMauiSupport.framework/PlugIns/MauiAUSP.appex/MauiAUSP`

```diff

 	<array>
 		<string>com.apple.SpeakSelection</string>
 	</array>
-	<key>com.apple.security.files.user-selected.read-only</key>
-	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/System/Library/AssetsV2/</string>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.private.usernotifications.accessory.host</key>
 	<true/>
 	<key>com.apple.private.usernotifications.forwarding</key>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.iconservices</string>
 		<string>com.apple.DeviceAccess.xpc</string>
+		<string>com.apple.contactsd</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### matd

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/matd`

```diff

 	<array>
 		<string>Discoverability.Signals</string>
 	</array>
+	<key>com.apple.private.imcore.imdpersistence.database-access</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>UninstallForLaunchServices</string>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
+	<key>com.apple.private.security.storage.MessagesMetaData</key>
+	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

```
### icloudsubscriptionoptimizerd

> `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd`

```diff

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Application Support/icloudsubscriptionoptimizerd/</string>

 		<string>com.apple.xpc.activity.unmanaged</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
 	</array>
-	<key>com.apple.security.files.user-selected.read-write</key>
-	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```

### 🆕 RemoteUINavigationProxy

> `/System/Library/RemoteUI/Plugins/RemoteUINavigationProxy.bundle/RemoteUINavigationProxy`

- No entitlements *(yet)*
### kbd

> `/System/Library/TextInput/kbd`

```diff

 	<true/>
 	<key>com.apple.feedbackd.client-forms</key>
 	<array>
+		<string>framework-autocorrect_S04_vi</string>
 		<string>framework-autocorrect_S03_fr</string>
 		<string>framework-autocorrect_S03_es</string>
 		<string>:framework-autocorrect-korean</string>

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.stickers.api</string>
+		<string>com.apple.stickers.recency</string>
 		<string>com.apple.spotlight.SearchAgent</string>
 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.ind.cloudfeatures</string>

```
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 		<string>com.apple.ap.promotedcontent.configurationsystem</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.ScreenTimeAgent.exception</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```diff

 	</array>
 	<key>com.apple.private.tvAppExtension</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceMediaLibrary</string>
+	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 		<string>com.apple.storeservices.itfe</string>
 		<string>com.apple.fitcored</string>
 		<string>com.apple.coreaudio.device</string>
+		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
+	<key>com.apple.symptoms.NetworkDiagnostics</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>com.apple.videoconference.allow-conferencing</key>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 	<array>
 		<string>com.apple.momentsd.MOUserNotifications</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Journal</string>
 		<string>group.com.apple.moments</string>
 	</array>
-	<key>com.apple.security.device.audio-input</key>
-	<true/>
-	<key>com.apple.security.device.camera</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

 	<array>
 		<string>com.apple.momentsd</string>
 	</array>
-	<key>com.apple.security.files.user-selected.read-write</key>
-	<true/>
-	<key>com.apple.security.network.client</key>
-	<true/>
-	<key>com.apple.security.personal-information.location</key>
-	<true/>
-	<key>com.apple.security.print</key>
-	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>

```
### JournalShareExtension

> `/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension`

```diff

 		<string>group.com.apple.Journal</string>
 		<string>group.com.apple.moments</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Journal</string>
 		<string>group.com.apple.moments</string>
 	</array>
-	<key>com.apple.security.network.client</key>
-	<true/>
 </dict>
 </plist>
 

```
### JournalWidgets

> `/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgets.appex/JournalWidgets`

```diff

 		<string>group.com.apple.Journal</string>
 		<string>group.com.apple.moments</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.moments</string>

```
### JournalWidgetsSecure

> `/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure`

```diff

 		<string>group.com.apple.Journal</string>
 		<string>group.com.apple.moments</string>
 	</array>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Journal</string>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 		<string>com.apple.safetycheckd</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.TextUnderstanding.process</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelmanager</string>
-		<string>com.apple.biome.access.user</string>
 		<string>com.apple.asktod</string>
 		<string>com.apple.communicationtrustd.service</string>
 		<string>com.apple.jetpackassetd.xpc</string>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
-	<key>com.apple.private.backgroundtaskmanagement.manage</key>
-	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Media.NowPlaying</string>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.MusicKit</string>
+		<string>com.apple.carplay.internal</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache/Library/Caches/com.apple.IconsCache/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<string>1</string>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
-	<key>com.apple.private.backgroundtaskmanagement.manage</key>
-	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

```
### PhotosReliveWidget

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget`

```diff

 	</array>
 	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>
 	<true/>
+	<key>com.apple.private.catalyst-openURL-source</key>
+	<true/>
 	<key>com.apple.private.cfnetwork.har-capture-amp</key>
 	<true/>
 	<key>com.apple.private.coreaudio.viewInterruptorName.allow</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
+	<key>com.apple.private.email</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.email.maild</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>

 	<true/>
 	<key>com.apple.springboard.addWebClipToHomeScreen</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.springboard.removeWebClipFromHomeScreen</key>

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>COREOS_CHARGE_PREDICTION</string>
-		<string>251</string>
 	</array>
 </dict>
 </plist>

```
### assetsubscriptiond

> `/usr/libexec/assetsubscriptiond`

```diff

 		<string>1210</string>
 		<string>1630</string>
 		<string>1701</string>
+		<string>SIRI_TTS_UAF_AB_DEVICE</string>
+		<string>SIML_ADM_PERSONALIZATION</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.private.attentionawareness.poll</key>
 	<true/>
-	<key>com.apple.private.avfoundation.background-camera-access</key>
-	<true/>
-	<key>com.apple.private.avfoundation.capture.allow</key>
-	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
 	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceListenEvent</string>
-		<string>kTCCServiceCamera</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>

 		<string>com.apple.accessories.connection-info-server</string>
 		<string>com.apple.carkit.layer-metadata</string>
 		<string>com.apple.chronoservices</string>
-		<string>com.apple.powerexperienced.powermitigationsmanager.service</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### continuitycaptured

> `/usr/libexec/continuitycaptured`

```diff

 	<true/>
 	<key>com.apple.itunescloudd.private</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.mediaremote.device-info</key>
 	<true/>
 	<key>com.apple.mediaremote.group-sessions</key>

 	<true/>
 	<key>com.apple.nearbyinteraction.background</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.avfoundation.background-camera-access</key>
 	<true/>
 	<key>com.apple.private.avfoundation.capture.allow</key>

 	<true/>
 	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>

 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
+		<string>/Library/Logs/MediaServices/</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>IOTimeSyncClockManagerUserClient</string>

 		<string>com.apple.iTunesCloud.SharedListeningConnectionService</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.itunescloud.remote-request-execution-service</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<array>
 		<string>systemgroup.com.apple.sharedpclogging</string>
 		<string>systemgroup.com.apple.osanalytics</string>
+		<string>systemgroup.com.apple.powerlog</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 		<string>180</string>
 		<string>181</string>
 		<string>333</string>
+		<string>SYSTEM_SPACE_INTELLIGENCE_VISUAL</string>
 	</array>
 	<key>com.apple.watchlist.private</key>
 	<true/>

```
### gamed

> `/usr/libexec/gamed`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.gamecenter</string>

```
### heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

```diff

 	<true/>
 	<key>com.apple.AudioAccessorySystemStateService</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.healthlite.spi</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PowerManagement.control</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 		<string>com.apple.inputAnalytics.IASSRAnalyzer</string>
 		<string>com.apple.inputAnalytics.IASGenmojiAnalyzer</string>
 		<string>com.apple.inputAnalytics.IASGenmojiUsageAnalyzer</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.inputanalyticsd</string>

```
### locationd

> `/usr/libexec/locationd`

```diff

 		<string>com.apple.private.alloy.regulatorysync</string>
 		<string>com.apple.private.alloy.location.fencehandoff</string>
 	</array>
+	<key>com.apple.private.ids.pnr-credential-vendor</key>
+	<true/>
 	<key>com.apple.private.ids.remotecredentials</key>
 	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Trial_Siri_SiriTextToSpeech/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_FM/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/</string>

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_SecureAnalytics_FM/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_Guardrail/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_Trial_Siri_SiriTextToSpeech/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_CoreMotion_FM/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.PowerManagement.control</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

```
### routined

> `/usr/libexec/routined`

```diff

 	</dict>
 	<key>com.apple.private.security.storage.CoreRoutine</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>
 	<true/>
 	<key>com.apple.private.sessionkit.customPushProcessIdentifier</key>

 	<key>com.apple.safetyalerts.spi</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
-	<string>/private/var/db/com.apple.countryd/</string>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/AddressBook/</string>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 		<key>FeatureDiscoverability</key>
 		<dict>
 			<key>Streams</key>
-			<array>
-				<string>App.InFocus</string>
-				<string>AppLaunch</string>
-				<string>Device.Wireless.Bluetooth</string>
-				<string>Discoverability.Signals</string>
-				<string>UserFocusComputedMode</string>
-			</array>
+			<dict>
+				<key>App.InFocus</key>
+				<dict/>
+				<key>AppLaunch</key>
+				<dict/>
+				<key>Device.Wireless.Bluetooth</key>
+				<dict/>
+				<key>Discoverability.Signals</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
 		</dict>
 	</dict>
 	<key>com.apple.private.network.socket-delegate</key>

```
### watchdogd

> `/usr/libexec/watchdogd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.endpoint-security.client</key>
+	<true/>
 	<key>com.apple.diagnosticpipeline.request</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceEndpointSecurityClient</string>
+		<string>kTCCServiceSystemPolicyAllFiles</string>
+	</array>
 	<key>com.apple.private.unblock</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>

```
### wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 	<true/>
 	<key>com.apple.private.wifianalytics.test</key>
 	<true/>
+	<key>com.apple.rapport.RegenerateIdentity</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.WiFiAware</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>com.apple.PineBoardServices</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.rapport</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>
 	<true/>
-	<key>com.apple.private.power.notifications-temp</key>
-	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>mDNSResponder</string>
 	<key>com.apple.private.snhelper</key>

```
