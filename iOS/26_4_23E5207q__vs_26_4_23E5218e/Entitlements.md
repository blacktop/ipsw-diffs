## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.amsengagementd</string>
 		<string>com.apple.AppStoreComponents</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```

### 🆕 AuthorizationPromptService

> `/Applications/AuthorizationPromptService.app/AuthorizationPromptService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.runningboard.assertions.angeltarget</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.frontboard.systemappservices</string>
	</array>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.tcc.remote-authorization-prompt</key>
	<true/>
</dict>
</plist>

```
### Charge

> `/Applications/Charge.app/Charge`

```diff

 	<true/>
 	<key>com.apple.developer.carp</key>
 	<true/>
+	<key>com.apple.private.CarAssetUtils.variants</key>
+	<true/>
 	<key>com.apple.private.RequiredVehicleAccessories</key>
 	<array>
 		<string>HighVoltageBattery</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.CarAssetUtils.variants</string>
 	</array>
 </dict>
 </plist>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 		<string>com.apple.communicationSafetySettings</string>
 		<string>com.apple.cameracapture</string>
 		<string>com.apple.CommunicationsUI</string>
+		<string>com.apple.CommunicationTrust</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.tvappservices.container</string>
+	</array>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

```
### ClarityBoard

> `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

 	<true/>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
+	<key>com.apple.backboardd.virtualDisplay</key>
+	<true/>
 	<key>com.apple.bulletinboard</key>
 	<true/>
 	<key>com.apple.bulletinboard.dataprovider</key>

```
### AssistantSettingsControlsExtension

> `/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension`

```diff

 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.Accessibility</string>
 		<string>com.apple.TelephonyUtilities</string>
+		<string>com.apple.siri</string>
 	</array>
 	<key>com.apple.usernotifications.usernotificationsettingsservice</key>
 	<true/>

```
### ClockAppIntents

> `/System/Library/ExtensionKit/Extensions/ClockAppIntents.appex/ClockAppIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.mobiletimer.ClockAppIntents</string>
+	<key>com.apple.developer.healthkit</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>

 	</array>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.mobiletimer</string>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
+	<key>com.apple.private.sleepd</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>RegionalSafetyAnalysis.Disablement</string>
 		<string>RegionalSafetyAnalysis.GuardrailResult</string>
 		<string>GenerativeExperiences.GuardrailResult</string>
+		<string>GenerativeExperiences.WritingToolsFeatures.Requests</string>
 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>

```
### PCCAgentClientExtension

> `/System/Library/ExtensionKit/Extensions/PCCAgentClientExtension.appex/PCCAgentClientExtension`

```diff

 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeExperiences.TransparencyLog</string>
+		<string>AppleIntelligence.Reporting.Invocation.Step</string>
 	</array>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>

```
### PasswordsDataMigration

> `/System/Library/ExtensionKit/Extensions/PasswordsDataMigration.appex/PasswordsDataMigration`

```diff

 		<string>com.apple.private.email</string>
 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>

```
### TelemetryAggregator

> `/System/Library/ExtensionKit/Extensions/TelemetryAggregator.appex/TelemetryAggregator`

```diff

 	<string>com.apple.DifferentialPrivacy.TelemetryAggregator</string>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
-	<key>com.apple.private.dprivacyd.metadata.allow</key>
-	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>MLHostTelemetry</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/ExtensionKit/Extensions/WebContentEnhancedSecurityExtension.appex/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	<array>
 		<string>jit</string>
 	</array>
+	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.spotlightknowledged</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</key>
 	<true/>
 	<key>com.apple.apfs.unlock</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### com.apple.PDFKit.OFD_Thumbnail

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/com.apple.PDFKit.OFD_Thumbnail.appex/com.apple.PDFKit.OFD_Thumbnail`

```diff

 	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

 	<array>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.ShazamKit/</string>
+		<string>/Library/com.apple.AppleMediaServices/PersistedBags/com.apple.ShazamKit/</string>
+		<string>/Library/HTTPStorages/com.apple.ShazamKit/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.locationd.synchronous</string>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	</array>
 	<key>com.apple.companion-authentication.store-purchase</key>
 	<true/>
+	<key>com.apple.coreidvd.document-upload</key>
+	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
 	<key>com.apple.developer.aps-environment</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.coreidvd.docUpload.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.companiond.xpc</string>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.watchnotificationsui.alertservice</string>
 		<string>com.apple.PineBoardServices</string>
+		<string>com.apple.ctkd.token-client</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<key>com.apple.trial.status.namespace-name.allow</key>
 	<array>
 		<string>COREOS_GMPOWER_VM_TUNING_PAGE_SHORTAGE_THRESHOLDS</string>
