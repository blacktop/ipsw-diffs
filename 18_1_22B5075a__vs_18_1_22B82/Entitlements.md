## 🔑 Entitlements

### Camera

> `/Applications/Camera.app/Camera`

```diff

 <dict>
 	<key>CanInheritApplicationStateFromOtherProcesses</key>
 	<true/>
+	<key>NSExtension</key>
+	<dict>
+		<key>NSExtensionFileProviderDocumentGroup</key>
+		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
+		<key>NSExtensionPointIdentifier</key>
+		<string>com.apple.fileprovider-nonui</string>
+		<key>NSExtensionPrincipalClass</key>
+		<string>PhotosFileProvider</string>
+	</dict>
 	<key>application-identifier</key>
 	<string>com.apple.camera</string>
 	<key>checklessPersistentURLTranslation</key>

```
### LockScreenCamera

> `/Applications/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

 <dict>
 	<key>CanInheritApplicationStateFromOtherProcesses</key>
 	<true/>
+	<key>NSExtension</key>
+	<dict>
+		<key>NSExtensionFileProviderDocumentGroup</key>
+		<string>group.com.apple.mobileslideshow.PhotosFileProvider</string>
+		<key>NSExtensionPointIdentifier</key>
+		<string>com.apple.fileprovider-nonui</string>
+		<key>NSExtensionPrincipalClass</key>
+		<string>PhotosFileProvider</string>
+	</dict>
 	<key>application-identifier</key>
 	<string>com.apple.camera.lockscreen</string>
 	<key>checklessPersistentURLTranslation</key>

```
### Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

 	<array>
 		<string>/private/var/MobileSoftwareUpdate/</string>
 		<string>/private/var/hardware/FactoryData/</string>
+		<string>/usr/standalone/update/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```

### 🆕 GroupKitAccountNotification

> `/System/Library/Accounts/Notification/GroupKitAccountNotification.bundle/GroupKitAccountNotification`

- No entitlements *(yet)*

### 🆕 MobileDevices-0002

> `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/MobileDevices-0002`

- No entitlements *(yet)*

### 🆕 ConditionalEngineAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/ConditionalEngineAppIntentsExtension.appex/ConditionalEngineAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.conditionalengine</string>
	<key>com.apple.CoreRoutine.LocationOfInterest</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.intelligenceflow.context</key>
	<true/>
	<key>com.apple.intelligenceflow.orchestrator</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.private.appintents-bundle-absolute-paths</key>
	<array>
		<string>/System/Library/PrivateFrameworks/ConditionalEngineAppIntents.framework</string>
	</array>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.contacts</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.intelligenceflow.group-identifier</key>
	<string>com.apple.conditionalengine</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.conditionalengine</string>
	</array>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
	</array>
	<key>com.apple.private.userprofiles.read</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.conditionalengine</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siriactionsd.xpc</string>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
		<string>com.apple.intelligenceflow.orchestrator</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.routined.registration</string>
		<string>com.apple.intelligenceflow.context</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.conditionalengine</string>
	</array>
	<key>com.apple.shortcuts.stepwise-execution</key>
	<true/>
	<key>com.apple.shortcuts.trigger-editing</key>
	<true/>
	<key>com.apple.shortcuts.variable-injection</key>
	<true/>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
</dict>
</plist>

```

### 🆕 ConditionalEngineLighthouseExtension

