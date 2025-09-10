## 🔑 Entitlements


### 🆕 MobileDevices-0001

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001`

- No entitlements *(yet)*

### 🆕 MobileDevices-0003

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003`

- No entitlements *(yet)*

### 🆕 AppleCentauriAlpha

> `/System/Library/DriverExtensions/AppleCentauriAlpha.dext/AppleCentauriAlpha`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.driverkit</key>
	<true/>
	<key>com.apple.developer.driverkit.transport.pci</key>
	<true/>
	<key>com.apple.driver.centauri.publish</key>
	<true/>
	<key>com.apple.private.corecaptureclient.driverkit</key>
	<true/>
	<key>com.apple.private.custom-coredump-location</key>
	<string>AppleCentauriAlpha-dextcrash-%P.%T.core</string>
	<key>com.apple.private.driverkit.driver-launch-configuration</key>
	<true/>
	<key>com.apple.private.enable-coredump-on-panic</key>
	<string>cent-alpha</string>
	<key>com.apple.private.wifi.driverkit</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 AppleCentauriBeta

> `/System/Library/DriverExtensions/AppleCentauriBeta.dext/AppleCentauriBeta`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.driverkit</key>
	<true/>
	<key>com.apple.developer.driverkit.transport.pci</key>
	<true/>
	<key>com.apple.driver.centauri.publish</key>
	<true/>
	<key>com.apple.private.corecaptureclient.driverkit</key>
	<true/>
	<key>com.apple.private.custom-coredump-location</key>
	<string>AppleCentauriBeta-dextcrash-%P.%T.core</string>
	<key>com.apple.private.driverkit.driver-launch-configuration</key>
	<true/>
	<key>com.apple.private.enable-coredump-on-panic</key>
	<string>cent-beta</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 AppleCentauriControl

> `/System/Library/DriverExtensions/AppleCentauriControl.dext/AppleCentauriControl`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.driverkit</key>
	<true/>
	<key>com.apple.developer.driverkit.transport.pci</key>
	<true/>
	<key>com.apple.private.coprocessor-logging</key>
	<true/>
	<key>com.apple.private.corecaptureclient.driverkit</key>
	<true/>
	<key>com.apple.private.custom-coredump-location</key>
	<string>AppleCentauriControl-dextcrash-%P.%T.core</string>
	<key>com.apple.private.driverkit.allows-publish</key>
	<true/>
	<key>com.apple.private.driverkit.driver-launch-configuration</key>
	<true/>
	<key>com.apple.private.enable-coredump-on-panic</key>
	<string>cent-ctrl</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 com.apple.HealthKit.HealthHTNCustomerDiagnosticExtension

> `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthHTNCustomerDiagnosticExtension.appex/com.apple.HealthKit.HealthHTNCustomerDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.authorization_bypass</key>
	<true/>
</dict>
</plist>

```

### 🆕 NTKExactitudesFaceBundle

> `/System/Library/NanoTimeKit/FaceBundles/NTKExactitudesFaceBundle.bundle/NTKExactitudesFaceBundle`

- No entitlements *(yet)*

### 🆕 NTKWarlockFaceBundle

> `/System/Library/NanoTimeKit/FaceBundles/NTKWarlockFaceBundle.bundle/NTKWarlockFaceBundle`

- No entitlements *(yet)*

### 🆕 warlock.metallib

> `/System/Library/NanoTimeKit/FaceBundles/NTKWarlockFaceBundle.bundle/warlock.metallib`

- No entitlements *(yet)*
### abm-helper

> `/System/Library/PrivateFrameworks/ABMHelper.framework/Support/abm-helper`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
+	<key>com.apple.driver.AirshipDaleBasebandControlInterface.user-access</key>
+	<true/>
+	<key>com.apple.driver.AirshipDaleBasebandTrace.user-access</key>
+	<true/>
 	<key>com.apple.driver.AppleBasebandPCI.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleBasebandPCIControl.user-access</key>

 		<string>IOAppleConvergedIPCBBUserClient</string>
 		<string>IOAppleConvergedIPCTraceBackendRaw</string>
 		<string>IOAppleConvergedIPCTraceUserClient</string>
+		<string>AirshipDaleBasebandControlInterfaceUserClient</string>
+		<string>AirshipDaleBasebandControlUserClient</string>
+		<string>AirshipDaleBasebandTraceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### AppleDeviceQueryService

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`

```diff

 	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>
-	<array/>
+	<array>
+		<string>com.apple.driver.AppleCentauriControl</string>
+	</array>
+	<key>com.apple.driver.AirshipDaleBasebandControlInterface.user-access</key>
+	<true/>
 	<key>com.apple.driver.AppleBasebandPCI.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleBasebandPCIControl.user-access</key>

