## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<string>409835401</string>
 	<key>application-identifier</key>
 	<string>com.apple.AMSEngagementViewService</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

```
### AuthKitUIService

> `/Applications/AuthKitUIService.app/AuthKitUIService`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.CallerAuditToken</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>

```
### AuthenticationServicesUI

> `/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI`

```diff

 		<string>com.apple.security.octagon</string>
 		<string>com.apple.sharingd</string>
 		<string>com.apple.AuthenticationServices.AutoFill</string>
+		<string>com.apple.cdp.daemon</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>

```
### AutoSettings

> `/Applications/AutoSettings.app/AutoSettings`

```diff

 	<true/>
 	<key>com.apple.private.CarPlayUIServices.punch-through</key>
 	<true/>
+	<key>com.apple.private.CarPlayUIServices.volume-notification</key>
+	<true/>
 	<key>com.apple.private.RequiredVehicleAccessories</key>
 	<array>
 		<string>AutomakerNotificationHistory</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.carkit.service</string>
+		<string>com.apple.CarPlayApp.volume-notification-service</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.CarPlayApp.punch-through-service</string>
 		<string>com.apple.CarAssetUtils.variants</string>

```
### Camera

> `/Applications/Camera.app/Camera`

```diff

 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
-	<key>com.apple.springboard.private.capture-button-events</key>
-	<true/>
 	<key>com.apple.springboard.setWantsLockButtonEvents</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### LockScreenCamera

> `/Applications/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
-	<key>com.apple.springboard.private.capture-button-events</key>
-	<true/>
 	<key>com.apple.springboard.setWantsLockButtonEvents</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### CameraMessagesApp

> `/Applications/Camera.app/PlugIns/CameraMessagesApp.appex/CameraMessagesApp`

```diff

 		<string>com.apple.camera</string>
 		<string>com.apple.MobileSMS</string>
 	</array>
-	<key>com.apple.springboard.private.capture-button-events</key>
-	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>

```
### CredentialSharingUIViewService

> `/Applications/CredentialSharingUIViewService.app/CredentialSharingUIViewService`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache/Library/Caches/com.apple.IconsCache/</string>

```
### ShareableCredentialsMessagesExtension

> `/Applications/CredentialSharingUIViewService.app/PlugIns/ShareableCredentialsMessagesExtension.appex/ShareableCredentialsMessagesExtension`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/PassKit/</string>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<true/>
 	<key>com.apple.geoservices.map-subscriptions.size-estimate</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.lookup</key>

 	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>siriRemembers</string>
+	</array>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>Lookup</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/WebClips/</string>
+		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
 		<string>/private/var/mobile/Library/Trial/Treatments/421/</string>
 		<string>/private/var/mobile/Library/Trial/Treatments/422/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.iphone.axserver</string>
 		<string>com.apple.ClipServices.clipserviced</string>

```

### 🆕 Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleH13CamInUserClient</string>
		<string>AppleH10CamInUserClient</string>
		<string>AppleH9CamInUserClient</string>
		<string>AppleH16CamInUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.applecamerad</string>
		<string>com.apple.appleh13camerad</string>
		<string>com.apple.appleh16camerad</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.Diagnostics</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Accessibility</string>
	</array>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>com.apple.system.get-hardware-identifiers</key>
	<true/>
</dict>
</plist>

```
### Diagnostic-8262

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262`

```diff

 		<string>com.apple.lsd.modifydb</string>
 		<string>com.apple.lsd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.corerepaird.test</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.lsd</string>

```
### Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
-		<string>UniqueChipID</string>
+		<string>SerialNumber</string>
 	</array>
 	<key>com.apple.private.applesepmanager.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.security.AppleImage4.user-client</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileSoftwareUpdate/Controller/RepairServices/</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/VeridianFWImage/</string>

 	<array>
 		<string>com.apple.corerepair</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.corerepaird.test</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 </dict>

```
### Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

 	<array>
 		<string>com.apple.corerepair.preflightControl</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.corerepaird.test</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 </dict>

```
### Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

 		<string>com.apple.appleh16camerad</string>
 		<string>com.apple.corerepair.preflightControl</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.corerepaird.test</string>
+	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
 </dict>

```
### Diagnostic-8343

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8343.appex/Diagnostic-8343`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/hardware/FactoryData/</string>
+		<string>/private/var/tmp/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.corerepair</string>
 	</array>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 </dict>
 </plist>
 

```
### Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.AppleNVMeEAN.allow</key>
+	<true/>
 	<key>com.apple.DiagnosticsKit.diagnosticmanager</key>
 	<true/>
 	<key>com.apple.DiagnosticsKit.extension</key>

 	<array>
 		<string>/private/var/tmp/</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>AppleNVMeEANUC</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.corerepair.preflightControl</string>

```
### SystemReport-AirPods

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport-AirPods.appex/SystemReport-AirPods`

```diff

 <dict>
 	<key>com.apple.DiagnosticsKit.extension</key>
 	<true/>
+	<key>com.apple.HearingModeService</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access-keyboard</key>

 		<string>IOAccessoryManagerUserClient</string>
 		<string>AppleSPUHIDDeviceUserClient</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.HearingModeService</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.accessory.Hearing</string>

```

### 🆕 SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.AppleNVMeEAN.allow</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>internal</string>
		<string>spi</string>
		<string>identity</string>
	</array>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.DiagnosticsSupport.CallStatsAccess</key>
	<true/>
	<key>com.apple.DiagnosticsSupport.HardwareButtonAccess</key>
	<true/>
	<key>com.apple.EnhancedLoggingState.client</key>
	<true/>
	<key>com.apple.HearingModeService</key>
	<true/>
	<key>com.apple.backboard.displaybrightness</key>
	<true/>
	<key>com.apple.bluetooth.internal</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coretelephony.Identity.get</key>
	<true/>
	<key>com.apple.driver.AppleAuthCP</key>
	<true/>
	<key>com.apple.driver.AppleAuthCP.user-access</key>
	<true/>
	<key>com.apple.hid.manager.user-access-keyboard</key>
	<true/>
	<key>com.apple.hid.multitouch.user-access</key>
	<true/>
	<key>com.apple.keystore.fdr-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.nano.nanoregistry</key>
	<true/>
	<key>com.apple.nfcacd.hwmanager</key>
	<true/>
	<key>com.apple.nfcd.ce</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.nfcd.info</key>
	<true/>
	<key>com.apple.nvmetunnel.allow</key>
	<true/>
	<key>com.apple.powerui.smartcharging</key>
	<true/>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
		<string>CLIENT_ENTITLEMENT</string>
		<string>PURGE_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>BasebandUniqueId</string>
		<string>BluetoothAddress</string>
		<string>EUICCChipID</string>
		<string>IntegratedCircuitCardIdentifier</string>
		<string>InternationalMobileEquipmentIdentity</string>
		<string>MesaSerialNumber</string>
		<string>MLBSerialNumber</string>
		<string>MobileEquipmentInfoCSN</string>
		<string>MobileEquipmentIdentifier</string>
		<string>RawPanelSerialNumber</string>
		<string>SerialNumber</string>
		<string>UniqueChipID</string>
		<string>UniqueDeviceID</string>
		<string>WifiAddress</string>
		<string>WirelessBoardSnum</string>
		<string>SysCfgDict</string>
		<string>BatterySerialNumber</string>
		<string>RoswellChipID</string>
		<string>BootManifestHash</string>
		<string>ArrowChipID</string>
		<string>ArrowUniqueChipID</string>
	</array>
	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.applemesa.allow</key>
	<true/>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.externalaccessory.showallaccessories</key>
	<true/>
	<key>com.apple.private.gasgauge-update</key>
	<true/>
	<key>com.apple.private.hid.client.admin</key>
	<true/>
	<key>com.apple.private.hid.client.event-filter</key>
	<true/>
	<key>com.apple.private.hid.client.service-protected</key>
	<true/>
	<key>com.apple.private.hid.manager.client</key>
	<true/>
	<key>com.apple.private.iokit.batterydata</key>
	<true/>
	<key>com.apple.private.iokit.batterydataprecise</key>
	<true/>
	<key>com.apple.private.mobileinboxupdater.xpc</key>
	<true/>
	<key>com.apple.private.mobilerepair.xpc</key>
	<true/>
	<key>com.apple.private.powersource-read</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceBluetoothAlways</string>
		<string>kTCCServiceBluetoothPeripheral</string>
	</array>
	<key>com.apple.private.touch.eeprom.access</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.carrier-bundle.read</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/preboot/</string>
		<string>/private/var/mobile/Library/Logs/AppleSupport/</string>
		<string>/private/var/logs/AppleSupport/</string>
		<string>/private/var/tmp/biokit_hw_issue_notification</string>
		<string>/private/var/mobile/Library/Preferences/com.apple.demo-settings.plist</string>
		<string>/private/var/mobile/Library/Preferences/com.apple.Accessibility.plist</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleNVMeUpdateUC</string>
		<string>AppleGasGaugeUpdateUserClient</string>
		<string>AppleGasGaugeUpdate</string>
		<string>AppleBasebandUserClient</string>
		<string>IOAccessoryManagerUserClient</string>
		<string>AppleSPUUserClient</string>
		<string>AppleSPUHIDDeviceUserClient</string>
		<string>AppleMultitouchSPIUserClient</string>
		<string>AppleMultitouchDeviceUserClient</string>
		<string>AppleEmbeddedTouchEEPROMDriverUC</string>
		<string>AppleNVMeEANUC</string>
		<string>AppleBiometricServicesUserClient</string>
		<string>IO80211APIUserClient</string>
		<string>AppleAuthCPUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.HearingModeService</string>
		<string>com.apple.private.corewifi.mobilewifi-xpc</string>
		<string>com.apple.wifi.manager</string>
		<string>com.apple.inboxupdaterd</string>
		<string>com.apple.springboard.blockableservices</string>
		<string>com.apple.iokit.powerdxpc</string>
		<string>com.apple.CheckerBoard.jail.com.apple.frontboard.systemappservices</string>
		<string>com.apple.CheckerBoard.jail.com.apple.frontboard.workspace</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.nfcacd.hwmanager</string>
		<string>com.apple.backlightd</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.mobilerepaird</string>
		<string>com.apple.ZhuGeService</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.powerui.smartChargeManager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
		<string>com.apple.purplebuddy</string>
		<string>com.apple.enhanced-logging-state</string>
		<string>com.apple.accessory.Hearing</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Diagnostics</string>
	</array>
	<key>com.apple.seld.cm</key>
	<true/>
	<key>com.apple.seld.tsmmanager</key>
	<true/>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>com.apple.system.get-hardware-identifiers</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
</dict>
</plist>

```
### FTMInternal-4

