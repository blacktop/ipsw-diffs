## 🔑 Entitlements

### filesystem

### AuthKitUIService

> `/Applications/AuthKitUIService.app/AuthKitUIService`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
+	<key>com.apple.idle-timer-services</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>ProvisioningUniqueDeviceID</string>
 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
 	</array>

 		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
+		<string>com.apple.icloud.findmydeviced</string>
 	</array>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>

```
### SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/hardware/hinge/</string>
 		<string>/private/var/hardware/FactoryData/</string>
 		<string>/private/preboot/</string>
 		<string>/private/var/mobile/Library/Logs/AppleSupport/</string>

```
### DockFolderViewService

> `/Applications/DockFolderViewService.app/DockFolderViewService`

```diff

 	<string>com.apple.DocumentManagerUICore.RecentsAvocado</string>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.diskarbitrationd.access</key>
+	<true/>
 	<key>com.apple.private.librarian.unrestricted-container-access</key>
 	<true/>
 	<key>com.apple.private.pluginkit.persona</key>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.FSEvents</string>
+		<string>com.apple.DiskArbitration.diskarbitrationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### EventViewService

> `/Applications/EventViewService.app/EventViewService`

```diff

 	<true/>
 	<key>com.apple.private.shazamevents.effective_bundle</key>
 	<true/>
+	<key>com.apple.private.sportskit.client</key>
+	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.sportsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.system.opendirectoryd.api</string>

 	<array>
 		<string>com.apple.Home.group</string>
 		<string>com.apple.avfaudio</string>
+		<string>com.apple.homed</string>
 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.voicetrigger.notbackedup</string>

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.system.opendirectoryd.api</string>

 	<array>
 		<string>com.apple.Home.group</string>
 		<string>com.apple.avfaudio</string>
+		<string>com.apple.homed</string>
 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.voicetrigger.notbackedup</string>

```
### InputUI

> `/Applications/InputUI.app/InputUI`

```diff

 	<true/>
 	<key>com.apple.Pasteboard.proxy-paste-authorization</key>
 	<true/>
+	<key>com.apple.Pasteboard.read-concealment</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>

```
### LocalAuthenticationUIService

> `/Applications/LocalAuthenticationUIService.app/LocalAuthenticationUIService`

```diff

 	<array>
 		<string>kern.exclaves_status</string>
 	</array>
+	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>
+	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>collaborations</string>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
+	<key>com.apple.voicememod.client</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.airdrop.client</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

```
### PeopleViewService

> `/Applications/PeopleViewService.app/PeopleViewService`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### PosterBoard

> `/Applications/PosterBoard.app/PosterBoard`

```diff

 	<true/>
 	<key>com.apple.springboard.application-removability.proxy</key>
 	<true/>
+	<key>com.apple.springboard.disableCloseToLock</key>
+	<true/>
 	<key>com.apple.springboard.fetchDisplayConfigs</key>
 	<true/>
 	<key>com.apple.springboard.homeScreenLayout</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.corespeech.corespeechd.xpc</key>
 	<true/>
+	<key>com.apple.corespeech.uitrainingservice</key>
+	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
 	<key>com.apple.developer.ClassKit-environment</key>

 	</dict>
 	<key>com.apple.private.audio.interprocess-tap</key>
 	<true/>
+	<key>com.apple.private.authentication-services.save-passwords-for-any-url</key>
+	<true/>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>

 		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
 		<string>com.apple.ConnectedAudio</string>
 		<string>com.apple.natvoc</string>
+		<string>com.apple.RelevancePlatform.AudioUnderstanding</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.capture-button-restriction</key>
 	<true/>
+	<key>com.apple.springboard.disableCloseToLock</key>
+	<true/>
 	<key>com.apple.springboard.externaldisplay.displayArrangements</key>
 	<true/>
 	<key>com.apple.springboard.focus-modes-home-screen-settings</key>

```
### SIMSetupUIService

> `/Applications/SIMSetupUIService.app/SIMSetupUIService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.bluetooth.discovery</key>
 	<dict>
 		<key>SIMTransfer</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.authentication-services-core.authorization-presenter-client</key>
+	<true/>
 	<key>com.apple.authentication-services.access-credential-identities</key>
 	<true/>
 	<key>com.apple.authentication-services.allow-authentication-request-any-rpid</key>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 	<true/>
 	<key>com.apple.developer.networking.multicast</key>
 	<true/>
+	<key>com.apple.developer.usernotifications.time-sensitive</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>

```
### ServicesPaymentAngel

> `/Applications/ServicesPaymentAngel.app/ServicesPaymentAngel`

```diff

 <dict>
 	<key>adi-client</key>
 	<string>409835401</string>
+	<key>application-identifier</key>
+	<string>com.apple.ServicesPaymentAngel</string>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.appleaccount.identity.read</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.cdp.followup</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.internal.seserviced.ptattestation</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>
 	<true/>
+	<key>com.apple.nfcd.assertion.handover</key>
+	<true/>
+	<key>com.apple.nfcd.assertion.tagreading</key>
+	<true/>
+	<key>com.apple.nfcd.hwmanager</key>
+	<true/>
+	<key>com.apple.nfcd.session.reader.internal</key>
+	<true/>
+	<key>com.apple.nfcd.session.se</key>
+	<true/>
 	<key>com.apple.payment.externalized-context</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

 	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.PassbookUISceneService.remote-ui</string>

 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.seserviced</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
+	<key>com.apple.seserviced.key</key>
+	<true/>
+	<key>com.apple.seserviced.kmlXpcService</key>
+	<true/>
 	<key>com.apple.springboard.biometricUnlockSuppression</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.wallet.banner</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x</string>
 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPad</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.alertItemsSuppression</key>
 	<true/>