+		<string>SEARCH_TOOL_ANSWER_SYNTHESIS</string>
 		<string>INTELLIGENCE_FLOW_PLAN_RESOLUTION</string>
 		<string>MYRIAD_BOOSTS</string>
 		<string>SIRI_AUDIO_APP_SELECTION_HOMEACCESSORY</string>

 		<string>SIRI_PRIVATE_LEARNING_SUGGESTIONS_PLATFORM</string>
 		<string>SIRI_REFERENCE_RESOLUTION_LIGHTHOUSE_PLUGIN</string>
 		<string>SIRI_REFERENCE_RESOLUTION_LIGHTHOUSE_PLUGIN_FOR_SHADOW_LOGGING</string>
+		<string>SIRI_SECURITY_IPI</string>
 		<string>SIRI_SELF_REFLECTION_ASK_REPEAT</string>
 		<string>SIRI_SELF_REFLECTION_TAP_TO_EDIT</string>
 		<string>SIRI_SPEECH_DATASET_SAMPLING</string>

 		<string>SIRI_VIDEO_APP_SELECTION</string>
 		<string>SIRI_VIDEO_SIGNAL_COLLECTION</string>
 		<string>UAF_AB_UNDERSTANDING</string>
+		<string>UAF_AB_MODELCATALOG</string>
 		<string>WATCH_RTS</string>
 	</array>
 	<key>com.apple.visualvoicemail.client</key>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	</array>
 	<key>com.apple.private.authentication-services.internal-authorization-requests</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.fetchNewestPolicies</key>
+	<true/>
+	<key>com.apple.private.eligibilityd.internalState</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.setInput</key>
 	<true/>
 	<key>com.apple.private.followup</key>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.watchnotificationsui.alertservice</string>
+		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.backboard.display.services</string>
 		<string>com.apple.iohideventsystem</string>

 	<true/>
 	<key>com.apple.shortcuts.background-running</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

 	<true/>
 	<key>com.apple.keystore.icsc_srp</key>
 	<true/>
+	<key>com.apple.keystore.keybag.create</key>
+	<true/>
+	<key>com.apple.keystore.keybag.load</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siri.embeddedspeech</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.uservault</string>
+		<string>com.apple.assistant.settings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/Managed Preferences/mobile/com.apple.webcontentfilter.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled`

```diff

 	<array>
 		<string>com.apple.appleaccount</string>
 		<string>com.apple.familycircled</string>
-		<string>com.apple.FamilyCircle</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.keystore.lockassertion</key>
+	<true/>
+	<key>com.apple.keystore.lockassertion.restore_from_backup</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.keystore.devicebackup</key>
 	<true/>
+	<key>com.apple.keystore.keybag.create</key>
+	<true/>
+	<key>com.apple.keystore.keybag.load</key>
+	<true/>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
 	<key>com.apple.keystore.lockassertion.restore_from_backup</key>

```
### NanoMediaDiagnosticExtension

> `/System/Library/PrivateFrameworks/NanoMusicSync.framework/PlugIns/NanoMediaDiagnosticExtension.appex/NanoMediaDiagnosticExtension`

```diff

 		<string>/Library/Logs/MediaServices/HTTPArchives/</string>
 		<string>/Library/Preferences/com.apple.NanoMusicSync.plist</string>
 		<string>/Media/iTunes_Control/iTunes/</string>
-		<string>/tmp/</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-only</key>
 	<array>

```
### com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

 	</array>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.CallHistory</key>

 		<string>com.apple.incoming-call-filter-server</string>
 		<string>com.apple.lsd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.ids</string>

```
### pasted

> `/System/Library/PrivateFrameworks/Pasteboard.framework/Support/pasted`

```diff

 	</array>
 	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.pasteboard</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.frontboard.systemappservices</string>

```
### com.apple.Safari.SafeBrowsing.Service

> `/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/com.apple.Safari.SafeBrowsing.Service`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.security.signal-exempt</key>
+	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
+	<key>com.apple.private.security.storage.SafariSafeBrowsing</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.analyticsd</string>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```diff

 	<key>aps-connection-initiate</key>
 	<true/>
 	<key>aps-environment</key>
-	<string>development</string>
+	<string>serverPreferred</string>
 	<key>com.apple.developer.icloud-container-environment</key>
-	<string>Development</string>
+	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
+	<key>com.apple.private.memory.ownership_transfer</key>
+	<true/>
 	<key>com.apple.private.metadata.exattrs</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>
 	<true/>
+	<key>com.apple.private.seeding.client</key>
+	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.runningboard.process-state</key>

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.seeding.client-helper</key>
+	<true/>
+	<key>com.apple.seeding.enrollment-helper</key>
+	<true/>
 	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>
 	<true/>
 	<key>com.apple.springboard-ui.client</key>

```

### 🆕 SwiftUITracingSupport

> `/System/Library/PrivateFrameworks/SwiftUITracingSupport.framework/SwiftUITracingSupport`

