## 🔑 Entitlements

### filesystem

### App Store

> `/System/Applications/App Store.app/Contents/MacOS/App Store`

```diff

 	<array>
 		<string>com.apple.storagekitd</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
+		<string>com.apple.biometrickitd</string>
 		<string>com.apple.commerce</string>
 		<string>com.apple.appstored.xpc.storequeue</string>
 		<string>com.apple.ak.auth.xpc</string>

```
### Books

> `/System/Applications/Books.app/Contents/MacOS/Books`

```diff

 	<string>production</string>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.background-tasks.continued-processing.inference</key>
+	<true/>
 	<key>com.apple.developer.carplay-audio</key>
 	<true/>
 	<key>com.apple.developer.declared-age-range</key>

 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Logs/AirTraffic/airtraffic.log</string>
+		<string>/Library/Logs/AppAnalytics/</string>
 		<string>/Library/Logs/MobileBackup/MobileBackup.log</string>
 		<string>/Library/Preferences/com.apple.Preferences.plist</string>
 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>

```
### CalendarIntentsExtension

> `/System/Applications/Calendar.app/Contents/Extensions/CalendarIntentsExtension.appex/Contents/MacOS/CalendarIntentsExtension`

```diff

 		<string>appEntityRelevanceRanking</string>
 		<string>personEntityRelevanceRanking</string>
 	</array>
+	<key>com.apple.private.suggestions.events</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCalendar</string>

 		<string>com.apple.dataaccess.dataaccessd</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.suggestd.events</string>
 	</array>
 	<key>com.apple.security.personal-information.calendars</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.iCal</string>
+		<string>com.apple.suggestions</string>
 	</array>
 </dict>
 </plist>

```
### Calendar

> `/System/Applications/Calendar.app/Contents/MacOS/Calendar`

```diff

 	<true/>
 	<key>com.apple.security.files.user-selected.read-write</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```
### FaceTime

> `/System/Applications/FaceTime.app/Contents/MacOS/FaceTime`

```diff

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.conversation-accessibility</key>
+	<true/>
+	<key>com.apple.developer.group-session</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.sensitivecontentanalysis.client</key>

 	<true/>
 	<key>com.apple.private.contactsui</key>
 	<true/>
+	<key>com.apple.private.copresence</key>
+	<true/>
+	<key>com.apple.private.copresence.system-activities</key>
+	<array>
+		<string>com.apple.FaceTime.Accessibility.Captions</string>
+		<string>com.apple.FaceTime.Translation.Interaction</string>
+	</array>
+	<key>com.apple.private.copresence.unaliased-identifiers</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	</array>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
+	<key>com.apple.private.security.storage.Messages</key>
+	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 	<array>
 		<string>/private/tmp/FaceTime/</string>
 		<string>/Library/Preferences/com.apple.conference.plist</string>
+		<string>/Library/MessagesMetaData/NickNameCache/</string>
+		<string>/Library/Messages/NickNameCache/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.logging</string>
 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.Accessibility</string>
+		<string>com.apple.messages.nicknames</string>
 	</array>
 	<key>com.apple.sensitivecontentanalysis.intervention.host</key>
 	<true/>

 		<string>record-calls</string>
 		<string>translate-calls</string>
 		<string>smart-holding</string>
+		<string>accessibility-interpreter</string>
 	</array>
 	<key>com.apple.usersafety.service</key>
 	<array>

```
### FindMy

> `/System/Applications/FindMy.app/Contents/MacOS/FindMy`

```diff

 	<true/>
 	<key>com.apple.icloud.findmydeviced.localfindable</key>
 	<true/>
+	<key>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</key>
+	<true/>
 	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>

```
### FindMyWidgetItems

> `/System/Applications/FindMy.app/Contents/PlugIns/FindMyWidgetItems.appex/Contents/MacOS/FindMyWidgetItems`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.fm</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.chronoservices</string>

 		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
 		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.findmy</string>
+	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```
### FindMyWidgetPeople

> `/System/Applications/FindMy.app/Contents/PlugIns/FindMyWidgetPeople.appex/Contents/MacOS/FindMyWidgetPeople`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.fm</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.chronoservices</string>

 		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
 		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.findmy</string>
+	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```
### Home

> `/System/Applications/Home.app/Contents/MacOS/Home`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents.media-client-id</key>

```
### HomeEnergyWidgetsExtension

> `/System/Applications/Home.app/Contents/PlugIns/HomeEnergyWidgetsExtension.appex/Contents/MacOS/HomeEnergyWidgetsExtension`

```diff

 		<string>com.apple.homeenergyd.xpc</string>
 		<string>com.apple.mobileactivationd</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Home</string>
+		<string>com.apple.HomeEnergyUI</string>
+		<string>com.apple.sync.NanoHome</string>
+	</array>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
 	<key>com.apple.springboard.launchapplications</key>

```
### HomeFeedbackDiagnosticExtension

> `/System/Applications/Home.app/Contents/PlugIns/HomeFeedbackDiagnosticExtension.appex/Contents/MacOS/HomeFeedbackDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>/Library/Caches/com.apple.home/</string>
 		<string>/Containers/Data/Application/</string>
+		<string>/Library/Caches/com.apple.home/</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Containers/Data/Application/</string>
+		<string>/Library/Caches/com.apple.home/</string>
 	</array>
 </dict>
 </plist>

```
### HomeUIUserList

> `/System/Applications/Home.app/Contents/PlugIns/HomeUIUserList.appex/Contents/MacOS/HomeUIUserList`

```diff

 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.ind.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>

```
### HomeWidget

> `/System/Applications/Home.app/Contents/PlugIns/HomeWidget.appex/Contents/MacOS/HomeWidget`

```diff

 		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.internal.studylogd</string>
 		<string>com.apple.itunescloud.in-app-message-service</string>
-		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.matter.native.xpc</string>
 		<string>com.apple.mediasetupd.server</string>

 		<string>com.apple.Home.ControlCenter</string>
 		<string>com.apple.Home.group</string>
 		<string>com.apple.Home.wallpaper</string>
+		<string>com.apple.HomeEnergyUI</string>
 		<string>com.apple.ImageIO</string>
 		<string>com.apple.Maps</string>
 		<string>com.apple.Preferences</string>

```
### GenerativePlaygroundAppIntents

> `/System/Applications/Image Playground.app/Contents/Extensions/GenerativePlaygroundAppIntents.appex/Contents/MacOS/GenerativePlaygroundAppIntents`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>

```
### Mail

> `/System/Applications/Mail.app/Contents/MacOS/Mail`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.passes.add-silently</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

```
### Maps

> `/System/Applications/Maps.app/Contents/MacOS/Maps`

```diff

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.jetpackassetd</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.Maps</string>

 		<string>com.apple.Maps.recents</string>
 		<string>com.apple.weather</string>
 	</array>
+	<key>com.apple.runningboard.jetengine</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.jetpackassetd.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<string>(allow system-socket network-inbound (require-all (socket-domain AF_SYSTEM) (socket-protocol 1)))</string>

```
### Messages

> `/System/Applications/Messages.app/Contents/MacOS/Messages`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.businessservicesd.brandLogo</key>
+	<true/>
 	<key>com.apple.communicationtrustd</key>
 	<array>
 		<string>read</string>

 	<array>
 		<string>kTCCServiceFocusStatus</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.tipsd.discoverability</key>
 	<true/>
 	<key>com.apple.private.translation</key>

```
### MessagesPluginNotificationExtension

> `/System/Applications/Messages.app/Contents/PlugIns/MessagesPluginNotificationExtension.appex/Contents/MacOS/MessagesPluginNotificationExtension`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.asktod</string>
+	</array>
 	<key>com.apple.springboard.homeScreenIconStyle</key>
 	<true/>
 </dict>

```
### Notes

> `/System/Applications/Notes.app/Contents/MacOS/Notes`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.internal.SpotlightAutomationTester</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
 		<string>com.apple.identityservicesd.pds</string>
 		<string>com.apple.rtcreportingd</string>

```
### Photos

> `/System/Applications/Photos.app/Contents/MacOS/Photos`

```diff

 	<array>
 		<string>group.com.apple.tipsnext</string>
 		<string>group.com.apple.Photos.PhotosFileProvider</string>
+		<string>group.com.apple.mobileslideshow.SharedAlbums</string>
 	</array>
 	<key>com.apple.security.assets.movies.read-only</key>
 	<true/>

```

### 🆕 JetIncubation

> `/System/Applications/Podcasts.app/Contents/Frameworks/JetIncubation.framework/Versions/A/JetIncubation`

- No entitlements *(yet)*

### 🆕 PodcastsLogging

> `/System/Applications/Podcasts.app/Contents/Frameworks/PodcastsLogging.framework/Versions/A/PodcastsLogging`

- No entitlements *(yet)*
### Shortcuts

> `/System/Applications/Shortcuts.app/Contents/MacOS/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>
 	<true/>
 	<key>com.apple.proactiveagentplatform.orchestrator</key>

 		<string>com.apple.photos.service</string>
 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>
 		<string>com.apple.proactiveagentplatform.orchestrator</string>
 		<string>com.apple.proactiveagentplatform.toolbox</string>

```
### Siri AI

> `/System/Applications/Siri AI.app/Contents/MacOS/Siri AI`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalProviderService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.agentMediaStore</key>
 	<true/>
 	<key>com.apple.generativeexperiences.agentSessionStore</key>

 	<true/>
 	<key>com.apple.private.menubar.allow</key>
 	<true/>
+	<key>com.apple.private.menubar.campo-takeover</key>
+	<true/>
 	<key>com.apple.private.metadata.exattrs</key>
 	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>

 	<true/>
 	<key>com.apple.private.siri.audiopowerupdate.xpc</key>
 	<true/>
+	<key>com.apple.private.siri.invoke</key>
+	<true/>
+	<key>com.apple.private.siri.invoke.text</key>
+	<true/>
 	<key>com.apple.private.siri.setup</key>
 	<true/>
 	<key>com.apple.private.siriappintentsd.orchestrator</key>

 		<string>com.apple.assistant.uibridge-service</string>
 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.generativeexperiences.corefollowup</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.private.siriappintentsd.orchestrator</string>
 	</array>

 		<string>com.apple.assistant</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.logging</string>
+		<string>com.apple.assistant.public</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.token</string>
 		<string>com.apple.Notes</string>

 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.siri.invoke</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

 		<string>com.apple.assistant</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.logging</string>
+		<string>com.apple.assistant.public</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.token</string>
 		<string>com.apple.Notes</string>

```
### Stocks

> `/System/Applications/Stocks.app/Contents/MacOS/Stocks`

```diff

 	<string>adi-client</string>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.background-tasks.continued-processing.inference</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### Magnifier

> `/System/Applications/Utilities/Magnifier.app/Contents/MacOS/Magnifier`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.Magnifier</string>
+	<key>com.apple.AXMediaUtilitiesService-access</key>
+	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AXMediaUtilitiesService</string>
 		<string>com.apple.CameraOverlayAngel.application-service</string>
 		<string>com.apple.UsageTrackingAgent</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>

```
### usbaudiod

> `/System/Library/Audio/Plug-Ins/usbaudio.bundle/Contents/MacOS/usbaudiod`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.audio.driver.extrinsic.registration</key>
+	<true/>
 	<key>com.apple.private.kernel.work-interval</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/Contents/MacOS/AccessibilityUIServer`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.AXMediaUtilitiesService-access</key>
+	<true/>
 	<key>com.apple.BackBoard.global-mouse-events</key>
 	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>

 	<array>
 		<string>com.apple.Accessibility</string>
 	</array>
