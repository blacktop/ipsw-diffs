## 🔑 Entitlements

### filesystem

### AVKitRoutingService

> `/Applications/AVKitRoutingService.app/AVKitRoutingService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.suppressrecordingstatetosystemstatus</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.useindependentinputaudioresourcesession</key>

```
### AuthKitUIService

> `/Applications/AuthKitUIService.app/AuthKitUIService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.owner</key>
 	<true/>
+	<key>com.apple.authkit.writer.internal</key>
+	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
 	<key>com.apple.cdp.utility</key>

 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-calls</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### CarPlaySettings

> `/Applications/CarPlaySettings.app/CarPlaySettings`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.systemsettings.extensions</string>
+	</array>
 </dict>
 </plist>
 

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 					<key>model</key>
 					<integer>3</integer>
 					<key>rssi</key>
-					<integer>-48</integer>
+					<integer>-46</integer>
 				</dict>
 				<dict>
 					<key>model</key>
 					<integer>4</integer>
 					<key>rssi</key>
-					<integer>-48</integer>
+					<integer>-46</integer>
 				</dict>
 				<dict>
 					<key>model</key>
 					<integer>5</integer>
 					<key>rssi</key>
-					<integer>-48</integer>
+					<integer>-46</integer>
 				</dict>
 				<dict>
 					<key>model</key>
 					<integer>10</integer>
 					<key>rssi</key>
-					<integer>-45</integer>
+					<integer>-43</integer>
 				</dict>
 				<dict>
 					<key>model</key>
 					<integer>11</integer>
 					<key>rssi</key>
-					<integer>-45</integer>
+					<integer>-43</integer>
 				</dict>
 				<dict>
 					<key>rssi</key>

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.corespeech.uitrainingservice</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.game-center</key>
 	<array>
 		<string>Account</string>

 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.companionsetup.diagnostics</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

 		<string>com.apple.SharingServices</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.siri.orchestration.capabilities</string>
+		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.sucontrollerd</string>

 	<true/>
 	<key>com.apple.timed</key>
 	<true/>
+	<key>com.apple.wifi.eap-nearby-device-setup-config-copy</key>
+	<true/>
 	<key>com.apple.wifip2pd</key>
 	<true/>
 	<key>com.apple.wlan.authentication</key>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.TextUnderstanding.process</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.TextUnderstanding.process</string>
 		<string>com.apple.corerecents.recentsd</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.appprotectiond.read</string>

```
### Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.orientation-lock-service</key>
+	<true/>
 	<key>com.apple.springboard.private.59482219-3102-41D6-BD94-8956D5D52CB6</key>
 	<true/>
 	<key>com.apple.springboard.private.9403EBFD-90B8-4676-84BF-9F38143337E3</key>

```
### DockFolderViewService

> `/Applications/DockFolderViewService.app/DockFolderViewService`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FinanceUIService

> `/Applications/FinanceUIService.app/FinanceUIService`

```diff

 	<array>
 		<string>com.apple.FinanceKit</string>
 	</array>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>FINANCE_ORDER_EXTRACTION</string>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.corespeech.uitrainingservice</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssetsIPad</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>

 		<string>com.apple.sharingd.b332setup</string>
 		<string>com.apple.sharingd</string>
 		<string>com.apple.SharingServices</string>
+		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 		<string>com.apple.soundboardservices.server</string>
 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

 		<string>com.apple.wifi.manager</string>
 		<string>com.apple.wirelessproxd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
-		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.MobileStoreDemo.test</string>
 		<string>com.apple.TouchRemote</string>

 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.AppleMediaServices.notbackedup</string>
+		<string>com.apple.assistant.backedup</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.registry</string>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
+	<key>com.apple.backboardd.displayTraits</key>
+	<true/>
 	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
 	<true/>
 	<key>com.apple.bannerkit.post</key>

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>DisplayExtendedProperties</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.activitykit.bypassAuthorizationUI</key>

 		<string>com.apple.biome.compute.publisher.service.user</string>
 		<string>com.apple.communicationtrustd.service</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.backboard.display.services</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.springboard.sceneaccessory.prototyping</key>
+	<true/>
 	<key>com.apple.springboard.shortcutitems.fullaccess</key>
 	<true/>
 	<key>com.apple.springboard.stark.activateRemoteAlert</key>

```

### 🆕 MagnifierAngelExtension

> `/Applications/MagnifierAngel.app/Extensions/MagnifierAngelExtension.appex/MagnifierAngelExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.accessibility.MagnifierAngel.MagnifierAngelExtension</string>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.accessibility.voiceover</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.aned.private.ANEAccess.allow</key>
	<true/>
	<key>com.apple.aned.private.adapterWeight.allow</key>
	<true/>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.appleneuralengine</key>
	<true/>
	<key>com.apple.appleneuralengine.private.allow</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
	<true/>
	<key>com.apple.developer.declared-age-range</key>
	<true/>
	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.AXIconVision</string>
		<string>com.apple.MobileAsset.ImageCaptionModel</string>
		<string>com.apple.MobileAsset.AXElementVision</string>
		<string>com.apple.MobileAsset.MagnifierAsset</string>
		<string>com.apple.MobileAsset.VideoIntelligence</string>
	</array>
	<key>com.apple.private.avfoundation.background-camera-access</key>
	<true/>
	<key>com.apple.private.avfoundation.capture.allow</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.incubation.sideloader</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.coremedia.extensions.audiorecording</key>
	<true/>
	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
	<array>
		<string>com.apple.Accessibility</string>
	</array>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/assets</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VideoIntelligence/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>H15ANEInDirectPathClient</string>
		<string>IOSurfaceAcceleratorClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.accessibility.AXSpringBoardServer</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.linkd.mediator</string>
		<string>com.apple.securityd.systemkeychain</string>
		<string>com.apple.networkserviceproxy</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.speech.localspeechrecognition</string>
		<string>com.apple.ax.MauiTTSSupport.MauiAUSP</string>
		<string>com.apple.ax.MauiTTSSupport.MauiAUSP.apple-extension-service</string>
		<string>com.apple.texttospeech.SiriAUSP</string>
		<string>com.apple.texttospeech.SiriAUSP.apple-extension-service</string>
		<string>com.apple.speech.MacinTalkFramework.MacinTalkAUSP</string>
		<string>com.apple.speech.MacinTalkFramework.MacinTalkAUSP.apple-extension-service</string>
		<string>com.apple.ax.KonaTTSSupport.KonaSynthesizer</string>
		<string>com.apple.ax.KonaTTSSupport.KonaSynthesizer.apple-extension-service</string>
		<string>com.apple.audio.AudioQueueServer</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.accessibility.voices</string>
		<string>com.apple.pluginkit.pkd</string>
		<string>com.apple.campo</string>
		<string>com.apple.milod.xpc.service</string>
		<string>com.apple.sessionservices</string>
		<string>com.apple.DeviceConfigurationAgent.consumer</string>
		<string>com.apple.akd</string>
		<string>com.apple.accountsd.accountmanager</string>
		<string>com.apple.inputservice.keyboardui</string>
		<string>com.apple.inputservice.input-ui-host</string>
		<string>com.apple.UIKit.KeyboardManagement.hosted</string>
		<string>com.apple.TextInput</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Accessibility</string>
		<string>com.apple.Accessibility.Assets</string>
		<string>com.apple.Accessibility.Magnifier</string>
		<string>com.apple.AccessibilityUIServer</string>
		<string>com.apple.VoiceOverTouch</string>
		<string>com.apple.keyboard.preferences</string>
	</array>
	<key>com.apple.security.ts.ane-client</key>
	<true/>
	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.requestDeviceUnlock</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.accessibility.MagnifierAngel</string>
+	<key>com.apple.AXMediaUtilitiesService-access</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AXMediaUtilitiesService</string>
 		<string>com.apple.milod.xpc.service</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>

```
### MediaRemoteUI

> `/Applications/MediaRemoteUI.app/MediaRemoteUI`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allows-set-output-device</key>
 	<true/>
+	<key>com.apple.backlight.allowsActivationObservation</key>
+	<true/>
 	<key>com.apple.backlight.allowsPerformingEventObservation</key>
 	<true/>
 	<key>com.apple.bannerkit.post</key>

```
### NFCUISceneService

> `/Applications/NFCUISceneService.app/NFCUISceneService`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.SharingServices</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.NFCUISceneService</string>
+	</array>
+	<key>com.apple.sharing.Client</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 </dict>

```
### PreBoard

> `/Applications/PreBoard.app/PreBoard`

```diff

 		<string>AppleCredentialManagerUserClient</string>
 		<string>AppleKeyStoreUserClient</string>
 		<string>AppleMobileFileIntegrityUserClient</string>
+		<string>AppleSPUHIDDriverUserClient</string>
+		<string>IOReportUserClient</string>
 	</array>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>

```
### SettingsImportExtension

> `/Applications/Preferences.app/PlugIns/SettingsImportExtension.appex/SettingsImportExtension`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>

 	<array>
 		<string>com.apple.locationd.synchronous</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.mediator</string>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<array>
 		<string>/System/Library/PrivateFrameworks/Settings.framework</string>
 	</array>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.exception.background-task-allowed</key>
 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>

 		<string>com.apple.installcoordinationd.PersonaLifecycle</string>
 		<string>com.apple.internal.hidrecorderd.xpc</string>
 		<string>com.apple.internal.mtrecorder.xpc</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.registry</string>

```

### 🆕 Rushmore

> `/Applications/Rushmore.app/Rushmore`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.backboardd.cancelsTouchesInHostedContent</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.posterboardservices.data-store</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.accessSwitcherConfiguration</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.deleteDataStore</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.deleteDescriptors</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.mutateConfigurationHostStorage</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.mutateSwitcherConfiguration</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
	<true/>
	<key>com.apple.posterboardservices.host.configuration</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.security.storage.AppDataContainers</key>
	<true/>
	<key>com.apple.private.security.storage.chronod</key>
	<true/>
	<key>com.apple.proactive.FaceSuggestions.xpc</key>
	<true/>
	<key>com.apple.rootless.storage.proactivepredictions</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.posterkit.host</key>
	<true/>
	<key>com.apple.runningboard.primitiveattribute</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.runningboard.request.identity</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/Applications/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>Library/chronod/icons/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>Library/Biome</string>
		<string>Library/Caches/com.apple.chrono/</string>
		<string>Library/DuetExpertCenter/AmbientConfigurationCache/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.hangtracermonitor</string>
		<string>com.apple.dmd.policy</string>
		<string>com.apple.posterboardservices.services</string>
		<string>com.apple.proactive.ContextualEngine.suggestions.xpc</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.chronoservices</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Rushmore</string>
		<string>com.apple.ambient</string>
		<string>com.apple.BreadBoard</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<true/>
</dict>
</plist>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
+	<key>com.apple.private.corewifi.keychain</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.guided-browsing-target</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>

 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.AutoUnlock.AuthenticationHintsProvider</string>
 		<string>com.apple.UserNotifications.OneTimeCodeService</string>
+		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>

```
### ScreenTimeSettingsShield

> `/Applications/ScreenTimeSettingsShield.app/ScreenTimeSettingsShield`

```diff

 	<true/>
 	<key>com.apple.backboardd</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-keyboard</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>AppleIntelligenceReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.Buddy</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>ProactiveAppPrediction</key>
 		<dict>
 			<key>Streams</key>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.private.alarmkit.bundleIdentifier</key>
 	<string>com.apple.reminders</string>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### Siri AI

> `/Applications/Siri AI.app/Siri AI`

