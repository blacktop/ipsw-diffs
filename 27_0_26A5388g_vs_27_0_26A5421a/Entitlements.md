## 🔑 Entitlements

### filesystem

### App Store

> `/System/Applications/App Store.app/Contents/MacOS/App Store`

```diff

 		<string>com.apple.AppStore</string>
 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.gamecenter</string>
+		<string>com.apple.storeservices.itfe</string>
 	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>

```
### Games

> `/System/Applications/Games.app/Contents/MacOS/Games`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents.build-lockup-from-mapi-response</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.small-offer-button</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Ocelot</string>

 		<string>com.apple.GameStoreKit</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.storeservices.itfe</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### Home

> `/System/Applications/Home.app/Contents/MacOS/Home`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.ageRange</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### GenerativePlaygroundAppIntents

> `/System/Applications/Image Playground.app/Contents/Extensions/GenerativePlaygroundAppIntents.appex/Contents/MacOS/GenerativePlaygroundAppIntents`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.GenerativePlaygroundAppIntents</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GenerativePlaygroundAppIntents</string>
 	<key>com.apple.appprotectiond.guard.access</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
 	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### Image Playground

> `/System/Applications/Image Playground.app/Contents/MacOS/Image Playground`

```diff

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_PromptBasedSegmentation/</string>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Applications/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.stickers.api</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>

```
### GenerativePlaygroundMessagesAppExtension

> `/System/Applications/Image Playground.app/Contents/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/Contents/MacOS/GenerativePlaygroundMessagesAppExtension`

```diff

 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Applications/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>

```
### Journal

> `/System/Applications/Journal.app/Contents/MacOS/Journal`

```diff

 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.CloudSubscriptionFeatures.datadetectors</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Messages

> `/System/Applications/Messages.app/Contents/MacOS/Messages`

```diff

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCamera</string>
+		<string>kTCCServiceCalendar</string>
 	</array>
 	<key>com.apple.private.tcc.allow-prompting</key>
 	<array>

 		<string>com.apple.BTLEAudioController.xpc</string>
 		<string>com.apple.transparencyd</string>
 		<string>com.apple.transparencyd.ids</string>
+		<string>com.apple.CalendarAgent</string>
 		<string>com.apple.CoreLocation.agent</string>
 		<string>com.apple.locationd.desktop.registration</string>
 		<string>com.apple.locationd.desktop.synchronous</string>

 SYS_recvfrom_nocancel
 SYS_recvmsg
 SYS_rename
+SYS_renameat
 SYS_renameatx_np
 SYS_rmdir
 SYS_sendmsg

```
### News

> `/System/Applications/News.app/Contents/MacOS/News`

```diff

 	<string>production</string>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.background-tasks.continued-processing.inference</key>
+	<true/>
 	<key>com.apple.developer.game-center</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

```
### Notes

> `/System/Applications/Notes.app/Contents/MacOS/Notes`

```diff

 	<true/>
 	<key>com.apple.modelmanager.assertion</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.pds.clientid</key>
 	<string>Notes</string>
 	<key>com.apple.private.CloudSharing.SPI</key>

```
### PasswordsMenuBarExtra

> `/System/Applications/Passwords.app/Contents/Library/LoginItems/PasswordsMenuBarExtra.app/Contents/MacOS/PasswordsMenuBarExtra`

```diff

 		<string>com.firstversionist.polypane</string>
 		<string>com.tab-browser.Tabbit</string>
 		<string>com.tabbit-ai.Tabbit</string>
+		<string>me.bnfy.bowser</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>

```
### PhotosFileProvider

> `/System/Applications/Photos.app/Contents/PlugIns/PhotosFileProvider.appex/Contents/MacOS/PhotosFileProvider`

```diff

 	<true/>
 	<key>com.apple.private.photos.cpanalytics.cache.read</key>
 	<true/>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.photos.service.mediaconversion</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### Siri AI

> `/System/Applications/Siri AI.app/Contents/MacOS/Siri AI`

```diff

 	<true/>
 	<key>com.apple.intelligenceflow.contextTool</key>
 	<true/>
+	<key>com.apple.intelligenceflow.imageretrieval</key>
+	<true/>
 	<key>com.apple.intelligenceflow.internal</key>
 	<true/>
 	<key>com.apple.intelligenceflow.orchestrator</key>

 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>path</string>
+		<string>bundleID</string>
 		<key>value</key>
-		<string>/Applications/Spotlight.app</string>
+		<string>com.apple.SiriApp</string>
 	</dict>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.CampoApp</string>

 		<string>com.apple.generativeexperiences.agentSessionStore</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
 		<string>com.apple.intelligenceflow.orchestrator</string>
+		<string>com.apple.intelligenceflow.imageretrieval</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.StatusKit.subscribe</string>
 		<string>com.apple.biome.access.system</string>

```

### 🆕 SettingsImportExtension

> `/System/Applications/System Settings.app/Contents/PlugIns/SettingsImportExtension.appex/Contents/MacOS/SettingsImportExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.Settings.extension.host</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.systempreferences.SettingsImportExtension</string>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.usage_oracle</key>
	<true/>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.linkd.observationStatusRegistry</key>
	<true/>
	<key>com.apple.runningboard.assertions.siri</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.linkd.mediator</string>
	</array>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.locationd.synchronous</string>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.mediator</string>
		<string>com.apple.linkd.transcript</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.systemsettings.extensions</string>
	</array>
</dict>
</plist>

```
### TV

> `/System/Applications/TV.app/Contents/MacOS/TV`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents.build-lockup-from-mapi-response</key>
 	<true/>
-	<key>com.apple.private.appstored </key>
+	<key>com.apple.private.appstorecomponents.small-offer-button</key>
+	<true/>
+	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Install</string>
 		<string>Queue</string>

 		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.fpsd</string>
 		<string>com.apple.TapToRadarKit.service</string>
+		<string>com.apple.appstored.xpc</string>
 	</array>
 	<key>com.apple.watchlist.private</key>
 	<true/>

```
### Activity Monitor

> `/System/Applications/Utilities/Activity Monitor.app/Contents/MacOS/Activity Monitor`

```diff

 	<true/>
 	<key>com.apple.private.controlcenter.controlcentermodule</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmapbundleidtouuid</key>
+	<true/>
 	<key>com.apple.private.gpuwrangler</key>
 	<true/>
+	<key>com.apple.private.launchservices.allowedtoforciblyremoveapplicationfromrunninglist</key>
+	<true/>
 	<key>com.apple.private.launchservices.allowedtoget.LSActivePageUserVisibleOriginsKey</key>
 	<true/>
 	<key>com.apple.private.launchservices.allowedtoget.LSPluginBundleIdentifierKey</key>
 	<true/>
+	<key>com.apple.private.network.statistics</key>
+	<true/>
 	<key>com.apple.private.systemstats.analysis-client</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>

```

### 🆕 AirPort Utility

> `/System/Applications/Utilities/AirPort Utility.app/Contents/MacOS/AirPort Utility`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.iaaccounts</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.wifi.associate</key>
	<true/>
	<key>com.apple.wifi.priority.id</key>
	<string>airport_utility</string>
	<key>com.apple.wifi.priority.internal</key>
	<true/>
	<key>com.apple.wifi.scan</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.hap.pairing</string>
	</array>
</dict>
</plist>

```
### Magnifier

> `/System/Applications/Utilities/Magnifier.app/Contents/MacOS/Magnifier`

```diff

 	<true/>
 	<key>com.apple.appleneuralengine.private.allow</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
 	<key>com.apple.modelcatalog.full-access</key>

 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>

 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.touchbarserver.mig</string>
 		<string>com.apple.translation.text</string>
 		<string>com.apple.translationd</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
+		<string>com.apple.akd</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### VoiceOver Utility

> `/System/Applications/Utilities/VoiceOver Utility.app/Contents/MacOS/VoiceOver Utility`

```diff

 		<key>com.apple.accessibility.VoiceOverPunctuation</key>
 		<string>com.apple.Accessibility</string>
 	</dict>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.translationd</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
+		<string>com.apple.akd</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### iPhone Mirroring

> `/System/Applications/iPhone Mirroring.app/Contents/MacOS/iPhone Mirroring`

```diff

 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceScreenCapture</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.automation.apple-events</key>

```

### 🆕 com.apple.HeadphoneSettingsUI

> `/System/Library/Accessibility/BundlesBase/com.apple.HeadphoneSettingsUI.axbundle/Versions/A/com.apple.HeadphoneSettingsUI`

- No entitlements *(yet)*
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/Contents/MacOS/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.accessibility.physicalinteraction.client</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	<true/>
 	<key>com.apple.audio.allows.mix.to.uplink</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.backboard.client</key>
 	<true/>
 	<key>com.apple.backboardd.excludeZoomContextsFromHitTesting</key>

 	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

 	<true/>
 	<key>com.apple.private.accessibility.visuals</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
 	<key>com.apple.private.application-service-browse</key>

 		<key>value</key>
 		<string>/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer</string>
 	</dict>
