## 🔑 Entitlements

### filesystem

### Books

> `/System/Applications/Books.app/Contents/MacOS/Books`

```diff

 	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>CrashReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>OSAnalytics.Stability.Crash</key>
+				<true/>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.librarian.can-get-application-info</key>
 	<true/>
 	<key>com.apple.private.mobileinstall.upgrade-enabled</key>

```
### BooksNotificationContentExtension

> `/System/Applications/Books.app/Contents/PlugIns/BooksNotificationContentExtension.appex/Contents/MacOS/BooksNotificationContentExtension`

```diff

 	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>CrashReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>OSAnalytics.Stability.Crash</key>
+				<true/>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.iBooks</string>

```
### Calendar

> `/System/Applications/Calendar.app/Contents/MacOS/Calendar`

```diff

 	</array>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.managed.account.identities</string>
 		<string>appleaccount</string>
 	</array>
 </dict>

```
### Contacts

> `/System/Applications/Contacts.app/Contents/MacOS/Contacts`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.suggestions</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

 	<true/>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.managed.account.identities</string>
 		<string>appleaccount</string>
 		<string>apple</string>
 		<string>appleaccount</string>

```
### Freeform

> `/System/Applications/Freeform.app/Contents/MacOS/Freeform`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.associated-domains</key>

```
### Home

> `/System/Applications/Home.app/Contents/MacOS/Home`

```diff

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.rapport.Client</key>
+	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>

```
### HomeWidget

> `/System/Applications/Home.app/Contents/PlugIns/HomeWidget.appex/Contents/MacOS/HomeWidget`

```diff

 	<true/>
 	<key>com.apple.coremedia.endpointremotecontrolsession.xpc</key>
 	<true/>
-	<key>com.apple.developer.declared-age-range</key>
-	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
-	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
-	<string>com.apple.Home</string>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
 	<array>
 		<string>com.apple.HomePlatformSettingsUI.ViewService</string>

```
### Maps

> `/System/Applications/Maps.app/Contents/MacOS/Maps`

```diff

 	<true/>
 	<key>com.apple.maps.model-access</key>
 	<true/>
+	<key>com.apple.maps.suggestions.signalpipeline</key>
+	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### Messages

> `/System/Applications/Messages.app/Contents/MacOS/Messages`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.iconservices</string>
+		<string>com.apple.iconservices.store</string>
 		<string>com.apple.lockdownmoded</string>
 		<string>com.apple.AudioAccessoryAssetManagementXPCService</string>
 		<string>com.apple.mobileactivationd</string>

```
### MessagesPluginNotificationExtension

> `/System/Applications/Messages.app/Contents/PlugIns/MessagesPluginNotificationExtension.appex/Contents/MacOS/MessagesPluginNotificationExtension`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
 </dict>
 </plist>
 

```
### Notes

> `/System/Applications/Notes.app/Contents/MacOS/Notes`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>

```
### Passwords

> `/System/Applications/Passwords.app/Contents/MacOS/Passwords`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.people</key>

```
### Photos

> `/System/Applications/Photos.app/Contents/MacOS/Photos`

```diff

 	<array>
 		<string>IOSurfaceAcceleratorParavirtClient</string>
 	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.modelmanager</string>
-		<string>com.apple.photos.ImageConversionService</string>
-		<string>com.apple.siri.uaf.subscription.service</string>
-	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.OmniSearch</string>

 		<string>com.apple.passd.payment</string>
 		<string>com.apple.visualintelligence.visual-action-prediction</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### Siri AI

> `/System/Applications/Siri AI.app/Contents/MacOS/Siri AI`

```diff

 	<true/>
 	<key>com.apple.private.Safari.History</key>
 	<true/>
+	<key>com.apple.private.SkyLight.event.monitor</key>
+	<true/>
 	<key>com.apple.private.SkyLight.systemgestures</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### TV

> `/System/Applications/TV.app/Contents/MacOS/TV`

```diff

 	<true/>
 	<key>com.apple.amp.library.client</key>
 	<true/>
+	<key>com.apple.appleaccount.identity.read</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.TV</string>
 	<key>com.apple.authkit.client.internal</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.aa.identity.xpc</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.amsaccountsd.security</string>

```
### VoiceMemosIntentsExtension

> `/System/Applications/VoiceMemos.app/Contents/PlugIns/VoiceMemosIntentsExtension.appex/Contents/MacOS/VoiceMemosIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.coreaudio.register-internal-aus</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
 	<key>com.apple.developer.siri</key>
 	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.VoiceMemos</string>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### LaunchPolicyAlertAgent

> `/System/Library/CoreServices/DeviceManagementClient/LaunchPolicyAlertAgent.app/Contents/MacOS/LaunchPolicyAlertAgent`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
-<dict/>
+<dict>
+	<key>com.apple.private.backgroundtaskmanagement.manage</key>
+	<true/>
+	<key>com.apple.private.security.storage.backgroundtaskmanagement</key>
+	<true/>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
+</dict>
 </plist>
 

```
### Dock

> `/System/Library/CoreServices/Dock.app/Contents/MacOS/Dock`

```diff

 	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.launchservices.allowedtoforciblyremoveapplicationfromrunninglist</key>
+	<true/>
 	<key>com.apple.private.launchservices.disclaimroleasparentapplication</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

```
### Setup Assistant

> `/System/Library/CoreServices/Setup Assistant.app/Contents/MacOS/Setup Assistant`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
-		<string>com.apple.MobileAsset.SetupAssistantNewFeaturesIntroduction</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsMac</string>
 	</array>

```
### mbuseragent

> `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/mbuseragent`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### mbusertrampoline

> `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/mbusertrampoline`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### MiniLauncher

> `/System/Library/CoreServices/Setup Assistant.app/Contents/SharedSupport/MiniLauncher`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
+	<key>com.apple.cdp.walrus</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### SpotlightPreferenceExtension

> `/System/Library/CoreServices/Spotlight.app/Contents/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
-		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### Spotlight

> `/System/Library/CoreServices/Spotlight.app/Contents/MacOS/Spotlight`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
-		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>

```
### System Events

> `/System/Library/CoreServices/System Events.app/Contents/MacOS/System Events`

```diff

 <dict>
 	<key>com.apple.Settings.extension.host</key>
 	<true/>
+	<key>com.apple.private.launchservices.canBeIgnoredForParentExitDetection</key>
+	<true/>
 	<key>com.apple.private.responsibility.set-arbitrary</key>
 	<true/>
 	<key>com.apple.private.tcc.allow-prompting</key>

```
### settings

> `/System/Library/CoreServices/UAUPlugins/SystemSettingsUserAccountUpdater.bundle/Contents/Resources/settings`

