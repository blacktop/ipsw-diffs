## 🔑 Entitlements

### filesystem

### Calendar

> `/System/Applications/Calendar.app/Contents/MacOS/Calendar`

```diff

 	</array>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

 		<string>com.apple.DeviceConfigurationAgent.publisher</string>
 		<string>com.apple.deviceconfigurationd.consumer</string>
 		<string>com.apple.deviceconfigurationd.publisher</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FaceTime

> `/System/Applications/FaceTime.app/Contents/MacOS/FaceTime`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.AddressBook</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.aps-client-cert-access</key>

```
### Games

> `/System/Applications/Games.app/Contents/MacOS/Games`

```diff

 	</array>
 	<key>com.apple.runningboard.jetengine</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.servicesintelligenced</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

```
### HomeEnergyWidgetsExtension

> `/System/Applications/Home.app/Contents/PlugIns/HomeEnergyWidgetsExtension.appex/Contents/MacOS/HomeEnergyWidgetsExtension`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.energykit</key>
 	<true/>
 	<key>com.apple.private.homeenergy</key>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.wpc.energyservices.keychain</string>

```
### GenerativePlaygroundAppIntents

> `/System/Applications/Image Playground.app/Contents/Extensions/GenerativePlaygroundAppIntents.appex/Contents/MacOS/GenerativePlaygroundAppIntents`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
+	<true/>
+	<key>com.apple.generativeexperiences.ExternalProviderService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
+		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.stickers.recency</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.ciphermld</string>
+		<string>com.apple.generativeexperiences.ExternalProviderService</string>
+		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### Journal

> `/System/Applications/Journal.app/Contents/MacOS/Journal`

```diff

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.das.private.bgtask.continuedprocessing</key>
 	<true/>
 	<key>com.apple.developer.declared-age-range</key>

```
### Mail

> `/System/Applications/Mail.app/Contents/MacOS/Mail`

```diff

 	<true/>
 	<key>com.apple.private.accounts.configuration-resolve</key>
 	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/AppleInternal/Library/Frameworks/ContextStagingIntents.framework</string>
+	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.AddressBook</string>
+	</array>
 	<key>com.apple.private.biome.pruner</key>
 	<array>
 		<string>Mail.Categorization</string>

 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>
+		<string>(allow file-issue-extension (extension-class "com.apple.spotlight.importer.readonly"))</string>
 		<string>(read-write-and-issue-extensions (regex (string-append "^/Volumes/" (uuid-regex-string) "(/|$)")))</string>
 		<string>(allow distributed-notification-post)</string>
 	</array>

```
### Messages

> `/System/Applications/Messages.app/Contents/MacOS/Messages`

```diff

 	<array>
 		<string>/System/iOSSupport/System/Library/PrivateFrameworks/ChatKit.framework</string>
 	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.AddressBook</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### Notes

> `/System/Applications/Notes.app/Contents/MacOS/Notes`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/AppleInternal/Library/Frameworks/ContextStagingIntents.framework</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### com.apple.Notes.SharingExtension

> `/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.SharingExtension.appex/Contents/MacOS/com.apple.Notes.SharingExtension`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
 	<key>com.apple.private.exchangesyncd</key>

```
### PasswordsMenuBarExtra

> `/System/Applications/Passwords.app/Contents/Library/LoginItems/PasswordsMenuBarExtra.app/Contents/MacOS/PasswordsMenuBarExtra`

```diff

 		<string>io.island.Island.dev</string>
 		<string>ru.yandex.desktop.yandex-browser</string>
 		<string>ai.perplexity.comet</string>
+		<string>ai.perplexity.comet-beta</string>
 		<string>ai.perplexity.comet-canary</string>
 		<string>ai.perplexity.comet-dev</string>
 		<string>com.coccoc.Coccoc</string>

```
### Phone

> `/System/Applications/Phone.app/Contents/MacOS/Phone`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-opus-codec</key>
 	<true/>
+	<key>com.apple.coreaudio.private.HasMicrophoneInjectionAccess</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.AddressBook</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.aps-client-cert-access</key>

 		<string>com.apple.biome.compute.publisher.service.user</string>
 		<string>com.apple.TextUnderstanding.process</string>
 		<string>com.apple.duetexpertd.assistant-actions</string>
+		<string>com.apple.sirittsd</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.support</string>
 		<string>com.apple.logging</string>
 		<string>com.apple.VideoConference</string>
 		<string>com.apple.GVAEncoder</string>

```
### Photos

> `/System/Applications/Photos.app/Contents/MacOS/Photos`

```diff

 	<true/>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.photos.service.debug</key>
 	<true/>
 	<key>com.apple.private.photos.service.diagnostics</key>

 	<array>
 		<string>com.apple.tipsd</string>
 	</array>
+	<key>com.apple.privatecloudcompute.knownRateLimits</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.privatecloudcompute</string>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.cloudphotod</string>

```
### Podcasts

> `/System/Applications/Podcasts.app/Contents/MacOS/Podcasts`

```diff

 	<true/>
 	<key>com.apple.developer.declared-age-range</key>
 	<true/>
+	<key>com.apple.developer.networking.carrier-constrained.app-optimized</key>
+	<false/>
+	<key>com.apple.developer.networking.carrier-constrained.appcategory</key>
+	<string>podcast-8017</string>
+	<key>com.apple.developer.networking.non-terrestrial.app-optimized</key>
+	<false/>
+	<key>com.apple.developer.networking.non-terrestrial.appcategory</key>
+	<string>podcast-8017</string>
 	<key>com.apple.developer.pass-type-identifiers</key>
 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>

 	<array>
 		<string>/private/var/mobile/Media/Podcasts/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>Library/UserConfigurationProfiles/Truth.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/DeviceRegistry/</string>

```
### Shortcuts

> `/System/Applications/Shortcuts.app/Contents/MacOS/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>

 				<string>IntelligencePlatform.Entity</string>
 			</array>
 		</dict>
+		<key>com.apple.shortcuts</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>Mail</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.intelligenceplatform.InternalBiome</string>
 		<string>com.apple.intelligenceplatform.KnowledgeConstruction</string>

 		<string>com.apple.siriactionsd.xpc</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.toolkitd.xpc</string>
+		<string>com.apple.wallpaper.public</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.TimeMachine</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.voiceservices</string>

```

### 🆕 Siri AI

