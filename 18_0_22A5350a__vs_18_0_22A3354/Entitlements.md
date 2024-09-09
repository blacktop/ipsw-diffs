## 🔑 Entitlements

### BarcodeScanner

> `/Applications/BarcodeScanner.app/BarcodeScanner`

```diff

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.ClipServices.clipserviced</string>
 		<string>com.apple.RemoteDisplay</string>
+		<string>com.apple.CameraOverlayAngel.application-service</string>
 	</array>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>

```
### BarcodeScannerCaptureExtension

> `/Applications/BarcodeScanner.app/Extensions/BarcodeScannerCaptureExtension.appex/BarcodeScannerCaptureExtension`

```diff

 	<array>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.appleneuralengine.private</string>
+		<string>com.apple.CameraOverlayAngel.application-service</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 CameraOverlayAngel

> `/Applications/CameraOverlayAngel.app/CameraOverlayAngel`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.backboardd.touchDeliveryObservation</key>
	<true/>
	<key>com.apple.coremedia.cameraviewfinder</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.coremedia.cameraviewfinder</string>
	</array>
	<key>com.apple.springboard.private.capture-button-full-fidelity-events</key>
	<true/>
</dict>
</plist>

```

### 🆕 GroupKitAccountNotification

> `/System/Library/Accounts/Notification/GroupKitAccountNotification.bundle/GroupKitAccountNotification`

- No entitlements *(yet)*

### 🆕 MobileDevices-0001

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001`

- No entitlements *(yet)*

### 🆕 MobileDevices-0003

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003`

- No entitlements *(yet)*

### 🆕 ConditionalEngineAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/ConditionalEngineAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.conditionalengine</string>
	<key>com.apple.CoreRoutine.LocationOfInterest</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.intelligenceflow.orchestrator</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework</string>
	</array>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.intelligenceflow.group-identifier</key>
	<string>com.apple.conditionalengine</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.conditionalengine</string>
	</array>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.userprofiles.read</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.conditionalengine</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siriactionsd.xpc</string>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.intelligenceflow.orchestrator</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.routined.registration</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.conditionalengine</string>
	</array>
	<key>com.apple.shortcuts.stepwise-execution</key>
	<true/>
	<key>com.apple.shortcuts.trigger-editing</key>
	<true/>
	<key>com.apple.shortcuts.variable-injection</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
</dict>
</plist>

```

### 🆕 ConditionalEngineLighthouseExtension

> `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/ConditionalEngineLighthouseExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.conditionalengine.ConditionalEngineLighthouseExtension</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 PasswordManagerAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasswordManagerAppIntentsExtension.appex/PasswordManagerAppIntentsExtension`

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

### 🆕 PasswordSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasswordSettingsAppIntentsExtension.appex/PasswordSettingsAppIntentsExtension`

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

### 🆕 TouchSensitiveButtonHIDService

> `/System/Library/HIDPlugins/ServicePlugins/TouchSensitiveButtonHIDService.plugin/TouchSensitiveButtonHIDService`

- No entitlements *(yet)*

### 🆕 TactSwitchHIDSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/TactSwitchHIDSessionFilter.plugin/TactSwitchHIDSessionFilter`

- No entitlements *(yet)*

### 🆕 UrchinBridgeSettings

> `/System/Library/NanoPreferenceBundles/Applications/UrchinBridgeSettings.bundle/UrchinBridgeSettings`

- No entitlements *(yet)*

### 🆕 NTKAtiumFaceBundleCompanion

> `/System/Library/NanoTimeKit/FaceBundles/NTKAtiumFaceBundleCompanion.bundle/NTKAtiumFaceBundleCompanion`

- No entitlements *(yet)*

### 🆕 NTKDolomiteFaceBundleCompanion

> `/System/Library/NanoTimeKit/FaceBundles/NTKDolomiteFaceBundleCompanion.bundle/NTKDolomiteFaceBundleCompanion`

- No entitlements *(yet)*

### 🆕 NTKSquallFaceBundleCompanion

> `/System/Library/NanoTimeKit/FaceBundles/NTKSquallFaceBundleCompanion.bundle/NTKSquallFaceBundleCompanion`

