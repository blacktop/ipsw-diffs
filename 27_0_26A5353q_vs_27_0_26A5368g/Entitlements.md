## 🔑 Entitlements

### filesystem

### Books

> `/System/Applications/Books.app/Contents/MacOS/Books`

```diff

 	<array/>
 	<key>com.apple.developer.carplay-audio</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### Campo

> `/System/Applications/Campo.app/Contents/MacOS/Campo`

```diff

 	</array>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.filederivatives.derive</key>
 	<true/>
 	<key>com.apple.filederivatives.list</key>

 		<string>IntelligenceFlow.ResponseGeneration</string>
 		<string>IntelligenceFlow.ExecutorTelemetry</string>
 		<string>Discoverability.Signals</string>
+		<string>Intelligence.Usage</string>
 	</array>
 	<key>com.apple.private.calendar.allow-integrations</key>
 	<true/>

 			<key>Search</key>
 			<array>
 				<string>SiriTranscript</string>
+				<string>SiriTranscriptConversation</string>
 			</array>
 		</dict>
 		<key>iftool.dump-stream</key>

 	<true/>
 	<key>com.apple.private.siri.setup</key>
 	<true/>
+	<key>com.apple.private.siriappintentsd.orchestrator</key>
+	<true/>
 	<key>com.apple.private.sleepd</key>
 	<true/>
 	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>

 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.generativeexperiences.corefollowup</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
-		<string>com.apple.siriappintentsd.orchestrator</string>
+		<string>com.apple.private.siriappintentsd.orchestrator</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.orchestration.prescribedaction</key>
 	<true/>
-	<key>com.apple.siriappintentsd.orchestrator</key>
-	<true/>
 	<key>com.apple.sirisuggestions.allow</key>
 	<true/>
 	<key>com.apple.spotlight.entitledattributes</key>

```
### FindMy

> `/System/Applications/FindMy.app/Contents/MacOS/FindMy`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.appleaccount.identity.read</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>0000000000.com.apple.findmy</string>
 	<key>com.apple.authkit.client.internal</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.icloud.searchpartyd.securelocations</string>
+		<string>com.apple.aa.identity.xpc</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### Home

> `/System/Applications/Home.app/Contents/MacOS/Home`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.energykit</key>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Home</string>
 	<key>com.apple.developer.usernotifications.critical-alerts</key>
 	<true/>
 	<key>com.apple.dropin</key>

 		<string>com.apple.AddressBook.abd</string>
 		<string>com.apple.AttentionAwareness</string>
 		<string>com.apple.CompanionLink</string>
+		<string>com.apple.CoreGraphics.CGPDFService</string>
 		<string>com.apple.DistributedTimers</string>
 		<string>com.apple.EnergyKitService</string>
 		<string>com.apple.OSASyncProxy.client</string>

 		<string>com.apple.system.opendirectoryd.api</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>
+		<string>com.apple.videoconference.camera</string>
 		<string>com.apple.wirelessproxd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>

 		<string>com.apple.AddressBook.abd</string>
 		<string>com.apple.AttentionAwareness</string>
 		<string>com.apple.CompanionLink</string>
+		<string>com.apple.CoreGraphics.CGPDFService</string>
 		<string>com.apple.DistributedTimers</string>
 		<string>com.apple.EnergyKitService</string>
 		<string>com.apple.OSASyncProxy.client</string>

 		<string>com.apple.system.opendirectoryd.api</string>
 		<string>com.apple.terminusd</string>
 		<string>com.apple.tvremotecore.xpc</string>
+		<string>com.apple.videoconference.camera</string>
 		<string>com.apple.wirelessproxd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>

```
### HomeWidget

> `/System/Applications/Home.app/Contents/PlugIns/HomeWidget.appex/Contents/MacOS/HomeWidget`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Home</string>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>

```
### Image Playground

> `/System/Applications/Image Playground.app/Contents/MacOS/Image Playground`

```diff

 	</array>
 	<key>com.apple.developer.declared-age-range</key>
 	<true/>
+	<key>com.apple.developer.private-cloud-compute</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp</string>
 	<key>com.apple.developer.usernotifications.communication</key>

 	<array>
 		<string>com.apple.GenerativePlaygroundApp</string>
 	</array>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.stickers.api</string>

```
### Journal

> `/System/Applications/Journal.app/Contents/MacOS/Journal`

```diff

 	<true/>
 	<key>com.apple.das.private.bgtask.continuedprocessing</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.healthkit.access</key>

```
### Mail

> `/System/Applications/Mail.app/Contents/MacOS/Mail`

```diff

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.duetexpertd.assistant-actions</string>
 		<string>com.apple.internal.SpotlightAutomationTester</string>
+		<string>com.apple.biome.compute.source.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### MapsDiagnostic

> `/System/Applications/Maps.app/Contents/PlugIns/MapsDiagnostic.appex/Contents/MacOS/MapsDiagnostic`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
-	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
-	<string>com.apple.Maps</string>
 	<key>com.apple.geoservices.map-subscriptions</key>
 	<array>
 		<string>*</string>

```
### PasswordsMenuBarExtra

> `/System/Applications/Passwords.app/Contents/Library/LoginItems/PasswordsMenuBarExtra.app/Contents/MacOS/PasswordsMenuBarExtra`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Passwords.ChangePasswordForMe</string>
+		<string>Passwords.SecurityRecommendations</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.personas.no.inherit</key>
+	<true/>
 	<key>com.apple.private.safari.automatic-password-change</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
 		<string>/Library/Containers/com.apple.Safari/Container.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>

```
### Passwords

> `/System/Applications/Passwords.app/Contents/MacOS/Passwords`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Passwords.ChangePasswordForMe</string>
+		<string>Passwords.SecurityRecommendations</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.personas.no.inherit</key>
+	<true/>
 	<key>com.apple.private.safari.automatic-password-change</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
 		<string>/Library/Containers/com.apple.Safari/Container.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>

```
### Photos

> `/System/Applications/Photos.app/Contents/MacOS/Photos`

```diff

 	</array>
 	<key>com.apple.private.cloudphotod.access</key>
 	<string>management</string>
-	<key>com.apple.private.cmphoto.decodeallowlist</key>
-	<dict>
-		<key>DICOM</key>
-		<array>
-			<integer>1684237600</integer>
-		</array>
-		<key>HEIF</key>
-		<array>
-			<integer>1635148593</integer>
-			<integer>1752589105</integer>
-			<integer>1635135537</integer>
-			<integer>1634743416</integer>
-			<integer>1634743400</integer>
-			<integer>1634755432</integer>
-			<integer>1634755438</integer>
-			<integer>1634755443</integer>
-			<integer>1634755439</integer>
-			<integer>1634759278</integer>
-			<integer>1634759272</integer>
-			<integer>1634742888</integer>
-			<integer>1634742376</integer>
-			<integer>1634759276</integer>
-			<integer>1936484717</integer>
-			<integer>1835821411</integer>
-			<integer>1785750887</integer>
-		</array>
-		<key>JFIF</key>
-		<array>
-			<integer>1785750887</integer>
-		</array>
-		<key>JPEG-XL</key>
-		<array>
-			<integer>1786276963</integer>
-			<integer>1786276896</integer>
-		</array>
-	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### Podcasts

> `/System/Applications/Podcasts.app/Contents/MacOS/Podcasts`

```diff

 	<array/>
 	<key>com.apple.developer.carplay-audio</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.pass-type-identifiers</key>
 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>243LU875E5.com.apple.podcasts</string>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.excludes-extensions</key>

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.podcasts</string>
+	</dict>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.fpsd.client</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.absd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>

 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.cache_delete</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>

```
### Shortcuts

> `/System/Applications/Shortcuts.app/Contents/MacOS/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.ExternalProviderService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.InternalBiome</key>

 		<string>holidayEvent</string>
 		<string>sportsTeams</string>
 	</array>
+	<key>com.apple.private.launchservices.disclaimroleasparentapplication</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.proactivepredictions</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Shortcuts_Generator/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.generativeexperiences.ExternalProviderService</string>
 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.intelligenceplatform.InternalBiome</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siriactionsd.xpc</string>
 		<string>com.apple.sirittsd</string>
+		<string>com.apple.toolkitd.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.TimeMachine</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.voiceservices</string>
 		<string>com.apple.voicetrigger</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.soundscapes.picker</key>
 	<true/>
+	<key>com.apple.toolkit.request-immediate-indexing.allow</key>
+	<true/>
+	<key>com.apple.toolkit.request-reindex.allow</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1025382176</string>
 	<key>keychain-access-groups</key>

```
### TV

> `/System/Applications/TV.app/Contents/MacOS/TV`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceAppleEvents</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>

```
### Activity Monitor

> `/System/Applications/Utilities/Activity Monitor.app/Contents/MacOS/Activity Monitor`

```diff

 	<true/>
 	<key>com.apple.private.launchservices.allowedtoget.LSPluginBundleIdentifierKey</key>
 	<true/>
+	<key>com.apple.private.systemstats.analysis-client</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>
 	<string>com.apple.ActivityMonitor</string>
 	<key>com.apple.sysmond.client</key>

```
### Magnifier

> `/System/Applications/Utilities/Magnifier.app/Contents/MacOS/Magnifier`

```diff

 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceSpeechRecognition</string>
 	</array>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.assets.pictures.read-write</key>
 	<true/>
 	<key>com.apple.security.device.camera</key>

 	<true/>
 	<key>com.apple.security.device.usb</key>
 	<true/>
-	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<key>com.apple.security.files.downloads.read-write</key>
+	<true/>
+	<key>com.apple.security.files.user-selected.read-write</key>
+	<true/>
+	<key>com.apple.security.network.client</key>
+	<true/>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>IOSurfaceRootUserClient</string>
+		<string>/Library/Accessibility</string>
+		<string>/Library/Services</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Application Support/CrashReporter</string>
+		<string>/Library/Autosave Information</string>
+		<string>/Library/Input Methods</string>
+		<string>/Library/Keyboard Layouts</string>
+	</array>
+	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
+	<array>
+		<string>AGXDeviceUserClient</string>
+		<string>AppleKeyStoreUserClient</string>
+		<string>AppleNVMeEANUC</string>
 		<string>H15ANEInDirectPathClient</string>
 		<string>IOSurfaceAcceleratorClient</string>
+		<string>IOSurfaceRootUserClient</string>
 	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.siriknowledged.koa.donate</string>
-		<string>com.apple.accessibility.AXSpringBoardServer</string>
-		<string>com.apple.modelmanager</string>
-		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.CameraOverlayAngel.application-service</string>
+		<string>com.apple.UsageTrackingAgent</string>
+		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.audio.AudioComponentRegistrar.daemon</string>
+		<string>com.apple.audio.SystemSoundServer-OSX</string>
+		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.campo</string>
+		<string>com.apple.coreservices.lsuseractivitymanager.xpc</string>
+		<string>com.apple.coreservices.sharedfilelistd.xpc</string>
+		<string>com.apple.corespeech.corespeechd.xpc</string>
+		<string>com.apple.corespeech.xpc</string>
+		<string>com.apple.mediaanalysisd.analysis</string>
+		<string>com.apple.metadata.mds.legacy</string>
+		<string>com.apple.metadata.mdwrite</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.siriknowledged.koa.donate</string>
+		<string>com.apple.synapse.backlink-service</string>
+		<string>com.apple.touchbarserver.mig</string>
+		<string>com.apple.translation.text</string>
+		<string>com.apple.translationd</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.applemultitouchtrackpad</string>
+		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.support</string>
+		<string>com.apple.coregraphics</string>
+		<string>com.apple.generativefunctions.generativefunctionsinstrumentation</string>
+		<string>com.apple.speech.recognition.applespeechrecognition.prefs</string>
+		<string>com.apple.speech.synthesis.general.prefs</string>
+		<string>kCFPreferencesAnyApplication</string>
+		<string>pbs</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.Accessibility</string>
 		<string>com.apple.Accessibility.Assets</string>
 		<string>com.apple.Accessibility.Magnifier</string>
 		<string>com.apple.AccessibilityUIServer</string>