+	<key>com.apple.private.automatic-assessment-configuration.restrictor</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.feedback.drafting</key>

 	<array>
 		<string>group.com.apple.VoiceOver</string>
 	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>

 		<string>com.apple.analyticsd</string>
 		<string>com.apple.siri.activation</string>
 		<string>com.apple.siri.activation.service</string>
+		<string>com.apple.siri.assessment-mode-restriction</string>
 		<string>com.apple.commandandcontrol</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.identityservicesd.idquery.embedded.auth</string>

 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### AuthorizationPromptService

> `/System/Library/CoreServices/AuthorizationPromptService.app/Contents/MacOS/AuthorizationPromptService`

```diff

 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.locationd.desktop.synchronous</string>
 		<string>com.apple.mdmclient.daemon.unrestricted</string>
+		<string>com.apple.nehelper</string>
 	</array>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>

```
### ControlStrip

> `/System/Library/CoreServices/ControlStrip.app/Contents/MacOS/ControlStrip`

```diff

 	<true/>
 	<key>com.apple.private.screencapture.allow</key>
 	<true/>
+	<key>com.apple.private.system-banner-client</key>
+	<true/>
 	<key>com.apple.private.touchbar.user-device</key>
 	<true/>
 </dict>

```
### Erase Assistant

> `/System/Library/CoreServices/Erase Assistant.app/Contents/MacOS/Erase Assistant`

```diff

 	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.RepairDeviceLookup.access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.keystore.filevault</key>

 	<true/>
 	<key>com.apple.private.securityd.stash</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.storagekitd.destructive</key>
 	<true/>
 	<key>com.apple.private.storagekitd.info</key>

```
### Family

> `/System/Library/CoreServices/Family.app/Contents/MacOS/Family`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>0000000000.com.apple.Family</string>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.biome.compute.publisher.service</key>
 	<true/>
 	<key>com.apple.developer.associated-domains</key>

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.iaaccounts</key>
+	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>

 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.contactsd.persistence</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.aa.identity.xpc</string>
+		<string>com.apple.ak.anisette.xpc</string>
+		<string>com.apple.ak.auth.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

```
### Finder

> `/System/Library/CoreServices/Finder.app/Contents/MacOS/Finder`

```diff

 	<string>com.apple.finder</string>
 	<key>com.apple.dock.add-item</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.filederivatives.derive</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-read</key>

 		<string>com.apple.spotlight.CSExattrCryptoService</string>
 		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### MediaRemoteUI

> `/System/Library/CoreServices/MediaRemoteUI.app/Contents/MacOS/MediaRemoteUI`

```diff

 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
+	<key>com.apple.mediaremote.system-volume-control</key>
+	<true/>
 	<key>com.apple.mediaremote.ui-control</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### MediaRemoteUIService

> `/System/Library/CoreServices/MediaRemoteUIService.app/Contents/MacOS/MediaRemoteUIService`

```diff

 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
+	<key>com.apple.mediaremote.system-volume-control</key>
+	<true/>
 	<key>com.apple.mediaremote.ui-control</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### MenuBarAgent

> `/System/Library/CoreServices/MenuBarAgent.app/Contents/MacOS/MenuBarAgent`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.controlcenter</string>
+		<string>com.apple.MenuBar</string>
 	</array>
 	<key>com.apple.private.sessionkit.alertPresenter</key>
 	<true/>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.controlcenter</string>
+		<string>com.apple.MenuBar</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### Pro Display Calibrator

> `/System/Library/CoreServices/Pro Display Calibrator.app/Contents/MacOS/Pro Display Calibrator`

```diff

 	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/usr/local/bin/IOMFBDebug</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.systemprofiler</string>

```
### AppleVNCServer

> `/System/Library/CoreServices/RemoteManagement/AppleVNCServer.bundle/Contents/MacOS/AppleVNCServer`

```diff

 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>
 		<string>(allow file-issue-extension (require-all (extension-class "com.apple.app-sandbox.read")))</string>
+		<string>(allow file-write* (subpath "/Users") (subpath "/Volumes"))</string>
 		<string>(allow file-read-metadata (subpath "/private/var/db/ConfigurationProfiles"))</string>
 		<string>(allow file-read-metadata (subpath "/private/var/folders"))</string>
 		<string>(allow hid-control)</string>

```
### SSFileCopyReceiver

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/Support/SSFileCopyReceiver.bundle/Contents/MacOS/SSFileCopyReceiver`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
+		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
+	</array>
+</dict>
+</plist>
+
 <!-- Launch Constraints (Parent) -->
 {
   "appl": 1,

```
### ScreenTimeWidgetExtension

> `/System/Library/CoreServices/Screen Time.app/Contents/PlugIns/ScreenTimeWidgetExtension.appex/Contents/MacOS/ScreenTimeWidgetExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.screentime-communication</key>

 	<array>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.ScreenTimeAgent.persistence</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.accountsd.accountmanager</string>

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ScreenTimeAgent.settings</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 	</array>
 	<key>fairplay-client</key>

```
### ScreenTimeWidgetIntentsExtension

> `/System/Library/CoreServices/Screen Time.app/Contents/PlugIns/ScreenTimeWidgetIntentsExtension.appex/Contents/MacOS/ScreenTimeWidgetIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.screentime-communication</key>

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ScreenTimeAgent.settings</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 </dict>
 </plist>

```
### mbsystemadministration

> `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/mbsystemadministration`

```diff

 	<true/>
 	<key>com.apple.private.securityd.stash</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.storagekitd.destructive</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### SetupAssistantSpringboard

> `/System/Library/CoreServices/Setup Assistant.app/Contents/SharedSupport/SetupAssistantSpringboard`

```diff

 <dict>
 	<key>com.apple.private.mbsystemadministration</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 </dict>
 </plist>
 

```
### SiriAppAccessMigrator

> `/System/Library/CoreServices/SiriAppAccessMigrator`

```diff

 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
 		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 </dict>
 </plist>

```
### SystemUIServer

> `/System/Library/CoreServices/SystemUIServer.app/Contents/MacOS/SystemUIServer`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.appkit-status-item-direct-events</key>
+	<true/>
 	<key>com.apple.private.menubar.allow</key>
 	<true/>
 	<key>com.apple.private.screencapturekit.noprompt</key>

 	</array>
 	<key>com.apple.studentd-access</key>
 	<true/>
+	<key>com.apple.visualintelligence.private.visual-action-prediction</key>
+	<true/>
 	<key>com.apple.wifi.bypass-location-services</key>
 	<true/>
 </dict>

```
### VoiceOver

> `/System/Library/CoreServices/VoiceOver.app/Contents/MacOS/VoiceOver`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.readonly</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>

 		<string>com.apple.sociallayerd</string>
 		<string>com.apple.windowmanager.external</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
+		<string>com.apple.akd</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### WidgetRenderer_Activities

> `/System/Library/CoreServices/WidgetRenderer_Activities.app/Contents/MacOS/WidgetRenderer_Activities`

```diff

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.duetexpertd</string>
 		<string>com.apple.frontboardservices.device_emulation</string>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
+	<key>com.apple.private.securityd.keychain-master-key-extraction</key>
+	<true/>
 	<key>com.apple.private.securityd.stash</key>
 	<true/>
 	<key>com.apple.private.sessionagent.sessionowner</key>

```
### screencaptureui

> `/System/Library/CoreServices/screencaptureui.app/Contents/MacOS/screencaptureui`

```diff

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.windowmanager</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.screencapture</string>

```
### AccessibilitySettingsExtension

> `/System/Library/ExtensionKit/Extensions/AccessibilitySettingsExtension.appex/Contents/MacOS/AccessibilitySettingsExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.avfoundation.allow-system-wide-context</key>
+	<true/>
+	<key>com.apple.avfoundation.allows-access-to-device-list</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.bluetooth.xpc</key>

```
### Appearance

> `/System/Library/ExtensionKit/Extensions/Appearance.appex/Contents/MacOS/Appearance`

```diff

 <dict>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.private.SkyLight.screencapturedirect</key>
 	<true/>
 	<key>com.apple.private.launchservices.changedefaulthandlers</key>

 	<array>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.ak.auth.xpc</string>
 	</array>
 </dict>
 </plist>

```
### AppleAccountIntents_macOS

> `/System/Library/ExtensionKit/Extensions/AppleAccountIntents_macOS.appex/Contents/MacOS/AppleAccountIntents_macOS`

```diff

 		<string>/System/Library/PrivateFrameworks/AppleAccountUI.framework</string>
 	</array>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### AppleIDSettings

> `/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.applicationaccess</string>
+		<string>com.apple.assistant.backedup</string>
 	</array>
 	<key>com.apple.security.files.user-selected.read-write</key>
 	<true/>

 		<string>com.apple.MobileSMS</string>
 		<string>familycircled</string>
 		<string>com.apple.cloud.quota</string>
