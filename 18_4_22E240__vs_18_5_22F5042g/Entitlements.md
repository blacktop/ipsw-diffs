## 🔑 Entitlements

### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.Accessibility</string>
 		<string>com.apple.Diagnostics</string>
 		<string>com.apple.Sharing</string>
 		<string>com.apple.enhanced-logging-state</string>
 		<string>com.apple.sharingd</string>
+		<string>com.apple.CosmeticAssessment</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>lockdown-identities</string>
+		<string>com.apple.CosmeticAssessment-Diagnostics</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

```diff

 	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.private.exclaves.kernel-domain</key>
+	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleH13CamInUserClient</string>

 	<array>
 		<string>com.apple.Accessibility</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

```diff

 	<true/>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
+	<key>com.apple.private.exclaves.kernel-domain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 </dict>
 </plist>
 

```
### Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```diff

 	<true/>
 	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
 	<true/>
+	<key>com.apple.private.exclaves.kernel-domain</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.avfaudio.devicetest.service</string>
 		<string>com.apple.audioanalyticsd</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleSMCClient</string>

```
### Diagnostic-8079

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079`

```diff

 	<true/>
 	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
 	<true/>
+	<key>com.apple.private.exclaves.kernel-domain</key>
+	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>

 		<string>com.apple.Accessibility</string>
 		<string>com.apple.HearingAids</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.DiagnosticsKit</string>

```
### Diagnostic-8246

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246`

```diff

 <dict>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
+	<key>com.apple.private.exclaves.kernel-domain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 </dict>
 </plist>
 

```
### Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

 	<true/>
 	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
 	<true/>
+	<key>com.apple.private.exclaves.kernel-domain</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<array>
 		<string>com.apple.avfaudio.devicetest.service</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleSMCClient</string>

```
### SystemReport-AirPods

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### SystemReport-BatteryCase

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport-BatteryCase.appex/SystemReport-BatteryCase`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>

```
### SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

 	<array>
 		<string>com.apple.Diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>sysctl.proc_translated</string>
+	</array>
 	<key>com.apple.seld.cm</key>
 	<true/>
 	<key>com.apple.seld.tsmmanager</key>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
+	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
+	<key>com.apple.springboard.private.capture-button-events</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.stereoleader.soundboard</key>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.private.parsec.default-client</key>
 	<string>com.apple.siri</string>
+	<key>com.apple.private.photos.service.internal.cloud</key>
+	<true/>
 	<key>com.apple.private.remindd</key>
 	<dict>
 		<key>userInteractive</key>

```
### TVSetupUIService

> `/Applications/TVSetupUIService.app/TVSetupUIService`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.sharing.Client</key>
+	<true/>
 	<key>com.apple.sharing.Services</key>
 	<true/>
 	<key>com.apple.sharing.Session</key>
 	<true/>
+	<key>com.apple.springboard.capture-button-restriction</key>
+	<true/>
+	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.private.capture-button-events</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.wifi.eap-nearby-device-setup-config-copy</key>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/usr/libexec</string>
+		<string>/Applications/</string>
 		<string>/Library/Ringtones/</string>
 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/MobileAsset/Assets/com_apple_MobileAsset_VoiceServices_VoiceResources/</string>

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
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.orchestration.capabilities</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.searchd</string>
 		<string>com.apple.gamepolicyd.tool.privileged</string>

 	<true/>
 	<key>com.apple.siri.external_request</key>
 	<true/>
+	<key>com.apple.siri.orchestration.capabilities</key>
+	<true/>
 	<key>com.apple.sos.trigger</key>
 	<true/>
 	<key>com.apple.soundscapes.picker</key>

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
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.FedStats.MLHostPlugin</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.FedStats.MLHostPlugin</string>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

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

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.FedStats.MLHostPluginClassA</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.FedStats.MLHostPluginClassA</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

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

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/FedStatsMLHostPluginClassB`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.FedStats.MLHostPluginClassB</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.FedStats.MLHostPluginClassB</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

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

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/GPNonUIExtension`

```diff

 	<array>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+		<string>/Library/UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 	<array>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+		<string>/Library/UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 LighthouseAVShadowEval

> `/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/LighthouseAVShadowEval`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.LighthouseAV.LighthouseAVShadowEval</string>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.MLHostTask</string>
	</array>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.coreaudio</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Device.Audio.AdaptiveVolume</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>LighthouseAVShadowEval</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Device.Audio.AdaptiveVolume</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_MLHostTask/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Documents/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.mobileasset.autoasset</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mobileasset.autoasset</string>
	</array>
