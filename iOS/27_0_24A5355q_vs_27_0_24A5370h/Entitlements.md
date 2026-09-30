## 🔑 Entitlements

### filesystem

### AccessorySetupUI

> `/Applications/AccessorySetupUI.app/AccessorySetupUI`

```diff

 	<true/>
 	<key>com.apple.DeviceAccess.private</key>
 	<true/>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
 	<key>com.apple.bluetooth.settings</key>

 		<string>com.apple.private.corewifi.wifi-network-sharing-ui-xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ProductKitService</string>
+		<string>com.apple.SharingServices</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.springboard</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.accessorysetupkit</string>
 	</array>
+	<key>com.apple.sharing.Client</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### ActivityMessagesExtension

> `/Applications/ActivityMessagesApp.app/PlugIns/ActivityMessagesExtension.appex/ActivityMessagesExtension`

```diff

 		<string>com.apple.private.healthd.server-extended</string>
 		<string>com.apple.activityawardsd</string>
 		<string>com.apple.activitysharingd</string>
+		<string>com.apple.spaceattributiond</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.ActivitySharing</string>
 		<string>com.apple.nanolifestyle</string>
 	</array>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 </dict>
 </plist>
 

```
### AskPermissionUI

> `/Applications/AskPermissionUI.app/AskPermissionUI`

```diff

 	<array>
 		<string>IOMobileFramebufferUserClient</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### AskToUIHost

> `/Applications/AskToUIHost.app/AskToUIHost`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.MobileSMS</string>
+	</dict>
+</dict>
+</plist>
 

```
### AuthorizationPromptService

> `/Applications/AuthorizationPromptService.app/AuthorizationPromptService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### Campo

> `/Applications/Campo.app/Campo`

```diff

 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.campo</string>
+	<key>com.apple.devicesharing.guest-user-mode-client</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.duet.expertcenter.consumer</key>

 	</array>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.filederivatives.derive</key>
 	<true/>
 	<key>com.apple.filederivatives.list</key>

 	<true/>
 	<key>com.apple.private.Safari.History</key>
 	<true/>
+	<key>com.apple.private.WebClips.read-write</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>

 		<string>IntelligenceFlow.Telemetry</string>
 		<string>IntelligenceFlow.ResponseGeneration</string>
 		<string>IntelligenceFlow.ExecutorTelemetry</string>
+		<string>Intelligence.Usage</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 			<key>Search</key>
 			<array>
 				<string>SiriTranscript</string>
+				<string>SiriTranscriptConversation</string>
 				<string>UnknownEntityType</string>
 			</array>
 		</dict>

 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
+	<key>com.apple.private.siriappintentsd.orchestrator</key>
+	<true/>
 	<key>com.apple.private.sleepd</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Media/PhotoData/OutgoingTemp/</string>
 		<string>/Library/DeviceRegistry/</string>
 		<string>/Library/Application Support/SNLUOverrides.sqlite</string>
 		<string>/Library/AddressBook/</string>
 		<string>/Library/Application Support/IntelligenceFlow/</string>
+		<string>/Library/Application Support/CampoUIInternal/</string>
 		<string>/Library/Application Support/SNLUOverrides.sqlite-shm</string>
 		<string>/Library/Application Support/SNLUOverrides.sqlite-wal</string>
 		<string>/Library/Application Support/SNLUOverrides.sqlite</string>

 		<string>/Library/com.apple.AppleMediaServices/</string>
 		<string>/tmp/</string>
 		<string>/Library/com.apple.siri-replay/</string>
+		<string>/Media/PhotoData/PhotoCloudSharingData/Caches/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.quicklook.UIExtension.viewservice</string>
-		<string>com.apple.siriappintentsd.orchestrator</string>
+		<string>com.apple.private.siriappintentsd.orchestrator</string>
 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.generativeexperiences.corefollowup</string>
 		<string>com.apple.ManagedSettingsAgent</string>

 		<string>com.apple.carousel.flashlightxpcservice</string>
 		<string>com.apple.realitysystemsupport.hid_server_backboard</string>
 		<string>com.apple.surfboard.entityinteractionservice</string>
+		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.calendar.EventKitUIRemoteUIExtension.viewservice</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.iconservices</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.orchestration.prescribedaction</key>
 	<true/>
-	<key>com.apple.siriappintentsd.orchestrator</key>
-	<true/>
 	<key>com.apple.siriinferenced</key>
 	<true/>
 	<key>com.apple.siriknowledged</key>

 	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
-	<key>com.apple.surfboard-prevent-homeui-from-hiding-when-launching</key>
+	<key>com.apple.surfboard.allow-scene-requests-while-backgrounded</key>
 	<true/>
 	<key>com.apple.surfboard.application-service-client</key>
 	<true/>

 	<true/>
 	<key>com.apple.surfboard.entity-interaction-observer</key>
 	<true/>
+	<key>com.apple.surfboard.force-quit-suppression</key>
+	<true/>
 	<key>com.apple.surfboard.immersion-client</key>
 	<true/>
 	<key>com.apple.surfboard.immersive-scene-dismissal</key>

 	<true/>
 	<key>com.apple.surfboard.scenesession-updates</key>
 	<true/>
+	<key>com.apple.surfboard.sharing-mode-launch-allowed</key>
+	<true/>
 	<key>com.apple.surfboard.should-ignore-if-last-scene-for-auto-show-homeui</key>
 	<true/>
 	<key>com.apple.surfboard.system-elements-assertion-immersive-visible</key>

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 			<array>
 				<string>CompanionSetup</string>
 			</array>
+			<key>resetTriggers</key>
+			<array>
+				<string>WiFiConnected</string>
+			</array>
 			<key>sceneIdentifier</key>
 			<string>CompanionSetup</string>
 			<key>screenLocked</key>

 	</array>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array>
+		<string>com.apple.container.HeadBoard</string>
+	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>
 	</array>
+	<key>com.apple.developer.sensitivecontentanalysis.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
 	<key>com.apple.findmy.findmylocate.fenceservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>BluetoothAddress</string>
+		<string>EthernetMacAddress</string>
 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
+		<string>WifiAddress</string>
+		<string>WifiAddressData</string>
 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>

 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.tvos.userprofiles</key>
 		<string>com.apple.tvos.userprofiles</string>
 	</dict>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.rtcreportingd</key>
+	<true/>
 	<key>com.apple.private.security.storage.DuetExpertCenter</key>
 	<true/>
 	<key>com.apple.private.security.storage.HomeKit</key>

 	<true/>
 	<key>com.apple.rootless.storage.proactivepredictions</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 		<string>/Library/DuetExpertCenter/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.Accessibility</string>
 		<string>com.apple.CompanionSetupKit</string>
 		<string>com.apple.coreaudio</string>
 	</array>

```
### CompanionViewService

> `/Applications/CompanionViewService.app/CompanionViewService`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
+		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### CredentialSharingUIViewService

> `/Applications/CredentialSharingUIViewService.app/CredentialSharingUIViewService`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.nfcd.hwmanager</key>
+	<true/>
 	<key>com.apple.odi.internal</key>
 	<true/>
 	<key>com.apple.passes.add-silently</key>

```
### CustomerEngagementUIService

> `/Applications/CustomerEngagementUIService.app/CustomerEngagementUIService`

```diff

 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.iconservices</string>
+		<string>com.apple.iconservices.store</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.corerepair.attestation</key>
 	<true/>
 	<key>com.apple.private.corerepair.xpc</key>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/hardware/FactoryData/</string>
 		<string>/private/var/MobileSoftwareUpdate/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### Diagnostic-9008

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/hardware/FactoryData/</string>
 		<string>/private/var/MobileSoftwareUpdate/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### Diagnostic-9010

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9010.appex/Diagnostic-9010`

```diff

 	<true/>
 	<key>com.apple.DiagnosticsSupport.HardwareButtonAccess</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.corerepair.xpc</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-filter</key>

 	<true/>
 	<key>com.apple.private.xpc.launchd.reboot</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/hardware/FactoryData/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.corerepair</string>

```
### Enhanced Logging

> `/Applications/Enhanced Logging.app/Enhanced Logging`

```diff

 	<string>com.apple.EnhancedLogging</string>
 	<key>com.apple.AppleServiceToolkit.host</key>
 	<true/>
+	<key>com.apple.developer.associated-domains</key>
+	<array/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.swc.system-app</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>Library/Logs/com.apple.diagnosticextensionsd/</string>

```
### FinanceUIService

> `/Applications/FinanceUIService.app/FinanceUIService`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.cards.all-access</key>
+	<true/>
 	<key>com.apple.finance.private</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.appleaccount.identity.read</key>
+	<true/>
 	<key>com.apple.appstored.install-apps</key>
 	<true/>
 	<key>com.apple.appstored.install-system-apps</key>

 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>
 		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
+		<string>CommApps.CallIntelligence.CallContextCardsFedStats</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.publisher.service.user</string>
 		<string>com.apple.communicationtrustd.service</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FaceTimeShareExtension

> `/Applications/InCallService.app/PlugIns/FaceTimeShareExtension.appex/FaceTimeShareExtension`

```diff

 <dict>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.developer.auto-elect-plugin</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>

 	<true/>
 	<key>com.apple.private.sociallayer.shareable-content</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
+	<key>com.apple.security.files.user-selected.read-write</key>
+	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.CloudSharing.SPIHelper-iOS</string>
+		<string>com.apple.CloudSharing.SPIHelper</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>

```
### InputUI

> `/Applications/InputUI.app/InputUI`

```diff

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authentication-services-core.allow-querying-credential-providers</key>
+	<true/>
 	<key>com.apple.authentication-services.access-credential-identities</key>
 	<true/>
 	<key>com.apple.authentication-services.app-passkey-autofill</key>

 		<string>com.apple.AccessibilityUIServer</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.AuthenticationServices.AutoFill</string>
+		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent</string>
 		<string>com.apple.securityd</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.security.kcsharing</string>

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

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

```
### PeerPaymentMessagesExtension

> `/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.messages.private.AllowParticipantAddressAccess</key>
 	<true/>
-	<key>com.apple.modelcatalog.full-access</key>
-	<true/>
-	<key>com.apple.modelmanager.inference</key>
-	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
 	<key>com.apple.nfcd.radio.powertoggle</key>

 		<string>UniqueChipID</string>
 		<string>SerialNumber</string>
 	</array>
-	<key>com.apple.private.assets.accessible-asset-types</key>
-	<array>
-		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
-		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
-	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
-	<key>com.apple.private.biome.read-write</key>
-	<array>
-		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
-		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
-	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.bundleid</key>

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
-	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
-	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.privatecloudcompute.admin</key>
-	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
-		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/tmp/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.seld.tsmmanager</string>
 		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
-		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.biome.access.user</string>
-		<string>com.apple.siri.uaf.service</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.mobileassetd.v2</string>
-		<string>com.apple.modelmanager</string>
 		<string>com.apple.imtransferservices.IMTransferAgent</string>
 		<string>com.apple.visualintelligence.visual-action-prediction</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
-	<array>
-		<string>com.apple.UnifiedAssetFramework</string>
-		<string>com.apple.modelcatalog.ajax</string>
-		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
-		<string>kCFPreferencesAnyApplication</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.stockholm</string>

