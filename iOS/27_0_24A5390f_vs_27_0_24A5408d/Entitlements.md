## 🔑 Entitlements

### filesystem

### AXUIViewService

> `/Applications/AXUIViewService.app/AXUIViewService`

```diff

 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
-	<false/>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### AuthorizationPromptService

> `/Applications/AuthorizationPromptService.app/AuthorizationPromptService`

```diff

 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.locationd.desktop.synchronous</string>
 		<string>com.apple.mdmclient.daemon.unrestricted</string>
+		<string>com.apple.nehelper</string>
 	</array>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>

```
### Campo

> `/Applications/Campo.app/Campo`

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

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.realitysimulation.render-on-top-spi</key>
+	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.rootless.storage.proactivepredictions</key>

 		<string>/Library/SMS/</string>
 		<string>/Media/PhotoData/</string>
 		<string>/Library/com.apple.ManagedSettings/</string>
+		<string>/Library/UserConfigurationProfiles/</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/Caches/com.apple.countryd/</string>

 		<string>com.apple.remindd</string>
 		<string>com.apple.remindd.userInteractive</string>
 		<string>com.apple.surfboard.entityinteractionservice</string>
+		<string>com.apple.surfboard.lockscreenservice</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.calendar.EventKitUIRemoteUIExtension.viewservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>

 		<string>com.apple.SpotlightFoundation</string>
 		<string>com.apple.SpotlightResources.Defaults</string>
 		<string>com.apple.spotlightui</string>
+		<string>com.apple.UIKit.LTSScrolling</string>
 		<string>com.apple.voiceservices</string>
 		<string>com.apple.PencilKit</string>
 		<string>kCFPreferencesAnyApplication</string>

 	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
+	<key>com.apple.surfboard-prevent-homeui-from-hiding-when-launching</key>
+	<true/>
 	<key>com.apple.surfboard.allow-scene-requests-while-backgrounded</key>
 	<true/>
 	<key>com.apple.surfboard.application-service-client</key>

 	<true/>
 	<key>com.apple.surfboard.launcherservice.client</key>
 	<true/>
+	<key>com.apple.surfboard.lock-screen-client</key>
+	<true/>
 	<key>com.apple.surfboard.opts-out-of-shared-coordinate-origin</key>
 	<true/>
 	<key>com.apple.surfboard.placement-client</key>

```
### CarPlaySettings

> `/Applications/CarPlaySettings.app/CarPlaySettings`

```diff

 	</array>
 	<key>com.apple.private.mediaexperience.setsilentmode.allow</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### CheckerBoard

> `/Applications/CheckerBoard.app/CheckerBoard`

```diff

 	<true/>
 	<key>com.apple.private.diagnosticscheckupd.launch</key>
 	<true/>
+	<key>com.apple.private.exclaves.indicator_min_on_time</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 		<dict>
 			<key>bleRSSIThresholdHint</key>
 			<integer>-48</integer>
+			<key>companionSetupFilters</key>
+			<array>
+				<dict>
+					<key>rssi</key>
+					<integer>-45</integer>
+				</dict>
+			</array>
 			<key>discoveryTypes</key>
 			<array>
 				<string>CompanionSetup</string>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 		<string>UniqueDeviceIDData</string>
 		<string>SerialNumber</string>
 	</array>
-	<key>com.apple.private.ProvInfoIOKitUserClient.access</key>
-	<true/>
 	<key>com.apple.private.SafariServices.PasswordPicker.directlyReceiveCredentials</key>
 	<true/>
 	<key>com.apple.private.SafariServices.PasswordPicker.setRemoteAppProperties</key>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.purplebuddy.budd.proximity.source.xpc</string>
 		<string>com.apple.purplebuddy.budd.migration.source.xpc</string>
+		<string>com.apple.siri.ssrvtuitrainingservice.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.sharing.airdrop.service</string>

```
### HearingWidgetExtension

> `/Applications/HearingApp.app/PlugIns/HearingWidgetExtension.appex/HearingWidgetExtension`

```diff

 	<array>
 		<string>com.apple.accessibility.heard</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.HearingAids</string>
 	</array>

```
### LimitedModeShieldApp

> `/Applications/LimitedModeShieldApp.app/LimitedModeShieldApp`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.private.appmanagedfeatures.activation</key>
 	<true/>
 	<key>com.apple.private.appmanagedfeatures.configuration</key>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 	<true/>
 	<key>com.apple.accessibility.voiceover</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
 	<key>com.apple.aned.private.adapterWeight.allow</key>

 	<true/>
 	<key>com.apple.appleneuralengine.private.allow</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>

 		<key>peripheralsensing</key>
 		<true/>
 	</dict>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
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
 	<key>com.apple.private.sessionkit.custom-platter-target</key>
 	<true/>
 	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.perceptiond.peripheralSensing</string>
 		<string>com.apple.campo</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
+		<string>com.apple.akd</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MediaRemoteUI

> `/Applications/MediaRemoteUI.app/MediaRemoteUI`

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

> `/Applications/MediaRemoteUIService.app/MediaRemoteUIService`

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

### 🆕 SettingsImportExtension

> `/Applications/Preferences.app/PlugIns/SettingsImportExtension.appex/SettingsImportExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.Settings.extension.host</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.Preferences.SettingsImportExtension</string>
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
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
 	<true/>
+	<key>com.apple.icloud.FindMyDevice.RepairDevice.access</key>
+	<true/>
 	<key>com.apple.icloud.FindMyDevice.RepairDeviceLookup.access</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.icloud.searchparty.beaconManager.repairdeviceaccess</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.advertisementcache.access</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.advertisementcache.read</key>

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.iokit.battery-shipping-charge-limit</key>
+	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>

 	<true/>
 	<key>com.apple.private.iokit.charging-iconography</key>
 	<true/>