</dict>
</plist>

```

### 🆕 MessageCenterApplicationServiceDiscoveryExtension

> `/System/Library/ExtensionKit/Extensions/MessageCenterApplicationServiceDiscoveryExtension.appex/MessageCenterApplicationServiceDiscoveryExtension`

- No entitlements *(yet)*

### 🆕 NeighborhoodActivityConduitIntentsExtension

> `/System/Library/ExtensionKit/Extensions/NeighborhoodActivityConduitIntentsExtension.appex/NeighborhoodActivityConduitIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.NeighborhoodActivityConduitService.NeighborhoodActivityConduitIntentsExtension</string>
	<key>com.apple.NeighborhoodActivityConduitService</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/NeighborhoodActivityConduitIntents.framework</string>
	</array>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.calls.NeighborhoodActivityConduitIntents</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.NeighborhoodActivityConduitService</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### ODDIPoirotMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/ODDIPoirotMetricsExtension`

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
### PFLHRPeriodPredCK

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK`

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
### PFLHRPeriodPredPush

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush`

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
### PFLNightingaleD

> `/System/Library/ExtensionKit/Extensions/PFLNightingaleD.appex/PFLNightingaleD`

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

### 🆕 PRIMLCKPreemptivePing

> `/System/Library/ExtensionKit/Extensions/PRIMLCKPreemptivePing.appex/PRIMLCKPreemptivePing`

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

> `/System/Library/ExtensionKit/Extensions/PnROnDeviceWorker.appex/PnROnDeviceWorker`

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

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`

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

> `/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker`

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

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`

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

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/SiriMASPFLCK`

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

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/SiriMASPFLPush`

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

> `/System/Library/ExtensionKit/Extensions/ZeoliteEvalExtension.appex/ZeoliteEvalExtension`

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
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MorphunData</string>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>Siri.PrivateLearning.MediaEntity</key>
+				<key>Siri.PrivateLearning.Media</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.assistant.shared</string>
 		<string>group.com.apple.siri.findmy</string>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.stocks</string>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.assistant.shared</string>
 		<string>group.com.apple.siri.findmy</string>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.stocks</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.rapport.siri</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

 		<string>/Library/Logs/CrashReporter/ssr/</string>
 		<string>/Library/Logs/CrashReporter/VoiceTrigger/</string>
 		<string>/Library/PeopleSuggester/</string>
+		<string>/Library/Shortcuts/</string>
 		<string>/Library/Trial/Treatments/SIRI_TEXT_TO_SPEECH/</string>
 		<string>/Library/Trial/Treatments/SIRI_UNDERSTANDING_NL_OVERRIDES/</string>
 		<string>/Library/Voicemail/</string>

 		<string>1720</string>
 		<string>1721</string>
 		<string>1740</string>
+		<string>1760</string>
 		<string>1890</string>
 		<string>200</string>
 		<string>322</string>

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
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

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
### eyereliefd

> `/System/Library/PrivateFrameworks/EyeRelief.framework/Resources/eyereliefd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	<array>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.AttentionAwareness</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FedStatsMLRPlugin

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/FedStatsMLRPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStats.Plugin</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.PriML.FedStats.Plugin</string>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### FedStatsMLRPluginClassB

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/FedStatsMLRPluginClassB`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStats.PluginClassB</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.PriML.FedStats.PluginClassB</string>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### FedStatsMLRPluginNonDnU

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/FedStatsMLRPluginNonDnU`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStatsPlugin.NonDnU</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.PriML.FedStatsPlugin.NonDnU</string>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

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

 		<string>/private/var/mobile/Library/UnifiedAssetFramework/</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_Guardrail/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

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

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.naturallanguaged</string>
 		<string>com.apple.dmd.policy</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.CalendarAgent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.siri.morphun</string>
 		<string>com.apple.assistant</string>
 		<string>com.apple.mediaremote</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 		<string>com.apple.MobileAsset.Trial.Siri.SiriDialogAssets</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlanner</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>

 		<string>com.apple.siri.vocabularyupdates</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.speech.localspeechrecognition</string>
+		<string>com.apple.spotlight.SearchAgent</string>
 		<string>com.apple.translationd</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.proactive.sports.xpc</string>

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.transportrestrictedmode.configurewhilelocked.allow</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.lockdownmode</string>

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

> `/System/Library/PrivateFrameworks/MediaStream.framework/Support/mstreamd`

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
### nanosystemsettingsd

> `/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd`

```diff

 		<string>/Library/DeviceRegistry/</string>
 		<string>/Library/IdentityServices/incomingfiles/</string>
 		<string>/tmp/BridgeDiagnosticLogs/</string>
