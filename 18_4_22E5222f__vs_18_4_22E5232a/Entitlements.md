## 🔑 Entitlements

### AppleIDSetupUIService

> `/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboard.systemappservices</key>

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.icloud.findmydeviced</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.appleidsetupd.repair.xpc</string>

 	<array>
 		<string>com.apple.AuthKit.AgeRangeSettingsCache</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.icloud.findmydevice.managed</string>
+		<string>systemgroup.com.apple.DeviceActivity</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 		<string>com.apple.facetimemessagestored.service</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.conference</string>
 		<string>com.apple.siri.activation.service</string>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.CarPlayApp.service</string>

```
### NewDeviceSetupUIService

> `/Applications/NewDeviceSetupUIService.app/NewDeviceSetupUIService`

```diff

 	<dict>
 		<key>MacSetup</key>
 		<dict>
+			<key>bleRSSIThresholdHint</key>
+			<integer>-45</integer>
 			<key>discoveryTypes</key>
 			<array>
 				<string>MacSetup</string>

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.set</key>
+	<array>
+		<string>Passcode</string>
+	</array>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.cdp.daemon</string>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<array>
 		<string>com.apple.CoreSuggestions</string>
 	</array>
+	<key>com.apple.private.usernotifications.settings</key>
+	<array>
+		<string>read</string>
+	</array>
 	<key>com.apple.private.xpc.domain-extension</key>
 	<true/>
 	<key>com.apple.privatefederatedlearning.allowed</key>

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.ciphermld</string>
+		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.Preferences</string>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.mobile.installd</string>
 		<string>com.apple.sysdiagnose.service.xpc</string>
+		<string>com.apple.cache_delete.public</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SiriAUSP

> `/System/Library/PrivateFrameworks/TextToSpeech.framework/PlugIns/SiriAUSP.appex/SiriAUSP`

```diff

 		<string>/tmp</string>
 		<string>/private/var/tmp</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/SiriTTS/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.audio.AudioConverterService</string>

 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Group Containers/group.com.apple.SiriTTS/</string>
+		<string>/Library/Caches/SiriTTS/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### TranslationUIService

> `/System/Library/PrivateFrameworks/TranslationUIServices.framework/PlugIns/TranslationUIService.appex/TranslationUIService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.neagent</key>
+	<false/>
+	<key>com.apple.private.nehelper.privileged</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.private.translation</string>

```

### 🆕 libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

- No entitlements *(yet)*

### 🆕 libffi-trampolines.dylib

> `/usr/lib/libffi-trampolines.dylib`

- No entitlements *(yet)*

### 🆕 libglInterpose.dylib

> `/usr/lib/libglInterpose.dylib`

- No entitlements *(yet)*

### 🆕 libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

- No entitlements *(yet)*

### 🆕 libobjc-trampolines.dylib

> `/usr/lib/libobjc-trampolines.dylib`

- No entitlements *(yet)*

### 🆕 libramrod.dylib

> `/usr/lib/libramrod.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.6.0.9.dylib

> `/usr/lib/libstdc++.6.0.9.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.6.dylib

> `/usr/lib/libstdc++.6.dylib`

- No entitlements *(yet)*

### 🆕 libstdc++.dylib

> `/usr/lib/libstdc++.dylib`

- No entitlements *(yet)*

### 🆕 BatteryAlgorithms

> `/usr/libexec/BatteryAlgorithms.framework/BatteryAlgorithms`

- No entitlements *(yet)*
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 	<string>com.apple.coreduetd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>PeopleSuggesterContactPriors</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Contacts.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>PeopleSuggester.ContactPrior</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>ShareSheetFeedback</key>
 		<dict>
 			<key>Streams</key>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 	<true/>
 	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
 	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.nearbyinteraction.background</key>

```
### routined

> `/usr/libexec/routined`

```diff

 	</array>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.connectbeforemigrationdidfinish</key>
+	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
 	<key>com.apple.aonsensed.xpc</key>

```
