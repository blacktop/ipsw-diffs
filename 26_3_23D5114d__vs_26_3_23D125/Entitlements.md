## 🔑 Entitlements

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
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

 	<array>
 		<string>com.apple.private.alloy.dropin.communication</string>
 		<string>com.apple.private.alloy.facetime.multi</string>
+		<string>com.apple.private.alloy.gftaastest.communication</string>
 		<string>com.apple.private.alloy.phonecontinuity</string>
 		<string>com.apple.private.alloy.phonecontinuity.ping</string>
 		<string>com.apple.private.alloy.facetime.video</string>

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
### afcd

> `/usr/libexec/afcd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.mobileactivationd.spi</key>
-	<true/>
-	<key>com.apple.private.MobileActivation</key>
-	<array>
-		<string>GetActivationState</string>
-		<string>RequestActivationState</string>
-	</array>
 	<key>com.apple.private.security.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

```
### cryptexd

> `/usr/libexec/cryptexd`

```diff

 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>
 	<string>com.apple.security.cryptexd</string>
+	<key>com.apple.private.xpc.launchd.load-jetsam-properties-path</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.persist-to-boot-mode</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.storage-mounter</key>

```
