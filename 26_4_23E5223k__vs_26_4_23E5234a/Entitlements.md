## 🔑 Entitlements


### 🆕 MobileDevices-0001

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001`

- No entitlements *(yet)*

### 🆕 MobileDevices-0002

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`

- No entitlements *(yet)*
### GPNonUIExtension

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/GPNonUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>GeneratedImageImageGeneration</key>
-		<dict>
-			<key>Streams</key>
-			<dict>
-				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
-		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>GeneratedImageImageGeneration</key>
-		<dict>
-			<key>Streams</key>
-			<dict>
-				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
-		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```

### 🆕 MeasureSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/MeasureSettingsAppIntentsExtension.appex/MeasureSettingsAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
</dict>
</plist>

```
### PasswordsDataMigration

> `/System/Library/ExtensionKit/Extensions/PasswordsDataMigration.appex/PasswordsDataMigration`

```diff

 	</dict>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.keychain.inet_expansion_fields</key>
+	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
 	<key>com.apple.private.migrationkit.system-dataclass</key>

```
### UnilogTelemetryWorker

> `/System/Library/ExtensionKit/Extensions/UnilogTelemetryWorker.appex/UnilogTelemetryWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.UnilogTelemetryWorker</string>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.unilog.UnilogTelemetryWorker</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>com.apple.aiml.unilog.healthTelemetry</key>

 	</dict>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.system</string>
+	</array>
 </dict>
 </plist>
 

```
### CoreSpotlightService

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService`

```diff

 	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
+	<key>com.apple.private.memory.ownership_transfer</key>
+	<true/>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

```
### PassKitSpotlightIndexExtension

> `/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitSpotlightIndexExtension.appex/PassKitSpotlightIndexExtension`

```diff

 <dict>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.Passbook</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	</dict>
 	<key>com.apple.private.corespotlight.bundleid</key>
 	<string>com.apple.Passbook</string>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.linkd.application-service</string>
+	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>

```

### 🆕 MeasureSettings

> `/System/Library/PreferenceBundles/MeasureSettings.bundle/MeasureSettings`

- No entitlements *(yet)*
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
-		<string>com.apple.MobileAsset.VideoIntelligence</string>
+		<string>com.apple.MobileAsset.Health</string>
 	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VideoIntelligence/</string>
+		<string>/private/var/db/com.apple.countryd/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.account.AppleAccount</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.cloudphotod</string>
 		<string>com.apple.coreduetd.knowledge</string>

 		<string>com.apple.sensitivecontentanalysis.testing</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.account.AppleAccount</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.cloudphotod</string>
 		<string>com.apple.coreduetd.knowledge</string>

 		<string>com.apple.sensitivecontentanalysis.testing</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.Passbook</string>
+	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.applesse.allow</key>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```diff

 	<key>aps-connection-initiate</key>
 	<true/>
 	<key>aps-environment</key>
-	<string>serverPreferred</string>
+	<string>production</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/preferences/com.apple.networkd.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudDocuments</string>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 		<string>com.apple.MobileAsset.Health</string>
 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
 		<string>com.apple.MobileAsset.AudiogramAssets</string>
-		<string>com.apple.MobileAsset.VideoIntelligence</string>
 		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>GeneratedImageImageGeneration</key>
-		<dict>
-			<key>Streams</key>
-			<dict>
-				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
-		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>GeneratedImageImageGeneration</key>
-		<dict>
-			<key>Streams</key>
-			<dict>
-				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
-		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### GenerativePlaygroundMessagesAppExtension

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>GeneratedImageImageGeneration</key>
-		<dict>
-			<key>Streams</key>
-			<dict>
-				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
-		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ContinuityCaptureAgent

> `/usr/libexec/ContinuityCaptureAgent`

```diff

 	<true/>
 	<key>com.apple.mediaremote.remote-control-discovery</key>
 	<true/>
+	<key>com.apple.modelmanager.assertion</key>
+	<true/>
 	<key>com.apple.nearbyinteraction.background</key>
 	<true/>
 	<key>com.apple.private.cmio.extension.configuration</key>

```
### bulletindistributord

> `/usr/libexec/bulletindistributord`

```diff

 		<string>com.apple.private.alloy.bulletindistributor</string>
 		<string>com.apple.private.alloy.bulletindistributor.settings</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/Applications/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Caches/GameKit/Images/GKBulletins/</string>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>com.apple.das.fairscheduling</string>
 		<string>com.apple.dasd.dailyPeriodic</string>
 		<string>com.apple.dasd.issueDetector</string>
-		<string>com.apple.dasd.idlestack</string>
 		<string>com.apple.dasd.swapkills</string>
 		<string>com.apple.dasd.widgetRefreshBudgets</string>
 		<string>com.apple.mt</string>

```
### icloudwebd

> `/usr/libexec/icloudwebd`

```diff

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceFileProviderDomain</string>
+		<string>kTCCServiceUbiquity</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

```
