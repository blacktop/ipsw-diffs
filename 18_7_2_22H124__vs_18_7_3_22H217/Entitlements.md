## 🔑 Entitlements

### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.composeclient</key>
 	<true/>
 	<key>com.apple.messages.sticker-sharing-level</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	</array>
 	<key>com.apple.managedconfiguration.profiled.set</key>
 	<array>
+		<string>ClientRestrictions</string>
 		<string>Passcode</string>
 	</array>
 	<key>com.apple.managedconfiguration.teslad-access</key>

 	<true/>
 	<key>com.apple.mediastream.mstreamd-access</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.mkb.usersession.delete</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

 	<true/>
 	<key>com.apple.private.WebKit.UnrestrictedApplePay</key>
 	<true/>
+	<key>com.apple.private.accessibility.scrod</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.accounts.bundleidspoofing</key>

```
### StickersUltraExtension

> `/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.private.BypassShelfAccess</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>

```
### StickersUltra

> `/Applications/StickersUltra.app/StickersUltra`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.private.BypassShelfAccess</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>

```
### iMessageAppsViewService

> `/Applications/iMessageAppsViewService.app/iMessageAppsViewService`

```diff

 	<true/>
 	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.sticker-sharing-level</key>
 	<string>system</string>
 	<key>com.apple.private.avatar.store</key>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<true/>
 	<key>com.apple.private.MagnifierAngel.client</key>
 	<true/>
+	<key>com.apple.private.accessibility.scrod</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.SafetyMonitor</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.SocialHighlight</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### IMTranscoderAgent

> `/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.pac.shared_region_id</key>

```
### IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent`

```diff

 	</array>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
 	<key>com.apple.pac.shared_region_id</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.sticker-sharing-level</key>
 	<string>messages</string>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>

```
### MessagesAssistantExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.private.CallHistory.read</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### MessagesAssistantUIExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantUIExtension.appex/MessagesAssistantUIExtension`

```diff

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

```
### MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### MessagesPluginNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

```
### MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
