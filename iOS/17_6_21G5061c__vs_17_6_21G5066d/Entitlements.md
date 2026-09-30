## 🔑 Entitlements

### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<array>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 	<array>
 		<string>com.apple.private.alloy.nameandphoto</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.private.alloy.biz</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>

 		<string>com.apple.camera</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.handwriting</string>
 		<string>com.apple.MobileSMS.CKDNDList</string>
 		<string>com.apple.MobileSMSPreview</string>

```
### MessagesAssistantExtension

> `/Applications/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension`

```diff

 	<array>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>

```
### MessagesNotificationExtension

> `/Applications/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<array>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>

```
### MessagesTranscriptExtension

> `/Applications/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<array>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.private.alloy.messagesquickswitch</string>
 		<string>com.apple.private.alloy.sms</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.private.alloy.sms.watch</string>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.private.alloy.messagenotification</string>

 		<string>com.apple.private.alloy.sms.watch</string>
 		<string>com.apple.private.alloy.sms</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.private.alloy.messagenotification</string>
 		<string>com.apple.private.alloy.gelato</string>

 	<key>com.apple.private.ids.registration</key>
 	<array>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.ess</string>
 		<string>com.apple.private.ac</string>
 	</array>

```
### mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 	<true/>
 	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
 	<true/>
+	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
+	<true/>
+	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
+	<true/>
 	<key>com.apple.private.applesepmanager.allow</key>
 	<true/>
 	<key>com.apple.private.corerepair.fdr</key>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<array>
 		<string>StoreDemoMode</string>
 	</array>
+	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
+	<true/>
+	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.wifid</string>
 	<key>com.apple.private.biome.read-write</key>

 	<true/>
 	<key>com.apple.private.mobilerepair.xpc</key>
 	<true/>
+	<key>com.apple.private.mobilestoredemo.enabledemo</key>
+	<array>
+		<string>Managed</string>
+	</array>
 	<key>com.apple.private.network-performance-tester</key>
 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>

 	<true/>
 	<key>com.apple.private.ppm.client</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.skywalk.observe-all</key>
 	<true/>
 	<key>com.apple.private.skywalk.observe-stats</key>

```
