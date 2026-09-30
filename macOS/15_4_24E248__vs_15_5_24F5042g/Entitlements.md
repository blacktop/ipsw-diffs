## 🔑 Entitlements

### GenerativePlaygroundAppIntents

> `/System/Applications/Image Playground.app/Contents/Extensions/GenerativePlaygroundAppIntents.appex/Contents/MacOS/GenerativePlaygroundAppIntents`

```diff

 	<array>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+		<string>/Library/UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### Image Playground

> `/System/Applications/Image Playground.app/Contents/MacOS/Image Playground`

```diff

 	<array>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+		<string>/Library/UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### GenerativePlaygroundMessagesAppExtension

> `/System/Applications/Image Playground.app/Contents/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/Contents/MacOS/GenerativePlaygroundMessagesAppExtension`

```diff

 	<array>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+		<string>/Library/UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### Mail

> `/System/Applications/Mail.app/Contents/MacOS/Mail`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
-	<key>com.apple.sage.textcomposition</key>
-	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.webprivacyd</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>
 		<string>com.apple.modelmanager</string>
-		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ProactiveSummarization.server</string>

```

### 🆕 Apple Diagnostics

> `/System/Library/CoreServices/Apple Diagnostics.app/Contents/MacOS/Apple Diagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.DiagnosticsSessionAvailability.client</key>
	<true/>
	<key>com.apple.private.security.no-sandbox</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<false/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.DiagnosticsSessionAvailabilityService.xpc</string>
	</array>
</dict>
</plist>

```
### ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

 	<true/>
 	<key>com.apple.private.crash-reporter</key>
 	<true/>
+	<key>com.apple.private.diagnostic-intelligence</key>
+	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>

```
### SiriNCService

> `/System/Library/CoreServices/Siri.app/Contents/XPCServices/SiriNCService.xpc/Contents/MacOS/SiriNCService`

```diff

 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.appleevents.allowedtosend</key>
 	<dict>
 		<key>com.apple.private.appleevents.allowed.aevt.odoc</key>

 		<string>kTCCServiceReminders</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
+		<string>kTCCServiceSystemPolicyAllFiles</string>
 		<string>kTCCServiceAccessibility</string>
 		<string>kTCCServiceSystemPolicyDesktopFolder</string>
 		<string>kTCCServiceSystemPolicyDocumentsFolder</string>

 	<true/>
 	<key>com.apple.runningboard.assertions.fuseboard</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.shazamd.ui</string>
 		<string>com.apple.siri.encore_xpc_service</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```

### 🆕 diagnosticservicesd

> `/System/Library/CoreServices/diagnosticservicesd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/OSAnalytics/Diagnostics/</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.diagnosticservicesd</string>
	<key>com.apple.trial.client</key>
	<array>
		<string>1731</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### AppleIDSettings

> `/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings`

```diff

 	<true/>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
+	<key>com.apple.private.ndoagent</key>
+	<true/>
 	<key>com.apple.private.networkserviceproxy</key>
 	<true/>
 	<key>com.apple.private.octagon</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ndoagent</string>
 		<string>com.apple.AddressBook.abd</string>
 		<string>com.apple.AddressBook.ContactsAccountsService</string>
 		<string>com.apple.aa.daemon.xpc</string>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/Contents/MacOS/FedStatsMLHostPlugin`

```diff

 		<string>Safari.WebsitesBlockingQuit</string>
 		<string>LocalAuthentication.UI.Dialogs</string>
 		<string>VisualIntelligenceCamera.DetectedLabels</string>
+		<string>RegionalSafetyAnalysis.Eligibility</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>com.apple.photos.geoanalytics.sent</string>
 		<string>com.apple.photos.geoanalytics</string>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
+		<string>RegionalSafetyAnalysis.Disablement</string>
+		<string>RegionalSafetyAnalysis.GuardrailResult</string>
+		<string>GenerativeExperiences.GuardrailResult</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

```
### FedStatsMLHostPluginClassA

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/Contents/MacOS/FedStatsMLHostPluginClassA`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Health.Medications.AddedMed</string>
+		<string>RegionalSafetyAnalysis.Eligibility</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
+		<string>RegionalSafetyAnalysis.KeywordID</string>
+		<string>RegionalSafetyAnalysis.Disablement</string>
+		<string>RegionalSafetyAnalysis.GuardrailResult</string>
+		<string>GenerativeExperiences.GuardrailResult</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

```
### FedStatsMLHostPluginClassB

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/Contents/MacOS/FedStatsMLHostPluginClassB`

```diff

 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>Safari.PageLoad</string>
 		<string>Siri.Health.Federated</string>
+		<string>Device.Wireless.ConnectivityContext</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

