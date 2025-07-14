## 🔑 Entitlements

### CameraMessagesApp

> `/Applications/Camera.app/PlugIns/CameraMessagesApp.appex/CameraMessagesApp`

```diff

 	<string>com.apple.camera.CameraMessagesApp</string>
 	<key>checklessPersistentURLTranslation</key>
 	<true/>
+	<key>com.apple.PencilKit.allowsSnapToShape</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

```
### ClarityPhotos

> `/Applications/ClarityPhotos.app/ClarityPhotos`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.ClarityUI.Photos</string>
 	</array>

```
### ContactPhotoCarouselRemoteAlert

> `/Applications/ContactPhotoCarouselRemoteAlert.app/ContactPhotoCarouselRemoteAlert`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CheckerBoard</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.AppleServiceToolkit</string>
 		<string>diagnosticextensionsd</string>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.private.feature-a</key>
+	<true/>
 	<key>com.apple.springboard.setVoiceControlEnabled</key>
 	<true/>
 	<key>com.apple.springboard.setWantsLockButtonEvents</key>

```
### DiagnosticsReporter

> `/Applications/DiagnosticsReporter.app/DiagnosticsReporter`

```diff

 	</array>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.surfboard.chrome-customization</key>
+	<true/>
 </dict>
 </plist>
 

```
### Diagnostic-4615

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4615.appex/Diagnostic-4615`

```diff

 	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
-		<string>AppleAuthCP</string>
 		<string>IOAccessoryManagerUserClient</string>
 		<string>AppleAuthCPUserClient</string>
-		<string>AppleBasebandUserClient</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.systemstatus</string>
 	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>

```
### Diagnostic-7004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004`

```diff

 	<true/>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
-	<key>com.apple.private.corerepair.allow-job-control</key>
-	<array>
-		<string>com.apple.appleh16camerad</string>
-	</array>
 	<key>com.apple.private.corerepair.xpc</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.corerepair</string>
 		<string>com.apple.diskimagecorerepair</string>
+		<string>com.apple.appleh13camerad</string>
 		<string>com.apple.appleh16camerad</string>
 	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>

```
### Family

> `/Applications/Family.app/Family`

```diff

 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
+	<key>com.apple.surfboard.sharing-mode-launch-allowed</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>511712240</string>
 	<key>keychain-access-groups</key>

```

### 🆕 FinanceStub

> `/Applications/FinanceStub.app/FinanceStub`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.FinanceStub</string>
	<key>com.apple.developer.associated-domains</key>
	<array/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.Passbook</string>
	</dict>
	<key>com.apple.private.swc.system-app</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.openurlinbackground</key>
	<true/>
</dict>
</plist>

```
### HealthPrivacyService

> `/Applications/HealthPrivacyService.app/HealthPrivacyService`

```diff

 		<string>write</string>
 		<string>reset</string>
 	</array>
+	<key>com.apple.private.healthkit.reality</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### RemotePeoplePicker

> `/Applications/InCallService.app/PlugIns/RemotePeoplePicker.appex/RemotePeoplePicker`

```diff

 <dict>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.QuartzCore.global-capture</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.people</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.runningboard.posterkit.host</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>

 	</array>
 	<key>com.apple.sharesheet.recipients</key>
 	<true/>
+	<key>com.apple.springboard.topButtonFrames</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### MailCompositionService

> `/Applications/MailCompositionService.app/MailCompositionService`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

```
### MediaRemoteUI

> `/Applications/MediaRemoteUI.app/MediaRemoteUI`

```diff

 	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.mediaremote.allow</key>
 	<array>
 		<string>TVPairing</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.itunescloudd.xpc</string>
+		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.coremedia.endpointpicker.xpc</string>
 		<string>com.apple.coremedia.routediscoverer.xpc</string>
 		<string>com.apple.coremedia.routingcontext.xpc</string>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.mediaremote.allow</key>
 	<array>
 		<string>TVPairing</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.itunescloudd.xpc</string>
+		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.carkit.service</string>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.bulletinboard.utilities</key>
 	<true/>
+	<key>com.apple.clarityboard.chromeVisibility</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.private.ids.idquery-cache</key>
 	<true/>
+	<key>com.apple.private.ids.report-spam-message</key>
+	<true/>
 	<key>com.apple.private.imavcore.imavagent</key>
 	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

 		<string>com.apple.voicemail.vmd</string>
 		<string>com.apple.datamigrator</string>
 		<string>com.apple.transparencyd</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 	</array>
 	<key>com.apple.TextUnderstanding.SmartReplies.Inference</key>
 	<true/>
+	<key>com.apple.activityawardsd</key>
+	<true/>
 	<key>com.apple.appstored.install-apps</key>
 	<true/>
 	<key>com.apple.appstored.xpc.updates</key>

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.clarityboard.chromeVisibility</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>

 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.stickers.api</string>
 		<string>com.apple.passd.device-registration</string>
+		<string>com.apple.activityawardsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MusicUIService

> `/Applications/MusicUIService.app/MusicUIService`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.itunescloudd.xpc</string>
+		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.neighborhood-activities</string>

```
### PCViewService

> `/Applications/PCViewService.app/PCViewService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.mediaremote.device-info</key>
 	<true/>
 	<key>com.apple.mediaremote.remote-control-discovery</key>
 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>com.apple.iohideventsystem</string>
 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.iphone.axserver-systemwide</string>
+		<string>com.apple.itunescloud.contenttaste</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.locationd.registration</string>

```
### PeopleViewService

> `/Applications/PeopleViewService.app/PeopleViewService`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
+	<key>com.apple.private.security.storage.coreduet_knowledge_store</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceWillow</string>
 	</array>
-	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.people</string>

```
### PeopleWidget_iOSExtension

> `/Applications/PeopleViewService.app/PlugIns/PeopleWidget_iOSExtension.appex/PeopleWidget_iOSExtension`

```diff

 	<array/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
-	<key>com.apple.findmy.findmylocate.friendshipservice</key>
-	<true/>
-	<key>com.apple.findmy.findmylocate.locationservice</key>
-	<true/>
-	<key>com.apple.findmy.findmylocate.settings</key>
-	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 		<string>com.apple.icloud.searchpartyd.securelocations</string>
 		<string>com.apple.people.agent</string>
 		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.findmy.findmylocate.friendshipservice</string>
-		<string>com.apple.findmy.findmylocate.locationservice</string>
-		<string>com.apple.findmy.findmylocate.settings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### PosterBoard

