## 🔑 Entitlements

### filesystem

### Feedback Assistant iOS

> `/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/AppleInternal/Library/Application Support/com.apple.feedback/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.menubar.allow-scene-override-associated-apps</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>

```
### RemotePaymentPassActionsMessagesExtension

> `/Applications/RemotePaymentPassActionsService.app/PlugIns/RemotePaymentPassActionsMessagesExtension.appex/RemotePaymentPassActionsMessagesExtension`

```diff

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.NanoPassbook.NPKCompanionViewService.connection.server</string>
+		<string>com.apple.familycircle.agent</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.nanopassbook</string>
 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>

```
### CoreServicesUIAgent

> `/System/Library/CoreServices/CoreServicesUIAgent.app/CoreServicesUIAgent`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lsd.open</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 	</array>

 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 </dict>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.iokit.dominoservice</key>
 	<true/>
+	<key>com.apple.private.iokit.powermanagement.read-assertions</key>
+	<true/>
 	<key>com.apple.private.iokit.powersource-control</key>
 	<true/>
 	<key>com.apple.private.iokit.preventSystemSleepSecurityIndicator</key>

```

### 🆕 capturesettingsdiagnostics

> `/System/Library/CoreServices/capturesettingsdiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.settingshost.diagnostics</string>
	</array>
</dict>
</plist>

```
### AppProtectionAppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/AppProtectionAppReplacementExtension.appex/AppProtectionAppReplacementExtension`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.write.access</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```

### 🆕 CallDirectoryAppMigrationExtension

> `/System/Library/ExtensionKit/Extensions/CallDirectoryAppMigrationExtension.appex/CallDirectoryAppMigrationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CallKit.call-directory</key>
	<array>
		<string>application-migration</string>
	</array>
	<key>com.apple.developer.app-migration.data-container-access</key>
	<array>
		<string>com.apple</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CallKit.CallDirectoryMaintenance</string>
	</array>
</dict>
</plist>

```

### 🆕 CallHistoryAppMigrationExtension

> `/System/Library/ExtensionKit/Extensions/CallHistoryAppMigrationExtension.appex/CallHistoryAppMigrationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CallHistory.sync.allow</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.developer.app-migration.data-container-access</key>
	<array>
		<string>com.apple</string>
	</array>
	<key>com.apple.private.CallHistory.read-write</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.security.storage.CallHistory</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/CallHistoryDB/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/CallHistoryDB/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CallHistorySyncHelper</string>
	</array>
</dict>
</plist>

```
### CoreMotionFoundationModelExtension

> `/System/Library/ExtensionKit/Extensions/CoreMotionFoundationModelExtension.appex/CoreMotionFoundationModelExtension`

```diff

 		<!-- Grants access to override assets - deny lists and disabled use case list -->
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
         <string>com.apple.MobileAsset.UAF.CoreMotion.Overrides</string>
-		<!-- grants access to anomaly fm assets -->
-        <string>com.apple.MobileAsset.UAF.MotionAnomalyFM</string>
 	</array>
 
 

 		<!-- Grants access to model assets -->
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/purpose_auto/</string>
-		<!-- Grants access to anomaly fm assets -->
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_MotionAnomalyFM/purpose_auto/</string>
 		<!-- Grants access to override assets - deny lists and disabled use case list -->
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel_Overrides/purpose_auto/</string>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/</string>
 
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_MotionAnomalyFM/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_MotionAnomalyFM/</string>
-
 		<!-- Grants access to override assets - deny lists and disabled use case list -->
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>

```
### CoreServicesAppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/CoreServicesAppReplacementExtension.appex/CoreServicesAppReplacementExtension`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.lsd.modifydb</string>
+	</array>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 </dict>
 </plist>
 

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.priml.crashrecords</string>
+		<string>com.apple.priml.participations</string>
+		<string>com.apple.priml.submissioncooldown</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.spotlight.IndexAgent</string>

```

### 🆕 FileProviderAppMigration

> `/System/Library/ExtensionKit/Extensions/FileProviderAppMigration.appex/FileProviderAppMigration`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```
### MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/MapsIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CoreRoutine.LearnedRoute</key>
+	<true/>
 	<key>com.apple.locationd.dynamic_accuracy_reduction</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 	<array>
 		<string>com.apple.Maps.MapsSync.store</string>
 		<string>com.apple.Maps.MapsSync.service</string>
