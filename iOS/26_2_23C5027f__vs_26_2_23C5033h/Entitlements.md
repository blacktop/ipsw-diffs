## 🔑 Entitlements


### 🆕 KaleidoscopePoster

> `/Applications/KaleidoscopePosterApp.app/Extensions/KaleidoscopePoster.appex/KaleidoscopePoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.WallClockPosters.KaleidoscopePoster</string>
	</array>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```

### 🆕 NTKKaleidoscopeShaders.metallib

> `/Applications/KaleidoscopePosterApp.app/Extensions/KaleidoscopePoster.appex/NTKKaleidoscopeShaders.metallib`

- No entitlements *(yet)*

### 🆕 KaleidoscopePosterApp

> `/Applications/KaleidoscopePosterApp.app/KaleidoscopePosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Posters.KaleidoscopePosterApp</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.composeclient</key>
 	<true/>
 	<key>com.apple.messages.sticker-sharing-level</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.private.WebKit.UnrestrictedApplePay</key>
 	<true/>
+	<key>com.apple.private.accessibility.scrod</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.accounts.bundleidspoofing</key>

```

### 🆕 PridePosterExtension

> `/Applications/PridePosterApp.app/Extensions/PridePosterExtension.appex/PridePosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
</dict>
</plist>

```

### 🆕 PridePosterApp

> `/Applications/PridePosterApp.app/PridePosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PridePoster</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

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
+	</array>
 	<key>com.apple.dmd-access</key>
 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.private.corespeech.audioinjection.xpc</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.siri.sirireaderd</string>
 		<string>com.apple.private.assistant.settings</string>
 		<string>com.apple.sirittsd</string>

```

### 🆕 ExtragalacticPoster

> `/Applications/UnityPosterApp.app/Extensions/ExtragalacticPoster.appex/ExtragalacticPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.WatchFacesWallpaperSupport.ExtragalacticPoster</string>
	</array>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```

### 🆕 RhizomePoster

> `/Applications/UnityPosterApp.app/Extensions/RhizomePoster.appex/RhizomePoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.WatchFacesWallpaperSupport.RhizomePoster</string>
	</array>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```

### 🆕 Unity2025Poster

> `/Applications/UnityPosterApp.app/Extensions/Unity2025Poster.appex/Unity2025Poster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
</dict>
</plist>

```

### 🆕 UnityPoster

> `/Applications/UnityPosterApp.app/Extensions/UnityPoster.appex/UnityPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CARenderServer</string>
		<string>com.apple.coremedia.compressionsession</string>
		<string>com.apple.coremedia.decompressionsession</string>
		<string>com.apple.coremedia.videocodecd.compressionsession</string>
		<string>com.apple.coremedia.videocodecd.compressionsession.xpc</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession.xpc</string>
	</array>
</dict>
</plist>

```

### 🆕 UnityPosterApp

> `/Applications/UnityPosterApp.app/UnityPosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Posters.UnityPosterApp</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### iMessageAppsViewService

> `/Applications/iMessageAppsViewService.app/iMessageAppsViewService`

```diff

 	<true/>
 	<key>com.apple.lightsourcesupport.listener</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.sticker-sharing-level</key>
 	<string>system</string>
 	<key>com.apple.private.avatar.store</key>

```
### CoreServicesUIAgent

> `/System/Library/CoreServices/CoreServicesUIAgent.app/CoreServicesUIAgent`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AGXDeviceUserClient</string>
+		<string>IOSurfaceAcceleratorClient</string>
+		<string>IOSurfaceRootUserClient</string>
+	</array>
 </dict>
 </plist>
 

```
### SafariBookmarksSyncAgent

> `/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.spotlight.IndexAgent</string>
+		<string>com.apple.securityd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<false/>
+	<key>com.apple.private.ids.firewall</key>
+	<true/>
 	<key>com.apple.private.ids.identityservicesd</key>
 	<true/>
 	<key>com.apple.private.ids.idquery-cache</key>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	<true/>
 	<key>com.apple.private.MagnifierAngel.client</key>
 	<true/>
+	<key>com.apple.private.accessibility.scrod</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 	<array>
 		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
 		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
+		<string>GenerativeExperiences.Proactive.UseModelShortcutsProd</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>

```
### com.apple.quicklook.ThumbnailsAgent

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent`

```diff

 	<true/>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.vfs.open-by-id</key>
 	<true/>
 	<key>com.apple.quicklook.extension-host</key>

