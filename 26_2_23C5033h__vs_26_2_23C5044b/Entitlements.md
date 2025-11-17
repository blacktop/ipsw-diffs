## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<dict>
 		<key>document-types</key>
 		<array>
+			<string>jp-national-id-card</string>
+			<string>photo-id</string>
 			<string>us-drivers-license</string>
 		</array>
 		<key>elements</key>
 		<array>
+			<string>age</string>
 			<string>given-name</string>
 			<string>family-name</string>
 			<string>address</string>

 	</dict>
 	<key>com.apple.developer.in-app-identity-presentment.merchant-identifiers</key>
 	<array>
+		<string>com.apple.ams-identity-verification</string>
 		<string>com.apple.asa-identity-verification</string>
 	</array>
 	<key>com.apple.developer.pass-type-identifiers</key>

```
### AccessibilityReader_iOS

> `/Applications/AccessibilityReader_iOS.app/AccessibilityReader_iOS`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.accessibility.AccessibilityPersonalVoiceUsageOverride</key>
+	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.developer.user-fonts</key>

```
### AppDistributionLaunchAngel

> `/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
 	<key>com.apple.payment.card-on-file</key>

```
### AppleIDSetupUIService

> `/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.coreidvd.digital-presentment.firstpartyclient</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.in-app-identity-presentment</key>
+	<dict>
+		<key>document-types</key>
+		<array>
+			<string>jp-national-id-card</string>
+			<string>photo-id</string>
+			<string>us-drivers-license</string>
+		</array>
+		<key>elements</key>
+		<array>
+			<string>age</string>
+			<string>given-name</string>
+			<string>family-name</string>
+			<string>address</string>
+			<string>issuing-authority</string>
+			<string>document-expiration-date</string>
+			<string>document-issue-date</string>
+			<string>document-number</string>
+			<string>driving-privileges</string>
+			<string>date-of-birth</string>
+		</array>
+	</dict>
+	<key>com.apple.developer.in-app-identity-presentment.merchant-identifiers</key>
+	<array>
+		<string>com.apple.ams-identity-verification</string>
+	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboard.systemappservices</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
+	<key>com.apple.mkb.usersession.keybagopaquedata</key>
+	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	</array>
 	<key>com.apple.clarityboard.inCallPresentation</key>
 	<true/>
+	<key>com.apple.communicationtrustd</key>
+	<array>
+		<string>read</string>
+	</array>
 	<key>com.apple.coreaudio.CanTapTelephony</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.publisher.service.user</string>
+		<string>com.apple.communicationtrustd.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.remindd.userInteractive</string>
+		<string>com.apple.sharingd.pairedcontactmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### PASViewService

> `/Applications/PASViewService.app/PASViewService`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.coreidvd.digital-presentment.firstpartyclient</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.in-app-identity-presentment</key>
+	<dict>
+		<key>document-types</key>
+		<array>
+			<string>jp-national-id-card</string>
+			<string>photo-id</string>
+			<string>us-drivers-license</string>
+		</array>
+		<key>elements</key>
+		<array>
+			<string>age</string>
+			<string>given-name</string>
+			<string>family-name</string>
+			<string>address</string>
+			<string>issuing-authority</string>
+			<string>document-expiration-date</string>
+			<string>document-issue-date</string>
+			<string>document-number</string>
+			<string>driving-privileges</string>
+			<string>date-of-birth</string>
+		</array>
+	</dict>
+	<key>com.apple.developer.in-app-identity-presentment.merchant-identifiers</key>
+	<array>
+		<string>com.apple.ams-identity-verification</string>
+	</array>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<dict>
 		<key>document-types</key>
 		<array>
+			<string>jp-national-id-card</string>
+			<string>photo-id</string>
 			<string>us-drivers-license</string>
 		</array>
 		<key>elements</key>
 		<array>
+			<string>age</string>
 			<string>given-name</string>
 			<string>family-name</string>
 			<string>address</string>

 	</dict>
 	<key>com.apple.developer.in-app-identity-presentment.merchant-identifiers</key>
 	<array>
+		<string>com.apple.ams-identity-verification</string>
 		<string>com.apple.asa-identity-verification</string>
 	</array>
 	<key>com.apple.developer.networking.wifi-info</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.fetchNewestPolicies</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.setInput</key>
 	<true/>
 	<key>com.apple.private.feedbacklogger</key>

```