> `/Applications/FTMInternal-4.app/FTMInternal-4`

```diff

 		<string>phone</string>
 		<string>carrier-settings</string>
 	</array>
+	<key>com.apple.cellular-logging.internal</key>
+	<true/>
 	<key>com.apple.developer.cellular-logging.allow</key>
 	<array>
 		<string>public-cellular-logging</string>

```
### FontPickerUIService

> `/Applications/FontPickerUIService.app/FontPickerUIService`

```diff

 	<array>
 		<string>com.apple.UIKit.FontPickerStorage</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>Install</string>
+	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>

```
### HealthPrivacyService

> `/Applications/HealthPrivacyService.app/HealthPrivacyService`

```diff

 	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
+	<key>com.apple.devicesharing.guest-user-mode-client</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.devicesharing.guestusermodeservice</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
 	<true/>
+	<key>com.apple.coremedia.cameraviewfinder</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
+	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.mediasafetynet.exceptions.cam</string>
+		<string>com.apple.coremedia.cameraviewfinder</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Media

> `/Applications/Media.app/Media`

```diff

 	<true/>
 	<key>com.apple.private.CarPlayUIServices.status-bar-style</key>
 	<true/>
+	<key>com.apple.private.CarPlayUIServices.volume-notification</key>
+	<true/>
 	<key>com.apple.private.RequiredVehicleAccessories</key>
 	<array>
 		<string>AudioSettings</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.CarPlayApp.volume-notification-service</string>
 		<string>com.apple.CarPlayApp.status-bar-service</string>
 		<string>com.apple.CarAssetUtils.variants</string>
 		<string>com.apple.carkit.service</string>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 		<string>com.apple.ImageIO</string>
 		<string>com.apple.nanolifestyle.privacy</string>
 		<string>PUICNPSPreferences</string>
-		<string>com.apple.IMCoreSpotlight</string>
 		<string>com.apple.proactive.experiments.responses</string>
 		<string>com.apple.messages.ordering-automation</string>
 		<string>com.apple.suggestions</string>

 		<string>com.apple.messages.commsafety</string>
 		<string>com.apple.contacts.sharedProfile</string>
 		<string>com.apple.ClarityUI.Messages</string>
+		<string>com.apple.IMCoreSpotlight</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### MobileSafari

> `/Applications/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>
 	<true/>
+	<key>com.apple.geoservices.map-subscriptions.check-existence</key>
+	<true/>
+	<key>com.apple.geoservices.map-subscriptions.size-estimate</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>

 		<string>com.apple.MobileAsset.SafariCloudHistoryConfiguration</string>
 		<string>com.apple.MobileAsset.CoreSuggestions</string>
 		<string>com.apple.MobileAsset.SafariBackgroundImage</string>
+		<string>com.apple.MobileAsset.UAF.SafariBrowsingAssistant</string>
 	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/Applications/</string>
 		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>/Library/Caches/com.apple.ClipServices/</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.email.maild</string>
 		<string>com.apple.AuthenticationServices.AutoFill</string>
 		<string>com.apple.WebKit.WebContent.Crashy</string>
+		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.sage.summarization</string>
 		<string>com.apple.generativeexperiences.summarization</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.CloudSubscriptionFeatures.datadetectors</string>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.SocialLayer</string>
+		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
-	<key>com.apple.photos.intelligence.llmDefaultOverwrite</key>
+	<key>com.apple.photos.intelligence.mcDefaultOverwrite</key>
 	<true/>
 	<key>com.apple.posterboardservices.data-store</key>
 	<true/>

 		<string>Photos.Search</string>
 		<string>Photos.Map</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>Discoverability.Signals</string>
+		<string>Discoverability.Usage</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>PhotosPFL</key>
+		<key>Photos</key>
 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>Photos.Memories.Shared</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>Photos.MemoryCreation</key>
 				<dict>
 					<key>mode</key>

 		<string>appEntityRelevanceRanking</string>
 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
+		<string>hasAssociationSubgraph</string>
 	</array>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>

```
### PhotoPicker

> `/Applications/MobileSlideShow.app/PlugIns/PhotoPicker.appex/PhotoPicker`

```diff

 		<string>appEntityRelevanceRanking</string>
 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
+		<string>hasAssociationSubgraph</string>
 	</array>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>

```
### PhotosMessagesApp

> `/Applications/MobileSlideShow.app/PlugIns/PhotosMessagesApp.appex/PhotosMessagesApp`

```diff

 		<string>appEntityRelevanceRanking</string>
 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
+		<string>hasAssociationSubgraph</string>
 	</array>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>

```
### PhotosPicker

> `/Applications/MobileSlideShow.app/PlugIns/PhotosPicker.appex/PhotosPicker`

```diff

 		<string>appEntityRelevanceRanking</string>
 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
+		<string>hasAssociationSubgraph</string>
 	</array>
 	<key>com.apple.private.keychain.sysbound</key>
 	<true/>

```

### 🆕 MomentsDiagnosticsExtensionFeedbackAssistant

> `/Applications/MomentsUIService.app/PlugIns/MomentsDiagnosticsExtensionFeedbackAssistant.appex/MomentsDiagnosticsExtensionFeedbackAssistant`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.momentsd.internal</key>
	<array>
		<string>MOPromptManagerTest</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/log/com.apple.xpc.launchd/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.momentsd/</string>
		<string>/Library/Logs/com.apple.momentsd/</string>
		<string>/Library/com.apple.momentsd/Temp/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/com.apple.MomentsDiagnosticExtension/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.momentsd</string>
	</array>
</dict>
</plist>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.PassKitCoreXPCService</string>
 		<string>com.apple.nfcd.hwmanager</string>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.softposreaderd</string>
 		<string>com.apple.idcredd.biometrics.xpc</string>
 		<string>com.apple.passd.sharing-channel</string>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 		<string>com.apple.WebSheet.plist</string>
 		<string>com.apple.wifi-private-mac-networks.plist</string>
 	</array>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.UIKit.status-bar-override-allow</key>
 	<true/>
 	<key>com.apple.USBCEntitlement</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.AllowUnapprovedSensor</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>

 		<string>modeConfigurationUIFlowLoggingEvent</string>
 		<string>SystemSettings.GestureEducation.Multitasking</string>
 		<string>SystemSettings.GestureEducation.PillOutcome</string>