```
### threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

 	<true/>
 	<key>com.apple.developer.driverkit.communicates-with-drivers</key>
 	<true/>
+	<key>com.apple.developer.driverkit.userclient-access</key>
+	<array>
+		<string>com.apple.driver.AppleCentauriBeta</string>
+		<string>com.apple.driver.AppleCentauriControl</string>
+		<string>com.apple.driver.AppleCentauriAlpha</string>
+	</array>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
 	<key>com.apple.iokit.powerdxpc</key>

```

### 🆕 ConnectivityDE

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ConnectivityDE.appex/ConnectivityDE`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.centaurid.xpc</key>
	<true/>
	<key>com.apple.private.osanalytics.defaults.allow</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/dextcores/</string>
		<string>/private/var/mobile/Library/Logs/CrashReporter/CoreCapture/</string>
		<string>/private/var/logs/CrashReporter/CoreCapture/BT/</string>
		<string>/private/var/logs/CrashReporter/CoreCapture/WiFi/</string>
		<string>/private/var/logs/CrashReporter/CoreCapture/MultiFunctionManager/</string>
		<string>/private/var/logs/CoreCapture/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/ConnectivityDE/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.centaurid.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/dextcores/</string>
		<string>/Library/Logs/CrashReporter/CoreCapture/BT/</string>
		<string>/Library/Logs/CrashReporter/CoreCapture/WiFi/</string>
		<string>/Library/Logs/CrashReporter/CoreCapture/MultiFunctionManager/</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/ConnectivityDE/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.centaurid.xpc</string>
	</array>
</dict>
</plist>

```

### 🆕 ConnectivityWiFiDE

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ConnectivityWiFiDE.appex/ConnectivityWiFiDE`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.centaurid.xpc</key>
	<true/>
	<key>com.apple.private.osanalytics.defaults.allow</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/Logs/CrashReporter/CoreCapture/WiFi/</string>
		<string>/private/var/mobile/Library/Logs/CrashReporter/CoreCapture/MultiFunctionManager/</string>
		<string>/private/var/logs/CrashReporter/CoreCapture/WiFi/</string>
		<string>/private/var/logs/CrashReporter/CoreCapture/MultiFunctionManager/</string>
		<string>/private/var/logs/CoreCapture/WiFi/</string>
		<string>/private/var/logs/CoreCapture/MultiFunctionManager/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/ConnectivityWiFiDE/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.centaurid.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Logs/CrashReporter/CoreCapture/WiFi/</string>
		<string>/Library/Logs/CrashReporter/CoreCapture/MultiFunctionManager/</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/ConnectivityWiFiDE/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.centaurid.xpc</string>
	</array>
</dict>
</plist>

```
### healthappworkd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/XPCServices/healthappworkd.xpc/healthappworkd`

```diff

 		<string>com.apple.brook</string>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.private.health.cardio-fitness</string>
+		<string>com.apple.private.health.hypertension-notifications</string>
 		<string>com.apple.private.health.walking-steadiness</string>
 		<string>com.apple.private.health.feature-availability-requirement-overrides</string>
 		<string>com.apple.private.health.medications</string>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 		<string>com.apple.brook</string>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.private.health.cardio-fitness</string>
+		<string>com.apple.private.health.hypertension-notifications</string>
 		<string>com.apple.private.health.walking-steadiness</string>
 		<string>com.apple.private.health.feature-availability-requirement-overrides</string>
 		<string>com.apple.private.health.medications</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array>
+		<string>com.apple.facetime</string>
+	</array>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudDocuments</string>
+	</array>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<string>com.apple.facetime</string>
 		<string>com.apple.Photos</string>
 	</array>
+	<key>com.apple.developer.ubiquity-container-identifiers</key>
+	<array>
+		<string>com.apple.facetime</string>
+	</array>
 	<key>com.apple.duet.expertcenter.consumer</key>
 	<true/>
 	<key>com.apple.facetimemessagestored.service</key>

 	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
+	<key>com.apple.private.clouddocs.auto-accept-share</key>
+	<true/>
+	<key>com.apple.private.clouddocs.sharing.private-interface</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

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

 	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>
 	<true/>
+	<key>com.apple.private.librarian.container-proxy</key>
+	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/ActivationState</string>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileDocuments</key>
+	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

```

### 🆕 RTSCV1

> `/System/Library/VideoProcessors/RTSCV1.bundle/RTSCV1`

- No entitlements *(yet)*
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 		<string>com.apple.brook</string>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.private.health.cardio-fitness</string>
+		<string>com.apple.private.health.hypertension-notifications</string>
 		<string>com.apple.private.health.walking-steadiness</string>
 		<string>com.apple.private.health.feature-availability-requirement-overrides</string>
 		<string>com.apple.Accessibility</string>

 		<string>com.apple.ConnectedAudio</string>
 		<string>com.apple.private.health.mental-health</string>
 		<string>com.apple.private.HearingTestFramework</string>
