## 🔑 Entitlements

### filesystem

### AskPermissionUI

> `/Applications/AskPermissionUI.app/AskPermissionUI`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>409835401</string>
 	<key>application-identifier</key>
 	<string>com.apple.AskPermissionUI</string>
 	<key>com.apple.UIKit.vends-view-services</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.adid</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.adid</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.cdp.daemon</string>
+		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.xpc.amsengagementd</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOMobileFramebufferUserClient</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>1445028844</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### ClarityPhotos

> `/Applications/ClarityPhotos.app/ClarityPhotos`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Media/PhotoData/Caches/</string>
+		<string>/Media/PhotoData/PhotoCloudSharingData/</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.ClarityUI.Photos</string>

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 	<true/>
 	<key>com.apple.bluetooth.discovery</key>
 	<dict>
+		<key>AddUser</key>
+		<dict>
+			<key>bleRSSIThresholdHint</key>
+			<integer>-45</integer>
+			<key>denyProductList</key>
+			<array>
+				<string>iPad7,11</string>
+				<string>iPad7,12</string>
+				<string>iPhone11,2</string>
+				<string>iPhone11,4</string>
+				<string>iPhone11,6</string>
+				<string>iPhone11,8</string>
+			</array>
+			<key>discoveryTypes</key>
+			<array>
+				<string>AddUser</string>
+			</array>
+			<key>sceneIdentifier</key>
+			<string>addUser</string>
+			<key>screenLocked</key>
+			<true/>
+			<key>setupDone</key>
+			<true/>
+			<key>systemUnlocked</key>
+			<true/>
+		</dict>
 		<key>MainSetup</key>
 		<dict>
 			<key>bleRSSIThresholdHint</key>

 					<key>rssi</key>
 					<integer>-48</integer>
 				</dict>
+				<dict>
+					<key>model</key>
+					<integer>5</integer>
+					<key>rssi</key>
+					<integer>-48</integer>
+				</dict>
+				<dict>
+					<key>model</key>
+					<integer>10</integer>
+					<key>rssi</key>
+					<integer>-45</integer>
+				</dict>
+				<dict>
+					<key>model</key>
+					<integer>11</integer>
+					<key>rssi</key>
+					<integer>-45</integer>
+				</dict>
 				<dict>
 					<key>rssi</key>
 					<integer>-45</integer>

 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
 		<string>com.apple.MobileAsset.SoftwareUpdate</string>
 		<string>com.apple.MobileAsset.SoftwareUpdateDocumentation</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsTV</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/Caches/com.apple.homed/Snapshots/</string>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 		<string>/Library/DuetExpertCenter/</string>
 	</array>

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.nexus</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.proactive.DefaultWidgetSuggester</string>
 		<string>com.apple.ScreenTimeAgent.persistence</string>
 		<string>com.apple.ScreenTimeAgent.private</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.SharingServices</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.siri.orchestration.capabilities</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.sucontrollerd</string>
 		<string>com.apple.systemstatus.activityattribution</string>
 		<string>com.apple.TextInput.user-directory-trader-server</string>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.Accessibility</string>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.CompanionSetupKit</string>
 		<string>com.apple.coreaudio</string>
 	</array>

 		<string>com.apple.passd.library</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.proactive.DefaultWidgetSuggester</string>
 		<string>com.apple.ScreenTimeAgent.persistence</string>
 		<string>com.apple.ScreenTimeAgent.private</string>
 		<string>com.apple.security.octagon</string>

```
### Diagnostic-8357

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8357.appex/Diagnostic-8357`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.diagnostic-intelligence</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.DiagnosticsService.Diagnostic-8357</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 	<array>
 		<string>/private/var/mobile/Library/Logs/AppleSupport/</string>
 		<string>/private/var/logs/AppleSupport/</string>
+		<string>/private/var/mobile/Library/Logs/CrashReporter/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.diagnosticservicesd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.corespeech.uitrainingservice</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### HomeControlService

> `/Applications/HomeControlService.app/HomeControlService`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.home.extension-host</key>
+	<true/>
 	<key>com.apple.private.homekit.allow-secure-access</key>
 	<true/>
 	<key>com.apple.private.homekit.cameraclips</key>

 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceWillow</string>
+	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceWillow</string>
+	</array>
+	<key>com.apple.runningboard.home-extensions</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.Home.group</string>

```

### 🆕 HomeProximityDynamicIslandUIService

> `/Applications/HomeProximityDynamicIslandUIService.app/HomeProximityDynamicIslandUIService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Home.ProximityDynamicIslandUIService</string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.developer.homekit</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.homekit.private-spi-access</key>
	<true/>
	<key>com.apple.private.homekit.allow-secure-access</key>
	<true/>
	<key>com.apple.private.sessionkit.custom-platter-target</key>
	<true/>
	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
	<true/>
	<key>com.apple.private.sessionkit.sessionRequest</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.matter.native.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.matter.native.xpc</string>
	</array>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