+		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.GenerativeModels.AgentSessionKit</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/Contents/MacOS/AssetMetricsExtension`

```diff

 	<array>
 		<string>group.com.apple.assistant.shared</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Application Support/com.apple.appleintelligencereporting.processing/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.feedbacklogger/</string>

```
### ControlCenterSettingsIntents

> `/System/Library/ExtensionKit/Extensions/ControlCenterSettingsIntents.appex/Contents/MacOS/ControlCenterSettingsIntents`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.admin.writeconfig.usersme</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.controlcenter</string>

```
### FamilyIntents

> `/System/Library/ExtensionKit/Extensions/FamilyIntents.appex/Contents/MacOS/FamilyIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/Contents/MacOS/FedAutoEvalPlugin`

```diff

 		<string>GenerativeExperiences.WritingToolsFeatures.Metadata</string>
 		<string>Siri.SELFProcessedEvent</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
+		<string>PrivateMLClient.SafetyMetrics</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>
 		</dict>
+		<key>SiriSafety</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>PrivateMLClient.SafetyMetrics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/Contents/MacOS/FedStatsPluginDynamic`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>MAD-TextUnderstanding-ProcessingResults</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>MediaAnalysis.TextUnderstanding.ProcessingResults</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>MAS</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>PCC-Safety-Metrics</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>PrivateMLClient.SafetyMetrics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Payment-Ring</key>
 		<dict>
 			<key>Streams</key>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/Contents/MacOS/FedStatsPluginStatic`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>MAD-TextUnderstanding-ProcessingResults</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>MediaAnalysis.TextUnderstanding.ProcessingResults</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>MAS</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>PCC-Safety-Metrics</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>PrivateMLClient.SafetyMetrics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Payment-Ring</key>
 		<dict>
 			<key>Streams</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Applications/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>

```
### GameCenterMacOSSettingsExtension

> `/System/Library/ExtensionKit/Extensions/GameCenterMacOSSettingsExtension.appex/Contents/MacOS/GameCenterMacOSSettingsExtension`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
-	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.Settings</string>
 	<key>com.apple.private.contactsui</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```

### 🆕 GameCenterSettingsSearchExtension

> `/System/Library/ExtensionKit/Extensions/GameCenterSettingsSearchExtension.appex/Contents/MacOS/GameCenterSettingsSearchExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Settings</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### KeyboardSettings

> `/System/Library/ExtensionKit/Extensions/KeyboardSettings.appex/Contents/MacOS/KeyboardSettings`

```diff

 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.assistant.settings</string>
+		<string>com.apple.visualintelligence.visual-action-prediction</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

 		<string>com.apple.inputmethod.VietnameseIM</string>
 		<string>com.apple.inputsources</string>
 	</array>
+	<key>com.apple.visualintelligence.private.visual-action-prediction</key>
+	<true/>
 </dict>
 </plist>
 

```
### MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/Contents/MacOS/MapsIntents`

```diff

 		<string>com.apple.Maps.MapsSync.store</string>
 		<string>com.apple.Maps.MapsSync.service</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.Maps.MapsSync.store</string>
+		<string>com.apple.Maps.MapsSync.service</string>
+	</array>
 </dict>
 </plist>
 

```
### MediaRemoteAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/MediaRemoteAppIntentsExtension.appex/Contents/MacOS/MediaRemoteAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
+	<key>com.apple.mediaremote.system-volume-control</key>
+	<true/>
 	<key>com.apple.mediaremote.ui-server-connection</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### MouseIntentsExtension

> `/System/Library/ExtensionKit/Extensions/MouseIntentsExtension.appex/Contents/MacOS/MouseIntentsExtension`

```diff

 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
 	<string>com.apple.systempreferences</string>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### PrivateMLClientInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/Contents/MacOS/PrivateMLClientInferenceProviderService`

```diff

 		<string>TokenGeneration.Inference.Requests</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeExperiences.TransparencyLog</string>
+		<string>PrivateMLClient.RecitationMetrics</string>
+		<string>PrivateMLClient.SafetyMetrics</string>
 	</array>
 	<key>com.apple.private.cloudtelemetry</key>
 	<true/>

```
### ProfilesSettingsIntents

> `/System/Library/ExtensionKit/Extensions/ProfilesSettingsIntents.appex/Contents/MacOS/ProfilesSettingsIntents`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 </dict>

```
### ScreenTimeSettingsResponseExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeSettingsResponseExtension.appex/Contents/MacOS/ScreenTimeSettingsResponseExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.ScreenTimeSettingsResponseExtension</string>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.screen-time-settings</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
+		<string>/Library/com.apple.AppleMediaServices/</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.AppleMediaServices</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.adid</string>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.iconservices</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
+		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.xpc.amsengagementd</string>
+	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>appleaccount</string>
+		<string>com.apple.certificates</string>
+		<string>com.apple.identities</string>
+		<string>com.apple.preferences</string>
 	</array>
 </dict>
 </plist>

```
### SecurityImprovementsExtension

> `/System/Library/ExtensionKit/Extensions/SecurityImprovementsExtension.appex/Contents/MacOS/SecurityImprovementsExtension`

```diff

 	<true/>
 	<key>com.apple.private.securityd.stash</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.softwareupdate.preferences</key>
 	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>

```

### 🆕 SiriSetupSettingsIntents

> `/System/Library/ExtensionKit/Extensions/SiriSetupSettingsIntents.appex/Contents/MacOS/SiriSetupSettingsIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Settings</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>com.apple.voicetrigger</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.siri</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.settings</string>
	</array>
</dict>
</plist>

```
### SoftwareUpdateSettingsExtension

> `/System/Library/ExtensionKit/Extensions/SoftwareUpdateSettingsExtension.appex/Contents/MacOS/SoftwareUpdateSettingsExtension`

```diff

 	<true/>
 	<key>com.apple.private.seeding.client</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.softwareupdate.preferences</key>
 	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>

```
### StartupDisk

> `/System/Library/ExtensionKit/Extensions/StartupDisk.appex/Contents/MacOS/StartupDisk`

```diff

 	<true/>
 	<key>com.apple.private.security.bootpolicy</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.storagekitd.destructive</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### TrackpadIntentsExtension

> `/System/Library/ExtensionKit/Extensions/TrackpadIntentsExtension.appex/Contents/MacOS/TrackpadIntentsExtension`

```diff

 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
 	<string>com.apple.systempreferences</string>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### UnilogAnalytics

> `/System/Library/ExtensionKit/Extensions/UnilogAnalytics.appex/Contents/MacOS/UnilogAnalytics`

```diff

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Unilog.SafariSearch.Aggregation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Unilog.SafariSearch.LongTermAggregationId</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Unilog.SafariSearch.Stage</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Unilog.Siri.Processed</key>
 				<dict>
 					<key>mode</key>

```

### 🆕 VpnSettingsIntents

> `/System/Library/ExtensionKit/Extensions/VpnSettingsIntents.appex/Contents/MacOS/VpnSettingsIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Settings</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### WallpaperSettingsIntents

> `/System/Library/ExtensionKit/Extensions/WallpaperSettingsIntents.appex/Contents/MacOS/WallpaperSettingsIntents`

```diff

 	<key>com.apple.developer.extension-host.screensaver</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.wallpaper</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.get-dstreams</key>
+	<true/>
+	<key>com.apple.private.apfs.get-file-exts</key>
+	<true/>
 	<key>com.apple.private.apfs.lock-container-load</key>
 	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>

```
### fsck_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.get-dstreams</key>
+	<true/>
+	<key>com.apple.private.apfs.get-file-exts</key>
+	<true/>
 	<key>com.apple.private.apfs.lock-container-load</key>
 	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>

```
### sm_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/sm_stats`

```diff

 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>
 	<true/>
+	<key>com.apple.private.apfs.get-dstreams</key>
+	<true/>
+	<key>com.apple.private.apfs.get-file-exts</key>
+	<true/>
 	<key>com.apple.private.apfs.lock-container-load</key>
 	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Support/accountsd`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.accountsd</string>
 	<key>com.apple.private.keychain.allow-delete-internal-on-sign-out</key>
 	<true/>
 	<key>com.apple.private.ndoagent</key>

```
### DocumentPopoverViewService

> `/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/DocumentPopoverViewService.xpc/Contents/MacOS/DocumentPopoverViewService`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

 	</array>
 	<key>com.apple.private.viewbridge.window.child.transparent</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+	</array>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 </dict>

```
### com.apple.appkit.xpc.openAndSavePanelService

> `/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/com.apple.appkit.xpc.openAndSavePanelService.xpc/Contents/MacOS/com.apple.appkit.xpc.openAndSavePanelService`

