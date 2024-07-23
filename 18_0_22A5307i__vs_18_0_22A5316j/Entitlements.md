## 🔑 Entitlements

### BarcodeScannerCaptureExtension

> `/Applications/BarcodeScanner.app/Extensions/BarcodeScannerCaptureExtension.appex/BarcodeScannerCaptureExtension`

```diff

 	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>H11ANEIn</string>
+		<string>H11ANEInDirectPathClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array/>
+	<array>
+		<string>com.apple.appleneuralengine</string>
+		<string>com.apple.appleneuralengine.private</string>
+	</array>
 </dict>
 </plist>
 

```
### CheckerBoard

> `/Applications/CheckerBoard.app/CheckerBoard`

```diff

 	</array>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
-	<key>com.apple.surfboard.legacy-placement</key>
-	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>
 	<true/>
 	<key>com.apple.systemstatus.domains</key>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.app-distribution.private</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

 	<array>
 		<string>/Library/com.apple.WatchListKit/</string>
 		<string>/Library/ContactsMetadata/</string>
+		<string>/Library/Logs/MediaServices/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.sportsd.xpc</string>
 		<string>com.apple.parsec-fbf</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>
+		<string>com.apple.itunescloud.remote-request-execution-service</string>
+		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
+	<key>com.apple.symptoms.NetworkOfInterest</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-call-capabilities</string>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	<array>
 		<string>com.apple.MobileAsset.BridgeAssets</string>
 	</array>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
 	<key>com.apple.private.corerepair.attestation</key>

 	<true/>
 	<key>com.apple.sharingd</key>
 	<true/>
+	<key>com.apple.springboard.126E27E0-D025-4A46-B2F1-AF49D4E0B105</key>
+	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
 	<key>com.apple.springboard.disallowControlCenter</key>

```
### Feedback Assistant iOS

> `/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS`

```diff

 		<string>com.apple.feedbackd.xpc</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.ProactiveSummarization.server</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### GameOverlayUI

> `/Applications/GameOverlayUI.app/GameOverlayUI`

```diff

 	<array>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.iphone.axserver-systemwide</string>
+		<string>com.apple.controlcenter.remoteservice</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 	</array>
 	<key>com.apple.private.accessories.showallconnections</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
+	<key>com.apple.developer.hid.virtual.device</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-device</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>

 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>RootDomainUserClient</string>
+		<string>IOHIDResourceDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### MobileSafari

> `/Applications/MobileSafari.app/MobileSafari`