+	<key>com.apple.private.iokit.powermanagement.read-assertions</key>
+	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>
 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>

 	</array>
 	<key>com.apple.private.mobilemail.mail-recipient-vetting</key>
 	<true/>
+	<key>com.apple.private.mobilerepair.shipmode</key>
+	<true/>
 	<key>com.apple.private.mobilerepair.xpc</key>
 	<true/>
 	<key>com.apple.private.mobilesms.messages-recipient-vetting</key>

 		<string>com.apple.identityservicesd.nsxpc</string>
 		<string>com.apple.identityservicesd.pds</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.installcoordinationd.PersonaLifecycle</string>
 		<string>com.apple.internal.hidrecorderd.xpc</string>
 		<string>com.apple.internal.mtrecorder.xpc</string>
 		<string>com.apple.linkd.extension</string>

```
### SOSBuddy

> `/Applications/SOSBuddy.app/SOSBuddy`

```diff

 	</array>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.bannerkit.post</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### ScreenTimeSettingsShield

> `/Applications/ScreenTimeSettingsShield.app/ScreenTimeSettingsShield`

```diff

 	<true/>
 	<key>com.apple.backboardd</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.screen-time-settings</key>

```
### ServicesPaymentAngel

> `/Applications/ServicesPaymentAngel.app/ServicesPaymentAngel`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.payment.externalized-context</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	</array>
 	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
 	<key>com.apple.private.eligibilityd.fetchNewestPolicies</key>

 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.aa.custodian.xpc</string>
 		<string>com.apple.aa.inheritance.xpc</string>
+		<string>com.apple.aa.accountService.xpc</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.developer.healthkit</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
+	<key>com.apple.private.healthkit.source.identities</key>
+	<array>
+		<string>com.apple.shortcuts</string>
+	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.photos.service.multilibrary</key>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
+	<key>com.apple.powerexperience.powermode.update</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>CLIENT_ENTITLEMENT</string>

 		<string>/private/var/mobile/Library/Assistant/AssistantSampled/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/Applications/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.commandandcontrol</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.powerd.lowpowermode</string>
+		<string>com.apple.powerexperienced.resourceusage</string>
 		<string>com.apple.siri.app</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.remindd</string>

```
### StickersUltraExtension

> `/Applications/StickersUltra.app/PlugIns/StickersUltraExtension.appex/StickersUltraExtension`

```diff

 		<string>com.apple.stickers.api</string>
 		<string>com.apple.stickers.launch-state-manager</string>
 		<string>com.apple.iconservices</string>
+		<string>com.apple.visualintelligence.visual-action-prediction</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### StickersUltra

> `/Applications/StickersUltra.app/StickersUltra`

```diff

 		<string>com.apple.stickers.api</string>
 		<string>com.apple.stickers.launch-state-manager</string>
 		<string>com.apple.iconservices</string>
+		<string>com.apple.visualintelligence.visual-action-prediction</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### WidgetRenderer_Activities

> `/Applications/WidgetRenderer_Activities.app/WidgetRenderer_Activities`

```diff

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.duetexpertd</string>
 		<string>com.apple.frontboardservices.device_emulation</string>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### WidgetRenderer_CarPlay

> `/Applications/WidgetRenderer_CarPlay.app/WidgetRenderer_CarPlay`

```diff

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.duetexpertd</string>
 		<string>com.apple.frontboardservices.device_emulation</string>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### WidgetRenderer_Default

> `/Applications/WidgetRenderer_Default.app/WidgetRenderer_Default`

```diff

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.duetexpertd</string>
 		<string>com.apple.frontboardservices.device_emulation</string>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### WidgetRenderer_Snapshots

> `/Applications/WidgetRenderer_Snapshots.app/WidgetRenderer_Snapshots`

```diff

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.duetexpertd</string>
 		<string>com.apple.frontboardservices.device_emulation</string>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```

### 🆕 WidgetRenderer_StandBy