```
### GPNonUIExtension

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/Contents/MacOS/GPNonUIExtension`

```diff

 	</array>
 	<key>com.apple.security.device.camera</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 	</array>
 	<key>com.apple.security.device.camera</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework</string>
+	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```

### 🆕 MessageCenterApplicationServiceDiscoveryExtension

> `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/Contents/MacOS/MessageCenterApplicationServiceDiscoveryExtension`

- No entitlements *(yet)*
### ODDIPoirotMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/Contents/MacOS/ODDIPoirotMetricsExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.ODDI.PoirotMetricsWorker</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.ODDI.PoirotMetricsWorker</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 PRIMLCKPreemptivePing

> `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/Contents/MacOS/PRIMLCKPreemptivePing`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PRIMLCKPreemptivePing</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.pfl.container</string>
		<string>com.apple.pfl.preprod.container</string>
		<string>com.apple.fedstats.GM.container</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.priml.pfl.plugins</string>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
	</array>
</dict>
</plist>

```
### PnROnDeviceWorker

> `/System/Library/ExtensionKit/Extensions/PnROnDeviceWorker.appex/Contents/MacOS/PnROnDeviceWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.lighthouse.PnROnDeviceWorker</string>
+	<key>com.apple.diagnosticpipeline.request</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifie</key>
 	<string>com.apple.lighthouse.PnROnDeviceWorker</string>
 	<key>com.apple.private.biome.read-only</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.diagnosticpipeline.service</string>
 	</array>
 </dict>
 </plist>

```
### PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/Contents/MacOS/PrivateEvolutionPlugin`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.priml.pfl.Morpheus.allowed</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### RepackagingWorker

> `/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/Contents/MacOS/RepackagingWorker`

```diff

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

 		<string>publish.unordered</string>
 		<string>plugin.state</string>
 	</array>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 </dict>
 </plist>
 

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/Contents/MacOS/SearchToolExtension`

```diff

 		<string>loiEntityRelevanceRanking</string>
 		<string>standardFeatureView</string>
 	</array>
+	<key>com.apple.private.itunescloud.ICUserStateCenter.siri</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.service.debug</key>

 	<true/>
 	<key>com.apple.private.security.storage.SiriFeatureStore</key>
 	<true/>
+	<key>com.apple.private.security.storage.SiriInference</key>
+	<true/>
+	<key>com.apple.private.security.storage.SiriVocabulary</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.spotlight.parsec</key>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
+		<string>/private/var/mobile/Library/Assistant/SiriVocabulary/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</string>
 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.dmd.policy</string>
+		<string>com.apple.siri.pommes_search_xpc_service</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.managedcorespotlightd</string>
 		<string>com.apple.triald.namespace-management</string>
+		<string>com.apple.siriinferenced</string>
+		<string>com.apple.siriinferenced.remembers</string>
+		<string>com.apple.siriknowledged</string>
+		<string>com.apple.siriknowledged.vocabulary.admin</string>
 		<string>com.apple.diagnosticpipeline.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/Trial/</string>
 		<string>/Library/Containers/com.apple.managedcorespotlightd/EnabledIndexes</string>
 	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>

 		<string>com.apple.contacts.account-caching</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.pommes_search_xpc_service</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.managedcorespotlightd</string>
+		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.diagnosticpipeline.service</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.siri.pommes_search_xpc_service</key>
+	<true/>
+	<key>com.apple.siri.vocabulary.admin</key>
+	<true/>
+	<key>com.apple.siriinferenced</key>
+	<true/>
+	<key>com.apple.siriknowledged</key>
+	<true/>
 	<key>com.apple.spotlight.entitledattributes</key>
 	<true/>
 	<key>com.apple.spotlight.photos.entitledattributes</key>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>SEARCH_TOOL_ANSWER_SYNTHESIS</string>
 		<string>337</string>
 		<string>755</string>
 	</array>

```
### SiriMASPFLCK

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/Contents/MacOS/SiriMASPFLCK`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### SiriMASPFLPush

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/Contents/MacOS/SiriMASPFLPush`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```

### 🆕 ZeoliteEvalExtension

> `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/Contents/MacOS/ZeoliteEvalExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.zeolite.ZeoliteEvalExtension</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.zeolite.ZeoliteEvalExtension</string>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.MLHostTask</string>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.assets.change-daemon-config</key>
	<true/>
	<key>com.apple.private.biome.pruner</key>
	<array>
		<string>Zeolite.Ledger.Embedding</string>
	</array>
	<key>com.apple.private.biome.read</key>
	<array>
		<string>App.Intent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Zeolite.Ledger.Embedding</string>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.dprivacyd.metadata.allow</key>
	<true/>
	<key>com.apple.private.email</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>ZeoliteEvalExtension</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>App.Intent</string>
				<string>GenerativeExperiences.TransparencyLog</string>
				<string>Zeolite.Ledger.Embedding</string>
				<string>Lighthouse.Ledger.TaskCustomEvent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.mlhost.allowedDictionaryGroups</key>
	<array>
		<string>com.apple.zeolite.ZeoliteEvalExtension</string>
	</array>
	<key>com.apple.private.mlhost.dictionaryRead</key>
	<true/>
	<key>com.apple.private.mlhost.dictionaryWrite</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
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
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.generativeexperiences.availabilityService</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.mlhostd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.mlhost</string>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.zeolite</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/System/Library/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.email.maild</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.generativeexperiences.availabilityService</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.mlhostd.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
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
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.coretelephony</string>
 	<key>com.apple.itunesstored.accounts</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistant_service`

```diff

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.assistant.shared</string>
 		<string>group.com.apple.siri.findmy</string>
 		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.notes</string>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.assistant.shared</string>
 		<string>group.com.apple.siri.findmy</string>
 		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.notes</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.CoreSpeech</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Shortcuts/</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<array>
 		<string>HeadGestures</string>

 		<string>1621</string>
 		<string>1701</string>
 		<string>1740</string>