```diff

 	<array>
 		<string>com.apple.radios.plist</string>
 	</array>
-	<key>com.apple.TapToRadarKit.service-access</key>
-	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

 	<true/>
 	<key>com.apple.assistant.uibridge-service</key>
 	<true/>
-	<key>com.apple.assistantd.odeon-remote</key>
-	<true/>
 	<key>com.apple.assistantisland.client</key>
 	<true/>
 	<key>com.apple.assistantisland.stage-scene</key>

 	<true/>
 	<key>com.apple.clarityboard.shows-scene</key>
 	<true/>
+	<key>com.apple.conversation-intelligence.availability</key>
+	<true/>
+	<key>com.apple.conversation-intelligence.recap</key>
+	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.campo</string>
-	<key>com.apple.devicesharing.guest-user-mode-client</key>
-	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.duet.expertcenter.consumer</key>

 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
-	<key>com.apple.powerexperience.powermode.update</key>
-	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>CLIENT_ENTITLEMENT</string>

 		<string>/System/Library/PrivateFrameworks/SearchUI.framework</string>
 		<string>/System/Library/PrivateFrameworks/SiriSharedUI.framework/</string>
 	</array>
-	<key>com.apple.private.appintents.extension-host</key>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+	</array>
+	<key>com.apple.private.appintents.connection</key>
 	<true/>
-	<key>com.apple.private.appintents.live-entities.read</key>
+	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appintents.trusted-entity-identifier</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.attentionawareness</key>
 	<true/>
+	<key>com.apple.private.attentionawareness.poll</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 				<string>Mail</string>
 				<string>DraftMail</string>
 				<string>MailAttachment</string>
+				<string>Note</string>
+				<string>Message</string>
 			</array>
 		</dict>
 		<key>generativesearch</key>

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.intelligenceflow</string>
+		<string>group.com.apple.tipsnext</string>
 	</array>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>

 	<array>
 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
-		<string>kTCCServiceReminders</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
-	<key>com.apple.realitysimulation.render-on-top-spi</key>
+	<key>com.apple.realitysimulation.can-receive-wolf-hover</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>

 		<string>group.com.apple.Maps</string>
 		<string>group.com.apple.icloud.fm</string>
 		<string>group.com.apple.notes</string>
+		<string>group.com.apple.tipsnext</string>
 		<string>group.com.apple.sports</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/Library/SMS/</string>
 		<string>/Media/PhotoData/</string>
 		<string>/Library/com.apple.ManagedSettings/</string>
-		<string>/Library/UserConfigurationProfiles/</string>
+		<string>/Library/MessagesMetaData/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/Caches/com.apple.countryd/</string>
 		<string>/Library/Caches/com.apple.keyboards/</string>

 		<string>/Library/Trial/</string>
 		<string>/Library/Mobile Documents/</string>
 		<string>/Containers/Shared/AppGroup/</string>
-		<string>/Library/MessagesMetaData/</string>
 		<string>/Library/DeviceRegistry.state/ActiveDeviceMiniStore.plist</string>
-		<string>/Library/Caches/com.apple.itunesstored/url-resolution.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.appintents.LiveEntityService</string>
 		<string>com.apple.intelligenceflow.contextTool</string>
+		<string>com.apple.visualintelligence.visual-action-prediction</string>
 		<string>com.apple.ind.xpc</string>
-		<string>com.apple.assistantd.odeon-remote</string>
-		<string>com.apple.companiond.xpc</string>
 		<string>com.apple.quicklook.UIExtension.viewservice</string>
 		<string>com.apple.private.siriappintentsd.orchestrator</string>
 		<string>com.apple.generativesearch.server.search</string>

 		<string>com.apple.thermalMonitor.siriEnabledNote</string>
 		<string>com.apple.Feedback.DraftingExtension.viewservice</string>
 		<string>com.apple.iCloudQuotaUI.RemoteiCloudQuotaUI.viewservice</string>
+		<string>com.apple.conversation-intelligence.service</string>
 		<string>com.apple.internal.SpotlightAutomationTester</string>
 		<string>com.apple.carousel.flashlightxpcservice</string>
 		<string>com.apple.carousel.sessionservice</string>
-		<string>com.apple.realitysystemsupport.hid_server_backboard</string>
-		<string>com.apple.remindd</string>
-		<string>com.apple.remindd.userInteractive</string>
-		<string>com.apple.surfboard.entityinteractionservice</string>
-		<string>com.apple.surfboard.lockscreenservice</string>
-		<string>com.apple.devicesharing.guestusermodeservice</string>
-		<string>com.apple.calendar.EventKitUIRemoteUIExtension.viewservice</string>
-		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.carousel.navigationservice</string>
 		<string>com.apple.iconservices</string>
+		<string>com.apple.linkd.application-service</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.watchnotificationsui.alertservice</string>
+		<string>com.apple.calendar.EventKitUIRemoteUIExtension.viewservice</string>
+		<string>com.apple.securepairingd</string>
 		<string>com.apple.linkd.registry</string>
-		<string>com.apple.userprofiles</string>
+		<string>com.apple.visualintelligence.visual-action-prediction</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<array>
 		<string>com.apple.AppSupport</string>
 		<string>com.apple.cloud.quota</string>
+		<string>com.apple.Carousel</string>
 		<string>com.apple.DocumentManager.defaults</string>
 		<string>com.apple.DuetExpertCenter.AppPredictionExpert</string>
 		<string>com.apple.duetexpertd</string>

 		<string>com.apple.preferences.sounds</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.raisetospeak</string>
+		<string>com.apple.reverie</string>
 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.SwiftUI</string>

 	<true/>
 	<key>com.apple.springboard.addWidgetToTodayView</key>
 	<true/>
-	<key>com.apple.springboard.allowIconVisibilityChanges</key>
-	<true/>
 	<key>com.apple.springboard.app-drag</key>
 	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>

 	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
-	<key>com.apple.surfboard-prevent-homeui-from-hiding-when-launching</key>
-	<true/>
 	<key>com.apple.surfboard.allow-scene-requests-while-backgrounded</key>
 	<true/>
 	<key>com.apple.surfboard.application-service-client</key>

 	<true/>
 	<key>com.apple.surfboard.disables-scene-snapshots</key>
 	<true/>
-	<key>com.apple.surfboard.entity-interaction-client</key>
-	<true/>
-	<key>com.apple.surfboard.entity-interaction-observer</key>
-	<true/>
-	<key>com.apple.surfboard.force-quit-suppression</key>
-	<true/>
 	<key>com.apple.surfboard.immersion-client</key>
 	<true/>
 	<key>com.apple.surfboard.immersive-scene-dismissal</key>
 	<true/>
 	<key>com.apple.surfboard.launcherservice.client</key>
 	<true/>
-	<key>com.apple.surfboard.lock-screen-client</key>
-	<true/>
 	<key>com.apple.surfboard.opts-out-of-shared-coordinate-origin</key>
 	<true/>
 	<key>com.apple.surfboard.placement-client</key>

 	<true/>
 	<key>com.apple.surfboard.scenesession-updates</key>
 	<true/>
-	<key>com.apple.surfboard.sharing-mode-launch-allowed</key>
-	<true/>
 	<key>com.apple.surfboard.should-ignore-if-last-scene-for-auto-show-homeui</key>
 	<true/>
 	<key>com.apple.surfboard.system-elements-assertion-immersive-visible</key>

 	<true/>
 	<key>com.apple.vfx-provider</key>
 	<true/>
+	<key>com.apple.visualintelligence.private.visual-action-prediction</key>
+	<true/>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
 	<key>com.apple.voiceservices.tts.customvoice</key>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<array>
 		<string>/System/Library/PrivateFrameworks/SiriSharedUI.framework/</string>
 	</array>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalProviderService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>

 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.openai</string>
+		<string>com.apple.snowflake</string>
 	</array>
 </dict>
 </plist>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<array>
 		<string>preferences.plist</string>
 	</array>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.accessibility.AccessibilityPersonalVoiceUsageOverride</key>
 	<true/>
 	<key>com.apple.accessibility.AccessibilityUIServer</key>

 	<key>com.apple.developer.user-fonts</key>
 	<array>
 		<string>app-usage</string>
+		<string>font-enumeration</string>
 	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.xpc.launchd.userspace-reboot</key>
 	<true/>
+	<key>com.apple.relevanced.AudioUnderstanding.classification</key>
+	<true/>
 	<key>com.apple.runningboard.AccessibilityUIServer</key>
 	<true/>
 	<key>com.apple.runningboard.VoiceOver</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.AXMediaUtilitiesService</string>
+		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.Feedback.DraftingExtension.viewservice</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.launchservices.clearadvertisingid</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.locationd.accessory_location</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

 	<true/>
 	<key>com.apple.launchservices.clearadvertisingid</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>

```

### 🆕 MobileDevices-0002

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`

- No entitlements *(yet)*
### PhotosViewService

> `/System/Library/CoreServices/PhotosViewService.app/PhotosViewService`

```diff

 	<true/>
 	<key>com.apple.private.cloudphotod.access</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.photos.allowassetexpunge</key>

 		<string>com.apple.cloudphotod</string>
 		<string>com.apple.photos.service</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobileslideshow</string>
+	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	</dict>
 	<key>com.apple.aop.hid-driver.user-client</key>
 	<dict>
+		<key>crane</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
 		<key>eclipse</key>
 		<dict>
 			<key>send-command</key>

 			<key>send-command</key>
 			<dict/>
 		</dict>
+		<key>gesture_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
 		<key>orientation</key>
 		<dict>
 			<key>send-command</key>
 			<dict/>
 		</dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+		<key>orientation_2</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
 	</dict>
 	<key>com.apple.appleaccount.identity.read</key>
 	<true/>

 		<string>com.apple.mobiletimer</string>
 		<string>com.apple.usernotifications.example</string>
 	</array>
+	<key>com.apple.private.usernotifications.content-extension-host</key>
+	<true/>
 	<key>com.apple.private.usernotifications.coreservice</key>
 	<true/>
 	<key>com.apple.private.usernotifications.event-service</key>

 	<true/>
 	<key>com.apple.springboard.application-removability.proxy</key>
 	<true/>
+	<key>com.apple.springboard.attribute.always-on-policies</key>
+	<true/>
+	<key>com.apple.springboard.attribute.always-on-user-preference</key>
+	<true/>
 	<key>com.apple.springboard.display-lookup</key>
 	<true/>
 	<key>com.apple.springboard.fetchDisplayConfigs</key>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<true/>
 	<key>com.apple.accessibility.axassets</key>
 	<true/>
+	<key>com.apple.accessibility.diagnostics.file-draft</key>
+	<true/>
 	<key>com.apple.accessibility.environmentaldosimetry</key>
 	<true/>
 	<key>com.apple.accessibility.image-explorer.client</key>

```

### 🆕 AccessibilityDiagnostics

> `/System/Library/ExtensionKit/Extensions/AccessibilityDiagnostics.appex/AccessibilityDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/Diagnostics/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.Accessibility</string>
		<string>com.apple.VoiceOverTouch</string>
		<string>com.apple.SpeakSelection</string>
		<string>com.apple.accessibility.livespeech</string>
	</array>
</dict>
</plist>

```
### AskPermissionAskToResponseExtension

> `/System/Library/ExtensionKit/Extensions/AskPermissionAskToResponseExtension.appex/AskPermissionAskToResponseExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.screen-time-settings</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.xpc.amsengagementd</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.askpermissiond</string>
+		<string>com.apple.xpc.amsengagementd</string>
+	</array>
 	<key>com.apple.storekit.client-override</key>
 	<true/>
 </dict>

```
### AskToViewExtension

> `/System/Library/ExtensionKit/Extensions/AskToViewExtension.appex/AskToViewExtension`

```diff

 	<key>com.apple.private.messages.associated-message-extension-bundle-identifiers</key>
 	<array>
 		<string>com.apple.AskToMessagesHost.AskToMessagesExtension</string>
+		<string>com.apple.PeopleMessageService.AskToBuy</string>
 	</array>
 	<key>com.apple.private.screen-time</key>
 	<true/>

```
### AudioAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/AudioAppIntentsExtension.appex/AudioAppIntentsExtension`

```diff

 	<string>com.apple.siri.AudioAppIntentsExtension</string>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 </dict>
 </plist>
 

```
### BlackPowderInferenceExtension

> `/System/Library/ExtensionKit/Extensions/BlackPowderInferenceExtension.appex/BlackPowderInferenceExtension`

```diff

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.openai</string>
+		<string>com.apple.snowflake</string>
 		<string>com.apple.openai.xcode</string>
 	</array>
 </dict>

```

### 🆕 CalendarPosterExtension

> `/System/Library/ExtensionKit/Extensions/CalendarPosterExtension.appex/CalendarPosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.appintents.extension-mediator.bundle-identifier</key>
	<string>com.apple.Rushmore</string>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.chrono/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.chronoservices</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.mobilecal</string>
	</array>
</dict>
</plist>

```
### CameraMessagesApp

> `/System/Library/ExtensionKit/Extensions/CameraMessagesApp.appex/CameraMessagesApp`

```diff

 		<string>NULL/ActivationPrivateKey</string>
 		<string>NULL/DeviceCertificate</string>
 	</array>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.photos.service.mediaconversion</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

```
### DocumentAppIntents

> `/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### DocumentAppShortcuts

> `/System/Library/ExtensionKit/Extensions/DocumentAppShortcuts.appex/DocumentAppShortcuts`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ExclavesInferenceProvider

> `/System/Library/ExtensionKit/Extensions/ExclavesInferenceProvider.appex/ExclavesInferenceProvider`

```diff

 	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.IntelligentConversationExtraction</string>
 		<string>com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition</string>
 	</array>
 	<key>com.apple.private.exclaves.conclave-host</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IntelligentConversationExtraction/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IntelligentConversationExtraction/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Speech_AutomaticSpeechRecognition/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Speech_AutomaticSpeechRecognition/</string>
 	</array>

