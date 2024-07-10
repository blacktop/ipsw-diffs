## 🔑 Entitlements

### App Store

> `/System/Applications/App Store.app/Contents/MacOS/App Store`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 	</array>
-	<key>com.apple.private.tcc.allow-prompting</key>
-	<array>
-		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
-	</array>
-	<key>com.apple.runningboard.jetengine</key>
-	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.device.camera</key>

```
### Books

> `/System/Applications/Books.app/Contents/MacOS/Books`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>
 	<true/>
+	<key>com.apple.coreduetd.allow</key>
+	<true/>
+	<key>com.apple.coreduetd.context</key>
+	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
 	<key>com.apple.developer.ClassKit-environment</key>

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.private.tipsd.discoverability</key>
+	<true/>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.backupd</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.appstored.xpc.updates</string>
+		<string>com.apple.tipsd</string>
+		<string>com.apple.coreduetd.context</string>
+		<string>com.apple.coreduetd</string>
+		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.UIKit.ShareUI.apple-extension-service</string>
 		<string>com.apple.UIKit.ShareUI.viewservice</string>
 		<string>com.apple.absd</string>

```
### GenerativePlaygroundAppIntents

> `/System/Applications/Image Playground.app/Contents/Extensions/GenerativePlaygroundAppIntents.appex/Contents/MacOS/GenerativePlaygroundAppIntents`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
-	<dict>
-		<key>type</key>
-		<string>bundleID</string>
-		<key>value</key>
-		<string>com.apple.GenerativePlaygroundApp</string>
-	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

```
### GenerativePlaygroundMessagesAppExtension

> `/System/Applications/Image Playground.app/Contents/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/Contents/MacOS/GenerativePlaygroundMessagesAppExtension`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
-	<dict>
-		<key>type</key>
-		<string>bundleID</string>
-		<key>value</key>
-		<string>com.apple.GenerativePlaygroundApp</string>
-	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

```
### Mail

> `/System/Applications/Mail.app/Contents/MacOS/Mail`

```diff

 	<true/>
 	<key>com.apple.private.familycontrols</key>
 	<true/>
-	<key>com.apple.private.feedback.drafting</key>
-	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.awdd</string>
 		<string>com.apple.coreduetd</string>

 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mail-shared</string>
-		<string>com.apple.onetimepasscodes</string>
 	</array>
 	<key>com.apple.spotlight.scopes</key>
 	<array>

```
### Messages Reply Extension

> `/System/Applications/Messages.app/Contents/PlugIns/Messages Reply Extension.appex/Contents/MacOS/Messages Reply Extension`

```diff

 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.iChat.inputLine</string>
-		<string>com.apple.messages</string>
 	</array>
 	<key>com.apple.sharesheet.recipients</key>
 	<true/>

```
### Messages Share Extension

> `/System/Applications/Messages.app/Contents/PlugIns/Messages Share Extension.appex/Contents/MacOS/Messages Share Extension`

```diff

 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.iChat.inputLine</string>
-		<string>com.apple.messages</string>
 	</array>
 	<key>com.apple.sharesheet.recipients</key>
 	<true/>

```
### Photos

> `/System/Applications/Photos.app/Contents/MacOS/Photos`

```diff

 		<string>com.apple.MobileAsset.VideoAppsMusicAssets3</string>
 		<string>com.apple.MobileAsset.MediaSupport</string>
 		<string>com.apple.MobileAsset.PhotosCuratedMusicLibraryAsset</string>
-		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>com.apple.OmniSearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
-		<string>com.apple.UnifiedAssetFramework</string>
-		<string>com.apple.modelcatalog.ajax</string>
 	</array>
 	<key>com.apple.security.files.bookmarks.app-scope</key>
 	<true/>

 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/AppleInternal/Library/Bundles/</string>
-		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
-		<string>/System/Library/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
-		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_Photos_MagicCleanup/purpose_auto/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
-		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_Photos_MagicCleanup/purpose_auto/</string>
-		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_Photos_MagicCleanup/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Application Support/Print Products/</string>
 		<string>/Library/Trial/NamespaceDescriptors/experiment/</string>
-		<string>/Library/UnifiedAssetFramework/</string>
-		<string>/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
-		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.siri.uaf.service</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### Podcasts

> `/System/Applications/Podcasts.app/Contents/MacOS/Podcasts`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>243LU875E5.groups.com.apple.podcasts</string>
-	</array>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

```
### MacPodcastsStorageExtension

> `/System/Applications/Podcasts.app/Contents/PlugIns/MacPodcastsStorageExtension.appex/Contents/MacOS/MacPodcastsStorageExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>243LU875E5.groups.com.apple.podcasts</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### MacQuicklookExtension

> `/System/Applications/Podcasts.app/Contents/PlugIns/MacQuicklookExtension.appex/Contents/MacOS/MacQuicklookExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>243LU875E5.groups.com.apple.podcasts</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### PodcastsNotificationExtension