+		<string>1760</string>
 		<string>1890</string>
 		<string>401</string>
 		<string>409</string>

 	</array>
 	<key>com.apple.trial.status.namespace-name.allow</key>
 	<array>
+		<string>INTELLIGENCE_FLOW_PLAN_RESOLUTION</string>
 		<string>MYRIAD_BOOSTS</string>
 		<string>SIRI_AUDIO_APP_SELECTION_HOMEACCESSORY</string>
 		<string>SIRI_AUDIO_APP_SELECTION_HOMEPOD</string>

```
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.AutoAssetNotification</string>
+		<string>com.apple.MobileAsset.MAAutoAsset</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNL</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNLOverrides</string>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.assistant.settings.remora</key>
 	<true/>
+	<key>com.apple.audio.isolated.historicalaudio.client.service</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>

 	<true/>
 	<key>com.apple.private.isolated.audio.coreaudioclient</key>
 	<true/>
+	<key>com.apple.private.isolated.audio.coreaudioclient.historicalaudio</key>
+	<true/>
 	<key>com.apple.private.isolated.audio.coreaudioclient.shareddsp</key>
 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
-	<key>com.apple.private.userprofiles.read</key>
+	<key>com.apple.private.userprofiles.read-write</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.audio.isolated.historicalaudio.client.service</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.perceptiond.entitykit</string>
 		<string>com.apple.coreduetd.people</string>

```
### corespeechd_system

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system`

```diff

 	<true/>
 	<key>com.apple.assistant.settings.remora</key>
 	<true/>
+	<key>com.apple.audio.isolated.historicalaudio.client.service</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>

 	<true/>
 	<key>com.apple.private.isolated.audio.coreaudioclient</key>
 	<true/>
+	<key>com.apple.private.isolated.audio.coreaudioclient.historicalaudio</key>
+	<true/>
 	<key>com.apple.private.isolated.audio.coreaudioclient.shareddsp</key>
 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
-	<key>com.apple.private.userprofiles.read</key>
+	<key>com.apple.private.userprofiles.read-write</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.audio.isolated.historicalaudio.client.service</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.perceptiond.api</string>
 		<string>com.apple.perceptiond.entitykit</string>

```
### FileProviderDiagnosticExtension

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/Contents/MacOS/FileProviderDiagnosticExtension`

```diff

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.fileproviderd</string>
+	</array>
 </dict>
 </plist>
 

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/generativeexperiencesd`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
+		<string>com.apple.MobileAsset.CN.Guardrail</string>
 	</array>
 	<key>com.apple.private.assistant.settings</key>
 	<true/>
 	<key>com.apple.private.biome.read-only</key>
-	<array>
-		<string>GenerativeExperiences.FailureTracking</string>
-	</array>
+	<array/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
+		<string>GenerativeExperiences.FailureTracking</string>
 	</array>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>RegionalSafetyAnalysisMetrics</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>RegionalSafetyAnalysis.Disablement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>RegionalSafetyAnalysis.Eligibility</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>com.apple.GenerativeFunctions.PeriodicTasks.InstrumentationUpload</key>
 		<dict>
 			<key>Streams</key>

 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 </dict>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/Versions/A/intelligencecontextd`

```diff

 	<true/>
 	<key>com.apple.mediaremote.remote-control-discovery</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MorphunData</string>

 		<string>Siri.Orchestration.RequestContext</string>
 		<string>Siri.ContextRefreshTriggers</string>
 	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd`

```diff

 		<string>com.apple.MobileAsset.Trial.Siri.SiriDialogAssets</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlanner</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>