```diff

 		<string>com.apple.UsageTrackingAgent.private</string>
 		<string>com.apple.remotemanagementd.ask</string>
 		<string>com.apple.passd.account</string>
+		<string>com.apple.passd.payment</string>
 		<string>com.apple.AppSSO.service-xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.translationd</string>

 		<string>com.apple.WebKit.WebContent.Crashy</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.webprivacyd</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

 		<string>com.apple.synapse.link-context-service</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.passd.payment</string>
 		<string>com.apple.donotdisturb.appconfiguration.service</string>
 		<string>com.apple.security.kcsharing</string>
-		<string>com.apple.webprivacyd</string>
 		<string>com.apple.SharePlay.GroupSessionService</string>
 		<string>com.apple.siri.sirireaderd</string>
 		<string>com.apple.sirittsd</string>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>Photos.Delete</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Photos.Edit</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Photos.Engagement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Photos.Favorite</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Photos.Memories.Curation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Photos.Memories.MoviePlayed;</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Photos.Memories.Notification</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>Photos.Memories.Shared</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>Photos.Memories.Viewed</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>Photos.MemoryCreation</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>Photos.Share</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 			</dict>
 		</dict>
 	</dict>

 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.mediaanalysisd.embeddingstore</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
+	<key>com.apple.private.MobileContainerManager.appGroup.noReference</key>
+	<array>
+		<string>group.com.apple.Journal</string>
+	</array>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdentifierLookup</key>

 	<true/>
 	<key>com.apple.private.Safari.History</key>
 	<true/>
-	<key>com.apple.private.Safari.PasswordBreachHelper</key>
-	<true/>
 	<key>com.apple.private.SensorKit.prerequisite.readwrite</key>
 	<true/>
 	<key>com.apple.private.WebKit.UnrestrictedApplePay</key>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>settings.TransparencyLogReport</key>
+		<key>AppleIntelligenceReportExport</key>
 		<dict>
 			<key>Streams</key>
 			<dict>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>PrivateCloudCompute.RequestLog</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 			</dict>
 		</dict>
 	</dict>

 		<string>group.com.apple.weather</string>
 		<string>group.com.apple.contacts.private-access</string>
 		<string>group.tvappservices.container</string>
+		<string>group.com.apple.ScreenContinuityServices</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.attributionkitd.xpc.developer-mode</string>
+		<string>com.apple.ind.cloudfeatures</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.journal</string>
 		<string>com.apple.contacts.sharedProfile</string>
 		<string>com.apple.photos.picker</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleNVMeEANUC</string>
+		<string>AppleAPFSUserClient</string>
 		<string>AGXCommandQueue</string>
 		<string>AGXDevice</string>
 		<string>AGXDeviceUserClient</string>

 		<string>com.apple.coreservices.appleidauthentication</string>
 		<string>com.apple.coreservices.appleidauthentication.keychainaccessgroup</string>
 		<string>com.apple.sharing.appleidauthentication</string>
-		<string>com.apple.sharing.safaripasswordsharing</string>
 		<string>com.apple.social.oauthurl</string>
 		<string>com.apple.passd</string>
 		<string>com.apple.managed.vpn.shared</string>
-		<string>com.apple.webkit.webauthn</string>
-		<string>com.apple.onetimecodegenerator</string>
-		<string>com.apple.password-manager</string>
 		<string>com.apple.mail.identities</string>
 		<string>com.apple.cfnetwork-recently-deleted</string>
-		<string>com.apple.password-manager-recently-deleted</string>
-		<string>com.apple.webkit.webauthn-recently-deleted</string>
-		<string>com.apple.password-manager.personal-recently-deleted</string>
-		<string>com.apple.password-manager.personal</string>
-		<string>com.apple.password-manager.generated-passwords</string>
 		<string>com.apple.AppleCareSupport-Preferences</string>
 	</array>
 	<key>keychain-cloud-circle</key>

```
### RemotePaymentPassActionsService

> `/Applications/RemotePaymentPassActionsService.app/RemotePaymentPassActionsService`

```diff

 	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### RemoteiCloudQuotaUI

> `/Applications/RemoteiCloudQuotaUI.app/RemoteiCloudQuotaUI`

```diff

 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.backupd</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.passd.account</string>
+		<string>com.apple.passd.payment</string>
 		<string>com.apple.AppSSO.service-xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.translationd</string>

 		<string>com.apple.AuthenticationServices.AutoFill</string>
 		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.email.maild</string>
+		<string>com.apple.webprivacyd</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.passd.payment</string>
 		<string>com.apple.security.kcsharing</string>
-		<string>com.apple.webprivacyd</string>
 		<string>com.apple.lsd.modifydb</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>

```
### SafetyMonitorApp

> `/Applications/SafetyMonitorApp.app/SafetyMonitorApp`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.carousel.liveactivities.associatedbundleid</key>
+	<string>com.apple.MobileSMS</string>
 	<key>com.apple.carousel.liveactivities.openurl</key>
 	<true/>
 	<key>com.apple.carousel.liveactivities.prevents_smartstack_dismissal</key>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.replicatorservices</string>
+		<string>com.apple.mediaexperience.endpoint.xpc</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.ScreenContinuityShell</string>
 	</array>
 	<key>com.apple.springboard.continuitysession</key>
 	<true/>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-keyboard</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 		<string>com.apple.softposreaderd</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.gms.availability</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.DeviceActivity</string>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<array>
 		<string>com.apple.siri.Settings</string>

 	</dict>
 	<key>com.apple.private.replay-kit</key>
 	<true/>
+	<key>com.apple.private.security.storage.Messages</key>
+	<true/>
+	<key>com.apple.private.security.storage.MessagesMetaData</key>
+	<true/>
 	<key>com.apple.private.security.storage.Notes</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriInference</key>

 	<array>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/tmp/SiriMessages/</string>
+		<string>/Library/SMS/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.siri.client_lite</string>
 		<string>com.apple.siri.location</string>
+		<string>com.apple.corespeech.voicetriggerservice</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
+	<key>com.apple.private.security.storage.SiriInference</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.security.storage.Weather</key>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>

 	<string>system</string>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
+	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### TVRemoteUIService

> `/Applications/TVRemoteUIService.app/TVRemoteUIService`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.hangtracermonitor</string>

```
### WidgetRenderer_CarPlay

