## 🔑 Entitlements

### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.app-distribution.private</key>
 	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	<true/>
 	<key>com.apple.private.sportskit.client</key>
 	<true/>
+	<key>com.apple.private.spotlight.cep-engagement-data</key>
+	<true/>
 	<key>com.apple.private.subscriptionservice.internal</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

```

### 🆕 T8150_IR_ISP_EK_Component_asan

> `/System/ExclaveKit/System/Library/Frameworks/T8150_IR_ISP_EK_Component.framework/T8150_IR_ISP_EK_Component_asan`

- No entitlements *(yet)*

### 🆕 T8150_RGB_ISP_EK_Component_asan

> `/System/ExclaveKit/System/Library/Frameworks/T8150_RGB_ISP_EK_Component.framework/T8150_RGB_ISP_EK_Component_asan`

- No entitlements *(yet)*

### 🆕 T8150_CoreAAClientKit_asan

> `/System/ExclaveKit/System/Library/PrivateFrameworks/T8150_CoreAAClientKit.framework/T8150_CoreAAClientKit_asan`

- No entitlements *(yet)*

### 🆕 T8150_ExclaveISPSharedLib_exclavekit_asan

> `/System/ExclaveKit/System/Library/PrivateFrameworks/T8150_ExclaveISPSharedLib_exclavekit.framework/T8150_ExclaveISPSharedLib_exclavekit_asan`

- No entitlements *(yet)*
### PasswordsDataMigration

> `/System/Library/ExtensionKit/Extensions/PasswordsDataMigration.appex/PasswordsDataMigration`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.coreduetd.allow</key>
+	<true/>
+	<key>com.apple.coreduetd.people</key>
+	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
+	<key>com.apple.private.keychain.kcsharing.client</key>
+	<true/>
 	<key>com.apple.private.migrationkit.system-dataclass</key>
 	<string>passwords</string>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.security.octagon</string>
+		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
+		<string>com.apple.AuthenticationServices.AutoFill</string>
+		<string>com.apple.Safari.PasswordBreachHelper</string>
+		<string>com.apple.SharedWebCredentials</string>
+		<string>com.apple.security.kcsharing</string>
+		<string>com.apple.coreduetd.people.user</string>
+		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.networkserviceproxy</string>
+		<string>com.apple.private.email</string>
+		<string>com.apple.imagent.embedded.auth</string>
+		<string>com.apple.ak.privateemail.xpc</string>
+	</array>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
+	<key>com.apple.sharing.Services</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.cfnetwork</string>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>
 	<true/>
 	<key>com.apple.app-distribution.private</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.airplay.carplayavvc</key>
 	<true/>
 	<key>com.apple.announced.client</key>

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.assistant.shared</string>
+		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.weather</string>
 	</array>
 	<key>com.apple.private.security.storage.CallHistory</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.assistant.shared</string>
+		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.weather</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
 	<key>com.apple.aned.private.processModelShare.allow</key>

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siri.embeddedspeech</string>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.airplay.carplayavvc</key>
 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>

 	<true/>
 	<key>com.apple.audio.isolated.historicalaudio.client.service</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<true/>
 	<key>com.apple.private.exclaves.conclave-host</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.siri.recorded-audio</string>
+		<string>group.com.apple.siri.ASR.shared</string>
 	</array>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.CoreSpeech</string>
+		<string>group.com.apple.siri.ASR.shared</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### SecureMessagingAgent

> `/System/Library/PrivateFrameworks/SecureMessaging.framework/SecureMessagingAgent`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>autobox</string>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.ts.daemon-container</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.securemessagingagent</string>
 	<key>keychain-access-groups</key>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/XPCServices/SiriSuggestionsBookkeepingService.xpc/SiriSuggestionsBookkeepingService`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
 	<key>com.apple.internal.intelligenceplatform.use-cases</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>siriRemembers</string>

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.sus.daemon</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>AppleIntelligenceReporting.AssetDelivery</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.SoftwareUpdateController</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.iokit.nvram-write-access</key>

 		<string>com.apple.CoreAuthentication.daemon.libxpc</string>
 		<string>com.apple.MobileTimer.timerserver</string>
 		<string>com.apple.MobileTimer.alarmserver</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
 	<true/>
-	<key>com.apple.private.mediaexperience.suppressrecordingstatetosystemstatus</key>
-	<true/>
 	<key>com.apple.private.mediaexperience.useindependentinputaudioresourcesession</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	</array>
 	<key>com.apple.NPKCompanionAgent.client</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.callhistoryd.service</key>
 	<true/>
 	<key>com.apple.cards.all-access</key>

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.feature-availability.read</key>

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 AppleLatticeSupport

> `/usr/libexec/AppleLatticeSupport.framework/AppleLatticeSupport`

- No entitlements *(yet)*
### MobileAssetEarlyBootTask

> `/usr/libexec/MobileAssetEarlyBootTask`

```diff

 <dict>
 	<key>com.apple.private.apfs.get-graft-info</key>
 	<true/>
+	<key>com.apple.private.diskimages.kext.user-client-access</key>
+	<true/>
 	<key>com.apple.private.vfs.exclave-fs-register</key>
 	<true/>
 	<key>com.apple.private.vfs.graftdmg</key>

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>
+		<string>AppleImage4UserClient</string>
+		<string>IOHDIXControllerUserClient</string>
 	</array>
 </dict>
 </plist>

```
### avconferenced

> `/usr/libexec/avconferenced`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sensitivecontentanalysis.client</key>
 	<array>
 		<string>analysis</string>

 		<string>/Library/Audio/Tunings/Generic/VAD/nnvad.dspg</string>
 		<string>/Library/Audio/Tunings/Generic/VAD/nnvad_ver1.plist</string>
 		<string>/Library/Audio/Tunings/Generic/VAD/nnvad.austrip</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### corecaptured

> `/usr/libexec/corecaptured`

```diff

 		<string>com.apple.private.bluetooth.driverkit</string>
 		<string>com.apple.private.corecaptureclient.driverkit</string>
 	</array>
+	<key>com.apple.private.kernel.get-kext-info</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOReportUserClient</string>

```

### 🆕 latticed

> `/usr/libexec/latticed`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.lattice.user.access</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<false/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>LatticeUserClient</string>
	</array>
	<key>com.apple.ssm.monitored-service-identifier</key>
	<string>com.apple.network.latticed</string>
</dict>
</plist>

```
### replayd

> `/usr/libexec/replayd`

```diff

 		<string>com.apple.ReplayKitNotifications</string>
 		<string>com.apple.ReplayKitNotifications.CallRecording</string>
 	</array>
+	<key>com.apple.runningboard.cameracapture</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.screen_watcher_notification</key>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.selectivesharing.session_system</key>
 	<true/>
 	<key>com.apple.selectivesharing.system</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
+	<key>com.apple.idle-timer-services</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.imagent.chat</key>

```