> `/Applications/PosterBoard.app/PosterBoard`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/DuetExpertCenter/caches/SuggestedModeFaces/</string>
+		<string>/Library/Caches/com.apple.chrono/snapshot-cache/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.excludes-extensions</key>
+	<true/>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.link-extension</string>

 	<true/>
 	<key>com.apple.mobilemail.mailservices</key>
 	<true/>
+	<key>com.apple.momentsd.internal</key>
+	<array>
+		<string>MOUserNotifications</string>
+		<string>MOOnboardingAndSettings</string>
+	</array>
 	<key>com.apple.multitasking.termination</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.pairunpairobliterate</key>

 		<string>com.apple.eyereliefd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
-	<string>com.apple.springboard</string>
+	<array>
+		<string>com.apple.springboard</string>
+		<string>com.apple.momentsd</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>kCFPreferencesAnyApplication</string>

 		<string>IOSurfaceRootUserClient</string>
 		<string>RootDomainUserClient</string>
 	</array>
+	<key>com.apple.security.lockdownmode.read</key>
+	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```
### ReplayKitAngel

> `/Applications/ReplayKitAngel.app/ReplayKitAngel`

```diff

 	<array>
 		<string>com.apple.sessionservices</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<string>com.apple.replayd</string>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>

```
### ScreenTimeWidgetExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension`

```diff

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.accountsd.accountmanager</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.DeviceActivity</string>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 		<string>com.apple.identities</string>
 		<string>com.apple.mobilesafari</string>
 		<string>com.apple.Sharing</string>
+		<string>com.apple.sharing.appleidauthentication</string>
 		<string>com.apple.VideoSubscriberAccount</string>
 		<string>lockdown-identities</string>
 	</array>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>bundleID</string>
+		<string>path</string>
 		<key>value</key>
-		<string>com.apple.shortcuts</string>
+		<string>/Applications/ShortcutsUI.app/ShortcutsUI</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>bundleID</string>
+		<string>path</string>
 		<key>value</key>
-		<string>com.apple.shortcuts</string>
+		<string>/Applications/ShortcutsViewService.app/ShortcutsViewService</string>
 	</dict>
 	<key>com.apple.private.corerecents</key>
 	<true/>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 		<string>/private/var/mobile/tmp/com.apple.WorkflowKit.BackgroundShortcutRunner/</string>
 		<string>/private/var/mobile/tmp/SiriMessages/</string>
 		<string>/private/var/mobile/Media/</string>
-		<string>/private/var/mobile/Containers/Shared/AppGroup/</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/Assistant/SpeechLogs/</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/VoiceTrigger/</string>
 		<string>/private/var/containers/Bundle/Application/</string>

```
### TDGSharingViewService

> `/Applications/TDGSharingViewService.app/TDGSharingViewService`

```diff

 		<string>com.apple.cdp.statemachine</string>
 		<string>com.apple.corefollowup.agent</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.TDGSharingViewServiceCompanion</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>

```
### VideoSubscriberAccountViewService

> `/Applications/VideoSubscriberAccountViewService.app/VideoSubscriberAccountViewService`

```diff

 	<true/>
 	<key>com.apple.appletv.pbs.allow-purge-topshelf</key>
 	<true/>
+	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.backboardd.launchapplications</key>

```
### WebSheet

> `/Applications/WebSheet.app/WebSheet`

```diff

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.surfboard.always-discard-last-scene</key>
+	<true/>
+	<key>com.apple.surfboard.scenesession-custom-focus-order</key>
+	<integer>1001</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.cfnetwork</string>

```
### iCloud+

> `/Applications/iCloud+.app/iCloud+`

```diff

 	<true/>
 	<key>com.apple.private.accounts.bundleidspoofing</key>
 	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.private.mediaexperience.suppressrecordingstatetosystemstatus</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.systemauthenticationstate.allow</key>
+	<true/>
 	<key>com.apple.private.replay-kit</key>
 	<true/>
 	<key>com.apple.private.rtcreportingd</key>

 	<true/>
 	<key>com.apple.runningboard.AccessibilityUIServer</key>
 	<true/>
+	<key>com.apple.runningboard.VoiceOver</key>
+	<true/>
 	<key>com.apple.runningboard.accessibility</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 		<string>com.apple.Accessibility.SwitchControl</string>
 		<string>com.apple.Accessibility</string>
 	</array>
+	<key>com.apple.runningboard.VoiceOver</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/</string>

```
### ClarityBoard

> `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/preferences/com.apple.networkd.plist</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 		<string>com.apple.HearingApp</string>
 		<string>com.apple.findmylocaldevice</string>
 		<string>com.apple.intelligentroutingd.xpc.media</string>
+		<string>com.apple.itunescloud.contenttaste</string>
+		<string>com.apple.itunescloudd.xpc</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<array>
 		<string>com.apple.VoiceOverNotifications</string>
 	</array>
+	<key>com.apple.runningboard.VoiceOver</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/Assets/com_apple_MobileAsset_VoiceServices_VoiceResources/</string>

```

### 🆕 MapsTransactionInsightsExtension

> `/System/Library/ExtensionKit/Extensions/MapsTransactionInsightsExtension.appex/MapsTransactionInsightsExtension`

- No entitlements *(yet)*
### com.apple.mlhost.CloudWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
-	<key>com.apple.mlhost.client-entitlement</key>
-	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.mlhost.configRead</key>
+	<true/>
+	<key>com.apple.private.mlhost.taskRead</key>
+	<true/>
+	<key>com.apple.private.mlhost.taskWrite</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 	<array>
 		<string>com.apple.mlhost</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.mlhostd.xpc</string>
