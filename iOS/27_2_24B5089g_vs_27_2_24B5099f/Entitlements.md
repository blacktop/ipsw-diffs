## 🔑 Entitlements

### filesystem

### AirDropUI

> `/Applications/AirDropUI.app/AirDropUI`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.menubar.hide-live-activity-settings</key>
+	<true/>
 	<key>com.apple.private.messages.collaboration-initiate-send</key>
 	<true/>
 	<key>com.apple.private.screentime-communication</key>

```
### CarPlaySettings

> `/Applications/CarPlaySettings.app/CarPlaySettings`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
+	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>
+	<true/>
 	<key>com.apple.private.CarAssetUtils.variants</key>
 	<true/>
 	<key>com.apple.private.CarPlayServices.icon-layout</key>

 	<array>
 		<string>/private/var/mobile/Library/CarPlay/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.caraccessoryframework.applinks</string>

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.aa.identity.xpc</string>
+		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.managedconfiguration.profiled.public</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>.GlobalPreferences</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.Accessibility</string>
 		<string>com.apple.SoundDetection</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.configurationprofiles</string>
+	</array>
 </dict>
 </plist>
 

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 			<integer>-48</integer>
 			<key>companionSetupFilters</key>
 			<array>
+				<dict>
+					<key>model</key>
+					<integer>3</integer>
+					<key>rssi</key>
+					<integer>-48</integer>
+				</dict>
+				<dict>
+					<key>model</key>
+					<integer>4</integer>
+					<key>rssi</key>
+					<integer>-48</integer>
+				</dict>
 				<dict>
 					<key>rssi</key>
 					<integer>-45</integer>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.private.action-button-events</key>
+	<true/>
 	<key>com.apple.springboard.private.capture-button-events</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.system-application</key>
+	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<true/>
 	<key>com.apple.springboard.126E27E0-D025-4A46-B2F1-AF49D4E0B105</key>
 	<true/>
+	<key>com.apple.springboard.SystemUIScene</key>
+	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
 	<key>com.apple.springboard.disallowControlCenter</key>

 	<true/>
 	<key>com.apple.springboard.private.action-button-events</key>
 	<true/>
-	<key>com.apple.springboard.sceneaccessory.prototyping</key>
-	<true/>
 	<key>com.apple.springboard.setVoiceControlEnabled</key>
 	<true/>
 	<key>com.apple.springboard.setWantsLockButtonEvents</key>

```
### HomeControlService

> `/Applications/HomeControlService.app/HomeControlService`

```diff

 	<true/>
 	<key>com.apple.private.homekit.cameraclips</key>
 	<true/>
+	<key>com.apple.private.homekit.delegate-granting</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### MediaRemoteUIService

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 	<key>com.apple.springboard.lockScreenContentAssertion</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 	<array>
 		<string>kern.exclaves_status</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleCredentialManagerUserClient</string>
+	</array>
 	<key>com.apple.seld.tsmmanager</key>
 	<true/>
 	<key>com.apple.seserviced.key</key>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.application-service-browse</key>

 	<array>
 		<string>kern.exclaves_status</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleCredentialManagerUserClient</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	</array>
 	<key>com.apple.private.game-center.bypass-authentication</key>
 	<true/>
+	<key>com.apple.private.healthcontentd</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>

 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 		<string>com.apple.generativeexperiences.agentSessionStore</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.healthcontentd</string>
 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>

 	<array>
 		<string>access-call-capabilities</string>
 		<string>access-calls</string>
+		<string>access-ui-data-source</string>
 		<string>modify-call-capabilities</string>
 		<string>access-call-providers</string>
 		<string>modify-call-providers</string>

```
### Siri AI

> `/Applications/Siri AI.app/Siri AI`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.intelligenceflow.contextTool</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.assistantd.odeon-remote</string>
 		<string>com.apple.companiond.xpc</string>