```
### GenerativeAssistantExtension

> `/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension`

```diff

 	<array>
 		<string>apple</string>
 		<string>com.apple.openai</string>
+		<string>com.apple.snowflake</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/MapsIntents`

```diff

 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Maps</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.Maps</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.Maps</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.Maps.MapsSync.store</string>

```
### PCCAgentClientExtension

> `/System/Library/ExtensionKit/Extensions/PCCAgentClientExtension.appex/PCCAgentClientExtension`

```diff

 	<true/>
 	<key>com.apple.privatecloudcompute.requests</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### PasswordsDataMigration

> `/System/Library/ExtensionKit/Extensions/PasswordsDataMigration.appex/PasswordsDataMigration`

```diff

 	</dict>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.keychain.inet_expansion_fields</key>
 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>

 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.privatecloudcompute</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>

```

### 🆕 PhotosClockPoster

> `/System/Library/ExtensionKit/Extensions/PhotosClockPoster.appex/PhotosClockPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.developer.sensitivecontentanalysis.client</key>
	<array>
		<string>analysis</string>
	</array>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.posterboardservices.data-store</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.accessSwitcherConfiguration</key>
	<true/>
	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.appintents.extension-mediator.bundle-identifier</key>
	<string>com.apple.Rushmore</string>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.photos.allowassetexpunge</key>
	<true/>
	<key>com.apple.private.photos.allowcollectionshare</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.sleepd</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.runningboard.posterkit.host</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/com.apple.mediaanalysisd/</string>
		<string>/private/var/mobile/tmp/com.apple.mediaanalysisd/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/tmp/</string>
		<string>/Media/DCIM/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>RootDomainUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.posterboardservices.services</string>
		<string>com.apple.posterboardservices.dataModel</string>
		<string>com.apple.perceptiond.entitykit</string>
		<string>com.apple.perceptiond.api</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.PowerManagement.control</string>
		<string>com.apple.iokit.powerdxpc</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.hardened-process.no-guard-objects</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```

### 🆕 PhotosMemoriesPoster

> `/System/Library/ExtensionKit/Extensions/PhotosMemoriesPoster.appex/PhotosMemoriesPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.appintents.extension-mediator.bundle-identifier</key>
	<string>com.apple.Rushmore</string>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.photoanalysisd.access</key>
	<true/>
	<key>com.apple.private.photos.allowassetexpunge</key>
	<true/>
	<key>com.apple.private.photos.allowcollectionshare</key>
	<true/>
	<key>com.apple.private.photos.allowmemorymutation</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/tmp/</string>
		<string>/Media/DCIM/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.hardened-process.no-guard-objects</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### PrivateMLClientInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService`

```diff

 	<true/>
 	<key>com.apple.privatecloudcompute.requests</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.usage</key>
+	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### ScreenTimeSettingsResponseExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeSettingsResponseExtension.appex/ScreenTimeSettingsResponseExtension`

```diff

 	<string>com.apple.ScreenTimeSettingsResponseExtension</string>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```

### 🆕 SignificantChangeResponseExtension

> `/System/Library/ExtensionKit/Extensions/SignificantChangeResponseExtension.appex/SignificantChangeResponseExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.family.ageRange</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.family.ageRange.xpc</string>
		<string>com.apple.managedappdistributiond.xpc</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.family.ageRange.xpc</string>
		<string>com.apple.managedappdistributiond.xpc</string>
	</array>
</dict>
</plist>

```
### SiriAttentionAndInvocationExtension

> `/System/Library/ExtensionKit/Extensions/SiriAttentionAndInvocationExtension.appex/SiriAttentionAndInvocationExtension`

```diff

 		<string>com.apple.corespeechdatacollection</string>
 		<string>com.apple.SpeakerIdWorker</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.assistant.settings</string>

```
### SiriLogProcessor

> `/System/Library/ExtensionKit/Extensions/SiriLogProcessor.appex/SiriLogProcessor`

```diff

 	<string>com.apple.aiml.siri.SiriLogProcessor</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.aiml.siri.SiriLogProcessor</string>
+	<key>com.apple.lighthouse.host-ole</key>
+	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 	<array>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
-		<string>com.apple.aiml.siri.OLEOrchestrator</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<array>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
-		<string>com.apple.aiml.siri.OLEOrchestrator</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 SiriTransparencyExtension

> `/System/Library/ExtensionKit/Extensions/SiriTransparencyExtension.appex/SiriTransparencyExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.SiriTransparencyExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.SiriTransparencyExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
		<string>Siri.ODDI.TransparencyReport</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Lighthouse.Ledger.TaskCustomEvent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.logging.stream</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.SiriTransparencyWorker</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.SiriTransparencyWorker</string>
	</array>
</dict>
</plist>

```
### TGOnDeviceInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/TGOnDeviceInferenceProviderService.appex/TGOnDeviceInferenceProviderService`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.CodeLM</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.FOVI</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
 		<string>com.apple.MobileAsset.UAF.Translation.MMAssets</string>
 	</array>

```

### 🆕 WidgetFaceExtension

> `/System/Library/ExtensionKit/Extensions/WidgetFaceExtension.appex/WidgetFaceExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.backboardd.cancelsTouchesInHostedContent</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
	<true/>
	<key>com.apple.chrono.widgetRenderer</key>
	<true/>
	<key>com.apple.chronod.toolservices</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.intents.uiextension.discovery</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.localizationswitcher</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.lookup</key>
	<dict>
		<key>appData</key>
		<true/>
	</dict>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.appintents.extension-mediator.bundle-identifier</key>
	<string>com.apple.Rushmore</string>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.chrono-extension-host</key>
	<true/>
	<key>com.apple.private.coreaudio.initiatetemporarybackgroundplayback.allow</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.iokit.batterydataprecise</key>
	<true/>
	<key>com.apple.private.replicator.controller</key>
	<true/>
	<key>com.apple.private.security.storage.AppDataContainers</key>
	<true/>
	<key>com.apple.private.security.storage.chronod</key>
	<true/>
	<key>com.apple.private.sessionkit.listener</key>
	<true/>
	<key>com.apple.proactive.FaceSuggestions.xpc</key>
	<true/>
	<key>com.apple.rootless.storage.proactivepredictions</key>
	<true/>
	<key>com.apple.runningboard.assertions.chronod</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.hereditarygrantoriginator</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.primitiveattribute</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.runningboard.terminateprocess</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Applications/</string>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/private/var/mobile/Library/DuetExpertCenter/</string>
		<string>/var/mobile/Library/ChronoData/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.chrono/</string>
		<string>/Library/Caches/com.apple.chrono/</string>
		<string>/Library/chronod/icons/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.audio.AudioSession</string>
		<string>com.apple.chrono.widgetcenterconnection</string>
		<string>com.apple.coremedia.systemcontroller.xpc</string>
		<string>com.apple.backboard.display.services</string>
		<string>com.apple.breadboardservices</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.CARenderServer</string>
		<string>com.apple.localizationswitcherd</string>
		<string>com.apple.sessionservices</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.linkd.mediator</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
		<string>com.apple.mobile.usermanagerd.xpc</string>
		<string>com.apple.chrono.event-service.gamed</string>
		<string>com.apple.proactive.FaceSuggestions.xpc</string>
		<string>com.apple.replicatorservices</string>
	</array>
	<key>com.apple.security.exception.mach-register.global-name</key>
	<array>
		<string>com.apple.gaspar.gsEvents</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.coremedia</string>
		<string>com.apple.coreanimation</string>
		<string>com.apple.Rushmore</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
		<string>com.apple.WidgetFace</string>
		<string>com.apple.WidgetFace.WidgetFaceExtension</string>
	</array>
	<key>com.apple.security.ts.mach-task-name</key>
	<true/>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
	<key>com.apple.security.ts.render-images</key>
	<true/>
	<key>com.apple.sessionservices</key>
	<true/>
	<key>com.apple.springboard.widget-metrics</key>
	<true/>
	<key>com.apple.usermanagerd.persona.fetch</key>
	<true/>
</dict>
</plist>

```
### frauddefensepfl

> `/System/Library/ExtensionKit/Extensions/frauddefensepfl.appex/frauddefensepfl`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.priml.pfl.plugins</string>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.priml.pfl.Morpheus.allowed</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 		<string>com.apple.mlhostd.xpc</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.gms.availability</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 HomeCommunicationSnippetProviderPlugin

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/HomeCommunicationSnippetProviderPlugin.bundle/HomeCommunicationSnippetProviderPlugin`

- No entitlements *(yet)*

### 🆕 SiriWellnessSnippetService

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/SiriWellnessSnippetService.bundle/SiriWellnessSnippetService`

- No entitlements *(yet)*
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.corepersonalization.client.graphEmbedding</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allowcarplayapps</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

 	<true/>
 	<key>com.apple.private.generativesearch.client.index</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.salientpostings</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.spotlightknowledge</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>CorePersonalization.IndexableEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>DocumentProcessing.TestItem</key>
 				<dict>
 					<key>mode</key>

 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.generativesearch.server.indexing</string>
+		<string>com.apple.corepersonalization.server.graphEmbedding</string>
+		<string>com.apple.generativesearch.server.salientpostings</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Turn</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Conversation</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 		<string>/private/var/db/MobileIdentityData/LaunchWarning.db</string>
 		<string>/private/var/db/MobileIdentityData/LaunchWarning.db-wal</string>
 		<string>/private/var/db/MobileIdentityData/LaunchWarning.db-shm</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_China_PWSCertificates/purpose_auto/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.relevanced.AssertionService</string>
 		<string>com.apple.seserviced.sereservation.client</string>
 		<string>com.apple.SIMSetupUIBannerService</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>

```
### extensionkitservice

> `/System/Library/Frameworks/ExtensionFoundation.framework/XPCServices/extensionkitservice.xpc/extensionkitservice`

```diff

 	<key>com.apple.private.extensionkit.host.any-extension</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
-	<string>pkd</string>
+	<string>autobox</string>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

 	<true/>
 	<key>com.apple.runningboard.statecapture</key>
 	<true/>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.ActivityMonitorApp</string>
+		<string>com.apple.Bridge</string>
 		<string>com.apple.Fitness</string>
 		<string>com.apple.Health.WatchPrivacyNotifications</string>
 		<string>com.apple.HeartRate</string>

```
### shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

 	<true/>
 	<key>com.apple.private.aop-audio.user-access</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.fpsd</string>
 		<string>com.apple.fairplayd</string>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.speech.localspeechrecognition</string>
+	<key>com.apple.developer.networking.multipath_extended</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceSpeechRecognition</string>

 		<string>com.apple.EmojiPreferences</string>
 		<string>com.apple.speech.localspeechrecognition</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>
 	<key>com.apple.security.ts.opengl-or-metal</key>

 	</array>
 	<key>com.apple.uservault</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.icl</string>
+		<string>com.apple.siri.osprey</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```

### 🆕 HIDSecureInputSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/HIDSecureInputSessionFilter.plugin/HIDSecureInputSessionFilter`

- No entitlements *(yet)*

### 🆕 RelevanceIntelligence

> `/System/Library/LocationBundles/RelevanceIntelligence.bundle/RelevanceIntelligence`

- No entitlements *(yet)*

### 🆕 AudioIntelligencePhoneSettings

> `/System/Library/NanoPreferenceBundles/General/AudioIntelligencePhoneSettings.bundle/AudioIntelligencePhoneSettings`

- No entitlements *(yet)*

### 🆕 AudioIntelligencePhoneBuddyFlow

> `/System/Library/NanoPreferenceBundles/SetupBundles/AudioIntelligencePhoneBuddyFlow.bundle/AudioIntelligencePhoneBuddyFlow`

- No entitlements *(yet)*

### 🆕 AmbientHostConfigurationProvider

> `/System/Library/Posters/HostConfigurationProviders/AmbientHostConfigurationProvider.bundle/AmbientHostConfigurationProvider`

- No entitlements *(yet)*
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.user</string>

 		<string>com.apple.springboard</string>
 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
 	</array>
+	<key>com.apple.springboard.orientation-lock-service</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>platform-application</key>

```
### AppIntentsLiveEntityService

> `/System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/XPCServices/AppIntentsLiveEntityService.xpc/AppIntentsLiveEntityService`

```diff

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	<array>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.registry</string>

```
### AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/AppIntentsRunnerXPCService`

```diff

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.locationd.synchronous</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.ts.read-any-bundle</key>
 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>

```
### appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/appleaccounttransparencyd`