+	<key>com.apple.private.device-configuration.provider.allowed-provider-ids</key>
+	<array>
+		<string>com.apple.accessibility.GuidedAccess</string>
+	</array>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.feedback.drafting</key>

 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-group</key>
 	<array>
 		<string>group.com.apple.VoiceOver</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AXMediaUtilitiesService</string>
 		<string>com.apple.Feedback.DraftingExtension.viewservice</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>

 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>
 		<string>com.apple.iphone.axserver</string>
+		<string>com.apple.AXMediaUtilitiesService</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### AirDropUI

> `/System/Library/CoreServices/AirDropUI.app/Contents/MacOS/AirDropUI`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
 	<true/>
+	<key>com.apple.private.airdrop.client</key>
+	<true/>
+	<key>com.apple.private.airdrop.settings</key>
+	<true/>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>SensitiveContentAnalysis.ContentInteractionFlow</string>

```
### ClockAngel

> `/System/Library/CoreServices/ClockAngel.app/Contents/MacOS/ClockAngel`

```diff

 	<true/>
 	<key>com.apple.private.alarmkit.alarmManager</key>
 	<true/>
+	<key>com.apple.private.menubar.allow-scene-override-associated-apps</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>

```
### com.apple.DFRSystemExtra.Siri

> `/System/Library/CoreServices/ControlStrip.app/Contents/XPCServices/com.apple.DFRSystemExtra.Siri.xpc/Contents/MacOS/com.apple.DFRSystemExtra.Siri`

```diff

 	<array>
 		<string>com.apple.system.siri</string>
 	</array>
+	<key>com.apple.private.siri.invoke</key>
+	<true/>
 </dict>
 </plist>
 

```
### FamilyOutOfProcessUIExtension

> `/System/Library/CoreServices/FamilyExtensionHost.app/Contents/Extensions/FamilyOutOfProcessUIExtension.appex/Contents/MacOS/FamilyOutOfProcessUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ScreenTimeAgent.Contacts</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.Contacts</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/Contents/MacOS/GameOverlayUI`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
 	<key>com.apple.runningboard.jetengine</key>

```
### Keychain Circle Notification

> `/System/Library/CoreServices/Keychain Circle Notification.app/Contents/MacOS/Keychain Circle Notification`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.notificationcenter-system</key>

```
### NowPlayingTouchUI

> `/System/Library/CoreServices/NowPlayingTouchUI.app/Contents/MacOS/NowPlayingTouchUI`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.mediaremote.now-playing-read-access</key>
+	<true/>
+	<key>com.apple.mediaremote.send-commands</key>
+	<true/>
 	<key>com.apple.private.DFRSystemExtra</key>
 	<array>
 		<string>com.apple.system.media-play-pause</string>

```

### 🆕 PreloginSystemBannerRenderer

> `/System/Library/CoreServices/PreloginSystemBannerRenderer.app/Contents/MacOS/PreloginSystemBannerRenderer`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.menubar.system-banners</key>
	<true/>
</dict>
</plist>

```
### PreviewShellMac

> `/System/Library/CoreServices/PreviewShellMac.app/Contents/MacOS/PreviewShellMac`

```diff

 <dict>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.dt.previewsd.allowed</key>
 	<true/>
 	<key>com.apple.osanalytics.canusediagnosticmonitor</key>
 	<true/>
+	<key>com.apple.private.chrono-extension-host</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.oop-jit.loader</key>

 	<true/>
 	<key>com.apple.private.viewbridge.preview</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.chronod</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.xcodepreviews</key>

```
### ScreenTimeWidgetExtension

> `/System/Library/CoreServices/Screen Time.app/Contents/PlugIns/ScreenTimeWidgetExtension.appex/Contents/MacOS/ScreenTimeWidgetExtension`

```diff

 		<string>App.InFocus</string>
 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### SiriAppAccessMigrator

> `/System/Library/CoreServices/SiriAppAccessMigrator`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
 		<string>kTCCServiceSiri</string>

```
### SystemUIServer

> `/System/Library/CoreServices/SystemUIServer.app/Contents/MacOS/SystemUIServer`

```diff

 	<true/>
 	<key>com.apple.private.screencapturekit.systemRecording</key>
 	<true/>
+	<key>com.apple.private.siri.invoke</key>
+	<true/>
 	<key>com.apple.private.skylight.statusbar</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### WindowManager

> `/System/Library/CoreServices/WindowManager.app/Contents/MacOS/WindowManager`

```diff

 	<array>
 		<string>WindowManager.StageManager.Toggled</string>
 	</array>
+	<key>com.apple.private.dock.spaces</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
 	<key>com.apple.private.screencapturekit.suppress-screen-indicator</key>

```
### destinationd

> `/System/Library/CoreServices/destinationd`

```diff

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.weather</string>

```
### loginwindow

> `/System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow`

```diff

 	<true/>
 	<key>com.apple.private.hibernation.set-preview</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-monitor</key>
+	<true/>
 	<key>com.apple.private.iokit.assertonlidclose</key>
 	<true/>
 	<key>com.apple.private.iokit.rootdomain-set-property</key>

```
### screencaptureui

> `/System/Library/CoreServices/screencaptureui.app/Contents/MacOS/screencaptureui`

```diff

 <dict>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.screencaptureui</string>
+	<key>com.apple.generativeexperiences.ExternalProviderService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.agentMediaStore</key>
 	<true/>
 	<key>com.apple.private.DFRSystemAppModal</key>

 		<string>com.apple.calaccessd</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.Feedback.DraftingExtension.viewservice</string>
 	</array>

```

### 🆕 DictationPersonalizationFides2Plugin

> `/System/Library/DistributedEvaluation/Plugins/DictationPersonalizationFides2Plugin.desPlugin/Contents/MacOS/DictationPersonalizationFides2Plugin`

- No entitlements *(yet)*

### 🆕 GlobalNNLMFidesPlugin

> `/System/Library/DistributedEvaluation/Plugins/GlobalNNLMFidesPlugin.desPlugin/Contents/MacOS/GlobalNNLMFidesPlugin`

- No entitlements *(yet)*
### AppleIDSettings

> `/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.systempreferences.AppleIDSettings</string>
+	<key>com.apple.authentication-services-core.allow-authentication-request-proxying</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.writer.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.developer.aps-environment</key>

 	<true/>
 	<key>com.apple.private.assistant.settings</key>
 	<true/>
+	<key>com.apple.private.authentication-services.internal-authorization-requests</key>
+	<true/>
 	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
 	<key>com.apple.private.clouddocs.rfa-email-setting</key>

 		<string>com.apple.ak.custodian.xpc</string>
 		<string>com.apple.ak.inheritance.xpc</string>
 		<string>com.apple.ak.walrus.xpc</string>
+		<string>com.apple.ak.appleidpasskey.xpc</string>
 		<string>com.apple.analyticsd</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
 		<string>com.apple.AppSSO.service-xpc</string>

```
### AppleIntelligenceReportingSELFIngestor

> `/System/Library/ExtensionKit/Extensions/AppleIntelligenceReportingSELFIngestor.appex/Contents/MacOS/AppleIntelligenceReportingSELFIngestor`

```diff

 	<true/>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
-	<key>com.apple.private.biome.read-write</key>
+	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>AssetDelivery.UAF.AssetSetAlterActivity</string>
+		<string>AssetDelivery.UAF.AssetSetStatus</string>
 		<string>AssetDelivery.UAF.DailyStatus</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>AssetDelivery.UAF.AssetSetAlterActivity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>AssetDelivery.UAF.AssetSetStatus</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>AssetDelivery.UAF.DailyStatus</key>
 				<dict>
 					<key>mode</key>
-					<string>read-write</string>
+					<string>read-only</string>
 				</dict>
 			</dict>
 		</dict>

```
### AssetMetrics

> `/System/Library/ExtensionKit/Extensions/AssetMetrics.appex/Contents/MacOS/AssetMetrics`

```diff

 		<string>Siri.SELFProcessedEvent</string>
 		<string>Device.KeybagLocked</string>
 		<string>Device.BootSession</string>
+		<string>AppleIntelligence.Reporting.AssetDeliveryLog.Availability</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 				<string>AssetDelivery.UAF.AssetSetAlterActivity</string>
 				<string>Device.KeybagLocked</string>
 				<string>Device.BootSession</string>
+				<string>AppleIntelligence.Reporting.AssetDeliveryLog.Availability</string>
 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.assistant.shared</string>
+	</array>
 	<key>com.apple.private.softwareupdate.preferences</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.assistant.shared</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Application Support/com.apple.appleintelligencereporting.processing/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.feedbacklogger/</string>

```
### DDUIExtension

> `/System/Library/ExtensionKit/Extensions/DDUIExtension.appex/Contents/MacOS/DDUIExtension`

```diff

 	<true/>
 	<key>com.apple.developer.networking.multicast</key>
 	<true/>
+	<key>com.apple.private.airdrop.client</key>
+	<true/>
 	<key>com.apple.private.airdrop.settings</key>
 	<true/>
 	<key>com.apple.private.application-service-browse</key>

```
### ExclavesInferenceProvider

> `/System/Library/ExtensionKit/Extensions/ExclavesInferenceProvider.appex/Contents/MacOS/ExclavesInferenceProvider`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.modelmanager.exclaves.test.internal</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### FaceTimeNotificationExtension

> `/System/Library/ExtensionKit/Extensions/FaceTimeNotificationExtension.appex/Contents/MacOS/FaceTimeNotificationExtension`

```diff

 		<string>translate-calls</string>
 		<string>record-calls</string>
 		<string>smart-holding</string>
+		<string>accessibility-interpreter</string>
 	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>

```
### FamilyOutOfProcessUIExtension

> `/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/Contents/MacOS/FamilyOutOfProcessUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ScreenTimeAgent.Contacts</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.Contacts</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### FamilySettings

> `/System/Library/ExtensionKit/Extensions/FamilySettings.appex/Contents/MacOS/FamilySettings`

```diff

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.people</key>
+	<true/>
 	<key>com.apple.private.safari.can-read-keychain-metadata</key>
 	<true/>
 	<key>com.apple.private.safari.can-remove-keychain-data</key>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/Contents/MacOS/FedStatsMLHostPlugin`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.LinguisticData</string>
+		<string>com.apple.MobileAsset.UAF.LinguisticData</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FedStatsMLHostPluginClassA

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/Contents/MacOS/FedStatsMLHostPluginClassA`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.LinguisticData</string>
+		<string>com.apple.MobileAsset.UAF.LinguisticData</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Health.Medications.AddedMed</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FedStatsMLHostPluginClassB

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/Contents/MacOS/FedStatsMLHostPluginClassB`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.LinguisticData</string>
+		<string>com.apple.MobileAsset.UAF.LinguisticData</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Moments.Stats.EventData</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/Contents/MacOS/FedStatsPluginDynamic`

```diff

 	<true/>
 	<key>com.apple.priml.pfl.Morpheus.allowed</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.LinguisticData</string>
+		<string>com.apple.MobileAsset.UAF.LinguisticData</string>
+	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/Contents/MacOS/FedStatsPluginStatic`

```diff

 	<true/>
 	<key>com.apple.priml.pfl.Morpheus.allowed</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.LinguisticData</string>
+		<string>com.apple.MobileAsset.UAF.LinguisticData</string>
+	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FindMyIntentsExtension

> `/System/Library/ExtensionKit/Extensions/FindMyIntentsExtension.appex/Contents/MacOS/FindMyIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
+	<key>com.apple.locationd.usage_oracle</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.findmy</string>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.icloud.fm</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>

 		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager.simplebeacon</string>
+		<string>com.apple.userprofiles</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.findmy</string>
 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>

 		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager.simplebeacon</string>
