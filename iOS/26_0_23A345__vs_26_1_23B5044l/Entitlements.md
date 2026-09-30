## 🔑 Entitlements

### AccessorySetupUI

> `/Applications/AccessorySetupUI.app/AccessorySetupUI`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.corewifi.wifi-network-sharing-ui</key>
+	<array>
+		<string>WiFiNetworkSharing</string>
+	</array>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.private.corewifi.wifi-network-sharing-ui-xpc</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### AirDropUI

> `/Applications/AirDropUI.app/AirDropUI`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### ContinuitySingShieldUI

> `/Applications/ContinuitySingShieldUI.app/ContinuitySingShieldUI`

```diff

 		<string>com.apple.itunescloudd.playactivity</string>
 		<string>com.apple.itunescloud.delegation-provider</string>
 		<string>com.apple.itunescloud.contenttaste</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>background-activities</string>
 	</array>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-calls</string>
+	</array>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>fairplay-client</key>

```
### Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>
 		<string>IOReportUserClient</string>
+		<string>EXDisplayPipeUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### Diagnostic-8187

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187`

```diff

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.iokit.soc-limit</key>
+	<true/>
 	<key>com.apple.private.powersource-read</key>
 	<true/>
 	<key>com.apple.private.powersource-write</key>

```
### Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>
 		<string>IOReportUserClient</string>
+		<string>EXDisplayPipeUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>
 		<string>IOReportUserClient</string>
+		<string>EXDisplayPipeUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>
 		<string>IOReportUserClient</string>
+		<string>EXDisplayPipeUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

```diff

 		<string>AppleH13CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>
 		<string>IOReportUserClient</string>
+		<string>EXDisplayPipeUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### FMDMagSafeSetupRemoteUI

> `/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Caches/com.apple.icloud.findmydeviced/</string>

```
### FMDMagSafeExtension

> `/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension`

```diff

 	<true/>
 	<key>com.apple.private.accessories.showallconnections</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Caches/com.apple.icloud.findmydeviced/</string>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.pairingmanager</string>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.translation</key>
+	<true/>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>
 		<string>read</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
+		<string>com.apple.translationd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>TranslationLanguageDonation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Translation.Communication.LanguageCode</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>collaborations</string>
 	<key>com.apple.private.managed-settings.effective-read</key>

 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callhistorymanager</string>
 		<string>com.apple.callintelligenced.service</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.publisher.service.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Media

> `/Applications/Media.app/Media`

```diff

 	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.CarRadio</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.developer.carp</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
 	<key>com.apple.private.CarAssetUtils.variants</key>

 		<string>Media</string>
 		<string>PositionTracker</string>
 	</array>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.caraccessoryframework.nowplaying</key>
 	<true/>
 	<key>com.apple.private.carkit</key>

 		<string>com.apple.CarPlayApp.punch-through-service</string>
 		<string>com.apple.CarPlayApp.volume-notification-service</string>
 		<string>com.apple.CarPlayApp.status-bar-service</string>
+		<string>com.apple.CarPlayApp.service</string>
 		<string>com.apple.CarAssetUtils.variants</string>
 		<string>com.apple.carkit.service</string>
 		<string>com.apple.caraccessoryframework.nowplaying</string>
+		<string>com.apple.itunescloud.music-subscription-status-service</string>
+	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>com.apple.sharing.appleidauthentication</string>
 	</array>
 </dict>
 </plist>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.mediacontrol.client</key>
+	<true/>
 	<key>com.apple.mediaremote.allow</key>
 	<array>
 		<string>TVPairing</string>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

```
### PCViewService

> `/Applications/PCViewService.app/PCViewService`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.mediacontrol.client</key>
+	<true/>
 	<key>com.apple.mediaremote.device-info</key>
 	<true/>
 	<key>com.apple.mediaremote.remote-control-discovery</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.authentication-services.access-credential-identities</key>
 	<true/>
+	<key>com.apple.authentication-services.allow-authentication-request-any-rpid</key>
+	<true/>
 	<key>com.apple.authentication-services.coordinate-account-authentication-modification</key>
 	<true/>
 	<key>com.apple.authentication-services.credential-sharing-groups</key>

 	<true/>
 	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>
 	<true/>
+	<key>com.apple.private.safetycheckd.scblocking</key>
+	<true/>
 	<key>com.apple.private.safetycheckd.scsharingreminders</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

 	<true/>
 	<key>com.apple.private.xpc.launchd.userspace-reboot</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.admin</key>
+	<true/>
+	<key>com.apple.privatecloudcompute.requests</key>
+	<true/>
 	<key>com.apple.proactive.ActionPrediction.predictions</key>
 	<true/>
 	<key>com.apple.proactive.AppPrediction.predictions</key>

```
### PreviewShell

> `/Applications/PreviewShell.app/PreviewShell`

```diff

 	</array>
 	<key>com.apple.springboard.allowIconVisibilityChanges</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.keyboardfocusservice</key>
 	<true/>
 	<key>com.apple.springboard.widget-metrics</key>

```
### PrintCenterWidgetExtension.iOS

> `/Applications/Print Center.app/PlugIns/PrintCenterWidgetExtension.iOS.appex/PrintCenterWidgetExtension.iOS`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.security.app-sandbox</key>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.printcenter</string>
+	</array>
+	<key>platform-application</key>
 	<true/>
 </dict>
 </plist>