> `/Applications/WidgetRenderer_StandBy.app/WidgetRenderer_StandBy`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.chrono.WidgetRenderer-Default</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.chrono.event-service-publisher</key>
	<true/>
	<key>com.apple.chrono.widgetRenderer</key>
	<true/>
	<key>com.apple.coreduet.knowledge</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.heartratecoordinator.spi.heartrate</key>
	<true/>
	<key>com.apple.lightsourcesupport.listener</key>
	<true/>
	<key>com.apple.lightsourcesupport.motion</key>
	<true/>
	<key>com.apple.localizationswitcher</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.nano.nanoregistry</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.lookup</key>
	<dict>
		<key>appData</key>
		<true/>
	</dict>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.appmanagedfeatures.configuration</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/Applications/WidgetRenderer_StandBy.app/WidgetRenderer_StandBy</string>
	</dict>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Carousel.Connection.Companion</string>
	</array>
	<key>com.apple.private.chrono-extension-host</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.graphics-restart-no-kill</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.authorization_bypass</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>DuetActivitySchedulerWidgetRefresh</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Widgets.Viewed</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.iokit.batterydataprecise</key>
	<true/>
	<key>com.apple.private.iokit.batteryhealthstate</key>
	<true/>
	<key>com.apple.private.iokit.charging-iconography</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.photos.XPCStoreOptIn</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<string>group.com.apple.chronod</string>
	<key>com.apple.private.security.storage.AppDataContainers</key>
	<true/>
	<key>com.apple.private.security.storage.chronod</key>
	<true/>
	<key>com.apple.private.sessionkit.listener</key>
	<true/>
	<key>com.apple.private.sessionkit.presentationAssertionRequester</key>
	<true/>
	<key>com.apple.private.sessionkit.sessionFinisher</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceSystemPolicyAppData</string>
		<string>kTCCServiceMotion</string>
	</array>
	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
	<true/>
	<key>com.apple.runningboard.assertions.chronod</key>
	<true/>
	<key>com.apple.runningboard.assertions.widgetRenderer</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Applications/</string>
		<string>/System/Library/CoreServices/</string>
		<string>/AppleInternal/Applications/</string>
		<string>/private/var/containers/Bundle/Application/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/chronod/</string>
		<string>/Library/Fonts/AddedFontCache.plist</string>
		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
		<string>/Library/UserFonts/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.chronod/</string>
		<string>/Library/Caches/com.apple.chrono/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<string>IOHIDLibUserClient</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.chronoservices</string>
		<string>com.apple.backboard.hid.services</string>
		<string>com.apple.backboard.display.services</string>
		<string>com.apple.iohideventsystem</string>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.CARenderServer</string>
		<string>com.apple.UIKit.KeyboardManagement.hosted</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.iphone.axserver-systemwide</string>
		<string>com.apple.accessibility.AXBackBoardServer</string>
		<string>com.apple.proactive.infoSuggestion.xpc</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.locationd.registration</string>
		<string>com.apple.PointerUI.pointeruid.service</string>
		<string>com.apple.fontservicesd</string>
		<string>com.apple.backboard.hid-services.xpc</string>
		<string>com.apple.springboard.services</string>
		<string>com.apple.locationd.synchronous</string>
		<string>com.apple.backlightd</string>
		<string>com.apple.symptom_diagnostics</string>
		<string>com.apple.localizationswitcherd</string>
		<string>com.apple.sessionservices</string>
		<string>com.apple.coremedia.compressionsession</string>
		<string>com.apple.coremedia.decompressionsession</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
		<string>com.apple.mobile.usermanagerd.xpc</string>
		<string>com.apple.chrono.event-service.gamed</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.lightsourcesupport.lightstate</string>
		<string>com.apple.heartratecoordinatord.requestor</string>
		<string>com.apple.appmanagedfeatures.configuration</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.local-name</key>
	<array>
		<string>com.apple.iphone.axserver</string>
	</array>
	<key>com.apple.security.exception.mach-register.global-name</key>
	<array>
		<string>com.apple.chrono.widgetcenterconnection</string>
		<string>com.apple.chronod.gsEvents</string>
		<string>com.apple.chronoservices</string>
	</array>
	<key>com.apple.security.exception.mach-register.local-name</key>
	<array>
		<string>com.apple.iphone.axserver</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
		<string>com.apple.chronod</string>
		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
		<string>com.apple.BatteryCenter.BatteryWidget</string>
		<string>com.apple.Preferences</string>
		<string>com.apple.coremedia</string>
		<string>com.apple.UIKit</string>
		<string>com.apple.keyboard</string>
		<string>com.apple.da</string>
		<string>com.apple.SpeakSelection</string>
		<string>com.apple.coreanimation</string>
		<string>com.apple.duetexpertd</string>
		<string>com.apple.frontboardservices.device_emulation</string>
		<string>com.apple.health.shared</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.ts.mach-task-name</key>
	<true/>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
	<key>com.apple.security.ts.power-assertions</key>
	<true/>
	<key>com.apple.security.ts.render-images</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.chrono</string>
	<key>com.apple.sessionservices</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### WidgetRenderer_WatchFaces

> `/Applications/WidgetRenderer_WatchFaces.app/WidgetRenderer_WatchFaces`

```diff

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.duetexpertd</string>
 		<string>com.apple.frontboardservices.device_emulation</string>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.accessibility.physicalinteraction.client</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.airplay.autoconnect.services.allow</key>
 	<true/>
 	<key>com.apple.airplay.receiver.mediaremote.services</key>

 	<true/>
 	<key>com.apple.audio.allows.mix.to.uplink</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

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
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 		<key>value</key>
 		<string>/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer</string>
 	</dict>
+	<key>com.apple.private.automatic-assessment-configuration.restrictor</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.private.driverkit.driver-access</key>
 	<array>
 		<string>com.apple.private.wifi.driverkit</string>

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

 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.akd</string>
 		<string>com.apple.private.corewifi.internal-xpc</string>
 		<string>com.apple.coremedia.endpointuiagent.xpc</string>
 		<string>com.apple.nanoprefsync</string>

 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
 		<string>com.apple.sharingd.nsxpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.springboard.secure-indicator-elevation</key>
+	<true/>
 	<key>com.apple.springboard.springboard.system-aperture-portaling</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>
 	<true/>
+	<key>com.apple.springboard.secure-indicator-elevation</key>
+	<true/>
 	<key>com.apple.springboard.system-component-layout-monitoring</key>
 	<true/>
 	<key>com.apple.springboard.system-component-restriction</key>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>
 	<true/>
+	<key>com.apple.springboard.secure-indicator-elevation</key>
+	<true/>
 	<key>com.apple.springboard.system-component-layout-monitoring</key>
 	<true/>
 	<key>com.apple.surfboard-prevent-homeui-from-hiding-when-launching</key>

```
### PhotosViewService

> `/System/Library/CoreServices/PhotosViewService.app/PhotosViewService`

```diff

 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.server.bluetooth.general.xpc</string>
 		<string>com.apple.powerd.smartpowernap</string>
+		<string>com.apple.powerd.coresmartpowernap</string>
 		<string>com.apple.biomesyncd.realTimeSession</string>
 		<string>com.apple.sessionservices</string>
 		<string>aps-connection-initiate</string>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<true/>
 	<key>com.apple.accessibility.voiceover</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.VoiceOver.Braille</string>

 	<true/>
 	<key>com.apple.private.accessibility.scrod</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.private.donotdisturb.behavior.resolution.client-identifiers</key>
 	<array>
 		<string>com.apple.accessibility.AXTapticChimesScheduler</string>

 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sociallayer.accessibility</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.TextInput.rdt</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
+		<string>com.apple.akd</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### AgeVerificationExtension

> `/System/Library/ExtensionKit/Extensions/AgeVerificationExtension.appex/AgeVerificationExtension`

```diff

 <dict>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/tmp/com.apple.AppleMediaServices/</string>

