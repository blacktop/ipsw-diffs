## 🔑 Entitlements


### 🆕 AccessoryLiveActivities_AuthorizationAppSheet

> `/Applications/AccessoryLiveActivities_AuthorizationAppSheet.app/AccessoryLiveActivities_AuthorizationAppSheet`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.chrono.accessoryLiveActivities.app.tool</key>
	<true/>
	<key>com.apple.chrono.accessoryLiveActivities.appSheet.selections</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.private.activitykit.activityAuthorizer</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.chronoservices</string>
		<string>com.apple.chrono.accessoryLiveActivities</string>
		<string>com.apple.sessionservices</string>
	</array>
</dict>
</plist>

```

### 🆕 AccessoryLiveActivities_AuthorizationDialogs

> `/Applications/AccessoryLiveActivities_AuthorizationAppSheet.app/PlugIns/AccessoryLiveActivities_AuthorizationDialogs.appex/AccessoryLiveActivities_AuthorizationDialogs`

- No entitlements *(yet)*
### AccessoryNotificationsSourceSelection

> `/Applications/AccessoryNotificationsSourceSelection.app/AccessoryNotificationsSourceSelection`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.chrono.accessoryLiveActivities.app.tool</key>
+	<true/>
+	<key>com.apple.chrono.accessoryLiveActivities.appSheet.selections</key>
+	<true/>
+	<key>com.apple.private.activitykit.activityAuthorizer</key>
+	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
+	<key>com.apple.private.usernotifications.accessorynotifications.settings</key>
+	<array>
+		<string>com.apple.AccessoryNotificationsSourceSelection</string>
+	</array>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>
 		<string>read</string>

```
### AccessorySetupUI

> `/Applications/AccessorySetupUI.app/AccessorySetupUI`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/mobile/Library/Caches/ProductKit/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 	<array>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.private.corewifi.wifi-network-sharing-ui-xpc</string>
+		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.ProductKitService</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```diff

 	<true/>
 	<key>com.apple.bluetooth.discovery</key>
 	<dict>
-		<key>AppleTVSetup</key>
-		<dict>
-			<key>bleRSSIThresholdHint</key>
-			<integer>-45</integer>
-			<key>discoveryFlags</key>
-			<array>
-				<string>AppleTVSetup</string>
-			</array>
-			<key>osFeatureFlag</key>
-			<string>CompanionServices/TVSetupV2</string>
-			<key>sceneIdentifier</key>
-			<string>AppleTVSetup</string>
-			<key>screenLocked</key>
-			<true/>
-			<key>systemUnlocked</key>
-			<true/>
-		</dict>
-		<key>CompanionSetup</key>
+		<key>MainSetup</key>
 		<dict>
 			<key>bleRSSIThresholdHint</key>
 			<integer>-45</integer>

 			<key>systemUnlocked</key>
 			<true/>
 		</dict>
-		<key>HomePodSetup</key>
-		<dict>
-			<key>bleRSSIThresholdHint</key>
-			<integer>-45</integer>
-			<key>discoveryFlags</key>
-			<array>
-				<string>HomePodSetup</string>
-			</array>
-			<key>discoveryTypes</key>
-			<array>
-				<string>HomePodSetupV2</string>
-			</array>
-			<key>osFeatureFlag</key>
-			<string>CompanionServices/HomePodSetupV2</string>
-			<key>sceneIdentifier</key>
-			<string>HomePodSetup</string>
-		</dict>
 	</dict>
 	<key>com.apple.bluetooth.system</key>
 	<true/>

```
### Family

> `/Applications/Family.app/Family`

```diff

 	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
+	<key>com.apple.excludes-extensions</key>
+	<true/>
 	<key>com.apple.family.ageRange</key>
 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>

 		<string>com.apple.ScreenTimeAgent.ask</string>
 		<string>com.apple.ScreenTimeAgent.setup</string>
 		<string>com.apple.ScreenTimeAgent.downtime</string>
-		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.passd.in-app-payment</string>
-		<string>com.apple.passd.library</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.contactsd.persistence</string>

```
### HeadphoneProxService

> `/Applications/HeadphoneProxService.app/HeadphoneProxService`

