## 🔑 Entitlements

### filesystem

### Campo

> `/Applications/Campo.app/Campo`

```diff

 	<array>
 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceReminders</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
-	<key>com.apple.private.tcc.manager.read.access</key>
-	<array>
-		<string>kTCCServiceAll</string>
-	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.weather</string>

 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/Caches/com.apple.keyboards/</string>
 		<string>/Library/Caches/GeoServices/</string>
-		<string>/Library/WebClips</string>
+		<string>/Library/WebClips/</string>
 		<string>/Library/Logs/CrashReporter/Assistant/</string>
 		<string>/Library/Logs/CrashReporter/VoiceTrigger/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>

 		<string>com.apple.internal.SpotlightAutomationTester</string>
 		<string>com.apple.carousel.flashlightxpcservice</string>
 		<string>com.apple.realitysystemsupport.hid_server_backboard</string>
+		<string>com.apple.remindd</string>
+		<string>com.apple.remindd.userInteractive</string>
 		<string>com.apple.surfboard.entityinteractionservice</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.calendar.EventKitUIRemoteUIExtension.viewservice</string>

```
### ClockAngel

> `/Applications/ClockAngel.app/ClockAngel`

```diff

 	<array>
 		<string>com.apple.sessionservices</string>
 	</array>
+	<key>com.apple.springboard.sceneaccessory.highlight</key>
+	<true/>
 </dict>
 </plist>
 

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 		<key>MainSetup</key>
 		<dict>
 			<key>bleRSSIThresholdHint</key>
-			<integer>-45</integer>
+			<integer>-48</integer>
+			<key>companionSetupFilters</key>
+			<array>
+				<dict>
+					<key>rssi</key>
+					<integer>-45</integer>
+				</dict>
+			</array>
 			<key>discoveryTypes</key>
 			<array>
 				<string>CompanionSetup</string>

```
### Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
+	<key>com.apple.keystore.device.verify</key>
+	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
+	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
 	<key>com.apple.private.corewifi.countrycode</key>

```
### Diagnostic-7004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004`

```diff

 		<string>com.apple.diskimagecorerepair</string>
 		<string>com.apple.appleh13camerad</string>
 		<string>com.apple.appleh16camerad</string>
+		<string>com.apple.cameraispd</string>
 	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>

```
### Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

 		<string>AppleGasGaugeUpdate</string>
 		<string>AppleSMCClient</string>
 		<string>AppleGasGaugeUpdateUserClient</string>
+		<string>AppleGasGaugeBeadsUpdateUserClient</string>
+		<string>AppleGasGaugeBeadsUpdate</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### Family

> `/Applications/Family.app/Family`

```diff

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.springboard-ui.client</key>
+	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### FamilyOutOfProcessUIExtension

> `/Applications/FamilyExtensionHost.app/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.familycircled</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### FamilyExtensionHost

> `/Applications/FamilyExtensionHost.app/FamilyExtensionHost`

```diff

 	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
+	<key>com.apple.private.ageRange</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	<true/>
 	<key>com.apple.private.allow-ldm-exempt-webview</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

```
### FaceTimeShareExtension

> `/Applications/InCallService.app/PlugIns/FaceTimeShareExtension.appex/FaceTimeShareExtension`

```diff

 <dict>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
-	<key>com.apple.developer.auto-elect-plugin</key>
-	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>

 	<true/>
 	<key>com.apple.private.sociallayer.shareable-content</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
-	<key>com.apple.security.files.user-selected.read-write</key>
-	<true/>
-	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.CloudSharing.SPIHelper</string>
+		<string>com.apple.CloudSharing.SPIHelper-iOS</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
 	<true/>
+	<key>com.apple.idle-timer-services</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.microlocation.connection</key>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.private.alarmkit.bundleIdentifier</key>
 	<string>com.apple.reminders</string>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### MusicRecognition

> `/Applications/MusicRecognition.app/MusicRecognition`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.mediaremote.request-bless</key>
+	<true/>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### PeopleMessageService

> `/Applications/PeopleMessageService.app/PeopleMessageService`

```diff

 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### PosterBoard

> `/Applications/PosterBoard.app/PosterBoard`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.lightsourcesupport.lightstate</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobilecal</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.chronod</string>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.accessibility.AccessibilityPersonalVoiceUsageOverride</key>
 	<true/>
+	<key>com.apple.accessibility.axassets</key>
+	<true/>
 	<key>com.apple.accessibility.physicalinteraction.client</key>
 	<true/>
 	<key>com.apple.accessoryupdater.launchauhelper.entitled</key>

 	<true/>
 	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
 	<true/>
+	<key>com.apple.generativeexperiences.agentSessionStore</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>

 		<string>AppLaunch</string>
 		<string>Device.Display.Backlight</string>
 		<string>FindMyLocationChange</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

 		<string>group.com.apple.SuggestedImage.SharedSecureContainer</string>
 		<string>group.com.apple.GenerativePlayground</string>
 		<string>group.com.apple.feedback</string>
+		<string>group.com.apple.TVRemote</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
+		<string>com.apple.generativeexperiences.agentSessionStore</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>

 	<true/>
 	<key>com.apple.sharing.Services</key>
 	<true/>
+	<key>com.apple.sharing.airdrop.readonly</key>
+	<true/>
 	<key>com.apple.shortcuts.automation-confirmation-reset</key>
 	<true/>
 	<key>com.apple.shortcuts.background-running</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 		<string>/Library/Caches/com.apple.ClipServices/</string>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 		<string>/Library/Safari/PasswordBreachStore.plist</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

```
### ScreenTimeWidgetExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.argos.availibility-bypass</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

```
### ServicesPaymentAngel

> `/Applications/ServicesPaymentAngel.app/ServicesPaymentAngel`

```diff

 	<true/>
 	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
+	<key>com.apple.private.jetpackassetd</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.PassbookUISceneService.remote-ui</string>
 		<string>com.apple.TapToRadarKit.service</string>
+		<string>com.apple.jetpackassetd.xpc</string>
 	</array>
 	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>
 	<true/>

```
### StoreKitUISceneService

> `/Applications/StoreKitUISceneService.app/StoreKitUISceneService`

