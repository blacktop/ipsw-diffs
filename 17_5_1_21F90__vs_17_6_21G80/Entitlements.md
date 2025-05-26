## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<string>409835401</string>
 	<key>application-identifier</key>
 	<string>com.apple.AMSEngagementViewService</string>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<true/>
 	<key>com.apple.app-distribution.private</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.geoservices.map-subscriptions.check-existence</key>
+	<true/>
+	<key>com.apple.geoservices.map-subscriptions.size-estimate</key>
+	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.itunesstored.lookup</key>

 	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>siriRemembers</string>
+	</array>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>Lookup</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.iphone.axserver</string>
 		<string>com.apple.ClipServices.clipserviced</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>

```
### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.QuartzCore.secure-mode</key>
+	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<array>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 	<array>
 		<string>com.apple.private.alloy.nameandphoto</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.private.alloy.biz</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>

 		<string>com.apple.camera</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.handwriting</string>
 		<string>com.apple.MobileSMS.CKDNDList</string>
 		<string>com.apple.MobileSMSPreview</string>

```
### MessagesAssistantExtension

> `/Applications/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension`

```diff

 	<array>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>

```
### MessagesNotificationExtension

> `/Applications/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<array>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>

```
### MessagesTranscriptExtension

> `/Applications/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<array>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>

```
### MobileSlideShow

> `/Applications/MobileSlideShow.app/MobileSlideShow`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
+	<key>com.apple.runningboard.photosretailexperience</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.PassKitCoreXPCService</string>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.idcredd.biometrics.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.seserviced.sereservation.client</string>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 		<string>modeConfigurationUIFlowLoggingEvent</string>
 		<string>SystemSettings.GestureEducation.Multitasking</string>
 		<string>SystemSettings.GestureEducation.PillOutcome</string>
+		<string>Safari.AutoPlay</string>
+		<string>Safari.WebPagePerformance</string>
+		<string>Safari.Navigations</string>
+		<string>Safari.PageLoad</string>
+		<string>Safari.WindowProxy</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
+	<key>com.apple.private.iokit.batteryhealthstate</key>
+	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>

 	<array>
 		<string>com.apple.springboard</string>
 		<string>com.apple.momentsd</string>
+		<string>com.apple.seserviced.contactlessCredential.settings</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### RecoverDeviceUI

> `/Applications/RecoverDeviceUI.app/RecoverDeviceUI`

```diff

 	<key>com.apple.bluetooth.discovery</key>
 	<dict>
 		<key>bleRSSIThresholdHint</key>
-		<integer>-60</integer>
+		<integer>-45</integer>
 		<key>discoveryFlags</key>
 		<array>
 			<string>OSR</string>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.BiometricLivenessFlag</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage.SetDSLModeEnabled</key>
 	<true/>
 	<key>com.apple.private.MobileActivation</key>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
+	<dict>
+		<key>com.apple.productkit.personalization</key>
+		<string>com.apple.productkit.personalization</string>
+	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>siriRemembers</string>
+	</array>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>UninstallForLaunchServices</string>

```
### com.apple.mlhost.TelemetryWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.TelemetryWorker.appex/com.apple.mlhost.TelemetryWorker`

```diff

 				<string>Lighthouse.Ledger.TaskTelemetry</string>
 				<string>Lighthouse.Ledger.DeviceTelemetry</string>
 				<string>Lighthouse.Ledger.TaskCustomEvent</string>
+				<string>Lighthouse.Ledger.DediscoPrivacyEvent</string>
 			</array>
 		</dict>
 	</dict>

```
### com.apple.HealthKit.HealthDiagnosticExtension

> `/System/Library/Frameworks/HealthKit.framework/PlugIns/com.apple.HealthKit.HealthDiagnosticExtension.appex/com.apple.HealthKit.HealthDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.powerd.lowpowermode.allow</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appstored</key>

```
### UtilityExtension

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
+	<key>com.apple.private.carkit</key>
+	<true/>
 	<key>com.apple.private.carkit.app</key>
 	<true/>
 	<key>com.apple.private.carkit.dnd</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.location</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>

 	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>
 	<true/>
+	<key>com.apple.siri.location</key>
+	<true/>
 	<key>com.apple.siri.pommes_search_xpc_service</key>
 	<true/>
 	<key>com.apple.siriinferenced</key>

