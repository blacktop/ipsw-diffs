## 🔑 Entitlements

### AppDistributionLaunchAngel

> `/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel`

```diff

 	<true/>
 	<key>com.apple.payment.card-on-file</key>
 	<true/>
+	<key>com.apple.payment.externalized-context</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### CredentialSharingUIViewService

> `/Applications/CredentialSharingUIViewService.app/CredentialSharingUIViewService`

```diff

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.security.storage.coreduet_knowledge_store</key>

```

### 🆕 FMDCFUTheftAndLossReminderExtension

> `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/FMDCFUTheftAndLossReminderExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
	<true/>
	<key>com.apple.icloud.findmydeviced.access</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.icloud.findmydeviced</string>
	</array>
</dict>
</plist>

```
### FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

 	<array>
 		<string>com.apple.nanoprefsync</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.icloud.findmydevice.managed</string>
+	</array>
 </dict>
 </plist>
 

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	<true/>
 	<key>com.apple.private.mobile.releasevalidation.tests</key>
 	<true/>
+	<key>com.apple.private.mobileinboxupdater.xpc</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.springboard.blockableservices</string>
+		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.surfboard.scenesessionservice</string>
 		<string>com.apple.surfboard.applicationservice</string>

```