- No entitlements *(yet)*
### UserNotificationsUIThumbnailProvider

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/PlugIns/UserNotificationsUIThumbnailProvider.appex/UserNotificationsUIThumbnailProvider`

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
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.tv.engagement</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.TapToRadarKit.service</string>
+	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.SharePlay.GroupSessionService</string>
 		<string>com.apple.CloudSharing.SPIHelper-iOS</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.networkserviceproxy.fetch-token</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.MobileStoreDemo.test</string>
 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.cloud.quota</string>
 	</array>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	</array>
 	<key>com.apple.springboard.allowallcallurls</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.storekit.client-override</key>
 	<true/>
 	<key>com.apple.symptom_analytics.query</key>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 		<string>com.apple.suggestions</string>
 		<string>com.apple.AppStoreComponents</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MailSearchQuery</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Mail.Search.Query</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>appEntityRelevanceRanking</string>

 	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
-	<key>com.apple.springboard.multiwindow.requestShelfPresentation</key>
-	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.shortcutitems.customimage</key>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.private.jetpackassetd</key>
 	<true/>
+	<key>com.apple.private.privacy.accounting.write</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 		<string>com.apple.trustedcloudcompute</string>
 		<string>com.apple.communicationSafetySettings</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
 	<key>com.apple.sharesheet.allow-custom-view</key>

```
### BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.keystore.keybag.create</key>
+	<true/>
+	<key>com.apple.keystore.keybag.load</key>
+	<true/>
 	<key>com.apple.lockdownd.allow-save-value</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>

```
### afcd

> `/usr/libexec/afcd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.private.MobileActivation</key>
+	<array>
+		<string>GetActivationState</string>
+		<string>RequestActivationState</string>
+	</array>
 	<key>com.apple.private.security.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>Device.Audio.AdaptiveVolume</string>
+		<string>Device.Audio.BehavioralVolume</string>
 	</array>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>

 		<string>com.apple.lsd.open</string>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.ctcategories.service</string>
 		<string>com.apple.account.AppleAccount</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### corecaptured

> `/usr/libexec/corecaptured`

```diff

 	</array>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.osanalytics.osanalyticshelper</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOReportUserClient</string>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>com.apple.das.fairscheduling</string>
 		<string>com.apple.dasd.dailyPeriodic</string>
 		<string>com.apple.dasd.issueDetector</string>
+		<string>com.apple.dasd.idlestack</string>
 		<string>com.apple.dasd.swapkills</string>
 		<string>com.apple.dasd.widgetRefreshBudgets</string>
 		<string>com.apple.mt</string>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 		<string>com.apple.SpotlightFoundation</string>
 		<string>com.apple.NanoHomeScreen.RelevantWidgetDefaults</string>
 		<string>com.apple.proactive.visual-action-prediction</string>
+		<string>com.apple.Spotlight</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>WritingToolsFeaturesRequests</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.WritingToolsFeatures.Requests</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>

```
### lockdownd

> `/usr/libexec/lockdownd`

```diff

 	<true/>
 	<key>com.apple.keystore.escrow.create</key>
 	<true/>
+	<key>com.apple.keystore.keybag.create</key>
+	<true/>
+	<key>com.apple.keystore.keybag.load</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

 	<array>
 		<string>Device.KeybagLocked</string>
 	</array>
+	<key>com.apple.private.corewifi</key>
+	<true/>
+	<key>com.apple.private.corewifi.mac-addr</key>
+	<true/>
 	<key>com.apple.private.gasgauge-update</key>
 	<true/>
 	<key>com.apple.private.iamlockdown</key>

 		<string>com.apple.carkit.service.lockdown</string>
 		<string>com.apple.amfi.lockdown</string>
 		<string>com.apple.backgroundassets.lockdownservice</string>
+		<string>com.apple.private.corewifi-xpc</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### mobile_house_arrest

> `/usr/libexec/mobile_house_arrest`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.private.MobileActivation</key>
+	<array>
+		<string>GetActivationState</string>
+		<string>RequestActivationState</string>
+	</array>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<true/>
 	<key>com.apple.private.iad.opt-in-control</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.ap.promotedcontentd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>PolicyInstrumentation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AdPlatforms.PolicyInstrumentation.Candidate</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>AdPlatforms.PolicyInstrumentation.Opportunity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<array>
 		<string>com.apple.ak.auth.xpc</string>
 	</array>
+	<key>com.apple.security.ts.mobile-keybag-access</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.ap.promotedcontentd</string>
 	<key>com.apple.trial.client</key>

```
### securityd

> `/usr/libexec/securityd`

```diff

 	<true/>
 	<key>com.apple.keystore.enable_cache_flow</key>
 	<true/>
+	<key>com.apple.keystore.keybag.create</key>
+	<true/>
+	<key>com.apple.keystore.keybag.load</key>
+	<true/>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

```
### spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.spotlightknowledged</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</key>
 	<true/>
 	<key>com.apple.apfs.unlock</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.spotlightknowledged</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</key>
 	<true/>
 	<key>com.apple.apfs.unlock</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>
 	<true/>
+	<key>com.apple.private.security.storage.SecureElementService</key>
+	<true/>
 	<key>com.apple.private.security.storage.sysdiagnose.sysdiagnose</key>
 	<true/>
 	<key>com.apple.private.seeding.client</key>

```
### thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.ts.power-assertions</key>
 	<true/>
 	<key>com.apple.systemapp.allowsShutdown</key>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

```