+		<string>Safari.AutoPlay</string>
+		<string>Safari.WebPagePerformance</string>
+		<string>Safari.Navigations</string>
+		<string>Safari.PageLoad</string>
+		<string>Safari.WindowProxy</string>
+		<string>Safari.Browsing.Assistant</string>
 	</array>
 	<key>com.apple.private.biometrickit.allow-enroll</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
+	<key>com.apple.private.iokit.batteryhealthstate</key>
+	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.CoreSuggestions</string>
+		<string>com.apple.MobileAsset.UAF.SafariBrowsingAssistant</string>
 	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.parsec.sba/shared_locks/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Caches/com.apple.ClipServices/</string>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.datadetectors</string>
 		<string>com.apple.newscore</string>
+		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SafetyMonitorApp

> `/Applications/SafetyMonitorApp.app/SafetyMonitorApp`

```diff

 	<true/>
 	<key>com.apple.carousel.liveactivities.openurl</key>
 	<true/>
+	<key>com.apple.carousel.liveactivities.prevents_smartstack_dismissal</key>
+	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 	<true/>
 	<key>com.apple.RemoteDisplay.SessionState</key>
 	<true/>
+	<key>com.apple.coremedia.cameraviewfinder</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>

 		<string>com.apple.ScreenContinuityShell</string>
 		<string>com.apple.RemoteDisplay</string>
 		<string>com.apple.systemstatus</string>
+		<string>com.apple.coremedia.cameraviewfinder</string>
 		<string>com.apple.sessionservices</string>
 	</array>
 	<key>com.apple.springboard.continuitysession</key>

 	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>
-	<key>fairplay-client</key>
-	<true/>
 </dict>
 </plist>
 

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
+	<dict>
+		<key>com.apple.productkit.personalization</key>
+		<string>com.apple.productkit.personalization</string>
+	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CarPlayApp.non-launching-service</string>
 		<string>com.apple.Photos.MultiLibrary</string>
+		<string>com.apple.SharingServices</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.bird.token</string>

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.sharing.Client</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.spotlight.entitledattributes</key>

 	<array>
 		<string>V568VXD5P8.is.workflow.my.app</string>
 		<string>com.apple.MediaRemote.pairing</string>
+		<string>com.apple.sharing.appleidauthentication</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.write</string>
 		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.siri.client_lite</string>
+		<string>com.apple.siri.location</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<array>
 		<string>stream.unifiedMessageStream.readonly</string>
 	</array>
+	<key>com.apple.siri.client_lite</key>
+	<true/>
+	<key>com.apple.siri.location</key>
+	<true/>
 	<key>com.apple.siriinferenced</key>
 	<true/>
 	<key>com.apple.siriknowledged</key>

```
### SleepLockScreen

> `/Applications/SleepLockScreen.app/SleepLockScreen`

```diff

 	<array>
 		<string>/Library/Weather/</string>
 	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>RootDomainUserClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.MobileTimer.alarmserver</string>

```
### SoftwareUpdateUIService

> `/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService`

```diff

 	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.security.no-container</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_SoftwareUpdateDocumentation/</string>

 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
-		<string>visualIdentifier</string>
+		<string>siriRemembers</string>
 		<string>nerdSummary</string>
 		<string>behavioralPopularitySignals</string>
 		<string>nerdEmbeddingsPeopleTable</string>

 	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
+	<key>com.apple.private.parsec.default-client</key>
+	<string>com.apple.spotlight</string>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.remindd</key>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/mobile/Library/Trial/</string>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.com.apple.security.temporaryGenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>
 		<string>photos.person</string>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.stickers</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<array>
 		<string>/private/var/mobile/Library/Application Support/com.apple.VisualGeneration/</string>
 		<string>/private/var/mobile/Media/PhotoData/Caches/VisionService/</string>
-		<string>/private/var/MobileAsset/AssetsV2/</string>
-		<string>/System/Library/PreinstalledAssetsV2/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SubcredentialInvitationMessagesExtension

> `/Applications/SubcredentialUIService.app/PlugIns/SubcredentialInvitationMessagesExtension.appex/SubcredentialInvitationMessagesExtension`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/PassKit/</string>

```
### SubcredentialUIService

> `/Applications/SubcredentialUIService.app/SubcredentialUIService`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Preferences/com.apple.stockholm.plist</string>

```

### 🆕 portrait_filters_archive_bin.metallib

> `/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_archive_bin.metallib`

- No entitlements *(yet)*

### 🆕 portrait_filters_fullsize_archive_bin.metallib

> `/System/Library/CoreImage/PortraitFilters.cifilter/portrait_filters_fullsize_archive_bin.metallib`

- No entitlements *(yet)*
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.accessibility.physicalinteraction.client</key>
 	<true/>
+	<key>com.apple.airplay.autoconnect.services.allow</key>
+	<true/>
 	<key>com.apple.airplay.receiver.mediaremote.services</key>
 	<true/>
 	<key>com.apple.airplay.receiverservices</key>

 	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
+	<key>com.apple.assistant.dictation.prerecorded</key>
+	<true/>
 	<key>com.apple.audio.allows.mix.to.uplink</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>

 		<string>com.apple.accessibility.controlcenter.sounddetection</string>
 		<string>com.apple.accessibility.controlcenter.hapticmusic</string>
 	</array>
+	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 		<string>com.apple.accessibility.lg</string>
 		<string>com.apple.facetime.bag</string>
 		<string>com.apple.accessibility.livespeech</string>
+		<string>com.apple.speech.SpeechRecognitionCommandAndControl</string>
 		<string>com.apple.WatchControl</string>
 		<string>com.apple.airplay</string>
 		<string>com.apple.ClarityUI</string>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.private.carkit.app</key>
 	<true/>
+	<key>com.apple.private.carkit.carconnectiontime</key>
+	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
 	<key>com.apple.private.carkit.themeAssetLibrary</key>

 		<string>com.apple.carkit.clustercontrol</string>
 		<string>com.apple.carkit.service</string>
 		<string>com.apple.carkit.theme-asset-library</string>
+		<string>com.apple.carkit.reconnectiontime.service</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.intents.intents-helper</string>
 		<string>com.apple.siri.activation.service</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.Pasteboard.trusted-authentication-message-request</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.ProactiveSummarization.feedback</key>

 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.usernotificationsvendor.listener</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>1720</string>
 		<string>962</string>
 	</array>
-	<key>com.apple.trial.status.namespace-name.allow</key>
-	<array>
-		<string>SIRI_CARPLAY_SETTINGS</string>
-	</array>
 	<key>com.apple.tzlink.allow</key>
 	<true/>
 	<key>com.apple.ui-services-discovery</key>

```
### DeveloperSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DeveloperSettingsIntents.appex/DeveloperSettingsIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
-	<string>com.apple.Preferences</string>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>

```

### 🆕 DictionarySettingsExtension

> `/System/Library/ExtensionKit/Extensions/DictionarySettingsExtension.appex/DictionarySettingsExtension`

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

### 🆕 GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.Photos</string>
	</array>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.person</string>
		<string>photos.face</string>
	</array>
	<key>com.apple.private.avfoundation.capture.allow</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>peopleSubgraph</string>
		<string>inferenceFeaturesECR</string>
		<string>personEntityRelevanceRanking</string>
		<string>entitySimilarityFeatures</string>
	</array>
	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
	<true/>
	<key>com.apple.private.photos.allowlibraryupgrade</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.librarymanagement</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.GenerativePlayground</string>
	</array>
	<key>com.apple.security.device.camera</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
	</array>
	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
	<array>
		<string>AppleNVMeEANUC</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### InferenceProviderService

> `/System/Library/ExtensionKit/Extensions/InferenceProviderService.appex/InferenceProviderService`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.FM.CodeLM</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.modelmanager.inferenceproviderservice</string>

```
### IntelligenceIntentsExtension

> `/System/Library/ExtensionKit/Extensions/IntelligenceIntentsExtension.appex/IntelligenceIntentsExtension`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/CallDirectory/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.identityservicesd.embedded.auth</string>

```

### 🆕 NotificationsSettingsExtension

> `/System/Library/ExtensionKit/Extensions/NotificationsSettingsExtension.appex/NotificationsSettingsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
</dict>
</plist>

```
### PFLHRPeriodPredCK

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK`