```diff

 	<string>*</string>
 	<key>com.apple.private.linkd.observationStatusRegistry</key>
 	<true/>
+	<key>com.apple.private.settings-search-reindex</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.siri</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

```

### 🆕 destinationd

> `/System/Library/CoreServices/destinationd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CoreRoutine.LocationOfInterest</key>
	<true/>
	<key>com.apple.CoreRoutine.LocationOfInterest.Delete</key>
	<true/>
	<key>com.apple.CoreRoutine.Prediction</key>
	<true/>
	<key>com.apple.CoreRoutine.VehicleLocation</key>
	<true/>
	<key>com.apple.CoreRoutine.Visit</key>
	<true/>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.cards.all-access</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.weather</string>
	<key>com.apple.developer.weatherkit</key>
	<true/>
	<key>com.apple.finance.private</key>
	<true/>
	<key>com.apple.finance.store</key>
	<true/>
	<key>com.apple.findmy.findmylocate.friendshipservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.locationservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.settings</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.geoservices.navigation_info</key>
	<true/>
	<key>com.apple.geoservices.setanydefault</key>
	<true/>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.intents.uiextension.discovery</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.private_info</key>
	<true/>
	<key>com.apple.locationd.route_hint</key>
	<true/>
	<key>com.apple.locationd.slv_configurer</key>
	<true/>
	<key>com.apple.locationd.spectator</key>
	<true/>
	<key>com.apple.locationd.usage_oracle</key>
	<true/>
	<key>com.apple.maps.model-access</key>
	<true/>
	<key>com.apple.maps.virtualgarage.vehicles</key>
	<true/>
	<key>com.apple.mobile.deleted.AllowFreeSpace</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd</string>
	</dict>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.maps.destinationd</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>FindMy.ContactActivity</string>
		<string>Maps.Suggestions.RecentConversationsIntent</string>
	</array>
	<key>com.apple.private.calendar.allow-suggestions</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.externalaccessory.showallaccessories</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.Maps</string>
	</array>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.suggestions.events</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
	<array>
		<string>com.apple.weather</string>
	</array>
	<key>com.apple.proactive.PersonalizationPortrait.Connections</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.Location.readOnly</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.weather.internal</string>
		<string>group.com.apple.Maps</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/System/Library/Preferences/Logging/</string>
		<string>/AppleInternal/Library/Preferences/Logging/</string>
		<string>/Library/Preferences/Logging/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Weather/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.Maps.Suggestions/</string>
		<string>/Library/HTTPStorages/com.apple.MapsSuggestions/</string>
		<string>/Library/Caches/com.apple.MapsSuggestions/</string>
		<string>/Library/Caches/com.apple.MapsIntelligence/</string>
		<string>/Library/Caches/Configuration/remote-configuration</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.weatherkit.authservice</string>
		<string>com.apple.finance.store</string>
		<string>com.apple.financed.service.financestore</string>
		<string>com.apple.financed.service.store </string>
		<string>com.apple.financed.service.coredatastore</string>
		<string>com.apple.findmy.findmylocate.friendshipservice</string>
		<string>com.apple.findmy.findmylocate.locationservice</string>
		<string>com.apple.findmy.findmylocate.settings</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.findmy.findmylocate.settings</string>
		<string>com.apple.coremedia.endpointremotecontrolsession.xpc</string>
		<string>com.apple.iapd.xpc</string>
		<string>com.apple.contactsd</string>
		<string>com.apple.iap2d.xpc</string>
		<string>com.apple.kvsd</string>
		<string>com.apple.iap2d.ExternalAccessory.distributednotification.server</string>
		<string>com.apple.ExternalAccessory.distributednotification.server</string>
		<string>com.apple.iaptransportd.ExternalAccessory.distributednotification.server</string>
		<string>com.apple.accessories.externalaccessory-server</string>
		<string>com.apple.calaccessd</string>
		<string>com.apple.proactive.PersonalizationPortrait.Connections</string>
		<string>com.apple.remindd</string>
		<string>com.apple.FileCoordination</string>
		<string>com.apple.NPKCompanionAgent.library</string>
		<string>com.apple.passd.library</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.coremedia.endpoint.xpc</string>
		<string>com.apple.airplay.endpoint.xpc</string>
		<string>com.apple.mediaexperience.endpoint.xpc</string>
		<string>com.apple.Maps.mapspushd</string>
		<string>com.apple.routined.registration</string>
		<string>com.apple.duet.expertcenter</string>
		<string>com.apple.Maps.IPC</string>
		<string>com.apple.navigationListener</string>
		<string>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</string>
		<string>com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite</string>
		<string>com.apple.proactive.PersonalizationPortrait.Location.readOnly</string>
		<string>com.apple.Maps.MapsSync.store</string>
		<string>com.apple.maps.virtualgarage.server</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read</key>
	<array>
		<string>com.apple.weather.internal</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.coremedia</string>
		<string>com.apple.MapsSuggestions</string>
		<string>com.apple.mobilecal</string>
		<string>com.apple.NanoHomeScreen.SmartStackSuggestions</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.weather.internal</string>
		<string>com.apple.suggestions</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.configurationprofiles</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Trial/</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Weather/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.Maps.mapspushd</string>
		<string>com.apple.routined.registration</string>
		<string>com.apple.Maps.IPC</string>
		<string>com.apple.CalendarAgent.proxy</string>
		<string>com.apple.Maps.MapsSync.store</string>
	</array>
	<key>com.apple.security.ts.geoservices</key>
	<true/>
	<key>com.apple.security.ts.location-services</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.maps.destinationd</string>
	<key>com.apple.trial.client</key>
	<array>
		<string>1660</string>
		<string>MAPS_SUGGESTIONS</string>
	</array>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### screencaptureui

> `/System/Library/CoreServices/screencaptureui.app/Contents/MacOS/screencaptureui`

```diff

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCalendar</string>
+		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.security.application-groups</key>
 	<array>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
 	<key>com.apple.security.personal-information.calendars</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>

 		<string>com.apple.visualintelligence.visual-action-prediction</string>
 		<string>com.apple.CalendarAgent</string>
 		<string>com.apple.calaccessd</string>
+		<string>com.apple.contactsd</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.Feedback.DraftingExtension.viewservice</string>

```
### AppleIDSettings

> `/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings`

```diff

 	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.developer.aps-environment</key>

```
### BiomeSELFIngestor

> `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/Contents/MacOS/BiomeSELFIngestor`

```diff

 		<dict>
 			<key>Streams</key>
 			<array>
