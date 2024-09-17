## 🔑 Entitlements

### AskToMessagesExtension

> `/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.messages.private.AllowAlertPresentation</key>
 	<true/>
+	<key>com.apple.messages.private.AllowGUIDAccess</key>
+	<true/>
 	<key>com.apple.messages.private.AllowParticipantAddressAccess</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<array>
 		<string>com.apple.asktod</string>
 		<string>com.apple.ScreenTimeAgent.ask</string>
+		<string>com.apple.contactsd</string>
+		<string>com.apple.contactsd.persistence</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.asktod</string>
 		<string>com.apple.ScreenTimeAgent.ask</string>
+		<string>com.apple.contactsd</string>
+		<string>com.apple.contactsd.persistence</string>
 	</array>
 </dict>
 </plist>

```
### BarcodeScanner

> `/Applications/BarcodeScanner.app/BarcodeScanner`

```diff

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.ClipServices.clipserviced</string>
 		<string>com.apple.RemoteDisplay</string>
+		<string>com.apple.CameraOverlayAngel.application-service</string>
 	</array>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>

```
### BarcodeScannerCaptureExtension

> `/Applications/BarcodeScanner.app/Extensions/BarcodeScannerCaptureExtension.appex/BarcodeScannerCaptureExtension`

```diff

 	<array>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.appleneuralengine.private</string>
+		<string>com.apple.CameraOverlayAngel.application-service</string>
 	</array>
 </dict>
 </plist>

```
### Camera

> `/Applications/Camera.app/Camera`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.intents.intents-helper</key>
 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.assetsd.nebulad</string>
 		<string>com.apple.assetsd.keepDaemonAlive</string>

```
### LockScreenCamera

> `/Applications/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.intents.intents-helper</key>
 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.assetsd.nebulad</string>
 		<string>com.apple.assetsd.keepDaemonAlive</string>

```

### 🆕 CameraOverlayAngel

> `/Applications/CameraOverlayAngel.app/CameraOverlayAngel`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.backboardd.touchDeliveryObservation</key>
	<true/>
	<key>com.apple.coremedia.cameraviewfinder</key>
	<true/>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Discoverability.Signals</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.coremedia.cameraviewfinder</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
	</array>
	<key>com.apple.springboard.private.capture-button-full-fidelity-events</key>
	<true/>
</dict>
</plist>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 	<true/>
 	<key>com.apple.BluetoothServices.cloud</key>
 	<true/>
+	<key>com.apple.HearingModeService</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.HearingModeService</string>
 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.accessories.connection-info-server</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	</array>
 	<key>com.apple.NeighborhoodActivityConduitService</key>
 	<true/>
+	<key>com.apple.QuartzCore.display-state</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.QuartzCore.occlusion-override</key>

```
### RemotePeoplePicker

> `/Applications/InCallService.app/PlugIns/RemotePeoplePicker.appex/RemotePeoplePicker`

```diff

 <dict>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.QuartzCore.display-state</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.QuartzCore.display-state</key>
+	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.activitysharingd</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.appstored.install-apps</key>

 		<string>com.apple.surfboard.scenesessionservice</string>
 		<string>com.apple.ProactiveSummarization.server</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.appprotectiond.guard</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobileSafari

> `/Applications/MobileSafari.app/MobileSafari`

```diff

 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.webprivacyd</string>
+		<string>com.apple.trial.status</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

 	<array>
 		<string>342</string>
 	</array>
+	<key>com.apple.trial.status.deployment-environment.allow</key>
+	<array>
+		<integer>2</integer>
+	</array>
 	<key>com.apple.watchlist.private</key>
 	<true/>
 	<key>fairplay-client</key>

```
### PeopleMessageService

> `/Applications/PeopleMessageService.app/PeopleMessageService`

```diff

 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
 	<key>com.apple.trial.client</key>
-	<true/>
+	<array>
+		<string>406</string>
+	</array>
 </dict>
 </plist>
 

```
### PeopleViewService

> `/Applications/PeopleViewService.app/PeopleViewService`

```diff

 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
 	<key>com.apple.trial.client</key>
-	<true/>
+	<array>
+		<string>406</string>
+	</array>
 </dict>
 </plist>
 

```
### ScreenTimeWidgetExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>

```
### ScreenTimeWidgetIntentsExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetIntentsExtension.appex/ScreenTimeWidgetIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.DragUI.presentationUpdateNotification</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>
 	<true/>
+	<key>com.apple.QuartzCore.global-capture</key>
+	<true/>
 	<key>com.apple.RemoteDisplay</key>
 	<true/>
 	<key>com.apple.RemoteDisplay.SessionState</key>
 	<true/>