```
### SIMSetupUIService

> `/Applications/SIMSetupUIService.app/SIMSetupUIService`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.identityservicesd.nsxpc</string>
 		<string>com.apple.imagent.embedded.auth</string>

```
### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.lsuseractivityd.LSAlwaysPick</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.siri.sirireaderd</string>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	</array>
 	<key>com.apple.sharing.Client</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.springboard.systemaperture</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	</array>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.centralized-feedback</key>
 	<true/>
 	<key>com.apple.private.feedback.drafting</key>

 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 		<string>UserFocus.ComputedMode</string>
 		<string>UserFocusComputedMode</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

```
### StoreKitUIService

> `/Applications/StoreKitUIService.app/StoreKitUIService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.ios.StoreKitUIService</string>
+	</dict>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
 	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.storeservices/</string>
+		<string>/tmp/</string>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.appstored.xpc.request</string>
 		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.cdp.daemon</string>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 		<string>com.apple.ShortcutsActions</string>
 		<string>com.apple.ShortcutsActions.ShortcutsTopHitsExtension</string>
 	</array>
+	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>

 	<true/>
 	<key>com.apple.shortcuts.dialogpresentation</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>

```
### Transfer to Android

> `/Applications/Transfer to Android.app/Transfer to Android`

```diff

 	<array/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.MigrationKit</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.clarityboard.shows-scene</key>
+	<true/>
 	<key>com.apple.coreaudio.CanTapTelephony</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-opus-codec</key>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	<true/>
 	<key>com.apple.carousel.backlightaccess</key>
 	<true/>
+	<key>com.apple.clarityboard.shows-scene</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-opus-codec</key>
 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>

```

### 🆕 CSUIAUpcallBundle

> `/System/Library/CoreServices/CSUIAUpcallBundle.bundle/CSUIAUpcallBundle`

- No entitlements *(yet)*
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.system-layers</key>
 	<true/>
+	<key>com.apple.UIKit.status-bar-override-allow</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.airplay.endpoint.xpc</key>

 		<string>com.apple.mediaaccessibility-CarPlay</string>
 		<string>com.apple.Accessibility</string>
 		<string>com.apple.SoundDetection</string>
+		<string>com.apple.springboard</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 		<string>media</string>
 		<string>calling</string>
 		<string>voice-control</string>
+		<string>status-bar-data-additions</string>
+		<string>status-bar-overrides</string>
+		<string>status-items</string>
+		<string>airplay</string>
+		<string>background-activities</string>
+		<string>focus</string>
 	</array>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>

```
### CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

 	<true/>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```

### 🆕 CoreServicesUIAgent

> `/System/Library/CoreServices/CoreServicesUIAgent.app/CoreServicesUIAgent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 		<string>com.apple.PerformanceTrace.ptpassivecollectiond.collectionconfig</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.display-lookup</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.lockScreenContentAssertion</key>
 	<true/>
 	<key>com.apple.springboard.multiwindow.triggerShowAllWindows</key>

```

### 🆕 DoorsSample

> `/System/Library/ExtensionKit/Extensions/DoorsSample.appex/DoorsSample`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.doors.DoorsSample</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.doors.DoorsSample</string>
	<key>com.apple.private.doors.client</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.doorsd.xpc</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.doors</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
	</array>
</dict>
</plist>

```

### 🆕 FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLMLHostPlugins.FedAutoEvalPlugin</string>
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
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.priml.pfl.Morpheus.allowed</key>
	<true/>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeExperiences.PromptTags</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>App.InFocus</string>
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
	<key>com.apple.private.email</key>
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
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
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
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.email.maild</string>
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.modelmanager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.gms.availability</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
	</array>
</dict>
</plist>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>Safari.WebPagePerformance</string>
 		<string>Emoji.Engagement</string>
 		<string>Siri.AppSelection.Music</string>
-		<string>SensitiveContentAnalysis.UIInteraction</string>
-		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 		<string>MediaAnalysis.PEC.Processing</string>

 		<string>VisualIntelligenceCamera.DetectedLabels</string>
 		<string>RegionalSafetyAnalysis.Eligibility</string>
 		<string>TrustKit.Decisioning.TKModelMessages</string>
+		<string>CommApps.CallIntelligence.HoldAssistFedStats</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### FedStatsMLHostPluginClassA

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA`

```diff

 		<string>RegionalSafetyAnalysis.KeywordID</string>
 		<string>RegionalSafetyAnalysis.Disablement</string>
 		<string>RegionalSafetyAnalysis.GuardrailResult</string>
+		<string>RegionalSafetyAnalysis.LiteViolationData</string>
 		<string>GenerativeExperiences.GuardrailResult</string>
 		<string>GenerativeExperiences.GeneratedImageFeatures.FailureReason</string>
 		<string>AppleIntelligence.Reporting.SafetyGuardrails</string>

```
### FedStatsMLHostPluginClassB

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB`

```diff

 		<string>Moments.Events.Engagement</string>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
 		<string>Safari.PageLoad</string>
 		<string>Siri.Health.Federated</string>
 		<string>Device.Wireless.ConnectivityContext</string>

```
### SCARemoteView Appex

> `/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/SCARemoteView Appex`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.screen-time</key>
 	<true/>

 		<string>analysis-history-read</string>
 		<string>analysis-history-write</string>
 	</array>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.runningboard.screentimeunlock</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.contactsd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>

 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.contactsd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>

```
### SiriAttentionAndInvocationExtension

> `/System/Library/ExtensionKit/Extensions/SiriAttentionAndInvocationExtension.appex/SiriAttentionAndInvocationExtension`

```diff

 		<string>com.apple.logd.admin</string>
 		<string>com.apple.userprofiles</string>
 		<string>com.apple.assistant.multiuser.service</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.siri.location</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.logd.admin</string>
 		<string>com.apple.userprofiles</string>
 		<string>com.apple.assistant.multiuser.service</string>
