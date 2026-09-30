## 🔑 Entitlements

### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 		<key>com.apple.productkit.personalization</key>
 		<string>com.apple.productkit.personalization</string>
 	</dict>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.followup</key>

```
### GameTrampoline

> `/Applications/GameTrampoline.app/GameTrampoline`

```diff

 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GameTrampoline</string>
 	<key>com.apple.developer.associated-domains</key>
-	<array>
-		<string>applinks:games.apple.com</string>
-	</array>
+	<array/>
 	<key>com.apple.developer.game-center</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key> com.apple.sharing.Session</key>
-	<true/>
 	<key>CARAppHidden</key>
 	<true/>
 	<key>CARCapableApp</key>

 		<string>com.apple.mediaremoteui</string>
 		<string>com.apple.Accessibility</string>
 	</array>
+	<key>com.apple.sharing.Session</key>
+	<true/>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x</string>
 		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPad</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction.iPhone</string>
+		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction.iPad</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.iconTintColor</key>
 	<true/>
 	<key>com.apple.springboard.lookupFolderPathForIcon</key>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
+	<key>com.apple.private.hid.client.admin</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-filter</key>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<array>
 		<string>com.apple.commandandcontrol</string>
 	</array>
+	<key>com.apple.realitysimulation.render-on-top-spi</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.audio.SystemSoundServer-iOS</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.SpringBoard.ReadyForRestore</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.keyboard.DictationInfoIsOnScreen</key>
 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.purplebuddy.launchMigrationSourceUI</key>

```
### AVCPlugin

> `/System/Library/ExtensionKit/Extensions/AVCPlugin.appex/AVCPlugin`

```diff

 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 	</array>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.storekit</key>
+	<array>
+		<string>ExternalGateway</string>
+	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>com.apple.attributionkitd.xpc.token-handoff</string>
 		<string>com.apple.backgroundassets.system</string>
 		<string>com.apple.StreamingUnzipService</string>
+		<string>com.apple.storekitd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.storekit.client-override</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```

### 🆕 FamilySettings

> `/System/Library/PreferenceBundles/FamilySettings.bundle/FamilySettings`

- No entitlements *(yet)*
### AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/AppIntentsRunnerXPCService`

```diff

 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
-	<key>get-task-allow</key>
-	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.modelmanager</string>
 		<string>com.apple.securityd.systemkeychain</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.xpc.amsengagementd</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.anvil</string>
 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.storeservices.itfe</string>
 	</array>

 	<string>1445028844</string>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.openai.xcode</string>
 		<string>com.apple.openai</string>
 		<string>apple</string>
 	</array>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 		<string>com.apple.Podcasts</string>
 		<string>243LU875E5.com.apple.podcasts</string>
 		<string>com.apple.MobileSMS</string>
+		<string>com.apple.GameTrampoline</string>
+		<string>com.apple.games</string>
 	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>

```
### communicationtrustd

> `/System/Library/PrivateFrameworks/CommunicationTrust.framework/Support/communicationtrustd`

```diff

 		<string>com.apple.cmfsyncagent.embedded.auth</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.AppSupport</string>
+	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### CMFSyncAgent

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.cmfsyncagent</string>
+	<key>com.apple.Contacts.database-allow</key>
+	<true/>
 	<key>com.apple.StatusKit.publish.types</key>
 	<array>
 		<string>com.apple.focus.status</string>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/</string>
+		<string>/private/var/mobile/Library/AddressBook/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.StatusKit.publish</string>

 	<array>
 		<string>com.apple.cmfsyncagent</string>
 	</array>
+	<key>com.apple.security.ts.addressbook</key>
+	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 </dict>

```

### 🆕 LogArchiveDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/LogArchiveDiagnosticExtension.appex/LogArchiveDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### intentrecommendd

> `/System/Library/PrivateFrameworks/IntentRecommendRuntime.framework/intentrecommendd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.intents.extension.discovery</key>
+	<true/>
 	<key>com.apple.linkd.registry</key>
 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>

```
### NewsScoringService

> `/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/NewsScoringService.xpc/NewsScoringService`

```diff

 	<array>
 		<string>group.com.apple.newsd</string>
 		<string>group.com.apple.stocks</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<integer>4201635476</integer>
 	<key>application-identifier</key>
 	<string>com.apple.passd</string>
 	<key>aps-connection-initiate</key>

 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.passd</string>
+	<key>com.apple.developer.weatherkit</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.finance.private</key>

 	<true/>
 	<key>com.apple.wallet.banner</key>
 	<true/>
+	<key>fairplay-client</key>
+	<integer>87750944</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.CredentialSharingService</string>

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.appconduitd.allowedSPI</key>
+	<array>
+		<string>CompanionAppInfo</string>
+	</array>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

```
### ThreatNotificationCFU

> `/System/Library/PrivateFrameworks/ThreatNotificationUI.framework/Extensions/ThreatNotificationCFU.appex/ThreatNotificationCFU`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.adid</string>
 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.corefollowup.agent</string>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 		<string>group.tvappservices.container</string>
 		<string>group.com.apple.sports</string>
 		<string>group.com.apple.tv.sharedcontainer</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.visioncompaniond</string>
 		<string>com.apple.itunescloudd.xpc</string>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.feature-setting.allowFindMyCar</key>
 	<true/>
+	<key>com.apple.maps.assertions</key>
+	<true/>
 	<key>com.apple.maps.ipc-access</key>
 	<true/>
 	<key>com.apple.maps.model-access</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>H11ANEInDirectPathClient</string>
 		<string>AppleVirtIONeuralEngineDeviceUserClient</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceWillow</string>

 	<array>
 		<string>/Library/Audio/Plug-Ins/HAL/</string>
 		<string>/private/var/preferences/SystemConfiguration/preferences.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.SoundProfileAsset</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>

 		<string>/usr/libexec</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.mediaremote.plist</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### companiond

> `/usr/libexec/companiond`

```diff

 		<string>com.apple.SharedWebCredentials</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.SystemConfiguration.configd</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
 		<string>com.apple.tvremotecore.xpc</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-call-capabilities</string>
+	</array>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```
