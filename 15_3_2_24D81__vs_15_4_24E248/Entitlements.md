## 🔑 Entitlements

### App Store

> `/System/Applications/App Store.app/Contents/MacOS/App Store`

```diff

 	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>
 	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
 	<key>com.apple.payment.amp-card-enrollment</key>
 	<true/>
 	<key>com.apple.payment.card-on-file</key>

 		<string>IAPHistory</string>
 		<string>Install</string>
 	</array>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.commerce</key>
 	<array>
 		<string>Accounts</string>

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.AMSUIPaymentViewService</string>
+		<string>com.apple.ap.promotedcontent.identifiermanager</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### BooksThumbnail

> `/System/Applications/Books.app/Contents/PlugIns/BooksThumbnail.appex/Contents/MacOS/BooksThumbnail`

```diff

 	<string>com.apple.iBooks.BooksThumbnail</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.iBooks.BooksThumbnail</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### FaceTime

> `/System/Applications/FaceTime.app/Contents/MacOS/FaceTime`

```diff

 	<string>0000000000.com.apple.FaceTime</string>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
+	<key>com.apple.assistant.dictation.prerecorded</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.bulletinboard.utilities</key>

```
### FindMy

> `/System/Applications/FindMy.app/Contents/MacOS/FindMy`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.chrono.invalidate-timelines</key>
+	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.people</key>

```
### FindMyNotificationsService

> `/System/Applications/FindMy.app/Contents/PlugIns/FindMyNotificationsService.appex/Contents/MacOS/FindMyNotificationsService`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.findmy.findmylocate.fenceservice</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>

```
### FindMyWidgetItems

> `/System/Applications/FindMy.app/Contents/PlugIns/FindMyWidgetItems.appex/Contents/MacOS/FindMyWidgetItems`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.authkit.client.internal</key>
-	<true/>
-	<key>com.apple.authkit.client.private</key>
-	<true/>
+	<key>application-identifier</key>
+	<string>com.apple.findmy</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>

 	<true/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionComplete</string>
-	<key>com.apple.developer.siri</key>
-	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
-	<key>com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService.access</key>
-	<true/>
-	<key>com.apple.icloud.findmydeviced.access</key>
-	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
+	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
 	<true/>
-	<key>com.apple.icloud.searchpartyd.ownersession</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.securelocations</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
 	<true/>
-	<key>com.apple.intents.extension.discovery</key>
-	<true/>
-	<key>com.apple.intents.uiextension.discovery</key>
+	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
-	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
-	<array>
-		<string>UniqueDeviceID</string>
-	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<key>value</key>
 		<string>com.apple.findmy</string>
 	</dict>
-	<key>com.apple.private.hsa-authentication-processing</key>
-	<true/>
-	<key>com.apple.private.network.socket-delegate</key>
-	<true/>
-	<key>com.apple.private.security.storage.FindMy</key>
-	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute</key>
-	<array>
-		<string>/tmp/findmydeviced-sandbox-violation</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_SharingDeviceAssets/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.icloud.searchparty.locationfetch.items</string>
-		<string>com.apple.icloud.findmydeviced.app-support</string>
-		<string>com.apple.hsa-authentication-server</string>
-		<string>com.apple.icloud.searchpartyd.ownersession</string>
-		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.chronoservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.dnssd.service</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.findmy.fmipcore.notbackedup</string>
-		<string>com.apple.findmy.fmfcore.notbackedup</string>
-		<string>com.apple.findmy</string>
-	</array>
-	<key>com.apple.security.network.client</key>
+	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
-	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/</string>
-	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.icloud.searchparty.locationfetch.items</string>
-		<string>com.apple.icloud.findmydeviced.app-support</string>
-		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
-		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
-		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.chronoservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.dnssd.service</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
-	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.findmy.fmipcore.notbackedup</string>
-		<string>com.apple.findmy.fmfcore.notbackedup</string>
-		<string>com.apple.findmy</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
+		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyuseragent.beaconmanager.simplebeacon</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### FindMyWidgetPeople

> `/System/Applications/FindMy.app/Contents/PlugIns/FindMyWidgetPeople.appex/Contents/MacOS/FindMyWidgetPeople`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.authkit.client.internal</key>
-	<true/>
-	<key>com.apple.authkit.client.private</key>
-	<true/>
+	<key>application-identifier</key>
+	<string>com.apple.findmy</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.findmy</string>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
 	<key>com.apple.chrono.open-urls-direct</key>

 	<true/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionComplete</string>
-	<key>com.apple.developer.siri</key>
-	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
-	<key>com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService.access</key>
-	<true/>
-	<key>com.apple.icloud.findmydeviced.access</key>
-	<true/>
-	<key>com.apple.icloud.fmfd.access</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
+	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
 	<true/>
-	<key>com.apple.icloud.searchpartyd.ownersession</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.securelocations</key>
-	<true/>
-	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
 	<true/>
-	<key>com.apple.intents.extension.discovery</key>
-	<true/>
-	<key>com.apple.intents.uiextension.discovery</key>
+	<key>com.apple.icloud.searchpartyd.ownersession</key>
 	<true/>
-	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
-	<array>
-		<string>UniqueDeviceID</string>
-	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<key>value</key>
 		<string>com.apple.findmy</string>
 	</dict>
-	<key>com.apple.private.hsa-authentication-processing</key>
-	<true/>
-	<key>com.apple.private.network.socket-delegate</key>
-	<true/>
-	<key>com.apple.private.security.storage.FindMy</key>
-	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute</key>
-	<array>
-		<string>/tmp/findmydeviced-sandbox-violation</string>
-		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_SharingDeviceAssets/</string>
-		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_SharingDeviceAssets/</string>
-	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.icloud.searchparty.locationfetch.items</string>
-		<string>com.apple.icloud.findmydeviced.app-support</string>
-		<string>com.apple.hsa-authentication-server</string>
-		<string>com.apple.icloud.searchpartyd.ownersession</string>
-		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.chronoservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.dnssd.service</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
 	</array>
-	<key>com.apple.security.exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.findmy.fmipcore.notbackedup</string>
-		<string>com.apple.findmy.fmfcore.notbackedup</string>
-		<string>com.apple.findmy</string>
-	</array>
-	<key>com.apple.security.network.client</key>
+	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
-	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Caches/</string>
-	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.icloud.searchparty.locationfetch.items</string>
-		<string>com.apple.icloud.findmydeviced.app-support</string>
-		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
-		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
-		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.chronoservices</string>
-		<string>com.apple.icloud.fmfd</string>
-		<string>com.apple.icloud.searchpartyd</string>
-		<string>com.apple.icloud.searchpartyd.securelocations</string>
-		<string>com.apple.dnssd.service</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>
-	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
-	<array>
-		<string>com.apple.findmy.fmipcore.notbackedup</string>
-		<string>com.apple.findmy.fmfcore.notbackedup</string>
-		<string>com.apple.findmy</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+		<string>com.apple.icloud.searchpartyuseragent.ownersession</string>
+		<string>com.apple.icloud.searchpartyuseragent.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyuseragent.beaconmanager.simplebeacon</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### Freeform

> `/System/Applications/Freeform.app/Contents/MacOS/Freeform`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.freeform</string>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.developer.aps-environment</key>

 	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>
 	<true/>
+	<key>com.apple.managedconfiguration.profiled.set</key>
+	<array>
+		<string>Passcode</string>
+	</array>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.hsa-authentication-processing</key>
+	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
 	<key>com.apple.private.metadata.exattrs</key>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.octagon</key>
+	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.print</key>

```
### Home

> `/System/Applications/Home.app/Contents/MacOS/Home`

```diff

 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.developer.homekit.background-mode</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	</array>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
+		<key>com.apple.homekit.camera.clips</key>
+		<string>com.apple.homekit</string>
 		<key>com.apple.homekit.events</key>
 		<string>com.apple.homekit</string>
 	</dict>

```
### GenerativePlaygroundAppIntents

> `/System/Applications/Image Playground.app/Contents/Extensions/GenerativePlaygroundAppIntents.appex/Contents/MacOS/GenerativePlaygroundAppIntents`

```diff

 	<string>com.apple.GenerativePlaygroundAppIntents</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GenerativePlaygroundAppIntents</string>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>

 		<string>com.apple.mobileslideshow</string>
 		<string>com.apple.Photos</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
+	<key>com.apple.generativeexperiences.summarization</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
-	<key>com.apple.private.appintents.attribution-override</key>
-	<true/>
-	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
-	<string>com.apple.GenerativePlaygroundApp</string>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
-	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
-	<dict>
-		<key>type</key>
-		<string>bundleID</string>
-		<key>value</key>
-		<string>com.apple.GenerativePlaygroundApp</string>
-	</dict>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 	</array>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-dispatch.internal</key>
+	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>GeneratedImageUserInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.photos.service.internal.library</key>
+	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tcc.allow-prompting</key>
-	<array>
-		<string>kTCCServiceCamera</string>
-	</array>
+	<key>com.apple.sage.summarization</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/MobileAsset/AssetsV2/</string>
-		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/Library/Application Support/com.apple.CoreSceneUnderstanding/</string>
 		<string>/Library/Application Support/com.apple.VisualGeneration/</string>
-		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
+		<string>/System/Library/PreinstalledAssetsV2/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.sage.summarization</string>
 		<string>com.apple.generativeexperiences.summarization</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.duetactivityscheduler</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.gms.availability</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
+	</array>
+	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
+	<array>
+		<string>AppleNVMeEANUC</string>
+	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.assistant.cdm</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.photos.service</string>
+		<string>com.apple.mediaanalysisd.service.public</string>
+		<string>com.apple.sage.summarization</string>
+		<string>com.apple.generativeexperiences.summarization</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>com.apple.gms.availability</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 </dict>
 </plist>
 

```
### Image Playground

> `/System/Applications/Image Playground.app/Contents/MacOS/Image Playground`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp</string>
+	<key>com.apple.VE.CVCalibration.client</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.GenerativePlaygroundApp</string>
 	<key>com.apple.appprotectiond.guard.access</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.arkit.authorization</key>
+	<array>
+		<string>worldTracking</string>
+	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>GeneratedImageUserInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

 	<true/>
 	<key>com.apple.private.photos.service.librarymanagement</key>
 	<true/>
+	<key>com.apple.private.security.arkit</key>
+	<array>
+		<string>allowImmersiveExemption</string>
+		<string>allowBackgroundPoseData</string>
+	</array>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.realitysimulation.apps</string>
+		<string>com.apple.ve.cvcalibrationd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.gms.availability</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>

 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### GenerativePlaygroundMessagesAppExtension

> `/System/Applications/Image Playground.app/Contents/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/Contents/MacOS/GenerativePlaygroundMessagesAppExtension`

```diff

 	</array>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>GeneratedImageUserInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

 	<array>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceCamera</string>
 	</array>
 	<key>com.apple.private.tcc.allow-prompting</key>
 	<array>

 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>

 		<string>com.apple.TextInput.preferences</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### Mail

> `/System/Applications/Mail.app/Contents/MacOS/Mail`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.ProactiveSummarization.feedback</key>
 	<true/>
 	<key>com.apple.ProactiveSummarization.model-input</key>

 	<true/>
 	<key>com.apple.finance.private</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.textcomposition</key>
 	<true/>
 	<key>com.apple.icloudmailagent.secret.xpc</key>

 		<string>com.apple.coreduetd</string>
 		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.dprivacyd</string>
 		<string>com.apple.CrashReporterSupportHelper</string>

 		<string>com.apple.icloudmailagent.secret.xpc</string>
 		<string>com.apple.usernoted.prefs</string>
 		<string>com.apple.businessservicesd</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
+		<string>com.apple.identityservicesd.desktop.auth</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

 	<array>
 		<string>com.apple.suggestions</string>
 		<string>com.apple.parsecd</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.mail-shared</string>
 		<string>com.apple.onetimepasscodes</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 	</array>
 	<key>com.apple.spotlight.scopes</key>
 	<array>

```
### MailQuickLookExtension

> `/System/Applications/Mail.app/Contents/PlugIns/MailQuickLookExtension.appex/Contents/MacOS/MailQuickLookExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.communicationsfilter</key>
 	<true/>
 	<key>com.apple.private.email</key>

```
### Messages

> `/System/Applications/Messages.app/Contents/MacOS/Messages`

```diff

 	</array>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>

```
### Messages Reply Extension

> `/System/Applications/Messages.app/Contents/PlugIns/Messages Reply Extension.appex/Contents/MacOS/Messages Reply Extension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.addressBook.sharingItems</key>

```
### Messages Share Extension

> `/System/Applications/Messages.app/Contents/PlugIns/Messages Share Extension.appex/Contents/MacOS/Messages Share Extension`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.addressBook.sharingItems</key>

```
### News

> `/System/Applications/News.app/Contents/MacOS/News`

```diff

 	<array>
 		<string>/System/iOSSupport/System/Library/PrivateFrameworks/NewsArticles.framework</string>
 		<string>/System/iOSSupport/System/Library/PrivateFrameworks/NewsUI2.framework</string>
+		<string>/System/iOSSupport/System/Library/PrivateFrameworks/CookingSupport.framework</string>
+	</array>
+	<key>com.apple.private.appintents-bundle-relative-paths</key>
+	<array>
+		<string>Frameworks/NewsArticles.framework</string>
+		<string>Frameworks/NewsUI2.framework</string>
+		<string>Frameworks/CookingSupport.framework</string>
 	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.aa.daemon.xpc</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### NewsTag

> `/System/Applications/News.app/Contents/PlugIns/NewsTag.appex/Contents/MacOS/NewsTag`

```diff

 	</array>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

```
### NewsToday2

> `/System/Applications/News.app/Contents/PlugIns/NewsToday2.appex/Contents/MacOS/NewsToday2`

```diff

 	</array>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.news</string>
+		<string>group.com.apple.newsd</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### NewsTodayIntents

> `/System/Applications/News.app/Contents/PlugIns/NewsTodayIntents.appex/Contents/MacOS/NewsTodayIntents`

```diff

 	</array>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### Notes

> `/System/Applications/Notes.app/Contents/MacOS/Notes`

```diff

 	</array>
 	<key>com.apple.developer.aps-environment</key>
 	<string>production</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<true/>
 	<key>com.apple.pds.clientid</key>
 	<string>Notes</string>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
 	<true/>
-	<key>com.apple.sage.summarization</key>
-	<true/>
-	<key>com.apple.sage.textcomposition</key>
-	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>com.apple.calculator</string>
 		<string>com.apple.applicationaccess</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.generativeassistantsettings</string>
+	</array>
 	<key>com.apple.security.files.user-selected.read-write</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

 		<string>com.apple.generativeexperiences.summarization</string>
 		<string>com.apple.generativeexperiences.textcomposition</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
-		<string>com.apple.sage.textcomposition</string>
 		<string>com.apple.icbaccountsd</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>

 		<string>com.apple.synapse.add-link-context-service</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.securityd.ckks</string>
-		<string>com.apple.sage.summarization</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>

```
### com.apple.Notes.QuickLookExtension

> `/System/Applications/Notes.app/Contents/PlugIns/com.apple.Notes.QuickLookExtension.appex/Contents/MacOS/com.apple.Notes.QuickLookExtension`

```diff

 <dict>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.maps</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

```
### Photos

> `/System/Applications/Photos.app/Contents/MacOS/Photos`

```diff

 		<string>com.apple.MobileAsset.MediaSupport</string>
 		<string>com.apple.MobileAsset.PhotosCuratedMusicLibraryAsset</string>
 		<string>com.apple.MobileAsset.UAF.Photos.MagicCleanup</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>group.com.apple.tipsnext</string>
 		<string>group.com.apple.Photos.PhotosFileProvider</string>
 	</array>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

 		<string>com.apple.cloudphotod</string>
 		<string>com.apple.mediastream.mstreamd</string>
 		<string>com.apple.modelmanager</string>
-		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.PhotoLibraryMigrationUtility.XPC</string>
 		<string>com.apple.routined.registration</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 	</array>

 		<string>com.apple.Desktop</string>
 		<string>com.apple.cloud.quota</string>
 		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>com.apple.gms.availability</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
+		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.photos.shareddefaults</string>
 	</array>
 	<key>com.apple.spotlight.photos.entitledattributes</key>

```
### Podcasts

> `/System/Applications/Podcasts.app/Contents/MacOS/Podcasts`

```diff

 		<string>/Library/NanoMusicSync/</string>
 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 		<string>/Media/ContentKeys/</string>
+		<string>/Media/iTunes_Control/Music/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.timesync.expositor</string>
 		<string>com.apple.timesync.manager</string>
 		<string>com.apple.timesync.ptp.manager</string>
-		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.passd.library</string>

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.absd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.chrono.avocadocontrollerconnection</string>
 		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.xpc.amsengagementd</string>
-		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>

 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.iTunes</string>
 	</array>
-	<key>com.apple.siri.koa.donate.internal</key>
-	<true/>
 	<key>com.apple.springboard.activateassistant</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### PodcastsWidget

> `/System/Applications/Podcasts.app/Contents/PlugIns/PodcastsWidget.appex/Contents/MacOS/PodcastsWidget`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.podcasts</string>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>243LU875E5.groups.com.apple.podcasts</string>

 	<array>
 		<string>243LU875E5.groups.com.apple.podcasts</string>
 	</array>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 </dict>
 </plist>
 

```
### Safari

> `/System/Applications/Safari.app/Contents/MacOS/Safari`

```diff

 	<true/>
 	<key>com.apple.developer.group-session.urlactivity</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.finance.private</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

 		<string>Safari.PageLoad</string>
 		<string>Safari.WindowProxy</string>
 		<string>Safari.MemoryFootprint</string>
+		<string>Safari.WebsitesBlockingQuit</string>
 		<string>Safari.Browsing.Assistant</string>
 	</array>
 	<key>com.apple.private.can-import-browsing-data-to-Safari</key>

 	<true/>
 	<key>com.apple.private.security.storage.cookies</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.user-intent-authority</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

 	<true/>
 	<key>com.apple.security.device.usb</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/assetsubscriptiond/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.coreduetd.knowledge</string>

 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Apple/System/Library/</string>
