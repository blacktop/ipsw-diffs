## 🔑 Entitlements

### filesystem

### CheckerBoard

> `/Applications/CheckerBoard.app/CheckerBoard`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.system-layers</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.arkit</key>
 	<true/>
 	<key>com.apple.arkit.service.appClipCode</key>

 	<true/>
 	<key>com.apple.private.corewifi.countrycode</key>
 	<true/>
-	<key>com.apple.private.diagnosticscheckupd.launch</key>
-	<true/>
 	<key>com.apple.private.exclaves.indicator_min_on_time</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>

 	<true/>
 	<key>com.apple.runningboard.UIKitKeyboardManagement</key>
 	<true/>
-	<key>com.apple.runningboard.assertions.frontboard</key>
-	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
 	<key>com.apple.runningboard.primitiveattribute</key>

 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleSPUHIDDriverUserClient</string>
 		<string>IOSurfaceAcceleratorClient</string>
 		<string>AGXDeviceUserClient</string>
 		<string>AppleCredentialManagerUserClient</string>

 	</array>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
+	<key>com.apple.springboard.display-region-blanking</key>
+	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>
 	<true/>
 	<key>com.apple.systemstatus.domains</key>

```
### Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

```diff

 		<string>AppleH10CamInUserClient</string>
 		<string>AppleH9CamInUserClient</string>
 		<string>AppleH16CamInUserClient</string>
+		<string>AppleCameraUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.applecamerad</string>
 		<string>com.apple.appleh13camerad</string>
 		<string>com.apple.appleh16camerad</string>
+		<string>com.apple.cameraispd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 Diagnostic-6023

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6023.appex/Diagnostic-6023`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.private.applemesa.allow</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleBiometricServicesUserClient</string>
	</array>
</dict>
</plist>

```

### 🆕 Diagnostic-6024

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6024.appex/Diagnostic-6024`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.aop.hid-driver.user-client</key>
	<dict>
		<key>orientation_1</key>
		<dict>
			<key>send-command</key>
			<dict/>
		</dict>
	</dict>
	<key>com.apple.private.hid.client.event-filter</key>
	<true/>
	<key>com.apple.private.hid.client.event-monitor</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>com.apple.CoreMotion</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleSPUHIDDriverUserClient</string>
	</array>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
</dict>
</plist>

```

### 🆕 Diagnostic-6025

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6025.appex/Diagnostic-6025`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.private.mobilerepair.shipmode</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mobilerepair.shipmode</string>
	</array>
</dict>
</plist>

```
### SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
+	<key>com.apple.private.iokit.battery-shipping-charge-limit</key>
+	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>

```
### ServicesPaymentAngel

> `/Applications/ServicesPaymentAngel.app/ServicesPaymentAngel`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.recovery</key>
+	<true/>
+	<key>com.apple.cdp.recoverykey</key>
+	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.telemetry</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
+	<key>com.apple.cdp.walrus.pcskeys</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.keystore.device</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.mkb.usersession.keybagopaquedata</key>
+	<true/>
 	<key>com.apple.payment.externalized-context</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.runningboard.assertions.angeltarget</key>

 		<string>com.apple.PassbookUISceneService.remote-ui</string>
 		<string>com.apple.ServicesPaymentAngel</string>
 		<string>com.apple.TapToRadarKit.service</string>
+		<string>com.apple.aa.identity.xpc</string>
+		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.hsa-authentication-server</string>
+		<string>com.apple.icloud.findmydeviced</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.jetpackassetd.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.springboard.biometricUnlockSuppression</key>

```

### 🆕 t8150.RELEASE.restore.stripped.sharedcache

> `/System/ExclaveCore/usr/share/exclavecore_sharedcache/t8150.RELEASE.restore.stripped.sharedcache`

- No entitlements *(yet)*

### 🆕 t8150.RELEASE.stripped.sharedcache

> `/System/ExclaveCore/usr/share/exclavecore_sharedcache/t8150.RELEASE.stripped.sharedcache`

- No entitlements *(yet)*
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.accessibility.motiontrackingd</string>
 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
+		<string>com.apple.relevanced.AudioUnderstanding</string>
 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.DeviceConfigurationAgent.consumer</string>

```

### 🆕 MobileDevices-0001

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001`

- No entitlements *(yet)*