```
### AppManagedFeaturesDemoExtension

> `/System/Library/ExtensionKit/Extensions/AppManagedFeaturesDemoExtension.appex/AppManagedFeaturesDemoExtension`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.safefinancing.demoextension</string>
+	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 </dict>
 </plist>
 

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension`

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
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

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

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/FedStatsPluginDynamic`

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

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/FedStatsPluginStatic`

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

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Applications/</string>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

```

### 🆕 MacinTalkAUSP

> `/System/Library/ExtensionKit/Extensions/MacinTalkAUSP.appex/MacinTalkAUSP`

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
### MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/MapsIntents`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>

```
### MediaRemoteAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/MediaRemoteAppIntentsExtension.appex/MediaRemoteAppIntentsExtension`

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

### 🆕 Celosia.metallib

> `/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/Celosia.metallib`

- No entitlements *(yet)*
### PhotosFileProvider

> `/System/Library/ExtensionKit/Extensions/PhotosFileProvider.appex/PhotosFileProvider`

```diff

 	<true/>
 	<key>com.apple.private.photos.cpanalytics.cache.read</key>
 	<true/>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.photos.service.mediaconversion</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

```
### PhotosMessagesApp

> `/System/Library/ExtensionKit/Extensions/PhotosMessagesApp.appex/PhotosMessagesApp`

```diff

 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
+	<key>com.apple.mediaanalysisd.client</key>
+	<true/>
 	<key>com.apple.messages.private.AllowAllPresentationStyles</key>
 	<true/>
 	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>

```
### PrivateMLClientInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService`

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
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.customaccesssinfo</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.ap.idmanager</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.servicesintelligence</key>
+	<true/>
 	<key>com.apple.private.storekit</key>
 	<array>
 		<string>AdvancedPurchase</string>

 		<string>com.apple.ScreenTimeAgent.exception</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.aa.identity.xpc</string>
+		<string>com.apple.servicesintelligenced</string>
+		<string>com.apple.amsondevicestoraged.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.AdPlatforms</string>
+		<string>com.apple.storeservices.itfe</string>
 	</array>
 	<key>com.apple.security.system-group-containers</key>
 	<array>

```
### ReceiptsExtractionDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/ReceiptsExtractionDiagnosticExtension.appex/ReceiptsExtractionDiagnosticExtension`

```diff

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.financed.service.coredatastore</string>

```
### ScreenTimeSettingsResponseExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeSettingsResponseExtension.appex/ScreenTimeSettingsResponseExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>application-identifier</key>
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
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.adid</string>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.FamilyControlsAgent</string>
 		<string>com.apple.FamilyControlsAgent.private</string>
+		<string>com.apple.iconservices</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
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

### 🆕 SiriSetupSettingsIntents

> `/System/Library/ExtensionKit/Extensions/SiriSetupSettingsIntents.appex/SiriSetupSettingsIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
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
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.customaccesssinfo</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.ap.idmanager</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.servicesintelligence</key>
+	<true/>
 	<key>com.apple.private.storekit</key>
 	<array>
 		<string>AdvancedPurchase</string>

 		<string>com.apple.ScreenTimeAgent.exception</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.aa.identity.xpc</string>
+		<string>com.apple.servicesintelligenced</string>
+		<string>com.apple.amsondevicestoraged.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.AdPlatforms</string>
+		<string>com.apple.storeservices.itfe</string>
 	</array>
 	<key>com.apple.security.system-group-containers</key>
 	<array>

```
### apfs_checkdigest

> `/System/Library/Filesystems/apfs.fs/apfs_checkdigest`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.get-dstreams</key>
+	<true/>
+	<key>com.apple.private.apfs.get-file-exts</key>
+	<true/>
 	<key>com.apple.private.apfs.lock-container-load</key>
 	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>

```
### apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.get-dstreams</key>
+	<true/>
+	<key>com.apple.private.apfs.get-file-exts</key>
+	<true/>
 	<key>com.apple.private.apfs.lock-container-load</key>
 	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>

```
### apfs_computedigest

> `/System/Library/Filesystems/apfs.fs/apfs_computedigest`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.get-dstreams</key>
+	<true/>
+	<key>com.apple.private.apfs.get-file-exts</key>
+	<true/>
 	<key>com.apple.private.apfs.lock-container-load</key>
 	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>

```
### apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

 		<string>CLIENT_ENTITLEMENT</string>
 		<string>PURGEABLE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.apfs.get-dstreams</key>
+	<true/>
+	<key>com.apple.private.apfs.get-file-exts</key>
+	<true/>
 	<key>com.apple.private.apfs.get-graft-info</key>
 	<true/>
 	<key>com.apple.private.apfs.key-cache-eviction</key>

```
### apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
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

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
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

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
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

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.coreidv.system-notifications.accounts</key>

```
### appmanagedfeaturesd

> `/System/Library/Frameworks/AppManagedFeatures.framework/Support/appmanagedfeaturesd`

```diff

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.configurationprofiles</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.appmanagedfeaturesd</string>
 	<key>com.apple.softwareupdateservices.client.allowed</key>

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
### CommCenterMobileHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper`

```diff

 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
+		<string>systemgroup.com.apple.regulatory_images</string>
 	</array>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	</array>
 	<key>com.apple.devicecheck.daemon-client</key>
 	<true/>
+	<key>com.apple.devicecheck.private.certificate.validity</key>
+	<integer>2628000</integer>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.finance.private</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>

 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceFinancialData</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>

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

> `/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent`

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

> `/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService`

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

> `/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension`

```diff

 	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screen-time-settings</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 </dict>

