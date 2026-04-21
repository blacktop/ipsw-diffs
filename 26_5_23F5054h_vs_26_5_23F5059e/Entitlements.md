## 🔑 Entitlements

### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Install</string>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

```
### axassetsd

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sirittsd</string>
 		<string>com.apple.voicebanking.services</string>
 		<string>com.apple.voicebanking.store</string>
 		<string>com.apple.siri.uaf.subscription.service</string>

```
### appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/appleaccounttransparencyd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.appleaccount.transparency</string>
-	</array>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.ts.daemon-container</key>
+	<true/>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.appleaccounttransparencyd</string>
 	<key>com.apple.transparencyd.aet</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### cdpd

> `/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd`

```diff

 	<true/>
 	<key>com.apple.securebackupd.access</key>
 	<true/>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.appleaccount.transparency</string>
-	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<array/>
 	<key>com.apple.developer.auto-elect-plugin</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.fairplay-streaming</key>

 	<true/>
 	<key>com.apple.developer.in-app-payments</key>
 	<array/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>INTERNAL.com.apple.Health</string>
 	<key>com.apple.developer.usernotifications.critical-alerts</key>
 	<true/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<array>
 		<string>com.apple.weather.internal</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.ap.config</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.AdPlatforms</string>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.familycircle.agent</key>
+	<true/>
 	<key>com.apple.features.all-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.BrowserEngineKit.Intermediary</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.securityd</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

```
### companiond

> `/usr/libexec/companiond`

```diff

 		<string>Library/Application Support/com.apple.DistributedTimers/</string>
 		<string>Library/Caches/com.apple.companiond/</string>
 		<string>Library/Caches/com.apple.HomeKit/com.apple.companiond/</string>
+		<string>Library/com.apple.AppleMediaServices/</string>
 		<string>Library/HTTPStorages/com.apple.companiond/</string>
 		<string>Library/Logs/com.apple.StoreServices/HTTPArchives/</string>
 	</array>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.symptom_analytics.query</key>
+	<true/>
+	<key>com.apple.symptoms.NetworkOfInterest</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-call-capabilities</string>

```
### gamed

> `/usr/libexec/gamed`

```diff

 		<string>com.apple.cloudd</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.iconservices</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>

```
### remindd

> `/usr/libexec/remindd`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
-	<key>com.apple.security.script-restrictions</key>
-	<true/>
 	<key>com.apple.security.ts.application-group-support</key>
 	<true/>
 	<key>com.apple.security.ts.asset-access</key>

```
### mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

 	<true/>
 	<key>com.apple.private.necp.policies</key>
 	<true/>
+	<key>com.apple.private.nehelper.privileged</key>
+	<true/>
 	<key>com.apple.private.network.awdl.restricted</key>
 	<true/>
 	<key>com.apple.private.network.delegation-whitelist</key>

```