```diff

 	<true/>
 	<key>com.apple.cdp.telemetry</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.write.access</key>
 	<true/>
+	<key>com.apple.assistant.analytics</key>
+	<true/>
 	<key>com.apple.assistant.flow_service</key>
 	<true/>
 	<key>com.apple.assistant.multiuser.service</key>

 		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.securelocations</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.carpd.xpc</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.write.access</key>
 	<true/>
+	<key>com.apple.assistant.analytics</key>
+	<true/>
 	<key>com.apple.assistant.analytics-observation</key>
 	<true/>
 	<key>com.apple.assistant.cdm.client</key>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appintents.trusted-entity-identifier</key>

 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.logging</string>
 		<string>com.apple.assistant.nano</string>
+		<string>com.apple.assistant.public</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.token</string>

 	<array>
 		<string>kern.exclaves_status</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### cksharingmanagementd

> `/System/Library/PrivateFrameworks/CKSharingManagementDaemon.framework/Support/cksharingmanagementd`

```diff

 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Applications/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.private.alloy.cloudkit.sharing.management-idswake</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.CloudKit</string>

```
### callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.callintelligenced.service</string>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>private</string>

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.facetime.bag</string>
+		<string>com.apple.callintelligenced</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.unthrottledAPIRequester</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```

### 🆕 SimpleClockPosterExtension

> `/System/Library/PrivateFrameworks/ClockFacePosters.framework/PlugIns/SimpleClockPosterExtension.appex/SimpleClockPosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PRWantsLocation</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.ClockFacePosters.SimpleAnalogPosterExtension</string>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.ClockFacePosters.SimpleAnalogPosterExtension</string>
	<key>com.apple.backboardd.cancelsTouchesInHostedContent</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent - 2</key>
	<true/>
	<key>com.apple.chrono.widgetRenderer</key>
	<true/>
	<key>com.apple.chronod.toolservices</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.developer.weatherkit</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.locationd.prompt_from_background</key>
	<true/>
	<key>com.apple.locationd.usage_oracle</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.chrono-extension-host</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.mobiletimerd</key>
	<true/>
	<key>com.apple.private.security.storage.chronod</key>
	<true/>
	<key>com.apple.runningboard.assertions.chronod</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.hereditarygrantoriginator</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.primitiveattribute</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.runningboard.terminateprocess</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Applications/</string>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/var/mobile/Library/ChronoData/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.chrono/</string>
		<string>/Library/Caches/com.apple.chrono/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/MappedImageCache/</string>
		<string>/Library/Caches/MappedImageCache/com.apple.ClockKitUI.configurableHands</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.systemstatus</string>
		<string>com.apple.MobileTimer.alarmserver</string>
		<string>com.apple.MobileTimer.timerserver</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.chrono.widgetcenterconnection</string>
		<string>com.apple.chrono.event-service.gamed</string>
		<string>com.apple.MobileTimer.timerserver</string>
		<string>com.apple.MobileTimer.alarmserver</string>
		<string>com.apple.systemstatus</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.Rushmore</string>
	</array>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>com.apple.springboard.widget-metrics</key>
	<true/>
	<key>com.apple.systemstatus.domains</key>
	<array>
		<string>status-bar-overrides</string>
	</array>
</dict>
</plist>

```

### 🆕 SimpleDigitalPosterExtension

> `/System/Library/PrivateFrameworks/ClockFacePosters.framework/PlugIns/SimpleDigitalPosterExtension.appex/SimpleDigitalPosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PRWantsLocation</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.ClockFacePosters.SimpleDigitalPosterExtension</string>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.ClockFacePosters.SimpleDigitalPosterExtension</string>
	<key>com.apple.backboardd.cancelsTouchesInHostedContent</key>
	<true/>
	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
	<true/>
	<key>com.apple.chrono.widgetRenderer</key>
	<true/>
	<key>com.apple.chronod.toolservices</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.developer.weatherkit</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.locationd.prompt_from_background</key>
	<true/>
	<key>com.apple.locationd.usage_oracle</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.associated-domains</key>
	<true/>
	<key>com.apple.private.chrono-extension-host</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.mobiletimerd</key>
	<true/>
	<key>com.apple.private.security.storage.chronod</key>
	<true/>
	<key>com.apple.runningboard.assertions.chronod</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.hereditarygrantoriginator</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.primitiveattribute</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.runningboard.terminateprocess</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Applications/</string>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/var/mobile/Library/ChronoData/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.chrono/</string>
		<string>/Library/Caches/com.apple.chrono/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/MappedImageCache/</string>
		<string>/Library/Caches/MappedImageCache/com.apple.ClockKitUI.configurableHands</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.chrono.event-service.gamed</string>
		<string>com.apple.chrono.widgetcenterconnection</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.MobileTimer.timerserver</string>
		<string>com.apple.MobileTimer.alarmserver</string>
		<string>com.apple.systemstatus</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.Rushmore</string>
	</array>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>com.apple.springboard.widget-metrics</key>
	<true/>
	<key>com.apple.systemstatus.domains</key>
	<array>
		<string>status-bar-overrides</string>
	</array>
</dict>
</plist>

```
### accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.smcsensor.user-access</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleCredentialManagerUserClient</string>

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 	<true/>
 	<key>com.apple.locationd.status</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
 	<true/>
 	<key>com.apple.private.CoreAnalytics.Preferences.write</key>

 		<string>com.apple.locationd.desktop.synchronous</string>
 		<string>com.apple.locationd.desktop.spi</string>
 		<string>com.apple.bluetooth.xpc</string>
+		<string>com.apple.nanoprefsync</string>
+		<string>com.apple.FileCoordination</string>
+		<string>com.apple.nano.nanoregistry.paireddeviceregistry</string>
+		<string>com.apple.pairedsyncd.syncstate</string>
+	</array>
+	<key>com.apple.security.exception.nano-preference.read-only</key>
+	<array>
+		<string>com.apple.RelevancePlatform.AudioUnderstanding</string>
+		<string>com.apple.RelevancePlatform.MindPalaceEnrollment</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gms.availability</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.RelevancePlatform.AudioUnderstanding</string>
+		<string>com.apple.RelevancePlatform.MindPalaceEnrollment</string>
+		<string>com.apple.nanoprefsyncd</string>
+		<string>com.apple.assistant.public</string>
+		<string>com.apple.assistant.support</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>CORE_PARSEC_DEVICE_GENERIC</string>
+	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>
 		<integer>0</integer>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.private.mediaexperience.microphoneattribution.allow</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.preferredminimummicrophoneindicatorlightontime.allow</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.useindependentinputaudioresourcesession</key>

 	<true/>
 	<key>com.apple.private.sleepd</key>
 	<true/>
+	<key>com.apple.private.speech-framework.server</key>
+	<true/>
 	<key>com.apple.private.speech-model-training</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	<string>serverPreferred</string>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
+	<key>com.apple.CoreRoutine.ScenarioTrigger</key>
+	<true/>
+	<key>com.apple.Maps.MapsSync.access</key>
+	<true/>
 	<key>com.apple.Pasteboard.background-access</key>
 	<true/>
 	<key>com.apple.Pasteboard.originating-bundle-id-query</key>

 	<true/>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 				<string>App.InFocus</string>
 			</array>
 		</dict>
+		<key>SGNotificationContextSignals</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Notification.Usage</string>
+			</array>
+		</dict>
 		<key>SmartRepliesFilter</key>
 		<dict>
 			<key>Streams</key>

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>entityTagging</string>
+		<string>visualIdentifier</string>
+		<string>handleMap</string>
+		<string>hasAssociationSubgraph</string>
+	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.reversetemplated</key>

```

### 🆕 ThreadDiagnosticExtension

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/PlugIns/ThreadDiagnosticExtension.appex/ThreadDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/Logs/</string>
	</array>
</dict>
</plist>

```

### 🆕 ImageConversionService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ImageConversionService.xpc/ImageConversionService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.desktopservices.ImageConversionService</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.desktopservices.ImageConversionService</string>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CoreServices.coreservicesd</string>
		<string>com.apple.lsd.mapdb</string>
		<string>com.apple.coremedia.videocodecd.compressionsession</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession.xpc</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### com.apple.DocumentManagerCore.Downloads

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Downloads.xpc/com.apple.DocumentManagerCore.Downloads`

```diff

 		<string>com.apple.FileProvider</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.DocumentManagerCore.Rename

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename`

```diff

 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.DesktopServicesHelper</string>
 		<string>com.apple.DesktopServicesHelper.FileService</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### AddTagsActionExtension

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/AddTagsActionExtension.appex/AddTagsActionExtension`

```diff

 		<string>com.apple.FileProvider</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### RecentsAvocado

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocado.appex/RecentsAvocado`

```diff

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### RecentsAvocadoIntentHandler

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/RecentsAvocadoIntentHandler.appex/RecentsAvocadoIntentHandler`

```diff

 		<string>com.apple.spotlight.userfs</string>
 		<string>com.apple.FileProvider</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SaveToFiles

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/SaveToFiles.appex/SaveToFiles`

```diff

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.DocumentManager.Service

> `/System/Library/PrivateFrameworks/DocumentManagerUICore.framework/PlugIns/com.apple.DocumentManager.Service.appex/com.apple.DocumentManager.Service`

```diff

 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.SmartNameSuggestionsService</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 FindMyLocationQualityService

> `/System/Library/PrivateFrameworks/FindMyLocationQuality.framework/XPCServices/FindMyLocationQualityService.xpc/FindMyLocationQualityService`

- No entitlements *(yet)*
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
 	<true/>
+	<key>com.apple.generativeexperiencesd.externalProviders</key>
+	<true/>
 	<key>com.apple.intelligenceflow.context</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>RegionalSafetyAnalysisMetrics</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>RegionalSafetyAnalysis.Disablement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>RegionalSafetyAnalysis.Eligibility</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>com.apple.AppleIntelligence.Reporting.AssetDeliveryLog</key>
 		<dict>
 			<key>Streams</key>

 	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
+	<key>com.apple.private.replicator.dataProvider</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.aiml.RapidResourceDelivery</string>
+	</array>
 	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 	<true/>
 	<key>com.apple.rootless.storage.triald</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.aiml.RapidResourceDelivery</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/UnifiedAssetFramework/</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_CN_Guardrail/</string>

 		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/installd/Library/MobileInstallation/</string>
+		<string>/private/var/containers/Bundle/Application/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.spotlightknowledged</string>
 		<string>com.apple.mobile.installd</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.replicatorservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.sage</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.gms.availability.reasons</string>
 		<string>com.apple.generativeexperiences.corefollowup</string>
 		<string>com.apple.generativepartnerservicesettings</string>
+		<string>group.com.apple.aiml.RapidResourceDelivery</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.appleintelligencereporting</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.openai</string>
-		<string>com.apple.openai.xcode</string>
+		<string>com.apple.snowflake</string>
 		<string>apple</string>
 	</array>
 </dict>

```
### MedicalIDFollowUpExtension

> `/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/MedicalIDFollowUpExtension.appex/MedicalIDFollowUpExtension`

```diff

 	<array>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.Bridge</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.corefollowup.agent</string>

```
### HealthPlansDiagnosticExtension

> `/System/Library/PrivateFrameworks/HealthPlans.framework/PlugIns/HealthPlansDiagnosticExtension.appex/HealthPlansDiagnosticExtension`

```diff

 	</array>
 	<key>com.apple.private.healthkit</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.healthappd.control</string>
+	</array>
 </dict>
 </plist>
 

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.agentmanagerd.learningGeneration</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.cards.all-access</key>

 	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.corepersonalization.client.insights</key>
+	<true/>
+	<key>com.apple.private.corepersonalization.client.memory</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

 				<string>EmploymentInsight</string>
 				<string>OrganizationInsight</string>
 			</array>
+			<key>Sets</key>
+			<dict>
+				<key>Health.Measurement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>SensedUserContext.Event</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>SensedUserContext.Pattern</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>SensedUserContext.Place</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
 		</dict>
 	</dict>
 	<key>com.apple.private.security.storage.Health</key>

 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VideoIntelligence/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	<array>
 		<string>com.apple.healthcontentd</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.agentmanager</string>
 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.bluetooth.xpc</string>

 		<string>com.apple.coremedia.mediaplaybackd.videoqueue</string>
 		<string>com.apple.coremedia.videocodecd.compressionsession</string>
 		<string>com.apple.coremedia.videocodecd.compressionsession.xpc</string>
+		<string>com.apple.corepersonalization.server.insights</string>
+		<string>com.apple.corepersonalization.server.memory</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>

```
### HealthReportDiagnosticExtension

> `/System/Library/PrivateFrameworks/HealthReport.framework/PlugIns/HealthReportDiagnosticExtension.appex/HealthReportDiagnosticExtension`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.healthcontentd</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>

 	<array>
 		<string>/Library/DeviceRegistry.state/ActiveDeviceMiniStore.plist</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.healthcontentd</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.health.shared</string>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 		<string>com.apple.LiveListenNotifications</string>
 		<string>com.apple.HearingAidsNotifications</string>
 	</array>
