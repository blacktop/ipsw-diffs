## 🔑 Entitlements


### 🆕 Diagnostic-9012

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9012.appex/Diagnostic-9012`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.diagnosticmanager</key>
	<true/>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.DiagnosticsSupport.HardwareButtonAccess</key>
	<true/>
	<key>com.apple.private.AppleSecureRepair.allow</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.corerepair.xpc</key>
	<true/>
	<key>com.apple.private.hid.client.event-filter</key>
	<true/>
	<key>com.apple.private.hid.client.event-monitor</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleBiometricServicesUserClient</string>
		<string>AppleSecureRepairUserClient</string>
	</array>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
</dict>
</plist>

```

### 🆕 WeatherPoster

> `/Applications/WeatherPosterApp.app/Extensions/WeatherPoster.appex/WeatherPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.weather</string>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.locationd.prompt_from_background</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.storage.Weather</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.weather</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.countryd/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Weather/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.weather</string>
		<string>com.apple.weather.internal</string>
		<string>com.apple.weather.sensitive</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```

### 🆕 WeatherPosterApp

> `/Applications/WeatherPosterApp.app/WeatherPosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Posters.WeatherPosterApp</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/private/var/staged_system_apps/WeatherPosterApp.app/WeatherPosterApp</string>
	</dict>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.WritingToolsUIService</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.devicesharing.guest-user-mode-client</key>
 	<true/>
 	<key>com.apple.feedbackd.remote-evaluation</key>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ctkd.token-client</string>
+		<string>com.apple.amsprivateidentifiers</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.avatarsd</string>

```
### PasswordsDataMigration

> `/System/Library/ExtensionKit/Extensions/PasswordsDataMigration.appex/PasswordsDataMigration`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.private.MobileContainerManager.lookup</key>
+	<dict>
+		<key>appData</key>
+		<array>
+			<string>com.apple.Passwords</string>
+		</array>
+	</dict>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>

```
### wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.wirelessinsightsd</string>
+	<key>com.apple.symptom_analytics.query</key>
+	<true/>
+	<key>com.apple.symptoms.NetworkOfInterest</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```
### accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.AUDeveloperSettings</string>
 		<string>com.apple.ACMobileShim</string>
 		<string>com.apple.GEO</string>
 	</array>

```
### itunesstored

> `/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored`

```diff

 	</array>
 	<key>com.apple.frontboard.app-badge-value-access</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.ibooks.BLService.private</key>
 	<true/>
 	<key>com.apple.itunesstored.metrics</key>

```
### afcd

> `/usr/libexec/afcd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.private.MobileActivation</key>
+	<array>
+		<string>GetActivationState</string>
+		<string>RequestActivationState</string>
+	</array>
 	<key>com.apple.private.security.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 	<true/>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.secureelementservice</string>
 	<key>com.apple.seld.tsmmanager</key>
 	<true/>
 	<key>com.apple.seserviced.SESUIServiceApp.session</key>

```
### triald

> `/usr/libexec/triald`

```diff

 		<key>pluginData</key>
 		<true/>
 	</dict>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```
### triald_system

> `/usr/libexec/triald_system`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### cfprefsd

> `/usr/sbin/cfprefsd`

```diff

 <dict>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.security.storage.CoreRoutine</key>
 	<true/>
 	<key>com.apple.private.security.storage.preferences</key>

```