+		<string>com.apple.HIToolbox</string>
+		<string>com.apple.Magnifier</string>
+		<string>com.apple.SpeakSelection</string>
+		<string>com.apple.accessibility.AccessibilityReader</string>
+		<string>com.apple.universalaccess</string>
 	</array>
-	<key>com.apple.security.files.downloads.read-write</key>
-	<true/>
-	<key>com.apple.security.files.user-selected.read-write</key>
-	<true/>
 	<key>com.apple.security.ts.ane-client</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### Accessibility Reader

> `/System/Library/CoreServices/Accessibility Reader.app/Contents/MacOS/Accessibility Reader`

```diff

 	<true/>
 	<key>com.apple.private.accessibility.forceBundleLoad</key>
 	<true/>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/Contents/MacOS/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.private.acccessibility.motionTrackingClient</key>
 	<true/>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
 	<key>com.apple.private.application-service-browse</key>

 		<string>com.apple.keyboard</string>
 		<string>com.apple.springboard</string>
 		<string>com.apple.assistant.logging</string>
-		<string>com.apple.Preferences</string>
 		<string>com.apple.UIKit</string>
 		<string>com.apple.CloudKit</string>
 		<string>com.apple.coreaudio</string>

 		<string>com.apple.UIKit</string>
 		<string>com.apple.preferences-framework</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.Preferences</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### AuthorizationPromptService

> `/System/Library/CoreServices/AuthorizationPromptService.app/Contents/MacOS/AuthorizationPromptService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### ControlCenter

> `/System/Library/CoreServices/ControlCenter.app/Contents/MacOS/ControlCenter`

```diff

 	<true/>
 	<key>com.apple.private.CommandAndControl.utility</key>
 	<true/>
+	<key>com.apple.private.DictationIM.feedback</key>
+	<true/>
 	<key>com.apple.private.MobileActivation</key>
 	<array>
 		<string>GetActivationState</string>

```
### Dock

> `/System/Library/CoreServices/Dock.app/Contents/MacOS/Dock`

```diff

 	</dict>
 	<key>com.apple.private.SkyLight.displaycontrol</key>
 	<true/>
+	<key>com.apple.private.SkyLight.event-capture.direct-touch</key>
+	<true/>
 	<key>com.apple.private.SkyLight.screencapturedirect</key>
 	<true/>
 	<key>com.apple.private.SkyLight.systemgestures</key>

```
### Dwell Control

> `/System/Library/CoreServices/Dwell Control.app/Contents/MacOS/Dwell Control`

```diff

 	<true/>
 	<key>com.apple.private.accessibility.remoteDeviceContent</key>
 	<true/>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### Enhanced Logging

> `/System/Library/CoreServices/Enhanced Logging.app/Contents/MacOS/Enhanced Logging`

```diff

 	<string>com.apple.EnhancedLogging</string>
 	<key>com.apple.AppleServiceToolkit.host</key>
 	<true/>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.EnhancedLogging</string>
+	<key>com.apple.developer.associated-domains</key>
+	<array/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

 	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
+	<key>com.apple.private.swc.system-app</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<false/>
 	<key>com.apple.security.attestation.access</key>

```
### MenuBarAgent

> `/System/Library/CoreServices/MenuBarAgent.app/Contents/MacOS/MenuBarAgent`

```diff

 	<true/>
 	<key>com.apple.private.menubar.system-banners</key>
 	<true/>
+	<key>com.apple.private.replicator.controller</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.controlcenter</string>

 	<true/>
 	<key>com.apple.private.sessionkit.sessionFinisher</key>
 	<true/>
+	<key>com.apple.private.sharing.unlock-manager</key>
+	<true/>
 	<key>com.apple.private.skylight.menubaragent</key>
 	<true/>
 	<key>com.apple.private.skylight.plugin-power</key>

 		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.backlightd</string>
+		<string>com.apple.replicatorservices</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.dockling.server</string>
 	</array>

```
### ScreensharingAgent

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/MacOS/ScreensharingAgent`

```diff

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
-		<string>kTCCServicePostEvent</string>
-		<string>kTCCServiceScreenCapture</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### screensharingd

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/MacOS/screensharingd`

```diff

 	<true/>
 	<key>com.apple.private.opendirectory.GetAuthenticationData</key>
 	<true/>
+	<key>com.apple.private.screensharing.xpcaccepted</key>
+	<true/>
 	<key>com.apple.private.sessionagent.spi</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>

```
### SSFileCopySender

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/Support/SSFileCopySender.bundle/Contents/MacOS/SSFileCopySender`

```diff

 <dict>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>kTCCServiceSystemPolicyAllFiles</string>
+		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceMediaLibrary</string>
+		<string>kTCCServiceSystemPolicyDesktopFolder</string>
+		<string>kTCCServiceSystemPolicyDocumentsFolder</string>
+		<string>kTCCServiceSystemPolicyDownloadsFolder</string>
+		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
+		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
+		<string>kTCCServiceFileProviderDomain</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### Setup Assistant

> `/System/Library/CoreServices/Setup Assistant.app/Contents/MacOS/Setup Assistant`

```diff

 	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 	<key>com.apple.private.skylight.plugin-power</key>

```
### mbuseragent

> `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/mbuseragent`

```diff

 	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>

```
### softwareupdated

> `/System/Library/CoreServices/Software Update.app/Contents/Resources/softwareupdated`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.softwareupdated</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>AppleIntelligenceReporting.AssetDelivery</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.SoftwareUpdateController</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.assertion-softwareupdate</key>
 	<true/>
 	<key>com.apple.private.iokit.assertonlidclose</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.sucore.SUCoreHelperService</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.temporary-exception.apple-events</key>
 	<array>

```
### SpotlightPreferenceExtension

> `/System/Library/CoreServices/Spotlight.app/Contents/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension`

```diff

 	<true/>
 	<key>com.apple.private.spotlight.preferences</key>
 	<true/>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-write</key>

```
### Spotlight

> `/System/Library/CoreServices/Spotlight.app/Contents/MacOS/Spotlight`

```diff

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.tipsd</string>

```
### ThermalTrap

> `/System/Library/CoreServices/ThermalTrap.app/Contents/MacOS/ThermalTrap`

```diff

 			<string>com.apple.thermaltrap</string>
 		</dict>
 	</array>
+	<key>com.apple.private.systemstats.analysis-client</key>
+	<true/>
 </dict>
 </plist>
 

```
### UniversalAccessControl

> `/System/Library/CoreServices/UniversalAccessControl.app/Contents/MacOS/UniversalAccessControl`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.admin.writeconfig</key>
 	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>

```
### WidgetRenderer_Activities

> `/System/Library/CoreServices/WidgetRenderer_Activities.app/Contents/MacOS/WidgetRenderer_Activities`

```diff

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceSystemPolicyAppData</string>
+		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>

```

### 🆕 AccessibilitySettingsSearchExtension

