## 🔑 Entitlements

### filesystem

### Contacts

> `/System/Applications/Contacts.app/Contents/MacOS/Contacts`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.suggestions</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

```
### Games

> `/System/Applications/Games.app/Contents/MacOS/Games`

```diff

 	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.servicesintelligenced</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

```
### PasswordsMenuBarExtra

> `/System/Applications/Passwords.app/Contents/Library/LoginItems/PasswordsMenuBarExtra.app/Contents/MacOS/PasswordsMenuBarExtra`

```diff

 		<string>io.island.Island.dev</string>
 		<string>ru.yandex.desktop.yandex-browser</string>
 		<string>ai.perplexity.comet</string>
+		<string>ai.perplexity.comet-beta</string>
 		<string>ai.perplexity.comet-canary</string>
 		<string>ai.perplexity.comet-dev</string>
 		<string>com.coccoc.Coccoc</string>

 		<string>com.phibrowser.canary.Mac</string>
 		<string>com.shift.browser</string>
 		<string>dev.iamevan.flow</string>
+		<string>app.glide-browser.glide</string>
+		<string>com.firstversionist.polypane</string>
+		<string>com.tab-browser.Tabbit</string>
+		<string>com.tabbit-ai.Tabbit</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/Contents/MacOS/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.servicesintelligenced</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/CallHistoryDB/</string>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Support/accountsd`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

```
### GameOverlayViewService

> `/System/Library/PrivateFrameworks/GameCenterUICore.framework/XPCServices/GameOverlayViewService.xpc/Contents/MacOS/GameOverlayViewService`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.MessagesLegacyTransferArchive</string>
+		<string>group.com.apple.servicesintelligenced</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 		<string>com.apple.CommunicationTrust</string>
 		<string>com.apple.MobileStoreDemo.test</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-write</key>
+	<array>
+		<string>kern.memorystatus_vm_pressure_send</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```

### 🆕 Managed Background Assets Relay Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/Versions/A/XPCServices/Managed Background Assets Relay Service.xpc/Contents/MacOS/Managed Background Assets Relay Service`

- No entitlements *(yet)*

### 🆕 Managed Background Assets Relay Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/Versions/Current/XPCServices/Managed Background Assets Relay Service.xpc/Contents/MacOS/Managed Background Assets Relay Service`

- No entitlements *(yet)*
### com.apple.MobileInstallationHelperService

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/Contents/MacOS/com.apple.MobileInstallationHelperService`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceSystemPolicyDesktopFolder</string>
 		<string>kTCCServiceSystemPolicyAppBundles</string>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 	</array>

```
### STExtractionService.privileged

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/Versions/A/XPCServices/STExtractionService.privileged.xpc/Contents/MacOS/STExtractionService.privileged`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobilegestalt.xpc</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### STExtractionService.privileged

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/Versions/Current/XPCServices/STExtractionService.privileged.xpc/Contents/MacOS/STExtractionService.privileged`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobilegestalt.xpc</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<key>com.apple.private.ids.messaging.high-priority</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	</array>
 	<key>com.apple.private.ids.registration</key>
 	<array>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>

 	<key>com.apple.private.ids.self-session</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<key>com.apple.private.ids.session</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<key>com.apple.private.ids.session-private</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

```
### logd

> `/usr/libexec/logd`

```diff

 	<true/>
 	<key>com.apple.private.logging.helper</key>
 	<true/>
+	<key>com.apple.private.security.storage.LogdPreferencesCache</key>
+	<true/>
 	<key>com.apple.private.set-atm-diagnostic-flag</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	</array>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 	<key>com.apple.private.skywalk.observe-all</key>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.telemetry</key>
 	<true/>
 	<key>com.apple.cdp.utility</key>

```


### SystemOS

### com.apple.WebKit.GPU

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 	<key>com.apple.tcc.delegated-services</key>

```
### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 	<key>com.apple.symptom_analytics.configure</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### com.apple.WebKit.WebContent

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### com.apple.WebKit.GPU

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 	<key>com.apple.tcc.delegated-services</key>

```
### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 	<key>com.apple.symptom_analytics.configure</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### com.apple.WebKit.WebContent

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 		<string>io.island.Island.dev</string>
 		<string>ru.yandex.desktop.yandex-browser</string>
 		<string>ai.perplexity.comet</string>
+		<string>ai.perplexity.comet-beta</string>
 		<string>ai.perplexity.comet-canary</string>
 		<string>ai.perplexity.comet-dev</string>
 		<string>com.coccoc.Coccoc</string>

 		<string>com.phibrowser.canary.Mac</string>
 		<string>com.shift.browser</string>
 		<string>dev.iamevan.flow</string>
+		<string>app.glide-browser.glide</string>
+		<string>com.firstversionist.polypane</string>
+		<string>com.tab-browser.Tabbit</string>
+		<string>com.tabbit-ai.Tabbit</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>

```
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/Current/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 		<string>io.island.Island.dev</string>
 		<string>ru.yandex.desktop.yandex-browser</string>
 		<string>ai.perplexity.comet</string>
+		<string>ai.perplexity.comet-beta</string>
 		<string>ai.perplexity.comet-canary</string>
 		<string>ai.perplexity.comet-dev</string>
 		<string>com.coccoc.Coccoc</string>

 		<string>com.phibrowser.canary.Mac</string>
 		<string>com.shift.browser</string>
 		<string>dev.iamevan.flow</string>
+		<string>app.glide-browser.glide</string>
+		<string>com.firstversionist.polypane</string>
+		<string>com.tab-browser.Tabbit</string>
+		<string>com.tabbit-ai.Tabbit</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>

```
### com.apple.WebKit.GPU

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### com.apple.WebKit.Networking

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.Development

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.GPU

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### com.apple.WebKit.Networking

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.Development

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```


### AppOS

### PasswordManagerBrowserExtensionHelper

> `/System/Library/CoreServices/PasswordManagerBrowserExtensionHelper.app/Contents/MacOS/PasswordManagerBrowserExtensionHelper`

```diff

           "signing-identifier": {
             "$in": [
               "ai.perplexity.comet",
+              "ai.perplexity.comet-beta",
               "ai.perplexity.comet-canary",
               "ai.perplexity.comet-dev"
             ]

           "signing-identifier": "dev.iamevan.flow",
           "team-identifier": "LP64XSF5PS"
         }
+      },
+      {
+        "$and": {
+          "signing-identifier": "app.glide-browser.glide",
+          "team-identifier": "M3M9SSHSKB"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.firstversionist.polypane",
+          "team-identifier": "UQ5NG7PA6X"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": {
+            "$in": [
+              "com.tab-browser.Tabbit",
+              "com.tabbit-ai.Tabbit"
+            ]
+          },
+          "team-identifier": "2DE8QTFYGR"
+        }
       }
     ]
   },

```


