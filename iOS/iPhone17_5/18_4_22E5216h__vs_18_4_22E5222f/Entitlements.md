## 🔑 Entitlements

### CarPlaySettings

> `/Applications/CarPlaySettings.app/CarPlaySettings`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.CarAssetUtils.variants</key>
+	<true/>
 	<key>com.apple.private.CarPlayServices.icon-layout</key>
 	<true/>
 	<key>com.apple.private.CarPlayUIServices.cluster-theme</key>

 		<string>com.apple.CarPlayApp.punch-through-service</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.CarPlayApp.cluster-theme-service</string>
+		<string>com.apple.CarAssetUtils.variants</string>
 		<string>com.apple.CarPlayApp.service</string>
 		<string>com.apple.CarPlayApp.status-bar-service</string>
 		<string>com.apple.carkit.service</string>

```
### PASViewService

> `/Applications/PASViewService.app/PASViewService`

```diff

 			<key>viewControllerClassName</key>
 			<string>PASViewService.PASVSPrimaryViewController</string>
 		</dict>
+		<key>AppleIDSignInFamily</key>
+		<dict>
+			<key>bleRSSIThresholdHint</key>
+			<integer>-45</integer>
+			<key>discoveryTypes</key>
+			<array>
+				<string>AppleIDSignInFamily</string>
+			</array>
+			<key>limitToDeviceClasses</key>
+			<array>
+				<string>iPad</string>
+				<string>iPhone</string>
+			</array>
+			<key>viewControllerClassName</key>
+			<string>PASViewService.PASVSPrimaryViewController</string>
+		</dict>
 	</dict>
 	<key>com.apple.bluetooth.system</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.screentime-setup</key>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.keystore.device.verify</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.set</key>
+	<array>
+		<string>Passcode</string>
+		<string>UserSettings</string>
+	</array>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.keystore.device.verify</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.set</key>
+	<array>
+		<string>Passcode</string>
+		<string>UserSettings</string>
+	</array>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
+	<key>com.apple.private.screentime-setup</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

```
### AccessibilityAppIntents

> `/System/Library/CoreServices/AccessibilityUIServer.app/Extensions/AccessibilityAppIntents.appex/AccessibilityAppIntents`

```diff

 <dict>
 	<key>com.apple.accessibility.AccessibilityUIServer</key>
 	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.accessibility.entitled.guidedaccess.enable</key>

```

### 🆕 MobileDevices-0002

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`

- No entitlements *(yet)*
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.chrono.controls</key>
 	<true/>
+	<key>com.apple.chrono.descriptorEnablement</key>
+	<array>
+		<string>com.apple.siri.TypeToSiriWidget</string>
+	</array>
 	<key>com.apple.chronod.toolservices</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

```
### ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension`

```diff

 	<string>com_apple_driver_FairPlayIOKitUserClient</string>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.xpc.amstoold</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
+	</array>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```
### com.apple.mlhost.CloudWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/com.apple.mlhost.CloudWorker`

```diff

 	<true/>
 	<key>com.apple.private.mlhost.taskWrite</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mlhostd.xpc</string>

 	<array>
 		<string>com.apple.mlhost</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mlhostd.xpc</string>

```
### com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/com.apple.mlhost.SampleWorker`

```diff

 	<true/>
 	<key>com.apple.private.mlhost.dictionaryWrite</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mlhostd.xpc</string>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```
### ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>OOPCocoa</string>
 	<key>com.apple.private.memory.ownership_transfer</key>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.GAX.SPI</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.app-distribution.private</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.adid</string>
+		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.appinstallationmetrics.xpc</string>
 		<string>com.apple.AssetCacheLocatorService</string>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 	<array>
 		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.apsd</string>
+		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.mobileactivationd</string>

```
### ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

```diff

 <dict>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.coreml.decypt_allowed</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>/Library/Caches/com.apple.pommes/</string>
 		<string>/Library/Caches/com.apple.siri.bundleservicecache.plist</string>
 		<string>/Library/Caches/com.apple.siri.conversationhandlercache.plist</string>
+		<string>/Library/Caches/com.apple.siri.transformationplugincache.plist</string>
 		<string>/Library/Caches/com.apple.speech.localspeechrecognition/lsr_audio_dumps/</string>
 		<string>/Library/Caches/CoreSpeech/</string>
 		<string>/Library/Caches/GeoServices/</string>

```
### parsec-fbf

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf`

```diff

 	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
+	<key>com.apple.private.osanalytics.cleanup-logs.allow</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.PegasusConfiguration</string>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>EventEntityExtraction</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.Intents.ExtractedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>ProactiveSummarization</key>
 		<dict>
 			<key>Streams</key>

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 		<string>com.apple.amsondevicestoraged</string>
 		<string>com.apple.AppleMediaServices.notbackedup</string>
 		<string>com.apple.AppleMediaServices</string>
+		<string>com.apple.itunesstored</string>
 		<string>com.apple.OnDeviceStorage</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.ts.system-tmpdir</key>
+	<string>com.apple.amsondevicestoraged</string>
 	<key>com.apple.security.ts.tmpdir</key>
-	<string>com.apple.OnDeviceStorage</string>
+	<string>com.apple.amsondevicestoraged</string>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceFinancialData</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

```
### PromotedContentJetService