+	<key>com.apple.springboard.disableCloseToLock</key>
+	<true/>
 	<key>com.apple.springboard.disallowControlCenter</key>
 	<true/>
 	<key>com.apple.springboard.disallowNotificationCenter</key>

```
### SharingUIService

> `/Applications/SharingUIService.app/SharingUIService`

```diff

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### ShazamEventsApp

> `/Applications/ShazamEventsApp.app/ShazamEventsApp`

```diff

 	<true/>
 	<key>com.apple.private.shazamevents.effective_bundle</key>
 	<true/>
+	<key>com.apple.private.sportskit.client</key>
+	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.sportsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	</array>
 	<key>com.apple.privatecloudcompute.knownRateLimits</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.shortcuts</key>

```
### Siri AI

> `/Applications/Siri AI.app/Siri AI`

```diff

 	</array>
 	<key>com.apple.intelligenceflow.querydecoration</key>
 	<true/>
+	<key>com.apple.intelligenceflow.quota</key>
+	<true/>
 	<key>com.apple.intelligenceflow.toolbox</key>
 	<true/>
 	<key>com.apple.intelligenceflow.transcript-entity-querying</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.intelligenceflow.contextTool</string>
+		<string>com.apple.intelligenceflow.quota</string>
 		<string>com.apple.visualintelligence.visual-action-prediction</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.quicklook.UIExtension.viewservice</string>

```
### SupportFlow

> `/Applications/SupportFlow.app/SupportFlow`

```diff

 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.iphone.axserver-systemwide</string>
 		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.nehelper</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.pearld</string>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.locationd.dynamic_accuracy_reduction</key>
 	<true/>
+	<key>com.apple.locationd.prompt_content_control</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

```
### iCloud+

> `/Applications/iCloud+.app/iCloud+`

```diff

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.surfboard.chrome-customization</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
+		<string>com.apple.iconservices</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

 		<string>com.apple.ClarityUI</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
-		<string>com.apple.mediaaccessibility</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.Accessibility</string>
 		<string>com.apple.Accessibility.Assets</string>
 		<string>com.apple.AssistiveTouch</string>
+		<string>com.apple.mediaaccessibility</string>
 		<string>com.apple.VoiceOverTouch</string>
 		<string>com.apple.ZoomTouch</string>
 	</array>

```
### ClarityBoard

> `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

 	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
+	<key>com.apple.private.biometrickit.allow-bioconvenience</key>
+	<true/>
 	<key>com.apple.private.biometrickit.allow-connect</key>
 	<true/>
 	<key>com.apple.private.biometrickit.allow-default</key>

 		<string>com.apple.backboard.display.services</string>
 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.backboard.system-app-server</string>
+		<string>com.apple.bioconvenienced</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.bulletinboard.observerconnection</string>
 		<string>com.apple.bulletinboard.settingsconnection</string>

```
### MusicKitUI

> `/System/Library/CoreServices/MusicKitUI.app/MusicKitUI`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.in-app-payments</key>

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.itunescloudd.xpc</string>
+		<string>com.apple.pearld</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<false/>
 	<key>com.apple.private.airdrop.settings</key>
 	<true/>
+	<key>com.apple.private.allow-background-haptics</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/SpringBoardIntents.framework</string>

 		<string>SetCapabilities</string>
 		<string>Lookup</string>
 	</array>
+	<key>com.apple.private.mobileobliteration.secure-erase-state</key>
+	<true/>
 	<key>com.apple.private.mobilesafari.searchengine</key>
 	<true/>
 	<key>com.apple.private.mobilestoredemo.enabledemo</key>

 		<string>com.apple.accessibility.MagnifierAngel</string>
 		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.manageddeviced.managed-apps</string>
+		<string>com.apple.mobile.obliteration</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 		<string>com.apple.tuningtargetd</string>
 		<string>com.apple.accessibility.heard</string>
 		<string>com.apple.accessibility.axassetsd</string>
+		<string>com.apple.accessibility.axassetsd.service</string>
 		<string>com.apple.homepod.axserver-systemwide</string>
 		<string>com.apple.accessibility.BrailleTranslation.BrailleTranslationService</string>
 		<string>com.apple.Carousel.wristmonitor</string>

```

### 🆕 AppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/AppReplacementExtension.appex/AppReplacementExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.VoiceShortcuts.AppReplacementExtension</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.siriactionsd.xpc</string>
	</array>
	<key>com.apple.shortcuts.app-replacement</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 AssistantAppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/AssistantAppReplacementExtension.appex/AssistantAppReplacementExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.assistant.domain.preferences.sideappreplacement</key>
	<true/>
	<key>com.apple.assistant.domain.system.settings.access</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.domain.system.settings.service</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
</dict>
</plist>

```

### 🆕 FamilyControlsAppDataMigrationExtension

> `/System/Library/ExtensionKit/Extensions/FamilyControlsAppDataMigrationExtension.appex/FamilyControlsAppDataMigrationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.FamilyControls.private-client</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.FamilyControlsAgent.private</string>
	</array>
</dict>
</plist>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/FedStatsPluginDynamic`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>Safari-Auto-Dark-Mode</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Safari.AutoDarkMode</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Safari-Pop-ups</key>
 		<dict>
 			<key>Streams</key>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/FedStatsPluginStatic`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>Safari-Auto-Dark-Mode</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Safari.AutoDarkMode</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Safari-Pop-ups</key>
 		<dict>
 			<key>Streams</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>GeneratedImageImageGeneration</key>

 	</array>
 	<key>com.apple.privatecloudcompute.knownRateLimits</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ind.xpc</string>
 		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>

```
### MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/MapsIntents`