> `/System/Applications/Podcasts.app/Contents/PlugIns/PodcastsNotificationExtension.appex/Contents/MacOS/PodcastsNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>243LU875E5.groups.com.apple.podcasts</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### PodcastsWidget

> `/System/Applications/Podcasts.app/Contents/PlugIns/PodcastsWidget.appex/Contents/MacOS/PodcastsWidget`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>243LU875E5.groups.com.apple.podcasts</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### com.apple.podcasts.SpotlightIndexExtension

> `/System/Applications/Podcasts.app/Contents/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/Contents/MacOS/com.apple.podcasts.SpotlightIndexExtension`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>243LU875E5.groups.com.apple.podcasts</string>
-	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### Safari

> `/System/Applications/Safari.app/Contents/MacOS/Safari`

```diff

 	<true/>
 	<key>com.apple.dock.add-item</key>
 	<true/>
-	<key>com.apple.duet.activityscheduler.allow</key>
-	<true/>
 	<key>com.apple.features.all-access</key>
 	<true/>
 	<key>com.apple.finance.private</key>

 	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
-	<key>com.apple.private.parsec.default-client</key>
-	<string>com.apple.Safari</string>
 	<key>com.apple.private.rsr-cryptex-access</key>
 	<true/>
 	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>

 		<string>com.apple.email.maild</string>
 		<string>com.apple.translationd</string>
 		<string>com.apple.cdp.daemon</string>
-		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.coreservices.lsbestappsuggestionmanager.xpc</string>
 		<string>com.apple.suggestd.urls</string>
 		<string>com.apple.security.octagon</string>

```
### Feedback Assistant

> `/System/Library/CoreServices/Applications/Feedback Assistant.app/Contents/MacOS/Feedback Assistant`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.ProactiveSummarization.feedback</key>
-	<true/>
-	<key>com.apple.ProactiveSummarization.model-input</key>
-	<true/>
-	<key>com.apple.ProactiveSummarization.summarization</key>
-	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

```
### Web App

> `/System/Library/CoreServices/Web App.app/Contents/MacOS/Web App`

```diff

 	<true/>
 	<key>com.apple.dock.add-item</key>
 	<true/>
-	<key>com.apple.duet.activityscheduler.allow</key>
-	<true/>
 	<key>com.apple.features.all-access</key>
 	<true/>
 	<key>com.apple.finance.private</key>

 	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
-	<key>com.apple.private.parsec.default-client</key>
-	<string>com.apple.Safari</string>
 	<key>com.apple.private.rsr-cryptex-access</key>
 	<true/>
 	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>

 		<string>com.apple.email.maild</string>
 		<string>com.apple.translationd</string>
 		<string>com.apple.cdp.daemon</string>
-		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.coreservices.lsbestappsuggestionmanager.xpc</string>
 		<string>com.apple.suggestd.urls</string>
 		<string>com.apple.security.octagon</string>

```
### AccessibilitySettingsWidgetExtension

> `/System/Library/ExtensionKit/Extensions/AccessibilitySettingsWidgetExtension.appex/Contents/MacOS/AccessibilitySettingsWidgetExtension`

```diff

 	<array>
 		<string>group.com.apple.accessibility.voicebanking</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.voicebanking.store</string>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
-		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.universalaccess</string>
 		<string>com.apple.mediaaccessibility</string>
 		<string>com.apple.Accessibility</string>

```
### AppleIDSettings

> `/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings`

```diff

 		<string>com.apple.windowserver.active</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>
-		<string>com.apple.ak.signinwithapple.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
-	<dict>
-		<key>type</key>
-		<string>path</string>
-		<key>value</key>
-		<string>/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension</string>
-	</dict>
 	<key>com.apple.private.avfoundation.capture.allow</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 	</array>
 	<key>com.apple.security.device.camera</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
+		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
+		<string>/System/Library/PreinstalledAssetsV2/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
+		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.assistant.cdm</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.photos.service</string>
+		<string>com.apple.mediaanalysisd.service.public</string>
+		<string>com.apple.sage.summarization</string>
+		<string>com.apple.generativeexperiences.summarization</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.biome.access.user</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>com.apple.gms.availability</string>
+		<string>kCFPreferencesAnyApplication</string>
+	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>IOSurfaceRootUserClient</string>
+		<string>AGXDeviceUserClient</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>

 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleNVMeEANUC</string>
-		<string>IOSurfaceRootUserClient</string>
-		<string>AGXDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/Contents/MacOS/SearchToolExtension`

```diff

 	<true/>
 	<key>com.apple.intelligenceflow.orchestrator</key>
 	<true/>
+	<key>com.apple.intelligenceflow.search</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.KnowledgeConstruction</key>

```
### SecurityPrivacyExtension

> `/System/Library/ExtensionKit/Extensions/SecurityPrivacyExtension.appex/Contents/MacOS/SecurityPrivacyExtension`

```diff

 	<true/>
 	<key>com.apple.private.iad.opt-in-control</key>
 	<true/>
-	<key>com.apple.private.ind.client</key>
-	<true/>
-	<key>com.apple.private.intelligenceplatform.use-cases</key>
-	<dict>
-		<key>AppleIntelligenceReportExport</key>
-		<dict>
-			<key>Streams</key>
-			<dict>
-				<key>GenerativeExperiences.TransparencyLog</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-				<key>PrivateCloudCompute.RequestLog</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
-		</dict>
-	</dict>
 	<key>com.apple.private.ironwood</key>
 	<true/>
 	<key>com.apple.private.lockdownmoded.read-write</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ap.adprivacyd.opt-out</string>
-		<string>com.apple.ind.cloudfeatures</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SiriPreferenceExtension

> `/System/Library/ExtensionKit/Extensions/SiriPreferenceExtension.appex/Contents/MacOS/SiriPreferenceExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.accounts.appleaccount.fullaccess</key>
-	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>SiriPreferenceExtension</string>
 	<key>com.apple.assistant.settings</key>

 	<true/>
 	<key>com.apple.private.corespeech.xpc.remote</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>SiriPreferenceExtension</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.TransparencyLog</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.siri.setup</key>
 	<true/>
 	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