+	<key>com.apple.accessibility.api</key>
+	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.replicatorservices</string>
+		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.oneness.dragserver</string>
+		<string>com.apple.screencontinuity.dragserver</string>
+	</array>
+	<key>com.apple.security.exception.mach-register.global-name</key>
+	<array>
+		<string>com.apple.oneness.dragserver</string>
+		<string>com.apple.screencontinuity.dragserver</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.ScreenContinuityShell</string>
 		<string>com.apple.applicationaccess</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Accessibility</string>
+	</array>
 	<key>com.apple.springboard.continuitysession</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.chrono.controls</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.coreaudio.CanRecordPastData</key>
 	<true/>
 	<key>com.apple.coreaudio.CanRecordWithoutSessionActivation</key>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.geoanalyticsd.telemetry</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.linkd.extension</string>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.mobilesafarishared</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>path</string>
+		<key>value</key>
+		<string>/Applications/StickerPickerService.app/StickerPickerService</string>
+	</dict>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
 	<key>com.apple.private.avfoundation.capture.allow</key>

```
### AccessibilityControlsExtension

> `/System/Library/CoreServices/AccessibilityUIServer.app/PlugIns/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`

```diff

 		<string>WifiAddressData</string>
 		<string>EthernetMacAddress</string>
 	</array>
-	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.Preferences</string>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```

### 🆕 MobileDevices-0001

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0001.bundle/MobileDevices-0001`

- No entitlements *(yet)*

### 🆕 MobileDevices-0003

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0003.bundle/MobileDevices-0003`

- No entitlements *(yet)*
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.notificationcenter.widgetcontrollerhascontent</key>
 	<true/>
+	<key>com.apple.notifications.logging</key>
+	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
 	<key>com.apple.payment.configuration</key>

```
### AccessibilityControlsExtension

> `/System/Library/ExtensionKit/Extensions/AccessibilityControlsExtension.appex/AccessibilityControlsExtension`

```diff

 		<string>WifiAddressData</string>
 		<string>EthernetMacAddress</string>
 	</array>
-	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.Preferences</string>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```

### 🆕 PasswordManagerAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasswordManagerAppIntentsExtension.appex/PasswordManagerAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
</dict>
</plist>

```

### 🆕 PasswordSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasswordSettingsAppIntentsExtension.appex/PasswordSettingsAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
</dict>
</plist>

```
### PhotosSearchClientLighthouse

> `/System/Library/ExtensionKit/Extensions/PhotosSearchClientLighthouse.appex/PhotosSearchClientLighthouse`

```diff

 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.PegasusConfiguration</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.photos.service</string>
 	</array>
+	<key>com.apple.spotlight.photos.entitledattributes</key>
+	<true/>
 </dict>
 </plist>
 

```
### PrivateMLClientInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService`

```diff

 		<string>com.apple.privatemlclient</string>
 		<string>com.apple.privatecloudcompute</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### eedmediaservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/eedmediaservice.xpc/eedmediaservice`

```diff

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceAcceleratorClient</string>
+		<string>AGXCommandQueue</string>
+		<string>AGXDevice</string>
+		<string>AGXDeviceUserClient</string>
+		<string>AGXSharedUserClient</string>
+		<string>IOAccelContext</string>
+		<string>IOAccelDevice</string>
+		<string>IOAccelSharedUserClient</string>
+		<string>IOAccelSubmitter2</string>
+		<string>IOAccelContext2</string>
+		<string>IOAccelDevice2</string>
+		<string>IOAccelSharedUserClient2</string>
 	</array>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>

```
### CoreSpotlightService

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlightService`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.searchd</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```

### 🆕 TouchSensitiveButtonHIDService

> `/System/Library/HIDPlugins/ServicePlugins/TouchSensitiveButtonHIDService.plugin/TouchSensitiveButtonHIDService`

- No entitlements *(yet)*

### 🆕 TactSwitchHIDSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/TactSwitchHIDSessionFilter.plugin/TactSwitchHIDSessionFilter`

- No entitlements *(yet)*

### 🆕 NTKAtiumFaceBundleCompanion

> `/System/Library/NanoTimeKit/FaceBundles/NTKAtiumFaceBundleCompanion.bundle/NTKAtiumFaceBundleCompanion`

- No entitlements *(yet)*

### 🆕 NTKDolomiteFaceBundleCompanion

> `/System/Library/NanoTimeKit/FaceBundles/NTKDolomiteFaceBundleCompanion.bundle/NTKDolomiteFaceBundleCompanion`