</dict>
</plist>

```
### HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.corespeech.uitrainingservice</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.allow-setup-payload</key>

 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.voicetrigger.notbackedup</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	<array>
 		<string>read</string>
 	</array>
+	<key>com.apple.conversation-accessibility.required-host-entitlement</key>
+	<true/>
 	<key>com.apple.coreaudio.CanTapTelephony</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.duetexpertd.SettingsActions</key>
 	<true/>
+	<key>com.apple.duetexpertd.assistant-actions</key>
+	<true/>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<array>
 		<string>com.apple.ams-identity-verification</string>
 	</array>
+	<key>com.apple.corespeech.uitrainingservice</key>
+	<true/>
 	<key>com.apple.coretelephony.Calls.allow</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

 		<string>com.apple.sharing.Setup</string>
 		<string>com.apple.sharing.iOSSetup</string>
 	</array>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 	<key>com.apple.softposreaderd.provision</key>
 	<true/>
 	<key>com.apple.softposreaderd.unifiedreader</key>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<array>
 		<string>com.apple.ams-identity-verification</string>
 	</array>
+	<key>com.apple.corespeech.uitrainingservice</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

```
### Siri AI

> `/Applications/Siri AI.app/Siri AI`

```diff

 	<true/>
 	<key>com.apple.carousel.flashlight.access</key>
 	<true/>
+	<key>com.apple.carousel.nonmatchingsessions</key>
+	<true/>
 	<key>com.apple.chrono.controlcenter</key>
 	<true/>
 	<key>com.apple.chrono.controls</key>

 	</array>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.appintents.live-entities.read</key>
+	<true/>
 	<key>com.apple.private.appintents.trusted-entity-identifier</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appintents.LiveEntityService</string>
 		<string>com.apple.intelligenceflow.contextTool</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.assistantd.odeon-remote</string>

 		<string>com.apple.iCloudQuotaUI.RemoteiCloudQuotaUI.viewservice</string>
 		<string>com.apple.internal.SpotlightAutomationTester</string>
 		<string>com.apple.carousel.flashlightxpcservice</string>
+		<string>com.apple.carousel.sessionservice</string>
 		<string>com.apple.realitysystemsupport.hid_server_backboard</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.remindd.userInteractive</string>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.AXMediaUtilitiesService-access</key>
+	<true/>
 	<key>com.apple.BackBoard.global-mouse-events</key>
 	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AXMediaUtilitiesService</string>
 		<string>com.apple.Feedback.DraftingExtension.viewservice</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>

 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>
 		<string>com.apple.iphone.axserver</string>
+		<string>com.apple.AXMediaUtilitiesService</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.manageddeviced.managed-apps.read</key>
+	<true/>
 	<key>com.apple.mediaexperience.endpoint.xpc</key>
 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>

 		<string>com.apple.assistant.request-dispatcher.uibridge-service</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.installcoordinationd</string>
+		<string>com.apple.manageddeviced.managed-apps</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>

```
### ClarityBoard

> `/System/Library/CoreServices/ClarityBoard.app/ClarityBoard`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.manageddeviced.managed-apps.read</key>
+	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.dt.xctestd.target</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.manageddeviced.managed-apps</string>
 		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.coremedia.mediaplaybackd.asset.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.player.xpc</string>

```
### CoreServicesUIAgent

> `/System/Library/CoreServices/CoreServicesUIAgent.app/CoreServicesUIAgent`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.manageddeviced.managed-apps.read</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.AppReplacementRefused</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.GetAppReplacementSource</key>

 		<string>com.apple.lsd.open</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.manageddeviced.managed-apps</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 MobileDevices-0004

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0004.bundle/MobileDevices-0004`

- No entitlements *(yet)*
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.servicesintelligence</key>
+	<true/>
 	<key>com.apple.private.storekit</key>
 	<array>
 		<string>AdvancedPurchase</string>

```

### 🆕 HomeDeveloperSettingsIntents

> `/System/Library/ExtensionKit/Extensions/HomeDeveloperSettingsIntents.appex/HomeDeveloperSettingsIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
</dict>
</plist>

```
### QuickLookUIExtension

> `/System/Library/ExtensionKit/Extensions/QuickLookUIExtension.appex/QuickLookUIExtension`

```diff

 		<string>com.apple.siri.activation</string>
 		<string>com.apple.siri.activation.service</string>
 		<string>com.apple.proactive.visual-action-prediction</string>