> `/System/Library/ExtensionKit/Extensions/AccessibilitySettingsSearchExtension.appex/Contents/MacOS/AccessibilitySettingsSearchExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>NSCameraUsageDescription</key>
	<string>Allows setup of features that use camera</string>
	<key>com.apple.AudioAccessoryServices</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>carrier-settings</string>
	</array>
	<key>com.apple.SiriTTSTrainingAgent.training</key>
	<true/>
	<key>com.apple.accessibility.LiveTranscriptionAgent</key>
	<true/>
	<key>com.apple.accessibility.LiveTranscriptionAgent.xpc</key>
	<true/>
	<key>com.apple.accessibility.axassets</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>AccessibilitySettingsExtension</string>
	<key>com.apple.assistant.dictation.prerecorded</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.bluetooth.xpc</key>
	<true/>
	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
	<string>com.apple.Settings</string>
	<key>com.apple.corespeech.corespeechd.xpc</key>
	<true/>
	<key>com.apple.corespeech.xpc</key>
	<true/>
	<key>com.apple.mediaremoted.xpc</key>
	<true/>
	<key>com.apple.private.CommandAndControl.utility</key>
	<true/>
	<key>com.apple.private.acccessibility.motionTrackingClient</key>
	<true/>
	<key>com.apple.private.accessibility.setVoiceOverAllowedCommands</key>
	<true/>
	<key>com.apple.private.accessibility.visuals</key>
	<true/>
	<key>com.apple.private.admin.writeconfig</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Settings</string>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.TTSAXResourceModelAssets</string>
	</array>
	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
	<true/>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.corespeech.corespeechd.xpc</key>
	<true/>
	<key>com.apple.private.corespeech.xpc</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.accessibility.voicebanking</string>
	</array>
	<key>com.apple.private.security.storage.preferences</key>
	<true/>
	<key>com.apple.private.security.storage.universalaccess</key>
	<true/>
	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceSpeechRecognition</string>
		<string>kTCCServiceVoiceBanking</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceAccessibility</string>
		<string>kTCCServiceListenEvent</string>
	</array>
	<key>com.apple.private.tcc.manager.access.delete</key>
	<array>
		<string>kTCCServiceVoiceBanking</string>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.private.tcc.manager.access.modify</key>
	<array>
		<string>kTCCServiceVoiceBanking</string>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.private.tcc.manager.access.read</key>
	<array>
		<string>kTCCServiceVoiceBanking</string>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.private.viewbridge.window.level</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.accessibility.voicebanking</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.voicebanking.store</string>
		<string>com.apple.voicebanking.services</string>
		<string>com.apple.accessibility.heard</string>
		<string>com.apple.backlightd</string>
		<string>com.apple.server.bluetooth</string>
		<string>com.apple.server.bluetooth.general.xpc</string>
		<string>com.apple.corespeech.corespeechd.xpc</string>
		<string>com.apple.corespeech.xpc</string>
		<string>com.apple.accessibility.LiveTranscriptionAgent</string>
		<string>com.apple.accessibility.LiveTranscriptionAgent.xpc</string>
		<string>com.apple.universalaccessd.startup</string>
		<string>com.apple.universalaccessd.running</string>
		<string>com.apple.universalaccessd</string>
		<string>com.apple.BezelServices</string>
		<string>com.apple.bluetooth.xpc</string>
		<string>com.apple.bluetooth.system</string>
		<string>com.apple.mediaremoted.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.audio-unit-host</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.AccessibilityVisualsAgent</string>
		<string>com.apple.ScreenReaderUIServer</string>
		<string>com.apple.DwellControl.startup</string>
		<string>com.apple.DwellControl.running</string>
		<string>com.apple.accessibility.dfrhud</string>
		<string>com.apple.accessibility.AXVisualSupportAgent.startup</string>
		<string>com.apple.accessibility.AXVisualSupportAgent.running</string>
		<string>com.apple.accessibility.AXVisualSupportAgent</string>
		<string>com.apple.KeyboardAccessAgent</string>
		<string>com.apple.distributed_notifications@1v3</string>
		<string>com.apple.distributed_notifications@Uv3</string>
		<string>com.apple.distributed_notifications@0v3</string>
		<string>com.apple.AssistiveControl.running</string>
		<string>com.apple.AssistiveControl.startup</string>
		<string>com.apple.VoiceOver.running</string>
		<string>com.apple.VoiceOver.startup</string>
		<string>com.apple.universalaccessd.running</string>
		<string>com.apple.universalaccessd.startup</string>
		<string>com.apple.universalaccessd</string>
		<string>com.apple.cmio.registerassistantservice</string>
		<string>com.apple.cmio.VDCAssistant</string>
		<string>com.apple.cmio.registerassistantservice.system-extensions</string>
		<string>com.apple.accessibility.LiveTranscriptionAgent</string>
		<string>com.apple.accessibility.LiveTranscriptionAgent.xpc</string>
		<string>com.apple.app-sandbox.read</string>
		<string>com.apple.app-sandbox.read-write</string>
		<string>com.apple.BezelServices</string>
		<string>com.apple.speech.synthesis.SpeakingHotKeyPort</string>
		<string>com.apple.HearingModeService</string>
		<string>com.apple.AudioAccessoryServices</string>
		<string>com.apple.mediaremoted.xpc</string>
		<string>com.apple.accessory.Hearing</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.local-name</key>
	<array>
		<string>com.apple.distributed_notifications@1v3</string>
		<string>com.apple.distributed_notifications@Uv3</string>
		<string>com.apple.distributed_notifications@0v3</string>
	</array>
	<key>com.apple.security.temporary-exception.sbpl</key>
	<array>
		<string>(allow iokit-get-properties iokit-set-properties)</string>
		<string>(allow distributed-notification-post)</string>
		<string>(allow nvram-get)</string>
		<string>(allow device-camera)</string>
		<string>(allow file-read* (extension "com.apple.app-sandbox.read"))</string>
		<string>(allow file-read* file-write* (subpath  "/Library/Caches/com.apple.KeyboardAccessAgent"))</string>
		<string>(allow file-issue-extension (require-all (extension-class "com.apple.app-sandbox.read" "com.apple.app-sandbox.read-write") (subpath "/Library/Caches/com.apple.KeyboardAccessAgent")))</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.universalaccess</string>
		<string>com.apple.mediaaccessibility</string>
		<string>com.apple.Accessibility</string>
		<string>com.apple.speech.recognition.AppleSpeechRecognition.prefs</string>
		<string>com.apple.speech.synthesis.general.prefs</string>
		<string>com.apple.AppleMultitouchMouse</string>
		<string>com.apple.driver.AppleBluetoothMultitouch.mouse</string>
		<string>com.apple.driver.AppleHIDMouse</string>
		<string>com.apple.AppleMultitouchTrackpad</string>
		<string>com.apple.driver.AppleBluetoothMultitouch.trackpad</string>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.assistant</string>
		<string>com.apple.Siri</string>
		<string>com.apple.accessibility.LiveCaptions</string>
		<string>com.apple.accessibility.LiveTranscriptionAgent</string>
		<string>com.apple.HearingAids</string>
		<string>com.apple.ComfortSounds</string>
		<string>com.apple.symbolichotkeys</string>
	</array>
	<key>com.apple.security.temporary-exception.user-preference.write</key>
	<array>
		<string>com.apple.universalaccess</string>
		<string>com.apple.mediaaccessibility</string>
		<string>com.apple.Accessibility</string>
		<string>com.apple.speech.recognition.AppleSpeechRecognition.prefs</string>
		<string>com.apple.speech.synthesis.general.prefs</string>
		<string>com.apple.AppleMultitouchMouse</string>
		<string>com.apple.driver.AppleBluetoothMultitouch.mouse</string>
		<string>com.apple.driver.AppleHIDMouse</string>
		<string>com.apple.AppleMultitouchTrackpad</string>
		<string>com.apple.driver.AppleBluetoothMultitouch.trackpad</string>
		<string>com.apple.trackpad.scrollBehavior</string>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.assistant</string>
		<string>com.apple.Siri</string>
		<string>com.apple.accessibility.LiveCaptions</string>
		<string>com.apple.accessibility.LiveTranscriptionAgent</string>
		<string>com.apple.symbolichotkeys</string>
	</array>
	<key>com.apple.shortcuts.background-running</key>
	<true/>
	<key>com.apple.shortcuts.library-read-access</key>
	<true/>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>access-call-capabilities</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>406</string>
	</array>
	<key>com.apple.universalaccessd</key>
	<true/>
	<key>com.apple.universalaccessd.running</key>
	<true/>
	<key>com.apple.universalaccessd.startup</key>
	<true/>
	<key>com.apple.voicebanking.services</key>
	<true/>
</dict>
</plist>

```
### AssetMetrics

> `/System/Library/ExtensionKit/Extensions/AssetMetrics.appex/Contents/MacOS/AssetMetrics`

```diff

 		<string>Sage.Transcript</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>AssetDelivery.UAF.DailyStatus</string>
+		<string>AssetDelivery.UAF.AssetSetStatus</string>
+		<string>AssetDelivery.UAF.DailyScheduledAssetStatus</string>
+		<string>AssetDelivery.UAF.AssetSetAlterActivity</string>
 		<string>Device.KeybagLocked</string>
 		<string>Device.BootSession</string>
 	</array>

 				<string>Siri.SELFProcessedEvent</string>
 				<string>IntelligenceFlow.Transcript.Datastream</string>
 				<string>AssetDelivery.UAF.DailyStatus</string>
+				<string>AssetDelivery.UAF.AssetSetStatus</string>
+				<string>AssetDelivery.UAF.DailyScheduledAssetStatus</string>
+				<string>AssetDelivery.UAF.AssetSetAlterActivity</string>
 				<string>Device.KeybagLocked</string>
 				<string>Device.BootSession</string>
 			</array>

```
### ExclavesInferenceProvider

> `/System/Library/ExtensionKit/Extensions/ExclavesInferenceProvider.appex/Contents/MacOS/ExclavesInferenceProvider`

```diff

 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition</string>
+	</array>
 	<key>com.apple.private.exclaves.conclave-host</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Speech_AutomaticSpeechRecognition/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Speech_AutomaticSpeechRecognition/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.modelcatalog.catalog</string>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/Contents/MacOS/FedStatsPluginDynamic`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
+	<key>com.apple.private.healthkit.read_authorization_bypass</key>
+	<array>
+		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
+		<string>HKQuantityTypeIdentifierStepCount</string>
+		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
+		<string>HKQuantityTypeIdentifierVO2Max</string>
+		<string>HKActivitySummaryTypeIdentifier</string>
+	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.priml.FedStatsPlugin.Dynamic</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Change-PW-for-Me-Recommendations</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Passwords.SecurityRecommendations</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Connectivity-Context</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>FedStats-Safari-Link-Tracking-Protection</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Safari.Navigations</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Generation-Failure-Reason</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Wallet-Order-Extraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>TrustKit.Decisioning.TKWalletOrderExtractionDomains</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Writing-Tools</key>
 		<dict>
 			<key>Streams</key>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/Contents/MacOS/FedStatsPluginStatic`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.healthkit</key>
+	<true/>
+	<key>com.apple.private.healthkit.read_authorization_bypass</key>
+	<array>
+		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
+		<string>HKQuantityTypeIdentifierStepCount</string>
+		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
+		<string>HKQuantityTypeIdentifierVO2Max</string>
+		<string>HKActivitySummaryTypeIdentifier</string>
+	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.priml.FedStatsPlugin.Static</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Change-PW-for-Me-Recommendations</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Passwords.SecurityRecommendations</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Connectivity-Context</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>FedStats-Safari-Link-Tracking-Protection</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Safari.Navigations</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Generation-Failure-Reason</key>
 		<dict>
 			<key>Streams</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Wallet-Order-Extraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>TrustKit.Decisioning.TKWalletOrderExtractionDomains</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Writing-Tools</key>
 		<dict>
 			<key>Streams</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.Photos</string>
 	</array>
+	<key>com.apple.developer.private-cloud-compute</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>

```
### GenerativePartnerPrototypeExtension

> `/System/Library/ExtensionKit/Extensions/GenerativePartnerPrototypeExtension.appex/Contents/MacOS/GenerativePartnerPrototypeExtension`

```diff

 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 	<array>
 		<string>GenerativePartnerPrototypeExtension</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>com.apple.openai</string>
+	</array>
 </dict>
 </plist>
 

```
### InternetAccountsSettingsExtension

> `/System/Library/ExtensionKit/Extensions/InternetAccountsSettingsExtension.appex/Contents/MacOS/InternetAccountsSettingsExtension`

```diff

 	<array>
 		<string>com.apple.PublicCloudStorage</string>
 		<string>com.apple.ProtectedCloudStorage</string>
+		<string>com.apple.managed.account.identities</string>
 	</array>
 	<key>keychain-cloud-circle</key>
 	<true/>

```
### ODDFeatureDigestsExtension

> `/System/Library/ExtensionKit/Extensions/ODDFeatureDigestsExtension.appex/Contents/MacOS/ODDFeatureDigestsExtension`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.ODDFeatureDigestsExtension</string>
+	<string>com.apple.siri.ODDFeatureDigestsExtension</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
+	<key>com.apple.private.assistant.settings</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
-	<string>com.apple.ODDFeatureDigestsExtension</string>
+	<string>com.apple.siri.ODDFeatureDigestsExtension</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Siri.SELFProcessedEvent</string>

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
+	<key>com.apple.private.logging.stream</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
-		<string>com.apple.ODDFeatureDigestsExtension</string>
-		<string>com.apple.poirot.poirot_tool</string>
+		<string>com.apple.siri.ODDFeatureDigestsExtension</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant</string>
+		<string>com.apple.assistant.support</string>
+		<string>com.apple.assistant.backedup</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
-		<string>com.apple.ODDFeatureDigestsExtension</string>
+		<string>com.apple.siri.ODDFeatureDigests.worker</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant</string>
+		<string>com.apple.assistant.support</string>
+		<string>com.apple.assistant.backedup</string>
+	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
-		<string>com.apple.ODDFeatureDigestsExtension</string>
+		<string>com.apple.siri.ODDFeatureDigests.worker</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 PasswordSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/PasswordSettingsAppIntentsExtension.appex/Contents/MacOS/PasswordSettingsAppIntentsExtension`

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

<!-- Launch Constraints (Self) -->
{
  "appl": 1,
  "ccat": 0,
  "comp": 1,
  "reqs": {
    "$or": {
      "on-authorized-authapfs-volume": true,
      "on-system-volume": true
    },
    "validation-category": 1
  },
  "vers": 1
}

<!-- Launch Constraints (Parent) -->
{
  "appl": 1,
  "ccat": 0,
  "comp": 1,
  "reqs": {
    "is-init-proc": true
  },
  "vers": 1
}

```
### PhotoPicker

> `/System/Library/ExtensionKit/Extensions/PhotoPicker.appex/Contents/MacOS/PhotoPicker`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/Contents/MacOS/PhotosPicker`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

```
### PhotosViewService

> `/System/Library/ExtensionKit/Extensions/PhotosViewService.appex/Contents/MacOS/PhotosViewService`