- No entitlements *(yet)*

### 🆕 NTKSquallFaceBundleCompanion

> `/System/Library/NanoTimeKit/FaceBundles/NTKSquallFaceBundleCompanion.bundle/NTKSquallFaceBundleCompanion`

- No entitlements *(yet)*
### motiontrackingd

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Support/motiontrackingd`

```diff

 		<string>com.apple.coremedia.mediaplaybackd.formatreader.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.remaker.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.sandboxserver.xpc</string>
+		<string>com.apple.systemstatus.activityattribution</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.ts.opengl-or-metal</key>
 	<true/>
+	<key>com.apple.systemstatus.activityattribution</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### AppleDeviceQueryService

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`

```diff

 	<true/>
 	<key>com.apple.afk.user</key>
 	<true/>
+	<key>com.apple.aop.user-client.full-access</key>
+	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>1720</string>
 		<string>1721</string>
 		<string>1740</string>
+		<string>1890</string>
 		<string>200</string>
 		<string>322</string>
 		<string>401</string>

 		<string>SIRI_MESSAGES_APP_SELECTION</string>
 		<string>SIRI_NETWORK_ENABLEMENT</string>
 		<string>SIRI_PIRENE_FEATURE_FLAGS</string>
+		<string>SIRI_PLAYBACK_CONTROLS_TAPTORADAR_CONFIGURATION</string>
 		<string>SIRI_PRIVATE_LEARNING_SUGGESTIONS_MEDIA</string>
 		<string>SIRI_PRIVATE_LEARNING_SUGGESTIONS_PLATFORM</string>
 		<string>SIRI_REFERENCE_RESOLUTION_LIGHTHOUSE_PLUGIN</string>

```
### nebulad

> `/System/Library/PrivateFrameworks/CameraUI.framework/Support/nebulad`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>AAPLPHOTOS.com.apple.assetsd.nebulad</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-offline-video-stabilization</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

 	</array>
 	<key>com.apple.springboard.activateawayviewplugins</key>
 	<true/>
+	<key>com.apple.springboard.private.capture-button-app-configuration-service</key>
+	<true/>
 </dict>
 </plist>
 

```
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/Applications/</string>
 		<string>/private/var/mobile/Library/Assistant/</string>
 		<string>/private/var/containers/Bundle/Application/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.siri.uaf.service</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.SiriNaturalLanguageParsing</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>

```
### druid

> `/System/Library/PrivateFrameworks/DragUI.framework/Support/druid`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.oneness.dragserver</string>
+		<string>com.apple.screencontinuity.dragserver</string>
 		<string>com.apple.realitysystemsupport.hid_server_backboard</string>
 		<string>com.apple.realitysimulation.apps</string>
 		<string>com.apple.UIKit.OverlayUI.services</string>

```
### FileProviderDiagnosticExtension

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/PlugIns/FileProviderDiagnosticExtension.appex/FileProviderDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.internal.fileprovider.debug</key>
 	<true/>
+	<key>com.apple.private.fileprovider.read-diagnostic-metadata</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>com.apple.GenerativeFunctions.PeriodicTasks.InstrumentationUpload</key>

 	<array>
 		<string>/Library/Caches/com.apple.GenerativeFunctions.generativeexperiencesd/</string>
 		<string>/Library/AppleIntelligencePlatform/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.private.assistant.settings</string>
+		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>

 		<string>com.apple.sage</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.generativeexperiences.corefollowup</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.ts.asset-access</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 	<true/>
 	<key>com.apple.runningboard.MobileSMS</key>
 	<true/>
+	<key>com.apple.springboard.delete-application-snapshots</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.MobileAccessoryUpdate.haywire</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOHIDLibUserClient</string>
		<string>AppleUSBHostDeviceUserClient</string>
		<string>AppleUSBHostInterfaceUserClient</string>
	</array>
</dict>
</plist>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Support/photoanalysisd`

```diff

 		<string>Photos.Map</string>
 		<string>Photos.Picker</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>Discoverability.Signals</string>
 	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>

 		<string>com.apple.gms.availability</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.mobileslideshow</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 com.apple.printactivityservice

> `/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.printactivityservice.xpc/com.apple.printactivityservice`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CanInheritApplicationStateFromOtherProcesses</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.printing.getjoblist</key>
	<true/>
	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.sessionkit.custom-platter-target</key>
	<true/>
	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
	<true/>
	<key>com.apple.private.sessionkit.sessionRequest</key>
	<true/>
	<key>com.apple.runningboard.primitiveattribute</key>
	<true/>
	<key>com.apple.runningboard.trustedtarget</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.sessionservices</string>
	</array>
