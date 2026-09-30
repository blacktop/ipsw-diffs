## 🔑 Entitlements

### CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

```diff

 		<string>com.apple.carkit.setupPromptDirector.service</string>
 		<string>com.apple.passd.payment</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.BridgeAssets</string>
+		<string>com.apple.MobileAsset.NanoRegistryPairingCompatibilityIndex</string>
 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>

 		<string>/private/var/hardware/FactoryData/</string>
 		<string>/private/var/preferences/FeatureFlags/Settings.plist</string>
 		<string>/System/Library/Caches/com.apple.factorydata/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_NanoRegistryPairingCompatibilityIndex/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
+	<key>com.apple.springboard.allowIconVisibilityChanges</key>
+	<true/>
 	<key>com.apple.springboard.allowallcallurls</key>
 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>

 	<true/>
 	<key>com.apple.springboard.private.capture-button-events</key>
 	<true/>
+	<key>com.apple.springboard.private.ringer-button-events</key>
+	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

```

### 🆕 Vehicle

> `/Applications/Vehicle.app/Vehicle`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARCapableApp</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.AutoSettings</string>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.CarAssetUtils.variants</key>
	<true/>
	<key>com.apple.private.CarPlayUIServices.punch-through</key>
	<true/>
	<key>com.apple.private.CarPlayUIServices.volume-notification</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>AutomakerNotificationHistory</string>
		<string>AudioSettings</string>
		<string>PositionTracker</string>
		<string>AutomakerSettings</string>
		<string>Vehicle</string>
	</array>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/Applications/AutoSettings.app/AutoSettings</string>
	</dict>
	<key>com.apple.private.carkit</key>
	<true/>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.private.carp.wake</key>
	<true/>
	<key>com.apple.private.externalaccessory.showallaccessories</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.carkit.service</string>
		<string>com.apple.CarPlayApp.volume-notification-service</string>
		<string>com.apple.caraccessoryframework.cardata</string>
		<string>com.apple.CarPlayApp.punch-through-service</string>
		<string>com.apple.CarAssetUtils.variants</string>
	</array>
</dict>
</plist>

```

### 🆕 Common_ISP_EK_TBModule

> `/System/ExclaveKit/System/Library/Frameworks/Common_ISP_EK_TBModule.framework/Common_ISP_EK_TBModule`

- No entitlements *(yet)*

### 🆕 IR_ISP_EK_TBModule

> `/System/ExclaveKit/System/Library/Frameworks/IR_ISP_EK_TBModule.framework/IR_ISP_EK_TBModule`

- No entitlements *(yet)*

### 🆕 RGB_ISP_EK_TBModule

> `/System/ExclaveKit/System/Library/Frameworks/RGB_ISP_EK_TBModule.framework/RGB_ISP_EK_TBModule`

- No entitlements *(yet)*
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 		<string>/private/var/MobileAsset/Assets/com_apple_MobileAsset_VoiceServices_VoiceResources/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_TTSAXResourceModelAssets/</string>
 		<string>/Library/Audio/Tunings/Generic/Haptics/</string>
+		<string>/private/var/containers/Bundle/Application/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

 	<array>
 		<string>com.apple.powerui.bdcdata</string>
 		<string>com.apple.powerexperienced.resourceusage</string>
+		<string>com.apple.datamigrator</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### GMSSELFIngestor

> `/System/Library/ExtensionKit/Extensions/GMSSELFIngestor.appex/GMSSELFIngestor`

```diff

 	</dict>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.siri.GMSSELFIngestor</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```
### PFLNightingaleD

> `/System/Library/ExtensionKit/Extensions/PFLNightingaleD.appex/PFLNightingaleD`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.priml.pfl.plugins</string>
+	<key>com.apple.priml.pfl.Morpheus.allowed</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.biome.writer</key>

```
### com.apple.quicklook.ThumbnailsAgent

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
-	<key>com.apple.private.extensionkit.host.unsandboxed-extensions-for-extension-points</key>
-	<array>
-		<string>com.apple.quicklook.thumbnail.secure</string>
-	</array>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
 	<key>com.apple.private.vfs.open-by-id</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 		<string>com.apple.remoted</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.securityd.systemkeychain</string>
 		<string>com.apple.server.bluetooth</string>
 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.shazamd.ui</string>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 		<string>kern.exclaves_status</string>
 		<string>kern.task_conclave</string>
 	</array>
-	<key>com.apple.security.get-task-allow</key>
-	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.server.bluetooth</string>

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
### com.apple.mobilesafari.SafariDiagnosticExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension`

```diff

 	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.safari</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/CrashReporter/</string>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.private.aop-voicetrigger.user-access</key>
 	<true/>
+	<key>com.apple.private.applesmc.user-access</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>

 		<string>IOPAudioClientManagerDeviceUserClient</string>
 		<string>AppleHapticsSupportUserClient</string>
 		<string>AHSPowerInterfaceUserClient</string>
+		<string>AppleSMCClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```diff

 <dict>
 	<key>aps-connection-initiate</key>
 	<true/>
-	<key>com.apple.TapToRadarKit.service-access</key>
-	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 	<array>
 		<string>com.apple.diagnosticspushd</string>
 	</array>
-	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.TapToRadarKit.service</string>
-	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 </dict>

```
### hangreporter

> `/usr/libexec/hangreporter`

```diff

 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.service-stats</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>IOReportUserClient</string>

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.tailspin.symbolication</key>
 	<true/>
 	<key>com.apple.trial.status.deployment-environment.allow</key>

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
### remoted

> `/usr/libexec/remoted`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/com.apple.remoted</string>
+		<string>/dev/console</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### spindump_fileparser

> `/usr/libexec/spindump_fileparser`

```diff

 	<true/>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>
 		<integer>0</integer>

```
### triald

> `/usr/libexec/triald`

```diff

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.allowed-manage-trial-factors</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 	</array>
 	<key>com.apple.remotemanagementd.management-state</key>
 	<true/>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.safari</string>
-	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/installd/Library/MobileInstallation/MigrationInfo.plist</string>

```
### wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/log/com.apple.wifi.analytics/</string>
+		<string>/private/var/log/com.apple.wifi.analytics/ch.out</string>
+		<string>/private/var/log/com.apple.wifi.analytics/usage.out</string>
+		<string>/private/var/log/com.apple.wifi.analytics/unavail.out</string>
+		<string>/private/var/root/Library/com.apple.wifianalyticsd/</string>
+		<string>/private/var/root/Library/com.apple.wifianalyticsd/.wa/</string>
+		<string>/private/var/root/Library/com.apple.wifianalyticsd/.wa/t.out</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### spindump

> `/usr/sbin/spindump`

```diff

 	<true/>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>IOReportUserClient</string>

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.system-task-ports.read</key>
 	<true/>
 	<key>com.apple.tailspin.dump-output</key>

```
