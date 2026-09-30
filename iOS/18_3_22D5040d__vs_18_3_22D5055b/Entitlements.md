## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.AMSEngagementViewService</string>
+	<key>com.apple.appstored.private</key>
+	<true/>
 	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
+		<string>com.apple.appstored.xpc.storequeue</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>

```
### SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

 	<true/>
 	<key>com.apple.private.powersource-read</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMicrophone</string>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/hardware/FactoryData/</string>
 		<string>/private/preboot/</string>
 		<string>/private/var/mobile/Library/Logs/AppleSupport/</string>
 		<string>/private/var/logs/AppleSupport/</string>
 		<string>/private/var/tmp/biokit_hw_issue_notification</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.demo-settings.plist</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.Accessibility.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>systemgroup.com.apple.powerlog</string>
 		<string>systemgroup.com.apple.DeviceActivity</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.icloud.gm</string>
+		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
+	</array>
 	<key>com.apple.seld.cm</key>
 	<true/>
 	<key>com.apple.seld.tsmmanager</key>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Shortcuts/</string>

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 AXFeatureOverrideServer

> `/System/Library/AccessibilityBundles/AXFeatureOverrideServer.axuiservice/AXFeatureOverrideServer`

- No entitlements *(yet)*
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.gamepolicyd.tool.privileged.xpc</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.geoservices.navigation_info</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 	<key>com.apple.private.usernotifications.settings</key>
 	<array>
 		<string>read</string>
+		<string>write</string>
 	</array>
 	<key>com.apple.private.vfs.allow-low-space-writes</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.searchd</string>
 		<string>com.apple.gamepolicyd.tool.privileged</string>
 		<string>com.apple.systemstatus</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.appstored</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.suggestions</string>

```
### iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.sandbox.container-query.all-users</key>
+	<true/>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/private/var/mobile/Library/Caches/com.apple.metal/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.metalfe/</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
+	<key>com.apple.private.keychain.sysbound</key>
+	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
 	<key>com.apple.private.managedclient.mdm.checkin</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.generativeexperiences.corefollowup</key>
+	<true/>
 	<key>com.apple.intelligenceflow.context</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>

 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.Preferences</string>
+	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.private.assistant.settings</string>
 		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.generativeexperiences.corefollowup</string>
 		<string>com.apple.appstored.xpc.request</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.CloudSubscriptionFeatures.ticket.cache</string>
 		<string>com.apple.CloudSubscriptionFeatures.cache</string>
 		<string>com.apple.CloudSubscriptionFeatures.gmCache</string>
+		<string>com.apple.icloud.gm</string>
 		<string>com.apple.csf.gm.bypass</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.mediaaccessibility</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### ind

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/ind`

```diff

 		<string>spi</string>
 		<string>identity</string>
 	</array>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.and.client</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.biome.access.user</string>

```
### com.apple.mobilesafari.SafariDiagnosticExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension`

```diff

 	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.safari</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/CrashReporter/</string>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.sharesheet.allow-custom-view</key>
+	<true/>
 	<key>com.apple.sharing.Client</key>
 	<true/>
 	<key>com.apple.shortcuts.background-running</key>

```
### linkd

> `/usr/libexec/linkd`

```diff

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>WaitForSystemAppMigrationToComplete</string>
+	</array>
 	<key>com.apple.private.remoteappintentsd.appevent</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobile.installd</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.siri.vocabularyupdates</string>

```
### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 	</array>
 	<key>com.apple.remotemanagementd.management-state</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.safari</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/installd/Library/MobileInstallation/MigrationInfo.plist</string>

```