+		<string>com.apple.cloudd</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.mlhost</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 com.apple.mlhost.QuartzWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.QuartzWorker.appex/com.apple.mlhost.QuartzWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mlhost.QuartzWorker</string>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.access</key>
	<array/>
	<key>com.apple.private.healthkit.read_authorization_bypass</key>
	<array>
		<string>HKQuantityTypeIdentifierVO2Max</string>
		<string>HKQuantityTypeIdentifierRestingHeartRate</string>
		<string>HKQuantityTypeIdentifierHeartRateVariabilitySDNN</string>
		<string>HKWorkoutTypeIdentifier</string>
		<string>HKQuantityTypeIdentifierDistanceWalkingRunning</string>
		<string>HKQuantityTypeIdentifierActiveEnergyBurned</string>
		<string>HKQuantityTypeIdentifierAppleExerciseTime</string>
		<string>HKQuantityTypeIdentifierAppleMoveTime</string>
		<string>HKQuantityTypeIdentifierAppleStandTime</string>
		<string>HKQuantityTypeIdentifierNumberOfTimesFallen</string>
		<string>HKCategoryTypeIdentifierMindfulSession</string>
		<string>HKQuantityTypeIdentifierTimeInDaylight</string>
		<string>HKCategoryTypeIdentifierSleepAnalysis</string>
		<string>HKCategoryTypeIdentifierSleepChanges</string>
		<string>HKQuantityTypeIdentifierHeartRate</string>
		<string>HKQuantityTypeIdentifierStepCount</string>
		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
		<string>HKQuantityTypeIdentifierBodyMass</string>
		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
		<string>HKQuantityTypeIdentifierHeight</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.lighthouse.quartz</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.lighthouse.quartz</string>
	</array>
	<key>com.apple.security.ts.application-group-support</key>
	<true/>
</dict>
</plist>

```
### com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.lighthouse.SampleWorker</string>
+	<string>com.apple.mlhost.SampleWorker</string>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.MLHostTask</string>
+	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
+	<key>com.apple.private.assets.change-daemon-config</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.mobileasset.autoasset</string>
+	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.mobileasset.autoasset</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.mlhost.TelemetryWorker</string>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskTelemetry</string>
+		<string>Lighthouse.Ledger.DeviceTelemetry</string>
+	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>MLHostTelemetry</key>

 	<array>
 		<string>com.apple.mlhost</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
+	</array>
 	<key>com.apple.security.ts.application-group-support</key>
 	<true/>
 </dict>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.appleaccount.appleaccount-delete</key>
 	<true/>
-	<key>com.apple.appleaccount.sign-out</key>
+	<key>com.apple.appleidsetup.signout</key>
 	<true/>
 	<key>com.apple.appletv.pbs.user-profiles.account-notification</key>
 	<true/>

```
### ContactViewViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### ContactsViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```

### 🆕 ccportrait_builtins_archive_bin.metallib

> `/System/Library/Frameworks/CoreImage.framework/ccportrait_builtins_archive_bin.metallib`

- No entitlements *(yet)*
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.apfs.key_migration</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.BifrostCodecs</string>

 		<string>IOAppleConvergedIPCBBControlUserClient</string>
 		<string>AppleCellularDataPlaneUserClient</string>
 		<string>AppleSARServiceUserClient</string>
+		<string>AppleAPFSUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	<string>com.apple.fileprovider.fileproviderd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.assertiond.app-state-monitor</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
+	<key>com.apple.osanalytics.otatasking-service-access</key>
+	<true/>
 	<key>com.apple.private.ArchiveService.XPC</key>
 	<true/>
 	<key>com.apple.private.CacheDelete</key>

 		<string>com.apple.rtcreportingd</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.OTATaskingAgent</string>
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
+	<key>com.apple.financekit.financial-insights.host</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.passd.library</string>
+		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.frontboard.systemappservices</string>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>

```
### coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.securestore.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.securestore.dsl.allow</key>
+	<true/>
+	<key>com.apple.private.applecredentialmanager.securestore.dsl.enable.allow</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.securestore.macbuddy.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.securestore.ratchet.reset.allow</key>
+	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmapbundleidtouuid</key>

 	<array>
 		<string>com.apple.coreauthd</string>
 	</array>
+	<key>com.apple.security.ts.read-any-bundle</key>
+	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.home-hint-suppression</key>

```
### TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

 	<string>com.apple.TrustedPeersHelper</string>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.TrustedPeersHelper</string>
 	<key>com.apple.developer.aps-environment</key>

 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.security.sfkeychainserver</string>
 		<string>com.apple.securityd</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>

```
### DeviceActivityReportService

> `/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.DeviceActivity</string>

```

### 🆕 WGAEltonUsersSettingsPhone

> `/System/Library/NanoPreferenceBundles/General/WGAEltonUsersSettingsPhone.bundle/WGAEltonUsersSettingsPhone`

- No entitlements *(yet)*

### 🆕 WGAEltonPhoneBuddyFlowPanel

> `/System/Library/NanoPreferenceBundles/SetupBundles/WGAEltonPhoneBuddyFlowPanel.bundle/WGAEltonPhoneBuddyFlowPanel`

- No entitlements *(yet)*

### 🆕 WGAEltonPreferencesSyncPhone

> `/System/Library/PreferencesSyncBundles/WGAEltonPreferencesSyncPhone.bundle/WGAEltonPreferencesSyncPhone`

- No entitlements *(yet)*
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler`

```diff

 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>bundleID</string>
+		<string>path</string>
 		<key>value</key>
-		<string>com.apple.shortcuts</string>
+		<string>/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns//BundledIntentHandler.appex/BundledIntentHandler</string>
 	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 		<string>/private/var/mobile/Library/Trial/Treatments/1100/</string>
 		<string>/private/var/mobile/Library/Trial/Treatments/1101/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/var/tmp/tailspins/siri/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Trial/Treatments/351/</string>

 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.suggestd.events</string>
 		<string>com.apple.proactive.PersonalizationPortrait.QuickType</string>
+		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>
+		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.remindd.userInteractive</string>
 		<string>com.apple.sysdiagnose.service.xpc</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>

 		<string>com.apple.carpd.xpc</string>
 		<string>com.apple.caraccessoryframework.gatekeeper</string>
 		<string>com.apple.sirittsd</string>
+		<string>com.apple.tailspind</string>
 		<string>com.apple.coreduetd.batterysaver</string>
 		<string>com.apple.powerd.lowpowermode</string>
 		<string>com.apple.backlightd</string>

 	<true/>
 	<key>com.apple.synapse.notes-activation-service</key>
 	<true/>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

 		<string>756</string>
 		<string>757</string>
 		<string>401</string>
+		<string>406</string>
 		<string>1630</string>
 		<string>1327</string>
 		<string>1328</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>SIRI_REFERENCE_RESOLUTION_LIGHTHOUSE_PLUGIN</string>
 		<string>SIRI_REFERENCE_RESOLUTION_LIGHTHOUSE_PLUGIN_FOR_SHADOW_LOGGING</string>
 		<string>SIRI_SPEECH_SV_SPEECH_PROFILE</string>
+		<string>SIRI_SUGGESTIONS_PLATFORM</string>
 		<string>SIRI_UI_RESPONSES_SETTINGS</string>
 		<string>SIRI_UNDERSTANDING_CLASSIC_DEPRECATION</string>
 		<string>SIRI_UNDERSTANDING_NL</string>

```
### BiomeWriteService

