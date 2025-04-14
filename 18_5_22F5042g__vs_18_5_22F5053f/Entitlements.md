## 🔑 Entitlements


### 🆕 AMSUIAuthenticationViewService

> `/Applications/AMSUIAuthenticationViewService.app/AMSUIAuthenticationViewService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>605149881</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.appleaccount.custodian</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.cdp.recoverykey</key>
	<true/>
	<key>com.apple.cdp.statemachine</key>
	<true/>
	<key>com.apple.icloud.findmydeviced.access</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled-access</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.CallerName</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<dict>
		<key>Item 0</key>
		<string>UniqueDeviceID</string>
		<key>Item 1</key>
		<string>ProvisioningUniqueDeviceID</string>
		<key>Item 2</key>
		<string>SerialNumber</string>
	</dict>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.adid</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.hsa-authentication-processing</key>
	<true/>
	<key>com.apple.private.managed-settings.effective-read</key>
	<true/>
	<key>com.apple.private.octagon</key>
	<true/>
	<key>com.apple.private.usage-tracking</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.icloud.findmydeviced</string>
		<string>com.apple.aa.daemon.xpc</string>
		<string>com.apple.security.octagon</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.hsa-authentication-server</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.fairplayd.versioned</string>
		<string>com.apple.adid</string>
		<string>com.apple.absd</string>
		<string>com.apple.absinthed</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.aa.custodian.xpc</string>
		<string>com.apple.ak.custodian.xpc</string>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.ak.puffin.xpc</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.icloud.findmydevice.managed</string>
		<string>systemgroup.com.apple.DeviceActivity</string>
	</array>
</dict>
</plist>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.associated-domains</key>
+	<array/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.swc.system-app</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceWillow</string>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<array>
 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.nanolifestyle.connectedgym</string>
+		<string>com.apple.seserviced.designatedkeys</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>Siri.Montara.SharedPreferences</string>
 		<string>SystemSettings.SearchTerms</string>
 		<string>iCloud.Subscription</string>
 		<string>CommunicationSafetyResult</string>

 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.Preferences</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>AppleIntelligenceReportExport</key>
 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>AppleIntelligenceReport.FedStatsTransparencyLog</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>GenerativeExperiences.TransparencyLog</key>
 				<dict>
 					<key>mode</key>

 				<string>Notification.Usage</string>
 			</array>
 		</dict>
+		<key>SiriMontaraSyncedPreferencesBuiltinWrites</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Siri.Montara.SharedPreferences</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Tips</key>
 		<dict>
 			<key>Streams</key>

 	<true/>
 	<key>com.apple.private.safari.offlinereadinglist</key>
 	<true/>
+	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>
+	<true/>
 	<key>com.apple.private.safetycheckd.scsharingreminders</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

 		<string>group.com.apple.contacts.private-access</string>
 		<string>group.tvappservices.container</string>
 		<string>group.com.apple.ScreenContinuityServices</string>
+		<string>group.com.apple.ScreenTime</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.publisher.service</string>
+		<string>com.apple.biome.compute.publisher.service.user</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.matter.support.xpc</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.activitysharingd</string>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
+		<string>IntelligenceFlow.Telemetry</string>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>Sage.Transcript</string>
+		<string>IntelligenceFlow.Transcript.Datastream</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>MLHostTelemetry</key>
+		<key>AssetMetricsWorker</key>
 		<dict>
 			<key>Streams</key>
 			<array>
 				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+				<string>IntelligenceFlow.Telemetry</string>
+				<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+				<string>IntelligenceFlow.Transcript.Datastream</string>
+				<string>Lighthouse.Ledger.LighthousePluginEvent</string>
+				<string>Sage.Transcript</string>
+				<string>Siri.SELFProcessedEvent</string>
+				<string>IntelligenceFlow.Transcript.Datastream</string>
 			</array>
 		</dict>
 	</dict>

 	<array>
 		<string>com.apple.AssetMetricsWorker</string>
 	</array>
+	<key>com.apple.siri.analytics.assistant</key>
+	<array>
+		<string>stream.unifiedMessageStream.readonly</string>
+		<string>stream.rawUnifiedMessageStream.readonly</string>
+	</array>
 </dict>
 </plist>
 

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>Safari.Browsing.Assistant</string>
 		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
 		<string>GenerativeExperiences.PromptTags</string>
+		<string>GenerativeExperiences.WritingToolsFeatures.ComposeAndAdjust</string>
 		<string>AdAttributionKit.AggregatedReporting.Purchase</string>
 		<string>AdAttributionKit.AggregatedReporting.Conversion</string>
 		<string>Siri.ASR.RequestMetricsRecord</string>

```
### FindMyIntentsExtension