+		<string>com.apple.userprofiles</string>
+		<string>com.apple.locationd.desktop.synchronous</string>
+		<string>com.apple.locationd.desktop.registration</string>
+		<string>com.apple.CoreLocation.agent</string>
 	</array>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>

```
### GPNonUIExtension

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/Contents/MacOS/GPNonUIExtension`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>

```
### GenerativeExperiencesSafetyInferenceProvider

> `/System/Library/ExtensionKit/Extensions/GenerativeExperiencesSafetyInferenceProvider.appex/Contents/MacOS/GenerativeExperiencesSafetyInferenceProvider`

```diff

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>

```

### 🆕 PegasusData

> `/System/Library/ExtensionKit/Extensions/PegasusData.appex/Contents/MacOS/PegasusData`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PegasusData</string>
	<key>com.apple.private.extensionkit.host.unsandboxed-extensions-for-extension-points</key>
	<array>
		<string>com.apple.PegasusData</string>
	</array>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.PegasusData</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.PegasusData</string>
		<string>com.apple.poirot.poirot_tool</string>
		<string>group.com.apple.PegasusConfiguration</string>
	</array>
</dict>
</plist>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/Contents/MacOS/PhotosPicker`

```diff

 		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
 		<string>group.com.apple.Photos.PhotosFileProvider</string>
 		<string>group.com.apple.ManagedSettings</string>
+		<string>group.com.apple.mobileslideshow.SharedAlbums</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### ProfilesSettingsExt

> `/System/Library/ExtensionKit/Extensions/ProfilesSettingsExt.appex/Contents/MacOS/ProfilesSettingsExt`

```diff

 	<true/>
 	<key>com.apple.private.mis.trust.set</key>
 	<true/>
-	<key>com.apple.private.remotemanagement.observer</key>
-	<true/>
-	<key>com.apple.private.remotemanagement.subscriber</key>
+	<key>com.apple.private.remotemanagement.settings</key>
 	<true/>
 	<key>com.apple.private.responsibility.set-to-other</key>
 	<true/>

```

### 🆕 SNCFeaturesPlugin

> `/System/Library/ExtensionKit/Extensions/SNCFeaturesPlugin.appex/Contents/MacOS/SNCFeaturesPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.pfl.SNCFeaturesPlugin</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.priml.dev.container</string>
		<string>com.apple.priml.preprod.container</string>
		<string>com.apple.priml.prod.container</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.priml.pfl.plugins</string>
	<key>com.apple.priml.pfl.Morpheus.allowed</key>
	<true/>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.dprivacyd.metadata.allow</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Lighthouse.Ledger.TaskCustomEvent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.priml.crashrecords</string>
		<string>com.apple.priml.participations</string>
		<string>com.apple.priml.submissioncooldown</string>
	</array>
</dict>
</plist>

```
### ScreenTimeAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/Contents/MacOS/ScreenTimeAppIntentsExtension`

```diff

 		<string>App.InFocus</string>
 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### ScreenTimePreferencesExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimePreferencesExtension.appex/Contents/MacOS/ScreenTimePreferencesExtension`

```diff

 		<string>App.InFocus</string>
 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### SecurityPrivacyExtension

> `/System/Library/ExtensionKit/Extensions/SecurityPrivacyExtension.appex/Contents/MacOS/SecurityPrivacyExtension`

```diff

 	<true/>
 	<key>com.apple.private.safari.can-remove-keychain-data</key>
 	<true/>
+	<key>com.apple.private.security.files.bookmarks.manage-revocable</key>
+	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
 	<key>com.apple.private.security.syspolicy.kext-policy-management</key>

```

### 🆕 SiriASRScoringExtension

> `/System/Library/ExtensionKit/Extensions/SiriASRScoringExtension.appex/Contents/MacOS/SiriASRScoringExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.agenticfeedback.siri.asrscoring</string>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.siriappintentsd.orchestrator</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.private.siriappintentsd.orchestrator</string>
	</array>
</dict>
</plist>

```

### 🆕 SiriExtensionsDigestExtension

> `/System/Library/ExtensionKit/Extensions/SiriExtensionsDigestExtension.appex/Contents/MacOS/SiriExtensionsDigestExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.SiriExtensionsDigestExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.SiriExtensionsDigestExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<string>Lighthouse.Ledger.TaskCustomEvent</string>
		</dict>
	</dict>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.logging.stream</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.siri.SiriExtensionsDigestExtension</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.symptom_diagnostics</string>
		<string>com.apple.assistant.settings</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.SiriExtensionsDigest.worker</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.SiriExtensionsDigest.worker</string>
	</array>
</dict>
</plist>

```

### 🆕 SiriLogProcessor

> `/System/Library/ExtensionKit/Extensions/SiriLogProcessor.appex/Contents/MacOS/SiriLogProcessor`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.aiml.siri.SiriLogProcessor</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.aiml.siri.SiriLogProcessor</string>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.aiml.siri.SiriLogProcessor</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SiriLogProcessor</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Siri.PrivateLearning.SELFEvent</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Siri.SELFProcessedEvent</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.aiml.siri.OLEOrchestrator</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.aiml.siri.OLEOrchestrator</string>
	</array>
	<key>com.apple.siri.analytics.assistant</key>
	<array>
		<string>runtime.host</string>
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
+	<key>com.apple.generativeexperiences.ExternalProviderService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.agentSessionStore</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>

```
### SiriSetupSettingsIntents

> `/System/Library/ExtensionKit/Extensions/SiriSetupSettingsIntents.appex/Contents/MacOS/SiriSetupSettingsIntents`

```diff

 	<string>com.apple.Settings</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-only</key>
-	<array>
-		<string>com.apple.voicetrigger</string>
-		<string>com.apple.assistant.settings</string>
-		<string>com.apple.assistant.backedup</string>
-		<string>com.apple.siri</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.assistant.settings</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.voicetrigger</string>
+		<string>com.apple.assistant.settings</string>
+		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.Siri</string>
+	</array>
 </dict>
 </plist>
 

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/Contents/MacOS/SiriSuggestionsLightHousePlugin`

```diff

 	<string>com.apple.siri.SiriSuggestionsLightHousePlugin</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siri.SiriSuggestionsLightHousePlugin</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 	</array>
 	<key>com.apple.private.security.storage.SiriInference</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.tccd</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.tccd</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 SiriTranscriptScoringExtension

> `/System/Library/ExtensionKit/Extensions/SiriTranscriptScoringExtension.appex/Contents/MacOS/SiriTranscriptScoringExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.agenticfeedback.siri.transcriptscoring</string>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.siriappintentsd.orchestrator</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.private.siriappintentsd.orchestrator</string>
	</array>
</dict>
</plist>

```
### TimeMachineSettings

> `/System/Library/ExtensionKit/Extensions/TimeMachineSettings.appex/Contents/MacOS/TimeMachineSettings`

```diff

 	<true/>
 	<key>com.apple.private.admin.writeconfig</key>
 	<true/>
+	<key>com.apple.private.backupd.session</key>
+	<string>TimeMachineSettings</string>
 	<key>com.apple.private.security.storage.TimeMachine</key>
 	<true/>
 	<key>com.apple.private.smb.timemachine-control</key>

```
### TrackpadIntentsExtension

> `/System/Library/ExtensionKit/Extensions/TrackpadIntentsExtension.appex/Contents/MacOS/TrackpadIntentsExtension`

```diff

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.AppleMultitouchTrackpad</string>
 		<string>com.apple.driver.AppleBluetoothMultitouch.trackpad</string>
+		<string>com.apple.spotlight</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 frauddefensepfl

> `/System/Library/ExtensionKit/Extensions/frauddefensepfl.appex/Contents/MacOS/frauddefensepfl`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.pfl.frauddefensepfl</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.priml.dev.container</string>
		<string>com.apple.priml.preprod.container</string>
		<string>com.apple.priml.prod.container</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.priml.pfl.plugins</string>
	<key>com.apple.priml.pfl.Morpheus.allowed</key>
	<true/>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.dprivacyd.allow</key>
	<true/>
	<key>com.apple.private.dprivacyd.metadata.allow</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Lighthouse.Ledger.TaskCustomEvent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.priml.crashrecords</string>
		<string>com.apple.priml.participations</string>
		<string>com.apple.priml.submissioncooldown</string>
	</array>
</dict>
</plist>

```
### apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_checkseal`

```diff

 	<true/>
 	<key>com.apple.private.apfs.get-file-exts</key>
 	<true/>
-	<key>com.apple.private.apfs.lock-container-load</key>
-	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

```
### fsck_apfs

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.get-file-exts</key>
 	<true/>
-	<key>com.apple.private.apfs.lock-container-load</key>
-	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

```
### sm_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/sm_stats`

```diff

 	<true/>
 	<key>com.apple.private.apfs.get-file-exts</key>
 	<true/>
-	<key>com.apple.private.apfs.lock-container-load</key>
-	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

```

### 🆕 CrisisResourceResponsePlugin

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/CrisisResourceResponsePlugin.bundle/Contents/MacOS/CrisisResourceResponsePlugin`

- No entitlements *(yet)*

### 🆕 MusicSnippetProviderPlugin

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/MusicSnippetProviderPlugin.bundle/Contents/MacOS/MusicSnippetProviderPlugin`

- No entitlements *(yet)*

### 🆕 PodcastsSnippetsProvider

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/PodcastsSnippetsProvider.bundle/Contents/MacOS/PodcastsSnippetsProvider`

- No entitlements *(yet)*

### 🆕 SiriFindMySnippetProviderPlugin

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/SiriFindMySnippetProviderPlugin.bundle/Contents/MacOS/SiriFindMySnippetProviderPlugin`

- No entitlements *(yet)*
### accountsd

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Support/accountsd`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
 	<key>com.apple.cdp.utility</key>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.ExchangeAccounts</string>
+	</array>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.email</key>

```
### corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/corespotlightd`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tcc.manager.read.access</key>
+	<key>com.apple.private.tcc.manager.access.read</key>
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
-	<key>com.apple.private.tcc.manager.read.access</key>
+	<key>com.apple.private.tcc.manager.access.read</key>
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
-	<key>com.apple.private.tcc.manager.read.access</key>
+	<key>com.apple.private.tcc.manager.access.read</key>
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
-	<key>com.apple.private.tcc.manager.read.access</key>
+	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>
 	</array>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 		<dict>
 			<key>Sets</key>
 			<dict>
+				<key>AmbientSensing.Activity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>App.Intents.IndexedEntity</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>GenerativeLearningPlatform.Insight</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>GenerativeLearningPlatform.TestItem</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Health.Measurement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Health.Statistics</key>
 				<dict>
 					<key>mode</key>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	<true/>
 	<key>com.apple.fileprovider.extension-host</key>
 	<true/>
+	<key>com.apple.fileprovider.fpck-service</key>
+	<true/>
 	<key>com.apple.fileprovider.import-cookie</key>
 	<true/>
 	<key>com.apple.fileprovider.resolver</key>

 	<true/>
 	<key>com.apple.private.tcc.override-prompt-policy</key>
 	<true/>
+	<key>com.apple.private.usernotifications.bundle-identifiers</key>
+	<array>
+		<string>com.apple.finder</string>
+	</array>
 	<key>com.apple.private.vfs.authorized-access</key>
 	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.photos.service</string>
+		<string>com.apple.usernotifications.listener</string>
 	</array>
 	<key>com.apple.spaceattribution.private</key>
 	<true/>