-		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
-		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
 		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>

```
### WallpaperHeliosExtension

> `/System/Library/ExtensionKit/Extensions/WallpaperHeliosExtension.appex/Contents/MacOS/WallpaperHeliosExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.locationd.effective_bundle</key>
-	<true/>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
 	<key>com.apple.private.wallpaper.extension</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.personal-information.location</key>
-	<true/>
 </dict>
 </plist>
 

```
### com.apple.automator.runner

> `/System/Library/Frameworks/Automator.framework/Versions/A/XPCServices/com.apple.automator.runner.xpc/Contents/MacOS/com.apple.automator.runner`

```diff

 	</array>
 	<key>com.apple.private.cs.automator-plugins</key>
 	<true/>
-	<key>com.apple.private.quarantine.control-add</key>
-	<true/>
 	<key>com.apple.private.tcc.allow-prompting</key>
 	<array>
 		<string>kTCCServiceAll</string>

```
### maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/Versions/A/XPCServices/maphelperservice.xpc/Contents/MacOS/maphelperservice`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict>
-	<key>com.apple.geoservices.restricted-tiles</key>
-	<array>
-		<string>offline</string>
-	</array>
-</dict>
+<dict/>
 </plist>
 

```
### ctkahp

> `/System/Library/Frameworks/CryptoTokenKit.framework/ctkahp.bundle/Contents/MacOS/ctkahp`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.ctkahp</string>
-	<key>com.apple.authorization.extract-password</key>
-	<true/>
 	<key>com.apple.keystore.device.smart-card</key>
 	<true/>
 	<key>com.apple.keystore.filevault</key>

```
### storekitagent

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitagent`

```diff

 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>
-		<string>com.apple.storekit</string>
 	</array>
 </dict>
 </plist>

```
### translationd

> `/System/Library/Frameworks/Translation.framework/translationd`

```diff

 		<string>com.apple.coreaudio</string>
 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.coremedia</string>
-		<string>com.apple.assistant.support</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 UtilityExtension_macOS

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/UtilityExtension_macOS.appex/Contents/MacOS/UtilityExtension_macOS`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>409835401</string>
	<key>application-identifier</key>
	<string>com.apple.AppleMediaServicesUI.UtilityExtension</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.AppleMediaServicesUI.UtilityExtension</string>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.multitasking.systemappassertions</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Library</string>
		<string>Queue</string>
		<string>Install</string>
	</array>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstoreagent.xpc</string>
		<string>com.apple.xpc.amsengagementd</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.xpc.amsaccountsd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.storeservices.itfe</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/AppleInternal/Library/Jet/</string>
		<string>/System/Library/Jet/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstoreagent.xpc</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.ak.anisette.xpc</string>
	</array>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```
### AMSUIPaymentViewService_macOS

> `/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/Versions/A/XPCServices/AMSUIPaymentViewService_macOS.xpc/Contents/MacOS/AMSUIPaymentViewService_macOS`

```diff

 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
-	<key>com.apple.security.network.client</key>
-	<true/>
 </dict>
 </plist>
 

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistant_service`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
-	<key>com.apple.private.email</key>
-	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.read_authorization_override</key>

 		<string>1630</string>
 		<string>1327</string>
 		<string>1328</string>
-		<string>1750</string>
 	</array>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
-	<key>com.apple.generativeexperiences.availability.internal</key>
-	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.geoservices.navigation_info</key>

 		<string>SIRI_DATA_INTEGRATION_TEST1</string>
 		<string>SIRI_DATA_INTEGRATION_TEST2</string>
 		<string>SIRI_DICTATION_ASSETS</string>
-		<string>SIRI_HEARABLES_VOX</string>
 		<string>SIRI_INFORMATION_CACHING</string>
 		<string>SIRI_MEMORY_SYNC_CONFIG</string>
 		<string>SIRI_MESSAGES_APP_SELECTION</string>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.intelligenceplatform</string>
 		<string>com.apple.suggestions</string>
-		<string>com.apple.AppleIntelligenceReport</string>
+		<string>com.apple.tokengeneration</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
-	<key>com.apple.private.biome.read-only</key>
-	<array>
-		<string>Carousel.Connection.Companion</string>
-	</array>
 	<key>com.apple.private.chrono-extension-host</key>
 	<true/>
 	<key>com.apple.private.coreaudio.initiatetemporarybackgroundplayback.allow</key>

```
### com.apple.CloudDocs.MobileDocumentsFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProvider.appex/Contents/MacOS/com.apple.CloudDocs.MobileDocumentsFileProvider`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.security.files.user-selected.executable</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>

```
### com.apple.CloudDocs.MobileDocumentsFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.MobileDocumentsFileProviderManaged.appex/Contents/MacOS/com.apple.CloudDocs.MobileDocumentsFileProviderManaged`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.security.files.user-selected.executable</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### com.apple.CloudDocs.iCloudDriveFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/Contents/MacOS/com.apple.CloudDocs.iCloudDriveFileProvider`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.security.files.user-selected.executable</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>