```diff

 <dict>
 	<key>com.apple.CoreRoutine.LearnedRoute</key>
 	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Maps</string>
 	<key>com.apple.locationd.dynamic_accuracy_reduction</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 	<array>
 		<string>com.apple.Maps.MapsSync.store</string>
 		<string>com.apple.Maps.MapsSync.service</string>
+		<string>com.apple.Maps.MapsSync.cache</string>
 		<string>com.apple.routined.registration</string>
 	</array>
 </dict>

```
### PasscodeAndBiometricsSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasscodeAndBiometricsSettingsAppIntentsExtension.appex/PasscodeAndBiometricsSettingsAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.private.biometrickit.allow-bioconvenience</key>
+	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 </dict>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 		<string>AD_PLATFORMS_APPSTORE_SLP_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_TT_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_PP_INCREMENTALITYAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_SRP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_SLP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_TT_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_PP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
 	</array>
 	<key>fairplay-client</key>
 	<string>1699554724</string>

```
### QuickLookUIExtension

> `/System/Library/ExtensionKit/Extensions/QuickLookUIExtension.appex/QuickLookUIExtension`

```diff

 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.SystemConfiguration.configd</string>
-		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.webinspector</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.mediaanalysisd.analysis</string>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 		<string>AD_PLATFORMS_APPSTORE_SLP_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_TT_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_PP_INCREMENTALITYAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_SRP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_SLP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_TT_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_PP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
 	</array>
 	<key>fairplay-client</key>
 	<string>1699554724</string>

```
### frauddefensepfl

> `/System/Library/ExtensionKit/Extensions/frauddefensepfl.appex/frauddefensepfl`

```diff

 	<string>production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
+		<string>com.apple.pfl.container</string>
+		<string>com.apple.pfl.preprod.container</string>
 		<string>com.apple.priml.dev.container</string>
 		<string>com.apple.priml.preprod.container</string>
 		<string>com.apple.priml.prod.container</string>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 		<string>com.apple.MessageSecurity.MSTimestampXPCService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### LimitedLibraryPickerViewService

> `/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService`

```diff

 		<key>value</key>
 		<string>/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService</string>
 	</dict>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.agentmanager.client.itemStatus</key>
+	<true/>
 	<key>com.apple.private.cascade.donation-requester</key>
 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>

 		<string>com.apple.generativesearch.server.indexing</string>
 		<string>com.apple.corepersonalization.server.graphEmbedding</string>
 		<string>com.apple.generativesearch.server.salientpostings</string>
+		<string>com.apple.agentmanager.server.itemStatus</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Turn</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Conversation</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### FamilyControlsAgent

> `/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent`

```diff

 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>
+	<key>com.apple.private.managed-settings.app-data-migration</key>
+	<true/>
 	<key>com.apple.private.managed-settings.apply</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```

### 🆕 PerceptionLocation

> `/System/Library/LocationBundles/PerceptionLocation.bundle/PerceptionLocation`

- No entitlements *(yet)*
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.akd</string>
+	</array>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.CoreODI</string>
+		<string>group.com.apple.akd</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

```
### contextstored

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.backboard.client</key>

 		<string>com.apple.rapport.people</string>
 		<string>com.apple.private.corewifi.readonly-xpc</string>
 		<string>com.apple.milod.xpc.service</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<string>serverPreferred</string>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
-	<key>com.apple.CoreRoutine.ScenarioTrigger</key>
-	<true/>
 	<key>com.apple.Maps.MapsSync.access</key>
 	<true/>
 	<key>com.apple.Pasteboard.background-access</key>

```
### ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

```diff

 	<string>com.apple.desktopservices.ArchiveService</string>
 	<key>com.apple.fileprovider.fetch-url</key>
 	<true/>
+	<key>com.apple.private.CacheDelete</key>
+	<array>
+		<string>CLIENT_ENTITLEMENT</string>
+		<string>PURGEABLE_ENTITLEMENT</string>
+		<string>PURGE_ENTITLEMENT</string>
+	</array>
 	<key>com.apple.private.QuarantineService.XPC</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.cache_delete</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
 	</array>
 	<key>keychain-access-groups</key>

```

### 🆕 WirelessPerceptionDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/WirelessPerceptionDiagnosticExtension.appex/WirelessPerceptionDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/tmp/com.apple.wirelessperceptiond/</string>
		<string>/private/var/tmp/com.apple.wirelessperceptiond/</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.wirelessperceptiond</string>
</dict>
</plist>

```
### RecentsAvocado

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado`

```diff

 	<string>com.apple.DocumentManagerUICore.RecentsAvocado</string>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.diskarbitrationd.access</key>
+	<true/>
 	<key>com.apple.private.librarian.unrestricted-container-access</key>
 	<true/>
 	<key>com.apple.private.pluginkit.persona</key>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.FSEvents</string>
+		<string>com.apple.DiskArbitration.diskarbitrationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SaveToFiles

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles`

```diff

 	<string>com.apple.DocumentManagerUICore.SaveToFiles</string>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.diskarbitrationd.access</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.librarian.unrestricted-container-access</key>

 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.FSEvents</string>
+		<string>com.apple.DiskArbitration.diskarbitrationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### HealthAgentsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HealthAgents.framework/PlugIns/HealthAgentsDiagnosticExtension.appex/HealthAgentsDiagnosticExtension`