### 🆕 SystemVoiceAssistant

> `/Applications/SystemVoiceAssistant.app/SystemVoiceAssistant`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.assistantkeyworddetector.xpc</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboard.shutdown</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled-access</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.Storage</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.Storage.Preboard</key>
	<true/>
	<key>com.apple.private.activitykit.canBypassActivityCountLimits</key>
	<true/>
	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
	<true/>
	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.private.launchservices.changedefaulthandlers</key>
	<array>
		<string>com.apple.default-app.assistant</string>
		<string>com.apple.default-app.side-button</string>
	</array>
	<key>com.apple.private.mediaexperience.allowrecordingtemporarily</key>
	<true/>
	<key>com.apple.private.mediaexperience.allowvoiprecording</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.sessionkit.custom-platter-target</key>
	<true/>
	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>
	<true/>
	<key>com.apple.private.sessionkit.sessionRequest</key>
	<true/>
	<key>com.apple.private.tcc.events.subscriber</key>
	<true/>
	<key>com.apple.private.tcc.manager.access.read</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.runningboard.assertions.angeltarget</key>
	<true/>
	<key>com.apple.runningboard.assertions.systemvoiceassistant</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.runningboard.systemvoiceassistant</key>
	<true/>
	<key>com.apple.runningboard.terminatemanagedprocesses</key>
	<true/>
	<key>com.apple.runningboard.terminateprocess</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/containers/Bundle/</string>
		<string>/private/var/db/MobileIdentityData/</string>
		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
		<string>/private/var/mobile/Library/UserConfigurationProfiles/</string>
		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.sessionservices</string>
		<string>com.apple.SBUserNotification</string>
		<string>com.apple.assistant.domain.keyworddetector.speech.service</string>
		<string>com.apple.assistant.domain.keyworddetector.service</string>
		<string>com.apple.corefollowup.agent</string>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.tccd</string>
		<string>com.apple.lsd.modifydb</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.assistant.domain.preferences</string>
		<string>com.apple.assistant.domain.preferences.notBackedUp</string>
		<string>com.apple.assistant.domain.preferences.changeLog</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>kern.exclaves_status</string>
	</array>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
</dict>
</plist>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.coreaudio.private.HasMicrophoneInjectionAccess</key>
 	<true/>
+	<key>com.apple.coreaudio.private.MicrophoneInjectionCanBypassMicMute</key>
+	<true/>
 	<key>com.apple.coreaudio.private.SystemWideTap</key>
 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>

```
### AegirProxyApp

> `/System/Library/CoreServices/AegirProxyApp.app/AegirProxyApp`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.NanoUniverse.AegirProxyApp</string>
+	<key>com.apple.developer.app-management-domain</key>
+	<string>com.apple.Posters</string>
+	<key>com.apple.developer.not-executable</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	</dict>
 	<key>com.apple.private.data-usage-classification-override</key>
 	<string>app</string>
+	<key>com.apple.private.security.no-container</key>
+	<true/>
+	<key>com.apple.private.security.system-application</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.location</key>
 	<true/>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 AegirPoster

> `/System/Library/CoreServices/AegirProxyApp.app/Extensions/AegirPoster.appex/AegirPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.locationd.prompt_from_background</key>
	<true/>
	<key>com.apple.locationd.slc_configurer</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.NanoUniverse.AegirProxyApp.AegirPoster</string>
	</array>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```
### ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

 	<true/>
 	<key>com.apple.private.analyticsqueryvalue</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.ReportCrash</string>
 	<key>com.apple.private.biome.read-write</key>

```
### ShortcutsTopHitsExtension

> `/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.CallHistory.sync.allow</key>
+	<key>com.apple.callhistoryd.service</key>
 	<true/>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
-	<key>com.apple.private.CallHistory.read</key>
-	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/ActionKit.framework</string>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
-	<key>com.apple.private.security.storage.CallHistory</key>
-	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 	<array>
 		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/CallHistoryDB/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.CallHistorySyncHelper</string>
+		<string>com.apple.callhistoryd.service</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.contactsd.support</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	</array>
 	<key>com.apple.private.game-center.bypass-authentication</key>
 	<true/>
+	<key>com.apple.private.graphics-restart-no-kill</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.feature-availability.read</key>

```
### osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

 		<string>UniqueDeviceID</string>
 		<string>SerialNumber</string>
 	</array>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.osanalyticshelper</string>
 	<key>com.apple.private.biome.read-only</key>

 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>AppleCredentialManagerUserClient</string>
 		<string>ApplePMGRUserClient</string>
 		<string>AppleSoCMiscUserClient</string>
 	</array>