```diff

 	</array>
 	<key>com.apple.private.cloudphotod.access</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.photos.allowassetexpunge</key>
 	<true/>
 	<key>com.apple.private.photos.allowcollectionshare</key>

```

### 🆕 SearchPartnerInferenceProvider

> `/System/Library/ExtensionKit/Extensions/SearchPartnerInferenceProvider.appex/Contents/MacOS/SearchPartnerInferenceProvider`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.external.searchpartner</string>
	<key>com.apple.private.network.system-token-fetch</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.tokengeneration</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.tokengeneration</string>
	</array>
</dict>
</plist>

```
### SiriPreferenceExtension

> `/System/Library/ExtensionKit/Extensions/SiriPreferenceExtension.appex/Contents/MacOS/SiriPreferenceExtension`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
 	<true/>
+	<key>com.apple.generativeexperiences.agentSessionStore</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService.secureWriteCloudSubscriptionFeaturesAvailability</key>

 	<array>
 		<string>kTCCServiceMicrophone</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceSiri</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceSiri</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiri</string>
+	</array>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>
 		<string>read</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.generativeexperiences.agentSessionStore</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.generativeexperiences.agentSessionStore</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### SiriVideoAppIntents

> `/System/Library/ExtensionKit/Extensions/SiriVideoAppIntents.appex/Contents/MacOS/SiriVideoAppIntents`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+</dict>
+</plist>
 

```
### SpotlightPreferenceExtension

> `/System/Library/ExtensionKit/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension`

```diff

 	<true/>
 	<key>com.apple.private.spotlight.preferences</key>
 	<true/>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-write</key>

```
### TGOnDeviceInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/TGOnDeviceInferenceProviderService.appex/Contents/MacOS/TGOnDeviceInferenceProviderService`

```diff

 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeExperiences.TransparencyLog</string>
+		<string>AppleIntelligence.Reporting.Invocation.Step</string>
 	</array>
 	<key>com.apple.private.iokit.kernel-memory-access</key>
 	<true/>

```
### AUHostingServiceXPC

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AUHostingServiceXPC.xpc/Contents/MacOS/AUHostingServiceXPC`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.audio.hosting-service</key>
+	<true/>
 	<key>com.apple.private.viewbridge.window.level</key>
 	<true/>
 	<key>com.apple.security.cs.allow-unsigned-executable-memory</key>

```
### AUHostingServiceXPC_arrow

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AUHostingServiceXPC_arrow.xpc/Contents/MacOS/AUHostingServiceXPC_arrow`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.audio.hosting-service</key>
+	<true/>
 	<key>com.apple.private.viewbridge.window.level</key>
 	<true/>
 	<key>com.apple.security.cs.allow-unsigned-executable-memory</key>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/corespotlightd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/Current/Support/corespotlightd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/Metadata.framework/Versions/A/Support/corespotlightd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/Metadata.framework/Versions/Current/Support/corespotlightd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<array>
 		<string>com.apple.StatusKit.presence</string>
 	</array>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.sharedpclogging</string>

```
### FinanceImageProcessingService

> `/System/Library/Frameworks/FinanceKit.framework/Versions/A/XPCServices/FinanceImageProcessingService.xpc/Contents/MacOS/FinanceImageProcessingService`

```diff

 	<array>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.privacyaccountingd</string>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.appleneuralengine</string>

```
### FinanceImageProcessingService

> `/System/Library/Frameworks/FinanceKit.framework/Versions/Current/XPCServices/FinanceImageProcessingService.xpc/Contents/MacOS/FinanceImageProcessingService`

```diff

 	<array>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.privacyaccountingd</string>
+		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.appleneuralengine</string>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 		<string>FINANCE_ORDER_EXTRACTION</string>
 		<string>FINANCE_BOSKOOP</string>
 		<string>FINANCE_CONFIG</string>
+		<string>FINANCE_RECEIPT_LINKING</string>
 		<string>1291</string>
 	</array>
 	<key>com.apple.trustkit.frauddefensed</key>

```
### mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/Versions/A/XPCServices/mscamerad-xpc.xpc/Contents/MacOS/mscamerad-xpc`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>2</integer>
+	<integer>3</integer>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>

```
### mscamerad-xpc

> `/System/Library/Frameworks/ImageCaptureCore.framework/Versions/Current/XPCServices/mscamerad-xpc.xpc/Contents/MacOS/mscamerad-xpc`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>2</integer>
+	<integer>3</integer>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>

```
### SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

```diff

 <dict>
 	<key>com.apple.ahp</key>
 	<true/>
-	<key>com.apple.private.aqua.createSession</key>
-	<true/>
-	<key>com.apple.private.logind.spi</key>
-	<true/>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>

```
### SecurityAgentHelper-x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-x86_64.xpc/Contents/MacOS/SecurityAgentHelper-x86_64`

```diff

 <dict>
 	<key>com.apple.ahp</key>
 	<true/>
-	<key>com.apple.private.aqua.createSession</key>
-	<true/>
-	<key>com.apple.private.logind.spi</key>
-	<true/>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>

```
### authd

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/authd.xpc/Contents/MacOS/authd`

```diff

 	<true/>
 	<key>com.apple.keystore.filevault</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.ExtractCredential</key>
 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>

```
### authd

> `/System/Library/Frameworks/Security.framework/Versions/Current/XPCServices/authd.xpc/Contents/MacOS/authd`

```diff

 	<true/>
 	<key>com.apple.keystore.filevault</key>
 	<true/>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.ExtractCredential</key>
 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>

```
### Assistive Control

> `/System/Library/Input Methods/Assistive Control.app/Contents/MacOS/Assistive Control`

```diff

 	<true/>
 	<key>com.apple.private.accessibility.secureTap</key>
 	<true/>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>

```
### Panel Editor

> `/System/Library/Input Methods/Assistive Control.app/Contents/Resources/Panel Editor.app/Contents/MacOS/Panel Editor`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAccessibility</string>

```

### 🆕 UniversalAccessPref

> `/System/Library/PreferencePanes/UniversalAccessPref.prefPane/Contents/MacOS/UniversalAccessPref`

- No entitlements *(yet)*
### AccountProfileRemoteViewService

> `/System/Library/PrivateFrameworks/AOSUI.framework/Versions/A/XPCServices/AccountProfileRemoteViewService.xpc/Contents/MacOS/AccountProfileRemoteViewService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.appleaccount.custodian</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.preferences.AppleIDAccount.remoteservice</string>
 	<key>com.apple.authkit.client.internal</key>

```
### AccountProfileRemoteViewService

> `/System/Library/PrivateFrameworks/AOSUI.framework/Versions/Current/XPCServices/AccountProfileRemoteViewService.xpc/Contents/MacOS/AccountProfileRemoteViewService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.appleaccount.custodian</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.preferences.AppleIDAccount.remoteservice</string>
 	<key>com.apple.authkit.client.internal</key>

```
### BundledIntentHandler

> `/System/Library/PrivateFrameworks/ActionKit.framework/PlugIns/BundledIntentHandler.appex/Contents/MacOS/BundledIntentHandler`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.corewifi.mac-addr</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>

```
### agentstored

> `/System/Library/PrivateFrameworks/AgentSessionKitRuntime.framework/Versions/A/agentstored`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.agentsessionstore</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/Contents/MacOS/AppIntentsRunnerXPCService`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.no-container</key>
 	<true/>
+	<key>com.apple.private.update-any-appshortcutsprovider</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>

 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.intelligenceflow.uiContext</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.registry</string>

```
### appstorecomponentsd

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd`

```diff

 	<true/>
 	<key>com.apple.private.jetpackassetd</key>
 	<true/>
+	<key>com.apple.private.jetpackassetd.system-client</key>
+	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```

### 🆕 appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/Versions/A/Resources/appleaccounttransparencyd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.cdp.telemetry</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.accountsd.accountmanager</string>
	</array>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.transparencyd.aet</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.appleaccounttransparency</string>
	</array>
</dict>
</plist>

```

### 🆕 appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/Versions/Current/Resources/appleaccounttransparencyd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.cdp.telemetry</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>com.apple.appleaccounttransparencyd</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.accountsd.accountmanager</string>
	</array>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.transparencyd.aet</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.appleaccounttransparency</string>
	</array>
</dict>
</plist>

```
### AppleCredentialManagerDaemon

> `/System/Library/PrivateFrameworks/AppleCredentialManager.framework/AppleCredentialManagerDaemon`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.daemon.allow</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.devicerestrictedmode.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.transportrestrictedmode.configurewhilelocked.allow</key>

```
### apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
-	<key>com.apple.private.power.notifications</key>
-	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.timed.sources</key>

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.safetyalerts</string>
+	</array>
 	<key>com.apple.timed</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.assistant.shared</string>
+		<string>group.com.apple.assistant.shared.backedup</string>
 		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.siri.recorded-audio</string>
 		<string>group.com.apple.siri.referenceResolution</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.assistant.shared</string>
+		<string>group.com.apple.assistant.shared.backedup</string>
 		<string>group.com.apple.siri.ASR.shared</string>
 		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.weather</string>

 	<true/>
 	<key>com.apple.siri.location</key>
 	<true/>
+	<key>com.apple.siri.scda</key>
+	<true/>
 	<key>com.apple.siri.vocabulary.admin</key>
 	<true/>
 	<key>com.apple.siriknowledged</key>

 		<string>INTELLIGENCE_FLOW_PLAN_RESOLUTION</string>
 		<string>MYRIAD_BOOSTS</string>
 		<string>SEARCH_TOOL_ANSWER_SYNTHESIS</string>
-		<string>SIRI_AUDIO_APP_SELECTION_HOMEACCESSORY</string>
 		<string>SIRI_AUDIO_APP_SELECTION_HOMEPOD</string>
 		<string>SIRI_AUDIO_DISABLE_MEDIA_ENTITY_SYNC</string>
 		<string>SIRI_AUDIO_LAPSED_MUSIC_USER</string>

```
### AuthKitUIMacService

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/Resources/AuthKitUIMacService.app/Contents/MacOS/AuthKitUIMacService`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.authkit.client.owner</key>
+	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
+</dict>
+</plist>
 

```
### AuthKitUIMacService

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/Current/Resources/AuthKitUIMacService.app/Contents/MacOS/AuthKitUIMacService`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.authkit.client.owner</key>
+	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
+</dict>
+</plist>
 

```
### deleted_helper

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper`

```diff

 	<true/>
 	<key>com.apple.private.osanalytics.SubmitLogs.allow</key>
 	<true/>
+	<key>com.apple.private.security.datavault.controller</key>
+	<true/>
 	<key>com.apple.private.vfs.entitled-reserve-access</key>
 	<true/>
 </dict>

```
### callintelligenced

> `/System/Library/PrivateFrameworks/CallIntelligence.framework/callintelligenced`

```diff

 	</array>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.TextUnderstanding.process</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.assistant.client</key>

 	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.agentSessionStore</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.gms.availability</key>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.TextUnderstanding.process</string>
+		<string>com.apple.generativeexperiences.agentSessionStore</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.xpc-service-name</key>
 	<array>

```
### SetStoreUpdateService

> `/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/XPCServices/SetStoreUpdateService.xpc/Contents/MacOS/SetStoreUpdateService`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.ts.mobile-keybag-access</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.SetStoreUpdateService</string>
 	<key>platform-application</key>

```
### SetStoreUpdateService

