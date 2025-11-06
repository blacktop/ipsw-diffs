## 🔑 Entitlements

### FMDMagSafeSetupRemoteUI

> `/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Caches/com.apple.icloud.findmydeviced/</string>

```
### FMDMagSafeExtension

> `/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension`

```diff

 	<true/>
 	<key>com.apple.private.accessories.showallconnections</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Caches/com.apple.icloud.findmydeviced/</string>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	</array>
 	<key>com.apple.sharing.Client</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.springboard.systemaperture</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	<true/>
 	<key>com.apple.shortcuts.dialogpresentation</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>

```
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.shortcuts.dialogpresentation</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.sirittsd.can-dump-audio</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.shortcuts.dialogpresentation</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### WidgetConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension`

```diff

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.shortcuts.background-running</key>
 	<true/>
+	<key>com.apple.shortcuts.file-bookmarks</key>
+	<true/>
 	<key>com.apple.shortcuts.trigger-editing</key>
 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<array>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 		<string>group.com.apple.icloud.findmydevice.followup</string>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
 	</array>
 	<key>com.apple.private.system-keychain</key>
 	<true/>

 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.icloud.findmydevice.magsafe</string>
+		<string>group.com.apple.icloud.findmydevice.followup</string>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