+		<string>/tmp/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.incoming-call-filter-server</string>
+		<string>com.apple.lsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 NeighborhoodActivityConduitIntents

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduitIntents.framework/NeighborhoodActivityConduitIntents`

- No entitlements *(yet)*
### NewDeviceOutreachExtension

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension`

```diff

 	<string>166430402</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.Diagnostics.host-view-service</key>
+	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

```
### ndoagent

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

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

 	<true/>
 	<key>com.apple.private.followup</key>
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
 	<key>com.apple.security.system-group-containers</key>
 	<array>
 		<string>systemgroup.com.apple.mobileactivationd</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>511712240</string>
 	<key>keychain-access-groups</key>

```
### SpotlightDiagnostic

> `/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic`

```diff

 		<string>/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Search/</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/com.apple.corespotlight.asl</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.ReportMemoryException</string>
+	</array>
 </dict>
 </plist>
 

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

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

```
### vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

 	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
-	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<key>com.apple.developer.hardened-process</key>
 	<true/>
 	<key>com.apple.imagent.av</key>
 	<true/>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 		<string>/private/var/mobile/Media/Purchases/</string>
 		<string>/private/var/mobile/Media/iTunes_Control/</string>
 		<string>/private/var/mobile/Media/ManagedPurchases/TVApp/</string>
+		<string>/private/var/mobile/Media/Music/Downloads/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```diff

 	<string>511712240</string>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>previous-application-identifiers</key>
+	<array>
+		<string>XLS5V72N46.com.apple.visionproapp</string>
+	</array>
 </dict>
 </plist>
 

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.icloud.searchpartyd.serverDrivenStrings</string>
 		<string>com.apple.searchparty.btfindingsession</string>
 		<string>com.apple.accessories.connection-info-server</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

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

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

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

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```diff

 	<array>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+		<string>/Library/UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
-	<key>com.apple.sage.textcomposition</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.PreviewLegacySignaturesConversion</string>

 		<string>com.apple.synapse.DocumentWorkflowsService</string>
 		<string>com.apple.siri.encore_xpc_service</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>
-		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.proactive.PersonalizationPortrait.Contact</string>
 		<string>com.apple.icloudmailagent.secret.xpc</string>
 		<string>com.apple.backboard.hid.services</string>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>SBStarkCapable</key>
 	<true/>
+	<key>abs-client</key>
+	<string>1192613791</string>
 	<key>adi-client</key>
 	<string>409835401</string>
 	<key>application-identifier</key>

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
 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.SocialLayer</string>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.private.iokit.system-nvram-internal-allow</key>
 	<true/>
+	<key>com.apple.private.ndoagent</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

```
### findmylocated

> `/usr/libexec/findmylocated`

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
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<true/>
 	<key>com.apple.frontboard.shutdown</key>
 	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.nfcd.hce</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleKeyStoreUserClient</string>
 		<string>AppleMobileApNonceUserClient</string>
 		<string>AppleSMCClient</string>
 		<string>RootDomainUserClient</string>

```
### lockdownd

> `/usr/libexec/lockdownd`

```diff

 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>IceFallID</string>
+		<string>IcefallInfo</string>
 		<string>UniqueDeviceID</string>
 		<string>InverseDeviceID</string>
 		<string>ProximitySensorCalibration</string>

```
### logd

> `/usr/libexec/logd`

```diff

 	<true/>
 	<key>com.apple.private.xpc.launchd.ios-system-session</key>
 	<true/>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>logd</string>

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
### remoteappintentsd

> `/usr/libexec/remoteappintentsd`

```diff

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.linkd.observationStatusRegistry</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

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
### visioncompaniond

> `/usr/libexec/visioncompaniond`

```diff

 	<array>
 		<string>com.apple.appstored.xpc.request</string>
 		<string>com.apple.apsd</string>
+		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.softwareupdateservicesd</string>

```