> `/Applications/WidgetRenderer_CarPlay.app/WidgetRenderer_CarPlay`

```diff

 		<string>/Library/chronod/</string>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/Library/UserFonts/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### WidgetRenderer_Default

> `/Applications/WidgetRenderer_Default.app/WidgetRenderer_Default`

```diff

 		<string>/Library/chronod/</string>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/Library/UserFonts/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 		<string>com.apple.facetime.bag</string>
 		<string>com.apple.accessibility.livespeech</string>
 		<string>com.apple.speech.SpeechRecognitionCommandAndControl</string>
+		<string>com.apple.Accessibility.SwitchControl</string>
 		<string>com.apple.WatchControl</string>
 		<string>com.apple.airplay</string>
 		<string>com.apple.ClarityUI</string>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	<true/>
 	<key>com.apple.springboard.activateassistant</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>
 	<true/>
 	<key>com.apple.springboard.system-component-layout-monitoring</key>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<true/>
 	<key>com.apple.idle-timer-services</key>
 	<true/>
+	<key>com.apple.private.CarPlayServices.icon-layout</key>
+	<true/>
+	<key>com.apple.private.accessories.showallconnections</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.attentionawareness.samplewhileabsent</key>
 	<true/>
+	<key>com.apple.private.carkit</key>
+	<true/>
+	<key>com.apple.private.carkit.app</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.externalaccessory.showallaccessories</key>
+	<true/>
 	<key>com.apple.private.hid.client.admin</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>

 	<array>
 		<string>com.apple.commandandcontrol</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.CarPlayApp.service</string>
+	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>

```
### ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

 	</array>
 	<key>com.apple.screensharing.accessibility</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read</key>
+	<array>
+		<string>/System/Library/CoreServices/SystemVersion.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.accessibility.AXBackBoardServer</string>
+		<string>com.apple.springboard.services</string>
+		<string>com.apple.iohideventsystem</string>
+		<string>com.apple.CARenderServer</string>
+		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.AccessibilityUIServer</string>
+		<string>com.apple.pasteboard.pasted</string>
+		<string>com.apple.timed.xpc</string>
+		<string>com.apple.locationd.synchronous</string>
+		<string>com.apple.commcenter.coretelephony.xpc</string>
+		<string>com.apple.commcenter.coretelephony.spi</string>
+		<string>com.apple.donotdisturb.service</string>
+		<string>com.apple.icloud.findmydeviced</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
 		<string>com.apple.backboardd</string>
+		<string>com.apple.UIKit</string>
+		<string>com.apple.screensharingserver</string>
+		<string>com.apple.MobileSMS</string>
 	</array>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>

 	<true/>
 	<key>platform-application</key>
 	<true/>
+	<key>seatbelt-profiles</key>
+	<array>
+		<string>ScreenSharingServer</string>
+	</array>
 </dict>
 </plist>
 

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Calendar</key>
 	<true/>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.security.storage.clipserviced</key>

 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
+	<key>com.apple.usernotificationsvendor.listener</key>
+	<true/>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>
 	<key>com.apple.visualvoicemail.client</key>

```

### 🆕 BluetoothSettingsAppIntentsWidgetExtension

> `/System/Library/ExtensionKit/Extensions/BluetoothSettingsAppIntentsWidgetExtension.appex/BluetoothSettingsAppIntentsWidgetExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.bluetooth.internal</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.bluetooth.xpc</key>
	<true/>
	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.bluetooth.xpc</string>
	</array>
</dict>
</plist>

```
### ExperimentationExtension