```

### 🆕 P192HIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/P192HIDServiceFilter.plugin/P192HIDServiceFilter`

- No entitlements *(yet)*
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
-	<key>com.apple.springboard.opensensitiveurl</key>
-	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>fairplay-client</key>

```
### askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.AskPermissionUI</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>1445028844</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 </dict>
 </plist>
 

```
### revisiond

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DocumentRevisions</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.TimeMachine</key>
 	<true/>
 	<key>com.apple.private.security.storage.ciconia</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.UnifiedAssetFramework</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 			</dict>
 		</dict>
 		<key>com.apple.AppleIntelligence.Reporting.Invocation.Step</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 	<true/>
 	<key>com.apple.trustkit.debug.ui</key>
 	<true/>
+	<key>com.apple.private.feedback.centralized-feedback</key>
+	<true/>
 	<key>com.apple.proactive.experiments.responses</key>
 	<true/>
 	<key>com.apple.TextUnderstanding.SmartReplies.Inference</key>

 	<true/>
 	<key>com.apple.CoreRoutine.SafetyMonitor</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.SocialHighlight</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.healthd.server</string>
 		<string>com.apple.proactive.experiments.responses</string>
 		<string>com.apple.TextUnderstanding.SmartReplies.Inference</string>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.feedback.centralized-feedback</key>
+	<true/>
 	<key>com.apple.private.game-center</key>
 	<array>
 		<string>Account</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.routined.safetyMonitor</string>
 		<string>com.apple.proactive.experiments.responses</string>
 		<string>com.apple.FileProvider</string>

```
### IMTranscoderAgent

> `/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/IMTranscoderAgent`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.pac.shared_region_id</key>

```
### IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/IMTransferAgent`

```diff

 	</array>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
 	<true/>
 	<key>com.apple.pac.shared_region_id</key>

```
### installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
 		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/db/com.apple.countryd/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>

 	<array>
 		<string>prefs:</string>
 		<string>x-apple-health:</string>
+		<string>settings-navigation:</string>
 	</array>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>

```
### jetpackassetd

> `/System/Library/PrivateFrameworks/JetCore.framework/Support/jetpackassetd`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.jetpackassetd</string>
+	<key>com.apple.symptom_analytics.query</key>
+	<true/>
+	<key>com.apple.symptoms.NetworkOfInterest</key>
+	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
-		<string>com.apple.MobileAsset.MigrationKit</string>
+		<string>com.apple.MobileAsset.OSMigration</string>
 	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

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
 		<string>App.InFocus</string>

 	<true/>
 	<key>com.apple.private.people</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/ScreenTimeDiagnostics/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstored.xpc.request</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.system</string>

```
### fitcoresessiond

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcoresessiond`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.heartratecoordinator.spi.heartrate</key>
+	<true/>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>HealthKitWorkout</string>

 		<string>com.apple.audio.AudioSession</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.AudioAccessoryServices</string>
+		<string>com.apple.heartratecoordinatord.requestor</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

```
### spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.springboard.backgroundappservices</string>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>UsageTracking</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.MediaUsage</string>
+				<string>App.WebUsage</string>
+				<string>Media.NowPlaying</string>
+				<string>ScreenTime.AppUsage</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/preferences/com.apple.networkd.plist</string>

```
### FindMy

> `/private/var/staged_system_apps/FindMy.app/FindMy`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.FindMyDevice.FindMyServiceValidation.access</key>
+	<true/>
 	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>
 	<array>
 		<string>com.apple.radios.plist</string>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.alloy.ids</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.appstored</key>

 	</array>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.fitness.artwork</string>
+	</array>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.in-app-payments</key>

 		<string>com.apple.aeroml.intentrecommend.mediasuggester</string>
 		<string>com.apple.siri.external_request</string>
 		<string>com.apple.sirittsd</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.UserAlerts.destinations</key>
+	<array>
+		<string>com.apple.CarPlay.UserAlerts</string>
+	</array>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.yelp.defaultaccess</key>

 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.MFAAuthentication.MFAANetwork</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.CarPlayApp.user-alerts-service</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### MobileCal

> `/private/var/staged_system_apps/MobileCal.app/MobileCal`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.developer.associated-domains</key>
+	<array/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.suggestions.events</key>
 	<true/>
+	<key>com.apple.private.swc.system-app</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.messages.sticker-sharing-level</key>
 	<string>messages</string>
 	<key>com.apple.mobile.deleted.AllowFreeSpace</key>

```
### MessagesAssistantExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.private.CallHistory.read</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### MessagesAssistantUIExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantUIExtension.appex/MessagesAssistantUIExtension`