> `/System/Applications/Siri AI.app/Contents/MacOS/Siri AI`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.campo</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.CoreRoutine.Application</key>
	<true/>
	<key>com.apple.CoreRoutine.LocationOfInterest</key>
	<true/>
	<key>com.apple.FaceTime.NoPrompt</key>
	<true/>
	<key>com.apple.Pasteboard.background-access</key>
	<true/>
	<key>com.apple.QuartzCore.global-capture</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.StatusKit.subscribe.types</key>
	<array>
		<string>com.apple.focus.status</string>
		<string>com.apple.availability</string>
	</array>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.amp.devices.client</key>
	<true/>
	<key>com.apple.apfs.unlock</key>
	<true/>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.assistant.client</key>
	<true/>
	<key>com.apple.assistant.request-dispatcher.uibridge-service</key>
	<true/>
	<key>com.apple.assistant.uibridge-service</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.coreduetd.people</key>
	<true/>
	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
	<true/>
	<key>com.apple.developer.extension-host.widget-extension</key>
	<true/>
	<key>com.apple.developer.icloud-services</key>
	<true/>
	<key>com.apple.developer.maps</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.Spotlight</string>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.duet.expertcenter.consumer</key>
	<true/>
	<key>com.apple.duetexpertd.assistant-actions</key>
	<true/>
	<key>com.apple.facetimemessagestored.service</key>
	<array>
		<string>access-facetime-messaging</string>
	</array>
	<key>com.apple.familycircle.agent</key>
	<true/>
	<key>com.apple.feedbackd.remote-evaluation</key>
	<true/>
	<key>com.apple.filederivatives.derive</key>
	<true/>
	<key>com.apple.filederivatives.list</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.fileprovider.extension-host</key>
	<true/>
	<key>com.apple.fileprovider.fetch-url</key>
	<true/>
	<key>com.apple.findmy.findmylocate.friendshipservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.locationservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.settings</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</key>
	<true/>
	<key>com.apple.generativeexperiences.agentMediaStore</key>
	<true/>
	<key>com.apple.generativeexperiences.agentSessionStore</key>
	<true/>
	<key>com.apple.generativeexperiences.corefollowup</key>
	<true/>
	<key>com.apple.icloud.fmfd.access</key>
	<true/>
	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
	<true/>
	<key>com.apple.intelligenceflow.context</key>
	<true/>
	<key>com.apple.intelligenceflow.contextIntelligence</key>
	<true/>
	<key>com.apple.intelligenceflow.contextTool</key>
	<true/>
	<key>com.apple.intelligenceflow.internal</key>
	<true/>
	<key>com.apple.intelligenceflow.orchestrator</key>
	<true/>
	<key>com.apple.intelligenceflow.orchestrator.features</key>
	<array>
		<string>executable-session</string>
		<string>debugging</string>
		<string>side-channel-debugging</string>
		<string>transcript-manipulation</string>
	</array>
	<key>com.apple.intelligenceflow.querydecoration</key>
	<true/>
	<key>com.apple.intelligenceflow.toolbox</key>
	<true/>
	<key>com.apple.intelligenceflow.transcript-entity-querying</key>
	<true/>
	<key>com.apple.intelligenceflow.transcript-entity-querying.query-all-groups</key>
	<true/>
	<key>com.apple.intelligenceflow.uiContext</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.Knosis</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.intelligenceplatform.knosis.indexes.read-only</key>
	<array>
		<string>stableGraphIndex</string>
		<string>eventGraphIndex</string>
		<string>liveGlobalKnowledgeIndex</string>
		<string>staticGlobalKnowledgeIndex</string>
		<string>ontologyIndex</string>
	</array>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.intents.uiextension.discovery</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.allow.background-processing-assertions</key>
	<true/>
	<key>com.apple.keystore.lockassertion</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.locationd.activity</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.time_zone</key>
	<true/>
	<key>com.apple.locationd.usage_oracle</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.menubar.campo</key>
	<true/>
	<key>com.apple.mobileassetd.v2</key>
	<true/>
	<key>com.apple.mobilemail.mailservices</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.pegasus.context</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.powerexperience.powermode.update</key>
	<true/>
	<key>com.apple.private.CallHistory.read</key>
	<true/>
	<key>com.apple.private.ClipServices</key>
	<true/>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.lookup</key>
	<dict>
		<key>appData</key>
		<array>
			<string>com.apple.SiriNCService</string>
		</array>
	</dict>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.Safari.History</key>
	<true/>
	<key>com.apple.private.SkyLight.systemgestures</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/SpotlightUIShared.framework</string>
		<string>/System/Library/PrivateFrameworks/SearchUI.framework</string>
	</array>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.appintents.trusted-entity-identifier</key>
	<true/>
	<key>com.apple.private.appleevents.allowedtosend</key>
	<dict>
		<key>com.apple.private.appleevents.allowed.aevt.odoc</key>
		<true/>
		<key>com.apple.private.appleevents.allowed.aevt.spot</key>
		<true/>
		<key>com.apple.private.appleevents.allowed.fndr.ovir</key>
		<true/>
	</dict>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstorecomponents.media-client-id</key>
	<string>com.apple.Siri.app</string>
	<key>com.apple.private.appstorecomponents.media-client-version</key>
	<string>1</string>
	<key>com.apple.private.aps-connection-initiate</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.TempMorphunData</string>
		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNL</string>
		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNLOverrides</string>
		<string>com.apple.MobileAsset.SpotlightResources</string>
		<string>com.apple.MobileAsset.LinguisticData</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.assistant.analytics</key>
	<true/>
	<key>com.apple.private.assistant.client</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/Applications/Spotlight.app</string>
	</dict>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.CampoApp</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Accessibility.ReduceMotion</string>
		<string>Accessibility.ReduceTransparency</string>
		<string>Accessibility.ColorFilters</string>
		<string>Accessibility.SmartInvert</string>
		<string>Accessibility.VoiceOver</string>
		<string>Accessibility.Zoom</string>
		<string>Accessibility.VoiceControl</string>
		<string>Accessibility.Contrast</string>
		<string>Accessibility.ClassicInvert</string>
		<string>Accessibility.WhitePoint</string>
		<string>App.InFocus</string>
		<string>App.Install</string>
		<string>AskToBuy</string>
		<string>CarPlay.Connected</string>
		<string>Clock.Alarm</string>
		<string>Family.ScreenTime.ChildState</string>
		<string>Device.Display.AlwaysOn</string>
		<string>Device.Display.Appearance</string>
		<string>Device.Display.NightShift</string>
		<string>Device.ScreenLocked</string>
		<string>Device.SilentMode</string>
		<string>Device.Display.TrueTone</string>
		<string>Device.Power.EnergyMode</string>
		<string>Device.Wireless.AirplaneMode</string>
		<string>Device.Wireless.BluetoothPowerEnabled</string>
		<string>Device.Wireless.CellularDataEnabled</string>
		<string>Device.Wireless.WiFiAvailabilityStatus</string>
		<string>Media.NowPlaying</string>
		<string>Motion.Activity</string>
		<string>ScreenTimeRequest</string>
		<string>UserFocus.ComputedMode</string>
		<string>UserFocusComputedMode</string>
		<string>IntelligenceFlow.Transcript.Datastream</string>
		<string>SiriExecution</string>
		<string>AppLaunch</string>
		<string>AppIntent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Siri.PostSiriEngagement</string>
		<string>PostSiriEngagement</string>
		<string>Motion.ObservedBehavior</string>
		<string>Motion.TripSegment</string>
		<string>Siri.FeedbackLearning.UserInteractions</string>
		<string>IntelligenceEngine.Interaction.Donation</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeModels.GenerativeFunctions.Events</string>
		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>
		<string>IntelligenceFlow.Telemetry</string>
		<string>IntelligenceFlow.ResponseGeneration</string>
		<string>IntelligenceFlow.ExecutorTelemetry</string>
		<string>Discoverability.Signals</string>
		<string>Intelligence.Usage</string>
	</array>
	<key>com.apple.private.calendar.allow-integrations</key>
	<true/>
	<key>com.apple.private.calendar.allow-suggestions</key>
	<true/>
	<key>com.apple.private.canGetAppLinkInfo</key>
	<true/>
	<key>com.apple.private.canrunwithoutvisibleui</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.contactsui</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.coreservices.canaccessanysharedfilelist</key>
	<string>read-only</string>
	<key>com.apple.private.coreservices.cangetcurrentactivityinfo</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.corespeech.corespeechservices</key>
	<true/>
	<key>com.apple.private.corespeech.xpc</key>
	<true/>
	<key>com.apple.private.corespeech.xpc.remote</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.sender</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.dmd.emergency-mode</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.dock.spotlight</key>
	<true/>
	<key>com.apple.private.email</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.feedback.centralized-feedback</key>
	<true/>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.generativesearch.client.search</key>
	<true/>
	<key>com.apple.private.hid.client.event-dispatch.internal</key>
	<true/>
	<key>com.apple.private.hid.client.event-monitor</key>
	<true/>
	<key>com.apple.private.iaaccounts</key>
	<true/>
	<key>com.apple.private.imcore.imagent</key>
	<true/>
	<key>com.apple.private.imcore.spi.database-access</key>
	<true/>
	<key>com.apple.private.ind.client</key>
	<true/>
	<key>com.apple.private.intelligenceflow.group-identifier</key>
	<string>com.apple.intelligenceflow</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>AppInFocusHeartbeat</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>App.InFocus</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>Assistant</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Siri.Service</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>Pasteboard</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Pasteboard.Change</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>ProactiveAppPrediction</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>App.InFocus</string>
			</array>
		</dict>
		<key>SpotlightEngagementData</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>App.InFocus</string>
				<string>App.Intent</string>
				<string>SystemSettings.SearchTerms</string>
				<string>Media.NowPlaying</string>
			</array>
		</dict>
		<key>com.apple.spotlightui</key>
		<dict>
			<key>Search</key>
			<array>
				<string>Global</string>
				<string>SiriTranscript</string>
				<string>SiriTranscriptConversation</string>
				<string>Mail</string>
				<string>DraftMail</string>
				<string>MailAttachment</string>
			</array>
		</dict>
		<key>generativesearch</key>
		<dict>
			<key>Search</key>
			<array>
				<string>SiriTranscript</string>
				<string>SiriTranscriptConversation</string>
			</array>
		</dict>
		<key>iftool.dump-stream</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>IntelligenceFlow.Telemetry</string>
				<string>IntelligenceFlow.ResponseGeneration</string>
				<string>IntelligenceFlow.ExecutorTelemetry</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>siriRemembers</string>
		<string>visualIdentifier</string>
		<string>nerdSummary</string>
		<string>behavioralPopularitySignals</string>
		<string>nerdEmbeddingsPeopleTable</string>
		<string>peopleAliasECR</string>
		<string>entitySummary</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>peopleSubgraph</string>
		<string>appleMusicEventSubgraph</string>
		<string>appleMusicEventMap</string>
		<string>people</string>
		<string>eventSubgraph</string>
		<string>relevance</string>
		<string>inferenceFeaturesECR</string>
		<string>appEntityRelevanceRanking</string>
		<string>personEntityRelevanceRanking</string>
		<string>personEntityLongTermRanking</string>
		<string>loiEntityRelevanceRanking</string>
		<string>defaultResolverInteractions</string>
		<string>bundleIdMap</string>
		<string>ifContextSubgraph</string>
		<string>entitySimilarityFeatures</string>
	</array>
	<key>com.apple.private.iokit.darkwake-control</key>
	<true/>
	<key>com.apple.private.iokit.powersource-control</key>
	<true/>
	<key>com.apple.private.kernel.override-cpumon</key>
	<true/>
	<key>com.apple.private.launchpad.list</key>
	<true/>
	<key>com.apple.private.launchservices.cansetapplicationstrusted</key>
	<true/>
	<key>com.apple.private.launchservices.disclaimroleasparentapplication</key>
	<true/>
	<key>com.apple.private.librarian.container-proxy</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.mailservice.all</key>
	<true/>
	<key>com.apple.private.managed-settings.effective-read</key>
	<true/>
	<key>com.apple.private.menubar.allow</key>
	<true/>
	<key>com.apple.private.metadata.exattrs</key>
	<true/>
	<key>com.apple.private.mobileinstall.allowedSPI</key>
	<array>
		<string>UninstallForLaunchServices</string>
	</array>
	<key>com.apple.private.mobiletimerd</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.network.system-token-fetch</key>
	<true/>
	<key>com.apple.private.notificationcenter.menu</key>
	<true/>
	<key>com.apple.private.notificationcenter.siri</key>
	<true/>
	<key>com.apple.private.notificationcenter.snippet</key>
	<true/>
	<key>com.apple.private.notificationcenterui.alerts</key>
	<true/>
	<key>com.apple.private.notificationcenterui.nchostable</key>
	<array>
		<string>com.apple.Siri</string>
	</array>
	<key>com.apple.private.nsurlsession.set-task-priority</key>
	<true/>
	<key>com.apple.private.parsec.default-client</key>
	<string>com.apple.campo</string>
	<key>com.apple.private.persona.adopt.any</key>
	<true/>
	<key>com.apple.private.persona.read</key>
	<true/>
	<key>com.apple.private.photos.allowcollectionshare</key>
	<true/>
	<key>com.apple.private.photos.allowlibraryupgrade</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.librarymanagement</key>
	<true/>
	<key>com.apple.private.remindd</key>
	<dict/>
	<key>com.apple.private.replicator.controller</key>
	<true/>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.screen-time-settings</key>
	<true/>
	<key>com.apple.private.screencontinuity.app-launch</key>
	<true/>
	<key>com.apple.private.screentime-downtime</key>
	<true/>
	<key>com.apple.private.screentime-setup</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.intelligenceflow</string>
		<string>group.com.apple.spotlight</string>
		<string>group.com.apple.tipsnext</string>
		<string>group.tvappservices.container</string>
		<string>.SiriTodayViewExtension</string>
	</array>
	<key>com.apple.private.security.storage.AppDataContainers</key>
	<true/>
	<key>com.apple.private.security.storage.FindMy</key>
	<true/>
	<key>com.apple.private.security.storage.Mail</key>
	<true/>
	<key>com.apple.private.security.storage.Messages</key>
	<true/>
	<key>com.apple.private.security.storage.MessagesMetaData</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.MobileDocuments</key>
	<true/>
	<key>com.apple.private.security.storage.Notes</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.SiriInference</key>
	<true/>
	<key>com.apple.private.security.storage.SiriVocabulary</key>
	<true/>
	<key>com.apple.private.security.storage.Spotlight</key>
	<true/>
	<key>com.apple.private.security.storage.Weather</key>
	<true/>
	<key>com.apple.private.security.storage.containers</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.security.storage.triald</key>
	<true/>
	<key>com.apple.private.security.storage.universalaccess</key>
	<true/>
	<key>com.apple.private.sessionkit.listener</key>
	<true/>
	<key>com.apple.private.sessionkit.sessionContributor</key>
	<true/>
	<key>com.apple.private.sharing.unlock-manager</key>
	<true/>
	<key>com.apple.private.siri.audiopowerupdate.xpc</key>
	<true/>
	<key>com.apple.private.siri.setup</key>
	<true/>
	<key>com.apple.private.siriappintentsd.orchestrator</key>
	<true/>
	<key>com.apple.private.sleepd</key>
	<true/>
	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>
	<true/>
	<key>com.apple.private.sportskit.client</key>
	<true/>
	<key>com.apple.private.spotlight.parsec</key>
	<true/>
	<key>com.apple.private.spotlight.search.internal</key>
	<true/>
	<key>com.apple.private.ssr.voiceprofileservice</key>
	<true/>
	<key>com.apple.private.subscriptionservice.internal</key>
	<true/>
	<key>com.apple.private.suggestions.contacts</key>
	<true/>
	<key>com.apple.private.suggestions.events</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAccessibility</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceAppleEvents</string>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceFaceID</string>
		<string>kTCCServiceLocation</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceReminders</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServicePhotosAdd</string>
		<string>kTCCServiceSystemPolicyAllFiles</string>
		<string>kTCCServiceSystemPolicyDesktopFolder</string>
		<string>kTCCServiceSystemPolicyDocumentsFolder</string>
		<string>kTCCServiceSystemPolicyDownloadsFolder</string>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.tcc.events.subscriber</key>
	<true/>
	<key>com.apple.private.tcc.manager.access.read</key>
	<array>
		<string>kTCCServiceAll</string>
	</array>
	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
	<array>
		<string>com.apple.weather</string>
		<string>com.apple.tipsd</string>
	</array>
	<key>com.apple.private.vfs.open-by-id</key>
	<true/>
	<key>com.apple.private.viewbridge.window.child.transparent</key>
	<true/>
	<key>com.apple.private.viewbridge.window.level</key>
	<true/>
	<key>com.apple.private.windowmanager</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.proactive.ActionPrediction.predictions</key>
	<true/>
	<key>com.apple.proactive.AppPrediction.predictions</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</key>
	<true/>
	<key>com.apple.proactive.appDirectory</key>
	<true/>
	<key>com.apple.proactive.client.predictions</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
	<true/>
	<key>com.apple.rootless.storage.proactivepredictions</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.routined.registration</key>
	<true/>
	<key>com.apple.runningboard.assertions.angeltarget</key>
	<true/>
	<key>com.apple.runningboard.assertions.angeltarget.campo</key>
	<true/>
	<key>com.apple.runningboard.assertions.shortcuts</key>
	<true/>
	<key>com.apple.runningboard.assertions.siri</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.posterkit.host</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.searchd.appservice</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<false/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.weather.internal</string>
		<string>group.tvappservices.container</string>
		<string>group.com.apple.intelligenceflow</string>
		<string>com.apple.spotlightui</string>
		<string>group.com.apple.spotlight</string>
		<string>group.com.apple.tipsnext</string>
		<string>group.com.apple.notes</string>
		<string>.SiriTodayViewExtension</string>
		<string>group.com.apple.siri.sirisuggestions</string>
	</array>
	<key>com.apple.security.device.bluetooth</key>
	<true/>
	<key>com.apple.security.device.microphone</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/</string>
		<string>/Applications/</string>
		<string>/Library/WebClips/</string>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/private/var/mobile/Library/Trial/</string>
		<string>/private/var/MobileAsset/</string>
		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Weather/</string>
		<string>/private/var/mobile/Library/DuetExpertCenter/caches/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/CallHistoryDB/</string>
		<string>/Library/com.apple.WatchListKit/</string>
		<string>/Library/ContactsMetadata/</string>
		<string>/Library/DuetExpertCenter/</string>
		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
		<string>/Library/SMS/</string>
		<string>/Media/PhotoData/</string>
		<string>/Library/MessagesMetaData/NickNameCache/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/SNLUOverrides.sqlite</string>
		<string>/Library/Application Support/SNLUOverrides.sqlite-shm</string>
		<string>/Library/Application Support/SNLUOverrides.sqlite-wal</string>
		<string>/Library/Assistant/ContinuousDialogManager/</string>
		<string>/Library/Assistant/SiriNLUOverrides/</string>
		<string>/Library/Logs/MediaServices/</string>
		<string>/Library/Shortcuts/</string>
		<string>/Library/Logs/com.apple.FeatureStore/</string>
		<string>/Library/IntelligencePlatform/</string>
		<string>/Library/Application Support/IntelligenceFlow/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.managedappdistributiond.xpc</string>
		<string>com.apple.AppDistributionLaunchAngel</string>
		<string>com.apple.ClipServices.clipserviced</string>
		<string>com.apple.duet.expertcenter</string>
		<string>com.apple.icloud.fmfd</string>
		<string>com.apple.lsdiconservice</string>
		<string>com.apple.proactive.ActionPrediction.predictions</string>
		<string>com.apple.proactive.AppPrediction.predictions</string>
		<string>com.apple.routined.registration</string>
		<string>com.apple.siri.activation.service</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
		<string>com.apple.watchlistd.xpc</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.biome.PublicStreamAccessService</string>
		<string>com.apple.ScreenTimeAgent.ask</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.ScreenTimeAgent.downtime</string>
		<string>com.apple.ScreenTimeAgent.setup</string>
		<string>com.apple.sportsd.xpc</string>
		<string>com.apple.findmy.findmylocate.friendshipservice</string>
		<string>com.apple.findmy.findmylocate.locationservice</string>
		<string>com.apple.findmy.findmylocate.settings</string>
		<string>com.apple.MobileTimer.alarmserver</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.write</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.calaccessd</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.triald.namespace-management</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.intelligenceplatform.Knosis</string>
		<string>com.apple.MobileAsset.SpotlightResources</string>
		<string>com.apple.itunescloud.remote-request-execution-service</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.internal.SpotlightAutomationTester</string>
		<string>com.apple.intelligenceflow.context</string>
		<string>com.apple.intelligenceflow.contextTool</string>
		<string>com.apple.intelligenceflow.uiContext</string>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.MediaGroups.daemon</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.seserviced.session</string>
		<string>com.apple.passd.library</string>
		<string>com.apple.sessionservices</string>
		<string>com.apple.translationd</string>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.nanomapsgd.xpc.MapsSuggestions</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.siriinferenced</string>
		<string>com.apple.siriinferenced.remembers</string>
		<string>com.apple.remindd</string>
		<string>com.apple.spotlight.IndexAgent</string>
		<string>com.apple.spotlight.SearchAgent</string>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.Maps.mapspushd</string>
		<string>com.apple.MobileTimer.timerserver</string>
		<string>com.apple.navigationListener</string>
		<string>com.apple.suggestd.contacts</string>
		<string>com.apple.suggestd.events</string>
		<string>com.apple.proactive.PersonalizationPortrait.QuickType</string>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
		<string>com.apple.itunescloud.in-app-message-service</string>
		<string>com.apple.remindd.userInteractive</string>
		<string>com.apple.sysdiagnose.service.xpc</string>
		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
		<string>com.apple.icloud.searchpartyd.pairingmanager</string>
		<string>com.apple.icloud.searchpartyd.ownersession</string>
		<string>com.apple.CompanionLink</string>
		<string>com.apple.SharingServices</string>
		<string>com.apple.dmd.emergency-mode</string>
		<string>com.apple.dmd.policy</string>
		<string>com.apple.assistant.flow_service</string>
		<string>com.apple.coreduetd.context</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.coreduetd.people</string>
		<string>com.apple.siriknowledged</string>
		<string>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</string>
		<string>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</string>
		<string>com.apple.siri-distributed-evaluation</string>
		<string>com.apple.siri.morphunassetsupdaterd</string>
		<string>com.apple.assistant.notification_service</string>
		<string>com.apple.shazamd</string>
		<string>com.apple.shazamd.ui</string>
		<string>com.apple.siri.device_resolution</string>
		<string>com.apple.icloud.searchparty.locationfetch.items</string>
		<string>com.apple.icloud.searchpartyd.securelocations</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.mediator</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.carpd.xpc</string>
		<string>com.apple.sirittsd</string>
		<string>com.apple.coreduetd.batterysaver</string>
		<string>com.apple.powerd.lowpowermode</string>
		<string>com.apple.backlightd</string>
		<string>com.apple.coremedia.flashlight</string>
		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
		<string>com.apple.locationd.synchronous</string>
		<string>com.apple.locationd.registration</string>
		<string>com.apple.locationd.spi</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.omniSearch.search</string>
		<string>com.apple.omniSearch.answerSynthesis</string>
		<string>com.apple.generativeexperiences.agentSessionStore</string>
		<string>com.apple.generativeexperiences.agentMediaStore</string>
		<string>com.apple.intelligenceflow.orchestrator</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.StatusKit.subscribe</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.email.maild</string>
		<string>com.apple.assistant.request-dispatcher.uibridge-service</string>
		<string>com.apple.assistant.uibridge-service</string>
		<string>com.apple.generativesearch.server.search</string>
		<string>com.apple.generativeexperiences.corefollowup</string>
		<string>com.apple.ScreenTimeSettingsAgent.private</string>
		<string>com.apple.private.siriappintentsd.orchestrator</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.generativepartnerservicesettings</string>
		<string>com.apple.siri.generativeassistantsettings</string>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.assistant.logging</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.token</string>
		<string>com.apple.Notes</string>
		<string>com.apple.speech.recognition.AppleSpeechRecognition.prefs</string>
		<string>com.apple.voicetrigger</string>
		<string>com.apple.ironwood.support</string>
		<string>com.apple.siri.internal</string>
		<string>com.apple.weather.internal</string>
		<string>com.apple.mobilesafarishared</string>
		<string>com.apple.cloud.quota</string>
		<string>com.apple.generativesearch</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AppPredictionWidget.defaults</string>
		<string>com.apple.AppStoreComponents</string>
		<string>com.apple.DataDeliveryServices</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>AGXDeviceUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AppleJPEGDriverUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>AppleVirtIONeuralEngineDeviceUserClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelContext2</string>
		<string>IOAccelDevice</string>
		<string>IOAccelDevice2</string>
		<string>IOAccelSharedUserClient</string>
		<string>IOAccelSharedUserClient2</string>
		<string>IOAccelSubmitter2</string>
		<string>IOHIDEventServiceFastPathUserClient</string>
		<string>IOMobileFramebufferUserClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>IOSurfaceRootUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.addressbook</key>
	<true/>
	<key>com.apple.security.personal-information.calendars</key>
	<true/>
	<key>com.apple.security.personal-information.contacts</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>com.apple.security.personal-information.photos-library</key>
	<true/>
	<key>com.apple.security.scripting-targets</key>
	<dict>
		<key>com.apple.Notes</key>
		<array>
			<string>com.apple.Notes.openlocation</string>
		</array>
		<key>com.apple.iTunes</key>
		<array>
			<string>com.apple.iTunes.playback</string>
		</array>
		<key>com.apple.systempreferences</key>
		<array>
			<string>preferencepane.reveal</string>
		</array>
	</dict>
	<key>com.apple.security.temporary-exception.apple-events</key>
	<array>
		<string>com.apple.Safari</string>
		<string>com.apple.finder</string>
		<string>com.apple.systempreferences</string>
		<string>com.apple.mail</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/</string>
		<string>/AppleInternal/Applications/</string>
		<string>/AppleInternal/Library/Assistant/</string>
		<string>/AppleInternal/Library/Frameworks/</string>
		<string>/System/Library/SystemProfiler/SPStorageReporter.spreporter</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
	<array>
		<string>/dev/null</string>
		<string>/private/var/tmp/siriBC</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Containers/com.apple.Notes/Data/</string>
		<string>/Library/VoiceTrigger/</string>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts/</string>
		<string>/Library/Mail/</string>
		<string>/Library/Caches/com.apple.speech.siri/</string>
		<string>/Library/Caches/GeoServices/</string>
		<string>/Library/Containers/com.apple.Notes/Data/Library/Notes/</string>
		<string>/Library/Assistant/</string>
		<string>/Library/Logs/Assistant/</string>
		<string>/Library/Containers/com.apple.SiriNCService/Data/Library/Preferences/</string>
		<string>/Library/Containers/com.apple.Siri.SiriTodayExtension/Data/Library/Preferences/</string>
		<string>/Library/VoiceTrigger/</string>
	</array>
	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
	<array>
		<string>IOMobileFramebufferUserClient</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ind.xpc</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.MenuBarAgent.systemservices</string>
		<string>com.apple.DataDeliveryServices.AssetService</string>
		<string>com.apple.storeassetd</string>
		<string>com.apple.commerce</string>
		<string>com.apple.awdd</string>
		<string>com.apple.analyticsd</string>
		<string>com.apple.rtcreportingd</string>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.MobileTimer.alarmserver</string>
		<string>com.apple.StatusKit.subscribe</string>
		<string>com.apple.ScreenTimeAgent.downtime</string>
		<string>com.apple.sleepd.sleepserver</string>
		<string>com.apple.toolbox.indexing-service</string>
		<string>com.apple.biome.compute.publisher.service.user</string>
		<string>com.apple.proactive.client.predictions</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.sirittsd</string>
		<string>com.apple.MobileTimer.timerserver</string>
		<string>com.apple.assistant.uibridge-service</string>
		<string>com.apple.assistant.request-dispatcher.uibridge-service</string>
		<string>com.apple.remoted</string>
		<string>com.apple.corespeech.corespeechservices</string>
		<string>com.apple.parsecd</string>
		<string>com.apple.airportd</string>
		<string>com.apple.assistant.analytics</string>
		<string>com.apple.assistant.client</string>
		<string>com.apple.assistantd.managedstorage</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.assistant.sync</string>
		<string>com.apple.backlightd</string>
		<string>com.apple.cache_delete</string>
		<string>com.apple.CoreDisplay.master</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.corerecents.recentsd</string>
		<string>com.apple.diskmanagementd</string>
		<string>com.apple.dock.launchpad</string>
		<string>com.apple.familycontrols</string>
		<string>com.apple.GSSCred</string>
		<string>com.apple.iohideventsystem</string>
		<string>com.apple.mediaremoted.xpc</string>
		<string>com.apple.notificationcenterui.alerts</string>
		<string>com.apple.notificationcenterui.customalerts</string>
		<string>com.apple.notificationcenterui.siri</string>
		<string>com.apple.remindd</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.siri.running</string>
		<string>com.apple.siri.startup</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.siriinferenced</string>
		<string>com.apple.siriinferenced.remembers</string>
		<string>com.apple.sirisuggestions</string>
		<string>com.apple.soagent</string>
		<string>com.apple.speech.speechdatainstallerd</string>
		<string>com.apple.speech.speechdatainstallerd.isavailable</string>
		<string>com.apple.systemprofiler</string>
		<string>com.apple.VoiceOver.running</string>
		<string>com.apple.VoiceOver.startup</string>
		<string>com.apple.wirelessproxd</string>
		<string>com.apple.server.bluetooth.classic.xpc</string>
		<string>com.apple.siri.UnifiedSiriTest.TestingEventService</string>
		<string>com.apple.icloud.searchparty.locationfetch.items</string>
		<string>com.apple.icloud.searchpartyd.securelocations</string>
		<string>com.apple.notificationcenterui.snippet</string>
		<string>com.apple.callkit.callcontrollerhost</string>
		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
		<string>com.apple.siri.audiopowerupdate.xpc</string>
		<string>com.apple.FileDerivativeService</string>
		<string>com.apple.mediaanalysisd.embeddingstore</string>
		<string>com.apple.duetexpertd.assistant-actions</string>
		<string>com.apple.ScreenTimeSettingsAgent.private</string>
		<string>com.apple.ManagedSettingsAgent</string>
		<string>com.apple.ManagedSettingsAgent.publisher</string>
	</array>
	<key>com.apple.security.temporary-exception.sbpl</key>
	<array>
		<string>(allow iokit-open (iokit-user-client-class "AppleKeyStoreUserClient"))</string>
		<string>(allow hid-control)</string>
		<string>(allow iokit-set-properties (iokit-property "HIDClickSpace") (iokit-property "HIDClickTime") (iokit-property "HIDKeyRepeat") (iokit-property "HIDMouseAcceleration") (iokit-property "HIDMouseKeysOn") (iokit-property "HIDScrollZoomModifierMask") (iokit-property "HIDSlowKeysDelay") (iokit-property "HIDStickyKeysOn") (iokit-property "HIDTrackpadAcceleration"))</string>
		<string>(allow iokit-set-properties (iokit-property "FanMode") (iokit-property "RequestToken"))</string>
		<string>(read-write-and-issue-extensions (regex (string-append "^/Volumes/" (uuid-regex-string) "(/|$)")))</string>
		<string>(allow distributed-notification-post)</string>
		<string>(allow mach-register (global-name "com.apple.Siri.running"))</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.assistant.logging</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.token</string>
		<string>com.apple.Notes</string>
		<string>com.apple.speech.recognition.AppleSpeechRecognition.prefs</string>
		<string>com.apple.voicetrigger</string>
		<string>com.apple.ironwood.support</string>
		<string>com.apple.siri.internal</string>
		<string>com.apple.generativesearch</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.generativeassistantsettings</string>
		<string>com.apple.generativepartnerservicesettings</string>
		<string>com.apple.assistant</string>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.CoreGraphics</string>
		<string>com.apple.universalaccess</string>
		<string>com.apple.Siri</string>
		<string>com.apple.speakerrecognition</string>
		<string>com.apple.speech.recognition.AppleSpeechRecognition.prefs</string>
		<string>com.apple.SiriNCService</string>
		<string>com.apple.Siri.SiriTodayExtension</string>
		<string>com.apple.voicetrigger</string>
		<string>com.apple.symbolichotkeys</string>
	</array>
	<key>com.apple.sharesheet.allow-custom-view</key>
	<true/>
	<key>com.apple.shortcuts.background-running</key>
	<true/>
	<key>com.apple.shortcuts.stepwise-execution</key>
	<true/>
	<key>com.apple.shortcuts.variable-injection</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
	<key>com.apple.siri.activation.service</key>
	<true/>
	<key>com.apple.siri.inference.EntityMatcher.admin</key>
	<true/>
	<key>com.apple.siri.orchestration.prescribedaction</key>
	<true/>
	<key>com.apple.sirisuggestions.allow</key>
	<true/>
	<key>com.apple.spotlight.entitledattributes</key>
	<true/>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>access-call-providers</string>
	</array>
	<key>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</key>
	<true/>
	<key>com.apple.toolkit.request-reindex.allow</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>332</string>
		<string>333</string>
		<string>334</string>
		<string>335</string>
		<string>336</string>
		<string>337</string>
		<string>409</string>
		<string>753</string>
		<string>755</string>
	</array>
	<key>com.apple.usermanagerd.persona.fetch</key>
	<true/>
	<key>com.apple.usermanagerd.persona.observer</key>
	<true/>
	<key>com.apple.watchlist.private</key>
	<true/>
	<key>com.apple.wifi.events</key>
	<true/>
	<key>com.apple.wifi.set_power</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.Spotlight</string>
		<string>apple</string>
		<string>com.apple.openai</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### System Settings