```diff

 	<array>
 		<string>/Library/Caches/com.apple.healthappd/HealthAgents/DiagnosticLogs/</string>
 		<string>/Library/Caches/com.apple.HealthAgents.HealthAgentsTester/HealthAgents/DiagnosticLogs/</string>
+		<string>/Library/Caches/com.apple.healthappd/HealthAgents/RegenCheckHistory/</string>
+		<string>/Library/Caches/com.apple.HealthAgents.HealthAgentsTester/HealthAgents/RegenCheckHistory/</string>
 	</array>
 </dict>
 </plist>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 	<true/>
 	<key>com.apple.TextUnderstanding.SmartReplies.Inference</key>
 	<true/>
+	<key>com.apple.businessservicesd.brandLogo</key>
+	<true/>
 	<key>com.apple.compass.cellular-waypoints.alert</key>
 	<true/>
 	<key>com.apple.compass.cellular-waypoints.availability</key>

 		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.contacts.poster.api</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.businessservicesd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.naturallanguaged/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/purpose_auto/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.public</string>
 		<string>com.apple.TelephonyUtilities</string>
+		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 FileAccessService

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/XPCServices/FileAccessService.xpc/FileAccessService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.fileprovider.fetch-url</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.FileProvider.LocalStorage</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CoreServices.coreservicesd</string>
		<string>com.apple.lsd.mapdb</string>
		<string>com.apple.FileProvider</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.intelligenceflow.intelligenceflowd</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.arkit.camera-access-private-formats.allow</key>

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.assistant.flow_service</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-opus-codec</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<key>com.apple.private.healthkit.authorization_manager</key>
 	<array>
 		<string>read</string>
+		<string>write</string>
 	</array>
 	<key>com.apple.private.healthkit.medicaliddata</key>
 	<true/>

 	</array>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceflow.FileAccessService.XPC</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>Dormancy</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.team6.buddy.peer</string>
+		<string>com.apple.chronoservices</string>
 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.generativelearning</string>
 		<string>com.apple.mediasetupd.server</string>

 		<string>com.apple.CoreAuthentication.agent</string>
 		<string>com.apple.toolkitd.xpc</string>
 		<string>com.apple.siriactionsd.xpc</string>
+		<string>com.apple.assistant.flow_service</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.local-name</key>
+	<array>
+		<string>com.apple.intelligenceflow.FileAccessService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.public</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
+		<string>com.apple.homed.notbackedup</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### intelligenceplatformd

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd`

```diff

 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### journalappd

> `/System/Library/PrivateFrameworks/JournalShared.framework/Support/journalappd`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Journal</string>

 	<array>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.installcoordinationd</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.nehelper</string>
 		<string>com.apple.musicd</string>
 		<string>com.apple.apsd</string>

```
### messagesescrowd

> `/System/Library/PrivateFrameworks/MessagesEscrow.framework/Daemon/messagesescrowd.xpc/messagesescrowd`

```diff

 	<array>
 		<string>/Library/SMS/Escrow/</string>
 		<string>/Library/SMS/Attachments/</string>
+		<string>/Library/SMS/StickerCache/</string>
 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 		<string>com.apple.passd.library</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.FileProvider</string>
+		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### mobiletimerd

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd`

```diff

 	<string>com.apple.mobiletimer</string>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/System/Library/PrivateFrameworks/MobileTimerSupport.framework</string>
+	</array>
 	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
 	<array>
 		<string>com.apple.mobiletimer</string>

 		<string>com.apple.NanoAlarm</string>
 		<string>com.apple.private.NanoTimer</string>
 	</array>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
 	<true/>
 	<key>com.apple.private.appintents.live-entities.write</key>

```
### com.apple.NanoTimeKit.CreateWatchFace

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/com.apple.NanoTimeKit.CreateWatchFace.appex/com.apple.NanoTimeKit.CreateWatchFace`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.NanoTimeKit.CreateWatchFace</string>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
 	<key>com.apple.developer.auto-elect-plugin</key>

 	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.replicator.controller</key>
+	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
 	<key>com.apple.private.security.storage.NanoTimeKit.FaceSupport</key>

 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.nanotimekit.facesupportserver</string>
 		<string>com.apple.photosface</string>
+		<string>com.apple.chronoservices</string>
+		<string>com.apple.replicatorservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Caches/com.apple.businessservicesd/</string>
+		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 	<string>com.apple.amsondevicestoraged</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.applemediaservices.ondevicestorage</string>

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```

### 🆕 PerceptionDiagnosticExtension

> `/System/Library/PrivateFrameworks/PerceptionDaemon.framework/PlugIns/PerceptionDiagnosticExtension.appex/PerceptionDiagnosticExtension`

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
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.mobileslideshow</string>
+		<string>com.apple.ambient</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### privacyaccountingd

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd`

```diff

 	<string>com.apple.privacyaccountingd</string>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.bringUpDaemon</key>
+	<true/>
 	<key>com.apple.private.security.storage.PrivacyAccounting</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.eligibilityd</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.lsd.xpc</string>

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.privatecloudcomputed</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.ind.cloudfeatures</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.CloudSubscriptionFeatures.cache</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>

```
### AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.remotemanagement.AccountSubscriber</string>
+	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
+	<array>
+		<string>AccountTakeover</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.personas.propagate</key>

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.contactsd</string>
+		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>

```
### ManagedStatusSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedStatusSubscriber.xpc/ManagedStatusSubscriber`