```
### PhotosUIService

> `/Applications/PhotosUIService.app/PhotosUIService`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<array>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 		<string>group.com.apple.tips</string>
+		<string>group.com.apple.feedback</string>
 	</array>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>

 		<string>group.tvappservices.container</string>
 		<string>group.com.apple.SuggestedImage.SharedSecureContainer</string>
 		<string>group.com.apple.GenerativePlayground</string>
+		<string>group.com.apple.feedback</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/com.apple.countryd/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.devicesharingd</string>
 		<string>com.apple.momentsd</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.CommCenter</string>
+		<string>com.apple.MobileSMS</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.parsecd</string>

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
 		<string>com.apple.ConnectedAudio</string>
+		<string>com.apple.natvoc</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### RemoteiCloudQuotaUI

> `/Applications/RemoteiCloudQuotaUI.app/RemoteiCloudQuotaUI`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.small-offer-button</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Library</string>

```
### SIMSetupUIService

> `/Applications/SIMSetupUIService.app/SIMSetupUIService`

```diff

 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>bootstrap-service</string>
-		<string>public-cellular-plan</string>
 		<string>cellular-plan</string>
 		<string>identity</string>
+		<string>public-cellular-plan</string>
+		<string>public-esim-qr-code</string>
 		<string>spi</string>
 	</array>
 	<key>com.apple.QuartzCore.secure-mode</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<array>
 		<string>/Library/Caches/com.apple.ClipServices/</string>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>spi</string>
 		<string>data-allowed-write</string>
 		<string>bootstrap-service</string>
+		<string>public-esim-qr-code</string>
 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.safari.cloudtabs</key>
 	<true/>
-	<key>com.apple.private.safefinancing</key>
-	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screen-time-settings</key>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.nfcd.hwmanager</key>
+	<true/>
+	<key>com.apple.nfcd.session.cardmigration</key>
+	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
 	<key>com.apple.payment.amp-card-enrollment</key>

 	<array>
 		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.passd.sharing-channel</string>
+		<string>com.apple.passd.payment</string>
 		<string>com.apple.accessories.connection-info-server</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
 		<string>com.apple.familycircle.agent</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.PassbookUISceneService.remote-ui</string>
+		<string>com.apple.nfcd.hwmanager</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
+	<key>com.apple.springboard.hardware-button-service.button-associated-hint-view</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>

 	<true/>
 	<key>com.apple.voicetrigger.voicetriggerservice</key>
 	<true/>
+	<key>com.apple.wallet.banner</key>
+	<true/>
 	<key>com.apple.wifi.eap-nearby-device-setup-config-copy</key>
 	<true/>
 	<key>com.apple.wifi.manager-access</key>

```
### SoftwareUpdateUIService

> `/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.susuiservice</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>

 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>appleaccount</string>
+		<string>com.apple.certificates</string>
+		<string>com.apple.identities</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceWillow</string>
 	</array>
-	<key>com.apple.private.tcc.manager.read.access</key>
+	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>

```

### 🆕 SupportFlowSpotlightIndex

> `/Applications/SupportFlow.app/PlugIns/SupportFlowSpotlightIndex.appex/SupportFlowSpotlightIndex`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.SupportFlow.SpotlightIndexExtension</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.tipsd</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.tipsd.access</key>
	<true/>
</dict>
</plist>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<array>
 		<string></string>
 	</array>
-	<key>com.apple.developer.healthkit</key>
-	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
-	<key>com.apple.private.UIKit.UIScene.allow-host-context-propagation</key>
-	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
-	<key>com.apple.private.health.scene-hosting</key>
-	<true/>
-	<key>com.apple.private.healthkit</key>
-	<true/>
-	<key>com.apple.private.healthkit.authorization_manager</key>
-	<array>
-		<string>read</string>
-		<string>write</string>
-	</array>
-	<key>com.apple.private.healthkit.source.identities</key>
-	<array>
-		<string>com.apple.siri</string>
-	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>

```
### extensionFilter

> `/Applications/Text Message Filter.app/PlugIns/extensionFilter.appex/extensionFilter`

```diff

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/</string>

```
### WebContentRestrictionsUI

> `/Applications/WebContentRestrictionsUI.app/WebContentRestrictionsUI`

```diff

 	<array>
 		<string>com.apple.springboard</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### WidgetRenderer_Activities

> `/Applications/WidgetRenderer_Activities.app/WidgetRenderer_Activities`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceSystemPolicyAppData</string>
+		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>

```
### WidgetRenderer_CarPlay

> `/Applications/WidgetRenderer_CarPlay.app/WidgetRenderer_CarPlay`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceSystemPolicyAppData</string>
+		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>

```
### WidgetRenderer_Default

> `/Applications/WidgetRenderer_Default.app/WidgetRenderer_Default`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceSystemPolicyAppData</string>
+		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>

```
### WidgetRenderer_Snapshots

> `/Applications/WidgetRenderer_Snapshots.app/WidgetRenderer_Snapshots`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceSystemPolicyAppData</string>
+		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>

```
### WidgetRenderer_WatchFaces

> `/Applications/WidgetRenderer_WatchFaces.app/WidgetRenderer_WatchFaces`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceSystemPolicyAppData</string>
+		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalProviderService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
 	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>

 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
+		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 		<string>com.apple.internal.InputTester</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.private.acccessibility.motionTrackingClient</key>
 	<true/>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 		<string>com.apple.keyboard</string>
 		<string>com.apple.springboard</string>
 		<string>com.apple.assistant.logging</string>
-		<string>com.apple.Preferences</string>
 		<string>com.apple.UIKit</string>
 		<string>com.apple.CloudKit</string>
 		<string>com.apple.coreaudio</string>

 		<string>com.apple.UIKit</string>
 		<string>com.apple.preferences-framework</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.Preferences</string>
 		<string>com.apple.WatchControl</string>
 		<string>com.apple.airplay</string>
 		<string>com.apple.ClarityUI</string>

```
### PhotosViewService

> `/System/Library/CoreServices/PhotosViewService.app/PhotosViewService`

```diff

 	<true/>
 	<key>com.apple.private.cloudphotod.access</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.photos.allowassetexpunge</key>
 	<true/>
 	<key>com.apple.private.photos.allowcollectionshare</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.ModeEntityScorer</key>
 	<true/>
+	<key>com.apple.Pasteboard.allowed-metadata-keys</key>
+	<array>
+		<string>SBUIRequiredApplicationBundleIdentifier</string>
+		<string>SBUIPreferredApplicationBundleIdentifier</string>
+		<string>SBUIIgnore</string>
+	</array>
 	<key>com.apple.Pasteboard.trusted-authentication-message-request</key>
 	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>

 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>
 	<true/>
+	<key>com.apple.mkb.usersession.load</key>
+	<true/>
 	<key>com.apple.mkb.usersession.loginwindow</key>
 	<true/>
+	<key>com.apple.mkb.usersession.switch</key>
+	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
 	<key>com.apple.mobile.keybagd.UserManager.logoutcritical</key>

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.DuetExpertCenterAsset</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
+		<string>com.apple.MobileAsset.UAF.IF.PlannerOverrides</string>
+		<string>com.apple.MobileAsset.UAF.Shortcuts.Generator</string>
+		<string>com.apple.MobileAsset.UAF.Siri.AnswerSynthesis</string>
+		<string>com.apple.MobileAsset.UAF.Siri.DialogAssets</string>
+		<string>com.apple.MobileAsset.UAF.Siri.FindMyConfigurationFiles</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingASRHammer</string>
+		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingNLOverrides</string>
+		<string>com.apple.MobileAsset.UAF.Translation.MMAssets</string>
 	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
 	<key>com.apple.private.attentionawareness</key>
 	<true/>
 	<key>com.apple.private.attentionawareness.continuousFaceDetect</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.usernotifications.subscriber-service.launching</string>
 		<string>com.apple.usernotifications.subscriber-service.non-launching</string>
 		<string>com.apple.usernotifications.event-service.launching</string>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 		<string>com.apple.AccessibilityUIServer</string>
 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.TextInput.rdt</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

 		<string>com.apple.ZoomTouch</string>
 		<string>com.apple.voiceservices</string>
 		<string>com.apple.keyboard.ContinuousPath</string>
+		<string>com.apple.Preferences</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### ASRFullPayloadCorrection

> `/System/Library/ExtensionKit/Extensions/ASRFullPayloadCorrection.appex/ASRFullPayloadCorrection`

```diff

 	</array>
 	<key>com.apple.siri.analytics.assistant</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.icl</string>
+	</array>
 </dict>
 </plist>
 

```
### AssetMetrics

> `/System/Library/ExtensionKit/Extensions/AssetMetrics.appex/AssetMetrics`

```diff

 		<string>Sage.Transcript</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>AssetDelivery.UAF.DailyStatus</string>
+		<string>AssetDelivery.UAF.AssetSetStatus</string>
+		<string>AssetDelivery.UAF.DailyScheduledAssetStatus</string>
+		<string>AssetDelivery.UAF.AssetSetAlterActivity</string>
 		<string>Device.KeybagLocked</string>
 		<string>Device.BootSession</string>
 	</array>

 				<string>Siri.SELFProcessedEvent</string>
 				<string>IntelligenceFlow.Transcript.Datastream</string>
 				<string>AssetDelivery.UAF.DailyStatus</string>
+				<string>AssetDelivery.UAF.AssetSetStatus</string>
+				<string>AssetDelivery.UAF.DailyScheduledAssetStatus</string>
+				<string>AssetDelivery.UAF.AssetSetAlterActivity</string>
 				<string>Device.KeybagLocked</string>
 				<string>Device.BootSession</string>
 			</array>

```

### 🆕 BackgroundSecurityImprovementSettingsIntents

> `/System/Library/ExtensionKit/Extensions/BackgroundSecurityImprovementSettingsIntents.appex/BackgroundSecurityImprovementSettingsIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### ExclavesInferenceProvider

> `/System/Library/ExtensionKit/Extensions/ExclavesInferenceProvider.appex/ExclavesInferenceProvider`

```diff

 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition</string>
+	</array>
 	<key>com.apple.private.exclaves.conclave-host</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Speech_AutomaticSpeechRecognition/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Speech_AutomaticSpeechRecognition/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.modelcatalog.catalog</string>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/FedStatsPluginDynamic`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
+	<key>com.apple.private.healthkit.read_authorization_bypass</key>
+	<array>
+		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
+		<string>HKQuantityTypeIdentifierStepCount</string>
+		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
+		<string>HKQuantityTypeIdentifierVO2Max</string>
+		<string>HKActivitySummaryTypeIdentifier</string>
+	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.priml.FedStatsPlugin.Dynamic</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Change-PW-for-Me-Recommendations</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Passwords.SecurityRecommendations</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Connectivity-Context</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>FedStats-Safari-Link-Tracking-Protection</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Safari.Navigations</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Generation-Failure-Reason</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Wallet-Order-Extraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>TrustKit.Decisioning.TKWalletOrderExtractionDomains</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Writing-Tools</key>
 		<dict>
 			<key>Streams</key>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/FedStatsPluginStatic`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
