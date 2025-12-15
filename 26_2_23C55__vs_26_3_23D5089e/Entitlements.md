## 🔑 Entitlements


### 🆕 AccessoryNotificationsSourceSelection

> `/Applications/AccessoryNotificationsSourceSelection.app/AccessoryNotificationsSourceSelection`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.usernotifications.settings</key>
	<array>
		<string>read</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.usernotifications.accessorynotifications</string>
		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
	</array>
</dict>
</plist>

```

### 🆕 AccessoryNotificationsSetupExtension

> `/Applications/AccessoryNotificationsSourceSelection.app/PlugIns/AccessoryNotificationsSetupExtension.appex/AccessoryNotificationsSetupExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.usernotifications.settings</key>
	<array>
		<string>read</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
	</array>
</dict>
</plist>

```

### 🆕 EmojiPoster

> `/Applications/EmojiPoster.app/EmojiPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.EmojiPoster</string>
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

### 🆕 EmojiPosterExtension

> `/Applications/EmojiPoster.app/Extensions/EmojiPosterExtension.appex/EmojiPosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
</dict>
</plist>

```

### 🆕 GradientPosterExtension

> `/Applications/GradientPoster.app/Extensions/GradientPosterExtension.appex/GradientPosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
</dict>
</plist>

```

### 🆕 GradientPoster

> `/Applications/GradientPoster.app/GradientPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.GradientPoster</string>
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
### TypeToSiriWidgetExtension

> `/Applications/Siri.app/PlugIns/TypeToSiriWidgetExtension.appex/TypeToSiriWidgetExtension`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.siri.TypeToSiriWidget</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
+	<key>com.apple.familycircle</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<string>YES</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.announced.client</key>
 	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

```
### Tamale

> `/Applications/Tamale.app/Tamale`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
 	<key>com.apple.application-identifier</key>

 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

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

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.aop.hid-device.user-client</key>
 	<dict>
 		<key>orientation</key>

```

### 🆕 ATXThumbnail

> `/System/Library/ExtensionKit/Extensions/ATXThumbnail.appex/ATXThumbnail`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.hardened-process.hardened-heap</key>
	<true/>
</dict>
</plist>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/AssetMetricsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>allow-softwareupdated</key>
+	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.siri.metrics.AssetMetricsExtension</string>
+	<key>com.apple.MobileAsset.MobileSoftwareUpdate.UpdateBrain</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.private.assistant.settings</key>

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Siri.SELFProcessedEvent</string>
+		<string>Device.KeybagLocked</string>
+		<string>Device.BootSession</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>Sage.Transcript</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>AssetDelivery.UAF.DailyStatus</string>
+		<string>Device.KeybagLocked</string>
+		<string>Device.BootSession</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

 				<string>Siri.SELFProcessedEvent</string>
 				<string>IntelligenceFlow.Transcript.Datastream</string>
 				<string>AssetDelivery.UAF.DailyStatus</string>
+				<string>Device.KeybagLocked</string>
+				<string>Device.BootSession</string>
 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.softwareupdate.preferences</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.mobile.softwareupdated</string>
 		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.mobile.softwareupdated</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

 		<string>stream.unifiedMessageStream.readonly</string>
 		<string>stream.rawUnifiedMessageStream.readonly</string>
 	</array>
+	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>
+	<true/>
 </dict>
 </plist>
 

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.priml.allowed-server-model-bundles</key>
-	<array/>
+	<dict>
+		<key>com.apple.fm.language.instruct_server_v1.autograder</key>
+		<array>
+			<string>Automated.Autograding.Genmoji</string>
+			<string>Automated.Autograding.Summarization</string>
+		</array>
+		<key>com.apple.fm.language.instruct_server_v1.shortcuts_ask_afm_action_v2</key>
+		<array>
+			<string>Shortcuts.AskAFMAction.automated</string>
+		</array>
+		<key>com.apple.fm.language.instruct_server_v1.text_summarizer</key>
+		<array>
+			<string>summarization.summarizeMailMessageOnDemand</string>
+		</array>
+	</dict>
 	<key>com.apple.priml.pfl.Morpheus.allowed</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allowmessagescontent</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

```

### 🆕 Notification

> `/System/Library/ExtensionKit/Extensions/Notification.appex/Notification`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.quicklook-thumbnail.blastdoor</key>
	<true/>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.hardened-process.hardened-heap</key>
	<true/>