```
### com.apple.CloudDocs.iCloudDriveFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/Contents/MacOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.security.files.user-selected.executable</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/Contents/MacOS/CloudDocsDiagnostic`

```diff

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/db/</string>
 	</array>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### CloudDocsStorageManagement

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsStorageManagement.appex/Contents/MacOS/CloudDocsStorageManagement`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Mobile Documents/</string>

```
### bird

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/Versions/A/Support/bird`

```diff

 	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
-	<key>com.apple.security.network.client</key>
-	<true/>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird</string>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.shortcutitems.fullaccess</key>

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.CoreAnalytics</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/Trial/Treatments/</string>
+		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SystemConfiguration.configd</string>

 	</array>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>1000</string>
+		<string>1010</string>
+		<string>1020</string>
+		<string>1030</string>
+		<string>1040</string>
+		<string>1041</string>
+		<string>1042</string>
+		<string>1043</string>
+		<string>1090</string>
+		<string>1100</string>
+		<string>1101</string>
+		<string>1110</string>
+		<string>1120</string>
+		<string>1130</string>
+		<string>1140</string>
+		<string>1150</string>
+		<string>1151</string>
+		<string>1152</string>
+		<string>1153</string>
+		<string>1154</string>
+		<string>1160</string>
+		<string>1161</string>
+		<string>1162</string>
+		<string>1170</string>
+		<string>1180</string>
+		<string>1190</string>
+		<string>1191</string>
+		<string>1200</string>
+		<string>1201</string>
+		<string>1202</string>
+		<string>1210</string>
+		<string>1220</string>
+		<string>1221</string>
+		<string>1230</string>
+		<string>1231</string>
+		<string>1240</string>
+		<string>1241</string>
+		<string>1250</string>
+		<string>1251</string>
+		<string>1252</string>
+		<string>1260</string>
+		<string>1261</string>
+		<string>1262</string>
+		<string>1270</string>
+		<string>1280</string>
+		<string>1290</string>
+		<string>1291</string>
+		<string>1292</string>
+		<string>1300</string>
+		<string>1310</string>
+		<string>1321</string>
+		<string>1320</string>
+		<string>1322</string>
+		<string>1323</string>
+		<string>1324</string>
+		<string>1325</string>
+		<string>1326</string>
+		<string>1327</string>
+		<string>1328</string>
+		<string>1329</string>
+		<string>1330</string>
+		<string>1331</string>
+		<string>1340</string>
+		<string>1341</string>
+		<string>1342</string>
+		<string>1350</string>
+		<string>1360</string>
+		<string>1370</string>
+		<string>1380</string>
+		<string>1390</string>
+		<string>1400</string>
+		<string>1410</string>
+		<string>1411</string>
+		<string>1420</string>
+		<string>1430</string>
+		<string>1431</string>
+		<string>1440</string>
+		<string>1441</string>
+		<string>1450</string>
+		<string>1460</string>
+		<string>1470</string>
+		<string>1480</string>
+		<string>1490</string>
+		<string>1491</string>
+		<string>1500</string>
+		<string>1510</string>
+		<string>1511</string>
+		<string>1512</string>
+		<string>1513</string>
+		<string>1520</string>
+		<string>1521</string>
+		<string>1530</string>
+		<string>1540</string>
+		<string>1541</string>
+		<string>1542</string>
+		<string>1543</string>
+		<string>1544</string>
+		<string>1545</string>
+		<string>1546</string>
+		<string>1547</string>
+		<string>1548</string>
+		<string>1549</string>
+		<string>1550</string>
+		<string>1551</string>
+		<string>1560</string>
+		<string>1570</string>
+		<string>1571</string>
+		<string>1580</string>
+		<string>1590</string>
+		<string>1600</string>
+		<string>1601</string>
+		<string>1602</string>
+		<string>1603</string>
+		<string>1610</string>
+		<string>1620</string>
+		<string>1630</string>
+		<string>1631</string>
+		<string>1632</string>
+		<string>1640</string>
+		<string>1650</string>
+		<string>1660</string>
+		<string>1670</string>
+		<string>1680</string>
+		<string>1690</string>
+		<string>1700</string>
+		<string>1701</string>
+		<string>1702</string>
+		<string>1710</string>
+		<string>1720</string>
+		<string>1730</string>
+		<string>1740</string>
+		<string>100</string>
+		<string>101</string>
+		<string>102</string>
+		<string>103</string>
+		<string>104</string>
+		<string>105</string>
+		<string>106</string>
+		<string>107</string>
+		<string>108</string>
+		<string>109</string>
+		<string>110</string>
+		<string>120</string>
+		<string>130</string>
+		<string>150</string>
+		<string>151</string>
+		<string>152</string>
+		<string>153</string>
+		<string>154</string>
+		<string>155</string>
+		<string>156</string>
+		<string>157</string>
+		<string>158</string>
+		<string>159</string>
+		<string>160</string>
+		<string>161</string>
+		<string>162</string>
+		<string>163</string>
+		<string>164</string>
+		<string>165</string>
+		<string>166</string>
+		<string>167</string>
+		<string>168</string>
+		<string>169</string>
+		<string>170</string>
+		<string>171</string>
+		<string>180</string>
+		<string>181</string>
+		<string>190</string>
+		<string>191</string>
+		<string>200</string>
+		<string>201</string>
+		<string>210</string>
+		<string>211</string>
+		<string>212</string>
+		<string>213</string>
+		<string>214</string>
+		<string>215</string>
+		<string>251</string>
+		<string>252</string>
+		<string>253</string>
+		<string>254</string>
+		<string>255</string>
+		<string>256</string>
+		<string>257</string>
+		<string>258</string>
+		<string>301</string>
+		<string>311</string>
+		<string>312</string>
+		<string>313</string>
+		<string>314</string>
+		<string>321</string>
+		<string>322</string>
+		<string>331</string>
+		<string>332</string>
+		<string>333</string>
+		<string>334</string>
+		<string>335</string>
+		<string>336</string>
+		<string>337</string>
+		<string>341</string>
+		<string>342</string>
+		<string>351</string>
+		<string>352</string>
+		<string>353</string>
+		<string>354</string>
+		<string>361</string>
+		<string>371</string>
+		<string>372</string>
+		<string>373</string>
+		<string>374</string>
+		<string>375</string>
+		<string>381</string>
+		<string>391</string>
+		<string>392</string>
+		<string>393</string>
+		<string>394</string>
+		<string>395</string>
+		<string>401</string>
+		<string>402</string>
+		<string>403</string>
+		<string>404</string>
+		<string>405</string>
+		<string>406</string>
+		<string>407</string>
+		<string>408</string>
+		<string>409</string>
+		<string>411</string>
+		<string>412</string>
+		<string>413</string>
+		<string>414</string>
+		<string>415</string>
+		<string>416</string>
+		<string>417</string>
+		<string>421</string>
+		<string>422</string>
+		<string>423</string>
+		<string>424</string>
+		<string>425</string>
+		<string>426</string>
+		<string>431</string>
+		<string>501</string>
+		<string>502</string>
+		<string>511</string>
+		<string>512</string>
+		<string>513</string>
+		<string>514</string>
+		<string>515</string>
+		<string>521</string>
+		<string>522</string>
+		<string>531</string>
+		<string>532</string>
+		<string>541</string>
+		<string>551</string>
+		<string>561</string>
+		<string>562</string>
+		<string>563</string>
+		<string>564</string>
+		<string>565</string>
+		<string>566</string>
+		<string>567</string>
+		<string>568</string>
+		<string>569</string>
+		<string>571</string>
+		<string>581</string>
+		<string>582</string>
+		<string>583</string>
+		<string>584</string>
+		<string>585</string>
+		<string>586</string>
+		<string>587</string>
+		<string>588</string>
+		<string>589</string>
+		<string>591</string>
+		<string>592</string>
+		<string>593</string>
+		<string>601</string>
+		<string>602</string>
+		<string>603</string>
+		<string>604</string>
+		<string>605</string>
+		<string>611</string>
+		<string>621</string>
+		<string>631</string>
+		<string>641</string>
+		<string>642</string>
+		<string>651</string>
+		<string>700</string>
+		<string>701</string>
+		<string>702</string>
+		<string>703</string>
+		<string>704</string>
+		<string>705</string>
+		<string>750</string>
+		<string>751</string>
+		<string>752</string>
+		<string>753</string>
+		<string>754</string>
+		<string>755</string>
+		<string>756</string>
+		<string>757</string>
+		<string>758</string>
+		<string>759</string>
+		<string>760</string>
+		<string>761</string>
+		<string>762</string>
+		<string>763</string>
+		<string>800</string>
+		<string>801</string>
+		<string>802</string>
+		<string>803</string>
+		<string>804</string>
+		<string>805</string>
+		<string>810</string>
+		<string>811</string>
+		<string>812</string>
+		<string>813</string>
+		<string>814</string>
+		<string>815</string>
+		<string>816</string>
+		<string>817</string>
+		<string>818</string>
+		<string>819</string>
+		<string>820</string>
+		<string>821</string>
+		<string>822</string>
+		<string>823</string>
+		<string>824</string>
+		<string>825</string>
+		<string>830</string>
+		<string>831</string>
+		<string>832</string>
+		<string>833</string>
+		<string>834</string>
+		<string>835</string>
+		<string>836</string>
+		<string>837</string>
+		<string>838</string>
+		<string>839</string>
+		<string>840</string>
+		<string>841</string>
+		<string>842</string>
+		<string>843</string>
+		<string>844</string>
+		<string>845</string>
+		<string>846</string>
+		<string>847</string>
+		<string>848</string>
+		<string>849</string>
+		<string>850</string>
+		<string>851</string>
+		<string>852</string>
+		<string>860</string>
+		<string>861</string>
 		<string>862</string>
+		<string>863</string>
+		<string>870</string>
+		<string>871</string>
+		<string>872</string>
+		<string>873</string>
+		<string>874</string>
+		<string>880</string>
+		<string>890</string>
+		<string>900</string>
+		<string>910</string>
+		<string>920</string>
+		<string>921</string>
+		<string>922</string>
+		<string>923</string>
+		<string>924</string>
+		<string>930</string>
+		<string>940</string>
+		<string>950</string>
+		<string>960</string>
+		<string>961</string>
+		<string>962</string>
+		<string>963</string>
+		<string>970</string>
+		<string>980</string>
+		<string>990</string>
+		<string>11</string>
+		<string>12</string>
+		<string>13</string>
+		<string>14</string>
+		<string>20</string>
+		<string>30</string>
+		<string>31</string>
+		<string>40</string>
+		<string>41</string>
+		<string>50</string>
+		<string>51</string>
+		<string>52</string>
+		<string>53</string>
+		<string>54</string>
+		<string>60</string>
+		<string>61</string>
+		<string>62</string>
+		<string>71</string>
+		<string>0</string>
+		<string>1</string>
 	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<string>com.apple.corespeechd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>SpeechProfile</key>
+		<key>__Koa__</key>
 		<dict>
 			<key>Sets</key>
 			<dict>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
-				<key>HomeKit.Home</key>
+				<key>HomeKit.Entity</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
-				<key>MediaLibrary.Media</key>
+				<key>Media.Entity</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
-				<key>Podcasts.Podcast</key>
+				<key>Podcasts.Entity</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
-				<key>Siri.PrivateLearning.Media</key>
+				<key>Siri.PrivateLearning.MediaEntity</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
-		<string>com.apple.ironwood.support</string>
 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.nano</string>
 		<string>com.apple.raisetospeak</string>

```
### DataDetectorsViewService