> `/System/Library/PrivateFrameworks/BiomeStorage.framework/XPCServices/BiomeWriteService.xpc/BiomeWriteService`

```diff

 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.compute.source.user</string>
+		<string>com.apple.biome.compute.source</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.biomed</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.biomed</string>
 	<key>com.apple.intelligenceplatform.IntelligencePlatformComputeService</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.private.chrono-extension-host</key>
 	<true/>
+	<key>com.apple.private.coreaudio.initiatetemporarybackgroundplayback.allow</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 	<array>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
-		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### CipherMLService

> `/System/Library/PrivateFrameworks/CipherML.framework/XPCServices/CipherMLService.xpc/CipherMLService`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
+	<key>com.apple.security.network.client</key>
+	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
+	<key>platform-application</key>
+	<true/>
+</dict>
+</plist>
 

```
### contextstored

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored`

```diff

 		<dict>
 			<key>Streams</key>
 			<array>
+				<string>App.InFocus</string>
+				<string>FrontBoard.DisplayElement</string>
+				<string>GameController.Connected</string>
 				<string>Location.MicroLocation.Localization</string>
+				<string>Location.PointOfInterest.Category</string>
+				<string>Location.Semantic</string>
+				<string>Screen.Recording</string>
 				<string>Screen.Sharing</string>
+				<string>UserFocus.ComputedMode</string>
+				<string>UserFocus.DoNotDisturbWhileDriving</string>
+				<string>UserFocus.InferredMode</string>
+				<string>UserFocus.SleepMode</string>
 			</array>
 		</dict>
 	</dict>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

 	<true/>
 	<key>com.apple.aned.private.processModelShare.allow</key>
 	<true/>
+	<key>com.apple.aned.private.secondaryANECompilerServiceAccess.allow</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siri.embeddedspeech</string>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
+	<key>com.apple.private.security.storage.SiriVocabulary</key>
+	<true/>
 	<key>com.apple.private.siri.activation</key>
 	<true/>
 	<key>com.apple.private.siri.invoke</key>

```
### SaveToFiles

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.DocumentManagerUICore.SaveToFiles</string>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.developer.auto-elect-plugin</key>

```
### com.apple.DocumentManager.Service

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service`

```diff

 	<string>com.apple.DocumentManagerUICore.Service</string>
 	<key>com.apple.Pasteboard.copy-on-paste</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>

 	<array>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServicePhotos</string>
+	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
+	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.private.trust-ubiquity-kvstore-identifier</key>

```
### druid

> `/System/Library/PrivateFrameworks/DragUI.framework/Support/druid`

```diff

 	<true/>
 	<key>com.apple.private.uikit.requestsystembanner</key>
 	<true/>
+	<key>com.apple.realitysimulation.render-on-top-spi</key>
+	<true/>
 	<key>com.apple.runningboard.DragUI</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	<true/>
 	<key>com.apple.surfboard.disable-realitychrome</key>
 	<true/>
+	<key>com.apple.surfboard.disables-scene-snapshots</key>
+	<true/>
+	<key>com.apple.surfboard.optsIntoDaemonSceneLifecycle</key>
+	<true/>
 	<key>com.apple.surfboard.scene-rendering-not-clipped</key>
 	<true/>
 	<key>com.apple.surfboard.scenesession-custom-focus-order</key>
 	<true/>
+	<key>com.apple.surfboard.scenesession-fov-opt-out</key>
+	<true/>
+	<key>com.apple.surfboard.system-elements-assertion-background-override</key>
+	<true/>
 	<key>com.apple.surfboard.system-elements-assertion-immersive-visible</key>
 	<true/>
 	<key>platform-application</key>

```
### facetimemessagestored

> `/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored`

```diff

 	</array>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<string>AGXDeviceUserClient</string>
 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
+		<string>IOGPUDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### GameCenterAuthenticateExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterAuthenticateExtension.appex/GameCenterAuthenticateExtension`

```diff

 	<string>NSFileProtectionComplete</string>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.facebook.defaultaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.developer.game-center</key>

 		<string>Multiplayer</string>
 		<string>TurnBasedMultiplayer</string>
 	</array>
+	<key>com.apple.developer.group-session</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.gamecenter</string>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

```
### GameCenterMatchmakerExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
+		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.group-activities.conversationmanagerhost</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.neighborhood-activities</string>

```
### GameCenterTurnBasedMatchmakerExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterTurnBasedMatchmakerExtension.appex/GameCenterTurnBasedMatchmakerExtension`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.sharing.airdrop.service</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.gamecenter</string>

```
### revisiond

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceFileProviderDomain</string>
 		<string>kTCCServiceSystemPolicyDocumentsFolder</string>
 		<string>kTCCServiceSystemPolicyDesktopFolder</string>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.os_version</key>
 	<true/>
+	<key>com.apple.private.healthkit.reality</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.default</key>
 	<string>com.apple.Health</string>
 	<key>com.apple.private.healthkit.sync</key>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.homekit</string>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>UserFocus.ComputedMode</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>HomeKitClientAccessoryControl</string>

 		<string>com.apple.nanoprefsync</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.sleepd.sleepserver</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

 	<string>/Library/Caches/PassKit/</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.contactsd</string>
 		<string>com.apple.kvsd</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-write</key>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.game-center</key>
+	<array>
+		<string>Account</string>
+		<string>Authenticate</string>
+		<string>Profile</string>
+		<string>Friends</string>
+		<string>Games</string>
+		<string>Scores</string>
+		<string>Achievements</string>
+		<string>Challenges</string>
+		<string>Multiplayer</string>
+		<string>TurnBasedMultiplayer</string>
+		<string>GameStats</string>
+	</array>
 	<key>com.apple.private.news-url-resolution</key>
 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>

```
### IntelligencePlatformComputeService

> `/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService`

```diff

 	<string>com.apple.intelligenceplatform.IntelligencePlatformComputeService</string>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 		<string>com.apple.siri.context.service</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.coreduetd.knowledge</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService`

