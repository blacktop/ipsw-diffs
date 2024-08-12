## 🔑 Entitlements

### AXUIViewService

> `/Applications/AXUIViewService.app/AXUIViewService`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.Accessibility</string>
 		<string>com.apple.Accessibility.GuidedAccess</string>
 		<string>com.apple.Accessibility</string>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 		<string>/Library/MessagesMetaData/NickNameCache/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 		<string>/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/Library/Application Support/com.apple.palette.green.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriDialogAssets</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

```
### ScreenContinuityShell

> `/Applications/ScreenContinuityShell.app/ScreenContinuityShell`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>

 	<true/>
 	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
 	<true/>
+	<key>com.apple.private.sessionkit.presentationAssertionRequester</key>
+	<true/>
+	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>
+	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>

 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.managedconfiguration.profiled</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.ScreenContinuityShell</string>
+		<string>com.apple.applicationaccess</string>
 	</array>
 	<key>com.apple.springboard.continuitysession</key>
 	<true/>

```

### 🆕 BluetoothModule

> `/System/Library/ControlCenter/Bundles/BluetoothModule.bundle/BluetoothModule`

- No entitlements *(yet)*
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.tvos.system-navigation</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.commandandcontrol</string>

```
### ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.SystemConfiguration.SCPreferences-read-access</key>
+	<array>
+		<string>com.apple.radios.plist</string>
+	</array>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

 		<string>com.apple.backboardd</string>
 		<string>com.apple.UIKit</string>
 		<string>com.apple.screensharingserver</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
 		<string>com.apple.MobileSMS</string>
 	</array>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.launchservices.clearadvertisingid</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
 	<key>com.apple.localizationswitcher</key>

 		<string>com.apple.mobile.data_sync/Bookmarks</string>
 		<string>com.apple.mobile.data_sync/Mail Accounts</string>
 	</array>
+	<key>com.apple.private.logging.flush-buffers</key>
+	<true/>
 	<key>com.apple.private.mediaexperience.allowemergencyalertpriority</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.setsilentmode.allow</key>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.Accessibility</string>
+		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.Accessibility.Assets</string>
 		<string>com.apple.VoiceOverTouch</string>
 		<string>com.apple.VoiceOverTouch.activities</string>

```
### ContactViewViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/ContactViewViewService`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
+	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### ContactsViewService

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/ContactsViewService`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```

### 🆕 CoreSpotlightTestImporter

> `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTestImporter.appex/CoreSpotlightTestImporter`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.corespotlight.bundleid</key>
	<string>com.apple.CoreSpotlight.TestImporter</string>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
</dict>
</plist>

```

### 🆕 CoreSpotlightTextImporter

> `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTextImporter.appex/CoreSpotlightTextImporter`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.corespotlight.bundleid</key>
	<string>com.apple.CoreSpotlight.TextImporter</string>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
</dict>
</plist>

```

### 🆕 FinanceImageProcessingService

> `/System/Library/Frameworks/FinanceKit.framework/XPCServices/FinanceImageProcessingService.xpc/FinanceImageProcessingService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.financekit.image-processing</string>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOGPUDeviceUserClient</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXDeviceUserClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
</dict>
</plist>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
-	<key>com.apple.financekit.image-processing.host</key>
+	<key>com.apple.finance.private</key>
 	<true/>
 	<key>com.apple.financekit.maps-insights.host</key>
 	<true/>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>
 	<true/>
+	<key>com.apple.dmd.operation.set-app-allow-user-to-hide</key>
+	<true/>
+	<key>com.apple.dmd.operation.set-app-allow-user-to-lock</key>
+	<true/>
 	<key>com.apple.dmd.operation.set-app-associated-domains</key>
 	<true/>
 	<key>com.apple.dmd.operation.set-app-associated-domains-enable-direct-downloads</key>

```
### PassKitIntentsUIExtension

> `/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitIntentsUIExtension.appex/PassKitIntentsUIExtension`