```diff

 	<true/>
 	<key>com.apple.storekit.private-merchandising-ui-host</key>
 	<true/>
+	<key>com.apple.surfboard-ui.client</key>
+	<true/>
+	<key>com.apple.surfboard.allow-scene-requests-while-backgrounded</key>
+	<true/>
+	<key>com.apple.surfboard.placement-client</key>
+	<true/>
+	<key>com.apple.surfboard.scenesession-updates</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### iCloud

> `/Applications/iCloud.app/iCloud`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.icloud-extended-share-access</key>
+	<array>
+		<string>InProcessShareAccessRequests</string>
+	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.Feedback.DraftingExtension.viewservice</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.photos.service</string>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.servicesintelligenced</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/Library/Caches/</string>

```
### PhotosViewService

> `/System/Library/CoreServices/PhotosViewService.app/PhotosViewService`

```diff

 	<true/>
 	<key>com.apple.private.photos.allowcollectionshare</key>
 	<true/>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.iokit.powersource-control</key>
 	<true/>
+	<key>com.apple.private.iokit.preventSystemSleepSecurityIndicator</key>
+	<true/>
 	<key>com.apple.private.kernel.darkboot</key>
 	<true/>
 	<key>com.apple.private.kernel.jetsam</key>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<true/>
 	<key>com.apple.carousel.backlightaccess</key>
 	<true/>
+	<key>com.apple.carousel.backlightcommand</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-opus-codec</key>
 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>

```

### 🆕 AgeVerificationExtension

> `/System/Library/ExtensionKit/Extensions/AgeVerificationExtension.appex/AgeVerificationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/tmp/com.apple.AppleMediaServices/</string>
	</array>
</dict>
</plist>

```
### AskPermissionAskToResponseExtension

> `/System/Library/ExtensionKit/Extensions/AskPermissionAskToResponseExtension.appex/AskPermissionAskToResponseExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.xpc.amsengagementd</string>
-		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.storekit.client-override</key>
 	<true/>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.assistant.shared</string>
+	</array>
 	<key>com.apple.private.softwareupdate.preferences</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.assistant.shared</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.feedbacklogger/</string>

```
### FamilyOutOfProcessUIExtension

> `/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.familycircled</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 		<string>GenerativeExperiences.PromptTags</string>
 		<string>GenerativeExperiences.WritingToolsFeatures.Requests</string>
 		<string>GenerativeExperiences.WritingToolsFeatures.Metadata</string>
+		<string>Siri.SELFProcessedEvent</string>
+		<string>IntelligenceFlow.Transcript.Datastream</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/FedStatsPluginDynamic`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>Call-Context-Cards</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>CommApps.CallIntelligence.CallContextCardsFedStats</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Camera-Auto-Focus</key>
 		<dict>
 			<key>Streams</key>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/FedStatsPluginStatic`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>Call-Context-Cards</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>CommApps.CallIntelligence.CallContextCardsFedStats</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Camera-Auto-Focus</key>
 		<dict>
 			<key>Streams</key>

```
### FinanceDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/FinanceDiagnosticExtension.appex/FinanceDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
-	<key>com.apple.finance.private</key>
+	<key>com.apple.finance.internal.read</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<string></string>

```
### MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/MapsIntents`

```diff

 	<string>com.apple.Maps</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.Maps.MapsSync.store</string>
+		<string>com.apple.Maps.MapsSync.service</string>
+	</array>
 </dict>
 </plist>
 

```
### OrderExtractionDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/OrderExtractionDiagnosticExtension.appex/OrderExtractionDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
-	<key>com.apple.finance.private</key>
+	<key>com.apple.finance.internal.read</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.finance.OrderExtractionDiagnosticExtension</string>

```
### PhotoPicker

> `/System/Library/ExtensionKit/Extensions/PhotoPicker.appex/PhotoPicker`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+		<string>com.apple.communicationSafetySettings</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.photos.picker</string>
 		<string>com.apple.restrictionspassword</string>
 		<string>com.apple.springboard</string>
 	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
-	<array>
-		<string>com.apple.communicationSafetySettings</string>
-	</array>
 	<key>com.apple.sensitivecontentanalysis.service</key>
 	<array>
 		<string>photos</string>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/PhotosPicker`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.background-tasks.continued-processing.inference</key>
+	<true/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### ReceiptsExtractionDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/ReceiptsExtractionDiagnosticExtension.appex/ReceiptsExtractionDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
-	<key>com.apple.finance.private</key>
+	<key>com.apple.finance.internal.read</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.finance.ReceiptsExtractionDiagnosticExtension</string>

```

### 🆕 SafariSearchUploadWorker

> `/System/Library/ExtensionKit/Extensions/SafariSearchUploadWorker.appex/SafariSearchUploadWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1821501079</string>
	<key>application-identifier</key>
	<string>com.apple.unilog.SafariSearchUploadWorker</string>
	<key>com.apple.developer.networking.multipath_extended</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Unilog.SafariSearch.Aggregation</string>
	</array>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.unilog.datacollector.SafariSearchUploadWorker</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>UnilogSafariSearchAggregation</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.SafariSearch.Aggregation</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.aiml.unilog.healthTelemetry</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.HealthAggregatedSummary</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Unilog.HealthTelemetry</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.SafariSearchUploadWorker</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SafariSearchUploadWorker</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SafariSearchUploadWorker</string>
	</array>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.siri.osprey</string>
	</array>
</dict>
</plist>

```

### 🆕 SafariUsageRetentionExtension

> `/System/Library/ExtensionKit/Extensions/SafariUsageRetentionExtension.appex/SafariUsageRetentionExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.safari.SafariUsageRetentionExtension</string>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.safari.SafariUsageRetentionExtension</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SafariUsageRetention</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Lighthouse.Ledger.TaskCustomEvent</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Unilog.SafariSearch.Aggregation</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Unilog.SafariSearch.LongTermAggregationId</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Unilog.SafariSearch.Stage</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.mlhost.allowedDictionaryGroups</key>
	<array>
		<string>SafariUsageRetention</string>
	</array>
	<key>com.apple.private.mlhost.dictionaryDelete</key>
	<true/>
	<key>com.apple.private.mlhost.dictionaryRead</key>
	<true/>
	<key>com.apple.private.mlhost.dictionaryWrite</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.mlhostd.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.mlhostd.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant.support</string>
	</array>