### 🆕 MobileDevices-0003

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003`

- No entitlements *(yet)*

### 🆕 AMSNearFieldExtension

> `/System/Library/ExtensionKit/Extensions/AMSNearFieldExtension.appex/AMSNearFieldExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>409835401</string>
	<key>application-identifier</key>
	<string>com.apple.AppleMediaServicesUI.AMSNearFieldExtension</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.ak.auth.xpc</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.AppleMediaServicesUI.AMSNearFieldExtension</string>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.internal.nfc.allow.backgrounded.session</key>
	<true/>
	<key>com.apple.internal.seserviced.ptattestation</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled-access</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.nfcd.assertion.handover</key>
	<true/>
	<key>com.apple.nfcd.assertion.tagreading</key>
	<true/>
	<key>com.apple.nfcd.background.tag.reading.extension.urls</key>
	<array>
		<string>https://giftcard.apple.com</string>
		<string>https://gc.apple.com</string>
	</array>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.nfcd.session.reader.internal</key>
	<true/>
	<key>com.apple.nfcd.session.se</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.payment.card-on-file</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Install</string>
		<string>Queue</string>
		<string>Library</string>
		<string>Purchase</string>
	</array>
	<key>com.apple.private.biometrickit.allow-connect</key>
	<true/>
	<key>com.apple.private.biometrickit.allow-default</key>
	<true/>
	<key>com.apple.private.fairplay.FPDI</key>
	<dict>
		<key>capabilities</key>
		<array>
			<integer>4014732562</integer>
		</array>
		<key>client-identifier</key>
		<string>com.apple.AppleMediaServicesUI.AMSNearFieldExtension</string>
	</dict>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.xpc.amstoold</string>
		<string>com.apple.fairplaydeviceidentityd</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.seserviced</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.passd.account</string>
		<string>com.apple.passd.library</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.mobile.keybagd.xpc</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.seserviced.key</key>
	<true/>
	<key>com.apple.seserviced.kmlXpcService</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```

### 🆕 NTKHermes2026FaceBundle

> `/System/Library/NanoTimeKit/FaceBundles/NTKHermes2026FaceBundle.bundle/NTKHermes2026FaceBundle`

- No entitlements *(yet)*

### 🆕 NTKHero27FaceBundle

> `/System/Library/NanoTimeKit/FaceBundles/NTKHero27FaceBundle.bundle/NTKHero27FaceBundle`

- No entitlements *(yet)*
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.translationd</string>
 		<string>com.apple.AudioAccessoryServices</string>
+		<string>com.apple.relevanced.AudioUnderstanding</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.chronoservices</string>
 	</array>

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
 	<key>com.apple.facetimed</key>

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
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.default-app.phone</string>
 	</array>
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
### nfcd

> `/usr/libexec/nfcd`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/usr/standalone/firmware/nfrestore/firmware/fw-hashes/SN450V-hashes.plist</string>
+		<string>/usr/standalone/firmware/nfrestore/firmware/fury-fw-hashes/PN800V-hashes.plist</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleBasebandUserClient</string>
 		<string>ApplePPMUserClient</string>
-		<string>AppleSMCSensorDispatcherUserClient</string>
 		<string>RootDomainUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>com.apple.stockholm.services.NFRestoreService</string>
 		<string>com.apple.stockholm.services.NFLocationService</string>
 		<string>com.apple.stockholm.services.NFRadioPowerSwitch</string>
+		<string>com.apple.stockholm.services.NFReportingService</string>
 		<string>com.apple.stockholm.services.NFUIService</string>
 		<string>com.apple.stockholm.services.NFTagProcessorService</string>
 		<string>com.apple.stockholm.services.NFStorageServer</string>
 		<string>com.apple.NFCUISceneService.remote-ui</string>
 		<string>com.apple.seserviced.session</string>
+		<string>com.apple.timed.xpc</string>
+		<string>com.apple.seserviced.presentment-authorization</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
+	<key>com.apple.seserviced.presentment-authorization</key>
+	<true/>
 	<key>com.apple.seserviced.session.acwg</key>
 	<true/>
 	<key>com.apple.seserviced.session.dck</key>

 	<true/>
 	<key>com.apple.sts.xpcservice.client</key>
 	<true/>
+	<key>com.apple.timed</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.applesse</string>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.announced.client</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

```