+	<key>com.apple.relevanced.AudioUnderstanding.classification</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Accessibility/</string>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceWillow</string>

```
### homeeventsd

> `/System/Library/PrivateFrameworks/HomeKitEvents.framework/Support/homeeventsd`

```diff

 	<array>
 		<string>com.apple.homeeventsd</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.messagesescrowd</string>
 		<string>com.apple.asktod</string>
+		<string>com.apple.ak.auth.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent`

```diff

 	<array>
 		<string>com.apple.private.alloy.idstransfers</string>
 	</array>
+	<key>com.apple.private.ids.region-store</key>
+	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>
 	<true/>
 	<key>com.apple.private.imcore.imtranscoderservice</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.cloudd</string>
+		<string>com.apple.identityservicesd.regionstore</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.PowerManagement.control</string>
+		<string>com.apple.dnssd.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 		<string>eventGraphIndex</string>
 		<string>ontologyIndex</string>
 	</array>
+	<key>com.apple.intents.intents-helper</key>
+	<true/>
 	<key>com.apple.linkd.registry</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.live-entities.read</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.xpc.launchd.app-server</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appintents.live-entities.read</key>

 	<true/>
 	<key>com.apple.private.generativesearch.client.search</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
+	<key>com.apple.private.healthkit.authorization_manager</key>
+	<array>
+		<string>read</string>
+	</array>
 	<key>com.apple.private.healthkit.medicaliddata</key>
 	<true/>
+	<key>com.apple.private.healthkit.source.identities</key>
+	<array>
+		<string>com.apple.siri</string>
+	</array>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.homekit.allow-secure-access</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.GenerativeSearch.SalientNgramIndex</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>SiriSignals.SalientNgramIndex</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.intelligenceflow.blocked-apps</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.BlockedApp</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>com.apple.intelligenceflow.mail-enrichment</key>
 		<dict>
 			<key>Search</key>

 	<array>
 		<string>group.com.apple.intelligenceflow</string>
 		<string>group.com.apple.siri.inference</string>
+		<string>group.com.apple.sirievaluation</string>
 	</array>
+	<key>com.apple.private.security.storage.DuetExpertCenter</key>
+	<true/>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.sessionkit.listener</key>
+	<true/>
 	<key>com.apple.private.shazamkit.allow-external-audio-recording</key>
 	<true/>
 	<key>com.apple.private.shazamkit.allow-internal-audio-recording</key>

 	<true/>
 	<key>com.apple.private.userprofiles.read-write</key>
 	<true/>
+	<key>com.apple.proactive.AppPrediction.predictions</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Location.readOnly</key>

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.rootless.storage.proactivepredictions</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.roya.capture</key>

 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 		<string>group.com.apple.siri.inference</string>
+		<string>group.com.apple.sirievaluation</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionComplete/index.spotlightV2/Cache/</string>
+		<string>/private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionCompleteUnlessOpen/index.spotlightV2/Cache/</string>
+		<string>/private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionCompleteUntilFirstUserAuthentication/index.spotlightV2/Cache/</string>
+		<string>/private/var/mobile/Library/Spotlight/CoreSpotlight/NSFileProtectionNone/index.spotlightV2/Cache/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

 	<array>
 		<string>com.apple.team6.buddy.peer</string>
 		<string>com.apple.generativesearch.server.search</string>
+		<string>com.apple.generativelearning</string>
 		<string>com.apple.mediasetupd.server</string>
 		<string>com.apple.surfboard.entityinteractionservice</string>
 		<string>com.apple.surfboard.environmentservice</string>

 		<string>com.apple.siri.orchestration.sirix</string>
 		<string>com.apple.corespeech.corespeechd.xpc</string>
 		<string>com.apple.siri.localspeechrecognitionbridge.xpc</string>
+		<string>com.apple.siri.request.ownership.mutex.service.xpc</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.callkit.callcontrollerhost</string>
 		<string>com.apple.tipsd.assistant</string>

```
### intelligencetasksd

> `/System/Library/PrivateFrameworks/IntelligenceTasksEngine.framework/Support/intelligencetasksd`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.AppleIntelligenceReport</string>
+		<string>com.apple.applicationaccess</string>
+	</array>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```

### 🆕 journalappd

> `/System/Library/PrivateFrameworks/JournalShared.framework/Support/journalappd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.Journal</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.installcoordinationd</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.installcoordinationd</string>
	</array>
	<key>com.apple.springboard.application-removability.proxy</key>
	<true/>
	<key>com.apple.usermanagerd.persona.fetch</key>
	<true/>
</dict>
</plist>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service`

```diff

 		<array>
 			<string>com.apple.backgroundassets.managed.helper.service</string>
 		</array>
+		<key>pluginData</key>
+		<true/>
 	</dict>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.appledepthd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

 	<array>
 		<string>InverseDeviceID</string>
 	</array>
+	<key>com.apple.private.accessories.transport-client</key>
+	<true/>
 	<key>com.apple.private.accessoryupdater.client</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### mobiletimerd

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.allowOversizedPayloads</key>
 	<true/>
+	<key>com.apple.private.activitykit.assetProviderBundleIdentifier</key>
+	<true/>
 	<key>com.apple.private.activitykit.bypassAuthorizationUI</key>
 	<true/>
 	<key>com.apple.private.activitykit.canBypassActivityCountLimits</key>

 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
 	<true/>
+	<key>com.apple.private.activitykit.userPreconsentAsserter</key>
+	<true/>
 	<key>com.apple.private.alarmkit.alarmManager</key>
 	<true/>
 	<key>com.apple.private.alarmkit.authorizationManager</key>

```
### NTKFaceSnapshotService

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/XPCServices/NTKFaceSnapshotService.xpc/NTKFaceSnapshotService`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.conversation-intelligence.availability</key>
+	<true/>
 	<key>com.apple.depth.divingd</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

```
### NFUIService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.runningboard.nfc.ui.scene.service</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.seserviced.presentment-authorization</string>
+		<string>com.apple.NFCUISceneService.remote-ui</string>
 	</array>
 	<key>com.apple.seserviced.presentment-authorization</key>
 	<true/>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/searchtoold`

```diff

 	<array>
 		<string>/System/Library/PrivateFrameworks/OmniSearch.framework</string>
 	</array>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
-	<key>com.apple.private.healthkit.authorization_bypass</key>
+	<key>com.apple.private.healthkit.feature-availability.read</key>
+	<array>
+		<string>HealthAge</string>
+	</array>
+	<key>com.apple.private.healthkit.medication-doseEvent.read-write</key>
 	<true/>
+	<key>com.apple.private.healthkit.source.identities</key>
+	<array>
+		<string>com.apple.siri</string>
+	</array>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>

 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.searchd</string>
 		<string>com.apple.searchd.background</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.biome.access.user</string>

 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.searchd</string>
 		<string>com.apple.searchd.background</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.contacts.account-caching</string>
 		<string>com.apple.biome.access.user</string>

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 		<string>/Library/HTTPStorages/com.apple.amsondevicestoraged/</string>
 		<string>/Library/HTTPStorages/amsondevicestoraged/</string>
 		<string>/Library/Logs/com.apple.StoreServices/HTTPArchives/</string>
+		<string>/Library/Caches/JetPackCache/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### pebbleplayd

> `/System/Library/PrivateFrameworks/PebblePlayDaemon.framework/pebbleplayd`

```diff

 	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.remoteDeviceControlByConversationApp.allow</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.systemcontroller.allowappstoinitiateplayback</key>
 	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>

```
### PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>SensedUserContext.EventEnriched</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>SensedUserContext.Pattern</key>
 				<dict>
 					<key>mode</key>

```
### AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/AccountSubscriber`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.MailPersonaStorage</string>
+		<string>group.com.apple.calendar</string>
+		<string>group.com.apple.mail</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>AppStore</string>

 	<array>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.adid</string>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.appstored.xpc.request</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.biome.access.system</string>

 		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.FamilyControlsAgent.private</string>
+		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.iconservices</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.SettingsServices.SearchReindexService</string>

 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.ScreenTimeSettingsAgent</string>
+	<key>com.apple.springboard.addApplicationIcon</key>
+	<true/>
+	<key>com.apple.springboard.lookupFolderPathForIcon</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.intelligenceplatform.Knosis</string>
 		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.MobileAsset.SpotlightResources</string>
-		<string>com.apple.private.appintents.connection</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.triald.namespace-management</string>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>

```
### com.apple.StreamingUnzipService.privileged

> `/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.privileged.xpc/com.apple.StreamingUnzipService.privileged`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.quarantine.control</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>StreamingUnzipService</string>
 	<key>com.apple.private.vfs.entitled-reserve-access</key>

```
### com.apple.StreamingUnzipService

> `/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.quarantine.control</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>StreamingUnzipService</string>
 	<key>com.apple.private.vfs.entitled-reserve-access</key>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
-	<key>com.apple.developer.icloud-container-identifiers</key>
-	<array>
-		<string>com.apple.facetime</string>
-	</array>
-	<key>com.apple.developer.icloud-services</key>
-	<array>
-		<string>CloudDocuments</string>
-	</array>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<string>com.apple.facetime</string>
 		<string>com.apple.Photos</string>
 	</array>
-	<key>com.apple.developer.ubiquity-container-identifiers</key>
-	<array>
-		<string>com.apple.facetime</string>
-	</array>
 	<key>com.apple.duet.expertcenter.consumer</key>
 	<true/>
 	<key>com.apple.facetimed</key>

 	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
-	<key>com.apple.private.clouddocs.auto-accept-share</key>
-	<true/>
-	<key>com.apple.private.clouddocs.sharing.private-interface</key>
-	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array/>
 	<key>com.apple.private.dmd.emergency-mode</key>
 	<true/>
 	<key>com.apple.private.dmd.policy</key>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.default-app.phone</string>
 	</array>
-	<key>com.apple.private.librarian.container-proxy</key>
-	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/ActivationState</string>

 	<true/>
 	<key>com.apple.private.mediaexperience.clearmutestatecache.allow</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.silentmodenotifications.allow</key>
 	<true/>
 	<key>com.apple.private.mediasafetynet.exception.callbanner</key>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
-	<key>com.apple.private.security.storage.MobileDocuments</key>
-	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>com.apple.financed.service.financestore</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer.async</string>
+		<string>com.apple.DeviceConfigurationAgent.publisher</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.xpc-service-name</key>
 	<array>

```
### VoiceBankingDiagnostics

> `/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/PlugIns/VoiceBankingDiagnostics.appex/VoiceBankingDiagnostics`

```diff

 		<string>com.apple.accessibility.livespeech</string>
 		<string>com.apple.accessibility.voicebanking</string>
 	</array>
+	<key>com.apple.voicebanking.services</key>
+	<true/>
 </dict>
 </plist>
 

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appintents.update-app-shortcut-apps</key>

```
### matd

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/matd`

```diff

 		<string>IOAccessoryManagerUserClient</string>
 		<string>IOUSBDeviceInterfaceUserClient</string>
 	</array>
+	<key>com.apple.voicememod.client</key>
+	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>fairplay-client</key>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.springboard.flash-color</key>
 	<true/>
+	<key>com.apple.springboard.orientation-lock-service</key>
+	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 		<string>com.apple.ShortcutsActions</string>
 		<string>com.apple.ShortcutsActions.ShortcutsTopHitsExtension</string>
 	</array>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.appintents.host-managed-progress-ui</key>
+	<true/>
 	<key>com.apple.private.appintents.trusted-entity-identifier</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.springboard.flash-color</key>
 	<true/>
+	<key>com.apple.springboard.orientation-lock-service</key>
+	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 		<string>com.apple.ShortcutsActions</string>
 		<string>com.apple.ShortcutsActions.ShortcutsTopHitsExtension</string>
 	</array>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

```
### FocusConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/FocusConfigurationExtension.appex/FocusConfigurationExtension`

```diff

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### SystemActionConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### WidgetConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/WidgetConfigurationExtension.appex/WidgetConfigurationExtension`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.application-service-browse</key>

```
### bird

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/bird`

```diff

 	<true/>
 	<key>com.apple.private.foundation.fileprovideridentifier</key>
 	<string>com.apple.bird</string>
+	<key>com.apple.private.genstore.icd-fpfs-migration</key>
+	<true/>
 	<key>com.apple.private.iaaccounts</key>
 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>

```
### icloudsubscriptionoptimizerd

> `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.icloudsubscriptionoptimizerd.xpc.client.entitlement.full-access</key>
+	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.iCloudSubscriptionOptimizerCore.PFLPlugin</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.SubscriptionOptimizerTimingModels</string>

 		<string>UserFocusComputedMode</string>
 		<string>iCloud.Subscription</string>
 	</array>
+	<key>com.apple.private.ciphermld.allow</key>
+	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 		<string>com.apple.siri-distributed-evaluation</string>
 		<string>com.apple.xpc.activity.unmanaged</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
+		<string>com.apple.ciphermld</string>
+		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.xpc.amsengagementd</string>
+		<string>com.apple.amsondevicestoraged.xpc</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.mediaremote.output-device-passwords.read</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.networkd.set_source_application</key>

```

