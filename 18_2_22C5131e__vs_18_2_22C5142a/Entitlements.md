## 🔑 Entitlements

### AppProtectionUIHost

> `/Applications/AppProtectionUIHost.app/AppProtectionUIHost`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.seserviced.contactlessCredential.settings</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>

```
### PeopleViewService

> `/Applications/PeopleViewService.app/PeopleViewService`

```diff

 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.spotlightui</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.people</string>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.lockup-buy-params</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents.media-client-id</key>
 	<string>com.apple.searchui</string>
 	<key>com.apple.private.appstorecomponents.media-client-version</key>

 		<string>UIStatusBarStyleOverrideFullScreenWebRTCCapture</string>
 		<string>UIStatusBarStyleOverrideFullScreenWebRTCAudioCapture</string>
 	</array>
+	<key>com.apple.springboard.swapIconsInProminentPositions</key>
+	<true/>
 	<key>com.apple.springboard.webClipService</key>
 	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.contactsui</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.shortcuts</string>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.ids</string>
 		<string>com.apple.PrototypeTools</string>
+		<string>com.apple.camera</string>
 		<string>com.apple.Bridge</string>
 		<string>/var/preferences/com.apple.networkextension.control</string>
 		<string>com.apple.TelephonyUtilities</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.SpringBoard.ReadyForRestore</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.donotdisturb.0191488e-ff8a-728d-a9f7-08a0a77abd7d.update.client-identifiers</key>

```

### 🆕 PhotosAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PhotosAppIntentsExtension.appex/PhotosAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>com.apple.VideoSubscriberAccount.DeveloperService</key>
 	<true/>
 	<key>com.apple.VideoSubscriberAccount.PrivacyService</key>

 	<array>
 		<string>com.apple.VideoSubscriberAccount.PrivacyService</string>
 		<string>com.apple.VideoSubscriberAccount.DeveloperService</string>
+		<string>com.apple.adid</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.appprotectiond.read</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.TelephonyUtilities</string>
+	</array>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-call-providers</string>

```
### com.apple.SafariServices.ContentBlockerLoader

> `/System/Library/Frameworks/SafariServices.framework/XPCServices/com.apple.SafariServices.ContentBlockerLoader.xpc/com.apple.SafariServices.ContentBlockerLoader`

```diff

 	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.safari</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Bundle/Application/</string>

```

### 🆕 PaymentContactlessUIPlugin

> `/System/Library/PreferenceBundles/PaymentContactlessUIPlugin.bundle/PaymentContactlessUIPlugin`

- No entitlements *(yet)*
### AAUIFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.ucrt.healing.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.imagent</key>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
 	<key>com.apple.runningboard.jetengine</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.availability.internal</string>

```
### CDPFollowUpExtension

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.backboardd.replacesystemapp</key>
 	<true/>
 	<key>com.apple.businessservicesd.prefetch</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.mobile.installd</string>
+        <string>com.apple.sysdiagnose.service.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>GetSystemAppMigrationStatus</string>
 		<string>WaitForSystemAppMigrationToComplete</string>
 	</array>
+    <key>com.apple.private.sysdiagnose</key>
+    <true/>
+    <key>com.apple.security.exception.process-info</key>
+    <true/>
 </dict>
 </plist>
 

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<array>
 		<string>IntelligenceFlow.JointResolverTelemetry</string>
 		<string>IntelligenceEngine.Interaction.Donation</string>
+		<string>IntelligenceFlow.PlanResolutionTelemetry</string>
 		<string>IntelligenceFlow.QueryDecorationTelemetry</string>
 		<string>IntelligenceFlow.Telemetry</string>
 		<string>IntelligenceFlow.ResponseGeneration</string>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/knowledgeconstructiond`

```diff

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>App.InFocus</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Autonaming.Messages.Inferences</key>
 				<dict>
 					<key>mode</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	</dict>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>GetSystemAppMigrationStatus</string>
+	</array>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.mobile.installd</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.sessionservices</string>

 	<array>
 		<string>180</string>
 	</array>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>V568VXD5P8.is.workflow.my.app</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.shortcuts</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.shortcuts</string>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
+	<key>com.apple.private.healthkit</key>
+	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>
 	<array>
 		<string>com.apple.shortcuts</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.lsd.mapdb</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 		<string>UIStatusBarStyleOverrideWebRTCCapture</string>
 		<string>UIStatusBarStyleOverrideWebRTCAudioCapture</string>
 	</array>
+	<key>com.apple.springboard.swapIconsInProminentPositions</key>
+	<true/>
 	<key>com.apple.springboard.systemNotesPresentation</key>
 	<true/>
 	<key>com.apple.springboard.wallpaperAnimationSuspension</key>

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

### 🆕 com.apple.Safari.SandboxBroker

> `/private/var/staged_system_apps/MobileSafari.app/XPCServices/com.apple.Safari.SandboxBroker.xpc/com.apple.Safari.SandboxBroker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.mobilesafari</string>
	</dict>
	<key>com.apple.private.imcore.spi.database-access</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/SMS/Attachments/</string>
		<string>/Containers/Data/Application/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleJPEGDriverUserClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
		<string>com.apple.trustd</string>
		<string>com.apple.webprivacyd</string>
		<string>com.apple.symptom_diagnostics</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.imessage.bag</string>
		<string>com.apple.MobileSMS</string>
		<string>com.apple.ids</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Safari.SandboxBroker</string>
	</array>
</dict>
</plist>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>259</string>
+	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>
 		<integer>0</integer>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
+	<key>com.apple.private.kernel.jetsam</key>
+	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.mako.status</key>

 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceExposureNotification</string>
 	</array>
+	<key>com.apple.private.write-kr-experiment-factors</key>
+	<true/>
 	<key>com.apple.private.xpc.allowed-get-service-name</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.service-stats</key>

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>259</string>
+	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>
 		<integer>0</integer>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>259</string>
+	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>
 		<integer>0</integer>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.inputanalyticsd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>GeneratedImageUserInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>

```
### nptocompaniond

> `/usr/libexec/nptocompaniond`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.lsd.mapdb</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

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