</dict>
</plist>

```
### ScreenTimeAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/ScreenTimeAppIntentsExtension`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### SiriAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/SiriAutoEvalPlugin.appex/SiriAutoEvalPlugin`

```diff

 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeExperiences.PromptTags</string>
 		<string>Siri.SELFProcessedEvent</string>
+		<string>IntelligenceFlow.Transcript.Datastream</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.background-tasks.continued-processing.inference</key>
+	<true/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```

### 🆕 WritingToolsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/WritingToolsAppIntentsExtension.appex/WritingToolsAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.WritingTools.WritingToolsAppIntentsExtension</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.WritingTools.WritingToolsAppIntentsExtension</string>
	<key>com.apple.feedbackd.remote-evaluation</key>
	<true/>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
	<true/>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.sage.textcomposition</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.sage.textcomposition</string>
		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.generativeexperiences.summarization</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.generativeassistantsettings</string>
		<string>com.apple.generativepartnerservicesettings</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.extensionkitservice</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.gms.availability</string>
	</array>
	<key>com.apple.shortcuts.stepwise-execution</key>
	<true/>
	<key>com.apple.shortcuts.variable-injection</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
</dict>
</plist>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.coreidv.system-notifications.accounts</key>

```
### appmanagedfeaturesd

> `/System/Library/Frameworks/AppManagedFeatures.framework/Support/appmanagedfeaturesd`

```diff

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 	<key>com.apple.usernotifications.always-show</key>
 	<true/>
 	<key>com.apple.usernotifications.critical-alerts</key>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.imcore.imdpersistence.database-access</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.assetsd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

```
### ContactViewViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### ContactsViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.developer.devicecheck.appattest-environment</key>
+	<string>production</string>
 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
 	<array>
 		<string>com.apple.pay.finance.development</string>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.devicecheck.daemon-client</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.finance.private</key>

 		<string>com.apple.WalletBlastDoorService</string>
 		<string>com.apple.email.maild</string>
 		<string>com.apple.frauddefensed</string>
+		<string>com.apple.devicecheckd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.Wallet</string>
 		<string>com.apple.financed</string>
 		<string>com.apple.FinanceKit</string>
+		<string>com.apple.AppAttest.client</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService`

```diff

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fpsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 	<key>com.apple.siri.external_request</key>
 	<true/>
 	<key>com.apple.smoot.subscriptionservice</key>

```
### TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.Keychains</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```

### 🆕 SpeechEncryptedLogsDiagnostic

> `/System/Library/Frameworks/Speech.framework/PlugIns/SpeechEncryptedLogsDiagnostic.appex/SpeechEncryptedLogsDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.logging.admin</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/</string>
		<string>/Library/Logs/CrashReporter/Assistant/</string>
		<string>/Library/Logs/CrashReporter/VoiceTrigger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.logd.admin</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.icl</string>
	</array>
</dict>
</plist>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.speech.localspeechrecognition</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
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
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

 	</array>
 	<key>com.apple.private.cloudtelemetry</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>

```
### DeviceActivityReportService

> `/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```

### 🆕 binary.metallib

> `/System/Library/PrivateFrameworks/AgentCanvasUICore.framework/binary.metallib`

- No entitlements *(yet)*
### appconduitd

> `/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd`

```diff

 		<string>GetAppMetadata</string>
 		<string>WaitForSystemAppMigrationToComplete</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/Truth.plist</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.installcoordinationd</string>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	</array>
 	<key>com.apple.companion-authentication.store-purchase</key>
 	<true/>
+	<key>com.apple.coreidvd.digital-presentment.firstpartyclient</key>
+	<true/>
 	<key>com.apple.coreidvd.document-upload</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.in-app-identity-presentment</key>
+	<dict>
+		<key>document-types</key>
+		<array>
+			<string>jp-national-id-card</string>
+			<string>photo-id</string>
+			<string>us-drivers-license</string>
+		</array>
+		<key>elements</key>
+		<array>
+			<string>age</string>
+			<string>given-name</string>
+			<string>family-name</string>
+			<string>address</string>
+			<string>issuing-authority</string>
+			<string>document-expiration-date</string>
+			<string>document-issue-date</string>
+			<string>document-number</string>
+			<string>driving-privileges</string>
+			<string>date-of-birth</string>
+		</array>
+	</dict>
+	<key>com.apple.developer.in-app-identity-presentment.merchant-identifiers</key>
+	<array>
+		<string>com.apple.ams-identity-verification</string>
+		<string>com.apple.asa-identity-verification</string>
+	</array>
 	<key>com.apple.developer.networking.wifi-info</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppleMediaServices</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.coreidvd.digital-presentment.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```

### 🆕 ANELargeModelCompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANELargeModelCompilerService.xpc/ANELargeModelCompilerService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.private.coreml.decypt_allowed</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.rootless.storage.ane_model_cache</key>
	<true/>
	<key>com.apple.rootless.storage.triald</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>ANECompilerService</string>
	</array>
</dict>
</plist>

```
### askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond`

```diff

 	<array>
 		<string>AskToBuy</string>
 	</array>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.people</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siri.SiriAudioDESPlugin</key>
 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siri.SiriVideoDESPlugin</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.TimeAppServices.timerclient</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.chrono.controls</key>
+	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<true/>
 	<key>com.apple.duet.appPreference.prediction</key>
 	<true/>
+	<key>com.apple.eligibilityd</key>
+	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>

 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.carkit.app.service</string>
 		<string>com.apple.CarPlayApp.service</string>
+		<string>com.apple.chronoservices</string>
 		<string>com.apple.ckdiscretionaryd</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

 		<string>com.apple.corespeech.speechmodeltraining.xpc</string>
 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.eligibilityd</string>
 		<string>com.apple.fairplayd</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.fairplayd.xpc</string>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.announce</string>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.carplay</string>
 		<string>com.apple.ClarityUI</string>
 		<string>com.apple.CloudKit</string>

 		<string>com.apple.homed</string>
 		<string>com.apple.homed.notbackedup</string>
 		<string>com.apple.intelligenceflow</string>
+		<string>com.apple.ironwood.support</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.keyboard.preferences</string>

```
### bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

