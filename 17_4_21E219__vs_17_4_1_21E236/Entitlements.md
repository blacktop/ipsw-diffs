## 🔑 Entitlements

### SoftwareUpdateUIService

> `/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>application-identifier</key>
-	<string>com.apple.susuiservice</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>

 	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
-	<key>com.apple.private.mobiletimerd</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_SoftwareUpdateDocumentation/</string>

 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.softwareupdateservicesd</string>
 		<string>CAREServer</string>
-		<string>com.apple.MobileTimer.timerserver</string>
-		<string>com.apple.MobileTimer.alarmserver</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
