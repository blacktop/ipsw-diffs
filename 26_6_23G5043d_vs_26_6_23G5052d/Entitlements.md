## 🔑 Entitlements

### filesystem

### AccessorySetupUI

> `/Applications/AccessorySetupUI.app/AccessorySetupUI`

```diff

 		<string>com.apple.ProductKitService</string>
 		<string>com.apple.SharingServices</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.springboard</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.accessorysetupkit</string>

```
### SharedWebCredentialViewService

> `/Applications/SharedWebCredentialViewService.app/SharedWebCredentialViewService`

```diff

 	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.security.container-required</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXDevice</string>

```
### WebContentRestrictionsUI

> `/Applications/WebContentRestrictionsUI.app/WebContentRestrictionsUI`

```diff

 	<array>
 		<string>com.apple.springboard</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### BrowserEngineKit.Intermediary

> `/System/Library/Frameworks/BrowserEngineKit.framework/XPCServices/BrowserEngineKit.Intermediary.xpc/BrowserEngineKit.Intermediary`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.family.ageRange</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.WebContentRestrictions</string>

 	<array>
 		<string>com.apple.DocumentManagerCore.Downloads</string>
 		<string>com.apple.ciphermld</string>
+		<string>com.apple.family.ageRange.xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

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
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

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
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.posterboardservices.data-store.refreshConfigurations</key>
 	<true/>
+	<key>com.apple.private.CacheDelete</key>
+	<array>
+		<string>CLIENT_ENTITLEMENT</string>
+		<string>PURGE_ENTITLEMENT</string>
+		<string>PURGE_SPECIAL_CASE_ENTITLEMENT</string>
+	</array>
 	<key>com.apple.private.CallHistory.read</key>
 	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.sirittsd</string>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>TTSFeatureStoreEvent</string>
+	</array>
 	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
 	<true/>
 	<key>com.apple.private.homehubd</key>

 	<array>
 		<string>group.com.apple.SiriTTS</string>
 	</array>
+	<key>com.apple.private.security.storage.SiriFeatureStore</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceWillow</string>

 		<string>/Library/VoiceServices/</string>
 		<string>/Library/Caches/com.apple.HomeKit/com.apple.sirittsd/</string>
 		<string>/Library/Caches/SiriTTS/</string>
+		<string>/Library/Logs/com.apple.FeatureStore/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.cdp.statemachine</key>
+	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.maps.model-access</key>
 	<true/>
+	<key>com.apple.maps.suggestions.signalpipeline</key>
+	<true/>
 	<key>com.apple.maps.virtualgarage.vehicles</key>
 	<true/>
 	<key>com.apple.media.ringtones.read-only</key>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

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
### nfcd

> `/usr/libexec/nfcd`

```diff

 		<string>com.apple.stockholm.services.NFStorageServer</string>
 		<string>com.apple.NFCUISceneService.remote-ui</string>
 		<string>com.apple.seserviced.session</string>
+		<string>com.apple.timed.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.sts.xpcservice.client</key>
 	<true/>
+	<key>com.apple.timed</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.applesse</string>

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