> `/System/Applications/System Settings.app/Contents/MacOS/System Settings`

```diff

 	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.agentSessionStore</key>
+	<true/>
 	<key>com.apple.linkd.registry</key>
 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>

```
### Migration Assistant

> `/System/Applications/Utilities/Migration Assistant.app/Contents/MacOS/Migration Assistant`

```diff

 <dict>
 	<key>com.apple.private.mbsystemadministration</key>
 	<true/>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.skylight.plugin-power</key>
 	<true/>
 </dict>

```
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/Contents/MacOS/AccessibilityUIServer`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.Feedback.DraftingExtension.viewservice</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.photos.service</string>

```
### ClockAngel

> `/System/Library/CoreServices/ClockAngel.app/Contents/MacOS/ClockAngel`

```diff

 	<array>
 		<string>com.apple.sessionservices</string>
 	</array>
+	<key>com.apple.springboard.sceneaccessory.highlight</key>
+	<true/>
 </dict>
 </plist>
 

```
### ControlCenter

> `/System/Library/CoreServices/ControlCenter.app/Contents/MacOS/ControlCenter`

```diff

 	<true/>
 	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>
 	<true/>
+	<key>com.apple.private.systemstats.analysis-client</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>

```
### FamilyOutOfProcessUIExtension

> `/System/Library/CoreServices/FamilyExtensionHost.app/Contents/Extensions/FamilyOutOfProcessUIExtension.appex/Contents/MacOS/FamilyOutOfProcessUIExtension`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.familycircled</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### FamilyExtensionHost