```diff

 	<string>com.apple.priml.pfl.plugins</string>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 		<string>HKQuantityTypeIdentifierHeartRateVariabilitySDNN</string>
 		<string>HKQuantityTypeIdentifierRestingHeartRate</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MLHostTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### PFLHRPeriodPredPush

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush`

```diff

 	<string>com.apple.priml.pfl.plugins</string>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 		<string>HKQuantityTypeIdentifierHeartRateVariabilitySDNN</string>
 		<string>HKQuantityTypeIdentifierRestingHeartRate</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MLHostTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### PFLNightingaleD

> `/System/Library/ExtensionKit/Extensions/PFLNightingaleD.appex/PFLNightingaleD`

```diff

 	<string>com.apple.priml.pfl.plugins</string>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 		<string>HKQuantityTypeIdentifierHeartRateVariabilitySDNN</string>
 		<string>HKQuantityTypeIdentifierRestingHeartRate</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MLHostTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### PhotosPFLPlugin

> `/System/Library/ExtensionKit/Extensions/PhotosPFLPlugin.appex/PhotosPFLPlugin`

```diff

 	<array>
 		<string>Photos.Style</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>MLHostTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+			</array>
+		</dict>
 		<key>PhotosPFL</key>
 		<dict>
 			<key>Streams</key>

```

### 🆕 PodcastsSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PodcastsSettingsAppIntentsExtension.appex/PodcastsSettingsAppIntentsExtension`

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

### 🆕 PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLMLHostPlugins.PrivateEvolutionPlugin</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.pfl.container</string>
		<string>com.apple.pfl.preprod.container</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.priml.pfl.plugins</string>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.cloudkit.systemService</key>
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
		<key>PrivateEvolutionPlugin</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Zeolite.Ledger.Embedding</string>
			</array>
		</dict>
	</dict>
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
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`

```diff

 	<array>
 		<string>com.apple.MobileAsset.SpotlightResources</string>
 		<string>com.apple.MobileAsset.LinguisticData</string>
+		<string>com.apple.MobileAsset.UAF.FM.com.apple.security.temporaryGenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.imcore.spi.database-access</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>peopleSubgraph</string>

```
### SettingsCellularAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SettingsCellularAppIntentsExtension.appex/SettingsCellularAppIntentsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+		<string>cellular-plan</string>
+	</array>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.CellularPlanDaemon.xpc</string>
+	</array>
 </dict>
 </plist>
 

```
### SiriMASPFLCK

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/SiriMASPFLCK`

```diff

 	<array>
 		<string>Siri.AppSelection.Music</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MLHostTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### SiriMASPFLPlugin

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPlugin.appex/SiriMASPFLPlugin`

```diff

 	<array>
 		<string>Siri.AppSelection.Music</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MLHostTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### SiriMASPFLPush

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/SiriMASPFLPush`

```diff

 	<array>
 		<string>Siri.AppSelection.Music</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MLHostTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.settings</string>
+		<string>com.apple.ironwood.support</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.siri.sirisuggestions</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/Library/Managed Preferences/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Shortcuts/ToolKit/</string>

 	<true/>
 	<key>com.apple.siriinferenced</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>1343</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### SummarizationTool

> `/System/Library/ExtensionKit/Extensions/SummarizationTool.appex/SummarizationTool`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>$(AppIdentifierPrefix)$(CFBundleIdentifier)</string>
+	<string>com.apple.summarization.SummarizationTool</string>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
-	<string>$(AppIdentifierPrefix)$(CFBundleIdentifier)</string>
+	<string>com.apple.summarization.SummarizationTool</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

```
### WebThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/WebThumbnailExtension`

```diff

 <dict>
 	<key>com.apple.private.quicklook-thumbnail.webkit</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.runningboard</string>
+	</array>
 </dict>
 </plist>
 

```
### ZeoliteExtension

> `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension`

```diff

 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>Zeolite.Ledger.Embedding</string>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>

 			<key>Streams</key>
 			<array>
 				<string>Zeolite.Ledger.Embedding</string>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>
 		</dict>
 	</dict>

```
### com.apple.CallKit.CallDirectory

> `/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.dynamicUseCase.allow</key>
 	<true/>
+	<key>com.apple.private.ids.remotecredentials</key>
+	<true/>
+	<key>com.apple.private.imcore.imremoteurlconnection</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>
 		<string>com.apple.ciphermld</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.facetime.bag</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>platform-application</key>

```
### com.apple.CallKit.CallDirectoryMaintenance

> `/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.dynamicUseCase.allow</key>
 	<true/>
+	<key>com.apple.private.ids.remotecredentials</key>
+	<true/>
+	<key>com.apple.private.imcore.imremoteurlconnection</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>
 		<string>com.apple.ciphermld</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.facetime.bag</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>platform-application</key>

```
### progressd

> `/System/Library/Frameworks/ClassKit.framework/progressd`

```diff

 		<string>com.apple.schoolwork</string>
 		<string>iCloud.com.apple.homeroom</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### LimitedLibraryPickerViewService

> `/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/System/Library/Frameworks/ContactsUI.framework/Extensions/LimitedLibraryPickerViewService.appex/LimitedLibraryPickerViewService</string>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### ContactsViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```

### 🆕 CoreLocationMapLNPromptPlugin

> `/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationMapLNPromptPlugin.appex/CoreLocationMapLNPromptPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.locationd.authorizeapplications</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
</dict>
</plist>

```
### eedmediaservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice`

```diff

 	<true/>
 	<key>com.apple.das.private.bgtask.continuedprocessing</key>
 	<true/>
+	<key>com.apple.das.private.bgtask.continuedprocessing.iconBundleIdentifier</key>
+	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>
 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>

 		<string>com.apple.locationd</string>
 		<string>com.apple.camera</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>IOSurfaceAcceleratorClient</string>
+	</array>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```
### CoreSpotlightService

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService`

```diff

 	<true/>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/CrashReporter/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.symptom_diagnostics</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.searchd</string>
+	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>platform-application</key>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<true/>
 	<key>com.apple.keystore.allow.background-processing-assertions</key>
 	<true/>
+	<key>com.apple.mobileassetd.v2</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
+	<key>com.apple.private.spotlight.openjournal</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.duetactivityscheduler</string>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<key>com.apple.private.ids.registration</key>
 	<array>
 		<string>com.apple.madrid</string>
+		<string>com.apple.private.alloy.multiplex1</string>
 	</array>
 	<key>com.apple.private.ids.server.messaging</key>
 	<array>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<true/>
 	<key>com.apple.financekit.financial-insights.host</key>
 	<true/>
+	<key>com.apple.financekit.image-processing.host</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

```
### com.apple.HealthKit.HealthDiagnosticExtension

> `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthDiagnosticExtension.appex/com.apple.HealthKit.HealthDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appstored</key>

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
-		<string>UserFocusComputedMode</string>
+		<string>UserFocus.ComputedMode</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

```diff

 	<array>
 		<string>com.apple.ReportMemoryException</string>
 		<string>com.apple.wifivelocityd</string>
+		<string>com.apple.coreautomationd.xpc.root</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

 	<string>serverPreferred</string>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.TrustedPeersHelper</string>
 	<key>com.apple.developer.aps-environment</key>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 	<array>
 		<string>/private/var/MobileAsset/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/PersonalDeviceVolumes/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/UnifiedAssetFramework/</string>

 		<string>751</string>
 		<string>1701</string>
 	</array>
+	<key>com.apple.uservault</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### AirPlaySenderService

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/XPCServices/AirPlaySenderService.xpc/AirPlaySenderService`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.avfoundation</string>
+		<string>com.apple.coreaudio</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.corevideo</string>
 		<string>com.apple.mediaremote</string>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<string>com.apple.weather</string>
 	<key>com.apple.duet.expertcenter.consumer</key>
 	<true/>
+	<key>com.apple.facetimemessagestored.service</key>
+	<array>
+		<string>access-facetime-messaging</string>
+	</array>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.facetimemessagestored.service</string>
 		<string>com.apple.siri.location</string>
 		<string>com.apple.tipsd.assistant</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>Media.NowPlaying</string>
 		<string>Notification</string>
 		<string>Sage.Transcript</string>
+		<string>Siri.Metrics.OnDeviceDigestExperimentMetrics</string>
 		<string>Siri.Metrics.OnDeviceDigestSegmentsCohorts</string>