+		<string>com.apple.private.health.blood-pressure-best-practices</string>
 		<string>com.apple.private.health.health-actions</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>com.apple.private.alloy.nameandphoto</string>
 		<string>com.apple.madrid</string>
 		<string>com.apple.madrid.lite</string>
+		<string>com.apple.madrid.lite.relay</string>
 		<string>com.apple.private.alloy.biz</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>

```
### perfpowermetricd

> `/usr/bin/perfpowermetricd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.computesafeguards.managing.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.computesafeguards.managing.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.computesafeguards.managing.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.computesafeguards.managing.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### aonsensed

> `/usr/libexec/aonsensed`

```diff

 	<true/>
 	<key>com.apple.developer.coreml.neural-engine-access</key>
 	<true/>
+	<key>com.apple.developer.driverkit.userclient-access</key>
+	<array>
+		<string>com.apple.driver.AppleCentauriControl</string>
+	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.fileprovider.extension-host</key>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.developer.networking.route_nc_read</key>
 	<true/>
+	<key>com.apple.driver.AirshipDaleBasebandControlInterface.user-access</key>
+	<true/>
 	<key>com.apple.driver.AppleBasebandPCI.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleBasebandPCIControl.user-access</key>

 		<string>AHSPowerInterfaceUserClient</string>
 		<string>AppleSMCClient</string>
 		<string>AppleProcessorTraceUserClient</string>
+		<string>AirshipDaleBasebandControlInterfaceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 centaurid

> `/usr/libexec/centaurid`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.developer.driverkit.userclient-access</key>
	<array>
		<string>com.apple.driver.AppleCentauriControl</string>
	</array>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.private.applecentaurimanager.user-access</key>
	<true/>
	<key>com.apple.private.kernel.global-proc-info</key>
	<true/>
	<key>com.apple.private.osanalytics.write-logs.allow</key>
	<true/>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.centaurid.CentauriNotifications</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOUserUserClient</string>
		<string>AppleKeyStoreUserClient</string>
		<string>AppleCentauriManagerUserClient</string>
	</array>
</dict>
</plist>

```
### lockdownd

> `/usr/libexec/lockdownd`

```diff

 	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>
-	<array/>
+	<array>
+		<string>com.apple.driver.AppleCentauriControl</string>
+	</array>
 	<key>com.apple.driver.I2C.device.user-access</key>
 	<true/>
 	<key>com.apple.dt.remotepairing.pairingmanagement</key>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.CoreMotion.IMUFoundationModel</string>
 		<string>com.apple.MobileAsset.UAF.FM.CodeLM</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>

 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Trial_Siri_SiriTextToSpeech/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/</string>

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_SecureAnalytics_FM/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_Guardrail/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_Trial_Siri_SiriTextToSpeech/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>

```
### restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
+	<key>com.apple.developer.driverkit.userclient-access</key>
+	<array>
+		<string>com.apple.driver.AppleCentauriControl</string>
+	</array>
 	<key>com.apple.driver.I2C.device.user-access</key>
 	<true/>
 	<key>com.apple.nearbyd.diagnostics</key>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.sysdiagnose_helper</string>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.corecapture.manager-access</key>
 	<true/>
 	<key>com.apple.generativeexperiences.sysdiagnose</key>

```
### BlueTool

> `/usr/sbin/BlueTool`

```diff

 	<key>com.apple.bluetooth.control</key>
 	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>
-	<array/>
+	<array>
+		<string>com.apple.driver.AppleCentauriBeta</string>
+	</array>
 	<key>com.apple.driver.AppleBluetoothModule.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleConvergedIPC.user-access</key>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<true/>
 	<key>com.apple.bulletinboard.utilities</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.corecapture.manager-access</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 		<string>com.apple.driver.driverkit.serial</string>
 		<string>com.apple.IOUserBluetoothSerialDriver</string>
 		<string>com.apple.AppleSunriseBluetooth</string>
+		<string>com.apple.driver.AppleCentauriBeta</string>
 	</array>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>

 		<string>/usr/sbin/BTLEServer/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/log/CoreCapture/com.apple.KalBluetooth_driver/FwLogs/</string>
+		<string>/private/var/log/CoreCapture/com.apple.driver.AppleCentauriBeta/BetaFirmwareLogs/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 		<string>com.apple.searchparty.managedperipheral</string>
 		<string>com.apple.DeviceAccess.xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.centaurid.xpc</string>
 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.bluetoothuser.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.centaurid.xpc</key>
+	<true/>
 	<key>com.apple.certui.greentea</key>
 	<true/>
 	<key>com.apple.chrono.controls</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.centaurid.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