> `/System/Library/PrivateFrameworks/DataDetectors.framework/Versions/A/XPCServices/DataDetectorsViewService.xpc/Contents/MacOS/DataDetectorsViewService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
-	<key>com.apple.private.calendar.allow-integrations</key>
-	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/Contents/MacOS/DPSubmissionService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.DPSubmissionService</string>
 	<key>aps-environment</key>
 	<string>development</string>
 	<key>com.apple.application-identifier</key>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.keystore.access-keychain-keys</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.mobileactivationd.bridge</key>

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>lib/PPM/</string>
+	</array>
+	<key>com.apple.security.ts.cloudkit-client</key>
+	<true/>
 	<key>iCloudServices</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
 	<key>platform-application</key>
 	<true/>
+	<key>seatbelt-profiles</key>
+	<array>
+		<string>DPSubmissionService</string>
+	</array>
 </dict>
 </plist>
 

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GenerativeFunctions.generativeexperiencesd</string>
-	<key>com.apple.assistant.settings</key>
-	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.intelligenceflow.context</key>

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
-	<key>com.apple.private.assistant.settings</key>
-	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/Contents/MacOS/imagent`

```diff

 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
-		<string>com.apple.Messages.diagnostics.usernotifications</string>
 		<string>com.apple.iChat</string>
 		<string>com.apple.MobileSMS</string>
 	</array>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/Contents/MacOS/IMDPersistenceAgent`