+		<string>Siri.Metrics.OnDeviceDigestUsageMetrics</string>
 		<string>Siri.SelfTriggerSuppression</string>
 		<string>Siri.UI</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>Discoverability.Signals</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>Siri.AnalyticsIdentifiers.HomeSeed</string>
 		<string>Siri.AnalyticsIdentifiers.UserAggregationId</string>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
+	<key>com.apple.private.appstorecomponents.media-client-id</key>
+	<string>com.apple.akd</string>
+	<key>com.apple.private.appstorecomponents.media-client-version</key>
+	<string>1</string>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.associated-domains</key>

 		<string>com.apple.asktod</string>
 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.timed.xpc</string>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.nanobuddy</string>
 		<string>com.apple.pairedsync</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.AppStoreComponents</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AvpFairPlayUserClient</string>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.carousel.nonmatchingsessions</key>
 	<true/>
 	<key>com.apple.chrono.event-service-publisher</key>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

 	<array>
 		<string>SIRI_SPEECH_SV_SPEECH_PROFILE</string>
 	</array>
+	<key>com.apple.uservault</key>
+	<true/>
 </dict>
 </plist>
 

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.private.exclaves.conclave-host</key>
 	<true/>
+	<key>com.apple.private.feedbacklogger</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>

 	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
 	<key>com.apple.private.siri.activation</key>

 		<string>/Library/CoreDuet/</string>
 		<string>/Library/PeopleSuggester/</string>
 		<string>/Library/Caches/com.apple.corespeech.cat.xpc/</string>
-		<string>/Library/Trial/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>/Library/Assistant/</string>
 		<string>/Library/Caches/RaiseToSpeak/</string>
 		<string>/Library/Caches/CoreSpeech/</string>
-		<string>/tmp/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.assistant.domain.validation.service</string>
 		<string>com.apple.assistant.domain.system.settings.service</string>
+		<string>com.apple.feedbacklogger</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>UAF_AB_UNDERSTANDING</string>
 	</array>
+	<key>com.apple.uservault</key>
+	<true/>
 	<key>com.apple.voicetrigger.voicetriggerservice</key>
 	<true/>
 	<key>keychain-access-groups</key>

 	</array>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

```
### speechmodeltrainingd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd`

```diff

 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.voiceservices.tts</string>
 		<string>com.apple.privacyaccountingd</string>
-		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.sirittsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<true/>
 	<key>com.apple.siri.embeddedspeech</key>
 	<true/>
-	<key>com.apple.siri.koa.donate.internal</key>
-	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>372</string>

```
### com.apple.DataDetectorsUI.ActionsExtension

> `/System/Library/PrivateFrameworks/DataDetectorsUI.framework/PlugIns/com.apple.DataDetectorsUI.ActionsExtension.appex/com.apple.DataDetectorsUI.ActionsExtension`

```diff

 	<string>com.apple.DataDetectorsUI.ActionsExtension</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.geoanalyticsd</string>
 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.lsd.xpc</string>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.private.amfi.can-check-trust-cache</key>
 	<true/>
+	<key>com.apple.private.amfi.data-migration</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>

```
### com.apple.DocumentManager.Service

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServicePhotosAdd</string>
+		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
-	<key>com.apple.private.assets.accessible-asset-types</key>
-	<array>
-		<string>com.apple.MobileAsset.MailDynamicData</string>
-	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### FedStatsMLRPluginClassB

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/FedStatsMLRPluginClassB`

```diff

 		<string>SensitiveContentAnalysis.UIInteraction</string>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>Safari.WindowProxy</string>
+		<string>Device.Wireless.ConnectivityContext</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>845</string>
 		<string>1542</string>
 		<string>1544</string>
+		<string>1546</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```

### 🆕 FileProviderDiagnosticExtension

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.internal.fileprovider.debug</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
</dict>
</plist>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.Accessibility</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
 		<string>iyfxmLogGVIaH7aEgqwcIA</string>
 	</array>
 	<key>com.apple.private.applemediaservices</key>

 	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Health</string>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 		<string>com.apple.accessibility.controlcenter.hearingdevices</string>
 		<string>com.apple.accessibility.controlcenter.hearingaids</string>
 	</array>
+	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
+	<true/>
 	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.app-badge-value-access</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 		<string>com.apple.private.alloy.willow.stream</string>
 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
+		<string>com.apple.private.alloy.energykit</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.ids.messaging.high-priority</key>

 		<string>com.apple.private.alloy.willow.stream</string>
 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
+		<string>com.apple.private.alloy.energykit</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.ids.remotecredentials</key>

 		<string>com.apple.private.alloy.willow.stream</string>
 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
+		<string>com.apple.private.alloy.energykit</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.ids.session</key>

 		<string>com.apple.private.alloy.willow.stream</string>
 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
+		<string>com.apple.private.alloy.energykit</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>

 		<string>com.apple.private.alloy.willow.stream</string>
 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
+		<string>com.apple.private.alloy.energykit</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

 	<array>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.ThreadNetwork.xpc</string>
-		<string>com.apple.coreautomationd.xpc.root</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.nanoprefsync</string>
 		<string>com.apple.siri.analytics.assistant</string>

```
### IMDMessageServicesAgent

> `/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent`

```diff

 	<string>YES</string>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	<true/>
 	<key>com.apple.locationd.place_inference</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.MorphunData</string>
+		<string>com.apple.MobileAsset.TempMorphunData</string>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.intelligenceflow.intelligencecontextd</string>
 	<key>com.apple.private.biome.read-only</key>

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.proactive.eventtracker</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.intelligenceflow</string>

 		<string>com.apple.contactsd</string>
 		<string>com.apple.uiintelligencesupport.agent</string>
 		<string>com.apple.siriinferenced</string>
+		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.siri.morphunassetsupdaterd</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.intelligenceflow</string>
 		<string>com.apple.mobilecal</string>
+		<string>com.apple.siri.morphun</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

 	<string>com.apple.intelligenceflow.intelligencecontextd</string>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>755</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>

 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.intelligenceplatform.EventLog</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.proactive.sports.xpc</string>
 		<string>com.apple.healthd.server</string>

 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.SoftwareUpdate</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.ImageConversionService.xpc/com.apple.photos.ImageConversionService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.aned.private.ANEAccess.allow</key>
+	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

```
### SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.Mail</key>

```
### QuickTypePFLExtension

> `/System/Library/PrivateFrameworks/NLPLearner.framework/PlugIns/QuickTypePFLExtension.appex/QuickTypePFLExtension`

```diff

 	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
-	<key>com.apple.privatefederatedlearning.allowed</key>
-	<true/>
 	<key>com.apple.runningboard.NLPLearner</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### NTKDiagnosticExtensionCompanion

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/PlugIns/NTKDiagnosticExtensionCompanion.appex/NTKDiagnosticExtensionCompanion`

```diff

 	<array>
 		<string>/private/var/mobile/Library/NanoTimeKit/</string>
 		<string>/private/var/mobile/Library/Caches/NanoTimeKit/</string>
+		<string>/private/var/mobile/Library/PhotosFace/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 	<string>628765583</string>
 	<key>application-identifier</key>
 	<string>com.apple.newsd</string>
+	<key>aps-environment</key>
+	<string>production</string>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.pegasus.context</key>

 	<array>
 		<string>group.com.apple.newsd</string>
 	</array>
+	<key>com.apple.private.sessionkit.custom-platter-target</key>
+	<true/>
+	<key>com.apple.private.sessionkit.customPushProcessIdentifier</key>
+	<true/>
+	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.newsd</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.news.ANFDecoder</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.news.TodayFeedConfigDecoder</string>
+		<string>com.apple.sessionservices</string>
+		<string>com.apple.duetactivityscheduler</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.newscore2</string>
 	</array>
+	<key>com.apple.sessionkit.broadcastPush</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1397409257</string>
 </dict>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.sessionservices</string>
-	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```
### PassKitServicesXPCService

> `/System/Library/PrivateFrameworks/PassKitServices.framework/XPCServices/PassKitServicesXPCService.xpc/PassKitServicesXPCService`

```diff

 	<true/>
 	<key>com.apple.developer.kernel.increased-memory-limit</key>
 	<true/>
+	<key>com.apple.nfcd.hwmanager</key>
+	<true/>
 	<key>com.apple.passd.peer-payment</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.nfcd.hwmanager</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.UIKit</string>