> `/System/Library/CoreServices/FamilyExtensionHost.app/Contents/MacOS/FamilyExtensionHost`

```diff

 	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
+	<key>com.apple.private.ageRange</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/Contents/MacOS/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.runningboard.trustedtarget</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.servicesintelligenced</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/CallHistoryDB/</string>

```
### PeopleMessageService

> `/System/Library/CoreServices/PeopleMessageService.app/Contents/MacOS/PeopleMessageService`

```diff

 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### PeopleMessagesAskToBuy

> `/System/Library/CoreServices/PeopleMessageService.app/Contents/PlugIns/PeopleMessagesAskToBuy.appex/Contents/MacOS/PeopleMessagesAskToBuy`

```diff

 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.contactsd.persistence</string>
 		<string>com.apple.AddressBook.ContactsAccountsService</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### PeopleMessagesScreenTime

> `/System/Library/CoreServices/PeopleMessageService.app/Contents/PlugIns/PeopleMessagesScreenTime.appex/Contents/MacOS/PeopleMessagesScreenTime`

```diff

 		<string>com.apple.AddressBook.ContactsAccountsService</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.servicesanalytics.xpc</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### SSFileCopyReceiver

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/Support/SSFileCopyReceiver.bundle/Contents/MacOS/SSFileCopyReceiver`

```diff

             ]
           }
         }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.apple.RemoteDesktop",
+          "validation-category": 1
+        }
       }
     ]
   },

```
### SSFileCopySender

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/Support/SSFileCopySender.bundle/Contents/MacOS/SSFileCopySender`

```diff

             ]
           }
         }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.apple.RemoteDesktop",
+          "validation-category": 1
+        }
       }
     ]
   },

```
### ScreenTimeWidgetExtension

> `/System/Library/CoreServices/Screen Time.app/Contents/PlugIns/ScreenTimeWidgetExtension.appex/Contents/MacOS/ScreenTimeWidgetExtension`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```

### 🆕 SiriAppAccessMigrator

> `/System/Library/CoreServices/SiriAppAccessMigrator`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.tcc.manager.access.modify</key>
	<array>
		<string>kTCCServiceSiri</string>
	</array>
</dict>
</plist>

```
### softwareupdated

> `/System/Library/CoreServices/Software Update.app/Contents/Resources/softwareupdated`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
-	<key>com.apple.private.intelligenceplatform.client-identifier</key>
-	<string>com.apple.softwareupdated</string>
-	<key>com.apple.private.intelligenceplatform.use-cases</key>
-	<dict>
-		<key>AppleIntelligenceReporting.AssetDelivery</key>
-		<dict>
-			<key>Streams</key>
-			<dict>
-				<key>AppleIntelligence.Reporting.AssetDeliveryLog.SoftwareUpdateController</key>
-				<dict>
-					<key>mode</key>
-					<string>read-write</string>
-				</dict>
-			</dict>
-		</dict>
-	</dict>
 	<key>com.apple.private.iokit.assertion-softwareupdate</key>
 	<true/>
 	<key>com.apple.private.iokit.assertonlidclose</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.sucore.SUCoreHelperService</string>
-		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.temporary-exception.apple-events</key>
 	<array>

```
### SpotlightPreferenceExtension

> `/System/Library/CoreServices/Spotlight.app/Contents/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
-		<string>kTCCServiceSiriAccess</string>
+		<string>kTCCServiceSiri</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### Spotlight

> `/System/Library/CoreServices/Spotlight.app/Contents/MacOS/Spotlight`

```diff

 	</array>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
-	<key>com.apple.private.security.storage.MessagesMetaData </key>
+	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.tcc.events.subscriber</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
-		<string>kTCCServiceSiriAccess</string>
+		<string>kTCCServiceSiri</string>
 	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>

```
### backupd-helper

> `/System/Library/CoreServices/TimeMachine/backupd-helper`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.vfs.snapshot</key>
+	<true/>
 	<key>com.apple.private.security.storage.TimeMachine</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### PhotosUserAccountUpdaterTool

> `/System/Library/CoreServices/UAUPlugins/PhotosUserAccountUpdaterPlugin.bundle/Contents/MacOS/PhotosUserAccountUpdaterTool`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.MobileContainerManager.lookup</key>
+	<dict>
+		<key>appData</key>
+		<array>
+			<string>com.apple.photolibraryd</string>
+		</array>
+	</dict>
 	<key>com.apple.private.photos.allowlibraryupgrade</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.photolibraryd.private</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.photolibraryd.private</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Containers/com.apple.photolibraryd/Data/Library/Preferences/</string>
+	</array>
 </dict>
 </plist>
 

```
### WindowManager

> `/System/Library/CoreServices/WindowManager.app/Contents/MacOS/WindowManager`

```diff

 	</array>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
+	<key>com.apple.private.screencapturekit.suppress-screen-indicator</key>
+	<true/>
 	<key>com.apple.private.skylight.capturegroupmodifier</key>
 	<true/>
 	<key>com.apple.private.skylight.windowmanager</key>

```
### iCloud

> `/System/Library/CoreServices/iCloud.app/Contents/MacOS/iCloud`

```diff

 	<string>serverPreferred</string>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.icloud-extended-share-access</key>
+	<array>
+		<string>InProcessShareAccessRequests</string>
+	</array>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

```
### mapspushd

> `/System/Library/CoreServices/mapspushd`

```diff

 	<true/>
 	<key>com.apple.maps.virtualgarage.vehicles</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.navigation.spi</key>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>
+		<string>com.apple.Maps.mapspushd</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### screencaptureui

> `/System/Library/CoreServices/screencaptureui.app/Contents/MacOS/screencaptureui`

```diff

 	<array>
 		<string>TestFlightFeedback</string>
 	</array>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>Screenshots</key>

 		<string>com.apple.CalendarAgent</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.generativeexperiences.agentMediaStore</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.Feedback.DraftingExtension.viewservice</string>
 	</array>
 	<key>com.apple.visualintelligence.private.visual-action-prediction</key>
 	<true/>

