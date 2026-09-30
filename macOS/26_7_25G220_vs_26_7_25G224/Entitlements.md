## 🔑 Entitlements

### filesystem


### 🆕 SpotlightPreferenceExtension

> `/System/Library/ExtensionKit/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.fileprovider.extension-host</key>
	<true/>
	<key>com.apple.fileprovider.fetch-url</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.spotlight.preferences</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.files.user-selected.read-write</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.Spotlight.Preferences</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Spotlight</string>
	</array>
	<key>com.apple.spotlight.entitledattributes</key>
	<true/>
</dict>
</plist>

```
### mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/Versions/A/XPCServices/mscamerad-xpc.xpc/Contents/MacOS/mscamerad-xpc`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>2</integer>
+	<integer>3</integer>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>

```
### mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/Versions/Current/XPCServices/mscamerad-xpc.xpc/Contents/MacOS/mscamerad-xpc`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>2</integer>
+	<integer>3</integer>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>

```

### 🆕 libxml_ruby.bundle

> `/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/gems/2.6.0/gems/libxml-ruby-3.2.1/lib/libxml_ruby.bundle`

- No entitlements *(yet)*

### 🆕 nokogiri.bundle

> `/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/gems/2.6.0/gems/nokogiri-1.13.8/ext/nokogiri/nokogiri.bundle`

- No entitlements *(yet)*

### 🆕 libxml_ruby.bundle

> `/System/Library/Frameworks/Ruby.framework/Versions/Current/usr/lib/ruby/gems/2.6.0/gems/libxml-ruby-3.2.1/lib/libxml_ruby.bundle`

- No entitlements *(yet)*

### 🆕 nokogiri.bundle

> `/System/Library/Frameworks/Ruby.framework/Versions/Current/usr/lib/ruby/gems/2.6.0/gems/nokogiri-1.13.8/ext/nokogiri/nokogiri.bundle`

- No entitlements *(yet)*

### 🆕 test

> `/bin/test`

- No entitlements *(yet)*

### 🆕 sha224

> `/sbin/sha224`

- No entitlements *(yet)*

### 🆕 b64encode

> `/usr/bin/b64encode`

- No entitlements *(yet)*

### 🆕 od

> `/usr/bin/od`

- No entitlements *(yet)*

### 🆕 parl5.34

> `/usr/bin/parl5.34`

- No entitlements *(yet)*

### 🆕 w

> `/usr/bin/w`

- No entitlements *(yet)*
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
-	<key>com.apple.hid.system.fast-path-motion-event-privileged</key>
-	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.locationd.Proximity.TagManagement</key>

 	<true/>
 	<key>com.apple.locationd.inertialodometry</key>
 	<true/>
-	<key>com.apple.locationd.motion_alarms-system-client</key>
-	<true/>
 	<key>com.apple.locationd.slv_configurer</key>
 	<true/>
 	<key>com.apple.locationd.spectator</key>

 	<true/>
 	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>
 	<true/>
-	<key>com.apple.private.breadboard.privacy.read</key>
-	<array>
-		<string>passive-camera</string>
-	</array>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.corewifi.countrycode</key>

 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
-	<key>com.apple.private.hid.client.motion-event-privileged</key>
-	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>
 	<true/>
 	<key>com.apple.private.mediasafetynet.exception.nearbyprecisionfinding</key>

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.cvhwa.xpc</string>
 		<string>com.apple.mediasafetynet.exceptions.cam</string>
-		<string>com.apple.breadboardservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```


### AppOS

### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

```