```diff

 	<true/>
 	<key>com.apple.private.enhancedloggingd.client</key>
 	<true/>
+	<key>com.apple.private.iokit.battery-shipping-charge-limit</key>
+	<true/>
+	<key>com.apple.private.mobilerepair.shipmode</key>
+	<true/>
 	<key>com.apple.private.mobilerepair.xpc</key>
 	<true/>
 	<key>com.apple.private.remotemanagement.subscriber</key>

 	<array>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.enhancedloggingd.xpc</string>
+		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.managedconfiguration.mdmdservice</string>
 		<string>com.apple.managedconfiguration.mdmuserdservice</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.mobilerepair.shipmode</string>
 		<string>com.apple.mobilerepaird</string>
 		<string>com.apple.remotemanagementd.store</string>
 		<string>com.apple.RemoteManagementAgent.store</string>

```
### SecureMessagingAgent

> `/System/Library/PrivateFrameworks/SecureMessaging.framework/SecureMessagingAgent`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.securemessagingagent</string>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.securemessaging</string>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.tccd</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SiriTTSTrainingAgent

> `/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.audio.AudioComponentRegistrar</string>
+		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
-		<string>com.apple.audio.AudioComponentRegistrar</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.system.opendirectoryd.api</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.apfs.itod.internal</key>
+	<true/>
 	<key>com.apple.apfs.spec_telemetry</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 	<true/>
 	<key>com.apple.private.security.storage.FileProvider</key>
 	<true/>
+	<key>com.apple.private.vfs.unmunged-access-time</key>
+	<true/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### stickersd

> `/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd`

```diff

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.stickers.api</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelmanager</string>

```
### voicebankingd

> `/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/Support/voicebankingd`

```diff

 	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-read-access</key>
 	<true/>
+	<key>com.apple.accessibility.AccessibilityPersonalVoiceAllowSynthesisWhileLocked</key>
+	<true/>
 	<key>com.apple.accessibility.AccessibilityPersonalVoiceUsageOverride</key>
 	<true/>
 	<key>com.apple.accessibility.axassets</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 		<string>Device.Power.BatteryLevel</string>
 		<string>Device.Power.LowPowerMode</string>
 		<string>Device.Power.PluggedIn</string>
+		<string>Device.ScreenLocked</string>
 		<string>Device.Wireless.AirplaneMode</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Device.Wireless.NFCTag</string>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Device.ScreenLocked</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Device.Wireless.AirplaneMode</key>
 				<dict>
 					<key>mode</key>

 	<true/>
 	<key>com.apple.privatecloudcompute.knownRateLimits</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.proactive.ActionPrediction.predictions</key>
 	<true/>
 	<key>com.apple.proactive.AppPrediction.predictions</key>

```
### matd

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/matd`

```diff

 	</array>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.iokit.soc-limit</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>UninstallForLaunchServices</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.privatecloudcompute.knownRateLimits</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.shortcuts</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<array>
 		<string>com.apple.private.alloy.shortcuts</string>
 	</array>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.shortcuts</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 	<true/>
 	<key>com.apple.privatecloudcompute.knownRateLimits</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.shortcuts</key>

 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.ind.xpc</string>
 		<string>com.apple.intelligenceflow.contextTool</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.intelligenceplatform.View</string>

 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.cloud.quota</string>
 		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>

```
### icloudsubscriptionoptimizerd

> `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.icloudsubscriptionoptimizerd</string>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 AppleAccountRUIContent

> `/System/Library/RemoteUI/Plugins/AppleAccountRUIContent.bundle/AppleAccountRUIContent`

- No entitlements *(yet)*
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 		<string>AD_PLATFORMS_APPSTORE_SLP_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_TT_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_PP_INCREMENTALITYAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_SRP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_SLP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_TT_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
+		<string>AD_PLATFORMS_APPSTORE_PP_INCREMENTALITYEXPOSURELOGGINGAPPSTORE</string>
 	</array>
 	<key>fairplay-client</key>
 	<string>1699554724</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 		<string>com.apple.FitnessIntelligence</string>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.conversation-intelligence</string>
+		<string>com.apple.reverie</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.coreaudio</string>
-		<string>com.apple.itunesstored</string>
 		<string>com.apple.NanoRegistry</string>
 		<string>com.apple.mobiletimer</string>
 		<string>com.apple.Bridge</string>

 		<string>com.apple.iBooks</string>
 		<string>com.apple.accessibility.livespeech</string>
 		<string>com.apple.RelevancePlatform.ConsiderateVolume</string>
+		<string>com.apple.RelevancePlatform.AudioUnderstanding</string>
 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.siri.setup</string>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>

 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>

 		<string>com.apple.security.octagon</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.symptom_analytics</string>

 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>

 		<string>com.apple.security.octagon</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.symptom_analytics</string>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>GeneratedImageImageGeneration</key>

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ind.xpc</string>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ind.xpc</string>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>

```
### Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```diff

 	<true/>
 	<key>com.apple.posterboardui.externalEditing</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>GeneratedImageImageGeneration</key>

 	</array>
 	<key>com.apple.privatecloudcompute.knownRateLimits</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ind.xpc</string>
 		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.photos.ImageConversionService</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppleMediaServicesUIDynamicService</string>
+		<string>com.apple.ind.xpc</string>
 		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.stickers.api</string>
 		<string>com.apple.assistant.cdm</string>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	</array>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>AD_PLATFORMS_RN_SEARCH_HOME_RN_AA_TEST</string>
-		<string>AD_PLATFORMS_RN_CORE_SEARCH_RN_AA_TEST</string>
+		<string>AD_PLATFORMS_RN_SEARCH_HOME_RNONDEVICEAATESTFACTOR</string>
+		<string>AD_PLATFORMS_RN_CORE_SEARCH_RNONDEVICEAATESTFACTOR</string>
 		<string>AD_PLATFORMS_APPSTORE_ALL_PLACEMENTS</string>
 		<string>MAPS_SRP_AUTOCOMPLETE</string>
 		<string>2020</string>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>UninstallForLaunchServices</string>
 	</array>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
 	<key>com.apple.private.parsec.default-client</key>