+	<key>com.apple.private.healthkit.read_authorization_bypass</key>
+	<array>
+		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
+		<string>HKQuantityTypeIdentifierStepCount</string>
+		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
+		<string>HKQuantityTypeIdentifierVO2Max</string>
+		<string>HKActivitySummaryTypeIdentifier</string>
+	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.priml.FedStatsPlugin.Static</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Change-PW-for-Me-Recommendations</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Passwords.SecurityRecommendations</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Connectivity-Context</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>FedStats-Safari-Link-Tracking-Protection</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Safari.Navigations</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Generation-Failure-Reason</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Wallet-Order-Extraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>TrustKit.Decisioning.TKWalletOrderExtractionDomains</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Writing-Tools</key>
 		<dict>
 			<key>Streams</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.Photos</string>
 	</array>
+	<key>com.apple.developer.private-cloud-compute</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>

```
### GenerativePartnerPrototypeExtension

> `/System/Library/ExtensionKit/Extensions/GenerativePartnerPrototypeExtension.appex/GenerativePartnerPrototypeExtension`

```diff

 	<string>com.apple.gms.GenerativePartnerPrototypeExtension</string>
 	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 	<array>
 		<string>GenerativePartnerPrototypeExtension</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>com.apple.openai</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 HomeKitNFCBackgroundTagReadingExtension

> `/System/Library/ExtensionKit/Extensions/HomeKitNFCBackgroundTagReadingExtension.appex/HomeKitNFCBackgroundTagReadingExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.nfcd.background.tag.reading.extension.nonui</key>
	<true/>
	<key>com.apple.nfcd.background.tag.reading.extension.urls</key>
	<array>
		<string>X-HM:</string>
		<string>x-hm:</string>
		<string>MT:</string>
		<string>mt:</string>
		<string>CH:</string>
		<string>ch:</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.homed.xpc.nfc.tag</string>
	</array>
</dict>
</plist>

```
### LighthouseASRReplay

> `/System/Library/ExtensionKit/Extensions/LighthouseASRReplay.appex/LighthouseASRReplay`

```diff

 	</array>
 	<key>com.apple.siri.analytics.assistant</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.icl</string>
+	</array>
 </dict>
 </plist>
 

```
### ODDFeatureDigestsExtension

> `/System/Library/ExtensionKit/Extensions/ODDFeatureDigestsExtension.appex/ODDFeatureDigestsExtension`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.ODDFeatureDigestsExtension</string>
+	<string>com.apple.siri.ODDFeatureDigestsExtension</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
+	<key>com.apple.private.assistant.settings</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
-	<string>com.apple.ODDFeatureDigestsExtension</string>
+	<string>com.apple.siri.ODDFeatureDigestsExtension</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Siri.SELFProcessedEvent</string>

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
+	<key>com.apple.private.logging.stream</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
-		<string>com.apple.ODDFeatureDigestsExtension</string>
-		<string>com.apple.poirot.poirot_tool</string>
+		<string>com.apple.siri.ODDFeatureDigestsExtension</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant</string>
+		<string>com.apple.assistant.support</string>
+		<string>com.apple.assistant.backedup</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
-		<string>com.apple.ODDFeatureDigestsExtension</string>
+		<string>com.apple.siri.ODDFeatureDigests.worker</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant</string>
+		<string>com.apple.assistant.support</string>
+		<string>com.apple.assistant.backedup</string>
+	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
-		<string>com.apple.ODDFeatureDigestsExtension</string>
+		<string>com.apple.siri.ODDFeatureDigests.worker</string>
 	</array>
 </dict>
 </plist>

```
### PhotoPicker

> `/System/Library/ExtensionKit/Extensions/PhotoPicker.appex/PhotoPicker`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

```
### PhotosMessagesApp

> `/System/Library/ExtensionKit/Extensions/PhotosMessagesApp.appex/PhotosMessagesApp`

```diff

 	</array>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/PhotosPicker`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

```
### PhotosPosterProvider

> `/System/Library/ExtensionKit/Extensions/PhotosPosterProvider.appex/PhotosPosterProvider`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.sensitivecontentanalysis.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
 	<key>com.apple.idle-timer-services</key>
 	<true/>
 	<key>com.apple.lightsourcesupport.listener</key>

 		<string>/Media/PhotoData/</string>
 		<string>/Media/DCIM/</string>
 		<string>/Media/PhotoStreamsData/</string>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### SCARemoteView Appex

> `/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/SCARemoteView Appex`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.family.ageRange</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.ManagedSettingsAgent</string>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.ManagedSettingsAgent</string>

```

### 🆕 SearchPartnerInferenceProvider

> `/System/Library/ExtensionKit/Extensions/SearchPartnerInferenceProvider.appex/SearchPartnerInferenceProvider`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.external.searchpartner</string>
	<key>com.apple.private.network.system-token-fetch</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.tokengeneration</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.tokengeneration</string>
	</array>
</dict>
</plist>

```
### SiriVideoAppIntents

> `/System/Library/ExtensionKit/Extensions/SiriVideoAppIntents.appex/SiriVideoAppIntents`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+</dict>
+</plist>
 

```
### TGOnDeviceInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/TGOnDeviceInferenceProviderService.appex/TGOnDeviceInferenceProviderService`

```diff

 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeExperiences.TransparencyLog</string>
+		<string>AppleIntelligence.Reporting.Invocation.Step</string>
 	</array>
 	<key>com.apple.private.iokit.kernel-memory-access</key>
 	<true/>

```

### 🆕 AppleThunderboltSAT

> `/System/Library/Extensions/AppleThunderboltSAT.kext/AppleThunderboltSAT`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.private.kernel.get-kext-info</key>
	<true/>
</dict>
</plist>

```

### 🆕 VTL

> `/System/Library/Extensions/VTLAdapter.kext/PlugIns/VTL.plugin/VTL`

- No entitlements *(yet)*
### appmanagedfeaturesd

> `/System/Library/Frameworks/AppManagedFeatures.framework/Support/appmanagedfeaturesd`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.teslad-access</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.allowed</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.apsd</string>
+		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.seeding.client</string>
 		<string>com.apple.softwareupdateservicesd</string>
 		<string>com.apple.usernotifications.listener</string>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.private.cloudphotod.access</key>
 	<string>library</string>
-	<key>com.apple.private.cmphoto.decodeallowlist</key>
-	<dict>
-		<key>DICOM</key>
-		<array>
-			<integer>1684237600</integer>
-		</array>
-		<key>HEIF</key>
-		<array>
-			<integer>1635148593</integer>
-			<integer>1752589105</integer>
-			<integer>1635135537</integer>
-			<integer>1634743416</integer>
-			<integer>1634743400</integer>
-			<integer>1634755432</integer>
-			<integer>1634755438</integer>
-			<integer>1634755443</integer>
-			<integer>1634755439</integer>
-			<integer>1634759278</integer>
-			<integer>1634759272</integer>
-			<integer>1634742888</integer>
-			<integer>1634742376</integer>
-			<integer>1634759276</integer>
-			<integer>1936484717</integer>
-			<integer>1835821411</integer>
-			<integer>1785750887</integer>
-		</array>
-		<key>JFIF</key>
-		<array>
-			<integer>1785750887</integer>
-		</array>
-		<key>JPEG-XL</key>
-		<array>
-			<integer>1786276963</integer>
-			<integer>1786276896</integer>
-		</array>
-	</dict>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.receiver</key>

 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
-	<key>com.apple.private.nsurlsession.set-discretionary-override-value</key>
-	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.allowcollectionshare</key>

```
### BrowserEngineKit.Intermediary

> `/System/Library/Frameworks/BrowserEngineKit.framework/XPCServices/BrowserEngineKit.Intermediary.xpc/BrowserEngineKit.Intermediary`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.DeviceConfigurationAgent.consumer</string>
-		<string>com.apple.DeviceConfigurationAgent.consumer.async</string>
-		<string>com.apple.DeviceConfigurationAgent.publisher</string>
 		<string>com.apple.DocumentManagerCore.Downloads</string>
 		<string>com.apple.ciphermld</string>
 		<string>com.apple.family.ageRange.xpc</string>

```
### CoreTelephonyDiagnosticExtension

> `/System/Library/Frameworks/CoreTelephony.framework/PlugIns/CoreTelephonyDiagnosticExtension.appex/CoreTelephonyDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-only</key>
-	<array>
-		<string>/var/wireless/Library/Databases/</string>
-	</array>
 </dict>
 </plist>
 

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
+	<key>com.apple.locationd.use-wireless-client-info</key>
+	<true/>
 	<key>com.apple.migrationd.client</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

 		<string>com.apple.seserviced.sereservation.client</string>
 		<string>com.apple.SIMSetupUIBannerService</string>
 	</array>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.security.lockdownmode.read</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### CommCenterMobileHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CoreRepairCoreXPCService</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.appprotectiond.read</string>

 		<string>/System/Library/Trial/NamespaceDescriptors/</string>
 		<string>/System/Library/Trial/NamespaceDescriptors/com.apple.Trial.NamespaceDescriptor.861.plist</string>
 	</array>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### CommCenterRootHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterRootHelper`

```diff

 		<string>kern.proc.all.0</string>
 		<string>net.routetable.0.0.3.0</string>
 	</array>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.CommCenterRootHelper</string>
 	<key>com.apple.tailspin.dump-output</key>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	</array>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.FileIndexer.client</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/Truth.plist</string>
 		<string>/.b/4/mobile/Library/Mobile Documents/</string>
 		<string>/.b/4/mobile/Library/LiveFiles/</string>
 		<string>/.b/4/mobile/Library/Application Support/FileProvider/</string>

```
### FinanceImageProcessingService

> `/System/Library/Frameworks/FinanceKit.framework/XPCServices/FinanceImageProcessingService.xpc/FinanceImageProcessingService`

```diff

 	<array>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.privacyaccountingd</string>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.appleneuralengine</string>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 		<string>FINANCE_ORDER_EXTRACTION</string>
 		<string>FINANCE_BOSKOOP</string>
 		<string>FINANCE_CONFIG</string>
+		<string>FINANCE_RECEIPT_LINKING</string>
 		<string>1291</string>
 		<string>1290</string>
 	</array>

```

### 🆕 com.apple.HealthKit.HealthKitTCCNotificationExtension

> `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthKitTCCNotificationExtension.appex/com.apple.HealthKit.HealthKitTCCNotificationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.authorization_bypass</key>
	<true/>
	<key>com.apple.private.healthkit.authorization_manager</key>
	<array>
		<string>read</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.healthd.server</string>
	</array>
</dict>
</plist>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	</array>
 	<key>com.apple.private.tcc.kill-on-assumed-identity-authorization-change</key>
 	<true/>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceHealthAccessReminder</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
+		<string>kTCCServiceHealthAccessReminder</string>
 		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.report</key>
+	<array>
+		<string>kTCCServiceHealthAccessReminder</string>
+	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>
 	<array>
 		<string>kTCCServiceMotion</string>

 		<string>com.apple.HealthKit.SensitiveLogsTemporaryEnablement</string>
 		<string>com.apple.nanolifestyle.sessiontrackerapp</string>
 		<string>com.apple.Noise</string>
+		<string>com.apple.powerlogd</string>
 		<string>com.apple.private.health.cardio-fitness</string>
 		<string>com.apple.sleepd</string>
 		<string>com.apple.workout.features.dormancy</string>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 		<string>/private/var/db/MobileIdentityData/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.AppleMediaServices/</string>

```