+		<string>com.apple.siri.location</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.corespeechdatacollection</string>
 	</array>
+	<key>com.apple.siri.location</key>
+	<true/>
 </dict>
 </plist>
 

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>BlockFontServiceInWebContentSandbox</string>
 		<string>UnifiedPDFEnabled</string>
 		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
 	</array>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>

 		<string>BlockFontServiceInWebContentSandbox</string>
 		<string>UnifiedPDFEnabled</string>
 		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
 	</array>
 	<key>com.apple.private.web-browser-engine.webcontent</key>
 	<true/>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>BlockFontServiceInWebContentSandbox</string>
 		<string>UnifiedPDFEnabled</string>
 		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
 	</array>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>

 		<string>BlockFontServiceInWebContentSandbox</string>
 		<string>UnifiedPDFEnabled</string>
 		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
 	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>

```

### 🆕 AudioConverterHardenedService

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterHardenedService.xpc/AudioConverterHardenedService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.coreaudio.LoadConvertersInProcess</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.private.memory.ownership_transfer</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>autobox</string>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Preferences/com.apple.coreaudio.plist</string>
		<string>/Library/Preferences/.GlobalPreferences_m.plist</string>
	</array>
</dict>
</plist>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.private.network.statistics</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.network.wake_pkt.control</key>
 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>

```
### CommCenterRootHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper`

```diff

 		<string>/private/var/wireless/Library/</string>
 		<string>/private/var/db/diagnostics/</string>
 		<string>/private/var/db/uuidtext/</string>
-		<string>/private/var/logs/system_logs.logarchive</string>
+		<string>/private/var/logs/system_logs.logarchive/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### icprefd-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/XPCServices/icprefd-xpc.xpc/icprefd-xpc`

```diff

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.symptom_diagnostics</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.ImageCaptureFramework</string>
 	</array>

```
### musicd

> `/System/Library/Frameworks/MusicKit.framework/Support/musicd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.ak.authorizationservices.xpc</string>
 		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.appstored.xpc.storequeue</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.attributionkitd.xpc.token-handoff</string>

 		<string>com.apple.appstored</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.ids</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
 		<string>com.apple.StoreKit</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```
### wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>
+		<string>kTCCServiceMotion</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.private.wifi.manager-access</key>

```

### 🆕 BackgroundSecurityImprovement

> `/System/Library/PreferenceBundles/BackgroundSecurityImprovement.bundle/BackgroundSecurityImprovement`

- No entitlements *(yet)*

### 🆕 SystemVersionSettings

> `/System/Library/PreferenceBundles/SystemVersionSettings.bundle/SystemVersionSettings`

- No entitlements *(yet)*

### 🆕 CoreMotionSync

> `/System/Library/PreferencesSyncBundles/CoreMotionSync.bundle/CoreMotionSync`

- No entitlements *(yet)*
### com.apple.accounts.dom

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/XPCServices/com.apple.accounts.dom.xpc/com.apple.accounts.dom`

```diff

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.devicesharingd.enrollmentassetservice</string>
+		<string>com.apple.lsd.open</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mobilesafarishared</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1397409257</string>
 	<key>keychain-access-groups</key>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
+		<string>com.apple.AppleMediaServicesUI.engagement.notifications</string>
+		<string>com.apple.AppleMediaServicesUI.engagement.notifications.macOS</string>
 		<string>com.apple.AppStore</string>
 		<string>com.apple.Fitness</string>
 		<string>com.apple.iCloudSettingsNotification</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.AppleIntelligence.Reporting.AssetDeliveryLog</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.Availability</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.AppleIntelligence.Reporting.Invocation.Step</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.Invocation.Step</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>com.apple.timed</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.background</key>
 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>

```

### 🆕 binaryArchive.g18p

> `/System/Library/PrivateFrameworks/CinematicFraming.framework/binaryArchive.g18p`

- No entitlements *(yet)*

### 🆕 CostModelSegmenter

> `/System/Library/PrivateFrameworks/CoreMLOdie.framework/XPCServices/CostModelSegmenter.xpc/CostModelSegmenter`

- No entitlements *(yet)*
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/Library/Audio/Tunings/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/dev/exfiltration-adc-corespeechd</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/ASRAssetOverrides/</string>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.private.security.datavault.controller</key>
 	<true/>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

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
### BluetoothDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothDiagnosticExtension.appex/BluetoothDiagnosticExtension`

```diff

 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Logs/Bluetooth/</string>
+		<string>/var/mobile/Library/Logs/Bluetooth/FWlogBackup/</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 ScreenTimeDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ScreenTimeDiagnosticExtension.appex/ScreenTimeDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.DiagnosticExtensions.ScreenTime</string>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>App.MediaUsage</string>
		<string>App.WebUsage</string>
		<string>Device.Display.Backlight</string>
		<string>Media.NowPlaying</string>
		<string>Notification.Usage</string>
		<string>ScreenTime.AppUsage</string>
	</array>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/ScreenTimeDiagnostics/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.DeviceActivity</string>
	</array>
</dict>
</plist>

```

### 🆕 ToolKitDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ToolKitDiagnosticExtension.appex/ToolKitDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts/</string>
	</array>
	<key>com.apple.toolkit.request-reindex.allow</key>
	<true/>
</dict>
</plist>