> `/System/Library/ExtensionKit/Extensions/FindMyIntentsExtension.appex/FindMyIntentsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.findmy.findmylocate.fenceservice</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
+		<string>com.apple.icloud.searchpartyd.intentsession</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>

 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
+		<string>com.apple.icloud.searchpartyd.intentsession</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>

```
### LighthouseServicesAnalyticsExtension

> `/System/Library/ExtensionKit/Extensions/LighthouseServicesAnalyticsExtension.appex/LighthouseServicesAnalyticsExtension`

```diff

 	<string>com.apple.lighthouse.LighthouseServicesAnalyticsExtension</string>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
-	<key>com.apple.internal.Blackbird.DataAccess</key>
+	<key>com.apple.internal.amp-ds-services-analytics</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.dprivacyd.allow</key>
+	<true/>
+	<key>com.apple.private.dprivacyd.metadata.allow</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.amsondevicestoraged.xpc</string>
+		<string>com.apple.private.dprivacyd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### ODDIMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIMetricsExtension.appex/ODDIMetricsExtension`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.siri.ODDI.MetricsExtension</string>
+	<string>com.apple.siri.ODDIMetricsExtension</string>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.private.assistant.settings</key>
 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
-	<string>com.apple.siri.ODDI.MetricsExtension</string>
+	<string>com.apple.siri.ODDIMetricsExtension</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Siri.SELFProcessedEvent</string>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-only</key>
-	<array>
-		<string>/private/var/db/os_eligibility/eligibility.plist</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Photos/</string>
 		<string>/Library/SMS/</string>
+		<string>/Media/Airlock/Photo/IrisVideo/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	</array>
 	<key>com.apple.spotlight.entitledattributes</key>
 	<true/>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>333</string>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<string>com.apple.coretelephony</string>
 	<key>com.apple.devicecheck.daemon-client</key>
 	<true/>
+	<key>com.apple.devicecheck.private.api</key>
+	<true/>
+	<key>com.apple.devicecheck.serialize</key>
+	<true/>
 	<key>com.apple.driver.AppleBasebandPCI.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleBasebandPCIControl.user-access</key>

```
### Illustrator_Preview

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/Illustrator_Preview.appex/Illustrator_Preview`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.DictionaryServices.dictionary2</string>

```
### com.apple.quicklook.extension.previewUI

> `/System/Library/Frameworks/QuickLook.framework/PlugIns/com.apple.quicklook.extension.previewUI.appex/com.apple.quicklook.extension.previewUI`

```diff

 	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>

```
### AppleCredentialManagerDaemon

> `/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.transportrestrictedmode.configurewhilelocked.allow</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleCredentialManagerUserClient</string>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	</array>
 	<key>com.apple.developer.networking.wifi-info</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.keystore.absinthe</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.companiond.xpc</string>
 		<string>com.apple.locationd.registration</string>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
+	<key>com.apple.developer.icloud-extended-share-access</key>
+	<array>
+		<string>InProcessShareOwnerParticipantInfo</string>
+	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```

### 🆕 MIBULoopbackServerHelper

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/XPCServices/MIBULoopbackServerHelper.xpc/MIBULoopbackServerHelper`

- No entitlements *(yet)*
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>RegionalSafetyAnalysisMetrics</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GuardrailResult</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>
 	<true/>

```
### PhotosStoryDiagnostics

> `/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PlugIns/PhotosStoryDiagnostics.appex/PhotosStoryDiagnostics`

```diff

 	<string>com.apple.PhotosIntelligence.PhotosStoryDiagnostics</string>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
+	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>/Media/PhotoData/internal/storydiagnostics/</string>
+		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 </dict>
 </plist>
 

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

 	</array>
 	<key>com.apple.rootless.storage.remotemanagementd</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.ScreenTime</string>