```diff

 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleVideoToolboxParavirtualizationUserClient</string>
 		<string>AGXCommandQueue</string>
 		<string>AGXDevice</string>
 		<string>AGXDeviceUserClient</string>

 		<string>IOAccelSharedUserClient</string>
 		<string>IOAccelSharedUserClient2</string>
 		<string>IOAccelSubmitter2</string>
+		<string>IOGPUDeviceUserClient</string>
 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleVideoToolboxParavirtualizationUserClient</string>
 		<string>AGXCommandQueue</string>
 		<string>AGXDevice</string>
 		<string>AGXDeviceUserClient</string>

 		<string>IOAccelSharedUserClient</string>
 		<string>IOAccelSharedUserClient2</string>
 		<string>IOAccelSubmitter2</string>
+		<string>IOGPUDeviceUserClient</string>
 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.NeighborhoodActivityConduitService</key>
+	<true/>
 	<key>com.apple.PairingManager.Read</key>
 	<true/>
 	<key>com.apple.PairingManager.RemovePeer</key>

 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.mediaremoted</string>
+	<key>com.apple.private.biome.pruner</key>
+	<array>
+		<string>MediaRemote.GroupSessionRecentParticipant</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.InFocus</string>
 	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>MediaRemote.GroupSessionRecentParticipant</string>
+	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>MediaRemote.GroupSessionRecentParticipant</string>
 		<string>Media.Route</string>
 	</array>
 	<key>com.apple.private.copresence</key>

```
### UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID`

```diff

 	<true/>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>
+	<key>com.apple.security.ts.power-assertions</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.MobileAccessoryUpdater</string>
 	<key>platform-application</key>

```
### UARPUpdaterServiceUSBPD

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD`

```diff

 	<true/>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>
+	<key>com.apple.security.ts.power-assertions</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.MobileAccessoryUpdater</string>
 	<key>platform-application</key>

```
### com.apple.SharePlay.NearbyInvitationsService

> `/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService`

```diff

 	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.ids.firewall</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.groupRemoteControl.cloud</string>

 		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.groupRemoteControl.cloud</string>
 	</array>
-	<key>com.apple.private.ids.remotecredentials</key>
-	<true/>
 	<key>com.apple.private.ids.self-session</key>
 	<array>
 		<string>com.apple.private.alloy.groupRemoteControl.cloud</string>

 		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.groupRemoteControl.cloud</string>
 	</array>
-	<key>com.apple.private.imcore.imremoteurlconnection</key>
-	<true/>
 	<key>com.apple.private.nearbyinteraction.device-presence</key>
 	<true/>
 	<key>com.apple.private.nearbyinteraction.privileged</key>

```
### com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.facetime</string>
+	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 		<string>ua</string>
 		<string>identity</string>
 	</array>
+	<key>com.apple.imagent</key>
+	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>
 	<true/>
 	<key>com.apple.internal.seserviced.fido</key>

```
### peopled

> `/System/Library/PrivateFrameworks/People.framework/peopled`

```diff

 	<true/>
 	<key>com.apple.coreduetd.knowledge</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.geod</string>
+		<string>com.apple.icloud.searchpartyd.securelocations</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### PhotosPosterProvider

> `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.idle-timer-services</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>

```
### ProactiveShareSheetDataHarvestingLighthousePlugin

> `/System/Library/PrivateFrameworks/ProactiveShareSheetDataHarvestingLighthouse.framework/PlugIns/ProactiveShareSheetDataHarvestingLighthousePlugin.appex/ProactiveShareSheetDataHarvestingLighthousePlugin`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Trial/Treatments/default_factors_210.pb</string>
+		<string>/Library/CoreDuet/People/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.accountsd.accountmanager</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```
### fitcored

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored`

```diff

 	<true/>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
+	<key>com.apple.security.ts.system-info</key>
+	<array>
+		<string>net.link.addr</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.fitcored</string>
 	<key>com.apple.sharing.DeviceDiscovery</key>

```
### SiriUserFeedbackLearningUniversalSuggestionsPlugin

> `/System/Library/PrivateFrameworks/SiriPrivateLearningAnalytics.framework/PlugIns/SiriUserFeedbackLearningUniversalSuggestionsPlugin.appex/SiriUserFeedbackLearningUniversalSuggestionsPlugin`

```diff

 	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.siri.SiriPrivateLearningAnalytics.SiriUserFeedbackLearningUniversalSuggestionsPlugin</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>AppIntent</string>

```
### sociallayerd

> `/System/Library/PrivateFrameworks/SocialLayer.framework/sociallayerd.app/sociallayerd`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.MobileSMS</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.sociallayerd.CloudKit.ckreader</string>

```
### SUFollowUpRollbackDetectedExtension

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUFollowUpRollbackDetectedExtension.appex/SUFollowUpRollbackDetectedExtension`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<string>/private/var/code_coverage/</string>
 	<key>com.apple.security.exception.mach</key>
 	<array>
 		<string>com.apple.corefollowup.agent</string>

```
### SUSFollowUpExtension

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/PlugIns/SUSFollowUpExtension.appex/SUSFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<string>/private/var/code_coverage/</string>
 	<key>com.apple.security.exception.mach</key>
 	<array>
 		<string>com.apple.corefollowup.agent</string>

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	<true/>
 	<key>com.apple.keystore.stash.persist</key>
 	<true/>
+	<key>com.apple.locationd.activity</key>
+	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
 	<key>com.apple.private.CacheDelete</key>

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<string>/private/var/code_coverage/</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### stickersd

> `/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd`

```diff

 	<array>
 		<string>/private/var/mobile/Library/Stickers/</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<true/>
 </dict>
 </plist>
 

```
### PhoneIntentHandler

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler`

```diff

 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.TelephonyUtilities</string>
+	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

 		<string>access-calls</string>
 		<string>access-call-providers</string>
 		<string>modify-calls</string>
+		<string>screen-calls</string>
 		<string>access-call-capabilities</string>
 		<string>modify-call-capabilities</string>
 		<string>register-gft-service</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>NULL/ActivationState</string>
 	</array>
+	<key>com.apple.private.mediaexperience.clearmutestatecache.allow</key>
+	<true/>
 	<key>com.apple.private.necp.match</key>
 	<true/>
 	<key>com.apple.private.notificationcenter-system</key>

```
### translationd

> `/System/Library/PrivateFrameworks/Translation.framework/translationd`

```diff

 	<string>translationd</string>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.coreaudio.allow-opus-codec</key>