+		<string>com.apple.routined.registration</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 MotionAnomalyFMExtension

> `/System/Library/ExtensionKit/Extensions/MotionAnomalyFMExtension.appex/MotionAnomalyFMExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>H11ANEInDirectPathClient</string>
		<string>AGXDeviceUserClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.aned.private.ANEAccess.allow</key>
	<true/>
	<key>com.apple.private.security.no-sandbox</key>
	<true/>

	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<!-- Grants access to AnomalyFM model assets -->
        <string>com.apple.MobileAsset.UAF.MotionAnomalyFM</string>
		<!-- Grants access to override assets - deny lists and disabled use case list -->
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>

	<!-- File System -->
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<!-- Grants the sandboxed client process access to create a short term lock on the asset set -->
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

		<!-- Grants the sandboxed client process access to read AnomalyFM assets -->
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_MotionAnomalyFM/purpose_auto/</string>
		<!-- Grants access to override assets - deny lists and disabled use case list -->
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

		<!-- Access to read preinstalled assets -->
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_MotionAnomalyFM/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_MotionAnomalyFM/</string>

		<!-- Grants access to override assets - deny lists and disabled use case list -->
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
	</array>

	<!-- UserDefaults -->
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<!-- Access to UAF UserDefaults -->
		<string>com.apple.UnifiedAssetFramework</string>

		<!-- Access to AJAX override UserDefaults -->
		<string>com.apple.modelcatalog.ajax</string>
	</array>

	<!-- XPC -->
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.modelmanager</string>
		<!-- Grants access to XPC with modelcatalogd -->
		<string>com.apple.modelcatalog.catalog</string>

		<!-- Needed to talk to UAF to do subscribe and unsubscribe -->
		<string>com.apple.siri.uaf.service</string>

		<!-- Grants access to XPC with mobileassetd -->
		<string>com.apple.mobileasset.autoasset</string>

		<!-- Needed for asset roots to work -->
		<string>com.apple.mobileassetd.v2</string>
	</array>
</dict>
</plist>

```

### 🆕 PFLSamplePlugin

> `/System/Library/ExtensionKit/Extensions/PFLSamplePlugin.appex/PFLSamplePlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.pfl.PFLSamplePlugin</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.priml.dev.container</string>
		<string>com.apple.priml.preprod.container</string>
		<string>com.apple.priml.prod.container</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.priml.pfl.plugins</string>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
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
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
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
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.dprivacyd.metadata.allow</key>
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
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.gms.availability</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.priml.crashrecords</string>
		<string>com.apple.priml.participations</string>
		<string>com.apple.priml.submissioncooldown</string>
	</array>
</dict>
</plist>

```

### 🆕 SafariFeatureUploadWorker

> `/System/Library/ExtensionKit/Extensions/SafariFeatureUploadWorker.appex/SafariFeatureUploadWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1821501079</string>
	<key>application-identifier</key>
	<string>com.apple.unilog.SafariFeatureUploadWorker</string>
	<key>com.apple.developer.networking.multipath_extended</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Unilog.SafariFeature.Aggregation</string>
	</array>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.unilog.datacollector.SafariFeatureUploadWorker</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>UnilogSafariFeatureAggregation</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.SafariFeature.Aggregation</key>
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
		<string>com.apple.SafariFeatureUploadWorker</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SafariFeatureUploadWorker</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SafariFeatureUploadWorker</string>
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

### 🆕 SafariFeatureUsageRetentionExtension

> `/System/Library/ExtensionKit/Extensions/SafariFeatureUsageRetentionExtension.appex/SafariFeatureUsageRetentionExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.safari.SafariFeatureUsageRetentionExtension</string>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.safari.SafariFeatureUsageRetentionExtension</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SafariFeatureUsageRetention</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Lighthouse.Ledger.TaskCustomEvent</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Unilog.SafariFeature.Aggregation</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Unilog.SafariFeature.Stage</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>UnilogInstrumentation.IdentifierProvider</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.SafariFeature.LongTermAggregationId</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.aiml.unilog.healthTelemetry</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.HealthTelemetry</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.mlhost.allowedDictionaryGroups</key>
	<array>
		<string>SafariFeatureUsageRetention</string>
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
</dict>
</plist>