```diff

 	<true/>
 	<key>com.apple.private.MobileContainerManager.stageSharedContent</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+		<string>SerialNumber</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

 	<array>
 		<string>group.com.apple.iBooks</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Media/Books/</string>
+		<string>/Media/ManagedPurchases/</string>
+		<string>/Library/Caches/com.apple.bookassetd/</string>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
+		<string>/Library/HTTPStorages/com.apple.bookassetd/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.backupd</string>
 		<string>com.apple.symptom_analytics</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.itunesstored</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.bookassetd</string>
+		<string>com.apple.AppleMediaServices</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOMobileFramebufferUserClient</string>

 		<string>com_apple_driver_FairPlayIOKitUserClient</string>
 		<string>AppleJPEGDriverUserClient</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.media.shared.books</string>
 		<string>systemgroup.com.apple.media.books.managed</string>
 	</array>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.bookassetd</string>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

 	<array>
 		<string>apple</string>
 	</array>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### cksharingmanagementd

> `/System/Library/PrivateFrameworks/CKSharingManagementDaemon.framework/Support/cksharingmanagementd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.ts.daemon-container</key>

```
### calaccessd

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/Support/calaccessd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.CalendarUI</string>
+	</array>
 	<key>com.apple.private.notificationcenter-system</key>
 	<array>
 		<dict>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.linkd.application-service</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
+		<string>com.apple.deviceconfigurationd.consumer</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<array>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 		<string>/Library/UserFonts/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>

```
### cloudd

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.utility</key>
 	<true/>
 	<key>com.apple.cdp.walrus</key>

```
### SpeechProfileDiagnostic

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/PlugIns/SpeechProfileDiagnostic.appex/SpeechProfileDiagnostic`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/SiriVocabulary/</string>
+		<string>/Library/Assistant/SpeechMaintenance/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 				<string>TextUnderstanding.Output.Topic</string>
 			</array>
 		</dict>
+		<key>com.apple.proactive.suggestions.SocialHighlights</key>
+		<dict>
+			<key>Views</key>
+			<array>
+				<string>siriRemembers</string>
+			</array>
+		</dict>
 		<key>com.apple.suggestions.TextUnderstandingObserver</key>
 		<dict>
 			<key>Streams</key>

```
### CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

```diff

 		<string>com.apple.preferred.network</string>
 		<string>com.apple.frozen.network</string>
 		<string>apple</string>
+		<string>com.apple.thread.datasetmacos</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.bringUpDaemon</key>
+	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
 	<key>com.apple.private.familycircle</key>

 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>
+		<string>kTCCServiceSiri</string>
 		<string>kTCCServiceUbiquity</string>
 	</array>
 	<key>com.apple.private.ubiquity-kvstore-access</key>

```
### ScreenTimeDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ScreenTimeDiagnosticExtension.appex/ScreenTimeDiagnosticExtension`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService`

```diff

 	<true/>
 	<key>com.apple.private.apfs.clonegroup</key>
 	<true/>
+	<key>com.apple.private.apfs.get-graft-info</key>
+	<true/>
 	<key>com.apple.private.apfs.get_purgeable_bulk_info</key>
 	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>

```
### donotdisturbd

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd`

```diff

 	<array>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### SaveToFiles

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles`

```diff

 	<string>com.apple.DocumentManagerUICore.SaveToFiles</string>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.librarian.unrestricted-container-access</key>
 	<true/>
 	<key>com.apple.private.metadata.exattrs</key>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.DocumentManager.Service

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service`

```diff

 	<true/>
 	<key>com.apple.private.diskarbitrationd.access</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
 	<key>com.apple.private.interstellar.data-access</key>

 		<string>com.apple.lsd.modifydb</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.SmartNameSuggestionsService</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 	<array>
 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 		<string>CLIENT_ENTITLEMENT</string>
+		<string>SERVICE_ENTITLEMENT</string>
 	</array>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
+	<key>com.apple.developer.weatherkit</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.generativelearningd.learningGeneration</key>

```
### healthrecordsd

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/healthrecordsd`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.health.records/</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-group-containers</key>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 		<string>com.apple.ids</string>
 		<string>com.apple.RelevancePlatform.ConsiderateVolume</string>
 		<string>com.apple.bluetooth</string>
+		<string>com.apple.TelephonyUtilities</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
-	<key>com.apple.private.AppleMediaServices</key>
-	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	</array>
 	<key>com.apple.private.appintents.transcript.donation-identifier-override</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.aps-environment</key>

```
### identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

 	<true/>
 	<key>com.apple.CoreTelephony.DataUsageInfo.allow</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.StatusKit.presence.clientID</key>
 	<string>identityservicesd</string>
 	<key>com.apple.StatusKit.publish.allTypes</key>

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.aps-priority-boost</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
+	<key>com.apple.mediasetupd.client</key>
+	<true/>
 	<key>com.apple.mobilemail.mailservices</key>
 	<true/>
 	<key>com.apple.modelcatalog.full-access</key>

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.screencapturekit.noprompt</key>
 	<true/>
+	<key>com.apple.private.searchtoold.search</key>
+	<true/>
 	<key>com.apple.private.security.arkit</key>
 	<array>
 		<string>allowImmersiveExemption</string>

 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceSpeechRecognition</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceSiri</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.surfboard.entityinteractionservice</string>
 		<string>com.apple.surfboard.environmentservice</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>

 		<string>com.apple.siri.turn.service.xpc</string>
 		<string>com.apple.powerexperienced.resourceusage</string>
 		<string>com.apple.private.corewifi.readonly-xpc</string>
+		<string>com.apple.CoreAuthentication.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### intelligencetasksd

> `/System/Library/PrivateFrameworks/IntelligenceTasksEngine.framework/Support/intelligencetasksd`

```diff

 	<string>com.apple.intelligencetasksd</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.intelligencetasksd</string>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.intelligencetasksd</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```