### 🆕 HealthAppAccessSettings

> `/System/Library/Settings/HealthAppAccessSettings.settings/HealthAppAccessSettings`

- No entitlements *(yet)*

### 🆕 HealthUIPlugin

> `/System/Library/Snippets/UIPlugins/HealthUIPlugin.bundle/HealthUIPlugin`

- No entitlements *(yet)*
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.accounts.facebook.defaultaccess</key>
 	<true/>
+	<key>com.apple.appconduit.remote-app-notifications.read</key>
+	<true/>
 	<key>com.apple.appleaccount.identity.read</key>
 	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>

 	<true/>
 	<key>com.apple.contacts.private</key>
 	<true/>
+	<key>com.apple.conversation-intelligence.recap</key>
+	<true/>
 	<key>com.apple.coreaudio.CanRecordPastData</key>
 	<true/>
 	<key>com.apple.coreaudio.CanRecordWithoutSessionActivation</key>

 	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
+	<key>com.apple.corespeech.uitrainingservice</key>
+	<true/>
 	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
 	<true/>
 	<key>com.apple.dataaccess.dataaccessd.PersistentPush</key>

 	<array>
 		<string>com.apple.Health</string>
 		<string>com.apple.Passbook</string>
+		<string>com.apple.campo</string>
 	</array>
 	<key>com.apple.private.userprofiles.read-write</key>
 	<true/>

 		<string>com.apple.userprofiles</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.conversation-intelligence.service</string>
+		<string>com.apple.EligibilityQuorum.com.apple.AudioIntelligence</string>
+		<string>com.apple.siri.location</string>
 		<string>com.apple.odi.legacySPIService</string>
 		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 	</array>

 		<string>com.apple.Sharing</string>
 		<string>com.apple.FitnessIntelligence</string>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.conversation-intelligence</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.usernotificationskit</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.HeartRate.preferences</string>
+		<string>com.apple.audiointelligence.topic.selection</string>
 		<string>com.apple.NanoHomeScreen.SmartStackSuggestions</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.siri.location</key>
+	<true/>
 	<key>com.apple.softposreaderd.provision</key>
 	<true/>
 	<key>com.apple.softposreaderd.unifiedreader</key>

```
### Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

 	</array>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceAddressBook</string>
+		<string>com.apple.private.avatar.store</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt.overridable</key>
 	<array>

```
### LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	</array>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<string>com.apple.DocumentsApp</string>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
+	<key>com.apple.filederivatives.derive</key>
+	<true/>
+	<key>com.apple.filederivatives.ocr</key>
+	<true/>
 	<key>com.apple.fileprovider.acl-read</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-write</key>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.desktopservices.ImageConversionService.XPC</key>
+	<true/>
 	<key>com.apple.private.diskarbitrationd.access</key>
 	<true/>
 	<key>com.apple.private.familycircle</key>

 		<string>com.apple.ProgressReporting</string>
 		<string>com.apple.FileProvider.ArchiveService</string>
 		<string>com.apple.desktopservices.ArchiveService</string>
+		<string>com.apple.desktopservices.ImageConversionService</string>
 		<string>com.apple.searchd</string>
 		<string>com.apple.FileProvider</string>
 		<string>com.apple.spotlight.userfs</string>

 		<string>com.apple.CoreServices.coreservicesd</string>
 		<string>com.apple.SmartNameSuggestionsService</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.FileDerivativeService</string>
+		<string>com.apple.FSEvents</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	</array>
 	<key>com.apple.developer.siri</key>
 	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>INTERNAL.com.apple.Fitness</string>
 	<key>com.apple.fitcore</key>
 	<true/>
 	<key>com.apple.fitcore.session</key>

```

### 🆕 AppEditIn

> `/private/var/staged_system_apps/Freeform.app/Frameworks/AppEditIn.framework/AppEditIn`

- No entitlements *(yet)*
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 	<array>
 		<string>L6VBL6N964.com.apple.freeform</string>
 		<string>CXZ9PY4T4T.group.com.analytics.shared.teams</string>
+		<string>CXZ9PY4T4T.com.apple.appsubscriptions.shared</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.fpsd.client</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	</array>
 	<key>com.apple.media.ringtones.read-only</key>
 	<true/>
+	<key>com.apple.mediaremote.set-playback-state</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.silentmodenotifications.allow</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 		<string>com.apple.paired-unlock</string>
 		<string>com.apple.heartratecoordinatord.observer</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.modelcatalog.catalog</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<string>1</string>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>

 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>
 	<true/>
+	<key>com.apple.private.cloudkit.systemService</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

 		<string>com.apple.Preferences</string>
 		<string>com.apple.Sharing</string>
 		<string>com.apple.applejpeg</string>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.avfaudio</string>
 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>

 		<string>com.apple.Preferences</string>
 		<string>com.apple.Sharing</string>
 		<string>com.apple.applejpeg</string>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.avfaudio</string>
 		<string>com.apple.avfoundation.frecents</string>
 		<string>com.apple.corehaptics</string>

```
### HomeDiagnosticExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeDiagnosticExtension.appex/HomeDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<key>com.apple.security.application-groups</key>
 	<array>
-		<string>/Library/Caches/com.apple.home/</string>
+		<string>com.apple.Home.group</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
-	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/Caches/com.apple.home/</string>
-	</array>
 </dict>
 </plist>
 

```
### HomeFeedbackDiagnosticExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeFeedbackDiagnosticExtension.appex/HomeFeedbackDiagnosticExtension`

```diff

 	<string>com.apple.Home.HomeFeedbackDiagnosticExtension</string>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>com.apple.Home.group</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Containers/Data/Application/</string>
-		<string>/Library/Caches/com.apple.home/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Containers/Data/Application/</string>
-		<string>/Library/Caches/com.apple.home/</string>
 	</array>
 </dict>
 </plist>

```
### Journal

> `/private/var/staged_system_apps/Journal.app/Journal`

```diff

 		<string>MOUserNotifications</string>
 		<string>MOOnboardingAndSettings</string>
 	</array>
+	<key>com.apple.private.InstallCoordination.allowed</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.installcoordinationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>com.apple.momentsd</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.installcoordinationd</string>
+	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.springboard.application-removability.proxy</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>511712240</string>
 	<key>keychain-access-groups</key>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.Magnifier</string>
+	<key>com.apple.AXMediaUtilitiesService-access</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AXMediaUtilitiesService</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.modelmanager</string>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 		<string>com.apple.MessagesBlastDoorService</string>
 		<string>com.apple.UnknownSendersBlastDoorService</string>
 		<string>com.apple.voicememod.xpc</string>
+		<string>com.apple.voicememod.client</string>
 		<string>com.apple.dprivacyd</string>
 		<string>com.apple.financed.service.financestore</string>
 		<string>com.apple.routined.safetyMonitor</string>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.lsuseractivityd.bestappsuggestion</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
+	<key>com.apple.private.corewifi.keychain</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>

 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.AutoUnlock.AuthenticationHintsProvider</string>
 		<string>com.apple.UserNotifications.OneTimeCodeService</string>
+		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.sage.summarization</string>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.private.jetpackassetd</key>
 	<true/>
+	<key>com.apple.private.mediacontentsafety.client</key>
+	<true/>
 	<key>com.apple.private.musicd.client</key>
 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>
-		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceFaceID</string>
-		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>

 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.musicd</string>
+		<string>com.apple.frontboard.systemappservices</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.shortcutitems.customimage</key>
 	<true/>
 	<key>com.apple.springboard.wallpaperAnimationSuspension</key>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.coreaudio.app-tap</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreidvd.spi</key>

 	</array>
 	<key>com.apple.private.xpc.domain-extension</key>
 	<true/>
-	<key>com.apple.proactive.PersonalizationPortrait.Config</key>
-	<true/>
-	<key>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</key>
-	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.routined.internal</string>
 		<string>com.apple.SafariLaunchAgent</string>
-		<string>com.apple.proactive.PersonalizationPortrait.Config</string>
-		<string>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.SharedWebCredentials</string>
 		<string>com.apple.fpsd</string>

 		<string>com.apple.MobileTimer.timerserver</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.sportsd.xpc</string>
+		<string>com.apple.nehelper</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.usernotifications.time-sensitive</key>
+	<true/>
 	<key>com.apple.email.maild</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.airdrop.client</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 	<true/>
 	<key>com.apple.private.corewifi.keychain</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

 		<string>com.apple.ak.privateemail.xpc</string>
 		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.privatecloudcompute</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>application-identifier</key>
 	<string>com.apple.mobileslideshow</string>
 	<key>backupd-connection-initiate</key>

 	<true/>
 	<key>com.apple.proactive.visual-action-prediction</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>

 		<string>/Library/LiveFiles/</string>
 		<string>/Library/Logs/MediaServices/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/Shortcuts/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.siri.activation.service</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
 		<string>com.apple.visualintelligence.visual-action-prediction</string>
+		<string>com.apple.appledepthd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.sharesheet.allow-custom-view</key>
 	<true/>
+	<key>com.apple.shortcuts.stepwise-execution</key>
+	<true/>
+	<key>com.apple.shortcuts.variable-injection</key>
+	<true/>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 	<key>com.apple.siri.activation</key>
 	<true/>
 	<key>com.apple.siri.activation.service</key>

```
### PhotosReliveWidget

> `/private/var/staged_system_apps/Photos.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget`

```diff

 	<string>com.apple.mobileslideshow.PhotosReliveWidget</string>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.developer.sensitivecontentanalysis.client</key>
+	<array>
+		<string>analysis</string>
+	</array>
+	<key>com.apple.mediaanalysisd.client</key>
+	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 		<string>photos.memory</string>
 		<string>photos.person</string>
 		<string>photos.scene</string>
+		<string>photos.shareparticipant</string>
 	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
+	<key>com.apple.private.tcc.allow.overridable</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 		<string>com.apple.ShortcutsActions</string>
 		<string>com.apple.ShortcutsActions.ShortcutsTopHitsExtension</string>
 	</array>
+	<key>com.apple.private.appintents.connection</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.orientation-lock-service</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.springboard.removeWebClipFromHomeScreen</key>

```

### 🆕 SiriShareExtension

> `/private/var/staged_system_apps/SiriApp.app/PlugIns/SiriShareExtension.appex/SiriShareExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.campo-client</key>
	<true/>
	<key>com.apple.developer.auto-elect-plugin</key>
	<true/>
</dict>
</plist>

```
### Stocks

> `/private/var/staged_system_apps/Stocks.app/Stocks`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.coreaudio.app-tap</key>
+	<true/>
 	<key>com.apple.developer.applesignin</key>
 	<array>
 		<string></string>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.nehelper</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### WeatherAppIntents

> `/private/var/staged_system_apps/Weather.app/Extensions/WeatherAppIntents.appex/WeatherAppIntents`

```diff

 	<array>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.routined.registration</string>
+		<string>com.apple.weatherd.notifications</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 WeatherFace

> `/private/var/staged_system_apps/Weather.app/Extensions/WeatherFace.appex/WeatherFace`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.weather</string>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.appintents.extension-mediator.bundle-identifier</key>
	<string>com.apple.weather</string>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.storage.Weather</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.weather</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Weather/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.perceptiond.entitykit</string>
		<string>com.apple.perceptiond.api</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
		<string>/AppleInternal/Library/Bundles/WeatherInternalExtras.bundle/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.weather</string>
		<string>com.apple.weather.internal</string>
		<string>com.apple.weather.sensitive</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```
### Weather

> `/private/var/staged_system_apps/Weather.app/Weather`

```diff

 	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>com.apple.weather</string>
+	</array>
 </dict>
 </plist>
 

```
### perfpowermetricd

> `/usr/bin/perfpowermetricd`

```diff

 	<true/>
 	<key>com.apple.private.mcc.datacollection-access</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.network.statistics</key>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.private.mcc.datacollection-access</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.network.statistics</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.mcc.datacollection-access</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.network.ipsec-wake-packet</key>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.private.mcc.datacollection-access</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.network.statistics</key>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	<true/>
 	<key>com.apple.private.ReportSystemMemory</key>
 	<true/>
+	<key>com.apple.private.accessories.transport-client</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>

```

### 🆕 agentmanagerd