```
### com.apple.DiagnosticExtensions.WiFi

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.WiFi.appex/com.apple.DiagnosticExtensions.WiFi`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
+	<key>com.apple.private.osanalytics.defaults.allow</key>
+	<true/>
 	<key>com.apple.private.wifivelocity</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/private/var/mobile/Library/Logs/</string>
 		<string>/Library/Logs/</string>
 		<string>/Library/Preferences/</string>
+		<string>/private/var/logs/CoreCapture/</string>
+		<string>/private/var/logs/CrashReporter/CoreCapture/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/run/com.apple.wifivelocity/</string>
 		<string>/private/var/log/com.apple.wifivelocity/</string>
+		<string>/private/var/tmp/ConnectivityDE/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.wifivelocityd</string>
+		<string>com.apple.centaurid.xpc</string>
 	</array>
 </dict>
 </plist>

```
### RecentsAvocado

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado`

```diff

 	<true/>
 	<key>com.apple.springboard.temporary.files-widget-transparency</key>
 	<true/>
+	<key>com.apple.springboard.widget-metrics</key>
+	<true/>
 </dict>
 </plist>
 

```
### EnergyKitService

> `/System/Library/PrivateFrameworks/EnergyKitInternal.framework/XPCServices/EnergyKitService.xpc/EnergyKitService`

```diff

 	<array>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.tcc.manager</key>
+	<true/>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Application Support/com.apple.homeenergyd/</string>

 		<string>com.apple.containermanagerd</string>
 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.homekitevents.xpc</string>
+		<string>com.apple.tccd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### facetimemessagestored

> `/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<string>com.apple.GenerativeFunctions.generativeexperiencesd</string>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.RegulatoryDomain.montara</key>
+	<true/>
 	<key>com.apple.TextUnderstanding.SmartReplies.Inference</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
-	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/tmp/</string>
+		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.nsurlsessiond</string>
+		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>

```
### homeenergyd

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

 	<array>
 		<string>com.apple.energykit.ami</string>
 		<string>com.apple.energykit.ami.dropbox</string>
+		<string>com.apple.homekit.events</string>
+		<string>com.apple.homekit.events.playground</string>
 	</array>
 	<key>com.apple.developer.icloud-extended-share-access</key>
 	<array>

 	<dict>
 		<key>com.apple.energykit.ami</key>
 		<string>com.apple.energykit.ami.LimitedPeers</string>
+		<key>com.apple.homekit.events</key>
+		<string>com.apple.homekit</string>
+		<key>com.apple.homekit.events.playground</key>
+		<string>com.apple.homekit</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.home.hindsight.read</key>
+	<true/>
+	<key>com.apple.private.home.hindsight.write</key>
+	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.homekit.home-location</key>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.weatherkit.authservice</string>
+		<string>com.apple.homekitevents.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.private.get-system-corpse</key>
 	<true/>
+	<key>com.apple.private.home.hindsight.read</key>
+	<true/>
+	<key>com.apple.private.home.hindsight.write</key>
+	<true/>
 	<key>com.apple.private.homeenergy</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

```
### DiagnosticExtension

> `/System/Library/PrivateFrameworks/IntelligencePlatform.framework/PlugIns/DiagnosticExtension.appex/DiagnosticExtension`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.suggestions.events</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Application Support</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.intelligenceplatform.Sysdiagnose</string>
+		<string>com.apple.suggestd.events</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.suggestions</string>
 	</array>
 </dict>
 </plist>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>

```
### ManagedSettingsExtension

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension`

```diff

-<?xml version="1.0" encoding="UTF-8"?>
-<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
-<plist version="1.0">
-<dict>
-	<key>application-identifier</key>
-	<string>com.apple.managedconfiguration.ManagedSettingsExtension</string>
-	<key>com.apple.managedconfiguration.profiled.set</key>
-	<array>
-		<string>ClientRestrictions</string>
-		<string>UserSettings</string>
-	</array>
-	<key>com.apple.private.InstallCoordination.allowed</key>
-	<true/>
-	<key>com.apple.private.managed-settings.effective-read</key>
-	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-only</key>
-	<array>
-		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.installcoordinationd/Library/InstallCoordination/Removability/</string>
-	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
-		<string>/Library/InstallCoordination/removability.plist</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/com.apple.managedconfiguration.ManagedSettingsExtension/</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.managedconfiguration.profiled</string>
-		<string>com.apple.installcoordinationd</string>
-	</array>
-	<key>com.apple.springboard.application-removability.proxy</key>
-	<true/>
-</dict>
-</plist>
 

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.accessibility.AXSpringBoardServerAccess</key>
+	<true/>
 	<key>com.apple.appprotectiond.read</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	<true/>
 	<key>com.apple.devicecheck.daemon-client</key>
 	<true/>
+	<key>com.apple.fileprovider.enumerate</key>
+	<true/>
+	<key>com.apple.fileprovider.fetch-url</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

 	<true/>
 	<key>com.apple.posterboardservices.data-store.refreshConfigurationSnapshot</key>
 	<true/>
+	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
+	<true/>
 	<key>com.apple.private.CallHistory.read</key>
 	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>

 	<true/>
 	<key>com.apple.private.corewifi.keychain</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MigrationKit.pauseBackgroundActivity</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.MigrationKit.resumeBackgroundActivity</key>
+	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
 	<key>com.apple.private.install.distributor-info-source</key>

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileDocuments</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCalendar</string>

 	<array>
 		<string>group.com.apple.FileProvider.LocalStorage</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/CloudStorage/</string>
+		<string>/Library/Mobile Documents/</string>
+		<string>/Containers/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/CallHistoryDB/</string>

 		<string>com.apple.MobileTimer.alarmserver</string>
 		<string>com.apple.posterboardservices.dataModel</string>
 		<string>com.apple.passd.library</string>
+		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.FileProvider</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DoNotDisturb</key>
 	<true/>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileBackup</key>

```
### com.apple.printactivityservice