### mapspushd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd`

```diff

 	<true/>
 	<key>com.apple.maps.virtualgarage.vehicles</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.navigation.spi</key>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>
+		<string>com.apple.Maps.mapspushd</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService`

```diff

 	<array>
 		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
 	</array>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
 	<true/>
+	<key>com.apple.private.CacheDelete</key>
+	<array>
+		<string>CLIENT_ENTITLEMENT</string>
+		<string>PURGE_ENTITLEMENT</string>
+		<string>PURGE_SPECIAL_CASE_ENTITLEMENT</string>
+	</array>
 	<key>com.apple.private.CallHistory.read</key>
 	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>

```
### com.apple.MobileAsset.DownloadService.Builtin

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/XPCServices/com.apple.MobileAsset.DownloadService.Builtin.xpc/com.apple.MobileAsset.DownloadService.Builtin`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read</key>
+	<array>
+		<string>/Library/Preferences/com.apple.networkextension.uuidcache.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>

```
### MBPrebuddyFollowUpExtension

> `/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBPrebuddyFollowUpExtension.appex/MBPrebuddyFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

```
### NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

 	<string>com.apple.NPKCompanionAgent</string>
 	<key>com.apple.NPKCompanionAgent.client</key>
 	<true/>
+	<key>com.apple.NanoPassbook.IDVRemoteDeviceService.client</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/searchtoold`

```diff

 		<string>loiEntityRelevanceRanking</string>
 		<string>standardFeatureView</string>
 	</array>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>

 		<string>com.apple.pommes</string>
 		<string>com.apple.generativesearch</string>
 		<string>com.apple.homed</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 	<true/>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.amsondevicestoraged</string>

 	<array>
 		<string>com.apple.chrono.event-service.amsondevicestoraged</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.servicesanalytics</string>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.photos.service</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.suggestions</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.OnDeviceStorage</string>

```
### com.apple.PerformanceTrace.PerformanceTraceService

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/com.apple.PerformanceTrace.PerformanceTraceService`

```diff

 	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.private.swiftuitracingsupport.record</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.PerformanceTrace.notifications</string>

```
### com.apple.photos.PCCService

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/XPCServices/com.apple.photos.PCCService.xpc/com.apple.photos.PCCService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.photos.PCCService</string>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

 	<array>
 		<string>App.InFocus</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```diff

 	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
-		<string>App.MediaUsage</string>
-		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>App.MediaUsage</string>
+		<string>App.WebUsage</string>
 		<string>Family.ScreenTime.ChildState</string>
 	</array>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceReminders</string>
 	</array>
-	<key>com.apple.private.tcc.manager.read.access</key>
+	<key>com.apple.private.tcc.events.subscriber</key>
+	<true/>
+	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>

```
### SeymourAppStoreService

> `/System/Library/PrivateFrameworks/SeymourServicesCore.framework/XPCServices/SeymourAppStoreService.xpc/SeymourAppStoreService`

```diff

 	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>1699554724</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### SeymourMetricsService

> `/System/Library/PrivateFrameworks/SeymourServicesCore.framework/XPCServices/SeymourMetricsService.xpc/SeymourMetricsService`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>1699554724</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### siriappintentsd

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/siriappintentsd`

```diff

 		<string>AppleIntelligence.Reporting.Invocation.Step</string>
 		<string>SessionResumptionEventBundle</string>
 		<string>SecurityValidationEvent</string>
+		<string>TokenGeneration.Inference.Requests</string>
 	</array>
 	<key>com.apple.private.corespotlight.skgupdater</key>
 	<true/>

 				<string>AppleIntelligence.Reporting.Invocation.Step</string>
 			</array>
 		</dict>
+		<key>SiriHeliosTokenGenerationReplay</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>TokenGeneration.Inference.Requests</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.logging.admin</key>
 	<true/>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 	<true/>
 	<key>com.apple.private.kernel.work-interval</key>
 	<true/>
+	<key>com.apple.private.personas.propagate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### stickersd

> `/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
-		<string>com.apple.EmojiPreferences</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.EmojiPreferences</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```

### 🆕 TextToSpeechKonaSupport

> `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/TextToSpeechKonaSupport`

- No entitlements *(yet)*

### 🆕 UARPAssetManagerServiceiCloud

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/XPCServices/UARPAssetManagerServiceiCloud.xpc/UARPAssetManagerServiceiCloud`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.MobileAccessoryUpdater.fudHelperAgent</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>cellular-plan</string>
		<string>public-cellular-plan</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>InverseDeviceID</string>
	</array>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.systemLaunchDaemonAccess</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/db/accessoryupdater/</string>
		<string>/private/var/run/</string>
		<string>/private/var/root/Library/Caches/</string>
		<string>/private/var/root/Library/HTTPStorages/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.commcenter.coretelephony.xpc</string>
		<string>com.apple.frontboard.systemappservices</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.ACMobileShim</string>
		<string>com.apple.AUDeveloperSettings</string>
		<string>com.apple.GEO</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.accessoryupdaterd</string>
		<string>com.apple.AUDeveloperSettings</string>
		<string>com.apple.security</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.asset-access</key>
	<true/>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>iCloud Services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

 			<array>
 				<string>App.MediaUsage</string>
 				<string>App.WebUsage</string>
+				<string>Intelligence.Usage</string>
 				<string>Media.NowPlaying</string>
 				<string>ScreenTime.AppUsage</string>
 			</array>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
+	<key>com.apple.private.notificationcenter.preferences</key>
+	<true/>
 	<key>com.apple.private.replicator.controller</key>
 	<true/>
 	<key>com.apple.private.replicator.dataProvider</key>

```
### visualintelligenced

> `/System/Library/PrivateFrameworks/VisualIntelligenceServices.framework/visualintelligenced`

```diff

 	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
+	<key>com.apple.aned.private.processModelShare.allow</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.visualintelligenced</string>
 	<key>com.apple.argos.availibility-bypass</key>

 	<string>com.apple.visualintelligenced</string>
 	<key>com.apple.private.payment.remote-network-payment-initiate</key>
 	<true/>