```diff

 	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.fileprovider.extension-host</key>
 	<true/>
 	<key>com.apple.imdpersistence.IMDPersistenceAgent-Syndication</key>

 		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.spotlight.entitledattributes</key>
 	<true/>

```
### DocumentPopoverViewService

> `/System/Library/Frameworks/AppKit.framework/Versions/Current/XPCServices/DocumentPopoverViewService.xpc/Contents/MacOS/DocumentPopoverViewService`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

 	</array>
 	<key>com.apple.private.viewbridge.window.child.transparent</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+	</array>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 </dict>

```
### com.apple.appkit.xpc.openAndSavePanelService

> `/System/Library/Frameworks/AppKit.framework/Versions/Current/XPCServices/com.apple.appkit.xpc.openAndSavePanelService.xpc/Contents/MacOS/com.apple.appkit.xpc.openAndSavePanelService`

```diff

 	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.fileprovider.extension-host</key>
 	<true/>
 	<key>com.apple.imdpersistence.IMDPersistenceAgent-Syndication</key>

 		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.spotlight.entitledattributes</key>
 	<true/>

```
### com.apple.automator.runner

> `/System/Library/Frameworks/Automator.framework/Versions/A/XPCServices/com.apple.automator.runner.xpc/Contents/MacOS/com.apple.automator.runner`

```diff

 		<string>com.apple.automator</string>
 		<string>com.apple.ScriptEditor2</string>
 	</array>
+	<key>com.apple.private.CFPasteboard.always-include-storage-class</key>
+	<true/>
 	<key>com.apple.private.cs.automator-plugins</key>
 	<true/>
 	<key>com.apple.private.quarantine.control-add</key>

```
### com.apple.automator.runner

> `/System/Library/Frameworks/Automator.framework/Versions/Current/XPCServices/com.apple.automator.runner.xpc/Contents/MacOS/com.apple.automator.runner`

```diff

 		<string>com.apple.automator</string>
 		<string>com.apple.ScriptEditor2</string>
 	</array>
+	<key>com.apple.private.CFPasteboard.always-include-storage-class</key>
+	<true/>
 	<key>com.apple.private.cs.automator-plugins</key>
 	<true/>
 	<key>com.apple.private.quarantine.control-add</key>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/corespotlightd`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tcc.manager.access.read</key>
+	<key>com.apple.private.tcc.manager.read.access</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/Current/Support/corespotlightd`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tcc.manager.access.read</key>
+	<key>com.apple.private.tcc.manager.read.access</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/Metadata.framework/Versions/A/Support/corespotlightd`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tcc.manager.access.read</key>
+	<key>com.apple.private.tcc.manager.read.access</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/Metadata.framework/Versions/Current/Support/corespotlightd`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tcc.manager.access.read</key>
+	<key>com.apple.private.tcc.manager.read.access</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowcarplayapps</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

```
### ctkahp

> `/System/Library/Frameworks/CryptoTokenKit.framework/ctkahp.bundle/Contents/MacOS/ctkahp`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.OpenDirectory</key>
 	<true/>
+	<key>com.apple.private.securityd.keychain-master-key-extraction</key>
+	<true/>
 	<key>com.apple.rootless.storage.ExtensibleSSO</key>
 	<true/>
 	<key>com.apple.rootless.volume.Preboot</key>

```
### ctkbind

> `/System/Library/Frameworks/CryptoTokenKit.framework/ctkbind.app/Contents/MacOS/ctkbind`

```diff

 	<true/>
 	<key>com.apple.keystore.device.smart-card</key>
 	<true/>
+	<key>com.apple.private.securityd.keychain-master-key-extraction</key>
+	<true/>
 	<key>com.apple.security.smartcard</key>
 	<true/>
 </dict>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.secure-apsclientv2</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 	<array>
 		<string>com.apple.CoreODI</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Caches/com.apple.businessservicesd/</string>

```
### ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/Versions/A/ManagedSettingsAgent`

```diff

 	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
 	<array>
 		<string>com.apple.WebContentRestrictions</string>
+		<string>com.apple.Accessibility</string>
 	</array>
 	<key>com.apple.private.device-configuration.provider.allowed-provider-ids</key>
 	<array>

```
### RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/Versions/A/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>

```
### RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/Versions/Current/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>

```
### ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/Versions/A/PlugIns/ScreenTimeWebExtension.appex/Contents/MacOS/ScreenTimeWebExtension`

```diff

 	</array>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screen-time-settings</key>
 	<true/>
+	<key>com.apple.rootless.storage.remotemanagementd</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source.user</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 </dict>

```
### ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/Versions/Current/PlugIns/ScreenTimeWebExtension.appex/Contents/MacOS/ScreenTimeWebExtension`

```diff

 	</array>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screen-time-settings</key>
 	<true/>
+	<key>com.apple.rootless.storage.remotemanagementd</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source.user</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 </dict>

```
### SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

```diff

 	<true/>
 	<key>com.apple.keystore.console</key>
 	<true/>
-	<key>com.apple.private.Authorization.SPI</key>
-	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>

```
### authorizationhost

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/MacOS/authorizationhost`

```diff

 	<true/>
 	<key>com.apple.keystore.filevault</key>
 	<true/>
-	<key>com.apple.private.Authorization.SPI</key>
-	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.ExtractCredential</key>

```
### XPCAcmeService

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/XPCAcmeService.xpc/Contents/MacOS/XPCAcmeService`

```diff

 	<string>com.apple.security.XPCAcmeService</string>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/tmp/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/tmp/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/mobile/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/mobile/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/root/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/root/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/root/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/root/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>platform-application</key>

```
### authd

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/authd.xpc/Contents/MacOS/authd`

```diff

 	<true/>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
-	<key>com.apple.private.security.storage.StagedPlugins</key>
-	<true/>
 	<key>com.apple.private.security.storage.authdb</key>
 	<true/>
 	<key>com.apple.rootless.storage.ExtensibleSSO</key>

```
### XPCAcmeService

> `/System/Library/Frameworks/Security.framework/Versions/Current/XPCServices/XPCAcmeService.xpc/Contents/MacOS/XPCAcmeService`

```diff

 	<string>com.apple.security.XPCAcmeService</string>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/tmp/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/tmp/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/mobile/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/mobile/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/mobile/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/root/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/root/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/private/var/root/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/private/var/root/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/com.apple.security.XPCAcmeService</string>
-		<string>/Library/Caches/com.apple.security.XPCAcmeService/</string>
-		<string>/Library/HTTPStorages/com.apple.security.XPCAcmeService</string>
-		<string>/Library/HTTPStorages/com.apple.security.XPCAcmeService/</string>
-	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>platform-application</key>

```
### authd

> `/System/Library/Frameworks/Security.framework/Versions/Current/XPCServices/authd.xpc/Contents/MacOS/authd`

```diff

 	<true/>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
-	<key>com.apple.private.security.storage.StagedPlugins</key>
-	<true/>
 	<key>com.apple.private.security.storage.authdb</key>
 	<true/>
 	<key>com.apple.rootless.storage.ExtensibleSSO</key>

```
### translationd

> `/System/Library/Frameworks/Translation.framework/translationd`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Translation.Assets</string>
+		<string>com.apple.MobileAsset.UAF.Translation.MMAssets</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 		<string>com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition</string>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Translation_MMAssets/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

```
### com.apple.Virtualization.VirtualMachine

> `/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine`

```diff

 	<true/>
 	<key>com.apple.private.biometrickit.allow-match</key>
 	<true/>
+	<key>com.apple.private.debug-usb.access</key>
+	<true/>
 	<key>com.apple.private.fpsd.client</key>
 	<true/>
 	<key>com.apple.private.ggdsw.GPUProcessProtectedContent</key>

```
### com.apple.Virtualization.VirtualMachine

> `/System/Library/Frameworks/Virtualization.framework/Versions/Current/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine`

```diff

 	<true/>
 	<key>com.apple.private.biometrickit.allow-match</key>
 	<true/>
+	<key>com.apple.private.debug-usb.access</key>
+	<true/>
 	<key>com.apple.private.fpsd.client</key>
 	<true/>
 	<key>com.apple.private.ggdsw.GPUProcessProtectedContent</key>

```

### 🆕 SteamControllerHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/SteamControllerHIDServicePlugin.plugin/Contents/MacOS/SteamControllerHIDServicePlugin`

- No entitlements *(yet)*
### com.apple.iCloudHelper

> `/System/Library/PrivateFrameworks/AOSKit.framework/Versions/A/XPCServices/com.apple.iCloudHelper.xpc/Contents/MacOS/com.apple.iCloudHelper`

```diff

 	<array>
 		<string>com.apple.ProtectedCloudStorage</string>
 		<string>com.apple.PublicCloudStorage</string>
+		<string>iCloud</string>
 	</array>
 </dict>
 </plist>

```
### com.apple.iCloudHelper

