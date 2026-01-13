## 🔑 Entitlements

### PasswordsMenuBarExtra

> `/System/Applications/Passwords.app/Contents/Library/LoginItems/PasswordsMenuBarExtra.app/Contents/MacOS/PasswordsMenuBarExtra`

```diff

 		<string>com.apple.ak.signinwithapple.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### Passwords

> `/System/Applications/Passwords.app/Contents/MacOS/Passwords`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### Safari

> `/System/Applications/Safari.app/Contents/MacOS/Safari`

```diff

 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.coreduetd.people.user</string>
 		<string>com.apple.familycircle.agent</string>
-		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.mdmclient.daemon.unrestricted</string>
 		<string>com.apple.softwareupdated.OSUpdate</string>
 		<string>com.apple.softwareupdated</string>

```
### PasswordManagerBrowserExtensionHelper

> `/System/Library/CoreServices/PasswordManagerBrowserExtensionHelper.app/Contents/MacOS/PasswordManagerBrowserExtensionHelper`

```diff

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.email.maild</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### Spotlight

> `/System/Library/CoreServices/Spotlight.app/Contents/MacOS/Spotlight`

```diff

 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
+	<key>com.apple.private.spotlight.cep-engagement-data</key>
+	<true/>
 	<key>com.apple.private.spotlight.parsec</key>
 	<true/>
 	<key>com.apple.private.spotlight.search.internal</key>

```
### UserAccountUpdater

> `/System/Library/CoreServices/UserAccountUpdater`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.LocalAuthentication.ExtractCredential</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.systemmigration.daemonclient</key>

 	<array>
 		<string>com.apple.private.migrationhelper.allow</string>
 	</array>
+	<key>com.apple.security.filevault.xpc.allow</key>
+	<true/>
 </dict>
 </plist>
 

```
### Web App

> `/System/Library/CoreServices/Web App.app/Contents/MacOS/Web App`

```diff

 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.coreduetd.people.user</string>
 		<string>com.apple.familycircle.agent</string>
-		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.mdmclient.daemon.unrestricted</string>
 		<string>com.apple.softwareupdated.OSUpdate</string>
 		<string>com.apple.softwareupdated</string>

```
### loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

```diff

 	</array>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.ExtractCredential</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage.MacBuddyPassword</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistant_service`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

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
 		<string>group.com.apple.siri.recorded-audio</string>
 		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.weather</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.assistant.shared</string>
+		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.weather</string>
 	</array>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech`

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

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.siri.recorded-audio</string>
 	</array>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.CoreSpeech</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### corespeechd_system

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system`

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
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 		<string>com.apple.email.maild</string>
 		<string>com.apple.imagent.desktop.auth</string>
 		<string>com.apple.ak.privateemail.xpc</string>
-		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/Contents/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/Contents/MacOS/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

 		<string>com.apple.MobileAsset.EmbeddedSpeechMac</string>
 		<string>com.apple.MobileAsset.SRCommandAndControl</string>
 	</array>
-	<key>com.apple.private.audio.suppress-mic-indicator</key>
-	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.coreaudio.allow-au-extensions-daemon</key>

```
### fdesetup

> `/usr/bin/fdesetup`

```diff

 	<true/>
 	<key>com.apple.private.managedclient.configurationprofiles</key>
 	<true/>
+	<key>com.apple.private.opendirectoryd.BootstrapToken</key>
+	<true/>
 	<key>com.apple.private.opendirectoryd.auth-hint</key>
 	<true/>
 	<key>com.apple.private.opendirectoryd.securetoken</key>

```
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

### 🆕 xprotectd

> `/usr/libexec/xprotectd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.endpoint-security.client</key>
	<true/>
	<key>com.apple.private.endpoint-security.client</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceSystemPolicyAllFiles</string>
		<string>kTCCServiceEndpointSecurityClient</string>
	</array>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
</dict>
</plist>

```