-	<key>com.apple.private.photos.service.librarymanagement</key>
-	<true/>
 	<key>com.apple.private.proactive.visual-action-prediction</key>
 	<true/>
 	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>

```
### voicememod

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/Support/voicememod`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.cloudkit.tccmanager</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.callhistoryd.service</key>
 	<true/>
 	<key>com.apple.cards.all-access</key>

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.nfcd.hwmanager</key>
+	<true/>
+	<key>com.apple.nfcd.session.reader.internal</key>
+	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>

 	<true/>
 	<key>com.apple.private.WebClips.read-write</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appintents.update-app-shortcut-apps</key>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.mode.assertion.user-requested.client-identifiers</key>

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.feature-availability.read</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>App.Intent</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>CarPlay.Connected</key>
 				<dict>
 					<key>mode</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.shortcuts</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>Mail</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.modelmanager</string>
+		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.passd.payment</string>
+		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.proactiveagentplatform.orchestrator</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.shortcuts.view-service</string>

 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>com.apple.HearingAids</string>
+		<string>com.apple.SoundDetection</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.appleaccount</string>
+		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.mediaaccessibility</string>
 		<string>com.apple.modelcatalog.ajax</string>

 	</array>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
+	<key>com.apple.wifi.manager-access</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>V568VXD5P8.is.workflow.my.app</string>

```
### matd

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/matd`

```diff

 	<array>
 		<string>preferences.plist</string>
 	</array>
+	<key>com.apple.USBCEntitlement</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleHPMARM</string>
+		<string>IOAccessoryManagerUserClient</string>
 		<string>IOUSBDeviceInterfaceUserClient</string>
 	</array>
 	<key>com.apple.wifi.manager-access</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>

 	<array>
 		<string>com.apple.private.alloy.shortcuts</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.shortcuts</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>DataActionsUsecase</key>

 				<string>IntelligencePlatform.Entity</string>
 			</array>
 		</dict>
+		<key>ToolKit.Sync</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.Intents.IndexedEnum</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>ToolKit.Tool</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.shortcuts</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>Mail</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MapKit.SnapshotService</string>
 		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
+		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.TextInput.rdt</string>
 		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.accessibility.voices</string>

 		<string>com.apple.audio.AudioConverterService</string>
 		<string>com.apple.audio.AudioUnitServer</string>
 		<string>com.apple.backlightd</string>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>

 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.intelligenceflow.contextTool</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>

```

### 🆕 FollowUpTemporary

> `/System/Library/Settings/FollowUpTemporary.settings/FollowUpTemporary`

- No entitlements *(yet)*

### 🆕 MusicRecognitionUIPlugin

> `/System/Library/Snippets/UIPlugins/MusicRecognitionUIPlugin.bundle/MusicRecognitionUIPlugin`

- No entitlements *(yet)*

### 🆕 com.apple.RemotePairing.AuditActivityNotifications

> `/System/Library/UserNotifications/Bundles/com.apple.RemotePairing.AuditActivityNotifications.bundle/com.apple.RemotePairing.AuditActivityNotifications`

- No entitlements *(yet)*
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.background-tasks.continued-processing.inference</key>
+	<true/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 			</dict>
 		</dict>
 	</dict>
-	<key>com.apple.private.internal-style-asam</key>
-	<true/>
 	<key>com.apple.private.jetpackassetd</key>
 	<true/>
 	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chrono.controls</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 		<string>com.apple.userprofiles</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.odi.legacySPIService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 	<array>
 		<string></string>
 	</array>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.extension-host.photo-editing</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

 	<array>
 		<string>analysis</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.camera</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.excludes-extensions</key>

```
### LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	<array>
 		<string></string>
 	</array>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.extension-host.photo-editing</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

 	<array>
 		<string>analysis</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.camera</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.excludes-extensions</key>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<array>
 		<string>/System/Library/PrivateFrameworks/ContactsUICore.framework</string>
 	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
 	<key>com.apple.private.biome.writer</key>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.ind.client</key>

 		<string>com.apple.lsd.modifydb</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.SmartNameSuggestionsService</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.servicesintelligenced</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 	<true/>
 	<key>com.apple.locationd.cardiohealthdata-read</key>
 	<true/>
+	<key>com.apple.locationd.cardiohealthdata-write</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>

```

### 🆕 HomeCoreSpotlightDelegateExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeCoreSpotlightDelegateExtension.appex/HomeCoreSpotlightDelegateExtension`

- No entitlements *(yet)*
### HomeEnergyWidgetsExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.energykit</key>
 	<true/>
 	<key>com.apple.private.homeenergy</key>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.wpc.energyservices.keychain</string>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
+	<true/>
+	<key>com.apple.generativeexperiences.ExternalProviderService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
+		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.ciphermld</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
+		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.das.private.bgtask.continuedprocessing</key>
 	<true/>
 	<key>com.apple.developer.declared-age-range</key>

```
### Measure

> `/private/var/staged_system_apps/Measure.app/Measure`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.measure</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.measure</string>
 	<key>com.apple.pearl.iokit-user-access</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### MobileCal

> `/private/var/staged_system_apps/MobileCal.app/MobileCal`

```diff

 	</array>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

 	<array>
 		<string>com.apple.communicationtrustd.service</string>
 		<string>com.apple.assistant.cdm</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.private.accounts.configuration-resolve</key>
 	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/AppleInternal/Library/Frameworks/ContextStagingIntents.framework</string>
+	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### com.apple.mobilenotes.SharingExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<array>
 		<string>/System/Library/PrivateFrameworks/ChatKit.framework</string>
 	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+		<string>com.apple.NanoContacts</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.safari</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>SafariUsageDonation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Unilog.SafariSearch.Stage</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.aiml.unilog.healthTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Unilog.HealthTelemetry</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>siriRemembers</string>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.photos.XPCStoreOptIn</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Safari/PasswordBreachStore.plist</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 	<true/>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.photos.service.debug</key>
 	<true/>
 	<key>com.apple.private.photos.service.diagnostics</key>

```
### PhotosReliveWidget

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget`