```
### CoreServicesUIAgent

> `/System/Library/CoreServices/CoreServicesUIAgent.app/CoreServicesUIAgent`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.AppReplacementRefused</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.GetAppReplacementSource</key>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.private.CallHistory.read</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.callhistoryd.service</string>
 		<string>com.apple.gamepolicyd.app.privileged</string>
+		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.appstored.xpc.jobmanager</string>
 		<string>com.apple.appstored.xpc.request</string>

```
### PhotosViewService

> `/System/Library/CoreServices/PhotosViewService.app/PhotosViewService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.no-guard-objects</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 		<string>UserSettings</string>
 		<string>Passcode</string>
 	</array>
+	<key>com.apple.manageddeviced.managed-apps.read</key>
+	<true/>
 	<key>com.apple.mediaremote.device-info</key>
 	<true/>
 	<key>com.apple.mediaremote.group-sessions</key>

 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
 		<string>com.apple.accessibility.MagnifierAngel</string>
 		<string>com.apple.aa.identity.xpc</string>
+		<string>com.apple.manageddeviced.managed-apps</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.osanalyticshelper</string>
 	<key>aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.SubmitDiagInfo.tower-access</key>
 	<true/>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.osanalyticshelper</string>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### AgeVerificationExtension

> `/System/Library/ExtensionKit/Extensions/AgeVerificationExtension.appex/AgeVerificationExtension`

```diff

 		<string>com.apple.MobileAsset.Vision.AgeEstimation</string>
 		<string>com.apple.MobileAsset.Vision.FaceLiveliness</string>
 	</array>
+	<key>com.apple.private.biometrickit.allow-connect</key>
+	<true/>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
+	<key>com.apple.private.biometrickit.allow-match</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/tmp/com.apple.AppleMediaServices/</string>

```

### 🆕 BTAppDataMigration

> `/System/Library/ExtensionKit/Extensions/BTAppDataMigration.appex/BTAppDataMigration`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.server.bluetooth.general.xpc</string>
	</array>
</dict>
</plist>

```

### 🆕 FileProviderSupersededAppReplacement

> `/System/Library/ExtensionKit/Extensions/FileProviderSupersededAppReplacement.appex/FileProviderSupersededAppReplacement`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.fileprovider.acl-write</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.fileprovider.superseded-app-replacement</key>
	<true/>
</dict>
</plist>

```
### InferenceProviderService

> `/System/Library/ExtensionKit/Extensions/InferenceProviderService.appex/InferenceProviderService`

```diff

 	<true/>
 	<key>com.apple.devicecheck.extension-client</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.updateVersionGatingRules</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 KeyboardAppMigration

> `/System/Library/ExtensionKit/Extensions/KeyboardAppMigration.appex/KeyboardAppMigration`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
	</array>
</dict>
</plist>

```

### 🆕 PerAppLanguageMigration

> `/System/Library/ExtensionKit/Extensions/PerAppLanguageMigration.appex/PerAppLanguageMigration`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.companionappd.connect.allow</key>
	<true/>
	<key>com.apple.companionappd.preferences.allow</key>
	<true/>
	<key>com.apple.localizationswitcher</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.localizationswitcherd</string>
		<string>com.apple.appconduitd.device-connection</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 PhotoLibraryInstallCoordinationExtension

> `/System/Library/ExtensionKit/Extensions/PhotoLibraryInstallCoordinationExtension.appex/PhotoLibraryInstallCoordinationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
</dict>
</plist>

```
### PrivacyAppIntents

> `/System/Library/ExtensionKit/Extensions/PrivacyAppIntents.appex/PrivacyAppIntents`

```diff

 	<string>com.apple.Preferences</string>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 </dict>
 </plist>
 

```
### ProximityReaderNFCExtension

> `/System/Library/ExtensionKit/Extensions/ProximityReaderNFCExtension.appex/ProximityReaderNFCExtension`

```diff

 	</array>
 	<key>com.apple.private.barcodesupport.allowNotifications</key>
 	<true/>