> `/System/Library/PrivateFrameworks/AOSKit.framework/Versions/Current/XPCServices/com.apple.iCloudHelper.xpc/Contents/MacOS/com.apple.iCloudHelper`

```diff

 	<array>
 		<string>com.apple.ProtectedCloudStorage</string>
 		<string>com.apple.PublicCloudStorage</string>
+		<string>iCloud</string>
 	</array>
 </dict>
 </plist>

```
### axassetsd

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.analyticsd</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.voicebanking.services</string>
 		<string>com.apple.voicebanking.store</string>

```
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/Contents/MacOS/BundledIntentHandler`

```diff

 	<array>
 		<string>com.apple.radios.plist</string>
 	</array>
+	<key>com.apple.accessibility.physicalinteraction.client</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.ActionKit.BundledIntentHandler</string>
 	<key>com.apple.bluetooth.system</key>

```
### agentstored

> `/System/Library/PrivateFrameworks/AgentSessionKitRuntime.framework/Versions/A/agentstored`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.appleintelligencereporting.processing</key>
 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GenerativeFunctions.agentstored</string>
 	<key>com.apple.assertiond.system-shell</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
 	<key>com.apple.developer.icloud-container-environment</key>

 	<true/>
 	<key>com.apple.linkd.registry</key>
 	<true/>
+	<key>com.apple.mobileactivationd.bridge</key>
+	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
-		<key>com.apple.agentsessionstore</key>
-		<string>com.apple.GenerativeModels.AgentSessionKit</string>
+		<key>com.apple.agentsessionstore.secure</key>
+		<string>com.apple.agentsessionstore.secure</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/ConfigurationProfiles/Settings/.deviceConfigurationBits</string>
+	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/AppleIntelligencePlatform/AgentSessionKit/</string>
 		<string>/Library/Shortcuts/</string>
+		<string>/Library/AgentSessionKitBackupStaging/</string>
 	</array>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.cfnetwork</string>
+		<string>apple</string>
+	</array>
 </dict>
 </plist>
 

```
### AppSSOAgent

> `/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSOAgent.app/Contents/MacOS/AppSSOAgent`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.AppSSOAgent</string>
+	<key>com.apple.authentication-services.allow-authentication-request-any-rpid</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.authorization.extract-password</key>

 	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.authentication-services.internal-authorization-requests</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.ctk.configuration-allowed-for-bundles</key>

 	<array>
 		<string>group.com.apple.KerberosExtension</string>
 	</array>
+	<key>com.apple.private.securityd.keychain-master-key-extraction</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### ASDAskPermissionExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/Contents/MacOS/ASDAskPermissionExtension`

```diff

 	<array>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstored.xpc.storequeue</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 </dict>
 </plist>

```
### appstoreagent

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstoreagent`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
+		<string>DaemonCallback</string>
 		<string>PrivilegedTask</string>
 	</array>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<string>systemgroup.com.apple.mobileactivationd</string>
 		<string>systemgroup.com.apple.pisco.suinfo</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>
 		<string>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 		<string>systemgroup.com.apple.mobileactivationd</string>
 		<string>systemgroup.com.apple.pisco.suinfo</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/Resources/amsaccountsd`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppleMediaServices</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>/Library/Caches/com.apple.amsaccountsd/</string>
 		<string>/Library/HTTPStorages/com.apple.amsaccountsd/</string>
 		<string>/Library/com.apple.AppleMediaServices/</string>
+		<string>/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.amsaccountsd/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/Current/Resources/amsaccountsd`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppleMediaServices</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>/Library/Caches/com.apple.amsaccountsd/</string>
 		<string>/Library/HTTPStorages/com.apple.amsaccountsd/</string>
 		<string>/Library/com.apple.AppleMediaServices/</string>
+		<string>/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.amsaccountsd/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistant_service`

```diff

 	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
+	<key>com.apple.telephonyutilities.callservicesd</key>
+	<array>
+		<string>access-call-providers</string>
+		<string>access-calls</string>
+		<string>modify-calls</string>
+		<string>access-call-capabilities</string>
+		<string>register-gft-service</string>
+	</array>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1320</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
+	<key>com.apple.private.corewifi.readonly</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.assistant.speech-request</key>
+	<true/>
 	<key>com.apple.private.domain-extension</key>
 	<true/>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>

 		<string>SIRI_DICTATION_ASSETS</string>
 		<string>SIRI_HEARABLES_VOX</string>
 		<string>SIRI_INFORMATION_CACHING</string>
+		<string>SIRI_INTELLIGENCE_FLOW_PLANNER</string>
 		<string>SIRI_MEMORY_SYNC_CONFIG</string>
 		<string>SIRI_MESSAGES_APP_SELECTION</string>
 		<string>SIRI_NETWORK_ENABLEMENT</string>

```
### AKAppSSOExtension_macOS

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension_macOS.appex/Contents/MacOS/AKAppSSOExtension_macOS`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.associated-domains</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

 	<array>
 		<string>com.apple.ak.authorizationservices.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.SharedWebCredentials</string>
 	</array>
 </dict>
 </plist>

```
### cksharingmanagementd

> `/System/Library/PrivateFrameworks/CKSharingManagementDaemon.framework/Support/cksharingmanagementd`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.alloy.cloudkit.sharing.management-idswake</key>
 	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>

```
### SetStoreUpdateService

> `/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/XPCServices/SetStoreUpdateService.xpc/Contents/MacOS/SetStoreUpdateService`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.SetStoreUpdateService</string>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### SetStoreUpdateService

> `/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/Current/XPCServices/SetStoreUpdateService.xpc/Contents/MacOS/SetStoreUpdateService`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.SetStoreUpdateService</string>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 KeychainMigrationService

> `/System/Library/PrivateFrameworks/ClassroomKit.framework/Versions/A/XPCServices/KeychainMigrationService.xpc/Contents/MacOS/KeychainMigrationService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.security.allow-migration</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>4WXS7A4F54.com.apple.macos.classroom</string>
	</array>
</dict>
</plist>

```
### cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/Support/cloudphotod`

```diff

 		<string>Photos</string>
 		<key>com.apple.photos.applibraries.prototyping</key>
 		<string>ManateeSharingTesting</string>
-		<key>com.apple.photos.asc.e2ee</key>
-		<string>com.apple.photos.asc.e2ee</string>
+		<key>com.apple.photos.asc.e2ee.secure</key>
+		<string>com.apple.photos.asc.e2ee.secure</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>

```

### 🆕 TrackpadCloudSettingsXPCService

> `/System/Library/PrivateFrameworks/CloudSettings.framework/Versions/A/XPCServices/TrackpadCloudSettingsXPCService.xpc/Contents/MacOS/TrackpadCloudSettingsXPCService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.cloudsettings.trackpad</string>
</dict>
</plist>

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.InFocus</string>
+		<string>Siri.ODDI.ODDAssistantLLMSiriDigests</string>
 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>

 				<string>App.InFocus</string>
 			</array>
 		</dict>
+		<key>SELFCommonEventTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Siri.ODDI.ODDAssistantLLMSiriDigests</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 		<string>cellular-plan</string>
 		<string>spi</string>
 	</array>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 	<true/>
 	<key>com.apple.rootless.storage.CoreAnalytics</key>
 	<true/>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>AppleSPUHIDDriverUserClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.analyticsagent</string>

```

### 🆕 default-binaryarchive.metallib

> `/System/Library/PrivateFrameworks/CoreRE.framework/Versions/A/Resources/default-binaryarchive.metallib`

- No entitlements *(yet)*

### 🆕 mxi-binaryarchive.metallib

> `/System/Library/PrivateFrameworks/CoreRE.framework/Versions/A/Resources/mxi-binaryarchive.metallib`

- No entitlements *(yet)*

### 🆕 default-binaryarchive.metallib

> `/System/Library/PrivateFrameworks/CoreRE.framework/Versions/Current/Resources/default-binaryarchive.metallib`

- No entitlements *(yet)*

### 🆕 mxi-binaryarchive.metallib

> `/System/Library/PrivateFrameworks/CoreRE.framework/Versions/Current/Resources/mxi-binaryarchive.metallib`

- No entitlements *(yet)*
### corespeechd_system

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system`

```diff

 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
-		<string>path</string>
+		<string>bundleID</string>
 		<key>value</key>
-		<string>/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd</string>
+		<string>com.apple.SiriApp</string>
 	</dict>
 	<key>com.apple.private.audio.dark-wake-audio</key>
 	<true/>

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/dev/exfiltration-adc-corespeechd</string>
+		<string>/dev/exfiltration-rts_nis_dbg</string>
 		<string>/tmp/SiriMessages/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### DeviceConfigurationAgent

> `/System/Library/PrivateFrameworks/DeviceConfiguration.framework/Versions/A/DeviceConfigurationAgent`