```
### lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/Versions/A/XPCServices/lockdownmoded`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.transportrestrictedmode.configurewhilelocked.allow</key>
+	<true/>
 	<key>com.apple.private.iokit.nvram-write-access</key>
 	<true/>
 	<key>com.apple.private.lockdown.reset-pairing</key>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<integer>1974055701</integer>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.pairing</string>
 		<string>com.apple.MediaRemote.pairing</string>
 		<string>com.apple.airplay</string>
 		<string>apple</string>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Versions/A/Support/mstreamd`

```diff

 	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>

```
### ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.aps-environment</key>
+	<string>production</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

 		<string>Purchase</string>
 		<string>PurchaseHistory</string>
 	</array>
+	<key>com.apple.private.aps-connection-initiate</key>
+	<array>
+		<string>com.apple.aps.applecare</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<true/>
 	<key>com.apple.private.security.bootpolicy</key>
 	<true/>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.NewDeviceOutreach.UserNotificationsBundle</string>
+	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lsd.open</string>
+		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.bluetooth.xpc</string>
+		<string>com.apple.apsd</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<key>com.apple.private.ids.messaging.high-priority</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	</array>
 	<key>com.apple.private.ids.registration</key>
 	<array>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>

 	<key>com.apple.private.ids.self-session</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<key>com.apple.private.ids.session</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<key>com.apple.private.ids.session-private</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

```
### XProtect

> `/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtect`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.rootless.signal-critical-processes</key>
+	<true/>
 	<key>com.apple.private.security.signal-exempt</key>
 	<true/>
 	<key>com.apple.private.xprotect.pluginservice</key>

```

### 🆕 XProtectRemediatorBundlore

> `/System/Library/Templates/Data/Library/Apple/System/Library/CoreServices/XProtect.app/Contents/MacOS/XProtectRemediatorBundlore`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.endpoint-security.submit.xp</key>
	<true/>
	<key>com.apple.private.security.signal-exempt</key>
	<true/>
	<key>com.apple.private.security.syspolicy.provenance</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceSystemPolicyAppBundles</string>
	</array>
	<key>com.apple.private.xprotect.pluginservice</key>
	<true/>
</dict>
</plist>

```
### GPUIExtension

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 	</array>
 	<key>com.apple.security.device.camera</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework</string>
+	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.audiomxd</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.mediaremote.full-now-playing-read-access</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	</array>
 	<key>com.apple.private.audio.hal.aop-audio.user-access</key>
 	<true/>
+	<key>com.apple.private.audio.orchestration.historicalaudiod</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.audio.isolated.historicalaudiod</string>
+	</array>
 </dict>
 </plist>
 

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 		<string>com.apple.cloudd</string>
 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.CompanionUIService.xpc</string>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.homehubd.manage</string>

 		<string>com.apple.CloudKit</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.homed</string>
+		<string>com.apple.nexus</string>
 		<string>com.apple.SocialLayer</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```

### 🆕 diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.aps-connection-initiate</key>
	<array>
		<string>com.apple.aps.diagnostics</string>
	</array>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.DiagnosticsModeAssistant</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.usernotifications.usernotificationservice</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.diagnosticspushd</string>
	</array>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
</dict>
</plist>

```
### findmylocateagent

> `/usr/libexec/findmylocateagent`

```diff

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### historicalaudiod

> `/usr/libexec/historicalaudiod`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.coreaudio.CanRecordPastData</key>
+	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
 	<key>com.apple.private.audio.hal.aop-audio.user-access</key>

 	<true/>
 	<key>com.apple.private.audio.orchestration.registration</key>
 	<true/>
+	<key>com.apple.private.audio.suppress-mic-indicator</key>
+	<true/>
 	<key>com.apple.private.exclaves.conclave-host</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.usesecuresession</key>

 		<string>kern.task_conclave</string>
 		<string>com.apple.audio.orchestrator.registrar.service</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.coreaudio</string>
+	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
 		<string>kern.exclaves_status</string>

```
### logd

> `/usr/libexec/logd`

```diff

 	</array>
 	<key>com.apple.rootless.volume.Preboot</key>
 	<true/>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 </dict>
 </plist>
 

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
### micactivityd

> `/usr/libexec/micactivityd`

```diff

 <dict>
 	<key>com.apple.private.audio.orchestration.registration</key>
 	<true/>
+	<key>com.apple.private.audio.suppress-mic-indicator</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.audio.isolated.client.service</string>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### searchpartyuseragent

> `/usr/libexec/searchpartyuseragent`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