```
### FinanceImageProcessingService

> `/System/Library/Frameworks/FinanceKit.framework/Versions/A/XPCServices/FinanceImageProcessingService.xpc/Contents/MacOS/FinanceImageProcessingService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.financekit.image-processing</string>
+	<key>com.apple.developer.usersafety.client</key>
+	<string>analysis</string>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.email</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```
### FinanceImageProcessingService

> `/System/Library/Frameworks/FinanceKit.framework/Versions/Current/XPCServices/FinanceImageProcessingService.xpc/Contents/MacOS/FinanceImageProcessingService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.financekit.image-processing</string>
+	<key>com.apple.developer.usersafety.client</key>
+	<string>analysis</string>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 		<key>value</key>
 		<string>com.apple.Passbook</string>
 	</dict>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.email</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
-	<key>com.apple.private.corespotlight.bundleid</key>
-	<string>com.apple.Passbook</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```
### managedappdistributionagent

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributionagent`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

```diff

 	<true/>
 	<key>com.apple.private.allow-weak-reply-port</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.aqua.createSession</key>

```
### SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

```diff

 <dict>
 	<key>com.apple.ahp</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
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
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>

```
### authorizationhost

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/MacOS/authorizationhost`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.User</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.configurationprofiles.bootstraptoken.readonly</key>

```
### authorizationhosthelper.arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.arm64.xpc/Contents/MacOS/authorizationhosthelper.arm64`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
 	<key>com.apple.security.smartcard</key>

```
### authorizationhosthelper.x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/authorizationhost.bundle/Contents/XPCServices/authorizationhosthelper.x86_64.xpc/Contents/MacOS/authorizationhosthelper.x86_64`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
 	<key>com.apple.security.smartcard</key>

```
### authtrampoline

> `/System/Library/Frameworks/Security.framework/authtrampoline`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
+</dict>
+</plist>
 

```
### DeviceActivityReportService

> `/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/A/PlugIns/DeviceActivityReportService.appex/Contents/MacOS/DeviceActivityReportService`

```diff

 	<array>
 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### DeviceActivityReportService

> `/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/Current/PlugIns/DeviceActivityReportService.appex/Contents/MacOS/DeviceActivityReportService`

```diff

 	<array>
 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```

### 🆕 OnDeviceProvider

> `/System/Library/PrivateFrameworks/AgenticFeedbackCore.framework/Versions/A/PlugIns/OnDeviceProvider.bundle/Contents/MacOS/OnDeviceProvider`

- No entitlements *(yet)*

### 🆕 PCCProvider

> `/System/Library/PrivateFrameworks/AgenticFeedbackCore.framework/Versions/A/PlugIns/PCCProvider.bundle/Contents/MacOS/PCCProvider`

- No entitlements *(yet)*

### 🆕 OnDeviceProvider

> `/System/Library/PrivateFrameworks/AgenticFeedbackCore.framework/Versions/Current/PlugIns/OnDeviceProvider.bundle/Contents/MacOS/OnDeviceProvider`

- No entitlements *(yet)*

### 🆕 PCCProvider

> `/System/Library/PrivateFrameworks/AgenticFeedbackCore.framework/Versions/Current/PlugIns/PCCProvider.bundle/Contents/MacOS/PCCProvider`

- No entitlements *(yet)*
### AirPlaySenderService

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/Versions/A/XPCServices/AirPlaySenderService.xpc/Contents/MacOS/AirPlaySenderService`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.mutetoggle</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.volumedown</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.volumeup</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### AirPlaySenderService

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/Versions/Current/XPCServices/AirPlaySenderService.xpc/Contents/MacOS/AirPlaySenderService`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.mutetoggle</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.volumedown</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.volumeup</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/Contents/MacOS/AppIntentsRunnerXPCService`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.dmd.policy</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>AppEntityDonation</key>

```
### ASDAskPermissionExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/Contents/MacOS/ASDAskPermissionExtension`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### appstoreagent

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstoreagent`

```diff

 	<string>com.apple.appstoreagent</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>App.ExtensionUsage</string>
 		<string>App.InFocus</string>
 		<string>OSAnalytics.Stability.Crash</string>
 	</array>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.coreservices.canUseDeviceEncryptionService</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### com.apple.AppStoreDaemon.StoreAEService

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/A/XPCServices/com.apple.AppStoreDaemon.StoreAEService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StoreAEService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### com.apple.AppStoreDaemon.StorePrivilegedODRService

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/A/XPCServices/com.apple.AppStoreDaemon.StorePrivilegedODRService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StorePrivilegedODRService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### com.apple.AppStoreDaemon.StorePrivilegedTaskService

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/A/XPCServices/com.apple.AppStoreDaemon.StorePrivilegedTaskService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StorePrivilegedTaskService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### com.apple.AppStoreDaemon.StoreAEService

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/Current/XPCServices/com.apple.AppStoreDaemon.StoreAEService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StoreAEService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### com.apple.AppStoreDaemon.StorePrivilegedODRService

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/Current/XPCServices/com.apple.AppStoreDaemon.StorePrivilegedODRService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StorePrivilegedODRService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### com.apple.AppStoreDaemon.StorePrivilegedTaskService

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/Current/XPCServices/com.apple.AppStoreDaemon.StorePrivilegedTaskService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StorePrivilegedTaskService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### com.apple.AppStoreDaemon.StoreUIService

> `/System/Library/PrivateFrameworks/AppStoreDaemonUI.framework/Versions/A/XPCServices/com.apple.AppStoreDaemon.StoreUIService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StoreUIService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### com.apple.AppStoreDaemon.StoreUIService

> `/System/Library/PrivateFrameworks/AppStoreDaemonUI.framework/Versions/Current/XPCServices/com.apple.AppStoreDaemon.StoreUIService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StoreUIService`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
 	<key>com.apple.security.hardened-process.dyld-ro</key>
 	<true/>
-	<key>com.apple.security.hardened-process.enhanced-security-version</key>
-	<integer>1</integer>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
 	<key>com.apple.security.hardened-process.platform-restrictions</key>

```
### appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/Versions/A/Resources/appleaccounttransparencyd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.appleaccounttransparencyd</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>com.apple.appleaccounttransparencyd</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.apsd</string>
 	</array>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>

```
### appleaccounttransparencyd

> `/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/Versions/Current/Resources/appleaccounttransparencyd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.appleaccounttransparencyd</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>com.apple.appleaccounttransparencyd</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.apsd</string>
 	</array>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>

```
### AAUIFollowUpExtension_macOS

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension_macOS.appex/Contents/MacOS/AAUIFollowUpExtension_macOS`

```diff

 	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### AppleIntelligenceReportingProcessingService

> `/System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/Versions/A/XPCServices/AppleIntelligenceReportingProcessingService.xpc/Contents/MacOS/AppleIntelligenceReportingProcessingService`

```diff

 	<true/>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
-	<key>com.apple.private.biome.read-write</key>
+	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>AssetDelivery.UAF.AssetSetAlterActivity</string>
+		<string>AssetDelivery.UAF.AssetSetStatus</string>
 		<string>AssetDelivery.UAF.DailyStatus</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>AssetDelivery.UAF.AssetSetAlterActivity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>AssetDelivery.UAF.AssetSetStatus</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>AssetDelivery.UAF.DailyStatus</key>
 				<dict>
 					<key>mode</key>
-					<string>read-write</string>
+					<string>read-only</string>
 				</dict>
 			</dict>
 		</dict>

```
### AppleIntelligenceReportingProcessingService

> `/System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/Versions/Current/XPCServices/AppleIntelligenceReportingProcessingService.xpc/Contents/MacOS/AppleIntelligenceReportingProcessingService`

```diff

 	<true/>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
-	<key>com.apple.private.biome.read-write</key>
+	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>AssetDelivery.UAF.AssetSetAlterActivity</string>
+		<string>AssetDelivery.UAF.AssetSetStatus</string>
 		<string>AssetDelivery.UAF.DailyStatus</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>AssetDelivery.UAF.AssetSetAlterActivity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>AssetDelivery.UAF.AssetSetStatus</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>AssetDelivery.UAF.DailyStatus</key>
 				<dict>
 					<key>mode</key>
-					<string>read-write</string>
+					<string>read-only</string>
 				</dict>
 			</dict>
 		</dict>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 		<string>com.apple.engagementd</string>
 		<string>com.apple.OnDeviceStorage</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version-string</key>
+	<string>2</string>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

 	</array>
 	<key>com.apple.private.dark-wake-network-reachability</key>
 	<true/>
+	<key>com.apple.private.ids.region-store</key>
+	<true/>
 	<key>com.apple.private.iokit.interactive-push</key>
 	<true/>
 	<key>com.apple.private.necp.match</key>

```
### AssetCacheManagerService

> `/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/Versions/A/XPCServices/AssetCacheManagerService.xpc/Contents/MacOS/AssetCacheManagerService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>

```
### AssetCacheManagerService

> `/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/Versions/Current/XPCServices/AssetCacheManagerService.xpc/Contents/MacOS/AssetCacheManagerService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.assistant.speech-request</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.modelcatalog</string>
+	</array>
 	<key>com.apple.private.domain-extension</key>
 	<true/>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>

 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.scda</key>
 	<true/>
+	<key>com.apple.siri.shared_flow_plugin_service</key>
+	<true/>
 	<key>com.apple.siri.vocabulary.admin</key>
 	<true/>
 	<key>com.apple.siriknowledged</key>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/Support/akd`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.appleaccount.transparency.metadata</key>
+	<true/>
 	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
 	<true/>
 	<key>com.apple.apsd.ios-device-push-token</key>

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.coreidvd.spi</key>

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.devicecheckd</string>
 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent</string>
+		<string>com.apple.appleaccount.transparency</string>
 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.asktod</string>

```
### AKFollowUpExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/Contents/MacOS/AKFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.cdp.followup</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.developer.game-center</key>
 	<array>
 		<string>Account</string>

```
### AuthKitUIMacService

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/Resources/AuthKitUIMacService.app/Contents/MacOS/AuthKitUIMacService`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict>
-	<key>com.apple.authkit.client.owner</key>
-	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
-</dict>
+<dict/>
 </plist>
 

```
### AKAuthorizationRemoteViewService

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/A/XPCServices/AKAuthorizationRemoteViewService.xpc/Contents/MacOS/AKAuthorizationRemoteViewService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.owner</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.clarityboard.shows-scene</key>
 	<true/>
 	<key>com.apple.developer.associated-domains</key>

```
### AuthKitUIMacService

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/Current/Resources/AuthKitUIMacService.app/Contents/MacOS/AuthKitUIMacService`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict>
-	<key>com.apple.authkit.client.owner</key>
-	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
-</dict>
+<dict/>
 </plist>
 

```
### AKAuthorizationRemoteViewService

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/Versions/Current/XPCServices/AKAuthorizationRemoteViewService.xpc/Contents/MacOS/AKAuthorizationRemoteViewService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.owner</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.clarityboard.shows-scene</key>
 	<true/>
 	<key>com.apple.developer.associated-domains</key>

```
### BackgroundTaskManagementAgent

> `/System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Support/BackgroundTaskManagementAgent.app/Contents/MacOS/BackgroundTaskManagementAgent`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canaccessanysharedfilelist</key>
 	<string>read-write</string>
-	<key>com.apple.private.security.signal-exempt.xxx</key>
+	<key>com.apple.private.security.signal-exempt</key>
 	<true/>
 	<key>com.apple.private.sharedfilelist.AllowRestrictedItemPropertyUpdates</key>
 	<true/>

```
### BiomeAgent

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/BiomeAgent`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.SiriInference</key>
 	<true/>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 	<true/>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>
 	<true/>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>

```
### bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

```diff

 	<array>
 		<string>IOMobileFramebufferUserClient</string>
 		<string>IOSurfaceRootUserClient</string>
-		<string>com_apple_driver_FairPlayIOKitUserClient</string>
 		<string>AppleJPEGDriverUserClient</string>
 	</array>
 	<key>com.apple.security.system-groups</key>

```
### calaccessd

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/Support/calaccessd`

```diff

 	<true/>
 	<key>com.apple.security.files.bookmarks.document-scope</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.security.personal-information.location</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```
### com.apple.CloudDocs.iCloudDriveFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/Contents/MacOS/com.apple.CloudDocs.iCloudDriveFileProviderManaged`