```diff

 	<string>com.apple.DeviceConfigurationAgent</string>
 	<key>com.apple.private.device-configuration.consumer.private</key>
 	<true/>
+	<key>com.apple.private.device-configuration.user.private</key>
+	<true/>
 	<key>com.apple.private.security.protected-system-container</key>
 	<true/>
 </dict>

```
### deviceconfigurationd

> `/System/Library/PrivateFrameworks/DeviceConfiguration.framework/Versions/A/deviceconfigurationd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.deviceconfigurationd</string>
+	<key>com.apple.private.container.access</key>
+	<dict>
+		<key>protectedSystem</key>
+		<dict>
+			<key>com.apple.DeviceConfigurationAgent</key>
+			<dict>
+				<key>data</key>
+				<dict>
+					<key>access</key>
+					<string>path-only</string>
+					<key>operations</key>
+					<array>
+						<string>delete</string>
+						<string>lookup</string>
+					</array>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.protected-system-container</key>
 	<true/>
 </dict>

```
### diskimages-helper

> `/System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/Resources/diskimages-helper`

```diff

 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
 	<integer>1</integer>
+	<key>com.apple.private.diskimages.helper</key>
+	<true/>
 	<key>com.apple.private.diskimages.kext.user-client-access</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### diskimages-helper

> `/System/Library/PrivateFrameworks/DiskImages.framework/Versions/Current/Resources/diskimages-helper`

```diff

 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
 	<integer>1</integer>
+	<key>com.apple.private.diskimages.helper</key>
+	<true/>
 	<key>com.apple.private.diskimages.kext.user-client-access</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```

### 🆕 GameTestIndicator

> `/System/Library/PrivateFrameworks/Ecosystem.framework/Support/GameTestIndicator`

- No entitlements *(yet)*
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/generativeexperiencesd`

```diff

 	<array>
 		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
+		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
 	</array>
 	<key>com.apple.shortcuts.stepwise-execution</key>
 	<true/>

```

### 🆕 IntelligenceFlowCustomerDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/IntelligenceFlowCustomerDiagnostics.appex/Contents/MacOS/IntelligenceFlowCustomerDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.intelligenceflow.IntelligenceFlowRuntime.IntelligenceFlowCustomerDiagnostics</string>
	<key>com.apple.intelligenceflow.context</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Sage.Transcript</string>
		<string>IntelligenceFlow.Transcript.Datastream</string>
		<string>IntelligenceEngine.Interaction.Donation</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>com.apple.intelligenceflow.IntelligenceFlowRuntime.IntelligenceFlowCustomerDiagnostics</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Sage.Transcript</string>
				<string>IntelligenceFlow.Transcript.Datastream</string>
				<string>IntelligenceEngine.Interaction.Donation</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.security.storage.SiriFeatureStore</key>
	<true/>
	<key>com.apple.private.siriappintentsd.orchestrator</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/folders/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.intelligenceflow.context</string>
		<string>com.apple.private.siriappintentsd.orchestrator</string>
	</array>
</dict>
</plist>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.intelligenceflow.contextTool</key>
 	<true/>
+	<key>com.apple.intelligenceflow.imageretrieval</key>
+	<true/>
 	<key>com.apple.intelligenceflow.orchestrator</key>
 	<true/>
 	<key>com.apple.intelligenceflow.orchestrator.features</key>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/Versions/A/XPCServices/Managed Background Assets Helper Service.xpc/Contents/MacOS/Managed Background Assets Helper Service`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.backgroundassets.managed.helper.fetching.service</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/Versions/Current/XPCServices/Managed Background Assets Helper Service.xpc/Contents/MacOS/Managed Background Assets Helper Service`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.backgroundassets.managed.helper.fetching.service</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/mediaanalysisd`

```diff

 		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
 		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>MediaAnalysis.TextUnderstanding.ProcessingResults</string>
 	</array>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.networkd_privileged</key>
+	<true/>
 	<key>com.apple.nowplaying.remote-media-host</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.musicd.client</key>
 	<true/>
+	<key>com.apple.private.necp.policies</key>
+	<true/>
+	<key>com.apple.private.nehelper.privileged</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.rtcreportingd</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.nehelper</string>
 		<string>com.apple.musicd</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.airplay.endpoint.xpc</string>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/modelcatalogd`

```diff

 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/searchtoold`

```diff

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.filebrowsingservices.path-resolver-client</key>
+	<true/>
 	<key>com.apple.private.generativesearch.client.search</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

 		<string>/Library/Shortcuts/</string>
 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 		<string>/Library/Application Support/com.apple.omniSearch.searchtoold/</string>
+		<string>/Library/Caches/PFSceneTaxonomyData</string>
+		<string>/Library/Caches/PFContentClassificationTaxonomyData</string>
+		<string>/Library/Caches/PFTimeZoneData</string>
+		<string>/Library/Caches/PFSceneGeographyData</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>/Library/Shortcuts/</string>
 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 		<string>/Library/Application Support/com.apple.omniSearch.searchtoold/</string>
+		<string>/Library/Caches/PFSceneTaxonomyData</string>
+		<string>/Library/Caches/PFContentClassificationTaxonomyData</string>
+		<string>/Library/Caches/PFTimeZoneData</string>
+		<string>/Library/Caches/PFSceneGeographyData</string>
 	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Versions/A/Support/photoanalysisd`

```diff

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.symptom_analytics</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 	<true/>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>
+	<key>com.apple.springboard.fetchDisplayConfigs</key>
+	<true/>
+	<key>com.apple.springboard.wallpaper.display-configuration</key>
+	<true/>
 	<key>com.apple.springboard.wallpaper.get</key>
 	<true/>
 	<key>com.apple.springboard.widget-metrics</key>

```
### com.apple.photos.PCCService

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/XPCServices/com.apple.photos.PCCService.xpc/Contents/MacOS/com.apple.photos.PCCService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.photos.PCCService</string>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>PrivateCloudCompute.RequestLog</string>
+	</array>
 	<key>com.apple.private.photos.restrictedresources.read</key>
 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

```
### com.apple.photos.PCCService

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/Current/XPCServices/com.apple.photos.PCCService.xpc/Contents/MacOS/com.apple.photos.PCCService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.photos.PCCService</string>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>PrivateCloudCompute.RequestLog</string>
+	</array>
 	<key>com.apple.private.photos.restrictedresources.read</key>
 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

```
### PlatformSSOUIAgent

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/Support/PlatformSSOUIAgent.app/Contents/MacOS/PlatformSSOUIAgent`

```diff

 	</array>
 	<key>com.apple.private.platformsso.agent</key>
 	<true/>
+	<key>com.apple.private.securityd.keychain-master-key-extraction</key>
+	<true/>
 	<key>com.apple.private.skylight.unconditional-activation</key>
 	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>

 	<true/>
 	<key>com.apple.security.smartcard</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.PlatformSSO</string>
+		<string>com.apple.PlatformSSO.auth</string>
+	</array>
 </dict>
 </plist>
 

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/Contents/MacOS/privatecloudcomputed`

```diff

 	<true/>
 	<key>com.apple.private.security.protected-system-container</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SBUserNotification</string>

```
### AccountSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/AccountSubscriber.xpc/Contents/MacOS/AccountSubscriber`

```diff

 	<string>com.apple.remotemanagement.AccountSubscriber</string>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.managedclient.remotemanagement</key>
+	<true/>
 	<key>com.apple.private.personas.propagate</key>
 	<true/>
 	<key>com.apple.private.remotemanagement.subscriber</key>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent`

```diff

 		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.dmd.policy</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/Versions/A/ScreenTimeSettingsAgent`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>AppStore</string>
+	</array>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.biome.read-only</key>

```
### ScreenTimeFollowUpExtension

> `/System/Library/PrivateFrameworks/ScreenTimeUI.framework/PlugIns/ScreenTimeFollowUpExtension.appex/Contents/MacOS/ScreenTimeFollowUpExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
+	<key>com.apple.private.screen-time.persistence</key>
+	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.DeviceActivity</string>
+	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.ScreenTime</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.DeviceActivity</string>
+	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ScreenTimeAgent.private</string>
+		<string>com.apple.ScreenTimeAgent.settings</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.UsageTrackingAgent.private</string>
 	</array>
 </dict>
 </plist>

```
### siriappintentsd

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/siriappintentsd`

```diff

 		<string>AppleIntelligence.Reporting.Invocation.Step</string>
 		<string>SessionResumptionEventBundle</string>
 		<string>SecurityValidationEvent</string>
+		<string>SecurityValidationProtoSecurityValidationEventPayload</string>
 		<string>TokenGeneration.Inference.Requests</string>
 	</array>
 	<key>com.apple.private.corespotlight.skgupdater</key>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/siriinferenced`

```diff

 		<string>com.apple.fpsd</string>
 		<string>com.apple.fairplayd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>

```
### SoftwareUpdateNotificationManager

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/Resources/SoftwareUpdateNotificationManager.app/Contents/MacOS/SoftwareUpdateNotificationManager`

```diff

 	<true/>
 	<key>com.apple.private.securityd.stash</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.softwareupdate.postlogoutinstall</key>
 	<true/>
 	<key>com.apple.private.softwareupdate.preferences</key>