```
### cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

```diff

 	<true/>
 	<key>com.apple.telephony.cupolicy-monitor-access</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.photos.client-side-encryption-manager</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.CloudSharingUI.AddParticipants

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/PlugIns/com.apple.CloudSharingUI.AddParticipants.appex/com.apple.CloudSharingUI.AddParticipants`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.coreduetd.people</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
 		<string>iyfxmLogGVIaH7aEgqwcIA</string>
 	</array>
 	<key>com.apple.private.applemediaservices</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<array>
 		<string>preferences.plist</string>
 	</array>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.accessoryupdater.uarp</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 		<string>com.apple.private.alloy.messagesquickswitch</string>
 		<string>com.apple.private.alloy.sms</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.private.alloy.sms.watch</string>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.private.alloy.messagenotification</string>

 		<string>com.apple.private.alloy.sms.watch</string>
 		<string>com.apple.private.alloy.sms</string>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.private.alloy.messagenotification</string>
 		<string>com.apple.private.alloy.gelato</string>

 	<key>com.apple.private.ids.registration</key>
 	<array>
 		<string>com.apple.madrid</string>
+		<string>com.apple.madrid.lite</string>
 		<string>com.apple.ess</string>
 		<string>com.apple.private.ac</string>
 	</array>

```
### NFRadioPowerSwitch

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRadioPowerSwitch.xpc/NFRadioPowerSwitch`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
+</dict>
+</plist>
 

```
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 	<string>628765583</string>
 	<key>application-identifier</key>
 	<string>com.apple.newsd</string>
+	<key>aps-environment</key>
+	<string>production</string>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.pegasus.context</key>

 	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
-	<key>com.apple.private.domain-extension</key>
-	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>

 	<array>
 		<string>group.com.apple.newsd</string>
 	</array>
+	<key>com.apple.private.sessionkit.custom-platter-target</key>
+	<true/>
+	<key>com.apple.private.sessionkit.customPushProcessIdentifier</key>
+	<true/>
+	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
+	<true/>
+	<key>com.apple.private.sessionkit.sessionRequest</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.newsd</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.news.ANFDecoder</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.news.TodayFeedConfigDecoder</string>
+		<string>com.apple.sessionservices</string>
+		<string>com.apple.duetactivityscheduler</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.newscore2</string>
 	</array>
+	<key>com.apple.sessionkit.broadcastPush</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>1397409257</string>
 </dict>

```
### SiriGeoIntentExtension

> `/System/Library/PrivateFrameworks/SiriGeo.framework/PlugIns/SiriGeoIntentExtension.appex/SiriGeoIntentExtension`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.location</string>
 		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>
 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.routined.registration</string>

 	<array>
 		<string>com.apple.GEO</string>
 	</array>
+	<key>com.apple.siri.location</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 SiriKitUIPlugin

> `/System/Library/Snippets/UIPlugins/SiriKitUIPlugin.bundle/SiriKitUIPlugin`

- No entitlements *(yet)*
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
 		<string>re6Zb+zwFKJNlkQTUeT+/w</string>
 		<string>hiHut/WR+B9Lx/vd0WyeNg</string>
 		<string>iyfxmLogGVIaH7aEgqwcIA</string>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

```
### MobileTimer

> `/private/var/staged_system_apps/MobileTimer.app/MobileTimer`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>
+		<string>/private/var/mobile/Media/Purchases/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/DeviceRegistry/</string>

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 		<string>com.apple.news.TodayFeedConfigDecoder</string>
 		<string>com.apple.newsd.analytics</string>
 		<string>com.apple.newsd.download</string>
+		<string>com.apple.newsd.live-activity</string>
 		<string>com.apple.newsd.today-feed</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.routined.internal</string>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<array>
 		<string>com.apple.financed.service.bankconnect</string>
 		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.seserviced.session</string>
 		<string>com.apple.SharingServices</string>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<true/>
 	<key>com.apple.springboard.externaldisplay.displayArrangements</key>
 	<true/>
+	<key>com.apple.springboard.home-screen-configuration</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### mlhostd

> `/usr/libexec/mlhostd`

```diff

 	</array>
 	<key>com.apple.private.biome.pruner</key>
 	<array>
-		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 		<string>Lighthouse.Ledger.TaskStatus</string>
 		<string>Lighthouse.Ledger.TaskError</string>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 		<string>Lighthouse.Ledger.TaskTelemetry</string>
 		<string>Lighthouse.Ledger.DeviceTelemetry</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
-		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 		<string>Lighthouse.Ledger.TaskStatus</string>
 		<string>Lighthouse.Ledger.TaskError</string>
+		<string>Lighthouse.Ledger.TaskCustomEvent</string>
 		<string>Lighthouse.Ledger.TaskTelemetry</string>
 		<string>Lighthouse.Ledger.DeviceTelemetry</string>
 	</array>

 			<array>
 				<string>Lighthouse.Ledger.TaskStatus</string>
 				<string>Lighthouse.Ledger.TaskError</string>
+				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 				<string>Lighthouse.Ledger.TaskTelemetry</string>
 				<string>Lighthouse.Ledger.DeviceTelemetry</string>
-				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>
 		</dict>
 	</dict>

```
### mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 	<true/>
 	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
 	<true/>
+	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
+	<true/>
+	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
+	<true/>
 	<key>com.apple.private.applesepmanager.allow</key>
 	<true/>
 	<key>com.apple.private.corerepair.fdr</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.timed</key>
 	<true/>
 	<key>com.apple.wirelessproxd-object-discovery</key>

```