</dict>
</plist>

```
### AudioConverterHardenedService

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterHardenedService.xpc/AudioConverterHardenedService`

```diff

 	<key>com.apple.private.memory.ownership_transfer</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
-	<string>AudioConverterService</string>
+	<string>autobox</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Preferences/com.apple.coreaudio.plist</string>

```
### HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

```diff

 	<array>
 		<string>/private/var/tmp/HKSV/</string>
 		<string>/private/var/log/com.apple.wifivelocity/</string>
+		<string>/private/var/db/diagnostics/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 		<string>com.apple.appstored</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.amsengagementd</string>
+		<string>com.apple.madctl</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

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
### com.apple.DiagnosticExtensions.WiFi

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.WiFi.appex/com.apple.DiagnosticExtensions.WiFi`

```diff

 	<true/>
 	<key>com.apple.private.wifivelocity</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Logs/</string>

 		<string>com.apple.wifivelocityd</string>
 		<string>com.apple.centaurid.xpc</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/Library/Logs/CrashReporter/CoreCapture/</string>
+		<string>/Library/Preferences/</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/run/com.apple.wifivelocity/</string>
+		<string>/private/var/log/com.apple.wifivelocity/</string>
+		<string>/private/var/tmp/ConnectivityDE/</string>
+	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.wifivelocityd</string>
+		<string>com.apple.centaurid.xpc</string>
+	</array>
+	<key>com.apple.wifivelocity</key>
+	<true/>
 </dict>
 </plist>
 

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.MobileAssetVerbose</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>AppleIntelligence.Reporting.AssetDeliveryLog.ModelCatalog</key>
 				<dict>
 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>AppleIntelligence.Reporting.AssetDeliveryLog.SoftwareUpdateController</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>AppleIntelligence.Reporting.AssetDeliveryLog.UnifiedAssetFramework</key>
 				<dict>
 					<key>mode</key>

 		<string>com.apple.appleintelligencereporting</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.generativepartnerservicesettings</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
+	</array>
 	<key>com.apple.security.ts.asset-access</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/MessagesMetaData/</string>
+		<string>/Library/Caches/com.apple.imdpersistence.IMDPersistenceAgent</string>
+	</array>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>AGXDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.MigrationKit.resumeBackgroundActivity</key>
 	<true/>
+	<key>com.apple.private.imcore.imagent</key>
+	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
 	<key>com.apple.private.install.distributor-info-source</key>

 		<string>/Library/CloudStorage/</string>
 		<string>/Library/Mobile Documents/</string>
 		<string>/Containers/</string>
+		<string>/Library/UserConfigurationProfiles/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.apfs.allocate_contig</key>
 	<true/>
 	<key>com.apple.private.apfs.create-sealed-snapshot</key>

```
### sociallayerd

> `/System/Library/PrivateFrameworks/SocialLayer.framework/sociallayerd.app/sociallayerd`

```diff

 	<true/>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-calls</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
-	<key>com.apple.developer.icloud-container-identifiers</key>
-	<array>
-		<string>com.apple.facetime</string>
-	</array>
-	<key>com.apple.developer.icloud-services</key>
-	<array>
-		<string>CloudDocuments</string>
-	</array>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<string>com.apple.facetime</string>
 		<string>com.apple.Photos</string>
 	</array>
-	<key>com.apple.developer.ubiquity-container-identifiers</key>
-	<array>
-		<string>com.apple.facetime</string>
-	</array>
 	<key>com.apple.duet.expertcenter.consumer</key>
 	<true/>
 	<key>com.apple.facetimemessagestored.service</key>

 	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
-	<key>com.apple.private.clouddocs.auto-accept-share</key>
-	<true/>
-	<key>com.apple.private.clouddocs.sharing.private-interface</key>
-	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
+		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.ess</string>
 		<string>com.apple.private.alloy.phone.auth</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
+		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.phone.auth</string>
 		<string>com.apple.private.alloy.facetime.audio</string>
 		<string>com.apple.private.alloy.facetime.sync</string>

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
+		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>
 		<string>com.apple.private.alloy.tincan.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
+		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>
 		<string>com.apple.private.alloy.tincan.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
+		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>
 		<string>com.apple.private.alloy.tincan.audio</string>

 	<array>
 		<string>com.apple.default-app.phone</string>
 	</array>
-	<key>com.apple.private.librarian.container-proxy</key>
-	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/ActivationState</string>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
-	<key>com.apple.private.security.storage.MobileDocuments</key>
-	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.icons_for_prompts</key>
+	<true/>
 	<key>com.apple.private.usernotifications.accessory.host</key>
 	<true/>
 	<key>com.apple.private.usernotifications.forwarding</key>

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
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.announced.client</key>
 	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

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
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.announced.client</key>
 	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

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
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 	</array>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.focus.activity-manager</string>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 		<string>com.apple.coremedia.volumecontroller.xpc</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.linkd.autoShortcut</string>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.BrowserEngineKit.Intermediary</string>
 		<string>com.apple.timed.xpc</string>
-		<string>com.apple.securityd.xpc</string>
+		<string>com.apple.securityd</string>
 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 		<string>group.com.apple.weather</string>
 		<string>group.com.apple.stocks-news</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/Application Support/com.apple.ap.promotedcontentd/shared/all/ro/</string>
+	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/Application Support/com.apple.ap.promotedcontentd/shared/all/rw/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.appprotectiond.write.access</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<string>com.apple.focus.activity-manager</string>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.email.maild</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>

```
### Stocks

