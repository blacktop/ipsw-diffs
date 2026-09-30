## 🔑 Entitlements

### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/mobile/Library/Mobile Documents/</string>
+		<string>/private/var/MobileAsset/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.PairingManager</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.ScreenTimeAgent.persistence</string>
+		<string>com.apple.ScreenTimeAgent.private</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.siri.analytics.assistant</string>

 		<string>com.apple.passd.payment</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.ScreenTimeAgent.persistence</string>
+		<string>com.apple.ScreenTimeAgent.private</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.sucontrollerd</string>

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 		<string>GenerativeExperiences.Proactive.UseModelShortcutsProd</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeExperiences.PromptTags</string>
+		<string>GenerativeExperiences.WritingToolsFeatures.Requests</string>
+		<string>GenerativeExperiences.WritingToolsFeatures.Metadata</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeExperiences.PromptTags</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>App.InFocus</string>
+		<string>GenerativeExperiences.WritingToolsFeatures.Metadata</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>AdPlatforms.PolicyInstrumentation.Opportunity</string>
 		<string>AdPlatforms.PolicyInstrumentation.Candidate</string>
 		<string>Mail.Search.Query</string>
+		<string>GenerativeExperiences.WritingToolsFeatures.Metadata</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### SearchUploadWorker

> `/System/Library/ExtensionKit/Extensions/SearchUploadWorker.appex/SearchUploadWorker`

```diff

 	<string>com.apple.unilog.SearchUploadWorker</string>
 	<key>com.apple.developer.networking.multipath_extended</key>
 	<true/>
-	<key>com.apple.internal.intelligenceplatform.use-cases</key>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>Unilog.MailSearch.Processed</string>
+	</array>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.unilog.datacollector.SearchUploadWorker</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>UnilogMailSearchProcessed</key>
 		<dict>

 			</dict>
 		</dict>
 	</dict>
-	<key>com.apple.private.biome.read-only</key>
-	<array>
-		<string>Unilog.MailSearch.Processed</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### SiriUploadWorker

> `/System/Library/ExtensionKit/Extensions/SiriUploadWorker.appex/SiriUploadWorker`

```diff

 	<string>com.apple.unilog.SiriUploadWorker</string>
 	<key>com.apple.developer.networking.multipath_extended</key>
 	<true/>
-	<key>com.apple.internal.intelligenceplatform.use-cases</key>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>Unilog.Siri.Processed</string>
+	</array>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.unilog.datacollector.SiriUploadWorker</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>UnilogSiriProcessed</key>
 		<dict>

 			</array>
 		</dict>
 	</dict>
-	<key>com.apple.private.biome.read-only</key>
-	<array>
-		<string>Unilog.Siri.Processed</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### axassetsd

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceVoiceBanking</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.voicebanking.services</string>
+		<string>com.apple.voicebanking.store</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.voiceservices.tts</string>

 	<array>
 		<string>406</string>
 	</array>
+	<key>com.apple.voicebanking.services</key>
+	<true/>
 	<key>inter-app-audio</key>
 	<true/>
 	<key>platform-application</key>

```
### SecureMessagingAgent

> `/System/Library/PrivateFrameworks/SecureMessaging.framework/SecureMessagingAgent`

```diff

 	<array>
 		<string>com.apple.ids</string>
 		<string>com.apple.securemessaging</string>
+		<string>com.apple.SwiftMLS</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### fitcored

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored`

```diff

 	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
-	<key>com.apple.developer.healthkit.background-delivery</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.seymour</string>

```
### watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/</string>
+		<string>/Library/com.apple.AppleMediaServices/PersistedBags/</string>
 		<string>/Library/com.apple.WatchListKit/</string>
 		<string>/Library/Logs/PersistentConnection/com.apple.watchlistd-watchlistd-APSClient.log</string>
 	</array>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
-	<key>com.apple.SensingPredict</key>
-	<true/>
 	<key>com.apple.account.AppleAccount</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

 		<string>com.apple.PowerManagement.control</string>
 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.server.bluetooth</string>
-		<string>com.apple.SensingPredictXPCService</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.springboard.services</string>
 		<string>com.apple.SystemConfiguration.configd</string>

```
### bulletindistributord

> `/usr/libexec/bulletindistributord`

```diff

 		<string>com.apple.private.alloy.bulletindistributor</string>
 		<string>com.apple.private.alloy.bulletindistributor.settings</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Caches/GameKit/Images/GKBulletins/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.donotdisturb.service</string>

```
### corecaptured

> `/usr/libexec/corecaptured`

```diff

 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
+	<key>com.apple.private.CacheDelete</key>
+	<array>
+		<string>CLIENT_ENTITLEMENT</string>
+		<string>NOTIFICATION_ENTITLEMENT</string>
+		<string>SERVICE_ENTITLEMENT</string>
+	</array>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>InverseDeviceID</string>

```
### corercd

> `/usr/libexec/corercd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOCECUserClient</string>
 		<string>IOHIDLibUserClient</string>
 		<string>RootDomainUserClient</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.TapToRadarKit.service</string>
+	</array>
 </dict>
 </plist>
 

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 		<string>/usr/standalone/firmware/SLAM/</string>
 		<string>/private/preboot/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
-		<string>/private/var/db/nearbyd</string>
+		<string>/private/var/db/nearbyd/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>wifip2pd</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.skywalk.register-user-pipe</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 	<true/>
 	<key>com.apple.runningboard.assertions.WiFiAware</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.lsd.mapdb</string>

 		<string>AppleKeyStoreUserClient</string>
 		<string>RootDomainUserClient</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+	</array>
 	<key>com.apple.security.ts.mach-task-name</key>
 	<true/>
 	<key>com.apple.security.ts.springboard-services</key>

```