```
### XPCAcmeService

> `/System/Library/Frameworks/Security.framework/XPCServices/XPCAcmeService.xpc/XPCAcmeService`

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
### wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

 		<string>com.apple.navigationListener</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.bluetooth.xpc</string>
+		<string>com.apple.iohideventsystem</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 AuthenticationServicesDeveloperSettings

> `/System/Library/PreferenceBundles/AuthenticationServicesDeveloperSettings.bundle/AuthenticationServicesDeveloperSettings`

- No entitlements *(yet)*

### 🆕 PasswordsDeveloperSettings

> `/System/Library/PreferenceBundles/PasswordsDeveloperSettings.bundle/PasswordsDeveloperSettings`

- No entitlements *(yet)*
### axassetsd

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/Support/axassetsd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.analyticsd</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.voicebanking.services</string>
 		<string>com.apple.voicebanking.store</string>

```
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/BundledIntentHandler`

```diff

 	<array>
 		<string>com.apple.radios.plist</string>
 	</array>
+	<key>com.apple.accessibility.physicalinteraction.client</key>
+	<true/>
 	<key>com.apple.backboard.displaybrightness</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

```
### agentstored

> `/System/Library/PrivateFrameworks/AgentSessionKitRuntime.framework/agentstored`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.appleintelligencereporting.processing</key>
 	<true/>
 	<key>com.apple.assertiond.system-shell</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

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

 	<array>
 		<string>/Library/AppleIntelligencePlatform/AgentSessionKit/</string>
 		<string>/Library/Shortcuts/</string>
+		<string>/Library/AgentSessionKitBackupStaging/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.ak.auth.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<string>com.apple.GenerativeFunctions.agentstored</string>
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
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppleMediaServices</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowquerydraintrigger</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.readonly</key>
 	<true/>
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
 		<string>SIRI_MESSAGES_ANNOUNCE_HINT_EDUCATION</string>
 		<string>SIRI_MESSAGES_APP_SELECTION</string>

```
### AKAppSSOExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.associated-domains</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>com.apple.aa.custodian.xpc</string>
 		<string>com.apple.aa.daemon.xpc
 </string>
+		<string>com.apple.SharedWebCredentials</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

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

> `/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService`

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
### clipserviced

> `/System/Library/PrivateFrameworks/ClipServices.framework/clipserviced`

```diff

 	<array>
 		<string>/Library/Caches/GeoServices/</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

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
### CloudSharingAccessSelectionViewService-iOS

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/CloudSharingAccessSelectionViewService-iOS.appex/CloudSharingAccessSelectionViewService-iOS`

```diff

 	<array>
 		<string>com.apple.coreduetd.people</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### com.apple.CloudSharingUI.AddParticipants

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants`

```diff

 	<array>
 		<string>com.apple.coreduetd.people</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### ACCNowPlayingFeature

> `/System/Library/PrivateFrameworks/CoreAccessoriesFeatures.framework/XPCServices/ACCNowPlayingFeature.xpc/ACCNowPlayingFeature`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>application-identifier</key>
+	<string>com.apple.accessories.now-playing-feature</string>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceMediaLibrary</string>
+	</array>
+	<key>platform-application</key>
+	<true/>
+</dict>
+</plist>
 

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
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>

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
### CoreRepairCoreXPCService

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/XPCServices/CoreRepairCoreXPCService.xpc/CoreRepairCoreXPCService`

```diff

 <dict>
 	<key>com.apple.AppleNVMeEAN.allow</key>
 	<true/>
+	<key>com.apple.CheckerBoard.services</key>
+	<true/>
 	<key>com.apple.CheckerBoard.services.reboot</key>
 	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>

 	<true/>
 	<key>com.apple.private.img4.nonce.trust-cache</key>
 	<true/>
+	<key>com.apple.private.iokit.battery-shipping-charge-limit</key>
+	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.iokit.batterydateoffirstuse</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CheckerBoard.services</string>
 		<string>com.apple.ctkd.token-client</string>
 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.appleh16camerad</string>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

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
### DTServiceHub

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub`

```diff

 	<integer>1</integer>
 	<key>com.apple.private.cpu-counters.system-control</key>
 	<true/>
+	<key>com.apple.private.cs.debugger.safe</key>
+	<true/>
 	<key>com.apple.private.dt.instrumentsxpc.allowed</key>
 	<true/>
 	<key>com.apple.private.dtservicehubidentity</key>

```
### LeakAgent

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/LeakAgent`

```diff

 <dict>
 	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
 	<true/>
+	<key>com.apple.private.cs.debugger.safe</key>
+	<true/>
 	<key>com.apple.private.iosurfaceinfo</key>
 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

```
### DeviceConfigurationAgent

> `/System/Library/PrivateFrameworks/DeviceConfiguration.framework/DeviceConfigurationAgent`

```diff

 	<string>com.apple.DeviceConfigurationAgent</string>
 	<key>com.apple.private.device-configuration.consumer.private</key>
 	<true/>
+	<key>com.apple.private.device-configuration.user.private</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.protected-system-container</key>

 	<array>
 		<string>com.apple.deviceconfigurationd.consumer.private.async</string>
 		<string>com.apple.deviceconfigurationd.publisher</string>
+		<string>com.apple.deviceconfigurationd.user.private.async</string>
 		<string>com.apple.duetactivityscheduler</string>
 	</array>
 </dict>

```
### deviceconfigurationd

> `/System/Library/PrivateFrameworks/DeviceConfiguration.framework/deviceconfigurationd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.deviceconfigurationd</string>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
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
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.protected-system-container</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.mobile.keybagd.xpc</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.DocumentManagerCore.Rename

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename`

```diff

 		<string>com.apple.FileProvider</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.CoreServices.coreservicesd</string>
+		<string>com.apple.DesktopServicesHelper</string>
+		<string>com.apple.DesktopServicesHelper.FileService</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
 		<string>com.apple.sage</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.gms.availability</string>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