+		<string>com.apple.visualintelligence.visual-action-prediction</string>
 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>
 		<string>com.apple.sage.summarization</string>

 	<array>
 		<string>access-call-providers</string>
 	</array>
+	<key>com.apple.visualintelligence.private.visual-action-prediction</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.Markup</string>

```
### TextInputAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/TextInputAppIntentsExtension.appex/TextInputAppIntentsExtension`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict/>
+<dict>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.keyboard.preferences</string>
+		<string>com.apple.assistant.support</string>
+	</array>
+</dict>
 </plist>
 

```

### 🆕 HomeDeveloperSettings

> `/System/Library/PreferenceBundles/HomeDeveloperSettings.bundle/HomeDeveloperSettings`

- No entitlements *(yet)*
### CategoriesService

> `/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```
### donotdisturbd

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd`

```diff

 	<true/>
 	<key>com.apple.personalization.notificationCategorization</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```

### 🆕 MedicalIDFollowUpExtension

> `/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/MedicalIDFollowUpExtension.appex/MedicalIDFollowUpExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.Health</string>
	</dict>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.medicaliddata</key>
	<true/>
	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.corefollowup.agent</string>
		<string>com.apple.healthappd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.private.healthkit.medicaliddata</string>
		<string>com.apple.private.healthkit</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.intelligentrouting.recommendationservice</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.keystore.info</key>

 	<array>
 		<string>com.apple.Home.ControlCenter</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corespotlight.bundleid</key>
 	<string>com.apple.homed</string>
 	<key>com.apple.private.corespotlight.internal</key>

 	<true/>
 	<key>com.apple.private.get-system-corpse</key>
 	<true/>
+	<key>com.apple.private.home.extension-host</key>
+	<true/>
 	<key>com.apple.private.home.hindsight.read</key>
 	<true/>
 	<key>com.apple.private.home.hindsight.write</key>

 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/containers/Bundle/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.NetworkInfo.DiagnosticExtension.apple-extension-service</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.ProductKitService</string>
 		<string>com.apple.audio.hapticd</string>
+		<string>com.apple.audio.SystemSoundServer-iOS</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>systemgroup.com.apple.ReportMemoryException</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/containers/Bundle/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.assistant.settings</string>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 		<string>private-controller-api</string>
 		<string>private-provider-api</string>
 	</array>
-	<key>com.apple.developer.homekit</key>
-	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
-	<key>com.apple.private.homekit</key>
-	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>ContextRetrieval</key>

 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.coreservices.quarantine-resolver</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
-		<string>com.apple.homed.xpc</string>
 		<string>com.apple.siri.device_resolution</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.public</string>
 		<string>com.apple.TelephonyUtilities</string>
-		<string>com.apple.homed</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

 	<string>com.apple.NeighborhoodActivityConduitService</string>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.conversation-accessibility.required-host-entitlement</key>
+	<true/>
 	<key>com.apple.developer.conversation-accessibility</key>
 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.phoneNumberResolver</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<key>value</key>
 		<string>com.apple.FaceTime</string>
 	</dict>
+	<key>com.apple.private.communicationsfilter</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.icfcallserver</key>
 	<true/>
+	<key>com.apple.private.ids.idquery-cache</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>

 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
 	</array>
+	<key>com.apple.private.ids.phone-number-authentication</key>
+	<true/>
 	<key>com.apple.private.ids.registration</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
 	</array>
+	<key>com.apple.private.ids.report-spam-message</key>
+	<true/>
 	<key>com.apple.private.ids.self-session</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>

 	</array>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.imcore.imremoteurlconnection</key>
+	<true/>
+	<key>com.apple.private.imcore.spi.database-access</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	<array>
 		<string>com.apple.mobilephone</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Caches/com.apple.businessservicesd/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/CallHistoryDB/</string>

 		<string>com.apple.incoming-call-filter-server</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.businessservicesd</string>
+		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
+		<string>com.apple.incoming-call-filter-server</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.allowallcallurls</key>
 	<true/>
+	<key>com.apple.system.get-alert-tone</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```

### 🆕 pebbleplayd