> `/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.printactivityservice.xpc/com.apple.printactivityservice`

```diff

 	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.printcenter</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.sessionservices</string>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/ScreenTimeDiagnostics/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.DiagnosticExtensions.xpc-helper-access</key>
+	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Search/</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/com.apple.corespotlight.asl</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.spotlight.diagnostic.helper</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.ReportMemoryException</string>

```
### SecureMessagingAgent

> `/System/Library/PrivateFrameworks/SecureMessaging.framework/SecureMessagingAgent`

```diff

 	<true/>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>autobox</string>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/preferences/com.apple.networkd.plist</string>
+		<string>/private/var/mobile/Library/SecureMessaging/</string>
+		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin</string>
+		<string>/private/var/mobile/Library/Carrier Bundles/Overlay/</string>
+	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.ids</string>
+		<string>com.apple.securemessaging</string>
+	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.securemessagingagent</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.securemessaging</string>
 	</array>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>Siri.SELFProcessedEvent</string>
 		<string>Photos.Engagement</string>
 		<string>Photos.Edit</string>
 		<string>Photos.Search</string>

```
### com.apple.FTLivePhotoService

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.ids.firewall</key>
 	<true/>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
-	<key>com.apple.authkit.client.private</key>
-	<true/>
 	<key>com.apple.backboardd.launchapplications</key>
 	<true/>
 	<key>com.apple.backboardd.proximityDetection</key>

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

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GroupActivitySession</string>
+		<string>CommApps.CallIntelligence.HoldAssistFedStats</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
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

 	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>
 	<true/>
-	<key>com.apple.private.librarian.container-proxy</key>
-	<true/>
+	<key>com.apple.private.launchservices.changedefaulthandlers</key>
+	<array>
+		<string>com.apple.default-app.phone</string>
+	</array>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/ActivationState</string>

 	<true/>
 	<key>com.apple.private.mediaexperience.clearmutestatecache.allow</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.silentmodenotifications.allow</key>
+	<true/>
 	<key>com.apple.private.mediasafetynet.exception.callbanner</key>
 	<true/>
 	<key>com.apple.private.mediasafetynet.pilldatasource</key>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
-	<key>com.apple.private.security.storage.MobileDocuments</key>
-	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.remindd</string>
+		<string>com.apple.lsd.modifydb</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.usernotificationsd</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.DeviceAccess.private</key>
 	<true/>
 	<key>com.apple.UserNotifications.RemoteNotifications.Replicator</key>

 		<string>com.apple.iconservices</string>
 		<string>com.apple.DeviceAccess.xpc</string>
 		<string>com.apple.contactsd</string>
+		<string>com.apple.apsd</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>ToolKitToolDefinition</key>
+				<key>ToolKit.Tool</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.private.airdrop.settings</key>
 	<true/>
+	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>

 	<true/>
 	<key>com.apple.shortcuts.dialogpresentation</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.sirittsd.can-dump-audio</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 		<string>com.apple.ShortcutsActions</string>
 		<string>com.apple.ShortcutsActions.ShortcutsTopHitsExtension</string>
 	</array>
+	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>

 	<true/>
 	<key>com.apple.shortcuts.dialogpresentation</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### WidgetConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension`

```diff

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>keychain-access-groups</key>

```

### 🆕 DefaultApps

> `/System/Library/Settings/DefaultApps.settings/DefaultApps`

- No entitlements *(yet)*
### AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.BluetoothServices.cloud</key>
-	<true/>
-	<key>com.apple.BluetoothServices</key>
-	<true/>
 	<key>adi-client</key>
 	<string>143531244</string>
 	<key>application-identifier</key>
 	<string>com.apple.visionproapp</string>
 	<key>aps-environment</key>
 	<string>production</string>
+	<key>com.apple.airplay.receiver.mediaremote.services</key>
+	<true/>
+	<key>com.apple.airplay.receiverservices</key>
+	<true/>
 	<key>com.apple.authkit.client</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.avfoundation.allows-access-to-device-list</key>
+	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
+	<key>com.apple.BluetoothServices.cloud</key>
+	<true/>
+	<key>com.apple.BluetoothServices</key>
+	<true/>
+	<key>com.apple.CompanionLink</key>
+	<true/>
+	<key>com.apple.coremedia.allow-mpeg4streaming</key>
+	<true/>
+	<key>com.apple.coremedia.allow-protected-content-playback</key>
+	<true/>
+	<key>com.apple.coremedia.salplayer</key>
+	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
+	<key>com.apple.developer.healthkit</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.spatialshowcase.userdata</string>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.devicesharing.enrollmentassetservice.client</key>
+	<true/>
+	<key>com.apple.devicesharingd.client</key>
+	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.PairingManager.HomeKit</key>
+	<true/>
+	<key>com.apple.PairingManager.Read</key>
+	<true/>
+	<key>com.apple.PairingManager.Write</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<string>com.apple.visionproapp</string>
 	<key>com.apple.private.appstorecomponents.media-client-version</key>
 	<string>1</string>
+	<key>com.apple.private.bmk.allow</key>
+	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
+	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
+	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
+	<key>com.apple.private.driverkit.driver-access</key>
+	<array>
+		<string>com.apple.private.wifi.driverkit</string>
+	</array>
 	<key>com.apple.private.fairplay.FPDI</key>
 	<dict>
 		<key>capabilities</key>

 		<key>client-identifier</key>
 		<string>amstool</string>
 	</dict>