```diff

 	<true/>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
-	<key>com.apple.private.pluginkit.persona</key>
-	<string>host</string>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### cloudd

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd`

```diff

 	<array>
 		<string>RootDomainUserClient</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.sharereportingd</string>
+	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Versions/A/Support/cloudphotod`

```diff

 	<key>com.apple.developer.icloud-extended-share-access</key>
 	<array>
 		<string>InProcessShareOwnerParticipantInfo</string>
+		<string>InProcessShareAccessRequests</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>

```
### LOMXPCService

> `/System/Library/PrivateFrameworks/ConfigurationProfiles.framework/XPCServices/LOMXPCService.xpc/Contents/MacOS/LOMXPCService`

```diff

 	<array>
 		<string>com.apple.ServiceManagement.daemons.modify</string>
 	</array>
+	<key>com.apple.private.xpc.smd-job-submit</key>
+	<true/>
 </dict>
 </plist>
 

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>

```
### cdpd

> `/System/Library/PrivateFrameworks/CoreCDP.framework/Versions/A/Resources/cdpd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.recoverykey</key>
+	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.telemetry</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
+	<key>com.apple.cdp.walrus.pcskeys</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### cdpd

> `/System/Library/PrivateFrameworks/CoreCDP.framework/Versions/Current/Resources/cdpd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.recoverykey</key>
+	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.telemetry</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
+	<key>com.apple.cdp.walrus.pcskeys</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### contextstored

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Versions/A/Resources/contextstored`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.rapport.people</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```
### contextstored

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Versions/Current/Resources/contextstored`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.rapport.people</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```

### 🆕 TTRAssistantSpeechAudioDiagnostic

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/PlugIns/TTRAssistantSpeechAudioDiagnostic.appex/Contents/MacOS/TTRAssistantSpeechAudioDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/Assistant/TTRAudio/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Logs/CrashReporter/Assistant/TTRAudio/</string>
	</array>
</dict>
</plist>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech`

```diff

 	<array>
 		<string>com.apple.assistant</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.public</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 	</array>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/Current/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech`

```diff

 	<array>
 		<string>com.apple.assistant</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.public</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 	</array>

```
### CoreRepairCoreXPCService

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/Versions/A/XPCServices/CoreRepairCoreXPCService.xpc/Contents/MacOS/CoreRepairCoreXPCService`

```diff

 	<true/>
 	<key>com.apple.private.corerepair.fdr</key>
 	<true/>
+	<key>com.apple.private.corerepair.preflight</key>
+	<true/>
+	<key>com.apple.private.corerepair.xpc</key>
+	<true/>
 	<key>com.apple.private.img4.nonce.pdi</key>
 	<true/>
 	<key>com.apple.private.img4.nonce.trust-cache</key>

```
### CoreRepairCoreXPCService

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/Versions/Current/XPCServices/CoreRepairCoreXPCService.xpc/Contents/MacOS/CoreRepairCoreXPCService`

```diff

 	<true/>
 	<key>com.apple.private.corerepair.fdr</key>
 	<true/>
+	<key>com.apple.private.corerepair.preflight</key>
+	<true/>
+	<key>com.apple.private.corerepair.xpc</key>
+	<true/>
 	<key>com.apple.private.img4.nonce.pdi</key>
 	<true/>
 	<key>com.apple.private.img4.nonce.trust-cache</key>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.private.audio.notification-wake-audio</key>
 	<true/>
+	<key>com.apple.private.audio.self-manages-sensor</key>
+	<true/>
 	<key>com.apple.private.audio.suppress-mic-indicator</key>
 	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>

```
### corespeechd_system

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system`

```diff

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>MediaLibrary.SharedPlaylist</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Podcasts.Podcast</key>
 				<dict>
 					<key>mode</key>

 		<string>com.apple.corespeechdatacollection</string>
 		<string>com.apple.adaptiveSiriVolume</string>
 		<string>com.apple.siri.features.dormancy</string>
+		<string>com.apple.speech.GeoLM</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/Support/suggestd`

```diff

 	<array>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceUbiquity</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.ubiquity-kvstore-access</key>
 	<array>

```
### dataaccessd

> `/System/Library/PrivateFrameworks/DataAccess.framework/Support/dataaccessd`

```diff

 	<array>
 		<string>group.com.apple.calendar</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.sharedpclogging</string>

```
### AirPlayDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/AirPlayDiagnosticExtension.appex/Contents/MacOS/AirPlayDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allows-set-output-device</key>
 	<true/>
+	<key>com.apple.developer.homekit</key>
+	<true/>
+	<key>com.apple.homekit.private-spi-access</key>
+	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceWillow</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.coremedia.endpoint.xpc</string>

 		<string>com.apple.coremedia.routingcontext.xpc</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
+		<string>com.apple.symptom_analytics</string>
 	</array>
+	<key>com.apple.symptoms.NetworkDiagnostics</key>
+	<true/>
+	<key>com.apple.symptoms.NetworkDiagnostics.query</key>
+	<true/>
 </dict>
 </plist>
 

```
### HomeEnergyDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/HomeEnergyDiagnosticExtension.appex/Contents/MacOS/HomeEnergyDiagnosticExtension`

```diff

 		<string>/Library/homeenergyd/</string>
 		<string>/Library/homeenergyd/com.apple.homeenergyd/</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.EnergyKit</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>

 		<string>/Library/homeenergyd/</string>
 		<string>/Library/homeenergyd/com.apple.homeenergyd/</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.EnergyKit</string>
+	</array>
 </dict>
 </plist>
 

```
### ScreenTimeDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ScreenTimeDiagnosticExtension.appex/Contents/MacOS/ScreenTimeDiagnosticExtension`

```diff

 	<array>
 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### donotdisturbd

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.donotdisturbd</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.personalization.notificationCategorization</string>
 		<string>com.apple.locationd.synchronous</string>
 		<string>com.apple.calaccessd</string>

```

### 🆕 GameTestIndicator

> `/System/Library/PrivateFrameworks/Ecosystem.framework/Support/GameTestIndicator`

- No entitlements *(yet)*
### facetimemessagestored

> `/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored`

```diff

 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.linkd.application-service</string>
+		<string>com.apple.frauddefensed</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<string>com.apple.facetimemessagestored</string>
 	<key>com.apple.sensitivecontentanalysis.service</key>
 	<string>videoVoiceMail</string>
+	<key>com.apple.trustkit.frauddefensed</key>
+	<true/>
 	<key>com.apple.usersafety.service</key>
 	<string>videoVoiceMail</string>
 	<key>platform-application</key>

```
### FaceTimeNotificationViewBridgeService

> `/System/Library/PrivateFrameworks/FaceTimeNotificationViewBridge.framework/Versions/A/XPCServices/FaceTimeNotificationViewBridgeService.xpc/Contents/MacOS/FaceTimeNotificationViewBridgeService`

```diff

 		<string>record-calls</string>
 		<string>translate-calls</string>
 		<string>smart-holding</string>
+		<string>accessibility-interpreter</string>
 	</array>
 </dict>
 </plist>

```
### FaceTimeNotificationViewBridgeService

> `/System/Library/PrivateFrameworks/FaceTimeNotificationViewBridge.framework/Versions/Current/XPCServices/FaceTimeNotificationViewBridgeService.xpc/Contents/MacOS/FaceTimeNotificationViewBridgeService`

```diff

 		<string>record-calls</string>
 		<string>translate-calls</string>
 		<string>smart-holding</string>
+		<string>accessibility-interpreter</string>
 	</array>
 </dict>
 </plist>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/Resources/familycircled`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.apply</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screentime-setup</key>
 	<true/>
 	<key>com.apple.private.security.daemon-container</key>

 		<string>com.apple.cksharingmanagementd</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ScreenTimeAgent.setup</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.family.sharing-client.com.apple.FamilyCircle</string>
 		<string>com.apple.family.sharing-client.com.apple.ScreenTimeServices</string>
 		<string>com.apple.family.sharing-client.com.apple.ScreenTimeSettings</string>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/Current/Resources/familycircled`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.apply</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.screentime-setup</key>
 	<true/>
 	<key>com.apple.private.security.daemon-container</key>

 		<string>com.apple.cksharingmanagementd</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ScreenTimeAgent.setup</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.family.sharing-client.com.apple.FamilyCircle</string>
 		<string>com.apple.family.sharing-client.com.apple.ScreenTimeServices</string>
 		<string>com.apple.family.sharing-client.com.apple.ScreenTimeSettings</string>

```
### healthd

> `/System/Library/PrivateFrameworks/HealthKit.framework/healthd`

```diff

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.memorystatus</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>WaitForSystemAppMigrationToComplete</string>

 		<string>com.apple.coreaudio</string>
 		<string>com.apple.FitnessCoaching</string>
 		<string>com.apple.health.shared</string>
+		<string>com.apple.healthcontentd</string>
 		<string>com.apple.migrationpluginwrapper</string>
 		<string>com.apple.Mind</string>
 		<string>com.apple.Mobility.notifications</string>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 		<string>com.apple.private.alloy.home.invite</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
-		<string>com.apple.private.alloy.homepod.topcap</string>
 	</array>
 	<key>com.apple.private.ids.messaging.high-priority</key>
 	<array>

 		<string>com.apple.private.alloy.home.invite</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
-		<string>com.apple.private.alloy.homepod.topcap</string>
 	</array>
 	<key>com.apple.private.ids.registration</key>
 	<array>

 		<string>com.apple.private.alloy.home.invite</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
-		<string>com.apple.private.alloy.homepod.topcap</string>
 	</array>
 	<key>com.apple.private.ids.session</key>
 	<array>

 		<string>com.apple.private.alloy.home.invite</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
-		<string>com.apple.private.alloy.homepod.topcap</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>
 	<array>

 		<string>com.apple.private.alloy.home.invite</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
-		<string>com.apple.private.alloy.homepod.topcap</string>
 	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>
 	<true/>

 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
-	<key>com.apple.systemstatus.activityattribution</key>
-	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
 	<key>com.apple.uarp</key>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/Contents/MacOS/IMDPersistenceAgent`

```diff

 	<array>
 		<string>ReadMessage</string>
 	</array>
+	<key>com.apple.private.communicationsfilter</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
+	<key>com.apple.announced.client</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.intelligenceflow.intelligenceflowd</string>
 	<key>com.apple.appprotectiond.read.access</key>

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
-	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
-	<array>
-		<string>photos.scene</string>
-		<string>photos.person</string>
-		<string>photos.face</string>
-	</array>
 	<key>com.apple.private.assistant.audio-session-event</key>
 	<true/>
 	<key>com.apple.private.attentionawareness</key>

 	<true/>
 	<key>com.apple.private.homekit.allow-secure-access</key>
 	<true/>
+	<key>com.apple.private.homekit.home-location</key>
+	<true/>
 	<key>com.apple.private.ids.agent.GroupRestricted</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.intelligenceflow.mail-enrichment</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>Mail</string>
+				<string>MailAttachment</string>
+			</array>
+			<key>Sets</key>
+			<dict>
+				<key>App.Intents.IndexedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Cascade.CachedDocument</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
-	<key>com.apple.private.photos.XPCStoreOptIn</key>
-	<true/>
 	<key>com.apple.private.photos.service.multilibrary</key>
 	<true/>
 	<key>com.apple.private.screencapturekit.noprompt</key>

 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.PhotosLibraries</key>
+	<true/>
 	<key>com.apple.private.security.storage.SiriFeatureStore</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriReferenceResolution</key>

 	<array>
 		<string>kTCCServiceSiriAccess</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceSiri</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.siri.device_resolution</key>
+	<true/>
 	<key>com.apple.siri.flowtools_xpc_service</key>
 	<true/>
+	<key>com.apple.siri.local-turn-status</key>
+	<true/>
 	<key>com.apple.siri.location</key>
 	<true/>
 	<key>com.apple.siri.orchestration.sirix</key>

 	<true/>
 	<key>com.apple.symptoms.NetworkDiagnostics</key>
 	<true/>
+	<key>com.apple.team6.buddy.peer.profile-read</key>
+	<true/>
+	<key>com.apple.toolkit.request-immediate-indexing.allow</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1150</string>

 		<string>INTELLIGENCE_FLOW_QUERY_DECORATOR</string>
 		<string>SIRI_SECURITY_IPI</string>
 		<string>SIRI_INTELLIGENCE_FLOW_PLANNER</string>
+		<string>SIRI_INTELLIGENCE_FLOW_TRAFFIC_CLASSIFIER</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/mediaanalysisd`