+	<true/>
 	<key>com.apple.developer.networking.multicast</key>
 	<true/>
 	<key>com.apple.developer.networking.multipath_extended</key>

```
### nsattributedstringagent

> `/System/Library/PrivateFrameworks/UIFoundation.framework/XPCServices/nsattributedstringagent.xpc/nsattributedstringagent`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>AGXDeviceUserClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

 	<array>
 		<string>com.apple.conference</string>
 		<string>com.apple.CloudKit</string>
+		<string>com.apple.DeviceActivity</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	</array>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>bundleID</string>
+		<string>path</string>
 		<key>value</key>
-		<string>com.apple.shortcuts</string>
+		<string>/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd</string>
 	</dict>
 	<key>com.apple.private.biome.read-only</key>
 	<array>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>bundleID</string>
+		<string>path</string>
 		<key>value</key>
-		<string>com.apple.shortcuts</string>
+		<string>/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns//ShortcutsIntents.appex/ShortcutsIntents</string>
 	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>bundleID</string>
+		<string>path</string>
 		<key>value</key>
-		<string>com.apple.shortcuts</string>
+		<string>/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices//BackgroundShortcutRunner.xpc/BackgroundShortcutRunner</string>
 	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### CatalystContentExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/CatalystContentExtension.appex/CatalystContentExtension`

```diff

 	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.coreaudio.initiatetemporarybackgroundplayback.allow</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>

```
### ICQFollowup

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup</string>
+	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>iCloud.Subscription</string>

```
### kbd

> `/System/Library/TextInput/kbd`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.LinguisticDataAuto</string>
 		<string>com.apple.MobileAsset.MecabraDictionaryRapidUpdates</string>
 		<string>com.apple.MobileAsset.DuetExpertCenterAsset</string>
 	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.stickers.api</string>
 		<string>com.apple.spotlight.SearchAgent</string>
 		<string>com.apple.ak.privateemail.xpc</string>

```

### 🆕 ccportrait_archive_bin.metallib

> `/System/Library/VideoProcessors/CCPortrait.bundle/ccportrait_archive_bin.metallib`

- No entitlements *(yet)*
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	</array>
 	<key>com.apple.private.ids.registration-control</key>
 	<true/>
+	<key>com.apple.private.ids.report-spam-message</key>
+	<true/>
 	<key>com.apple.private.imavcore.imavagent</key>
 	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<array>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServicePhotos</string>
-		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.private.trust-ubiquity-kvstore-identifier</key>
 	<true/>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.preferred_source</key>
 	<true/>
+	<key>com.apple.private.healthkit.reality</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.Health.Medications</string>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
+	<key>com.apple.accounts.inactive.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.Home</string>
 	<key>com.apple.assistant.dictation.prerecorded</key>

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.internal.studylogd</string>
+		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mediasetupd.server</string>

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.internal.studylogd</string>
+		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mediasetupd.server</string>

```
### HomeEnergyWidgetsExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
-	<key>com.apple.locationd.effective_bundle</key>
-	<true/>
 	<key>com.apple.private.homeenergy</key>
 	<true/>
 	<key>com.apple.private.homekit.allow-secure-access</key>

 	<array>
 		<string>com.apple.Home</string>
 		<string>com.apple.HomeEnergyUI</string>
+		<string>com.apple.sync.NanoHome</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
 	<true/>
+	<key>com.apple.mediaanalysisd.client</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.AXIconVision</string>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.MusicApp</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
+	<key>com.apple.runningboard.sonic</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Music</string>

```
### MusicCoreSpotlightExtension

> `/private/var/staged_system_apps/Music.app/PlugIns/MusicCoreSpotlightExtension.appex/MusicCoreSpotlightExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceMediaLibrary</string>
+	</array>
+</dict>
+</plist>
 

```
### MusicWidgets

> `/private/var/staged_system_apps/Music.app/PlugIns/MusicWidgets.appex/MusicWidgets`

```diff

 	<true/>
 	<key>com.apple.mediaremote.remote-control-discovery</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	<array>
 		<string>group.com.apple.Music</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 		<string>/Library/Caches/com.apple.Music/</string>
 		<string>/Media/</string>
 	</array>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.financed.service.bankconnect</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.seserviced.session</string>
 		<string>com.apple.SharingServices</string>

 	<string>com.apple.stockholm</string>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.FinanceKit</string>
 		<string>com.apple.AppleMediaServices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

 		<string>com.apple.Wallet</string>
 		<string>com.apple.Wallet.public</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>H11ANEInDirectPathClient</string>
+		<string>AppleVirtIONeuralEngineDeviceUserClient</string>
+	</array>
 	<key>com.apple.security.system-group-containers</key>
 	<array>
 		<string>systemgroup.com.apple.mobileactivationd</string>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
 	</array>
+	<key>com.apple.security.temporary-exception.sbpl</key>
+	<array>
+		<string>(allow file-read* (literal (string-append "/Library/Managed Preferences/" (param "_USER") "/com.apple.applicationaccess.plist")))</string>
+	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.SocialLayer</string>

```
### fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

 	<true/>
 	<key>com.apple.internal.fileprovider.fpck</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
 	<key>com.apple.private.foundation.filecoordination-debug</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.clpc.reporting</key>
 	<true/>
+	<key>com.apple.private.dmm.service</key>
+	<true/>
 	<key>com.apple.private.exposure-notification</key>
 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>

 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
+	<key>com.apple.private.mako.status</key>
+	<true/>
 	<key>com.apple.private.mcc.bwstats-access</key>
 	<true/>
 	<key>com.apple.private.mcc.datacollection-access</key>

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Device.Charging.SmartCharging</string>
+		<string>Device.Charging.BatteryGauging</string>
 	</array>
 	<key>com.apple.private.iokit.limitedpower-wakerequest</key>
 	<true/>

```
### SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

 	<true/>
 	<key>com.apple.springboard.secureAppAssertion</key>
 	<true/>
+	<key>com.apple.surfboard.immersion-client</key>
+	<true/>
 	<key>com.apple.surfboard.scenesession-updates</key>
 	<true/>
 	<key>com.apple.surfboard.sharing-mode-client</key>

```
### adid

> `/usr/libexec/adid`