> `/usr/libexec/agentmanagerd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.AgentManager.agentmanagerd</string>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>AppleIntelligence.Reporting.Invocation.Step</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.Events</string>
		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>
	</array>
	<key>com.apple.private.corepersonalization.client.insights</key>
	<true/>
	<key>com.apple.private.corepersonalization.client.workflowExecution</key>
	<true/>
	<key>com.apple.private.generativesearch.client.index</key>
	<true/>
	<key>com.apple.private.generativesearch.client.search</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>com.apple.generativelearningplatform</key>
		<dict>
			<key>Search</key>
			<array>
				<string>AutofillExtraction</string>
				<string>Calendar</string>
				<string>Contact</string>
				<string>ExplicitMemory</string>
				<string>FrequentLocation</string>
				<string>Global</string>
				<string>NameInsight</string>
				<string>Mail</string>
				<string>Message</string>
				<string>NLPObservation</string>
				<string>Note</string>
				<string>Reminder</string>
				<string>RoutineHabit</string>
				<string>SensedContextEvent</string>
				<string>SensedContextAugmentedEvent</string>
				<string>SensedContextPattern</string>
				<string>SensedContextPerson</string>
				<string>SensedContextPlace</string>
				<string>SiriTranscript</string>
				<string>SiriTranscriptConversation</string>
				<string>Summary</string>
				<string>UserActivity</string>
				<string>HealthSummary</string>
				<string>FitnessActivityRings</string>
				<string>FitnessMindfulSession</string>
				<string>FitnessWorkout</string>
				<string>HealthCategorySample</string>
				<string>HealthCharacteristics</string>
				<string>HealthClassification</string>
				<string>HealthStatistics</string>
				<string>HealthSleepDaySummary</string>
				<string>HealthStateOfMindSample</string>
				<string>HealthOvernightVitalsSummary</string>
			</array>
			<key>Sets</key>
			<dict>
				<key>App.Intents.IndexedEntity</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Cascade.CachedDocument</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>GenerativeLearningPlatform.EchoRecord</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>GenerativeLearningPlatform.Insight</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>GenerativeLearningPlatform.SummarizationRecord</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontextevent</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.Event</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontexteventenriched</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.EventEnriched</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontextpattern</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.Pattern</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontextplace</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.Place</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/SearchManager/</string>
		<string>/tmp/com.apple.agentmanager/</string>
		<string>/private/var/mobile/Library/generativelearningd/</string>
		<string>/private/var/mobile/Library/Application Support/GenerativeLearningPlatform/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.TapToRadarKit.service</string>
		<string>com.apple.corepersonalization.server.workflowExecution</string>
		<string>com.apple.corepersonalization.server.insights</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.health.shared</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.agentmanager</string>
	<key>com.apple.trial.client</key>
	<array>
		<string>SSP_HEALTH_CONFIG</string>
	</array>
	<key>com.apple.usermanagerd.persona.fetch</key>
	<true/>
</dict>
</plist>

```
### announced

> `/usr/libexec/announced`

```diff

 		<string>com.apple.assistant.multiuser.service.remora</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.userprofiles</string>
+		<string>com.apple.corespeech.corespeechd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.anomalydetectiond</string>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+	</array>
 	<key>com.apple.aop.fastpath.user-client</key>
 	<dict>
 		<key>AHAFp</key>

 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.frontboard.systemappservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### appledepthd

> `/usr/libexec/appledepthd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_AppleDepth_MLModel/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.AppleDepth.MLModel/shared_locks/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
+	<key>com.apple.security.ts.asset-access</key>
+	<true/>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.backboardd.replacesystemapp</key>
 	<true/>
+	<key>com.apple.backlight.allowsActivationObservation</key>
+	<true/>
 	<key>com.apple.backlight.allowsPerformingEventObservation</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

```
### batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

 		<string>BATTERYINTELLIGENCE_BHF</string>
 		<string>BATTERYINTELLIGENCE_BATTERY_ANALYSIS</string>
 		<string>BATTERYINTELLIGENCE_BATTERY_ANALYSIS_TTL</string>
+		<string>BATTERYINTELLIGENCE_TLC</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### cameracaptured

> `/usr/libexec/cameracaptured`

```diff

 	<true/>
 	<key>com.apple.private.mediaexperience.cleanvoice.allow</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.suppressregionalcamerasystemsoundbehavior.allow</key>
 	<true/>
 	<key>com.apple.private.privacy.accounting.write</key>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.cloudkit.customAccounts</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.CompanionServices</key>

 	<array>
 		<string>access-call-capabilities</string>
 	</array>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```

### 🆕 conversationd

> `/usr/libexec/conversationd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.conversationd</string>
	<key>aps-environment</key>
	<string>Production</string>
	<key>com.apple.AudioAccessoryServices</key>
	<true/>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.TextUnderstanding.process</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.generativeexperiences.agentSessionStore</key>
	<true/>
	<key>com.apple.mediaremote.remote-control-discovery</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.nano.nanoregistry</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.networkrelay.deviceMonitor</key>
	<true/>
	<key>com.apple.networkrelay.devicePreferences</key>
	<true/>
	<key>com.apple.networkrelay.devices.read</key>
	<true/>
	<key>com.apple.private.application-service-browse</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.reverie</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.Events</string>
		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
	<array>
		<string>com.apple.AudioIntelligence</string>
	</array>
	<key>com.apple.private.exclaves.conclave-host</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>ConversationCaptureContextCollection</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>App.InFocus</string>
				<string>Siri.Execution</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.managed-settings.effective-read</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.sessionkit.custom-platter-target</key>
	<true/>
	<key>com.apple.private.sessionkit.customPushProcessIdentifier</key>
	<true/>
	<key>com.apple.private.sessionkit.sessionRequest</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCalendar</string>
	</array>
	<key>com.apple.private.tcc.manager.access.read</key>
	<array>
		<string>kTCCServiceSiriAccess</string>
	</array>
	<key>com.apple.private.trustedclocking.workloop-control</key>
	<true/>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.campo</string>
	</array>
	<key>com.apple.relevanced.AudioUnderstanding.live-rewind</key>
	<true/>
	<key>com.apple.relevanced.AudioUnderstanding.recap</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.reverie</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/</string>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>com.apple.RelevancePlatform.AudioUnderstanding</string>
		<string>/private/var/mobile/tmp/</string>
		<string>/dev/exfiltration-adc-conversatio</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>TrustedClockingUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.private.sessionkit.customPushProcessIdentifier</string>
		<string>com.apple.relevanced.AudioUnderstanding</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.generativeexperiences.agentSessionStore</string>
		<string>com.apple.nanoprefsync</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.compute.publisher.service.user</string>
		<string>com.apple.deviceconfigurationd.consumer</string>
		<string>com.apple.mediaremoted.xpc</string>
		<string>com.apple.AudioAccessoryServices</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.tccd</string>
		<string>com.apple.accountsd.accountmanager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.demo-settings</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.reverie</string>
		<string>com.apple.EligibilityQuorum</string>
		<string>com.apple.campo</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>kern.stackshot_stats</string>
		<string>kern.exclaves_status</string>
		<string>kern.task_conclave</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-write</key>
	<array>
		<string>kern.bootargs</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
		<string>TrustedClockingUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.siri.speakerprofile.embedding.service.xpc</key>
	<true/>
	<key>nano-preferences-read-write</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 corepersonalizationd

> `/usr/libexec/corepersonalizationd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.CorePersonalization.corepersonalizationd</string>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.agentmanager.client.registration</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>AppleIntelligence.Reporting.Invocation.Step</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.Events</string>
		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>
	</array>
	<key>com.apple.private.generativesearch.client.index</key>
	<true/>
	<key>com.apple.private.generativesearch.client.search</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.key-value.local.read-write</key>
	<array>
		<string>com.apple.private.health.healthplans.featureStatus</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>com.apple.corepersonalization</key>
		<dict>
			<key>Search</key>
			<array>
				<string>AutofillExtraction</string>
				<string>Calendar</string>
				<string>Contact</string>
				<string>ExplicitMemory</string>
				<string>FrequentLocation</string>
				<string>Global</string>
				<string>NameInsight</string>
				<string>Mail</string>
				<string>Message</string>
				<string>NLPObservation</string>
				<string>Note</string>
				<string>Reminder</string>
				<string>RoutineHabit</string>
				<string>SensedContextEvent</string>
				<string>SensedContextAugmentedEvent</string>
				<string>SensedContextPattern</string>
				<string>SensedContextPerson</string>
				<string>SensedContextPlace</string>
				<string>SiriTranscript</string>
				<string>SiriTranscriptConversation</string>
				<string>Summary</string>
				<string>UserActivity</string>
				<string>HealthSummary</string>
				<string>FitnessActivityRings</string>
				<string>FitnessMindfulSession</string>
				<string>FitnessWorkout</string>
				<string>HealthCategorySample</string>
				<string>HealthCharacteristics</string>
				<string>HealthClassification</string>
				<string>HealthStatistics</string>
				<string>HealthSleepDaySummary</string>
				<string>HealthStateOfMindSample</string>
				<string>HealthOvernightVitalsSummary</string>
			</array>
			<key>Sets</key>
			<dict>
				<key>App.Intents.IndexedEntity</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Cascade.CachedDocument</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>CorePersonalization.EchoRecord</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>CorePersonalization.SummarizationRecord</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>GenerativeLearningPlatform.Insight</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.healthmeasurement</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>Fitness.ActivityRings</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Fitness.MindfulSession</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Fitness.Workout</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Health.Measurement</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontextevent</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.Event</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontexteventenriched</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.EventEnriched</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontextpattern</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.Pattern</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontextperson</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.Person</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.generativelearningplatform.cascade.sensedcontextplace</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SensedUserContext.Place</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/CorePersonalization/</string>
		<string>/tmp/com.apple.corepersonalization/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.agentmanager.server.registration</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.generativesearch.server.search</string>
		<string>com.apple.contactsd</string>
		<string>com.apple.lsd.modifydb</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.biome.compute.source.user</string>
		<string>com.apple.SetStoreUpdateService</string>
		<string>com.apple.healthd.server</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.health.shared</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.corepersonalization</string>
</dict>
</plist>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceAudioAccessoryHeadTrackData</string>
+		<string>kTCCServiceAccessoryWorker</string>
+		<string>kTCCServiceAccessoryWorkerGPU</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>

 		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceAudioAccessoryHeadTrackData</string>
+		<string>kTCCServiceAccessoryWorker</string>
+		<string>kTCCServiceAccessoryWorkerGPU</string>
 	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>
 	<array>

 	</array>
 	<key>com.apple.private.validated-resolver</key>
 	<true/>
+	<key>com.apple.runningboard.extensionkit</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>

```
### gamed

> `/usr/libexec/gamed`

```diff

 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>IAPHistory</string>
+		<string>Library</string>
+		<string>PurchaseHistory</string>
 	</array>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>

```
### idcredd

> `/usr/libexec/idcredd`

```diff

 	<string>com.apple.coreidv.idcredd</string>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.internal.seserviced.ptattestation</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.seserviced</string>

```
### locationd

> `/usr/libexec/locationd`

```diff

 			<key>send-command</key>
 			<dict/>
 		</dict>
-		<key>orientation_2</key>
-		<dict>
-			<key>send-command</key>
-			<dict/>
-		</dict>
 		<key>pdr</key>
 		<dict>
 			<key>send-command</key>

 		<string>/private/var/mobile/Library/Preferences/com.apple.workout.features.dormancy.plist</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.nanolifestyle.sessiontrackerapp.plist</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/mobile/Library/DeviceRegistry/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.nanolifestyle.privacy</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.workout.features.dormancy</string>
+		<string>com.apple.RelevancePlatform.AudioUnderstanding</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 	</array>
 	<key>com.apple.private.mediaAccessibility.customBundle</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.queryrecordingclients.allow</key>
+	<true/>
 	<key>com.apple.private.memory.ownership_transfer</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```

### 🆕 memoryanalyticsd

> `/usr/libexec/memoryanalyticsd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.memoryanalyticsd</string>
	<key>com.apple.diagnosticpipeline.request</key>
	<true/>
	<key>com.apple.private.AuthorizationServices</key>
	<array>
		<string>system.preferences.nvram</string>
	</array>
	<key>com.apple.private.osanalytics.defaults.allow </key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.ReportMemoryException</string>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.system-task-ports.read</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>MEMORY_ANALYSIS_MODEL_LOADING</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>appleaccount</string>
	</array>
</dict>
</plist>

```
### misd

> `/usr/libexec/misd`

