## 🔑 Entitlements

### filesystem

### Messages

> `/System/Applications/Messages.app/Contents/MacOS/Messages`

```diff

 SYS_recvfrom_nocancel
 SYS_recvmsg
 SYS_rename
+SYS_renameat
 SYS_renameatx_np
 SYS_rmdir
 SYS_sendmsg

```
### com.apple.DFRSystemExtra.ScreenLock

> `/System/Library/CoreServices/ControlStrip.app/Contents/XPCServices/com.apple.DFRSystemExtra.ScreenLock.xpc/Contents/MacOS/com.apple.DFRSystemExtra.ScreenLock`

```diff

 	<array>
 		<string>com.apple.system.screen-lock</string>
 	</array>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 </dict>
 </plist>
 

```
### loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
+	<key>com.apple.private.securityd.keychain-master-key-extraction</key>
+	<true/>
 	<key>com.apple.private.securityd.stash</key>
 	<true/>
 	<key>com.apple.private.sessionagent.sessionowner</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.sessionmanager</key>
 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>

```

### 🆕 AGXMetalG14

> `/System/Library/Extensions/AGXMetalG14.bundle/Contents/MacOS/AGXMetalG14`

- No entitlements *(yet)*

### 🆕 AGXMetalG18G

> `/System/Library/Extensions/AGXMetalG18G.bundle/Contents/MacOS/AGXMetalG18G`

- No entitlements *(yet)*
### WorkflowServiceRunner

> `/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/WorkflowServiceRunner.xpc/Contents/MacOS/WorkflowServiceRunner`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.responsibility.set-to-self.at-launch</key>
+	<true/>
+	<key>com.apple.private.tcc.allow-prompting</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
+</dict>
+</plist>
 

```
### WorkflowServiceRunner

> `/System/Library/Frameworks/AppKit.framework/Versions/Current/XPCServices/WorkflowServiceRunner.xpc/Contents/MacOS/WorkflowServiceRunner`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.responsibility.set-to-self.at-launch</key>
+	<true/>
+	<key>com.apple.private.tcc.allow-prompting</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
+</dict>
+</plist>
 

```
### MTPluginFormatReader

> `/System/Library/Frameworks/MediaToolbox.framework/Versions/A/XPCServices/MTPluginFormatReader.xpc/Contents/MacOS/MTPluginFormatReader`

```diff

 	<true/>
 	<key>com.apple.security.cs.disable-library-validation</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```
### MTPluginFormatReaderZonto

> `/System/Library/Frameworks/MediaToolbox.framework/Versions/A/XPCServices/MTPluginFormatReaderZonto.xpc/Contents/MacOS/MTPluginFormatReaderZonto`

```diff

 	<true/>
 	<key>com.apple.security.cs.disable-library-validation</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```
### MTPluginFormatReader

> `/System/Library/Frameworks/MediaToolbox.framework/Versions/Current/XPCServices/MTPluginFormatReader.xpc/Contents/MacOS/MTPluginFormatReader`

```diff

 	<true/>
 	<key>com.apple.security.cs.disable-library-validation</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```
### MTPluginFormatReaderZonto

> `/System/Library/Frameworks/MediaToolbox.framework/Versions/Current/XPCServices/MTPluginFormatReaderZonto.xpc/Contents/MacOS/MTPluginFormatReaderZonto`

```diff

 	<true/>
 	<key>com.apple.security.cs.disable-library-validation</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```

### 🆕 libxml_ruby.bundle

> `/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/gems/2.6.0/gems/libxml-ruby-3.2.1/ext/libxml/libxml_ruby.bundle`

- No entitlements *(yet)*

### 🆕 libxml_ruby.bundle

> `/System/Library/Frameworks/Ruby.framework/Versions/Current/usr/lib/ruby/gems/2.6.0/gems/libxml-ruby-3.2.1/ext/libxml/libxml_ruby.bundle`

- No entitlements *(yet)*
### VTDecoderXPCService

> `/System/Library/Frameworks/VideoToolbox.framework/Versions/A/XPCServices/VTDecoderXPCService.xpc/Contents/MacOS/VTDecoderXPCService`

```diff

 	<array>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```
### VTDecoderXPCServiceZonto

> `/System/Library/Frameworks/VideoToolbox.framework/Versions/A/XPCServices/VTDecoderXPCServiceZonto.xpc/Contents/MacOS/VTDecoderXPCServiceZonto`

```diff

 	<array>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```
### VTDecoderXPCService

> `/System/Library/Frameworks/VideoToolbox.framework/Versions/Current/XPCServices/VTDecoderXPCService.xpc/Contents/MacOS/VTDecoderXPCService`

```diff

 	<array>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```
### VTDecoderXPCServiceZonto

> `/System/Library/Frameworks/VideoToolbox.framework/Versions/Current/XPCServices/VTDecoderXPCServiceZonto.xpc/Contents/MacOS/VTDecoderXPCServiceZonto`

```diff

 	<array>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```

### 🆕 T1057HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/T1057HIDServicePlugin.plugin/Contents/MacOS/T1057HIDServicePlugin`