```diff

         <string>com.apple.adid</string>
         <string>com.apple.adid.xpc</string>
     </array>
+    <key>com.apple.security.ts.system-info</key>
+    <array>
+        <string>net.link.addr</string>
+    </array>
+    <key>com.apple.security.exception.shared-preference.read-write</key>
+    <array>
+        <string>com.apple.FairPlay</string>
+    </array>
     <key>com.apple.security.exception.iokit-user-client-class</key>
     <array>
         <string>com_apple_driver_FairPlayIOKitUserClient</string>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<array>
 		<string>com.apple.private.alloy.accounts.representative</string>
 	</array>
-	<key>com.apple.private.ids.registration</key>
-	<array>
-		<string>com.apple.ess</string>
-		<string>com.apple.madrid</string>
-	</array>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>
 	<key>com.apple.private.notificationcenter-system</key>

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.analyticsd</string>
 		<string>com.apple.apsd</string>
-		<string>com.apple.CARenderServer</string>
 		<string>com.apple.cloudd</string>
-		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.corefollowup.agent</string>
-		<string>com.apple.gamed</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.identityservicesd.idquery.desktop.auth</string>
 		<string>com.apple.identityservicesd.idquery.embedded.auth</string>

```

### 🆕 appleidsetupd

> `/usr/libexec/appleidsetupd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.appleidsetupd</string>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
	<array>
		<string>Removal</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.ids.registration</key>
	<array>
		<string>com.apple.ess</string>
		<string>com.apple.madrid</string>
	</array>
	<key>com.apple.private.managedclient.mdm.unenroll</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.commcenter.coretelephony.xpc</string>
		<string>com.apple.accountsd.accountmanager</string>
		<string>com.apple.managedconfiguration.profiled</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### asd

> `/usr/libexec/asd`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.weather</string>
+		<string>com.apple.CoreODI</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

```
### atc

> `/usr/libexec/atc`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.adid.xpc</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>
 		<string>com.apple.Carousel.CSLSBackgroundTaskRequestService</string>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<array>
 		<string>/Library/Audio/Plug-Ins/HAL/</string>
 		<string>/Library/Audio/Tunings/</string>
+		<string>/private/var/preferences/SystemConfiguration/com.apple.radios.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>com_apple_audio_IOBorealisOwlUserClient</string>
+		<string>IOGPUDeviceUserClient</string>
 		<string>AGXDeviceUserClient</string>
 		<string>AppleJPEGDriverUserClient</string>
 		<string>AppleAOPVoiceTriggerUserClient</string>

```
### ciphermld

> `/usr/libexec/ciphermld`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.ciphermld</string>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### continuitycaptured

> `/usr/libexec/continuitycaptured`

```diff

 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.dockaccessoryd</string>
 		<string>com.apple.dockaccessoryd.debug</string>
+		<string>com.apple.lsd.open</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>com.apple.aprs</string>
 		<string>com.apple.dasd.activityDurationTracker</string>
 		<string>com.apple.gridDataServices</string>
+		<string>com.apple.gridDataServices.config</string>
 		<string>com.apple.duetactivityscheduler.trial</string>
 		<string>com.apple.duetactivityscheduler.policydatacollection</string>
 	</array>

```
### demod_helper

> `/usr/libexec/demod_helper`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileBackup</key>
+	<true/>
 	<key>com.apple.private.security.storage.demo_backup</key>
 	<true/>
 	<key>com.apple.private.vfs.snapshot</key>

```
### dmd

> `/usr/libexec/dmd`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreRemovability</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 			<array>
 				<string>App.InFocus</string>
 				<string>App.Intent</string>
+				<string>Device.Wireless.Bluetooth</string>
 				<string>UserFocus.InferredMode</string>
 				<string>UserFocus.ComputedMode</string>
 				<string>UserFocus.SleepMode</string>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.contactsd</string>
-		<string>com.apple.identityservicesd.embedded.auth</string>
-		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
-		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
-		<string>com.apple.geod</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.apsd</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.cloudd</string>
+		<string>com.apple.commcenter.coretelephony.xpc</string>
+		<string>com.apple.contactsd</string>
+		<string>com.apple.geod</string>
+		<string>com.apple.icloud.searchpartyd.securelocations</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
+		<string>com.apple.locationd.synchronous</string>
+		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.securityd</string>
 		<string>com.apple.timed.xpc</string>
-		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
-		<string>com.apple.locationd.synchronous</string>
+		<string>com.apple.usernotifications.usernotificationservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### locationd

> `/usr/libexec/locationd`

```diff

 			<dict/>
 		</dict>
 	</dict>
+	<key>com.apple.aop.hid-driver.hid-service.pdr</key>
+	<true/>
 	<key>com.apple.aop.hid-driver.user-client</key>
 	<dict>
 		<key>cma</key>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.locationd.clx</string>
 	<key>com.apple.distributedsensingd-motionState</key>
 	<true/>
 	<key>com.apple.driver.AppleBasebandPCI.user-access</key>

 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>Device.Wireless.WakeOnWiFiStatus</string>
+		<string>Device.Wireless.WiFiAvailabilityStatus</string>
 		<string>MicroLocationRestrictedLocalization</string>
 		<string>Location.MicroLocationVisit</string>
 		<string>UserFocusComputedMode</string>
+		<string>Device.Wireless.CellularQualityStatus</string>
 	</array>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
-		<string>/private/var/db/accessoryupdater/uarp/</string>
 		<string>/private/var/db/accessoryupdater/DurianUpdaterService/</string>
-		<string>/private/var/db/accessoryupdater/HawkeyeFirmware/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.safetyalerts</string>
 		<string>com.apple.managedassetsd</string>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.geoanalyticsd</string>
+		<string>com.apple.kvsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### logd_reporter

> `/usr/libexec/logd_reporter`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.kernel.get-kext-info</key>
-	<true/>
-	<key>com.apple.private.xpc.launchd.ios-system-session</key>
-	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>logd_helper</string>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 		<string>AppleVXD393UserClient</string>
 		<string>AppleJPEGDriverUserClient</string>
 		<string>AppleVideoToolboxParavirtualizationUserClient</string>
+		<string>IOGPUDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### mlhostd

> `/usr/libexec/mlhostd`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.mlhost</string>
+	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.mlhost</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/mobile/</string>
-		<string>/usr/libexec</string>
+		<string>/usr/libexec/mlhostd</string>
 		<string>/System/Library/MLHost/</string>
-	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/mobile/Library/LighthouseBackground/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/LighthouseBackground/</string>
+		<string>/AppleInternal/System/Library/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
-	<array>
-		<string>kCFPreferencesAnyApplication</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mlhost</string>

```
### mlruntimed