+	<key>com.apple.private.proximity-reader.engagement.customer</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```

### 🆕 ScreenTimeAppDataMigrationExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeAppDataMigrationExtension.appex/ScreenTimeAppDataMigrationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screen-time-settings</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ScreenTimeAgent.private</string>
		<string>com.apple.ScreenTimeSettingsAgent.private</string>
	</array>
</dict>
</plist>

```

### 🆕 ScreenTimeSettingsAppDataMigrationExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeSettingsAppDataMigrationExtension.appex/ScreenTimeSettingsAppDataMigrationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.screen-time-settings</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ScreenTimeSettingsAgent.private</string>
	</array>
</dict>
</plist>

```

### 🆕 AppleThunderboltSAT_TS

> `/System/Library/Extensions/AppleThunderboltSAT_TS.kext/AppleThunderboltSAT_TS`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.private.kernel.get-kext-info</key>
	<true/>
</dict>
</plist>

```

### 🆕 SiriHealthFlowTools

> `/System/Library/FlowTools/Tools/SiriHealthFlowTools.flowtool/SiriHealthFlowTools`

- No entitlements *(yet)*
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<string>com.apple.assetsd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>Photos</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Photos.Delete</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>PhotosIDCard</key>
 		<dict>
 			<key>Sets</key>

 	</array>
 	<key>com.apple.private.tcc.events.subscriber</key>
 	<true/>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.report</key>
 	<array>
 		<string>kTCCServicePhotos</string>

 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.MessageSecurity.MSTimestampXPCService</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.source</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FinanceImageProcessingService

> `/System/Library/Frameworks/FinanceKit.framework/XPCServices/FinanceImageProcessingService.xpc/FinanceImageProcessingService`

```diff

 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.email.maild</string>
+		<string>com.apple.icloudmailagent.secret.xpc</string>
 		<string>com.apple.tccd</string>
 		<string>com.apple.webkit</string>
 	</array>

```
### HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

```diff

 	</array>
 	<key>com.apple.private.wifivelocity</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/tmp/HKSV/</string>

```

### 🆕 NEAppReplacement

> `/System/Library/Frameworks/NetworkExtension.framework/PlugIns/NEAppReplacement.appex/NEAppReplacement`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.nehelper.privileged</key>
	<true/>
	<key>com.apple.private.networkextension.configuration</key>
	<string>super</string>
</dict>
</plist>

```

### 🆕 PassbookStoragePlugin

> `/System/Library/PreferenceBundles/StoragePlugins/PassbookStoragePlugin.bundle/PassbookStoragePlugin`

- No entitlements *(yet)*
### agentstored

> `/System/Library/PrivateFrameworks/AgentSessionKitRuntime.framework/agentstored`

```diff

 	<string>com.apple.GenerativeFunctions.agentstored</string>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>INTELLIGENCE_PLATFORM_AGENTSESSIONKIT</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.cfnetwork</string>

```
### AirPlaySenderService

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/XPCServices/AirPlaySenderService.xpc/AirPlaySenderService`

```diff

 	<true/>
 	<key>com.apple.PairingManager.Read</key>
 	<true/>
+	<key>com.apple.PairingManager.RemovePeer</key>
+	<true/>
 	<key>com.apple.PairingManager.Write</key>
 	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.maps.ipc-access</key>
 	<true/>
+	<key>com.apple.maps.suggestions.sources</key>
+	<true/>
 	<key>com.apple.mediaplayer.radio.private</key>
 	<true/>
 	<key>com.apple.mediaremote.device-info</key>

```
### CategoriesService

> `/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService`

```diff

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 </dict>
 </plist>
 

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.iconservices</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.transcript</string>

```
### ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

```diff

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueChipID</string>

 	</array>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.mobileactivationd</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAuthCPUserClient</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.mfiaccessory</string>
+	</array>
 </dict>
 </plist>
 

```
### DTServiceHub

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub`

```diff

 	<key>com.apple.private.agx.performance-spi</key>
 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>1</integer>