</dict>
</plist>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 		<string>Safari.MemoryFootprint</string>
 		<string>Mail.Recategorization</string>
 		<string>Photos.MemoryCreation</string>
-		<string>Photos.Curation</string>
+		<string>Photos.Memories.Curation</string>
 		<string>Photos.Delete</string>
 		<string>Photos.Search</string>
 		<string>Photos.Memories.Shared</string>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 		<string>Safari.MemoryFootprint</string>
 		<string>Mail.Recategorization</string>
 		<string>Photos.MemoryCreation</string>
-		<string>Photos.Curation</string>
+		<string>Photos.Memories.Curation</string>
 		<string>Photos.Delete</string>
 		<string>Photos.Search</string>
 		<string>Photos.Memories.Shared</string>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 		<string>Safari.MemoryFootprint</string>
 		<string>Mail.Recategorization</string>
 		<string>Photos.MemoryCreation</string>
-		<string>Photos.Curation</string>
+		<string>Photos.Memories.Curation</string>
 		<string>Photos.Delete</string>
 		<string>Photos.Search</string>
 		<string>Photos.Memories.Shared</string>

```
### SoftwareUpdateSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber`

```diff

 		<string>com.apple.RemoteManagementAgent.store</string>
 		<string>com.apple.softwareupdateservicesd</string>
 		<string>com.apple.remoted</string>
+		<string>com.apple.seeding.client</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.remotemanagement.SoftwareUpdateSubscriber</string>
 		<string>com.apple.softwareupdateservicesd</string>
+		<string>com.apple.seeding.client</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<array>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 		<string>com.apple.MobileAsset.SpotlightResources</string>
 		<string>com.apple.appprotectiond.read</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>kCFPreferencesAnyApplication</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.DataDeliveryServices</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.businessservicesd.businessmetadata</key>
+	<true/>
 	<key>com.apple.coreaudio.private.HasMicrophoneInjectionAccess</key>
 	<true/>
 	<key>com.apple.coreaudio.private.MicrophoneInjectionCanBypassMicMute</key>

```
### ZhuGeService

> `/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService`

```diff

 	<true/>
 	<key>com.apple.afk.user</key>
 	<true/>
+	<key>com.apple.aop.user-client.full-access</key>
+	<true/>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

```

### 🆕 com.apple.HearingModeUserNotifications

> `/System/Library/UserNotifications/Bundles/com.apple.HearingModeUserNotifications.bundle/com.apple.HearingModeUserNotifications`

- No entitlements *(yet)*

### 🆕 SmartStyleV1

> `/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1`

- No entitlements *(yet)*
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<string></string>
-	<key>com.apple.private.imcore.imdpersistence.database-access</key>
-	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>MapsShareETAFeedback</key>

 		<string>com.apple.Maps.mapspushd.geoservices</string>
 		<string>com.apple.intents.intents-helper</string>
 		<string>com.apple.Maps.xpc.SharedTrip</string>
+		<string>com.apple.Maps.xpc.SharedTrip.Capabilities</string>
 		<string>com.apple.CarPlayApp.service</string>
 		<string>com.apple.siri.activation.service</string>
 		<string>com.apple.maps.virtualgarage.server</string>

```
### RecordWidgetExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/RecordWidgetExtension.appex/RecordWidgetExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.VoiceMemos.RecordWidget</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.VoiceMemos.shared</string>
+	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceMemos.shared</string>

```

### 🆕 modelcatalogdump

> `/usr/bin/modelcatalogdump`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.modelcatalogtool</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.modelcatalogtool</string>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.modelcatalog.ajax</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
</dict>
</plist>

```
### SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>38B8709B-AD36-4257-9247-E94F834BC24A</key>
-	<true/>
 	<key>com.apple.CompanionLink</key>
 	<true/>
 	<key>com.apple.RemoteDisplay</key>

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.arkit.authorization</key>
+	<array>
+		<string>appleDeviceTracking</string>
+	</array>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```
### aonsensed

> `/usr/libexec/aonsensed`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>aop2.gps-data.ent</key>
+	<true/>
+	<key>aop2.gps-debug</key>
+	<true/>
+	<key>com.apple.afk.shmem-user</key>
+	<true/>
+	<key>com.apple.afk.user</key>
+	<true/>
 	<key>com.apple.aonsensed.xpc</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>cma</key>
