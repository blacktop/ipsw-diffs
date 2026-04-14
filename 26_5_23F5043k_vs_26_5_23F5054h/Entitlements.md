## 🔑 Entitlements

### FamilyOutOfProcessUIExtension

> `/Applications/FamilyExtensionHost.app/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.familycircled</key>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.alarmkit.bundleIdentifier</key>
+	<string>com.apple.reminders</string>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.screentime</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.angeltarget</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>

```
### SoftwareUpdateUIService

> `/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.softwareupdateservicesd</string>

```
### BlackPowderInferenceExtension

> `/System/Library/ExtensionKit/Extensions/BlackPowderInferenceExtension.appex/BlackPowderInferenceExtension`

```diff

 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>com.apple.AppleIntelligence.Reporting.Invocation.Step</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.Invocation.Step</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### FamilyOutOfProcessUIExtension

> `/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.familycircled</key>

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.priml.PFLMLHostPlugins.FedAutoEvalPlugin</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.priml.PFLMLHostPlugins.FedAutoEvalPlugin</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<array>
 		<string>read</string>
 	</array>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

```
### GPNonUIExtension

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/GPNonUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageGeneration</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageGeneration</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### SCARemoteView Appex

> `/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/SCARemoteView Appex`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.contactsd</string>

```
### SiriAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/SiriAutoEvalPlugin.appex/SiriAutoEvalPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.priml.PFLMLHostPlugins.SiriAutoEvalPlugin</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.priml.PFLMLHostPlugins.SiriAutoEvalPlugin</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.pac.exception</key>
+	<true/>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>EnableExperimentalSandbox</string>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/ExtensionKit/Extensions/WebContentEnhancedSecurityExtension.appex/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.pac.exception</key>
+	<true/>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>EnableExperimentalSandbox</string>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.pac.exception</key>
+	<true/>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>EnableExperimentalSandbox</string>

```
### ServicesAccountLinkingService

> `/System/Library/Frameworks/ServicesAccountLinking.framework/XPCServices/ServicesAccountLinkingService.xpc/ServicesAccountLinkingService`

```diff

 	<true/>
 	<key>com.apple.security.ts.read-any-bundle</key>
 	<true/>
+	<key>com.apple.security.ts.tmpdir</key>
+	<string>com.apple.ServicesAccountLinkingService</string>
 	<key>fairplay-client</key>
 	<string>511712240</string>
 	<key>platform-application</key>

```

### 🆕 appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/appleaccounttransparencyd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.appleaccount.transparency</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.transparencyd.aet</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.appleaccounttransparency</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.dasd.widgetBudgetReset</key>
 	<true/>
+	<key>com.apple.developer.accessory-data-provider</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.networking.custom-protocol</key>

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.analyticsagent</string>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.InFocus</string>
+	</array>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>AppUsageTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>com.apple.gms.availability</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.analyticsagent</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.analyticsagent</string>
 	<key>platform-application</key>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.private.install.distributor-info-source</key>
 	<true/>
+	<key>com.apple.private.iokit.batterydataprecise</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.security.daemon-container</key>

```
### smbclientd

> `/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd`

```diff

 	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
+	<key>com.apple.private.LiveFS.connection</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.security.app-sandbox</key>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<array>
 		<string>group.com.apple.coreservices.useractivityd</string>
 	</array>
+	<key>com.apple.private.sharing.activity-advertiser</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceUbiquity</string>

```
### assetsubscriptiond

> `/usr/libexec/assetsubscriptiond`

```diff

 	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
 	<key>com.apple.private.assets.change-daemon-config</key>

```
### carkitd

> `/usr/libexec/carkitd`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpoint.xpc</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.locationd.accessory_location</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

```
### cryptexd

> `/usr/libexec/cryptexd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Cryptex</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicySysAdminFiles</string>

 	</array>
 	<key>com.apple.watchdogd.runtime-opt-in</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.internal.dpm</string>
+	</array>
 </dict>
 </plist>
 

```
### frauddefensed

> `/usr/libexec/frauddefensed`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.trustkit</string>
 		<string>com.apple.frauddefensed</string>
 		<string>com.apple.messages</string>
 	</array>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 		<string>/usr/local/bin/suServer.py</string>
 		<string>/usr/local/bin/python3</string>
 	</array>
+	<key>com.apple.springboard.homeScreenLayoutAvailability</key>
+	<true/>
 	<key>com.apple.wifi_nan.event_monitor</key>
 	<true/>
 	<key>com.apple.wifip2p.daemon_monitor</key>

```
### linkd

> `/usr/libexec/linkd`

```diff

 		<string>com.apple.remoteappintentsd.appevent</string>
 		<string>com.apple.CARenderServer</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.homed</string>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.AdPlatforms</string>
+		<string>com.apple.ap.config</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### remindd

> `/usr/libexec/remindd`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.security.ts.application-group-support</key>
 	<true/>
 	<key>com.apple.security.ts.asset-access</key>

```
### securityd

> `/usr/libexec/securityd`

```diff

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.appletv.pbs.allow-screen-saver</key>
+	<true/>
+	<key>com.apple.appletv.pbs.allow-sleep</key>
+	<true/>
 	<key>com.apple.appletv.pbs.allow-user-interface-style-change</key>
 	<true/>
+	<key>com.apple.appletv.pbs.allow-wake</key>
+	<true/>
 	<key>com.apple.appletv.pbs.app-info-service-access</key>
 	<true/>
+	<key>com.apple.appletv.pbs.mediaremote</key>
+	<true/>
 	<key>com.apple.appletv.pbs.person-monitor-service-access</key>
 	<true/>
 	<key>com.apple.appletv.pbs.person-monitor-service-access.write</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-device</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-dispatch</key>
+	<true/>
+	<key>com.apple.private.hid.client.event-monitor</key>
+	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
+		<string>IOHIDUserDeviceCreate</string>
+		<string>IOHIDResourceDeviceUserClient</string>
+		<string>IOHIDUserClient</string>
+		<string>IO80211APIUserClient</string>
 		<string>IOHIDLibUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>com.apple.watchlistd.xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>
+		<string>com.apple.remote-text-editing-legacy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