```
### ADAskForExceptionExtension

> `/System/Library/ExtensionKit/Extensions/ADAskForExceptionExtension.appex/ADAskForExceptionExtension`

```diff

 <dict>
 	<key>com.apple.app-distribution.private</key>
 	<true/>
-	<key>com.apple.itunesstored.private</key>
-	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.asktod</string>
 		<string>com.apple.managedappdistributiond.xpc</string>

```

### 🆕 SideButtonSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SideButtonSettingsAppIntentsExtension.appex/SideButtonSettingsAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.assistant.domain.system.settings.access</key>
	<true/>
	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.assistant.domain.system.settings.service</string>
	</array>
</dict>
</plist>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 		<string>com.apple.backgroundassets</string>
 		<string>com.apple.gamecenter</string>
 		<string>com.apple.VideoSubscriberAccount</string>
+		<string>com.apple.managedappdistributiond</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### AMSFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/PlugIns/AMSFollowUpExtension.appex/AMSFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.coreidvd.digital-presentment.firstpartyclient</key>
+	<true/>
 	<key>com.apple.coreidvd.document-upload</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.in-app-identity-presentment</key>
+	<dict>
+		<key>document-types</key>
+		<array>
+			<string>jp-national-id-card</string>
+			<string>photo-id</string>
+			<string>us-drivers-license</string>
+		</array>
+		<key>elements</key>
+		<array>
+			<string>age</string>
+			<string>given-name</string>
+			<string>family-name</string>
+			<string>address</string>
+			<string>issuing-authority</string>
+			<string>document-expiration-date</string>
+			<string>document-issue-date</string>
+			<string>document-number</string>
+			<string>driving-privileges</string>
+			<string>date-of-birth</string>
+		</array>
+	</dict>
+	<key>com.apple.developer.in-app-identity-presentment.merchant-identifiers</key>
+	<array>
+		<string>com.apple.ams-identity-verification</string>
+		<string>com.apple.asa-identity-verification</string>
+	</array>
 	<key>com.apple.developer.pass-type-identifiers</key>
 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>

```
### AMSEngagementViewExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/AMSEngagementViewExtension.appex/AMSEngagementViewExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
 		<string>com.apple.appstored.xpc</string>

```
### bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

```diff

 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### featureaccessd

> `/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/featureaccessd`

```diff

 		<string>com.apple.CloudSubscriptionFeatures.waitlist</string>
 		<string>com.apple.icloud.gm</string>
 		<string>com.apple.gms.availability</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### jetpackassetd

> `/System/Library/PrivateFrameworks/JetCore.framework/Support/jetpackassetd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>development</string>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DoNotDisturb</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

```
### NanoMediaDiagnosticExtension

> `/System/Library/PrivateFrameworks/NanoMusicSync.framework/PlugIns/NanoMediaDiagnosticExtension.appex/NanoMediaDiagnosticExtension`

```diff

 		<string>/Library/Logs/MediaServices/HTTPArchives/</string>
 		<string>/Library/Preferences/com.apple.NanoMusicSync.plist</string>
 		<string>/Media/iTunes_Control/iTunes/</string>
+		<string>/tmp/</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-only</key>
 	<array>

```
### com.apple.ReminderKitUI.ReminderCreationViewService

> `/System/Library/PrivateFrameworks/ReminderKitUI.framework/PlugIns/com.apple.ReminderKitUI.ReminderCreationViewService.appex/com.apple.ReminderKitUI.ReminderCreationViewService`

```diff

 	</array>
 	<key>com.apple.locationd.prompt_behavior</key>
 	<true/>
+	<key>com.apple.private.alarmkit.bundleIdentifier</key>
+	<string>com.apple.reminders</string>
 	<key>com.apple.private.cloudkit.customAccounts</key>
 	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>