```diff

 		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
 		<string>com.apple.chronoservices</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+	</array>
 </dict>
 </plist>
 

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.developer.declared-age-range</key>
 	<true/>
+	<key>com.apple.developer.networking.carrier-constrained.app-optimized</key>
+	<false/>
+	<key>com.apple.developer.networking.carrier-constrained.appcategory</key>
+	<string>podcast-8017</string>
+	<key>com.apple.developer.networking.non-terrestrial.app-optimized</key>
+	<false/>
+	<key>com.apple.developer.networking.non-terrestrial.appcategory</key>
+	<string>podcast-8017</string>
 	<key>com.apple.developer.pass-type-identifiers</key>
 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>

 	<array>
 		<string>/private/var/mobile/Media/Podcasts/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>Library/UserConfigurationProfiles/Truth.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/DeviceRegistry/</string>

```
### Reminders

> `/private/var/staged_system_apps/Reminders.app/Reminders`

```diff

 	<string>production</string>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>

 	</array>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.feature-availability.read</key>

 				<string>IntelligencePlatform.Entity</string>
 			</array>
 		</dict>
+		<key>com.apple.shortcuts</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>Mail</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.intelligenceplatform.InternalBiome</string>

 		<string>com.apple.SoundDetection</string>
 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.spotlightui</string>

```
### SiriApp

> `/private/var/staged_system_apps/SiriApp.app/SiriApp`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.SiriApp</string>
+	<key>com.apple.assistantd.odeon-remote</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.private.appintents.trusted-entity-identifier</key>

```
### Tips

> `/private/var/staged_system_apps/Tips.app/Tips`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.tips</string>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### launchd

> `/sbin/launchd`

```diff

 	<true/>
 	<key>com.apple.private.delegate-signals</key>
 	<true/>
+	<key>com.apple.private.endpoint-security.submit.bootstrap</key>
+	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>
 	<true/>
 	<key>com.apple.private.kernel.darkboot</key>

```
### fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.vfs.authorized-access</key>
 	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>

```
### BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

```
### BatteryDischargeService

> `/usr/libexec/BatteryDischargeService`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.powerd.lowpowermode.allow</key>
+	<true/>
+	<key>com.apple.powerui.smartcharging</key>
+	<true/>
+	<key>com.apple.private.iokit.battery-shipping-charge-limit</key>
+	<true/>
+	<key>com.apple.private.iokit.powermanagement</key>
+	<true/>
+	<key>com.apple.private.xpc.launchd.mach-service.com.apple.BatteryDischargeService</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.powerd.lowpowermode</string>
+	</array>
+</dict>
+</plist>
 

```
### ContinuityCaptureAgent

> `/usr/libexec/ContinuityCaptureAgent`

```diff

 	<true/>
 	<key>com.apple.networkd_privileged</key>
 	<true/>
+	<key>com.apple.networkrelay.devices.read</key>
+	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
 	<key>com.apple.private.cmio.extension.configuration</key>

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ak.auth.xpc</string>

```
### aned

> `/usr/libexec/aned`

```diff

 <dict>
 	<key>com.apple.ANECompilerService.allow</key>
 	<true/>
+	<key>com.apple.ANELargeModelCompilerService.allow</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.ane.iokit-user-access</key>

```
### betaenrollmentd

> `/usr/libexec/betaenrollmentd`

```diff

 	<array>
 		<string>Removal</string>
 	</array>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>BuildVersion</string>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 		<string>com.apple.private.alloy.contextsync</string>
 		<string>com.apple.private.alloy.contextsync.local</string>
 	</array>
+	<key>com.apple.private.intelligencetasks.sets.maintenance.client</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.userprofiles</string>
-		<string>com.apple.cascade.Maintenance</string>
+		<string>com.apple.intelligencetasksd.sets.Maintenance</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 		<string>/Media/DCIM/</string>
 		<string>/Media/Deferred/</string>
 		<string>/Media/PhotoData/CaptureDebug/</string>
+		<string>/Media/PhotoData/Photos.sqlite</string>
+		<string>/Media/PhotoData/Photos.sqlite-shm</string>
+		<string>/Media/PhotoData/Photos.sqlite-wal</string>
 		<string>/Library/Caches/com.apple.cameracaptured/</string>
 		<string>/Library/Caches/com.apple.deferredmediad/</string>
 		<string>/Library/Caches/CoreMotion/CoreMotion.log</string>

```
### cameraispd

> `/usr/libexec/cameraispd`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>VADResourceArbiterUserClient</string>
 		<string>AppleCameraPhotonDetectorUserClient</string>
-		<string>IOUserClient</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### coreidvd

> `/usr/libexec/coreidvd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.TextUnderstanding.process</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>

 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.businessservicesd</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.TextUnderstanding.process</string>
 	</array>
 	<key>com.apple.security.system-group-containers</key>
 	<array>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.systemstats.analysis-client</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCalendar</string>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 			<key>Search</key>
 			<array>
 				<string>SiriTranscript</string>
+				<string>SiriTranscriptConversation</string>
 			</array>
 			<key>Streams</key>
 			<array>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.pencil.pairing.services</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### hybridsearchd

> `/usr/libexec/hybridsearchd`

```diff

 	<array/>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
-		<string>com.apple.GenerativeLearningPlatform.hybridsearchd</string>
+		<string>com.apple.hybridsearchd</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.generativesearch</string>
 	</array>
 	<key>com.apple.security.exception.user-preference-write</key>
 	<array>
-		<string>com.apple.GenerativeLearningPlatform.hybridsearchd</string>
+		<string>com.apple.hybridsearchd</string>
 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
-		<string>com.apple.GenerativeLearningPlatform.hybridsearchd</string>
+		<string>com.apple.hybridsearchd</string>
 	</array>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 		<string>com.apple.UIKit</string>
 		<string>com.apple.gms.availability</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.keyboard.preferences</string>
+		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### keybagd

> `/usr/libexec/keybagd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.wvek</key>
+	<true/>
 	<key>com.apple.keystore.config.bind_kek_to_kb</key>
 	<true/>
 	<key>com.apple.keystore.config.set.user_uuid</key>

```
### locationd

> `/usr/libexec/locationd`

