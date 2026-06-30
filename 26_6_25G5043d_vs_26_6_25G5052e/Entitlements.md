## 🔑 Entitlements

### filesystem

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
### Podcasts

> `/System/Applications/Podcasts.app/Contents/MacOS/Podcasts`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
+	</array>
 	<key>com.apple.private.ShazamKit</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.podcasts</string>
+	</dict>
 	<key>com.apple.private.fpsd.client</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.absd</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.cache_delete</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.jetpackassetd.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>

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
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.Passbook</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

```
### SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

```diff

 <dict>
 	<key>com.apple.ahp</key>
 	<true/>
-	<key>com.apple.private.aqua.createSession</key>
-	<true/>
-	<key>com.apple.private.logind.spi</key>
-	<true/>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
-	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
-	<true/>
 	<key>com.apple.security.smartcard</key>
 	<true/>
 </dict>

```
### SecurityAgentHelper-x86_64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-x86_64.xpc/Contents/MacOS/SecurityAgentHelper-x86_64`

```diff

 <dict>
 	<key>com.apple.ahp</key>
 	<true/>
-	<key>com.apple.private.aqua.createSession</key>
-	<true/>
-	<key>com.apple.private.logind.spi</key>
-	<true/>
 	<key>com.apple.private.security.clear-library-validation</key>
 	<true/>
-	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
-	<true/>
 	<key>com.apple.security.smartcard</key>
 	<true/>
 </dict>

```
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
 	<key>com.apple.frontboard.launchapplications</key>

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
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.coreidvd.digital-presentment.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.Carousel</string>
 		<string>com.apple.CloudKit</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.homed</string>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.cdp.telemetry</key>
+	<true/>
 	<key>com.apple.cdp.utility</key>
 	<true/>
 	<key>com.apple.developer.hardened-process</key>

```


### SystemOS

### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>

```
### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/Current/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.security.enable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
+	<key>com.apple.private.security.mutable-state-flags</key>
+	<array>
+		<string>BlockNetworkAccess</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>

```