```
### MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.backboardd.proximityDetection</key>
 	<true/>
+	<key>com.apple.businessservicesd.brandLogo</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.asktod</string>
 		<string>com.apple.stickers.recency</string>
+		<string>com.apple.businessservicesd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<true/>
 	<key>com.apple.backboardd.proximityDetection</key>
 	<true/>
+	<key>com.apple.businessservicesd.brandLogo</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.asktod</string>
 		<string>com.apple.stickers.recency</string>
+		<string>com.apple.businessservicesd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authentication-services-core.authorization-presenter-client</key>
+	<true/>
 	<key>com.apple.authentication-services.access-credential-identities</key>
 	<true/>
 	<key>com.apple.authentication-services.allow-authentication-request-any-rpid</key>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.atc.private</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.ageRange</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstored</key>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 	<true/>
 	<key>com.apple.privatecloudcompute.knownRateLimits</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite</key>
 	<true/>
 	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ind.xpc</string>
 		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.coreduetd</string>

```
### PhotosReliveWidget

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget`

```diff

 	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.XPCStoreOptIn</key>

 	<array>
 		<string>/Media/DCIM/</string>
 		<string>/Media/PhotoStreamsData/</string>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
 		<string>com.apple.chronoservices</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Reminders

> `/private/var/staged_system_apps/Reminders.app/Reminders`

```diff

 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.public</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	</array>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.ind.client</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>DataActionsUsecase</key>

 	<true/>
 	<key>com.apple.privatecloudcompute.knownRateLimits</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.proactive.ActionPrediction.predictions</key>
 	<true/>
 	<key>com.apple.proactive.AppPrediction.predictions</key>

 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.ind.xpc</string>
 		<string>com.apple.intelligenceplatform.InternalBiome</string>
 		<string>com.apple.intelligenceplatform.KnowledgeConstruction</string>
 		<string>com.apple.intelligenceplatform.View</string>

 		<string>com.apple.SoundDetection</string>
 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.cloud.quota</string>
 		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>

```
### appleh16camerad

> `/usr/libexec/appleh16camerad`

```diff

 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.private.camera.isp-setfile-load</key>
+	<true/>
 	<key>com.apple.private.cmio.extension.configuration</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/UserConfigurationProfiles/</string>
+		<string>/private/var/mobile/Library/studentd/isLockedToMultipleApps</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/WebClips/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### atc

> `/usr/libexec/atc`

```diff

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>com.apple.voicememod.client</key>
+	<true/>
 	<key>fairplay-client</key>
 	<integer>177554772</integer>
 	<key>keychain-access-groups</key>

```
### audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

 	<array>
 		<string>com.apple.MobileAsset.AudioAnalytics</string>
 	</array>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.coreaudio</string>
 	<key>com.apple.private.biome.writer</key>

 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.ctcategories.service</string>
 		<string>com.apple.account.AppleAccount</string>
+		<string>com.apple.backlightd</string>
+		<string>com.apple.AttentionAwareness</string>
+		<string>com.apple.iohideventsystem</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 bioconvenienced

> `/usr/libexec/bioconvenienced`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.keystore.convenience-bio</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.mkb.usersession.info</key>
	<true/>
	<key>com.apple.perceptiond.access</key>
	<dict>
		<key>perception</key>
		<true/>
	</dict>
	<key>com.apple.private.exclaves.conclave-host</key>
	<true/>
</dict>
</plist>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.linkd.registry</key>

```
### conversationd

> `/usr/libexec/conversationd`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.RelevancePlatform.AudioUnderstanding</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.demo-settings</string>
 	</array>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.batteryintelligenced.thermalprediction-read</key>
+	<true/>
 	<key>com.apple.bulletinboard.dataprovider</key>
 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>

 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
+	<key>com.apple.powerui.smartcharging</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>PURGEABLE_ENTITLEMENT</string>

 		<string>com.apple.griddatad.registration</string>
 		<string>com.apple.biome.ContextSync</string>
 		<string>com.apple.biomesyncd.sync</string>
+		<string>com.apple.batteryintelligenced.thermalprediction</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>COREOS_DAS</string>
 		<string>COREOS_APRS</string>
 		<string>COREOS_CLAS</string>
+		<string>COREOS_DRM_APRS</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### demod

> `/usr/libexec/demod`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.FileIndexer.client</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.ignoreRestrictions</key>

```
### demod_helper

> `/usr/libexec/demod_helper`

```diff

 	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
+	<key>com.apple.private.applesmc.user-access</key>
+	<true/>
 	<key>com.apple.private.iokit.ddl-write</key>
 	<true/>
 	<key>com.apple.private.security.datavault.controller</key>

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>
+		<string>AppleSMCClient</string>
 	</array>
 	<key>com.apple.security.system-container</key>
 	<true/>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 	<true/>
 	<key>com.apple.developer.media-device-discovery-extension</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents.media-client-id</key>

```
### diagnosticscheckupd

> `/usr/libexec/diagnosticscheckupd`

```diff

 	<true/>
 	<key>com.apple.developer.pluginkit.provide-environment</key>
 	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SysCfg</string>

 	</array>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.corerepair.attestation</key>
+	<true/>
+	<key>com.apple.private.corerepair.diagnostics-delegate</key>
+	<true/>
+	<key>com.apple.private.corerepair.xpc</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.diagnosticscheckupd</string>

