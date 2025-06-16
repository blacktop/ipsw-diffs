## 🔑 Entitlements

### AdaptiveMusicApp

> `/Applications/AdaptiveMusicApp.app/AdaptiveMusicApp`

```diff

 	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 </dict>
 </plist>
 

```
### Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.systemstatus.publisher</string>
+		<string>com.apple.systemstatus</string>
 		<string>com.apple.applecamerad</string>
 		<string>com.apple.appleh13camerad</string>
 		<string>com.apple.appleh16camerad</string>

 	<true/>
 	<key>com.apple.system.get-hardware-identifiers</key>
 	<true/>
+	<key>com.apple.systemstatus.publisher.domains</key>
+	<array>
+		<string>media</string>
+	</array>
 </dict>
 </plist>
 

```
### GameCenterMessageExtension

> `/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension`

```diff

 		<string>Multiplayer</string>
 		<string>TurnBasedMultiplayer</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.gamecenter</string>
 	<key>com.apple.itunesstored.private</key>

```
### com.apple.Maps.appremoval

> `/System/Library/AppRemovalServices/com.apple.Maps.appremoval.xpc/com.apple.Maps.appremoval`

```diff

 	<array>
 		<string>com.apple.Maps.offline.*</string>
 	</array>
+	<key>com.apple.geoservices.shrinkdb.force</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>UninstallForLaunchServices</string>

```
### CameraSettingsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/CameraSettingsAppIntentsExtension.appex/CameraSettingsAppIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 </dict>
 </plist>
 

```
### acdiagnose

> `/System/Library/Frameworks/Accounts.framework/Support/acdiagnose`

```diff

 	<string>AAACCOUNTS.com.apple.acdiagnose</string>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.game-center</key>
+	<array>
+		<string>Games</string>
+	</array>
 	<key>com.apple.private.install.can-set-install-requestor</key>
 	<true/>
 	<key>com.apple.private.install.distributor-info-source</key>

 		<string>com.apple.fontservicesd</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.gamed</string>
 		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.lsd.installation</string>
 		<string>com.apple.lsd.modifydb</string>

```
### AirPlaySenderService

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/XPCServices/AirPlaySenderService.xpc/AirPlaySenderService`

```diff

 	<array>
 		<string>com.apple.airplay</string>
 		<string>com.apple.airplay.pairing</string>
+		<string>com.apple.pairing</string>
 	</array>
 </dict>
 </plist>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 		<string>SIRI_AUDIO_APP_SELECTION_HOMEPOD</string>
 		<string>SIRI_AUDIO_DISABLE_MEDIA_ENTITY_SYNC</string>
 		<string>SIRI_AUDIO_LAPSED_MUSIC_USER</string>
+		<string>SIRI_AUDIO_STC</string>
 		<string>SIRI_AUDIO_TAPTORADAR_CONFIGURATION</string>
 		<string>SIRI_AUDIO_TTS_BEHAVIOR</string>
 		<string>SIRI_CARPLAY_JARVIS</string>

```
### cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.corespeechd</string>
+	<key>com.apple.account.AppleAccount</key>
+	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.airplay.carplayavvc</key>
 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.account.AppleAccount</string>
+		<string>com.apple.accounts.appleaccount.fullaccess</string>
 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.audio.isolated.historicalaudio.client.service</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>

```

### 🆕 AirPlayDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/AirPlayDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.coremedia.endpoint.xpc</string>
		<string>com.apple.coremedia.routediscoverer.xpc</string>
		<string>com.apple.coremedia.routingcontext.xpc</string>
		<string>com.apple.airplay.endpoint.xpc</string>
		<string>com.apple.mediaexperience.endpoint.xpc</string>
	</array>
</dict>
</plist>

```
### FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.ndoagent</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### revisiond

> `/System/Library/PrivateFrameworks/GenerationalStorage.framework/revisiond`

```diff

 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
 	</array>
+	<key>com.apple.private.vfs.authorized-access</key>
+	<true/>
 	<key>com.apple.private.vfs.fsevents-watcher</key>
 	<true/>
 	<key>com.apple.private.vfs.open-by-id</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
-		<key>RegionalSafetyAnalysisMetrics</key>
-		<dict>
-			<key>Streams</key>
-			<dict>
-				<key>RegionalSafetyAnalysis.Disablement</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-				<key>RegionalSafetyAnalysis.Eligibility</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
-		</dict>
 		<key>com.apple.GenerativeFunctions.PeriodicTasks.InstrumentationUpload</key>
 		<dict>
 			<key>Streams</key>

 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
 	</array>