```
### AboutExtension

> `/System/Library/ExtensionKit/Extensions/AboutExtension.appex/Contents/MacOS/AboutExtension`

```diff

 	<array>
 		<string>group.com.apple.corerepair</string>
 	</array>
+	<key>com.apple.private.sessionagent.spi</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### AppleIDSettings

> `/System/Library/ExtensionKit/Extensions/AppleIDSettings.appex/Contents/MacOS/AppleIDSettings`

```diff

 	</array>
 	<key>com.apple.family.ageRange</key>
 	<true/>
+	<key>com.apple.generativeexperiences.agentSessionStore</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.findmydevice-user-agent.access</key>

 		<string>com.apple.dnssd.service</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.generativeexperiences.agentSessionStore</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
 		<string>com.apple.icloud.findmydeviced</string>

```
### AskPermissionAskToResponseExtension

> `/System/Library/ExtensionKit/Extensions/AskPermissionAskToResponseExtension.appex/Contents/MacOS/AskPermissionAskToResponseExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.xpc.amsengagementd</string>
-		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.storekit.client-override</key>
 	<true/>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/Contents/MacOS/AssetMetricsExtension`

```diff

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
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.feedbacklogger/</string>

```
### DoNotDisturbAppIntents

> `/System/Library/ExtensionKit/Extensions/DoNotDisturbAppIntents.appex/Contents/MacOS/DoNotDisturbAppIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
+	<string>com.apple.Settings</string>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<array>
 		<string>com.apple.donotdisturb.DoNotDisturbAppIntents</string>

```
### FamilyOutOfProcessUIExtension

> `/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/Contents/MacOS/FamilyOutOfProcessUIExtension`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.familycircled</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### FamilySettings

> `/System/Library/ExtensionKit/Extensions/FamilySettings.appex/Contents/MacOS/FamilySettings`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/Contents/MacOS/FedAutoEvalPlugin`

```diff

 		<string>GenerativeExperiences.PromptTags</string>
 		<string>GenerativeExperiences.WritingToolsFeatures.Requests</string>
 		<string>GenerativeExperiences.WritingToolsFeatures.Metadata</string>
+		<string>Siri.SELFProcessedEvent</string>
+		<string>IntelligenceFlow.Transcript.Datastream</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### FedStatsPluginDynamic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginDynamic.appex/Contents/MacOS/FedStatsPluginDynamic`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>Call-Context-Cards</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>CommApps.CallIntelligence.CallContextCardsFedStats</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Camera-Auto-Focus</key>
 		<dict>
 			<key>Streams</key>

```
### FedStatsPluginStatic

> `/System/Library/ExtensionKit/Extensions/FedStatsPluginStatic.appex/Contents/MacOS/FedStatsPluginStatic`

```diff

 				</dict>
 			</dict>
 		</dict>
+		<key>Call-Context-Cards</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>CommApps.CallIntelligence.CallContextCardsFedStats</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>Camera-Auto-Focus</key>
 		<dict>
 			<key>Streams</key>

```
### MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/Contents/MacOS/MapsIntents`

```diff

 	<string>com.apple.Maps</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.Maps.MapsSync.store</string>
+		<string>com.apple.Maps.MapsSync.service</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 SafariSearchUploadWorker

> `/System/Library/ExtensionKit/Extensions/SafariSearchUploadWorker.appex/Contents/MacOS/SafariSearchUploadWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1821501079</string>
	<key>application-identifier</key>
	<string>com.apple.unilog.SafariSearchUploadWorker</string>
	<key>com.apple.developer.networking.multipath_extended</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Unilog.SafariSearch.Aggregation</string>
	</array>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.unilog.datacollector.SafariSearchUploadWorker</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>UnilogSafariSearchAggregation</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.SafariSearch.Aggregation</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.aiml.unilog.healthTelemetry</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.HealthAggregatedSummary</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Unilog.HealthTelemetry</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.SafariSearchUploadWorker</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SafariSearchUploadWorker</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SafariSearchUploadWorker</string>
	</array>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.siri.osprey</string>
	</array>
</dict>
</plist>

```
### ScreenTimePreferencesExtension

> `/System/Library/ExtensionKit/Extensions/ScreenTimePreferencesExtension.appex/Contents/MacOS/ScreenTimePreferencesExtension`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### SiriAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/SiriAutoEvalPlugin.appex/Contents/MacOS/SiriAutoEvalPlugin`

```diff

 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeExperiences.PromptTags</string>
 		<string>Siri.SELFProcessedEvent</string>
+		<string>IntelligenceFlow.Transcript.Datastream</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### SpotlightPreferenceExtension

> `/System/Library/ExtensionKit/Extensions/SpotlightPreferenceExtension.appex/Contents/MacOS/SpotlightPreferenceExtension`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
-		<string>kTCCServiceSiriAccess</string>
+		<string>kTCCServiceSiri</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

```
### WallpaperAerialsExtension

> `/System/Library/ExtensionKit/Extensions/WallpaperAerialsExtension.appex/Contents/MacOS/WallpaperAerialsExtension`

```diff

 	<true/>
 	<key>com.apple.security.personal-information.location</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/System/Library/Wallpapers/.default/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/System/Library/Desktop Pictures/</string>

```

### 🆕 WritingToolsAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/WritingToolsAppIntentsExtension.appex/Contents/MacOS/WritingToolsAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.WritingTools.WritingToolsAppIntentsExtension</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.WritingTools.WritingToolsAppIntentsExtension</string>
	<key>com.apple.feedbackd.remote-evaluation</key>
	<true/>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.generativeexperiences.textcomposition</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.appintents.extend-timeout-on-progress-updates</key>
	<true/>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.sage.textcomposition</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.sage.textcomposition</string>
		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.generativeexperiences.summarization</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.generativeassistantsettings</string>
		<string>com.apple.generativepartnerservicesettings</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.generativeexperiences.textcomposition</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.extensionkitservice</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.gms.availability</string>
	</array>
	<key>com.apple.shortcuts.stepwise-execution</key>
	<true/>
	<key>com.apple.shortcuts.variable-injection</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
</dict>
</plist>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Support/accountsd`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

```
### SpeechSynthesisServerXPC

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/SpeechSynthesis.framework/Versions/A/XPCServices/SpeechSynthesisServerXPC.xpc/Contents/MacOS/SpeechSynthesisServerXPC`

```diff

 <dict>
 	<key>Ubiquity Container Identifiers</key>
 	<string></string>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### SpeechSynthesisServerXPC

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/Current/Frameworks/SpeechSynthesis.framework/Versions/A/XPCServices/SpeechSynthesisServerXPC.xpc/Contents/MacOS/SpeechSynthesisServerXPC`

```diff

 <dict>
 	<key>Ubiquity Container Identifiers</key>
 	<string></string>
+	<key>com.apple.private.accessibility.visuals</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/Versions/A/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fpsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 	<key>com.apple.siri.external_request</key>
 	<true/>
 	<key>com.apple.smoot.subscriptionservice</key>

```
### RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/Versions/Current/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fpsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 	<key>com.apple.siri.external_request</key>
 	<true/>
 	<key>com.apple.smoot.subscriptionservice</key>

```

### 🆕 PhotosViewService

> `/System/Library/Frameworks/PhotosUI.framework/Versions/A/XPCServices/PhotosViewService.xpc/Contents/MacOS/PhotosViewService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PhotosViewService</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.cloudphotod.access</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.photos.allowassetexpunge</key>
	<true/>
	<key>com.apple.private.photos.allowcollectionshare</key>
	<true/>
	<key>com.apple.private.photos.restrictedresources.read</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.photos.ImageConversionService</string>
		<string>com.apple.cloudphotod</string>
		<string>com.apple.photos.service</string>
	</array>
	<key>com.apple.security.files.bookmarks.app-scope</key>
	<true/>
	<key>com.apple.security.files.bookmarks.document-scope</key>
	<true/>
</dict>
</plist>

```
### TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/TrustedPeersHelper.xpc/Contents/MacOS/TrustedPeersHelper`

```diff

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.Keychains</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```
### TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/Versions/Current/XPCServices/TrustedPeersHelper.xpc/Contents/MacOS/TrustedPeersHelper`

```diff

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.Keychains</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```

### 🆕 SpeechEncryptedLogsDiagnostic

> `/System/Library/Frameworks/Speech.framework/PlugIns/SpeechEncryptedLogsDiagnostic.appex/Contents/MacOS/SpeechEncryptedLogsDiagnostic`

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

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.speech.localspeechrecognition</string>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.EmbeddedSpeech</string>

 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingAsrHammer</string>
 		<string>com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Assistant/SpeechMaintenance/</string>
+	</array>
 	<key>com.apple.siri.analytics.assistant</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/Versions/Current/XPCServices/localspeechrecognition.xpc/Contents/MacOS/localspeechrecognition`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.speech.localspeechrecognition</string>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.EmbeddedSpeech</string>

 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingAsrHammer</string>
 		<string>com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>

 	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Assistant/SpeechMaintenance/</string>
+	</array>
 	<key>com.apple.siri.analytics.assistant</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### DeviceActivityReportService

> `/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/A/PlugIns/DeviceActivityReportService.appex/Contents/MacOS/DeviceActivityReportService`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### DeviceActivityReportService

> `/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/Current/PlugIns/DeviceActivityReportService.appex/Contents/MacOS/DeviceActivityReportService`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### CharacterPalette

> `/System/Library/Input Methods/CharacterPalette.app/Contents/MacOS/CharacterPalette`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceCamera</string>
 		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.rootless.datavault.controller.internal</key>

 		<string>com.apple.stickersd.group</string>
 		<string>group.com.apple.SuggestedImage.SharedSecureContainer</string>
 	</array>
+	<key>com.apple.security.device.camera</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>

```

### 🆕 binary.metallib

> `/System/Library/PrivateFrameworks/AgentCanvasUICore.framework/Versions/A/Resources/binary.metallib`

- No entitlements *(yet)*

### 🆕 binary.metallib

> `/System/Library/PrivateFrameworks/AgentCanvasUICore.framework/Versions/Current/Resources/binary.metallib`

- No entitlements *(yet)*
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/Resources/amsaccountsd`

```diff

 	</array>
 	<key>com.apple.companion-authentication.store-purchase</key>
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
 	<key>com.apple.developer.networking.wifi-info</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppleMediaServices</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.coreidvd.digital-presentment.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/Current/Resources/amsaccountsd`

```diff

 	</array>
 	<key>com.apple.companion-authentication.store-purchase</key>
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
 	<key>com.apple.developer.networking.wifi-info</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppleMediaServices</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.coreidvd.digital-presentment.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```

### 🆕 ANELargeModelCompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANELargeModelCompilerService.xpc/Contents/MacOS/ANELargeModelCompilerService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.private.coreml.decypt_allowed</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.rootless.storage.ane_model_cache</key>
	<true/>
	<key>com.apple.rootless.storage.triald</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>ANECompilerService</string>
	</array>
</dict>
</plist>

```
### AskPermissionUI

> `/System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/Resources/AskPermissionUI.app/Contents/MacOS/AskPermissionUI`

```diff

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<key>com.apple.security.network.client</key>
+	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.askpermissiond</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
+		<string>com.apple.askpermissiond</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fpsd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>
 	</array>
-	<key>com.apple.security.network.client</key>
-	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Versions/A/Resources/askpermissiond`

```diff

 	<array>
 		<string>com.apple.askpermission.notifications</string>
 	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.usernotifications.usernotificationservice</string>
-		<string>com.apple.biome.PublicStreamAccessService</string>
+		<string>com.apple.asktod</string>
 		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.PublicStreamAccessService</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplayd</string>
 		<string>com.apple.familycircle.agent</string>
-		<string>com.apple.asktod</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.usernotifications.usernotificationservice</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>

```
### AskPermissionUI

> `/System/Library/PrivateFrameworks/AskPermission.framework/Versions/Current/Resources/AskPermissionUI.app/Contents/MacOS/AskPermissionUI`

