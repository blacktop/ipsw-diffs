## 🔑 Entitlements

### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
+	<key>com.apple.runningboard.photosretailexperience</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>group.com.apple.coreservices.useractivityd</string>
-	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceUbiquity</string>

 	</array>
 	<key>com.apple.runningboard.assertions.useractivityd</key>
 	<true/>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.coreservices.useractivityd</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<true/>
 	<key>com.apple.springboard.externaldisplay.displayArrangements</key>
 	<true/>
+	<key>com.apple.springboard.home-screen-configuration</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.private.mobilerepair.xpc</key>
 	<true/>
-	<key>com.apple.private.mobilestoredemo.enabledemo</key>
-	<array>
-		<string>Managed</string>
-	</array>
 	<key>com.apple.private.network-performance-tester</key>
 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>

```