```
### KonaSynthesizer

> `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/PlugIns/KonaSynthesizer.appex/KonaSynthesizer`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accessibility.voices</string>
 		<string>com.apple.audio.AudioConverterService</string>
 		<string>com.apple.logd</string>
 		<string>com.apple.system.notification_center</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accessibility.voices</string>
 		<string>com.apple.audio.AudioConverterService</string>
 		<string>com.apple.logd</string>
 		<string>com.apple.system.notification_center</string>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
-	<key>com.apple.CallHistory.sync.allow</key>
-	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>cellular-plan</string>

 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.callhistoryd.service</key>
+	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.chrono.controls</key>

 	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
-	<key>com.apple.private.CallHistory.read</key>
-	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.deleteContainerContent</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>siriactionsd</string>
-	<key>com.apple.private.security.storage.CallHistory</key>
-	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.security.storage.triald</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
-		<string>/Library/CallHistoryDB/</string>
 		<string>/Library/Shortcuts/</string>
 		<string>/Library/Shortcuts/ssh/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.NPKCompanionAgent.Server</string>
 		<string>com.apple.NPKCompanionAgent.library</string>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.biomesyncd.sync</string>
+		<string>com.apple.callhistoryd.service</string>
 		<string>com.apple.chrono.widgetcenterconnection</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

```
### matd

> `/System/Library/PrivateFrameworks/WelcomeKit.framework/matd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.WorkflowKit.BackgroundShortcutRunner</string>
-	<key>com.apple.CallHistory.sync.allow</key>
-	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>cellular-plan</string>

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.callhistoryd.service</key>
+	<true/>
 	<key>com.apple.chrono.controls</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 	<true/>
 	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
 	<true/>
-	<key>com.apple.private.CallHistory.read</key>
-	<true/>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>BackgroundShortcutRunner</string>
-	<key>com.apple.private.security.storage.CallHistory</key>
-	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.announce/</string>
-		<string>/Library/CallHistoryDB/</string>
 		<string>/Library/Cookies/</string>
 		<string>/Library/HTTPStorages/</string>
 		<string>/Library/WebKit/com.apple.WorkflowKit.BackgroundShortcutRunner/</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.CARenderServer</string>
-		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MapKit.SnapshotService</string>
 		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.calaccessd</string>
+		<string>com.apple.callhistoryd.service</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.contactsd</string>

```

### 🆕 SideButtonSettings

> `/System/Library/Settings/SideButtonSettings.settings/SideButtonSettings`

- No entitlements *(yet)*
### MobileCal

> `/private/var/staged_system_apps/MobileCal.app/MobileCal`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.alarmkit.bundleIdentifier</key>
+	<string>com.apple.reminders</string>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>

 	<true/>
 	<key>com.apple.private.emergency-mode</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.AppStore</string>
+	</dict>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.lightsourcesupport.lightstate</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.surfboard.applicationservice</string>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 		<string>group.com.apple.tipsnext</string>
 		<string>group.com.apple.sports</string>
 		<string>group.com.apple.safari</string>
+		<string>group.com.apple.BrowserKit</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

 		<string>com.apple.suggestions</string>
 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.BrowserKit</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<string>com.apple.Music</string>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
+	<key>com.apple.developer.wireless-insights.service-predictions</key>
+	<true/>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.ak.privateemail.xpc</string>
+		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### RemindersSharingExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension`

```diff

 	</array>
 	<key>com.apple.locationd.prompt_behavior</key>
 	<true/>
+	<key>com.apple.private.alarmkit.bundleIdentifier</key>
+	<string>com.apple.reminders</string>
 	<key>com.apple.private.avfoundation.capture.allow</key>
 	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>

```
### BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DoNotDisturb</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

```
### FinishRestoreFromBackup

> `/usr/libexec/FinishRestoreFromBackup`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DoNotDisturb</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

```
### appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

 	<array>
 		<string>/private/var/mobile/</string>
 		<string>/Library/Preferences/com.apple.networkd.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### asktod

> `/usr/libexec/asktod`

```diff

 		<string>com.apple.contactsd.persistence</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.family.ageRange.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### continuitycaptured

> `/usr/libexec/continuitycaptured`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.mediaremote.active-system-endpoint-assertion</key>
+	<true/>
 	<key>com.apple.mediaremote.device-info</key>
 	<true/>
 	<key>com.apple.mediaremote.group-sessions</key>

```