```diff

 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
-		<string>com.apple.Messages.diagnostics.usernotifications</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.iChat</string>
 	</array>

```

### 🆕 com.apple.ImageGenerationUI.DiagnosticExtension

> `/System/Library/PrivateFrameworks/ImageGenerationUI.framework/Versions/A/PlugIns/com.apple.ImageGenerationUI.DiagnosticExtension.appex/Contents/MacOS/com.apple.ImageGenerationUI.DiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### installcoordination_proxy

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordination_proxy`

```diff

 <dict>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
-	<key>com.apple.private.InstallCoordination.overridePlaceholderDisposition</key>
-	<true/>
 	<key>com.apple.private.InstallCoordination.uninstall</key>
 	<true/>
 	<key>com.apple.private.MobileInstallationHelperService.InstallCoordinationProxyOpsEnabled</key>

```
### LookupViewService

> `/System/Library/PrivateFrameworks/Lookup.framework/Versions/A/XPCServices/LookupViewService.xpc/Contents/MacOS/LookupViewService`

```diff

 	<string>com.apple.searchui</string>
 	<key>com.apple.private.appstorecomponents.media-client-version</key>
 	<string>1</string>
-	<key>com.apple.private.coreservices.canmaplsdatabase</key>
-	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.spotlight.parsec</key>

 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/Preferences/com.apple.commerce.plist</string>
 		<string>/usr/local/lib/log</string>
 	</array>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/mediaanalysisd`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
-		<string>com.apple.photos.shareddefaults</string>
 		<string>com.apple.CoreRecognition</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.Spotlight</string>

```
### MetricMeasurementHelper

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/Versions/A/XPCServices/MetricMeasurementHelper.xpc/Contents/MacOS/MetricMeasurementHelper`

```diff

 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
-	<key>com.apple.runningboard.terminateprocess</key>
-	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.sysmond</string>

```

### 🆕 ModelCatalogCompilationService

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/XPCServices/ModelCatalogCompilationService.xpc/Contents/MacOS/ModelCatalogCompilationService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.ModelCatalog.ModelCatalogCompilationService</string>
	<key>com.apple.aned.private.processModelShare.allow</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.ModelCatalog.ModelCatalogCompilationService</string>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
	</array>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.ModelCatalog.ModelCatalogCompilationService</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
	</array>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
		<string>H11ANEInDirectPathClient</string>
	</array>
</dict>
</plist>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/modelcatalogd`

```diff

 <dict>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-read-no-fault</key>
 	<true/>
+	<key>com.apple.aned.private.processModelShare.allow</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.modelcatalogd</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.modelcatalog.compilationService</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