-	<key>com.apple.developer.healthkit</key>
-	<true/>
-	<key>com.apple.devicesharing.enrollmentassetservice.client</key>
-	<true/>
-	<key>com.apple.private.bmk.allow</key>
-	<true/>
 	<key>com.apple.private.healthkit.metadata.private</key>
 	<true/>
 	<key>com.apple.private.healthkit.read_authorization_bypass</key>
 	<array>
 		<string>HKVisionPrescriptionTypeIdentifier</string>
 	</array>
+	<key>com.apple.private.MobileActivation</key>
+	<array>
+		<string>GetActivationState</string>
+	</array>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.rtcreportingd</key>
+	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>

 	<array>
 		<string>RemoteDownloadIdentifiers</string>
 		<string>Articles</string>
+		<string>ProductPageCustomPresentationStyle</string>
 	</array>
 	<key>com.apple.private.tvAppExtension</key>
 	<true/>
+	<key>com.apple.rapport.Client</key>
+	<true/>
+	<key>com.apple.runningboard.visionproapp.airplayreceiver</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>IOTimeSyncClockManagerUserClient</string>
+		<string>IOTimeSyncDomainUserClient</string>
+		<string>IOTimeSyncgPTPManagerUserClient</string>
+		<string>IOTimeSyncNetworkPortUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.BluetoothCloudServices</string>
 		<string>com.apple.devicesharingd.enrollmentassetservice</string>
+		<string>com.apple.devicesharingd</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.PairingManager</string>
+		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.visioncompaniond</string>
+		<string>com.apple.wifip2pd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.airplay</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.visioncompaniond</string>
 		<string>com.apple.visionproapp.notifications</string>
 		<string>com.apple.TetsuoUITests</string>
 	</array>
+	<key>com.apple.springboard.appbackgroundstyle</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
+	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
+	<true/>
+	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>
+	<array>
+		<string>preferences.plist</string>
+	</array>
+	<key>com.apple.timed</key>
+	<true/>
+	<key>com.apple.timed.sources</key>
+	<array>
+		<string>AirPlaySendingDeviceTime</string>
+	</array>
 	<key>com.apple.visioncompaniond.client</key>
 	<true/>
+	<key>com.apple.wifi.events</key>
+	<true/>
+	<key>com.apple.wifi.events.private</key>
+	<true/>
+	<key>com.apple.wifi.manager-access</key>
+	<true/>
+	<key>com.apple.wifip2pd</key>
+	<true/>
+	<key>com.apple.wlan.authentication</key>
+	<true/>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
+	<key>com.apple.private.mediaexperience.systemcontroller.allowappstoinitiateplayback</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>511712240</string>
-	<key>com.apple.itunesstored.private</key>
-	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.airplay</string>
+		<string>com.apple.airplay.pairing</string>
+		<string>com.apple.pairing</string>
+	</array>
 	<key>previous-application-identifiers</key>
 	<array>
 		<string>XLS5V72N46.com.apple.visionproapp</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.keystore.device.verify</key>
+	<true/>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>

 	<array>
 		<string>MDMInfo</string>
 	</array>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
+	<key>com.apple.mkb.usersession.keybagopaquedata</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.seserviced.storage-management-presentation</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 	<array>
 		<string>Discoverability.Signals</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

```
### LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	<array>
 		<string>Discoverability.Signals</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

```
### MirroredWidgetExtension

> `/private/var/staged_system_apps/Fitness.app/PlugIns/MirroredWidgetExtension.appex/MirroredWidgetExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.linkd.autoShortcut</string>
+	</array>
+</dict>
+</plist>
 

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.keystore.device.verify</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
 	<array>
 		<string>PopInstallationQueue</string>

 	<true/>
 	<key>com.apple.nfcd.session.reader.internal</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceCamera</string>
+		<string>kTCCServiceEnergyKitGuidance</string>
 		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>

```
### HomeEnergyWidgetsExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceEnergyKitGuidance</string>
 		<string>kTCCServiceWillow</string>
 	</array>
 	<key>com.apple.runningboard.launchprocess</key>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobileassetd.v2</string>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.modelcatalog.catalog</string>

 	<true/>
 	<key>fairplay-client</key>
 	<string>511712240</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>C4MF3YMD84.com.apple.journal</string>
+	</array>
 </dict>
 </plist>
 

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.argos.availibility-bypass</key>
 	<true/>
+	<key>com.apple.askto.responseui.host</key>
+	<true/>
 	<key>com.apple.asktod</key>
 	<true/>
 	<key>com.apple.assistant.cdm.client</key>

 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 		<string>MLSE.ShareSheet.ConversationUserInteraction</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceMediaLibrary</string>
+		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 		<string>loiEntityRelevanceRanking</string>
 		<string>hasAssociationSubgraph</string>
 	</array>
+	<key>com.apple.private.kernel.panic</key>
+	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/ActivationPrivateKey</string>

```
### Reminders

> `/private/var/staged_system_apps/Reminders.app/Reminders`

```diff

 		<string>com.apple.chrono.widgetcenterconnection</string>
 		<string>com.apple.tipsd</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
+		<string>com.apple.alarmkitservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.shortcuts.background-running</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.shortcuts.trigger-editing</key>
 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>

```
### modelcatalogdump

> `/usr/bin/modelcatalogdump`

```diff

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>SIML_ADM_PERSONALIZATION</string>
+		<string>SIRI_TTS_UAF_AB_DEVICE</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### modelmanagerdump