```diff

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<key>com.apple.security.network.client</key>
+	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.askpermissiond</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>
+		<string>com.apple.askpermissiond</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fpsd</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>
 	</array>
-	<key>com.apple.security.network.client</key>
-	<true/>
 	<key>com.apple.symptom_analytics.query</key>
 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>

```
### askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Versions/Current/Resources/askpermissiond`

```diff

 	<array>
 		<string>com.apple.askpermission.notifications</string>
 	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.usernotifications.usernotificationservice</string>
-		<string>com.apple.biome.PublicStreamAccessService</string>
+		<string>com.apple.asktod</string>
 		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.PublicStreamAccessService</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplayd</string>
 		<string>com.apple.familycircle.agent</string>
-		<string>com.apple.asktod</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.usernotifications.usernotificationservice</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistant_service`

```diff

 	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>

 	</array>
 	<key>com.apple.developer.networking.multipath_extended</key>
 	<true/>
+	<key>com.apple.eligibilityd</key>
+	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.assistant.backedup</string>
-		<string>com.apple.ironwood.support</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<array>

```
### cksharingmanagementd

> `/System/Library/PrivateFrameworks/CKSharingManagementDaemon.framework/Support/cksharingmanagementd`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations</key>
 	<true/>
-	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
-	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.ts.daemon-container</key>

```
### RemoteGenerationViewService

> `/System/Library/PrivateFrameworks/CharacterPicker.framework/Versions/A/XPCServices/RemoteGenerationViewService.xpc/Contents/MacOS/RemoteGenerationViewService`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceCamera</string>
 		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.rootless.datavault.controller.internal</key>

 	<array>
 		<string>group.com.apple.GenerativePlayground</string>
 	</array>
+	<key>com.apple.security.device.camera</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/System/Library/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

```
### RemoteGenerationViewService

> `/System/Library/PrivateFrameworks/CharacterPicker.framework/Versions/Current/XPCServices/RemoteGenerationViewService.xpc/Contents/MacOS/RemoteGenerationViewService`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceCamera</string>
 		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.rootless.datavault.controller.internal</key>

 	<array>
 		<string>group.com.apple.GenerativePlayground</string>
 	</array>
+	<key>com.apple.security.device.camera</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/System/Library/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<array>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 		<string>/Library/UserFonts/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>

```
### cloudd

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd`

```diff

 	<string>com.apple.cloudd</string>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.utility</key>
 	<true/>
 	<key>com.apple.cdp.walrus</key>

```
### SpeechProfileDiagnostic

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/PlugIns/SpeechProfileDiagnostic.appex/Contents/MacOS/SpeechProfileDiagnostic`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/SiriVocabulary/</string>
+		<string>/Library/Assistant/SpeechMaintenance/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### speechmaintenanced

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/speechmaintenanced`

```diff

 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrAssistant</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 				</dict>
 			</dict>
 		</dict>
+		<key>ASRNCBVQProfileGeneration</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.IntentVocabulary.CustomContactGroupName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomContactName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Contacts.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

 		<string>appEntityRelevanceRanking</string>
 		<string>visualIdentifier</string>
 	</array>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/</string>

 	<array>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.assistant.settings</string>
+		<string>com.apple.modelcatalog.catalog</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<array>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/Support/suggestd`

```diff

 				<string>TextUnderstanding.Output.Topic</string>
 			</array>
 		</dict>
+		<key>com.apple.proactive.suggestions.SocialHighlights</key>
+		<dict>
+			<key>Views</key>
+			<array>
+				<string>siriRemembers</string>
+			</array>
+		</dict>
 		<key>com.apple.suggestions.TextUnderstandingObserver</key>
 		<dict>
 			<key>Streams</key>

```
### CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

```diff

 		<string>com.apple.preferred.network</string>
 		<string>com.apple.frozen.network</string>
 		<string>apple</string>
+		<string>com.apple.thread.datasetmacos</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

 	</array>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
+	<key>com.apple.developer.networking.manage-thread-network-credentials</key>
+	<true/>
 	<key>com.apple.developer.networking.multicast</key>
 	<true/>
 	<key>com.apple.iokit.powerdxpc</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>wpantund</string>
+	<key>com.apple.private.threadnetwork</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	<array>
 		<string>com.apple.thread.network</string>
 		<string>com.apple.thread.dataset</string>
+		<string>com.apple.thread.datasetmacos</string>
 		<string>com.apple.preferred.network</string>
 		<string>com.apple.frozen.network</string>
 		<string>apple</string>

```
### ScreenTimeDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ScreenTimeDiagnosticExtension.appex/Contents/MacOS/ScreenTimeDiagnosticExtension`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/Versions/A/XPCServices/FilesystemMetadataSnapshotService.xpc/Contents/MacOS/FilesystemMetadataSnapshotService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.apfs.get-graft-info</key>
+	<true/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
 </dict>

```
### FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/Versions/Current/XPCServices/FilesystemMetadataSnapshotService.xpc/Contents/MacOS/FilesystemMetadataSnapshotService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.apfs.get-graft-info</key>
+	<true/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
 </dict>

```
### donotdisturbd

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/Support/donotdisturbd`

```diff

 	<array>
 		<string>/Library/Fonts/AddedFontCache.plist</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```

### 🆕 FindMySecureEnvironmentXPCService

> `/System/Library/PrivateFrameworks/FindMySecureEnvironment.framework/XPCServices/FindMySecureEnvironmentXPCService.xpc/Contents/MacOS/FindMySecureEnvironmentXPCService`

- No entitlements *(yet)*
### GameOverlayViewService

> `/System/Library/PrivateFrameworks/GameCenterUICore.framework/XPCServices/GameOverlayViewService.xpc/Contents/MacOS/GameOverlayViewService`

```diff

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>com.apple.MessagesLegacyTransferArchive</string>
+		<string>group.com.apple.servicesintelligenced</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
+	<key>com.apple.mediasetupd.client</key>
+	<true/>
 	<key>com.apple.mobilemail.mailservices</key>
 	<true/>
 	<key>com.apple.modelcatalog.full-access</key>

 	<true/>
 	<key>com.apple.private.screencapturekit.noprompt</key>
 	<true/>
+	<key>com.apple.private.searchtoold.search</key>
+	<true/>
 	<key>com.apple.private.security.arkit</key>
 	<array>
 		<string>allowImmersiveExemption</string>

 		<string>kTCCServiceReminders</string>
 		<string>kTCCServiceSpeechRecognition</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceSiri</string>
+	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAll</string>

```
### intelligencetasksd

> `/System/Library/PrivateFrameworks/IntelligenceTasksEngine.framework/Support/intelligencetasksd`

```diff

 	<string>com.apple.intelligencetasksd</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.intelligencetasksd</string>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.intelligencetasksd</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/A/XPCServices/com.apple.photos.ImageConversionService.xpc/Contents/MacOS/com.apple.photos.ImageConversionService`

```diff

 	<array>
 		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
 	</array>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
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
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### com.apple.MobileAsset.DownloadService.Builtin

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/Versions/A/XPCServices/com.apple.MobileAsset.DownloadService.Builtin.xpc/Contents/MacOS/com.apple.MobileAsset.DownloadService.Builtin`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read</key>
+	<array>
+		<string>/Library/Preferences/com.apple.networkextension.uuidcache.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/run/MobileAssetCriticalDomainsUpdated.plist</string>

```
### com.apple.MobileAsset.DownloadService.Builtin

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/Versions/Current/XPCServices/com.apple.MobileAsset.DownloadService.Builtin.xpc/Contents/MacOS/com.apple.MobileAsset.DownloadService.Builtin`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read</key>
+	<array>
+		<string>/Library/Preferences/com.apple.networkextension.uuidcache.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/run/MobileAssetCriticalDomainsUpdated.plist</string>

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/Versions/A/searchtoold`

```diff

 	<true/>
 	<key>com.apple.diagnosticpipeline.request</key>
 	<true/>
+	<key>com.apple.filederivatives.derive</key>
+	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>loiEntityRelevanceRanking</string>
 		<string>standardFeatureView</string>
 	</array>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>

 	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
+	<key>com.apple.private.security.storage.SystemPolicyAllFiles</key>
+	<true/>
 	<key>com.apple.private.spotlight.parsec</key>
 	<true/>
 	<key>com.apple.private.spotlight.search.internal</key>

 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceReminder</string>
 		<string>kTCCServiceMediaLibrary</string>
+		<string>kTCCServiceFileProviderDomain</string>
+		<string>kTCCServiceSystemPolicyAllFiles</string>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 		<string>kTCCServiceSystemPolicyNetworkVolumes</string>
 	</array>

 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</key>
 	<true/>
+	<key>com.apple.rootless.storage.SystemPolicyAllFiles</key>
+	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.rootless.storage.shortcuts</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
-	<key>com.apple.security.app-sandbox</key>
-	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.siri.referenceResolution</string>

 		<string>com.apple.SpotlightResources.Defaults</string>
 		<string>com.apple.siri.morphun</string>
 		<string>com.apple.generativesearch</string>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>platform-application</key>
 	<true/>
+	<key>seatbelt-profiles</key>
+	<array>
+		<string>com.apple.omniSearch.searchtoold</string>
+	</array>
 </dict>
 </plist>
 

```
### amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```diff

 	</array>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.amsondevicestoraged</string>

```
### peopled

> `/System/Library/PrivateFrameworks/People.framework/peopled`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.peopled</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<array>
 		<string>group.com.apple.people</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/CallHistoryDB/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/CallHistoryDB/</string>

 		<string>com.apple.icloud.searchpartyd.securelocations</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.CallHistorySyncHelper</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.PerformanceTrace.PerformanceTraceService

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/Versions/A/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/Contents/MacOS/com.apple.PerformanceTrace.PerformanceTraceService`

```diff

 	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.private.swiftuitracingsupport.record</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.PerformanceTrace.notifications</string>

```
### com.apple.PerformanceTrace.PerformanceTraceService

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/Versions/Current/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/Contents/MacOS/com.apple.PerformanceTrace.PerformanceTraceService`

```diff

 	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.private.swiftuitracingsupport.record</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.PerformanceTrace.notifications</string>

```
### photolibraryd

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd`

```diff

 	<true/>
 	<key>com.apple.private.icloud-account-access</key>
 	<true/>
+	<key>com.apple.private.imcore.imdpersistence.database-access</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.photolibraryd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

```
### com.apple.photos.PCCService

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/A/XPCServices/com.apple.photos.PCCService.xpc/Contents/MacOS/com.apple.photos.PCCService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.photos.PCCService</string>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

```
### com.apple.photos.PCCService

> `/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/Versions/Current/XPCServices/com.apple.photos.PCCService.xpc/Contents/MacOS/com.apple.photos.PCCService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.photos.PCCService</string>
+	<key>com.apple.private.photos.restrictedresources.read</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

```
### RemoteManagementAgent

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagementAgent`

```diff

 	<true/>
 	<key>com.apple.private.rsr-cryptex-access</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>

```
### remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

 	<true/>
 	<key>com.apple.private.rsr-cryptex-access</key>
 	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>

```
### rmdinspect

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/rmdinspect`

```diff

 <dict>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.rmdinspect</string>
+	<key>com.apple.private.MobileContainerManager.lookup</key>
+	<dict>
+		<key>protectedSystem</key>
+		<array>
+			<string>com.apple.RemoteManagementAgent</string>
+		</array>
+	</dict>
 	<key>com.apple.private.remotemanagement</key>
 	<true/>
+	<key>com.apple.private.security.no-container</key>
+	<true/>
+	<key>com.apple.private.security.protected-system-container</key>
+	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/containers/Data/ProtectedSystem/</string>
+		<string>/private/var/db/rmd/</string>
+	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.containermanagerd.system</string>
+		<string>com.apple.remotemanagementd</string>
+		<string>com.apple.RemoteManagementAgent</string>
+	</array>
 </dict>
 </plist>
 

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent`

```diff

 	<array>
 		<string>App.InFocus</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/Versions/A/ScreenTimeSettingsAgent`