```
### PassKitServicesXPCService

> `/System/Library/PrivateFrameworks/PassKitServices.framework/Versions/A/XPCServices/PassKitServicesXPCService.xpc/Contents/MacOS/PassKitServicesXPCService`

```diff

 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
+	<key>com.apple.passd.peer-payment</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.nfcd.hwmanager</string>
-		<string>com.apple.passd.peer-payment</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### photolibraryd

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd`

```diff

 		<string>com.apple.mediaanalysisd.embeddingstore</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.duetactivityscheduler</string>
-		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

 	<true/>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>
-	<key>com.apple.symptom_diagnostics.report</key>
-	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>394</string>

```
### PodcastContentService

> `/System/Library/PrivateFrameworks/PodcastServices.framework/XPCServices/PodcastContentService.xpc/Contents/MacOS/PodcastContentService`

```diff

 <dict>
 	<key>com.apple.amp.library.client</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>243LU875E5.groups.com.apple.podcasts</string>
-	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>

```
### writeconfig

> `/System/Library/PrivateFrameworks/SystemAdministration.framework/XPCServices/writeconfig.xpc/Contents/MacOS/writeconfig`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.scripting</key>
 	<true/>
-	<key>com.apple.private.syspolicy.gatekeeper.settings-management</key>
-	<true/>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
 		<string>kTCCServiceAccessibility</string>

```
### Accessibility Tutorial

> `/System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Resources/Accessibility Tutorial.app/Contents/MacOS/Accessibility Tutorial`

```diff

 	<true/>
 	<key>com.apple.private.accessibility.setVoiceOverAllowedCommands</key>
 	<true/>
-	<key>com.apple.private.security.storage.universalaccess</key>
-	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceSpeechRecognition</string>
 		<string>SearchUIInlineActionButtonAccessibility</string>
 	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.universalaccess</string>
-		<string>com.apple.Accessibility</string>
-		<string>com.apple.speech.synthesis.general.prefs</string>
-	</array>
-	<key>com.apple.security.temporary-exception.user-preference.write</key>
-	<array>
-		<string>com.apple.universalaccess</string>
-		<string>com.apple.Accessibility</string>
-		<string>com.apple.speech.synthesis.general.prefs</string>
-	</array>
 </dict>
 </plist>
 

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>group.com.apple.coreservices.useractivityd</string>
-	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceUbiquity</string>

 	</array>
 	<key>com.apple.runningboard.assertions.useractivityd</key>
 	<true/>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.coreservices.useractivityd</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/Contents/MacOS/BackgroundShortcutRunner`

```diff

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.airplay.endpoint.xpc</string>
-		<string>com.apple.calaccessd</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>

```
### ContainerMetadataExtractor

> `/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/Contents/MacOS/ContainerMetadataExtractor`

```diff

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/containers/</string>
 	</array>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 </dict>
 </plist>
 

```
### TelemetryDiskChecker

> `/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/TelemetryDiskChecker.xpc/Contents/MacOS/TelemetryDiskChecker`

```diff

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/telemetry-db/</string>
 	</array>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Application Support/CloudDocs/session/telemetry-db/</string>

```
### iCloudNotificationAgent

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotificationAgent`

```diff

 	<array>
 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.CloudSubscriptionFeatures.cache</string>
-		<string>com.apple.CloudSubscriptionFeatures.geoCache</string>
-		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
-		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
-		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
-		<string>com.apple.CloudSubscriptionFeatures.ticket.cache</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 UtilityExtension_catalyst

> `/System/iOSSupport/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/PlugIns/UtilityExtension_catalyst.appex/Contents/MacOS/UtilityExtension_catalyst`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>409835401</string>
	<key>application-identifier</key>
	<string>com.apple.AppleMediaServicesUI.UtilityExtension</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.AppleMediaServicesUI.UtilityExtension</string>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.multitasking.systemappassertions</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Library</string>
		<string>Queue</string>
		<string>Install</string>
	</array>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstoreagent.xpc</string>
		<string>com.apple.xpc.amsengagementd</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.xpc.amsaccountsd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.storeservices.itfe</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/AppleInternal/Library/Jet/</string>
		<string>/System/Library/Jet/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstoreagent.xpc</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.ak.anisette.xpc</string>
	</array>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```
### brctl

> `/usr/bin/brctl`

```diff

 	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
+	<key>com.apple.security.exception.ts.tmpdir</key>
+	<array>
+		<string>com.apple.bird.codecoverage</string>
+	</array>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 </dict>

```
### modelmanagerdump

> `/usr/bin/modelmanagerdump`

```diff

 	<true/>
 	<key>com.apple.modelmanager.dumpState</key>
 	<true/>
-	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
-	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.modelmanager.loadBundle</key>

```
### security

> `/usr/bin/security`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
-	<key>com.apple.private.platformsso.security</key>
-	<true/>
 </dict>
 </plist>
 

```
### shortcuts

> `/usr/bin/shortcuts`

```diff

 	<array>
 		<string>iCloud.is.workflow.my.workflows</string>
 	</array>
-	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>1</integer>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
 	</array>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.shortcuts</string>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SharingServices</string>

```
### AssetCache

> `/usr/libexec/AssetCache/AssetCache`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>AvpFairPlayUserClient.access</key>
-	<true/>
 	<key>com.apple.private.AssetCacheServices.Manager</key>
 	<true/>
 	<key>com.apple.private.AssetCacheServices.Tetherator</key>

 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 	</array>