```diff

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>UniqueDeviceID</string>
 		<string>UniqueDeviceIDData</string>
 		<string>SerialNumber</string>
 	</array>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 		<string>com.apple.corerecents.recentsd</string>
 		<string>com.apple.callintelligenced.service</string>
 		<string>com.apple.safetycheckd</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.cdp.walrus</key>
 	<true/>
+	<key>com.apple.chrono.accessoryLiveActivities.app.tool</key>
+	<true/>
 	<key>com.apple.chrono.controls</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 	</array>
 	<key>com.apple.private.ndoagent</key>
 	<true/>
+	<key>com.apple.private.nearbyinteraction.device-presence</key>
+	<true/>
+	<key>com.apple.private.nearbyinteraction.privileged</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.network.system-token-fetch</key>

 	</array>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
+	<key>com.apple.private.usernotifications.accessorynotifications.settings</key>
+	<array>
+		<string>com.apple.Preferences</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.Passbook</string>

 		<string>com.apple.alarmkitservices</string>
 		<string>com.apple.seserviced.storage-management-presentation</string>
 		<string>com.apple.homeenergyd.xpc</string>
+		<string>com.apple.chrono.accessoryLiveActivities</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AppleIntelligenceReportingSELFIngestor

> `/System/Library/ExtensionKit/Extensions/AppleIntelligenceReportingSELFIngestor.appex/AppleIntelligenceReportingSELFIngestor`

```diff

 	<array>
 		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
 		<string>/private/var/MobileAsset/AssetsV2/</string>
+		<string>/private/var/MobileSoftwareUpdate/last_update_result.plist</string>
+		<string>/System/Volumes/Update/last_update_result.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	<array>
 		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
 		<string>/System/Library/AssetsV2/</string>
+		<string>/private/var/MobileSoftwareUpdate/last_update_result.plist</string>
+		<string>/System/Volumes/Update/last_update_result.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### AskToViewExtension

> `/System/Library/ExtensionKit/Extensions/AskToViewExtension.appex/AskToViewExtension`

```diff

 	<array>
 		<string>com.apple.asktod</string>
 	</array>
-	<key>com.apple.springboard.opensensitiveurl </key>
+	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 </dict>
 </plist>

```

### 🆕 Vermillion

> `/System/Library/ExtensionKit/Extensions/Vermillion.appex/Vermillion`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.pfl.Vermillion</string>
	<key>com.apple.developer.healthkit</key>
	<true/>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.pfl.container</string>
		<string>com.apple.pfl.preprod.container</string>
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
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.access</key>
	<array/>
	<key>com.apple.private.healthkit.read_authorization_bypass</key>
	<array>
		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
		<string>HKQuantityTypeIdentifierBasalBodyTemperature</string>
		<string>HKCategoryTypeIdentifierAppetiteChanges</string>
		<string>HKCategoryTypeIdentifierBloating</string>
		<string>HKCategoryTypeIdentifierChills</string>
		<string>HKCategoryTypeIdentifierFatigue</string>
		<string>HKCategoryTypeIdentifierHairLoss</string>
		<string>HKCategoryTypeIdentifierHeadache</string>
		<string>HKCategoryTypeIdentifierHotFlashes</string>
		<string>HKCategoryTypeIdentifierMemoryLapse</string>
		<string>HKCategoryTypeIdentifierMoodChanges</string>
		<string>HKCategoryTypeIdentifierNausea</string>
		<string>HKCategoryTypeIdentifierNightSweats</string>
		<string>HKCategoryTypeIdentifierSleepChanges</string>
		<string>HKQuantityTypeIdentifierActiveEnergyBurned</string>
		<string>HKQuantityTypeIdentifierAppleExerciseTime</string>
		<string>HKCategoryTypeIdentifierAppleStandHour</string>
		<string>HKQuantityTypeIdentifierAppleStandTime</string>
		<string>HKQuantityTypeIdentifierBasalEnergyBurned</string>
		<string>HKQuantityTypeIdentifierDistanceCycling</string>
		<string>HKQuantityTypeIdentifierDistanceDownhillSnowSports</string>
		<string>HKQuantityTypeIdentifierDistanceSwimming</string>
		<string>HKQuantityTypeIdentifierDistanceWalkingRunning</string>
		<string>HKQuantityTypeIdentifierFlightsClimbed</string>
		<string>HKCategoryTypeIdentifierMindfulSession</string>
		<string>HKQuantityTypeIdentifierStepCount</string>
		<string>HKQuantityTypeIdentifierTimeInDaylight</string>
		<string>HKWorkoutTypeIdentifier</string>
		<string>HKActivitySummaryTypeIdentifier</string>
		<string>HKQuantityTypeIdentifierBodyMass</string>
		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
		<string>HKQuantityTypeIdentifierOxygenSaturation</string>
		<string>HKQuantityTypeIdentifierAppleSleepingWristTemperature</string>
		<string>HKQuantityTypeIdentifierBloodPressureDiastolic</string>
		<string>HKQuantityTypeIdentifierHeartRate</string>
		<string>HKQuantityTypeIdentifierBloodPressureSystolic</string>
		<string>HKQuantityTypeIdentifierHeartRateVariabilitySDNN</string>
		<string>HKQuantityTypeIdentifierRestingHeartRate</string>
		<string>HKQuantityTypeIdentifierWalkingHeartRateAverage</string>
		<string>HKQuantityTypeIdentifierAppleWalkingSteadiness</string>
		<string>HKQuantityTypeIdentifierNumberOfTimesFallen</string>
		<string>HKQuantityTypeIdentifierSixMinuteWalkTestDistance</string>
		<string>HKQuantityTypeIdentifierStairAscentSpeed</string>
		<string>HKQuantityTypeIdentifierStairDescentSpeed</string>
		<string>HKQuantityTypeIdentifierVO2Max</string>
		<string>HKQuantityTypeIdentifierWalkingAsymmetryPercentage</string>
		<string>HKQuantityTypeIdentifierWalkingDoubleSupportPercentage</string>
		<string>HKQuantityTypeIdentifierWalkingSpeed</string>
		<string>HKQuantityTypeIdentifierWalkingStepLength</string>
		<string>HKQuantityTypeIdentifierRespiratoryRate</string>
		<string>HKCategoryTypeIdentifierSleepAnalysis</string>
		<string>HKScoredAssessmentTypeIdentifierPHQ9</string>
		<string>HKScoredAssessmentTypeIdentifierGAD7</string>
	</array>
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
</dict>
</plist>