+	<key>com.apple.private.nsurlsession.impersonate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>

 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.containermanagerd</string>
 		<string>com.apple.controlcenter.remoteservice</string>
+		<string>com.apple.timed.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.AppSupport</string>
 		<string>com.apple.CloudSubscriptionFeatures</string>
 		<string>com.apple.CloudSubscriptionFeatures.followup.engagement</string>
-		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
 		<string>com.apple.CloudSubscriptionFeatures.ticket.cache</string>
 		<string>com.apple.CloudSubscriptionFeatures.cache</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 		<string>com.apple.sage</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.generativeexperiences.corefollowup</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.GenerativeFunctions.generativeexperiencesd</string>
+	<key>com.apple.timed</key>
+	<true/>
 </dict>
 </plist>
 

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 	<string>com.apple.modelcatalogd</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.generativeexperiences.FailureTracking</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.generativeexperiences.FailureTracking</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### PhotosPosterProvider

> `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PlugIns/PhotosPosterProvider.appex/PhotosPosterProvider`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.posterboardservices.services</string>
 		<string>com.apple.posterboardservices.dataModel</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### StocksKitService

> `/System/Library/PrivateFrameworks/StocksKit.framework/XPCServices/StocksKitService.xpc/StocksKitService`

```diff

 		<string>com.apple.StocksKitService</string>
 		<string>com.apple.AppleMediaServices</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>IOSurfaceRootUserClient</string>
+		<string>AppleParavirtDeviceUserClient</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.ts.daemon-container</key>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

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
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Seymour/AirPlayKit/</string>
+		<string>/private/var/mobile/Library/Seymour/</string>
 		<string>/private/var/mobile/Library/DeviceRegistry/</string>
 		<string>/private/var/mobile/Library/CoreDuet/People/</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
+		<string>/private/var/mobile/Media/Downloads/com.apple.UserManagedAssets/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>/Library/MessagesMetaData/NickNameCache/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>Library/Seymour/</string>
-		<string>Media/Downloads/com.apple.UserManagedAssets</string>
-	</array>
+	<array/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.activityawardsd</string>

```
### NewsTag

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag`

```diff

 	<string>ZL6BUSYGB3.com.apple.news.tag</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.chrono.invalidatesOnStorefrontChange</key>
 	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>

 	<array>
 		<string>/Library/News/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.newsd.analytics</string>
+		<string>com.apple.news.ScoringService</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.newscore</string>
 		<string>com.apple.newscore2</string>
 	</array>
-	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.newsd.analytics</string>
-		<string>com.apple.news.ScoringService</string>
-	</array>
 </dict>
 </plist>
 

```
### NewsToday2

> `/private/var/staged_system_apps/News.app/PlugIns/NewsToday2.appex/NewsToday2`

```diff

 	<string>ZL6BUSYGB3.com.apple.news.widget</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.chrono.invalidatesOnStorefrontChange</key>
 	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
 		<string>com.apple.newsd.analytics</string>
 		<string>com.apple.newsd.download</string>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 	<array>
 		<string>com.apple.airplay</string>
 		<string>com.apple.airplay.pairing</string>
+		<string>com.apple.pairing</string>
 	</array>
 	<key>lskdd-client</key>
 	<string>898061433</string>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.icloud.findmydevice.shared-configuration</string>
+		<string>group.com.apple.icloud.findmydevice.followup</string>
 	</array>
 	<key>com.apple.private.system-keychain</key>
 	<true/>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.communicationsfilter</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.fmf.local</string>

```
### gamed

> `/usr/libexec/gamed`

```diff

 	<true/>
 	<key>com.apple.datadetectors.source-write.user</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
 	<array/>
 	<key>com.apple.developer.icloud-container-environment</key>

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
	<key>keychain-access-groups</key>
	<array>
		<string>appleaccount</string>
	</array>
</dict>
</plist>

```

### 🆕 meshnetd

> `/usr/libexec/meshnetd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
</dict>
</plist>

```
### securityd

> `/usr/libexec/securityd`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.siri.findmy</string>
+	</array>
 	<key>com.apple.private.security.storage.CoreKnowledge</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 	<true/>
 	<key>com.apple.rootless.storage.coreknowledge</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.siri.findmy</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>

 		<string>com.apple.carpd.xpc</string>
 		<string>com.apple.caraccessoryframework.gatekeeper</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.ak.anisette.xpc</string>
+		<string>com.apple.ak.auth.xpc</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.medialibraryd.xpc</string>

 		<string>com.apple.IntelligenceTasks</string>
 		<string>com.apple.SiriEntityMatcher</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```