+	<key>com.apple.private.sleepd</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 		<string>com.apple.audio.AURemoteIOServer</string>
 		<string>com.apple.videoconference.camera</string>
 		<string>com.apple.healthd.server</string>
+		<string>com.apple.sleepd.sleepserver</string>
 		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.audio.AudioQueueServer</string>

```
### HearingWidgetExtension

> `/System/Library/PrivateFrameworks/HearingWidgetExtension.appex/HearingWidgetExtension`

```diff

 	<array>
 		<string>com.apple.accessibility.heard</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.HearingAids</string>
 	</array>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	</array>
 	<key>com.apple.private.assistant.settings</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.SiriApp</string>
+	</dict>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.intelligenceflow.intelligencecontextd</string>
 	<key>com.apple.private.biome.read-only</key>

 		<string>com.apple.callkit.callcontrollerhost</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.coreservices.quarantine-resolver</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.siri.device_resolution</string>

```

### 🆕 IntelligenceFlowCustomerDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowCustomerDiagnostics.appex/IntelligenceFlowCustomerDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.intelligenceflow.IntelligenceFlowRuntime.IntelligenceFlowCustomerDiagnostics</string>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
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
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/com.apple.FeatureStore/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.intelligenceflow.context</string>
		<string>com.apple.private.siriappintentsd.orchestrator</string>
	</array>
</dict>
</plist>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.intelligenceflow.contextTool</key>
 	<true/>
+	<key>com.apple.intelligenceflow.imageretrieval</key>
+	<true/>
 	<key>com.apple.intelligenceflow.orchestrator</key>
 	<true/>
 	<key>com.apple.intelligenceflow.orchestrator.features</key>

 	<true/>
 	<key>com.apple.private.attentionawareness.poll</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.SiriApp</string>
+	</dict>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.intelligenceflow.intelligenceflowd</string>
 	<key>com.apple.private.biome.read-only</key>

 		<string>com.apple.intelligenceflow.orchestrator</string>
 		<string>com.apple.intelligenceflow.uiContext</string>
 		<string>com.apple.intelligenceflow.querydecoration</string>
+		<string>com.apple.intelligenceflow.imageretrieval</string>
 		<string>com.apple.intelligenceplatform.Knosis</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>

 		<string>com.apple.powerexperienced.resourceusage</string>
 		<string>com.apple.private.corewifi.readonly-xpc</string>
 		<string>com.apple.CoreAuthentication.agent</string>
+		<string>com.apple.toolkitd.xpc</string>
+		<string>com.apple.siriactionsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.symptoms.NetworkDiagnostics</key>
 	<true/>
+	<key>com.apple.toolkit.request-immediate-indexing.allow</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1150</string>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/XPCServices/Managed Background Assets Helper Service.xpc/Managed Background Assets Helper Service`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.backgroundassets.managed.helper.fetching.service</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

```
### navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

 	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
+	<string>com.apple.Maps</string>
 	<key>com.apple.private.appintents.live-entities.read</key>
 	<true/>
 	<key>com.apple.private.appintents.live-entities.write</key>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
 		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>MediaAnalysis.TextUnderstanding.ProcessingResults</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
 	<key>com.apple.private.ciphermld.allow</key>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
 		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>MediaAnalysis.TextUnderstanding.ProcessingResults</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
 	<key>com.apple.private.ciphermld.allow</key>

```
### mediaanalysisd-generation

> `/System/Library/PrivateFrameworks/MediaAnalysisGeneration.framework/XPCServices/mediaanalysisd-generation.xpc/mediaanalysisd-generation`

```diff

 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.mediaanalysisd-generation</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/</string>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

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

> `/System/Library/PrivateFrameworks/OmniSearch.framework/searchtoold`

```diff

 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.filebrowsingservices.path-resolver-client</key>
+	<true/>
 	<key>com.apple.private.generativesearch.client.search</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.userprofiles</string>
 		<string>com.apple.tccd</string>
+		<string>com.apple.FileBrowsingServices.PathResolver</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<array>
 		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.photos.service</string>
+		<string>com.apple.visualintelligence.visual-action-prediction</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
+	<key>com.apple.visualintelligence.private.visual-action-prediction</key>
+	<true/>
 	<key>com.apple.wallet.banner</key>
 	<true/>
 	<key>fairplay-client</key>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

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

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/XPCServices/com.apple.photos.PCCService.xpc/com.apple.photos.PCCService`

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
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

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
### DeviceConfigurationSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/DeviceConfigurationSubscriber.xpc/DeviceConfigurationSubscriber`

```diff

 		<string>com.apple.deviceconfigurationd.provider</string>
 		<string>com.apple.deviceconfigurationd.provider.async</string>
 		<string>com.apple.DeviceConfigurationAgent.provider</string>
+		<string>com.apple.DeviceConfigurationAgent.provider.async</string>
 		<string>com.apple.remotemanagementd.store</string>
 		<string>com.apple.RemoteManagementAgent.store</string>
 	</array>

```
### ManagedStatusSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedStatusSubscriber.xpc/ManagedStatusSubscriber`

```diff

 	<string>com.apple.remotemanagement.ManagedStatusSubscriber</string>
 	<key>com.apple.managedconfiguration.mdmd-access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.mdmuserd-access</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDM.plist</string>
+		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MultiUserDeviceConfiguration.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.enhancedloggingd.xpc</string>
 		<string>com.apple.managedconfiguration.mdmdservice</string>
+		<string>com.apple.managedconfiguration.mdmuserdservice</string>
 		<string>com.apple.mobilerepaird</string>
 		<string>com.apple.remotemanagementd.store</string>
 		<string>com.apple.RemoteManagementAgent.store</string>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>AppStore</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Device.Display.Backlight</string>

 		<string>App.WebUsage</string>
 		<string>Family.ScreenTime.ChildState</string>
 	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Discoverability.Signals</string>
+	</array>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.ScreenTimeSettings</key>

 	<array>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.adid</string>
+		<string>com.apple.appstored.xpc.request</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>

 	<array>
 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceReminders</string>
 	</array>
-	<key>com.apple.private.tcc.events.subscriber</key>
-	<true/>
-	<key>com.apple.private.tcc.manager.access.read</key>
+	<key>com.apple.private.tcc.manager.read.access</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>

```
### budd

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/budd`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>

 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.aa.accountService.xpc</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-write</key>
 	<array>

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

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>

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
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### PhoneIntentHandler

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler`