```diff

 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
+	<key>com.apple.private.photos.allowcollectionshare</key>
+	<true/>
 	<key>com.apple.private.photos.coresceneunderstanding.taxonomy.read-write</key>
 	<true/>
 	<key>com.apple.private.photos.service.debug</key>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/A/XPCServices/com.apple.photos.ImageConversionService.xpc/Contents/MacOS/com.apple.photos.ImageConversionService`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.gms.availability</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleVideoToolboxParavirtualizationUserClient</string>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/A/XPCServices/com.apple.photos.VideoConversionService.xpc/Contents/MacOS/com.apple.photos.VideoConversionService`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleVideoToolboxParavirtualizationUserClient</string>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/Current/XPCServices/com.apple.photos.ImageConversionService.xpc/Contents/MacOS/com.apple.photos.ImageConversionService`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.inference</key>

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.gms.availability</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleVideoToolboxParavirtualizationUserClient</string>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/Current/XPCServices/com.apple.photos.VideoConversionService.xpc/Contents/MacOS/com.apple.photos.VideoConversionService`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleVideoToolboxParavirtualizationUserClient</string>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Versions/A/Support/mstreamd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 		<string>com.apple.aa.accountService.xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```
### mobiletimerd

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd`

```diff

 	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
 	<array>
 		<string>com.apple.mobiletimer</string>
+		<string>com.apple.mobiletimer.Alarms</string>
 		<string>com.apple.clock</string>
 		<string>com.apple.NanoAlarm</string>
 		<string>com.apple.private.NanoTimer</string>

```
### ModelCatalogAgent

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/ModelCatalogAgent`

```diff

 		</dict>
 		<key>ModelCatalogSubscriptionEvaluation</key>
 		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>ModelCatalog.Subscriptions.RequestedUseCases</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
 			<key>Streams</key>
 			<dict>
 				<key>AppleIntelligence.Availability</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>ModelCatalog.Subscriptions.ExplicitRequests</key>
-				<dict>
-					<key>mode</key>
-					<string>read-only</string>
-				</dict>
 			</dict>
 		</dict>
 	</dict>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.SetStoreUpdateService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/modelcatalogd`

```diff

 		</dict>
 		<key>ModelCatalogSubscriptionEvaluation</key>
 		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>ModelCatalog.Subscriptions.RequestedUseCases</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
 			<key>Streams</key>
 			<dict>
 				<key>AppleIntelligence.Availability</key>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>ModelCatalog.Subscriptions.ExplicitRequests</key>
-				<dict>
-					<key>mode</key>
-					<string>read-only</string>
-				</dict>
 			</dict>
 		</dict>
 		<key>RegionalSafetyAnalysisMetrics</key>

 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.SetStoreUpdateService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/searchtoold`

```diff

 	<true/>
 	<key>com.apple.diagnosticpipeline.request</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.filederivatives.derive</key>
 	<true/>
 	<key>com.apple.fileprovider.enumerate</key>

 				<string>TextUnderstandingDeliveryTracking</string>
 				<string>TextUnderstandingEvent</string>
 				<string>TextUnderstandingIdentificationDocument</string>
+				<string>SiriTranscript</string>
+				<string>SiriTranscriptConversation</string>
+			</array>
+		</dict>
+		<key>generativesearch</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>SiriTranscript</string>
+				<string>SiriTranscriptConversation</string>
 			</array>
 		</dict>
 	</dict>

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.amsondevicestoraged</string>
+	<key>aps-connection-initiate</key>
+	<true/>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array>
+		<string>com.apple.applemediaservices.ondevicestorage</string>
+	</array>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.icloud-account-access</key>

 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.apsd</string>
+		<string>com.apple.cloudd</string>
 		<string>com.apple.fpsd</string>
 		<string>com.apple.fairplayd</string>
 		<string>com.apple.fairplayd.xpc</string>

```
### PhotosDiagnostics

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PlugIns/PhotosDiagnostics.appex/Contents/MacOS/PhotosDiagnostics`

```diff

 	<true/>
 	<key>com.apple.private.photos.service.sbextensions</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServicePhotos</string>
+	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.Photos.CPLDiagnose</string>
+		<string>com.apple.photos.service</string>
 	</array>
 </dict>
 </plist>

```
### photolibraryd

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	<true/>
 	<key>com.apple.security.files.bookmarks.app-scope</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>

```
### PlatformSSOUIAgent

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/Support/PlatformSSOUIAgent.app/Contents/MacOS/PlatformSSOUIAgent`

```diff

 	<true/>
 	<key>com.apple.keystore.device.smart-card</key>
 	<true/>
+	<key>com.apple.keystore.filevault</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.BackgroundUI</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

```
### PerfPowerServicesSignpostService

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/XPCServices/PerfPowerServicesSignpostService.xpc/Contents/MacOS/PerfPowerServicesSignpostService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.PerfPowerServicesSignpostService</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.PerfPowerServicesSignpostService</string>
 	<key>com.apple.developer.icloud-container-environment</key>

 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.powerlogHelperd.XPCService.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### PerfPowerServicesSignpostService

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/Current/XPCServices/PerfPowerServicesSignpostService.xpc/Contents/MacOS/PerfPowerServicesSignpostService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.PerfPowerServicesSignpostService</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.PerfPowerServicesSignpostService</string>
 	<key>com.apple.developer.icloud-container-environment</key>

 	<array>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.powerlogHelperd.XPCService.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### scrod

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/A/Resources/scrod`

```diff

 	<true/>
 	<key>com.apple.hid.manager.user-access-privileged</key>
 	<true/>
+	<key>com.apple.keyboardservices.textreplacement.allow</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appGroup</key>

 	<array>
 		<string>com.apple.voicebanking.services</string>
 		<string>com.apple.voicebanking.store</string>
+		<string>com.apple.TextInput.shortcuts</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### scrod

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/Current/Resources/scrod`

```diff

 	<true/>
 	<key>com.apple.hid.manager.user-access-privileged</key>
 	<true/>
+	<key>com.apple.keyboardservices.textreplacement.allow</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appGroup</key>

 	<array>
 		<string>com.apple.voicebanking.services</string>
 		<string>com.apple.voicebanking.store</string>
+		<string>com.apple.TextInput.shortcuts</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
+	<key>com.apple.authkit.deviceList</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.InFocus</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/Versions/A/ScreenTimeSettingsAgent`

```diff

 	<string>com.apple.ScreenTimeSettingsAgent</string>
 	<key>com.apple.asktod</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### siriappintentsd

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/siriappintentsd`

```diff

 		<string>SessionResumptionEventBundle</string>
 		<string>SecurityValidationEvent</string>
 		<string>SecurityValidationProtoSecurityValidationEventPayload</string>
+		<string>SiriTrajectoryInstrumentationEvent</string>
 		<string>TokenGeneration.Inference.Requests</string>
 	</array>
 	<key>com.apple.private.corespotlight.skgupdater</key>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/siriinferenced`

```diff

 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCalendar</string>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite</key>
 	<true/>

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.tccd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.siri.homeAutomation</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.siri.inference.SiriSignals</string>
+		<string>com.apple.assistant.public</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.fairplayd</string>
 		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.servicesanalytics.xpc</string>
+		<string>com.apple.tccd</string>
 	</array>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>

 	<array>
 		<string>755</string>
 		<string>910</string>
-		<string>351</string>
-		<string>1320</string>
+		<string>SIRI_VALUE_INFERENCE_CONTACT_RESOLUTION</string>
+		<string>SIRI_VALUE_INFERENCE_MESSAGES_SMART_APP_SELECTION</string>
 		<string>1321</string>
-		<string>1326</string>
-		<string>1327</string>
-		<string>1328</string>
+		<string>SIRI_VALUE_INFERENCE_MEGADOME_ECR</string>
+		<string>SIRI_VALUE_INFERENCE_SIRI_REMEMBERS</string>
+		<string>SIRI_VALUE_INFERENCE_PERVASIVE_ENTITY_RESOLUTION</string>
 		<string>1340</string>
 		<string>1341</string>
 		<string>1342</string>
 		<string>1343</string>
-		<string>1710</string>
+		<string>TV_SEARCH_APP_ORDERING_SIGNAL_COLLECTION</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```

### 🆕 OLEOrchestrator

> `/System/Library/PrivateFrameworks/SiriProcessing.framework/Versions/A/XPCServices/OLEOrchestrator.xpc/Contents/MacOS/OLEOrchestrator`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.lighthouse.host-ole</key>
	<true/>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskStatus</string>
	</array>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.runningboard.terminateprocess</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### MusicAppSelectionPFLPlugin

> `/System/Library/PrivateFrameworks/SiriSignals.framework/PlugIns/MusicAppSelectionPFLPlugin.appex/Contents/MacOS/MusicAppSelectionPFLPlugin`

```diff

 	</array>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>1329</string>
+		<string>SIRI_VALUE_INFERENCE_MUSIC_APP_SELECTION_PFL</string>
 	</array>
 </dict>
 </plist>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/Versions/A/XPCServices/SiriSuggestionsBookkeepingService.xpc/Contents/MacOS/SiriSuggestionsBookkeepingService`

```diff

 	<true/>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.tccd</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/Versions/Current/XPCServices/SiriSuggestionsBookkeepingService.xpc/Contents/MacOS/SiriSuggestionsBookkeepingService`

```diff

 	<true/>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.tccd</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>

```
### imageplaygroundd

> `/System/Library/PrivateFrameworks/SuggestedImage.framework/Support/imageplaygroundd`

```diff

 		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>
+	<key>com.apple.springboard.fetchDisplayConfigs</key>
+	<true/>
+	<key>com.apple.springboard.wallpaper.display-configuration</key>
+	<true/>
 </dict>
 </plist>
 

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	</array>
 	<key>com.apple.coretelephony.Calls.allow</key>
 	<true/>
+	<key>com.apple.developer.conversation-accessibility</key>
+	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<key>com.apple.private.ids.messaging.high-priority</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	</array>
 	<key>com.apple.private.ids.registration</key>
 	<array>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>

 	<key>com.apple.private.ids.self-session</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<key>com.apple.private.ids.session</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<key>com.apple.private.ids.session-private</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<true/>
 	<key>com.apple.runningboard.assertions.callservicesd</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.appintents.LiveEntityService</string>
 		<string>com.apple.audioanalyticsd</string>
+		<string>com.apple.conversation.accessibility</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.xpc-service-name</key>
+	<array>
+		<string>com.apple.extensionkitservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTrackingAgent`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

 			<array>
 				<string>App.MediaUsage</string>
 				<string>App.WebUsage</string>