```diff

 			<key>send-command</key>
 			<dict/>
 		</dict>
+		<key>devmotion3_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
 		<key>devmotion6</key>
 		<dict>
 			<key>send-command</key>

 		<string>CLIENT_ENTITLEMENT</string>
 		<string>SERVICE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.CoreRepairCore.repairInfo</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>systemData</key>

 		<string>com.apple.AccessorySensorManager</string>
 		<string>com.apple.perceptiond.context</string>
 		<string>com.apple.StatusKit.local.actor</string>
+		<string>com.apple.CoreRepairCoreXPCService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

 	<true/>
 	<key>com.apple.AppleNVMeSanitize.allow</key>
 	<true/>
+	<key>com.apple.afk.user</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.fdr-access</key>

 		<string>AppleEffaceableStorageUserClient</string>
 		<string>AppleAPFSUserClient</string>
 		<string>IOMobileFramebufferUserClient</string>
+		<string>AFKEndpointInterfaceUserClient</string>
 		<string>IOAVControllerConcreteUserClient</string>
 		<string>IOSurfaceRootUserClient</string>
 		<string>IOWatchdogUserClient</string>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read</key>
+	<array>
+		<string>/Library/Preferences/com.apple.networkextension.uuidcache.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/run/bootSessionMA.txt</string>

```
### mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.ctkd.token-client</string>
 		<string>com.apple.ctkd</string>
+		<string>com.apple.devicedatareset.DeviceDataResetService</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.wipedevice</key>
+	<true/>
 </dict>
 </plist>
 

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>
+		<string>Intelligence.Usage</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### nexusd

> `/usr/libexec/nexusd`

```diff

 	<true/>
 	<key>com.apple.developer.networking.multicast</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

```
### passcodenagd

> `/usr/libexec/passcodenagd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.managedconfiguration.passcodenagd</string>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.set</key>

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MCNagMeta.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>Library/UserConfigurationProfiles/Truth.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/UserConfigurationProfiles/PasscodeDoesNotComply</string>

 	</array>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

```
### powerexceptionsd

> `/usr/libexec/powerexceptionsd`

```diff

 <dict>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.geoservices.navigation_info</key>
+	<true/>
 	<key>com.apple.powerui.smartcharging</key>
 	<true/>
 	<key>com.apple.private.applegraphicsdevicecontrol</key>

 		<string>AppleSMCSensorDispatcherUserClient</string>
 		<string>AppleCLPCUserClient</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.navigationListener</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.powerlog</string>

```
### powerexperienced

> `/usr/libexec/powerexperienced`

```diff

 	<true/>
 	<key>com.apple.osintelligence.charging</key>
 	<true/>
+	<key>com.apple.powerd.extendedbattery</key>
+	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
 	<key>com.apple.private.clpc.policy</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.OSIntelligence.battery</string>
+		<string>com.apple.powerd.extendedbattery</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.dmd-access</key>
 	<true/>
 	<key>com.apple.dmd.operation.remove-app</key>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Trial/</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### ptpassivecollectiond

> `/usr/libexec/ptpassivecollectiond`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.systemstats.analysis-client</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.PerformanceTrace.notifications</string>

```
### ptpd

> `/usr/libexec/ptpd`

```diff

 	</array>
 	<key>com.apple.private.photos.allowassetexpunge</key>
 	<true/>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
 	<key>com.apple.private.photos.service.mediaconversion</key>

```
### remotepairingdeviced

> `/usr/libexec/remotepairingdeviced`

```diff

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.RemotePairing.AuditActivityNotifications</string>
+	</array>
 	<key>com.apple.rapport.Client</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

 		<string>com.apple.PineBoardServices</string>
 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.remoted</string>
+		<string>com.apple.usernoted.client</string>
+		<string>com.apple.usernotifications.listener</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### restorecameraispd

> `/usr/libexec/restorecameraispd`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>VADResourceArbiterUserClient</string>
 		<string>AppleCameraPhotonDetectorUserClient</string>
-		<string>IOUserClient</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 		<string>com.apple.security.octagon</string>
 		<string>com.apple.nearbyd.xpc.diagnostics</string>
 		<string>com.apple.secureelementservice.test.events</string>
-		<string>com.apple.seservicexctests.credential-events</string>
+		<string>com.apple.seservicetests.credential-events</string>
 		<string>com.apple.passd.nf-events</string>
 		<string>com.apple.nfcd.credential-events</string>
 		<string>com.apple.seld.tsmmanager</string>

```
### terminusd

> `/usr/libexec/terminusd`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.ApplicationService.ServiceDiscovery</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-only</key>
 	<array>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.telemetry</key>
 	<true/>
 	<key>com.apple.cdp.utility</key>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 		<string>/Library/Caches/com.apple.tvremoted/</string>
 		<string>/Library/Caches/tvapp_bag/</string>
 		<string>/Library/HTTPStorages/com.apple.tvremoted/</string>
-		<string>/Library/</string>
+		<string>/Library/tvremoted/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.ACMobileShim</string>
+		<string>com.apple.AUDeveloperSettings</string>
 		<string>com.apple.GEO</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### uarpd

> `/usr/libexec/uarpd`

```diff

 	<true/>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>
+	<key>com.apple.security.ts.geoservices</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.MobileAccessoryUpdater</string>
 	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 		<string>AppleSPUFastpathDriverUserClient</string>
 		<string>AppleSPUUserClient</string>
 		<string>IOHIDLibUserClient</string>
-		<string>IOUserClient</string>
+		<string>IOUserUserClient</string>
 		<string>AppleCredentialManagerUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 	<true/>
 	<key>keychain-access-groups</key>
 	<array>
-		<string>apple</string>
 		<string>com.apple.bluetooth</string>
 		<string>com.apple.ExposureNotification</string>
 	</array>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
+	<key>com.apple.locationd.use-wireless-client-info</key>
+	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.mDNSResponder.record-cache.local-record-info</key>

```


### AppOS

### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 		<string>com.apple.apsd</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.backboard.hid.services</string>
+		<string>com.apple.backboard.hid-services.xpc</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.appprotectiond.extensionmonitor</string>
 		<string>com.apple.appprotectiond.extensioninfo</string>

```