```
### dietappleh16camerad

> `/usr/libexec/dietappleh16camerad`

```diff

 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.private.camera.isp-setfile-load</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### icloudmailagent

> `/usr/libexec/icloudmailagent`

```diff

 	<array>
 		<string>com.apple.kvsd</string>
 		<string>com.apple.apsd</string>
+		<string>com.apple.mediaanalysisd.service.public</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<true/>
 	<key>com.apple.backboardd.displayTraits</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.feedbackd.remote-evaluation</key>

```
### managedappsd

> `/usr/libexec/managedappsd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.devicemanagementclient.managedappsd</string>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.ManagedApps</string>
+	</array>
+	<key>com.apple.private.device-configuration.provider.allowed-provider-ids</key>
+	<array>
+		<string>com.apple.ManagedApps</string>
+	</array>
 	<key>com.apple.private.remotemanagement.subscriber</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	<array>
 		<string>/private/var/Managed Preferences/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.deviceconfigurationd.consumer</string>
+		<string>com.apple.deviceconfigurationd.consumer.async</string>
+		<string>com.apple.deviceconfigurationd.publisher</string>
+		<string>com.apple.deviceconfigurationd.provider</string>
+		<string>com.apple.deviceconfigurationd.provider.async</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.devicemanagementclient.managedappsd</string>
 	</array>
 	<key>com.apple.security.system-container</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.configurationprofiles</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<array>
 		<string>com.apple.devicemanagementclient.managedappsd</string>

```
### mediasetupd

> `/usr/libexec/mediasetupd`

```diff

 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.userprofiles</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.home</string>
+	</array>
 	<key>com.apple.symptom_analytics.diagnostics</key>
 	<true/>
 	<key>com.apple.symptom_analytics.query</key>

```
### mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 	<true/>
 	<key>com.apple.private.corerepair.xpc</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.CoreRepair</string>
+	</array>
 	<key>com.apple.private.exclaves.conclave-host</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<true/>
 	<key>com.apple.private.iokit.batteryhealthstate</key>
 	<true/>
+	<key>com.apple.private.mobilerepair.shipmode</key>
+	<true/>
 	<key>com.apple.private.security.AppleImage4.user-client</key>
 	<true/>
 	<key>com.apple.private.security.bootpolicy</key>

 		<string>com.apple.ctkd.token-client</string>
 		<string>com.apple.ctkd</string>
 		<string>com.apple.devicedatareset.DeviceDataResetService</string>
+		<string>com.apple.deviceconfigurationd.consumer</string>
+		<string>com.apple.mobilerepair.shipmode</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

```
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.activityprogress.activityprogressui.services</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>security.codesigning.config</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```
### ospredictiond

> `/usr/libexec/ospredictiond`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
+	<key>com.apple.das.private.usagepriorities</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Activity.Level</string>
+		<string>App.InFocus</string>
 		<string>Device.Power.PluggedIn</string>
 		<string>NowPlaying</string>
 		<string>Device.ScreenLocked</string>

 				<string>Activity.Level</string>
 			</array>
 		</dict>
+		<key>OSPersonalizedScheduling</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>

```

### 🆕 perceptiond

> `/usr/libexec/perceptiond`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.perceptiond</string>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.bannerkit.post</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.CanRecordWithoutSessionActivation</key>
	<true/>
	<key>com.apple.corespeech.corespeechd.xpc</key>
	<true/>
	<key>com.apple.corespeech.supportheysiriwhenrecord</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.EmbeddedSpeech</string>
		<string>com.apple.MobileAsset.SpeechEndpointAssetsTV</string>
		<string>com.apple.MobileAsset.SpeakerRecognitionAssets</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsTV</string>
	</array>
	<key>com.apple.private.avfoundation.background-camera-access</key>
	<true/>
	<key>com.apple.private.avfoundation.capture.allow</key>
	<true/>
	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
	<true/>
	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>
	<true/>
	<key>com.apple.private.breadboard.ambient-sensing.read</key>
	<true/>
	<key>com.apple.private.breadboard.privacy.read</key>
	<true/>
	<key>com.apple.private.cmcapture.frame-receiver</key>
	<true/>
	<key>com.apple.private.exclaves.conclave-host</key>
	<true/>
	<key>com.apple.private.isolated.audio.coreaudioclient.shareddsp</key>
	<true/>
	<key>com.apple.private.mediaexperience.usesecuresession</key>
	<true/>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMicrophone</string>
	</array>
	<key>com.apple.private.userprofiles.read</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/</string>
		<string>/private/var/mobile/tmp/com.apple.audiomxd/AudioCapture/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AGXDeviceUserClient</string>
		<string>AppleJPEGDriverUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelDevice</string>
		<string>IOSurfaceRootUserClient</string>
		<string>IOSurfaceAcceleratorClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.modelmanager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.natvoc</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>kern.exclaves_status</string>
		<string>kern.task_conclave</string>
		<string>kern.bootargs</string>
	</array>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.security.ts.render-images</key>
	<true/>
	<key>com.apple.sigmon.producer</key>
	<array>
		<string>/Perception/AmbientLight</string>
		<string>/Perception/PerceivedPeople</string>
	</array>
	<key>com.apple.siri</key>
	<true/>
	<key>com.apple.siri.activation</key>
	<true/>
	<key>com.apple.siri.activation.service</key>
	<true/>
	<key>com.apple.siri.speakerprofile.embedding.service.xpc</key>
	<true/>
</dict>
</plist>

```
### powerexperienced

> `/usr/libexec/powerexperienced`