> `/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.siri.metrics.MetricsExtension</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
+	<key>com.apple.private.assistant.settings</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.siri.metrics.MetricsExtension</string>
 	<key>com.apple.private.biome.read-only</key>

 	<array>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<array>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>Safari.WindowProxy</string>
 		<string>Siri.AssistantSuggestionFeatures</string>
 		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
+		<string>Photos.Delete</string>
+		<string>Photos.Memories.Curation</string>
+		<string>Photos.MemoryCreation</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```

### 🆕 LLMCacheSELFIngestor

> `/System/Library/ExtensionKit/Extensions/LLMCacheSELFIngestor.appex/LLMCacheSELFIngestor`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.LLMCacheSELFIngestor</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>CacheManagerLogging.StreamMapper</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>LLMCache.CacheManagerTelemetry</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### MetricsExtension

> `/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/MetricsExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.siri.metrics.MetricsExtension</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
+	<key>com.apple.private.assistant.settings</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.siri.metrics.MetricsExtension</string>
 	<key>com.apple.private.biome.read-only</key>

 	<array>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<array>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>

```

### 🆕 NLPLearnerExtension

> `/System/Library/ExtensionKit/Extensions/NLPLearnerExtension.appex/NLPLearnerExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.NLPLearnerExtension</string>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.LinguisticDataAuto</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/tmp/ </string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_LinguisticDataAuto/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.mobileasset.autoasset</string>
	</array>
</dict>
</plist>

```
### PFLASLAppEmbedding

> `/System/Library/ExtensionKit/Extensions/PFLASLAppEmbedding.appex/PFLASLAppEmbedding`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLASLArcadeRanking

> `/System/Library/ExtensionKit/Extensions/PFLASLArcadeRanking.appex/PFLASLArcadeRanking`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLASLArcadeRetention

> `/System/Library/ExtensionKit/Extensions/PFLASLArcadeRetention.appex/PFLASLArcadeRetention`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLASLExperimental

> `/System/Library/ExtensionKit/Extensions/PFLASLExperimental.appex/PFLASLExperimental`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLCSLAppStore

> `/System/Library/ExtensionKit/Extensions/PFLCSLAppStore.appex/PFLCSLAppStore`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PFLCSLAppStore2

> `/System/Library/ExtensionKit/Extensions/PFLCSLAppStore2.appex/PFLCSLAppStore2`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### PhotosPFLPlugin

> `/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin`

```diff

 				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>
 		</dict>
-		<key>PhotosPFL</key>
+		<key>Photos</key>
 		<dict>
 			<key>Streams</key>
 			<dict>

```

### 🆕 SoundAndHapticsControls

> `/System/Library/ExtensionKit/Extensions/SoundAndHapticsControls.appex/SoundAndHapticsControls`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
</dict>
</plist>

```
### WiFiSettingsControlsExtension

> `/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension`

```diff

 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.private.corewifi</key>
+	<true/>
+	<key>com.apple.private.corewifi.bssid</key>
+	<true/>
+	<key>com.apple.private.corewifi.countrycode</key>
+	<true/>
+	<key>com.apple.private.corewifi.internal</key>
+	<true/>
+	<key>com.apple.private.corewifi.mac-addr</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.private.corewifi.internal-xpc</string>
+		<string>com.apple.private.corewifi-xpc</string>
+	</array>
+	<key>com.apple.wifi.manager-access</key>
+	<true/>
 </dict>
 </plist>
 

```
### ZeoliteExtension

> `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension`

```diff

 		<dict>
 			<key>Streams</key>
 			<array>
+				<string>GenerativeExperiences.TransparencyLog</string>
 				<string>Zeolite.Ledger.Embedding</string>
 				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	</array>
 	<key>com.apple.private.mediaanalysisd.datamanagement.embedding</key>
 	<true/>
+	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.service.mediaconversion</key>

```
### LimitedLibraryPickerViewService

> `/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService`

```diff

 		<key>value</key>
 		<string>/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService</string>
 	</dict>
+	<key>com.apple.private.contactsui</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>/Library/Finance/</string>
 		<string>/Library/Caches/Finance/</string>
 		<string>/Library/Caches/com.apple.financed/</string>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.Wallet</string>
 		<string>com.apple.passd</string>
 		<string>com.apple.Wallet.public</string>
+		<string>com.apple.AppleMediaServices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 		<string>com.apple.appinstallationmetrics.xpc</string>
 		<string>com.apple.AssetCacheLocatorService</string>
 		<string>com.apple.backboard.hid.services</string>