### 🆕 NearFieldPrivateServiceLocation

> `/System/Library/LocationBundles/NearFieldPrivateServiceLocation.bundle/NearFieldPrivateServiceLocation`

- No entitlements *(yet)*

### 🆕 SpotlightIndexingProgressSettings

> `/System/Library/PreferenceBundles/SpotlightIndexingProgressSettings.bundle/SpotlightIndexingProgressSettings`

- No entitlements *(yet)*
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.corewifi.mac-addr</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>

```
### agentstored

> `/System/Library/PrivateFrameworks/AgentSessionKitRuntime.framework/agentstored`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.agentsessionstore</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.biome.compute.publisher.service.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>
+		<string>com.apple.kvsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/AppIntentsRunnerXPCService`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.no-container</key>
 	<true/>
+	<key>com.apple.private.update-any-appshortcutsprovider</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>

 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.intelligenceflow.uiContext</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.registry</string>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>InternalBuild</string>
 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
 		<string>UniqueDeviceIDData</string>

```

### 🆕 appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/appleaccounttransparencyd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.cdp.telemetry</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.appleaccounttransparencyd</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.transparencyd.aet</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.appleaccounttransparency</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### AppleCredentialManagerDaemon

> `/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.daemon.allow</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.transportrestrictedmode.configurewhilelocked.allow</key>

```

### 🆕 FakeAPNSServerTests

> `/System/Library/PrivateFrameworks/ApplePushService.framework/FakeAPNSServerTests.xctest/FakeAPNSServerTests`

- No entitlements *(yet)*
### apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

 	<true/>
 	<key>com.apple.private.network.aop2_offload</key>
 	<true/>
-	<key>com.apple.private.power.notifications</key>
-	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

 	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
+		<string>systemgroup.com.apple.safetyalerts</string>
 		<string>systemgroup.com.apple.osanalytics</string>
 		<string>systemgroup.com.apple.sharedpclogging</string>
 	</array>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.assistant.shared</string>
+		<string>group.com.apple.assistant.shared.backedup</string>
 		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.weather</string>
 	</array>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.assistant.shared</string>
+		<string>group.com.apple.assistant.shared.backedup</string>
 		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.weather</string>
 	</array>

 		<string>com.apple.siri.morphunassetsupdaterd</string>
 		<string>com.apple.siri.orchestration.prescribedaction</string>
 		<string>com.apple.siri.reference_resolution_module</string>
+		<string>com.apple.siri.scda</string>
 		<string>com.apple.siri.shared_flow_plugin_service</string>
 		<string>com.apple.siri.siriaudio-helper</string>
 		<string>com.apple.siri.uaf.service</string>

 	<true/>
 	<key>com.apple.siri.opportune_speaking_model_service</key>
 	<true/>
+	<key>com.apple.siri.scda</key>
+	<true/>
 	<key>com.apple.siri.siriaudio-helper</key>
 	<true/>
 	<key>com.apple.siri.sync_deep_verification</key>

 		<string>INTELLIGENCE_FLOW_PLAN_RESOLUTION</string>
 		<string>MYRIAD_BOOSTS</string>
 		<string>SEARCH_TOOL_ANSWER_SYNTHESIS</string>
-		<string>SIRI_AUDIO_APP_SELECTION_HOMEACCESSORY</string>
 		<string>SIRI_AUDIO_APP_SELECTION_HOMEPOD</string>
 		<string>SIRI_AUDIO_DISABLE_MEDIA_ENTITY_SYNC</string>
 		<string>SIRI_AUDIO_LAPSED_MUSIC_USER</string>

```
### deleted_helper

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper`

```diff

 	<true/>
 	<key>com.apple.private.osanalytics.SubmitLogs.allow</key>
 	<true/>
+	<key>com.apple.private.security.datavault.controller</key>
+	<true/>
 	<key>com.apple.private.vfs.entitled-reserve-access</key>
 	<true/>
 </dict>

```
### callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

```diff

 	</array>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.TextUnderstanding.process</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.assistant.client</key>

 	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.agentSessionStore</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.gms.availability</key>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.TextUnderstanding.process</string>
+		<string>com.apple.generativeexperiences.agentSessionStore</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.xpc-service-name</key>
 	<array>

```
### SetStoreUpdateService

> `/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.ts.mobile-keybag-access</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.SetStoreUpdateService</string>
 	<key>platform-application</key>

```
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.SiriFeatureStore</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>

 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/purpose_auto/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.locationd.activity</key>
+	<true/>
+	<key>com.apple.locationd.clearauthorizations</key>
+	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
+	<key>com.apple.locationd.spectator</key>
+	<true/>
+	<key>com.apple.locationd.status</key>
+	<true/>
 	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
 	<true/>
 	<key>com.apple.private.CoreAnalytics.Preferences.write</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.locationd.desktop.agent</string>
+		<string>com.apple.locationd.desktop.registration</string>
+		<string>com.apple.locationd.desktop.synchronous</string>
+		<string>com.apple.locationd.desktop.spi</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>com.apple.analyticsagent</string>
 	</array>
+	<key>com.apple.security.personal-information.location</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.analyticsagent</string>
 	<key>platform-application</key>

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 	</array>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.iokit.CoreAnalytics.user</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

 	</array>
 	<key>com.apple.uservault</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.icl</string>
+	</array>
 </dict>
 </plist>
 

```
### CorePrescriptionService

> `/System/Library/PrivateFrameworks/CorePrescription.framework/XPCServices/CorePrescriptionService.xpc/CorePrescriptionService`

```diff

 	<true/>
 	<key>com.apple.managedassets.api.usermode</key>
 	<true/>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
 	<key>com.apple.private.arkit.authorization</key>
 	<array>
 		<string>appClipCode</string>

 	</array>
 	<key>com.apple.private.security.storage.Health</key>
 	<true/>
+	<key>com.apple.purplebuddy.budd.access</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>AppleKeyStoreUserClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.arkitd.local_res_fact</string>

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.managedassetsd</string>
 		<string>com.apple.masd</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.purplebuddy.budd.xpc</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.musebuddy</string>
+		<string>com.apple.musebuddy.notbackedup</string>
+		<string>com.apple.purplebuddy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.polaris.client</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>CLIENT_ENTITLEMENT</string>

 		<string>/Library/CoreDuet/</string>
 		<string>/Library/PeopleSuggester/</string>
 		<string>/Library/Caches/com.apple.corespeech.cat.xpc/</string>
+		<string>/Library/Caches/com.apple.speechmaintenanced/ranked_entity_cache/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 		<string>/Library/Biome/</string>
 	</array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.polaris.cache</string>
 		<string>com.apple.siri.deviceselection</string>
 		<string>com.apple.account.AppleAccount</string>
 		<string>com.apple.accounts.appleaccount.fullaccess</string>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.corespeech</string>
+		<string>com.apple.icl</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### speechmodeltrainingd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd`

```diff

 		<string>372</string>
 		<string>401</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.icl</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/CoreCapture/BT</string>
+		<string>/private/var/db/com.apple.countryd/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.WirelessCoexManager</string>
 		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.countryd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### DTServiceHub

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.cltm</string>
+		<string>com.apple.springboard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.sysmond.client</key>
 	<true/>
+	<key>modify-anchor-certificates</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### IMDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/IMDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.security.storage.Messages</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/SMS/com.apple.imdpersistence.IMDIndexingThrottleHistory.plist</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.IMCoreSpotlight</string>

```
### ScreenTimeDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ScreenTimeDiagnosticExtension.appex/ScreenTimeDiagnosticExtension`

```diff

 	</array>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/ScreenTimeDiagnostics/</string>

 	<array>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### EnergyKitService

> `/System/Library/PrivateFrameworks/EnergyKitInternal.framework/XPCServices/EnergyKitService.xpc/EnergyKitService`

```diff

 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.EnergyKitService</string>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.wpc.energyservices.keychain</string>

```
### DraftingExtension-iOS

> `/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.siriappintentsd.orchestrator</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.feedback</string>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
-	<key>com.apple.siriappintentsd.orchestrator</key>
-	<true/>
 </dict>
 </plist>
 

```

### 🆕 FileBrowsingPathResolver

> `/System/Library/PrivateFrameworks/FileBrowsingServices.framework/XPCServices/FileBrowsingPathResolver.xpc/FileBrowsingPathResolver`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.FileBrowsingServices.PathResolver</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.FileBrowsingServices.PathResolver</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.CloudDocs</string>
	</array>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.fileprovider.fetch-url</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.lookup</key>
	<dict>
		<key>appGroup</key>
		<array>
			<string>group.com.apple.FileProvider.LocalStorage</string>
			<string>group.com.apple.FileProvider.DomainCaching</string>
		</array>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.librarian.unrestricted-container-access</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.storage.FileProvider</key>
	<true/>
	<key>com.apple.private.security.storage.MobileDocuments</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.FileProvider.LocalStorage</string>
		<string>group.com.apple.FileProvider.DomainCaching</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Mobile Documents/</string>
		<string>/Library/CloudStorage/</string>
		<string>/Library/LiveFiles/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.FileProvider</string>
		<string>com.apple.fileproviderd</string>
		<string>com.apple.FileCoordination</string>
		<string>com.apple.CoreServices.coreservicesd</string>
		<string>com.apple.coreservices.launchservicesd</string>
		<string>com.apple.coreservices.quarantine-resolver</string>
		<string>com.apple.lsd.mapdb</string>
		<string>com.apple.lsd.modifydb</string>
		<string>com.apple.bird</string>
		<string>com.apple.containermanagerd</string>
		<string>com.apple.SystemConfiguration.configd</string>
		<string>com.apple.FSEvents</string>
		<string>com.apple.iconservices</string>
		<string>com.apple.filesystems.fskitd</string>
		<string>com.apple.diskarbitrationd</string>
		<string>com.apple.mobile.keybagd.xpc</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### FitnessIntelligenceInferenceService

> `/System/Library/PrivateFrameworks/FitnessIntelligenceDaemonCore.framework/XPCServices/FitnessIntelligenceInferenceService.xpc/FitnessIntelligenceInferenceService`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sirittsservice.modify-proxy-assets</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
 	</array>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>GetSystemAppMigrationStatus</string>
+	</array>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
 	<key>com.apple.private.photos.allowassetexpunge</key>

 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/installd/Library/MobileInstallation/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Turn</string>
 		<string>com.apple.spotlightknowledged</string>
+		<string>com.apple.mobile.installd</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.AppleMediaServices</string>
+		<string>com.apple.mobile.installation</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### homeenergyd

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>

 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.homeenergyd</string>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.wpc.energyservices.keychain</string>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.private.energykit</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.fillmore.getTriggerStats</key>
 	<true/>
 	<key>com.apple.private.fillmore.provideEmac</key>

 	<array>
 		<string>/Home/DemoContent/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.AppleMediaServices/sap-setup-cert.txt</string>
+		<string>/Library/Caches/com.apple.AppleMediaServices/Metrics/</string>
+		<string>/Library/Caches/com.apple.AppleMediaServices/PersistedBags/</string>
+		<string>/Library/com.apple.AppleMediaServices/Metrics/</string>
+		<string>/Library/com.apple.AppleMediaServices/PersistedBags/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.communicationtrustd.service</string>

```
### IDSBlastDoorService

