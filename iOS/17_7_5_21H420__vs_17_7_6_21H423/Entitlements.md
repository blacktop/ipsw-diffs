## 🔑 Entitlements

### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### com.apple.mobilenotes.SharingExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.personas.propagate</key>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.debug</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.debug</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.cache_delete</string>
+		<string>com.apple.containermanagerd</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