```
### SiriLogProcessor

> `/System/Library/ExtensionKit/Extensions/SiriLogProcessor.appex/SiriLogProcessor`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.aiml.siri.OLEOrchestrator</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.analytics.assistant</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.aiml.siri.OLEOrchestrator</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.analytics.assistant</string>
+	</array>
 	<key>com.apple.siri.analytics.assistant</key>
 	<array>
 		<string>runtime.host</string>

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.public</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.ironwood.support</string>
 	</array>

 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.public</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>

```

### 🆕 SpringBoardAppReplacement

> `/System/Library/ExtensionKit/Extensions/SpringBoardAppReplacement.appex/SpringBoardAppReplacement`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.springboard.addApplicationIcon</key>
	<true/>
</dict>
</plist>

```

### 🆕 com.apple.CoreSuggestions.SuggestionsAppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/com.apple.CoreSuggestions.SuggestionsAppReplacementExtension.appex/com.apple.CoreSuggestions.SuggestionsAppReplacementExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.duetexpertd</string>
		<string>com.apple.spotlightui</string>
	</array>
</dict>
</plist>

```
### frauddefensepfl

> `/System/Library/ExtensionKit/Extensions/frauddefensepfl.appex/frauddefensepfl`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.priml.pfl.plugins</string>
+	<key>com.apple.mediaanalysisd.client</key>
+	<true/>
 	<key>com.apple.priml.pfl.Morpheus.allowed</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.imcore.imdpersistence.database-access</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>MLHostTelemetry</key>

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mlhostd.xpc</string>
 		<string>com.apple.cloudd</string>
+		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 PodcastsSnippetsProvider

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/PodcastsSnippetsProvider.bundle/PodcastsSnippetsProvider`

- No entitlements *(yet)*
### ContactViewViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.Archetype.personalContext</string>
 		<string>com.apple.familycircle.agent</string>

```
### ContactsViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.Archetype.personalContext</string>
 		<string>com.apple.familycircle.agent</string>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>333</string>
+		<string>336</string>
 	</array>
 </dict>
 </plist>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	<true/>
 	<key>com.apple.fileprovider.extension-host</key>
 	<true/>
+	<key>com.apple.fileprovider.fpck-service</key>
+	<true/>
 	<key>com.apple.fileprovider.import-cookie</key>
 	<true/>
 	<key>com.apple.fileprovider.resolver</key>

```

### 🆕 RelevanceIntelligence

> `/System/Library/LocationBundles/RelevanceIntelligence.bundle/RelevanceIntelligence`

- No entitlements *(yet)*
### AMSFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/PlugIns/AMSFollowUpExtension.appex/AMSFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.small-offer-button</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Library</string>

```
### callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.facetimemessagestored.service</key>
 	<array>
 		<string>access-facetime-messaging</string>

 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.TextUnderstanding.process</string>
 		<string>com.apple.generativeexperiences.agentSessionStore</string>
+		<string>com.apple.duetactivityscheduler</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.xpc-service-name</key>
 	<array>

```
### accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

 	</array>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.private.accessories.transport-client</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>RegionCode</string>

```
### DraftingExtension-iOS

> `/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-iOS.appex/DraftingExtension-iOS`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/AppleInternal/Library/Application Support/com.apple.feedback/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
-		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/installd/Library/MobileInstallation/</string>
 	</array>

```
### HealthPlansDiagnosticExtension

> `/System/Library/PrivateFrameworks/HealthPlans.framework/PlugIns/HealthPlansDiagnosticExtension.appex/HealthPlansDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.private.health.control</key>
+	<array>
+		<string>arbiter</string>
+	</array>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 com.apple.health.records.assembler

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.assembler.xpc/com.apple.health.records.assembler`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.health.records.assembler</string>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.authorization_bypass</key>
	<true/>
	<key>com.apple.private.healthrecordsd</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.health.records/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.healthrecordsd</string>
		<string>com.apple.healthd.server</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### intelligenceplatformd

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/intelligenceplatformd`