> `/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.communicationtrustd.service</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.messagesescrowd</string>
+		<string>com.apple.asktod</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.asktod</key>
+	<true/>
 </dict>
 </plist>
 

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 		<string>com.apple.kvsd</string>
 		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.contacts.poster.api</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.naturallanguaged</string>
 		<string>com.apple.dmd.policy</string>
 		<string>com.apple.modelmanager</string>

 		<string>com.apple.CalendarAgent</string>
 		<string>com.apple.callkit.callcontrollerhost</string>
 		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.siri.device_resolution</string>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<string>com.apple.intelligenceflow.intelligenceflowd</string>
 	<key>com.apple.Archetype.personalContext</key>
 	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>cellular-plan</string>
+		<string>internal</string>
+		<string>notify-all</string>
+		<string>spi</string>
+		<string>data-usage</string>
+		<string>identity</string>
+		<string>phone</string>
+		<string>dm</string>
+	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>

 	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
+	<key>com.apple.fileprovider.fetch-url</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	<true/>
 	<key>com.apple.itunescloudd.private</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
-	<dict/>
+	<dict>
+		<key>Dormancy</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Dormancy.Feature.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>defaultResolverInteractions</string>

 		<string>entitySimilarityFeatures</string>
 		<string>siriRemembers</string>
 	</array>
+	<key>com.apple.private.memorystatus</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>

 	<true/>
 	<key>com.apple.runningboard.assertions.shortcuts</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.siri</key>
+	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.intelligenceflow</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.locationd.registration</string>
 		<string>com.apple.locationd.synchronous</string>

 		<string>com.apple.generativeexperiences.agentMediaStore</string>
 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.FileDerivativeService</string>
+		<string>com.apple.FileProvider</string>
 		<string>com.apple.siri.audio.stream.player.service.xpc</string>
 		<string>com.apple.siri.turn.service.xpc</string>
 		<string>com.apple.powerexperienced.resourceusage</string>

 		<string>com.apple.siri.identityprovider</string>
 		<string>com.apple.homed</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.memorystatus_vm_pressure_level</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

 	<true/>
 	<key>com.apple.spotlight.search</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 	<key>com.apple.symptoms.NetworkDiagnostics</key>
 	<true/>
 	<key>com.apple.trial.client</key>

 	</array>
 	<key>platform-application</key>
 	<true/>
+	<key>vm-pressure-level</key>
+	<true/>
 </dict>
 </plist>
 

```
### lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded`

```diff

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.lockdownmoded.contact-exemptions</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### MapsBlastDoorService

> `/System/Library/PrivateFrameworks/MapsBlastDoorSupport.framework/XPCServices/MapsBlastDoorService.xpc/MapsBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.modelmanager.query</key>
+	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.HomeAIDESPlugin</key>

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd</string>
 	</dict>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.Intent</string>
+	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.shazamkit.allow-signature-generation</key>

 		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
 		<string>/private/var/mobile/Library/Trial/Treatments/361/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_AppleEmbeddingModel/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.account.AppleAccount</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.intents.intents-helper</string>
 		<string>com.apple.cloudphotod</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.ciphermld</string>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.modelmanager.query</key>
+	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.HomeAIDESPlugin</key>

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd</string>
 	</dict>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.Intent</string>
+	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.shazamkit.allow-signature-generation</key>

 		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
 		<string>/private/var/mobile/Library/Trial/Treatments/361/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_AppleEmbeddingModel/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.account.AppleAccount</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.intents.intents-helper</string>
 		<string>com.apple.cloudphotod</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.ciphermld</string>

```
### MediaAnalysisBlastDoorService

> `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService`

```diff

 	<array>
 		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
 	</array>
-	<key>com.apple.private.cmphoto.decodeallowlist</key>
-	<dict>
-		<key>DICOM</key>
-		<array>
-			<integer>1684237600</integer>
-		</array>
-		<key>HEIF</key>
-		<array>
-			<integer>1635148593</integer>
-			<integer>1752589105</integer>
-			<integer>1635135537</integer>
-			<integer>1634743416</integer>
-			<integer>1634743400</integer>
-			<integer>1634755432</integer>
-			<integer>1634755438</integer>
-			<integer>1634755443</integer>
-			<integer>1634755439</integer>
-			<integer>1634759278</integer>
-			<integer>1634759272</integer>
-			<integer>1634742888</integer>
-			<integer>1634742376</integer>
-			<integer>1634759276</integer>
-			<integer>1936484717</integer>
-			<integer>1835821411</integer>
-			<integer>1785750887</integer>
-		</array>
-		<key>JFIF</key>
-		<array>
-			<integer>1785750887</integer>
-		</array>
-		<key>JPEG-XL</key>
-		<array>
-			<integer>1786276963</integer>
-			<integer>1786276896</integer>
-		</array>
-	</dict>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd`

```diff

 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>

```
### HubbleBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/HubbleBlastDoorService.xpc/HubbleBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
+		<string>com.apple.gpumemd.check_in_request</string>
 		<string>com.apple.language.changed</string>
 		<string>com.apple.mobile.keybagd.lock_status</string>
 		<string>com.apple.powerlog.*</string>

```
### MessagesAirlockService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### MessagesBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### UnknownSendersBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/UnknownSendersBlastDoorService.xpc/UnknownSendersBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### medialibraryd

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd`

```diff

 	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
 	<array>
 		<string>com.apple.Music</string>
+		<string>com.apple.NanoMusic</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

```
### nanosystemsettingsd

> `/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd`

```diff

 	<true/>
 	<key>com.apple.nanoregistry.BDE85C67-0FDD-4A95-A9B9-3CB5DD0C06A2</key>
 	<true/>
+	<key>com.apple.nanoregistry.F47B90E6-F2D5-49D0-A8F2-C880AA3FED19</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```

### 🆕 NFReportingService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFReportingService.xpc/NFReportingService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
</dict>
</plist>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/searchtoold`

```diff

 		<string>loiEntityRelevanceRanking</string>
 		<string>standardFeatureView</string>
 	</array>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.service.debug</key>

 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
 		<string>/private/var/mobile/Library/Assistant/SiriVocabulary/</string>
 		<string>/private/var/mobile/tmp/com.apple.omniSearch.searchtoold/</string>
+		<string>/private/var/mobile/tmp/com.apple.searchtoold/</string>
 		<string>/Library/Shortcuts/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.networkserviceproxy.fetch-token</string>
 		<string>com.apple.carousel.notificationservice</string>
 		<string>com.apple.Maps.xpc.connectionBroker.endpointRecorder</string>
 		<string>com.apple.mobileasset.autoasset</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.networkserviceproxy.fetch-token</string>
 		<string>com.apple.carousel.notificationservice</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.assistant.cdm</string>

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.securityd.xpc</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.spaceattributiond</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<string>com.apple.amsondevicestoraged</string>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.amsondevicestoraged</string>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### com.apple.PerformanceTrace.PerformanceTraceService

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/com.apple.PerformanceTrace.PerformanceTraceService`

```diff

 <dict>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.agx.performance-spi</key>
 	<true/>
+	<key>com.apple.private.kernel.get-kernel-info</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
 	<key>com.apple.private.ktrace-allow</key>

 		<string>AGXDevice</string>
 		<string>AGXSharedUserClient</string>
 		<string>AppleCLPCUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
+		<string>RTBuddyUserClient</string>
 	</array>
+	<key>com.apple.system-task-ports.read</key>
+	<true/>
 </dict>
 </plist>
 

```
### remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>

```
### SESDiagnosticExtension

> `/System/Library/PrivateFrameworks/SEService.framework/PlugIns/SESDiagnosticExtension.appex/SESDiagnosticExtension`

```diff

 		<string>/private/var/mobile/Library/Logs/</string>
 		<string>/private/var/mobile/Library/Preferences/</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.seserviced</string>
+		<string>com.apple.MobileBluetooth.debug</string>
+	</array>
 </dict>
 </plist>
 

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```diff

 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/ScreenTimeDiagnostics/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Application Support/com.apple.remotemanagementd/</string>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```
### servicesintelligenced

> `/System/Library/PrivateFrameworks/ServicesIntelligence.framework/servicesintelligenced`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.servicesintelligenced</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.servicesintelligenced</string>
+	<key>com.apple.developer.healthkit.background-delivery</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
+	<key>com.apple.private.healthkit.read_authorization_bypass</key>
+	<array>
+		<string>HKWorkoutTypeIdentifier</string>
+	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.restricted-application-groups</key>

 		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.ciphermld</string>
 		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.healthd.server</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### fitcored

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored`

```diff

 	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.seymour.xpc.appstore</key>
 	<true/>
 	<key>com.apple.private.seymour.xpc.asset</key>

```
### AirDropAlertUI

> `/System/Library/PrivateFrameworks/Sharing.framework/PlugIns/AirDropAlertUI.appex/AirDropAlertUI`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.security.no-sandbox</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/mobile/Containers/Data/PluginKitPlugin/</string>
-		<string>/private/</string>
-		<string>/</string>
-	</array>
+	<array/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.sharing.transfer-observer</string>

```
### siriappintentsd

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/siriappintentsd`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppleIntelligence.Reporting.Invocation.Step</string>
+		<string>SessionResumptionEventBundle</string>
+		<string>SecurityValidationEvent</string>
 	</array>
 	<key>com.apple.private.corespotlight.skgupdater</key>
 	<true/>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.audio.AudioQueueServer</string>
 		<string>com.apple.audio.AudioSession</string>
+		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.coremedia.samplebufferaudiorenderer.xpc</string>
 		<string>com.apple.coremedia.samplebufferrendersynchronizer.xpc</string>

```
### SiriHeadlessService

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService`

```diff

 	<true/>
 	<key>com.apple.assistant.uibridge-service</key>
 	<true/>
+	<key>com.apple.assistantd.odeon-remote</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<array>
 		<string>endpoint-read</string>
 	</array>
+	<key>com.apple.private.homekit</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.necp.match</key>

 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.siri.orchestration.capabilities</string>
+		<string>com.apple.assistantd.odeon-remote</string>
+		<string>com.apple.siri.audiopowerupdate.xpc</string>
 	</array>
 	<key>com.apple.siri.analytics.assistant</key>
 	<true/>
+	<key>com.apple.siri.audiopowerupdate.xpc</key>
+	<true/>
 	<key>com.apple.siri.client_lite</key>
 	<true/>
 	<key>com.apple.siri.deviceselection.allow</key>