```diff

 	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
-		<string>App.MediaUsage</string>
-		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>App.MediaUsage</string>
+		<string>App.WebUsage</string>
 		<string>Family.ScreenTime.ChildState</string>
 	</array>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

```
### siriappintentsd

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/siriappintentsd`

```diff

 		<string>AppleIntelligence.Reporting.Invocation.Step</string>
 		<string>SessionResumptionEventBundle</string>
 		<string>SecurityValidationEvent</string>
+		<string>TokenGeneration.Inference.Requests</string>
 	</array>
 	<key>com.apple.private.corespotlight.skgupdater</key>
 	<true/>

 				<string>AppleIntelligence.Reporting.Invocation.Step</string>
 			</array>
 		</dict>
+		<key>SiriHeliosTokenGenerationReplay</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>TokenGeneration.Inference.Requests</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.logging.admin</key>
 	<true/>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriTextToSpeech</string>
-		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 	<array>
 		<string>group.com.apple.SiriTTS</string>
 	</array>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### WindowServer

> `/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer`

```diff

 			<dict/>
 		</dict>
 	</dict>
+	<key>com.apple.aop.user-client</key>
+	<dict>
+		<key>las</key>
+		<dict>
+			<key>get-property</key>
+			<dict/>
+			<key>perform-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.appledfr.client</key>
 	<true/>
 	<key>com.apple.bluetooth.internal</key>

 	<true/>
 	<key>com.apple.iohideventsystem.server</key>
 	<true/>
+	<key>com.apple.keystore.fdr-access</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.private.AmbientDisplay.messaging</key>
 	<true/>
+	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
+	<true/>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

 	<array>
 		<string>AppleHIDTransportBootloaderUserClient</string>
 		<string>AppleHIDTransportDeviceUserClient</string>
+		<string>AppleSPUUserClient</string>
 	</array>
 	<key>com.apple.systemstatus.domains</key>
 	<array>

```
### WindowServer

> `/System/Library/PrivateFrameworks/SkyLight.framework/Versions/Current/Resources/WindowServer`

```diff

 			<dict/>
 		</dict>
 	</dict>
+	<key>com.apple.aop.user-client</key>
+	<dict>
+		<key>las</key>
+		<dict>
+			<key>get-property</key>
+			<dict/>
+			<key>perform-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.appledfr.client</key>
 	<true/>
 	<key>com.apple.bluetooth.internal</key>

 	<true/>
 	<key>com.apple.iohideventsystem.server</key>
 	<true/>
+	<key>com.apple.keystore.fdr-access</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.private.AmbientDisplay.messaging</key>
 	<true/>
+	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
+	<true/>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>

 	<array>
 		<string>AppleHIDTransportBootloaderUserClient</string>
 		<string>AppleHIDTransportDeviceUserClient</string>
+		<string>AppleSPUUserClient</string>
 	</array>
 	<key>com.apple.systemstatus.domains</key>
 	<array>

```
### stickersd

> `/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
-		<string>com.apple.EmojiPreferences</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.EmojiPreferences</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager</key>
 	<true/>
+	<key>com.apple.private.tcc.system-tccd-forwarder</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.tccd</string>

```

### 🆕 UARPAssetManagerServiceiCloud

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/XPCServices/UARPAssetManagerServiceiCloud.xpc/Contents/MacOS/UARPAssetManagerServiceiCloud`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.MobileAccessoryUpdater.fudHelperAgent</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>cellular-plan</string>
		<string>public-cellular-plan</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>InverseDeviceID</string>
	</array>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.systemLaunchDaemonAccess</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/db/accessoryupdater/</string>
		<string>/private/var/run/</string>
		<string>/private/var/root/Library/Caches/</string>
		<string>/private/var/root/Library/HTTPStorages/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.commcenter.coretelephony.xpc</string>
		<string>com.apple.frontboard.systemappservices</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.ACMobileShim</string>
		<string>com.apple.AUDeveloperSettings</string>
		<string>com.apple.GEO</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.accessoryupdaterd</string>
		<string>com.apple.AUDeveloperSettings</string>
		<string>com.apple.security</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.asset-access</key>
	<true/>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>iCloud Services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTrackingAgent`

```diff

 	<array>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

 			<array>
 				<string>App.MediaUsage</string>
 				<string>App.WebUsage</string>
+				<string>Intelligence.Usage</string>
 				<string>Media.NowPlaying</string>
 				<string>ScreenTime.AppUsage</string>
 			</array>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
+	<key>com.apple.private.notificationcenter.preferences</key>
+	<true/>
 	<key>com.apple.private.replicator.controller</key>
 	<true/>
 	<key>com.apple.private.replicator.dataProvider</key>

```
### visualintelligenced

> `/System/Library/PrivateFrameworks/VisualIntelligenceServices.framework/visualintelligenced`

```diff

 	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
+	<key>com.apple.aned.private.processModelShare.allow</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.visualintelligenced</string>
 	<key>com.apple.argos.availibility-bypass</key>

 	<string>com.apple.visualintelligenced</string>
 	<key>com.apple.private.payment.remote-network-payment-initiate</key>
 	<true/>
-	<key>com.apple.private.photos.service.librarymanagement</key>
-	<true/>
 	<key>com.apple.private.proactive.visual-action-prediction</key>
 	<true/>
 	<key>com.apple.private.safariviewcontroller.custom-network-attribution-capable</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Versions/A/Support/siriactionsd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siriactionsd</string>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.chrono.controls</key>
 	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>

 	<true/>
 	<key>com.apple.private.MobileContainerManager.deleteContainerContent</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appintents.update-app-shortcut-apps</key>

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.mode.assertion.user-requested.client-identifiers</key>

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.shortcuts</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>App.Intent</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>CarPlay.Connected</key>
 				<dict>
 					<key>mode</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>com.apple.shortcuts</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>Mail</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.BTServer.le</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.backlightd</string>
 		<string>com.apple.biome.access.system</string>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.modelmanager</string>
+		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.proactiveagentplatform.orchestrator</string>
 		<string>com.apple.shortcuts.view-service</string>
 		<string>com.apple.siri.uaf.service</string>

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.appleaccount</string>
+		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/Contents/MacOS/ShortcutsIntents`

```diff

 		<string>com.apple.sirittsd</string>
 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.spotlight.SearchAgent</string>
+		<string>com.apple.wallpaper.public</string>
 		<string>com.apple.windowmanager.external</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 	</array>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/Contents/MacOS/BackgroundShortcutRunner`

```diff

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.generativesearch.client.search</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.source.identities</key>

 	<true/>
 	<key>com.apple.private.ids.agent.GroupRestricted</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.shortcuts</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
 		<key>DataActionsUsecase</key>

 				<string>IntelligencePlatform.Entity</string>
 			</array>
 		</dict>
+		<key>ToolKit.Sync</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.Intents.IndexedEnum</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>ToolKit.Tool</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.shortcuts</key>
+		<dict>
+			<key>Search</key>
+			<array>
+				<string>Mail</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.assistant.cdm</string>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.chronoservices</string>

 		<string>com.apple.generativeexperiences.ExternalProviderTCCManagingXPC</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
+		<string>com.apple.generativesearch.server.search</string>
 		<string>com.apple.intelligenceflow.contextTool</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.intelligenceplatform.View</string>

 		<string>com.apple.sirittsd</string>
 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.spotlight.SearchAgent</string>
+		<string>com.apple.wallpaper.public</string>
 		<string>com.apple.webprivacyd</string>
 		<string>com.apple.windowmanager.external</string>
 	</array>

 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.TimeMachine</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>

```

### 🆕 MusicRecognitionUIPlugin

> `/System/Library/Snippets/UIPlugins/MusicRecognitionUIPlugin.bundle/Contents/MacOS/MusicRecognitionUIPlugin`

- No entitlements *(yet)*

### 🆕 com.apple.RemotePairing.AuditActivityNotifications

> `/System/Library/UserNotifications/Bundles/com.apple.RemotePairing.AuditActivityNotifications.bundle/Contents/MacOS/com.apple.RemotePairing.AuditActivityNotifications`

- No entitlements *(yet)*
### FamilyOutOfProcessUIExtension

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/Contents/MacOS/FamilyOutOfProcessUIExtension`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.familycircled</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

```
### ContactViewViewService

> `/System/iOSSupport/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactViewViewService.appex/Contents/MacOS/ContactViewViewService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### ContactsViewService

> `/System/iOSSupport/System/Library/Frameworks/ContactsUI.framework/PlugIns/ContactsViewService.appex/Contents/MacOS/ContactsViewService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileAddressBook</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

```
### RemotePlayerService

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fpsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 	<key>com.apple.siri.external_request</key>
 	<true/>
 	<key>com.apple.smoot.subscriptionservice</key>

```
### RemotePlayerService

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/Current/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fpsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+	</array>
 	<key>com.apple.siri.external_request</key>
 	<true/>
 	<key>com.apple.smoot.subscriptionservice</key>

```
### DeviceActivityReportService

> `/System/iOSSupport/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/A/PlugIns/DeviceActivityReportService.appex/Contents/MacOS/DeviceActivityReportService`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### DeviceActivityReportService

> `/System/iOSSupport/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Versions/Current/PlugIns/DeviceActivityReportService.appex/Contents/MacOS/DeviceActivityReportService`

```diff

 		<string>App.MediaUsage</string>
 		<string>App.WebUsage</string>
 		<string>Device.Display.Backlight</string>
+		<string>Intelligence.Usage</string>
 		<string>Media.NowPlaying</string>
 		<string>Notification.Usage</string>
 		<string>ScreenTime.AppUsage</string>

```
### voicememod

> `/System/iOSSupport/System/Library/PrivateFrameworks/VoiceMemos.framework/Support/voicememod`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.cloudkit.tccmanager</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### AddShortcutExtension

> `/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/Contents/MacOS/AddShortcutExtension`

```diff

 		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.siriactionsd.xpc</string>
+		<string>com.apple.wallpaper.public</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### CatalystContentExtension

> `/System/iOSSupport/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/CatalystContentExtension.appex/Contents/MacOS/CatalystContentExtension`

```diff

 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.powerui.smartChargeManager</string>
+		<string>com.apple.wallpaper.public</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### launchd

> `/sbin/launchd`

```diff

 	<true/>
 	<key>com.apple.private.delegate-signals</key>
 	<true/>
+	<key>com.apple.private.endpoint-security.submit.bootstrap</key>
+	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>
 	<true/>
 	<key>com.apple.private.kernel.darkboot</key>

```
### AirPlayXPCHelper

> `/usr/libexec/AirPlayXPCHelper`

```diff

 	<true/>
 	<key>com.apple.PairingManager.Write</key>
 	<true/>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.airplay.agent.services.allow</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

```
### ContinuityCaptureAgent

> `/usr/libexec/ContinuityCaptureAgent`

```diff

 	<true/>
 	<key>com.apple.networkd_privileged</key>
 	<true/>
+	<key>com.apple.networkrelay.devices.read</key>
+	<true/>
 	<key>com.apple.private.application-service-browse</key>
 	<true/>
 	<key>com.apple.private.cmio.extension.configuration</key>

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ak.auth.xpc</string>

```
### aned

> `/usr/libexec/aned`

```diff

 <dict>
 	<key>com.apple.ANECompilerService.allow</key>
 	<true/>
+	<key>com.apple.ANELargeModelCompilerService.allow</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.ane.iokit-user-access</key>

```
### aneuserd

> `/usr/libexec/aneuserd`

```diff

 <dict>
 	<key>com.apple.ANECompilerService.allow</key>
 	<true/>
+	<key>com.apple.ANELargeModelCompilerService.allow</key>
+	<true/>
 	<key>com.apple.ane.iokit-user-access</key>
 	<true/>
 	<key>com.apple.aneuserd.private.allow</key>

 	<true/>
 	<key>com.apple.rootless.storage.triald</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 		<string>com.apple.private.alloy.contextsync</string>
 		<string>com.apple.private.alloy.contextsync.local</string>
 	</array>