```
### contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.contacts.favorites</string>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.CallHistory.read</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### AppleIntelligenceReportingProcessingService

> `/System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/XPCServices/AppleIntelligenceReportingProcessingService.xpc/AppleIntelligenceReportingProcessingService`

```diff

 	<array>
 		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
 		<string>/private/var/MobileAsset/AssetsV2/</string>
+		<string>/private/var/MobileSoftwareUpdate/last_update_result.plist</string>
+		<string>/System/Volumes/Update/last_update_result.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	<array>
 		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
 		<string>/System/Library/AssetsV2/</string>
+		<string>/private/var/MobileSoftwareUpdate/last_update_result.plist</string>
+		<string>/System/Volumes/Update/last_update_result.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.game-center</key>
+	<array>
+		<string>Account</string>
+	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>
 	<key>com.apple.private.kvs.ignore-quota</key>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	</array>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.DeviceAccess</key>
+	<true/>
 	<key>com.apple.DeviceAccess.private</key>
 	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>

 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.private.sessionkit.alertPresenter</key>
+	<true/>
 	<key>com.apple.private.sessionkit.listener</key>
 	<true/>
 	<key>com.apple.private.sessionkit.sessionFinisher</key>

 	</array>
 	<key>com.apple.private.tcc.events.subscriber</key>
 	<true/>
+	<key>com.apple.private.tcc.icons_for_prompts</key>
+	<true/>
+	<key>com.apple.private.usernotifications.accessorynotifications.settings</key>
+	<array>
+		<string>com.apple.chronod.accessoryLiveActivitiesForwarding</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.chronod.diagnostics.usernotifications</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.DeviceAccess.xpc</string>
+		<string>com.apple.usernotifications.accessorynotifications</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### cdpd

> `/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd`

```diff

 	<true/>
 	<key>com.apple.securebackupd.access</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.appleaccount.transparency</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>

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
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 		<string>com.apple.keyboard.preferences</string>
 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.SOS</string>
+		<string>com.apple.facetime.bag</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/UnifiedAssetFramework</string>
 		<string>/Library/Assistant/RecordedAudio/</string>
+		<string>/Library/Assistant/CustomVocabulary/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### mobiletimerd

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd`

```diff

 	<string>com.apple.mobiletimer</string>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.mobiletimer</string>
+		<string>com.apple.clock</string>
+	</array>
 	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
 	<true/>
 	<key>com.apple.private.appintents.live-entities.write</key>

```
### ProductKitService

> `/System/Library/PrivateFrameworks/ProductKitCore.framework/XPCServices/ProductKitService.xpc/ProductKitService`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/Caches/ProductKit</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 SwiftUITracingSupport

> `/System/Library/PrivateFrameworks/SwiftUITracingSupport.framework/SwiftUITracingSupport`

- No entitlements *(yet)*
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
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
-		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

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

 	<true/>
 	<key>com.apple.bulletinboard.settings</key>
 	<true/>
+	<key>com.apple.chrono.accessoryLiveActivities.app.tool</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.contactsd</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.FileCoordination</string>
+		<string>com.apple.chrono.accessoryLiveActivities</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>
 		<string>com.apple.usernotifications.accessorynotifications</string>
 		<string>com.apple.usernotificationsvendor.listener</string>
+		<string>com.apple.usernotifications.accessory.session</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>nano-preferences-read-write</key>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.sensitivecontentanalysis.client</key>

 	</array>
 	<key>com.apple.security.device.camera</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/com.apple.messages/</string>

 		<string>com.apple.ScreenTimeAgent.communication</string>
 		<string>com.apple.safetycheckd</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Magnifier