> `/System/Library/PrivateFrameworks/CascadeSets.framework/Versions/Current/XPCServices/SetStoreUpdateService.xpc/Contents/MacOS/SetStoreUpdateService`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.ts.mobile-keybag-access</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.SetStoreUpdateService</string>
 	<key>platform-application</key>

```
### cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/Support/cloudphotod`

```diff

 	<true/>
 	<key>com.apple.mobile.keybagd.UserManager.sync</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.cloudkit.assetBoundaryKey</key>

```
### com.apple.CloudPhotosConfiguration

> `/System/Library/PrivateFrameworks/CloudPhotoServices.framework/Versions/A/XPCServices/com.apple.CloudPhotosConfiguration.xpc/Contents/MacOS/com.apple.CloudPhotosConfiguration`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
 	<integer>1</integer>
 	<key>com.apple.private.icloud-account-access</key>

```
### com.apple.CloudPhotosConfiguration

> `/System/Library/PrivateFrameworks/CloudPhotoServices.framework/Versions/Current/XPCServices/com.apple.CloudPhotosConfiguration.xpc/Contents/MacOS/com.apple.CloudPhotosConfiguration`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
 	<integer>1</integer>
 	<key>com.apple.private.icloud-account-access</key>

```
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.SiriFeatureStore</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/purpose_auto/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.e5rt.e5bundlecache/</string>

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.locationd.activity</key>
+	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
+	<key>com.apple.locationd.spectator</key>
+	<true/>
+	<key>com.apple.locationd.status</key>
+	<true/>
 	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
 	<true/>
 	<key>com.apple.private.CoreAnalytics.Preferences.write</key>

 	</dict>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
+	<key>com.apple.security.personal-information.location</key>
+	<true/>
 </dict>
 </plist>
 

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 	</array>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.iokit.CoreAnalytics.user</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech`

```diff

 	</array>
 	<key>com.apple.uservault</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.icl</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/Current/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech`

```diff

 	</array>
 	<key>com.apple.uservault</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.icl</string>
+	</array>
 </dict>
 </plist>
 

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 		<string>/Library/CoreDuet/</string>
 		<string>/Library/PeopleSuggester/</string>
 		<string>/Library/Caches/com.apple.corespeech.cat.xpc/</string>
+		<string>/Library/Caches/com.apple.speechmaintenanced/ranked_entity_cache/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 		<string>/Library/Biome/</string>
 	</array>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.corespeech</string>
+		<string>com.apple.icl</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### corespeechd_system

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.polaris.client</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>CLIENT_ENTITLEMENT</string>

 		<string>/Library/CoreDuet/</string>
 		<string>/Library/PeopleSuggester/</string>
 		<string>/Library/Caches/com.apple.corespeech.cat.xpc/</string>
+		<string>/Library/Caches/com.apple.speechmaintenanced/ranked_entity_cache/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
 		<string>/Library/Biome/</string>
 	</array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.polaris.cache</string>
 		<string>com.apple.siri.deviceselection</string>
 		<string>com.apple.account.AppleAccount</string>
 		<string>com.apple.accounts.appleaccount.fullaccess</string>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.corespeech</string>
+		<string>com.apple.icl</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/CoreCapture/BT</string>
+		<string>/private/var/db/com.apple.countryd/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.securityd.ckks</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.WirelessCoexManager</string>
+		<string>com.apple.countryd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 DesktopServicesScriptingHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/Resources/DesktopServicesScriptingHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.responsibility.set-arbitrary</key>
	<true/>
	<key>com.apple.private.security.storage.mobilesync</key>
	<true/>
	<key>com.apple.private.system-extension.app-manager</key>
	<true/>
</dict>
</plist>

```

### 🆕 DesktopServicesScriptingHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/Current/Resources/DesktopServicesScriptingHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.responsibility.set-arbitrary</key>
	<true/>
	<key>com.apple.private.security.storage.mobilesync</key>
	<true/>
	<key>com.apple.private.system-extension.app-manager</key>
	<true/>
</dict>
</plist>

```
### IMDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/Contents/MacOS/IMDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.security.storage.Messages</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Messages/com.apple.imdpersistence.IMDIndexingThrottleHistory.plist</string>
+	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.IMCoreSpotlight</string>

```
### ScreenTimeDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ScreenTimeDiagnosticExtension.appex/Contents/MacOS/ScreenTimeDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 </dict>
 </plist>

```
### DraftingExtension-macOS

> `/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-macOS.appex/Contents/MacOS/DraftingExtension-macOS`

```diff

 	</array>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.siriappintentsd.orchestrator</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.assistant.backedup</string>
 	</array>
-	<key>com.apple.siriappintentsd.orchestrator</key>
-	<true/>
 </dict>
 </plist>
 

```

### 🆕 FileBrowsingPathResolver

> `/System/Library/PrivateFrameworks/FileBrowsingServices.framework/Versions/A/XPCServices/FileBrowsingPathResolver.xpc/Contents/MacOS/FileBrowsingPathResolver`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.FileBrowsingServices.PathResolver</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.FileBrowsingServices.PathResolver</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.CloudDocs</string>
	</array>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.fileprovider.fetch-url</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.lookup</key>
	<dict>
		<key>appGroup</key>
		<array>
			<string>group.com.apple.FileProvider.LocalStorage</string>
			<string>group.com.apple.FileProvider.DomainCaching</string>
		</array>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.librarian.unrestricted-container-access</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.storage.FileProvider</key>
	<true/>
	<key>com.apple.private.security.storage.MobileDocuments</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.FileProvider.LocalStorage</string>
		<string>group.com.apple.FileProvider.DomainCaching</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Mobile Documents/</string>
		<string>/Library/CloudStorage/</string>
		<string>/Library/LiveFiles/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.FileProvider</string>
		<string>com.apple.fileproviderd</string>
		<string>com.apple.FileCoordination</string>
		<string>com.apple.CoreServices.coreservicesd</string>
		<string>com.apple.coreservices.launchservicesd</string>
		<string>com.apple.coreservices.quarantine-resolver</string>
		<string>com.apple.lsd.mapdb</string>
		<string>com.apple.lsd.modifydb</string>
		<string>com.apple.bird</string>
		<string>com.apple.containermanagerd</string>
		<string>com.apple.SystemConfiguration.configd</string>
		<string>com.apple.FSEvents</string>
		<string>com.apple.iconservices</string>
		<string>com.apple.filesystems.fskitd</string>
		<string>com.apple.diskarbitrationd</string>
		<string>com.apple.mobile.keybagd.xpc</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/generativeexperiencesd`

```diff

 	</array>
 	<key>com.apple.private.launchservices.canmodifypreferences</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>GetSystemAppMigrationStatus</string>
+	</array>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
 	<key>com.apple.private.photos.allowassetexpunge</key>

```
### healthd

> `/System/Library/PrivateFrameworks/HealthKit.framework/healthd`

```diff

 	</array>
 	<key>com.apple.private.tcc.kill-on-assumed-identity-authorization-change</key>
 	<true/>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceHealthAccessReminder</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
+		<string>kTCCServiceHealthAccessReminder</string>
 		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.report</key>
+	<array>
+		<string>kTCCServiceHealthAccessReminder</string>
+	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>
 	<array>
 		<string>kTCCServiceMotion</string>

 		<string>com.apple.HealthKit.SensitiveLogsTemporaryEnablement</string>
 		<string>com.apple.nanolifestyle.sessiontrackerapp</string>
 		<string>com.apple.Noise</string>
+		<string>com.apple.powerlogd</string>
 		<string>com.apple.private.health.cardio-fitness</string>
 		<string>com.apple.sleepd</string>
 		<string>com.apple.workout.features.dormancy</string>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.HearingAids</string>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<string>com.apple.homed</string>
 	<key>com.apple.private.ctr.thread</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.fillmore.getTriggerStats</key>
 	<true/>
 	<key>com.apple.private.fillmore.provideEmac</key>

```
### IDSBlastDoorService

> `/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/Versions/A/XPCServices/IDSBlastDoorService.xpc/Contents/MacOS/IDSBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### IDSBlastDoorService

> `/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/Versions/Current/XPCServices/IDSBlastDoorService.xpc/Contents/MacOS/IDSBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/Contents/MacOS/imagent`

```diff

 	</array>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.imagent</string>
+	<key>com.apple.asktod</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.communicationtrustd</key>

 	<array>
 		<string>com.apple.lockdownmoded</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.asktod</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.asktod</string>
 	</array>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd`

```diff

 	<string>com.apple.intelligenceflow.intelligenceflowd</string>
 	<key>com.apple.Archetype.personalContext</key>
 	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>cellular-plan</string>
+		<string>internal</string>
+		<string>notify-all</string>
+		<string>spi</string>
+		<string>data-usage</string>
+		<string>identity</string>
+		<string>phone</string>
+		<string>dm</string>
+	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>

 	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
+	<key>com.apple.fileprovider.fetch-url</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	<true/>
 	<key>com.apple.itunescloudd.private</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.healthkit.medicaliddata</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
-	<dict/>
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
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>defaultResolverInteractions</string>

 	<true/>
 	<key>com.apple.runningboard.assertions.shortcuts</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.siri</key>
+	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.intelligenceflow</string>

 	<true/>
 	<key>com.apple.spotlight.search</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.symptoms.NetworkDiagnostics</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/Versions/A/XPCServices/lockdownmoded`

```diff

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.lockdownmoded.contact-exemptions</string>
+	</array>
 </dict>
 </plist>
 

```
### MapsBlastDoorService

> `/System/Library/PrivateFrameworks/MapsBlastDoorSupport.framework/Versions/A/XPCServices/MapsBlastDoorService.xpc/Contents/MacOS/MapsBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/mediaanalysisd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.shazamkit.allow-signature-generation</key>
 	<true/>
 	<key>com.apple.private.stickers</key>

 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/System/Library/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_AppleEmbeddingModel/purpose_auto/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>

```
### MediaAnalysisBlastDoorService

> `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/Versions/A/XPCServices/MediaAnalysisBlastDoorService.xpc/Contents/MacOS/MediaAnalysisBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### MediaAnalysisBlastDoorService

> `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/Versions/Current/XPCServices/MediaAnalysisBlastDoorService.xpc/Contents/MacOS/MediaAnalysisBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/A/XPCServices/com.apple.photos.ImageConversionService.xpc/Contents/MacOS/com.apple.photos.ImageConversionService`

```diff

 	<array>
 		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
 	</array>
-	<key>com.apple.private.cmphoto.decodeallowlist</key>
-	<dict>
-		<key>DICOM</key>
-		<array>
-			<integer>1684237600</integer>
-		</array>
-		<key>HEIF</key>
-		<array>
-			<integer>1635148593</integer>
-			<integer>1752589105</integer>
-			<integer>1635135537</integer>
-			<integer>1634743416</integer>
-			<integer>1634743400</integer>
-			<integer>1634755432</integer>
-			<integer>1634755438</integer>
-			<integer>1634755443</integer>
-			<integer>1634755439</integer>
-			<integer>1634759278</integer>
-			<integer>1634759272</integer>
-			<integer>1634742888</integer>
-			<integer>1634742376</integer>
-			<integer>1634759276</integer>
-			<integer>1936484717</integer>
-			<integer>1835821411</integer>
-			<integer>1785750887</integer>
-		</array>
-		<key>JFIF</key>
-		<array>
-			<integer>1785750887</integer>
-		</array>
-		<key>JPEG-XL</key>
-		<array>
-			<integer>1786276963</integer>
-			<integer>1786276896</integer>
-		</array>
-	</dict>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/Current/XPCServices/com.apple.photos.ImageConversionService.xpc/Contents/MacOS/com.apple.photos.ImageConversionService`

```diff

 	<array>
 		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
 	</array>