> `/usr/libexec/mlruntimed`

```diff

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>1020</string>
 		<string>1580</string>
 	</array>
 	<key>com.apple.trial.status.evaluation.mlruntime.allow</key>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<string>/private/var/code_coverage/</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.remoted</string>

 	<true/>
 	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>
 	<true/>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 	<true/>
 	<key>com.apple.runningboard.targetidentities</key>
 	<true/>
-	<key>com.apple.security.exception.iokit-user-client-class</key>
-	<array>
-		<string>RootDomainUserClient</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.nano.nanoregistry.paireddeviceregistry</string>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.mediaremote.device-info</key>
 	<true/>
 	<key>com.apple.mediaremote.group-sessions</key>

 		<string>com.apple.iohideventsystem</string>
 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.iphone.axserver-systemwide</string>
+		<string>com.apple.itunescloud.contenttaste</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.kvsd</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.driverkit.driver-access</key>
+	<array>
+		<string>com.apple.private.wifi.driverkit</string>
+	</array>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>

 		<string>com.apple.private.alloy.coreduet.sync</string>
 		<string>com.apple.private.alloy.nearby</string>
 	</array>
-	<key>com.apple.private.ids.registration</key>
-	<array>
-		<string>com.apple.private.alloy.airdrop.walkaway</string>
-	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>
 	<key>com.apple.private.ids.session</key>

 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
+		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.frontboard.systemappservices</string>

 		<string>com.apple.sharing.appleidauthentication</string>
 		<string>com.apple.rapport</string>
 		<string>InternetAccounts</string>
+		<string>com.apple.ProtectedCloudStorage</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.maps.model-access</key>
 	<true/>
+	<key>com.apple.momentsd.internal</key>
+	<array>
+		<string>MOOnboardingAndSettings</string>
+	</array>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.communicationsfilter</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.corelocation.map-helper-service</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.momentsd</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.imagent.embedded.auth</string>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 	<string>com.apple.safetyalertsd</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>Device.Wireless.CellularQualityStatus</string>
 		<string>Device.Wireless.WiFi</string>
+		<string>Device.Wireless.WiFiAvailabilityStatus</string>
+		<string>Device.Wireless.WakeOnWiFiStatus</string>
 		<string>Device.Wireless.CellularAvailabilityStatus</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
 	</array>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.routined.registration</string>
+		<string>com.apple.corefollowup.agent</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.private.homekit.remote-login.private</key>
 	<true/>
+	<key>com.apple.private.ids.agent.GroupRestricted</key>
+	<true/>
 	<key>com.apple.private.ids.continuity</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

 		<string>com.apple.private.alloy.sharing.paireddevice</string>
 		<string>com.apple.private.alloy.sharing.ranging</string>
 	</array>
+	<key>com.apple.private.ids.registration</key>
+	<array>
+		<string>com.apple.private.alloy.airdrop.walkaway</string>
+	</array>
 	<key>com.apple.private.ids.session</key>
 	<array>
 		<string>com.apple.private.alloy.nearby</string>

 	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
+	<key>com.apple.private.security.storage.DiagnosticReports.read-only</key>
+	<true/>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

 		<string>com.apple.BluetoothCloudServices</string>
 		<string>com.apple.bulletinboard.observerconnection</string>
 		<string>com.apple.carousel.wakegesturemonitor</string>
+		<string>com.apple.Carousel.contextuallock</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.CloudPhotoDerivativeGenerator</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.airplay</string>
 		<string>com.apple.communicationSafetySettings</string>
+		<string>com.apple.Wallet.public</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 		<string>systemgroup.com.apple.sharedpclogging</string>
+		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>

 		<string>com.apple.sharing.cdb</string>
 		<string>com.apple.Sharing</string>
 		<string>com.apple.sharing.safaripasswordsharing</string>
+		<string>com.apple.ProtectedCloudStorage</string>
 	</array>
 	<key>keychain-cloud-circle</key>
 	<true/>

```
### symptomsd-diag

> `/usr/libexec/symptomsd-diag`

```diff

 	<string>com.apple.symptomsd-diag</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+	</array>
 	<key>com.apple.DiagnosticExtensions.extensionHost</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	<true/>
 	<key>com.apple.triald.internal</key>
 	<true/>
+	<key>com.apple.triald.system.internal</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>com.apple.wifivelocity</key>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>App.InFocus</string>
 		<string>AppLaunch</string>
 		<string>UserFocusComputedMode</string>
 	</array>

 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
+	<key>com.apple.private.realityenrollment</key>
+	<true/>
 	<key>com.apple.private.remindd</key>
 	<dict>
 		<key>readWritePublic</key>

 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.contactsd</string>
+		<string>com.apple.enroll.state</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

```
### triald

> `/usr/libexec/triald`

```diff

 		<string>/private/var/Managed Preferences/mobile/</string>
 		<string>/Library/Managed Preferences/mobile</string>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/mobile/Library/OSAnalytics/Preferences/</string>
+	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>AppleVirtIONeuralEngineDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.ts.ane-client</key>
+	<true/>
 	<key>com.apple.triald.system.internal</key>
 	<true/>
 	<key>platform-application</key>

```
### videocodecd

> `/usr/libexec/videocodecd`

```diff

 		<string>AppleJPEGDriverUserClient</string>
 		<string>AppleVideoToolboxParavirtualizationUserClient</string>
 		<string>AGXDeviceUserClient</string>
+		<string>IOGPUDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.wpantund.xpc</string>
 		<string>com.apple.geoanalyticsd</string>
+		<string>com.apple.wifip2pd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
+	<key>com.apple.wifip2pd</key>
+	<true/>
 	<key>com.apple.wifivelocity</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 		<string>com.apple.backboard.display.services</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.matter.support.xpc</string>
+		<string>com.apple.UXMAssertionService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.private.wifianalytics.fw-trap</key>
 	<true/>
+	<key>com.apple.proactive.eventtracker</key>
+	<true/>
 	<key>com.apple.purplebuddy.budd.access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/usr/sbin/</string>
 		<string>/Applications/Preferences.app/Preferences/</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PayloadManifest.plist</string>
+		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>Library/UserConfigurationProfiles/PayloadManifest.plist</string>
+		<string>Library/Trial/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>access-calls</string>
 		<string>modify-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>1650</string>
+	</array>
 	<key>com.apple.wifi.cloudasset-access</key>
 	<true/>
 	<key>com.apple.wifi.hostapd</key>

```