> `/usr/bin/modelmanagerdump`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inferenceMonitor</key>
 	<true/>
+	<key>com.apple.modelmanager.inferenceprovidermanager</key>
+	<true/>
 	<key>com.apple.modelmanager.loadBundle</key>
 	<true/>
 	<key>com.apple.modelmanager.query</key>
 	<true/>
 	<key>com.apple.modelmanager.test</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.allowed</key>
+	<true/>
+	<key>com.apple.private.InstallCoordination.uninstall</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.forceDomain</key>
 	<true/>
 	<key>com.apple.private.eligibilityd.resetDomain</key>
 	<true/>
+	<key>com.apple.private.launchservices.cansetapplicationstrusted</key>
+	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.security.no-container</key>

 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<false/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.remoted.control</string>

 	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/AppleInternal/Tests/ModelManager/Utilities/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 		<string>com.apple.password-manager.website-metadata.testing</string>
 		<string>com.apple.passwords.filevault</string>
 		<string>com.apple.passwords.filevault.testing</string>
+		<string>com.apple.passwords.filevault.testing.testing</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DoNotDisturb</key>
 	<true/>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileBackup</key>

```
### FinishRestoreFromBackup

> `/usr/libexec/FinishRestoreFromBackup`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DoNotDisturb</key>
 	<true/>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileBackup</key>

```
### NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.nvmetunnel.allow</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.duetactivityscheduler</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>ASPUserClient</string>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	</array>
 	<key>com.apple.seld.cm.event</key>
 	<true/>
+	<key>com.apple.springboard.CFUserNotification</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
+	<key>com.apple.surfboard.CFUserNotification</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.systemapp.allowsShutdown</key>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.scodec-user-client.access</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.speechtranslationclient</key>
 	<true/>
 	<key>com.apple.private.stackshot.stats</key>

 		<string>/Library/Audio/Plug-Ins/HAL/</string>
 		<string>/Library/Audio/Tunings/</string>
 		<string>/private/var/preferences/SystemConfiguration/com.apple.radios.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### avconferenced

> `/usr/libexec/avconferenced`

```diff

 	<array>
 		<string>ScreenSharing</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>SensitiveContentAnalysis.MediaAnalysis</string>
+		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
+		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+	</array>
 	<key>com.apple.private.carkit</key>
 	<true/>
 	<key>com.apple.private.coreaudio.mutenotificationincludecontextkey</key>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<string>production</string>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.PairingManager.HomeKit</key>
+	<true/>
+	<key>com.apple.PairingManager.Read</key>
+	<true/>
+	<key>com.apple.PairingManager.Write</key>
+	<true/>
 	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
 	<true/>
 	<key>com.apple.appletv.pbs.user-profiles</key>

```
### coreidvd

> `/usr/libexec/coreidvd`

```diff

 	<true/>
 	<key>com.apple.private.extensionkit.extension-management</key>
 	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.applepay</string>
+	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>coreidvd</string>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>coreidvd</string>
-	</array>
 </dict>
 </plist>
 

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.developer.accessory-extension</key>
+	<true/>
 	<key>com.apple.developer.accessory-setup-discovery-extension</key>
 	<true/>
+	<key>com.apple.developer.accessory-transport-extension</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.media-device-discovery-extension</key>

 	</array>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.tcc.events.subscriber</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>
 		<string>kTCCServiceBluetoothAlways</string>
+		<string>kTCCServiceAll</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
+		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
+		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceAll</string>
 	</array>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.DeviceAccess</string>
+		<string>com.apple.deviceaccessd</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```

### 🆕 doorsd

> `/usr/libexec/doorsd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.doorsd</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.doorsd</string>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.doors.worker-host-entitlement</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.intelligenceflow.context</key>
	<true/>
	<key>com.apple.intelligenceflow.uiContext</key>
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
	<key>com.apple.private.biome.pruner</key>
	<array>
		<string>Doors.Tracing</string>
		<string>Doors.Events</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Doors.Tracing</string>
		<string>Doors.Events</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>DoorsTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Doors.Tracing</string>
				<string>Doors.Events</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.doors</string>
	</array>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.runningboard.terminateprocess</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.doors</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/usr/libexec/doorsd</string>
		<string>/System/Library/Doors/</string>
		<string>/AppleInternal/Library/Doors/</string>
		<string>/Library/Preferences/com.apple.networkd.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.doorsd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.mediator</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.lsd.mapdb</string>
		<string>com.apple.intelligenceflow.uiContext</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.doors</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.ts.application-group-support</key>
	<true/>
	<key>com.apple.security.ts.mobile-keybag-access</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 				<string>HomeKit.Client.AccessoryControl</string>
 				<string>Location.PointOfInterest.Category</string>
 				<string>Location.Semantic</string>
+				<string>Location.MicroLocationVisit</string>
 				<string>App.Clip.InFocus</string>
 				<string>Audio.Route</string>
 				<string>CarPlay.Connected</string>
 				<string>Device.Power.PluggedIn</string>
 				<string>Media.NowPlaying</string>
+				<string>App.RelevantShortcuts</string>
 			</array>
 		</dict>
 	</dict>

```
### enhancedloggingd

> `/usr/libexec/enhancedloggingd`

