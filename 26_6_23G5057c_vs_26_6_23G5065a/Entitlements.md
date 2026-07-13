## 🔑 Entitlements

### filesystem

### AccessorySetupUI

> `/Applications/AccessorySetupUI.app/AccessorySetupUI`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
 	<key>com.apple.bluetooth.settings</key>

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ProductKitService</string>
 		<string>com.apple.SharingServices</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 		<string>analysis-history-read</string>
 		<string>analysis-history-write</string>
 	</array>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### WebContentRestrictionsUI

> `/Applications/WebContentRestrictionsUI.app/WebContentRestrictionsUI`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.springboard</string>

```
### PhotoPicker

> `/System/Library/ExtensionKit/Extensions/PhotoPicker.appex/PhotoPicker`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+		<string>com.apple.communicationSafetySettings</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.photos.picker</string>
 		<string>com.apple.restrictionspassword</string>
 		<string>com.apple.springboard</string>
 	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
-	<array>
-		<string>com.apple.communicationSafetySettings</string>
-	</array>
 	<key>com.apple.sensitivecontentanalysis.service</key>
 	<array>
 		<string>photos</string>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/PhotosPicker`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.communicationSafetySettings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.contacts.provider-host</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 		<string>com.apple.assistant.backedup</string>
 		<string>HomeKit</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-write</key>
+	<array>
+		<string>kern.memorystatus_vm_pressure_send</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### STExtractionService.privileged

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/XPCServices/STExtractionService.privileged.xpc/STExtractionService.privileged`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobilegestalt.xpc</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.CoreTelephony.CommCenterHelper.allow</key>
 	<true/>
+	<key>com.apple.DeviceAccess.private</key>
+	<true/>
 	<key>com.apple.FTLivePhotoService</key>
 	<array>
 		<string>modify-moments</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.DeviceAccess.xpc</string>
 		<string>com.apple.accessibility.voices</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>

```
### matd

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/matd`

```diff

 	<array>
 		<string>preferences.plist</string>
 	</array>
+	<key>com.apple.USBCEntitlement</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleHPMARM</string>
+		<string>IOAccessoryManagerUserClient</string>
 		<string>IOUSBDeviceInterfaceUserClient</string>
 	</array>
 	<key>com.apple.wifi.manager-access</key>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.businessservicesd.businessmetadata</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

```
### PhotosReliveWidget

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget`

```diff

 		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
 		<string>com.apple.chronoservices</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+	</array>
 </dict>
 </plist>
 

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 		<key>value</key>
 		<string>/usr/libexec/cameracaptured</string>
 	</dict>
+	<key>com.apple.private.audio.client-audit-token-override</key>
+	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.controlcenter.service.moduleidentifiers</key>

```
### logd

> `/usr/libexec/logd`

```diff

 	<true/>
 	<key>com.apple.private.power.notifications</key>
 	<true/>
+	<key>com.apple.private.security.storage.LogdPreferencesCache</key>
+	<true/>
 	<key>com.apple.private.set-atm-diagnostic-flag</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.ios-system-session</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/secureconfig/</string>
+	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
 		<string>kern.exclaves_status</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	</array>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 	<key>com.apple.private.skywalk.observe-all</key>

```


### SystemOS

### com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>

```
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.sqlite.defensive</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/ExtensionKit/Extensions/WebContentEnhancedSecurityExtension.appex/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```