```
### SoftwareUpdateNotificationManager

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/Current/Resources/SoftwareUpdateNotificationManager.app/Contents/MacOS/SoftwareUpdateNotificationManager`

```diff

 	<true/>
 	<key>com.apple.private.securityd.stash</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.softwareupdate.postlogoutinstall</key>
 	<true/>
 	<key>com.apple.private.softwareupdate.preferences</key>

```
### imageplaygroundd

> `/System/Library/PrivateFrameworks/SuggestedImage.framework/Support/imageplaygroundd`

```diff

 		<string>com.apple.ciphermld</string>
 		<string>com.apple.usernotifications.listener</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.applicationaccess</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>.GlobalPreferences</string>

```
### systemstatusd

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/Support/systemstatusd`

```diff

 	<true/>
 	<key>com.apple.rootless.critical</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.systemstatusd</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 </dict>
 </plist>
 

```
### PhoneIntentHandler

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/Contents/MacOS/PhoneIntentHandler`

```diff

 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.identityservicesd.desktop.auth</string>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.commcenter.xpc</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/Contents/MacOS/BackgroundShortcutRunner`

```diff

 <dict>
 	<key>com.apple.LaunchApp</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	<true/>
 	<key>com.apple.netauth.user.auth</key>
 	<true/>
+	<key>com.apple.private.CFPasteboard.always-include-storage-class</key>
+	<true/>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.SkyLight.displaycontrol</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.assistant.cdm</string>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.modelmanager</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.private.corewifi.internal-xpc</string>
 		<string>com.apple.remindd</string>

```
### bird

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/Support/bird`

```diff

 	</array>
 	<key>com.apple.private.cloudkit.usePublicAPSToken</key>
 	<true/>
+	<key>com.apple.private.container.access</key>
+	<dict>
+		<key>appData</key>
+		<dict>
+			<key>*</key>
+			<dict>
+				<key>systemData</key>
+				<dict>
+					<key>access</key>
+					<string>read-write</string>
+					<key>domains</key>
+					<array>
+						<string>com.apple.bird</string>
+					</array>
+					<key>operations</key>
+					<array>
+						<string>lookup</string>
+						<string>create</string>
+					</array>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

```
### deviceinterfaced

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Support/deviceinterfaced`

```diff

 	</array>
 	<key>com.apple.private.AppleRSMChannel.access</key>
 	<true/>
+	<key>com.apple.private.debug-usb.access</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleRSMChannelControllerClient</string>

```
### GPUIExtension

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Applications/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>

```

### 🆕 MacinTalkAUSP

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/MacinTalkAUSP.appex/Contents/MacOS/MacinTalkAUSP`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accessibility.systemvoiceprovider</key>
	<true/>
	<key>com.apple.coreaudio.allow-opus-codec</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.TTSAXResourceModelAssets</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_TTSAXResourceModelAssets/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
		<string>com.apple.accessibility.voices</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.voiceservices</string>
		<string>com.apple.SpeakSelection</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Caches/TTSResourceCache.plist</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
		<string>com.apple.accessibility.voices</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SpeakSelection</string>
		<string>com.apple.voiceservices</string>
	</array>
	<key>com.apple.security.ts.ipc-posix-shm</key>
	<array>
		<string>apple.shm.notification_center</string>
	</array>
</dict>
</plist>

```
### MauiAUSP

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/MauiAUSP.appex/Contents/MacOS/MauiAUSP`

```diff

 	<array>
 		<string>com.apple.SpeakSelection</string>
 	</array>
-	<key>com.apple.security.files.user-selected.read-only</key>
-	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/System/Library/AssetsV2/</string>

```
### RemotePlayerService

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>

```
### RemotePlayerService

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/Current/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>

```
### ScreenTimeWebExtension

> `/System/iOSSupport/System/Library/Frameworks/ScreenTime.framework/Versions/A/PlugIns/ScreenTimeWebExtension.appex/Contents/MacOS/ScreenTimeWebExtension`

```diff

 	</array>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screen-time-settings</key>
 	<true/>
+	<key>com.apple.rootless.storage.remotemanagementd</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source.user</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 </dict>

```
### ScreenTimeWebExtension

> `/System/iOSSupport/System/Library/Frameworks/ScreenTime.framework/Versions/Current/PlugIns/ScreenTimeWebExtension.appex/Contents/MacOS/ScreenTimeWebExtension`

```diff

 	</array>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screen-time-settings</key>
 	<true/>
+	<key>com.apple.rootless.storage.remotemanagementd</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source.user</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 </dict>

```
### powermetrics

> `/usr/bin/powermetrics`

```diff

 <dict>
 	<key>com.apple.private.applegraphicsdevicecontrol</key>
 	<true/>
+	<key>com.apple.private.pmgr.nrg.reporting</key>
+	<true/>
 	<key>com.apple.system-task-ports.inspect</key>
 	<true/>
 </dict>

```
### tccutil

> `/usr/bin/tccutil`

```diff

 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceSystemPolicyAllFiles</string>
+		<string>kTCCServiceAll</string>
 	</array>
 </dict>
 </plist>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	</dict>
 	<key>com.apple.aop.user-client.full-access</key>
 	<true/>
-	<key>com.apple.backboardd.lastUserEventTime</key>
-	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
 	<key>com.apple.batteryintelligenced.batteryanalysis-read</key>

 	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
 	<key>com.apple.private.bdc.tasking</key>
 	<true/>
 	<key>com.apple.private.clpc.reporting</key>

 		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.trial.status</string>
+		<string>com.apple.AttentionAwareness</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<string>com.apple.PerfPowerServicesExtended</string>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
-	<key>com.apple.backboardd.lastUserEventTime</key>
-	<true/>
 	<key>com.apple.backboardd.proximityStatusEvent</key>
 	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>

 	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
 	<key>com.apple.private.bdc.tasking</key>
 	<true/>
 	<key>com.apple.private.cloudkit.buddyAccess</key>

 		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.trial.status</string>
+		<string>com.apple.AttentionAwareness</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### aned

> `/usr/libexec/aned`

```diff

 	<true/>
 	<key>com.apple.private.ANEStorageMaintainer.allow</key>
 	<true/>
+	<key>com.apple.private.MobileContainerManager.allowed</key>
+	<true/>
+	<key>com.apple.private.MobileContainerManager.lookup</key>
+	<dict>
+		<key>app</key>
+		<true/>
+		<key>appData</key>
+		<true/>
+		<key>appGroup</key>
+		<true/>
+	</dict>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### appleh13camerad

> `/usr/libexec/appleh13camerad`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>VADResourceArbiterUserClient</string>
 		<string>ApplePhotonDetectorUserClient</string>
-		<string>IOUserClient</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### appleh16camerad

> `/usr/libexec/appleh16camerad`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>VADResourceArbiterUserClient</string>
 		<string>AppleH16PhotonDetectorUserClient</string>
-		<string>IOUserClient</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### asktod

> `/usr/libexec/asktod`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>ScreenTimeRequest</string>
-		<string>AskToBuy</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.device-configuration.provider.allowed-provider-ids</key>
+	<array>
+		<string>com.apple.AutomaticAssessmentConfiguration</string>
+	</array>
 	<key>com.apple.private.managedclient.configurationprofiles</key>
 	<true/>
 	<key>com.apple.private.managedclient.configurationprofiles.installsource</key>

```
### ciphermld

> `/usr/libexec/ciphermld`

```diff

 	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
-	<key>com.apple.private.applemediaservices</key>
-	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	<array>
 		<string>/Library/Caches/com.apple.ciphermld/</string>
 		<string>/Library/HTTPStorages/com.apple.ciphermld/</string>
-		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.parsecd</string>
-		<string>com.apple.itunesstored</string>
-		<string>com.apple.jett.switch-itms</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### corebrightnessd

> `/usr/libexec/corebrightnessd`

```diff

 	</array>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
+	<key>com.apple.private.hid.client.service-protected</key>
+	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>
 	<true/>
 	<key>com.apple.private.ppm.client</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>App.InFocus</string>
 		<string>App.Install</string>
 		<string>Device.Power.PluggedIn</string>
+		<string>Device.KeybagLocked</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

```
### enhancedloggingd

> `/usr/libexec/enhancedloggingd`

```diff

 	<true/>
 	<key>com.apple.appletv.pbs.bulletin-service-access</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.AppleServiceToolkit</string>
 		<string>com.apple.EnhancedLogging</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.AppleServiceToolkit</string>
 		<string>com.apple.EnhancedLogging</string>
 	</array>
 </dict>

```
### feedbackd

> `/usr/libexec/feedbackd`

