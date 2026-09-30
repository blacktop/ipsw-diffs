## 🔑 Entitlements

### filesystem


### 🆕 FaceTimeMacHelper

> `/System/Applications/Phone.app/Contents/PlugIns/FaceTimeMacHelper.bundle/Contents/MacOS/FaceTimeMacHelper`

- No entitlements *(yet)*

### 🆕 RemotePeoplePicker

> `/System/Applications/Phone.app/Contents/PlugIns/RemotePeoplePicker.appex/Contents/MacOS/RemotePeoplePicker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.people</key>
	<true/>
	<key>com.apple.coreduetd.people.user</key>
	<true/>
	<key>com.apple.private.appleevents.allowedtosend</key>
	<dict>
		<key>com.apple.private.appleevents.allowed.aevt.optc</key>
		<true/>
	</dict>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.security.storage.CallHistory</key>
	<true/>
	<key>com.apple.private.suggestions</key>
	<true/>
	<key>com.apple.private.suggestions.contacts</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.personal-information.addressbook</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.coreduetd.people</string>
		<string>com.apple.coreduetd.people.user</string>
		<string>com.apple.duetknowledged.activity</string>
		<string>com.apple.suggestd.suggestionmanager</string>
		<string>com.apple.suggestd.contacts</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
	</array>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>access-calls</string>
		<string>modify-calls</string>
		<string>access-call-capabilities</string>
		<string>modify-call-capabilities</string>
		<string>access-call-providers</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```
### usbaudiod

> `/System/Library/Audio/Plug-Ins/usbaudio.bundle/Contents/MacOS/usbaudiod`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.audio.driver.extrinsic.registration</key>
+	<true/>
 	<key>com.apple.private.kernel.work-interval</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```

### 🆕 libxml_ruby.bundle

> `/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/gems/2.6.0/gems/libxml-ruby-3.2.1/ext/libxml/libxml_ruby.bundle`

- No entitlements *(yet)*

### 🆕 libxml_ruby.bundle

> `/System/Library/Frameworks/Ruby.framework/Versions/Current/usr/lib/ruby/gems/2.6.0/gems/libxml-ruby-3.2.1/ext/libxml/libxml_ruby.bundle`

- No entitlements *(yet)*

### 🆕 md5sum

> `/sbin/md5sum`

- No entitlements *(yet)*

### 🆕 atrm

> `/usr/bin/atrm`

- No entitlements *(yet)*

### 🆕 fgrep

> `/usr/bin/fgrep`

- No entitlements *(yet)*