```
### sleepd

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/Truth.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.developer.healthkit</key>
+	<true/>
 	<key>com.apple.frontboard.disable-watchdog</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### TelephonyBlastDoorService

> `/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/XPCServices/TelephonyBlastDoorService.xpc/TelephonyBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<array>
 		<string>GroupActivitySession</string>
 		<string>CommApps.CallIntelligence.HoldAssistFedStats</string>
+		<string>CommApps.CallIntelligence.CallContextCardsFedStats</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>

 	<array>
 		<string>/Media/Purchases/</string>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### ThumbnailsBlastDoorService

> `/System/Library/PrivateFrameworks/ThumbnailsBlastDoorSupport.framework/XPCServices/ThumbnailsBlastDoorService.xpc/ThumbnailsBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

 	<array>
 		<string>hw.osenvironment</string>
 	</array>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<array>
 		<string>Accessibility.SoundDetection</string>
 		<string>Alarm</string>
+		<string>App.InFocus</string>
 		<string>App.Intent</string>
 		<string>App.Intents.Transcript</string>
 		<string>CarPlay.Connected</string>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>App.InFocus</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>CarPlay.Connected</key>
 				<dict>
 					<key>mode</key>

```
### WalletBlastDoorService

> `/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/XPCServices/WalletBlastDoorService.xpc/WalletBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.corewifi.mac-addr</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.mode.assertion.user-requested.client-identifiers</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.corewifi.mac-addr</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.mode.assertion.user-requested.client-identifiers</key>

```
### RemoteiCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Extensions/RemoteiCloudQuotaUI.appex/RemoteiCloudQuotaUI`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.small-offer-button</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Library</string>

```
### itunesstored

> `/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored`

```diff

 	<true/>
 	<key>com.apple.networkd.set_source_application</key>
 	<true/>
+	<key>com.apple.odi.internal</key>
+	<true/>
 	<key>com.apple.odr.itunesstored</key>
 	<true/>
 	<key>com.apple.passes.add-silently</key>

```

### 🆕 ReplayKitScreenRecordingAttribution

> `/System/Library/SystemStatus/Bundles/Attribution/ReplayKitScreenRecordingAttribution.bundle/ReplayKitScreenRecordingAttribution`

- No entitlements *(yet)*
### kbd

> `/System/Library/TextInput/kbd`

```diff

 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.frontboard.systemappservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.setTypingActive</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>

```

### 🆕 com.apple.Dataclass.Siri

> `/System/Library/iCloudSettings/com.apple.Dataclass.Siri.bundle/com.apple.Dataclass.Siri`

- No entitlements *(yet)*
### AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.visionproapp.kvs</string>
 	<key>adi-client</key>
 	<string>143531244</string>
 	<key>application-identifier</key>

 	<true/>
 	<key>com.apple.coremedia.salplayer</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.devicesharingd</string>
+		<string>com.apple.tv</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Books

> `/private/var/staged_system_apps/Books.app/Books`

```diff

 	<array/>
 	<key>com.apple.developer.carplay-audio</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.nanoregistry.BDE85C67-0FDD-4A95-A9B9-3CB5DD0C06A2</key>
 	<true/>
+	<key>com.apple.nanoregistry.F47B90E6-F2D5-49D0-A8F2-C880AA3FED19</key>
+	<true/>
 	<key>com.apple.nanoregistry.termsacknowledgementregistry</key>
 	<true/>
 	<key>com.apple.nanosystemsettings</key>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>Dormancy</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Dormancy.Feature.RemoteUserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>

 		<string>/Library/UserConfigurationProfiles/PayloadManifest.plist</string>
 		<string>/Library/UserConfigurationProfiles/PayloadDependency.plist</string>
 		<string>/Library/UserConfigurationProfiles/ClientTruth.plist</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 		<string>/Library/Caches/MappedImageCache/com.apple.nanotimekit.ClockFaceSnapshots/</string>
 		<string>/Library/Mail/</string>
 		<string>/Library/Caches/PassKit/</string>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
-	<key>com.apple.private.healthkit.authorization_bypass</key>
-	<true/>
 	<key>com.apple.private.healthkit.authorization_manager</key>
 	<array>
 		<string>read</string>
 		<string>write</string>
 	</array>
-	<key>com.apple.private.healthkit.source.default</key>
-	<string>com.apple.Health</string>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.siri</string>
+		<string>com.apple.camera</string>
 	</array>
 	<key>com.apple.private.imagecapturecore.authorization_bypass</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
-	<key>com.apple.springboard.private.action-button-events</key>
-	<true/>
 	<key>com.apple.springboard.private.capture-button-events</key>
 	<true/>
 	<key>com.apple.springboard.setWantsLockButtonEvents</key>
 	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
+		<string>access-call-capabilities</string>
+		<string>access-call-providers</string>
 		<string>access-calls</string>
 	</array>
 	<key>com.apple.trial.client</key>

```
### LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
-	<key>com.apple.private.healthkit.authorization_bypass</key>
-	<true/>
 	<key>com.apple.private.healthkit.authorization_manager</key>
 	<array>
 		<string>read</string>
 		<string>write</string>
 	</array>
-	<key>com.apple.private.healthkit.source.default</key>
-	<string>com.apple.Health</string>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.siri</string>
+		<string>com.apple.camera</string>
 	</array>
 	<key>com.apple.private.imagecapturecore.authorization_bypass</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
-	<key>com.apple.springboard.private.action-button-events</key>
-	<true/>
 	<key>com.apple.springboard.private.capture-button-events</key>
 	<true/>
 	<key>com.apple.springboard.requestDeviceUnlock</key>

 	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
+		<string>access-call-capabilities</string>
+		<string>access-call-providers</string>
 		<string>access-calls</string>
 	</array>
 	<key>com.apple.trial.client</key>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.communicationtrustd</key>
+	<array>
+		<string>read</string>
+		<string>write</string>
+	</array>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.people</key>

 		<string>com.apple.contacts.poster.api</string>
 		<string>com.apple.sharingd.pairedcontactmanager</string>
 		<string>com.apple.Archetype.personalContext</string>
+		<string>com.apple.communicationtrustd.service</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.communicationSafetySettings</string>
+		<string>com.apple.CommunicationTrust</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-extended-share-access</key>
 	<array>
 		<string>InProcessShareOwnerParticipantInfo</string>

 		<string>CloudKit</string>
 		<string>CloudDocuments</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.DocumentsApp</string>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-read</key>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.appleaccount.identity.read</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 		<string>com.apple.icloud.findmydeviced.localfindable</string>
 		<string>com.apple.findmydeviced.btfindingsession</string>
 		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.hsa-authentication-server</string>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.energykit</key>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Home</string>
 	<key>com.apple.developer.usernotifications.critical-alerts</key>
 	<true/>
 	<key>com.apple.dropin</key>

 		<string>com.apple.AddressBook.abd</string>
 		<string>com.apple.AttentionAwareness</string>
 		<string>com.apple.CompanionLink</string>
+		<string>com.apple.CoreGraphics.CGPDFService</string>
 		<string>com.apple.DistributedTimers</string>
 		<string>com.apple.EnergyKitService</string>
 		<string>com.apple.OSASyncProxy.client</string>

 		<string>com.apple.system.opendirectoryd.api</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>
+		<string>com.apple.videoconference.camera</string>
 		<string>com.apple.wirelessproxd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>

 		<string>com.apple.AddressBook.abd</string>
 		<string>com.apple.AttentionAwareness</string>
 		<string>com.apple.CompanionLink</string>
+		<string>com.apple.CoreGraphics.CGPDFService</string>
 		<string>com.apple.DistributedTimers</string>
 		<string>com.apple.EnergyKitService</string>
 		<string>com.apple.OSASyncProxy.client</string>

 		<string>com.apple.system.opendirectoryd.api</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>
+		<string>com.apple.videoconference.camera</string>
 		<string>com.apple.wirelessproxd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>

```
### HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Home</string>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>

```
### HomeWidgetLockScreen

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Home</string>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>

```
### Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```diff

 	</array>
 	<key>com.apple.developer.declared-age-range</key>
 	<true/>
+	<key>com.apple.developer.private-cloud-compute</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp</string>
 	<key>com.apple.developer.usernotifications.communication</key>

 	<array>
 		<string>com.apple.GenerativePlaygroundApp</string>
 	</array>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.stickers.api</string>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 	<true/>
 	<key>com.apple.das.private.bgtask.continuedprocessing</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.healthkit.access</key>

```
### MagnifierExtension

> `/private/var/staged_system_apps/Magnifier.app/Extensions/MagnifierExtension.appex/MagnifierExtension`

```diff

 		<string>com.apple.networkserviceproxy</string>
 		<string>com.apple.speech.localspeechrecognition</string>
 		<string>com.apple.campo</string>
+		<string>com.apple.coremedia.cameraviewfinder</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.inputservice.keyboardui</string>
+		<string>com.apple.inputservice.input-ui-host</string>
+		<string>com.apple.UIKit.KeyboardManagement.hosted</string>
+		<string>com.apple.TextInput</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.duetexpertd.assistant-actions</string>
 		<string>com.apple.internal.SpotlightAutomationTester</string>
+		<string>com.apple.biome.compute.source.user</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### NotesAppMigrationExtension

> `/private/var/staged_system_apps/MobileNotes.app/Extensions/NotesAppMigrationExtension.appex/NotesAppMigrationExtension`

```diff

 	<string>notes</string>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.notes.import</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Shortcuts/</string>
+	</array>
+	<key>com.apple.shortcuts.stepwise-execution</key>
+	<true/>
+	<key>com.apple.shortcuts.variable-injection</key>
+	<true/>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 </dict>
 </plist>
 

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/AppleInternal/Library/Frameworks/ContextStagingIntents.framework</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### com.apple.mobilenotes.QuickLookExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.QuickLookExtension.appex/com.apple.mobilenotes.QuickLookExtension`

```diff

 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>fairplay-client</key>
 	<string>508119322</string>
 	<key>platform-application</key>

```
### MessagesAssistantExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.commcenter.xpc</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 		<string>/Library/Caches/com.apple.storeservices/</string>
 		<string>/Library/Caches/com.apple.ClipServices/</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 	</array>

```

### 🆕 SafariActionExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariActionExtension.appex/SafariActionExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
</dict>
</plist>

<!-- Launch Constraints (Parent) -->
{
  "appl": 1,
  "ccat": 0,
  "comp": 1,
  "reqs": {
    "is-init-proc": true
  },
  "vers": 1
}

```

### 🆕 SafariShareExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariShareExtension.appex/SafariShareExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
</dict>
</plist>

<!-- Launch Constraints (Parent) -->
{
  "appl": 1,
  "ccat": 0,
  "comp": 1,
  "reqs": {
    "is-init-proc": true
  },
  "vers": 1
}

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
-	<key>com.apple.modelcatalog.full-access</key>
-	<true/>
-	<key>com.apple.modelmanager.inference</key>
-	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.pairunpairobliterate</key>

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.WalletMobileAssets</string>
-		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
-		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Wallet.Transaction</string>
-		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
-		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
 	<key>com.apple.private.biometrickit.allow-connect</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
-	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
-	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 		<string>com.apple.Passbook</string>
 		<string>com.apple.PassbookUIService</string>
 	</array>