+		<string>com.apple.backboard.hid-services.xpc</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

```
### activitysharingd

> `/System/Library/PrivateFrameworks/ActivitySharingServices.framework/activitysharingd`

```diff

 		<string>com.apple.ActivityMonitorApp</string>
 		<string>com.apple.Fitness</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
-		<string>/private/var/mobile/Library/DeviceRegistry.state/</string>
-		<string>/private/var/mobile/Library/Health/ActivitySharing</string>
-		<string>/private/var/mobile/Library/Health/ActivitySharing/ContactsCache/</string>
+		<string>/Library/DeviceRegistry.state/</string>
+		<string>/Library/Health/ActivitySharing</string>
+		<string>/Library/Health/ActivitySharing/ContactsCache/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 		<string>App.InFocus</string>
 		<string>FrontBoard.DisplayElement</string>
 		<string>OSAnalytics.Stability.Crash</string>
+		<string>Siri.Execution</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>/Library/Caches/com.apple.pommes/</string>
 		<string>/Library/Caches/com.apple.siri.bundleservicecache.plist</string>
 		<string>/Library/Caches/com.apple.siri.conversationhandlercache.plist</string>
+		<string>/Library/Caches/com.apple.speech.localspeechrecognition/lsr_audio_dumps/</string>
 		<string>/Library/Caches/CoreSpeech/</string>
 		<string>/Library/Caches/GeoServices/</string>
 		<string>/Library/Caches/VoiceTrigger/</string>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.carousel.nonmatchingsessions</key>

 	<array>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/Library/UserFonts/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.carousel.sessionservice</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.replicatorservices</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### bird

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/bird`

```diff

 		<string>performModifyWebSharingOperation:withBlock:</string>
 		<string>getNewWebSharingIdentity:</string>
 	</array>
+	<key>com.apple.private.cloudkit.temporary.deviceCapabilities</key>
+	<true/>
 	<key>com.apple.private.cloudkit.usePublicAPSToken</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.cloudkit.temporary.deviceCapabilities</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.feedback.centralized-feedback</key>
+	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.intelligenceplatform.Knosis</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>164</string>
 		<string>165</string>
 		<string>166</string>
+		<string>182</string>
 		<string>190</string>
 		<string>191</string>
 		<string>601</string>

```
### threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.DiagnosticExtensions.extension</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.iokit.powerdxpc</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>wpantund</string>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/Logs/CrashReporter/CoreCapture/BT</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.WirelessCoexManager</string>

 	<array>
 		<string>com.apple.homed</string>
 		<string>com.apple.ccmapping_ios</string>
+		<string>com.apple.ccmapping_ios_ver_100</string>
+		<string>com.apple.ccmapping_ios_ver_200</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### DTServiceHub

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub`

```diff

 	</array>
 	<key>com.apple.private.usernotifications.notification-simulator</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.service-stats</key>
+	<true/>
 	<key>com.apple.private.xpc.service-attach</key>
 	<true/>
 	<key>com.apple.private.xpc.service-configure</key>

```
### FedStatsMLRPlugin

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/FedStatsMLRPlugin`

```diff

 		<string>Safari.WindowProxy</string>
 		<string>Siri.AssistantSuggestionFeatures</string>
 		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
+		<string>Photos.MemoryCreation</string>
+		<string>Photos.Memories.Curation</string>
+		<string>Photos.Delete</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>1547</string>
 		<string>1548</string>
 		<string>1549</string>
+		<string>1550</string>
 		<string>1551</string>
 	</array>
 	<key>platform-application</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.Accessibility</string>
+		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.srp-mdns-proxy.proxy</string>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.ThreadNetwork.xpc</string>
 		<string>com.apple.familycircle.agent</string>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.srp-mdns-proxy.proxy</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>755</string>
+		<string>351</string>
+		<string>409</string>
+		<string>753</string>
+		<string>1630</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 	<array>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 	</array>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.duetactivityscheduler</string>

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalogd</string>
 		<string>com.apple.modelcatalog.ajax</string>
