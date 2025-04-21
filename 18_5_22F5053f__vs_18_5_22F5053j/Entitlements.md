## 🔑 Entitlements

### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.VoiceOverTouch</string>
 		<string>com.apple.Accessibility</string>
 		<string>com.apple.Diagnostics</string>
 		<string>com.apple.Sharing</string>

```
### Family

> `/Applications/Family.app/Family`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.screentime-ask</key>

```
### MailCompositionService

> `/Applications/MailCompositionService.app/MailCompositionService`

```diff

 	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
+	</array>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
 	<key>com.apple.private.security.storage.DiagnosticReports.read-only</key>

 		<string>group.tvappservices.container</string>
 		<string>group.com.apple.ScreenContinuityServices</string>
 		<string>group.com.apple.ScreenTime</string>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

```

### 🆕 TVAppServicesAccountNotificationPlugin

> `/System/Library/Accounts/Notification/TVAppServicesAccountNotificationPlugin.bundle/TVAppServicesAccountNotificationPlugin`

- No entitlements *(yet)*
### FedStatsMLHostPluginClassA

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/FedStatsMLHostPluginClassA`

```diff

 		<string>RegionalSafetyAnalysis.Disablement</string>
 		<string>RegionalSafetyAnalysis.GuardrailResult</string>
 		<string>GenerativeExperiences.GuardrailResult</string>
+		<string>GenerativeExperiences.GeneratedImageFeatures.FailureReason</string>
 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>

```
### com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

 	<true/>
 	<key>com.apple.developer.gpu-restricted</key>
 	<true/>
+	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
+	<true/>
 	<key>com.apple.developer.web-browser-engine.rendering</key>
 	<true/>
 	<key>com.apple.mediaremote.external-artwork-validation</key>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<array>
 		<string>RequestBrickState</string>
 	</array>
+	<key>com.apple.private.MobileContainerManager.allowed</key>
+	<true/>
 	<key>com.apple.private.SecureNetworking.ipsec_db</key>
 	<true/>
 	<key>com.apple.private.SecureNetworking.ipsec_ike</key>

```
### KerberosExtension

> `/System/Library/PrivateFrameworks/AppSSOKerberos.framework/PlugIns/KerberosExtension.appex/KerberosExtension`

```diff

 	<array>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.identities</string>

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### PhotosSearchDiagnostics

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosSearchDiagnostics.appex/PhotosSearchDiagnostics`

```diff

 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
+	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
+	<true/>
 	<key>com.apple.private.photos.service.debug</key>
 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>

```
### demod

> `/usr/libexec/demod`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.FailureTracking</key>
+	<true/>
+	<key>com.apple.generativeexperiences.FailureTracking.clearFailureTracking</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mobile.keybagd.pc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceIdentityXPCService.access</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
+	<true/>
+	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfigurationXPCService.access</key>
+	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceUserNotificationsXPCService.access</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
+	</array>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>kTCCServiceAccessibility</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.nanoprefsync</string>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 		<string>Discoverability.Signals</string>
 		<string>UserFocusComputedMode</string>
 	</array>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>Discoverability.Signals</string>

 		<string>com.apple.aa.custodian.xpc</string>
 		<string>com.apple.aa.inheritance.xpc</string>
 		<string>com.apple.appconduitd.device-connection</string>
+		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.enroll.state</string>

```