+	<integer>2</integer>
 	<key>com.apple.private.cpu-counters.system-control</key>
 	<true/>
 	<key>com.apple.private.cs.debugger.safe</key>

 	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
+	<key>com.apple.private.network.statistics</key>
+	<true/>
 	<key>com.apple.private.perfpowerservices.metricmonitor</key>
 	<true/>
 	<key>com.apple.private.pluginkit.manager</key>

```
### LeakAgent

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent`

```diff

 	<true/>
 	<key>com.apple.private.iosurfaceinfo</key>
 	<true/>
+	<key>com.apple.private.runtime-analysis-helper</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### RemoteInjectionAgent

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/RemoteInjectionAgent`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.runtime-analysis-helper</key>
+	<true/>
+</dict>
+</plist>
 

```
### com.apple.dt.instruments.dtsecurity

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity`

```diff

 	<key>com.apple.private.AppleProcessorTrace.Trace</key>
 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>1</integer>
+	<integer>2</integer>
 	<key>com.apple.private.host-exception-port-override</key>
 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>

```
### DeviceConfigurationAgent

> `/System/Library/PrivateFrameworks/DeviceConfiguration.framework/DeviceConfigurationAgent`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.deviceconfigurationd.consumer.private.async</string>
+		<string>com.apple.deviceconfigurationd.consumer.private</string>
 		<string>com.apple.deviceconfigurationd.publisher</string>
 		<string>com.apple.deviceconfigurationd.user.private.async</string>
 		<string>com.apple.duetactivityscheduler</string>
 	</array>
+	<key>com.apple.security.ts.tmpdir</key>
+	<array>
+		<string>com.apple.DeviceConfigurationAgent</string>
+	</array>
 </dict>
 </plist>
 

```
### deviceconfigurationd

> `/System/Library/PrivateFrameworks/DeviceConfiguration.framework/deviceconfigurationd`

```diff

 	<array>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
+	<key>com.apple.security.ts.tmpdir</key>
+	<array>
+		<string>com.apple.deviceconfigurationd</string>
+	</array>
 </dict>
 </plist>
 

```
### devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

 	<true/>
 	<key>com.apple.keystore.device.verify</key>
 	<true/>
+	<key>com.apple.mobileactivationd.recovery-activation-record</key>
+	<true/>
 	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
 	<true/>
 	<key>com.apple.private.CoreAnalytics.RolloverEvents.allow</key>

```
### BluetoothHeadset

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothHeadset.appex/BluetoothHeadset`

```diff

 	<array>
 		<string>com.apple.BTLELoggingManager.xpc</string>
 		<string>com.apple.bluetooth.xpc</string>
+		<string>com.apple.bluetoothuser.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>

```
### ContinuousRecordingsDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension`

```diff

 	<array>
 		<string>/Library/Logs/ContinuousRecordings/</string>
 	</array>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 </dict>
 </plist>
 

```
### IMDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/IMDiagnosticExtension`

```diff

 	<array>
 		<string>/Library/SMS/com.apple.imdpersistence.IMDIndexingThrottleHistory.plist</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.MobileSMS.CKDNDList</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.IMCoreSpotlight</string>

```
### donotdisturbd

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd`

```diff

 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.spotlight.SearchAgent</string>
 	</array>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 		<string>com.apple.nsurlsessiond</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.siriactionsd.xpc</string>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>

 	<true/>
 	<key>com.apple.timed</key>
 	<true/>
+	<key>com.apple.toolkit.request-immediate-indexing.allow</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>150</string>

 	</array>
 	<key>com.apple.triald.client</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.openai</string>