```diff

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.contacts</key>

```
### MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### MessagesPluginNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesPluginNotificationExtension.appex/MessagesPluginNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

```
### MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.message-payload-provider.host</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### RemindersWidgetExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
+	<true/>
+	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.sessionkit.custom-platter-target</key>
+	<true/>
 	<key>com.apple.private.sessionkit.listener</key>
 	<true/>
+	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
+	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

```
### perfpowermetricd

> `/usr/bin/perfpowermetricd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	</array>
 	<key>com.apple.private.networkextension.configuration</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>

```
### appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

 		<key>value</key>
 		<string>/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService</string>
 	</dict>
+	<key>com.apple.private.eligibilityd.fetchNewestPolicies</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothAlways</string>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.findmydeviced.aoverc</string>

```
### fseventsd

> `/usr/libexec/fseventsd`

```diff

 	<true/>
 	<key>com.apple.private.vfs.fsevents-activity-watcher</key>
 	<true/>
+	<key>com.apple.rootless.datavault.metadata</key>
+	<true/>
 	<key>com.apple.rootless.storage.SystemPolicyAllFiles</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### hidd

> `/usr/libexec/hidd`

```diff

 	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.kernel.work-interval</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceListenEvent</string>

```
### installd

> `/usr/libexec/installd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.can-register-install-results</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.mobile.installd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>AppInstallEvents</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>App.Installation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.keychain.appclipdeletion</key>

```
### lsd

> `/usr/libexec/lsd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
+	<key>com.apple.private.security.storage.FileProvider</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>allow-softwareupdated</key>
+	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.mobileassetd</string>
 	<key>aps-connection-initiate</key>

```
### nehelper

> `/usr/libexec/nehelper`

```diff

 		<string>com.apple.certificates</string>
 		<string>com.apple.managed.vpn.shared</string>
 		<string>com.apple.terminusd.local-identity</string>
+		<string>com.apple.narrativecertd</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

```
### safarifetcherd

> `/usr/libexec/safarifetcherd`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.securityd</string>
+	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.Safari.WBSDevice</string>
 	</array>
 	<key>vm-pressure-level</key>
 	<true/>

```
### safetycheckd

> `/usr/libexec/safetycheckd`

```diff

 		<string>NULL/ActivationPrivateKey</string>
 		<string>NULL/DeviceCertificate</string>
 	</array>
+	<key>com.apple.private.network.delegation-whitelist</key>
+	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
 	<key>com.apple.private.security.storage.Notes</key>

```
### trustd

> `/usr/libexec/trustd`

```diff

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.trustd</string>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Device.Networking.TLS</string>
+	</array>
 	<key>com.apple.private.keychain.certificates</key>
 	<true/>
 	<key>com.apple.private.necp.match</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>seatbelt-profiles</key>
 	<array>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<true/>
 	<key>com.apple.appletv.pbs.person-monitor-service-access.write</key>
 	<true/>
+	<key>com.apple.appletv.pbs.profile-picker-service-access</key>
+	<true/>
+	<key>com.apple.appletv.pbs.profile-picker-service-access.read</key>
+	<true/>
 	<key>com.apple.appletv.pbs.user-profiles</key>
 	<true/>
 	<key>com.apple.appletv.pbs.user-profiles.select</key>

```
### visionhwserverd

> `/usr/libexec/visionhwserverd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
-	<key>com.apple.security.exception.files.absolute-path.read-only</key>
-	<string>/private/var/mobile/</string>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<string>/private/var/mobile/tmp/</string>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```