-				<string>IntelligenceFlow.Transcript.Datastream</string>
 				<string>IntelligenceFlow.Experimentation</string>
 				<string>IntelligenceFlow.JointResolverTelemetry</string>
 				<string>IntelligenceFlow.PlanResolutionTelemetry</string>

```

### 🆕 CDsAndDvDsSettingsIntents

> `/System/Library/ExtensionKit/Extensions/CDsAndDvDsSettingsIntents.appex/Contents/MacOS/CDsAndDvDsSettingsIntents`

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

```
### ClassroomDeviceExpert

> `/System/Library/ExtensionKit/Extensions/ClassroomDeviceExpert.appex/Contents/MacOS/ClassroomDeviceExpert`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/Contents/MacOS/ComposeReviewExtension`

```diff

 		<string>com.apple.xpc.amstoold</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
 	</array>
-	<key>com.apple.security.iokit-user-client-class</key>
-	<string>com_apple_driver_FairPlayIOKitUserClient</string>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### DesktopSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DesktopSettingsIntents.appex/Contents/MacOS/DesktopSettingsIntents`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.launchservices.changedefaulthandlers</key>
 	<array>
 		<string>http</string>

```
### FamilySettings

> `/System/Library/ExtensionKit/Extensions/FamilySettings.appex/Contents/MacOS/FamilySettings`

```diff

 	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>development</string>
 	<key>com.apple.developer.hardened-process</key>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/Contents/MacOS/FedStatsPluginDynamic`

```diff

 		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
 		<string>HKQuantityTypeIdentifierStepCount</string>
 		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
+		<string>HKCharacteristicTypeIdentifierFitzpatrickSkinType</string>
+		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
 		<string>HKQuantityTypeIdentifierVO2Max</string>
+		<string>HKQuantityTypeIdentifierAppleExerciseTime</string>
 		<string>HKActivitySummaryTypeIdentifier</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Pcc-Recitation-Block-Rate</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>PrivateMLClient.RecitationMetrics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Pegasus-Partial-URLs</key>
 		<dict>
 			<key>Streams</key>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/Contents/MacOS/FedStatsPluginStatic`

```diff

 		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
 		<string>HKQuantityTypeIdentifierStepCount</string>
 		<string>HKCharacteristicTypeIdentifierBiologicalSex</string>
+		<string>HKCharacteristicTypeIdentifierFitzpatrickSkinType</string>
+		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
 		<string>HKQuantityTypeIdentifierVO2Max</string>
+		<string>HKQuantityTypeIdentifierAppleExerciseTime</string>
 		<string>HKActivitySummaryTypeIdentifier</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>Pcc-Recitation-Block-Rate</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>PrivateMLClient.RecitationMetrics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Pegasus-Partial-URLs</key>
 		<dict>
 			<key>Streams</key>

```
### GameCenterMacOSSettingsExtension

> `/System/Library/ExtensionKit/Extensions/GameCenterMacOSSettingsExtension.appex/Contents/MacOS/GameCenterMacOSSettingsExtension`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.contactsui</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```

### 🆕 GameControllerSettingsIntents

> `/System/Library/ExtensionKit/Extensions/GameControllerSettingsIntents.appex/Contents/MacOS/GameControllerSettingsIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
	<string>com.apple.Settings</string>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Settings</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### IntelligencePlatformDataActionsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/IntelligencePlatformDataActionsAppIntentsExtension.appex/Contents/MacOS/IntelligencePlatformDataActionsAppIntentsExtension`

```diff

 		<string>App.InFocus</string>
 		<string>Media.NowPlaying</string>
 		<string>ScreenTime.AppUsage</string>
+		<string>Intelligence.Usage</string>
 		<string>Device.Display.Backlight</string>
 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### InternationalSettingsExtension

> `/System/Library/ExtensionKit/Extensions/InternationalSettingsExtension.appex/Contents/MacOS/InternationalSettingsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 </dict>

```
### NotificationsSettingsIntents

> `/System/Library/ExtensionKit/Extensions/NotificationsSettingsIntents.appex/Contents/MacOS/NotificationsSettingsIntents`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.notificationcenter.preferences</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### OBCEngagePlugin

> `/System/Library/ExtensionKit/Extensions/OBCEngagePlugin.appex/Contents/MacOS/OBCEngagePlugin`

```diff

 	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>Location.Semantic</string>
 		<string>Location.MicroLocationVisit</string>
 		<string>Location.Visit</string>
 		<string>Location.SignificantLocation</string>

 		<dict>
 			<key>Streams</key>
 			<array>
+				<string>Location.Semantic</string>
 				<string>Location.MicroLocationVisit</string>
 				<string>Location.Visit</string>
 				<string>Location.SignificantLocation</string>

```
### ODDFeatureDigestsExtension

> `/System/Library/ExtensionKit/Extensions/ODDFeatureDigestsExtension.appex/Contents/MacOS/ODDFeatureDigestsExtension`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
+		<string>Siri.ODDI.ODDAssistantLLMSiriDigests</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

```

### 🆕 SafariUsageRetentionExtension

> `/System/Library/ExtensionKit/Extensions/SafariUsageRetentionExtension.appex/Contents/MacOS/SafariUsageRetentionExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.safari.SafariUsageRetentionExtension</string>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.safari.SafariUsageRetentionExtension</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SafariUsageRetention</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Lighthouse.Ledger.TaskCustomEvent</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Unilog.SafariSearch.Aggregation</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Unilog.SafariSearch.Stage</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>UnilogInstrumentation.IdentifierProvider</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.SafariSearch.LongTermAggregationId</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.aiml.unilog.healthTelemetry</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.HealthTelemetry</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.mlhost.allowedDictionaryGroups</key>
	<array>
		<string>SafariUsageRetention</string>
	</array>
	<key>com.apple.private.mlhost.dictionaryDelete</key>
	<true/>
	<key>com.apple.private.mlhost.dictionaryRead</key>
	<true/>
	<key>com.apple.private.mlhost.dictionaryWrite</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.mlhostd.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.mlhostd.xpc</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant.support</string>
	</array>
</dict>
</plist>

```