```diff

 		<string>Feedback.TextToImageEvaluationData</string>
 		<string>Feedback.TextImageToImageEvaluationData</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>FeedbackDonationFetch</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Feedback.TextToTextEvaluationData</string>
+				<string>Feedback.TextToImageEvaluationData</string>
+				<string>Feedback.TextImageToImageEvaluationData</string>
+				<string>Feedback.EvaluationResponse</string>
+			</array>
+		</dict>
+		<key>FeedbackDuplicateCheck</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Feedback.TextToTextEvaluationData</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.InputAnalytics.SecureContainer</string>
+		<string>group.com.apple.mail</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### linkd

> `/usr/libexec/linkd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.linkd</string>
 	<key>com.apple.chronoservices</key>

```
### mdmclient

> `/usr/libexec/mdmclient`

```diff

 		<string>system.install.apple-software</string>
 		<string>system.install.apple-software.standard-user</string>
 	</array>
+	<key>com.apple.private.InstallCoordination.AddPersona</key>
+	<true/>
+	<key>com.apple.private.InstallCoordination.RemovePersona</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.modelmanager</key>
 	<true/>
-	<key>com.apple.runningboard.terminateprocess</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/assetsubscriptiond/</string>

```
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
+	<key>com.apple.locationd.use-wireless-client-info</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

```
### perfpowermetricd

> `/usr/libexec/perfpowermetricd`

```diff

 	<string>com.apple.PerfPowerServicesExtended</string>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
-	<key>com.apple.backboardd.lastUserEventTime</key>
-	<true/>
 	<key>com.apple.backboardd.proximityStatusEvent</key>
 	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>

 	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
 	<key>com.apple.private.bdc.tasking</key>
 	<true/>
 	<key>com.apple.private.cloudkit.buddyAccess</key>

 		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.trial.status</string>
+		<string>com.apple.AttentionAwareness</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### powerexperienced

> `/usr/libexec/powerexperienced`

```diff

 		<string>AppleCLPCUserClient</string>
 		<string>AppleSMCClient</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/Library/Trial/</string>
+	</array>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>364</string>

```
### powerlogHelperd

> `/usr/libexec/powerlogHelperd`

```diff

 	<string>com.apple.PerfPowerServicesExtended</string>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
-	<key>com.apple.backboardd.lastUserEventTime</key>
-	<true/>
 	<key>com.apple.backboardd.proximityStatusEvent</key>
 	<true/>
 	<key>com.apple.basebandd.xpc.allow</key>

 	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
 	<key>com.apple.private.bdc.tasking</key>
 	<true/>
 	<key>com.apple.private.cloudkit.buddyAccess</key>

 		<string>com.apple.batteryintelligenced.batteryanalysis</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.trial.status</string>
+		<string>com.apple.AttentionAwareness</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### runningboardd

> `/usr/libexec/runningboardd`

```diff

 	<true/>
 	<key>com.apple.private.xpc.launchd.allow-posixspawn-telemetry</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.allow-set-bundle-path</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.app-server</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<array>
 		<string>data-allowed-write</string>
 	</array>
+	<key>com.apple.CoreRoutine.LocationOfInterest</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

 	<true/>
 	<key>com.apple.geoanalyticsd.telemetry</key>
 	<true/>
+	<key>com.apple.geoservices.setanydefault</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 		<string>access-calls</string>
 		<string>modify-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<true/>
 	<key>com.apple.wifi.awdl</key>
 	<true/>
 	<key>com.apple.wifi.eap-nearby-device-setup-config-copy</key>

```
### spatialpreviewd

> `/usr/libexec/spatialpreviewd`

```diff

 	<string>Apple</string>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
+	<key>com.apple.private.arkit.authorization</key>
+	<array>
+		<string>eyeTracking</string>
+	</array>
 	<key>com.apple.private.copresence</key>
 	<true/>
 	<key>com.apple.private.copresence.system-activities</key>

 		<string>/private/var/tmp/</string>
 		<string>/var/mobile/Library/Caches/com.apple.remotespatialpreviewd/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.UXMAssertionService</string>
+		<string>com.apple.sidecar-relay</string>
+		<string>com.apple.arkit.service.gazeTracking</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.remotespatialpreviewservices</string>

```
### spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowcarplayapps</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

```
### spotlightknowledged.importer

> `/usr/libexec/spotlightknowledged.importer`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowcarplayapps</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

```
### spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowcarplayapps</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

```
### studentd

> `/usr/libexec/studentd`

```diff

 	<string>com.apple.studentd</string>
 	<key>com.apple.ClassroomKit.BooksService-access</key>
 	<true/>
+	<key>com.apple.ClassroomKit.KeychainMigrationService-access</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

```
### swtransparencyd

> `/usr/libexec/swtransparencyd`

```diff

 	</array>
 	<key>com.apple.private.security.storage.SFAnalytics</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.privatecloudcompute.serverEnvironment</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### textcontextd

> `/usr/libexec/textcontextd`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.mail</string>
+	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.spotlight.entitledattributes</key>

```
### textunderstandingd

> `/usr/libexec/textunderstandingd`

```diff

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceCalendar</string>
 	</array>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.TextUnderstanding</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.mail</string>
+	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>

```
### toolkitd

> `/usr/libexec/toolkitd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.duetactivityscheduler</string>

 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>

```
### appleh13camerad

> `/usr/sbin/appleh13camerad`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>VADResourceArbiterUserClient</string>
 		<string>ApplePhotonDetectorUserClient</string>
-		<string>IOUserClient</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>VADResourceArbiterUserClient</string>
 		<string>AppleH16PhotonDetectorUserClient</string>
-		<string>IOUserClient</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### screencapture

> `/usr/sbin/screencapture`

```diff

 	</array>
 	<key>com.apple.private.touchbar.display.stream</key>
 	<true/>
+	<key>com.apple.private.windowmanager</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.screencapture</string>

 	<true/>
 	<key>com.apple.security.device.microphone</key>
 	<true/>
+	<key>com.apple.visualintelligence.private.visual-action-prediction</key>
+	<true/>
 </dict>
 </plist>
 

```
### softwareupdate

> `/usr/sbin/softwareupdate`

```diff

 	<true/>
 	<key>com.apple.private.securityd.stash</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.softwareupdate.disablescan</key>
 	<true/>
 	<key>com.apple.private.softwareupdate.postlogoutinstall</key>

```
### spctl

> `/usr/sbin/spctl`

```diff

 <dict>
 	<key>com.apple.private.iokit.nvram-csr</key>
 	<true/>
+	<key>com.apple.private.syspolicy.cache-management</key>
+	<true/>
 </dict>
 </plist>
 

```
### systemkeychain

> `/usr/sbin/systemkeychain`

```diff

 <dict>
 	<key>com.apple.private.security.storage.SystemKeychain</key>
 	<true/>
+	<key>com.apple.private.securityd.keychain-master-key-extraction</key>
+	<true/>
 </dict>
 </plist>
 

```


### SystemOS

### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
+		<string>BlockNetworkAccess</string>
 		<string>BlockEnhancedSecurityLinks</string>
 	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>
+		<string>BlockNetworkAccess</string>
 		<string>BlockEnhancedSecurityLinks</string>
 	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>

```
### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
+		<string>BlockNetworkAccess</string>
 		<string>BlockEnhancedSecurityLinks</string>
 	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>
+		<string>BlockNetworkAccess</string>
 		<string>BlockEnhancedSecurityLinks</string>
 	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>

```
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 		<string>com.firstversionist.polypane</string>
 		<string>com.tab-browser.Tabbit</string>
 		<string>com.tabbit-ai.Tabbit</string>
+		<string>me.bnfy.bowser</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>

```
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/Current/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 		<string>com.firstversionist.polypane</string>
 		<string>com.tab-browser.Tabbit</string>
 		<string>com.tabbit-ai.Tabbit</string>
+		<string>me.bnfy.bowser</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>

```


### AppOS

### Safari

> `/System/Applications/Safari.app/Contents/MacOS/Safari`

```diff

 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/SafariSwift.framework</string>
+		<string>/AppleInternal/Library/Frameworks/ContextStagingIntents.framework</string>
 	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>

```
### PasswordManagerBrowserExtensionHelper

> `/System/Library/CoreServices/PasswordManagerBrowserExtensionHelper.app/Contents/MacOS/PasswordManagerBrowserExtensionHelper`

```diff

           },
           "team-identifier": "2DE8QTFYGR"
         }
+      },
+      {
+        "$and": {
+          "signing-identifier": "me.bnfy.bowser",
+          "team-identifier": "XYGUCY4498"
+        }
       }
     ]
   },

```
### safaridriver

> `/usr/bin/safaridriver`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.launchservices.allowedtolaunchwitharguments</key>
+	<true/>
 	<key>com.apple.private.security.storage.WebDriver</key>
 	<true/>
 	<key>com.apple.private.webinspector.driver-client</key>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

```