-	</array>
-	<key>com.apple.security.temporary-exception.files.home-relative-path.read</key>
-	<array>
-		<string>/Library/UnifiedAssetFramework/</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 </dict>
 </plist>

```
### NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 		<string>com.apple.news.TodayFeedConfigDecoder</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 	<array>
 		<string>com.apple.momentsd</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.PersonalizedSensingService</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 	<string>com.apple.photoanalysisd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>PhotosPFL</key>
+		<key>Photos</key>
 		<dict>
 			<key>Streams</key>
 			<dict>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>Photos.Memories.Shared</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Photos.Memories.Viewed</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Photos.MemoryCreation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>Photos.Picker</key>
 				<dict>
 					<key>mode</key>

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.privatecloudcomputed</string>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>PrivateCloudCompute.RequestLog</string>
+	</array>
 	<key>com.apple.private.cloudtelemetry</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>TransparencyLogging</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>PrivateCloudCompute.RequestLog</string>
+			</array>
+		</dict>
+	</dict>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.transparency.privateCloudCompute</key>
 	<true/>
 </dict>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 		<string>Safari.MemoryFootprint</string>
 		<string>Mail.Recategorization</string>
 		<string>Photos.MemoryCreation</string>
+		<string>Photos.Curation</string>
+		<string>Photos.Delete</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 		<string>Safari.MemoryFootprint</string>
 		<string>Mail.Recategorization</string>
 		<string>Photos.MemoryCreation</string>
+		<string>Photos.Curation</string>
+		<string>Photos.Delete</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 		<string>Safari.MemoryFootprint</string>
 		<string>Mail.Recategorization</string>
 		<string>Photos.MemoryCreation</string>
+		<string>Photos.Curation</string>
+		<string>Photos.Delete</string>
 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>

```
### SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### budd

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/budd`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-keyboard</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.cloudd</string>

 		<string>com.apple.BarcodeSupport.Helper</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.SecureBackupDaemon.concurrent</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.gms.availability</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### fitcored

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored`

```diff

 		<string>Library/Cookies/</string>
 		<string>Library/HTTPStorages/</string>
 		<string>Library/Logs/com.apple.StoreServices/HTTPArchives/</string>
+		<string>Library/Caches/JetPackCache/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 		<string>com.apple.homehubd.manage</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.audioanalyticsd</string>
+		<string>com.apple.sirittsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.internal.testplatform</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.assistant.support</string>
+		<string>com.apple.assistant.backedup</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

 	<array>
 		<string>/private/var/mobile/Library/Trial/</string>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### SWTFollowUpExtension

> `/System/Library/PrivateFrameworks/TransparencyUI.framework/PlugIns/SWTFollowUpExtension.appex/SWTFollowUpExtension`

```diff

 	<array>
 		<string>com.apple.corefollowup.agent</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>group.com.apple.coreservices.useractivityd</string>
-	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceUbiquity</string>

 	</array>
 	<key>com.apple.runningboard.assertions.useractivityd</key>
 	<true/>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.coreservices.useractivityd</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.usernotificationsd</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.bulletinboard.observer</key>
 	<true/>
 	<key>com.apple.bulletinboard.settings</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.UserNotifications</string>
+	</array>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>

 	</array>
 	<key>com.apple.private.usernotifications.systemservice</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.UserNotifications</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.bulletinboard.settingsconnection</string>
 		<string>com.apple.carkit.service</string>
+		<string>com.apple.containermanagerd</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>
 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.airplay.endpoint.xpc</string>

```
### vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

 	<true/>
 	<key>com.apple.CommCenter.Messages-send</key>
 	<true/>
+	<key>com.apple.CommCenter.StormBreaker</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

```
### FocusConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.WorkflowUI.FocusConfigurationExtension</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.read</string>
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
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

```
### ind

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/ind`

```diff

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.cache</string>
+		<string>com.apple.CloudSubscriptionFeatures.geoCache</string>
+		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
+		<string>com.apple.CloudSubscriptionFeatures.ticket.cache</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>

```
### ICQFollowup

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup`

```diff

 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.backupd</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### RemoteiCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI`

```diff

 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.backupd</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### kbd

> `/System/Library/TextInput/kbd`

```diff

 		<string>com.apple.TextInput</string>
 		<string>com.apple.cfnetwork</string>
 		<string>com.apple.password-manager</string>