+	<key>com.apple.private.intelligencetasks.sets.maintenance.client</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.userprofiles</string>
-		<string>com.apple.cascade.Maintenance</string>
+		<string>com.apple.intelligencetasksd.sets.Maintenance</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### cameraispd

> `/usr/libexec/cameraispd`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>VADResourceArbiterUserClient</string>
 		<string>AppleCameraPhotonDetectorUserClient</string>
-		<string>IOUserClient</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### cameraispdarwinsimd

> `/usr/libexec/cameraispdarwinsimd`

```diff

 		<string>IOSurfaceRootUserClient</string>
 		<string>VADResourceArbiterUserClient</string>
 		<string>AppleCameraPhotonDetectorUserClient</string>
-		<string>IOUserClient</string>
 	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.systemstats.analysis-client</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCalendar</string>

```
### duetexpertd

> `/usr/libexec/duetexpertd`

```diff

 			<key>Search</key>
 			<array>
 				<string>SiriTranscript</string>
+				<string>SiriTranscriptConversation</string>
 			</array>
 			<key>Streams</key>
 			<array>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 	</dict>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.InputAnalytics.SecureContainer</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.openai</string>

```
### mdmclient

> `/usr/libexec/mdmclient`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>

```
### mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

 	<true/>
 	<key>com.apple.AppleNVMeSanitize.allow</key>
 	<true/>
+	<key>com.apple.afk.user</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.fdr-access</key>

 		<string>AppleEffaceableStorageUserClient</string>
 		<string>AppleAPFSUserClient</string>
 		<string>IOMobileFramebufferUserClient</string>
+		<string>AFKEndpointInterfaceUserClient</string>
 		<string>IOAVControllerConcreteUserClient</string>
 		<string>IOSurfaceRootUserClient</string>
 		<string>IOWatchdogUserClient</string>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read</key>
+	<array>
+		<string>/Library/Preferences/com.apple.networkextension.uuidcache.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/run/MobileAssetCriticalDomainsUpdated.plist</string>

```
### mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 		<string>com.apple.iokit.powerdxpc</string>
 		<string>com.apple.ctkd.token-client</string>
 		<string>com.apple.ctkd</string>
+		<string>com.apple.devicedatareset.DeviceDataResetService</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.wipedevice</key>
+	<true/>
 </dict>
 </plist>
 

```
### nexusd

> `/usr/libexec/nexusd`

```diff

 	<true/>
 	<key>com.apple.developer.networking.multicast</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

```
### powerexperienced

> `/usr/libexec/powerexperienced`

```diff

 	<true/>
 	<key>com.apple.osintelligence.charging</key>
 	<true/>
+	<key>com.apple.powerd.extendedbattery</key>
+	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
 	<key>com.apple.private.clpc.policy</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.OSIntelligence.battery</string>
+		<string>com.apple.powerd.extendedbattery</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Trial/</string>
+		<string>/Library/UserConfigurationProfiles/Truth.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 		<string>com.apple.security.octagon</string>
 		<string>com.apple.nearbyd.xpc.diagnostics</string>
 		<string>com.apple.secureelementservice.test.events</string>
-		<string>com.apple.seservicexctests.credential-events</string>
+		<string>com.apple.seservicetests.credential-events</string>
 		<string>com.apple.passd.nf-events</string>
 		<string>com.apple.nfcd.credential-events</string>
 		<string>com.apple.seld.tsmmanager</string>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.cdp.telemetry</key>
 	<true/>
 	<key>com.apple.cdp.utility</key>

```

### 🆕 tvremoted

> `/usr/libexec/tvremoted`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.tvremoted</string>
	<key>com.apple.CompanionLink</key>
	<true/>
	<key>com.apple.PairingManager.Read</key>
	<true/>
	<key>com.apple.PairingManager.RemovePeer</key>
	<true/>
	<key>com.apple.PairingManager.Write</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.appletv.pbs.allow-screen-saver</key>
	<true/>
	<key>com.apple.appletv.pbs.allow-sleep</key>
	<true/>
	<key>com.apple.appletv.pbs.allow-user-interface-style-change</key>
	<true/>
	<key>com.apple.appletv.pbs.allow-wake</key>
	<true/>
	<key>com.apple.appletv.pbs.app-info-service-access</key>
	<true/>
	<key>com.apple.appletv.pbs.mediaremote</key>
	<true/>
	<key>com.apple.appletv.pbs.person-monitor-service-access</key>
	<true/>
	<key>com.apple.appletv.pbs.person-monitor-service-access.write</key>
	<true/>
	<key>com.apple.appletv.pbs.profile-picker-service-access</key>
	<true/>
	<key>com.apple.appletv.pbs.profile-picker-service-access.read</key>
	<true/>
	<key>com.apple.appletv.pbs.profile-picker-service-access.selectUser</key>
	<true/>
	<key>com.apple.appletv.pbs.topshelf-content-service-access</key>
	<true/>
	<key>com.apple.appletv.pbs.user-profiles</key>
	<true/>
	<key>com.apple.appletv.pbs.user-profiles.select</key>
	<true/>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.bluetooth.doap</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.coreaudio.CanRecordPastData</key>
	<true/>
	<key>com.apple.coreaudio.allow-opus-codec</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.homekit</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.hid.manager.user-access-device</key>
	<true/>
	<key>com.apple.homekit.private-spi-access</key>
	<true/>
	<key>com.apple.icloud.findmydeviced.localfindable.tvremote</key>
	<true/>
	<key>com.apple.intelligentrouting.recommendationservice</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.mediaremote.allow</key>
	<array>
		<string>SiriPassThrough</string>
		<string>TVPairing</string>
	</array>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>EthernetMacAddress</string>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
		<string>UniqueDeviceIDData</string>
		<string>WifiAddress</string>
		<string>WifiAddressData</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>bundleID</string>
		<key>value</key>
		<string>com.apple.TVRemoteApp</string>
	</dict>
	<key>com.apple.private.controlcenter.service.moduleidentifiers</key>
	<array>
		<string>com.apple.control-center.AppleTVRemoteModule</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.hid.client.event-dispatch</key>
	<true/>
	<key>com.apple.private.hid.client.event-monitor</key>
	<true/>
	<key>com.apple.private.homekit</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>tvremoted</string>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceBluetoothAlways</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.tvappservices.container</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Applications/</string>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/private/var/preferences/SystemConfiguration/com.apple.wifi.plist</string>
		<string>/usr/libexec/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Caches/com.apple.HomeKit.configurations/tvremoted/</string>
		<string>/Library/Caches/com.apple.HomeKit/tvremoted/</string>
		<string>/Library/Caches/com.apple.tvremoted/</string>
		<string>/Library/Caches/tvapp_bag/</string>
		<string>/Library/HTTPStorages/com.apple.tvremoted/</string>
		<string>/Library/tvremoted/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOHIDUserDeviceCreate</string>
		<string>IOHIDResourceDeviceUserClient</string>
		<string>IOHIDUserClient</string>
		<string>IO80211APIUserClient</string>
		<string>IOHIDLibUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioQueueServer</string>
		<string>com.apple.audio.AudioSession</string>
		<string>com.apple.audio.SystemSoundServer-iOS</string>
		<string>com.apple.audio.voicetrigger.xpc</string>
		<string>com.apple.audioanalyticsd</string>
		<string>com.apple.bluetooth.xpc</string>
		<string>com.apple.BTLEAudioController.xpc</string>
		<string>com.apple.controlcenter.remoteservice</string>
		<string>com.apple.coremedia.carplayavvc.xpc</string>
		<string>com.apple.coremedia.routediscoverer.xpc</string>
		<string>com.apple.coremedia.routingcontext.xpc</string>
		<string>com.apple.coremedia.systemcontroller.xpc</string>
		<string>com.apple.coremedia.volumecontroller.xpc</string>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.homed.xpc</string>
		<string>com.apple.icloud.findmydeviced.localfindable.tvremote</string>
		<string>com.apple.intelligentroutingd.xpc.media</string>
		<string>com.apple.iohideventsystem</string>
		<string>com.apple.locationd.registration</string>
		<string>com.apple.locationd.synchronous</string>
		<string>com.apple.lsd.open</string>
		<string>com.apple.mediaremoted.xpc</string>
		<string>com.apple.mediasetupd.server</string>
		<string>com.apple.PairingManager</string>
		<string>com.apple.PowerManagement.control</string>
		<string>com.apple.server.bluetooth.le.att.xpc</string>
		<string>com.apple.watchlistd.xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.xpc.amsengagementd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.appletvservices</string>
		<string>com.apple.assistant.logging</string>
		<string>com.apple.audio.virtualaudio</string>
		<string>com.apple.avfoundation.avvc</string>
		<string>com.apple.avfoundation.frecents</string>
		<string>com.apple.coreaudio</string>
		<string>com.apple.coremedia</string>
		<string>com.apple.homesharing</string>
		<string>com.apple.Sharing</string>
		<string>com.apple.videos-preferences</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.itunescloud</string>
		<string>com.apple.mediaremote</string>
		<string>com.apple.tvremoted</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.springboard.launchapplications</key>
	<true/>
	<key>com.apple.springboard.lockScreenContentAssertion</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>com.apple.watchlist.private</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.MediaRemote.pairing</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.ACMobileShim</string>
+		<string>com.apple.AUDeveloperSettings</string>
 		<string>com.apple.GEO</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### uarpd

> `/usr/libexec/uarpd`

```diff

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.uarpassetmanager.uarp</string>
 	</array>
+	<key>com.apple.security.ts.geoservices</key>
+	<true/>
 	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>
 	<true/>
 	<key>com.apple.uarpassetmanager.uarp</key>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 		<string>AppleSPUFastpathDriverUserClient</string>
 		<string>AppleSPUUserClient</string>
 		<string>IOHIDLibUserClient</string>
-		<string>IOUserClient</string>
+		<string>IOUserUserClient</string>
 		<string>AppleCredentialManagerUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 	<true/>
 	<key>keychain-access-groups</key>
 	<array>
-		<string>apple</string>
 		<string>com.apple.bluetooth</string>
 		<string>com.apple.ExposureNotification</string>
 	</array>

```


### SystemOS

### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 		<string>io.island.Island.dev</string>
 		<string>ru.yandex.desktop.yandex-browser</string>
 		<string>ai.perplexity.comet</string>
+		<string>ai.perplexity.comet-beta</string>
 		<string>ai.perplexity.comet-canary</string>
 		<string>ai.perplexity.comet-dev</string>
 		<string>com.coccoc.Coccoc</string>

```
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/Current/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 		<string>io.island.Island.dev</string>
 		<string>ru.yandex.desktop.yandex-browser</string>
 		<string>ai.perplexity.comet</string>
+		<string>ai.perplexity.comet-beta</string>
 		<string>ai.perplexity.comet-canary</string>
 		<string>ai.perplexity.comet-dev</string>
 		<string>com.coccoc.Coccoc</string>

```


### AppOS

### Safari

> `/System/Applications/Safari.app/Contents/MacOS/Safari`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.passes.add</key>
+	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.safari</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>SafariUsageDonation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Unilog.SafariSearch.Stage</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.aiml.unilog.healthTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Unilog.HealthTelemetry</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>*</string>
 	<key>com.apple.private.keychain.inet_expansion_fields</key>

```
### PasswordManagerBrowserExtensionHelper

> `/System/Library/CoreServices/PasswordManagerBrowserExtensionHelper.app/Contents/MacOS/PasswordManagerBrowserExtensionHelper`

```diff

           "signing-identifier": {
             "$in": [
               "ai.perplexity.comet",
+              "ai.perplexity.comet-beta",
               "ai.perplexity.comet-canary",
               "ai.perplexity.comet-dev"
             ]

```
### Web App

> `/System/Library/CoreServices/Web App.app/Contents/MacOS/Web App`

```diff

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.passes.add</key>
+	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.safari</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>SafariUsageDonation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Unilog.SafariSearch.Stage</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.aiml.unilog.healthTelemetry</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Unilog.HealthTelemetry</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>*</string>
 	<key>com.apple.private.keychain.inet_expansion_fields</key>

```