> `/private/var/staged_system_apps/Magnifier.app/Magnifier`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Magnifier</string>
 	<key>com.apple.developer.user-fonts</key>
 	<array>
 		<string>app-usage</string>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<integer>4014732562</integer>
+		<key>client-identifier</key>
+		<string>com.apple.Maps</string>
+	</dict>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/mobile/Library/Application Support/com.apple.ap.promotedcontentd/shared/all/ro/</string>
 		<string>/private/var/db/MobileIdentityData/AuthListReadyCdHashes.plist</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/mobile/Library/ReplayKit/</string>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/var/mobile/Library/Application Support/com.apple.ap.promotedcontentd/shared/all/rw/</string>
 		<string>/private/var/mobile/Library/SMS/</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Maps/</string>
 		<string>/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.fairplaydeviceidentityd</string>
+		<string>com.apple.ap.promotedcontent.injectbucketid</string>
+		<string>com.apple.ap.promotedcontent.metrics</string>
+		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.appintents.LiveEntityService</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.misagent</string>
+		<string>com.apple.appintents.LiveEntityService</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.realitysimulation.apps</string>
 		<string>com.apple.finance.store</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.AdPlatforms</string>
 		<string>com.apple.Maps.commute</string>
 		<string>com.apple.GMM</string>
 		<string>com.apple.NanoMailKit</string>

 	</array>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>AD_PLATFORMS_APPSTORE_ALL_PLACEMENTS</string>
 		<string>MAPS_SRP_AUTOCOMPLETE</string>
 		<string>2020</string>
 	</array>

```
### caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
+	<key>com.apple.private.carkit</key>
+	<true/>
 	<key>com.apple.private.carkit.sessionBoost</key>
 	<true/>
 	<key>com.apple.private.carp</key>

 		<string>com.apple.CarPlayApp.cluster-theme-service</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.carkit.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### dasd

> `/usr/libexec/dasd`

```diff

 		<string>ActivityScheduler.Dependency.Completion</string>
 		<string>ActivityScheduler.Dependency.Result</string>
 		<string>Device.Thermals.BatteryTemperature</string>
+		<string>Device.AppResume.Predictions</string>
 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.custom.properties.writable</key>
 	<true/>
+	<key>com.apple.bluetooth.internal</key>
+	<true/>
 	<key>com.apple.bluetooth.pairedInfoSecurity</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

 	<array>
 		<string>systemgroup.com.apple.accessorysetupkit</string>
 	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.events.subscriber</key>

 		<string>kTCCServiceAccessoryNotifications</string>
 		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
+		<string>kTCCServiceAudioAccessoryHeadTrackData</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>

 		<string>kTCCServiceAccessoryNotifications</string>
 		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
+		<string>kTCCServiceAudioAccessoryHeadTrackData</string>
 	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>
 	<array>

 	<array>
 		<string>/private/var/preferences/com.apple.networkextension.plist</string>
 		<string>/usr/sbin/</string>
+		<string>/private/var/Managed Preferences/mobile/com.apple.bluetooth.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/preferences/com.apple.networkd.plist</string>
 		<string>/private/var/mobile/tmp/com.apple.deviceaccessd/</string>
+		<string>/Library/Managed Preferences/mobile/com.apple.bluetooth.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.DeviceAccess/</string>
+		<string>/Library/Managed Preferences/mobile/com.apple.bluetooth.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	<array>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.DeviceAccess</string>
+		<string>com.apple.Bluetooth</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

 	<array>
 		<string>systemgroup.com.apple.accessorysetupkit</string>
 	</array>
+	<key>com.apple.security.temporary-exception.sbpl</key>
+	<array>
+		<string>(allow user-preference-read (preference-domain "com.apple.bluetooth"))</string>
+		<string>(allow file-read-data (preference-domain "com.apple.bluetooth"))</string>
+		<string>(allow user-preference-write (preference-domain "com.apple.bluetooth"))</string>
+	</array>
 	<key>com.apple.wifip2pd</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### gamed

> `/usr/libexec/gamed`

```diff

 	<true/>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
 	<key>com.apple.private.ids.registration</key>

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
### textunderstandingd

> `/usr/libexec/textunderstandingd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.textunderstandingd</string>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>

 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.proactive.PersonalizationPortrait.TextUnderstanding</string>
 		<string>com.apple.FileProvider</string>
+		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 		<string>/usr/sbin/BTLEServer/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/log/CoreCapture/com.apple.KalBluetooth_driver/FwLogs/</string>
+		<string>/private/var/Managed Preferences/mobile/com.apple.bluetooth.plist</string>
 		<string>/private/var/log/CoreCapture/com.apple.driver.AppleCentauriBeta/BetaFirmwareLogs/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>

```