+				<string>Demo.ScreenTime.AppUsage</string>
+				<string>Demo.ScreenTime.MediaUsage</string>
+				<string>Demo.ScreenTime.NowPlaying</string>
+				<string>Demo.ScreenTime.WebUsage</string>
 				<string>Intelligence.Usage</string>
 				<string>Media.NowPlaying</string>
 				<string>ScreenTime.AppUsage</string>

```
### visualintelligenced

> `/System/Library/PrivateFrameworks/VisualIntelligenceServices.framework/visualintelligenced`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.generativeexperiences.agentMediaStore</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.proactiveagentplatform.orchestrator</key>
 	<true/>
 	<key>com.apple.proactiveagentplatform.orchestrator.features</key>

 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.proactiveagentplatform.orchestrator</string>
 		<string>com.apple.shortcuts.view-service</string>
 		<string>com.apple.siri.uaf.service</string>

 		<string>com.apple.appleaccount</string>
 		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.homed</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/Contents/MacOS/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.shortcuts</key>

 		<string>com.apple.photos.service</string>
 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.shazamd</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/Contents/MacOS/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.rootless.storage.shortcuts_sandbox_profile</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.private.corewifi.internal-xpc</string>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.sharing.airdrop.service</string>
 		<string>com.apple.shortcuts.view-service</string>

```
### ShortcutsMacHelper

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/ShortcutsMacHelper.xpc/Contents/MacOS/ShortcutsMacHelper`

```diff

 	<string>com.apple.WorkflowKit.MacHelper</string>
 	<key>com.apple.dock.add-item</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.private.responsibility.set-to-self</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.automation.apple-events</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.linkd.mediator</string>
+	</array>
 	<key>com.apple.shortcuts.mac-helper</key>
 	<true/>
 </dict>

```

### 🆕 CrisisResourceUIPlugin

> `/System/Library/Snippets/UIPlugins/CrisisResourceUIPlugin.bundle/Contents/MacOS/CrisisResourceUIPlugin`

- No entitlements *(yet)*

### 🆕 MusicSnippetsUI

> `/System/Library/Snippets/UIPlugins/MusicSnippetsUI.bundle/Contents/MacOS/MusicSnippetsUI`

- No entitlements *(yet)*

### 🆕 PodcastsSnippetsUI

> `/System/Library/Snippets/UIPlugins/PodcastsSnippetsUI.bundle/Contents/MacOS/PodcastsSnippetsUI`

- No entitlements *(yet)*
### FamilyOutOfProcessUIExtension

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/Contents/MacOS/FamilyOutOfProcessUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ScreenTimeAgent.Contacts</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.ScreenTimeAgent.Contacts</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### ContactViewViewService

> `/System/iOSSupport/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/Contents/MacOS/ContactViewViewService`

```diff

 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.Archetype.personalContext</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### ContactsViewService

> `/System/iOSSupport/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/Contents/MacOS/ContactsViewService`

```diff

 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.Archetype.personalContext</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### DeviceActivityReportService

> `/System/iOSSupport/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/A/PlugIns/DeviceActivityReportService.appex/Contents/MacOS/DeviceActivityReportService`

```diff

 	<array>
 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### DeviceActivityReportService

> `/System/iOSSupport/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/Current/PlugIns/DeviceActivityReportService.appex/Contents/MacOS/DeviceActivityReportService`

```diff

 	<array>
 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
+		<string>Demo.ScreenTime.AppUsage</string>
+		<string>Demo.ScreenTime.DisplayBacklight</string>
+		<string>Demo.ScreenTime.MediaUsage</string>
+		<string>Demo.ScreenTime.Notifications</string>
+		<string>Demo.ScreenTime.NowPlaying</string>
+		<string>Demo.ScreenTime.WebUsage</string>
 		<string>Device.Display.Backlight</string>
 		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>

```
### AKAuthorizationRemoteViewService

> `/System/iOSSupport/System/Library/PrivateFrameworks/AuthKitUIMacHelper.framework/Versions/A/XPCServices/AKAuthorizationRemoteViewService.xpc/Contents/MacOS/AKAuthorizationRemoteViewService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.owner</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.clarityboard.shows-scene</key>
 	<true/>
 	<key>com.apple.developer.associated-domains</key>

```
### AKAuthorizationRemoteViewService

> `/System/iOSSupport/System/Library/PrivateFrameworks/AuthKitUIMacHelper.framework/Versions/Current/XPCServices/AKAuthorizationRemoteViewService.xpc/Contents/MacOS/AKAuthorizationRemoteViewService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.owner</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.clarityboard.shows-scene</key>
 	<true/>
 	<key>com.apple.developer.associated-domains</key>

```
### launchd

> `/sbin/launchd`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
+	<key>com.apple.developer.lockdown-mode.state</key>
+	<true/>
 	<key>com.apple.private.amfi.can-allow-non-platform</key>
 	<true/>
 	<key>com.apple.private.delegate-signals</key>

```
### fm

> `/usr/bin/fm`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.fmtool</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.fmtool</string>
 	<key>com.apple.modelmanager.inference</key>

```

### 🆕 game-mode-detect

> `/usr/bin/game-mode-detect`

- No entitlements *(yet)*

### 🆕 game-test-tool

> `/usr/bin/game-test-tool`

- No entitlements *(yet)*

### 🆕 ibv_ctl

> `/usr/bin/ibv_ctl`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.IORDMACMUC</key>
	<true/>
	<key>com.apple.private.IORDMAFamilyUC</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>IORDMAFamilyUC</string>
		<string>IORDMACMUserClient</string>
	</array>
</dict>
</plist>

```
### modelcatalogdump

> `/usr/bin/modelcatalogdump`

```diff

 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>AppleIntelligence.Availability</string>
-		<string>ModelCatalog.Subscriptions.ExplicitRequests</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.modelcatalogtool</string>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
-				<key>ModelCatalog.Subscriptions.ExplicitRequests</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
 			</dict>
 		</dict>
 	</dict>

```
### tccutil

> `/usr/bin/tccutil`

```diff

 		<string>kTCCServiceSystemPolicyAllFiles</string>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.tcc.manager.service-descriptions</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 timeout

> `/usr/bin/timeout`

- No entitlements *(yet)*
### AirPlayXPCHelper

> `/usr/libexec/AirPlayXPCHelper`

```diff

 	<true/>
 	<key>com.apple.private.appfirewallclient</key>
 	<true/>
+	<key>com.apple.private.audio.driver.extrinsic.registration</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.mutetoggle</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.volumedown</key>
+	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.AirPlay.DACP.volumeup</key>
+	<true/>
 	<key>com.apple.private.driverkit.driver-access</key>
 	<array>
 		<string>com.apple.private.wifi.driverkit</string>

```
### AssetCache

> `/usr/libexec/AssetCache/AssetCache`

```diff

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.container.access</key>
+	<dict>
+		<key>protectedSystem</key>
+		<dict>
+			<key>com.apple.AssetCacheManagerService</key>
+			<dict>
+				<key>data</key>
+				<dict>
+					<key>access</key>
+					<string>read-write</string>
+					<key>operations</key>
+					<array>
+						<string>lookup</string>
+					</array>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
+	<key>com.apple.private.security.storage.containers</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### CSCSupportd

> `/usr/libexec/CSCSupportd`

```diff

 	<true/>
 	<key>com.apple.private.iokit.assertonlidclose</key>
 	<true/>
+	<key>com.apple.private.mobileinboxupdater.xpc</key>
+	<true/>
 </dict>
 </plist>
 

```
### SidecarDisplayAgent

> `/usr/libexec/SidecarDisplayAgent`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ensemble</string>
+		<string>com.apple.MenuBarAgent.systemservices</string>
 	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
 	<key>com.apple.cdp.recovery</key>
 	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.cdp.walrus.pcskeys</key>

```

### 🆕 appledepthd

> `/usr/libexec/appledepthd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/assetsubscriptiond/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.uaf.subscription.service</string>
	</array>
</dict>
</plist>

```
### avconferenced

> `/usr/libexec/avconferenced`

```diff

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.audio.driver.extrinsic.registration</key>
+	<true/>
 	<key>com.apple.private.audio.interprocess-tap</key>
 	<true/>
 	<key>com.apple.private.audio.notification-wake-audio</key>

 	<array>
 		<string>analysis</string>
 	</array>
-	<key>com.apple.private.speechtranslation.serverhost</key>
-	<true/>
 	<key>com.apple.private.speechtranslationclient</key>
 	<true/>
 	<key>com.apple.private.spindump.generatespindump</key>

```
### ciphermld

> `/usr/libexec/ciphermld`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.ciphermld</string>
+	<key>com.apple.developer.default-data-protection</key>
+	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.ciphermld</string>
 	<key>com.apple.duet.activityscheduler.allow</key>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.rapport.people</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```
### corerepaird

> `/usr/libexec/corerepaird`

```diff

 	<true/>
 	<key>com.apple.private.corerepair.fdr</key>
 	<true/>
+	<key>com.apple.private.corerepair.preflight</key>
+	<true/>
+	<key>com.apple.private.corerepair.xpc</key>
+	<true/>
 	<key>com.apple.private.img4.nonce.pdi</key>
 	<true/>
 	<key>com.apple.private.img4.nonce.trust-cache</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>App.Install</string>
 		<string>Device.Power.PluggedIn</string>
 		<string>Device.KeybagLocked</string>
+		<string>Device.Wireless.NFCTag</string>
+		<string>Media.NowPlaying</string>
+		<string>CarPlay.Connected</string>
+		<string>Device.Activity.Prediction</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### endpointsecurityd

> `/usr/libexec/endpointsecurityd`

```diff

 	</array>
 	<key>com.apple.private.security.storage.SystemExtensionManagement</key>
 	<true/>
+	<key>com.apple.private.xpc.smd-job-submit</key>
+	<true/>
 </dict>
 </plist>
 

```
### findmydevice-user-agent

> `/usr/libexec/findmydevice-user-agent`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.TVRemoteCore</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.icloud.findmydeviced.ua-services.access</key>
 	<true/>
+	<key>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.ownersession</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.pairingmanager</key>
+	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.CallerName</key>

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.tvremote.findmy</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.icloud.findmydeviced</string>

```
### findmylocateagent

> `/usr/libexec/findmylocateagent`

```diff

 	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.fmf.local</string>

```
### fskitd

> `/usr/libexec/fskitd`

```diff

 	<array>
 		<string>group.com.apple.fskit.settings</string>
 	</array>
+	<key>com.apple.private.security.storage.network.heritable</key>
+	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### gamed

> `/usr/libexec/gamed`

```diff

 		<string>com.apple.amsprivateidentifiers</string>
 		<string>com.apple.ctkd.token-client</string>
 	</array>
+	<key>com.apple.symptom_analytics.query</key>
+	<true/>
+	<key>com.apple.symptoms.NetworkOfInterest</key>
+	<true/>
 </dict>
 </plist>
 

```
### gamesaved

> `/usr/libexec/gamesaved`

```diff

 	<string>com.apple.gamesaved</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.fileprovider.iwork-collaboration-messaging</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.librarian.container-proxy</key>

```
### generativelearningd

