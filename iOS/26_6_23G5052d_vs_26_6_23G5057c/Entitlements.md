## 🔑 Entitlements

### filesystem

### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.mobileslideshow</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.servicesintelligenced</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/Library/Caches/</string>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.coreidv.system-notifications.accounts</key>

```

### 🆕 Managed Background Assets Relay Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Relay Service.xpc/Managed Background Assets Relay Service`

- No entitlements *(yet)*
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.servicesintelligenced</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

```

### 🆕 SafariActionExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariActionExtension.appex/SafariActionExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
</dict>
</plist>

```

### 🆕 SafariShareExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariShareExtension.appex/SafariShareExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
</dict>
</plist>

```
### fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.vfs.authorized-access</key>
 	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>

```
### keybagd

> `/usr/libexec/keybagd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.wvek</key>
+	<true/>
 	<key>com.apple.keystore.config.bind_kek_to_kb</key>
 	<true/>
 	<key>com.apple.keystore.config.set.user_uuid</key>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.telemetry</key>
 	<true/>
 	<key>com.apple.cdp.utility</key>

```