```
### healthcontentd

> `/System/Library/PrivateFrameworks/HealthContent.framework/healthcontentd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.healthcontentd</string>
-		<string>com.apple.storeservices.itfe</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
+		<key>com.apple.home-monitoring</key>
+		<string>com.apple.homekit</string>
 		<key>com.apple.homekit</key>
 		<string>com.apple.homekit</string>
 		<key>com.apple.homekit.camera.clips</key>

```
### identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

 	</array>
 	<key>com.apple.private.vfs.allow-low-space-writes</key>
 	<true/>
+	<key>com.apple.rapport.AccessPolicy</key>
+	<true/>
+	<key>com.apple.rapport.EndpointContext</key>
+	<true/>
 	<key>com.apple.rapport.LaunchListener</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.cloudtelemetryd</string>
+		<string>com.apple.rapport.AccessPolicy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>com.apple.tailspin.dump-output</key>
+	<true/>
 	<key>com.apple.telephony.cupolicy-monitor-access</key>
 	<true/>
 	<key>com.apple.terminusd.companionlink</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.nanobuddy</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.communicationSafetySettings</string>
-		<string>com.apple.MobileSMS.CKDNDList</string>
 		<string>com.apple.TelephonyUtilities</string>
 	</array>
 	<key>com.apple.private.translation</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.MobileSMS.CKDNDList</string>
 		<string>com.apple.trustkit</string>
 		<string>com.apple.onetimepasscodes</string>
 		<string>com.apple.MobileSMS</string>

```
### installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

 	<array>
 		<string>MDMInfo</string>
 	</array>
+	<key>com.apple.manageddeviced.managed-apps.read</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.CacheDelete</key>

 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.nanoprefsync</string>
 		<string>com.apple.managedappdistributiond.installcoordination</string>
+		<string>com.apple.manageddeviced.managed-apps</string>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.accountsd</string>
 		<string>com.apple.MobileInstallationHelperService</string>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 		<string>entitySimilarityFeatures</string>
 		<string>siriRemembers</string>
 	</array>
+	<key>com.apple.private.mediaexperience.systemcontroller.allowappstoinitiateplayback</key>
+	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```
### intentrecommendd

> `/System/Library/PrivateFrameworks/IntentRecommendRuntime.framework/intentrecommendd`

```diff

 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.linkd.application-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.maps.suggestions.sources</key>
+	<true/>
 	<key>com.apple.maps.virtualgarage.vehicles</key>
 	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-apac-codec</key>
 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>

 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.TapToRadarKit.service</string>
+	</array>
 </dict>
 </plist>
 

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.devicecheck.daemon-client</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>

```
### accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

 	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### auearlyboot

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/auearlyboot`

```diff

 	<string>com.apple.auearlyboot</string>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### UARPUpdaterServiceLegacyAudio

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceLegacyAudio.xpc/UARPUpdaterServiceLegacyAudio`

```diff

 	<string>com.apple.MobileAccessoryUpdater</string>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### NTKFaceSnapshotService

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/NTKFaceSnapshotService.xpc/NTKFaceSnapshotService`

```diff

 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.depth.divingd</string>
+		<string>com.apple.conversation-intelligence.service</string>
+		<string>com.apple.EligibilityQuorum.com.apple.AudioIntelligence</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### nanotimekitcompaniond

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond`

```diff

 		<string>com.apple.avatar.support</string>
 		<string>com.apple.avatar.service</string>
 		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.conversation-intelligence.service</string>
+		<string>com.apple.EligibilityQuorum.com.apple.AudioIntelligence</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.incoming-call-filter-server</string>
 		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.linkd.registry</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.idcredentials.biometrics</key>

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.visualintelligence.visual-action-prediction</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.suggestions</string>
+		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```diff

 	<true/>
 	<key>com.apple.private.settings-search-reindex</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