```diff

 	<string>com.apple.enhancedloggingd</string>
 	<key>com.apple.EnhancedLoggingState.client</key>
 	<true/>
+	<key>com.apple.developer.homekit</key>
+	<true/>
+	<key>com.apple.developer.homekit.background-mode</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
 	<key>com.apple.diagnosticextensionsd.xpcclient</key>
 	<true/>
-	<key>com.apple.private.accounts.allaccounts</key>
+	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.homekit</key>
+	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceWillow</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>tmp/com.apple.enhancedloggingd/</string>

 	<array>
 		<string>com.apple.diagnosticextensionsd.session</string>
 		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.homed.xpc</string>
 	</array>
 </dict>
 </plist>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<array>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 		<string>group.com.apple.icloud.findmydevice.followup</string>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
 	</array>
 	<key>com.apple.private.system-keychain</key>
 	<true/>

 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+		<string>group.com.apple.icloud.findmydevice.followup</string>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### fseventsd

> `/usr/libexec/fseventsd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.security.disk-device-access</key>
+	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
+	<key>com.apple.private.security.storage.SystemPolicyAllFiles</key>
+	<true/>
+	<key>com.apple.private.vfs.filesec-access</key>
+	<true/>
 	<key>com.apple.private.vfs.fsevents-activity-watcher</key>
 	<true/>
+	<key>com.apple.rootless.storage.SystemPolicyAllFiles</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>

```
### idcredd

> `/usr/libexec/idcredd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.coreidv.idcredd</string>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.internal.seserviced.ptattestation</key>

 	<array>
 		<string>com.apple.MobileAsset.CoreIDVAssets</string>
 	</array>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.idcredd</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

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
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
+	<key>com.apple.private.softwareupdated.OSUpdate</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
 	<true/>
+	<key>com.apple.private.networkextension.configuration</key>
+	<true/>
 	<key>com.apple.private.power.notifications-temp</key>
 	<true/>
 	<key>com.apple.private.privacy.accounting.write</key>

```
### lsd

> `/usr/libexec/lsd`

```diff

 	<true/>
 	<key>com.apple.private.amfi.can-check-trust-cache</key>
 	<true/>
+	<key>com.apple.private.apfs.get-graft-info</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.coreservices.canforcedatabasegc</key>

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
### mobile_diagnostics_relay

> `/usr/libexec/mobile_diagnostics_relay`

```diff

 <dict>
 	<key>allow-obliterate-device</key>
 	<true/>
+	<key>com.apple.developer.nfc.readersession.formats</key>
+	<array>
+		<string>NDEF</string>
+		<string>ISO15693</string>
+		<string>VAS</string>
+		<string>TAG</string>
+	</array>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
 	<key>com.apple.nfcd.seshat</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
+	<key>com.apple.private.RemoteServiceDiscovery.device-admin</key>
+	<true/>
+	<key>com.apple.private.lockdown.finegrained-get</key>
+	<array>
+		<string>com.apple.PurpleBuddy/SetupDone</string>
+		<string>com.apple.PurpleBuddy/SetupFinishedAllSteps</string>
+		<string>com.apple.PurpleBuddy/SetupState</string>
+		<string>com.apple.lockdown.datamigrator/MigrationDone</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>RootDomainUserClient</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 </dict>
 </plist>
 

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_SecureAnalytics_FM/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CN_Guardrail/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/</string>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/System/Library/CoreServices/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```

### 🆕 otter

> `/usr/libexec/otter`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.networking.ethernet.user-access</key>
	<true/>
	<key>com.apple.private.AppleDPDKResourcesUserClient.access</key>
	<true/>
	<key>com.apple.private.AppleUIOMemUserClient.access</key>
	<true/>
	<key>com.apple.private.AppleUIOPCIUserClient.access</key>
	<true/>
	<key>com.apple.private.IORDMAFamilyUC</key>
	<true/>
	<key>com.apple.private.mlx5flowtable.client</key>
	<true/>
	<key>com.apple.private.necp.policies</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>MLX5FlowTableL2UserClient</string>
</dict>
</plist>

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.springboard.addWebClipToHomeScreen</key>
 	<true/>
+	<key>com.apple.springboard.application-removability.proxy</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>

```
### remindd

> `/usr/libexec/remindd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>NSSupportsAlarmKit</key>
+	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.remindd</string>
 	<key>aps-connection-initiate</key>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.alarmkit.bundleIdentifier</key>
+	<string>com.apple.reminders</string>
 	<key>com.apple.private.appintents.relevant.custom-identifier-allowed</key>
 	<true/>
 	<key>com.apple.private.aps-client-cert-access</key>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.alarmkitservices</string>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.PowerManagement.control</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.sharingd</string>
+	</array>
 	<key>com.apple.private.security.storage-exempt</key>
 	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>

 	<true/>
 	<key>com.apple.samples.cloudkit.sharing</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.sharingd</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Applications/</string>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.AppleIntelligence.Reporting.AssetDeliveryLog.ModelCatalog</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.ModelCatalog</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.AppleIntelligence.Reporting.AssetDeliveryLog.UnifiedAssetFramework</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.UnifiedAssetFramework</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.link.vocabulary.index</key>
 	<true/>

```
### textcomposerd

> `/usr/libexec/textcomposerd`

```diff

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
+	<key>com.apple.security.network.server</key>
+	<true/>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### triald

> `/usr/libexec/triald`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.nanobuddy</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
 	</array>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 		<string>com.apple.itunescloud</string>
 		<string>com.apple.mediaremote</string>
 		<string>com.apple.tvremoted</string>
-		<string>com.apple.TVRemoteMediaServices</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### usermanagerhelper

> `/usr/libexec/usermanagerhelper`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.usermanagerd</string>

```
### visioncompaniond

> `/usr/libexec/visioncompaniond`

```diff

 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

```