-	<key>com.apple.private.cmphoto.decodeallowlist</key>
-	<dict>
-		<key>DICOM</key>
-		<array>
-			<integer>1684237600</integer>
-		</array>
-		<key>HEIF</key>
-		<array>
-			<integer>1635148593</integer>
-			<integer>1752589105</integer>
-			<integer>1635135537</integer>
-			<integer>1634743416</integer>
-			<integer>1634743400</integer>
-			<integer>1634755432</integer>
-			<integer>1634755438</integer>
-			<integer>1634755443</integer>
-			<integer>1634755439</integer>
-			<integer>1634759278</integer>
-			<integer>1634759272</integer>
-			<integer>1634742888</integer>
-			<integer>1634742376</integer>
-			<integer>1634759276</integer>
-			<integer>1936484717</integer>
-			<integer>1835821411</integer>
-			<integer>1785750887</integer>
-		</array>
-		<key>JFIF</key>
-		<array>
-			<integer>1785750887</integer>
-		</array>
-		<key>JPEG-XL</key>
-		<array>
-			<integer>1786276963</integer>
-			<integer>1786276896</integer>
-		</array>
-	</dict>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Versions/A/Support/mstreamd`

```diff

 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>

```
### HubbleBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/HubbleBlastDoorService.xpc/Contents/MacOS/HubbleBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
+		<string>com.apple.gpumemd.check_in_request</string>
 		<string>com.apple.language.changed</string>
 		<string>com.apple.mobile.keybagd.lock_status</string>
 		<string>com.apple.powerlog.*</string>

```
### MessagesAirlockService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/MessagesAirlockService.xpc/Contents/MacOS/MessagesAirlockService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### MessagesBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/MessagesBlastDoorService.xpc/Contents/MacOS/MessagesBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### UnknownSendersBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/UnknownSendersBlastDoorService.xpc/Contents/MacOS/UnknownSendersBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### HubbleBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/Current/XPCServices/HubbleBlastDoorService.xpc/Contents/MacOS/HubbleBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
+		<string>com.apple.gpumemd.check_in_request</string>
 		<string>com.apple.language.changed</string>
 		<string>com.apple.mobile.keybagd.lock_status</string>
 		<string>com.apple.powerlog.*</string>

```
### MessagesAirlockService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/Current/XPCServices/MessagesAirlockService.xpc/Contents/MacOS/MessagesAirlockService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### MessagesBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/Current/XPCServices/MessagesBlastDoorService.xpc/Contents/MacOS/MessagesBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### UnknownSendersBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/Current/XPCServices/UnknownSendersBlastDoorService.xpc/Contents/MacOS/UnknownSendersBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/searchtoold`

```diff

 		<string>loiEntityRelevanceRanking</string>
 		<string>standardFeatureView</string>
 	</array>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.service.debug</key>

 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 		<string>/Library/Application Support/com.apple.omniSearch.searchtoold/</string>
 	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.assistant.cdm</string>
-		<string>com.apple.photos.service</string>
-		<string>com.apple.photoanalysisd</string>
-		<string>com.apple.apsd</string>
-		<string>com.apple.cloudd</string>
-		<string>com.apple.CompanionLink</string>
-		<string>com.apple.intelligenceplatform.EntityResolution</string>
-		<string>com.apple.intelligenceplatform.Feedback</string>
-		<string>com.apple.intelligenceplatform.View</string>
-		<string>com.apple.locationd.synchronous</string>
-		<string>com.apple.email.maild</string>
-		<string>com.apple.parsecd</string>
-		<string>com.apple.modelmanager</string>
-		<string>com.apple.mediaanalysisd.analysis</string>
-		<string>com.apple.mediaanalysisd.service.public</string>
-		<string>com.apple.searchd</string>
-		<string>com.apple.searchd.background</string>
-		<string>com.apple.linkd.registry</string>
-		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.biome.access.user</string>
-		<string>com.apple.generativeexperiences.availabilityService</string>
-		<string>com.apple.tokengeneration</string>
-		<string>com.apple.CarPlayApp.service</string>
-		<string>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</string>
-		<string>com.apple.proactive.ActionPrediction.predictions</string>
-		<string>com.apple.dmd.policy</string>
-		<string>com.apple.siri.uaf.service</string>
-		<string>com.apple.siri.uaf.subscription.service</string>
-		<string>com.apple.mobileassetd.v2</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.managedcorespotlightd</string>
-		<string>com.apple.triald.namespace-management</string>
-		<string>com.apple.diagnosticpipeline.service</string>
-		<string>com.apple.homed.xpc</string>
-		<string>com.apple.mediaanalysisd.embeddingstore</string>
-		<string>com.apple.generativesearch.server.search</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.spotlightui</string>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.networkserviceproxy.fetch-token</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.photos.service</string>

 		<string>com.apple.omniSearch.answerSynthesis</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.generativesearch.server.search</string>
+		<string>com.apple.mediaanalysisd.analysis</string>
+		<string>com.apple.tokengeneration</string>
+		<string>com.apple.CarPlayApp.service</string>
+		<string>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</string>
+		<string>com.apple.proactive.ActionPrediction.predictions</string>
+		<string>com.apple.dmd.policy</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.triald.namespace-management</string>
+		<string>com.apple.homed.xpc</string>
+		<string>com.apple.mediaanalysisd.embeddingstore</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 		<string>com.apple.fpsd</string>
 		<string>com.apple.fairplayd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.spaceattributiond</string>
 	</array>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### com.apple.PerformanceTrace.PerformanceTraceService

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/Versions/A/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/Contents/MacOS/com.apple.PerformanceTrace.PerformanceTraceService`

```diff

 <dict>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.agx.performance-spi</key>
 	<true/>
+	<key>com.apple.private.kernel.get-kernel-info</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
 	<key>com.apple.private.ktrace-allow</key>

 		<string>AGXDevice</string>
 		<string>AGXSharedUserClient</string>
 		<string>AppleCLPCUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
+		<string>RTBuddyUserClient</string>
 	</array>
+	<key>com.apple.system-task-ports.read</key>
+	<true/>
 </dict>
 </plist>
 

```
### com.apple.PerformanceTrace.PerformanceTraceService

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/Versions/Current/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/Contents/MacOS/com.apple.PerformanceTrace.PerformanceTraceService`

```diff

 <dict>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.agx.performance-spi</key>
 	<true/>
+	<key>com.apple.private.kernel.get-kernel-info</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
 	<key>com.apple.private.ktrace-allow</key>

 		<string>AGXDevice</string>
 		<string>AGXSharedUserClient</string>
 		<string>AppleCLPCUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
+		<string>RTBuddyUserClient</string>
 	</array>
+	<key>com.apple.system-task-ports.read</key>
+	<true/>
 </dict>
 </plist>
 

```
### photolibraryd

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd`

```diff

 	<true/>
 	<key>com.apple.private.cloudphotod.access</key>
 	<string>library</string>
-	<key>com.apple.private.cmphoto.decodeallowlist</key>
-	<dict>
-		<key>DICOM</key>
-		<array>
-			<integer>1684237600</integer>
-		</array>
-		<key>HEIF</key>
-		<array>
-			<integer>1635148593</integer>
-			<integer>1752589105</integer>
-			<integer>1635135537</integer>
-			<integer>1634743416</integer>
-			<integer>1634743400</integer>
-			<integer>1634755432</integer>
-			<integer>1634755438</integer>
-			<integer>1634755443</integer>
-			<integer>1634755439</integer>
-			<integer>1634759278</integer>
-			<integer>1634759272</integer>
-			<integer>1634742888</integer>
-			<integer>1634742376</integer>
-			<integer>1634759276</integer>
-			<integer>1936484717</integer>
-			<integer>1835821411</integer>
-			<integer>1785750887</integer>
-		</array>
-		<key>JFIF</key>
-		<array>
-			<integer>1785750887</integer>
-		</array>
-		<key>JPEG-XL</key>
-		<array>
-			<integer>1786276963</integer>
-			<integer>1786276896</integer>
-		</array>
-	</dict>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.receiver</key>

```
### PlatformSSOUIAgent

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/Support/PlatformSSOUIAgent.app/Contents/MacOS/PlatformSSOUIAgent`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.BackgroundUI</key>
 	<true/>
-	<key>com.apple.private.LocalAuthentication.CallerName</key>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.ExtractCredential</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
 	<true/>
+	<key>com.apple.private.SkyLight.loginwindow</key>
+	<true/>
 	<key>com.apple.private.SoftwareUpdate.Client</key>
 	<true/>
 	<key>com.apple.private.authentication-services.internal-authorization-requests</key>
 	<true/>
+	<key>com.apple.private.avatar.store</key>
+	<true/>
 	<key>com.apple.private.ctk.configuration-allowed-for-bundles</key>
 	<array>
 		<string>com.apple.PlatformSSOToken</string>
 	</array>
 	<key>com.apple.private.platformsso.agent</key>
 	<true/>
+	<key>com.apple.private.skylight.unconditional-activation</key>
+	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### VoiceOver Quickstart

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Resources/VoiceOver Quickstart.app/Contents/MacOS/VoiceOver Quickstart`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
 	<key>com.apple.private.skylight.unconditional-activation</key>

```
### VoiceOver Quickstart

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/Current/Resources/VoiceOver Quickstart.app/Contents/MacOS/VoiceOver Quickstart`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
 	<key>com.apple.private.skylight.unconditional-activation</key>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent`

```diff

 		<string>com.apple.cloudd</string>
 		<string>com.apple.asktod</string>
 		<string>com.apple.UsageTrackingAgent.private</string>
-		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.people.agent</string>

 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.people.agent</string>
 		<string>com.apple.FamilyControlsAgent</string>

```
### siriappintentsd

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/siriappintentsd`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppleIntelligence.Reporting.Invocation.Step</string>
+		<string>SessionResumptionEventBundle</string>
+		<string>SecurityValidationEvent</string>
 	</array>
 	<key>com.apple.private.corespotlight.skgupdater</key>
 	<true/>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/siriinferenced`

```diff

 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.system.opendirectoryd.api</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>

```
### SiriHeadlessService

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService`

```diff

 	<true/>
 	<key>com.apple.assistant.uibridge-service</key>
 	<true/>
+	<key>com.apple.assistantd.odeon-remote</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<array>
 		<string>endpoint-read</string>
 	</array>
+	<key>com.apple.private.homekit</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.necp.match</key>

 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.siri.orchestration.capabilities</string>
+		<string>com.apple.assistantd.odeon-remote</string>
+		<string>com.apple.siri.audiopowerupdate.xpc</string>
 	</array>
 	<key>com.apple.siri.analytics.assistant</key>
 	<true/>
+	<key>com.apple.siri.audiopowerupdate.xpc</key>
+	<true/>
 	<key>com.apple.siri.client_lite</key>
 	<true/>
 	<key>com.apple.siri.deviceselection.allow</key>

```
### StoreKitUIServiceMac

> `/System/Library/PrivateFrameworks/StoreKitUIMac.framework/Versions/A/XPCServices/StoreKitUIServiceMac.xpc/Contents/MacOS/StoreKitUIServiceMac`