```diff

 <dict>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.Passbook</string>
+	</dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
-	<key>com.apple.security.exception.iokit-user-client-class</key>
-	<array>
-		<string>RootDomainUserClient</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.xpc.amsengagementd</string>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreAppProtection</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.ignoreRemovability</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.ignoreRestrictions</key>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.dmd.policy</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>ContextRetrieval</key>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
+	<key>com.apple.mkb.usersession.keybagopaquedata</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>MediaAnalysis.PEC.Processing</string>
 		<string>Safari.PageLoad</string>
 		<string>Siri.Health.Federated</string>
 		<string>AppleID.ChildSetup</string>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>MediaAnalysis.PEC.Processing</string>
 		<string>Safari.PageLoad</string>
 		<string>Siri.Health.Federated</string>
 		<string>AppleID.ChildSetup</string>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
+		<string>MediaAnalysis.PEC.Processing</string>
 		<string>Safari.PageLoad</string>
 		<string>Siri.Health.Federated</string>
 		<string>AppleID.ChildSetup</string>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.sender</key>
 	<true/>
+	<key>com.apple.private.corespotlight.skgupdater</key>
+	<true/>
 	<key>com.apple.private.dmd.emergency-mode</key>
 	<true/>
 	<key>com.apple.private.dmd.policy</key>

```
### MagnifierExtension

> `/private/var/staged_system_apps/Magnifier.app/Extensions/MagnifierExtension.appex/MagnifierExtension`

```diff

 		<string>com.apple.CameraOverlayAngel.application-service</string>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.appleneuralengine.private</string>
+		<string>com.apple.pluginkit.pkd</string>
+		<string>com.apple.ax.MauiTTSSupport.MauiAUSP</string>
+		<string>com.apple.ax.MauiTTSSupport.MauiAUSP.apple-extension-service</string>
+		<string>com.apple.texttospeech.SiriAUSP</string>
+		<string>com.apple.texttospeech.SiriAUSP.apple-extension-service</string>
+		<string>com.apple.speech.MacinTalkFramework.MacinTalkAUSP</string>
+		<string>com.apple.speech.MacinTalkFramework.MacinTalkAUSP.apple-extension-service</string>
+		<string>com.apple.ax.KonaTTSSupport.KonaSynthesizer</string>
+		<string>com.apple.ax.KonaTTSSupport.KonaSynthesizer.apple-extension-service</string>
+		<string>com.apple.audio.AudioQueueServer</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.Accessibility.Assets</string>
 		<string>com.apple.Accessibility.Magnifier</string>
 		<string>com.apple.AccessibilityUIServer</string>
+		<string>com.apple.SpeakSelection</string>
 	</array>
 	<key>com.apple.security.ts.ane-client</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
+	<key>com.apple.springboard.private.9403EBFD-90B8-4676-84BF-9F38143337E3</key>
+	<true/>
 	<key>com.apple.springboard.requestDeviceUnlock</key>
 	<true/>
 	<key>platform-application</key>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 	<true/>
 	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
 	<true/>
+	<key>com.apple.springboard.private.9403EBFD-90B8-4676-84BF-9F38143337E3</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### MobileCal

> `/private/var/staged_system_apps/MobileCal.app/MobileCal`

```diff

 	<string>com.apple.mobilecal</string>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.routined.registration</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.remindd</string>
 		<string>com.apple.mobilecal</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```
### CalendarWidgetExtension

> `/private/var/staged_system_apps/MobileCal.app/PlugIns/CalendarWidgetExtension.appex/CalendarWidgetExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<true/>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>
+	<key>com.apple.private.calendar.calendar-widget-extension</key>
+	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.SharedWebCredentials</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.feedbacklogger</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.ind.client</key>

 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.feedbacklogger</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
 	<key>com.apple.nfcd.session.reader.internal</key>

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.WebUI</string>
 	</array>

```
### appprotectiond

> `/usr/libexec/appprotectiond`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accounts.connectbeforemigrationdidfinish</key>
+	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.BackgroundUI</key>

```
### asktod

> `/usr/libexec/asktod`

```diff

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.iconservices</string>
+		<string>com.apple.iconservices.store</string>
 		<string>com.apple.people.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.iconservices</string>
+		<string>com.apple.iconservices.store</string>
 		<string>com.apple.people.agent</string>
 	</array>
 	<key>com.apple.security.ts.identity-services-client</key>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.AirPlayRoutePrediction</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.networkd</string>
+		<string>com.apple.purplebuddy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### photosfaced

> `/usr/libexec/photosfaced`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
+	<key>com.apple.networkrelay.deviceMonitor</key>
+	<true/>
+	<key>com.apple.networkrelay.devices.read</key>
+	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### routined

> `/usr/libexec/routined`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.lockscreen.shared</string>
 		<string>com.apple.momentsd</string>
 		<string>com.apple.duetexpertd</string>
 	</array>

```
