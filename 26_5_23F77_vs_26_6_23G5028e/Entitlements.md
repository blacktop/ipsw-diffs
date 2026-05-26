## 🔑 Entitlements

### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
+		<string>com.apple.tv</string>
 		<string>com.apple.Passbook</string>
 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.journal</string>

```

### 🆕 AXFlashScreenUIServer

> `/System/Library/AccessibilityBundles/AXFlashScreenUIServer.axuiservice/AXFlashScreenUIServer`

- No entitlements *(yet)*
### GameOverlayUI

> `/System/Library/CoreServices/GameOverlayUI.app/GameOverlayUI`

```diff

 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.appstored.install-apps</key>
+	<true/>
+	<key>com.apple.appstored.private</key>
+	<true/>
+	<key>com.apple.appstored.update-apps</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

```
### ShortcutsTopHitsExtension

> `/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension`

```diff

 	</array>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
+	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.shortcuts</string>
+	</dict>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
-	<key>com.apple.private.security.storage.triald</key>
-	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.storekit</key>

 	<array>
 		<string>/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>
 		<string>/Library/Trial/NamespaceDescriptors/</string>
-		<string>/Library/Trial/Treatments/511/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
-	<key>com.apple.private.security.storage.triald</key>
-	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.storekit</key>

 	<array>
 		<string>/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>
 		<string>/Library/Trial/NamespaceDescriptors/</string>
-		<string>/Library/Trial/Treatments/511/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### CMFSyncAgent

> `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent`

```diff

 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

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
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 <plist version="1.0">
 <dict>
 	<key>com.apple.fileprovider.share</key>
-        <true/>
+	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.customAccounts</key>

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.trustkit</string>
 		<string>com.apple.onetimepasscodes</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.conference</string>

```

### 🆕 MapsBlastDoorService

> `/System/Library/PrivateFrameworks/MapsBlastDoorSupport.framework/XPCServices/MapsBlastDoorService.xpc/MapsBlastDoorService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
	<false/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.hardened-process.hardened-heap</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.restrict.notifyd</key>
	<true/>
	<key>com.apple.pac.shared_region_id</key>
	<string>BlastDoor</string>
	<key>com.apple.private.darwin-notification.introspect</key>
	<array>
		<string>com.apple.system.logging.prefschanged</string>
		<string>com.apple.system.timezone</string>
		<string>com.apple.CFPreferences._domainsChangedExternally</string>
	</array>
	<key>com.apple.private.disable-log-mach-ports</key>
	<true/>
	<key>com.apple.private.pac.exception</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>blastdoor-messages</string>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>blastdoor-post-launch</string>
	</array>
	<key>com.apple.private.security.message-filter</key>
	<true/>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>blastdoor-post-launch</string>
	</array>
	<key>com.apple.security.hardened-process.containment.ipc</key>
	<true/>
	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>
	<integer>1</integer>
</dict>
</plist>

```
### mapspushd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/mapspushd`

```diff

 		<string>com.apple.Maps.MapsSync.store</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.MapsBlastDoorService</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```

### 🆕 NFLocationService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFLocationService.xpc/NFLocationService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
</dict>
</plist>

```

### 🆕 NFReportingService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFReportingService.xpc/NFReportingService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
</dict>
</plist>

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
### icloudsubscriptionoptimizerd

> `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerDaemon.framework/icloudsubscriptionoptimizerd/icloudsubscriptionoptimizerd`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.ts.power-assertions</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.icloudsubscriptionoptimizerd</string>
 	<key>platform-application</key>

```
### LighthousePlugin

> `/System/Library/PrivateFrameworks/iCloudSubscriptionOptimizerLighthouse.framework/PlugIns/LighthousePlugin.appex/LighthousePlugin`

```diff

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/var/mobile/Library/Trial/Treatments/default_factors_1370.pb</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.triald.namespace-management </string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
-		<string>1370</string>
+		<string>LIGHTHOUSE_ICLOUD_SHADOW_EVALUATION</string>
 	</array>
 </dict>
 </plist>

```
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
-	<key>com.apple.private.security.storage.triald</key>
-	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.storekit</key>

 	<array>
 		<string>/Library/Caches/com.apple.iTunesCloud/InAppMessages/ResourceCache/</string>
 		<string>/Library/Trial/NamespaceDescriptors/</string>
-		<string>/Library/Trial/Treatments/511/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 	<array/>
 	<key>com.apple.developer.carplay-video</key>
 	<true/>
+	<key>com.apple.developer.declared-age-range</key>
+	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
 	<key>com.apple.developer.networking.multicast</key>

 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>
 	</array>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.tv</string>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>

```
### Games

> `/private/var/staged_system_apps/Games.app/Games`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.appstored.install-apps</key>
+	<true/>
+	<key>com.apple.appstored.private</key>
+	<true/>
+	<key>com.apple.appstored.update-apps</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<array/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

```
### Photos

> `/private/var/staged_system_apps/Photos.app/Photos`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
 	<true/>
+	<key>com.apple.security.hardened-process.no-guard-objects</key>
+	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
 	<key>com.apple.sharesheet.allow-custom-view</key>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 	<string>com.apple.biomesyncd</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>Health.Workout</string>
 		<string>ContextSync.LOI</string>
 	</array>
 	<key>com.apple.private.biome.sensorActivation</key>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.keystore.config.set.inactivity_reboot</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.escrow.create</key>

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
### nfcd

> `/usr/libexec/nfcd`

```diff

 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.accessoryd.nf-events</string>
 		<string>com.apple.stockholm.services.NFRestoreService</string>
+		<string>com.apple.stockholm.services.NFLocationService</string>
 		<string>com.apple.stockholm.services.NFRadioPowerSwitch</string>
+		<string>com.apple.stockholm.services.NFReportingService</string>
 		<string>com.apple.stockholm.services.NFUIService</string>
 		<string>com.apple.stockholm.services.NFTagProcessorService</string>
 		<string>com.apple.stockholm.services.NFStorageServer</string>

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.keystore.config.set</key>
 	<true/>
+	<key>com.apple.keystore.config.set.inactivity_reboot</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
 	<key>com.apple.keystore.device.verify</key>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.ak.auth.xpc</string>
 	</array>
 	<key>com.apple.security.ts.mobile-keybag-access</key>

```