```
### PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 	</array>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>1420</string>
+		<string>1800</string>
 	</array>
 	<key>fairplay-client</key>
 	<string>511712240</string>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 	</array>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
-	<key>com.apple.photos.intelligence.llmDefaultOverwrite</key>
+	<key>com.apple.photos.intelligence.mcDefaultOverwrite</key>
 	<true/>
 	<key>com.apple.posterboardservices.data-store</key>
 	<true/>

 	<array>
 		<string>com.apple.MobileAsset.VideoAppsMusicAssets</string>
 		<string>com.apple.MobileAsset.VideoAppsMusicAssets3</string>
+		<string>com.apple.MobileAsset.LinguisticData</string>
 		<string>com.apple.MobileAsset.PhotosCuratedMusicLibraryAsset</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>

 		<string>appEntityRelevanceRanking</string>
 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
+		<string>hasAssociationSubgraph</string>
 	</array>
 	<key>com.apple.private.mediaanalysisd.datamanagement.embedding</key>
 	<true/>

```

### 🆕 PhotosStoryDiagnostics

> `/System/Library/PrivateFrameworks/PhotosIntelligence.framework/PlugIns/PhotosStoryDiagnostics.appex/PhotosStoryDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PhotosIntelligence.PhotosStoryDiagnostics</string>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Media/PhotoData/internal/storydiagnostics/</string>
	</array>
</dict>
</plist>

```
### PerfPowerServicesSignpostReader

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader`

```diff

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.trial.status.deployment-environment.allow</key>
+	<array>
+		<integer>0</integer>
+	</array>
 </dict>
 </plist>
 

```
### liveactivitiesd

> `/System/Library/PrivateFrameworks/SessionCore.framework/Support/liveactivitiesd`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/UserConfigurationProfiles/</string>
+		<string>/Library/DeviceRegistry/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```

### 🆕 SiriSuggestionsInternalXPCServices

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsInternalXPCServices.xpc/SiriSuggestionsInternalXPCServices`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>AppIntent</string>
		<string>siriRemembers</string>
		<string>App.InFocus</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.security.storage.SiriInference</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/com.apple.siri.inference/</string>
		<string>/Library/Shortcuts/ToolKit/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant.settings</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.sirisuggestions</string>
	</array>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
	<key>com.apple.siriinferenced</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>1343</string>
	</array>
</dict>
</plist>

```
### sleepd

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd`

```diff

 		<string>com.apple.private.alloy.sleep.classd</string>
 		<string>com.apple.private.alloy.avconference.avctester</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>com.apple.sleepd.inBedDetection</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Device.ScreenLocked</string>
+				<string>Device.Power.PluggedIn</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>WaitForSystemAppMigrationToComplete</string>

```
### spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.allow-SUController</key>
+	<true/>
 	<key>com.apple.private.allow-subridge</key>
 	<true/>
 	<key>com.apple.private.apfs.attribution-tags</key>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 		<string>com.apple.usernotifications.systemservice</string>
 		<string>com.apple.pearld</string>
 		<string>com.apple.spotlight.IndexAgent</string>
+		<string>com.apple.spotlight.SearchAgent</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.bulletinboard.observerconnection</string>
 		<string>com.apple.sharingd.nsxpc</string>

 		<string>com.apple.bulletinboard</string>
 		<string>com.apple.usernotificationsd</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>RootDomainUserClient</string>
+	</array>
 	<key>com.apple.security.ts.read-any-bundle</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```

### 🆕 ccportrait_archive_bin.metallib

> `/System/Library/VideoProcessors/CCPortrait.bundle/ccportrait_archive_bin.metallib`

- No entitlements *(yet)*
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.tv.sharedcontainer</string>
+		<string>group.tvappservices.container</string>
 	</array>
 	<key>com.apple.private.security.system-application</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.tvappservices.container</string>
 		<string>group.com.apple.sports</string>
 		<string>group.com.apple.tv.sharedcontainer</string>
 	</array>

```
### TVIntentsExtension

> `/private/var/staged_system_apps/AppleTV.app/PlugIns/TVIntentsExtension.appex/TVIntentsExtension`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.tv.sharedcontainer</string>
+		<string>group.tvappservices.container</string>
 	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>

 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.tvappservices.container</string>
 		<string>group.com.apple.tv.sharedcontainer</string>
+		<string>group.tvappservices.container</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### TVWidgetExtension

> `/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.tv.sharedcontainer</string>
+		<string>group.tvappservices.container</string>
 	</array>
 	<key>com.apple.private.sessionkit.listener</key>
 	<true/>

 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.tvappservices.container</string>
 		<string>group.com.apple.sports</string>
 		<string>group.com.apple.tv.sharedcontainer</string>
 	</array>

```
### BooksWidgetExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksWidgetExtension.appex/BooksWidgetExtension`

```diff

 	<array>
 		<string>group.com.apple.iBooks</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Media/Books/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.iBooks.BookDataStoreService</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 		<string>com.apple.proactive.sleepSchedule</string>
 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.softposreaderd</string>
+		<string>com.apple.aa.daemon.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Calculator

> `/private/var/staged_system_apps/Calculator.app/Calculator`

```diff

 	<array>
 		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
+	<key>file-read-data</key>
+	<true/>
 	<key>file-write-data</key>
 	<true/>
 	<key>platform-application</key>
 	<true/>
+	<key>user-preference-read</key>
+	<true/>
 	<key>user-preference-write</key>
 	<true/>
 </dict>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>kTCCServiceFaceID</string>
+		<string>kTCCServicePhotosAdd</string>
+		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceCamera</string>
+		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
 	<array>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
 		<string>re6Zb+zwFKJNlkQTUeT+/w</string>
 		<string>hiHut/WR+B9Lx/vd0WyeNg</string>
 		<string>iyfxmLogGVIaH7aEgqwcIA</string>

```
### HomeWidgetSingleAccessoryIntent

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent`

```diff

 		<string>com.apple.MobileAsset.VoiceTriggerHSAssetsIPad</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>
-	<string>com.apple.Home.HomeWidget</string>
+	<string>com.apple.Home.HomeWidget.Interactive</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.Intent</string>

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.homeenergy</key>
+	<true/>
 	<key>com.apple.private.homekit.allow-secure-access</key>
 	<true/>
 	<key>com.apple.private.homekit.cameraclips</key>

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>com.apple.Home.group</string>
+	</array>
 	<key>com.apple.private.security.storage.Home</key>
 	<true/>
 	<key>com.apple.private.security.storage.HomeKit</key>

 		<string>com.apple.datamigrator</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.internal.studylogd</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>
+		<string>com.apple.linkd.registry</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mediasetupd.server</string>

 		<string>com.apple.Home.ControlCenter</string>
 		<string>com.apple.Home.group</string>
 		<string>com.apple.Home.wallpaper</string>
+		<string>com.apple.HomeEnergyUI</string>
 		<string>com.apple.ImageIO</string>
 		<string>com.apple.Maps</string>
 		<string>com.apple.Preferences</string>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.internal.studylogd</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>
 		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.linkd.registry</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.pearld</string>

```

### 🆕 GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.Photos</string>
	</array>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.appintents.attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.GenerativePlaygroundApp</string>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.person</string>
		<string>photos.face</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>peopleSubgraph</string>
		<string>inferenceFeaturesECR</string>
		<string>personEntityRelevanceRanking</string>
		<string>entitySimilarityFeatures</string>
	</array>
	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
	<true/>
	<key>com.apple.private.photos.allowlibraryupgrade</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.librarymanagement</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<false/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.GenerativePlayground</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
</dict>
</plist>

```

### 🆕 Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.GenerativePlaygroundApp</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.GenerativePlaygroundApp</string>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.Photos</string>
	</array>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.person</string>
		<string>photos.face</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>peopleSubgraph</string>
		<string>inferenceFeaturesECR</string>
		<string>personEntityRelevanceRanking</string>
		<string>entitySimilarityFeatures</string>
	</array>
	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
	<true/>
	<key>com.apple.private.photos.allowlibraryupgrade</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.librarymanagement</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.GenerativePlayground</string>
	</array>
	<key>com.apple.security.device.camera</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
	</array>
	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
	<array>
		<string>AppleNVMeEANUC</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```