> `/System/Library/ExtensionKit/Extensions/ConditionalEngineLighthouseExtension.appex/ConditionalEngineLighthouseExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.conditionalengine.ConditionalEngineLighthouseExtension</string>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 UrchinBridgeSettings

> `/System/Library/NanoPreferenceBundles/Applications/UrchinBridgeSettings.bundle/UrchinBridgeSettings`

- No entitlements *(yet)*

### 🆕 groupkitd

> `/System/Library/PrivateFrameworks/GroupKit.framework/groupkitd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.groupkitd</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Production</string>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.groupkit.crypto</key>
		<string>com.apple.groupkit.crypto</string>
		<key>com.apple.groupkit.limitedPeersCrypto</key>
		<string>com.apple.groupkit.limitedPeersCrypto</string>
		<key>com.apple.groupkit.limitedPeersMetadata</key>
		<string>com.apple.groupkit.limitedPeersMetadata</string>
		<key>com.apple.groupkit.metadata</key>
		<string>com.apple.groupkit.metadata</string>
	</dict>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.groupkit.allgroups</key>
	<true/>
	<key>com.apple.private.ids.messaging</key>
	<array>
		<string>com.apple.private.alloy.groupkit</string>
		<string>com.apple.private.alloy.groupkit.invite</string>
	</array>
	<key>com.apple.private.ids.messaging.urgent-priority</key>
	<array>
		<string>com.apple.private.alloy.groupkit</string>
		<string>com.apple.private.alloy.groupkit.invite</string>
	</array>
	<key>com.apple.private.ids.registration</key>
	<array>
		<string>com.apple.private.alloy.groupkit</string>
		<string>com.apple.private.alloy.groupkit.invite</string>
	</array>
	<key>com.apple.private.protectedcloudstorage.keysyncing</key>
	<true/>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/HTTPStorages/com.apple.groupkitd/</string>
		<string>/Library/com.apple.groupkitd/</string>
		<string>/Library/Caches/com.apple.groupkitd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.apsd</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.ak.auth.xpc</string>
		<string>com.apple.accountsd.accountmanager</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.rtcreportingd</string>
		<string>com.apple.protectedcloudstorage.protectedcloudkeysyncing</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.contactsd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.CloudKit</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.groupkit</string>
		<string>com.apple.groupkitd</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.addressbook</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.groupkitd</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.groupkit.crypto</string>
		<string>com.apple.groupkit.limitedPeersCrypto</string>
		<string>com.apple.groupkit.groupaccesskeys</string>
		<string>com.apple.ProtectedCloudStorage.groupkit.groupaccesskeys</string>
		<string>com.apple.groupkit.highsecuritygroupaccesskeys</string>
		<string>com.apple.ProtectedCloudStorage.groupkit.highsecuritygroupaccesskeys</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### SBRendererService

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/XPCServices/SBRendererService.xpc/SBRendererService`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.springboard.SBRendererService</string>
-	<key>com.apple.QuartzCore.global-capture</key>
-	<true/>
-	<key>com.apple.private.coreservices.canmaplsdatabase</key>
-	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
-	<key>com.apple.runningboard.assertions.frontboard</key>
-	<true/>
-	<key>com.apple.runningboard.launchprocess</key>
-	<true/>
-	<key>com.apple.runningboard.posterboard</key>
-	<true/>
-	<key>com.apple.runningboard.posterkit.host</key>
-	<true/>
-	<key>com.apple.runningboard.primitiveattribute</key>
-	<true/>
-	<key>com.apple.runningboard.trustedtarget</key>
-	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.springboard.SBRendererService/</string>

 		<string>com.apple.coremedia.decompressionsession</string>
 		<string>com.apple.coremedia.videocodecd.decompressionsession</string>
 		<string>com.apple.coremedia.videocodecd.decompressionsession.xpc</string>
-		<string>com.apple.posterboardservices.dataModel</string>
-		<string>com.apple.proactive.FaceSuggestions.xpc</string>
-		<string>com.apple.linkd.extension</string>
-		<string>com.apple.linkd.registry</string>
-		<string>com.apple.chronoservices</string>
-		<string>com.apple.extensionkitservice</string>
-		<string>com.apple.donotdisturb.service</string>
-		<string>com.apple.locationd.registration</string>
-		<string>com.apple.locationd.synchronous</string>
-		<string>com.apple.CARenderServer</string>
-		<string>com.apple.systemstatus</string>
-		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.backboard.hid.services</string>
+		<string>com.apple.backboard.display.services</string>
+		<string>com.apple.backboard.hid-services.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.ts.render-images</key>
 	<true/>
-	<key>com.apple.security.ts.tmpdir</key>
-	<string>com.apple.SBRenderer</string>
 	<key>com.apple.security.ts.xpc-service-name</key>
 	<array>
 		<string>com.apple.coremedia.decompressionsession.xpc</string>
 		<string>com.apple.coremedia.compressionsession.xpc</string>
 	</array>
-	<key>com.apple.springboard-ui.client</key>
-	<true/>
-	<key>com.apple.springboard.wallpaper.get</key>
-	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>temporary-sandbox</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.lp</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.facetime.sync</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.facetime.video</string>
 		<string>com.apple.private.alloy.facetime.audio</string>

```