```diff

 			<dict/>
 		</dict>
 	</dict>
+	<key>com.apple.batteryintelligenced.thermalprediction-read</key>
+	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
 	<key>com.apple.locationd.asmanager</key>

 	<true/>
 	<key>com.apple.powerd.extendedbattery</key>
 	<true/>
+	<key>com.apple.powerui.smartcharging</key>
+	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
 	<key>com.apple.private.clpc.policy</key>

 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.OSIntelligence.battery</string>
 		<string>com.apple.powerd.extendedbattery</string>
+		<string>com.apple.batteryintelligenced.thermalprediction</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 		<string>AD_PLATFORMS_APPSTORE_SRP_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_TT_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_PP_INCREMENTALITYAPPSTORE</string>
-		<string>AD_PLATFORMS_RN_CORE_SEARCH_RN_AA_TEST</string>
-		<string>AD_PLATFORMS_RN_SEARCH_HOME_RN_AA_TEST</string>
+		<string>AD_PLATFORMS_RN_CORE_SEARCH_RNONDEVICEAATESTFACTOR</string>
+		<string>AD_PLATFORMS_RN_SEARCH_HOME_RNONDEVICEAATESTFACTOR</string>
 		<string>AD_PLATFORMS_APPSTORE_SLP_ADEVENTKIT</string>
 		<string>AD_PLATFORMS_APPSTORE_SRP_ADEVENTKIT</string>
 		<string>AD_PLATFORMS_APPSTORE_TT_ADEVENTKIT</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.continuitycapture.capabilities</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmapbundleidtouuid</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.ApplicationService.ServiceDiscovery</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.continuitycaptured.capabilities</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### remoted

> `/usr/libexec/remoted`

```diff

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>CoalescedTargetProperties</string>
 		<string>EthernetMacAddress</string>
 		<string>SerialNumber</string>
 		<string>UniqueChipID</string>

```
### routined

> `/usr/libexec/routined`

```diff

 	<array>
 		<string>AppLaunch</string>
 		<string>AppIntent</string>
+		<string>Device.BootSession</string>
+		<string>Device.Power.BatteryLevel</string>
 		<string>Device.Power.PluggedIn</string>
 		<string>Device.ScreenLocked</string>
 		<string>Device.Wireless.WiFi</string>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 		<string>com.apple.imessage.bag</string>
 		<string>com.apple.AppSupport.plist</string>
 		<string>com.apple.stockholm</string>
+		<string>com.apple.purplebuddy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.security.ts.identity-services-client</key>
 	<true/>
+	<key>com.apple.security.ts.ipc-posix-sem</key>
+	<string>purplebuddy.sentinel</string>
 	<key>com.apple.security.ts.power-assertions</key>
 	<true/>
 	<key>com.apple.security.ts.read-factory-files</key>

```
### sportsd

> `/usr/libexec/sportsd`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.activityAuthorizer</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.watchlistd.xpc</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>

```
### spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.agentmanager.client.itemStatus</key>
+	<true/>
 	<key>com.apple.private.cascade.donation-requester</key>
 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>

 		<string>com.apple.generativesearch.server.indexing</string>
 		<string>com.apple.corepersonalization.server.graphEmbedding</string>
 		<string>com.apple.generativesearch.server.salientpostings</string>
+		<string>com.apple.agentmanager.server.itemStatus</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Turn</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Conversation</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.agentmanager.client.itemStatus</key>
+	<true/>
 	<key>com.apple.private.cascade.donation-requester</key>
 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>

 		<string>com.apple.generativesearch.server.indexing</string>
 		<string>com.apple.corepersonalization.server.graphEmbedding</string>
 		<string>com.apple.generativesearch.server.salientpostings</string>
+		<string>com.apple.agentmanager.server.itemStatus</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Turn</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Conversation</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### textunderstandingd

> `/usr/libexec/textunderstandingd`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.privatecloudcompute</string>
+		<string>com.apple.linkd.application-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<array>
 		<string>/Applications/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 		<string>/private/var/preferences/SystemConfiguration/com.apple.wifi.plist</string>
 		<string>/usr/libexec/</string>
 	</array>

```

### 🆕 wirelessperceptiond

> `/usr/libexec/wirelessperceptiond`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.networking.wifi-info</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.wirelessperceptiond</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>WirelessPerception.MotionDetection:subscriptions</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>WirelessPerception.MotionDetection</string>
	</array>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.corewifi.NDD.setter</key>
	<true/>
	<key>com.apple.private.corewifi.blockedbands.setter</key>
	<true/>
	<key>com.apple.private.corewifi.bssid</key>
	<true/>
	<key>com.apple.private.corewifi.companioncountrycode.setter</key>
	<true/>
	<key>com.apple.private.corewifi.countrycode</key>
	<true/>
	<key>com.apple.private.corewifi.internal</key>
	<true/>
	<key>com.apple.private.corewifi.mac-addr</key>
	<true/>
	<key>com.apple.private.corewifi.readonly</key>
	<true/>
	<key>com.apple.private.managedclient.configurationprofiles</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>AirPort</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>RootDomainUserClient</string>
		<string>AppleSPUUserClient</string>
		<string>IOHIDLibUserClient</string>
		<string>IOSurfaceRootUserClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>AGXDeviceUserClient</string>
		<string>AppleSMCClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.wirelessperception.session</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.wirelessperception</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<string>WirelessPerception</string>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>com.apple.wirelessperception.session</key>
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
### appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.private.camera.isp-setfile-load</key>
+	<true/>
 	<key>com.apple.private.cmio.extension.configuration</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>

```
### dietappleh16camerad

> `/usr/sbin/dietappleh16camerad`

```diff

 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.private.camera.isp-setfile-load</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```