-	<key>com.apple.privatecloudcompute.admin</key>
-	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache/Library/Caches/com.apple.IconsCache/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
-		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
-		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 	<array>
 		<string>com.apple.financed.service.bankconnect</string>
 		<string>com.apple.odi.legacySPIService</string>
-		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.biome.access.user</string>
-		<string>com.apple.siri.uaf.service</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.mobileassetd.v2</string>
-		<string>com.apple.modelmanager</string>
 		<string>com.apple.finhealthd.service</string>
 		<string>com.apple.seserviced.storage-management-presentation</string>
 		<string>com.apple.AppDistributionLaunchAngel</string>

 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.seserviced.contactlessCredential.settings</string>
 		<string>com.apple.seserviced.designatedkeys</string>
-		<string>com.apple.UnifiedAssetFramework</string>
-		<string>com.apple.modelcatalog.ajax</string>
-		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
-		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Passwords.ChangePasswordForMe</string>
+		<string>Passwords.SecurityRecommendations</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.personas.no.inherit</key>
+	<true/>
 	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>
 	<true/>
 	<key>com.apple.private.safariviewservice.automatic-password-change</key>

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Safari/AutoFillQuirks.plist</string>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 	<true/>
 	<key>com.apple.private.cloudphotod.access</key>
 	<string>management</string>
-	<key>com.apple.private.cmphoto.decodeallowlist</key>
-	<dict>
-		<key>DICOM</key>
-		<array>
-			<integer>1684237600</integer>
-		</array>
-		<key>HEIF</key>
-		<array>
-			<integer>1635148593</integer>
-			<integer>1752589105</integer>
-			<integer>1635135537</integer>
-			<integer>1634743416</integer>
-			<integer>1634743400</integer>
-			<integer>1634755432</integer>
-			<integer>1634755438</integer>
-			<integer>1634755443</integer>
-			<integer>1634755439</integer>
-			<integer>1634759278</integer>
-			<integer>1634759272</integer>
-			<integer>1634742888</integer>
-			<integer>1634742376</integer>
-			<integer>1634759276</integer>
-			<integer>1936484717</integer>
-			<integer>1835821411</integer>
-			<integer>1785750887</integer>
-		</array>
-		<key>JFIF</key>
-		<array>
-			<integer>1785750887</integer>
-		</array>
-		<key>JPEG-XL</key>
-		<array>
-			<integer>1786276963</integer>
-			<integer>1786276896</integer>
-		</array>
-	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<array/>
 	<key>com.apple.developer.carplay-audio</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.pass-type-identifiers</key>
 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>243LU875E5.com.apple.podcasts</string>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.excludes-extensions</key>

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.podcasts</string>
+	</dict>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.fpsd.client</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.absd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>

 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.cache_delete</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.sleepd.sleepserver</string>
+		<string>com.apple.toolkitd.xpc</string>
 		<string>com.apple.translationd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>

 	<true/>
 	<key>com.apple.springboard.webClipService</key>
 	<true/>
+	<key>com.apple.toolkit.request-immediate-indexing.allow</key>
+	<true/>
+	<key>com.apple.toolkit.request-reindex.allow</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>180</string>

```

### 🆕 TVRemoteIntents

> `/private/var/staged_system_apps/TVRemote.app/PlugIns/TVRemoteIntents.appex/TVRemoteIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.tvremotecore.xpc</string>
	</array>
	<key>com.apple.sharing.Client</key>
	<true/>
	<key>com.apple.springboard.activateRemoteAlert</key>
	<true/>
	<key>com.apple.springboard.launchapplications</key>
	<true/>
	<key>com.apple.springboard.lockScreenContentAssertion</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
</dict>
</plist>

```

### 🆕 TVRemoteWidget

> `/private/var/staged_system_apps/TVRemote.app/PlugIns/TVRemoteWidget.appex/TVRemoteWidget`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.TVRemoteApp</string>
</dict>
</plist>

```

### 🆕 BatteryDischargeService

> `/usr/libexec/BatteryDischargeService`

- No entitlements *(yet)*
### NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

 	</dict>
 	<key>com.apple.private.MobileContainerManager.userManagedAssets</key>
 	<true/>
+	<key>com.apple.private.apfs.get-graft-info</key>
+	<true/>
 	<key>com.apple.private.apfs.purgeable.extents</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.microlocation.connection</key>
+	<true/>
 	<key>com.apple.osintelligence.battery</key>
 	<true/>
 	<key>com.apple.osintelligence.charging</key>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 		<string>com.apple.lskdd.xpc</string>
 		<string>com.apple.mediaanalysisd.realtime</string>
 		<string>com.apple.mediaexperience.carplaymodecontroller.xpc</string>
-		<string>com.apple.MediaGroups.daemon</string>
 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### aned

> `/usr/libexec/aned`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.triald</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### aonsensed

> `/usr/libexec/aonsensed`

```diff

 	<true/>
 	<key>com.apple.nearbyinteraction.background</key>
 	<true/>
-	<key>com.apple.polaris.client</key>
-	<true/>
 	<key>com.apple.private.AccessorySensorManager</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<string>/Library/UnifiedAssetFramework</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.polaris.daemon_default</string>
-		<string>com.apple.polaris.systemgraph_v2</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
-		<string>com.apple.polaris.cache</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```
### applekeystored

> `/usr/libexec/applekeystored`

```diff

 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
-	<key>com.apple.rootless.datavault.controller.internal</key>
+	<key>com.apple.rootless.install</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>platform-application</key>

```
### arkitd

> `/usr/libexec/arkitd`

```diff

 	<true/>
 	<key>com.apple.locationd.trusted_ARKit_hinter</key>
 	<true/>
-	<key>com.apple.polaris.client</key>
-	<true/>
-	<key>com.apple.polaris.consumer.all-streams</key>
-	<true/>
-	<key>com.apple.polaris.producer.all-streams</key>
-	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
-	<key>com.apple.private.avfoundation.background-camera-access</key>
-	<true/>
-	<key>com.apple.private.avfoundation.capture.allow</key>
-	<true/>
-	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
-	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>arkitd</string>
-	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceCamera</string>
-		<string>kTCCServiceMicrophone</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.coremedia.capturesource</string>
-	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
-	<array>
-		<string>com.apple.coremedia</string>
-		<string>com.apple.avfoundation</string>
-		<string>com.apple.coreaudio</string>
-		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
-	</array>
-	<key>com.apple.security.iokit-user-client-class</key>
-	<array>
-		<string>AGXDeviceUserClient</string>
-		<string>H11ANEInDirectPathClient</string>
-		<string>IOSurfaceAcceleratorClient</string>
-		<string>IOSurfaceRootUserClient</string>
-	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.arkitd</string>
 </dict>

```
### asktod

> `/usr/libexec/asktod`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>ScreenTimeRequest</string>
+		<string>AskToBuy</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 		<string>pairing</string>
 		<string>token-auth</string>
 	</array>
-	<key>com.apple.MediaGroups.client</key>
-	<true/>
-	<key>com.apple.MediaGroups.groups</key>
-	<array>
-		<string>com.apple.media-group.solo-HomePodAccessory</string>
-		<string>com.apple.media-group.solo-SpeakerAccessory</string>
-		<string>com.apple.media-group.solo-AudioReceiverAccessory</string>
-		<string>com.apple.media-group.PSG</string>
-		<string>com.apple.media-group.media-system</string>
-		<string>com.apple.media-group.room</string>
-	</array>
 	<key>com.apple.MobileAsset.VoiceTriggerAssetsWatch</key>
 	<true/>
 	<key>com.apple.PairingManager.HomeKit</key>

 	<true/>
 	<key>com.apple.carousel.onWristMonitor.actions</key>
 	<string>monitor</string>
-	<key>com.apple.coreaudio.CanRecordPastData</key>
-	<true/>
-	<key>com.apple.coreaudio.CanRecordWithoutSessionActivation</key>
-	<true/>
 	<key>com.apple.coreaudio.allow-oop-v2-au</key>
 	<true/>
 	<key>com.apple.coreaudio.private.ProcessingTap</key>

 		<string>com.apple.lskdd</string>
 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.mediaanalysisd.realtime</string>
-		<string>com.apple.MediaGroups.daemon</string>
 		<string>com.apple.privacyaccountingd</string>
 		<string>com.apple.relatived.tempest</string>
 		<string>com.apple.SBUserNotification</string>

```
### batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

 	<true/>
 	<key>com.apple.private.powersource-read</key>
 	<true/>
+	<key>com.apple.private.smcsensor.user-access</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.batteryintelligence-notifications</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/usr/libexec/</string>
+		<string>/private/var/mobile/Library/Trial/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.batteryintelligence.internal</string>
+		<string>com.apple.batteryintelligenced.thermalcontrol</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<string>/Library/Trial/</string>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 	<true/>
 	<key>com.apple.private.IOSurface.wiredSendRights</key>
 	<true/>
+	<key>com.apple.private.MobileContainerManager.lookup</key>
+	<dict>
+		<key>daemon</key>
+		<array>
+			<string>com.apple.cameracaptured</string>
+		</array>
+	</dict>
 	<key>com.apple.private.MobileContainerManager.userManagedAssets</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
 		<string>SavageSerialNumber</string>
+		<string>BootManifestHash</string>
 	</array>
 	<key>com.apple.private.ReplayKitAngel.client</key>
 	<true/>

 	</array>
 	<key>com.apple.security.ts.ane-client</key>
 	<true/>
+	<key>com.apple.security.ts.daemon-container</key>
+	<true/>
 	<key>com.apple.security.ts.read-any-bundle</key>
 	<true/>
 	<key>com.apple.security.ts.read-factory-files</key>

```
### centaurid

> `/usr/libexec/centaurid`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.fenceservice</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceFaceID</string>

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.Carousel</string>
 		<string>com.apple.CloudKit</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.homed</string>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.cloud</key>
+	<true/>
+	<key>com.apple.private.photos.service.librarymanagement</key>
+	<true/>
 	<key>com.apple.private.replicator.dataProvider</key>
 	<true/>
+	<key>com.apple.private.security.storage.PhotosLibraries</key>
+	<true/>
 	<key>com.apple.private.sessionkit.listener</key>
 	<true/>
 	<key>com.apple.private.sleepd</key>

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

 		<string>com.apple.financed.service.coredatastore</string>
 		<string>com.apple.financed.service.store</string>
 		<string>com.apple.financed.service.financestore</string>
+		<string>com.apple.photos.service</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-write</key>
 	<string>com.apple.NanoHomeScreen.RelevantWidgetDefaults</string>

```
### hybridsearchd

> `/usr/libexec/hybridsearchd`

```diff

 		<dict>
 			<key>Sets</key>
 			<dict>
-				<key>TextUnderstanding.Extracted.Order</key>
+				<key>TextUnderstanding.Extracted.DeliveryTracking</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>TextUnderstanding.Extracted.DeliveryTracking</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>TextUnderstanding.Extracted.Event</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>TextUnderstanding.Extracted.Order</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
 				<key>TextUnderstanding.Extracted.RestaurantReservation</key>
 				<dict>
 					<key>mode</key>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	</array>
 	<key>com.apple.private.xpc.launchd.reboot</key>
 	<true/>