> `/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/XPCServices/PromotedContentJetService.xpc/PromotedContentJetService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.runningboard.jetengine</key>

 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 		<string>/Library/Caches/com.apple.ap.PromotedContentJetService/</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.itunesstored</string>

```
### fitcored

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored`

```diff

 	<array>
 		<string>Library/Seymour/</string>
 		<string>Library/Caches/com.apple.fitcored/</string>
-		<string>/tmp</string>
+		<string>tmp</string>
 		<string>Media/</string>
 		<string>Library/Preferences/</string>
 		<string>Library/Cookies/</string>

```
### fitcoresessiond

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcoresessiond`

```diff

 		<string>/private/var/mobile/Library/Preferences/com.apple.fitcored.session.plist</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.AppSupport.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>Library/Preferences/</string>
+		<string>Library/Seymour/</string>
+		<string>tmp</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.seymour</string>

```
### AppleVisionProApp

> `/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp`

```diff

 	<key>application-identifier</key>
 	<string>com.apple.visionproapp</string>
 	<key>aps-environment</key>
-	<string>development</string>
+	<string>production</string>
 	<key>com.apple.authkit.client</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

```
### MailQuickLookExtension

> `/private/var/staged_system_apps/MobileMail.app/PlugIns/MailQuickLookExtension.appex/MailQuickLookExtension`

```diff

 	<string>com.apple.mobilemail.MailQuickLookExtension</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.businessservicesd.businessmetadata</key>
+	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
+	<key>com.apple.icloudmailagent.secret.xpc</key>
+	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
 	<key>com.apple.private.networkserviceproxy</key>

 	<array>
 		<string>group.com.apple.mail</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Caches/com.apple.businessservicesd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.PointerUI.pointeruid.service</string>

 		<string>com.apple.networkserviceproxy</string>
 		<string>com.apple.tccd</string>
 		<string>com.apple.WebKit.GPU</string>
+		<string>com.apple.icloudmailagent.secret.xpc</string>
+		<string>com.apple.businessservicesd</string>
+		<string>com.apple.quicklook.ThumbnailsAgent</string>
 	</array>
 </dict>
 </plist>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
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
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

 	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
 	<true/>
-	<key>com.apple.sage.summarization</key>
-	<true/>
-	<key>com.apple.sage.textcomposition</key>
-	<true/>
 	<key>com.apple.screenshotservices.ssuiservice.showscreenshotui</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.identityservicesd.pds</string>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.rtcreportingd</string>
 		<string>com.apple.dprivacyd</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
-		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.sharingd.nsxpc</string>
 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.spotlight.SearchAgent</string>
-		<string>com.apple.sage.summarization</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.tipsd</string>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<array>
 		<string>UIInstallation</string>
 	</array>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
 	<key>com.apple.multitasking.systemappassertions</key>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.keystore.device.verify</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.set</key>
+	<array>
+		<string>Passcode</string>
+		<string>UserSettings</string>
+	</array>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 		<string>/Library/NanoMusicSync/</string>
 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 		<string>/Media/ContentKeys/</string>
+		<string>/Media/iTunes_Control/Music/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### TipsQuicklook

> `/private/var/staged_system_apps/Tips.app/PlugIns/TipsQuicklook.appex/TipsQuicklook`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.tips.TipsQuicklookExtension</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>
 	<true/>
+	<key>com.apple.private.mobilestoredemo.enabledemo</key>
+	<array>
+		<string>Manage</string>
+	</array>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.powersource-read</key>

```
### aned

> `/usr/libexec/aned`

```diff

 	<true/>
 	<key>com.apple.ane.iokit-user-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.ANEStorageMaintainer.allow</key>
 	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>

```
### caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

 	<true/>
 	<key>com.apple.runningboard.caraccessoryd</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.CarPlayApp.cluster-theme-service</string>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<array>
 		<string>/Library/DuetActivityScheduler/</string>
 		<string>/Library/Logs/CrashReporter/</string>
+		<string>/Library/Trial/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>COREOS_DAS</string>
-		<string>252</string>
+		<string>COREOS_APRS</string>
+		<string>COREOS_CLAS</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### demod

> `/usr/libexec/demod`

```diff

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.ignoreRestrictions</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.deleteContainerContent</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.findmy</string>
+		<string>com.apple.FindMySafetyAlertsNotifications</string>
 	</array>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>

```
### milod

> `/usr/libexec/milod`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MiloLimitedUsageIndicators</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>HomeKit.Client.AccessoryControl</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
 	<string></string>
 	<key>com.apple.rapport.Client</key>

```
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.nsurlsessiond</string>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.carousel.defaulturlsessionpolicy</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

```
### visioncompaniond

> `/usr/libexec/visioncompaniond`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.visionproapp</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_SoftwareUpdateDocumentation/</string>

 		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.softwareupdateservicesd</string>
+		<string>com.apple.usernotifications.listener</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.CloudKit</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<array>
 		<string>com.apple.driver.driverkit.serial</string>
 		<string>com.apple.IOUserBluetoothSerialDriver</string>
+		<string>com.apple.AppleSunriseBluetooth</string>
 	</array>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/usr/sbin/BTLEServer/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/log/CoreCapture/com.apple.KalBluetooth_driver/FwLogs/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