+		<string>com.apple.password-manager.personal</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.AttentionAwareness</string>

```
### Books

> `/private/var/staged_system_apps/Books.app/Books`

```diff

 	<array>
 		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceMediaLibrary</string>
-		<string>kTCCServicePhotos</string>
+		<string>kTCCServicePhotosAdd</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>

 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.mediaartworkd.xpc</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	<array>
 		<string>/Library/Caches/</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>IOSurfaceAcceleratorParavirtClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.searchparty.btfindingsession</string>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.locationd.synchronous</string>
 		<string>com.apple.locationd.registration</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>

```
### HealthBalanceWidgetExtension

> `/private/var/staged_system_apps/Health.app/PlugIns/HealthBalanceWidgetExtension.appex/HealthBalanceWidgetExtension`

```diff

 <dict>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionComplete</string>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.health.shared</string>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
+	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.pds.clientid</key>

 	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>
 		<string>photos.person</string>

 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/System/Library/PrivateFrameworks/PodcastsUI.framework</string>
+	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>
-		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>

```
### Stocks

> `/private/var/staged_system_apps/Stocks.app/Stocks`

```diff

 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
+	<key>com.apple.private.iokit.batterydataprecise</key>
+	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>
 	<true/>
 	<key>com.apple.private.ioreporting.access</key>

 	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
+	<key>com.apple.wifip2pd</key>
+	<true/>
 </dict>
 </plist>
 

```
### MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

 	<true/>
 	<key>com.apple.private.apfs.trim-active-file</key>
 	<true/>
-	<key>com.apple.private.oop-jit.loader</key>
-	<string>previews</string>
+	<key>com.apple.private.oop-jit.dir-manager</key>
+	<true/>
 	<key>com.apple.private.security.disk-device-access</key>
 	<true/>
 	<key>com.apple.private.vfs.snapshot</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
+	<key>com.apple.private.iokit.batterydataprecise</key>
+	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>
 	<true/>
 	<key>com.apple.private.ioreporting.access</key>

 	</array>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
+	<key>com.apple.wifip2pd</key>
+	<true/>
 	<key>vm-pressure-level</key>
 	<true/>
 </dict>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
+	<key>com.apple.private.iokit.batterydataprecise</key>
+	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>
 	<true/>
 	<key>com.apple.private.ioreporting.access</key>

 	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
+	<key>com.apple.wifip2pd</key>
+	<true/>
 </dict>
 </plist>
 

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 		<string>Location.Semantic</string>
 		<string>Device.Power.BatteryLevel</string>
 		<string>Device.Power.PluggedIn</string>
-		<string>Device.Networking.EdgeSelection</string>
 		<string>Device.TimeZone</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Location.MicroLocationVisit</string>

```
### appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.PineBoardRiseServices</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 		<string>com.apple.AudioAccessory</string>
 		<string>com.apple.PersonalAudio</string>
 		<string>com.apple.Noise</string>
+		<string>com.apple.accessory.Hearing</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 			<key>send-command</key>
 			<dict/>
 		</dict>
+		<key>eclipse</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
 		<key>gyro</key>
 		<dict>
 			<key>send-command</key>

 	<true/>
 	<key>com.apple.carkit.layer-metadata</key>
 	<true/>
+	<key>com.apple.chrono.controls</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 		<string>com.apple.accessories.transport-server</string>
 		<string>com.apple.accessories.connection-info-server</string>
 		<string>com.apple.carkit.layer-metadata</string>
+		<string>com.apple.chronoservices</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 	<array>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.CompanionLink</string>
-		<string>com.apple.biomed.sensorActivation</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 		<string>com.apple.realitysimulation.host</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.ReplayKitAngel.mach</string>
-		<string>com.apple.audio.AudioQueueServer</string>
-		<string>com.apple.audio.AudioSession</string>
-		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.managedassetsd</string>
 		<string>com.apple.surfboard.scenesessionservice</string>
 		<string>com.apple.TapToRadarKit.service</string>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.companiond</string>