- No entitlements *(yet)*

### 🆕 T6502HIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/T6502HIDServicePlugin.plugin/Contents/MacOS/T6502HIDServicePlugin`

- No entitlements *(yet)*

### 🆕 kernel.release.t8110

> `/System/Library/Kernels/kernel.release.t8110`

- No entitlements *(yet)*

### 🆕 kernel.release.t8152

> `/System/Library/Kernels/kernel.release.t8152`

- No entitlements *(yet)*

### 🆕 kernel.release.t8160

> `/System/Library/Kernels/kernel.release.t8160`

- No entitlements *(yet)*
### AKAppSSOExtension_macOS

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension_macOS.appex/Contents/MacOS/AKAppSSOExtension_macOS`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.associated-domains</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

 	<array>
 		<string>com.apple.ak.authorizationservices.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.SharedWebCredentials</string>
 	</array>
 </dict>
 </plist>

```
### diskimages-helper

> `/System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/Resources/diskimages-helper`

```diff

 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
 	<integer>1</integer>
+	<key>com.apple.private.diskimages.helper</key>
+	<true/>
 	<key>com.apple.private.diskimages.kext.user-client-access</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### diskimages-helper

> `/System/Library/PrivateFrameworks/DiskImages.framework/Versions/Current/Resources/diskimages-helper`

```diff

 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
 	<integer>1</integer>
+	<key>com.apple.private.diskimages.helper</key>
+	<true/>
 	<key>com.apple.private.diskimages.kext.user-client-access</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 	</array>
 	<key>com.apple.private.tcc.manager</key>
 	<true/>
+	<key>com.apple.private.tcc.system-tccd-forwarder</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.tccd</string>

```

### 🆕 reboot

> `/sbin/reboot`

- No entitlements *(yet)*

### 🆕 sha1

> `/sbin/sha1`

- No entitlements *(yet)*

### 🆕 atq

> `/usr/bin/atq`

- No entitlements *(yet)*

### 🆕 bintrans

> `/usr/bin/bintrans`

- No entitlements *(yet)*

### 🆕 id

> `/usr/bin/id`

- No entitlements *(yet)*

### 🆕 parldyn5.34

> `/usr/bin/parldyn5.34`

- No entitlements *(yet)*
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.hid.system.fast-path-motion-event-privileged</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.locationd.Proximity.TagManagement</key>

 	<true/>
 	<key>com.apple.locationd.inertialodometry</key>
 	<true/>
+	<key>com.apple.locationd.motion_alarms-system-client</key>
+	<true/>
 	<key>com.apple.locationd.slv_configurer</key>
 	<true/>
 	<key>com.apple.locationd.spectator</key>

 	<true/>
 	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>
 	<true/>
+	<key>com.apple.private.breadboard.privacy.read</key>
+	<array>
+		<string>passive-camera</string>
+	</array>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.corewifi.countrycode</key>

 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
+	<key>com.apple.private.hid.client.motion-event-privileged</key>
+	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>
 	<true/>
 	<key>com.apple.private.mediasafetynet.exception.nearbyprecisionfinding</key>

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.cvhwa.xpc</string>
 		<string>com.apple.mediasafetynet.exceptions.cam</string>
+		<string>com.apple.breadboardservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### studentd

> `/usr/libexec/studentd`

```diff

 	<array>
 		<string>group.com.apple.studentd</string>
 	</array>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```


### SystemOS


### 🆕 SwiftUITracingSupport

> `/System/Library/PrivateFrameworks/SwiftUITracingSupport.framework/Versions/A/SwiftUITracingSupport`

- No entitlements *(yet)*


### AppOS

### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
-	<key>com.apple.private.network.socket-delegate</key>
-	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

```