```
### spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

 		<string>com.apple.springboard.backgroundappservices</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.softwareupdateservicesd</string>
+		<string>com.apple.coremedia.figvirtualcapturecard.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### imageplaygroundd

> `/System/Library/PrivateFrameworks/SuggestedImage.framework/Support/imageplaygroundd`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.imageplaygroundd</string>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>Photos.Delete</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.imageplaygroundd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>com.apple.imageplaygroundd.PhotosDelete.reader</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Photos.Delete</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.duetactivityscheduler</string>
-		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.publisher.service.user</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.posterboardservices.dataModel</string>
 		<string>com.apple.ciphermld</string>

 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>
+	<key>com.apple.security.ts.mobile-keybag-access</key>
+	<true/>
 	<key>com.apple.springboard.fetchDisplayConfigs</key>
 	<true/>
 	<key>com.apple.springboard.wallpaper.display-configuration</key>

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 	<key>com.apple.private.healthkit.authorization_manager</key>
 	<array>
 		<string>reset</string>
+		<string>read</string>
 	</array>
 	<key>com.apple.private.healthkit.data-access-report</key>
 	<true/>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceMicrophoneInjection</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceBluetoothAlways</string>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	</array>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
+		<string>com.apple.private.alloy.contextsync</string>
+		<string>com.apple.private.alloy.contextsync.local</string>
 		<string>com.apple.private.alloy.shortcuts</string>
 		<string>com.apple.private.alloy.siri.voiceshortcuts</string>
 	</array>

```
### webprivacyd

> `/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.imcore.imremoteurlconnection</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>/Library/Caches/com.apple.WebPrivacy</string>
 		<string>/Library/Caches/com.apple.WebPrivacy/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.duetactivityscheduler</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.ids</string>
+		<string>com.apple.webprivacyd</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.webkit.bag</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>platform-application</key>

```
### itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 		<string>com.apple.kvsd</string>
 		<string>com.apple.fpsd</string>
 		<string>com.apple.fairplayd</string>
+		<string>com.apple.linkd.application-service</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```

### 🆕 SuggestedActionsSettings

> `/System/Library/Settings/SuggestedActionsSettings.settings/SuggestedActionsSettings`

- No entitlements *(yet)*
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
+	<key>com.apple.runningboard.tv</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.tvappservices.container</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.dataaccess.dataaccessd.PersistentPush</key>
 	<string>com.apple.Bridge</string>
+	<key>com.apple.developer.avfoundation.multitasking-camera-access</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 		<string>applinks:find.apple.com</string>
 		<string>applinks:find.apple.com.cn</string>
 	</array>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.findmy.findingui</key>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.ageRange</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.chrono.descriptorEnablement</key>
+	<array>
+		<string>com.apple.Fitness.FitnessWidget</string>
+	</array>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.chronoservices</string>
 		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.fitnessintelligenced</string>
 		<string>com.apple.frontboard.systemappservices</string>

 		<string>com.apple.siri.external_request</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ak.anisette.xpc</string>
+		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.appstored.xpc.jobmanager</string>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.locationd.place_inference</key>
+	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.private.homekit.cameraclips</key>
 	<true/>
+	<key>com.apple.private.homekit.delegate-granting</key>
+	<true/>
 	<key>com.apple.private.homekit.diagnostics</key>
 	<true/>
 	<key>com.apple.private.homekit.home-location</key>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.ciphermld</string>
 		<string>com.apple.generativeexperiences.ExternalProviderService</string>
 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 	</array>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.knowledge</key>

 	<true/>
 	<key>com.apple.maps.model-access</key>
 	<true/>
+	<key>com.apple.maps.suggestions.donations</key>
+	<true/>
+	<key>com.apple.maps.suggestions.predictions</key>
+	<true/>
 	<key>com.apple.maps.suggestions.signalpipeline</key>
 	<true/>
+	<key>com.apple.maps.suggestions.sources</key>
+	<true/>
 	<key>com.apple.maps.virtualgarage.vehicles</key>
 	<true/>
 	<key>com.apple.media.ringtones.read-only</key>

 		<string>com.apple.CarPlayApp.user-alerts-service</string>
 		<string>com.apple.safetyalerts</string>
 		<string>com.apple.jetpackassetd.xpc</string>
-		<string>com.apple.chrono.widgetcenterconnection</string>
+		<string>com.apple.chronoservices</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### GeneralMapsWidget

> `/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.maps.suggestions.donations</key>
+	<true/>
+	<key>com.apple.maps.suggestions.predictions</key>
+	<true/>
+	<key>com.apple.maps.suggestions.signalpipeline</key>
+	<true/>
+	<key>com.apple.maps.suggestions.sources</key>
+	<true/>
 	<key>com.apple.navigation.spi</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.rootless.storage.proactivepredictions</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Maps</string>

 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/DuetExpertCenter/streams/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.Maps.Suggestions/</string>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.appleaccount.custodian</key>
 	<true/>