> `/private/var/staged_system_apps/Stocks.app/Stocks`

```diff

 		<string>group.com.apple.stocks-news</string>
 		<string>group.com.apple.news</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<string>/private/var/mobile/Library/Application Support/com.apple.ap.promotedcontentd/shared/all/ro/</string>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<string>/private/var/mobile/Library/Application Support/com.apple.ap.promotedcontentd/shared/all/rw/</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>

```

### 🆕 WeatherPoster

> `/private/var/staged_system_apps/WeatherPosterApp.app/Extensions/WeatherPoster.appex/WeatherPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.weather</string>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.locationd.prompt_from_background</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.storage.Weather</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.weather</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.countryd/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Weather/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.weather</string>
		<string>com.apple.weather.internal</string>
		<string>com.apple.weather.sensitive</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```

### 🆕 WeatherPosterApp

> `/private/var/staged_system_apps/WeatherPosterApp.app/WeatherPosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Posters.WeatherPosterApp</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/private/var/staged_system_apps/WeatherPosterApp.app/WeatherPosterApp</string>
	</dict>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### DumpPanic

> `/usr/libexec/DumpPanic`

```diff

 	<array>
 		<string>InverseDeviceID</string>
 	</array>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
 	<key>com.apple.private.coredump-encryption-key</key>
 	<true/>
 	<key>com.apple.private.diagnostic-intelligence</key>

```
### MobileGestaltHelper

> `/usr/libexec/MobileGestaltHelper`

```diff

 	<array>
 		<string>NULL/ActivationRegulatoryVariant</string>
 	</array>
+	<key>com.apple.private.security.storage.MobileGestaltCache</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleBiometricServicesUserClient</string>

```
### assetsubscriptiond

> `/usr/libexec/assetsubscriptiond`

```diff

 	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/preferences/com.apple.networkd.plist</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### containermanagerd_system

> `/usr/libexec/containermanagerd_system`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileContainerManager</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileGestaltCache</key>
+	<true/>
 	<key>com.apple.private.vfs.allow-low-space-writes</key>
 	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 	<array>
 		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
+		<string>kTCCServiceAccessoryNotifications</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
+		<string>kTCCServiceAccessoryNotifications</string>
 		<string>kTCCServiceAll</string>
 	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>

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
### mobile_diagnostics_relay

> `/usr/libexec/mobile_diagnostics_relay`

```diff

 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
-	<key>com.apple.private.RemoteServiceDiscovery.device-admin</key>
-	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>com.apple.PurpleBuddy/SetupDone</string>

 	<array>
 		<string>RootDomainUserClient</string>
 	</array>
-	<key>com.apple.security.network.client</key>
-	<true/>
 </dict>
 </plist>
 

```
### watchdogd

> `/usr/libexec/watchdogd`

```diff

 	<true/>
 	<key>com.apple.private.apfs.key_migration</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
 	<key>com.apple.private.endpoint-security.client</key>
 	<true/>
 	<key>com.apple.private.endpoint-security.default-muter</key>

```
### webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

 		<string>com.apple.Safari.History.Service</string>
 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.security.octagon</string>
+		<string>com.apple.securityd</string>
 		<string>com.apple.lsd.xpc</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>

```