```diff

 	<array>
 		<string>group.com.apple.storekit</string>
 	</array>
+	<key>com.apple.appstored.octane</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.payment.all-access</key>

```
### StoreKitUIServiceMac

> `/System/Library/PrivateFrameworks/StoreKitUIMac.framework/Versions/Current/XPCServices/StoreKitUIServiceMac.xpc/Contents/MacOS/StoreKitUIServiceMac`

```diff

 	<array>
 		<string>group.com.apple.storekit</string>
 	</array>
+	<key>com.apple.appstored.octane</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.payment.all-access</key>

```
### TelephonyBlastDoorService

> `/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/XPCServices/TelephonyBlastDoorService.xpc/Contents/MacOS/TelephonyBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.replaykit.sharingsession.notification</string>

```
### ThumbnailsBlastDoorService

> `/System/Library/PrivateFrameworks/ThumbnailsBlastDoorSupport.framework/Versions/A/XPCServices/ThumbnailsBlastDoorService.xpc/Contents/MacOS/ThumbnailsBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### ThumbnailsBlastDoorService

> `/System/Library/PrivateFrameworks/ThumbnailsBlastDoorSupport.framework/Versions/Current/XPCServices/ThumbnailsBlastDoorService.xpc/Contents/MacOS/ThumbnailsBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### UASettingsShortcuts

> `/System/Library/PrivateFrameworks/UniversalAccess.framework/PlugIns/UASettingsShortcuts.appex/Contents/MacOS/UASettingsShortcuts`

```diff

 <dict>
 	<key>com.apple.private.acccessibility.motionTrackingClient</key>
 	<true/>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### Accessibility Tutorial

> `/System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Resources/Accessibility Tutorial.app/Contents/MacOS/Accessibility Tutorial`

```diff

 	<true/>
 	<key>com.apple.private.accessibility.setVoiceOverAllowedCommands</key>
 	<true/>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceOver</string>

```
### Accessibility Tutorial

> `/System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/Current/Resources/Accessibility Tutorial.app/Contents/MacOS/Accessibility Tutorial`

```diff

 	<true/>
 	<key>com.apple.private.accessibility.setVoiceOverAllowedCommands</key>
 	<true/>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.VoiceOver</string>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>App.InFocus</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>CarPlay.Connected</key>
 				<dict>
 					<key>mode</key>

 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.spotlight.search.internal</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Shortcuts_Generator/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.appleaccount</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

```
### WalletBlastDoorService

> `/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/Versions/A/XPCServices/WalletBlastDoorService.xpc/Contents/MacOS/WalletBlastDoorService`

```diff

 		<string>com.apple.analyticsd.running</string>
 		<string>com.apple.asl.remote</string>
 		<string>com.apple.caulk.alloc.audiodump</string>
+		<string>com.apple.caulk.alloc.rtdump</string>
 		<string>com.apple.coreaudio.list_components</string>
 		<string>com.apple.distnote.locale_changed</string>
 		<string>com.apple.language.changed</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/Contents/MacOS/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.ExternalProviderService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.corewifi.mac-addr</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.mode.assertion.user-requested.client-identifiers</key>

 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.shazamkit.allow-external-audio-recording</key>
 	<true/>
 	<key>com.apple.private.shazamkit.allow-internal-audio-recording</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Shortcuts_Generator/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>

 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.ExternalProviderService</string>
 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.TimeMachine</string>

 		<string>com.apple.assistant</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.mobilenotes</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.voiceservices</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/Contents/MacOS/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.ExternalProviderService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.intelligenceflow.contextTool</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>

 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.corewifi.mac-addr</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.mode.assertion.user-requested.client-identifiers</key>

 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.shazamkit.allow-external-audio-recording</key>
 	<true/>
 	<key>com.apple.private.shazamkit.allow-internal-audio-recording</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_Shortcuts_Generator/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.generativeexperiences.ExternalProviderService</string>
 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.intelligenceflow.contextTool</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.TimeMachine</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

```
### WritingToolsViewService

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/XPCServices/WritingToolsViewService.xpc/Contents/MacOS/WritingToolsViewService`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalProviderService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.generativeexperiences.generativeexperiencessession</key>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
+		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 WritingToolsViewService

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/Current/XPCServices/WritingToolsViewService.xpc/Contents/MacOS/WritingToolsViewService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.WritingTools.xpc.WritingToolsViewService</string>
	<key>com.apple.assertiond.system-shell</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.campo-client</key>
	<true/>
	<key>com.apple.duetexpertd.assistant-actions</key>
	<true/>
	<key>com.apple.feedbackd.remote-evaluation</key>
	<true/>
	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
	<true/>
	<key>com.apple.generativeexperiences.ExternalProviderService</key>
	<true/>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.locationd.effective-bundle</key>
	<true/>
	<key>com.apple.locationd.usage-oracle</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/XPCServices/WritingToolsViewService.xpc/Contents/MacOS/WritingToolsViewService</string>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.network.system-token-fetch</key>
	<true/>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.xpc.launchd.app-server</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.sage.textcomposition</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts/</string>
		<string>/Library/Application Support/com.apple.WritingTools/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.sage.textcomposition</string>
		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.linkd.mediator</string>
		<string>com.apple.securityd.systemkeychain</string>
		<string>com.apple.networkserviceproxy</string>
		<string>com.apple.familycircle.agent</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.gms.availability</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.generativepartnerservicesettings</string>
	</array>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
		<string>com.apple.generativeexperiences.ExternalProviderService</string>
		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.generativepartnerservicesettings</string>
		<string>com.apple.siri.generativeassistantsettings</string>
	</array>
	<key>com.apple.shortcuts.stepwise-execution</key>
	<true/>
	<key>com.apple.shortcuts.variable-injection</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.openai</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.Dataclass.Siri

> `/System/Library/iCloudSettings/com.apple.Dataclass.Siri.bundle/Contents/MacOS/com.apple.Dataclass.Siri`

- No entitlements *(yet)*
### GPUIExtension

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.Photos</string>
 	</array>
+	<key>com.apple.developer.private-cloud-compute</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 	</array>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.photos.ImageConversionService</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.modelmanager</string>

```
### SCARemoteView Appex

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/Contents/MacOS/SCARemoteView Appex`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.family.ageRange</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.ManagedSettingsAgent</string>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.SensitiveContentAnalysis.analysishistory</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.ManagedSettingsAgent</string>

```
### BooksDiagnosticExtension

> `/System/iOSSupport/System/Library/PrivateFrameworks/BookLibrary.framework/PlugIns/BooksDiagnosticExtension.appex/Contents/MacOS/BooksDiagnosticExtension`

```diff

 		<string>/Library/Containers/com.apple.iBooksX/Data/Documents/</string>
 		<string>/Library/Containers/com.apple.iBooksX/Data/Library/Application Support/</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 </dict>
 </plist>
 

```
### EnergyKitService

> `/System/iOSSupport/System/Library/PrivateFrameworks/EnergyKitInternal.framework/Versions/A/XPCServices/EnergyKitService.xpc/Contents/MacOS/EnergyKitService`

```diff

 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.EnergyKitService</string>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.wpc.energyservices.keychain</string>

```
### EnergyKitService

> `/System/iOSSupport/System/Library/PrivateFrameworks/EnergyKitInternal.framework/Versions/Current/XPCServices/EnergyKitService.xpc/Contents/MacOS/EnergyKitService`

```diff

 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.EnergyKitService</string>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.wpc.energyservices.keychain</string>

```
### homeenergyd

> `/System/iOSSupport/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.homeenergyd</string>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.homeenergy.utilityonboarding</string>

```

### 🆕 game-mode-detect

> `/usr/bin/game-mode-detect`

- No entitlements *(yet)*

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
### tailspin

> `/usr/bin/tailspin`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.computesafeguards.managing.allow</key>
+	<true/>
 	<key>com.apple.logd.admin</key>
 	<true/>
 	<key>com.apple.private.AppleProcessorTrace.Trace</key>

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.microlocation.connection</key>
+	<true/>
 	<key>com.apple.osintelligence.battery</key>
 	<true/>
 	<key>com.apple.osintelligence.charging</key>

```
### aned

> `/usr/libexec/aned`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.triald</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

```
### aonsensed

> `/usr/libexec/aonsensed`

```diff

 	<true/>
 	<key>com.apple.nearbyinteraction.background</key>
 	<true/>
-	<key>com.apple.polaris.client</key>
-	<true/>
 	<key>com.apple.private.AccessorySensorManager</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<string>/Library/UnifiedAssetFramework</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.polaris.daemon_default</string>
-		<string>com.apple.polaris.systemgraph_v2</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
-		<string>com.apple.polaris.cache</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```
### applekeystored

> `/usr/libexec/applekeystored`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```
### arkitd

> `/usr/libexec/arkitd`

```diff

 	<true/>
 	<key>com.apple.developer.networking.multicast</key>
 	<true/>
-	<key>com.apple.polaris.client</key>
-	<true/>
-	<key>com.apple.polaris.consumer.all-streams</key>
-	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

```
### asktod

> `/usr/libexec/asktod`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>ScreenTimeRequest</string>
+		<string>AskToBuy</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.mediaremote.full-now-playing-read-access</key>
 	<true/>
 	<key>com.apple.private.SkyLight.displaysyncsessioncontrol</key>

```
### centaurid

> `/usr/libexec/centaurid`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.fenceservice</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceWillow</string>
 	</array>

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.Carousel</string>
 		<string>com.apple.CloudKit</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.homed</string>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.cloud</key>
+	<true/>
+	<key>com.apple.private.photos.service.librarymanagement</key>
+	<true/>
 	<key>com.apple.private.replicator.controller</key>
 	<true/>
 	<key>com.apple.private.security.storage.DuetExpertCenter</key>
 	<true/>
 	<key>com.apple.private.security.storage.Mail</key>
 	<true/>
+	<key>com.apple.private.security.storage.PhotosLibraries</key>
+	<true/>
 	<key>com.apple.private.security.storage.proactivepredictions</key>
 	<true/>
 	<key>com.apple.private.sessionkit.listener</key>

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

```
### findmydevice-user-agent

> `/usr/libexec/findmydevice-user-agent`

```diff

 	<string>com.apple.icloud.findmydeviced</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>aps-environment</key>
+	<string>serverPreferred</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

```
### generativelearningd

> `/usr/libexec/generativelearningd`

```diff

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### historicalaudiod

> `/usr/libexec/historicalaudiod`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.audio.AudioComponentRegistrar</key>
+	<true/>
 	<key>com.apple.coreaudio.CanRecordPastData</key>
 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>

 	<array>
 		<string>kTCCServiceMicrophone</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/dev/exfiltration-adc-historicala</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>kern.task_conclave</string>
-		<string>com.apple.audio.orchestrator.registrar.service</string>
-	</array>
-	<key>com.apple.security.exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.coreaudio</string>
-	</array>
-	<key>com.apple.security.exception.sysctl.read-only</key>
-	<array>
-		<string>kern.exclaves_status</string>
-		<string>kern.task_conclave</string>
-	</array>
 </dict>
 </plist>
 

```
### hybridsearchd

> `/usr/libexec/hybridsearchd`