- No entitlements *(yet)*

### 🆕 BreathingDisturbanceAnalyzerDiagnosticExtension

> `/System/Library/PrivateFrameworks/BreathingAlgorithms.framework/PlugIns/BreathingDisturbanceAnalyzerDiagnosticExtension.appex/BreathingDisturbanceAnalyzerDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.authorization_bypass</key>
	<true/>
	<key>com.apple.private.healthkit.feature-availability.read</key>
	<array>
		<string>SleepApneaNotifications</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<string>/private/var/mobile/Library/Logs/HealthAlgorithms/BreathingAlgorithms/</string>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.BreathingAlgorithms</string>
</dict>
</plist>

```

### 🆕 groupkitd

> `/System/Library/PrivateFrameworks/GroupKit.framework/groupkitd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.groupkitd</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Production</string>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.groupkit.crypto</key>
		<string>com.apple.groupkit.crypto</string>
		<key>com.apple.groupkit.limitedPeersCrypto</key>
		<string>com.apple.groupkit.limitedPeersCrypto</string>
		<key>com.apple.groupkit.limitedPeersMetadata</key>
		<string>com.apple.groupkit.limitedPeersMetadata</string>
		<key>com.apple.groupkit.metadata</key>
		<string>com.apple.groupkit.metadata</string>
	</dict>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.groupkit.allgroups</key>
	<true/>
	<key>com.apple.private.ids.messaging</key>
	<array>
		<string>com.apple.private.alloy.groupkit</string>
		<string>com.apple.private.alloy.groupkit.invite</string>
	</array>
	<key>com.apple.private.ids.messaging.urgent-priority</key>
	<array>
		<string>com.apple.private.alloy.groupkit</string>
		<string>com.apple.private.alloy.groupkit.invite</string>
	</array>
	<key>com.apple.private.ids.registration</key>
	<array>
		<string>com.apple.private.alloy.groupkit</string>
		<string>com.apple.private.alloy.groupkit.invite</string>
	</array>
	<key>com.apple.private.protectedcloudstorage.keysyncing</key>
	<true/>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/HTTPStorages/com.apple.groupkitd/</string>
		<string>/Library/com.apple.groupkitd/</string>
		<string>/Library/Caches/com.apple.groupkitd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.apsd</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.accountsd.accountmanager</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.rtcreportingd</string>
		<string>com.apple.protectedcloudstorage.protectedcloudkeysyncing</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.contactsd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.CloudKit</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.groupkit</string>
		<string>com.apple.groupkitd</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.addressbook</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.groupkitd</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.groupkit.crypto</string>
		<string>com.apple.groupkit.limitedPeersCrypto</string>
		<string>com.apple.groupkit.groupaccesskeys</string>
		<string>com.apple.ProtectedCloudStorage.groupkit.groupaccesskeys</string>
		<string>com.apple.groupkit.highsecuritygroupaccesskeys</string>
		<string>com.apple.ProtectedCloudStorage.groupkit.highsecuritygroupaccesskeys</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

```

### 🆕 SmartStyleV1

> `/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1`

- No entitlements *(yet)*
### aonsensed

> `/usr/libexec/aonsensed`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>aop2.gps-data.ent</key>
+	<true/>
+	<key>aop2.gps-debug</key>
+	<true/>
+	<key>com.apple.afk.shmem-user</key>
+	<true/>
+	<key>com.apple.afk.user</key>
+	<true/>
 	<key>com.apple.aonsensed.xpc</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>cma</key>
+		<dict>
+			<key>historical-memory</key>
+			<dict/>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.private.corewifi-xpc</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AFKSharedMemoryUserClient</string>
+		<string>RootDomainUserClient</string>
+		<string>AFKMemoryDescriptorManagerUserClient</string>
+		<string>AFKEndpointInterfaceUserClient</string>
+		<string>AppleAOPAudioUserClient</string>
+		<string>IOHIDLibUserClient</string>
+		<string>AppleSPUFastpathDriverUserClient</string>
+	</array>
+	<key>staticregion</key>
+	<true/>
+	<key>trusted.trusted-data</key>
+	<true/>
 </dict>
 </plist>
 

```