```diff

 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.identityservicesd.desktop.auth</string>
 		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.commcenter.xpc</string>

```
### matd

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/matd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
+	<key>com.apple.private.security.storage.MessagesEscrow</key>
+	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.Pasteboard.trusted-bundle-layout</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MapKit.SnapshotService</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.TextInput.rdt</string>

 		<string>com.apple.nesessionmanager</string>
 		<string>com.apple.posterboardservices.dataModel</string>
 		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.private.corewifi.internal-xpc</string>
 		<string>com.apple.remindd</string>

```
### bird

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/bird`

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
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.private.accounts.customaccesssinfo</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.ap.idmanager</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.servicesintelligence</key>
+	<true/>
 	<key>com.apple.private.storekit</key>
 	<array>
 		<string>AdvancedPurchase</string>

 		<string>com.apple.ScreenTimeAgent.exception</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.aa.identity.xpc</string>
+		<string>com.apple.servicesintelligenced</string>
+		<string>com.apple.amsondevicestoraged.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.AdPlatforms</string>
+		<string>com.apple.storeservices.itfe</string>
 	</array>
 	<key>com.apple.security.system-group-containers</key>
 	<array>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents.build-lockup-from-mapi-response</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.small-offer-button</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Purchase</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<true/>
 	<key>com.apple.NPKCompanionAgent.client</key>
 	<true/>
+	<key>com.apple.NanoPassbook.IDVRemoteDeviceService.session.client</key>
+	<true/>
 	<key>com.apple.PassKit.issuer-provisioning.consumer</key>
 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<true/>
 	<key>com.apple.aeroml.intentrecommend.mediasuggester</key>
 	<true/>
+	<key>com.apple.appleaccount.identity.read</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
 	<key>com.apple.developer.networking.carrier-constrained.app-optimized</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.fitnessintelligenced</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.activityawardsd</string>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	<true/>
 	<key>com.apple.private.appstorecomponents.build-lockup-from-mapi-response</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents.small-offer-button</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Ocelot</string>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.fpsd.client</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 		<string>com.apple.GameStoreKit</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.storeservices.itfe</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

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
### HomeNotification

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification`

```diff

 	<string>com.apple.Home.HomeNotification</string>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.inactive.fullaccess</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+		<string>re6Zb+zwFKJNlkQTUeT+/w</string>
+	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

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

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

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

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/Applications/</string>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 	<true/>
 	<key>com.apple.accessibility.voiceover</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
 	<key>com.apple.aned.private.adapterWeight.allow</key>

 	<true/>
 	<key>com.apple.appleneuralengine.private.allow</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
 	<true/>
 	<key>com.apple.developer.declared-age-range</key>

 	<true/>
 	<key>com.apple.private.MagnifierAngel.client</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/MagnifierSupport.framework</string>

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
 	<key>com.apple.private.system-keychain</key>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.accessibility.MagnifierAngel.mach</string>
 		<string>com.apple.campo</string>
+		<string>com.apple.DeviceConfigurationAgent.consumer</string>
+		<string>com.apple.akd</string>
+		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>
 	<true/>
+	<key>com.apple.private.appintents.exception.continue-in-foreground-no-prompt-allowed</key>
+	<true/>
 	<key>com.apple.private.appintents.live-entities.read</key>
 	<true/>
 	<key>com.apple.private.appintents.live-entities.write</key>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	</array>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<array>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<array>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<true/>
 	<key>com.apple.developer.browser.app-installation</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

 	<string>Browser-9003</string>
 	<key>com.apple.developer.networking.slicing.trafficcategory</key>
 	<string>video-2</string>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.mobilesafari</string>
 	<key>com.apple.developer.web-browser</key>
 	<true/>
 	<key>com.apple.diagnosticpipeline.request</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.ageRange</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/MobileSafari.framework</string>
+		<string>/AppleInternal/Library/Frameworks/ContextStagingIntents.framework</string>
 	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.background-tasks.continued-processing.inference</key>
+	<true/>
 	<key>com.apple.developer.carplay-audio</key>
 	<true/>
 	<key>com.apple.developer.declared-age-range</key>

```
### Weather

> `/private/var/staged_system_apps/Weather.app/Weather`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.ageRange</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<false/>
 	<key>com.apple.private.applemediaservices</key>

```

### 🆕 meminfo

> `/usr/bin/meminfo`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.kernel.get-kext-info</key>
	<true/>
	<key>com.apple.private.memoryinfo</key>
	<true/>
</dict>
</plist>

```
### perfpowermetricd

> `/usr/bin/perfpowermetricd`

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
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

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
 	<key>com.apple.private.automatic-assessment-configuration.restrictor</key>
 	<true/>
+	<key>com.apple.private.device-configuration.provider.allowed-provider-ids</key>
+	<array>
+		<string>com.apple.AutomaticAssessmentConfiguration</string>
+	</array>
 	<key>com.apple.private.neagent</key>
 	<true/>
 	<key>com.apple.private.necp.policies</key>

 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.DeviceConfigurationAgent.provider.async</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### atc

> `/usr/libexec/atc`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.atc</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>Dormancy</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Dormancy.Feature.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.librarian.can-get-application-info</key>

```
### batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

 	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
