## 🔑 Entitlements

### filesystem

### ScreenTimeWidgetExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.screentime-communication</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ScreenTimeAgent.settings</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
 		<string>com.apple.familycircle.agent</string>

```
### ScreenTimeWidgetIntentsExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.screentime-communication</key>

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ScreenTimeAgent.settings</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 </dict>
 </plist>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 		<string>background-activities</string>
 		<string>focus</string>
 	</array>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```
### MusicKitUI

> `/System/Library/CoreServices/MusicKitUI.app/MusicKitUI`

```diff

 	<array>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceMediaLibrary</string>
+	</array>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.accountsd</string>
 	<key>com.apple.private.keychain.allow-delete-internal-on-sign-out</key>
 	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 		<string>com.apple.engagementd</string>
 		<string>com.apple.OnDeviceStorage</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions-string</key>
+	<string>2</string>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

 	</array>
 	<key>com.apple.accessories.ACCBluetoothPairingService.access</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>
 	<true/>
 	<key>com.apple.backboardd.proximityStatusEvent</key>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.networkd_privileged</key>
+	<true/>
 	<key>com.apple.nowplaying.remote-media-host</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.musicd.client</key>
 	<true/>
+	<key>com.apple.private.necp.policies</key>
+	<true/>
+	<key>com.apple.private.nehelper.privileged</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.rtcreportingd</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.nehelper</string>
 		<string>com.apple.musicd</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.airplay.endpoint.xpc</string>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<string>com.apple.migrationd</string>
 	<key>com.apple.CallHistory.sync.allow</key>
 	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
 	<key>com.apple.USBCEntitlement</key>

```
### ScreenTimeFollowUpExtension

> `/System/Library/PrivateFrameworks/ScreenTimeUI.framework/PlugIns/ScreenTimeFollowUpExtension.appex/ScreenTimeFollowUpExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
+	<key>com.apple.private.contacts</key>
+	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
+	<key>com.apple.private.screen-time.persistence</key>
+	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.ScreenTime</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ScreenTimeAgent.private</string>
+		<string>com.apple.ScreenTimeAgent.settings</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.UsageTrackingAgent.private</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.DeviceActivity</string>
+	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.DeviceActivity</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.iBooks.BDSService.private</key>

 		<string>/Library/Caches/com.apple.NanoTimeKit/</string>
 		<string>/Library/Caches/NanoTimeKit/</string>
 		<string>/tmp/BridgeDiagnosticLogs/</string>
-		<string>/Library/VoiceTrigger/SAT/</string>
+		<string>/Library/VoiceTrigger/</string>
 		<string>/Library/Preferences/com.apple.coreaudio.plist</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.system</string>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.coreaudio</string>
+		<string>com.apple.itunesstored</string>
 		<string>com.apple.NanoRegistry</string>
 		<string>com.apple.mobiletimer</string>
 		<string>com.apple.Bridge</string>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<array>
 		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>

 		<string>/private/var/mobile/Library/Seymour/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>
 		<string>/private/var/mobile/Library/Caches/</string>
+		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.fitcored</string>
 		<string>com.apple.coreaudio.device</string>
 		<string>com.apple.suggestions</string>
+		<string>com.apple.private.health.respiratory</string>
+		<string>com.apple.private.health.age-gating</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FitnessWidget

> `/private/var/staged_system_apps/Fitness.app/PlugIns/FitnessWidget.appex/FitnessWidget`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>
 	<true/>
+	<key>com.apple.private.healthkit.feature-availability.read-any</key>
+	<true/>
+	<key>com.apple.private.sleepd</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/DeviceRegistry/</string>
+		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sleepd.sleepserver</string>
 		<string>com.apple.fitnessintelligenced</string>
 		<string>com.apple.heartratecoordinatord.observer</string>
 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.appconduitd.device-connection</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.private.health.respiratory</string>
+		<string>com.apple.private.health.age-gating</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.nanolifestyle</string>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.CloudSubscriptionFeatures.datadetectors</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### asd

> `/usr/libexec/asd`

```diff

 <dict>
 	<key>adi-client</key>
 	<string>583940298</string>
+	<key>application-identifier</key>
+	<string>com.apple.asd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 				<string>ApplePay.Security.Features</string>
 			</array>
 		</dict>
+		<key>com.apple.asd</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>Mail</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.replicator.controller</key>
 	<true/>

 		<string>com.apple.apsd</string>
 		<string>com.apple.financed.service.financestore</string>
 		<string>com.apple.financed.service.coredatastore</string>
+		<string>com.apple.generativesearch.server.search</string>
 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<array>
 		<string>com.apple.AutoWake.xml</string>
 	</array>
+	<key>com.apple.TVRemoteCore</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.aop.hid-driver.user-client</key>
 	<dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
 		<key>wombat</key>
 		<dict>
 			<key>send-command</key>

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
 	<key>com.apple.private.sandbox.profile:embedded</key>

```