+		<string>/private/var/db/os_eligibility/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>
 		<string>com.apple.sociallayerd</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.coreservices.lsbestappsuggestionmanager.xpc</string>
 		<string>com.apple.suggestd.urls</string>
 		<string>com.apple.security.octagon</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.system.opendirectoryd.api</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>

 		<string>(allow authorization-right-obtain (right-name "com.apple.Safari.parental-controls"))</string>
 		<string>(allow file-read* file-write* (require-any (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2") (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2-shm") (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2-wal") (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2-lock") (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2-journal")))</string>
 		<string>(allow distributed-notification-post)</string>
+		<string>(allow user-preference-read (preference-domain "com.apple.gms.availability"))</string>
 		<string>(allow user-preference-read (preference-domain "com.apple.newscore"))</string>
 		<string>(allow user-preference-read user-preference-write (preference-domain "com.apple.news"))</string>
 		<string>(allow file-read* (home-literal "/Library/Trial"))</string>

 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.SafariBookmarksSyncAgent</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.news</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.Passwords</string>

```
### Shortcuts

> `/System/Applications/Shortcuts.app/Contents/MacOS/Shortcuts`

```diff

 		<string>group.is.workflow.my.app</string>
 		<string>pbs</string>
 	</array>
-	<key>com.apple.sharesheet.allow-custom-view</key>
-	<true/>
 	<key>com.apple.sharing.Client</key>
 	<true/>
 	<key>com.apple.shortcuts.background-running</key>

```
### QuickLookExtension

> `/System/Applications/Shortcuts.app/Contents/PlugIns/QuickLookExtension.appex/Contents/MacOS/QuickLookExtension`

```diff

 <dict>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.shortcuts.QuickLookExtension</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### ThumbnailExtension

> `/System/Applications/Shortcuts.app/Contents/PlugIns/ThumbnailExtension.appex/Contents/MacOS/ThumbnailExtension`

```diff

 <dict>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.shortcuts.ThumbnailExtension</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### Stocks

> `/System/Applications/Stocks.app/Contents/MacOS/Stocks`

```diff

 	<array>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.stocks-news</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.private.security.storage.Stocks</key>
 	<true/>

```
### StocksWidget

> `/System/Applications/Stocks.app/Contents/PlugIns/StocksWidget.appex/Contents/MacOS/StocksWidget`

```diff

 	<string>com.apple.stocks</string>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	<array>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.stocks-news</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>

 	<array>
 		<string>group.com.apple.stocks</string>
 		<string>group.com.apple.stocks-news</string>
+		<string>group.com.apple.news</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### TV

> `/System/Applications/TV.app/Contents/MacOS/TV`

```diff

 	<true/>
 	<key>com.apple.itunescloud.in-app-message-service</key>
 	<true/>
+	<key>com.apple.launchservices.receivereferrerrurl</key>
+	<true/>
 	<key>com.apple.mediaremote.allow</key>
 	<array>
 		<string>TVPairing</string>

```
### HelpViewer-Quicklook

> `/System/Applications/Tips.app/Contents/PlugIns/HelpViewer-Quicklook.appex/Contents/MacOS/HelpViewer-Quicklook`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.helpviewer.QuicklookExtension</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

```
### Screen Sharing

> `/System/Applications/Utilities/Screen Sharing.app/Contents/MacOS/Screen Sharing`

```diff

 	</array>
 	<key>com.apple.developer.copresence</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.identitylookup.classification-ui.extension-host</key>
 	<true/>
 	<key>com.apple.identitylookup.classification.extension-host</key>

```
### VoiceMemos

> `/System/Applications/VoiceMemos.app/Contents/MacOS/VoiceMemos`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.place_inference</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>

 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Application Support/com.apple.voicememos/</string>
+		<string>/Library/Logs/AppAnalytics/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### VoiceMemosIntentsExtension

> `/System/Applications/VoiceMemos.app/Contents/PlugIns/VoiceMemosIntentsExtension.appex/Contents/MacOS/VoiceMemosIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.place_inference</key>

 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<string>/private/var/mobile/Media/Recordings/</string>
 		<string>/private/var/mobile/Library/Recordings/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/AppAnalytics/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

 	<array>
 		<string>access-calls</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### WeatherAppIntents

> `/System/Applications/Weather.app/Contents/Extensions/WeatherAppIntents.appex/Contents/MacOS/WeatherAppIntents`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.weather</string>
+	<key>com.apple.CoreRoutine.LocationOfInterest</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.chronoservices</string>
+		<string>com.apple.routined.registration</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### WeatherMenu

> `/System/Applications/Weather.app/Contents/Library/LoginItems/WeatherMenu.app/Contents/MacOS/WeatherMenu`

```diff

 	<string>com.apple.weather</string>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmanagebackgroundtasks</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Weather/</string>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.newscore2</string>
 		<string>com.apple.newscore</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>1445028844</string>
 </dict>
 </plist>
 

```
### Weather

> `/System/Applications/Weather.app/Contents/MacOS/Weather`

```diff

 	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
-	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
+	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>

 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.weatherd.weatherkit</string>
 		<string>com.apple.weatherd.notifications</string>
+		<string>com.apple.weatherd.summary-strings</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.ap.promotedcontent.pcinterface</string>
 		<string>com.apple.ap.promotedcontent.mescalinterface</string>

```
### iPhone Mirroring

> `/System/Applications/iPhone Mirroring.app/Contents/MacOS/iPhone Mirroring`

```diff

 	<true/>
 	<key>com.apple.private.replicator.controller</key>
 	<true/>
+	<key>com.apple.private.rtcreportingd</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>

 		<string>com.apple.videoconference.camera</string>
 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.usernotifications.settings-vendor</string>
+		<string>com.apple.rtcreportingd</string>
 	</array>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>

```

### 🆕 GameCenterAccountAuthenticationPlugin

> `/System/Library/Accounts/Authentication/GameCenterAccountAuthenticationPlugin.bundle/Contents/MacOS/GameCenterAccountAuthenticationPlugin`

- No entitlements *(yet)*

### 🆕 PCSReadingFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/PCSReadingFlowDelegatePlugin.bundle/Contents/MacOS/PCSReadingFlowDelegatePlugin`

- No entitlements *(yet)*

### 🆕 usbaudiodxpc

> `/System/Library/Audio/Plug-Ins/HAL/usbaudiodxpc.driver/Contents/MacOS/usbaudiodxpc`

- No entitlements *(yet)*

### 🆕 IOAccessoryManager

> `/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/Contents/MacOS/IOAccessoryManager`

- No entitlements *(yet)*
### fbahelperd

> `/System/Library/CoreServices/Applications/Feedback Assistant.app/Contents/Library/LaunchServices/fbahelperd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
-	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
-	<string>com.apple.seeding</string>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.allow-nsurlsession-proxy</key>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
-	<key>com.apple.seeding.client-helper</key>
-	<true/>
 </dict>
 </plist>
 

```
### Feedback Assistant

> `/System/Library/CoreServices/Applications/Feedback Assistant.app/Contents/MacOS/Feedback Assistant`

```diff

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.ProactiveSummarization.server</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant.settings</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### AskToMessagesExtension

> `/System/Library/CoreServices/AskToMessagesHost.app/Contents/PlugIns/AskToMessagesExtension.appex/Contents/MacOS/AskToMessagesExtension`

```diff

 <dict>
 	<key>com.apple.asktod</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.messages.private.AllowAlertPresentation</key>

```
### PasswordManagerBrowserExtensionHelper

> `/System/Library/CoreServices/PasswordManagerBrowserExtensionHelper.app/Contents/MacOS/PasswordManagerBrowserExtensionHelper`

```diff

 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>
 		<string>(allow process-info-pidfdinfo)</string>
+		<string>(allow ipc-posix-sem-create ipc-posix-sem-open (ipc-posix-name "com.apple.PMBEH/Backoff"))</string>
 		<string>(allow file-read* (literal "/Library/Preferences/com.apple.networkd.plist"))</string>
 		<string>(allow file* (home-subpath "/Library/Safari/Touch Icons Cache/"))</string>
 		<string>(allow mach-issue-extension (require-all (extension-class "com.apple.webkit.extension.mach")))</string>

 </dict>
 </plist>
 
+<!-- Launch Constraints (Parent) -->
+{
+  "appl": 1,
+  "ccat": 0,
+  "comp": 1,
+  "reqs": {
+    "$or-array": [
+      {
+        "$and": {
+          "signing-identifier": "com.google.Chrome",
+          "team-identifier": "EQHXZ8M8AV"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.google.Chrome.beta",
+          "team-identifier": "EQHXZ8M8AV"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.google.Chrome.canary",
+          "team-identifier": "EQHXZ8M8AV"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.microsoft.edgemac",
+          "team-identifier": "UBF8T346G9"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.microsoft.edgemac.Beta",
+          "team-identifier": "UBF8T346G9"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.microsoft.edgemac.Dev",
+          "team-identifier": "UBF8T346G9"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.microsoft.edgemac.Canary",
+          "team-identifier": "UBF8T346G9"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "org.mozilla.firefox",
+          "team-identifier": "43AQ936H96"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "org.mozilla.firefoxdeveloperedition",
+          "team-identifier": "43AQ936H96"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "org.mozilla.nightly",
+          "team-identifier": "43AQ936H96"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "company.thebrowser.Browser",
+          "team-identifier": "S6N382Y83G"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.brave.Browser",
+          "team-identifier": "KL8N8XSYF4"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.vivaldi.Vivaldi",
+          "team-identifier": "4XF3XNRN6Y"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.operasoftware.Opera",
+          "team-identifier": "A2P9LX4JPN"
+        }
+      },
+      {
+        "$and": {
+          "signing-identifier": "com.operasoftware.OperaGX",
+          "team-identifier": "A2P9LX4JPN"
+        }
+      }
+    ]
+  },
+  "vers": 1
+}
+

```
### PeopleMessagesAskToBuy

> `/System/Library/CoreServices/PeopleMessageService.app/Contents/PlugIns/PeopleMessagesAskToBuy.appex/Contents/MacOS/PeopleMessagesAskToBuy`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### PeopleMessagesScreenTime

> `/System/Library/CoreServices/PeopleMessageService.app/Contents/PlugIns/PeopleMessagesScreenTime.appex/Contents/MacOS/PeopleMessagesScreenTime`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

```
### ProfileHelper

> `/System/Library/CoreServices/ProfileHelper.app/Contents/MacOS/ProfileHelper`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.LocalAuthentication.SaveExtractableCredential</key>
+	<true/>
 	<key>com.apple.private.managedclient.configurationprofiles.purgatory</key>
 	<true/>
+	<key>com.apple.private.managedclient.mdmclient-private</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

 		<string>/Library/Managed Preferences/com.apple.mdmclient.plist</string>
 		<string>/Library/Managed Preferences/com.apple.mcxtools.plist</string>
 		<string>/Library/Managed Preferences/com.apple.MCXDebug.plist</string>
+		<string>/Library/Preferences/com.apple.MCXDebug.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mdmclient.agent</string>
+		<string>com.apple.mdmclient.daemon</string>
 		<string>com.apple.mdmclient.agent.unrestricted</string>
 		<string>com.apple.mdmclient.daemon.unrestricted</string>
 	</array>

 	<array>
 		<string>com.apple.mdmclient</string>
 		<string>com.apple.mcxtools</string>
-		<string>com.apple.MCXDebug</string>
+		<string>/Library/Managed Preferences/com.apple.mdmclient.plist</string>
+		<string>/Library/Preferences/com.apple.MCXDebug.plist</string>
 	</array>
 </dict>
 </plist>

```
### ScreensharingAgent

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/MacOS/ScreensharingAgent`

```diff

 <dict>
 	<key>com.apple.coreaudio.app-tap</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.SkyLight.displaycontrol</key>
 	<true/>
 	<key>com.apple.private.SkyLight.screencapturedirect</key>

```
### SSInvitationAgent

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/Support/SSInvitationAgent.app/Contents/MacOS/SSInvitationAgent`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<dict>

```
### ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

 	</array>
 	<key>com.apple.SubmitDiagInfo.tower-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
+	<key>com.apple.private.MobileContainerManager.lookup</key>
+	<dict>
+		<key>appData</key>
+		<true/>
+	</dict>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	<array>
 		<string>kTCCServiceSystemPolicyAllFiles</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.allowed-complete-urgent-log-submission</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1240</string>
+		<string>1731</string>
 	</array>
 	<key>com.apple.trial.status.deployment-environment.allow</key>
 	<array>

```
### ReportSystemMemory

> `/System/Library/CoreServices/ReportSystemMemory`

```diff

 	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 </dict>

```
### ScopedBookmarkAgent

> `/System/Library/CoreServices/ScopedBookmarkAgent`

```diff

 	<true/>
 	<key>com.apple.private.netauth.quarantine.opt-out</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.scopedbookmarkagent</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyAllFiles</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.scopedbookmarkagent</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 </dict>

```
### Setup Assistant

> `/System/Library/CoreServices/Setup Assistant.app/Contents/MacOS/Setup Assistant`

```diff

 	<true/>
 	<key>com.apple.private.remotemanagement.enrollment</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
 	<key>com.apple.private.securityd.keybag-unload</key>

 	<true/>
 	<key>com.apple.private.skylight.unconditional-activation</key>
 	<true/>
+	<key>com.apple.private.softwareupdate.preferences</key>
+	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>
 	<true/>
 	<key>com.apple.private.storagekitd.destructive</key>

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.usernoted.prefs</string>
+		<string>com.apple.system.opendirectoryd.api</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mbsystemadministration.override</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.remoted</string>

```
### mbsystemadministration

> `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/mbsystemadministration`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.keystore.filevault</key>

 	<true/>
 	<key>com.apple.rootless.install</key>
 	<true/>
+	<key>com.apple.sharing.Client</key>
+	<true/>
+	<key>com.apple.sharing.Session</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>appleaccount</string>

```
### mbuseragent

> `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/mbuseragent`

```diff

 	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>

 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.usernoted.prefs</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.system.opendirectoryd.api</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### MiniLauncher

> `/System/Library/CoreServices/Setup Assistant.app/Contents/SharedSupport/MiniLauncher`

```diff

 	<true/>
 	<key>com.apple.private.mbsystemadministration</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.private.softwareupdate.preferences</key>
+	<true/>
 	<key>com.apple.private.storagekitd.info</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### Siri

> `/System/Library/CoreServices/Siri.app/Contents/MacOS/Siri`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceReminders</string>
+		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceAccessibility</string>
 		<string>kTCCServiceSystemPolicyDesktopFolder</string>

```
### SiriNCService

> `/System/Library/CoreServices/Siri.app/Contents/XPCServices/SiriNCService.xpc/Contents/MacOS/SiriNCService`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceReminders</string>
+		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceAccessibility</string>
 		<string>kTCCServiceSystemPolicyDesktopFolder</string>

 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/var/tmp/</string>
 		<string>/dev/null</string>
 		<string>/private/var/tmp/siriBC</string>
 	</array>

```
### softwareupdated

> `/System/Library/CoreServices/Software Update.app/Contents/Resources/softwareupdated`

```diff

 	<true/>
 	<key>com.apple.keystore.filevault</key>
 	<true/>
+	<key>com.apple.keystore.stash.access</key>
+	<true/>
+	<key>com.apple.osintelligence.inactivity</key>
+	<true/>
 	<key>com.apple.private.AuthorizationServices</key>
 	<array>
 		<string>system.install.apple-software.standard-user</string>

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.iokit.assertonlidclose</key>
+	<true/>
 	<key>com.apple.private.launchservices.entitledtoaccessothersessions</key>
 	<true/>
 	<key>com.apple.private.logout.forcecontinue</key>

```
### TipsQuicklook

> `/System/Library/CoreServices/TipsSpotlightHandler.app/Contents/PlugIns/TipsQuicklook.appex/Contents/MacOS/TipsQuicklook`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.tips</string>

```
### PhotosUserAccountUpdaterTool

> `/System/Library/CoreServices/UAUPlugins/PhotosUserAccountUpdaterPlugin.bundle/Contents/MacOS/PhotosUserAccountUpdaterTool`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.photos.allowlibraryupgrade</key>
+	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServicePhotos</string>
+	</array>
+</dict>
+</plist>
 

```
### IndexSettings

> `/System/Library/CoreServices/UAUPlugins/SettingsUAUPlugin.bundle/Contents/Resources/IndexSettings`

```diff

 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.transcript</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.systemsettings.extensions</string>
+	</array>
 </dict>
 </plist>
 

```
### WatchFaceMacThumbnailExtension

> `/System/Library/CoreServices/WatchFaceAlert.app/Contents/PlugIns/WatchFaceMacThumbnailExtension.appex/Contents/MacOS/WatchFaceMacThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

```
### Web App

> `/System/Library/CoreServices/Web App.app/Contents/MacOS/Web App`

```diff

 	<true/>
 	<key>com.apple.developer.group-session.urlactivity</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.finance.private</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
 	<key>com.apple.generativeexperiences.summarization</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

 		<string>Safari.PageLoad</string>
 		<string>Safari.WindowProxy</string>
 		<string>Safari.MemoryFootprint</string>
+		<string>Safari.WebsitesBlockingQuit</string>
 		<string>Safari.Browsing.Assistant</string>
 	</array>
 	<key>com.apple.private.can-import-browsing-data-to-Safari</key>

 	<true/>
 	<key>com.apple.private.security.storage.cookies</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.user-intent-authority</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

 	<true/>
 	<key>com.apple.security.device.usb</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/assetsubscriptiond/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.coreduetd.knowledge</string>

 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Apple/System/Library/</string>
+		<string>/private/var/db/os_eligibility/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.proactive.PersonalizationPortrait.SocialHighlight</string>
 		<string>com.apple.sociallayerd</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.coreservices.lsbestappsuggestionmanager.xpc</string>
 		<string>com.apple.suggestd.urls</string>
 		<string>com.apple.security.octagon</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.system.opendirectoryd.api</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.ak.signinwithapple.xpc</string>
 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>

 		<string>(allow authorization-right-obtain (right-name "com.apple.Safari.parental-controls"))</string>
 		<string>(allow file-read* file-write* (require-any (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2") (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2-shm") (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2-wal") (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2-lock") (home-literal "/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2-journal")))</string>
 		<string>(allow distributed-notification-post)</string>
+		<string>(allow user-preference-read (preference-domain "com.apple.gms.availability"))</string>
 		<string>(allow user-preference-read (preference-domain "com.apple.newscore"))</string>
 		<string>(allow user-preference-read user-preference-write (preference-domain "com.apple.news"))</string>
 		<string>(allow file-read* (home-literal "/Library/Trial"))</string>

 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.SafariBookmarksSyncAgent</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.news</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.Passwords</string>

```
### WiFiAgent

> `/System/Library/CoreServices/WiFiAgent.app/Contents/MacOS/WiFiAgent`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.wifid.known-networks</string>
 	<key>com.apple.keystore.access-keychain-keys</key>

```
### WidgetKit Simulator

> `/System/Library/CoreServices/WidgetKit Simulator.app/Contents/MacOS/WidgetKit Simulator`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.chronod.toolservices</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

```
### audioaccessoryd

> `/System/Library/CoreServices/audioaccessoryd`

```diff

 	<array>
 		<string>BluetoothAddress</string>
 		<string>SysCfg</string>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+		<string>SerialNumber</string>
+		<string>UniqueChipID</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.SkyLight.displaycontrol</key>
 	<true/>

 		<string>kTCCServiceBluetoothPeripheral</string>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceMotion</string>
+		<string>kTCCServiceBluetoothAlways</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

 		<string>com.apple.ShareAudioNotifications</string>
 		<string>com.apple.AudioAccessoryUserNotifications</string>
 		<string>com.apple.HearingModeUserNotifications</string>
+		<string>com.apple.SleepDetectionUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 		<string>com.apple.audio.AudioComponentRegistrar</string>
 		<string>com.apple.relatived.public</string>
 		<string>com.apple.healthd.server</string>
+		<string>com.apple.BTAudioHALPluginAccessories</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.private.health.feature-availability-requirement-overrides</string>
+		<string>com.apple.assistant.domain.preferences</string>
 		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

 	<true/>
 	<key>com.apple.siri.external_request</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.systemstatus.domains</key>
 	<array>
 		<string>media</string>

```
### mapspushd

> `/System/Library/CoreServices/mapspushd`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.VehicleLocation</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.Maps</string>
 	<key>com.apple.geoservices.manifestrequesttoken</key>

```
### osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.osanalytics.factoryproxysync</string>
 		<string>com.apple.osanalytics.OTATaskingAgent</string>
 		<string>com.apple.osanalytics</string>
 		<string>com.apple.softwareupdateservicesd</string>

```
### talagentd

> `/System/Library/CoreServices/talagentd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.containers</key>
 	<true/>
 	<key>com.apple.private.skylight.session_persistence</key>

```
### com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 	<true/>
 	<key>com.apple.developer.driverkit.transport.pci.bridge</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.custom-coredump-location</key>
 	<string>wifi-bcmwlan-dextcrash-%P.%T.core</string>
 	<key>com.apple.private.driverkit.driver-launch-configuration</key>

```
### com.apple.DriverKit-AppleUSBSLCOM

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleUSBSLCOM.dext/com.apple.DriverKit-AppleUSBSLCOM`

```diff

 			<key>idVendor</key>
 			<integer>4292</integer>
 		</dict>
+		<dict>
+			<key>bConfigurationValue</key>
+			<integer>1</integer>
+			<key>bInterfaceNumber</key>
+			<integer>0</integer>
+			<key>idProduct</key>
+			<integer>60016</integer>
+			<key>idVendor</key>
+			<integer>4292</integer>
+		</dict>
+		<dict>
+			<key>bConfigurationValue</key>
+			<integer>1</integer>
+			<key>bInterfaceNumber</key>
+			<integer>1</integer>
+			<key>idProduct</key>
+			<integer>60016</integer>
+			<key>idVendor</key>
+			<integer>4292</integer>
+		</dict>
 	</array>
 </dict>
 </plist>

```
### AccessibilitySettingsExtension

> `/System/Library/ExtensionKit/Extensions/AccessibilitySettingsExtension.appex/Contents/MacOS/AccessibilitySettingsExtension`

```diff

 	<array>
 		<string>com.apple.MobileAsset.TTSAXResourceModelAssets</string>
 	</array>
+	<key>com.apple.private.assistant.settings</key>
+	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
 	<key>com.apple.private.bmk.allow</key>

 	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>
 	<true/>
+	<key>com.apple.private.siri.setup</key>
+	<true/>
 	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.temporary-exception.audio-unit-host</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.assistant.settings</string>
+	</array>
 	<key>com.apple.shortcuts.background-running</key>
 	<true/>
 	<key>com.apple.shortcuts.library-read-access</key>

```
### AssetMetricsExtension

> `/System/Library/ExtensionKit/Extensions/AssetMetricsExtension.appex/Contents/MacOS/AssetMetricsExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AudiovisualThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/AudiovisualThumbnailExtension.appex/Contents/MacOS/AudiovisualThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.quicklook-thumbnail.video</key>

```
### BiomeSELFIngestor

> `/System/Library/ExtensionKit/Extensions/BiomeSELFIngestor.appex/Contents/MacOS/BiomeSELFIngestor`

```diff

 				<string>IntelligenceFlow.SearchToolTelemetry</string>
 				<string>IntelligenceFlow.ExecutorTelemetry</string>
 				<string>IntelligenceFlow.IFRequestTelemetry</string>
+				<string>IntelligenceFlow.PlanGenerationTelemetry</string>
 			</array>
 		</dict>
 	</dict>

```
### CalendarThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/CalendarThumbnailExtension.appex/Contents/MacOS/CalendarThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.security.message-filter</key>

```
### ClippingsThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ClippingsThumbnailExtension.appex/Contents/MacOS/ClippingsThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.security.message-filter</key>

```
### ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/Contents/MacOS/ComposeReviewExtension`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.AppleMediaServicesUI.ComposeReviewExtension</string>
+	</dict>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>

 	<array>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amstoold</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>com_apple_driver_FairPlayIOKitUserClient</string>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.xpc.amsaccountsd</string>
+		<string>com.apple.xpc.amstoold</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
+	</array>
 	<key>fairplay-client</key>
 	<string>1445028844</string>
 	<key>keychain-access-groups</key>

```
### ContactThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ContactThumbnailExtension.appex/Contents/MacOS/ContactThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.security.message-filter</key>

```
### DesktopSettings

> `/System/Library/ExtensionKit/Extensions/DesktopSettings.appex/Contents/MacOS/DesktopSettings`

```diff

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.dock</string>
 		<string>com.apple.spaces</string>
+		<string>com.apple.symbolichotkeys</string>
 		<string>com.apple.widgets</string>
 		<string>com.apple.WindowManager</string>
 	</array>

```
### DesktopSettingsIntents

> `/System/Library/ExtensionKit/Extensions/DesktopSettingsIntents.appex/Contents/MacOS/DesktopSettingsIntents`

```diff

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.dock</string>
 		<string>com.apple.spaces</string>
+		<string>com.apple.symbolichotkeys</string>
 		<string>com.apple.widgets</string>
 		<string>com.apple.WindowManager</string>
 	</array>

```
### DevicePropertiesExtension

> `/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/Contents/MacOS/DevicePropertiesExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ExperimentationExtension

> `/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/Contents/MacOS/ExperimentationExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### FamilySettings

> `/System/Library/ExtensionKit/Extensions/FamilySettings.appex/Contents/MacOS/FamilySettings`

```diff

 	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>development</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.familycircle.checklist</string>
-	<key>com.apple.icloud.fmfd.access</key>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>

 		<string>com.apple.AddressBook.ContactsAccountsService</string>
 		<string>com.apple.icloud.findmydeviced.app-support</string>
 		<string>com.apple.familycircle.agent</string>
-		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.publisher.service.user</string>
 		<string>com.apple.biome.compute.source.user</string>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/Contents/MacOS/FedStatsMLHostPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.FedStats.MLHostPlugin</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.FedStats.MLHostPlugin</string>
+	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
+		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>
 		<string>Device.Wireless.BluetoothGATTSession</string>
 		<string>Media.StreamingStats</string>
 		<string>App.InFocus</string>

 		<string>AeroML.Insights.PhotosSearchInsights</string>
 		<string>AeroML.LabeledData.PhotosSearchLabeledData</string>
 		<string>AeroML.DataCorrelations.PhotosSearchDataCorrelations</string>
+		<string>AeroML.RawEvent.PhotosSearchSession</string>
 		<string>CameraCapture.AutoFocusROI</string>
 		<string>Photos.Style</string>
 		<string>WalletPaymentsCommerce.FinancialInsights.RecurringSendSuggestions</string>
 		<string>Safari.Browsing.Assistant</string>
-		<string>GenerativeExperiences.TransparencyLog</string>
 		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
+		<string>GenerativeExperiences.PromptTags</string>
 		<string>AdAttributionKit.AggregatedReporting.Purchase</string>
 		<string>AdAttributionKit.AggregatedReporting.Conversion</string>
 		<string>Siri.ASR.RequestMetricsRecord</string>
 		<string>WalletPaymentsCommerce.UserProofing.Result</string>
+		<string>Autonaming.Messages.AccuracyFedStats</string>
+		<string>Safari.WebsitesBlockingQuit</string>
+		<string>LocalAuthentication.UI.Dialogs</string>
+		<string>VisualIntelligenceCamera.DetectedLabels</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.coreidvd.identity-proofing-data-sharing.xpc</string>
 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>

```
### FedStatsMLHostPluginClassA

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassA.appex/Contents/MacOS/FedStatsMLHostPluginClassA`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.FedStats.MLHostPluginClassA</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.FedStats.MLHostPluginClassA</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### FedStatsMLHostPluginClassB

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPluginClassB.appex/Contents/MacOS/FedStatsMLHostPluginClassB`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.FedStats.MLHostPluginClassB</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.FedStats.MLHostPluginClassB</string>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### FindMyIntentsExtension

> `/System/Library/ExtensionKit/Extensions/FindMyIntentsExtension.appex/Contents/MacOS/FindMyIntentsExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
+	<key>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</key>
+	<true/>
+	<key>com.apple.icloud.searchparty.ownersession.fmipitemaccess</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconsharing.access</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.intentsession</key>
+	<true/>
+	<key>com.apple.icloud.searchpartyd.ownersession</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.findmy</string>
+	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<dict>
+		<key>type</key>
+		<string>bundleID</string>
+		<key>value</key>
+		<string>com.apple.findmy</string>
+	</dict>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceAddressBook</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+	</array>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.icloud.searchparty.locationfetch.items</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchparty.beaconManager.deviceManageraccess</string>
+		<string>com.apple.icloud.searchpartyd.beaconsharingservice</string>
+	</array>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 </dict>
 </plist>
 

```
### FontThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/FontThumbnailExtension.appex/Contents/MacOS/FontThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.security.message-filter</key>

```

### 🆕 GPNonUIExtension

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/Contents/MacOS/GPNonUIExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.application-identifier</key>
	<string>com.apple.ImagePlayground.NonUIExtension</string>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.assistant.cdm.client</key>
	<true/>
	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
	<array>
		<string>com.apple.mobileslideshow</string>
		<string>com.apple.Photos</string>
	</array>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
	<true/>
	<key>com.apple.generativeexperiences.summarization</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.assertion</key>
	<true/>
	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.photos.bourgeoisie</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.person</string>
		<string>photos.face</string>
	</array>
	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/System/Library/ExtensionKit/Extensions/InlineExtension.appex/Contents/MacOS/InlineExtension</string>
	</dict>
	<key>com.apple.private.avfoundation.capture.allow</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.feedback.drafting</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>GeneratedImageUserInteraction</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>peopleSubgraph</string>
		<string>inferenceFeaturesECR</string>
		<string>personEntityRelevanceRanking</string>
		<string>entitySimilarityFeatures</string>
	</array>
	<key>com.apple.private.mediaanalysisd.datamanagement.vuindex</key>
	<true/>
	<key>com.apple.private.photos.allowassetexpunge</key>
	<true/>
	<key>com.apple.private.photos.allowlibraryupgrade</key>
	<true/>
	<key>com.apple.private.photos.service.internal.cloud</key>
	<true/>
	<key>com.apple.private.photos.service.internal.library</key>
	<true/>
	<key>com.apple.private.photos.service.librarymanagement</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.PhotosLibraries</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.sage.summarization</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.GenerativePlayground</string>
	</array>
	<key>com.apple.security.device.camera</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
		<string>/System/Library/PreinstalledAssetsV2/</string>
		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Visual/purpose_auto/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Visual/</string>
		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
	</array>
	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
	<array>
		<string>AppleNVMeEANUC</string>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXDeviceUserClient</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.photos.ImageConversionService</string>
		<string>com.apple.assistant.cdm</string>
		<string>com.apple.modelmanager</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.photoanalysisd</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.sage.summarization</string>
		<string>com.apple.generativeexperiences.summarization</string>
		<string>com.apple.generativeexperiences.availabilityService</string>
		<string>com.apple.feedbackd.centralized-feedback</string>
		<string>com.apple.extensionkitservice</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.ind.cloudfeatures</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>com.apple.gms.availability</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 	</array>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>GeneratedImageUserInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

 	</array>
 	<key>com.apple.security.device.camera</key>
 	<true/>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>

 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 GameCenterDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/GameCenterDiagnosticExtension.appex/Contents/MacOS/GameCenterDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.developer.game-center</key>
	<true/>
	<key>com.apple.private.game-center</key>
	<array>
		<string>Account</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.gamecenter</string>
	</array>
</dict>
</plist>

```
### HomeAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/HomeAppIntentsExtension.appex/Contents/MacOS/HomeAppIntentsExtension`

```diff

 	<array>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.matter.native.xpc</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.matter.native.xpc</string>

```
### ImageThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ImageThumbnailExtension.appex/Contents/MacOS/ImageThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.quicklook-thumbnail.video</key>

```

### 🆕 MessagesAnalyticsWorker

> `/System/Library/ExtensionKit/Extensions/MessagesAnalyticsWorker.appex/Contents/MacOS/MessagesAnalyticsWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.poirot.MessagesAnalyticsWorker</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Messages.Search.Event</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.feedbacklogger</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.poirot.MessagesAnalyticsWorker</string>
		<string>com.apple.poirot.poirot_tool</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.feedbacklogger</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.parsecd</string>
	</array>
</dict>
</plist>

```
### MetricsExtension

> `/System/Library/ExtensionKit/Extensions/MetricsExtension.appex/Contents/MacOS/MetricsExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 ODDIMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIMetricsExtension.appex/Contents/MacOS/ODDIMetricsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.ODDI.MetricsExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.ODDI.MetricsExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
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
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.ODDI.MetricsWorker</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.assistant.backedup</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.ODDI.MetricsWorker</string>
	</array>
</dict>
</plist>

```

### 🆕 ODDIPoirotMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/Contents/MacOS/ODDIPoirotMetricsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.siri.ODDIPoirotMetricsExtension</string>
		<string>com.apple.poirot.poirot_tool</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.feedbacklogger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### OfficeThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/OfficeThumbnailExtension.appex/Contents/MacOS/OfficeThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.security.message-filter</key>

```
### PackageThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/PackageThumbnailExtension.appex/Contents/MacOS/PackageThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.security.message-filter</key>

```

### 🆕 PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/Contents/MacOS/PrivateEvolutionPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLMLHostPlugins.PrivateEvolutionPlugin</string>
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
	<key>com.apple.generativeexperiences.availabilityService</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeExperiences.PromptTags</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
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
	<key>com.apple.private.email</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Lighthouse.Ledger.TaskCustomEvent</string>
			</array>
		</dict>
		<key>PrivateEvolutionPlugin</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Zeolite.Ledger.Embedding</string>
				<string>GenerativeExperiences.TransparencyLog</string>
				<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
				<string>App.Intent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.email.maild</string>
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.modelmanager</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
		<string>kCFPreferencesAnyApplication</string>
		<string>com.apple.gms.availability</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.modelcatalog.ajax</string>
	</array>
</dict>
</plist>

```

### 🆕 SearchToolDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolDiagnosticExtension.appex/Contents/MacOS/SearchToolDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.omniSearch.SearchToolDiagnosticExtension</string>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SearchToolExtension</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>SearchTool.Transcript</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.spotlight.search.internal</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/Contents/MacOS/SearchToolExtension`

```diff

 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.diagnosticpipeline.request</key>
+	<true/>
+	<key>com.apple.fileprovider.enumerate</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>

 	<true/>
 	<key>com.apple.photos.bourgeoisie</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/OmniSearch.framework</string>

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>SearchTool.Transcript</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 			</dict>
 		</dict>
 	</dict>

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
+	<key>com.apple.private.security.storage.SiriFeatureStore</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.spotlight.parsec</key>

 	<true/>
 	<key>com.apple.private.suggestions</key>
 	<true/>
+	<key>com.apple.private.suggestions.contacts</key>
+	<true/>
 	<key>com.apple.private.suggestions.events</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Containers/com.apple.managedcorespotlightd/EnabledIndexes</string>
+		<string>/Library/Trial/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Logs/com.apple.FeatureStore/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobileasset.autoasset</string>

 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.dmd.policy</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.managedcorespotlightd</string>
+		<string>com.apple.triald.namespace-management</string>
+		<string>com.apple.diagnosticpipeline.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.spotlightui</string>
 		<string>com.apple.OmniSearch</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.tokengeneration</string>

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.SpotlightResources.Defaults</string>
+		<string>com.apple.siri.morphun</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.personal-information.addressbook</key>
+	<true/>
 	<key>com.apple.security.personal-information.calendars</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>

 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Containers/com.apple.managedcorespotlightd/EnabledIndexes</string>
+	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>AGXDeviceUserClient</string>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.managedcorespotlightd</string>
+		<string>com.apple.diagnosticpipeline.service</string>
+	</array>
+	<key>com.apple.security.temporary-exception.sbpl</key>
+	<array>
+		<string>(allow file-issue-extension (extension-class "com.apple.managedcorespotlightd.read-write"))</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.spotlight</string>
 		<string>com.apple.OmniSearch</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.tokengeneration</string>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>337</string>
+		<string>755</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### SecurityPrivacyExtension

> `/System/Library/ExtensionKit/Extensions/SecurityPrivacyExtension.appex/Contents/MacOS/SecurityPrivacyExtension`

```diff

 	<true/>
 	<key>com.apple.developer.extension-host.systemprefsapp.privacy</key>
 	<true/>
+	<key>com.apple.hidrm</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>

 	<true/>
 	<key>com.apple.nfcd.session.se</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.CarveoutProperty</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.DiagnosticsSessionAvailability.client</key>

 	</dict>
 	<key>com.apple.private.ironwood</key>
 	<true/>
+	<key>com.apple.private.locationaccessstore.administer</key>
+	<true/>
 	<key>com.apple.private.lockdownmoded.read-write</key>
 	<true/>
 	<key>com.apple.private.logging.admin</key>

 	<true/>
 	<key>com.apple.rootless.storage.remotemanagementd</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Application Support/locationaccessstored/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.locationaccessstored.registration</string>
 		<string>com.apple.ap.adprivacyd.opt-out</string>
 		<string>com.apple.ind.cloudfeatures</string>
 	</array>

 		<string>com.apple.AdPlatforms</string>
 		<string>com.apple.communicationSafetySettings</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleProcessorTraceUserClient</string>
+	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/SystemPolicy-prefs.plist</string>

```

### 🆕 SiriMASPFLCK

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/Contents/MacOS/SiriMASPFLCK`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLMLHostPlugins.SiriMASPFLCK</string>
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
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.AppSelection.Music</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
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
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```

### 🆕 SiriMASPFLPush

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/Contents/MacOS/SiriMASPFLPush`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLMLHostPlugins.SiriMASPFLPush</string>
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
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.AppSelection.Music</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
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
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```
### SiriPreferenceExtension

> `/System/Library/ExtensionKit/Extensions/SiriPreferenceExtension.appex/Contents/MacOS/SiriPreferenceExtension`

```diff

 	<true/>
 	<key>com.apple.private.notificationcenter.preferences</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.siri.setup</key>
 	<true/>
 	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>

```
### SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/Contents/MacOS/SiriSuggestionsLightHousePlugin`

```diff

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppIntent</string>

 	<array>
 		<string>group.com.apple.siri.sirisuggestions</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.siri.inference/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sirisuggestions</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siriinferenced.remembers</string>
 		<string>com.apple.intelligenceplatform.View</string>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.ironwood.support</string>
 	</array>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sirisuggestions</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siriinferenced.remembers</string>
 		<string>com.apple.intelligenceplatform.View</string>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.mobileasset.autoasset</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant.backedup</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siriinferenced</key>
 	<true/>
+	<key>com.apple.sirisuggestions.allow</key>
+	<true/>
+	<key>com.apple.sirisuggestions.application-id</key>
+	<string>com.apple.siri.SiriSuggestionsLightHousePlugin</string>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1343</string>
+		<string>755</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### SiriTurnRestatementExtension

> `/System/Library/ExtensionKit/Extensions/SiriTurnRestatementExtension.appex/Contents/MacOS/SiriTurnRestatementExtension`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.Lighthouse.DeepThought.SiriTurnRestatementExtension</string>
+	<string>com.apple.SiriMetrics.SiriTurnRestatementExtension</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Siri.SELFProcessedEvent</string>

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SpeakerIdSamplingExtension

> `/System/Library/ExtensionKit/Extensions/SpeakerIdSamplingExtension.appex/Contents/MacOS/SpeakerIdSamplingExtension`

```diff

 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.ssr.rpisamplingservice</string>
+		<string>com.apple.symptom_diagnostics</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Storage

> `/System/Library/ExtensionKit/Extensions/Storage.appex/Contents/MacOS/Storage`

```diff

 	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyAllFiles</string>

```
### TextThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/TextThumbnailExtension.appex/Contents/MacOS/TextThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.security.message-filter</key>

```
### VisualGenerationInference

> `/System/Library/ExtensionKit/Extensions/VisualGenerationInference.appex/Contents/MacOS/VisualGenerationInference`

```diff

 	<string>com.apple.VisualGeneration.inference</string>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.ane.memoryUnwiringOptOutAccess.allow</key>
+	<true/>
 	<key>com.apple.aned.private.adapterWeight.allow</key>
 	<true/>
 	<key>com.apple.aned.private.allow</key>

```
### WebThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/Contents/MacOS/WebThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.extension-sandbox-profile</key>
 	<string>quicklook-thumbnail-secure</string>
 	<key>com.apple.private.quicklook-thumbnail.webkit</key>

```
### ZeoliteExtension

> `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/Contents/MacOS/ZeoliteExtension`

```diff

 	<array>
 		<string>Zeolite.Ledger.Embedding</string>
 	</array>
+	<key>com.apple.private.biome.read</key>
+	<array>
+		<string>App.Intent</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

 		<dict>
 			<key>Streams</key>
 			<array>
+				<string>App.Intent</string>
 				<string>GenerativeExperiences.TransparencyLog</string>
 				<string>Zeolite.Ledger.Embedding</string>
 				<string>Lighthouse.Ledger.TaskCustomEvent</string>
 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.mlhost.allowedDictionaryGroups</key>
+	<array>
+		<string>com.apple.zeolite.ZeoliteExtension</string>
+	</array>
+	<key>com.apple.private.mlhost.dictionaryRead</key>
+	<true/>
+	<key>com.apple.private.mlhost.dictionaryWrite</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mlhostd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.mlhostd.xpc</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### com.apple.mlhost.CloudWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.CloudWorker.appex/Contents/MacOS/com.apple.mlhost.CloudWorker`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.mlhost.allowedTasks</key>
+	<array>
+		<string>*</string>
+	</array>
 	<key>com.apple.private.mlhost.configRead</key>
 	<true/>
+	<key>com.apple.private.mlhost.taskDelete</key>
+	<true/>
 	<key>com.apple.private.mlhost.taskRead</key>
 	<true/>
 	<key>com.apple.private.mlhost.taskWrite</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mlhostd.xpc</string>

 	<array>
 		<string>com.apple.mlhost</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mlhostd.xpc</string>

```
### com.apple.mlhost.SampleWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.SampleWorker.appex/Contents/MacOS/com.apple.mlhost.SampleWorker`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.mlhost.allowedDictionaryGroups</key>
+	<array>
+		<string>SampleWorker</string>
+	</array>
+	<key>com.apple.private.mlhost.dictionaryDelete</key>
+	<true/>
+	<key>com.apple.private.mlhost.dictionaryRead</key>
+	<true/>
+	<key>com.apple.private.mlhost.dictionaryWrite</key>
+	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mlhostd.xpc</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```

### 🆕 AGXMetalG15X_M2

> `/System/Library/Extensions/AGXMetalG15X_M2.bundle/Contents/MacOS/AGXMetalG15X_M2`

- No entitlements *(yet)*
### apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_boot_util`

```diff

 	<true/>
 	<key>com.apple.rootless.storage.early_boot_mount</key>
 	<true/>
+	<key>com.apple.rootless.volume.Preboot</key>
+	<true/>
 	<key>com.apple.rootless.volume.Recovery</key>
 	<true/>
+	<key>com.apple.rootless.volume.iSCPreboot</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>AppleAPFSUserClient</string>
 </dict>

```
### apfs_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_stats`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.apfs.get-graft-info</key>
-	<true/>
 	<key>com.apple.private.apfs.omm.ctl</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Support/accountsd`

```diff

 	<array>
 		<string>com.apple.accounts.exists.plist</string>
 	</array>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.inactive.fullaccess</key>
 	<true/>
 	<key>com.apple.appleaccount.appleaccount-delete</key>

```
### acdiagnose

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Support/acdiagnose`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>AAACCOUNTS.com.apple.acdiagnose</string>
 	<key>com.apple.private.accounts.allaccounts</key>

```
### TrustedUIService

> `/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/TrustedUIService.xpc/Contents/MacOS/TrustedUIService`

```diff

 	</array>
 	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
 	<true/>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 </dict>
 </plist>
 

```
### com.apple.appkit.xpc.openAndSavePanelService

> `/System/Library/Frameworks/AppKit.framework/Versions/C/XPCServices/com.apple.appkit.xpc.openAndSavePanelService.xpc/Contents/MacOS/com.apple.appkit.xpc.openAndSavePanelService`

```diff

 	<dict>
 		<key>appData</key>
 		<true/>
+		<key>appGroup</key>
+		<array>
+			<string>group.com.apple.FileProvider.DomainCaching</string>
+		</array>
 		<key>pluginData</key>
 		<true/>
 	</dict>

 	<true/>
 	<key>com.apple.private.coreservices.canaccessanysharedfilelist</key>
 	<string>read-write</string>
+	<key>com.apple.private.defaults-impersonate</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.ind.client</key>

 	<true/>
 	<key>com.apple.private.security.sandbox-manager</key>
 	<true/>
+	<key>com.apple.private.security.user-intent-authority</key>
+	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>
 	<true/>
 	<key>com.apple.private.spotlight.search.internal</key>

```
### AudioConverterService

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterService.xpc/Contents/MacOS/AudioConverterService`

```diff

 <dict>
 	<key>com.apple.coreaudio.LoadConvertersInProcess</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.memory.ownership_transfer</key>
 	<true/>
 </dict>

```
### managedcorespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/managedcorespotlightd`

```diff

 		<key>appData</key>
 		<true/>
 	</dict>
+	<key>com.apple.private.corespotlight.skgupdater</key>
+	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.roots-installed-read-only</key>

 	<array>
 		<string>com.apple.searchd</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.spotlightknowledged</string>
+	</array>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>platform-application</key>

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<true/>
 	<key>com.apple.mobileassetd.v2</key>
 	<true/>
+	<key>com.apple.private.ciphermld.allow</key>
+	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</string>
+		<string>com.apple.ciphermld</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.linkd.registry</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### FamilyControlsAgent

> `/System/Library/Frameworks/FamilyControls.framework/Versions/A/FamilyControlsAgent`

```diff

 	<string>serverPreferred</string>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.fileprovider.extension-host</key>

 	<true/>
 	<key>com.apple.private.vfs.skip-mtime-updates</key>
 	<true/>
+	<key>com.apple.private.vfs.support-long-paths</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.fileprovider</key>
 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.FileProvider.DomainCaching</string>
+	</array>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
 	<key>com.apple.security.files.bookmarks.app-scope</key>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Finance/</string>
+		<string>/Library/FinanceBackup/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### GroupSessionService

> `/System/Library/Frameworks/GroupActivities.framework/Versions/A/XPCServices/GroupSessionService.xpc/Contents/MacOS/GroupSessionService`

```diff

 <dict>
 	<key>com.apple.StatusKit.presence.clientID</key>
 	<string>groupsessionservice</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.safari.groupactivities</string>

```
### intents_helper

> `/System/Library/Frameworks/Intents.framework/XPCServices/intents_helper.xpc/Contents/MacOS/intents_helper`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### jsc

> `/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
 	<true/>
 	<key>com.apple.private.pac.exception</key>

```
### coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.coreauthd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DialogAnalyticsWriter</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>LocalAuthentication.UI.Dialogs</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.lasecureio.remote</key>
 	<true/>
 	<key>com.apple.private.network.intcoproc.restricted</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.backlightd</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleCredentialManagerUserClient</string>
+		<string>AppleKeyStoreUserClient</string>
 	</array>
 	<key>com.apple.sharing.DeviceDiscovery</key>
 	<true/>

```

### 🆕 managedsettingsdiagnoticstool

> `/System/Library/Frameworks/ManagedSettings.framework/managedsettingsdiagnoticstool`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.team-identifier</key>
	<string>Apple</string>
	<key>com.apple.private.managed-settings.diagnostics</key>
	<true/>
</dict>
</plist>

<!-- Launch Constraints (Parent) -->
{
  "appl": 1,
  "ccat": 0,
  "comp": 1,
  "reqs": {
    "$or-array": [
      {
        "$and": {
          "apple-internal": true
        }
      },
      {
        "$and": {
          "$or": {
            "on-authorized-authapfs-volume": true,
            "on-system-volume": true
          },
          "launch-type": 2,
          "signing-identifier": "com.apple.sysdiagnosed",
          "validation-category": 1
        }
      }
    ]
  },
  "vers": 1
}

```
### RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/Versions/A/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
+	<true/>
 	<key>com.apple.private.coreaudio.viewInterruptorName.allow</key>
 	<true/>
 	<key>com.apple.private.coremedia.pidinheritance.allow</key>

```
### com.apple.gpusw.ParavirtualizedGraphicsGPUTask

> `/System/Library/Frameworks/ParavirtualizedGraphics.framework/Versions/A/XPCServices/com.apple.gpusw.ParavirtualizedGraphicsGPUTask.xpc/Contents/MacOS/com.apple.gpusw.ParavirtualizedGraphicsGPUTask`

```diff

 <dict>
 	<key>com.apple.private.ggdsw.GPUProcessProtectedContent</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/System/Library/Frameworks/ParavirtualizedGraphics.framework</string>
+		<string>/AppleInternal/Library/Frameworks/ParavirtualizedGraphics.framework</string>
+	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>IOGPUDeviceUserClient</string>
+		<string>IOSurfaceRootUserClient</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.PassKit.PaymentAuthorizationUIExtension

> `/System/Library/Frameworks/PassKit.framework/PlugIns/com.apple.PassKit.PaymentAuthorizationUIExtension.appex/Contents/MacOS/com.apple.PassKit.PaymentAuthorizationUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.CallerPID</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

```
### OFD_Preview

> `/System/Library/Frameworks/Quartz.framework/Versions/A/Frameworks/ImageKit.framework/Versions/A/PlugIns/OFD_Preview.appex/Contents/MacOS/OFD_Preview`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

```
### OFD_Thumbnail

> `/System/Library/Frameworks/Quartz.framework/Versions/A/Frameworks/ImageKit.framework/Versions/A/PlugIns/OFD_Thumbnail.appex/Contents/MacOS/OFD_Thumbnail`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

```
### qlmanage

> `/System/Library/Frameworks/QuickLook.framework/Versions/A/Resources/qlmanage.app/Contents/MacOS/qlmanage`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.dmd.policy</key>
-	<true/>
-	<key>com.apple.private.screen-time</key>
-	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.security.cs.disable-library-validation</key>
 	<true/>
 	<key>com.apple.security.get-task-allow</key>

```
### quicklookd

> `/System/Library/Frameworks/QuickLook.framework/Versions/A/Resources/quicklookd.app/Contents/MacOS/quicklookd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyAllFiles</string>

```
### QuickLookSatellite

> `/System/Library/Frameworks/QuickLook.framework/Versions/A/XPCServices/QuickLookSatellite.xpc/Contents/MacOS/QuickLookSatellite`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### com.apple.quicklook.ThumbnailsAgent

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent`

```diff

 	<string>com.apple.quicklook.ThumbnailsAgent</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.quicklook.ThumbnailsAgent</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>

```
### QLPreviewGenerationExtension

> `/System/Library/Frameworks/QuickLookUI.framework/Versions/A/PlugIns/QLPreviewGenerationExtension.appex/Contents/MacOS/QLPreviewGenerationExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 </dict>

```
### QuickLookUIHelper

> `/System/Library/Frameworks/QuickLookUI.framework/Versions/A/Resources/QuickLookUIHelper.app/Contents/MacOS/QuickLookUIHelper`

```diff

 <dict>
 	<key>com.apple.FaceTime.NoPrompt</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.maps</key>
 	<true/>
 	<key>com.apple.private.dmd.policy</key>

```
### QuickLookUIService

> `/System/Library/Frameworks/QuickLookUI.framework/Versions/A/XPCServices/QuickLookUIService.xpc/Contents/MacOS/QuickLookUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.maps</key>
 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>

```
### SceneKitQLPreviewExtension

> `/System/Library/Frameworks/SceneKit.framework/PlugIns/SceneKitQLPreviewExtension.appex/Contents/MacOS/SceneKitQLPreviewExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.quickLook.externalResources</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### SceneKitQLThumbnailExtension

> `/System/Library/Frameworks/SceneKit.framework/PlugIns/SceneKitQLThumbnailExtension.appex/Contents/MacOS/SceneKitQLThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.quickLook.externalResources</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/Versions/A/PlugIns/ScreenTimeWebExtension.appex/Contents/MacOS/ScreenTimeWebExtension`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>App.WebUsage</string>
+	</array>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 </dict>
 </plist>
 

```
### SecurityAgent

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/MacOS/SecurityAgent`

```diff

 	<true/>
 	<key>com.apple.private.aqua.createSession</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.SecurityAgent</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DialogAnalyticsWriter</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>LocalAuthentication.UI.Dialogs</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.logind.spi</key>
 	<true/>
 	<key>com.apple.private.opendirectoryd.BootstrapToken</key>

 	<true/>
 	<key>com.apple.rootless.storage.ExtensibleSSO</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 	<key>com.apple.security.smartcard</key>
 	<true/>
 	<key>com.apple.systemstatus.domains</key>

```
### storekitagent

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitagent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.appstored.octane</key>

```

### 🆕 get-network-info

> `/System/Library/Frameworks/SystemConfiguration.framework/Versions/A/Resources/get-network-info`

- No entitlements *(yet)*
### VTDecoderXPCService

> `/System/Library/Frameworks/VideoToolbox.framework/Versions/A/XPCServices/VTDecoderXPCService.xpc/Contents/MacOS/VTDecoderXPCService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.codec-registry</key>
 	<true/>
 	<key>com.apple.private.proreshw</key>

```
### VTDecoderXPCServiceZonto

> `/System/Library/Frameworks/VideoToolbox.framework/Versions/A/XPCServices/VTDecoderXPCServiceZonto.xpc/Contents/MacOS/VTDecoderXPCServiceZonto`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.codec-registry</key>
 	<true/>
 	<key>com.apple.private.proreshw</key>

```
### com.apple.Virtualization.PluginLoader

> `/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.PluginLoader.xpc/Contents/MacOS/com.apple.Virtualization.PluginLoader`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.domain-extension</key>
-	<true/>
 	<key>com.apple.private.virtualization.plugin-loader</key>
 	<true/>
 	<key>com.apple.private.virtualization.plugin-loader-service</key>
 	<true/>
+	<key>com.apple.private.xpc.domain-extension</key>
+	<true/>
 </dict>
 </plist>
 

```
### com.apple.Virtualization.VirtualMachine

> `/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine`

```diff

 	<true/>
 	<key>com.apple.private.virtualization.plugin-loader</key>
 	<true/>
+	<key>com.apple.private.xpc.domain-extension</key>
+	<true/>
 	<key>com.apple.security.hypervisor</key>
 	<true/>
 	<key>com.apple.usb.hostcontrollerinterface</key>

```
### com.apple.WebKit.GPU

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.GPU.xpc/Contents/MacOS/com.apple.WebKit.GPU`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-vorbis-decode</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.videotoolbox.client-sandboxed-decoder</key>
 	<true/>
 	<key>com.apple.mediaremote.external-artwork-validation</key>

```
### com.apple.WebKit.Networking

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.Networking.xpc/Contents/MacOS/com.apple.WebKit.Networking`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.WebContentRestrictions</string>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.CaptivePortal.xpc/Contents/MacOS/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-vorbis-decode</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
 	<true/>
 	<key>com.apple.developer.videotoolbox.client-sandboxed-decoder</key>

 		<string>com.apple.accessibility.cache.vot</string>
 		<string>com.apple.accessibility.cache.zoom</string>
 		<string>com.apple.accessibility.cache.*</string>
+		<string>com.apple.system.DirectoryService.InvalidateCache*</string>
 		<string>com.apple.coreservices.launchservices.session.*</string>
 		<string>user.uid.501.syslog.*</string>
 		<string>com.apple.sessionagent.screenLockUIIsHidden</string>

 		<string>com.apple.sessionagent.shieldWindowIsShowing</string>
 		<string>com.apple.sessionagent.shieldWindowLowered</string>
 		<string>com.apple.sessionagent.shieldWindowRaised</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache.group</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache.host</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache.service</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache.user</string>
 		<string>__ABDataBaseChangedByOtherProcessNotification</string>
 		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
 		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>

 		<string>com.apple.CFNetwork.har-capture-update</string>
 		<string>com.apple.CFPreferences._domainsChangedExternally</string>
 		<string>com.apple.LaunchServices.database</string>
+		<string>com.apple.TTS.synthProviderVoicesDidUpdate</string>
 		<string>com.apple.UIKit.LoggingPreferences</string>
 		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
 		<string>com.apple.WebKit.deleteAllCode</string>

 		<string>com.apple.WebKit.showGraphicsLayerTree</string>
 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>
+		<string>com.apple.WebKit.showLegacyFlexReasons</string>
 		<string>com.apple.WebKit.showMemoryCache</string>
 		<string>com.apple.WebKit.showPaintOrderTree</string>
 		<string>com.apple.WebKit.showRenderTree</string>

 		<string>org.WebKit.memoryWarning</string>
 		<string>org.WebKit.memoryWarning.begin</string>
 		<string>org.WebKit.memoryWarning.end</string>
+		<string>org.WebKit.testNotification</string>
 	</array>
 	<key>com.apple.private.gpu-restricted</key>
 	<true/>

 		<string>BlockIOKitInWebContentSandbox</string>
 		<string>local:WebContentProcessLaunched</string>
 		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>BlockOpenDirectoryInWebContentSandbox</string>
+		<string>BlockMobileAssetInWebContentSandbox</string>
+		<string>BlockMobileGestaltInWebContentSandbox</string>
+		<string>BlockWebInspectorInWebContentSandbox</string>
+		<string>BlockIconServicesInWebContentSandbox</string>
+		<string>BlockFontServiceInWebContentSandbox</string>
 	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>

 		<string>local:WebContentProcessLaunched</string>
 		<string>EnableQuickLookSandboxResources</string>
 		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>BlockOpenDirectoryInWebContentSandbox</string>
+		<string>BlockMobileAssetInWebContentSandbox</string>
+		<string>BlockMobileGestaltInWebContentSandbox</string>
+		<string>BlockWebInspectorInWebContentSandbox</string>
+		<string>BlockIconServicesInWebContentSandbox</string>
+		<string>BlockFontServiceInWebContentSandbox</string>
 	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>

```
### com.apple.WebKit.WebContent

> `/System/Library/Frameworks/WebKit.framework/Versions/A/XPCServices/com.apple.WebKit.WebContent.xpc/Contents/MacOS/com.apple.WebKit.WebContent`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-vorbis-decode</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
 	<true/>
 	<key>com.apple.developer.videotoolbox.client-sandboxed-decoder</key>

 		<string>com.apple.accessibility.cache.vot</string>
 		<string>com.apple.accessibility.cache.zoom</string>
 		<string>com.apple.accessibility.cache.*</string>
+		<string>com.apple.system.DirectoryService.InvalidateCache*</string>
 		<string>com.apple.coreservices.launchservices.session.*</string>
 		<string>user.uid.501.syslog.*</string>
 		<string>com.apple.sessionagent.screenLockUIIsHidden</string>

 		<string>com.apple.sessionagent.shieldWindowIsShowing</string>
 		<string>com.apple.sessionagent.shieldWindowLowered</string>
 		<string>com.apple.sessionagent.shieldWindowRaised</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache.group</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache.host</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache.service</string>
-		<string>com.apple.system.DirectoryService.InvalidateCache.user</string>
 		<string>__ABDataBaseChangedByOtherProcessNotification</string>
 		<string>_AXNotification_AXSAppValidatingTestingPreference</string>
 		<string>_AXNotification_IsAXValidationRunnerCollectingValidations</string>

 		<string>com.apple.CFNetwork.har-capture-update</string>
 		<string>com.apple.CFPreferences._domainsChangedExternally</string>
 		<string>com.apple.LaunchServices.database</string>
+		<string>com.apple.TTS.synthProviderVoicesDidUpdate</string>
 		<string>com.apple.UIKit.LoggingPreferences</string>
 		<string>com.apple.WebKit.LibraryPathDiagnostics</string>
 		<string>com.apple.WebKit.deleteAllCode</string>

 		<string>com.apple.WebKit.showGraphicsLayerTree</string>
 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>
+		<string>com.apple.WebKit.showLegacyFlexReasons</string>
 		<string>com.apple.WebKit.showMemoryCache</string>
 		<string>com.apple.WebKit.showPaintOrderTree</string>
 		<string>com.apple.WebKit.showRenderTree</string>

 		<string>org.WebKit.memoryWarning</string>
 		<string>org.WebKit.memoryWarning.begin</string>
 		<string>org.WebKit.memoryWarning.end</string>
+		<string>org.WebKit.testNotification</string>
 	</array>
 	<key>com.apple.private.gpu-restricted</key>
 	<true/>

 		<string>BlockIOKitInWebContentSandbox</string>
 		<string>local:WebContentProcessLaunched</string>
 		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>BlockOpenDirectoryInWebContentSandbox</string>
+		<string>BlockMobileAssetInWebContentSandbox</string>
+		<string>BlockMobileGestaltInWebContentSandbox</string>
+		<string>BlockWebInspectorInWebContentSandbox</string>
+		<string>BlockIconServicesInWebContentSandbox</string>
+		<string>BlockFontServiceInWebContentSandbox</string>
 	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>

 		<string>local:WebContentProcessLaunched</string>
 		<string>EnableQuickLookSandboxResources</string>
 		<string>ParentProcessCanEnableQuickLookStateFlag</string>
+		<string>BlockOpenDirectoryInWebContentSandbox</string>
+		<string>BlockMobileAssetInWebContentSandbox</string>
+		<string>BlockMobileGestaltInWebContentSandbox</string>
+		<string>BlockWebInspectorInWebContentSandbox</string>
+		<string>BlockIconServicesInWebContentSandbox</string>
+		<string>BlockFontServiceInWebContentSandbox</string>
 	</array>
 	<key>com.apple.private.verified-jit</key>
 	<true/>

```

### 🆕 HIDRMServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/HIDRMServiceFilter.plugin/Contents/MacOS/HIDRMServiceFilter`

- No entitlements *(yet)*

### 🆕 HIDRMSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/HIDRMSessionFilter.plugin/Contents/MacOS/HIDRMSessionFilter`

- No entitlements *(yet)*
### com.apple.accounts.dom

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/XPCServices/com.apple.accounts.dom.xpc/Contents/MacOS/com.apple.accounts.dom`

```diff

 <dict>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>AAACCOUNTS.com.apple.accounts.dom</string>
 	<key>com.apple.chronoservices</key>

 	<array>
 		<string>group.com.apple.calendar</string>
 		<string>group.com.apple.notes</string>
+		<string>group.com.apple.freeform</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### AppSSOAgent

> `/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSOAgent.app/Contents/MacOS/AppSSOAgent`

```diff

 	<true/>
 	<key>com.apple.authorization.extract-password</key>
 	<true/>
+	<key>com.apple.devicecheck.private.device</key>
+	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>
 	<true/>
 	<key>com.apple.keystore.device.smart-card</key>

 	<array>
 		<string>group.com.apple.KerberosExtension</string>
 	</array>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.PlatformSSO.notifications</string>

 	<array>
 		<string>com.apple.PlatformSSO</string>
 		<string>com.apple.PlatformSSO.auth</string>
+		<string>appattest-device</string>
 	</array>
 </dict>
 </plist>

```
### appstorecomponentsd

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
+	<key>com.apple.payment.amp-card-enrollment</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 		<string>PurchaseHistory</string>
 		<string>IAPHistory</string>
 	</array>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.commerce</key>
 	<array>
 		<string>Accounts</string>

```
### appstoreagent

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstoreagent`

```diff

 		<string>kTCCServiceSystemPolicyDesktopFolder</string>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 	</array>
+	<key>com.apple.private.uninstalld.client</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.AppStore</string>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.nsurlsession.impersonate</key>
+	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
 	<key>com.apple.private.security.app-install</key>

```
### airport

> `/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.driverkit.driver-access</key>
 	<array>
 		<string>com.apple.private.wifi.driverkit</string>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/Resources/amsaccountsd`

```diff

 	<array>
 		<string>monitor</string>
 	</array>
+	<key>com.apple.companion-authentication.store-purchase</key>
+	<true/>
 	<key>com.apple.coreidvd.spi</key>
 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
-	<key>com.apple.private.bmk.allow</key>
+	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
 	<key>com.apple.private.cfnetwork.har-capture-amp</key>
 	<true/>

 		<string>kTCCServiceWillow</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.ts</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.AppleMediaServicesUI.engagement.notifications</string>
 		<string>com.apple.AppleMediaServicesUI.engagement.notifications.macOS</string>
 		<string>com.apple.AppStore</string>
+		<string>com.apple.iCloudSettingsNotification</string>
 		<string>com.apple.Music</string>
 		<string>com.apple.tv</string>
 		<string>com.apple.Fitness</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.amsondevicestoraged.xpc</string>
+		<string>com.apple.companiond.xpc</string>
 		<string>com.apple.locationd.registration</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.asd.scoring</string>

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.passd.library</string>
+		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.xpc.amsserverdatacacheservice</string>
 		<string>com.apple.xpc.amsengagementd</string>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.amsaccountsd</string>
+		<string>com.apple.OnDeviceStorage</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>com_apple_driver_FairPlayIOKitUserClient</string>

```
### amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.amsondevicestoraged</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.ts</key>
+	<true/>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.amsengagementd.analytics</string>

 	<array>
 		<string>com.apple.AppStore</string>
 		<string>com.apple.Fitness</string>
+		<string>com.apple.iCloudSettingsNotification</string>
 		<string>com.apple.iBooks</string>
 		<string>com.apple.Music</string>
 		<string>com.apple.news</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.amsondevicestoraged.xpc</string>
 		<string>com.apple.apsd</string>
+		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.mobileactivationd</string>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.engagementd</string>
+		<string>com.apple.OnDeviceStorage</string>
 	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>

```
### AMSUIPaymentViewService_macOS

> `/System/Library/PrivateFrameworks/AppleMediaServicesUIPaymentSheets.framework/Versions/A/XPCServices/AMSUIPaymentViewService_macOS.xpc/Contents/MacOS/AMSUIPaymentViewService_macOS`

```diff

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 </dict>
 </plist>
 

```
### ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/Contents/MacOS/ANECompilerService`

```diff

 <dict>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.coreml.decypt_allowed</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

```
### apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

```
### RAQLPreviewExtension

> `/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/RAQLPreviewExtension.appex/Contents/MacOS/RAQLPreviewExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

```
### RAQLThumbnailExtension

> `/System/Library/PrivateFrameworks/AssetViewer.framework/PlugIns/RAQLThumbnailExtension.appex/Contents/MacOS/RAQLThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

```
### RAQL-Inline-Service

> `/System/Library/PrivateFrameworks/AssetViewer.framework/Versions/A/XPCServices/RAQL-Inline-Service.xpc/Contents/MacOS/RAQL-Inline-Service`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+</dict>
+</plist>
 

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistant_service`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>_Cryptex</key>
 	<string>com.apple.system.app</string>
 	<key>adi-client</key>

 		<string>Siri.PostSiriEngagement</string>
 		<string>SiriPrivateLearningSELFEvent</string>
 		<string>SiriIntentEvents</string>
+		<string>App.Intent</string>
 	</array>
 	<key>com.apple.private.calendar.allow-integrations</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.siri.findmy</string>
+		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.siri.inference</string>
 	</array>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.siri.findmy</string>
+		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.notes</string>
 		<string>group.com.apple.siri.inference</string>
 	</array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.orchestration.configuration</string>
 		<string>com.apple.siri.orchestration.intelligencesession</string>
 		<string>com.apple.siri.location</string>
 		<string>com.apple.siri.pommes_search_xpc_service</string>

 		<string>com.apple.itunescloud.contenttaste</string>
 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.extensionkitservice</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.location</key>
 	<true/>
+	<key>com.apple.siri.orchestration.configuration</key>
+	<true/>
 	<key>com.apple.siri.orchestration.intelligencesession</key>
 	<true/>
 	<key>com.apple.siri.pommes_search_xpc_service</key>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

 		<string>Media.NowPlaying</string>
 		<string>Notification</string>
 		<string>Notification.Usage</string>
+		<string>Photos.Delete</string>
+		<string>Photos.Edit</string>
+		<string>Photos.Engagement</string>
+		<string>Photos.Favorite</string>
+		<string>Photos.Memories.Shared</string>
+		<string>Photos.Memories.Viewed</string>
+		<string>Photos.Picker</string>
+		<string>Photos.Search</string>
+		<string>Photos.Share</string>
 		<string>Siri.Metrics.OnDeviceDigestExperimentMetrics</string>
 		<string>Siri.Metrics.OnDeviceDigestSegmentsCohorts</string>
 		<string>Siri.Metrics.OnDeviceDigestUsageMetrics</string>

 	<true/>
 	<key>com.apple.private.networkserviceproxy</key>
 	<true/>
+	<key>com.apple.private.power.notifications</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.security.no-container</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
+		<string>group.com.apple.assistant.shared</string>
+		<string>group.com.apple.siri.recorded-audio</string>
 		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.weather</string>
 	</array>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.assistant.shared</string>
 		<string>group.com.apple.siri.referenceResolution</string>
 		<string>group.com.apple.weather</string>
 	</array>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/Support/akd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
 	<key>com.apple.appletv.pbs.user-presentation-service-access</key>

 	</array>
 	<key>com.apple.private.authentication-services.internal-authorization-requests</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.managedconfiguration.mdmdservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.AppStoreComponents</string>
+		<string>com.apple.aaa.serverbackoff</string>
+		<string>com.apple.AuthKit.AgeRangeSettingsCache</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.aaa.serverbackoff</string>
+	</array>
 	<key>com.apple.security.ts.ipc-posix-sem</key>
 	<true/>
 	<key>com.apple.security.ts.ipc-posix-shm</key>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>
+		<string>ichat</string>
 		<string>com.apple.akd</string>
 		<string>com.apple.cfnetwork</string>
 		<string>com.apple.akd.pcsauth</string>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.applicationaccess</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.intelligenceplatform</string>
 		<string>com.apple.suggestions</string>

```
### bookdatastored

> `/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.iBooks.BookDataStoreService</string>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
 	<key>com.apple.developer.icloud-container-environment</key>

```
### businessservicesd

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd`

```diff

 		<string>spi</string>
 		<string>sim-authentication</string>
 	</array>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.businessservicesd</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Development</string>
 	<key>com.apple.developer.icloud-services</key>

```
### SpotlightEventPreview

> `/System/Library/PrivateFrameworks/CalendarUI.framework/Versions/A/PlugIns/SpotlightEventPreview.appex/Contents/MacOS/SpotlightEventPreview`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCalendar</string>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	<array>
 		<string>com.apple.private.alloy.widgets</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>DuetActivitySchedulerWidgetRefresh</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<dict>
+					<key>Widgets.Refresh</key>
+					<dict>
+						<key>mode</key>
+						<string>read-write</string>
+					</dict>
+					<key>Widgets.Viewed</key>
+					<dict>
+						<key>mode</key>
+						<string>read-only</string>
+					</dict>
+				</dict>
+			</array>
+		</dict>
+		<key>LNActivityProvider</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>App.Intents.Transcript</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.batterydataprecise</key>
 	<true/>
 	<key>com.apple.private.logging.admin</key>

 		<string>com.apple.replicatorservices</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### CloudTelemetryService

> `/System/Library/PrivateFrameworks/CloudTelemetry.framework/Versions/A/XPCServices/CloudTelemetryService.xpc/Contents/MacOS/CloudTelemetryService`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.osanalytics.defaults.allow</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 </dict>

```
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.assistant_cdmd</string>
-	<key>com.apple.TapToRadarKit.service-access</key>
-	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

```
### accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

 	<string>com.apple.accessoryd</string>
 	<key>com.apple.USBCEntitlement</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.driver.AppleAuthCP.user-access</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access-device</key>
 	<true/>
 	<key>com.apple.iokit.IOPort.user-access</key>

```

### 🆕 ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/A/XPCServices/ACCHWComponentAuthService.xpc/Contents/MacOS/ACCHWComponentAuthService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.driver.AppleAuthCP.user-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueChipID</string>
		<string>BootManifestHash</string>
		<string>RoswellChipID</string>
		<string>BatterySerialNumber</string>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
		<string>UniqueDeviceIDData</string>
		<string>ScreenSerialNumber</string>
		<string>TopModuleAuthChipID</string>
	</array>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleAuthCPUserClient</string>
	</array>
</dict>
</plist>

```
### analyticsagent

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsagent`

```diff

 	<true/>
 	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
 	<true/>
+	<key>com.apple.private.osanalytics.defaults.allow</key>
+	<true/>
 </dict>
 </plist>
 

```
### analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

 	<array>
 		<string>Device.ScreenLocked</string>
 		<string>OSAnalytics.CA.HighEngagementDevices</string>
+		<string>Trial.Experiment.NamespaceUpdates</string>
 	</array>
 	<key>com.apple.private.corewifi</key>
 	<true/>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/XPCServices/com.apple.siri.embeddedspeech.xpc/Contents/MacOS/com.apple.siri.embeddedspeech`

```diff

 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/tmp/com.apple.siri-distributed-evaluation/</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/PersonalDeviceVolumes/</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/ASRAssetOverrides/</string>

```
### HapticsQLPreviewExtension

> `/System/Library/PrivateFrameworks/CoreHapticsTools.framework/PlugIns/HapticsQLPreviewExtension.appex/Contents/MacOS/HapticsQLPreviewExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.quickLook.externalResources</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>

```
### HapticsQLThumbnailExtension

> `/System/Library/PrivateFrameworks/CoreHapticsTools.framework/PlugIns/HapticsQLThumbnailExtension.appex/Contents/MacOS/HapticsQLThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<true/>
 	<key>com.apple.datadetectors.source-write.system</key>
 	<true/>
-	<key>com.apple.developer.networking.multipath</key>
-	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.da</string>
 		<string>com.apple.UnifiedAssetFramework</string>

```
### CoreSpeechXPC

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/XPCServices/CoreSpeechXPC.xpc/Contents/MacOS/CoreSpeechXPC`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.corespeech.cat.xpc</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.hid.system.user-access-fast-path</key>
 	<true/>
 	<key>com.apple.homepodaccessorysettings.client</key>
 	<true/>
+	<key>com.apple.intelligenceflow.context</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

 		<string>Siri.SelfTriggerSuppression</string>
 		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
 		<string>Siri.ASR.RequestMetricsRecord</string>
+		<string>Siri.ASR.ContextualReplayRecord</string>
 	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.corespeech.xpc.remote</key>
 	<true/>
+	<key>com.apple.private.corespeech_launchagent.xpc</key>
+	<true/>
 	<key>com.apple.private.corespeechd.activation</key>
 	<true/>
 	<key>com.apple.private.exclaves.conclave-host</key>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>App.Intents.IndexedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.Intents.IndexedEnum</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 				<key>App.Shortcut.Entity</key>
 				<dict>
 					<key>mode</key>

 	</array>
 	<key>com.apple.private.iokit.darkwake-control</key>
 	<true/>
+	<key>com.apple.private.isolated.audio.coreaudioclient</key>
+	<true/>
+	<key>com.apple.private.isolated.audio.coreaudioclient.shareddsp</key>
+	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.siri.recorded-audio</string>
+	</array>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
 	<key>com.apple.private.siri.activation</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/Library/Audio/Tunings/</string>
 	</array>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/PersonalDeviceVolumes/</string>
-	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/ASRAssetOverrides/</string>

 		<string>com.apple.assistant.dictation</string>
 		<string>com.apple.audio.AudioSession</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.assistant.domain.status.service</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceflow.context</string>
+		<string>com.apple.intelligenceflow.querydecoration</string>
 		<string>com.apple.assistant.domain.validation.service</string>
 		<string>com.apple.assistant.domain.system.settings.service</string>
 		<string>com.apple.feedbacklogger</string>

 		<string>756</string>
 		<string>757</string>
 		<string>1701</string>
+		<string>1441</string>
 	</array>
 	<key>com.apple.trial.status.namespace-name.allow</key>
 	<array>

```

### 🆕 corespeechd_system

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd_system`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string></string>
	<key>com.apple.airplay.carplayavvc</key>
	<true/>
	<key>com.apple.aned.private.ANEAccess.allow</key>
	<true/>
	<key>com.apple.assistant.analytics</key>
	<true/>
	<key>com.apple.assistant.client</key>
	<true/>
	<key>com.apple.assistant.dictation</key>
	<true/>
	<key>com.apple.assistant.dictation.prerecorded</key>
	<true/>
	<key>com.apple.assistant.domain.audio.level.client.provider</key>
	<true/>
	<key>com.apple.assistant.domain.preferences.notifier</key>
	<true/>
	<key>com.apple.assistant.domain.status.access</key>
	<true/>
	<key>com.apple.assistant.domain.system.settings.access</key>
	<true/>
	<key>com.apple.assistant.domain.validation.client</key>
	<true/>
	<key>com.apple.assistant.multiuser.service</key>
	<true/>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.assistant.settings.remora</key>
	<true/>
	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-access-to-device-list</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.bluetooth.doap</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.callkit</key>
	<array>
		<string>private-controller-api</string>
	</array>
	<key>com.apple.coreaudio.CanRecordPastData</key>
	<true/>
	<key>com.apple.coreaudio.CanRecordWithoutSessionActivation</key>
	<true/>
	<key>com.apple.coreaudio.CanTapTelephony</key>
	<true/>
	<key>com.apple.coreaudio.app-tap</key>
	<true/>
	<key>com.apple.coreaudio.i-am-siri</key>
	<true/>
	<key>com.apple.coreaudio.private.SystemWideTap</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.coreduetd.people</key>
	<true/>
	<key>com.apple.corespeech.cat.xpc</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.hid.system.user-access-fast-path</key>
	<true/>
	<key>com.apple.homepodaccessorysettings.client</key>
	<true/>
	<key>com.apple.intelligenceflow.context</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.locationd.activity</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>CLIENT_ENTITLEMENT</string>
		<string>PURGE_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.asr</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.borealis</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.phs</key>
	<true/>
	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siri.speech-dictation-personalization</key>
	<true/>
	<key>com.apple.private.ShazamKit</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrUaap</string>
		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrAssistant</string>
		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrHammer</string>
		<string>com.apple.MobileAsset.Trial.Siri.SiriDictationAssets</string>
		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAttentionAssets</string>
		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingAsrHammer</string>
		<string>com.apple.MobileAsset.AdBlockerAssets</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsWatch</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsMarsh</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsTV</string>
		<string>com.apple.MobileAsset.SpeechEndpointAssets</string>
		<string>com.apple.MobileAsset.SpeechEndpointAssetsWatch</string>
		<string>com.apple.MobileAsset.SpeechEndpointAssetsTV</string>
		<string>com.apple.MobileAsset.SpeechEndpointMacOSAssets</string>
		<string>com.apple.MobileAsset.SpeechEndpointMarshAssets</string>
		<string>com.apple.MobileAsset.RaiseToSpeakAssets</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsMac</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsASMac</string>
		<string>com.apple.MobileAsset.SpeakerRecognitionAssets</string>
		<string>com.apple.MobileAsset.SpeakerRecognitionASMacAssets</string>
		<string>com.apple.MobileAsset.EmbeddedSpeech</string>
		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>
		<string>com.apple.MobileAsset.VoiceTriggerHSAssetsIPad</string>
		<string>com.apple.MobileAsset.VoiceTriggerHSAssetsWatch</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsStudioDisplay</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.attentionawareness</key>
	<true/>
	<key>com.apple.private.attentionawareness.samplewhileabsent</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd</string>
	</dict>
	<key>com.apple.private.audio.dark-wake-audio</key>
	<true/>
	<key>com.apple.private.audio.hal.aop-audio.user-access</key>
	<true/>
	<key>com.apple.private.audio.interprocess-tap</key>
	<true/>
	<key>com.apple.private.audio.notification-wake-audio</key>
	<true/>
	<key>com.apple.private.audio.suppress-mic-indicator</key>
	<true/>
	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
	<true/>
	<key>com.apple.private.avfoundation.capture.nonstandard-client.allowed-media-types</key>
	<dict>
		<key>AVMediaTypeMetadataObject</key>
		<array>
			<string>AVMetadataObjectTypeTrackedFaces</string>
		</array>
	</dict>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.corespeechd</string>
	<key>com.apple.private.biome.read-only</key>
	<string>Dictation.UserEdit</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Emoji.Engagement</string>
		<string>Dictation.UserEdit</string>
		<string>Siri.VoiceTriggerStatistics</string>
		<string>SiriDictation</string>
		<string>Siri.SelfTriggerSuppression</string>
		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
		<string>Siri.ASR.RequestMetricsRecord</string>
		<string>Siri.ASR.ContextualReplayRecord</string>
	</array>
	<key>com.apple.private.bmk.allow</key>
	<true/>
	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
	<true/>
	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
	<true/>
	<key>com.apple.private.coreaudio.viewInterruptorName.allow</key>
	<true/>
	<key>com.apple.private.corespeech.xpc.remote</key>
	<true/>
	<key>com.apple.private.corespeech_launchagent.xpc</key>
	<true/>
	<key>com.apple.private.corespeechd.activation</key>
	<true/>
	<key>com.apple.private.exclaves.conclave-host</key>
	<true/>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.private.healthkit</key>
	<true/>
	<key>com.apple.private.healthkit.medicaliddata</key>
	<true/>
	<key>com.apple.private.hid.client.event-monitor</key>
	<true/>
	<key>com.apple.private.homehubd</key>
	<array>
		<string>endpoint-read</string>
	</array>
	<key>com.apple.private.homekit.siri-audio-connection</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.corespeechd</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>PeopleSuggesterContactPriors</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>PeopleSuggester.ContactPrior</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
		<key>SpeechProfile</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>App.InstalledApp</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomCarName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomCarProfileName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomContactGroupName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomContactName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomMediaAudiobookAuthorName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomMediaAudiobookTitle</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomMediaMusicArtistName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomMediaPlaylistTitle</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomMediaShowTitle</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomNotebookItemGroupName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomNotebookItemTitle</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomPaymentsAccountNickname</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomPaymentsOrganizationName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomPhotoAlbumName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomPhotoTag</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomVoiceCommandName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.CustomWorkoutActivityName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.GlobalMediaAudiobookAuthor</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.GlobalMediaAudiobookTitle</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.GlobalMediaMusicArtistName</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.GlobalMediaPlaylistTitle</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.IntentVocabulary.GlobalMediaShowTitle</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.Intents.IndexedEntity</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.Intents.IndexedEnum</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.Shortcut.Entity</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>App.Shortcut.Phrase</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Calendar.Event</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>CarPlay.RadioStation</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Contacts.Contact</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>FindMy.Device</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Fitness.Guest</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Health.Medication</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>HomeKit.Home</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>HomeKit.HomeServiceArea</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Location.SignificantLocation</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>MediaLibrary.Media</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Podcasts.Podcast</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Siri.PrivateLearning.Contact</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Siri.PrivateLearning.Media</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>UserAccount.Identity</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
			<key>Streams</key>
			<dict>
				<key>CarPlay.Connected</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>appEntityRelevanceRanking</string>
		<string>personEntityRelevanceRanking</string>
		<string>loiEntityRelevanceRanking</string>
		<string>personEntityLongTermRanking</string>
		<string>personImportanceSignals</string>
		<string>entityImportanceSignals</string>
		<string>siriPersonView</string>
	</array>
	<key>com.apple.private.iokit.darkwake-control</key>
	<true/>
	<key>com.apple.private.isolated.audio.coreaudioclient</key>
	<true/>
	<key>com.apple.private.isolated.audio.coreaudioclient.shareddsp</key>
	<true/>
	<key>com.apple.private.kernel.global-proc-info</key>
	<true/>
	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
	<true/>
	<key>com.apple.private.mediaexperience.isusingbuiltinmicforrecording.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.microphoneattribution.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.preferredminimummicrophoneindicatorlightontime.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.usesecuresession</key>
	<true/>
	<key>com.apple.private.mediasafetynet.exception.announcemessage</key>
	<true/>
	<key>com.apple.private.mobiletimerd</key>
	<true/>
	<key>com.apple.private.perceptiond.client</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.siri.recorded-audio</string>
	</array>
	<key>com.apple.private.security.storage.SiriVocabulary</key>
	<true/>
	<key>com.apple.private.siri.activation</key>
	<true/>
	<key>com.apple.private.siri.invoke</key>
	<true/>
	<key>com.apple.private.speech-model-training</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceBluetoothAlways</string>
	</array>
	<key>com.apple.private.tcc.manager.access.read</key>
	<array>
		<string>kTCCServiceAll</string>
	</array>
	<key>com.apple.private.userprofiles.read</key>
	<true/>
	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.rootless.storage.CoreSpeech</key>
	<true/>
	<key>com.apple.runningboard.assertions.appshack</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.CoreSpeech</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/</string>
		<string>/private/var/db/assetsubscriptiond/</string>
		<string>/Library/Audio/Tunings/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/ASRAssetOverrides/</string>
		<string>/Library/CoreDuet/</string>
		<string>/Library/PeopleSuggester/</string>
		<string>/Library/Caches/com.apple.corespeech.cat.xpc/</string>
		<string>/Library/UnifiedAssetFramework/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/DES/Records/com.apple.siri.speech-dictation-personalization/</string>
		<string>/Library/VoiceTrigger/</string>
		<string>/Library/Logs/CrashReporter/Assistant/</string>
		<string>/Library/Logs/CrashReporter/VoiceTrigger/</string>
		<string>/Library/Logs/CrashReporter/ssr/</string>
		<string>/Library/Logs/CrashReporter/CoreSpeech/</string>
		<string>/Library/Logs/CrashReporter/RTS/</string>
		<string>/Library/Caches/VoiceTrigger/</string>
		<string>/Library/Caches/com.apple.corespeechd/</string>
		<string>/Documents/Logs/CoreSpeech/</string>
		<string>/Library/Assistant/</string>
		<string>/Library/Caches/RaiseToSpeak/</string>
		<string>/Library/Caches/CoreSpeech/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleSPUHIDDriverUserClient</string>
		<string>IOHIDEventServiceFastPathUserClient</string>
		<string>AGXDeviceUserClient</string>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>H11ANEInDirectPathClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mobile.usermanagerd.xpc</string>
		<string>com.apple.perceptiond.api</string>
		<string>com.apple.perceptiond.entitykit</string>
		<string>com.apple.coreduetd.people</string>
		<string>com.apple.server.bluetooth</string>
		<string>com.apple.server.bluetooth.general.xpc</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
		<string>com.apple.sirittsd</string>
		<string>com.apple.carousel.backlightxpc</string>
		<string>com.apple.usernotifications.usernotificationservice</string>
		<string>com.apple.frontboard.systemappservices</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.assistant.settings.remora</string>
		<string>com.apple.MobileTimer.timerserver</string>
		<string>com.apple.MobileTimer.alarmserver</string>
		<string>com.apple.audio.voicetrigger.xpc</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.voicetrigger.voicetriggerservice</string>
		<string>com.apple.audio.AudioQueueServer</string>
		<string>com.apple.server.bluetooth</string>
		<string>com.apple.SystemConfiguration.NetworkInformation</string>
		<string>com.apple.mediaremoted.xpc</string>
		<string>com.apple.coremedia.carplayavvc.xpc</string>
		<string>com.apple.iohideventsystem</string>
		<string>com.apple.siri.activation</string>
		<string>com.apple.siri.activation.horseman</string>
		<string>com.apple.siri.activation.blackbird</string>
		<string>com.apple.assistant.analytics</string>
		<string>com.apple.audio.SystemSoundServer-iOS</string>
		<string>com.apple.BTLEAudioController.xpc</string>
		<string>com.apple.healthd.server</string>
		<string>com.apple.SystemConfiguration.configd</string>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.locationd.registration</string>
		<string>com.apple.backlightd</string>
		<string>com.apple.carousel.wakegesturemonitor</string>
		<string>com.apple.homekit.audio.xpc</string>
		<string>com.apple.SBUserNotification</string>
		<string>com.apple.nsurlsessiond.NSURLSessionProxyService</string>
		<string>com.apple.nsurlstorage-cache</string>
		<string>com.apple.commcenter.xpc</string>
		<string>com.apple.mediasafetynet.exceptions</string>
		<string>com.apple.symptom_diagnostics</string>
		<string>com.apple.corespeech.mockremoteplugin.xpc</string>
		<string>com.apple.systemstatus.activityattribution</string>
		<string>com.apple.assistant.multiuser.service</string>
		<string>com.apple.callkit.callcontrollerhost</string>
		<string>com.apple.siri.morphunassetsupdaterd</string>
		<string>com.apple.homehubd.manage</string>
		<string>com.apple.AttentionAwareness</string>
		<string>com.apple.corespeech.speechmodeltraining.xpc</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.remoted</string>
		<string>com.apple.PairingManager</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.homepodaccessorysettings.server</string>
		<string>com.apple.audio.isolated.client.service</string>
		<string>com.apple.assistant.dictation</string>
		<string>com.apple.audio.AudioSession</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.assistant.domain.status.service</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.intelligenceplatform.EntityResolution</string>
		<string>com.apple.intelligenceflow.context</string>
		<string>com.apple.intelligenceflow.querydecoration</string>
		<string>com.apple.assistant.domain.validation.service</string>
		<string>com.apple.assistant.domain.system.settings.service</string>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.uservault</string>
		<string>com.apple.assistant.domain.audio.level.service</string>
		<string>com.apple.cache_delete</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.ironwood.support</string>
		<string>com.apple.TelephonyUtilities</string>
		<string>com.apple.nano</string>
		<string>com.apple.raisetospeak</string>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.assistant.support</string>
		<string>com.apple.CoreMotion</string>
		<string>com.apple.airplay</string>
		<string>com.apple.mediaremote</string>
		<string>com.apple.UIKit</string>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.assistant.domain.preferences</string>
		<string>com.apple.keyboard.preferences</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.assistant</string>
		<string>com.apple.niservices</string>
		<string>com.apple.voicetrigger</string>
		<string>com.apple.voicetrigger.notbackedup</string>
		<string>com.apple.avfoundation.avvc</string>
		<string>com.apple.audio.virtualaudio</string>
		<string>com.apple.speakerrecognition</string>
		<string>com.apple.coreaudio</string>
		<string>com.apple.coremedia</string>
		<string>com.apple.raisetospeak</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>kern.stackshot_stats</string>
		<string>net.routetable.0.0.3.0</string>
		<string>kern.exclaves_status</string>
		<string>kern.task_conclave</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.server.bluetooth</string>
		<string>com.apple.server.bluetooth.general.xpc</string>
	</array>
	<key>com.apple.security.ts.ane-client</key>
	<true/>
	<key>com.apple.security.ts.mobile-keybag-access</key>
	<true/>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
	<key>com.apple.security.ts.play-audio</key>
	<true/>
	<key>com.apple.security.ts.play-media</key>
	<true/>
	<key>com.apple.security.ts.power-assertions</key>
	<true/>
	<key>com.apple.security.ts.read-any-bundle</key>
	<true/>
	<key>com.apple.security.ts.springboard-services</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string></string>
	<key>com.apple.sensorkit.writer.allow</key>
	<array>
		<string>com.apple.SensorKit.speechMetrics.siri</string>
		<string>com.apple.SensorKit.speechEmotion.siri</string>
		<string>com.apple.SensorKit.soundDetection.siri</string>
	</array>
	<key>com.apple.siri.activation</key>
	<true/>
	<key>com.apple.siri.embeddedspeech</key>
	<true/>
	<key>com.apple.siri.external_request</key>
	<true/>
	<key>com.apple.system-task-ports.name.safe</key>
	<true/>
	<key>com.apple.systemstatus.activityattribution</key>
	<true/>
	<key>com.apple.systemstatus.publisher.domains</key>
	<array>
		<string>media</string>
	</array>
	<key>com.apple.telephonyutilities.callservicesd</key>
	<array>
		<string>access-calls</string>
		<string>access-call-providers</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>200</string>
		<string>322</string>
		<string>404</string>
		<string>372</string>
		<string>401</string>
		<string>751</string>
		<string>756</string>
		<string>757</string>
		<string>1701</string>
		<string>1441</string>
	</array>
	<key>com.apple.trial.status.namespace-name.allow</key>
	<array>
		<string>UAF_AB_UNDERSTANDING</string>
	</array>
	<key>com.apple.uservault</key>
	<true/>
	<key>com.apple.voicetrigger.voicetriggerservice</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.corespeech</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/Support/suggestd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 	<true/>
 	<key>com.apple.private.canmodifyanyuseractivity</key>
 	<true/>
+	<key>com.apple.private.ciphermld.allow</key>
+	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.CoreSuggestions.PseudoEvents</key>

 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>EventEntityExtraction</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.Intents.ExtractedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>ProactiveSummarization</key>
 		<dict>
 			<key>Streams</key>

 	<array>
 		<string>com.apple.CoreSuggestions</string>
 	</array>
+	<key>com.apple.private.usernotifications.settings</key>
+	<array>
+		<string>read</string>
+	</array>
 	<key>com.apple.private.xpc.domain-extension</key>
 	<true/>
 	<key>com.apple.privatefederatedlearning.allowed</key>

 	<true/>
 	<key>com.apple.rootless.storage.triald</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.sage.summarization</key>
 	<true/>
 	<key>com.apple.sage.textcomposition</key>

 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.ciphermld</string>
+		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.iokit.powerdxpc</key>
 	<false/>
 	<key>com.apple.private.ckks</key>

```
### devicecheckd

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.device-identifiers</key>
 	<true/>
+	<key>com.apple.mobileactivationd.eda</key>
+	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
+	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 	</array>
 	<key>keychain-access-groups</key>
 	<array>
+		<string>com.apple.PlatformSSO.auth</string>
 		<string>lockdown-identities</string>
 		<string>2bit-identity</string>
 		<string>com.apple.appattest.identities</string>
+		<string>appattest-webauthn</string>
+		<string>appattest-device</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/Versions/A/XPCServices/diskimagescontroller.xpc/Contents/MacOS/diskimagescontroller`

```diff

 	<key>com.apple.diskimages.creator-uc</key>
 	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>1</integer>
+	<integer>2</integer>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.vfs.role-account-openfrom</key>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/maild`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 		<string>group.com.apple.mail</string>
 		<string>com.apple.MailPersonaStorage</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>

```

### 🆕 ExclaveFDRDecode

> `/System/Library/PrivateFrameworks/ExclaveFDRDecode.framework/Versions/A/ExclaveFDRDecode`

- No entitlements *(yet)*
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/Resources/familycircled`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<true/>
 	<key>com.apple.private.icloud-account-access</key>
 	<true/>
+	<key>com.apple.private.managed-settings.apply</key>
+	<true/>
 	<key>com.apple.private.security.storage.familycircled</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<array>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.ManagedSettingsAgent</string>
 	</array>
 </dict>
 </plist>

```
### FedStatsMLRPlugin

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPlugin.appex/Contents/MacOS/FedStatsMLRPlugin`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStats.Plugin</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.PriML.FedStats.Plugin</string>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### FedStatsMLRPluginClassB

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginClassB.appex/Contents/MacOS/FedStatsMLRPluginClassB`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStats.PluginClassB</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.PriML.FedStats.PluginClassB</string>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

```
### FedStatsMLRPluginNonDnU

> `/System/Library/PrivateFrameworks/FedStats.framework/PlugIns/FedStatsMLRPluginNonDnU.appex/Contents/MacOS/FedStatsMLRPluginNonDnU`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.mlpt.PriML.FedStatsPlugin.NonDnU</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.mlpt.PriML.FedStatsPlugin.NonDnU</string>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>

```
### DraftingExtension-macOS

> `/System/Library/PrivateFrameworks/Feedback.framework/PlugIns/DraftingExtension-macOS.appex/Contents/MacOS/DraftingExtension-macOS`

```diff

 	<array>
 		<string>group.com.apple.feedback</string>
 	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.feedback</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.Feedback.DraftingExtension</string>
+	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

 		<string>com.apple.ist.ds.appleconnect2.service.agent</string>
 		<string>com.apple.ist.ds.service.rlogd</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant.settings</string>
+	</array>
 </dict>
 </plist>
 

```
### com.apple.gamecenter.GameCenterUIService

> `/System/Library/PrivateFrameworks/GameCenterUICore.framework/XPCServices/com.apple.gamecenter.GameCenterUIService.xpc/Contents/MacOS/com.apple.gamecenter.GameCenterUIService`

```diff

 	<true/>
 	<key>com.apple.private.messages.autoshare</key>
 	<true/>
+	<key>com.apple.private.runningboard.roles</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<true/>
 	<key>com.apple.private.suggestions</key>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
+	<true/>
 	<key>com.apple.intelligenceflow.context</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.modelmanager.query</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	</array>
 	<key>com.apple.private.assistant.settings</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>GenerativeExperiences.FailureTracking</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>

 				<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 			</array>
 		</dict>
+		<key>com.apple.GenerativeFunctions.PeriodicTasks.ReportAvailabilityTask</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Availability</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>com.apple.GenerativeModelsFoundation.FailureTracking</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>GenerativeExperiences.FailureTracking</string>
+			</array>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

```
### healthd

> `/System/Library/PrivateFrameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.ctr.thread</key>
+	<true/>
 	<key>com.apple.private.fillmore.getTriggerStats</key>
 	<true/>
 	<key>com.apple.private.fillmore.provideEmac</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.StatusKit.presence</string>
+		<string>com.apple.linkd.autoShortcut</string>
+		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.MobileStoreDemo.test</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### HydraQLPreviewExtension

> `/System/Library/PrivateFrameworks/Hydra.framework/Plugins/HydraQLPreviewExtension.appex/Contents/MacOS/HydraQLPreviewExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.hydrars</key>
 	<true/>
 	<key>com.apple.private.quickLook.externalResources</key>

```
### HydraQLThumbnailExtension

> `/System/Library/PrivateFrameworks/Hydra.framework/Plugins/HydraQLThumbnailExtension.appex/Contents/MacOS/HydraQLThumbnailExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.hydrars</key>
 	<true/>
 	<key>com.apple.private.quickLook.externalResources</key>

```
### identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/Contents/MacOS/identityservicesd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.private.alloy.safari.groupactivities</string>
 		<string>com.apple.private.alloy.safetymonitor</string>
 		<string>com.apple.private.alloy.gftaastest.communication</string>
-		<string>com.apple.private.alloy.groupkit</string>
-		<string>com.apple.private.alloy.groupkit.invite</string>
 		<string>com.apple.private.alloy.arcade.fastsync</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.arcade.gftaas</string>

```
### IDSBlastDoorService

> `/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/Versions/A/XPCServices/IDSBlastDoorService.xpc/Contents/MacOS/IDSBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<false/>
 	<key>com.apple.coregraphics.disableinmemoryfonts</key>
 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.imageio.allowabletypes</key>
 	<array/>
 	<key>com.apple.pac.shared_region_id</key>

 	<array/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>blastdoor-ids</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>blastdoor-ids</string>
-	</array>
 </dict>
 </plist>
 

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/Contents/MacOS/imagent`

```diff

 	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>development</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>CLIENT_ENTITLEMENT</string>

 		<string>SERVICE_ENTITLEMENT</string>
 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	<true/>
 	<key>com.apple.private.sysdiagnose</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 	<array>
 		<string>group.com.apple.ManagedSettings</string>
 	</array>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

 		<string>appleaccount</string>
 		<string>InternetAccounts</string>
 		<string>IMCore</string>
+		<string>trustkit</string>
 	</array>
 </dict>
 </plist>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/Contents/MacOS/IMDPersistenceAgent`

```diff

 	<string>com.apple.imdpersistenceagent</string>
 	<key>com.apple.datadetectors.source-read.user</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.usernotifications.communication</key>
 	<true/>
 	<key>com.apple.developer.usernotifications.critical-alerts</key>

```
### IMTranscoderAgent

> `/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/Contents/MacOS/IMTranscoderAgent`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>IMTranscoderAgent</string>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>

```
### IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferServices.framework/IMTransferAgent.app/Contents/MacOS/IMTransferAgent`

```diff

 	</array>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.imtransferagent</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 		<string>com.apple.private.alloy.facetime.messaging</string>
 		<string>com.apple.private.alloy.safari.groupactivities</string>
 		<string>com.apple.private.alloy.gftaastest.communication</string>
-		<string>com.apple.private.alloy.groupkit</string>
-		<string>com.apple.private.alloy.groupkit.invite</string>
 		<string>com.apple.private.alloy.arcade.fastsync</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.arcade.gftaas</string>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/Versions/A/intelligencecontextd`

```diff

 		<string>eventGraphIndex</string>
 		<string>ontologyIndex</string>
 	</array>
+	<key>com.apple.mediaremote.device-info</key>
+	<true/>
+	<key>com.apple.mediaremote.remote-control-discovery</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MorphunData</string>

 	<true/>
 	<key>com.apple.siri.inference.EntityMatcher.useSensitiveLogging</key>
 	<true/>
+	<key>com.apple.siri.location</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>755</string>

```
### IntelligenceFlowDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/IntelligenceFlowDiagnostics.appex/Contents/MacOS/IntelligenceFlowDiagnostics`

```diff

 	<array>
 		<string>Sage.Transcript</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
+		<string>IntelligenceEngine.Interaction.Donation</string>
 	</array>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>

 			<array>
 				<string>Sage.Transcript</string>
 				<string>IntelligenceFlow.Transcript.Datastream</string>
+				<string>IntelligenceEngine.Interaction.Donation</string>
 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.storage.SiriFeatureStore</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/intelligenceflowd`

```diff

 	<true/>
 	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
 	<true/>
+	<key>com.apple.corespotlight.search.allowed.bundleIDs</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

 	<true/>
 	<key>com.apple.intelligenceflow.uiContext</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.uiextension.discovery</key>

 		<string>IntelligenceFlow.ResponseGeneration</string>
 		<string>IntelligenceFlow.Experimentation</string>
 		<string>IntelligenceFlow.IFRequestTelemetry</string>
+		<string>IntelligenceFlow.PlanGenerationTelemetry</string>
 		<string>PostSiriEngagement</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>Siri.Remembers.InteractionHistory</string>

 	<array>
 		<string>com.apple.private.alloy.shortcuts</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>defaultResolverInteractions</string>
+		<string>visualIdentifier</string>
+		<string>bundleIdMap</string>
+		<string>entitySimilarityFeatures</string>
+	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>
 	<true/>
 	<key>com.apple.private.photos.XPCStoreOptIn</key>

 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
+	<key>com.apple.private.security.storage.Spotlight</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.shazamkit.allow-external-audio-recording</key>

 	<true/>
 	<key>com.apple.private.shazamkit.allow-signature-generation</key>
 	<true/>
+	<key>com.apple.private.suggestions.contacts</key>
+	<true/>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
+	<key>com.apple.siri.location</key>
+	<true/>
 	<key>com.apple.siriknowledged.koa.donate.internal</key>
 	<true/>
 	<key>com.apple.spotlight.entitledattributes</key>

 		<string>1170</string>
 		<string>1180</string>
 		<string>1760</string>
-		<string>1761</string>
+		<string>INTELLIGENCE_FLOW_QUERY_DECORATOR</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### intelligenceplatformd

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/intelligenceplatformd`

```diff

 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.intelligenceplatform.IntelligencePlatformCore.ERMLRuntimePlugin</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
+	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>
 		<string>photos.scene</string>

 		<string>Motion.Activity</string>
 		<string>Location.Semantic</string>
 		<string>UserFocus.ComputedMode</string>
+		<string>IntelligencePlatform.Views.Updated</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>1161</string>
 		<string>1170</string>
 		<string>1180</string>
+		<string>755</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### knowledgeconstructiond

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/Versions/A/knowledgeconstructiond`

```diff

 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>

 					<key>mode</key>
 					<string>read-only</string>
 				</dict>
+				<key>Autonaming.Messages.AccuracyFedStats</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
 				<key>Autonaming.Messages.Inferences</key>
 				<dict>
 					<key>mode</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

 		<string>1180</string>
 		<string>1190</string>
 		<string>1191</string>
+		<string>755</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### com.apple.MailServiceAgent

> `/System/Library/PrivateFrameworks/MailService.framework/Versions/A/XPCServices/com.apple.MailServiceAgent.xpc/Contents/MacOS/com.apple.MailServiceAgent`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.email.maild</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/mediaanalysisd`

```diff

 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>
+		<string>MediaAnalysis.VideoAnalysis.PerAsset</string>
+		<string>MediaAnalysis.VideoAnalysis.PerLibrary</string>
 		<string>MediaAnalysis.PEC.Processing</string>
 		<string>MediaAnalysis.VisualSearch.Processing</string>
 	</array>

```
### MediaAnalysisBlastDoorService

> `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/Versions/A/XPCServices/MediaAnalysisBlastDoorService.xpc/Contents/MacOS/MediaAnalysisBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.posterboardservices.disallowArchivingAppleArchive</key>
 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>blastdoor-messages</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>
-		<string>blastdoor-hubble</string>
 	</array>
 	<key>com.apple.private.security.message-filter</key>
 	<true/>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>
-		<string>blastdoor-hubble</string>
-	</array>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>blastdoor-messages</string>
 	</array>
 </dict>
 </plist>

```
### com.apple.photos.ImageConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/A/XPCServices/com.apple.photos.ImageConversionService.xpc/Contents/MacOS/com.apple.photos.ImageConversionService`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

```
### com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/A/XPCServices/com.apple.photos.VideoConversionService.xpc/Contents/MacOS/com.apple.photos.VideoConversionService`

```diff

 	<true/>
 	<key>com.apple.coremedia.cameraviewfinder</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

```
### mstreamd

> `/System/Library/PrivateFrameworks/MediaStream.framework/Versions/A/Support/mstreamd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.application-identifier</key>
+	<string>AAPLPHOTOS.com.apple.mstreamd</string>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```

### 🆕 com.apple.MessageUIMacHelperService

> `/System/Library/PrivateFrameworks/MessageUIMacHelper.framework/Versions/A/XPCServices/com.apple.MessageUIMacHelperService.xpc/Contents/MacOS/com.apple.MessageUIMacHelperService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.application-identifier</key>
	<string>com.apple.MessageUIMacHelperService</string>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```
### MessagesAirlockService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/MessagesAirlockService.xpc/Contents/MacOS/MessagesAirlockService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.private.pac.exception</key>

```
### MessagesBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/Versions/A/XPCServices/MessagesBlastDoorService.xpc/Contents/MacOS/MessagesBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
 	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.posterboardservices.disallowArchivingAppleArchive</key>
 	<true/>
 	<key>com.apple.private.pac.exception</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>blastdoor-messages</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>

 	</array>
 	<key>com.apple.private.security.storage.PassKit</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>blastdoor-messages</string>
-	</array>
 </dict>
 </plist>
 

```
### accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```

### 🆕 ModelCatalogAgent

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/ModelCatalogAgent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.SystemConfiguration.SCDynamicStore-read-no-fault</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.ModelCatalogAgent</string>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>AppleIntelligence.Availability</string>
	</array>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>ModelCatalog.Subscriptions.Decisions</string>
	</array>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.ModelCatalogAgent</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>ModelCatalogSubscriptionEvaluation</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Availability</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>ModelCatalog.Subscriptions.Decisions</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>ModelCatalog.Subscriptions.ExplicitRequests</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/UnifiedAssetFramework/</string>
		<string>/Library/AppleIntelligencePlatform/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.mobileasset.autoasset</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
		<string>com.apple.ModelCatalogAgent</string>
		<string>com.apple.modelcatalog.ajax</string>
		<string>kCFPreferencesAnyApplication</string>
	</array>
</dict>
</plist>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/modelcatalogd`

```diff

 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
-	<key>com.apple.private.followup</key>
-	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>AppleIntelligence.Availability</string>
+	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>ModelCatalog.Subscriptions.Decisions</string>
+		<string>GenerativeExperiences.FailureTracking</string>
+	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ModelCatalogSubscriptionEvaluation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Availability</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>ModelCatalog.Subscriptions.Decisions</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>ModelCatalog.Subscriptions.ExplicitRequests</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.storage.AppleIntelligencePlatform</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>

 	<true/>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/UnifiedAssetFramework/</string>

 		<string>com.apple.modelcatalogd</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>
+		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 NetworkInfoDiagnosticExtension

> `/System/Library/PrivateFrameworks/NetworkInfo.framework/PlugIns/NetworkInfoDiagnosticExtension.appex/Contents/MacOS/NetworkInfoDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CompanionLink</key>
	<true/>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.networking.multipath</key>
	<true/>
	<key>com.apple.locationd.activity</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.status</key>
	<true/>
	<key>com.apple.private.network.interface-control</key>
	<true/>
	<key>com.apple.private.network.statistics</key>
	<true/>
	<key>com.apple.private.networkQuality</key>
	<true/>
	<key>com.apple.private.networking.elevated-logging</key>
	<true/>
	<key>com.apple.private.pcapd-local</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.sysctl.read-write</key>
	<array>
		<string>net.route.verbose</string>
		<string>net.inet6.icmp6.nd6_debug</string>
		<string>net.inet6.ip6.select_srcaddr_debug</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/networkinfodiagext/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.pcapd-local</string>
	</array>
	<key>com.apple.wifi.manager-access</key>
	<true/>
</dict>
</plist>

```
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.news.ScoringService.allow</key>
+	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### IPSExtension

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/PlugIns/IPSExtension.appex/Contents/MacOS/IPSExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>

```

### 🆕 amsondevicestoraged

> `/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.amsondevicestoraged</string>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.icloud-account-access</key>
	<true/>
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.amsondevicestoraged</string>
	</array>
	<key>com.apple.private.sqlite.sqlite-encryption</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.amsondevicestoraged</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<string>2178910101</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.cdp.utility</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>Production</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-development-container-identifiers</key>
 	<array>
 		<string>com.apple.passes</string>

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
-	<key>com.apple.private.bmk.allow</key>
+	<key>com.apple.private.biometrickit.allow-default</key>
 	<true/>
 	<key>com.apple.private.ckks</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.octagon</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.PassbookUIService</string>
+		<string>com.apple.pay.merchant-tokens</string>
 	</array>
 </dict>
 </plist>

```
### photoanalysisd

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Versions/A/Support/photoanalysisd`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest.ExtendLifetime</key>
 	<true/>
+	<key>com.apple.CoreRoutine.Visit</key>
+	<true/>
 	<key>com.apple.PersonalizedSensingService</key>
 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>

```
### photolibraryd

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/Support/photolibraryd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 		<string>/AppleInternal/Library/Frameworks/Python.framework/</string>
 		<string>/AppleInternal/Library/Python/</string>
 		<string>/usr/local/bin/cplctl</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>

```
### PerfPowerServicesSignpostReader

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/XPCServices/PerfPowerServicesSignpostReader.xpc/Contents/MacOS/PerfPowerServicesSignpostReader`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
-		<string>GenerativeModels.GenerativeFunctions.SystemInstrumenetation</string>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 	</array>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>

```

### 🆕 PerfPowerTelemetryClientRegistrationService

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/XPCServices/PerfPowerTelemetryClientRegistrationService.xpc/Contents/MacOS/PerfPowerTelemetryClientRegistrationService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.powerlog</string>
	</array>
</dict>
</plist>

```

### 🆕 PromotedContentJetService

> `/System/Library/PrivateFrameworks/PromotedContentJetSupport.framework/Versions/A/XPCServices/PromotedContentJetService.xpc/Contents/MacOS/PromotedContentJetService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.runningboard.jetengine</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/JetPackCache/</string>
		<string>/Library/HTTPStorages/com.apple.ap.PromotedContentJetService/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/Caches/com.apple.ap.PromotedContentJetService/</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.itunesstored</string>
		<string>com.apple.AppleMediaServices</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AdPlatforms</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.ap.PromotedContentJetService</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 ManagedSettingsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedSettingsSubscriber.xpc/Contents/MacOS/ManagedSettingsSubscriber`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.application-identifier</key>
	<string>com.apple.remotemanagement.ManagedSettingsSubscriber</string>
	<key>com.apple.private.managed-settings.apply</key>
	<true/>
	<key>com.apple.private.remotemanagement.subscriber</key>
	<true/>
</dict>
</plist>

```
### com.apple.SafariPlatformSupport.Helper

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper`

```diff

 	<true/>
 	<key>com.apple.authentication-services.access-credential-identities</key>
 	<true/>
+	<key>com.apple.authentication-services.app-passkey-autofill</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AuthenticationServices.AutoFill</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeAgent`

```diff

 	<string>production</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Versions/A/siriinferenced`

```diff

 	</array>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siriinference-dodml-plugin</key>
 	<true/>
+	<key>com.apple.private.SiriSuggestionsBookkeepingService.xpc</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.SiriInferenceHolidays</string>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>Photos.Engagement</string>
+		<string>Photos.Edit</string>
+		<string>Photos.Search</string>
+		<string>Photos.Favorite</string>
+		<string>Photos.Share</string>
+		<string>Photos.Picker</string>
+		<string>Photos.Delete</string>
+		<string>Photos.Memories.Viewed</string>
+		<string>Photos.Memories.Shared</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>UserFocus.ComputedMode</string>
 		<string>Location.Semantic</string>

 		<string>Siri.Execution</string>
 		<string>HomeKit.Client.AccessoryControl</string>
 		<string>Siri.RecognizedUser</string>
+		<string>App.Intents.Transcript</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>Siri.Remembers.AssistantSuggestions</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>Siri.Audio.CompanionContext</string>
+		<string>IntelligenceEngine.Interaction.Donation</string>
 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>

 		<string>group.com.apple.tipsnext</string>
 		<string>group.com.apple.siri.remembers</string>
 		<string>group.com.apple.siri.inference</string>
+		<string>group.com.apple.siri.sirisuggestions</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/MobileAsset/</string>
 		<string>~/Library/DuetExpertCenter/UICaches/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 		<string>com.apple.intelligenceflow.context</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.linkd.registry</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SiriSuggestionsBookkeepingService

> `/System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/Versions/A/XPCServices/SiriSuggestionsBookkeepingService.xpc/Contents/MacOS/SiriSuggestionsBookkeepingService`

```diff

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppIntent</string>

 	<array>
 		<string>group.com.apple.siri.sirisuggestions</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.suggestions</string>
 	</array>

 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.sirisuggestions</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
 		<string>com.apple.linkd.registry</string>

 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siriinferenced</key>
 	<true/>
+	<key>com.apple.sirisuggestions.allow</key>
+	<true/>
+	<key>com.apple.sirisuggestions.application-id</key>
+	<string>com.apple.siri.SuggestionsBookkeepingService</string>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1343</string>
+		<string>755</string>
 	</array>
 </dict>
 </plist>

```
### com.apple.SiriTTSService.TrialProxy

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/Versions/A/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/Contents/MacOS/com.apple.SiriTTSService.TrialProxy`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>

```
### sociallayerd

> `/System/Library/PrivateFrameworks/SocialLayer.framework/sociallayerd.app/Contents/MacOS/sociallayerd`

```diff

 	<string>com.apple.sociallayerd</string>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.imdpersistence.IMDPersistenceAgent-Syndication</key>
 	<true/>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.appleevents.allowedtosend</key>

```
### SoftwareUpdateNotificationManager

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/Resources/SoftwareUpdateNotificationManager.app/Contents/MacOS/SoftwareUpdateNotificationManager`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.iokit.wakerequest</key>
 	<true/>
 	<key>com.apple.keystore.filevault</key>

 	<true/>
 	<key>com.apple.private.SoftwareUpdateNotificationManagerService</key>
 	<true/>
+	<key>com.apple.private.accounts.allaccounts</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.configurationprofiles.bootstraptoken.readwrite</key>
 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.iokit.assertonlidclose</key>
+	<true/>
 	<key>com.apple.private.logout.forcecontinue</key>
 	<true/>
 	<key>com.apple.private.mobilestoredemo.enabledemo</key>

```
### spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

 	<true/>
 	<key>com.apple.apfs.spec_telemetry</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>TEST_ENTITLEMENT</string>

 		<string>PURGEABLE_ENTITLEMENT</string>
 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.MobileContainerManager.allowed</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.softwareupdateservicesd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

```
### StatusKitAgent

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent`

```diff

 	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	</dict>
 	<key>com.apple.private.cloudkit.spi</key>
 	<true/>
+	<key>com.apple.private.ids.firewall</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.status.keysharing</string>

```
### stickersd

> `/System/Library/PrivateFrameworks/Stickers.framework/Support/stickersd`

```diff

 		<key>com.apple.stickers.user</key>
 		<string>com.apple.stickers.user</string>
 	</dict>
+	<key>com.apple.private.cloudkit.spi</key>
+	<string>YES</string>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
 	<key>com.apple.private.corespotlight.bundleid</key>
 	<string>com.apple.Stickers</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>com.apple.stickersd.group</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>com.apple.stickersd.group</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Stickers/</string>

```
### systemmigrationd

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/Resources/systemmigrationd`

```diff

 		<string>kTCCServiceSystemPolicyAllFiles</string>
 		<string>kTCCServiceBluetoothAlways</string>
 	</array>
-	<key>com.apple.private.tcc.manager</key>
-	<true/>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceAccessibility</string>
+		<string>kTCCServicePostEvent</string>
+		<string>kTCCServiceScreenCapture</string>
+		<string>kTCCServiceSystemPolicyAllFiles</string>
+	</array>
 	<key>com.apple.rootless.datavault.controller</key>
 	<true/>
 	<key>com.apple.rootless.install.heritable</key>

```
### tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.endpoint-security.submit.tcc</key>
+	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
 	<key>com.apple.private.notificationcenterui.tcc</key>

```
### idleassetsd

> `/System/Library/PrivateFrameworks/TVIdleServices.framework/idleassetsd`

```diff

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.cache_delete</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### TelephonyBlastDoorService

> `/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/XPCServices/TelephonyBlastDoorService.xpc/Contents/MacOS/TelephonyBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
+	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
+	<false/>
 	<key>com.apple.coregraphics.disableinmemoryfonts</key>
 	<true/>
 	<key>com.apple.coregraphics.disablepdf</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.imageio.allowabletypes</key>
+	<array/>
+	<key>com.apple.pac.shared_region_id</key>
+	<string>BlastDoor</string>
+	<key>com.apple.private.coremedia.allowabletypecategories</key>
+	<array/>
+	<key>com.apple.private.pac.exception</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>blastdoor-ids</string>
 	<key>com.apple.private.security.enable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.private.security.message-filter</key>
+	<true/>
 	<key>com.apple.private.security.mutable-state-flags</key>
 	<array>
 		<string>blastdoor-post-launch</string>

```
### com.apple.FTLivePhotoService

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/Contents/MacOS/com.apple.FTLivePhotoService`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.telephonyutilities.callservicesdaemon.usernotificationprovider</string>
-		<string>com.apple.telephonyutilities.callservicesdaemon.reportingcontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationmanager</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>

```
### callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

 	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.developer.notificationcenter-identifiers</key>
 	<array>
 		<string>com.apple.facetime</string>

```
### SiriAUSP

> `/System/Library/PrivateFrameworks/TextToSpeech.framework/PlugIns/SiriAUSP.appex/Contents/MacOS/SiriAUSP`

```diff

 		<string>/tmp</string>
 		<string>/private/var/tmp</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/SiriTTS/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.audio.AudioConverterService</string>

 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Group Containers/group.com.apple.SiriTTS/</string>
+		<string>/Library/Caches/SiriTTS/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTrackingAgent`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.coreservices.useractivityd</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceUbiquity</string>

 	</array>
 	<key>com.apple.runningboard.assertions.useractivityd</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.coreservices.useractivityd</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.replicator.replication</string>
 		<string>com.apple.replicatorservices</string>
+		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### WalletBlastDoorService

> `/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/Versions/A/XPCServices/WalletBlastDoorService.xpc/Contents/MacOS/WalletBlastDoorService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>_UrgentLogSubmission</key>
+	<dict>
+		<key>CheckedAllocations</key>
+		<true/>
+	</dict>
+	<key>com.apple.coreaudio.LoadDecodersInProcess</key>
+	<false/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.pac.shared_region_id</key>
 	<string>BlastDoor</string>
 	<key>com.apple.private.pac.exception</key>

```
### watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

 		<string>ClientRestrictions</string>
 		<string>UserSettings</string>
 	</array>
+	<key>com.apple.mediaremote.now-playing-read-access</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### DiagnosticExtension

> `/System/Library/PrivateFrameworks/WiFiVelocity.framework/PlugIns/DiagnosticExtension.appex/Contents/MacOS/DiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

```

### 🆕 CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/PlugIns/CloudDocsDiagnostic.appex/Contents/MacOS/CloudDocsDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.unrestrictedPersona</key>
	<true/>
	<key>com.apple.private.clouddocs.read-diagnostic-metadata</key>
	<true/>
	<key>com.apple.private.clouddocs.spi</key>
	<array>
		<string>dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:</string>
	</array>
	<key>com.apple.private.pluginkit.persona</key>
	<string>system</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.iCloudDrive</string>
	</array>
	<key>com.apple.private.security.storage.CloudDocsDB</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.iCloudDrive</string>
	</array>
	<key>com.apple.security.enterprise-volume-access</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/CloudDocs/session/db/</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/CloudDocs/session/db/</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
	</array>
</dict>
</plist>

```

### 🆕 CloudDocsStorageManagement

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/PlugIns/CloudDocsStorageManagement.appex/Contents/MacOS/CloudDocsStorageManagement`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.clouddocs.account-access</key>
	<true/>
	<key>com.apple.private.clouddocs.spi</key>
	<array>
		<string>computePurgeableSpaceForAllUrgenciesWithReply:</string>
	</array>
	<key>com.apple.private.clouddocs.storage-management</key>
	<true/>
	<key>com.apple.private.fileprovider.storage-management</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Mobile Documents/</string>
		<string>/Library/Application Support/CloudDocs/</string>
		<string>/Library/Caches/com.apple.bird/</string>
		<string>/Desktop/</string>
		<string>/Documents/</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.icloud.managed</string>
	</array>
</dict>
</plist>

```

### 🆕 iCloud Drive

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/Resources/iCloud Drive.app/Contents/MacOS/iCloud Drive`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
</dict>
</plist>

```

### 🆕 bird

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Versions/A/Support/bird`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>allow-softwareupdated</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.bird</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>aps-environment</key>
	<string>serverPreferred</string>
	<key>com.apple.DiagnosticExtensions.extensionHost</key>
	<true/>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.and.client</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.bird</string>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.developer.aps-environment</key>
	<string>serverPreferred</string>
	<key>com.apple.developer.default-data-protection</key>
	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>production</string>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.fileprovider.migration-import-progress</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboard.shutdown</key>
	<true/>
	<key>com.apple.internal.fileprovider.fpck</key>
	<true/>
	<key>com.apple.internal.fileprovider.sync-root-management</key>
	<true/>
	<key>com.apple.mobile.keybagd.UserManager.sync</key>
	<true/>
	<key>com.apple.multitasking.termination</key>
	<true/>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>PURGE_ENTITLEMENT</string>
		<string>CLIENT_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.aps-connection-initiate</key>
	<true/>
	<key>com.apple.private.clouddocs.bundle-service</key>
	<true/>
	<key>com.apple.private.clouddocs.telemetry-disk-checker</key>
	<true/>
	<key>com.apple.private.cloudkit.accountDetailAccess</key>
	<true/>
	<key>com.apple.private.cloudkit.assetBoundaryKey</key>
	<true/>
	<key>com.apple.private.cloudkit.customAccounts</key>
	<true/>
	<key>com.apple.private.cloudkit.displaysSystemAcceptPrompt</key>
	<true/>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.packages</key>
	<true/>
	<key>com.apple.private.cloudkit.participant-pii</key>
	<true/>
	<key>com.apple.private.cloudkit.protectiondata</key>
	<true/>
	<key>com.apple.private.cloudkit.publishAssets</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<array>
		<string>performModifyWebSharingOperation:withBlock:</string>
		<string>getNewWebSharingIdentity:</string>
	</array>
	<key>com.apple.private.cloudkit.temporary.deviceCapabilities</key>
	<true/>
	<key>com.apple.private.cloudkit.usePublicAPSToken</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.desktopservices.home-folder.set-path</key>
	<true/>
	<key>com.apple.private.desktopservices.icloud-desktop.move-and-merge</key>
	<true/>
	<key>com.apple.private.foundation.fileprovider-any-path</key>
	<true/>
	<key>com.apple.private.foundation.fileprovideridentifier</key>
	<string>com.apple.bird</string>
	<key>com.apple.private.iaaccounts</key>
	<true/>
	<key>com.apple.private.kernel.global-proc-info</key>
	<true/>
	<key>com.apple.private.launchservices.allowopenwithanyhandler</key>
	<true/>
	<key>com.apple.private.librarian.can-reclaim-space</key>
	<true/>
	<key>com.apple.private.mobileinstall.allowedSPI</key>
	<array>
		<string>InstallForLaunchServices</string>
		<string>UninstallForLaunchServices</string>
	</array>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>com.apple.bird</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.CloudDocs</string>
		<string>group.com.apple.iCloudDrive</string>
	</array>
	<key>com.apple.private.security.scoped-bookmark-key</key>
	<true/>
	<key>com.apple.private.security.storage.CloudDocsDB</key>
	<true/>
	<key>com.apple.private.security.storage.CloudKit</key>
	<true/>
	<key>com.apple.private.security.storage.DocumentRevisions</key>
	<true/>
	<key>com.apple.private.security.storage.MobileDocuments</key>
	<true/>
	<key>com.apple.private.security.storage.iCloudDrive</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
		<string>kTCCServiceSystemPolicyDesktopFolder</string>
		<string>kTCCServiceSystemPolicyDocumentsFolder</string>
		<string>kTCCServiceFileProviderDomain</string>
	</array>
	<key>com.apple.private.tcc.manager.access.delete</key>
	<array>
		<string>kTCCServiceUbiquity</string>
	</array>
	<key>com.apple.private.tcc.manager.access.modify</key>
	<array>
		<string>kTCCServiceUbiquity</string>
	</array>
	<key>com.apple.private.tcc.manager.access.read</key>
	<array>
		<string>kTCCServiceAll</string>
	</array>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceUbiquity</string>
		<string>kTCCServiceSystemPolicyAllFiles</string>
	</array>
	<key>com.apple.private.tcc.manager.compute-designated-requirement</key>
	<true/>
	<key>com.apple.private.tcc.override-prompt-policy</key>
	<true/>
	<key>com.apple.private.vfs.authorized-access</key>
	<true/>
	<key>com.apple.private.vfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.vfs.open-by-id</key>
	<true/>
	<key>com.apple.private.vfs.snapshot</key>
	<true/>
	<key>com.apple.private.vfs.snapshot.user</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.CloudDocs</string>
		<string>group.com.apple.iCloudDrive</string>
	</array>
	<key>com.apple.security.enterprise-volume-access</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.shortcutitems.fullaccess</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>255</string>
	</array>
	<key>com.apple.usermanagerd.persona.fetch</key>
	<true/>
</dict>
</plist>

```

### 🆕 PhoneSuggestions

> `/System/Library/Siri/DM/SiriSuggestions/Owners/PhoneSuggestions.bundle/Contents/MacOS/PhoneSuggestions`

- No entitlements *(yet)*

### 🆕 SiriNotebookSuggestionsPlugin

> `/System/Library/Siri/DM/SiriSuggestions/Owners/SiriNotebookSuggestionsPlugin.bundle/Contents/MacOS/SiriNotebookSuggestionsPlugin`

- No entitlements *(yet)*

### 🆕 SiriTimeSuggestionsPlugin

> `/System/Library/Siri/DM/SiriSuggestions/Owners/SiriTimeSuggestionsPlugin.bundle/Contents/MacOS/SiriTimeSuggestionsPlugin`

- No entitlements *(yet)*

### 🆕 SystemMigrationPlugin

> `/System/Library/SystemMigrationPlugins/SystemMigrationPlugin.bundle/Contents/MacOS/SystemMigrationPlugin`

- No entitlements *(yet)*
### deviceinterfaced

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Support/deviceinterfaced`

```diff

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleRSMChannelControllerClient</string>
+		<string>AppleUSBHostFrameworkDeviceClient</string>
+		<string>AppleUSBHostFrameworkInterfaceClient</string>
 	</array>
 </dict>
 </plist>

```
### remotepairingd

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/XPCServices/remotepairingd.xpc/Contents/MacOS/remotepairingd`

```diff

 	<true/>
 	<key>com.apple.dt.coredevice.tunnelservice.client</key>
 	<true/>
+	<key>com.apple.private.RemoteServiceDiscovery.allow-sandbox</key>
+	<true/>
 	<key>com.apple.private.RemoteServiceDiscovery.device-admin</key>
 	<true/>
 	<key>com.apple.private.necp.match</key>

```

### 🆕 MobileDevices-0002

> `/System/Library/Templates/Data/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0002.bundle/Contents/MacOS/MobileDevices-0002`

- No entitlements *(yet)*

### 🆕 MobileDevices-0004

> `/System/Library/Templates/Data/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0004.bundle/Contents/MacOS/MobileDevices-0004`

- No entitlements *(yet)*

### 🆕 CPUTrace

> `/System/Library/Trace/Providers/CPUTrace.bundle/Contents/MacOS/CPUTrace`

- No entitlements *(yet)*
### GPUIExtension

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/Contents/MacOS/GPUIExtension`

```diff

 	</array>
 	<key>com.apple.private.feedback.drafting</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>GeneratedImageUserInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>visualIdentifier</string>

 	</array>
 	<key>com.apple.security.device.camera</key>
 	<true/>
+	<key>com.apple.security.files.user-selected.read-only</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>

 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides</string>
 		<string>/System/Library/PreinstalledAssetsV2/</string>
-		<string>/var/db/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ind.cloudfeatures</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

```
### Business

> `/System/iOSSupport/System/Library/Frameworks/BusinessChat.framework/PlugIns/Business.appex/Contents/MacOS/Business`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

```
### RemotePlayerService

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/XPCServices/RemotePlayerService.xpc/Contents/MacOS/RemotePlayerService`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
+	<true/>
 	<key>com.apple.private.coreaudio.viewInterruptorName.allow</key>
 	<true/>
 	<key>com.apple.private.coremedia.pidinheritance.allow</key>

```
### ScreenTimeWebExtension

> `/System/iOSSupport/System/Library/Frameworks/ScreenTime.framework/Versions/A/PlugIns/ScreenTimeWebExtension.appex/Contents/MacOS/ScreenTimeWebExtension`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>App.WebUsage</string>
+	</array>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 </dict>
 </plist>
 

```
### AnimojiStickersExtension

> `/System/iOSSupport/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AnimojiStickersExtension.appex/Contents/MacOS/AnimojiStickersExtension`

```diff

 <dict>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.messages.private.BypassShelfAccess</key>

```
### AvatarPickerMemojiEditor

> `/System/iOSSupport/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPickerMemojiEditor.appex/Contents/MacOS/AvatarPickerMemojiEditor`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### AvatarPickerMemojiPicker

> `/System/iOSSupport/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/AvatarPickerMemojiPicker.appex/Contents/MacOS/AvatarPickerMemojiPicker`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### StickersUltraExtension

> `/System/iOSSupport/System/Library/PrivateFrameworks/AvatarUI.framework/PlugIns/StickersUltraExtension.appex/Contents/MacOS/StickersUltraExtension`

```diff

 <dict>
 	<key>com.apple.camera.iokit-user-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.messages.private.BypassShelfAccess</key>

```

### 🆕 EnergyKitService

> `/System/iOSSupport/System/Library/PrivateFrameworks/EnergyKit.framework/Versions/A/XPCServices/EnergyKitService.xpc/Contents/MacOS/EnergyKitService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.EnergyKitService</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.developer.homekit</key>
	<true/>
	<key>com.apple.energykit.store</key>
	<true/>
	<key>com.apple.homekit.private-spi-access</key>
	<true/>
	<key>com.apple.locationd.authorizeapplications</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.private.homekit</key>
	<true/>
	<key>com.apple.private.homekit.home-location</key>
	<true/>
	<key>com.apple.private.homekit.location</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.security.exception.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Application Support/com.apple.homeenergyd/</string>
		<string>/private/var/mobile/Library/homeenergyd/</string>
		<string>/private/var/mobile/Library/homeenergyd/com.apple.homeenergyd/</string>
		<string>/private/var/mobile/Library/Weather/</string>
		<string>/private/var/mobile/Library/Caches/com.apple.EnergyKitService/</string>
		<string>/private/var/mobile/Library/Caches/com.apple.wpc.energyservices.gridservices/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/com.apple.homeenergyd/</string>
		<string>/Library/Application Support/homeenergyd/</string>
		<string>/Library/Application Support/homeenergyd/com.apple.homeenergyd/</string>
		<string>/Library/homeenergyd/</string>
		<string>/Library/homeenergyd/com.apple.homeenergyd/</string>
		<string>/Library/Caches/com.apple.wpc.homeservices.energyservices/</string>
		<string>/Library/Caches/com.apple.wpc.energyservices.utilityservices/</string>
		<string>/Library/Caches/com.apple.HomeKit.configurations/</string>
		<string>/Library/Caches/com.apple.HomeKit/</string>
		<string>/Library/Caches/com.apple.homeenergyd/</string>
		<string>/Library/HTTPStorages/com.apple.homeenergyd/</string>
		<string>/Library/HTTPStorages/com.apple.EnergyKitService/</string>
		<string>/Library/Caches/com.apple.EnergyKitService/</string>
		<string>/Library/Weather/</string>
		<string>/Library/Caches/com.apple.wpc.energyservices.gridservices/</string>
		<string>/Containers/Data/Application/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.homed.xpc</string>
		<string>com.apple.containermanagerd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.EnergyKit</string>
		<string>com.apple.Home</string>
		<string>com.apple.homeenergyd</string>
		<string>com.apple.wpc.homeservices.energyservices</string>
		<string>com.apple.wpc.energyservices.utilityservices</string>
		<string>com.apple.wpc.energyservices.gridservices</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.EnergyKitService</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### homeenergyd

> `/System/iOSSupport/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.wpc.energyservices.utilityservices</string>
+		<string>com.apple.wpc.energyservices.gridservices</string>
 	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>

```
### IMTranscoderAgent

> `/System/iOSSupport/System/Library/PrivateFrameworks/IMTranscoding.framework/XPCServices/IMTranscoderAgent.xpc/Contents/MacOS/IMTranscoderAgent`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-encode</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.pac.shared_region_id</key>

```
### PeerPaymentMessagesExtension

> `/System/iOSSupport/System/Library/PrivateFrameworks/PassKitUI.framework/PlugIns/PeerPaymentMessagesExtension.appex/Contents/MacOS/PeerPaymentMessagesExtension`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>

```
### HashtagImagesExtension

> `/System/iOSSupport/System/Library/PrivateFrameworks/SearchToShareCore.framework/Plugins/HashtagImagesExtension.appex/Contents/MacOS/HashtagImagesExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.messages.private.AllowAlertPresentation</key>
 	<true/>
 	<key>com.apple.messages.private.AllowConversationIdentifierAccess</key>

```
### launchd

> `/sbin/launchd`

```diff

 <dict>
 	<key>com.apple.apfs.get-dev-by-role</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.private.amfi.can-allow-non-platform</key>
 	<true/>
+	<key>com.apple.private.delegate-signals</key>
+	<true/>
 	<key>com.apple.private.iokit.system-nvram-allow</key>
 	<true/>
 	<key>com.apple.private.kernel.darkboot</key>

```
### csfdiagnose

> `/usr/bin/csfdiagnose`

```diff

 <dict>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.generativeexperiences.availabilityService</key>
+	<true/>
+	<key>com.apple.generativeexperiences.availabilityService.waitlistStatus</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.ind.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.generativeexperiences.availabilityService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

 	<true/>
 	<key>com.apple.private.vfs.snapshot</key>
 	<true/>
+	<key>com.apple.private.vfs.support-long-paths</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/</string>

```
### gcore

> `/usr/bin/gcore`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.security.cs.debugger.read.root</key>
 	<true/>
 </dict>

```
### ktrace

> `/usr/bin/ktrace`

```diff

 <dict>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
+	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kernel-info</key>
 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
+	<key>com.apple.private.logging.admin</key>
+	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleProcessorTraceUserClient</string>
+	</array>
 </dict>
 </plist>
 

```
### modelcatalogdump

> `/usr/bin/modelcatalogdump`

```diff

 	<string>com.apple.modelcatalogtool</string>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
+	<key>com.apple.modelcatalog.subscriptions</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>AppleIntelligence.Availability</string>
+		<string>ModelCatalog.Subscriptions.ExplicitRequests</string>
+	</array>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.modelcatalogtool</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ModelCatalogSubscriptionEvaluation</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Availability</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>ModelCatalog.Subscriptions.ExplicitRequests</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/mobile/Library/UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.modelcatalog.subscriptions</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biome.compute.source.user</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.CloudSubscriptionFeatures.gmBypass</string>
 		<string>com.apple.modelcatalog.ajax</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### modelmanagerdump

> `/usr/bin/modelmanagerdump`

```diff

 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOReportUserClient</string>
+		<string>AGXDeviceUserClient</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/db/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### mpsgraphtool

> `/usr/bin/mpsgraphtool`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.aned.private.adapterWeight.allow</key>
+	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
 	<key>com.apple.networking.ethernet.user-access</key>

```
### qlmanage

> `/usr/bin/qlmanage`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.private.dmd.policy</key>
-	<true/>
-	<key>com.apple.private.screen-time</key>
-	<true/>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.security.cs.disable-library-validation</key>
 	<true/>
 	<key>com.apple.security.get-task-allow</key>

```
### shortcuts

> `/usr/bin/shortcuts`

```diff

 		<string>iCloud.is.workflow.my.workflows</string>
 	</array>
 	<key>com.apple.private.amfi.version-restriction</key>
-	<integer>1</integer>
+	<integer>2</integer>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-groups</key>
-	<array>
-		<string>group.com.apple.shortcuts</string>
-		<string>group.is.workflow.my.app</string>
-		<string>group.is.workflow.shortcuts</string>
-	</array>
-	<key>com.apple.security.application-groups</key>
-	<array>
-		<string>group.com.apple.shortcuts</string>
-		<string>group.is.workflow.my.app</string>
-		<string>group.is.workflow.shortcuts</string>
-	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### slogin

> `/usr/bin/slogin`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.ssh.passphrases</string>

```
### ssh

> `/usr/bin/ssh`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.ssh.passphrases</string>

```
### ssh-add

> `/usr/bin/ssh-add`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.ssh.passphrases</string>

```
### tailspin

> `/usr/bin/tailspin`

```diff

 <dict>
 	<key>com.apple.logd.admin</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
 	<key>com.apple.private.kernel.ktrace-background</key>

 	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleProcessorTraceUserClient</string>
+		<string>AppleHWAccessUserClient</string>
+	</array>
 	<key>com.apple.system-task-ports.read</key>
 	<true/>
 	<key>com.apple.tailspin.config-apply</key>
 	<true/>
+	<key>com.apple.tailspin.cputrace</key>
+	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
 	<key>com.apple.tailspin.symbolication</key>

```
### trace

> `/usr/bin/trace`

```diff

 <dict>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
+	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kernel-info</key>
 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
+	<key>com.apple.private.logging.admin</key>
+	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleProcessorTraceUserClient</string>
+	</array>
 </dict>
 </plist>
 

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.private.AuthenticationServicesAgent</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>
 	<dict>
 		<key>appData</key>

 		<string>com.apple.security.octagon</string>
 		<string>com.apple.password-manager</string>
 		<string>lockdown-identities</string>
+		<string>com.apple.cfnetwork.testing</string>
+		<string>com.apple.webkit.webauthn.testing</string>
+		<string>com.apple.password-manager.testing</string>
 		<string>com.apple.password-manager.personal</string>
+		<string>com.apple.password-manager.personal.testing</string>
 		<string>com.apple.cfnetwork-recently-deleted</string>
+		<string>com.apple.cfnetwork-recently-deleted.testing</string>
 		<string>com.apple.password-manager-recently-deleted</string>
+		<string>com.apple.password-manager-recently-deleted.testing</string>
 		<string>com.apple.webkit.webauthn-recently-deleted</string>
+		<string>com.apple.webkit.webauthn-recently-deleted.testing</string>
 		<string>com.apple.password-manager.personal-recently-deleted</string>
+		<string>com.apple.password-manager.personal-recently-deleted.testing</string>
 		<string>com.apple.managed.passkey.attestation</string>
+		<string>com.apple.managed.passkey.attestation.testing</string>
 	</array>
 </dict>
 </plist>

```
### DumpPanic

> `/usr/libexec/DumpPanic`

```diff

 	</array>
 	<key>com.apple.private.coredump-encryption-key</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.DumpPanic</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>PanicPatternMatching</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Diagnostics.Panic</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>
 	<key>com.apple.private.security.disk-device-access</key>

 	<true/>
 	<key>com.apple.rootless.volume.VM</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>AppleNVMeNamespaceUC</string>
 	<key>com.apple.security.system-groups</key>

```
### MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

 	<true/>
 	<key>com.apple.private.apfs.allocate_contig</key>
 	<true/>
+	<key>com.apple.private.apfs.get-graft-info</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.apfs.trim-active-file</key>
 	<true/>
 	<key>com.apple.private.oop-jit.dir-manager</key>
 	<true/>
+	<key>com.apple.private.security.bootpolicy</key>
+	<true/>
 	<key>com.apple.private.security.disk-device-access</key>
 	<true/>
+	<key>com.apple.private.vfs.exclave-fs-register</key>
+	<true/>
+	<key>com.apple.private.vfs.graftdmg</key>
+	<true/>
 	<key>com.apple.private.vfs.snapshot</key>
 	<true/>
 	<key>com.apple.rootless.install</key>

```
### MobileStorageMounter

> `/usr/libexec/MobileStorageMounter`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileStorageMounter</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.job-manager</key>
+	<string>com.apple.mobile.storage_mounter</string>
 	<key>com.apple.private.xpc.launchd.storage-mounter</key>
 	<true/>
 	<key>com.apple.rootless.storage.MobileStorageMounter</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.debug</key>

```
### PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

 	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>
 	<true/>
+	<key>com.apple.private.mobilestoredemo.enabledemo</key>
+	<array>
+		<string>Manage</string>
+	</array>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.powersource-read</key>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	<true/>
 	<key>com.apple.private.ioaccelmemoryinfo</key>
 	<true/>
+	<key>com.apple.private.kernel.get-kext-info</key>
+	<true/>
 	<key>com.apple.private.nehelper.privileged</key>
 	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>application-identifier</key>
 	<string>com.apple.iad-cloudkit</string>
 	<key>aps-connection-initiate</key>

```
### airportd

> `/usr/libexec/airportd`

```diff

 	<true/>
 	<key>com.apple.countryd.contribute</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

 	<true/>
 	<key>com.apple.networkd_privileged</key>
 	<true/>
+	<key>com.apple.private.SkyLight.displaycontrol</key>
+	<true/>
 	<key>com.apple.private.SkyLight.event.monitor</key>
 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>

```
### amfid

> `/usr/libexec/amfid`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.amfi.developer-mode-control</key>
 	<true/>
 	<key>com.apple.private.iokit.nvram-read-access</key>

```
### aned

> `/usr/libexec/aned`

```diff

 	<true/>
 	<key>com.apple.ane.iokit-user-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.ANEStorageMaintainer.allow</key>
 	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<string></string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.appleaccountd</string>
+	<key>com.apple.authkit.birthday</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.cdp.recoverykey</key>

 	<true/>
 	<key>com.apple.cdp.walrus.pcskeys</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>
-	<key>com.apple.private.security.storage.IntelligencePlatform</key>
-	<true/>
 	<key>com.apple.private.security.storage.appleaccountd</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

 	<true/>
 	<key>com.apple.PairingManager.Write</key>
 	<true/>
+	<key>com.apple.account.dca.fullaccess</key>
+	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
 	<key>com.apple.appleidsetup.repair.client</key>

 	<true/>
 	<key>com.apple.familycircle.agent</key>
 	<true/>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
 	<array>
 		<string>Removal</string>

 		<key>value</key>
 		<string>/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService</string>
 	</dict>
+	<key>com.apple.private.followup</key>
+	<true/>
 	<key>com.apple.private.game-center</key>
 	<array>
 		<string>Account</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.icloud.findmydeviced</string>
 		<string>com.apple.ak.anisette.xpc</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.frontboard.systemappservices</string>

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.userprofiles</string>
-		<string>com.apple.PineBoardRiseServices</string>
+		<string>com.apple.corefollowup.agent</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### asktod

> `/usr/libexec/asktod`

```diff

 <dict>
 	<key>com.apple.askto.extension.host</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.people.legacy.service.extension</key>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 	<true/>
 	<key>com.apple.mediaremote.restrict-command-clients</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
+	<key>com.apple.private.managedclient.configurationprofiles</key>
+	<true/>
 	<key>com.apple.private.managedclient.configurationprofiles.installsource</key>
 	<string>AutomaticAssessmentConfiguration</string>
 	<key>com.apple.private.nehelper.privileged</key>

 		<string>com.apple.siri.invoke</string>
 		<string>com.apple.mdmclient.agent</string>
 		<string>com.apple.mdmclient.daemon</string>
+		<string>com.apple.lsd.mapdb</string>
+		<string>com.apple.lsd.modifydb</string>
+		<string>com.apple.CoreServices.coreservicesd</string>
 	</array>
 </dict>
 </plist>

```
### atcrtcomm

> `/usr/libexec/atcrtcomm`

```diff

 <dict>
 	<key>com.apple.driver.AppleTypeCRetimer.user-access</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleTypeCRetimerUserClient</string>

```
### audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

 	<true/>
 	<key>com.apple.launchservices.MoveDocumentOnOpen</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.CarveoutProperty</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.AudioAnalytics</string>

 		<string>IOHIDLibUserClient</string>
 		<string>AppleSPUHIDDeviceUserClient</string>
 		<string>IOReportUserClient</string>
+		<string>AppleProcessorTraceUserClient</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>

```
### avconferenced

> `/usr/libexec/avconferenced`

```diff

 	<true/>
 	<key>com.apple.developer.game-center</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
 	<key>com.apple.imagent.av</key>

```

### 🆕 betaenrollmentagent

> `/usr/libexec/betaenrollmentagent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.betaenrollmentagent</string>
	<key>com.apple.MobileAsset.SoftwareUpdate</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.seeding</string>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.allow-nsurlsession-proxy</key>
	<true/>
	<key>com.apple.private.assets.change-daemon-config</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.seeding</string>
	</array>
	<key>com.apple.private.softwareupdate.preferences</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.seeding.daemon.entitlement</key>
	<true/>
</dict>
</plist>

```
### betaenrollmentd

> `/usr/libexec/betaenrollmentd`

```diff

 	<string>com.apple.betaenrollmentd</string>
 	<key>com.apple.MobileAsset.SoftwareUpdate</key>
 	<true/>
-	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
-	<true/>
-	<key>com.apple.authkit.client.internal</key>
-	<true/>
-	<key>com.apple.authkit.client.private</key>
-	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
-	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
-	<string>com.apple.seeding</string>
-	<key>com.apple.private.accounts.allaccounts</key>
-	<true/>
 	<key>com.apple.private.allow-nsurlsession-proxy</key>
 	<true/>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
-	<key>com.apple.private.coreservices.canmaplsdatabase</key>
-	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.seeding</string>

 	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
-	<key>com.apple.seeding.client-helper</key>
-	<true/>
 </dict>
 </plist>
 

```
### bluetoothuserd

> `/usr/libexec/bluetoothuserd`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	</array>
 	<key>com.apple.private.ids.identityservicesd</key>
 	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.icloudpairing</string>
+	</array>
+	<key>com.apple.private.ids.messaging.high-priority</key>
+	<array>
+		<string>com.apple.private.alloy.icloudpairing</string>
+	</array>
 	<key>com.apple.private.ids.registration</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### ciphermld

> `/usr/libexec/ciphermld`

```diff

 	<string>com.apple.ciphermld</string>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.pegasus.context</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.PegasusConfiguration</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.ciphermld/</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.networkserviceproxy</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.kvsd</string>
 		<string>com.apple.CipherMLService</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.parsecd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.parsecd</string>
 		<string>com.apple.itunesstored</string>
 		<string>com.apple.jett.switch-itms</string>
 	</array>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<true/>
 	<key>com.apple.appletv.pbs.user-profiles</key>
 	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authentication-services-core.allow-authentication-request-proxying</key>
 	<true/>
 	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.carousel.wakegesturemonitor</key>
 	<true/>
 	<key>com.apple.companionuiservice.client</key>

 	<string>production</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
+	<key>com.apple.locationd.effective-bundle</key>
+	<true/>
+	<key>com.apple.locationd.usage-oracle</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

 	</array>
 	<key>com.apple.private.userprofiles.read</key>
 	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Applications/</string>

 		<string>/Library/Preferences/SystemConfiguration/preferences.plist</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Application Support/com.apple.DistributedTimers/</string>

 	<array>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.ak.authorizationservices.xpc</string>
+		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent</string>
+		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.carousel.wakegesturemonitor</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.CompanionLink</string>

 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.homehubd.manage</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.mediator</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.MobileTimer.alarmserver</string>
 		<string>com.apple.MobileTimer.timerserver</string>
 		<string>com.apple.PineBoardServices</string>

```
### configd

> `/usr/libexec/configd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.networkd.modify_settings</key>
 	<true/>
 	<key>com.apple.networkd_privileged</key>

 	</array>
 	<key>com.apple.private.vfs.allow-low-space-writes</key>
 	<true/>
+	<key>com.apple.rootless.volume.Preboot</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>IO80211APIUserClient</string>

```
### corecaptured

> `/usr/libexec/corecaptured`

```diff

 	<true/>
 	<key>com.apple.corecaptured.remoteservice-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.coreduetd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>ShareSheetFeedback</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>ShareSheet.Feedback</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.kernel.system-override</key>

```
### cryptexd

> `/usr/libexec/cryptexd`

```diff

 	<array>
 		<string>kTCCServiceSystemPolicySysAdminFiles</string>
 	</array>
+	<key>com.apple.private.unload-trust-cache</key>
+	<true/>
 	<key>com.apple.private.vfs.graftdmg</key>
 	<true/>
 	<key>com.apple.private.xpc.allowed-launch-types</key>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.computesafeguards.managing.allow</key>
+	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>

 		<string>Activity.Level</string>
 		<string>ContextSync.DeviceActivityLevel</string>
 		<string>App.InFocus</string>
+		<string>App.Install</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>ActivityScheduler.Dependency.Completion</string>
 		<string>ActivityScheduler.Dependency.Result</string>
+		<string>Device.Thermals.BatteryTemperature</string>
 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>AppResumeBiomeUseCase</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Device.Power.PluggedIn</string>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
+		<key>DuetActivitySchedulerAppPredictions</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>App.InFocus</string>
+			</array>
+		</dict>
 		<key>PhotosIntentSyncRemoteDeviceActivity</key>
 		<dict>
 			<key>Streams</key>

 	<array>
 		<string>/Library/DuetActivityScheduler/</string>
 		<string>/Library/Logs/CrashReporter/</string>
+		<string>/Library/Trial/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.commcenter.carrierspace.xpc</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
+		<string>com.apple.computesafeguards.managing</string>
 		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.coremedia.cameraviewfinder</string>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>COREOS_DAS</string>
-		<string>252</string>
+		<string>COREOS_APRS</string>
+		<string>COREOS_CLAS</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

 	<false/>
 	<key>com.apple.rootless.datavault.metadata</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<string>AppleAPFSUserClient</string>
 </dict>
 </plist>
 

```
### dmd

> `/usr/libexec/dmd`

```diff

 	<true/>
 	<key>com.apple.private.configurationprofiles.readwrite</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
 	<key>com.apple.private.managedclient.mdmclient-private</key>

```
### feedbackd

> `/usr/libexec/feedbackd`

```diff

 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.appleseed.FeedbackAssistant</string>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.surfboard.application-service-client</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.private.dark-wake-push</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
+	<true/>
 	<key>com.apple.private.findmymacd.spi</key>
 	<true/>
 	<key>com.apple.private.icloud.FindMyDeviceBridge.access</key>

```
### findmylocateagent

> `/usr/libexec/findmylocateagent`

```diff

 	<string>com.apple.findmy.findmylocateagent</string>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.chrono.invalidate-timelines</key>
+	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.icloud.findmydeviced.access</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.securelocations.access</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<array>
 		<string>com.apple.private.alloy.fmf.local</string>
 		<string>com.apple.private.alloy.fmf</string>
+		<string>com.apple.private.alloy.fmd</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
 		<string>com.apple.private.alloy.fmf</string>
 		<string>com.apple.private.alloy.fmf.local</string>
+		<string>com.apple.private.alloy.fmd</string>
 	</array>
 	<key>com.apple.private.ids.registration</key>
 	<true/>

 	<key>com.apple.private.ids.session</key>
 	<array>
 		<string>com.apple.private.alloy.fmf</string>
+		<string>com.apple.private.alloy.fmd</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>
 	<array>
 		<string>com.apple.private.alloy.fmf</string>
+		<string>com.apple.private.alloy.fmd</string>
 	</array>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.security.allow-migration</key>
 	<true/>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>

 		<string>com.apple.cloudd</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
+		<string>com.apple.icloud.findmydeviced</string>
+		<string>com.apple.chronoservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### fskitd

> `/usr/libexec/fskitd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>application-identifier</key>
-	<string>com.apple.filesystems.fskitd</string>
 	<key>com.apple.application-identifier</key>
-	<string>com.apple.filesystems.fskitd</string>
+	<string>com.apple.fskitd</string>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.private.LiveFS.connection</key>

 	<true/>
 	<key>com.apple.private.fskit.module-runner</key>
 	<true/>
-	<key>com.apple.private.security.restricted-application-group</key>
+	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.fskit.settings</string>
 	</array>

 	<array>
 		<string>group.com.apple.fskit.settings</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/LiveFiles/</string>
-	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.fskit.fskit_agent</string>
-	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>AppleLIFSUserClient</string>
 </dict>

```

### 🆕 gamed

> `/usr/libexec/gamed`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>NSBonjourServices</key>
	<array>
		<string>_gamed._tcp</string>
	</array>
	<key>application-identifier</key>
	<string>com.apple.gamed</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>aps-environment</key>
	<string>serverPreferred</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.gamed</string>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.people</key>
	<true/>
	<key>com.apple.datadetectors.source-write.user</key>
	<true/>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Production</string>
	<key>com.apple.developer.icloud-database-environment</key>
	<string>development</string>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.notificationcenter-identifiers</key>
	<array>
		<string>com.apple.gamecenter</string>
	</array>
	<key>com.apple.developer.usernotifications.time-sensitive</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>PurchaseHistory</string>
		<string>CrossFire</string>
		<string>Library</string>
		<string>Ocelot</string>
		<string>IAPHistory</string>
	</array>
	<key>com.apple.private.aps-connection-initiate</key>
	<true/>
	<key>com.apple.private.biome.writer</key>
	<string>GameCenter.AchievementEarned</string>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.commerce</key>
	<array>
		<string>Accounts</string>
	</array>
	<key>com.apple.private.commercekit.appstore</key>
	<true/>
	<key>com.apple.private.corerecents</key>
	<true/>
	<key>com.apple.private.ids.registration</key>
	<array>
		<string>com.apple.private.alloy.arcade</string>
		<string>com.apple.private.alloy.arcade.fastsync</string>
	</array>
	<key>com.apple.private.ids.remoteurlconnection</key>
	<true/>
	<key>com.apple.private.imcore.imagent</key>
	<true/>
	<key>com.apple.private.imcore.imdpersistence.database-access</key>
	<true/>
	<key>com.apple.private.imcore.imremoteurlconnection</key>
	<true/>
	<key>com.apple.private.imcore.imtranscoderservice</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>GameCenterLibraryRecentlyPlayed</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>App.InFocus</string>
			</array>
		</dict>
		<key>GameCenterSuggestionFeedback</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>GameCenter.SuggestionFeedback</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.nsurlsession.impersonate</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.gamecenter</string>
	</array>
	<key>com.apple.private.security.storage.coreduet_knowledge_store</key>
	<true/>
	<key>com.apple.private.suggestions.contacts</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceLiverpool</string>
		<string>kTCCServiceUbiquity</string>
		<string>kTCCServiceGameCenterFriends</string>
	</array>
	<key>com.apple.private.tcc.allow-prompting</key>
	<array>
		<string>kTCCServiceGameCenterFriends</string>
	</array>
	<key>com.apple.private.tcc.allow.overridable</key>
	<array>
		<string>kTCCServiceGameCenterFriends</string>
	</array>
	<key>com.apple.private.tcc.manager.access.delete</key>
	<array>
		<string>kTCCServiceGameCenterFriends</string>
	</array>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceGameCenterFriends</string>
	</array>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.gamecenter</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.gamecenter</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Applications/</string>
	</array>
	<key>com.apple.security.exception.files.home-subpath.read-write</key>
	<array/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.MobileSMS</string>
		<string>com.apple.messages</string>
		<string>com.apple.applicationaccess</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.AppStoreComponents</string>
	</array>
	<key>com.apple.security.lockdownmode.read</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.personal-information.addressbook</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.storeagent-xpc</string>
		<string>com.apple.ak.anisette.xpc</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.usernotifications.usernotificationservice</string>
		<string>com.apple.usernotifications.listener</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.GameOverlayUI</string>
		<string>com.apple.GameOverlayUIInternal</string>
	</array>
	<key>item1</key>
	<string>/Library/Caches/com.apple.AppleMediaServices</string>
</dict>
</plist>

```
### handwritingd

> `/usr/libexec/handwritingd`

```diff

 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keyboardservices.textreplacement.allow</key>
 	<true/>
 	<key>com.apple.modelcatalog.full-access</key>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.modelcatalog.catalog</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 historicalaudiod

> `/usr/libexec/historicalaudiod`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.private.audio.hal.aop-audio.user-access</key>
	<true/>
	<key>com.apple.private.audio.hal.speaker-tap.user-access</key>
	<true/>
	<key>com.apple.private.audio.orchestration.registration</key>
	<true/>
	<key>com.apple.private.exclaves.conclave-host</key>
	<true/>
	<key>com.apple.private.mediaexperience.usesecuresession</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>kern.task_conclave</string>
		<string>com.apple.audio.orchestrator.registrar.service</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>kern.exclaves_status</string>
		<string>kern.task_conclave</string>
	</array>
</dict>
</plist>

```
### icloudmailagent

> `/usr/libexec/icloudmailagent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
-	<string></string>
+	<string>com.apple.icloudmailagent</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.aps-environment</key>
+	<string>production</string>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.icloudmailagent</string>
+	<key>com.apple.pds.clientid</key>
+	<array>
+		<string>com.apple.aps.icloud.mcc</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.private.corespotlight.bundleid</key>
-	<string></string>
+	<string>com.apple.icloudmailagent</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.mail</string>

 	<array>
 		<string>group.com.apple.mail</string>
 	</array>
-	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.apsd</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/Trial/</string>
+	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>1500</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### keychainsharingmessagingd

> `/usr/libexec/keychainsharingmessagingd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.kcsharing.invite</string>

```
### linkd

> `/usr/libexec/linkd`

```diff

 	<string>com.apple.linkd</string>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.linkd.registry</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 		<string>kTCCServiceSystemPolicyDocumentsFolder</string>
 		<string>kTCCServiceSystemPolicyDownloadsFolder</string>
 	</array>
-	<key>com.apple.security.automation.apple-events</key>
+	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
-	<key>com.apple.siri.koa.donate.internal</key>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
+	<key>com.apple.security.automation.apple-events</key>
 	<true/>
 </dict>
 </plist>

```

### 🆕 locationaccessstored

> `/usr/libexec/locationaccessstored`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.status</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.locationd.synchronous</string>
		<string>com.apple.duetactivityscheduler</string>
	</array>
</dict>
</plist>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<array>
 		<string>com.apple.private.wifi.driverkit</string>
 	</array>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
+		<string>com.apple.eligibilityd</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### logd

> `/usr/libexec/logd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.notify.root_access</key>
 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>

```
### mc_notifier

> `/usr/libexec/mc_notifier`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.smbfs.update-notifier-pid</key>
+	<true/>
+</dict>
+</plist>
 

```
### mdmclient

> `/usr/libexec/mdmclient`

```diff

 		<string>DaemonManaged</string>
 		<string>ManagedApp</string>
 		<string>upp</string>
+		<string>Update</string>
 	</array>
 	<key>com.apple.private.aps-client-cert-access</key>
 	<true/>

```

### 🆕 micactivityd

> `/usr/libexec/micactivityd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.audio.orchestration.registration</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.audio.isolated.client.service</string>
	</array>
</dict>
</plist>

```
### mlhostd

> `/usr/libexec/mlhostd`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.mlhost</string>

 	<true/>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

```
### mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

 	</array>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>2010</string>
 		<string>551</string>
 	</array>
 </dict>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	<array>
 		<string>/private/var/run/MobileAssetCritialDomainsUpdated.plist</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
+		<string>/private/var/run/MobileAssetSuspendSystemOptionalForSoftwareUpdate.nonce</string>
 		<string>/private/var/code_coverage/</string>
 		<string>/private/var/run/com.apple.mobileassetd-AutoAsset-DeviceBoot-UUID</string>
 	</array>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 	<string>com.apple.thimble.thtool</string>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.ane.memoryUnwiringOptOutAccess.allow</key>
+	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
 	<key>com.apple.developer.ane.increased-model-size-limit</key>

 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.FM.Visual</string>
 		<string>com.apple.MobileAsset.UAF.IF.Planner</string>
+		<string>com.apple.MobileAsset.CN.Guardrail</string>
 	</array>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.modelmanagerd</string>

 	<key>com.apple.private.extensionkit.host.unsandboxed-extensions-for-extension-points</key>
 	<array>
 		<string>com.apple.modelmanager.inferenceprovider</string>
+		<string>com.apple.modelmanager.inferenceprovider.safety</string>
 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>

```
### naturallanguaged

> `/usr/libexec/naturallanguaged`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.naturallanguaged</string>
+	<key>com.apple.generativeexperiences.textcomposition</key>
+	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 </dict>
 </plist>
 

```
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.security.storage.Location</key>
 	<true/>
+	<key>com.apple.private.sessionkit.listener</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.coremedia.mediaplaybackd.player.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.remaker.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.sandboxserver.xpc</string>
+		<string>com.apple.sessionservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### nfcd

> `/usr/libexec/nfcd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>
 	<true/>
 	<key>com.apple.keystore.sik.access</key>

```
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.nsurlsessiond</string>
 	<key>com.apple.chronoservices</key>

```
### pboard

> `/usr/libexec/pboard`

```diff

 <dict>
 	<key>com.apple.private.coreservices.useractivityd.sharedpasteboard</key>
 	<true/>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 pcapd

> `/usr/libexec/pcapd`

- No entitlements *(yet)*
### powerexperienced

> `/usr/libexec/powerexperienced`

```diff

 		<string>AppleCLPCUserClient</string>
 		<string>AppleSMCClient</string>
 	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>364</string>
+	</array>
 </dict>
 </plist>
 

```
### powerlogHelperd

> `/usr/libexec/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.launch-xpc</key>
 	<true/>
+	<key>com.apple.PerfPowerServices.signpost-reading</key>
+	<true/>
 	<key>com.apple.PerformanceTrace.Tracing</key>
 	<true/>
 	<key>com.apple.QuartzCore.debug</key>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2463478364</string>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>spi</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	<string>com.apple.rapportd</string>
 	<key>com.apple.CompanionLink</key>
 	<true/>
-	<key>com.apple.Contacts.database-allow</key>
-	<true/>
 	<key>com.apple.PairingManager.HomeKit</key>
 	<true/>
 	<key>com.apple.PairingManager.Read</key>

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Development</string>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
+	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
+	<array>
+		<string>com.apple.network.application-service</string>
+	</array>
+	<key>com.apple.findmy.findmylocate.friendshipservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.frontboard.debugapplications</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.ckks</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
+	<key>com.apple.private.cloudkit.systemService</key>
+	<true/>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmapbundleidtouuid</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceBluetoothPeripheral</string>
 		<string>kTCCServiceWillow</string>

 	<array>
 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.CompanionLink</string>
+		<string>com.apple.findmy.findmylocate.settings</string>
+		<string>com.apple.findmy.findmylocate.friendshipservice</string>
+		<string>com.apple.findmy.findmylocate.locationservice</string>
 		<string>com.apple.rapport</string>
 		<string>com.apple.rapport.NearbyInvitation</string>
 		<string>com.apple.securityd.ckks</string>
 		<string>com.apple.SharedWebCredentials</string>
 		<string>com.apple.SiriVOXService.client</string>
+		<string>com.apple.StatusKit.local</string>
+		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>

 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.SBUserNotification</string>
-		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.cloudd</string>
+		<string>com.apple.contactsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>com.apple.wifi.awdl</key>

```
### relatived

> `/usr/libexec/relatived`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-protected</key>
+	<true/>
 	<key>com.apple.hid.system.fast-path-motion-event-privileged</key>
 	<true/>
 	<key>com.apple.hid.system.user-access-fast-path</key>

```
### remoted

> `/usr/libexec/remoted`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>
 	<true/>
 	<key>com.apple.keystore.filevault</key>

```
### retimerd

> `/usr/libexec/retimerd`

```diff

 <dict>
 	<key>com.apple.driver.AppleTypeCRetimer.user-access</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleTypeCRetimerUserClient</string>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
+	<key>com.apple.aonsensed.xpc</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.routined</string>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.developer.extension-host.widget-extension</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### runningboardd

> `/usr/libexec/runningboardd`

```diff

 	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.pluginkit.manager</key>
 	<true/>
 	<key>com.apple.private.process.suspend-resume.any</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.findmy.findmylocate.locationservice</key>
+	<true/>
+	<key>com.apple.findmy.findmylocate.settings</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>

 	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.registration</key>

 	<true/>
 	<key>com.apple.private.ids.session</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

```
### searchpartyuseragent

> `/usr/libexec/searchpartyuseragent`

```diff

 	</array>
 	<key>com.apple.findmy.findmybeaconingd.push</key>
 	<true/>
+	<key>com.apple.findmy.findmylocate.fenceservice</key>
+	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.registration</key>

 	<true/>
 	<key>com.apple.private.ids.session</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>
 	<array>
-		<string>com.apple.private.alloy.fmd</string>
 		<string>com.apple.private.alloy.findmy.itemsharing-crossaccount</string>
 	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	<true/>
 	<key>com.apple.dmd.operation.fetch-classroom-instructor-endpoint</key>
 	<true/>
+	<key>com.apple.extensionkit.host.extension-point-identifiers</key>
+	<array>
+		<string>com.apple.share-services</string>
+		<string>com.apple.ui-services</string>
+		<string>com.apple.services</string>
+	</array>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.locationservice</key>

 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 		<string>PURGE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.CloudSharing.SPI</key>
+	<true/>
 	<key>com.apple.private.SkyLight.displaycontrol</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<array>
 		<string>group.com.apple.sharingd</string>
 	</array>
+	<key>com.apple.private.security.storage-exempt</key>
+	<true/>
 	<key>com.apple.private.security.storage.AirDrop</key>
 	<true/>
 	<key>com.apple.private.security.storage.HomeKit</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.containermanagerd</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/com.apple.sharingd/ShareSheetTestingSnapshots/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>IO80211APIUserClient</string>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/assetsubscriptiond/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.orchestration.capabilities</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.SystemConfiguration.configd</string>
 		<string>com.apple.triald.namespace-management</string>

 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.medialibraryd.xpc</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.feedbacklogger</string>

 		<string>com.apple.AppSupport</string>
 		<string>com.apple.triald</string>
 		<string>com.apple.mobilecal</string>
+		<string>com.apple.siri.inference.EntityMatcher</string>
+		<string>com.apple.siri.vocabulary</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.siri.embeddedspeech</key>
 	<true/>
+	<key>com.apple.siri.orchestration.capabilities</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

 	<true/>
 	<key>com.apple.pf.allow</key>
 	<true/>
+	<key>com.apple.private.ctr.thread</key>
+	<true/>
 	<key>com.apple.private.fillmore.AccessoryInfo.modification</key>
 	<true/>
 	<key>com.apple.private.fillmore.prefix.modification</key>

```
### studentd

> `/usr/libexec/studentd`

```diff

 	<true/>
 	<key>com.apple.developer.ClassKit-environment</key>
 	<string>production</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.dmd-access</key>
 	<true/>
 	<key>com.apple.dmd.operation.fetch-safari-bookmarks</key>

```
### swtransparencyd

> `/usr/libexec/swtransparencyd`

```diff

 	<array>
 		<string>group.com.apple.swtransparency</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.osanalytics</string>
+	</array>
 </dict>
 </plist>
 

```
### syspolicyd

> `/usr/libexec/syspolicyd`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.cloudtelemetry</key>
+	<true/>
 	<key>com.apple.private.endpoint-security.submit.gatekeeper</key>
 	<true/>
 	<key>com.apple.private.endpoint-security.submit.xp</key>

 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceSystemPolicyAllFiles</string>
 	</array>
+	<key>com.apple.private.tcc.external.report</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
 		<string>kTCCServiceDeveloperTool</string>

```

### 🆕 systemservicemonitord

> `/usr/libexec/systemservicemonitord`

- No entitlements *(yet)*
### tailspind

> `/usr/libexec/tailspind`

```diff

 	<true/>
 	<key>com.apple.logd.admin</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
 	<key>com.apple.private.kernel.ktrace-background</key>

 	<array>
 		<string>com.apple.tailspin.notifications</string>
 	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleProcessorTraceUserClient</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### testmanagerd

> `/usr/libexec/testmanagerd`

```diff

 	<true/>
 	<key>com.apple.private.screencapturekit.noprompt</key>
 	<true/>
+	<key>com.apple.private.screencapturekit.suppress-screen-indicator</key>
+	<true/>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
 	<key>com.apple.private.spindump.generatespindump</key>

 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 		<string>kTCCServiceAppleEvents</string>
 	</array>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.ts.play-media</key>
 	<true/>
 	<key>com.apple.tailspin.dump-output</key>

```

### 🆕 textunderstandingd

> `/usr/libexec/textunderstandingd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.application-identifier</key>
	<string>com.apple.textunderstandingd</string>
	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
	<true/>
	<key>com.apple.fileprovider.acl-read</key>
	<true/>
	<key>com.apple.fileprovider.acl-write</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.fileprovider.extension-host</key>
	<true/>
	<key>com.apple.fileprovider.fetch-url</key>
	<true/>
	<key>com.apple.intelligenceplatform.EntityResolution</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.mediaanalysisd.analysis</key>
	<true/>
	<key>com.apple.mediaanalysisd.client</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
	</array>
	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
	<array>
		<string>photos.person</string>
		<string>photos.face</string>
	</array>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.textunderstandingd</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>TextUnderstanding.DocumentUnderstanding.PoemBuffer</string>
		<string>TextUnderstanding.DocumentUnderstanding.Poem</string>
		<string>TextUnderstanding.DocumentUnderstanding.PoemAnalytics</string>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
	</array>
	<key>com.apple.private.corespotlight.bundleid</key>
	<string>com.apple.FileProvider.LocalStorage</string>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
		<string>entityAliasECR</string>
		<string>entitySubgraph</string>
		<string>entitySummary</string>
		<string>eventSubgraph</string>
		<string>peopleSubgraph</string>
		<string>inferenceFeaturesECR</string>
		<string>personEntityRelevanceRanking</string>
		<string>appEntityRelevanceRanking</string>
		<string>loiEntityRelevanceRanking</string>
	</array>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.security.storage.TextUnderstanding</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.proactive.experiments.responses</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXDeviceUserClient</string>
		<string>IOSurfaceRootUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>H11ANEInDirectPathClient</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>SMART_REPLY_EN</string>
		<string>UNDERSTANDING_PLATFORM_DOCUMENT_UNDERSTANDING</string>
		<string>UNDERSTANDING_PLATFORM_FOUND_IN</string>
		<string>UNDERSTANDING_PLATFORM_POEM</string>
	</array>
	<key>com.apple.webkit-client</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### transparencyStaticKey

> `/usr/libexec/transparencyStaticKey`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.transparencyStaticKey</string>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	<true/>
 	<key>com.apple.cdp.utility</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.transparency.transparencyd</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.ProtectedCloudStorage.KTAccountKey</string>

```
### triald

> `/usr/libexec/triald`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>

 	<array>
 		<string>Siri.AnalyticsIdentifiers.UserAggregationId</string>
 	</array>
-	<key>com.apple.private.biome.read-write</key>
-	<string>Lighthouse.Ledger.TrialdEvent</string>
 	<key>com.apple.private.cloudkit.buddyAccess</key>
 	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>NamespaceUpdates</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Trial.Experiment.NamespaceUpdates</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.cache_delete</string>
 		<string>com.apple.mobileasset.autoasset</string>

```
### triald_system

> `/usr/libexec/triald_system`

```diff

 	<string>com.apple.triald.system</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.triald.system</string>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriResponseFrameworkFiles</string>

```
### warmd

> `/usr/libexec/warmd`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
+</dict>
+</plist>
 

```
### watchdogd

> `/usr/libexec/watchdogd`

```diff

 	<true/>
 	<key>com.apple.private.apfs.key_migration</key>
 	<true/>
+	<key>com.apple.private.endpoint-security.client</key>
+	<true/>
+	<key>com.apple.private.endpoint-security.default-muter</key>
+	<true/>
+	<key>com.apple.private.endpoint-security.embeddedclient</key>
+	<true/>
 	<key>com.apple.private.iowatchdog.user-access</key>
 	<true/>
 	<key>com.apple.private.security.storage.spindump</key>

 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>
 	<string>com.apple.watchdogd</string>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>EndpointSecurityExternalClient</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleAPFSUserClient</string>

```
### wifiFirmwareLoader

> `/usr/libexec/wifiFirmwareLoader`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>

```
### wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>

```
### wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
 	<array>
 		<string>Inspection</string>

```
### wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>

```
### wps

> `/usr/libexec/wps`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.private.driverkit.driver-access</key>
+	<array>
+		<string>com.apple.private.wifi.driverkit</string>
+	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>IOUserUserClient</string>
 		<string>IO80211APIUserClient</string>
 	</array>
+	<key>com.apple.wlan.authentication</key>
+	<true/>
 </dict>
 </plist>
 

```
### BTLEServer

> `/usr/sbin/BTLEServer`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.devicesharing.guest-user-mode-client</key>

 		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
 		<string>HKQuantityTypeIdentifierHeight</string>
 	</array>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.CallHistory</key>

```
### BTLEServerAgent

> `/usr/sbin/BTLEServerAgent`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.devicesharing.guest-user-mode-client</key>

 		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
 		<string>HKQuantityTypeIdentifierHeight</string>
 	</array>
+	<key>com.apple.private.osanalytics.write-logs.allow</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.CallHistory</key>

```
### WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

 		<string>spi</string>
 		<string>bb-xpc</string>
 	</array>
+	<key>com.apple.private.ctr.thread</key>
+	<true/>
 	<key>com.apple.private.driverkit.driver-access</key>
 	<array>
 		<string>com.apple.private.wifi.driverkit</string>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<array>
 		<string>com.apple.driver.driverkit.serial</string>
 		<string>com.apple.IOUserBluetoothSerialDriver</string>
+		<string>com.apple.AppleSunriseBluetooth</string>
 	</array>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
 	<key>com.apple.driver.AppleBluetoothModule.user-access</key>
 	<true/>
 	<key>com.apple.driver.AppleConvergedIPC.user-access</key>

 	<array>
 		<string>Device.Wireless.BluetoothGATTSession</string>
 		<string>Device.Wireless.BluetoothPowerEnabled</string>
+		<string>Device.Wireless.Bluetooth</string>
 	</array>
 	<key>com.apple.private.carkit</key>
 	<true/>

 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/usr/sbin/BTLEServer/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/log/CoreCapture/com.apple.KalBluetooth_driver/FwLogs/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### coreaudiod

> `/usr/sbin/coreaudiod`

```diff

 <dict>
 	<key>com.apple.modelmanager.inferenceMonitor</key>
 	<true/>
+	<key>com.apple.private.AppleProcessorTrace.Trace</key>
+	<true/>
 	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>

 		<string>com.apple.developer.driverkit.family.audio</string>
 		<string>com.apple.developer.driverkit.allow-any-userclient-access</string>
 	</array>
+	<key>com.apple.private.exclaves.kernel-domain</key>
+	<true/>
 	<key>com.apple.private.kernel.audio_latency</key>
 	<true/>
 	<key>com.apple.private.kernel.work-interval</key>

 	<string>com.apple.private.audio.coreaudiod</string>
 	<key>com.apple.rootless.storage.AudioSettings</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AppleProcessorTraceUserClient</string>
+		<string>AppleHWAccessUserClient</string>
+	</array>
 	<key>com.apple.systemstatus.publisher.domains</key>
 	<string>media</string>
+	<key>com.apple.tailspin.cputrace</key>
+	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
 </dict>

```
### filecoordinationd

> `/usr/sbin/filecoordinationd`

```diff

 	<true/>
 	<key>com.apple.private.vfs.dataless-resolver</key>
 	<true/>
+	<key>com.apple.private.vfs.support-long-paths</key>
+	<true/>
 </dict>
 </plist>
 

```
### mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.iokit.wakerequest</key>
 	<true/>
 	<key>com.apple.mDNSResponder_Helper</key>

```
### notifyd

> `/usr/sbin/notifyd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.developer.hardened-process</key>
+	<true/>
+	<key>com.apple.developer.hardened-process.hardened-heap</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.ios-system-session</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### softwareupdate

> `/usr/sbin/softwareupdate`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
+	<key>com.apple.private.iokit.assertonlidclose</key>
+	<true/>
 	<key>com.apple.private.logout.forcecontinue</key>
 	<true/>
 	<key>com.apple.private.opendirectoryd.ownership.read</key>

```
### usernoted

> `/usr/sbin/usernoted`

```diff

 	<key>com.apple.private.donotdisturb.settings.modify.client-identifiers</key>
 	<string>com.apple.private.ncprefs.dnd</string>
 	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
-	<string>com.apple.private.nc.usernoted</string>
+	<array>
+		<string>com.apple.private.nc.usernoted</string>
+		<string>com.apple.UserNotificationCore.SpotlightIndexer</string>
+	</array>
 	<key>com.apple.private.donotdisturb.state.updates.client-identifiers</key>
 	<string>com.apple.private.nc.usernoted</string>
 	<key>com.apple.private.ids.messaging</key>

```