### 🆕 ScreenTimeAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimeAppIntentsExtension.appex/Contents/MacOS/ScreenTimeAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.ScreenTimeAppIntentsExtension</string>
	<key>com.apple.chrono.open-urls-direct</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.developer.default-data-protection</key>
	<string>NSFileProtectionComplete</string>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.team-identifier</key>
	<string>Apple</string>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Settings</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>App.InFocus</string>
		<string>App.MediaUsage</string>
		<string>App.WebUsage</string>
		<string>Device.Display.Backlight</string>
		<string>Intelligence.Usage</string>
		<string>Media.NowPlaying</string>
		<string>Notification.Usage</string>
		<string>ScreenTime.AppUsage</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.managed-settings.effective-read</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screen-time-settings</key>
	<true/>
	<key>com.apple.private.screen-time.persistence</key>
	<true/>
	<key>com.apple.private.usage-tracking</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.UsageTrackingAgent.private</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.ManagedSettingsAgent</string>
		<string>com.apple.ScreenTimeSettingsAgent.private</string>
		<string>com.apple.accountsd.accountmanager</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.DeviceActivity</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.DeviceActivity</string>
	</array>
</dict>
</plist>

```
### ScreenTimePreferencesExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimePreferencesExtension.appex/Contents/MacOS/ScreenTimePreferencesExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.commcenter.coretelephony.xpc</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/Contents/MacOS/SearchToolExtension`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
-		<string>com.apple.MobileAsset.UAF.Siri.AnswerSynthesis</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>

 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_AnswerSynthesis/purpose_auto/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>UAF_AB_ANSWER_SYNTHESIS</string>
-		<string>SEARCH_TOOL_ANSWER_SYNTHESIS</string>
 		<string>337</string>
 		<string>755</string>
 	</array>

```
### SiriPreferenceExtension

> `/System/Library/ExtensionKit/Extensions/SiriPreferenceExtension.appex/Contents/MacOS/SiriPreferenceExtension`

```diff

 	</array>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>
-		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
-		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
-		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/Contents/MacOS/SiriSuggestionsLightHousePlugin`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.siri.inference</string>
 		<string>group.com.apple.siri.sirisuggestions</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### SpotlightPreferenceExtension

> `/System/Library/ExtensionKit/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
-		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### StartupDiskWidgetExtension

> `/System/Library/ExtensionKit/Extensions/StartupDiskWidgetExtension.appex/Contents/MacOS/StartupDiskWidgetExtension`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### TGOnDeviceInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/TGOnDeviceInferenceProviderService.appex/Contents/MacOS/TGOnDeviceInferenceProviderService`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
+		<string>com.apple.MobileAsset.UAF.Translation.MMAssets</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.tgondeviceinferenceproviderservice</string>

```
### TimeMachineSettingsIntents

> `/System/Library/ExtensionKit/Extensions/TimeMachineSettingsIntents.appex/Contents/MacOS/TimeMachineSettingsIntents`

```diff

 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
 	<string>com.apple.systempreferences</string>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.systempreferences</string>
+	<string>com.apple.Settings</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 </dict>

```
### AppIntentsDiagnosticExtension

> `/System/Library/Frameworks/AppIntents.framework/Versions/A/PlugIns/AppIntentsDiagnosticExtension.appex/Contents/MacOS/AppIntentsDiagnosticExtension`

```diff

 	<array>
 		<string>com.apple.linkd.registry</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.linkd.registry</string>
+	</array>
 </dict>
 </plist>
 

```
### WorkflowServiceRunner

> `/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/WorkflowServiceRunner.xpc/Contents/MacOS/WorkflowServiceRunner`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.responsibility.set-to-self.at-launch</key>
+	<true/>
+	<key>com.apple.private.tcc.allow-prompting</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
+</dict>
+</plist>
 

```
### WorkflowServiceRunner

> `/System/Library/Frameworks/AppKit.framework/Versions/Current/XPCServices/WorkflowServiceRunner.xpc/Contents/MacOS/WorkflowServiceRunner`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.responsibility.set-to-self.at-launch</key>
+	<true/>
+	<key>com.apple.private.tcc.allow-prompting</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
+</dict>
+</plist>
 

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

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.cascade.donation-requester</key>
+	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
 	<array>
 		<string>com.apple.pay.finance.development</string>
-		<string>com.apple.pay.finance.dropbox.development</string>
 	</array>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.pay.finance</string>
-		<string>com.apple.pay.finance.dropbox</string>
 	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>

```
### managedappdistributionagent

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributionagent`

```diff

 		<string>CLIENT_ENTITLEMENT</string>
 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 	</array>
-	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
-	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.ignoreAppProtection</key>

 	</array>
 	<key>com.apple.private.OAHSoftwareUpdate</key>
 	<true/>
-	<key>com.apple.private.ProvInfoIOKitUserClient.access</key>
-	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.adid</key>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 		<string>system.install.apple-software.standard-user</string>
 		<string>system.install.software.mdm-provided</string>
 	</array>
-	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
-	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

```
### MediaPlayerDiagnosticExtension

> `/System/Library/Frameworks/MediaPlayer.framework/Versions/A/PlugIns/MediaPlayerDiagnosticExtension.appex/Contents/MacOS/MediaPlayerDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.musicd</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/MediaServices/</string>

```
### MediaPlayerDiagnosticExtension

> `/System/Library/Frameworks/MediaPlayer.framework/Versions/Current/PlugIns/MediaPlayerDiagnosticExtension.appex/Contents/MacOS/MediaPlayerDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.musicd</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/MediaServices/</string>

```
### SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>

```

### 🆕 SpeechEncryptedLogsDiagnostic

> `/System/Library/Frameworks/Speech.framework/Versions/A/PlugIns/SpeechEncryptedLogsDiagnostic.appex/Contents/MacOS/SpeechEncryptedLogsDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.logging.admin</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/</string>
		<string>/Library/Logs/CrashReporter/Assistant/</string>
		<string>/Library/Logs/CrashReporter/VoiceTrigger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.logd.admin</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.icl</string>
	</array>
</dict>
</plist>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/Versions/A/XPCServices/localspeechrecognition.xpc/Contents/MacOS/localspeechrecognition`

```diff

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.speech.localspeechrecognition</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>com.apple.AppleIntelligence.Reporting.Invocation.Step</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.Invocation.Step</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/Versions/Current/XPCServices/localspeechrecognition.xpc/Contents/MacOS/localspeechrecognition`

```diff

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.speech.localspeechrecognition</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>com.apple.AppleIntelligence.Reporting.Invocation.Step</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.Invocation.Step</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>

```
### AppIntentsLiveEntityService

> `/System/Library/PrivateFrameworks/AppIntentsLiveEntitySupport.framework/XPCServices/AppIntentsLiveEntityService.xpc/Contents/MacOS/AppIntentsLiveEntityService`

```diff

 	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
-	<key>com.apple.private.sandbox.profile:embedded</key>
-	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
-	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
-	<array>
-		<string>/Library/com.apple.PrivacyDisclosure/</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.appprotectiond.guard</string>
-		<string>com.apple.appprotectiond.read</string>
-		<string>com.apple.linkd.extension</string>
-		<string>com.apple.linkd.mediator</string>
-		<string>com.apple.linkd.registry</string>
-	</array>
 	<key>com.apple.security.system-container</key>
 	<true/>
 </dict>