```diff

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>

```
### navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

 	<array>
 		<string>maps.parkedCar</string>
 	</array>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.AppleDepth</string>
+	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>

```
### PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.momentsd/</string>

```
### SeymourMetricsService

> `/System/Library/PrivateFrameworks/SeymourServicesCore.framework/XPCServices/SeymourMetricsService.xpc/SeymourMetricsService`

```diff

 	<string>690470489</string>
 	<key>application-identifier</key>
 	<string>com.apple.Seymour.Metrics.xpc</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.Seymour.Metrics.xpc</string>
 	<key>com.apple.fitcore</key>

 	<array>
 		<string>Library/Caches/com.apple.AppleMediaServices</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.runningboard.jetengine</key>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsBookkeepingService.xpc/SiriSuggestionsBookkeepingService`

```diff

 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.suggestions</string>
+		<string>com.apple.assistant.public</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 	<array>
 		<string>reset</string>
 	</array>
+	<key>com.apple.private.healthkit.data-access-report</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.tccd.sync</string>

```

### 🆕 PodcastsSnippetsUI

> `/System/Library/Snippets/UIPlugins/PodcastsSnippetsUI.bundle/PodcastsSnippetsUI`

- No entitlements *(yet)*
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.safetycheckd</string>

```

### 🆕 MedicalIDFollowUpExtension

> `/private/var/staged_system_apps/Health.app/PlugIns/MedicalIDFollowUpExtension.appex/MedicalIDFollowUpExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.Health</string>
	</dict>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.medicaliddata</key>
	<true/>
	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.corefollowup.agent</string>
		<string>com.apple.healthappd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.private.healthkit.medicaliddata</string>
		<string>com.apple.private.healthkit</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.GeoPolygonDataAssets</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.imagent.EnhancedLinkSecurityStore</string>
+		<string>com.apple.internal.SpotlightAutomationTester</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ASPCarryLog

> `/usr/libexec/ASPCarryLog`

```diff

 		<string>vm.pagesize</string>
 		<string>kern.osrevision</string>
 		<string>hw.memsize</string>
+		<string>vm.compressor.swapper.swapouts_pressure</string>
+		<string>vm.compressor.swapper.swapouts_freezer</string>
+		<string>vm.compressor.swapper.swapouts_donate</string>
+		<string>vm.compressor.swapper.swapouts_scavenger</string>
+		<string>vm.compressor.swapper.swapouts_darkwake</string>
 	</array>
 	<key>com.apple.storage-data</key>
 	<true/>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.accessories.transport-client</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.audio.driver.extrinsic.registration</key>

```
### feedbackd

> `/usr/libexec/feedbackd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/AppleInternal/Library/Application Support/com.apple.feedback/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.audio.AudioSession</string>
 		<string>com.apple.backboard.display.services</string>
+		<string>com.apple.server.bluetooth.le.att.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
+		<string>com.apple.MobileAsset.UAF.MotionAnomalyFM</string>
 		<string>com.apple.MobileAsset.UAF.Music.ConcertsRanking</string>
 		<string>com.apple.MobileAsset.UAF.Photos.SpatialPhotosRelive</string>
 		<string>com.apple.MobileAsset.UAF.Translation.Assets</string>

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_SpatialPhotosRelive/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_Planner/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_MotionAnomalyFM/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Music_ConcertsRanking/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_DialogAssets/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_FindMyConfigurationFiles/</string>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_SpatialPhotosRelive/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IF_Planner/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IF_PlannerOverrides/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_MotionAnomalyFM/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Music_ConcertsRanking/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Siri_DialogAssets/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Siri_FindMyConfigurationFiles/</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	</array>
 	<key>com.apple.private.homekit</key>
 	<true/>
+	<key>com.apple.private.homekit.home-location</key>
+	<true/>
 	<key>com.apple.private.homekit.pairing-identity</key>
 	<true/>
 	<key>com.apple.private.homekit.pairing-identity.private</key>

```
### spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```diff

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>333</string>
+		<string>336</string>
 	</array>
 </dict>
 </plist>

```
### spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```diff

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>333</string>
+		<string>336</string>
 	</array>
 </dict>
 </plist>

```