+	<key>com.apple.private.clpc.analysis</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.batteryintelligence</string>

 	<true/>
 	<key>com.apple.private.powersource-read</key>
 	<true/>
+	<key>com.apple.private.ppm.superclient</key>
+	<true/>
 	<key>com.apple.private.smcsensor.user-access</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 	<array>
 		<string>AGXDeviceUserClient</string>
 		<string>AppleSMCClient</string>
+		<string>ApplePPMUserClient</string>
+		<string>AppleCLPCUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

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
### corerepaird

> `/usr/libexec/corerepaird`

```diff

 <dict>
 	<key>com.apple.AppleNVMeEAN.allow</key>
 	<true/>
+	<key>com.apple.CheckerBoard.services</key>
+	<true/>
 	<key>com.apple.CheckerBoard.services.reboot</key>
 	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>

 	<true/>
 	<key>com.apple.private.img4.nonce.trust-cache</key>
 	<true/>
+	<key>com.apple.private.iokit.battery-shipping-charge-limit</key>
+	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.iokit.batterydateoffirstuse</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CheckerBoard.services</string>
 		<string>com.apple.ctkd.token-client</string>
 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.appleh16camerad</string>

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
### idcredd

> `/usr/libexec/idcredd`

```diff

 	<true/>
 	<key>com.apple.nfcd.session.se</key>
 	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
 	<key>com.apple.private.appleidv.allow</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.passd.library</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.seserviced</string>
 		<string>com.apple.securityd</string>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-capture</key>
 	<true/>
+	<key>com.apple.backboardd.displayTraits</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.feedbackd.remote-evaluation</key>

 	<array>
 		<string>kTCCServicePhotosAdd</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.mail</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>private/var/db/eligibilityd/eligibility.plist</string>

 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.audio.AudioSession</string>
+		<string>com.apple.backboard.display.services</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.keyboard.preferences</string>
 		<string>com.apple.suggestions</string>
+		<string>com.apple.assistant.support</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### linkd

> `/usr/libexec/linkd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.linkd</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.linkd.suggestedentities</string>
 		<string>com.apple.mobile.installd</string>
 		<string>com.apple.siriknowledged.koa.donate</string>

```
### manageddeviced

> `/usr/libexec/manageddeviced`

```diff

 		<string>UninstallForLaunchServices</string>
 		<string>InstallForLaunchServices</string>
 	</array>
+	<key>com.apple.private.persona-read-all</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 		<string>modify-activity-session-airplay</string>
 		<string>access-calls</string>
 	</array>
+	<key>com.apple.translation.can-override-client-pid</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>311</string>

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
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 	<true/>
 	<key>com.apple.private.accounts.bundleidspoofing</key>
 	<true/>
+	<key>com.apple.private.activityprogress.ui.preserve-failure-subtitle</key>
+	<true/>
 	<key>com.apple.private.activityprogress.ui.show</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

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
### riskdatad

> `/usr/libexec/riskdatad`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>abs-client</key>
-	<string>143531244</string>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

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

 	<true/>
 	<key>com.apple.geoanalyticsd.telemetry</key>
 	<true/>
+	<key>com.apple.geoservices.setanydefault</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.localfindable</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
+	<key>com.apple.private.attentionawareness.poll</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.sharingd</string>
 	<key>com.apple.private.biome.read-write</key>

 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.accessories.blepairing</string>
 		<string>com.apple.appleidsetupd.repair.xpc</string>
+		<string>com.apple.AttentionAwareness</string>
 		<string>com.apple.audio.hapticd</string>
 		<string>com.apple.BluetoothCloudServices</string>
 		<string>com.apple.bulletinboard.observerconnection</string>

 		<string>access-calls</string>
 		<string>modify-calls</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>com.apple.uservault</key>

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
### symptomsd

> `/usr/libexec/symptomsd`

```diff

 	<true/>
 	<key>com.apple.SystemConfiguration.SCNetworkInterfaceSetAdvisory</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.awdd.manager-access</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

```
### symptomsd-helper

> `/usr/libexec/symptomsd-helper`

```diff

 	<true/>
 	<key>com.apple.SystemConfiguration.SCNetworkInterfaceSetAdvisory</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>orientation_1</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.awdd.manager-access</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

```
### terminusd

> `/usr/libexec/terminusd`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Caches/com.apple.HomeKit</string>
-		<string>Library/Caches/com.apple.HomeKit.configurations/</string>
 		<string>Library/Caches/com.apple.HomeKit/com.apple.terminusd/</string>
 		<string>tmp/</string>
 	</array>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.home</string>
-		<string>com.apple.TVOSUpdate</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-write</key>
 	<array>

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
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.corerecents.recentsd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.generativesearch.server.insights</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

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
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/</string>

 		<string>com.apple.email.maild</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.privatecloudcompute</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

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
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>

 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.userprofiles</string>
 	</array>
 	<key>com.apple.shortcuts.toolkitd</key>

```
### trustd

> `/usr/libexec/trustd`

```diff

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.ValidUpdater</string>
 		<string>com.apple.cloudtelemetry</string>
+		<string>com.apple.timed.xpc</string>
 	</array>
 	<key>com.apple.validUpdater.acccess</key>
 	<true/>

```
### uarphidd

> `/usr/libexec/uarphidd`

```diff

 	<key>com.apple.security.ts.asset-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
-	<string>com.apple.uarphidd</string>
+	<string>com.apple.MobileAccessoryUpdater</string>
 	<key>com.apple.uarp</key>
 	<true/>
 	<key>com.apple.uarp.endpoint.transport</key>

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


### ExclaveOS


### 🆕 ACIExclaveProcKit

> `/System/ExclaveKit/System/Library/PrivateFrameworks/ACIExclaveProcKit.framework/ACIExclaveProcKit`

- No entitlements *(yet)*