+	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### STSDiagnostic

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/PlugIns/STSDiagnostic.appex/STSDiagnostic`

```diff

 	<array>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/VoiceServices/</string>
 		<string>/private/var/mobile/Library/Logs/SiriTTSService/</string>
+		<string>/private/var/mobile/Library/Caches/SiriTTS/BNNSModels/</string>
 	</array>
 </dict>
 </plist>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.imagent.av</key>
 	<true/>
+	<key>com.apple.imsharedutilities.forceContactsOOP</key>
+	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>
 	<true/>
 	<key>com.apple.messages.nicknames</key>

```
### SystemActionConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension`

```diff

 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns//SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension</string>
+	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.iBooks.BDSService.private</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.idcredentials.biometrics</key>

 	<true/>
 	<key>com.apple.private.screentime-setup</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
+	</array>
 	<key>com.apple.private.security.storage.Mail</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

 		<string>group.com.apple.iBooks</string>
 		<string>group.com.apple.mail</string>
 		<string>group.com.apple.bridge</string>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService.access</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>

 	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
+	</array>
 	<key>com.apple.private.security.storage.FindMy</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.icloud.fm</string>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute</key>
 	<array>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
 	<true/>
+	<key>com.apple.sage.summarization</key>
+	<true/>
+	<key>com.apple.sage.textcomposition</key>
+	<true/>
 	<key>com.apple.screenshotservices.ssuiservice.showscreenshotui</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>

 		<string>com.apple.sharingd.nsxpc</string>
 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.spotlight.SearchAgent</string>
+		<string>com.apple.sage.summarization</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.tipsd</string>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<array>
 		<string>com.apple.FinanceKit</string>
 		<string>com.apple.AppleMediaServices</string>
+		<string>com.apple.seserviced.designatedkeys</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Reminders

> `/private/var/staged_system_apps/Reminders.app/Reminders`

```diff

 	</array>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.passd.library</string>

```
### csfdiagnose

> `/usr/bin/csfdiagnose`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.csfctl</string>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.secureWriteCloudSubscriptionFeaturesAvailability</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
 	<true/>
 	<key>com.apple.modelcatalog.full-access</key>

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.ap.promotedcontent.supportinterface</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.AdPlatforms</string>
 		<string>com.apple.AppStore</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ak.auth.xpc</string>
+	</array>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>511</string>

```
### appprotectiond

> `/usr/libexec/appprotectiond`

```diff

 	<true/>
 	<key>com.apple.dmd-access</key>
 	<true/>
-	<key>com.apple.dmd.operation.fetch-apps</key>
+	<key>com.apple.dmd.operation.fetch-app-info</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.BackgroundUI</key>
 	<true/>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/dev/exfiltration-audio_capture</string>
+		<string>/dev/exfiltration-adc-audiomxd</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### dprivacyd

> `/usr/libexec/dprivacyd`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.dprivacyd</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Lighthouse.Ledger.DediscoPrivacyEvent</string>

 	</dict>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>dprivacyd</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligenceReport.FedStatsTransparencyLog</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.screentime-communication</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.AppleIntelligenceReport</string>
 		<string>com.apple.DPSubmissionService</string>
 	</array>
 	<key>com.apple.security.system-groups</key>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>
 	<true/>
+	<key>com.apple.private.mobileinboxupdater.loopback-server</key>
+	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>
+		<string>com.apple.MIBULoopbackServerHelper</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<true/>
 	<key>com.apple.private.mobileassetd.use-download-dir</key>
 	<true/>
+	<key>com.apple.private.mobileinboxupdater.xpc</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.inboxupdaterd</string>
+		<string>com.apple.springboard.blockableservices</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>
+		<string>com.apple.springboard.blockableservices</string>
+		<string>com.apple.inboxupdaterd</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 	</array>

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.appattest.spi</key>
 	<true/>
+	<key>com.apple.assessmentmode.fetch-active-restriction-uuids</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 		<string>com.apple.adid</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.ak.auth.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ak.auth.xpc</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.ap.promotedcontentd</string>
 	<key>com.apple.trial.client</key>

```