```
### appstoreagent

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstoreagent`

```diff

 	</array>
 	<key>com.apple.private.OAHSoftwareUpdate</key>
 	<true/>
-	<key>com.apple.private.ProvInfoIOKitUserClient.access</key>
-	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.adid</key>

```
### AAUIFollowUpExtension_macOS

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension_macOS.appex/Contents/MacOS/AAUIFollowUpExtension_macOS`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
 	<key>com.apple.cdp.walrus</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
+	<key>com.apple.private.security.storage.PhotosLibraries</key>
+	<true/>
 	<key>com.apple.private.security.storage.SiriReferenceResolution</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriSELF</key>

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceMotion</string>
+		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceWillow</string>
 	</array>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/Support/akd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.recovery</key>
+	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
 	<key>com.apple.cdp.walrus</key>

```
### AKFollowUpExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/Contents/MacOS/AKFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.writer.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
 	<key>com.apple.developer.game-center</key>
 	<array>
 		<string>Account</string>

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.aggregated.addaily</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.iohideventsystem</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### CDPFollowUpExtension

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/Contents/MacOS/CDPFollowUpExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.recovery</key>
+	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
+	<key>com.apple.cdp.telemetry</key>
+	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

```
### speechmaintenanced

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/speechmaintenanced`

```diff

 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### corespeechd_system

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system`

```diff

 	<true/>
 	<key>com.apple.AudioAccessorySystemStateService</key>
 	<true/>
+	<key>com.apple.CompanionLink</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.account.AppleAccount</key>

 	<true/>
 	<key>com.apple.corespeech.cat.xpc</key>
 	<true/>
+	<key>com.apple.developer.homekit</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<array>
 		<string>endpoint-read</string>
 	</array>
+	<key>com.apple.private.homekit</key>
+	<true/>
+	<key>com.apple.private.homekit.allow-access-without-prompting</key>
+	<true/>
 	<key>com.apple.private.homekit.siri-audio-connection</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceMicrophone</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceBluetoothAlways</string>
+		<string>kTCCServiceHomeKit</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Caches/com.apple.HomeKit.configurations</string>
+		<string>/Library/Caches/com.apple.HomeKit</string>
 		<string>/Library/DES/Records/com.apple.siri.speech-dictation-personalization/</string>
 		<string>/Library/VoiceTrigger/</string>
 		<string>/Library/Logs/CrashReporter/Assistant/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.homed.xpc</string>
+		<string>com.apple.CompanionLink</string>
 		<string>com.apple.polaris.cache</string>
 		<string>com.apple.siri.deviceselection</string>
 		<string>com.apple.account.AppleAccount</string>

```
### IMDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/Contents/MacOS/IMDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/Versions/A/XPCServices/FilesystemMetadataSnapshotService.xpc/Contents/MacOS/FilesystemMetadataSnapshotService`

```diff

 <dict>
 	<key>com.apple.private.apfs.get-graft-info</key>
 	<true/>
+	<key>com.apple.private.vfs.snapshot</key>
+	<true/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
 </dict>

```
### FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/Versions/Current/XPCServices/FilesystemMetadataSnapshotService.xpc/Contents/MacOS/FilesystemMetadataSnapshotService`

```diff

 <dict>
 	<key>com.apple.private.apfs.get-graft-info</key>
 	<true/>
+	<key>com.apple.private.vfs.snapshot</key>
+	<true/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
 </dict>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/Resources/familycircled`

```diff

 	<true/>
 	<key>com.apple.authkit.familyDeviceList</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/Current/Resources/familycircled`

```diff

 	<true/>
 	<key>com.apple.authkit.familyDeviceList</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

```
### ParentalControls

> `/System/Library/PrivateFrameworks/FamilyControls.framework/Versions/A/Resources/ParentalControls.app/Contents/MacOS/ParentalControls`

```diff

 	<true/>
 	<key>com.apple.asktod</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.logind.spi</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

```
### ParentalControls

> `/System/Library/PrivateFrameworks/FamilyControls.framework/Versions/Current/Resources/ParentalControls.app/Contents/MacOS/ParentalControls`

```diff

 	<true/>
 	<key>com.apple.asktod</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.logind.spi</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.skgupdater</key>
 	<true/>
+	<key>com.apple.private.device-configuration.effective-configuration-ids.read</key>
+	<array>
+		<string>com.apple.modelcatalog</string>
+	</array>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

```
### healthd

> `/System/Library/PrivateFrameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.fitnesscoachingd</key>
 	<true/>
+	<key>com.apple.fitnessintelligenced</key>
+	<true/>
 	<key>com.apple.frontboard.app-badge-value-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.fitnesscoachingd</string>
+		<string>com.apple.fitnessintelligenced</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.health.RemoteHeartRateStreamService</string>
 		<string>com.apple.healthrecordsd</string>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
 	<key>com.apple.private.AppleMediaServices</key>

 		<string>com.apple.CommunicationTrust</string>
 		<string>com.apple.MobileStoreDemo.test</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-write</key>
+	<array>
+		<string>kern.memorystatus_vm_pressure_send</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/Versions/A/intelligencecontextd`

```diff

 	</array>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.generativeexperiences.agentMediaStore</key>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceScreenCapture</string>
 	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceLiverpool</string>
-		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
-		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceSpeechRecognition</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>
-		<string>kTCCServiceSiri</string>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>

 		<string>1760</string>
 		<string>INTELLIGENCE_FLOW_QUERY_DECORATOR</string>
 		<string>SIRI_SECURITY_IPI</string>
+		<string>SIRI_INTELLIGENCE_FLOW_PLANNER</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### IntelligencePlatformComputeService

> `/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/Versions/A/XPCServices/IntelligencePlatformComputeService.xpc/Contents/MacOS/IntelligencePlatformComputeService`

```diff

 	</dict>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
-	<key>com.apple.private.photos.XPCStoreOptIn</key>
-	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.IntelligencePlatform</key>

```
### intelligenceplatformd

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/intelligenceplatformd`

```diff

 		<string>App.MediaUsage</string>
 		<string>Media.NowPlaying</string>
 		<string>ScreenTime.AppUsage</string>
+		<string>Intelligence.Usage</string>
 		<string>WalletPaymentsCommerce.FoundIn.OrderEmail</string>
 		<string>WalletPaymentsCommerce.FoundIn.ClassicOrder</string>
 		<string>WalletPaymentsCommerce.FoundIn.Transaction</string>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/knowledgeconstructiond`