+	<key>com.apple.rootless.volume.iSCHardware</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```
### keybagd

> `/usr/libexec/keybagd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>

```
### locationd

> `/usr/libexec/locationd`

```diff

 			<key>send-command</key>
 			<dict/>
 		</dict>
+		<key>flip</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
 		<key>gesture</key>
 		<dict>
 			<key>send-command</key>

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appmanagedfeatures.configuration</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.CoreLocationConfig</string>

 		<string>com.apple.uarp.endpoint.transport</string>
 		<string>com.apple.telephony.control-msg.xpc</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appmanagedfeatures.configuration</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.safetyalerts</string>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
-		<string>/Library/VirtualCaptureCard/</string>
 		<string>/Library/ProVideoStorage/</string>
 		<string>/Library/Caches/com.apple.mediaplaybackd/</string>
 		<string>/Library/HTTPStorages/com.apple.mediaplaybackd/</string>

```
### mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

 	<true/>
 	<key>com.apple.modelmanager.query</key>
 	<true/>
+	<key>com.apple.private.exclaves.stats-server</key>
+	<true/>
 	<key>com.apple.private.kernel.darkboot</key>
 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>

```
### mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

 <dict>
 	<key>com.apple.AppleNVMeEAN.allow</key>
 	<true/>
+	<key>com.apple.AppleNVMeSanitize.allow</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.fdr-access</key>

 	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>
 	<true/>
+	<key>com.apple.private.iomfb.set-block</key>
+	<true/>
 	<key>com.apple.private.iowatchdog.user-access</key>
 	<true/>
 	<key>com.apple.private.memorystatus</key>

 		<string>AppleEffaceableStorageUserClient</string>
 		<string>AppleAPFSUserClient</string>
 		<string>IOMobileFramebufferUserClient</string>
+		<string>IOAVControllerConcreteUserClient</string>
 		<string>IOSurfaceRootUserClient</string>
 		<string>IOWatchdogUserClient</string>
 		<string>AppleNVMeEANUC</string>
+		<string>AppleNVMeUserClient</string>
 	</array>
 </dict>
 </plist>

```
### nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.networking.multicast</key>
 	<true/>
 	<key>com.apple.frontboard.app-badge-value-access</key>

 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDM.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Logs/CrashReporter/DiagnosticLogs/</string>

 		<string>com.apple.MobileBluetooth.debug</string>
 		<string>com.apple.Bridge</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

 	<array>
 		<string>/Library/Trial/</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.servicesanalytics.xpc</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### ospredictiond

> `/usr/libexec/ospredictiond`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.microlocation.connection</key>
+	<true/>
 	<key>com.apple.osintelligence.battery</key>
 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>

```

### 🆕 polarisd

> `/usr/libexec/polarisd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.afk.user</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.diagnosticpipeline.request</key>
	<true/>
	<key>com.apple.polaris.client</key>
	<true/>
	<key>com.apple.polaris.consumer.all-streams</key>
	<true/>
	<key>com.apple.polaris.producer.all-streams</key>
	<true/>
	<key>com.apple.private.PolarisSystemTransition.access</key>
	<true/>
	<key>com.apple.private.kernel.panic</key>
	<true/>
	<key>com.apple.private.logging.flush-buffers</key>
	<true/>
	<key>com.apple.private.master-sync-generator.user-access</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceMotion</string>
	</array>
	<key>com.apple.pst.ApplePayLockDown</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.logd.admin</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.polaris</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleParavirtDeviceUserClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>IOSurfaceRootUserClient</string>
		<string>NBDisplayControlUserClient</string>
		<string>NBCoreUserClient</string>
		<string>NBTimesyncUserClient</string>
		<string>AFKEndpointInterfaceUserClient</string>
		<string>CompanionMgrEPICUserClient</string>
		<string>AppleCCPUUserClient</string>
		<string>CCPUAppEPICUserClient</string>
		<string>CCPUDebugServiceUserClient</string>
		<string>CCPUPmuServiceUserClient</string>
		<string>CCPUExpertUserClient</string>
		<string>CCPURegSamplerUserClient</string>
		<string>CCPUTestEndpointUserClient</string>
		<string>CCPUSMCSamplerUserClient</string>
		<string>RootDomainUserClient</string>
		<string>SCodecUserClient</string>
		<string>VDKManifestAgentUserClient</string>
		<string>PSTDriverServerUserClient</string>
	</array>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.tailspin.dump-output</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceMediaLibrary</string>
+		<string>kTCCServiceMotion</string>
 		<string>kTCCServiceWillow</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 	<true/>
 	<key>com.apple.proximitycontrol.remoteActivity</key>
 	<true/>
+	<key>com.apple.rapport.AdvertisePublicBluetoothAddress</key>
+	<true/>
 	<key>com.apple.rapport.Client</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

```
### remoteappintentsd

> `/usr/libexec/remoteappintentsd`

```diff

 	<true/>
 	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
+	<key>com.apple.private.ids.agent.GroupRestricted</key>
+	<true/>
 	<key>com.apple.private.linkd.observationStatusRegistry</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>

```
### riskdatad

> `/usr/libexec/riskdatad`

```diff

 	<true/>
 	<key>com.apple.developer.networking.wifi-info</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.mediaconversion</key>
 	<true/>
-	<key>com.apple.private.power.notifications-temp</key>
+	<key>com.apple.private.power.notifications</key>
 	<true/>
 	<key>com.apple.private.safari.can-inspect-autofill-feature-availability</key>
 	<true/>

```
### tailspind

> `/usr/libexec/tailspind`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.computesafeguards.managing.allow</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.telemetry</key>
+	<true/>
 	<key>com.apple.cdp.utility</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

```
### triald

> `/usr/libexec/triald`

```diff

 	<true/>
 	<key>com.apple.geoservices.experiments.bucket-id.read</key>
 	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>

```
### triald_system

> `/usr/libexec/triald_system`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.icloud.findmydeviced.localfindable.tvremote</string>
 		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.iohideventsystem</string>
 		<string>com.apple.locationd.registration</string>

 		<string>com.apple.watchlistd.xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>
-		<string>com.apple.icloud.findmydeviced.localfindable.tvremote</string>
-		<string>com.apple.remote-text-editing-legacy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### usermanagerd

> `/usr/libexec/usermanagerd`

```diff

 	<true/>
 	<key>com.apple.private.persona.modify</key>
 	<true/>
+	<key>com.apple.private.routefs-allow</key>
+	<true/>
 	<key>com.apple.private.security.container-manager</key>
 	<true/>
 	<key>com.apple.private.security.datavault.controller</key>

```
### videocodecd

> `/usr/libexec/videocodecd`

```diff

 	<true/>
 	<key>com.apple.private.proreshw</key>
 	<true/>
+	<key>com.apple.private.rtcreportingd</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.lskdd</string>
 		<string>com.apple.lskdd.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.rtcreportingd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### visioncompaniond

> `/usr/libexec/visioncompaniond`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.visionproapp.kvs</string>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>

 		<string>com.apple.apsd</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.installcoordinationd</string>
+		<string>com.apple.kvsd</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.softwareupdateservicesd</string>
 		<string>com.apple.usernotifications.listener</string>

```
### wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 	<string>wifip2pd</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.skywalk.observe-all</key>
+	<true/>
+	<key>com.apple.private.skywalk.observe-stats</key>
+	<true/>
 	<key>com.apple.private.skywalk.register-user-pipe</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/db/os_eligibility/</string>
 		<string>/System/Library/IdentityServices/ServiceDefinitions/com.apple.wifip2pd.InactivityConfig.plist</string>
+		<string>/usr/sbin/wifid</string>
+		<string>/usr/sbin/mDNSResponder</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.coreservices.quarantine-resolver</string>
 		<string>com.apple.networkd_privileged</string>
-		<string>com.apple.private.skywalk.observe-stats</string>
 		<string>com.apple.private.nehelper.privileged</string>
 		<string>com.apple.MobileInternetSharing</string>
 		<string>com.apple.analyticsd</string>

```
### BTMap

> `/usr/sbin/BTMap`

```diff

 	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>

```
### WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

 	<array>
 		<string>/Library/Trial/</string>
 		<string>/System/Library/Trial/NamespaceDescriptors/</string>
-		<string>/System/Library/Trial/NamespaceDescriptors/com.apple.Trial.NamespaceDescriptor.860.plist</string>
-		<string>/System/Library/Trial/NamespaceDescriptors/com.apple.Trial.NamespaceDescriptor.862.plist</string>
-		<string>/System/Library/Trial/NamespaceDescriptors/com.apple.Trial.NamespaceDescriptor.861.plist</string>
-		<string>/System/Library/Trial/NamespaceDescriptors/com.apple.Trial.NamespaceDescriptor.1920.plist</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	</array>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>860</string>
-		<string>861</string>
-		<string>862</string>
-		<string>1920</string>
+		<string>TELEPHONY_WIFI_CELLULAR_HANDOVER_POLICY</string>
 		<string>TELEPHONY_WRM_WIFI_METRICS</string>
+		<string>WIRELESS_DATA_ANALYTICS_CELLULAR_PRODUCT_EXPERIMENTATION_INTERNAL</string>
 	</array>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>

```

### 🆕 bluetoothaudiod

> `/usr/sbin/bluetoothaudiod`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.bluetoothaudiod</string>
	<key>com.apple.BTServer.allowRestrictedServices</key>
	<true/>
	<key>com.apple.BTServer.le.att</key>
	<true/>
	<key>com.apple.accessories.transport.allowauth</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.bluetoothaudiod</string>
	<key>com.apple.bluetooth.custom.properties.writable</key>
	<true/>
	<key>com.apple.bluetooth.pairedInfoSecurity</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.bluetoothaudiod.cb</key>
	<true/>
	<key>com.apple.donotdisturb.service</key>
	<true/>
	<key>com.apple.mediaremote.full-now-playing-read-access</key>
	<true/>
	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
	<array>
		<string>com.apple.BTLEServer.ANCS</string>
	</array>
	<key>com.apple.private.siri.activation</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceBluetoothPeripheral</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>RootDomainUserClient</string>
	</array>
	<key>com.apple.siri.activation</key>
	<true/>
	<key>com.apple.siri.external_request</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>access-calls</string>
		<string>modify-calls</string>
	</array>
</dict>
</plist>

```


### SystemOS

### adattributiond

> `/System/Library/Frameworks/WebKit.framework/Daemons/adattributiond`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
+	<key>com.apple.private.networkserviceproxy</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>com.apple.WebKit.adattributiond</string>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<dict>
+		<key>0</key>
+		<string>com.apple.networkserviceproxy</string>
+	</dict>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```

### 🆕 HybridDatabaseToolUtils

> `/System/Library/PrivateFrameworks/HybridDatabaseToolUtils.framework/HybridDatabaseToolUtils`

- No entitlements *(yet)*


### AppOS

### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 			<string>com.apple.Passwords</string>
 		</array>
 	</dict>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.associated-domains</key>

 	<array>
 		<string>com.apple.Passwords</string>
 	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Passwords.SecurityRecommendations</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

```