> `/usr/libexec/generativelearningd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GenerativeSearch.generativelearningd</string>
 	<key>com.apple.duet.activityscheduler.allow</key>

 				<string>SiriTranscriptConversation</string>
 				<string>Summary</string>
 				<string>UserActivity</string>
+				<string>HealthSummary</string>
+				<string>FitnessActivityRings</string>
+				<string>FitnessMindfulSession</string>
+				<string>FitnessWorkout</string>
+				<string>HealthCategorySample</string>
+				<string>HealthCharacteristics</string>
+				<string>HealthClassification</string>
+				<string>HealthStatistics</string>
+				<string>HealthSleepDaySummary</string>
+				<string>HealthStateOfMindSample</string>
+				<string>HealthOvernightVitalsSummary</string>
 			</array>
 			<key>Sets</key>
 			<dict>

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
-		<string>/private/var/mobile/Library/generativelearningd/</string>
 		<string>/private/var/mobile/Library/SearchManager/</string>
-		<string>/private/var/mobile/Library/Application Support/GenerativeLearningPlatform/</string>
 		<string>/tmp/com.apple.generativelearning/</string>
+		<string>/private/var/mobile/Library/generativelearningd/</string>
+		<string>/private/var/mobile/Library/Application Support/GenerativeLearningPlatform/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.modelmanager</string>
+		<string>com.apple.TapToRadarKit.service</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.ts.daemon-container</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.generativelearning</string>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 </dict>
 </plist>
 

```
### hybridsearchd

> `/usr/libexec/hybridsearchd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.Contacts.database-allow</key>
-	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.GenerativeSearch.FitnessIntelligenceDonationStore</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Fitness.ActivityRings</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Fitness.MindfulSession</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Fitness.Workout</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>com.apple.GenerativeSearch.GLPTestDonationStore</key>
 		<dict>
 			<key>Sets</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.GenerativeSearch.HealthKitDonationStore</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Health.Measurement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>com.apple.GenerativeSearch.InsightEntity</key>
 		<dict>
 			<key>Sets</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Cascade.CachedDocument</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 			</dict>
 		</dict>
 		<key>com.apple.GenerativeSearch.RemindersDonationStore</key>

 				<string>UserActivityInsight</string>
 				<string>VehicleInsight</string>
 				<string>PersonInsight</string>
+				<string>MotivatorInsight</string>
+				<string>BarrierInsight</string>
+				<string>ResourceInsight</string>
+				<string>FitnessActivityRings</string>
+				<string>FitnessMindfulSession</string>
+				<string>FitnessWorkout</string>
+				<string>HealthCategorySample</string>
+				<string>HealthCharacteristics</string>
+				<string>HealthClassification</string>
+				<string>HealthStatistics</string>
+				<string>HealthSleepDaySummary</string>
+				<string>HealthStateOfMindSample</string>
+				<string>HealthOvernightVitalsSummary</string>
+				<string>WorkoutPlaceInsight</string>
+				<string>HealthSummaryInsight</string>
 				<string>Mail</string>
 				<string>Message</string>
 				<string>NLPObservation</string>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>kTCCServiceAddressBook</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/Application Support/AddressBook/</string>
-		<string>/Library/AddressBook/</string>
+		<string>kTCCServiceCalendar</string>
 	</array>
 	<key>com.apple.security.hardened-process</key>
 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.personal-information.addressbook</key>
+	<key>com.apple.security.personal-information.calendars</key>
 	<true/>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<true/>
 	<key>com.apple.private.diagnosticscheckupd.launch</key>
 	<true/>
+	<key>com.apple.private.iokit.assertonlidclose</key>
+	<true/>
 	<key>com.apple.private.iokit.limitedpower-wakerequest</key>
 	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>

```
### knowledge-agent

> `/usr/libexec/knowledge-agent`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
 	<true/>
 	<key>com.apple.proactive.ProactiveSuggestionClientModel.xpc</key>

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
### nexusd

> `/usr/libexec/nexusd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>
 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>

```
### searchpartyuseragent

> `/usr/libexec/searchpartyuseragent`

```diff

 	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### secd

> `/usr/libexec/secd`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.airdrop.client</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.application-service-browse</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.analyticsd</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.callkit.callcontrollerhost</string>

 	<true/>
 	<key>com.apple.studentd-access</key>
 	<true/>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-call-capabilities</string>

```
### sportsd

> `/usr/libexec/sportsd`

```diff

 	<array>
 		<string>group.com.apple.sports</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 	<key>com.apple.watchlist.private.suppression</key>
 	<true/>
 	<key>fairplay-client</key>

```
### spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```diff

 		<dict>
 			<key>Sets</key>
 			<dict>
+				<key>AmbientSensing.Activity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>App.Intents.IndexedEntity</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>GenerativeLearningPlatform.Insight</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>GenerativeLearningPlatform.TestItem</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Health.Measurement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Health.Statistics</key>
 				<dict>
 					<key>mode</key>

```
### spotlightknowledged.importer

> `/usr/libexec/spotlightknowledged.importer`

```diff

 		<dict>
 			<key>Sets</key>
 			<dict>
+				<key>AmbientSensing.Activity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>App.Intents.IndexedEntity</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>GenerativeLearningPlatform.Insight</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>GenerativeLearningPlatform.TestItem</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Health.Measurement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Health.Statistics</key>
 				<dict>
 					<key>mode</key>

```
### spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```diff

 		<dict>
 			<key>Sets</key>
 			<dict>
+				<key>AmbientSensing.Activity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>App.Intents.IndexedEntity</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>GenerativeLearningPlatform.Insight</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>GenerativeLearningPlatform.TestItem</key>
 				<dict>
 					<key>mode</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Health.Measurement</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>Health.Statistics</key>
 				<dict>
 					<key>mode</key>

```
### studentd

> `/usr/libexec/studentd`

```diff

 	<true/>
 	<key>com.apple.private.launchservices.allowedtolaunchwithenvironmentvariables</key>
 	<true/>
+	<key>com.apple.private.managedclient.certpayloadrecovery</key>
+	<true/>
 	<key>com.apple.private.managedclient.configurationprofiles</key>
 	<true/>
 	<key>com.apple.private.notificationcenter-system</key>

```
### sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

 	<array>
 		<string>group.com.apple.VoiceOver</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<string>com.apple.bluetoothuser.xpc</string>
 </dict>

```
### toolkitd

> `/usr/libexec/toolkitd`

```diff

 		<string>(allow distributed-notification-post)</string>
 		<string>(allow file-read* (regex #"\.app($|/)"))</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.homed</string>
+	</array>
 	<key>com.apple.shortcuts.toolkitd</key>
 	<true/>
 </dict>

```
### triald

> `/usr/libexec/triald`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Siri.AnalyticsIdentifiers.UserAggregationId</string>
+		<string>Safari.SearchEngine</string>
 	</array>
 	<key>com.apple.private.cloudkit.buddyAccess</key>
 	<true/>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.powerlog</string>
+	</array>
 	<key>com.apple.triald.system.from-agent</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### triald_system

> `/usr/libexec/triald_system`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.powerlog</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.triald</string>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
+	<key>com.apple.homepodaccessorysettings.client</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.localfindable.tvremote</key>
 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.homepodaccessorysettings.server</string>
 		<string>com.apple.icloud.findmydeviced.localfindable.tvremote</string>
 		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.iohideventsystem</string>

```
### uarpd

> `/usr/libexec/uarpd`

```diff

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.uarpassetmanager.uarp</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocation</key>
+	<true/>
+	<key>com.apple.security.hardened-processs.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>
 	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>

```
### watchdogd

> `/usr/libexec/watchdogd`

```diff

 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>
 	<string>com.apple.watchdogd</string>
+	<key>com.apple.private.xpc.launchd.system-job-bootstrap</key>
+	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>EndpointSecurityExternalClient</string>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>
 	<true/>
-	<key>com.apple.tailspin.config-apply</key>
-	<true/>
-	<key>com.apple.tailspin.dump-output</key>
-	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```


### SystemOS

### com.apple.WebKit.WebContent.Development

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 </dict>
 </plist>
 
-<!-- Launch Constraints (Self) -->
-{
-  "appl": 1,
-  "ccat": 0,
-  "comp": 1,
-  "reqs": {
-    "$or": {
-      "on-authorized-authapfs-volume": true,
-      "on-system-volume": true
-    },
-    "validation-category": 1
-  },
-  "vers": 1
-}
-
-<!-- Launch Constraints (Parent) -->
-{
-  "appl": 1,
-  "ccat": 0,
-  "comp": 1,
-  "reqs": {
-    "is-init-proc": true
-  },
-  "vers": 1
-}
-

```
### com.apple.WebKit.WebContent.Development

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 </dict>
 </plist>
 
-<!-- Launch Constraints (Self) -->
-{
-  "appl": 1,
-  "ccat": 0,
-  "comp": 1,
-  "reqs": {
-    "$or": {
-      "on-authorized-authapfs-volume": true,
-      "on-system-volume": true
-    },
-    "validation-category": 1
-  },
-  "vers": 1
-}
-
-<!-- Launch Constraints (Parent) -->
-{
-  "appl": 1,
-  "ccat": 0,
-  "comp": 1,
-  "reqs": {
-    "is-init-proc": true
-  },
-  "vers": 1
-}
-

```

### 🆕 ProcessorTrace

> `/System/Library/PrivateFrameworks/ProcessorTrace.framework/Versions/A/ProcessorTrace`

- No entitlements *(yet)*
### com.apple.WebKit.WebContent.Development

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 </dict>
 </plist>
 
-<!-- Launch Constraints (Self) -->
-{
-  "appl": 1,
-  "ccat": 0,
-  "comp": 1,
-  "reqs": {
-    "$or": {
-      "on-authorized-authapfs-volume": true,
-      "on-system-volume": true
-    },
-    "validation-category": 1
-  },
-  "vers": 1
-}
-
-<!-- Launch Constraints (Parent) -->
-{
-  "appl": 1,
-  "ccat": 0,
-  "comp": 1,
-  "reqs": {
-    "is-init-proc": true
-  },
-  "vers": 1
-}
-

```
### com.apple.WebKit.WebContent.Development

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 </dict>
 </plist>
 
-<!-- Launch Constraints (Self) -->
-{
-  "appl": 1,
-  "ccat": 0,
-  "comp": 1,
-  "reqs": {
-    "$or": {
-      "on-authorized-authapfs-volume": true,
-      "on-system-volume": true
-    },
-    "validation-category": 1
-  },
-  "vers": 1
-}
-
-<!-- Launch Constraints (Parent) -->
-{
-  "appl": 1,
-  "ccat": 0,
-  "comp": 1,
-  "reqs": {
-    "is-init-proc": true
-  },
-  "vers": 1
-}
-

```


### AppOS

### Safari

> `/System/Applications/Safari.app/Contents/MacOS/Safari`

```diff

 		<string>Safari.PageLoad</string>
 		<string>Safari.WindowProxy</string>
 		<string>Safari.MemoryFootprint</string>
+		<string>Safari.SearchEngine</string>
 		<string>Unilog.SafariSearch.Stage</string>
+		<string>Unilog.SafariFeature.Stage</string>
 		<string>Safari.WebsitesBlockingQuit</string>
 		<string>Safari.Browsing.Assistant</string>
 		<string>Passwords.ChangePasswordForMe</string>

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>Unilog.SafariFeature.Stage</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>Unilog.SafariSearch.Stage</key>
 				<dict>
 					<key>mode</key>

```
### Web App

> `/System/Library/CoreServices/Web App.app/Contents/MacOS/Web App`

```diff

 		<string>Safari.PageLoad</string>
 		<string>Safari.WindowProxy</string>
 		<string>Safari.MemoryFootprint</string>
+		<string>Safari.SearchEngine</string>
 		<string>Unilog.SafariSearch.Stage</string>
+		<string>Unilog.SafariFeature.Stage</string>
 		<string>Safari.WebsitesBlockingQuit</string>
 		<string>Safari.Browsing.Assistant</string>
 		<string>Passwords.ChangePasswordForMe</string>

 		<dict>
 			<key>Streams</key>
 			<dict>
+				<key>Unilog.SafariFeature.Stage</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>Unilog.SafariSearch.Stage</key>
 				<dict>
 					<key>mode</key>

```