```diff

 		<string>Device.Display.Backlight</string>
 		<string>Media.NowPlaying</string>
 		<string>ScreenTime.AppUsage</string>
+		<string>Intelligence.Usage</string>
 		<string>WalletPaymentsCommerce.FoundIn.OrderEmail</string>
 		<string>WalletPaymentsCommerce.FoundIn.ClassicOrder</string>
 		<string>WalletPaymentsCommerce.FoundIn.Transaction</string>

```
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/Versions/A/XPCServices/Managed Background Assets Helper Service.xpc/Contents/MacOS/Managed Background Assets Helper Service`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>
+		<string>/private/var/mobile/Containers/Data/Application/*/tmp/com.apple.backgroundassets.managed.helper.service/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	<array>
 		<string>com.apple.backgroundassets.managed.helper.fetching.service</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.spaceattributiond</string>
+		<string>com.apple.userprofiles</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fpsd</string>
+	</array>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>
 	<key>com.apple.spaceattribution.private</key>

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```

### 🆕 Managed Background Assets Relay Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/Versions/A/XPCServices/Managed Background Assets Relay Service.xpc/Contents/MacOS/Managed Background Assets Relay Service`

- No entitlements *(yet)*
### Managed Background Assets Helper Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/Versions/Current/XPCServices/Managed Background Assets Helper Service.xpc/Contents/MacOS/Managed Background Assets Helper Service`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.userprofiles.read</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>
+		<string>/private/var/mobile/Containers/Data/Application/*/tmp/com.apple.backgroundassets.managed.helper.service/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	<array>
 		<string>com.apple.backgroundassets.managed.helper.fetching.service</string>
 		<string>com.apple.fairplaydeviceidentityd</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.spaceattributiond</string>
+		<string>com.apple.userprofiles</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fpsd</string>
+	</array>
 	<key>com.apple.security.ts.daemon-container</key>
 	<true/>
 	<key>com.apple.spaceattribution.private</key>

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```

### 🆕 Managed Background Assets Relay Service

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssets.framework/Versions/Current/XPCServices/Managed Background Assets Relay Service.xpc/Contents/MacOS/Managed Background Assets Relay Service`

- No entitlements *(yet)*
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Bundle/</string>

```
### com.apple.MobileInstallationHelperService

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/XPCServices/com.apple.MobileInstallationHelperService.xpc/Contents/MacOS/com.apple.MobileInstallationHelperService`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceSystemPolicyDesktopFolder</string>
 		<string>kTCCServiceSystemPolicyAppBundles</string>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 	</array>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/searchtoold`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.omniSearch.searchtoold</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
-		<string>com.apple.MobileAsset.UAF.Siri.AnswerSynthesis</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>

 		<string>kTCCServiceSystemPolicyAllFiles</string>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
+		<string>kTCCServiceSiriAccess</string>
+	</array>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceSiriAccess</string>
 	</array>
 	<key>com.apple.private.xpc.launchd.app-server</key>
 	<true/>

 		<string>com.apple.managedcorespotlightd</string>
 		<string>com.apple.diagnosticpipeline.service</string>
 		<string>com.apple.omniSearch.search</string>
-		<string>com.apple.omniSearch.answerSynthesis</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.mediaanalysisd.analysis</string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>UAF_AB_ANSWER_SYNTHESIS</string>
 		<string>337</string>
 		<string>755</string>
 	</array>

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/Contents/MacOS/privatecloudcomputed`

```diff

 	</array>
 	<key>com.apple.private.cloudtelemetry</key>
 	<true/>
+	<key>com.apple.private.container.access</key>
+	<dict>
+		<key>daemon</key>
+		<dict>
+			<key>com.apple.privatecloudcomputed</key>
+			<dict>
+				<key>data</key>
+				<dict>
+					<key>access</key>
+					<string>path-only</string>
+					<key>operations</key>
+					<array>
+						<string>delete</string>
+					</array>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>TransparencyLogging</key>

 	<true/>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.SBUserNotification</string>

```
### scrod

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/A/Resources/scrod`

```diff

 	</array>
 	<key>com.apple.generativeexperiences.summarization</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-privileged</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appGroup</key>

```
### scrod

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/Current/Resources/scrod`

```diff

 	</array>
 	<key>com.apple.generativeexperiences.summarization</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-privileged</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appGroup</key>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/Versions/A/ScreenTimeSettingsAgent`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.settings-search-reindex</key>
+	<true/>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

```

### 🆕 SettingsSearchReindexService

> `/System/Library/PrivateFrameworks/SettingsServices.framework/Versions/A/XPCServices/SettingsSearchReindexService.xpc/Contents/MacOS/SettingsSearchReindexService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SettingsServices.Reindexer</string>
	</array>
</dict>
</plist>

```

### 🆕 SettingsSearchReindexService

> `/System/Library/PrivateFrameworks/SettingsServices.framework/Versions/Current/XPCServices/SettingsSearchReindexService.xpc/Contents/MacOS/SettingsSearchReindexService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SettingsServices.Reindexer</string>
	</array>
</dict>
</plist>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/siriinferenced`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/Versions/A/XPCServices/SiriSuggestionsBookkeepingService.xpc/Contents/MacOS/SiriSuggestionsBookkeepingService`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.siri.inference</string>
 		<string>group.com.apple.siri.sirisuggestions</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/Versions/Current/XPCServices/SiriSuggestionsBookkeepingService.xpc/Contents/MacOS/SiriSuggestionsBookkeepingService`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.siri.inference</string>
 		<string>group.com.apple.siri.sirisuggestions</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

```
### StoreKitUIServiceMac

> `/System/Library/PrivateFrameworks/StoreKitUIMac.framework/Versions/A/XPCServices/StoreKitUIServiceMac.xpc/Contents/MacOS/StoreKitUIServiceMac`

```diff

 	<array>
 		<string>group.com.apple.storekit</string>
 	</array>
+	<key>adi-client</key>
+	<string>409835401</string>
 	<key>com.apple.appstored.octane</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

```
### StoreKitUIServiceMac

> `/System/Library/PrivateFrameworks/StoreKitUIMac.framework/Versions/Current/XPCServices/StoreKitUIServiceMac.xpc/Contents/MacOS/StoreKitUIServiceMac`

```diff

 	<array>
 		<string>group.com.apple.storekit</string>
 	</array>
+	<key>adi-client</key>
+	<string>409835401</string>
 	<key>com.apple.appstored.octane</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

```
### STExtractionService.privileged

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/Versions/A/XPCServices/STExtractionService.privileged.xpc/Contents/MacOS/STExtractionService.privileged`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobilegestalt.xpc</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### STExtractionService.privileged

> `/System/Library/PrivateFrameworks/StreamingExtractor.framework/Versions/Current/XPCServices/STExtractionService.privileged.xpc/Contents/MacOS/STExtractionService.privileged`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobilegestalt.xpc</string>
+		<string>com.apple.backgroundassets.managed.relay.service</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 VSTPrecompiledPipelines.metallib

> `/System/Library/PrivateFrameworks/Vista.framework/Versions/A/Resources/VSTPrecompiledPipelines.metallib`

- No entitlements *(yet)*

### 🆕 VSTPrecompiledPipelines.metallib

> `/System/Library/PrivateFrameworks/Vista.framework/Versions/Current/Resources/VSTPrecompiledPipelines.metallib`

- No entitlements *(yet)*
### MediaPlayerDiagnosticExtension

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/PlugIns/MediaPlayerDiagnosticExtension.appex/Contents/MacOS/MediaPlayerDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.musicd</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/MediaServices/</string>

```
### MediaPlayerDiagnosticExtension

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/Current/PlugIns/MediaPlayerDiagnosticExtension.appex/Contents/MacOS/MediaPlayerDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.musicd</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/MediaServices/</string>

```
### launchd

> `/sbin/launchd`

```diff

 	<true/>
 	<key>com.apple.private.set-atm-diagnostic-flag</key>
 	<true/>
+	<key>com.apple.private.shared-region.config</key>
+	<true/>
 	<key>com.apple.private.spawn-panic-crash-behavior</key>
 	<true/>
 	<key>com.apple.private.spawn-subsystem-root</key>

```
### ibv_devices

> `/usr/bin/ibv_devices`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.IORDMACMUC</key>
+	<true/>
 	<key>com.apple.private.IORDMAFamilyUC</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IORDMAFamilyUC</string>
+		<string>IORDMACMUserClient</string>
 	</array>
 </dict>
 </plist>

```
### ibv_devinfo

> `/usr/bin/ibv_devinfo`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.IORDMACMUC</key>
+	<true/>
 	<key>com.apple.private.IORDMAFamilyUC</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IORDMAFamilyUC</string>
+		<string>IORDMACMUserClient</string>
 	</array>
 </dict>
 </plist>

```
### ibv_uc_pingpong

> `/usr/bin/ibv_uc_pingpong`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.IORDMACMUC</key>
+	<true/>
 	<key>com.apple.private.IORDMAFamilyUC</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IORDMAFamilyUC</string>
+		<string>IORDMACMUserClient</string>
 	</array>
 </dict>
 </plist>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.recovery</key>
+	<true/>
 	<key>com.apple.cdp.recoverykey</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
 	<key>com.apple.cdp.walrus.pcskeys</key>

```
### frauddefensed

> `/usr/libexec/frauddefensed`

```diff

 	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>

```
### gamecontrolleragentd

> `/usr/libexec/gamecontrolleragentd`

```diff

 	<string>com.apple.GameController.gamecontrolleragentd</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GameController.gamecontrolleragentd</string>
+	<key>com.apple.gamepolicyd.tool.privileged.xpc</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyDesktopFolder</string>

```
### gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

 	<string>com.apple.GameController.gamecontrollerd</string>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
-	<key>com.apple.developer.game-center</key>
-	<true/>
-	<key>com.apple.gamepolicyd.tool.privileged.xpc</key>
-	<true/>
 	<key>com.apple.hid.manager.user-access-interface-rematch</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access-privileged</key>
 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
-	<key>com.apple.private.game-center</key>
-	<array>
-		<string>Account</string>
-	</array>
 	<key>com.apple.private.game-controller.GCResource</key>
 	<true/>
 	<key>com.apple.private.game-controller.dynamic-device-manager</key>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
-	<string>Development</string>
+	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.mobileinboxupdater.personalization</string>

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.nfcd.hce</key>
 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>

 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.diagnosticscheckupd.launch</key>
+	<true/>
 	<key>com.apple.private.iokit.limitedpower-wakerequest</key>
 	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>

 	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>

 	<true/>
 	<key>com.apple.rootless.volume.iSCHardware</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>
 		<string>com.apple.MIBULoopbackServerHelper</string>
 		<string>com.apple.cloudd</string>
+		<string>com.apple.diagnosticscheckupd</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### linkd

> `/usr/libexec/linkd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.dmd.policy</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.linkd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

```
### logd

> `/usr/libexec/logd`

```diff

 	<true/>
 	<key>com.apple.private.persona-read-all</key>
 	<true/>
+	<key>com.apple.private.security.storage.LogdPreferencesCache</key>
+	<true/>
 	<key>com.apple.private.set-atm-diagnostic-flag</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### nexusd

> `/usr/libexec/nexusd`

```diff

 	<array>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.event-monitor</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Ringtones/</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	</array>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
+	<key>com.apple.private.sharing.paired-contacts</key>
+	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
 	<key>com.apple.private.skywalk.observe-all</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
+	<key>com.apple.geoanalyticsd.telemetry</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 	<true/>
 	<key>com.apple.locationd.Proximity.TagManagement</key>
 	<true/>
+	<key>com.apple.locationd.activity</key>
+	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### searchpartyuseragent

> `/usr/libexec/searchpartyuseragent`

```diff

 	<true/>
 	<key>com.apple.icloud.searchpartyd.access</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.btFinding.access</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.useragentdaemoninternal</key>
 	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>

```
### secd

> `/usr/libexec/secd`

```diff

 	<true/>
 	<key>com.apple.authkit.devicelist.server-only</key>
 	<true/>
+	<key>com.apple.cdp.followup</key>
+	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

```
### spinandd

> `/usr/libexec/spinandd`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.private.iokit.nvram-write-access</key>
+	<true/>
 </dict>
 </plist>
 

```
### spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.cascade.donation-requester</key>
+	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

```
### spotlightknowledged.importer

> `/usr/libexec/spotlightknowledged.importer`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.cascade.donation-requester</key>
+	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

```
### spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```diff

 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.cascade.donation-requester</key>
+	<true/>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

```
### symptomsd

> `/usr/libexec/symptomsd`

```diff

 	<array>
 		<string>com.apple.private.alloy.autobugcapture</string>
 	</array>
+	<key>com.apple.private.iokit.powermanagement.read-assertions</key>
+	<true/>
 	<key>com.apple.private.logging.admin</key>
 	<true/>
 	<key>com.apple.private.nehelper.privileged</key>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	<true/>
 	<key>com.apple.private.appmanagedfeatures.configuration</key>
 	<true/>
+	<key>com.apple.private.container.debug</key>
+	<true/>
 	<key>com.apple.private.eligibilityd.dumpSysdiagnoseDataToDir</key>
 	<true/>
 	<key>com.apple.private.endpoint-security.xpc</key>

```
### trustdFileHelper

> `/usr/libexec/trustdFileHelper`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.trustd</key>
 	<true/>
+	<key>com.apple.private.security.storage.trustd-private</key>
+	<true/>
 </dict>
 </plist>
 

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 		<string>/private/var/preferences/SystemConfiguration/com.apple.wifi.plist</string>
 		<string>/usr/libexec/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/tvremoted/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
-		<string>/Library/Caches/com.apple.HomeKit.configurations/tvremoted/</string>
-		<string>/Library/Caches/com.apple.HomeKit/tvremoted/</string>
+		<string>/Library/Caches/com.apple.HomeKit/com.apple.tvremoted/</string>
 		<string>/Library/Caches/com.apple.tvremoted/</string>
 		<string>/Library/Caches/tvapp_bag/</string>
 		<string>/Library/HTTPStorages/com.apple.tvremoted/</string>
-		<string>/Library/tvremoted/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
-		<string>IOHIDUserDeviceCreate</string>
-		<string>IOHIDResourceDeviceUserClient</string>
-		<string>IOHIDUserClient</string>
 		<string>IO80211APIUserClient</string>
 		<string>IOHIDLibUserClient</string>
+		<string>IOHIDResourceDeviceUserClient</string>
+		<string>IOHIDUserClient</string>
+		<string>IOHIDUserDeviceCreate</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.coreaudio</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.homesharing</string>
+		<string>com.apple.rapport</string>
 		<string>com.apple.Sharing</string>
+		<string>com.apple.TVRemoteCore</string>
 		<string>com.apple.videos-preferences</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### tznotify

> `/usr/libexec/tznotify`

```diff

 <dict>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceSystemPolicyAppData</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.TimeZoneUpdates.tznotify</string>

```
### xpcproxy

> `/usr/libexec/xpcproxy`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.driverkitd</key>
 	<true/>
+	<key>com.apple.private.shared-region.config</key>
+	<true/>
 	<key>com.apple.private.spawn-driver</key>
 	<true/>
 	<key>com.apple.private.spawn-panic-crash-behavior</key>

```
### xprotectd

> `/usr/libexec/xprotectd`

```diff

 <dict>
 	<key>com.apple.developer.endpoint-security.client</key>
 	<true/>
+	<key>com.apple.private.CFPasteboard.invalidate-caches</key>
+	<true/>
 	<key>com.apple.private.endpoint-security.client</key>
 	<true/>
 	<key>com.apple.private.endpointsecurity.publisher</key>

```
### BTLEServer

> `/usr/sbin/BTLEServer`

```diff

 	<true/>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### BTLEServerAgent

> `/usr/sbin/BTLEServerAgent`

```diff

 	<true/>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
-	<key>keychain-access-groups</key>
-	<array>
-		<string>apple</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	</array>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
+	<key>com.apple.developer.homekit</key>
+	<true/>
 	<key>com.apple.driver.AppleBluetoothModule.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleConvergedIPC.user-access</key>

 	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
+	<key>com.apple.homekit.private-spi-access</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.access</key>

 	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
+	<key>com.apple.private.homekit.beacon-keybag</key>
+	<true/>
 	<key>com.apple.private.iokit.nvram-bluetooth</key>
 	<true/>
 	<key>com.apple.private.iokit.powersource-control</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceBluetoothPeripheral</string>
+		<string>kTCCServiceWillow</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>

 		<string>com.apple.backboard.display.services</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.matter.support.xpc</string>
+		<string>com.apple.homed.beacon-keybag</string>
 		<string>com.apple.UXMAssertionService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.ProductKitService</string>

```


### SystemOS

### com.apple.WebKit.GPU

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.sqlite.defensive</key>

```
### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.sqlite.defensive</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.GPU

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.sqlite.defensive</key>

```
### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.sqlite.defensive</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```

### 🆕 com.apple.WebDriver.MCPService

> `/System/Library/PrivateFrameworks/WebDriver.framework/Versions/A/XPCServices/com.apple.WebDriver.MCPService.xpc/Contents/MacOS/com.apple.WebDriver.MCPService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.webinspector.driver</key>
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

### 🆕 com.apple.WebDriver.MCPService

> `/System/Library/PrivateFrameworks/WebDriver.framework/Versions/Current/XPCServices/com.apple.WebDriver.MCPService.xpc/Contents/MacOS/com.apple.WebDriver.MCPService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.webinspector.driver</key>
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
### com.apple.WebKit.GPU

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### com.apple.WebKit.Networking

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.Development

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.GPU

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### com.apple.WebKit.Networking

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.Development

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.Development.xpc/Contents/MacOS/com.apple.WebKit.WebContent.Development`

```diff

 	<array>
 		<string>jit</string>
 	</array>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.EnhancedSecurity.xpc/Contents/MacOS/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```
### com.apple.WebKit.WebContent

> `/System/iOSSupport/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	</array>
 	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
 	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>

```


### AppOS

### Safari

> `/System/Applications/Safari.app/Contents/MacOS/Safari`

```diff

 		<string>Safari.PageLoad</string>
 		<string>Safari.WindowProxy</string>
 		<string>Safari.MemoryFootprint</string>
+		<string>Unilog.SafariSearch.Stage</string>
 		<string>Safari.WebsitesBlockingQuit</string>
 		<string>Safari.Browsing.Assistant</string>
 		<string>Passwords.ChangePasswordForMe</string>

```
### PasswordManagerBrowserExtensionHelper

> `/System/Library/CoreServices/PasswordManagerBrowserExtensionHelper.app/Contents/MacOS/PasswordManagerBrowserExtensionHelper`

```diff

 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>3</integer>
+	<integer>4</integer>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.associated-domains</key>

```
### Web App

> `/System/Library/CoreServices/Web App.app/Contents/MacOS/Web App`

```diff

 		<string>Safari.PageLoad</string>
 		<string>Safari.WindowProxy</string>
 		<string>Safari.MemoryFootprint</string>
+		<string>Unilog.SafariSearch.Stage</string>
 		<string>Safari.WebsitesBlockingQuit</string>
 		<string>Safari.Browsing.Assistant</string>
 		<string>Passwords.ChangePasswordForMe</string>

```
### SafariBookmarksSyncAgent

> `/usr/libexec/SafariBookmarksSyncAgent`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.Safari</string>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>*</string>
 	<key>com.apple.private.safari.can-use-sandbox-broker</key>

```