+	<key>com.apple.appleaccount.identity.read</key>
+	<true/>
 	<key>com.apple.appstored.xpc.updates</key>
 	<true/>
 	<key>com.apple.assertiond.background-view-services</key>

 		<string>com.apple.aa.custodian.xpc</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.aa.inheritance.xpc</string>
+		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.symptom_diagnostics</string>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 	<array>
 		<string>H11ANEInDirectPathClient</string>
 		<string>AppleVirtIONeuralEngineDeviceUserClient</string>
+		<string>AppleCredentialManagerUserClient</string>
 	</array>
 	<key>com.apple.security.system-group-containers</key>
 	<array>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.shortcuts</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

```
### ContinuityCaptureAgent

> `/usr/libexec/ContinuityCaptureAgent`

```diff

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.avfoundation.capture.toggle-continuity-capture</key>
+	<true/>
 	<key>com.apple.private.cmio.extension.configuration</key>
 	<true/>
 	<key>com.apple.private.continuitycapture.audioinputprovider</key>

```
### aidearlyboot

> `/usr/libexec/aidearlyboot`

```diff

 	<string>com.apple.aidearlyboot</string>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 	<true/>
 	<key>com.apple.PairingManager.Read</key>
 	<true/>
+	<key>com.apple.PairingManager.RemovePeer</key>
+	<true/>
 	<key>com.apple.PairingManager.Write</key>
 	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>

```
### asktod

> `/usr/libexec/asktod`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2132707621</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.ams.bag</key>
+	<true/>
 	<key>com.apple.askto.extension.host</key>
 	<true/>
 	<key>com.apple.asktod.responseBroadcasting</key>

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.keystore.absinthe</key>
+	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.people.legacy.service.extension</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+		<string>SerialNumber</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.asktod</string>
 	<key>com.apple.private.biome.read-only</key>

 	<array>
 		<string>/Library/com.apple.asktod/</string>
 		<string>/Library/Caches/com.apple.asktod/</string>
+		<string>/Library/HTTPStorages/</string>
+		<string>/Library/com.apple.AppleMediaServices/PersistedBags/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.fairplayd.versioned</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<string>com.apple.asktod</string>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.store.ams.bag</key>
+	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

 	<array>
 		<string>com.apple.server.bluetooth.general.xpc</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant.backedup</string>
+	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
-	<key>com.apple.intelligenceplatform.Coordination</key>
-	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<string>com.apple.cloudd</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
-		<string>com.apple.intelligenceplatform.Coordination</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.userprofiles</string>
 		<string>com.apple.intelligencetasksd.sets.Maintenance</string>
 	</array>

```
### dasd

> `/usr/libexec/dasd`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.iokit.batterydataprecise</key>
+	<true/>
 	<key>com.apple.private.kernel.get-task-allow</key>
 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.powersource-read</key>
+	<true/>
 	<key>com.apple.private.systemstats.analysis-client</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### demod

> `/usr/libexec/demod`

```diff

 	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.corewifi.keychain</key>

```
### diagnosticextensionsd

