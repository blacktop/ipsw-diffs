## 🔑 Entitlements

### ShortcutsTopHitsExtension

> `/System/Library/CoreServices/ShortcutsActions.app/Extensions/ShortcutsTopHitsExtension.appex/ShortcutsTopHitsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.callhistoryd.service</key>
+	<key>com.apple.CallHistory.sync.allow</key>
 	<true/>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/ActionKit.framework</string>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 	<array>
 		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/CallHistoryDB/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.callhistoryd.service</string>
+		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.contactsd.support</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-identifiers</key>
+	<array>
+		<string>com.apple.facetime</string>
+	</array>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudDocuments</string>
+	</array>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<string>com.apple.facetime</string>
 		<string>com.apple.Photos</string>
 	</array>
+	<key>com.apple.developer.ubiquity-container-identifiers</key>
+	<array>
+		<string>com.apple.facetime</string>
+	</array>
 	<key>com.apple.duet.expertcenter.consumer</key>
 	<true/>
 	<key>com.apple.facetimemessagestored.service</key>

 	<true/>
 	<key>com.apple.private.carkit.dnd</key>
 	<true/>
+	<key>com.apple.private.clouddocs.auto-accept-share</key>
+	<true/>
+	<key>com.apple.private.clouddocs.sharing.private-interface</key>
+	<true/>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.contactsui</key>

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

 	<array>
 		<string>com.apple.default-app.phone</string>
 	</array>
+	<key>com.apple.private.librarian.container-proxy</key>
+	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/ActivationState</string>

 	<true/>
 	<key>com.apple.private.security.storage.Messages</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileDocuments</key>
+	<true/>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>cellular-plan</string>

 	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
-	<key>com.apple.callhistoryd.service</key>
-	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.chrono.controls</key>

 	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.deleteContainerContent</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>siriactionsd</string>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.security.storage.triald</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/CallHistoryDB/</string>
 		<string>/Library/Shortcuts/</string>
 		<string>/Library/Shortcuts/ssh/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.NPKCompanionAgent.Server</string>
 		<string>com.apple.NPKCompanionAgent.library</string>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.biomesyncd.sync</string>
-		<string>com.apple.callhistoryd.service</string>
 		<string>com.apple.chrono.widgetcenterconnection</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.WorkflowKit.BackgroundShortcutRunner</string>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>cellular-plan</string>

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
-	<key>com.apple.callhistoryd.service</key>
-	<true/>
 	<key>com.apple.chrono.controls</key>
 	<true/>
 	<key>com.apple.chronoservices</key>

 	<true/>
 	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>BackgroundShortcutRunner</string>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.announce/</string>
+		<string>/Library/CallHistoryDB/</string>
 		<string>/Library/Cookies/</string>
 		<string>/Library/HTTPStorages/</string>
 		<string>/Library/WebKit/com.apple.WorkflowKit.BackgroundShortcutRunner/</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.CARenderServer</string>
+		<string>com.apple.CallHistorySyncHelper</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
 		<string>com.apple.MapKit.SnapshotService</string>
 		<string>com.apple.PhotosUIPrivate.PhotosPosterProvider</string>

 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.calaccessd</string>
-		<string>com.apple.callhistoryd.service</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.contactsd</string>

```