```diff

 	<true/>
 	<key>com.apple.pf.allow</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.system-job-bootstrap</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOUserEthernetResourceUserClient</string>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
+		<string>com.apple.MobileAsset.UAF.FOVI</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
+		<string>com.apple.MobileAsset.UAF.IntelligentConversationExtraction</string>
 		<string>com.apple.MobileAsset.UAF.MotionAnomalyFM</string>
 		<string>com.apple.MobileAsset.UAF.Music.ConcertsRanking</string>
 		<string>com.apple.MobileAsset.UAF.Photos.SpatialPhotosRelive</string>

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FOVI/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Handwriting_Synthesis/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Photos_SpatialPhotosRelive/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_Planner/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IntelligentConversationExtraction/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_MotionAnomalyFM/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Music_ConcertsRanking/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_DialogAssets/</string>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FOVI/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Handwriting_Synthesis/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_SpatialPhotosRelive/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IF_Planner/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IF_PlannerOverrides/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_IntelligentConversationExtraction/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_MotionAnomalyFM/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Music_ConcertsRanking/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Siri_DialogAssets/</string>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.database-accessibility-assertion</key>
 	<true/>
+	<key>com.apple.private.healthkit.key-value.local.read-write</key>
+	<array>
+		<string>com.apple.private.health.healthplans.featureStatus</string>
+	</array>
 	<key>com.apple.private.healthkit.metadata.private</key>
 	<true/>
 	<key>com.apple.private.healthkit.read_authorization_bypass</key>

```
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>com.apple.locationd.Proximity.TagManagement</key>
 	<true/>
+	<key>com.apple.locationd.accessory_location</key>
+	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.asmanager</key>

 	<true/>
 	<key>com.apple.locationd.gnss-extensions</key>
 	<true/>
+	<key>com.apple.locationd.harvest.contribute</key>
+	<true/>
 	<key>com.apple.locationd.inertialodometry</key>
 	<true/>
 	<key>com.apple.locationd.motion_alarms-system-client</key>

 		<string>com.apple.AccessorySensorManager</string>
 		<string>com.apple.BacklightServices.backlight</string>
 		<string>com.apple.DeviceAccess.xpc</string>
+		<string>com.apple.locationd.harvester</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceUserTracking</string>

 		<string>AD_PLATFORMS_APPSTORE_SRP_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_TT_INCREMENTALITYAPPSTORE</string>
 		<string>AD_PLATFORMS_APPSTORE_PP_INCREMENTALITYAPPSTORE</string>
+		<string>AD_PLATFORMS_RN_CORE_SEARCH_RN_AA_TEST</string>
+		<string>AD_PLATFORMS_RN_SEARCH_HOME_RN_AA_TEST</string>
+		<string>AD_PLATFORMS_APPSTORE_SLP_ADEVENTKIT</string>
+		<string>AD_PLATFORMS_APPSTORE_SRP_ADEVENTKIT</string>
+		<string>AD_PLATFORMS_APPSTORE_TT_ADEVENTKIT</string>
+		<string>AD_PLATFORMS_APPSTORE_PP_ADEVENTKIT</string>
 	</array>
 	<key>fairplay-client</key>
 	<string>700802717</string>

```
### remoteappintentsd

> `/usr/libexec/remoteappintentsd`

```diff

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.diagnosticpipeline.service</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.observationStatusRegistry</string>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>
 	<true/>
+	<key>com.apple.private.healthkit.key-value.local.read-write</key>
+	<array>
+		<string>com.apple.private.health.healthplans.featureStatus</string>
+	</array>
 	<key>com.apple.private.healthkit.medicaliddata</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.lsd.mapdb</string>
+		<string>com.apple.ctkd.token-client</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<true/>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.safetyalertsd.secureAlerts</string>
+	</array>
 </dict>
 </plist>
 

```
### safetycheckd

> `/usr/libexec/safetycheckd`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.SafetyMonitor</key>
 	<true/>
+	<key>com.apple.Maps.MapsSync.access</key>
+	<true/>
 	<key>com.apple.Maps.tripsharing.sharing</key>
 	<true/>
 	<key>com.apple.activitysharingd</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
+	<key>com.apple.findmy.locationquality.access</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.geoanalyticsd.telemetry</key>

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.locationd.routine</key>
+	<true/>
 	<key>com.apple.locationd.status</key>
 	<true/>
 	<key>com.apple.mobileactivationd.bridge</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
+		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

```
### seld

> `/usr/libexec/seld`

```diff

 	<array>
 		<string>com.apple.seserviced</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 		<string>com.apple.triald</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
+		<string>com.apple.assistant.public</string>
 		<string>com.apple.mobilecal</string>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.gms.availability</string>

```

### 🆕 siriusergroundingd

> `/usr/libexec/siriusergroundingd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.duetactivityscheduler.allow</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SalientNgramIndexDonation</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>SiriSignals.SalientNgramIndex</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/com.apple.siriusergroundingd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.SetStoreUpdateService</string>
	</array>
	<key>com.apple.security.exception.mach-register.global-name</key>
	<array>
		<string>com.apple.generativesearch.server.salientpostings</string>
		<string>com.apple.generativesearch.server.salienttokenize</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.siriusergroundingd</string>
	</array>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.siriusergroundingd</string>
</dict>
</plist>

```
### softposreaderd

> `/usr/libexec/softposreaderd`

```diff

 	<true/>
 	<key>com.apple.private.applesse.baa</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.personallyidentifiableinformation.allow </key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.seserviced.sereservation.client</key>

```
### spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.corepersonalization.client.graphEmbedding</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allowcarplayapps</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

 	<true/>
 	<key>com.apple.private.generativesearch.client.index</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.salientpostings</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.spotlightknowledge</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>CorePersonalization.IndexableEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>DocumentProcessing.TestItem</key>
 				<dict>
 					<key>mode</key>

 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.generativesearch.server.indexing</string>
+		<string>com.apple.corepersonalization.server.graphEmbedding</string>
+		<string>com.apple.generativesearch.server.salientpostings</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Turn</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Conversation</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.corepersonalization.client.graphEmbedding</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allowcarplayapps</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

 	<true/>
 	<key>com.apple.private.generativesearch.client.index</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.salientpostings</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.spotlightknowledge</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>CorePersonalization.IndexableEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>DocumentProcessing.TestItem</key>
 				<dict>
 					<key>mode</key>

 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.generativesearch.server.indexing</string>
+		<string>com.apple.corepersonalization.server.graphEmbedding</string>
+		<string>com.apple.generativesearch.server.salientpostings</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Turn</string>
 		<string>com.apple.cascade.donationrequest.Siri.Transcript.Conversation</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### symptomsd

> `/usr/libexec/symptomsd`

```diff

 	<true/>
 	<key>com.apple.private.network.statistics</key>
 	<true/>
+	<key>com.apple.private.networkextension.configuration</key>
+	<true/>
 	<key>com.apple.private.networkserviceproxy</key>
 	<true/>
 	<key>com.apple.private.nlcd-control</key>

```
### symptomsd-helper

> `/usr/libexec/symptomsd-helper`

```diff

 	<true/>
 	<key>com.apple.private.network.statistics</key>
 	<true/>
+	<key>com.apple.private.networkextension.configuration</key>
+	<true/>
 	<key>com.apple.private.networkserviceproxy</key>
 	<true/>
 	<key>com.apple.private.nlcd-control</key>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	<true/>
 	<key>com.apple.private.container.debug</key>
 	<true/>
+	<key>com.apple.private.device-configuration.diagnostics</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.dumpSysdiagnoseDataToDir</key>
 	<true/>
 	<key>com.apple.private.endpoint-security.xpc</key>

 		<string>group.com.apple.cv3d.dgn</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<string>com.apple.intelligenceplatform.Sysdiagnose</string>
+	<array>
+		<string>com.apple.intelligenceplatform.Sysdiagnose</string>
+		<string>com.apple.deviceconfigurationd.diagnostics.async</string>
+		<string>com.apple.DeviceConfigurationAgent.diagnostics.async</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.voicetrigger.notbackedup</string>

```
### terminusd

> `/usr/libexec/terminusd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmapbundleidtouuid</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 	<true/>
 	<key>com.apple.symptoms.linkAdvisory.ULPN</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>TERMINUS_COMPANION_APL</string>
+	</array>
 	<key>com.apple.wifip2pd</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<true/>
 	<key>com.apple.homepodaccessorysettings.client</key>
 	<true/>
-	<key>com.apple.icloud.findmydeviced.localfindable</key>
-	<true/>
 	<key>com.apple.icloud.findmydeviced.localfindable.tvremote</key>
 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>

 		<string>com.apple.watchlistd.xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>
-		<string>com.apple.icloud.findmydeviced.localfindable</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### uarppersonalizationd

> `/usr/libexec/uarppersonalizationd`

```diff

 	</array>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.uarppersonalizationd</string>
+	<key>com.apple.mobileactivationd.bridge</key>
+	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.installerauthagent</string>
 		<string>com.apple.AppSSO.service-xpc</string>
 		<string>com.apple.uarp.asset.personalization.complete</string>
+		<string>com.apple.mobileactivationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.uarppersonalization.btleserver</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>com.apple.narrative.client</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.private.accessories.transport-client</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

```
### wifid

> `/usr/sbin/wifid`

```diff

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.centaurid.xpc</string>
+		<string>com.apple.wirelessperception.session</string>
 		<string>com.apple.AccessorySetupUI</string>
 		<string>com.apple.AccessorySetupUI.services.presenter</string>
 		<string>com.apple.lsd.mapdb</string>

 	<true/>
 	<key>com.apple.wifivelocity</key>
 	<true/>
+	<key>com.apple.wirelessperception.session</key>
+	<true/>
 	<key>com.apple.wlan.authentication</key>
 	<true/>
 	<key>keychain-access-groups</key>

```


### SystemOS

### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
 		<string>com.apple.mediaaccessibility.captionAppearanceSettingsChanged</string>
 		<string>com.apple.powerlog.state_changed</string>
+		<string>com.apple.powerlog.state_changed.ClientID.*</string>
 		<string>com.apple.preferences.sounds.keyboard-audio.changed</string>
 		<string>com.apple.runningboard.daemonstartup</string>
 		<string>com.apple.system.logging.prefschanged</string>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/ExtensionKit/Extensions/WebContentEnhancedSecurityExtension.appex/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
 		<string>com.apple.mediaaccessibility.captionAppearanceSettingsChanged</string>
 		<string>com.apple.powerlog.state_changed</string>
+		<string>com.apple.powerlog.state_changed.ClientID.*</string>
 		<string>com.apple.preferences.sounds.keyboard-audio.changed</string>
 		<string>com.apple.runningboard.daemonstartup</string>
 		<string>com.apple.system.logging.prefschanged</string>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>com.apple.mediaaccessibility.audibleMediaSettingsChanged</string>
 		<string>com.apple.mediaaccessibility.captionAppearanceSettingsChanged</string>
 		<string>com.apple.powerlog.state_changed</string>
+		<string>com.apple.powerlog.state_changed.ClientID.*</string>
 		<string>com.apple.preferences.sounds.keyboard-audio.changed</string>
 		<string>com.apple.runningboard.daemonstartup</string>
 		<string>com.apple.system.logging.prefschanged</string>

 	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>
+	<key>com.apple.private.verified-jit-mode</key>
+	<integer>1</integer>
 	<key>com.apple.private.web-browser-engine.webcontent</key>
 	<true/>
 	<key>com.apple.private.webinspector.allow-remote-inspection</key>

```


### AppOS

### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<string>com.apple.mobilesafari</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.BTServer.rawBytesAdvertise</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.keychain.inet_expansion_fields</key>

```
### SafariBookmarksSyncAgent

> `/usr/libexec/SafariBookmarksSyncAgent`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.bundleid</key>
 	<string>com.apple.mobilesafari</string>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.safari.notify</string>
+	</array>
+	<key>com.apple.private.ids.messaging.urgent-priority</key>
+	<array>
+		<string>com.apple.private.alloy.safari.notify</string>
+	</array>
+	<key>com.apple.private.ids.registration</key>
+	<array>
+		<string>com.apple.private.alloy.safari.notify</string>
+	</array>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>*</string>
 	<key>com.apple.private.security.container-required</key>

 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.securityd</string>
 		<string>com.apple.linkd.application-service</string>
+		<string>com.apple.siriactionsd.xpc</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.identityservicesd.nsxpc</string>
+		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.linkd.registry</string>
 		<string>com.apple.spotlight.SearchAgent</string>
 	</array>
+	<key>com.apple.security.exception.mach-register.global-name</key>
+	<array>
+		<string>com.apple.private.alloy.safari.notify-idswake</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mobilesafarishared</string>
 	</array>
+	<key>com.apple.shortcuts.trigger-editing</key>
+	<true/>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.Safari.WBSDevice</string>

```
### webpushd

> `/usr/libexec/webpushd`

```diff

 <dict>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.private.launchservices.allowopenwithanyhandler</key>

 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```


### ExclaveOS


### 🆕 TextUnderstandingExclaveKitComponent

> `/System/ExclaveKit/System/Library/PrivateFrameworks/TextUnderstandingExclaveKitComponent.framework/TextUnderstandingExclaveKitComponent`

- No entitlements *(yet)*