### 🆕 GenerativePlaygroundMessagesAppExtension

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
	</array>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.messages.private.AllowConversationContextAccess</key>
	<false/>
	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.person</string>
		<string>photos.face</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>peopleSubgraph</string>
		<string>inferenceFeaturesECR</string>
		<string>personEntityRelevanceRanking</string>
		<string>entitySimilarityFeatures</string>
	</array>
	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
	<true/>
	<key>com.apple.private.photos.allowlibraryupgrade</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.librarymanagement</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.GenerativePlayground</string>
	</array>
	<key>com.apple.security.device.camera</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/AssetsV2/</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 		<string>com.apple.momentsd</string>
 		<string>com.apple.MomentsUIService</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.journal.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/MagnifierSupport.framework</string>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<string></string>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MapsShareETAFeedback</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>MapsShare.ETAFeedback</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.mediaexperience.silentmodenotifications.allow</key>
 	<true/>
 	<key>com.apple.private.mis.online_auth_agent</key>

```
### MobileCal

> `/private/var/staged_system_apps/MobileCal.app/MobileCal`

```diff

 	<true/>
 	<key>com.apple.private.remindd</key>
 	<dict>
+		<key>sync</key>
+		<true/>
 		<key>userInteractive</key>
 		<true/>
 	</dict>

 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.remindd.userInteractive</string>
+		<string>com.apple.realitysystemsupport.hid_server_backboard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.private.networkserviceproxy</key>
 	<true/>
+	<key>com.apple.private.parsec.default-client</key>
+	<string>com.apple.mobilemail</string>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.personas.propagate</key>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.mobilenotes</string>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	<array>
 		<string>/Media/PhotoData/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 		<string>/Library/Caches/com.apple.notes.autoincrement.lock</string>
 		<string>/Library/Caches/com.apple.notes.objectcreation.lock</string>
+		<string>/Library/CallServices/Recordings/</string>
+		<string>/Library/CallServices/Greetings/Recordings/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
 		<string>/Library/IntelligencePlatform/Artifacts/visualIdentifier/visualIdentifier.db</string>
 	</array>

```
### com.apple.mobilenotes.WidgetExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.mobilenotes</string>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

 		<string>com.apple.mobilenotes.HTMLConverter</string>
 		<string>com.apple.mobilenotes.NotesImporter</string>
 		<string>com.apple.xpc.amstreatmentstoreservice</string>
+		<string>com.apple.frontboard.systemappservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mobilenotes</string>
 	</array>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>508119322</string>
 	<key>platform-application</key>

```
### MobileTimer

> `/private/var/staged_system_apps/MobileTimer.app/MobileTimer`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
+		<string>/Library/Ringtones/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 		<string>com.apple.news.TodayFeedConfigDecoder</string>
 		<string>com.apple.newsd.analytics</string>
 		<string>com.apple.newsd.download</string>
+		<string>com.apple.newsd.live-activity</string>
 		<string>com.apple.newsd.today-feed</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.routined.internal</string>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<array>
 		<string>com.apple.MobileAsset.WalletMobileAssets</string>
 	</array>
+	<key>com.apple.private.associated-domains</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Wallet.Transaction</string>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.financed.service.bankconnect</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.softposreaderd</string>
 		<string>com.apple.passd.sharing-channel</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>

 	<true/>
 	<key>com.apple.sharing.Client</key>
 	<true/>
+	<key>com.apple.softposreaderd</key>
+	<true/>
 	<key>com.apple.softposreaderd.provision</key>
 	<true/>
 	<key>com.apple.springboard.allowIconVisibilityChanges</key>

```

### 🆕 PassbookLockedWidgetsExtension

> `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Passbook.PassbookWidgets</string>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.chrono.open-urls-direct</key>
	<true/>
	<key>com.apple.developer.default-data-protection</key>
	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
	<key>com.apple.finance.private</key>
	<true/>
	<key>com.apple.finance.store</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.peerpayment.all-access</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/Frameworks/FinanceKitUI.framework</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.financed.service.coredatastore</string>
		<string>com.apple.financed.service.store</string>
		<string>com.apple.passd.account</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.passd.library</string>
		<string>com.apple.passd.peer-payment</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
</dict>
</plist>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.cdp.daemon</string>
 	</array>
 	<key>com.apple.security.files.user-selected.read-write</key>
 	<true/>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.private.cfnetwork.har-capture-amp</key>
 	<true/>
+	<key>com.apple.private.coreaudio.viewInterruptorName.allow</key>
+	<true/>
 	<key>com.apple.private.coreservices.alwaysEligibleEvenWhenInBackground</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### WeatherWidget

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CoreRoutine.LocationOfInterest</key>
+	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.chronoservices</string>
+		<string>com.apple.routined.registration</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### modelmanagerdump

> `/usr/bin/modelmanagerdump`

```diff

 	<true/>
 	<key>com.apple.modelmanager.test</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.forceDomain</key>
+	<true/>
+	<key>com.apple.private.eligibilityd.resetDomain</key>
+	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.security.no-container</key>

```
### taskinfo

> `/usr/bin/taskinfo`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.coalition-policy</key>
+	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
-	<key>com.apple.system-task-ports.inspect</key>
+	<key>com.apple.system-task-ports.read</key>
 	<true/>
 </dict>
 </plist>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ak.appleidpasskey.xpc</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
+		<string>com.apple.UNCUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### MobileStorageMounter

> `/usr/libexec/MobileStorageMounter`

```diff

 	<array>
 		<string>systemgroup.com.apple.mobilestorageproxy</string>
 	</array>
+	<key>com.apple.security.ts.nvram-read</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>mobile_storage_mounter</string>

```

### 🆕 NRDUpdated

> `/usr/libexec/NRDUpdated`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobile.NRDUpdated</string>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>PURGE_ENTITLEMENT</string>
		<string>CLIENT_ENTITLEMENT</string>
		<string>PURGEABLE_ENTITLEMENT</string>
		<string>PURGE_SPECIAL_CASE_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.amfi.can-load-trust-cache</key>
	<true/>
	<key>com.apple.private.apfs.allocate_contig</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.RecoveryOSUpdateBrain</string>
	</array>
	<key>com.apple.private.domain-extension</key>
	<true/>
	<key>com.apple.private.pmap.load-trust-cache</key>
	<array>
		<string>global.ota-update-brain</string>
	</array>
	<key>com.apple.private.security.bootpolicy</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.cache_delete</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleMobileFileIntegrityUserClient</string>
	</array>
</dict>
</plist>

```
### aonsensed

> `/usr/libexec/aonsensed`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.private.corewifi-xpc</string>
 	</array>
 </dict>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<true/>
 	<key>com.apple.keystore.lockassertion</key>
 	<true/>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
+	<key>com.apple.mkb.usersession.keybagopaquedata</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ak.auth.xpc</string>

```
### appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.appleidsetup.notifications</string>
-		<string>com.apple.Preferences</string>
 	</array>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>

```
### appprotectiond

> `/usr/libexec/appprotectiond`

```diff

 <dict>
 	<key>com.apple.dmd.operation.fetch-apps</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.BackgroundUI</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerAuditToken</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage.BiometricSuccessAge</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.PasscodeSuccessAge</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.UI</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>

```
### asd

> `/usr/libexec/asd`

```diff

 		<string>Media/</string>
 		<string>Library/Finance/</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>Library/Caches/com.apple.asd/</string>
-		<string>Library/HTTPStorages/com.apple.asd/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appprotectiond.read</string>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>production</string>
+	<key>com.apple.AudioAccessoryServices</key>
+	<true/>
 	<key>com.apple.BluetoothUIService</key>
 	<true/>
 	<key>com.apple.CompanionLink</key>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	</array>
 	<key>com.apple.private.ppm.client</key>
 	<true/>
+	<key>com.apple.private.sysdiagnose</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceListenEvent</string>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.spindump.generatespindump</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Audio/Tunings/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/Library/Caches/CoreMotion/CoreMotion.log</string>
 		<string>/Library/VirtualCaptureCard/</string>
 		<string>/Library/com.apple.imagecapture/</string>
+		<string>/Library/Logs/CrashReporter/cameracaptured/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.realitysimulation.host</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.ReplayKitAngel.mach</string>
+		<string>com.apple.audio.AudioQueueServer</string>
+		<string>com.apple.audio.AudioSession</string>
+		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.managedassetsd</string>
 		<string>com.apple.surfboard.scenesessionservice</string>
 		<string>com.apple.TapToRadarKit.service</string>

```
### carkitd

> `/usr/libexec/carkitd`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpoint.xpc</key>
 	<true/>
+	<key>com.apple.locationd.accessory_location</key>
+	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### continuitycaptured

> `/usr/libexec/continuitycaptured`

```diff

 	<true/>
 	<key>com.apple.RemoteDisplay.SessionState</key>
 	<true/>