> `/System/Library/PrivateFrameworks/PebblePlayDaemon.framework/pebbleplayd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-access-to-device-list</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.mediaremote.now-playing-read-access</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.lookup</key>
	<dict>
		<key>appData</key>
		<true/>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.mediaexperience.systemcontroller.allowappstoinitiateplayback</key>
	<true/>
	<key>com.apple.private.mobileinstall.allowedSPI</key>
	<array>
		<string>CreateSerializedPlaceholder</string>
	</array>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.endowment-originator</key>
	<true/>
	<key>com.apple.runningboard.invalidateanyassertion</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.primitiveattribute</key>
	<true/>
	<key>com.apple.runningboard.targetidentities</key>
	<true/>
	<key>com.apple.runningboard.terminateprocess</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mobile.installd</string>
		<string>com.apple.dmd.policy</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.misagent</string>
		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
		<string>com.apple.mobile.usermanagerd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.newscore</string>
		<string>com.apple.newscore2</string>
	</array>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.ts.read-any-bundle</key>
	<true/>
</dict>
</plist>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<array>
 		<string>read</string>
 	</array>
+	<key>com.apple.conversation-accessibility.required-host-entitlement</key>
+	<true/>
 	<key>com.apple.conversation-recording.required-host-entitlement</key>
 	<true/>
 	<key>com.apple.coreaudio.private.HasMicrophoneInjectionAccess</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	</array>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.proactiveagentplatform.group-identifier</key>
 	<string>com.apple.shortcuts</string>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
+	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
+	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
 	<true/>
 	<key>com.apple.private.coremedia.pidinheritance.allow</key>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 		<string>com.apple.replaykit.AudioConferenceControlCenterModule</string>
 		<string>com.apple.replaykit.VideoConferenceControlCenterModule</string>
 	</array>
+	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
+	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
 	<true/>
 	<key>com.apple.private.coreaudio.viewInterruptorName.allow</key>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.locationd.status</key>
 	<true/>
+	<key>com.apple.locationd.stored_location</key>
+	<true/>
 	<key>com.apple.locationd.time_zone</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>

```
### merchantd

> `/usr/libexec/merchantd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.payment.remote-network-payment-host-initiate</key>
 	<true/>
 	<key>com.apple.private.payment.remote-network-payment-initiate</key>

```
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.nearbyd</string>
+	<key>com.apple.AccessorySensorManager</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

 	<true/>
 	<key>com.apple.aop.hid-driver.hid-service.pdr</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>eclipse</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.aop.rose.controller.admin</key>
 	<true/>
 	<key>com.apple.aop.user-client</key>

 	</dict>
 	<key>com.apple.backboardd.launchapplications</key>
 	<true/>
+	<key>com.apple.backlight.allowsActivationObservation</key>
+	<true/>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.hid.system.fast-path-motion-event-privileged</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.locationd.Proximity.TagManagement</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
+	<key>com.apple.locationd.asmanager</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.gnss-extensions</key>
 	<true/>
 	<key>com.apple.locationd.inertialodometry</key>
 	<true/>
+	<key>com.apple.locationd.motion_alarms-system-client</key>
+	<true/>
 	<key>com.apple.locationd.slv_configurer</key>
 	<true/>
 	<key>com.apple.locationd.spectator</key>

 	<true/>
 	<key>com.apple.private.avfoundation.metadata-cameras.allow</key>
 	<true/>
+	<key>com.apple.private.breadboard.privacy.read</key>
+	<array>
+		<string>passive-camera</string>
+	</array>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.corewifi.countrycode</key>

 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
+	<key>com.apple.private.hid.client.motion-event-privileged</key>
+	<true/>
 	<key>com.apple.private.hid.client.service-protected</key>
 	<true/>
 	<key>com.apple.private.mediasafetynet.exception.nearbyprecisionfinding</key>

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.cvhwa.xpc</string>
 		<string>com.apple.mediasafetynet.exceptions.cam</string>
+		<string>com.apple.breadboardservices</string>
+		<string>com.apple.AccessorySensorManager</string>
+		<string>com.apple.BacklightServices.backlight</string>
 		<string>com.apple.DeviceAccess.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.backboardd.replayClone</key>
 	<true/>
+	<key>com.apple.backboardd.touchStreams</key>
+	<true/>
 	<key>com.apple.backboardd.virtualDisplay</key>
 	<true/>
 	<key>com.apple.coreaudio.app-tap</key>

 	</array>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.skylight.event-tap.direct-touch</key>
+	<true/>
 	<key>com.apple.private.skylight.expanse</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### sharereportingd

> `/usr/libexec/sharereportingd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.sharereportingd</string>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit-Anonymous</string>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 		<string>com.apple.cloudd</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.controlcenter.remoteservice</string>
+		<string>com.apple.EligibilityQuorum.com.apple.AudioIntelligence</string>
 		<string>com.apple.enroll.state</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<true/>
 	<key>com.apple.homepodaccessorysettings.client</key>
 	<true/>
+	<key>com.apple.icloud.findmydeviced.localfindable</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.localfindable.tvremote</key>
 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>

 		<string>com.apple.watchlistd.xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>
+		<string>com.apple.icloud.findmydeviced.localfindable</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```


### AppOS

### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
+	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Unilog.SafariSearch.Stage</string>

```