+		<string>com.apple.DistributedTimers</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
-	<key>com.apple.generativeexperiences.classification</key>
-	<true/>
 	<key>com.apple.geoservices.navd.clientIdentifier</key>
 	<string>/System/Library/LocationBundles/CalendarLocation.bundle</string>
 	<key>com.apple.geoservices.navd.routehypothesis</key>

 		<string>com.apple.healthd.server</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.foundationmodels.languagemodelservice</string>
-		<string>com.apple.generativeexperiences.classification</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.nanoprefsync</string>
 	</array>

```
### gamepolicyd

> `/usr/libexec/gamepolicyd`

```diff

 	<true/>
 	<key>com.apple.private.clpc.policy</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.set-game-mode</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.modelmanager</string>

```
### hangtelemetryd

> `/usr/libexec/hangtelemetryd`

```diff

 	<array>
 		<string>com.apple.da</string>
 	</array>
+	<key>com.apple.security.ts.ipc-posix-sem</key>
+	<array>
+		<string>hangtelemetryd.onceatboot</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<string>com.apple.inputanalyticsd</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.inputanalyticsd</string>
 	<key>com.apple.security.ts.xpc-service-name</key>

```
### mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.modelmanager.assertion</key>
+	<true/>
 	<key>com.apple.modelmanager.query</key>
 	<true/>
 	<key>com.apple.private.kernel.darkboot</key>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 		<string>/private/var/code_coverage/</string>
 		<string>/private/var/run/com.apple.mobileassetd-AutoAsset-DeviceBoot-UUID</string>
 	</array>

```
### mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 	<true/>
 	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
 	<true/>
+	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
+	<true/>
+	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
+	<true/>
 	<key>com.apple.private.applesepmanager.allow</key>
 	<true/>
 	<key>com.apple.private.corerepair.attestation</key>

```
### proactiveeventtrackerd

> `/usr/libexec/proactiveeventtrackerd`

```diff

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.feedbacklogger</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.MobileAsset.SharingDeviceAssets</key>
 	<true/>
+	<key>com.apple.NeighborhoodActivityConduitService</key>
+	<true/>
 	<key>com.apple.PCAngel.HandoffUI</key>
 	<true/>
 	<key>com.apple.PairingManager.Read</key>

 		<string>com.apple.MobileTimer.alarmserver</string>
 		<string>com.apple.nanoprefsync</string>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
+		<string>com.apple.NeighborhoodActivityConduitService</string>
 		<string>com.apple.PCAngel.xpc</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.PointerUI.pointeruid.service</string>

```
### ptpd

> `/usr/libexec/ptpd`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.coremedia.cameraviewfinder</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### remoted

> `/usr/libexec/remoted`

```diff

 	</array>
 	<key>com.apple.private.RemoteServiceDiscovery.device-admin</key>
 	<true/>
+	<key>com.apple.private.network.management.data</key>
+	<true/>
 	<key>com.apple.private.settime</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
+	<key>com.apple.private.screencapturekit.noprompt</key>
+	<true/>
 	<key>com.apple.private.screencapturekit.sharingsession</key>
 	<true/>
 	<key>com.apple.private.screencapturekit.sharingsessionsystemui</key>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>Tips</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Discoverability.Signals</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.storage.CoreRoutine</key>
 	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.compute.source.user</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.icloud.searchpartyd</string>
 		<string>searchpartyd-baa-fmna-group</string>
 	</array>
 	<key>platform-application</key>

```
### symptomsd-diag

> `/usr/libexec/symptomsd-diag`

```diff

 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.cloudkit.buddyAccess</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.sysdiagnose_helper</string>
 	<key>com.apple.awdd.manager-access</key>
 	<true/>
 	<key>com.apple.corecapture.manager-access</key>
 	<true/>
+	<key>com.apple.generativeexperiences.sysdiagnose</key>
+	<true/>
 	<key>com.apple.hid.AppleDeviceManagementHIDFilter.entitlement</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.Sysdiagnose</key>

```
### videosubscriptionsd

> `/usr/libexec/videosubscriptionsd`

```diff

 	<array>
 		<string>kTCCServiceMSO</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount</string>
+		<string>/private/var/mobile/Library/Application Support/com.apple.VideoSubscriberAccount/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.VideoSubscriberAccount.AnalyticsService</string>

```