-	<key>com.apple.backlight.backlightaccess</key>
-	<true/>
-	<key>com.apple.backlight.performrequest</key>
-	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-read</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-read-xpc</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 	<string>com.apple.deviceaccessd</string>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.companionappd.connect.allow</key>
+	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

```
### dprivacyd

> `/usr/libexec/dprivacyd`

```diff

 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.familycircle.agent</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.DPSubmissionService</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### finish_demo_restore

> `/usr/libexec/finish_demo_restore`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.security.storage.demo_backup</key>
 	<true/>
 </dict>

```
### fskitd

> `/usr/libexec/fskitd`

```diff

 	<true/>
 	<key>com.apple.private.fskit.module-runner</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-group</key>
+	<array>
+		<string>group.com.apple.fskit.settings</string>
+	</array>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.fskit.settings</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/LiveFiles/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fskit.fskit_agent</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>AppleLIFSUserClient</string>
 </dict>

```
### hangreporter

> `/usr/libexec/hangreporter`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>

 			<key>Streams</key>
 			<array>
 				<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+				<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 			</array>
 		</dict>
 	</dict>

 	<array>
 		<integer>0</integer>
 	</array>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 </dict>
 </plist>
 

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Location</key>
 	<true/>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.security.storage.containers</key>
 	<true/>
 	<key>com.apple.private.security.storage.pipelined</key>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	</array>
 	<key>com.apple.managedconfiguration.profiled.usercompliance</key>
 	<true/>
+	<key>com.apple.managedconfiguration.teslad-access</key>
+	<true/>
 	<key>com.apple.mkb.usersession.delete</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

```
### milod

> `/usr/libexec/milod`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.TapToRadarKit.service</string>
+		<string>com.apple.spaceattributiond</string>
 	</array>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>com.apple.wifi.priority.internal</key>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.FM.CodeLM</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.modelmanagerd</string>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.feedbackd.client-forms</key>
+	<array>
+		<string>:framework-journalingsuggestions-onboarding</string>
+		<string>:framework-journalingsuggestions-customize</string>
+		<string>:framework-journalingsuggestions-settings</string>
+		<string>:framework-journalingsuggestions-blank</string>
+	</array>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
 	<key>com.apple.keystore.allow.background-processing-assertions</key>

 	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>

 		<string>lifeEventSubgraph</string>
 		<string>entityTagging</string>
 		<string>visualIdentifier</string>
+		<string>hasAssociationSubgraph</string>
 	</array>
 	<key>com.apple.private.interstellar.data-access</key>
 	<array>

 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.private.intelligenceplatform.views.read-only</string>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.extensionkitservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

 	<array>
 		<string>com.apple.iCloud.FollowUp</string>
 	</array>
+	<key>com.apple.privatecloudcompute.serverEnvironment</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### pmudiagnose

> `/usr/libexec/pmudiagnose/pmudiagnose`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.driver.SPMI.device.user-access</key>
+	<key>com.apple.driver.SPMI.user-access</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
-		<string>AppleARMSPMIUserClient</string>
+		<string>AppleARMSPMIDeviceUserClient</string>
 		<string>AppleSMCClient</string>
 		<string>ApplePTDUserClient</string>
 	</array>

```
### powerexperienced

> `/usr/libexec/powerexperienced`

```diff

 	<true/>
 	<key>com.apple.osintelligence.charging</key>
 	<true/>
+	<key>com.apple.private.applesmc.user-access</key>
+	<true/>
 	<key>com.apple.private.clpc.policy</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleCLPCUserClient</string>
+		<string>AppleSMCClient</string>
 	</array>
 </dict>
 </plist>

```
### ptpd

> `/usr/libexec/ptpd`

```diff

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.BackgroundUI</key>
+	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.lockdown.is-host-trusted</key>
 	<array>
 		<string>com.apple.ptp</string>

```
### remindd

> `/usr/libexec/remindd`

```diff

 	<string></string>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.reminders</string>
+	<key>com.apple.feedbackd.client-forms</key>
+	<array>
+		<string>framework-reminders-grocerylist</string>
+	</array>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.feedbackd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### routined

> `/usr/libexec/routined`

```diff

 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.safetyalerts</string>
-		<string>com.apple.biome.access.user</string>
 		<string>com.apple.kvsd</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.biome.PublicStreamAccessService</string>
-		<string>com.apple.chrono.widgetcenterconnection</string>
-		<string>com.apple.commcenter.coretelephony.xpc</string>
-		<string>com.apple.findmy.findmybeaconingd.push</string>
-		<string>com.apple.findmy.findmylocate.friendshipservice</string>
-		<string>com.apple.findmy.findmylocate.settings</string>
-		<string>com.apple.geod</string>
-		<string>com.apple.routined.registration</string>
-		<string>com.apple.usernotifications.listener</string>
-		<string>com.apple.usernotifications.usernotificationservice</string>
-		<string>com.apple.cmfsyncagent.embedded.auth</string>
-		<string>com.apple.accessories.connection-info-server</string>
-	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-container</key>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.timed</key>
 	<true/>
 	<key>com.apple.wirelessproxd-object-discovery</key>

```
### securityd

> `/usr/libexec/securityd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.securityd</string>
 	<key>com.apple.aps-environment</key>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>allow-softwareupdated</key>
+	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.seserviced</string>
 	<key>com.apple.BTServer.allowLEConnectionHandleQuery</key>

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.developer.homekit</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.credential-state-access</key>
 	<true/>
+	<key>com.apple.private.homekit</key>
+	<true/>
+	<key>com.apple.private.homekit.home-location</key>
+	<true/>
+	<key>com.apple.private.homekit.location</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.keysharing</string>

 	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceWillow</string>
+	</array>
 	<key>com.apple.private.tcc.manager</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<array>
 		<string>read</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.private.voicememod.client</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.reboot</key>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 				<key>App.InstalledApp</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomCarName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomCarProfileName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomContactGroupName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomContactName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomMediaAudiobookAuthorName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomMediaAudiobookTitle</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomMediaMusicArtistName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomMediaPlaylistTitle</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomMediaShowTitle</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomNotebookItemGroupName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomNotebookItemTitle</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomPaymentsAccountNickname</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomPaymentsOrganizationName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomPhotoAlbumName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomPhotoTag</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomVoiceCommandName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.CustomWorkoutActivityName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.GlobalMediaAudiobookAuthor</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.GlobalMediaAudiobookTitle</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.GlobalMediaMusicArtistName</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.GlobalMediaPlaylistTitle</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.IntentVocabulary.GlobalMediaShowTitle</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.Intents.IndexedEntity</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.Intents.IndexedEnum</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.Shortcut.Entity</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>App.Shortcut.Phrase</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>Calendar.Event</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>CarPlay.RadioStation</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>Contacts.Contact</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>FindMy.Device</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>Fitness.Guest</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>Health.Medication</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>HomeKit.Home</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>Location.SignificantLocation</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>MediaLibrary.Media</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>Podcasts.Podcast</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>Siri.PrivateLearning.Contact</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>Siri.PrivateLearning.Media</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 				<key>UserAccount.Identity</key>
 				<dict>
 					<key>mode</key>
-					<string>read</string>
+					<string>read-only</string>
 				</dict>
 			</dict>
 		</dict>

 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.mobilecal</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

 	<true/>
 	<key>com.apple.pf.allow</key>
 	<true/>
+	<key>com.apple.private.fillmore.AccessoryInfo.modification</key>
+	<true/>
 	<key>com.apple.private.fillmore.prefix.modification</key>
 	<true/>
 	<key>com.apple.private.fillmore.service.add</key>

```
### swtransparencyd

> `/usr/libexec/swtransparencyd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.swtransparencyd</string>
+	<key>com.apple.private.cloudtelemetry</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>

 	<array>
 		<string>group.com.apple.swtransparency</string>
 	</array>
+	<key>com.apple.privatecloudcompute.serverEnvironment</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.swtransparency</string>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.coreaudio.CanRecordPastData</key>

```
### webinspectord

> `/usr/libexec/webinspectord`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.dt.remotepairing.metadataprovider</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.idle-timer-services</key>

```
### spindump

> `/usr/sbin/spindump`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>

 			<key>Streams</key>
 			<array>
 				<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+				<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 			</array>
 		</dict>
 	</dict>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
+	<key>com.apple.mDNSResponder.record-cache.local-record-info</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.pairunpairobliterate</key>

```