-	<key>com.apple.security.iokit-user-client-class</key>
-	<array>
-		<string>AvpFairPlayUserClient</string>
-	</array>
 </dict>
 </plist>
 

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
-	<key>com.apple.private.ind.client</key>
-	<true/>
 	<key>com.apple.private.iokit.BDCDataCopy</key>
 	<true/>
-	<key>com.apple.private.iokit.battery-gauging-mitigation</key>
-	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.ind.cloudfeatures</string>
-		<string>com.apple.ind.xpc</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.preferences.sounds</string>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
-	<key>com.apple.private.ind.client</key>
-	<true/>
 	<key>com.apple.private.ioaccelmemoryinfo</key>
 	<true/>
 	<key>com.apple.private.iokit.BDCDataCopy</key>
 	<true/>
-	<key>com.apple.private.iokit.battery-gauging-mitigation</key>
-	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.ind.cloudfeatures</string>
-		<string>com.apple.ind.xpc</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.preferences.sounds</string>

```
### airportd

> `/usr/libexec/airportd`

```diff

 	<true/>
 	<key>com.apple.networkd_privileged</key>
 	<true/>
-	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
-	<array>
-		<string>StoreDemoMode</string>
-	</array>
 	<key>com.apple.private.SkyLight.event.monitor</key>
 	<true/>
-	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
-	<true/>
-	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
-	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
 	<key>com.apple.private.corewifi.countrycode</key>

 	<array>
 		<string>AirPort</string>
 	</array>
-	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
-	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.wifianalytics</key>

```
### avconferenced

> `/usr/libexec/avconferenced`

```diff

 		<string>facetime</string>
 		<string>facetime-audio</string>
 	</array>
-	<key>com.apple.private.mediaexperience.smartRoutingScore.allow</key>
-	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.notificationcenterui.alerts</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>com.apple.duetactivityscheduler.plugin</string>
 		<string>com.apple.das.fairscheduling</string>
 		<string>com.apple.dasd.dailyPeriodic</string>
-		<string>com.apple.dasd.issueDetector</string>
 		<string>com.apple.dasd.swapkills</string>
 		<string>com.apple.dasd.widgetRefreshBudgets</string>
 		<string>com.apple.mt</string>

```
### gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

 	<array>
 		<string>kTCCServiceSystemPolicyDesktopFolder</string>
 		<string>kTCCServicePhotos</string>
-		<string>kTCCServiceListenEvent</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

```
### mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.modelmanager.query</key>
-	<true/>
 	<key>com.apple.private.memoryinfo</key>
 	<true/>
 	<key>com.apple.private.memorystatus</key>

```
### powerlogHelperd

> `/usr/libexec/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.private.hid.manager.client</key>
 	<true/>
-	<key>com.apple.private.ind.client</key>
-	<true/>
 	<key>com.apple.private.ioaccelmemoryinfo</key>
 	<true/>
 	<key>com.apple.private.iokit.BDCDataCopy</key>
 	<true/>
-	<key>com.apple.private.iokit.battery-gauging-mitigation</key>
-	<true/>
 	<key>com.apple.private.iokit.batterydata</key>
 	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.ind.cloudfeatures</string>
-		<string>com.apple.ind.xpc</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.preferences.sounds</string>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.private.audio.interprocess-tap</key>
 	<true/>
-	<key>com.apple.private.audio.suppress-mic-indicator</key>
-	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>ScreenSharing</string>

 	<array>
 		<string>UIStatusBarStyleOverrideScreenReplayRecording</string>
 	</array>
-	<key>com.apple.systemstatus.domains</key>
-	<array>
-		<string>media</string>
-	</array>
-	<key>com.apple.systemstatus.publisher.domains</key>
-	<array>
-		<string>media</string>
-	</array>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>replayd</string>

```
### oahd

> `/usr/libexec/rosetta/oahd`

```diff

 	<string>com.apple.oahd</string>
 	<key>com.apple.private.security.storage.oahd</key>
 	<true/>
-	<key>com.apple.private.ecosystemanalytics.rosetta</key>
-	<true/>
 </dict>
 </plist>
 

```

### 🆕 silhouette

> `/usr/libexec/silhouette`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.silhouette</string>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.Config</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/CoreDuet/Knowledge/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.suggestd.PersonalizationPortrait.DeletionTracking</string>
		<string>com.apple.coreduetd.knowledge</string>
	</array>
</dict>
</plist>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
-	<key>com.apple.generativeexperiences.availabilityService</key>
-	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>351</string>
 		<string>401</string>
 		<string>406</string>
 		<string>409</string>

 		<string>961</string>
 		<string>1000</string>
 		<string>1210</string>
-		<string>1630</string>
 		<string>1701</string>
 	</array>
 </dict>

```
### uarppersonalizationd

> `/usr/libexec/uarppersonalizationd`

```diff

 	<true/>
 	<key>com.apple.uarppersonalization</key>
 	<true/>
-	<key>com.apple.uarppersonalization.btleserver</key>
-	<true/>
 </dict>
 </plist>
 

```
### usernoted

> `/usr/sbin/usernoted`

```diff

 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
-	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceAddressBook</string>
-	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.usernoted</string>

```