```diff

 		<dict>
 			<key>Sets</key>
 			<dict>
-				<key>TextUnderstanding.Extracted.Order</key>
+				<key>TextUnderstanding.Extracted.DeliveryTracking</key>
 				<dict>
 					<key>mode</key>
 					<string>read-only</string>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>TextUnderstanding.Extracted.DeliveryTracking</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>TextUnderstanding.Extracted.Event</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>TextUnderstanding.Extracted.Order</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
 				<key>TextUnderstanding.Extracted.RestaurantReservation</key>
 				<dict>
 					<key>mode</key>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	</array>
 	<key>com.apple.private.xpc.launchd.reboot</key>
 	<true/>
+	<key>com.apple.rootless.volume.iSCHardware</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>

```
### keybagd

> `/usr/libexec/keybagd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 </dict>
 </plist>
 

```
### managedappsd

> `/usr/libexec/managedappsd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.devicemanagementclient.managedappsd</string>
+	<key>com.apple.private.managedclient.configurationprofiles</key>
+	<true/>
+	<key>com.apple.private.managedclient.configurationprofiles.installsource</key>
+	<string>RemoteManagement</string>
 	<key>com.apple.private.remotemanagement.subscriber</key>
 	<true/>
 	<key>com.apple.private.security.protected-system-container</key>

```
### micactivityd

> `/usr/libexec/micactivityd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.audio.AudioComponentRegistrar</key>
+	<true/>
 	<key>com.apple.private.audio.hal.speaker-tap.user-access</key>
 	<true/>
 	<key>com.apple.private.audio.orchestration.registration</key>

 	<array>
 		<string>kTCCServiceMicrophone</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/dev/exfiltration-adc-micactivity</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.audio.orchestrator.registrar.service</string>
-	</array>
 </dict>
 </plist>
 

```
### mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

 	<true/>
 	<key>com.apple.modelmanager.query</key>
 	<true/>
+	<key>com.apple.private.exclaves.stats-server</key>
+	<true/>
 	<key>com.apple.private.memoryinfo</key>
 	<true/>
 	<key>com.apple.private.memorystatus</key>

```
### mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

 <dict>
 	<key>com.apple.AppleNVMeEAN.allow</key>
 	<true/>
+	<key>com.apple.AppleNVMeSanitize.allow</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.fdr-access</key>

 	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>
 	<true/>
+	<key>com.apple.private.iomfb.set-block</key>
+	<true/>
 	<key>com.apple.private.iowatchdog.user-access</key>
 	<true/>
 	<key>com.apple.private.memorystatus</key>

 		<string>AppleEffaceableStorageUserClient</string>
 		<string>AppleAPFSUserClient</string>
 		<string>IOMobileFramebufferUserClient</string>
+		<string>IOAVControllerConcreteUserClient</string>
 		<string>IOSurfaceRootUserClient</string>
 		<string>IOWatchdogUserClient</string>
 		<string>AppleNVMeEANUC</string>
+		<string>AppleNVMeUserClient</string>
 	</array>
 </dict>
 </plist>

```
### networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.servicesanalytics.xpc</string>
+	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.transparency.privateCloudCompute</key>

```
### ospredictiond

> `/usr/libexec/ospredictiond`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.microlocation.connection</key>
+	<true/>
 	<key>com.apple.osintelligence.battery</key>
 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>

```

### 🆕 polarisd

> `/usr/libexec/polarisd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.afk.user</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.diagnosticpipeline.request</key>
	<true/>
	<key>com.apple.polaris.client</key>
	<true/>
	<key>com.apple.polaris.consumer.all-streams</key>
	<true/>
	<key>com.apple.polaris.producer.all-streams</key>
	<true/>
	<key>com.apple.private.PolarisSystemTransition.access</key>
	<true/>
	<key>com.apple.private.kernel.panic</key>
	<true/>
	<key>com.apple.private.logging.flush-buffers</key>
	<true/>
	<key>com.apple.private.master-sync-generator.user-access</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceMotion</string>
	</array>
	<key>com.apple.pst.ApplePayLockDown</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.logd.admin</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.polaris</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleParavirtDeviceUserClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>IOSurfaceRootUserClient</string>
		<string>NBDisplayControlUserClient</string>
		<string>NBCoreUserClient</string>
		<string>NBTimesyncUserClient</string>
		<string>AFKEndpointInterfaceUserClient</string>
		<string>CompanionMgrEPICUserClient</string>
		<string>AppleCCPUUserClient</string>
		<string>CCPUAppEPICUserClient</string>
		<string>CCPUDebugServiceUserClient</string>
		<string>CCPUPmuServiceUserClient</string>
		<string>CCPUExpertUserClient</string>
		<string>CCPURegSamplerUserClient</string>
		<string>CCPUTestEndpointUserClient</string>
		<string>CCPUSMCSamplerUserClient</string>
		<string>RootDomainUserClient</string>
		<string>SCodecUserClient</string>
		<string>VDKManifestAgentUserClient</string>
		<string>PSTDriverServerUserClient</string>
	</array>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.tailspin.dump-output</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### studentd

> `/usr/libexec/studentd`

```diff

 	<array>
 		<string>group.com.apple.studentd</string>
 	</array>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### tailspind

> `/usr/libexec/tailspind`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.computesafeguards.managing.allow</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

```
### thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

 	<array>
 		<string>com.apple.coreduetd.context</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>RootDomainUserClient</string>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.telemetry</key>
+	<true/>
 	<key>com.apple.cdp.utility</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

```
### triald

> `/usr/libexec/triald`

```diff

 	<true/>
 	<key>com.apple.geoservices.experiments.bucket-id.read</key>
 	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>

```
### triald_system

> `/usr/libexec/triald_system`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 	<string>wifip2pd</string>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.skywalk.observe-all</key>
+	<true/>
+	<key>com.apple.private.skywalk.observe-stats</key>
+	<true/>
 	<key>com.apple.private.skywalk.register-user-pipe</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/db/os_eligibility/</string>
 		<string>/System/Library/IdentityServices/ServiceDefinitions/com.apple.wifip2pd.InactivityConfig.plist</string>
+		<string>/usr/sbin/wifid</string>
+		<string>/usr/sbin/mDNSResponder</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.coreservices.quarantine-resolver</string>
 		<string>com.apple.networkd_privileged</string>
-		<string>com.apple.private.skywalk.observe-stats</string>
 		<string>com.apple.private.nehelper.privileged</string>
 		<string>com.apple.MobileInternetSharing</string>
 		<string>com.apple.analyticsd</string>

```

### 🆕 bluetoothaudiod

> `/usr/sbin/bluetoothaudiod`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.bluetoothaudiod</string>
	<key>com.apple.BTServer.allowRestrictedServices</key>
	<true/>
	<key>com.apple.BTServer.le.att</key>
	<true/>
	<key>com.apple.accessories.transport.allowauth</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.bluetoothaudiod</string>
	<key>com.apple.bluetooth.custom.properties.writable</key>
	<true/>
	<key>com.apple.bluetooth.pairedInfoSecurity</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.bluetoothaudiod.cb</key>
	<true/>
	<key>com.apple.donotdisturb.service</key>
	<true/>
	<key>com.apple.mediaremote.full-now-playing-read-access</key>
	<true/>
	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
	<array>
		<string>com.apple.BTLEServer.ANCS</string>
	</array>
	<key>com.apple.private.siri.activation</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceBluetoothPeripheral</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>RootDomainUserClient</string>
	</array>
	<key>com.apple.siri.activation</key>
	<true/>
	<key>com.apple.siri.external_request</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>access-calls</string>
		<string>modify-calls</string>
	</array>
</dict>
</plist>

```
### diskutil

> `/usr/sbin/diskutil`

```diff

 <dict>
 	<key>com.apple.diskimages.attach</key>
 	<true/>
+	<key>com.apple.diskimages.sla-prompt</key>
+	<true/>
 	<key>com.apple.keystore.filevault</key>
 	<true/>
 	<key>com.apple.private.AuthorizationServices</key>

```


### SystemOS


### 🆕 HybridDatabaseToolUtils

> `/System/Library/PrivateFrameworks/HybridDatabaseToolUtils.framework/Versions/A/HybridDatabaseToolUtils`

- No entitlements *(yet)*
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Passwords.ChangePasswordForMe</string>
+		<string>Passwords.SecurityRecommendations</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.personas.no.inherit</key>
+	<true/>
 	<key>com.apple.private.safari.automatic-password-change</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

 	<array>
 		<string>/Library/Containers/com.apple.Safari/Data/Library/Preferences/</string>
 		<string>/Library/Containers/com.apple.Safari/Data/Library/Safari/AutoFillQuirks.plist</string>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
 		<string>/Library/Containers/com.apple.Safari/Container.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>

```
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/Current/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Passwords.ChangePasswordForMe</string>
+		<string>Passwords.SecurityRecommendations</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.personas.no.inherit</key>
+	<true/>
 	<key>com.apple.private.safari.automatic-password-change</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

 	<array>
 		<string>/Library/Containers/com.apple.Safari/Data/Library/Preferences/</string>
 		<string>/Library/Containers/com.apple.Safari/Data/Library/Safari/AutoFillQuirks.plist</string>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
 		<string>/Library/Containers/com.apple.Safari/Container.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>EnableQuickLookSandboxResources</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>

```
### com.apple.WebKit.WebContent.Development

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>EnableQuickLookSandboxResources</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>EnableQuickLookSandboxResources</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>

```
### com.apple.WebKit.WebContent

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>EnableQuickLookSandboxResources</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>EnableQuickLookSandboxResources</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>

```
### com.apple.WebKit.WebContent.Development

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>EnableQuickLookSandboxResources</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>EnableQuickLookSandboxResources</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>

```
### com.apple.WebKit.WebContent

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>EnableExperimentalSandbox</string>
+		<string>BlockIOKitInWebContentSandbox</string>
+		<string>local:WebContentProcessLaunched</string>
+		<string>EnableQuickLookSandboxResources</string>
+		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>UnifiedPDFEnabled</string>
+		<string>WebProcessDidNotInjectStoreBundle</string>
+		<string>BlockUserInstalledFonts</string>
+	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>
 	<key>com.apple.private.webkit.use-xpc-endpoint</key>

```


### AppOS

### Safari

> `/System/Applications/Safari.app/Contents/MacOS/Safari`

```diff

 		<string>Safari.WebsitesBlockingQuit</string>
 		<string>Safari.Browsing.Assistant</string>
 		<string>Passwords.ChangePasswordForMe</string>
+		<string>Passwords.SecurityRecommendations</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.Events</string>
 		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>

 	<array>
 		<string>/Library/Trial/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>

```
### PasswordManagerBrowserExtensionHelper

> `/System/Library/CoreServices/PasswordManagerBrowserExtensionHelper.app/Contents/MacOS/PasswordManagerBrowserExtensionHelper`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Passwords.ChangePasswordForMe</string>
+		<string>Passwords.SecurityRecommendations</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>

 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Containers/com.apple.Safari/Data/Library/Preferences/</string>
+		<string>/Library/Safari/PasswordBreachStore.plist</string>
 		<string>/Library/Containers/com.apple.Safari/Container.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>

```
### Web App

> `/System/Library/CoreServices/Web App.app/Contents/MacOS/Web App`

```diff

 		<string>Safari.WebsitesBlockingQuit</string>
 		<string>Safari.Browsing.Assistant</string>
 		<string>Passwords.ChangePasswordForMe</string>
+		<string>Passwords.SecurityRecommendations</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.Events</string>
 		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Passwords.SecurityRecommendations</string>
+	</array>
 	<key>com.apple.private.email</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

```