+		<dict>
+			<key>historical-memory</key>
+			<dict/>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.bluetooth.internal</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.private.corewifi-xpc</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AFKSharedMemoryUserClient</string>
+		<string>RootDomainUserClient</string>
+		<string>AFKMemoryDescriptorManagerUserClient</string>
+		<string>AFKEndpointInterfaceUserClient</string>
+		<string>AppleAOPAudioUserClient</string>
+		<string>IOHIDLibUserClient</string>
+		<string>AppleSPUFastpathDriverUserClient</string>
+	</array>
+	<key>staticregion</key>
+	<true/>
+	<key>trusted.trusted-data</key>
+	<true/>
 </dict>
 </plist>
 

```
### appprotectiond

> `/usr/libexec/appprotectiond`

```diff

 <dict>
 	<key>com.apple.accounts.connectbeforemigrationdidfinish</key>
 	<true/>
+	<key>com.apple.dmd-access</key>
+	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.BackgroundUI</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.dmd.policy</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>

 	<array>
 		<string>com.apple.lsd.appprotection</string>
 		<string>com.apple.containermanagerd.system</string>
+		<string>com.apple.dmd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### asd

> `/usr/libexec/asd`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.replicator.controller</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>asd</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.ScreenContinuityServices</string>
+	</array>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>

```
### asktod

> `/usr/libexec/asktod`

```diff

 		<string>com.apple.iconservices</string>
 		<string>com.apple.iconservices.store</string>
 		<string>com.apple.people.agent</string>
+		<string>com.apple.contactsd</string>
+		<string>com.apple.contactsd.persistence</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.familycircle.agent</string>

 		<string>com.apple.iconservices</string>
 		<string>com.apple.iconservices.store</string>
 		<string>com.apple.people.agent</string>
+		<string>com.apple.contactsd</string>
+		<string>com.apple.contactsd.persistence</string>
 	</array>
 	<key>com.apple.security.ts.identity-services-client</key>
 	<true/>

```

### 🆕 atcrtcomm

> `/usr/libexec/atcrtcomm`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.driver.AppleTypeCRetimer.user-access</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleTypeCRetimerUserClient</string>
	</array>
</dict>
</plist>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 		<string>com.apple.MuteControlUserNotifications</string>
 		<string>com.apple.ShareAudioNotifications</string>
 		<string>com.apple.AudioAccessoryUserNotifications</string>
+		<string>com.apple.HearingModeUserNotifications</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

```
### demod

> `/usr/libexec/demod`

```diff

 <dict>
 	<key>abs-client</key>
 	<string>143531244</string>
+	<key>application-identifier</key>
+	<string>com.apple.msd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.findmydevice-user-agent.access</key>

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
 	<key>com.apple.multitasking.termination</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry</key>

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.InFocus</string>

 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Safari</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.coreduetd.allow</string>
 		<string>com.apple.coreduetd.context</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.gms.availability</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### dockaccessoryd

> `/usr/libexec/dockaccessoryd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access-protected</key>

```
### icloudmailagent

> `/usr/libexec/icloudmailagent`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.icloudmailagent</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.aps-environment</key>
+	<string>production</string>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.icloudmailagent</string>
 	<key>com.apple.mobilemail.mailservices</key>
 	<true/>
+	<key>com.apple.pds.clientid</key>
+	<array>
+		<string>com.apple.aps.icloud.mcc</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.email</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.apsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	<array>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.inputAnalytics.serverStats</string>
+	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.inputanalyticsd</string>
 	<key>com.apple.security.ts.xpc-service-name</key>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.private.screencapturekit.sharingsessionsystemui</key>
 	<true/>
+	<key>com.apple.private.screencapturekit.suppress-screen-indicator</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.replayd</string>

 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.applicationaccess</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.selectivesharing.session_system</key>

```

### 🆕 retimerd

> `/usr/libexec/retimerd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.driver.AppleTypeCRetimer.user-access</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleTypeCRetimerUserClient</string>
	</array>
</dict>
</plist>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	</array>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.HearingModeService</key>
+	<true/>
 	<key>com.apple.MobileInternetSharing.allow</key>
 	<true/>
 	<key>com.apple.PairingManager.HomeKit</key>

 		<string>com.apple.diagnosticextensionsd.sharing-wakeup</string>
 		<string>com.apple.distributed_notifications@Uv3</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.HearingModeService</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.icloud.searchpartyd.accessorydiscoverysession</string>

```

### 🆕 usbctelemetryd

> `/usr/libexec/usbctelemetryd`

- No entitlements *(yet)*
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.chrono.controls</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.countryd.access</key>

```