> `/usr/libexec/diagnosticextensionsd`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.feedback</string>
+		<string>group.com.apple.diagnosticextensionsd</string>
 	</array>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.feedback</string>
+		<string>group.com.apple.diagnosticextensionsd</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>group.com.apple.feedback</string>
+		<string>group.com.apple.diagnosticextensionsd</string>
 		<string>com.apple.enhanced-logging-state</string>
 		<string>com.apple.diagnosticextensionsd</string>
 		<string>com.apple.DiagnosticExtensions.extensionTracker</string>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 	<true/>
 	<key>com.apple.private.WebClips.read-write</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### feedbackd

> `/usr/libexec/feedbackd`

```diff

 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>FeedbackDonationBulkDelete</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Feedback.TextToTextEvaluationData</string>
+				<string>Feedback.TextToImageEvaluationData</string>
+				<string>Feedback.TextImageToImageEvaluationData</string>
+			</array>
+		</dict>
 		<key>FeedbackDonationFetch</key>
 		<dict>
 			<key>Streams</key>

 	<array>
 		<string>/Library/Cookies/</string>
 		<string>/Library/HTTPStorages/com.apple.feedbackd/</string>
+		<string>/tmp/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<string>com.apple.inputanalyticsd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageFailureReason</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.FailureReason</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageImageInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 		<string>spi</string>
 		<string>identity</string>
 	</array>
+	<key>com.apple.DeviceRecovery.Control</key>
+	<true/>
+	<key>com.apple.DeviceRecovery.RestrictEraseAndUpdate</key>
+	<true/>
 	<key>com.apple.GAX.SPI</key>
 	<true/>
 	<key>com.apple.MobileInternetSharing.allow</key>

```
### memoryanalyticsd

> `/usr/libexec/memoryanalyticsd`

```diff

 	</array>
 	<key>com.apple.system-task-ports.read</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>MEMORY_ANALYSIS_MODEL_LOADING</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>appleaccount</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	</array>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>
+	<key>com.apple.rapport.AccessPolicy</key>
+	<true/>
 	<key>com.apple.rapport.Client</key>
 	<true/>
 	<key>com.apple.rapport.NearbyInvitation</key>

 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.rapport</string>
+		<string>com.apple.rapport.AccessPolicy</string>
 		<string>com.apple.rapport.NearbyInvitation</string>
 		<string>com.apple.securityd.ckks</string>
 		<string>com.apple.SharedWebCredentials</string>

```
### remindd

> `/usr/libexec/remindd`

```diff

 	<string></string>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.reminders</string>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.feedbackd.client-forms</key>
 	<array>
 		<string>framework-reminders-grocerylist</string>

```
### routined

> `/usr/libexec/routined`

```diff

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>LOMO_CHECK_IN</string>
+		<string>MOMENTS_TRIAL</string>
 	</array>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>

```
### securepairingd

> `/usr/libexec/securepairingd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

 	<array>
 		<string>/private/var/tmp/</string>
 		<string>/private/var/mobile/tmp/AudioCapture/</string>
+		<string>/private/var/mobile/tmp/com.apple.audiomxd/AudioCapture/adm/</string>
 		<string>/dev/exfiltration-adc-securepairi</string>
 	</array>
 	<key>com.apple.security.hardened-process</key>

```
### toolkitd

> `/usr/libexec/toolkitd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.contextsync</string>
+		<string>com.apple.private.alloy.contextsync.local</string>
+	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.shortcuts</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
+	<key>com.apple.private.homekit.home-location</key>
+	<true/>
+	<key>com.apple.private.homekit.location</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>tvremoted</string>
 	<key>com.apple.private.tcc.allow</key>

```
### uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

 	<true/>
 	<key>com.apple.uarpassetmanagerservice.uarp</key>
 	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### uarpd

> `/usr/libexec/uarpd`

```diff

 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocation</key>
-	<true/>
-	<key>com.apple.security.hardened-processs.checked-allocations.soft-mode</key>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>

```


