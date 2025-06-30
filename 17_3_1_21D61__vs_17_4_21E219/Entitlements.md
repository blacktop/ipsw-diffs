## 🔑 Entitlements

### AMSEngagementViewService

> `/Applications/AMSEngagementViewService.app/AMSEngagementViewService`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
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
+			<string>us-drivers-license</string>
+		</array>
+		<key>elements</key>
+		<array>
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
+		<string>com.apple.asa-identity-verification</string>
+	</array>
 	<key>com.apple.developer.pass-type-identifiers</key>
 	<array>
 		<string>*.pass.com.apple.itunes.storecredit</string>

 	<true/>
 	<key>com.apple.surfboard.disable-realitychrome</key>
 	<true/>
-	<key>com.apple.surfboard.scenesession-custom-focus-order</key>
-	<integer>2030</integer>
 	<key>com.apple.surfboard.scenesession-updates</key>
 	<true/>
 	<key>com.apple.surfboard.sharing-mode-launch-allowed</key>

```
### AirDropUI

> `/Applications/AirDropUI.app/AirDropUI`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.messages.collaboration-initiate-send</key>
+	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

```
### AirPlaySenderUIApp

> `/Applications/AirPlaySenderUIApp.app/AirPlaySenderUIApp`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.proactive.eventtracker</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.airplay.discoverybroker</string>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>313</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 AppDistributionLaunchAngel

> `/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.AppDistributionLaunchAngel</string>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.runningboard.assertions.angeltarget</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/JetPackCache/</string>
		<string>/Library/com.apple.AppleMediaServices/</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appstorecomponentsd.xpc</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
</dict>
</plist>

```
### AppStore

> `/Applications/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.appstored.xpc.updates</key>
 	<true/>
+	<key>com.apple.attributionkitd.impression-intake</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 		<string>Personalization</string>
 		<string>Update</string>
 		<string>PurchaseHistory</string>
+		<string>AppCapabilities</string>
 	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.attributionkitd.xpc.impression-intake</string>
 		<string>com.apple.ap.promotedcontent.pcinterface</string>
 		<string>com.apple.ap.promotedcontent.mescalinterface</string>
 		<string>com.apple.appstored.xpc.storequeue</string>

```
### AppStoreWidgetsExtension

> `/Applications/AppStore.app/PlugIns/AppStoreWidgetsExtension.appex/AppStoreWidgetsExtension`

```diff

 		<string>Personalization</string>
 		<string>Update</string>
 		<string>PurchaseHistory</string>
+		<string>AppCapabilities</string>
 	</array>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>

```
### ProductPageExtension

> `/Applications/AppStore.app/PlugIns/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.appstored.xpc.updates</key>
 	<true/>
+	<key>com.apple.attributionkitd.impression-intake</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 		<string>Personalization</string>
 		<string>Update</string>
 		<string>PurchaseHistory</string>
+		<string>AppCapabilities</string>
 	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.attributionkitd.xpc.impression-intake</string>
 		<string>com.apple.ap.promotedcontent.pcinterface</string>
 		<string>com.apple.ap.promotedcontent.mescalinterface</string>
 		<string>com.apple.appstored.xpc.storequeue</string>

```
### SubscribePageExtension

> `/Applications/AppStore.app/PlugIns/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.appstored.xpc.updates</key>
 	<true/>
+	<key>com.apple.attributionkitd.impression-intake</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 		<string>Personalization</string>
 		<string>Update</string>
 		<string>PurchaseHistory</string>
+		<string>AppCapabilities</string>
 	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.attributionkitd.xpc.impression-intake</string>
 		<string>com.apple.ap.promotedcontent.pcinterface</string>
 		<string>com.apple.ap.promotedcontent.mescalinterface</string>
 		<string>com.apple.appstored.xpc.storequeue</string>

```
### AskPermissionUI

> `/Applications/AskPermissionUI.app/AskPermissionUI`

```diff

 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
+	<key>com.apple.private.security.container-required</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.askpermissiond</string>
+		<string>com.apple.xpc.amsengagementd</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOMobileFramebufferUserClient</string>
 	</array>
+	<key>platform-application</key>
+	<true/>
 </dict>
 </plist>
 

```
### AuthenticationServicesUI

> `/Applications/AuthenticationServicesUI.app/AuthenticationServicesUI`

```diff

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.security.octagon</string>
 		<string>com.apple.sharingd</string>
+		<string>com.apple.AuthenticationServices.AutoFill</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>

```

### 🆕 AutoSettings

> `/Applications/AutoSettings.app/AutoSettings`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARCapableApp</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.AutoSettings</string>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.CarAssetUtils.variants</key>
	<true/>
	<key>com.apple.private.CarPlayUIServices.punch-through</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>AutomakerNotificationHistory</string>
		<string>AudioSettings</string>
		<string>PositionTracker</string>
		<string>AutomakerSettings</string>
		<string>PairedDevices</string>
		<string>Vehicle</string>
	</array>
	<key>com.apple.private.carkit</key>
	<true/>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.carkit.service</string>
		<string>com.apple.caraccessoryframework.cardata</string>
		<string>com.apple.CarPlayApp.punch-through-service</string>
		<string>com.apple.CarAssetUtils.variants</string>
	</array>
</dict>
</plist>

```
### BarcodeScanner

> `/Applications/BarcodeScanner.app/BarcodeScanner`

```diff

 	<array>
 		<string>spi</string>
 		<string>public-cellular-plan</string>
+		<string>public-esim-qr-code</string>
 	</array>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.proactive.eventtracker</key>
+	<true/>
 	<key>com.apple.rapport.SessionPaired</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>313</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### Business

> `/Applications/BusinessExtensionsWrapper.app/PlugIns/Business.appex/Business`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.mobileinstall.upgrade-enabled</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.UIKit.ShareUI</string>
+		<string>com.apple.businessservicesd</string>
 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>

```
### Camera

> `/Applications/Camera.app/Camera`

```diff

 	<array>
 		<string>spi</string>
 		<string>public-cellular-plan</string>
+		<string>public-esim-qr-code</string>
 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.imagecapturecore.authorization_bypass</key>
+	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>
 	<true/>
 	<key>com.apple.private.ind.client</key>

 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite</key>
 	<true/>
+	<key>com.apple.proactive.eventtracker</key>
+	<true/>
 	<key>com.apple.rapport.SessionPaired</key>
 	<true/>
 	<key>com.apple.rapport.people</key>

 	<array>
 		<string>/Library/Caches/com.apple.WebKit.Networking/</string>
 		<string>/Library/LiveFiles/com.apple.filesystems.userfsd/</string>
+		<string>/Library/Caches/com.apple.DocumentCamera/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.setWantsLockButtonEvents</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>313</string>
+	</array>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>
 	<key>fairplay</key>

```

### 🆕 CarCamera

> `/Applications/CarCamera.app/CarCamera`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARAppHidden</key>
	<true/>
	<key>CARCapableApp</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.CarCamera</string>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.CarPlayUIServices.punch-through</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>AutomakerExteriorCamera</string>
	</array>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.caraccessoryframework.cardata</string>
		<string>com.apple.CarPlayApp.punch-through-service</string>
	</array>
</dict>
</plist>

```
### CarPlaySettings

> `/Applications/CarPlaySettings.app/CarPlaySettings`

```diff

 	<true/>
 	<key>com.apple.private.CarPlayServices.icon-layout</key>
 	<true/>
+	<key>com.apple.private.CarPlayUIServices.cluster-theme</key>
+	<true/>
 	<key>com.apple.private.CarPlayUIServices.status-bar-style</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>read</string>
 		<string>write</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/CarPlay/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CarPlayApp.cluster-theme-service</string>
 		<string>com.apple.CarPlayApp.service</string>
 		<string>com.apple.CarPlayApp.status-bar-service</string>
 		<string>com.apple.carkit.service</string>

```
### CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

```diff

 	<string>com.apple.CarPlaySetupApp</string>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
 	<key>com.apple.private.carkit.setupPromptDirector</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.carkit.setupPromptDirector.service</string>
+		<string>com.apple.passd.payment</string>
 	</array>
 </dict>
 </plist>

```
### CarPlayWallpaper

> `/Applications/CarPlayWallpaper.app/CarPlayWallpaper`

```diff

 	<true/>
 	<key>com.apple.developer.carp</key>
 	<true/>
+	<key>com.apple.private.CarAssetUtils.variants</key>
+	<true/>
+	<key>com.apple.private.CarPlayUIServices.cluster-theme</key>
+	<true/>
 	<key>com.apple.private.carp</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.carpd.xpc</string>
-		<string>com.apple.caraccessoryframework.gatekeeper</string>
+		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.CarAssetUtils.variants</string>
+		<string>com.apple.CarPlayApp.cluster-theme-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 Charge

> `/Applications/Charge.app/Charge`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARAppHidden</key>
	<true/>
	<key>CARCapableApp</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.CarCharge</string>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>HighVoltageBattery</string>
		<string>Charging</string>
	</array>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.caraccessoryframework.cardata</string>
	</array>
</dict>
</plist>

```

### 🆕 Climate

> `/Applications/Climate.app/Climate`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARCapableApp</key>
	<true/>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.CarAssetUtils.variants</key>
	<true/>
	<key>com.apple.private.CarPlayUIServices.punch-through</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>Seat</string>
		<string>VehicleVariants</string>
		<string>AutomakerSettings</string>
		<string>PositionTracker</string>
		<string>Climate</string>
	</array>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CarPlayApp.punch-through-service</string>
		<string>com.apple.caraccessoryframework.cardata</string>
		<string>com.apple.CarAssetUtils.variants</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.CarClimate</string>
	</array>
</dict>
</plist>

```
### ClockAngel

> `/Applications/ClockAngel.app/ClockAngel`

```diff

 		<string>com.apple.MobileTimer.alarmserver</string>
 		<string>com.apple.locationd.registration</string>
 		<string>com.apple.locationd.synchronous</string>
+		<string>com.apple.MobileTimer.stopwatchserver</string>
 	</array>
 </dict>
 </plist>

```

### 🆕 Closures

> `/Applications/Closures.app/Closures`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARAppHidden</key>
	<true/>
	<key>CARCapableApp</key>
	<true/>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.CarAssetUtils.variants</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>Seat</string>
		<string>PositionTracker</string>
		<string>Body</string>
		<string>VehicleVariants</string>
	</array>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.caraccessoryframework.cardata</string>
		<string>com.apple.CarAssetUtils.variants</string>
	</array>
</dict>
</plist>

```
### CompanionServicesViewService

> `/Applications/CompanionServicesViewService.app/CompanionServicesViewService`

```diff

 	<string>559326803</string>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.authentication-services-core.allow-authentication-request-proxying</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>

```
### DDActionsService

> `/Applications/DDActionsService.app/DDActionsService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.sportsd.xpc</string>
 		<string>com.apple.parsec-fbf</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### SystemReport-iOS-D83-D84

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport-iOS-D83-D84.appex/SystemReport-iOS-D83-D84`

```diff

 	<true/>
 	<key>com.apple.nvmetunnel.allow</key>
 	<true/>
+	<key>com.apple.powerui.smartcharging</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>

 		<string>com.apple.mobilerepaird</string>
 		<string>com.apple.ZhuGeService</string>
 		<string>com.apple.private.corewifi-xpc</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### Family

> `/Applications/Family.app/Family`

```diff

 	<array>
 		<string>com.apple.ams-identity-verification</string>
 	</array>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.fileprovider.fetch-url</key>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.mobilemail.mail-recipient-vetting</key>
 	<true/>
 	<key>com.apple.private.mobilesms.messages-recipient-vetting</key>

 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceWillow</string>
 	</array>
+	<key>com.apple.private.usage-tracking</key>
+	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.webkit</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
-		<string>/Library/CallHistoryDB/</string>
-		<string>/Library/com.apple.WatchListKit/</string>
-		<string>/Library/ContactsMetadata/</string>
-		<string>/Library/DuetExpertCenter/</string>
-		<string>/Library/Preferences/com.apple.mobilephone.speeddial.plist</string>
-		<string>/Library/SMS/</string>
-		<string>/Library/MessagesMetaData/</string>
-		<string>/Library/Spotlight/</string>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.passd.library</string>
 		<string>com.apple.passd.payment</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
 		<string>kern.hv_vmm_present</string>

 		<string>AGXDeviceUserClient</string>
 		<string>IOSurfaceAcceleratorClient</string>
 	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.DeviceActivity</string>
+	</array>
 	<key>com.apple.sharesheet.allow-custom-view</key>
 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>

```
### FinanceUIService

> `/Applications/FinanceUIService.app/FinanceUIService`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.financed.service.financestore</string>
+		<string>com.apple.financed.service.coredatastore</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.FinanceKit</string>
 	</array>
 	<key>com.apple.trial.client</key>
 	<array>

```
### GameCenterUIService

> `/Applications/GameCenterUIService.app/GameCenterUIService`

```diff

 		<string>TurnBasedMultiplayer</string>
 		<string>GameStats</string>
 	</array>
-	<key>com.apple.private.mobilesms.messages-recipient-vetting</key>
-	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### HDSViewService

> `/Applications/HDSViewService.app/HDSViewService`

```diff

 	<true/>
 	<key>com.apple.networkrelay.devices.write</key>
 	<true/>
+	<key>com.apple.nfcd.hwmanager</key>
+	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
 	<key>com.apple.payment.amp-card-enrollment</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.airdrop.settings</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.applemediaservices.multiuser</key>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/mobile/Library/Preferences/</string>
 		<string>/private/preboot/</string>
 		<string>/private/var/hardware/FactoryData/System/Library/Caches/com.apple.factorydata/</string>
 		<string>/private/var/preferences/FeatureFlags/Settings.plist</string>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/private/var/mobile/Library/Preferences/com.apple.sharingd.plist</string>
 		<string>/Library/Logs/CrashReporter/</string>
 		<string>/Library/VoiceTrigger/</string>
 		<string>/Library/Preferences/com.apple.coreaudio.plist</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.sharingd</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.aa.custodian.xpc</string>
 		<string>com.apple.amsaccountsd.multiuser</string>

```
### HearingApp

> `/Applications/HearingApp.app/HearingApp`

```diff

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.SoundDetectionModels</string>
+	</array>
 	<key>com.apple.private.sessionkit.custom-platter-target</key>
 	<true/>
 	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
 	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/MobileAsset/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.HearingApp</string>

```
### HomeControlService

> `/Applications/HomeControlService.app/HomeControlService`

```diff

 	<string>com.apple.Home.HomeControlService</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>App.Intent</string>
 		<string>HomeKitClientAccessoryControl</string>
 		<string>HomeKitClientActionSet</string>
 		<string>HomeKitClientMediaAccessoryControl</string>

```
### HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.icloud.fmfd</string>
 		<string>com.apple.speakerrecognition</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 	</array>
 	<key>com.apple.seld.tsmmanager</key>
 	<true/>

```
### InCallService

> `/Applications/InCallService.app/InCallService`

```diff

 	</array>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accessibility.SpeakTypingServices</key>
+	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.phoneNumberResolver</string>

 	<true/>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>
+	<key>com.apple.private.ids.report-spam-message</key>
+	<true/>
 	<key>com.apple.private.imavcore.imavagent</key>
 	<true/>
 	<key>com.apple.private.imcore.imagent</key>

 		<string>/Library/CallServices/Images/</string>
 		<string>/Library/Accessibility/ClarityBoardEnabled</string>
 		<string>/Library/MessagesMetaData/NickNameCache/</string>
+		<string>/Library/Caches/com.apple.businessservicesd/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.containermanagerd</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.messages.nicknames</string>
 		<string>com.apple.Accessibility</string>
 		<string>com.apple.facetime</string>

```

### 🆕 Media

> `/Applications/Media.app/Media`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARCapableApp</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.CarRadio</string>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.CarAssetUtils.variants</key>
	<true/>
	<key>com.apple.private.CarPlayUIServices.status-bar-style</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>AudioSettings</string>
		<string>AutomakerSettings</string>
		<string>Media</string>
		<string>PositionTracker</string>
	</array>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.caraccessoryframework.cardata</string>
		<string>com.apple.CarPlayApp.status-bar-service</string>
		<string>com.apple.CarAssetUtils.variants</string>
	</array>
</dict>
</plist>

```
### MediaRemoteUI

> `/Applications/MediaRemoteUI.app/MediaRemoteUI`

```diff

 	</array>
 	<key>com.apple.private.audio.interprocess-tap</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.Intent</string>
+	</array>
 	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### MessagesViewService

> `/Applications/MessagesViewService.app/MessagesViewService`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>
 	<true/>
+	<key>com.apple.private.security.storage.PassKit</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.sociallayer.collaboration-handshake</key>

```
### MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

 	</array>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accountsd.accountmanager</key>
+	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.bulletinboard.utilities</key>
 	<true/>
 	<key>com.apple.clarityboard.chromeVisibility</key>

 	<true/>
 	<key>com.apple.private.ids.idquery-cache</key>
 	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+		<string>com.apple.madrid</string>
+	</array>
+	<key>com.apple.private.ids.messaging.urgent-priority</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+	</array>
+	<key>com.apple.private.ids.registration</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+	</array>
 	<key>com.apple.private.ids.report-spam-message</key>
 	<true/>
 	<key>com.apple.private.imavcore.imavagent</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.facetimemessagestored.service</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>

```
### VoicemailMessageNotificationExtension

> `/Applications/MobilePhone.app/PlugIns/VoicemailMessageNotificationExtension.appex/VoicemailMessageNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>
 	<true/>
+	<key>com.apple.facetimemessagestored.service</key>
+	<array>
+		<string>access-facetime-messaging</string>
+	</array>
 	<key>com.apple.private.security.storage.Voicemail</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.voicemail.vmd</string>
+		<string>com.apple.facetimemessagestored.service</string>
 	</array>
 	<key>com.apple.springboard.allowallcallurls</key>
 	<true/>

```
### MobileSMS

> `/Applications/MobileSMS.app/MobileSMS`

```diff

 	</array>
 	<key>com.apple.TextUnderstanding.SmartReplies.Inference</key>
 	<true/>
+	<key>com.apple.accountsd.accountmanager</key>
+	<true/>
 	<key>com.apple.activityawardsd</key>
 	<true/>
 	<key>com.apple.appstored.install-apps</key>

 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-capture-filter-rendering</key>

 	<true/>
 	<key>com.apple.backboardd.hostCanRequireTouchesFromHostedContent</key>
 	<true/>
+	<key>com.apple.backboardd.touchDeliveryObservation</key>
+	<true/>
 	<key>com.apple.carousel.backlightaccess</key>
 	<true/>
 	<key>com.apple.cdp.statemachine</key>

 	<true/>
 	<key>com.apple.ios.StoreKit.store-page</key>
 	<true/>
+	<key>com.apple.itunescloudd.private</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

 	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
 		<string>com.apple.madrid</string>
 		<string>com.apple.private.alloy.biz</string>
 	</array>
+	<key>com.apple.private.ids.messaging.urgent-priority</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+	</array>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>
+	<key>com.apple.private.ids.registration</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+		<string>com.apple.private.alloy.biz</string>
+	</array>
 	<key>com.apple.private.ignore-preferences-size-limits</key>
 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
+	<key>com.apple.private.security.storage.PassKit</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.shared-with-you.on-screen-content</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.coreduetd.knowledge</string>

 		<string>UITextInputContextIdentifiers</string>
 		<string>com.apple.AppleMediaServices</string>
 		<string>com.apple.imessage.bag</string>
+		<string>com.apple.facetime.bag</string>
 		<string>PUICNPSPreferences</string>
 		<string>com.apple.EmojiCache</string>
 		<string>com.apple.messages.nicknames</string>

```
### MessagesNotificationExtension

> `/Applications/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
+	<key>com.apple.private.security.storage.PassKit</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### MessagesTranscriptExtension

> `/Applications/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
+	<key>com.apple.private.security.storage.PassKit</key>
+	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### MobileSMSSpotlightImporter

> `/Applications/MobileSMS.app/PlugIns/MobileSMSSpotlightImporter.appex/MobileSMSSpotlightImporter`

```diff

 		<key>value</key>
 		<string>com.apple.MobileSMS</string>
 	</dict>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.MobileSMS</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.imdpersistence.IMDPersistenceAgent</string>
+		<string>com.apple.spotlight.SearchAgent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### SafariLinkExtension

> `/Applications/MobileSafari.app/Extensions/SafariLinkExtension.appex/SafariLinkExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/System/Library/PrivateFrameworks/MobileSafariSwift.framework</string>
+	</array>
 	<key>com.apple.private.safari.can-use-bookmarks-sync-agent</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

```
### MobileSafari

> `/Applications/MobileSafari.app/MobileSafari`

```diff

 	<array>
 		<string>spi</string>
 		<string>public-cellular-plan</string>
+		<string>public-esim-qr-code</string>
 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.appattest.spi</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>

 	<true/>
 	<key>com.apple.developer.WebKit.ServiceWorkers</key>
 	<true/>
+	<key>com.apple.developer.browser.app-installation</key>
+	<true/>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

 	<string>com.apple.Safari.SyncedTabs</string>
 	<key>com.apple.developer.web-browser</key>
 	<true/>
+	<key>com.apple.developer.web-browser-engine.host</key>
+	<true/>
 	<key>com.apple.features.all-access</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/System/Cryptexes/OS/System/Library/PrivateFrameworks/MobileSafariSwift.framework</string>
+	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>App.WebUsage</string>
+		<string>Discoverability.Signals</string>
+		<string>Discoverability.Usage</string>
 		<string>Safari.AutoPlay</string>
 		<string>Safari.WebPagePerformance</string>
 		<string>Safari.Navigations</string>
 		<string>Safari.PageLoad</string>
+		<string>Safari.WindowProxy</string>
 	</array>
 	<key>com.apple.private.can-load-any-content-blocker</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
-	<key>com.apple.private.security.storage.triald</key>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>

 		<string>com.apple.mobilesafari</string>
 		<string>com.apple.tipsd</string>
 	</array>
-	<key>com.apple.private.webinspector.allow-remote-inspection</key>
+	<key>com.apple.private.web-browser-engine.host</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
 	<true/>

 		<string>/private/var/db/MobileIdentityData/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/Applications/</string>
+		<string>/private/var/db/os_eligibility/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.datamigrator</string>
 		<string>com.apple.online-auth-agent.xpc</string>
+		<string>com.apple.Safari.SearchHelper</string>
 		<string>com.apple.misagent</string>
 		<string>com.apple.sportsd.xpc</string>
 		<string>com.apple.email.maild</string>

 		<string>com.apple.SharePlay.GroupSessionService</string>
 		<string>com.apple.siri.sirireaderd</string>
 		<string>com.apple.sirittsd</string>
-		<string>com.apple.Safari.SearchHelper</string>
 		<string>com.apple.chronoservices</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### PhotoPicker

> `/Applications/MobileSlideShow.app/PlugIns/PhotoPicker.appex/PhotoPicker`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.photos.picker</string>
 	</array>

```
### PhotosPicker

> `/Applications/MobileSlideShow.app/PlugIns/PhotosPicker.appex/PhotosPicker`

```diff

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
-	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.photos.picker</string>
 	</array>

```
### PCViewService

> `/Applications/PCViewService.app/PCViewService`

```diff

 			<string>/Applications/PCViewService.app/PCViewService</string>
 		</dict>
 	</array>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.Intent</string>
+	</array>
 	<key>com.apple.private.coordination.alarms</key>
 	<true/>
 	<key>com.apple.private.coordination.timers</key>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.apple-pay-trust.all-access</key>
 	<true/>
 	<key>com.apple.asd.allow</key>

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.WalletMobileAssets</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.PassKitCoreXPCService</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.passd.assertions</string>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.apple-pay-trust.all-access</key>
 	<true/>
 	<key>com.apple.asd.allow</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.idcredd.biometrics.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.seserviced.sereservation.client</string>
 		<string>com.apple.seserviced.session</string>

 		<string>com.apple.financed.service.bankconnect</string>
 		<string>com.apple.financed.service.financestore</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.AppleMediaServices</string>

```
### PeopleMessageService

> `/Applications/PeopleMessageService.app/PeopleMessageService`

```diff

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.ScreenTimeAgent.ask</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.coreduetd.people</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### PeopleMessagesAskToBuy

> `/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.people</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.askpermissiond</string>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.contactsd.persistence</string>
+		<string>com.apple.AddressBook.ContactsAccountsService</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### PeopleMessagesScreenTime

> `/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.people</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ScreenTimeAgent.ask</string>

 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.contactsd.persistence</string>
+		<string>com.apple.AddressBook.ContactsAccountsService</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### PreBoard

> `/Applications/PreBoard.app/PreBoard`

```diff

 	<true/>
 	<key>com.apple.CommCenter.Preferences-delete</key>
 	<true/>
+	<key>com.apple.QuartzCore.display-state</key>
+	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 		<string>preferences-reset</string>
 		<string>carrier-space</string>
 		<string>developer-settings</string>
+		<string>public-cellular-plan</string>
+		<string>public-esim-qr-code</string>
+		<string>bootstrap-service</string>
 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.apple-pay-trust.all-access</key>
 	<true/>
 	<key>com.apple.appleaccount.beneficiary</key>

 	<true/>
 	<key>com.apple.developer.ClassKit-environment</key>
 	<string>production</string>
+	<key>com.apple.developer.associated-domains</key>
+	<array/>
 	<key>com.apple.developer.coreml.model-deployment</key>
 	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>

 	<true/>
 	<key>com.apple.features.all-access</key>
 	<true/>
+	<key>com.apple.feedbackd.client-forms</key>
+	<array>
+		<string>framework-autocorrect_S02_frCA</string>
+		<string>framework-autocorrect_S02_esES</string>
+		<string>:framework-autocorrect-korean</string>
+	</array>
 	<key>com.apple.fileprovider.acl-read</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-write</key>

 	</array>
 	<key>com.apple.nearbyd.diagnostics</key>
 	<true/>
+	<key>com.apple.networkd.allow_bootstrap_cellular_service_request</key>
+	<true/>
 	<key>com.apple.networkd.modify_settings</key>
 	<true/>
 	<key>com.apple.networkd.set_account_identifier</key>

 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.BiometricLivenessFlag</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.Preboard</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage.SetDSLModeEnabled</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppLaunch</string>
+		<string>App.InFocus</string>
+		<string>App.MediaUsage</string>
+		<string>App.WebUsage</string>
+		<string>Device.Display.Backlight</string>
 		<string>FindMyLocationChange</string>
+		<string>Media.NowPlaying</string>
+		<string>Notification.Usage</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.internalState</key>
+	<true/>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.exposure-notification</key>
 	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>

 	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
 		<string>com.apple.private.alloy.maps.eta</string>
 		<string>com.apple.private.alloy.sms</string>
 		<string>com.apple.private.alloy.passbook.provisioning</string>
 	</array>
+	<key>com.apple.private.ids.messaging.urgent-priority</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+	</array>
 	<key>com.apple.private.ids.nearby</key>
 	<true/>
 	<key>com.apple.private.ids.phone-number-authentication</key>
 	<true/>
 	<key>com.apple.private.ids.registration</key>
 	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+		<string>com.apple.private.alloy.biz</string>
 		<string>com.apple.madrid</string>
 		<string>com.apple.ess</string>
 	</array>

 	<true/>
 	<key>com.apple.private.security.storage.clipserviced</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.securityd.ae.disable</key>

 	<true/>
 	<key>com.apple.private.sharing.unlock-manager</key>
 	<true/>
+	<key>com.apple.private.sirittsservice.impersonate-clients</key>
+	<array>
+		<string>com.apple.siri.MultilingualReading</string>
+	</array>
 	<key>com.apple.private.sleepd</key>
 	<true/>
 	<key>com.apple.private.subscriptionservice.internal</key>

 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
+	<key>com.apple.private.swc.system-app</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.feedbackd.xpc</string>
 		<string>com.apple.posterboardui.services </string>
 		<string>com.apple.backupd</string>
 		<string>com.apple.ak.privateemail.xpc</string>

 	<true/>
 	<key>com.apple.seserviced.seendpoints.certificateauthorities</key>
 	<true/>
+	<key>com.apple.seserviced.settings.mach</key>
+	<true/>
 	<key>com.apple.sh</key>
 	<true/>
 	<key>com.apple.sharesheet.allow-custom-view</key>

 	<true/>
 	<key>com.apple.symptoms.cosm.admin</key>
 	<true/>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>com.apple.systemstatus.domains</key>
 	<array>
 		<string>status-bar-overrides</string>

```
### PreviewShell

> `/Applications/PreviewShell.app/PreviewShell`

```diff

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.dt.previewsd.allowed</key>
+	<true/>
+	<key>com.apple.osanalytics.canusediagnosticmonitor</key>
+	<true/>
 	<key>com.apple.private.chrono-extension-host</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.dt.previewsd.crashlistener</string>
 		<string>com.apple.chronoservices</string>
 	</array>
 	<key>com.apple.springboard.allowIconVisibilityChanges</key>

```

### 🆕 ProximityReaderSceneUI

> `/Applications/ProximityReaderSceneUI.app/ProximityReaderSceneUI`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.ProximityReaderSceneUI</string>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.accessibility.AXSBServer.assertions</key>
	<true/>
	<key>com.apple.accessibility.feature.securepay</key>
	<true/>
	<key>com.apple.backboard.display.services</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.nfcd.assertion.handover</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.CallerPID</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.airdrop.settings</key>
	<true/>
	<key>com.apple.private.hid.client.event-filter</key>
	<true/>
	<key>com.apple.private.internal-style-asam</key>
	<true/>
	<key>com.apple.private.mediaexperience.silentmodenotifications.allow</key>
	<true/>
	<key>com.apple.private.passkit.pass-presentation-suppress-from-background</key>
	<true/>
	<key>com.apple.private.security.container-required</key>
	<true/>
	<key>com.apple.private.security.storage.ContactlessReader</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.proximityreader.connect-pin-ui-service</key>
	<true/>
	<key>com.apple.proximityreader.connect-tap-ui-service</key>
	<true/>
	<key>com.apple.proximityreader.show-tap-ui</key>
	<true/>
	<key>com.apple.proxreader.ui-service</key>
	<true/>
	<key>com.apple.runningboard.assertions.angeltarget</key>
	<true/>
	<key>com.apple.runningboard.assertions.frontboard</key>
	<true/>
	<key>com.apple.runningboard.trustedtarget</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/ContactlessReader/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.sharingd</string>
		<string>com.apple.SharingServices</string>
		<string>com.apple.softposreaderd</string>
		<string>com.apple.nfcd.hwmanager</string>
		<string>com.apple.merchantd.internals</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.backlightd</string>
		<string>com.apple.PassbookUISceneService.remote-ui</string>
		<string>com.apple.accessibility.AXSpringBoardServer</string>
	</array>
	<key>com.apple.security.exception.mach-register.global-name</key>
	<array>
		<string>com.apple.accessibility.gax.client</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.merchantd</string>
		<string>com.apple.UIKit</string>
		<string>com.apple.Preferences</string>
		<string>com.apple.coreaudio</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.ProximityReaderSceneUI</string>
	</array>
	<key>com.apple.sharing.Client</key>
	<true/>
	<key>com.apple.softposreaderd</key>
	<integer>2</integer>
	<key>com.apple.springboard.SystemUIScene</key>
	<true/>
	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<array>
		<string>incallservice</string>
	</array>
	<key>com.apple.wallet.banner</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### RecoverDeviceUI

> `/Applications/RecoverDeviceUI.app/RecoverDeviceUI`

```diff

 		</array>
 		<key>limitToDeviceClasses</key>
 		<array>
+			<string>iPad</string>
 			<string>iPhone</string>
 		</array>
 		<key>viewControllerClassName</key>

```
### ReplayKitAngel

> `/Applications/ReplayKitAngel.app/ReplayKitAngel`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.sessionservices</string>
+		<string>com.apple.frontboard.systemappservices</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<string>com.apple.replayd</string>

 	<true/>
 	<key>com.apple.springboard.openurlswhenlocked</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides</key>
 	<true/>
 	<key>com.apple.springboard.statusbarstyleoverrides.coordinator</key>

```
### SIMSetupUIService

> `/Applications/SIMSetupUIService.app/SIMSetupUIService`

```diff

 	<true/>
 	<key>com.apple.springboard.appbackgroundstyle</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<string>com.apple.SafariViewService</string>
 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
+		<string>cellular-plan</string>
 		<string>spi</string>
 		<string>public-cellular-plan</string>
+		<string>public-esim-qr-code</string>
 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>

 	</array>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.networkd.allow_bootstrap_cellular_service_request</key>
+	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
 	<key>com.apple.nfcd.session.reader.internal</key>

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.uninstall</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<array>
 		<string>App.WebApp.InFocus</string>
 		<string>App.WebUsage</string>
+		<string>Discoverability.Signals</string>
+		<string>Discoverability.Usage</string>
 	</array>
 	<key>com.apple.private.can-load-any-content-blocker</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
+	<key>com.apple.private.launchservices.changedefaulthandlers</key>
+	<array>
+		<string>http</string>
+		<string>https</string>
+	</array>
 	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>
 	<string>*</string>
 	<key>com.apple.private.networkserviceproxy</key>

 	<string>com.apple.mobilesafari</string>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.suggestions.events</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<array>
 		<string>com.apple.WebKit.PushBundles</string>
 	</array>
-	<key>com.apple.private.webinspector.allow-remote-inspection</key>
-	<true/>
 	<key>com.apple.private.webinspector.proxy-application</key>
 	<true/>
 	<key>com.apple.private.webkit.pushbundle</key>

 	<true/>
 	<key>com.apple.security.device.usb</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Caches/com.apple.ClipServices/</string>

 		<string>com.apple.passd.payment</string>
 		<string>com.apple.security.kcsharing</string>
 		<string>com.apple.webprivacyd</string>
+		<string>com.apple.lsd.modifydb</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### ScreenTimeWidgetExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.InFocus</string>
+		<string>App.MediaUsage</string>
+		<string>App.WebUsage</string>
+		<string>Device.Display.Backlight</string>
+		<string>Media.NowPlaying</string>
+		<string>Notification.Usage</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
 	<key>com.apple.private.screen-time.persistence</key>
 	<true/>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.UsageTrackingAgent.private</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.accountsd.accountmanager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>com.apple.MobileAsset.WalletMobileAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerHSAssetsIPad</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone12AndOlder</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone13x</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone14x</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPad</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

 	<true/>
 	<key>com.apple.private.photos.service.internal.cloud</key>
 	<true/>
+	<key>com.apple.private.rtcreportingd</key>
+	<true/>
 	<key>com.apple.private.safari.cloudtabs</key>
 	<true/>
 	<key>com.apple.private.screen-time</key>

 	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.seeding.client</key>
 	<true/>
 	<key>com.apple.private.seserviced.sereservation.client</key>

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/VoiceTrigger/</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleSMCClient</string>

```
### SharingViewService

> `/Applications/SharingViewService.app/SharingViewService`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.backboardd.hidPersistentProperty-digitizer</key>
+	<true/>
 	<key>com.apple.backboardd.proximityDetection</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>

 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.accessorydiscovery</key>
+	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.pairingmanager</key>

 	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
+	<key>com.apple.runningboard.sharingviewservice</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/preboot/</string>

 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.HRTFEnrollmentService</string>
 		<string>com.apple.icloud.fmfd</string>
+		<string>com.apple.icloud.searchpartyd.accessorydiscoverysession</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.pairingmanager</string>
 		<string>com.apple.identityservicesd.nsxpc</string>

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceMotion</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceReminders</string>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceMotion</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceReminders</string>

```
### SoftwareUpdateUIService

> `/Applications/SoftwareUpdateUIService.app/SoftwareUpdateUIService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.susuiservice</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>

 	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
+	<key>com.apple.private.mobiletimerd</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileSoftwareUpdate/MobileAsset/AssetsV2/com_apple_MobileAsset_SoftwareUpdateDocumentation/</string>

 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.softwareupdateservicesd</string>
 		<string>CAREServer</string>
+		<string>com.apple.MobileTimer.timerserver</string>
+		<string>com.apple.MobileTimer.alarmserver</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 	</array>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allows-set-output-device</key>

 		<string>Device.Power.EnergyMode</string>
 		<string>Device.Wireless.AirplaneMode</string>
 		<string>Device.Display.Appearance</string>
-		<string>Device.Wireless.WiFi</string>
+		<string>Device.Wireless.WiFiAvailabilityStatus</string>
 		<string>Device.Wireless.BluetoothPowerEnabled</string>
 		<string>Device.Wireless.CellularDataEnabled</string>
 		<string>Device.Display.TrueTone</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.ClipServices.clipserviced</string>
 		<string>com.apple.duet.expertcenter</string>
 		<string>com.apple.icloud.fmfd</string>

```
### TDGSharingViewService

> `/Applications/TDGSharingViewService.app/TDGSharingViewService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

```

### 🆕 TirePressure

> `/Applications/TirePressure.app/TirePressure`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARAppHidden</key>
	<true/>
	<key>CARCapableApp</key>
	<true/>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.CarAssetUtils.variants</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>VehicleVariants</string>
		<string>Tire</string>
		<string>PositionTracker</string>
	</array>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.caraccessoryframework.cardata</string>
		<string>com.apple.CarAssetUtils.variants</string>
	</array>
</dict>
</plist>

```

### 🆕 Trip

> `/Applications/Trip.app/Trip`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CARAppHidden</key>
	<true/>
	<key>CARCapableApp</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.CarTrip</string>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.RequiredVehicleAccessories</key>
	<array>
		<string>DriveInformation</string>
	</array>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.caraccessoryframework.cardata</string>
	</array>
</dict>
</plist>

```
### Web

> `/Applications/Web.app/Web`

```diff

 	<string>com.apple.webapp</string>
 	<key>com.apple.assertiond.background-view-services</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.allowed</key>
+	<true/>
+	<key>com.apple.private.InstallCoordination.uninstall</key>
+	<true/>
+	<key>com.apple.private.WebClips.read-write</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<key>value</key>
 		<string>com.apple.mobilesafari</string>
 	</dict>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>
 	<string>*</string>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
-	<key>com.apple.private.webinspector.allow-remote-inspection</key>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.installcoordinationd</string>
+	</array>
 </dict>
 </plist>
 

```
### WebSheet

> `/Applications/WebSheet.app/WebSheet`

```diff

 		<string>com.apple.managedconfiguration.profiled</string>
 		<string>com.apple.email.maild</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.musebuddy</string>
+	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<array>
 		<string>prefs:root=WIFI</string>

 	<true/>
 	<key>com.apple.surfboard.always-discard-last-scene</key>
 	<true/>
+	<key>com.apple.surfboard.chrome-customization</key>
+	<true/>
 	<key>com.apple.surfboard.scenesession-custom-focus-order</key>
-	<integer>1001</integer>
+	<integer>1501</integer>
+	<key>com.apple.surfboard.setup-launch-allowed</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.cfnetwork</string>

```

### 🆕 BuiltinAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin`

- No entitlements *(yet)*
### AccessibilityUIServer

> `/System/Library/CoreServices/AccessibilityUIServer.app/AccessibilityUIServer`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.SoundAnalysis.AccessibilitySoundActions</key>
+	<true/>
+	<key>com.apple.SoundAnalysis.AccessibilitySoundRecognition</key>
+	<true/>
+	<key>com.apple.SoundAnalysis.AllAnalysisRequests</key>
+	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
 	<true/>
 	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>

 	<true/>
 	<key>com.apple.pointerui.persistentlyHidePointer</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.Preboard</key>
+	<true/>
 	<key>com.apple.private.MobileActivation</key>
 	<array>
 		<string>GetActivationState</string>

 		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.incoming-call-filter-server</string>
+		<string>com.apple.soundanalysisd</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
 		<string>com.apple.TextInput</string>
 		<string>com.apple.TextInput.accessibility</string>

```
### assistivetouchd

> `/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.accessibility.physicalinteraction.client</key>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.system-layers</key>
 	<true/>
+	<key>com.apple.airplay.endpoint.xpc</key>
+	<true/>
 	<key>com.apple.assertiond.system-shell</key>
 	<true/>
 	<key>com.apple.assistant.client</key>

 	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
+	<key>com.apple.coremedia.endpoint.xpc</key>
+	<true/>
 	<key>com.apple.developer.carp</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.mediaexperience.endpoint.xpc</key>
+	<true/>
 	<key>com.apple.private.CarPlayUIServices.status-bar-style</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.donotdisturb.service</string>
 		<string>com.apple.donotdisturb.service.non-launching</string>
-		<string>com.apple.caraccessoryframework.gatekeeper</string>
 		<string>com.apple.carkit.app.service</string>
 		<string>com.apple.carkit.clustercontrol</string>
 		<string>com.apple.carkit.service</string>
 		<string>com.apple.carkit.theme-asset-library</string>
-		<string>com.apple.carpd.xpc</string>
+		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.intents.intents-helper</string>
 		<string>com.apple.siri.activation.service</string>
 		<string>com.apple.siri.audiopowerupdate.xpc</string>

```
### CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

 		<string>com.apple.CarPlaySupport.banner-source</string>
 		<string>com.apple.CarPlayApp.service</string>
 		<string>com.apple.CarPlayApp.status-bar-service</string>
+		<string>com.apple.carkit.navigation.service</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

 	<true/>
 	<key>com.apple.accessibility.AXSettingsShortcuts</key>
 	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.accessibility.physicalinteraction.client</key>

```
### SafariBookmarksSyncAgent

> `/System/Library/CoreServices/SafariSupport.bundle/SafariBookmarksSyncAgent`

```diff

 	<dict>
 		<key>com.apple.SafariShared.CloudTabs</key>
 		<string>com.apple.SafariShared.CloudTabs</string>
+		<key>com.apple.SafariShared.Settings</key>
+		<string>com.apple.SafariShared.CloudTabs</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>

```
### ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

 	<key>com.apple.CommCenter.fine-grained</key>
 	<array>
 		<string>data-allowed</string>
+		<string>spi</string>
+		<string>cellular-plan</string>
 	</array>
 	<key>com.apple.Pasteboard.background-access</key>
 	<true/>

 			<string>com.apple.ScreenSharing</string>
 		</dict>
 	</array>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.private.ac</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.screensharing.accessibility</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.security.octagon</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.debug</key>
 	<true/>
+	<key>com.apple.QuartzCore.display-state</key>
+	<true/>
 	<key>com.apple.QuartzCore.displayable-context</key>
 	<true/>
 	<key>com.apple.QuartzCore.flipbook</key>

 	<true/>
 	<key>com.apple.abm.helper.mobile.allow</key>
 	<true/>
+	<key>com.apple.accessibility.IDSServices</key>
+	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
+	<key>com.apple.accessibility.SpeakTypingServices</key>
+	<true/>
+	<key>com.apple.accessibility.SpringBoard</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.aop.hid-device.user-client</key>

 	<true/>
 	<key>com.apple.nfcd.singleUser</key>
 	<true/>
+	<key>com.apple.nfcd.wallet.presentation</key>
+	<true/>
 	<key>com.apple.notificationcenter.widgetcontrollerhascontent</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>

 	<true/>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Repair</string>

 	</array>
 	<key>com.apple.private.attentionawareness</key>
 	<true/>
+	<key>com.apple.private.attentionawareness.continuousFaceDetect</key>
+	<true/>
 	<key>com.apple.private.attentionawareness.motionDetect</key>
 	<true/>
 	<key>com.apple.private.attentionawareness.poll</key>

 		<string>HomeKitClientAccessoryControl</string>
 		<string>HomeKitClientMediaAccessoryControl</string>
 		<string>HomeKitClientActionSet</string>
+		<string>App.Intent</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 		<string>Device.Display.Appearance</string>
 		<string>Device.Display.AlwaysOn</string>
 		<string>OSAnalytics.Hardware.Reliability</string>
-		<string>SpringBoard.GestureEducation.PillLaunch</string>
 	</array>
 	<key>com.apple.private.biome.realTimeSensorSession</key>
 	<true/>

 		<string>com.apple.focus.activity-manager</string>
 		<string>com.apple.springboard.SBIconController</string>
 		<string>com.apple.proactive.AppPredictionClient</string>
-		<string>com.apple.springboard.AppIntents</string>
 		<string>com.apple.private.SpringBoard.focus.intents</string>
 	</array>
 	<key>com.apple.private.donotdisturb.settings.updates.client-identifiers</key>

 	<true/>
 	<key>com.apple.private.security.storage.familycircled</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.sessionkit.alertPresenter</key>

 	<array>
 		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
 		<string>/private/var/mobile/Library/Trial/Treatments/180/</string>
+		<string>/private/var/db/os_eligibility/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### vot

> `/System/Library/CoreServices/VoiceOverTouch.app/vot`

```diff

 	</array>
 	<key>com.apple.accessibility.BrailleTranslationService-access</key>
 	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.accessibility.axassets</key>

```
### iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/var/PersonaVolumes/</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache/</string>
 		<string>/private/var/tmp/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.iconservicesagent/</string>

```

### 🆕 ADFollowUpExtension

> `/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.followup</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.corefollowup.agent</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.managedappdistributiond</string>
	</array>
</dict>
</plist>

```

### 🆕 AppStoreEvalLighthouseWorker

> `/System/Library/ExtensionKit/Extensions/AppStoreEvalLighthouseWorker.appex/AppStoreEvalLighthouseWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.AppleMediaDiscovery.AppStoreEvalLighthouseWorker</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.AppleMediaDiscovery.AppStoreEvalLighthouseWorker</string>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.ASEModelsEvaluation</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.assets.change-daemon-config</key>
	<true/>
	<key>com.apple.private.biome.writer</key>
	<array>
		<string>Lighthouse.Ledger.TaskCustomEvent</string>
	</array>
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
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_ASEModelsEvaluation/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.mobileasset.autoasset</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mobileassetd</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.mobileasset.autoasset</string>
	</array>
</dict>
</plist>

```

### 🆕 ComposeReviewExtension

> `/System/Library/ExtensionKit/Extensions/ComposeReviewExtension.appex/ComposeReviewExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.AppleMediaServicesUI.ComposeReviewExtension</string>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.ak.auth.xpc</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.AppleMediaServicesUI.ComposeReviewExtension</string>
	<key>com.apple.authkit.client</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>com_apple_driver_FairPlayIOKitUserClient</string>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```

### 🆕 ExperimentationExtension

> `/System/Library/ExtensionKit/Extensions/ExperimentationExtension.appex/ExperimentationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.metrics.MetricsExtension</string>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.metrics.MetricsExtension</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
		<string>Siri.Metrics.OnDeviceDigestUsageMetrics</string>
		<string>Siri.Metrics.OnDeviceDigestExperimentMetrics</string>
	</array>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
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
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.feedbacklogger</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.WebKit.GPU

> `/System/Library/ExtensionKit/Extensions/GPUExtension.appex/com.apple.WebKit.GPU`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.rendering</key>
	<true/>
	<key>com.apple.mediaremote.external-artwork-validation</key>
	<true/>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.attribution.explicitly-assumed-identities</key>
	<array>
		<dict>
			<key>type</key>
			<string>wildcard</string>
		</dict>
	</array>
	<key>com.apple.private.avfoundation.capture.temporary.no-media-environment.allow</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.mediaexperience.processassertionaudittokens.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.recordingWebsite.allow</key>
	<true/>
	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>
	<true/>
	<key>com.apple.private.memory.ownership_transfer</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.web-browser-engine.gpu</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.systemstatus.activityattribution</string>
	</array>
	<key>com.apple.springboard.statusbarstyleoverrides</key>
	<true/>
	<key>com.apple.springboard.statusbarstyleoverrides.coordinator</key>
	<array>
		<string>UIStatusBarStyleOverrideWebRTCAudioCapture</string>
		<string>UIStatusBarStyleOverrideWebRTCCapture</string>
	</array>
	<key>com.apple.systemstatus.activityattribution</key>
	<true/>
	<key>com.apple.tcc.delegated-services</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMicrophone</string>
	</array>
</dict>
</plist>

```
### MapsTransactionInsightsExtension

> `/System/Library/ExtensionKit/Extensions/MapsTransactionInsightsExtension.appex/MapsTransactionInsightsExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.finance.private</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.financed.service.coredatastore</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.FinanceKit</string>
+	</array>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.mobileactivationd</string>
+	</array>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>1290</string>
+	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.FinanceKit</string>
+	</array>
+</dict>
+</plist>
 

```

### 🆕 MercuryPosterExtension

> `/System/Library/ExtensionKit/Extensions/MercuryPosterExtension.appex/MercuryPosterExtension`

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

### 🆕 MusicEngagementExtension

> `/System/Library/ExtensionKit/Extensions/MusicEngagementExtension.appex/MusicEngagementExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Music.MusicEngagementExtension</string>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.Music.MusicEngagementExtension</string>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServicePhotosAdd</string>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.Music</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.SocialLayer</string>
		<string>com.apple.mediaplaybackcore</string>
		<string>com.apple.videos-preferences</string>
		<string>com.apple.mobileipod</string>
		<string>com.apple.Music</string>
		<string>com.apple.Fuse</string>
		<string>com.apple.itunesstored</string>
		<string>com.apple.homesharing</string>
		<string>com.apple.mediaremote</string>
		<string>com.apple.MediaSocial</string>
		<string>com.apple.restrictionspassword</string>
		<string>com.apple.itunescloudd</string>
		<string>com.apple.medialibrary</string>
		<string>com.apple.itunescloud</string>
		<string>com.apple.itunescloud.internal</string>
		<string>com.apple.AppleMediaServices</string>
		<string>com.apple.springboard</string>
		<string>com.apple.ClarityUI.Music</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
</dict>
</plist>

```

### 🆕 com.apple.WebKit.Networking

> `/System/Library/ExtensionKit/Extensions/NetworkingExtension.appex/com.apple.WebKit.Networking`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.networking</key>
	<true/>
	<key>com.apple.multitasking.systemappassertions</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.private.accounts.bundleidspoofing</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>InstallWebAttribution</string>
	</array>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.WebContentRestrictions</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.ciphermld.allow</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.dmd.policy</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceWebKitIntelligentTrackingPrevention</string>
		<string>kTCCServiceUserTracking</string>
	</array>
	<key>com.apple.private.web-browser-engine.network</key>
	<true/>
	<key>com.apple.private.webkit.adattributiond</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.private.webkit.webpush</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
	<key>com.apple.symptom_analytics.configure</key>
	<true/>
</dict>
</plist>

```
### PFLHRPeriodPredCK

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredCK.appex/PFLHRPeriodPredCK`

```diff

 	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
+	</array>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
 	<key>com.apple.private.cloudkit.spi</key>

```

### 🆕 PFLHRPeriodPredPush

> `/System/Library/ExtensionKit/Extensions/PFLHRPeriodPredPush.appex/PFLHRPeriodPredPush`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLHRPeriodPredPush</string>
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
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
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
	<array>
		<string>menstrual-cycles-spi</string>
	</array>
	<key>com.apple.private.healthkit.read_authorization_bypass</key>
	<array>
		<string>HKCharacteristicTypeIdentifierUserEnteredMenstrualCycleLength</string>
		<string>HKCharacteristicTypeIdentifierUserEnteredMenstrualPeriodLength</string>
		<string>HKQuantityTypeIdentifierBodyMassIndex</string>
		<string>HKCharacteristicTypeIdentifierDateOfBirth</string>
		<string>HKCategoryTypeIdentifierMenstrualFlow</string>
		<string>HKCategoryTypeIdentifierIntermenstrualBleeding</string>
		<string>HKCategoryTypeIdentifierSexualActivity</string>
		<string>HKCategoryTypeIdentifierCervicalMucusQuality</string>
		<string>HKCategoryTypeIdentifierOvulationTestResult</string>
		<string>HKCategoryTypeIdentifierPregnancyTestResult</string>
		<string>HKCategoryTypeIdentifierProgesteroneTestResult</string>
		<string>HKCategoryTypeIdentifierPregnancy</string>
		<string>HKCategoryTypeIdentifierLactation</string>
		<string>HKCategoryTypeIdentifierContraceptive</string>
		<string>HKQuantityTypeIdentifierBasalBodyTemperature</string>
		<string>HKQuantityTypeIdentifierAppleSleepingWristTemperature</string>
		<string>HKQuantityTypeIdentifierHeartRate</string>
		<string>HKCategoryTypeIdentifierProlongedMenstrualPeriods</string>
		<string>HKCategoryTypeIdentifierPersistentIntermenstrualBleeding</string>
		<string>HKCategoryTypeIdentifierIrregularMenstrualCycles</string>
		<string>HKCategoryTypeIdentifierInfrequentMenstrualCycles</string>
		<string>HKCategoryTypeIdentifierAbdominalCramps</string>
		<string>HKCategoryTypeIdentifierAcne</string>
		<string>HKCategoryTypeIdentifierAppetiteChanges</string>
		<string>HKCategoryTypeIdentifierBladderIncontinence</string>
		<string>HKCategoryTypeIdentifierBloating</string>
		<string>HKCategoryTypeIdentifierBreastPain</string>
		<string>HKCategoryTypeIdentifierChills</string>
		<string>HKCategoryTypeIdentifierConstipation</string>
		<string>HKCategoryTypeIdentifierDiarrhea</string>
		<string>HKCategoryTypeIdentifierDrySkin</string>
		<string>HKCategoryTypeIdentifierFatigue</string>
		<string>HKCategoryTypeIdentifierHairLoss</string>
		<string>HKCategoryTypeIdentifierHeadache</string>
		<string>HKCategoryTypeIdentifierHotFlashes</string>
		<string>HKCategoryTypeIdentifierLowerBackPain</string>
		<string>HKCategoryTypeIdentifierMemoryLapse</string>
		<string>HKCategoryTypeIdentifierMoodChanges</string>
		<string>HKCategoryTypeIdentifierNausea</string>
		<string>HKCategoryTypeIdentifierNightSweats</string>
		<string>HKCategoryTypeIdentifierPelvicPain</string>
		<string>HKCategoryTypeIdentifierSleepChanges</string>
		<string>HKCategoryTypeIdentifierVaginalDryness</string>
		<string>HKCategoryTypeIdentifierSleepAnalysis</string>
		<string>HKQuantityTypeIdentifierHeartRateVariabilitySDNN</string>
		<string>HKQuantityTypeIdentifierRestingHeartRate</string>
	</array>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mlhostd.xpc</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.healthd.server</string>
		<string>com.apple.HealthAlgorithms.HistoricalAnalyzerService</string>
		<string>com.apple.HealthAlgorithms.DayStreamProcessorService</string>
	</array>
</dict>
</plist>

```
### RepackagingWorker

> `/System/Library/ExtensionKit/Extensions/RepackagingWorker.appex/RepackagingWorker`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.aiml.RepackagingWorker</string>
+	<key>com.apple.application-identifier</key>
+	<string>com.apple.aiml.RepackagingWorker</string>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
+	<key>com.apple.private.assistant.settings</key>
+	<true/>
 	<key>com.apple.private.feedbacklogger</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.triald.namespace-management </string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.assistant.settings</string>

 	<array>
 		<string>com.apple.aiml.InstrumentationStreams.RepackagingPlugin</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.siri.analytics.assistant</string>
+		<string>com.apple.feedbacklogger</string>
+		<string>com.apple.assistant.settings</string>
+	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.aiml.InstrumentationStreams.RepackagingPlugin</string>
+	</array>
 	<key>com.apple.siri.analytics.assistant</key>
 	<array>
 		<string>runtime.introspection</string>

```

### 🆕 SiriMASPFLCK

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLCK.appex/SiriMASPFLCK`

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
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.AppSelection.Music</string>
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

> `/System/Library/ExtensionKit/Extensions/SiriMASPFLPush.appex/SiriMASPFLPush`

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
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.AppSelection.Music</string>
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

### 🆕 SiriSuggestionsLightHousePlugin

> `/System/Library/ExtensionKit/Extensions/SiriSuggestionsLightHousePlugin.appex/SiriSuggestionsLightHousePlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.SiriSuggestionsLightHousePlugin</string>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>Siri.Remembers.AssistantSuggestions</string>
		<string>Siri.AssistantSuggestionFeatures</string>
	</array>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>siriRemembers</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siriinferenced.remembers</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.siriinferenced</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.siri.sirisuggestions</string>
	</array>
	<key>com.apple.siriinferenced</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 SiriUserSegmentation

> `/System/Library/ExtensionKit/Extensions/SiriUserSegmentation.appex/SiriUserSegmentation`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.SiriPrivateLearningAnalytics.SiriUserSegmentation</string>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.SiriPrivateLearningAnalytics.SiriUserSegmentation</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SiriUserSegmentation</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>CarPlay.Connected</string>
				<string>Device.Wireless.Bluetooth</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.siri.userfeedbacklearning</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.siri.userfeedbacklearning</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
	</array>
</dict>
</plist>

```

### 🆕 com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.imageio.allowabletypes</key>
	<array>
		<string>org.webmproject.webp</string>
		<string>public.jpeg</string>
		<string>public.png</string>
		<string>com.compuserve.gif</string>
	</array>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.pac.shared_region_id</key>
	<string>WebContent</string>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>AppCacheDisabled</string>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
	</array>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>AppCacheDisabled</string>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
	</array>
	<key>com.apple.private.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.private.webinspector.allow-remote-inspection</key>
	<true/>
	<key>com.apple.private.webinspector.proxy-application</key>
	<true/>
	<key>com.apple.private.webkit.lockdown-mode</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
</dict>
</plist>

```

### 🆕 com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-end-points</key>
	<true/>
	<key>com.apple.QuartzCore.webkit-limited-types</key>
	<true/>
	<key>com.apple.coreaudio.allow-vorbis-decode</key>
	<true/>
	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
	<true/>
	<key>com.apple.developer.cs.allow-jit</key>
	<true/>
	<key>com.apple.developer.gpu-restricted</key>
	<true/>
	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
	<true/>
	<key>com.apple.developer.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.mediaremote.set-playback-state</key>
	<true/>
	<key>com.apple.pac.shared_region_id</key>
	<string>WebContent</string>
	<key>com.apple.private.allow-explicit-graphics-priority</key>
	<true/>
	<key>com.apple.private.coremedia.extensions.audiorecording.allow</key>
	<true/>
	<key>com.apple.private.coremedia.pidinheritance.allow</key>
	<true/>
	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
	<true/>
	<key>com.apple.private.memorystatus</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.enable-state-flags</key>
	<array>
		<string>AppCacheDisabled</string>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
	</array>
	<key>com.apple.private.security.mutable-state-flags</key>
	<array>
		<string>AppCacheDisabled</string>
		<string>EnableExperimentalSandbox</string>
		<string>BlockIOKitInWebContentSandbox</string>
		<string>local:WebContentProcessLaunched</string>
	</array>
	<key>com.apple.private.verified-jit</key>
	<true/>
	<key>com.apple.private.web-browser-engine.webcontent</key>
	<true/>
	<key>com.apple.private.webinspector.allow-remote-inspection</key>
	<true/>
	<key>com.apple.private.webinspector.proxy-application</key>
	<true/>
	<key>com.apple.private.webkit.use-xpc-endpoint</key>
	<true/>
	<key>com.apple.runningboard.assertions.webkit</key>
	<true/>
</dict>
</plist>

```

### 🆕 ApplePMUFirmwareDriver

> `/System/Library/Extensions/ApplePMUFirmwareDriver.kext/ApplePMUFirmwareDriver`

- No entitlements *(yet)*

### 🆕 AppleTopCaseHIDEventDriver

> `/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleTopCaseHIDEventDriver.kext/AppleTopCaseHIDEventDriver`

- No entitlements *(yet)*

### 🆕 AppleUSBTopCaseDriver

> `/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleUSBTopCaseDriver.kext/AppleUSBTopCaseDriver`

- No entitlements *(yet)*

### 🆕 EXBrightKext

> `/System/Library/Extensions/EXBrightKext.kext/EXBrightKext`

- No entitlements *(yet)*
### apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

 	<array>
 		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
 	</array>
+	<key>com.apple.private.vfs.exclave-fs-register</key>
+	<true/>
 	<key>com.apple.private.vfs.graftdmg</key>
 	<true/>
 	<key>com.apple.private.vfs.snapshot</key>

```
### apfs_checkdigest

> `/System/Library/Filesystems/apfs.fs/apfs_checkdigest`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.sep.ramdisk</key>
+	<true/>
 	<key>com.apple.container.crypto.io</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

```
### apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.sep.ramdisk</key>
+	<true/>
 	<key>com.apple.container.crypto.io</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

```
### apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.sep.ramdisk</key>
+	<true/>
 	<key>com.apple.container.crypto.io</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

```
### fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.sep.ramdisk</key>
+	<true/>
 	<key>com.apple.container.crypto.io</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

```
### slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.sep.ramdisk</key>
+	<true/>
+	<key>com.apple.container.crypto.io</key>
+	<true/>
 	<key>com.apple.private.security.disk-device-access</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<string>AppleAPFSUserClient</string>
 </dict>
 </plist>
 

```
### sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.sep.ramdisk</key>
+	<true/>
 	<key>com.apple.container.crypto.io</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

```
### fsck_apfs

> `/System/Library/Filesystems/apfs_userfs.fs/fsck_apfs`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.sep.ramdisk</key>
+	<true/>
 	<key>com.apple.container.crypto.io</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.game-center</key>
+	<array>
+		<string>Account</string>
+	</array>
 	<key>com.apple.private.groupkit.allgroups</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

```

### 🆕 attributionkitd

> `/System/Library/Frameworks/AdAttributionKit.framework/Support/attributionkitd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.backboardd.eventAuthenticationVerification</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstorecomponents</key>
	<true/>
	<key>com.apple.private.appstorecomponents.media-client-id</key>
	<string>com.apple.attributionkitd</string>
	<key>com.apple.private.appstorecomponents.media-client-version</key>
	<string>1</string>
	<key>com.apple.private.appstored</key>
	<array>
		<string>SKANInterop</string>
	</array>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Caches/com.apple.attributionkitd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.AppDistributionLaunchAngel</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
		<string>com.apple.fairplayd.versioned</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.appstorecomponentsd.xpc</string>
		<string>com.apple.backboard.hid.services</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.attributionkitd</string>
		<string>com.apple.AppStoreComponents</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.read-any-bundle</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### CTParserService

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/XPCServices/CTParserService.xpc/CTParserService`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>autobox</string>
+</dict>
+</plist>
 

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 	<true/>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.associated-domains</key>
+	<true/>
 	<key>com.apple.private.attentionawareness</key>
 	<true/>
 	<key>com.apple.private.attentionawareness.poll</key>

 		<string>com.apple.abm.cellularcert</string>
 		<string>com.apple.audioanalyticsd</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>
+		<string>com.apple.SharedWebCredentials</string>
 	</array>
 	<key>com.apple.security.lockdownmode.read</key>
 	<true/>

```
### FamilyControlsAgent

> `/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.carrier_1</string>
 		<string>com.apple.conference</string>
 		<string>com.apple.ids</string>
 		<string>com.apple.UIKit</string>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
-	<key>com.apple.duet.activityscheduler.allow</key>
-	<true/>
 	<key>com.apple.fileprovider.enumerate</key>
 	<true/>
 	<key>com.apple.fileprovider.extension-host</key>
 	<true/>
 	<key>com.apple.fileprovider.import-cookie</key>
 	<true/>
+	<key>com.apple.mobile.keybagd.UserManager.sync</key>
+	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>

 	<array>
 		<string>PURGE_ENTITLEMENT</string>
 		<string>CLIENT_ENTITLEMENT</string>
+		<string>NOTIFICATION_ENTITLEMENT</string>
 	</array>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.endpoint-security.dataless-manipulation</key>
 	<true/>
-	<key>com.apple.private.foundation.fileprovider-lifetime-daemon-dependant</key>
+	<key>com.apple.private.foundation.fileprovider-any-path</key>
 	<true/>
 	<key>com.apple.private.personas.propagate</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.security.storage.DocumentRevisions</key>
 	<true/>
-	<key>com.apple.private.security.storage.ciconia</key>
-	<true/>
 	<key>com.apple.private.security.storage.iCloudDrive</key>
 	<true/>
 	<key>com.apple.private.vfs.authorized-access</key>

 	<true/>
 	<key>com.apple.runningboard.assertions.fileprovider</key>
 	<true/>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/.b/9/Library/LiveFiles/</string>
 		<string>/.b/9/Library/Application Support/FileProvider/</string>
 		<string>/.b/9/Library/CloudStorage/</string>
+		<string>/private/var/mobile/.DocumentRevisions-V100/</string>
+		<string>/var/mobile/.DocumentRevisions-V100/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/private/var/mobile/.backup.i/var/mobile/Library/Application Support/FileProvider/</string>
 		<string>/private/var/mobile/.backup.i/var/mobile/Library/CloudStorage/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Mobile Documents/</string>

 		<string>com.apple.assertiond.applicationstateconnection</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.FileProviderDaemon.AppStoreService</string>
+		<string>com.apple.FileProviderDaemon.FPCKService</string>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.rtcreportingd</string>
 		<string>com.apple.cache_delete.public</string>

```
### financed

> `/System/Library/Frameworks/FinanceKit.framework/financed`

```diff

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.delete</key>
+	<array>
+		<string>kTCCServiceFinancialData</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
-		<string>kTCCServiceAll</string>
+		<string>kTCCServiceFinancialData</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1291</string>
+		<string>1290</string>
+	</array>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.FinanceKit</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 		<string>com.apple.private.alloy.health.sync.sharingsetup</string>
 		<string>com.apple.private.alloy.healthappnotificationsync</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.healthd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>Medications</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Health.Medication</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>
 	<array>
 		<string>WaitForSystemAppMigrationToComplete</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.WorkoutKitXPCService</string>

```
### ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

 	<array>
 		<string>/private/var/mobile/Library/Preferences/.GlobalPreferences.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.ImageIOXPCService/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ImageIOXPCService</string>

```
### coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.ownerpresence.allow</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.preboard.config.allow</key>
+	<true/>
 	<key>com.apple.private.applecredentialmanager.securestore.allow</key>
 	<true/>
 	<key>com.apple.private.applecredentialmanager.securestore.dsl.allow</key>

 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```

### 🆕 applicensedeliveryd

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.applicensedeliveryd</string>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.managedappdistributiond.xpc</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.applicensedelivery</string>
	</array>
	<key>com.apple.security.ts.read-any-bundle</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>adi-client</key>
 	<string>409835401</string>
 	<key>application-identifier</key>
 	<string>com.apple.managedappdistributiond</string>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+	</array>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
+	<key>com.apple.attributionkitd.token-handoff</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.backboardd.eventAuthenticationVerification</key>
+	<true/>
+	<key>com.apple.backboardd.setAuthenticatedTouches</key>
+	<true/>
 	<key>com.apple.dmd-access</key>
 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appinstallationmetrics</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
+	<key>com.apple.private.followup</key>
+	<true/>
+	<key>com.apple.private.install.distributor-info-source</key>
+	<true/>
+	<key>com.apple.private.marketplace-extension-host</key>
+	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/com.apple.AppleMediaServices/</string>

 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 		<string>/Library/Caches/com.apple.managedappdistributiond/</string>
 		<string>/Library/HTTPStorages/com.apple.managedappdistributiond/</string>
+		<string>/Library/Logs/com.apple.StoreServices/HTTPArchives/</string>
+		<string>/tmp/com.apple.managedappdistributiond/</string>
+		<string>/Library/Caches/JetPackCache/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.adid</string>
 		<string>com.apple.apsd</string>
+		<string>com.apple.appinstallationmetrics.xpc</string>
 		<string>com.apple.AssetCacheLocatorService</string>
+		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.cache_delete.public</string>
+		<string>com.apple.CARenderServer</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fontservicesd</string>
+		<string>com.apple.corefollowup.agent</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.lsd.installation</string>

 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.dmd</string>
+		<string>com.apple.xpc.amsuniversallinks</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
+		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.attributionkitd.xpc.token-handoff</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.appstored</string>

 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.managedappdistributiond</string>
+		<string>com.apple.appstored</string>
+	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>com_apple_driver_FairPlayIOKitUserClient</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-container</key>
 	<true/>
+	<key>com.apple.security.system-groups</key>
+	<array>
+		<string>systemgroup.com.apple.installcoordinationd</string>
+		<string>systemgroup.com.apple.applicensedelivery</string>
+	</array>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>
 	<key>com.apple.security.ts.power-assertions</key>

```
### RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>com.apple.SonicKit</string>
+	</array>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

 	<true/>
 	<key>com.apple.runningboard.remoteplayerservice</key>
 	<true/>
+	<key>com.apple.runningboard.sonic</key>
+	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>com.apple.SonicKit</string>
+	</array>
 	<key>com.apple.security.assets.music.read-write</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>com.apple.mediaartworkd.xpc</string>
 		<string>com.apple.MediaPlayer.MPRadioControllerServer</string>
 		<string>com.apple.rtcreportingd</string>
-		<string>com.apple.storebookkeeperd.xpc</string>
 		<string>com.apple.atc.xpc</string>
 		<string>com.apple.atc.xpc.downloadprogress</string>
 		<string>com.apple.atc.xpc.runkeeplocaltask</string>

```
### merchantd

> `/System/Library/Frameworks/ProximityReader.framework/merchantd`

```diff

 	<true/>
 	<key>com.apple.proximityreader.show-tap-ui</key>
 	<true/>
+	<key>com.apple.proxreader.ui-service</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/ContactlessReader/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.accessibility.AXBackBoardServer</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.coreidvd.mobile-document-reader.xpc</string>
 		<string>com.apple.symptom_diagnostics</string>

 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.ak.anisette.xpc</string>
+		<string>com.apple.proxreader.uis-mach</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### SensorKitViewService

> `/System/Library/Frameworks/SensorKit.framework/PlugIns/SensorKitViewService.appex/SensorKitViewService`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>
+		<string>kTCCServiceSensorKitHistoricalCardioMetrics</string>
+		<string>kTCCServiceSensorKitHistoricalMobilityMetrics</string>
 		<string>kTCCServiceSensorKitBedSensing</string>
 		<string>kTCCServiceSensorKitFacialMetrics</string>
 		<string>kTCCServiceSensorKitSpeechMetrics</string>

 	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
+		<string>kTCCServiceSensorKitHistoricalMobilityMetrics</string>
+		<string>kTCCServiceSensorKitHistoricalCardioMetrics</string>
 		<string>kTCCServiceSensorKitBedSensing</string>
 		<string>kTCCServiceSensorKitFacialMetrics</string>
 		<string>kTCCServiceSensorKitSpeechMetrics</string>

 	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>
 	<array>
+		<string>kTCCServiceSensorKitHistoricalMobilityMetrics</string>
+		<string>kTCCServiceSensorKitHistoricalCardioMetrics</string>
 		<string>kTCCServiceSensorKitBedSensing</string>
 		<string>kTCCServiceSensorKitFacialMetrics</string>
 		<string>kTCCServiceSensorKitSpeechMetrics</string>

```

### 🆕 SensorKitLongTermStorageHelper

> `/System/Library/Frameworks/SensorKit.framework/XPCServices/SensorKitLongTermStorageHelper.xpc/SensorKitLongTermStorageHelper`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.locationd.cold-storage</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.sensorkit.debugging.allow</key>
	<true/>
	<key>com.apple.private.tcc.manager.access.read</key>
	<array>
		<string>kTCCServiceAll</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/locationd/ColdStorage/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.locationd.registration</string>
		<string>com.apple.SensorKit.debugging</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.sensorkitd</string>
	</array>
	<key>com.apple.security.ts.read-any-bundle</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### com.apple.SensorKitAppHelper

> `/System/Library/Frameworks/SensorKit.framework/XPCServices/com.apple.SensorKitAppHelper.xpc/com.apple.SensorKitAppHelper`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>
+		<string>kTCCServiceSensorKitHistoricalCardioMetrics</string>
+		<string>kTCCServiceSensorKitHistoricalMobilityMetrics</string>
 		<string>kTCCServiceSensorKitBedSensing</string>
 		<string>kTCCServiceSensorKitFacialMetrics</string>
 		<string>kTCCServiceSensorKitSpeechMetrics</string>

 	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>
 	<array>
+		<string>kTCCServiceSensorKitHistoricalMobilityMetrics</string>
+		<string>kTCCServiceSensorKitHistoricalCardioMetrics</string>
 		<string>kTCCServiceSensorKitBedSensing</string>
 		<string>kTCCServiceSensorKitFacialMetrics</string>
 		<string>kTCCServiceSensorKitSpeechMetrics</string>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrAssistant</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrHammer</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriDictationAssets</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingAsrHammer</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.assistant</string>
 		<string>com.apple.assistant.support</string>
+		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.speech.localspeechrecognition</string>
 		<string>com.apple.corevideo</string>
 		<string>com.apple.UnifiedAssetFramework</string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>1441</string>
 		<string>372</string>
 		<string>401</string>
 		<string>751</string>

```
### storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sqlite.sqlite-encryption</key>
 	<true/>
 	<key>com.apple.private.storekit.background-auth</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/usr/local/bin/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```

### 🆕 translationd

> `/System/Library/Frameworks/Translation.framework/translationd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1821501079</string>
	<key>application-identifier</key>
	<string>translationd</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.coreaudio.allow-opus-codec</key>
	<true/>
	<key>com.apple.developer.networking.multicast</key>
	<true/>
	<key>com.apple.developer.networking.multipath_extended</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.VoiceServicesVocalizerVoice</string>
		<string>com.apple.MobileAsset.VoiceServices.CustomVoice</string>
		<string>com.apple.MobileAsset.VoiceServices.GryphonVoice</string>
		<string>com.apple.MobileAsset.VoiceServices.VoiceResources</string>
		<string>com.apple.MobileAsset.Trial.Siri.SiriTextToSpeech</string>
		<string>com.apple.MobileAsset.LanguageDetectorAssets</string>
		<string>com.apple.MobileAsset.SpeechEndpointAssets</string>
		<string>com.apple.MobileAsset.SpeechTranslationAssets</string>
		<string>com.apple.MobileAsset.SpeechTranslationAssets2</string>
		<string>com.apple.MobileAsset.SpeechTranslationAssets3</string>
		<string>com.apple.MobileAsset.SpeechTranslationAssets4</string>
		<string>com.apple.MobileAsset.SpeechTranslationAssets5</string>
		<string>com.apple.MobileAsset.SpeechTranslationAssets6</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
	<true/>
	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
	<true/>
	<key>com.apple.private.feedbacklogger</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.private.translation</string>
	</array>
	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.private.translation</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/mobile/Library/Trial/</string>
		<string>/private/var/MobileAsset/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>Library/Translation/</string>
		<string>Library/Caches/com.apple.translationd/</string>
		<string>Library/HTTPStorages/com.apple.translationd/</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOSurfaceRootUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.pluginkit.pkd</string>
		<string>com.apple.containermanagerd</string>
		<string>com.apple.assistant.settings</string>
		<string>com.apple.assistant.analytics</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.fairplayd.versioned</string>
		<string>com.apple.triald.namespace-management</string>
		<string>com.apple.audio.AudioQueueServer</string>
		<string>com.apple.audio.AudioSession</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.voiceservices.tts</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.sirittsd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.coreaudio</string>
		<string>com.apple.voicetrigger</string>
		<string>com.apple.coremedia</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.translationd</string>
		<string>com.apple.osprey</string>
		<string>com.apple.voiceservices</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.ane-client</key>
	<true/>
	<key>com.apple.security.ts.asset-access</key>
	<true/>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
	<key>com.apple.security.ts.power-assertions</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.translationd</string>
	<key>com.apple.siri.analytics.assistant</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>406</string>
	</array>
	<key>com.apple.voiced.can-dump-audio</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.siri.osprey</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 libWebKitSwift.dylib

> `/System/Library/Frameworks/WebKit.framework/Frameworks/libWebKitSwift.dylib`

- No entitlements *(yet)*
### DeviceActivityReportService

> `/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/PlugIns/DeviceActivityReportService.appex/DeviceActivityReportService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.InFocus</string>
+		<string>App.MediaUsage</string>
+		<string>App.WebUsage</string>
+		<string>Device.Display.Backlight</string>
+		<string>Media.NowPlaying</string>
+		<string>Notification.Usage</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>

```

### 🆕 AppleDeviceManagementHIDFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleDeviceManagementHIDFilter.plugin/AppleDeviceManagementHIDFilter`

- No entitlements *(yet)*

### 🆕 AppInstallationSettings

> `/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings`

- No entitlements *(yet)*

### 🆕 ContactlessAndCredentialSettings

> `/System/Library/PreferenceBundles/ContactlessAndCredentialSettings.bundle/ContactlessAndCredentialSettings`

- No entitlements *(yet)*

### 🆕 WalletPrivacySettings

> `/System/Library/PreferenceBundles/Privacy/WalletPrivacySettings.bundle/WalletPrivacySettings`

- No entitlements *(yet)*
### axauditd

> `/System/Library/PrivateFrameworks/AccessibilityAudit.framework/Support/axauditd`

```diff

 	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
+	<key>com.apple.accessibility.axauditd</key>
+	<true/>
 	<key>com.apple.accessibility.voiceover</key>
 	<true/>
 	<key>com.apple.backboardd.launchapplications</key>

```
### AXSettingsShortcuts

> `/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/PlugIns/AXSettingsShortcuts.appex/AXSettingsShortcuts`

```diff

 <dict>
 	<key>com.apple.accessibility.AXSettingsShortcuts</key>
 	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.security.no-sandbox

```
### com.apple.accounts.dom

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/XPCServices/com.apple.accounts.dom.xpc/com.apple.accounts.dom`

```diff

 	<array>
 		<string>com.apple.chronoservices</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.mobilesafarishared</string>
+	</array>
 	<key>fairplay-client</key>
 	<string>1397409257</string>
 	<key>keychain-access-groups</key>

```
### AppSSODaemon

> `/System/Library/PrivateFrameworks/AppSSO.framework/Support/AppSSODaemon`

```diff

 	<string>appsso</string>
 	<key>com.apple.rootless.storage.ExtensibleSSO</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/ExtensibleSSO/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.GSSCred</string>

```
### appstorecomponentsd

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>379332956</string>
 	<key>application-identifier</key>
 	<string>com.apple.appstorecomponentsd</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.appconduitd.allowedSPI</key>
 	<array>
 		<string>DeletableSystemAppInstallability</string>

 	<true/>
 	<key>com.apple.carousel.auth-alerts</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Application Support/CrashReporter/DiagnosticMessagesHistory.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.Carousel.authAlertXPCService</string>
 		<string>com.apple.appconduitd.application-manager</string>
 		<string>com.apple.storekitd</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### ASDAskPermissionExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/ASDAskPermissionExtension`

```diff

 	<key>com.apple.private.appstored</key>
 	<array>
 		<string>Purchase</string>
+		<string>Queue</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.appstored.xpc</string>
+		<string>com.apple.appstored.xpc.storequeue</string>
 	</array>
 	<key>com.apple.security.system-container</key>
 	<true/>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<true/>
 	<key>com.apple.ap.adservicesd.statusconditionclient.allow_write</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.appconduitd.device-connection.connect.allow</key>
 	<true/>
 	<key>com.apple.appstored-services-host.event</key>

 	<true/>
 	<key>com.apple.asd.client</key>
 	<string>9824938448</string>
+	<key>com.apple.attributionkitd.token-handoff</key>
+	<true/>
 	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.game-center</key>
+	<array>
+		<string>Games</string>
+	</array>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.appstore</string>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.install.distributor-info-source</key>
+	<true/>
 	<key>com.apple.private.launchservices.canchangeupdateavailability</key>
 	<true/>
 	<key>com.apple.private.mobileinstall.allowedSPI</key>

 	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceFaceID</string>

 	</array>
 	<key>com.apple.remotenotification.preferences</key>
 	<true/>
-	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
-	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
 	<key>com.apple.security.enterprise-volume-access</key>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.gamed</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.lsd.system.mapdb</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>

 		<string>com.apple.backupd</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.backgroundassets.system</string>
+		<string>com.apple.attributionkitd.xpc.token-handoff</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### AppStoreOverlaysService

> `/System/Library/PrivateFrameworks/AppStoreOverlays.framework/PlugIns/AppStoreOverlaysService.appex/AppStoreOverlaysService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.attributionkitd.impression-intake</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.private.appstorecomponents</key>

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.attributionkitd.xpc.impression-intake</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.appstorecomponentsd.xpc</string>
 	</array>

```
### amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

 	</dict>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.forceDomain</key>
+	<true/>
+	<key>com.apple.private.eligibilityd.forceDomainSet</key>
+	<true/>
+	<key>com.apple.private.eligibilityd.resetAllDomains</key>
+	<true/>
+	<key>com.apple.private.eligibilityd.resetDomain</key>
+	<true/>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.commcenter.xpc</string>
 		<string>com.apple.coreidvd.proofing</string>
+		<string>com.apple.eligibilityd</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.xpc.amsserverdatacacheservice</string>
+		<string>com.apple.xpc.amsengagementd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

 	<true/>
 	<key>com.apple.networkd_privileged</key>
 	<true/>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Device.Wireless.APSDInterfaceStatus</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.TextUnderstanding.SmartReplies.Inference</key>
 	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
 	<key>com.apple.accessibility.physicalinteraction.client</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.aosnotification.aosnotifyd-access</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.assistant.flow_service</key>
 	<true/>
 	<key>com.apple.assistant.multiuser.service</key>

 	<true/>
 	<key>com.apple.chrono.invalidate-timelines</key>
 	<true/>
+	<key>com.apple.chronoservices</key>
+	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
 	<key>com.apple.coreaudio.allow-amr-decode</key>

 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>Siri.Health.Federated</string>
 		<string>SiriExecution</string>
 		<string>PostSiriEngagement</string>
 		<string>Siri.PostSiriEngagement</string>

 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.assistant_service</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>SiriPrivateLearning</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Siri.PrivateLearning.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Siri.PrivateLearning.MediaEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>siriRemembers</string>

 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.security.storage.universalaccess</key>

 	<true/>
 	<key>com.apple.private.siri-morphunassetsupdaterd</key>
 	<true/>
+	<key>com.apple.private.sirittsservice.impersonate-clients</key>
+	<array>
+		<string>com.apple.siri.MultilingualReading</string>
+	</array>
 	<key>com.apple.private.sleepd</key>
 	<true/>
 	<key>com.apple.private.social.facebook.upload</key>

 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.powerui.lowpowermode</string>
+		<string>com.apple.reminders</string>
+		<string>com.apple.NanoReminders</string>
+		<string>com.apple.siri.NotificationSource</string>
 	</array>
 	<key>com.apple.private.usernotifications.settings</key>
 	<array>

 		<string>/private/var/mobile/Library/Trial/Treatments/961/</string>
 		<string>/private/var/mobile/Library/Trial/Treatments/1100/</string>
 		<string>/private/var/mobile/Library/Trial/Treatments/1101/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.itunescloud.in-app-message-service</string>
 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.remindd.userInteractive</string>
+		<string>com.apple.chrono.widgetcenterconnection</string>
 		<string>com.apple.sysdiagnose.service.xpc</string>
 		<string>com.apple.icloud.searchpartyd.beaconmanager</string>
 		<string>com.apple.icloud.searchpartyd.pairingmanager</string>

 		<string>com.apple.shazamd</string>
 		<string>com.apple.shazamd.ui</string>
 		<string>com.apple.siri.device_resolution</string>
+		<string>com.apple.AppDistributionLaunchAngel</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.securelocations</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.carpd.xpc</string>
 		<string>com.apple.caraccessoryframework.gatekeeper</string>
+		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.tailspind</string>
 		<string>com.apple.coreduetd.batterysaver</string>

 		<string>com.apple.coremedia.flashlight</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.SetStoreUpdateService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.ClarityUI</string>
+		<string>com.apple.remindd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.audio.puffin</string>
 		<string>com.apple.UnifiedAssetFramework</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.announced.clientid</key>
 	<string>com.apple.assistant.assistantd</string>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.assistant.analytics-observation</key>
 	<true/>
 	<key>com.apple.assistant.cdm.client</key>

 	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
-	<key>com.apple.private.CacheDelete</key>
-	<array>
-		<string>CANCEL_PURGE_ENTITLEMENT</string>
-		<string>CLIENT_ENTITLEMENT</string>
-		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
-		<string>PURGE_ENTITLEMENT</string>
-		<string>PURGEABLE_ENTITLEMENT</string>
-		<string>SERVICE_ENTITLEMENT</string>
-	</array>
 	<key>com.apple.private.CallHistory.read-write</key>
 	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.fides.borealis</key>

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>PostSiriEngagement</string>
+		<string>Siri.AnalyticsIdentifiers.HomeSeed</string>
+		<string>Siri.AnalyticsIdentifiers.UserAggregationId</string>
+		<string>Siri.AnalyticsIdentifiers.UserSeed</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>Siri.SELFProcessedEvent</string>
 		<string>Siri.VoiceTriggerStatistics</string>
 		<string>SiriExecution</string>
 		<string>SiriPrivateLearningSELFEvent</string>
 	</array>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Siri.AnalyticsIdentifiers.HomeSeed</string>
+		<string>Siri.AnalyticsIdentifiers.UserAggregationId</string>
+		<string>Siri.AnalyticsIdentifiers.UserSeed</string>
+	</array>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>

 	<array>
 		<string>com.apple.private.alloy.siri.proxy</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>PrivacyFriendlyAnalyticsIdentifiersProvider</key>
+		<dict>
+			<key>Streams</key>
+			<array>
+				<string>Siri.AnalyticsIdentifiers.HomeSeed</string>
+				<string>Siri.AnalyticsIdentifiers.UserAggregationId</string>
+				<string>Siri.AnalyticsIdentifiers.UserSeed</string>
+			</array>
+		</dict>
+	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>
 		<string>appEntityRelevanceRanking</string>

 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.siri-morphunassetsupdaterd</key>

 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
 		<string>/private/var/db/MobileIdentityData/Indeterminates.plist</string>
 		<string>/private/var/db/MobileIdentityData/Version.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/MobileAsset/Assets/com_apple_MobileAsset_RaiseToSpeakAssets/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_POMMESAssets</string>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
+		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.bulletinboard.observerconnection</string>
 		<string>com.apple.bulletinboard.settingsconnection</string>
 		<string>com.apple.cache_delete.public</string>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.locationd.registration</string>
 		<string>com.apple.locationd.synchronous</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.mediaremoted.xpc</string>
 		<string>com.apple.misagent</string>

 		<string>com.apple.voicetrigger</string>
 		<string>com.apple.voicetrigger.notbackedup</string>
 	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

 	</array>
 	<key>com.apple.trial.status.namespace-name.allow</key>
 	<array>
+		<string>SIRI_AUDIO_APP_SELECTION_HOMEPOD</string>
 		<string>SIRI_AUDIO_DISABLE_MEDIA_ENTITY_SYNC</string>
 		<string>SIRI_AUDIO_LAPSED_MUSIC_USER</string>
 		<string>SIRI_AUDIO_TTS_BEHAVIOR</string>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
+	<key>com.apple.private.appstorecomponents.media-client-id</key>
+	<string>com.apple.akd</string>
+	<key>com.apple.private.appstorecomponents.media-client-version</key>
+	<string>1</string>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.associated-domains</key>

 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.storagekitd.info</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/eligibilityd/eligibility.plist</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.asktod</string>
+		<string>com.apple.timed.xpc</string>
+		<string>com.apple.appstorecomponentsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.nanobuddy</string>
 		<string>com.apple.pairedsync</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.AppStoreComponents</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

 		<string>com.apple.certificates</string>
 		<string>com.apple.identities</string>
 		<string>com.apple.mdm.attestation</string>
+		<string>com.apple.inheritance.cryptoaccess</string>
 	</array>
 	<key>keychain-cloud-circle</key>
 	<true/>

```
### com.apple.BarcodeSupport.BarcodeNotificationService

> `/System/Library/PrivateFrameworks/BarcodeSupport.framework/com.apple.BarcodeSupport.BarcodeNotificationService`

```diff

 	<array>
 		<string>spi</string>
 		<string>public-cellular-plan</string>
+		<string>public-esim-qr-code</string>
 	</array>
 	<key>com.apple.Pasteboard.background-access</key>
 	<true/>

```
### biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.biomed</string>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.Biome</key>

 	<true/>
 	<key>com.apple.private.security.storage.SiriInference</key>
 	<true/>
+	<key>com.apple.private.sqlite.sqlite-encryption</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.SetStoreUpdateService</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### businessservicesd

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/businessservicesd`

```diff

 	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.ciphermld.allow</key>
+	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.setEnvironment</key>

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ciphermld</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```

### 🆕 SetStoreUpdateService

> `/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.SetStoreUpdateService</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.SetStoreUpdateService</string>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.SetStoreUpdateService</string>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.cascade.SetChangeRelayService</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.biome.compute.source.user</string>
		<string>com.apple.biome.compute.source</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.ts.mobile-keybag-access</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.SetStoreUpdateService</string>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 		<string>com.apple.facetime.bag</string>
 		<string>com.apple.imessage.bag</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.SiriViewService</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### CipherMLService

> `/System/Library/PrivateFrameworks/CipherML.framework/XPCServices/CipherMLService.xpc/CipherMLService`

```diff

 <dict>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.fairplayd.versioned</string>
+	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.jett.switch-itms</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>fairplay-client</key>

```
### com.apple.CloudDocs.iCloudDriveFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider`

```diff

 	</array>
 	<key>com.apple.fileprovider.purposeidentifier</key>
 	<string>com.apple.bird</string>
-	<key>com.apple.private.clouddocs.ciconia</key>
-	<true/>
 	<key>com.apple.private.clouddocs.folder-sharing-proxy</key>
 	<true/>
+	<key>com.apple.private.clouddocs.sync-bubble-client</key>
+	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>
 	<true/>
-	<key>com.apple.private.security.storage.ciconia</key>
-	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 	<array>
 		<string>/Library/Application Support/CloudDocs/session/containers/</string>
 	</array>
-	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Application Support/CloudDocs/ciconia/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.revisiond</string>

 		<string>/Library/Application Support/CloudDocs/session/containers/</string>
 		<string>/Library/Application Support/CloudDocs/session/v/</string>
 	</array>
-	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
-	<array>
-		<string>/Library/Application Support/CloudDocs/ciconia/</string>
-	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.revisiond</string>

```
### com.apple.CloudDocs.iCloudDriveFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged`

```diff

 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
-	<key>com.apple.private.clouddocs.ciconia</key>
-	<true/>
 	<key>com.apple.private.clouddocs.folder-sharing-proxy</key>
 	<true/>
 	<key>com.apple.private.cloudkit.masquerade</key>

 		<string>com.apple.bird</string>
 		<string>group.com.apple.iCloudDrive</string>
 	</array>
-	<key>com.apple.private.security.storage.CloudDocsDB</key>
-	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### CloudDocsDiagnostic

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic`

```diff

 	<true/>
 	<key>com.apple.private.clouddocs.spi</key>
 	<array>
-		<string>dumpDatabaseTo:containerID:personaID:includeAllItems:reply:</string>
+		<string>dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:</string>
 	</array>
 	<key>com.apple.private.pluginkit.persona</key>
 	<string>system</string>

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Application Support/CloudDocs/session/db/</string>
-		<string>/Library/Application Support/CloudDocs/session/ciconia_diagnose/</string>
 	</array>
 	<key>com.apple.security.exception.ts.tmpdir</key>
 	<array>

 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Application Support/CloudDocs/session/db/</string>
-		<string>/Library/Application Support/CloudDocs/session/ciconia_diagnose/</string>
 	</array>
 </dict>
 </plist>

```
### bird

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/bird`

```diff

 	<true/>
 	<key>com.apple.private.clouddocs.bundle-service</key>
 	<true/>
-	<key>com.apple.private.clouddocs.ciconia</key>
-	<true/>
 	<key>com.apple.private.clouddocs.telemetry-disk-checker</key>
 	<true/>
 	<key>com.apple.private.cloudkit.accountDetailAccess</key>

 	<true/>
 	<key>com.apple.private.desktopservices.icloud-desktop.move-and-merge</key>
 	<true/>
+	<key>com.apple.private.foundation.fileprovider-any-path</key>
+	<true/>
 	<key>com.apple.private.foundation.fileprovideridentifier</key>
 	<string>com.apple.bird</string>
 	<key>com.apple.private.iaaccounts</key>

 	<true/>
 	<key>com.apple.private.security.storage.MobileDocuments</key>
 	<true/>
-	<key>com.apple.private.security.storage.ciconia</key>
-	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

```
### cloudd

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd`

```diff

 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
+	<key>com.apple.spaceattribution.private</key>
+	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNL</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNLOverrides</string>
+		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingNLOverrides</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 		<string>/private/var/tmp/</string>
 		<string>/private/var/mobile/tmp/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.e5rt.e5bundlecache/</string>

```
### contextstored

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored`

```diff

 		<string>IOAccelContext2</string>
 		<string>IOAccelDevice2</string>
 		<string>IOAccelSharedUserClient2</string>
+		<string>IOGPUDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.network.server</key>
 	<true/>

```
### com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrAssistant</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrHammer</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriDictationAssets</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingAsrHammer</string>
 		<string>com.apple.MobileAsset.EmbeddedSpeech</string>
 		<string>com.apple.MobileAsset.EmbeddedSpeechWatch</string>
 		<string>com.apple.MobileAsset.EmbeddedSpeechMac</string>

```
### parsec-fbf

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf`

```diff

 		<string>com.apple.assistant.support</string>
 		<string>com.apple.spotlightui</string>
 	</array>
-	<key>com.apple.springboard.allHomeScreenApplicationBundleIdentifiers</key>
-	<true/>
 	<key>fairplay-client</key>
 	<string>511712240</string>
 	<key>keychain-access-groups</key>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.parsecd</string>
 	<key>com.apple.coreduetd.allow</key>

 	<array>
 		<string>group.com.apple.PegasusConfiguration</string>
 	</array>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.subscriptionservice.all-sources.read-only</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readWrite</key>

 	<array>
 		<string>group.com.apple.PegasusConfiguration</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.xpc.amsengagementd</string>

 		<string>com.apple.trial.status</string>
 		<string>com.apple.networkserviceproxy</string>
 		<string>com.apple.apsd</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 CoreRepairCoreXPCService

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/XPCServices/CoreRepairCoreXPCService.xpc/CoreRepairCoreXPCService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.AppleNVMeEAN.allow</key>
	<true/>
	<key>com.apple.CheckerBoard.services.reboot</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>identity</string>
	</array>
	<key>com.apple.frontboard.shutdown</key>
	<true/>
	<key>com.apple.keystore.fdr-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.libFDR.AllowIdentifierOverride</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.nfcd.info</key>
	<true/>
	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>AmbientLightSensorSerialNumber</string>
		<string>BasebandBoardSnum</string>
		<string>BasebandChipId</string>
		<string>BasebandSerialNumber</string>
		<string>BasebandUniqueId</string>
		<string>RosalineSerialNumber</string>
		<string>SavageChipID</string>
		<string>SavageSerialNumber</string>
		<string>HWModelStr</string>
		<string>ProductType</string>
		<string>SavageUID</string>
		<string>SavageChipID</string>
		<string>YonkersUID</string>
		<string>YonkersChipID</string>
		<string>UniqueChipID</string>
		<string>BatterySerialNumber</string>
		<string>MobileEquipmentIdentifier</string>
		<string>SerialNumber</string>
		<string>SecureElementID</string>
		<string>IceFallID</string>
		<string>MesaSerialNumber</string>
	</array>
	<key>com.apple.private.PurpleReverseProxy.allowed</key>
	<true/>
	<key>com.apple.private.ZhuGeInternalSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.apfs.revert-to-snapshot</key>
	<true/>
	<key>com.apple.private.applesepmanager.allow</key>
	<true/>
	<key>com.apple.private.bindfs-allow</key>
	<true/>
	<key>com.apple.private.core-repair</key>
	<true/>
	<key>com.apple.private.corerepair.fdr</key>
	<true/>
	<key>com.apple.private.img4.nonce.pdi</key>
	<true/>
	<key>com.apple.private.img4.nonce.trust-cache</key>
	<true/>
	<key>com.apple.private.iokit.batterydataprecise</key>
	<true/>
	<key>com.apple.private.iokit.batterydateoffirstuse</key>
	<true/>
	<key>com.apple.private.iokit.nvram-write-access</key>
	<true/>
	<key>com.apple.private.security.AppleImage4.user-client</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.vfs.snapshot</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.iokit.powerdxpc</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleImage4UserClient</string>
		<string>AppleSEPUserClient</string>
		<string>AppleNVMeEANUC</string>
		<string>IOAccessoryManagerUserClient</string>
		<string>AppleBiometricServicesUserClient</string>
	</array>
	<key>com.apple.symptom_analytics.query</key>
	<true/>
	<key>com.apple.symptoms.NetworkOfInterest</key>
	<true/>
</dict>
</plist>

```
### CoreSpeechXPC

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/CoreSpeechXPC.xpc/CoreSpeechXPC`

```diff

 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAttentionAssets</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsWatch</string>

 	<array>
 		<string>/private/var/MobileAsset/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/UnifiedAssetFramework/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobileasset.autoasset</string>

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>
 	<true/>
+	<key>com.apple.bluetooth.doap</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.callkit</key>

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.coreduetd.people</key>
+	<true/>
 	<key>com.apple.corespeech.cat.xpc</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>

 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrHammer</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriDictationAssets</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAttentionAssets</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
+		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingAsrHammer</string>
 		<string>com.apple.MobileAsset.AdBlockerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssets</string>
 		<string>com.apple.MobileAsset.VoiceTriggerAssetsIPad</string>

 	</array>
 	<key>com.apple.private.homekit.siri-audio-connection</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.corespeechd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>__Koa__</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.InstalledApp</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomCarName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomCarProfileName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomContactGroupName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomContactName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaAudiobookAuthorName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaAudiobookTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaMusicArtistName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaPlaylistTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaShowTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomNotebookItemGroupName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomNotebookItemTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomPaymentsAccountNickname</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomPaymentsOrganizationName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomPhotoAlbumName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomPhotoTag</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomVoiceCommandName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomWorkoutActivityName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaAudiobookAuthor</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaAudiobookTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaMusicArtistName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaPlaylistTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaShowTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.Shortcut.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>App.Shortcut.Phrase</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Calendar.Event</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>CarPlay.RadioStation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Contacts.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>FindMy.Device</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Fitness.Guest</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Health.Medication</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>HomeKit.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Location.SignificantLocation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Media.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Podcasts.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Siri.PrivateLearning.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Siri.PrivateLearning.MediaEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>UserAccount.Identity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.iokit.darkwake-control</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.microphoneattribution.allow</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.usesecuresession</key>
+	<true/>
 	<key>com.apple.private.mediasafetynet.exception.announcemessage</key>
 	<true/>
 	<key>com.apple.private.mobiletimerd</key>

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.rootless.storage.CoreSpeech</key>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/CoreDuet/</string>
+		<string>/Library/PeopleSuggester/</string>
 		<string>/Library/Caches/com.apple.corespeech.cat.xpc/</string>
 		<string>/Library/Trial/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.coreduetd.people</string>
 		<string>com.apple.server.bluetooth</string>
 		<string>com.apple.server.bluetooth.general.xpc</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager</string>

 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.homepodaccessorysettings.server</string>
+		<string>com.apple.audio.isolated.client.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.assistant</string>
 		<string>com.apple.nano</string>
 		<string>com.apple.raisetospeak</string>

 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
 		<string>net.routetable.0.0.3.0</string>
+		<string>kern.exclaves_status</string>
+		<string>kern.task_conclave</string>
 	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>

```
### speechmodeltrainingd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/speechmodeltrainingd`

```diff

 	<array>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrAssistant</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriDictationAssets</string>
+		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.EmbeddedSpeech</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>

 		<string>/Library/HTTPStorages</string>
 		<string>/Library/HTTPStorages/com.apple.siri.speech-model-training/</string>
 		<string>/Library/Trial/</string>
+		<string>/Library/UnifiedAssetFramework/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### com.apple.datadetectors.AddToRecentsService

> `/System/Library/PrivateFrameworks/DataDetectorsUI.framework/XPCServices/com.apple.datadetectors.AddToRecentsService.xpc/com.apple.datadetectors.AddToRecentsService`

```diff

 	<string>com.apple.datadetectors.AddToRecentsService</string>
 	<key>com.apple.private.corerecents</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobilesafarishared</string>
+	</array>
+	<key>com.apple.springboard.openurlinbackground</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>com.apple.datadetectors.AddToRecentsService</string>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 		<string>com.apple.MobileAsset.VoiceServices.CombinedVocalizerVoices</string>
 		<string>com.apple.MobileAsset.VoiceServicesVocalizerVoice</string>
 		<string>com.apple.MobileAsset.MacinTalkVoiceAssets</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone12AndOlder</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone13x</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone14x</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x</string>
+		<string>com.apple.MobileAsset.VoiceTriggerRePromptListiPad</string>
 	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.install.distributor-info-source</key>
+	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
-	<key>com.apple.private.security.storage-exempt.heritable</key>
+	<key>com.apple.private.security.datavault.controller</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 		<string>group.com.apple.weather</string>
 		<string>group.com.apple.mail</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Preferences/com.apple.coreaudio.device.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/VoiceTrigger/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>

```
### datamigratorhelper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/datamigratorhelper.xpc/datamigratorhelper`

```diff

 <dict>
 	<key>com.apple.private.kernel.panic</key>
 	<true/>
+	<key>com.apple.private.logging.admin</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.logd.admin</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 IngestService

> `/System/Library/PrivateFrameworks/DendriteIngest.framework/XPCServices/IngestService.xpc/IngestService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.aiml.dendrite.host-ingestion</key>
	<true/>
</dict>
</plist>

```

### 🆕 ContinuousRecordingsDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/ContinuousRecordings/</string>
	</array>
</dict>
</plist>

```
### HomeEnergyDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/HomeEnergyDiagnosticExtension.appex/HomeEnergyDiagnosticExtension`

```diff

 		<string>/Library/Application Support/com.apple.homeenergyd/</string>
 		<string>/Library/Application Support/homeenergyd/</string>
 		<string>/Library/Application Support/homeenergyd/com.apple.homeenergyd/</string>
+		<string>/Library/homeenergyd/</string>
+		<string>/Library/homeenergyd/com.apple.homeenergyd/</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/Application Support/com.apple.homeenergyd/</string>
+		<string>/private/var/mobile/Library/homeenergyd/</string>
+		<string>/private/var/mobile/Library/homeenergyd/com.apple.homeenergyd/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
 	<array>

```
### DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

 	<string>development</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.DPSubmissionService</string>
-	<key>com.apple.developer.exposure-notification</key>
-	<true/>
 	<key>com.apple.developer.icloud-services</key>
 	<array>
 		<string>CloudKit</string>

 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
-	<key>com.apple.private.exposure-notification</key>
-	<true/>
-	<key>com.apple.private.exposure-notification-device-identity</key>
+	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
-	<key>com.apple.private.exposure-notification-differential-privacy</key>
+	<key>com.apple.private.network.system-token-fetch</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>Library/PPM/</string>
+		<string>Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.DPSubmissionService/</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.DPSubmissionService/</string>
+	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
 	<key>iCloudServices</key>

```
### diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.vfs.role-account-openfrom</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/tmp/di2_coverage/</string>
-	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>DIDeviceCreatorUserClient</string>

```
### FilesystemMetadataSnapshotService

> `/System/Library/PrivateFrameworks/DiskSpaceDiagnostics.framework/XPCServices/FilesystemMetadataSnapshotService.xpc/FilesystemMetadataSnapshotService`

```diff

 		<string>CLIENT_ENTITLEMENT</string>
 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.apfs.get_purgeable_bulk_info</key>
+	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>
 	<true/>
 	<key>com.apple.rootless.datavault.metadata</key>

```
### facetimemessagestored

> `/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored`

```diff

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.commcenter.coretelephony.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 FPCKService

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/XPCServices/FPCKService.xpc/FPCKService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.FileProviderDaemon.FPCKService</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.FileProviderDaemon.FPCKService</string>
	<key>com.apple.private.rtcreportingd</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.storage.FileProvider</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceSystemPolicyDesktopFolder</string>
		<string>kTCCServiceSystemPolicyDocumentsFolder</string>
		<string>kTCCServiceFileProviderDomain</string>
	</array>
	<key>com.apple.private.vfs.authorized-access</key>
	<true/>
	<key>com.apple.private.vfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.revisiond</string>
		<string>com.apple.FileCoordination</string>
		<string>com.apple.rtcreportingd</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-write</key>
	<array>
		<string>kern.rage_vnode</string>
		<string>kern.vfsnspace</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>254</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 finhealthclient

> `/System/Library/PrivateFrameworks/FinHealth.framework/ClientTools/finhealthclient`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.finhealth.all-access</key>
	<true/>
	<key>com.apple.payment.all-access</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.passd.payment</string>
	</array>
</dict>
</plist>

```
### GameCenterAuthenticateExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterAuthenticateExtension.appex/GameCenterAuthenticateExtension`

```diff

 	</array>
 	<key>com.apple.private.hsa-authentication-processing</key>
 	<true/>
+	<key>com.apple.private.ids.registration</key>
+	<array>
+		<string>com.apple.madrid</string>
+		<string>com.apple.ess</string>
+	</array>
 	<key>com.apple.private.messages.associated-message-extension-bundle-identifiers</key>
 	<array>
 		<string>com.apple.gamecenter.GameCenterUIService.GameCenterMessageExtension</string>
 	</array>
-	<key>com.apple.private.mobilesms.messages-recipient-vetting</key>
-	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### GameCenterDashboardExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterDashboardExtension.appex/GameCenterDashboardExtension`

```diff

 	<array>
 		<string>com.apple.gamecenter.GameCenterUIService.GameCenterMessageExtension</string>
 	</array>
-	<key>com.apple.private.mobilesms.messages-recipient-vetting</key>
-	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### GameCenterMatchmakerExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension`

```diff

 	<array>
 		<string>com.apple.gamecenter.GameCenterUIService.GameCenterMessageExtension</string>
 	</array>
-	<key>com.apple.private.mobilesms.messages-recipient-vetting</key>
-	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### GameCenterTurnBasedMatchmakerExtension

> `/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterTurnBasedMatchmakerExtension.appex/GameCenterTurnBasedMatchmakerExtension`

```diff

 	<array>
 		<string>com.apple.gamecenter.GameCenterUIService.GameCenterMessageExtension</string>
 	</array>
-	<key>com.apple.private.mobilesms.messages-recipient-vetting</key>
-	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

```
### geod

> `/System/Library/PrivateFrameworks/GeoServices.framework/geod`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.geoservices.locationshift.cache-access</key>
+	<true/>
 	<key>com.apple.geoservices.offline-services</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### heard

> `/System/Library/PrivateFrameworks/HearingCore.framework/heard`

```diff

 	</array>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.accessibility.ActionSheet</key>
+	<true/>
+	<key>com.apple.accessibility.IDSServices</key>
+	<true/>
 	<key>com.apple.accessibility.api</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>

```
### homeenergyd

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

 	<key>com.apple.security.exception.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/mobile/Library/Application Support/com.apple.homeenergyd/</string>
+		<string>/private/var/mobile/Library/homeenergyd/</string>
+		<string>/private/var/mobile/Library/homeenergyd/com.apple.homeenergyd/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Application Support/com.apple.homeenergyd/</string>
 		<string>/Library/Application Support/homeenergyd/</string>
 		<string>/Library/Application Support/homeenergyd/com.apple.homeenergyd/</string>
+		<string>/Library/homeenergyd/</string>
+		<string>/Library/homeenergyd/com.apple.homeenergyd/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.ts.system-info</key>
+	<array>
+		<string>net.link.addr</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.PairingManager.Read</key>
 	<true/>
+	<key>com.apple.StatusKit.presence.clientID</key>
+	<string>homed</string>
 	<key>com.apple.SystemConfiguration.SCPreferences-read-access</key>
 	<array>
 		<string>preferences.plist</string>

 		<string>com.apple.homekit</string>
 		<key>com.apple.homekit.events</key>
 		<string>com.apple.homekit</string>
-		<key>com.apple.homekit.events.playground</key>
-		<string>com.apple.homekit</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.bluetooth.xpc</string>
-		<string>com.apple.chronoservices</string>
 		<string>com.apple.ThreadNetwork.xpc</string>
 		<string>com.apple.coreautomationd.xpc.root</string>
 		<string>com.apple.familycircle.agent</string>

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.wpantund.xpc</string>
 		<string>com.apple.sleepd.sleepserver</string>
+		<string>com.apple.StatusKit.presence</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.systemstatus.activityattribution</key>
 	<true/>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>
 	<key>com.apple.wifi.manager-access</key>

```
### identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

 	</array>
 	<key>com.apple.private.nehelper.privileged</key>
 	<true/>
+	<key>com.apple.private.network.delegation-allowlist</key>
+	<true/>
 	<key>com.apple.private.network.interface-control</key>
 	<true/>
 	<key>com.apple.private.network.restricted.port.ids_cloud_service_connector</key>

 	<string>/Library/Caches/PassKit/</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.kvsd</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-write</key>

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 	<true/>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.MobileSMS</string>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
 	<key>com.apple.private.interstellar.data-access</key>

 	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
-	<key>com.apple.private.corespotlight.internal</key>
-	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.dmd.emergency-mode</key>

 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.avconference.avctester</string>
-		<string>com.apple.private.alloy.electrictouch</string>
 		<string>com.apple.private.alloy.messagesquickswitch</string>
 		<string>com.apple.private.alloy.sms</string>
 		<string>com.apple.madrid</string>

 	<key>com.apple.private.ids.messaging.high-priority</key>
 	<array>
 		<string>com.apple.private.alloy.avconference.avctester</string>
-		<string>com.apple.private.alloy.electrictouch</string>
 		<string>com.apple.private.alloy.messagesquickswitch</string>
 		<string>com.apple.private.alloy.sms.watch</string>
 		<string>com.apple.private.alloy.sms</string>

 	</array>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>
-	<key>com.apple.private.corespotlight.search.internal</key>
-	<true/>
 	<key>com.apple.multitasking.systemappassertions</key>
 	<true/>
 	<key>com.apple.private.exposure-notification</key>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.timed.xpc</string>
-        <string>com.apple.transparencyd</string>
+		<string>com.apple.transparencyd</string>
+		<string>com.apple.spotlight.SearchAgent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.private.ids.report-spam-message</key>
 	<true/>
-    <key>com.apple.transparency.kt</key>
-    <true/>
+	<key>com.apple.transparency.kt</key>
+	<true/>
 </dict>
 </plist>
 

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.MobileSMS</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.dmd.emergency-mode</key>

 		<string>com.apple.gamed</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.TextUnderstanding.SmartReplies.Inference</string>
+		<string>com.apple.spotlight.SearchAgent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

 		<string>com.apple.lsd.system.mapdb</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.nanoprefsync</string>
+		<string>com.apple.managedappdistributiond.installcoordination</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### IntelligencePlatformComputeService

> `/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService`

```diff

 	<true/>
 	<key>com.apple.intelligenceplatform.AssetRegistry</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.Coordination</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EventLog</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.InferenceSupport</key>

 		<string>Location.HashedCoordinates</string>
 		<string>Motion.Activity</string>
 	</array>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
 	<key>com.apple.private.email</key>
 	<true/>
 	<key>com.apple.private.photoanalysisd.access</key>

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.IntelligencePlatform</key>
 	<true/>
+	<key>com.apple.private.sqlite.sqlite-encryption</key>
+	<true/>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
 		<string>kTCCServicePhotos</string>

 	<array>
 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.cmfsyncagent.embedded.auth</string>
 		<string>com.apple.email.maild</string>

 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
+		<string>com.apple.intelligenceplatform.Coordination</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ERMLRuntimePlugin

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/PlugIns/ERMLRuntimePlugin.appex/ERMLRuntimePlugin`

```diff

 	<array>
 		<string>entityRelevanceHistoricalFeatures</string>
 	</array>
+	<key>com.apple.private.security.no-container</key>
+	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>

```
### destinationd

> `/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd`

```diff

 	<true/>
 	<key>com.apple.locationd.private_info</key>
 	<true/>
-	<key>com.apple.locationd.prompt_behavior</key>
-	<true/>
 	<key>com.apple.locationd.route_hint</key>
 	<true/>
 	<key>com.apple.locationd.slv_configurer</key>

```
### nanomapscd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/nanomapscd`

```diff

 	<true/>
 	<key>com.apple.geoservices.custom-manifest-configuration</key>
 	<true/>
+	<key>com.apple.geoservices.locationshift.cache-access</key>
+	<true/>
 	<key>com.apple.geoservices.map-subscriptions.watch-sync</key>
 	<true/>
 	<key>com.apple.locationd.authorizeapplications</key>

```
### navd

> `/System/Library/PrivateFrameworks/MapsSupport.framework/navd`

```diff

 	<true/>
 	<key>com.apple.assertiond.app-state-monitor</key>
 	<true/>
+	<key>com.apple.cards.all-access</key>
+	<true/>
 	<key>com.apple.chronoservices</key>
 	<true/>
 	<key>com.apple.findmy.findmylocate.friendshipservice</key>

 	<true/>
 	<key>com.apple.geoanalyticsd.analytics</key>
 	<true/>
+	<key>com.apple.geoservices.map-subscriptions.size-estimate</key>
+	<true/>
 	<key>com.apple.geoservices.preload</key>
 	<true/>
 	<key>com.apple.geoservices.resource-manifest-update-assertion</key>

 		<key>value</key>
 		<string>/System/Library/PrivateFrameworks/MapsSupport.framework/navd</string>
 	</dict>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 	<array>
 		<string>com.apple.Maps</string>
 	</array>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Maps</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.contactsd</string>
 		<string>com.apple.accessories.externalaccessory-server</string>
+		<string>com.apple.passd.library</string>
 		<string>com.apple.assertiond.applicationstateconnection</string>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.audio.AudioQueueServer</string>

```
### mapssyncd

> `/System/Library/PrivateFrameworks/MapsSync.framework/mapssyncd`

```diff

 	<array>
 		<string>com.apple.cloudd</string>
 		<string>com.apple.apsd</string>
+		<string>com.apple.geod</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>App.Intent</string>
 		<string>App.InFocus</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>

 		<string>com.apple.duetexpertd</string>
 		<string>com.apple.spotlightui</string>
 		<string>com.apple.suggestions</string>
+		<string>com.apple.TelephonyUtilities.sharePlayAppPolicies</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.security.ts.mach-task-name</key>
 	<true/>
-	<key>com.apple.security.ts.springboard-services</key>
-	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.mediaremoted</string>
 	<key>com.apple.sharing.ProximityClient</key>

```
### MessagesBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService`

```diff

 		<string>blastdoor-post-launch</string>
 		<string>blastdoor-hubble</string>
 	</array>
+	<key>com.apple.private.security.storage.PassKit</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>blastdoor-messages</string>

```
### accessoryupdaterd

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Support/accessoryupdaterd`

```diff

 	<array>
 		<string>com.apple.accessoryupdater.UARPUpdaterServiceStrap</string>
 	</array>
+	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>
+	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
 	<key>com.apple.system.diagnostics.iokit-properties</key>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.packages</key>
 	<true/>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.cloudkit.spi</key>
 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.install.distributor-info-source</key>
+	<true/>
+	<key>com.apple.private.iokit.soc-limit</key>
+	<true/>
 	<key>com.apple.private.keychain-backup-client</key>
 	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>

 		<string>CopySafeHarbors</string>
 		<string>Install</string>
 		<string>InstallForLaunchServices</string>
-		<string>InstallForInstallCoordination</string>
+		<string>CreateSerializedPlaceholder</string>
 		<string>Lookup</string>
 		<string>ProcessRestoredContainer</string>
 		<string>RegisterSafeHarbor</string>

```
### medialibraryd

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd`

```diff

 	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>
 	<true/>
+	<key>com.apple.private.CacheDelete</key>
+	<array>
+		<string>CLIENT_ENTITLEMENT</string>
+		<string>PURGEABLE_ENTITLEMENT</string>
+		<string>SERVICE_ENTITLEMENT</string>
+		<string>NOTIFICATION_ENTITLEMENT</string>
+		<string>PURGE_ENTITLEMENT</string>
+		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
+	</array>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.medialibraryd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MediaLibrary</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Media.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.privacy.accounting.write</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.FSEvents</string>
+		<string>com.apple.cache_delete</string>
 		<string>com.apple.assistant.multiuser.service</string>
 		<string>com.apple.medialibraryd.xpc</string>
 		<string>com.apple.privacyaccountingd</string>
-		<string>com.apple.storebookkeeperd.xpc</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
+		<string>com.apple.SetStoreUpdateService</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.support</string>
 	</array>
 	<key>com.apple.siri.koa.donate.internal</key>
 	<true/>

```

### 🆕 NFRadioPowerSwitch

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRadioPowerSwitch.xpc/NFRadioPowerSwitch`

- No entitlements *(yet)*

### 🆕 NFRestoreService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFRestoreService.xpc/NFRestoreService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.private.network.intcoproc.restricted</key>
	<true/>
	<key>com.apple.private.stockholm.allow</key>
	<true/>
	<key>com.apple.private.stockholm.remoteservice</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>AppleStockholmControlUserClient</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleStockholmControlUserClient</string>
	</array>
</dict>
</plist>

```

### 🆕 NFUIService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.sharing.Client</key>
	<true/>
</dict>
</plist>

```
### com.apple.SharePlay.NearbyInvitationsService

> `/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService`

```diff

 	<true/>
 	<key>com.apple.nearbyinteraction.background</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.aps-client-cert-access</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 	<array>
 		<string>com.apple.SharePlay.NearbyInvitationsService</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
+	<key>com.apple.security.network.server</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/Library/Preferences/com.apple.applepushserviced.plist</string>

```
### com.apple.NeighborhoodActivityConduitService

> `/System/Library/PrivateFrameworks/NeighborhoodActivityConduit.framework/XPCServices/com.apple.NeighborhoodActivityConduitService.xpc/com.apple.NeighborhoodActivityConduitService`

```diff

 	</dict>
 	<key>com.apple.private.contacts</key>
 	<true/>
+	<key>com.apple.private.icfcallserver</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.facetime.multi</string>

 		<string>com.apple.RemoteDisplay</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.imagent.embedded.auth</string>
+		<string>com.apple.incoming-call-filter-server</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.passd.class-d</string>
+	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```
### peopled

> `/System/Library/PrivateFrameworks/People.framework/peopled`

```diff

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.private.CallHistory.read-write</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents.relevant.custom-identifier-allowed</key>

```

### 🆕 PPSFeatureFlagReader

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PPSFeatureFlagReader.xpc/PPSFeatureFlagReader`

- No entitlements *(yet)*
### previewsd

> `/System/Library/PrivateFrameworks/PreviewsOSSupport.framework/Support/previewsd`

```diff

 	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
-	<key>com.apple.osanalytics.canusediagnosticmonitor</key>
-	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>

```
### com.apple.PrintKit.PrinterTool

> `/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.printing.bandservice</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

```
### privacyaccountingd

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/Versions/A/Resources/privacyaccountingd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.privacyaccountingd</string>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.security.storage.PrivacyAccounting</key>

```
### DPMLRuntimePlugin

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePlugin.appex/DPMLRuntimePlugin`

```diff

 	<true/>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>SpringBoard.GestureEducation.PillLaunch</string>
 		<string>SystemSettings.GestureEducation.PillOutcome</string>
 		<string>SystemSettings.GestureEducation.Multitasking</string>
+		<string>Safari.WindowProxy</string>
+		<string>Siri.AssistantSuggestionFeatures</string>
+		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
+		<string>IntelligencePlatform.EntityTagging.PersonInference</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>visualIdentifier</string>
+	</array>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
+		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>1543</string>
 		<string>1544</string>
 		<string>841</string>
+		<string>1548</string>
+		<string>1551</string>
+		<string>1547</string>
+		<string>1549</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### DPMLRuntimePluginClassB

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginClassB.appex/DPMLRuntimePluginClassB`

```diff

 	<true/>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>SpringBoard.GestureEducation.PillLaunch</string>
 		<string>SystemSettings.GestureEducation.PillOutcome</string>
 		<string>SystemSettings.GestureEducation.Multitasking</string>
+		<string>Safari.WindowProxy</string>
+		<string>Siri.AssistantSuggestionFeatures</string>
+		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
+		<string>IntelligencePlatform.EntityTagging.PersonInference</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>visualIdentifier</string>
+	</array>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
+		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>1543</string>
 		<string>1544</string>
 		<string>841</string>
+		<string>1548</string>
+		<string>1551</string>
+		<string>1547</string>
+		<string>1549</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### DPMLRuntimePluginNonDnU

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PlugIns/DPMLRuntimePluginNonDnU.appex/DPMLRuntimePluginNonDnU`

```diff

 	<true/>
 	<key>com.apple.coreidvd.identity-proofing-data-sharing</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>

 		<string>SpringBoard.GestureEducation.PillLaunch</string>
 		<string>SystemSettings.GestureEducation.PillOutcome</string>
 		<string>SystemSettings.GestureEducation.Multitasking</string>
+		<string>Safari.WindowProxy</string>
+		<string>Siri.AssistantSuggestionFeatures</string>
+		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
+		<string>IntelligencePlatform.EntityTagging.PersonInference</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>visualIdentifier</string>
+	</array>
 	<key>com.apple.private.photos.internaldirectory.data.read-write</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.private.dprivacyd</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomed</string>
+		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>1543</string>
 		<string>1544</string>
 		<string>841</string>
+		<string>1548</string>
+		<string>1551</string>
+		<string>1547</string>
+		<string>1549</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### ManagedAppsSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/ManagedAppsSubscriber.xpc/ManagedAppsSubscriber`

```diff

 	<true/>
 	<key>com.apple.dmd.operation.fetch-apps</key>
 	<true/>
-	<key>com.apple.dmd.operation.remove-app</key>
+	<key>com.apple.dmd.operation.stop-managing-app</key>
 	<true/>
 	<key>com.apple.private.managedappdistribution.ddm</key>
 	<true/>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

 	<true/>
 	<key>com.apple.private.accounts.bundleidspoofing</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.InFocus</string>
+		<string>Device.Display.Backlight</string>
+		<string>Media.NowPlaying</string>
+		<string>Notification.Usage</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>App.MediaUsage</string>

```
### budd

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/budd`

```diff

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```
### AppLaunchIntentExtension

> `/System/Library/PrivateFrameworks/SiriAppLaunchIntents.framework/PlugIns/AppLaunchIntentExtension.appex/AppLaunchIntentExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.siri.SiriAppLaunchIntents.AppLaunchIntentExtension</string>
 	<key>com.apple.appletv.pbs.app-info-service-access</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.private.intents.extension</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 </dict>
 </plist>
 

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 	<string>com.apple.siriinferenced</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.CoreRoutine.LocationOfInterest</key>
+	<true/>
 	<key>com.apple.Maps.tripsharing.sharing</key>
 	<true/>
 	<key>com.apple.MobileAsset.SoftwareUpdate</key>

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siriinferenced</string>
+	<key>com.apple.assistant.settings</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>
 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.extensionkit.host.extension-point-identifiers</key>

 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
 	<key>com.apple.mlruntime.host.ondemand</key>
 	<true/>
 	<key>com.apple.mlruntime.host.ondemandplugin</key>

 		<string>Motion.Activity</string>
 		<string>Siri.Execution</string>
 		<string>HomeKitClientAccessoryControl</string>
+		<string>Siri.RecognizedUser</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Siri.Remembers.MessageHistory</string>
 		<string>Siri.Remembers.CallHistory</string>
 		<string>Siri.Remembers.InteractionHistory</string>
+		<string>Siri.Remembers.AudioHistory</string>
 		<string>Siri.Remembers.AssistantSuggestions</string>
 		<string>Siri.PostSiriEngagement</string>
+		<string>Siri.Audio.CompanionContext</string>
 	</array>
+	<key>com.apple.private.biome.sync</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

 		<string>personEntityRelevanceRanking</string>
 		<string>loiEntityRelevanceRanking</string>
 	</array>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.siri.userfeedbacklearning</string>
+	</array>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriInference</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriReferenceResolution</key>
 	<true/>
+	<key>com.apple.private.sqlite.sqlite-encryption</key>
+	<true/>
 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.routined.registration</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
+		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.analyticsd</string>
 		<string>com.apple.remindd</string>

 		<string>com.apple.backlightd</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.Maps.xpc.SharedTrip</string>
+		<string>com.apple.siriknowledged</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.mediaremote</string>
 		<string>com.apple.siri.homeAutomation</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.siri.inference.SiriSignals</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.siriinferenced</string>
+	<key>com.apple.siriknowledged</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>755</string>

 		<string>1340</string>
 		<string>1341</string>
 		<string>1342</string>
+		<string>1320</string>
+		<string>1710</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 		<string>IOAccelSharedUserClient2</string>
 		<string>IOAccelSubmitter2</string>
 		<string>IOSurfaceRootUserClient</string>
+		<string>IOGPUDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.homehubd.manage</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.audioanalyticsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.triald</string>
 		<string>com.apple.siri.audio</string>
 		<string>com.apple.SpeakSelection</string>
+		<string>com.apple.internal.testplatform</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### SiriTTSTrainingAgent

> `/System/Library/PrivateFrameworks/SiriTTSTraining.framework/SiriTTSTrainingAgent`

```diff

 		<string>IOAccelSharedUserClient2</string>
 		<string>IOAccelSubmitter2</string>
 		<string>IOSurfaceRootUserClient</string>
+		<string>IOGPUDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 SiriUserSegmentsPlugin

> `/System/Library/PrivateFrameworks/SiriUserSegments.framework/PlugIns/SiriUserSegmentsPlugin.appex/SiriUserSegmentsPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.SiriPrivateLearningAnalytics.SiriUserSegments.Plugin</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Siri.SELFProcessedEvent</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SiriUserSegmentation</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>CarPlay.Connected</string>
				<string>Device.Wireless.Bluetooth</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.siri.userfeedbacklearning</string>
	</array>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.siri.userfeedbacklearning</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
	</array>
</dict>
</plist>

```
### softwareupdateservicesd

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/Support/softwareupdateservicesd`

```diff

 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.contextstored.read_write_shm</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.iokit.batterydataprecise</key>

 	<true/>
 	<key>com.apple.private.managed-settings.effective-read</key>
 	<true/>
+	<key>com.apple.private.mobiletimerd</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>

 		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.CoreAuthentication.daemon</string>
 		<string>com.apple.CoreAuthentication.daemon.libxpc</string>
+		<string>com.apple.MobileTimer.timerserver</string>
+		<string>com.apple.MobileTimer.alarmserver</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```

### 🆕 SonicDiagnostics

> `/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>com.apple.SonicKit</string>
	</array>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.SonicKit</string>
	</array>
</dict>
</plist>

```
### com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

 	<true/>
 	<key>com.apple.corespeech.corespeechd.xpc</key>
 	<true/>
+	<key>com.apple.corespeech.supportheysiriwhenrecord</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.EmbeddedSpeech</string>

```
### syncdefaultsd

> `/System/Library/PrivateFrameworks/SyncedDefaults.framework/Support/syncdefaultsd`

```diff

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>syncdefaultsd</string>
 	<key>com.apple.private.security.daemon-container</key>

```
### TailspinSymbolicationServer

> `/System/Library/PrivateFrameworks/TailspinSymbolication.framework/XPCServices/TailspinSymbolicationServer.xpc/TailspinSymbolicationServer`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.security.storage.spindump</key>
+	<true/>
+</dict>
+</plist>
 

```
### UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.InFocus</string>
+		<string>App.MediaUsage</string>
+		<string>App.WebUsage</string>
+		<string>Device.Display.Backlight</string>
+		<string>Media.NowPlaying</string>
+		<string>Notification.Usage</string>
+	</array>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
 	<dict>
 		<key>com.apple.UsageTracking</key>

```
### useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

 	</array>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
+	<key>com.apple.private.managed-settings.effective-read</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceUbiquity</string>

 	</array>
 	<key>com.apple.runningboard.assertions.useractivityd</key>
 	<true/>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
+		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.sharing.handoff.advertising</string>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>Alarm</string>
+		<string>App.Intent</string>
 		<string>CarPlay</string>
 		<string>ContextSync.WalletTransaction</string>
 		<string>Device.Power.BatteryLevel</string>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.springboard</string>
 		<string>group.is.workflow.my.app</string>
 	</array>
 	<key>com.apple.security.files.bookmarks.app-scope</key>

```
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.mediaremote.device-info</key>
+	<true/>
+	<key>com.apple.mediaremote.remote-control-discovery</key>
+	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
 	<key>com.apple.mobilemail.mailservices</key>

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceMotion</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceReminders</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.mediaremote.device-info</key>
+	<true/>
+	<key>com.apple.mediaremote.remote-control-discovery</key>
+	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
 	<key>com.apple.mobilemail.mailservices</key>

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceMotion</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceReminders</string>

```
### CatalystContentExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/CatalystContentExtension.appex/CatalystContentExtension`

```diff

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceMotion</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceReminders</string>

```

### 🆕 SystemActionConfigurationExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/SystemActionConfigurationExtension.appex/SystemActionConfigurationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.WorkflowUI.SystemActionConfigurationExtension</string>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Production</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>iCloud.is.workflow.my.workflows</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudDocuments</string>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.ubiquity-container-identifiers</key>
	<array>
		<string>iCloud.is.workflow.my.workflows</string>
	</array>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.intents.extension.discovery</key>
	<true/>
	<key>com.apple.intents.uiextension.discovery</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled-access</key>
	<true/>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.controlcenter.service.moduleidentifiers</key>
	<array>
		<string>com.apple.control-center.QRCodeModule</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceCalendar</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.proactive.eventtracker</key>
	<true/>
	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.runningboard.assertions.siri</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.is.workflow.my.app</string>
		<string>group.is.workflow.shortcuts</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Applications/</string>
		<string>/private/var/containers/Bundle/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/UserConfigurationProfiles/</string>
		<string>/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts/</string>
		<string>/Media/iTunes_Control/iTunes/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.calaccessd</string>
		<string>com.apple.controlcenter.remoteservice</string>
		<string>com.apple.coreduetd.knowledge</string>
		<string>com.apple.itunescloudd.xpc</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
		<string>com.apple.medialibraryd.xpc</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.siri.VoiceShortcuts.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.medialibrary</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.shortcuts</string>
		<string>com.apple.siri.shortcuts</string>
		<string>group.is.workflow.my.app</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.configurationprofiles</string>
	</array>
	<key>com.apple.siri.VoiceShortcuts.xpc</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>V568VXD5P8.is.workflow.my.app</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### ZhuGeService

> `/System/Library/PrivateFrameworks/ZhuGeSupport.framework/XPCServices/ZhuGeService.xpc/ZhuGeService`

```diff

 	<true/>
 	<key>com.apple.private.domain-extension</key>
 	<true/>
-	<key>com.apple.private.factorysupportd.reverseproxy</key>
-	<true/>
 	<key>com.apple.private.security.bootpolicy</key>
 	<true/>
 	<key>com.apple.private.xpc.domain-extension</key>

 		<string>IOAppleConvergedIPCBBUserClient</string>
 		<string>IOPortTransportAIDBusUserClient</string>
 	</array>
+	<key>com.apple.stockholm.kext.entitlement</key>
+	<true/>
 </dict>
 </plist>
 

```
### itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

 	<true/>
 	<key>com.apple.private.nsurlsession.set-task-priority</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

 	<array>
 		<string>com.apple.Music</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.aps.itunescloudd</string>

```

### 🆕 GeoUIPlugin

> `/System/Library/Snippets/UIPlugins/GeoUIPlugin.bundle/GeoUIPlugin`

- No entitlements *(yet)*
### kbd

> `/System/Library/TextInput/kbd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>serverPreferred</string>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>cellular-plan</string>
+	</array>
 	<key>com.apple.MobileAsset.LinguisticData</key>
 	<true/>
 	<key>com.apple.MobileAsset.TextInput.SpellChecker</key>

 	<true/>
 	<key>com.apple.duet.expertcenter.consumer</key>
 	<true/>
+	<key>com.apple.feedbackd.client-forms</key>
+	<array>
+		<string>framework-autocorrect_S02_frCA</string>
+		<string>framework-autocorrect_S02_esES</string>
+		<string>:framework-autocorrect-korean</string>
+	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.handwritingd.allowBackgroundRecognition</key>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.security.storage.Safari</key>
+	<true/>
 	<key>com.apple.private.security.storage.kbd</key>
 	<true/>
 	<key>com.apple.private.stickers</key>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/MobileAsset/AssetsV2/</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.WebUI.plist</string>
 		<string>/private/var/.DocumentRevisions-V100/PerUID</string>
+		<string>/private/var/mobile/Library/Safari/AutoFillQuirks.plist</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.feedbackd.xpc</string>
+		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.stickers.api</string>
 		<string>com.apple.spotlight.SearchAgent</string>

 	<array>
 		<string>com.apple.SensorKit.keyboardMetrics</string>
 	</array>
+	<key>com.apple.spotlight.entitledattributes</key>
+	<true/>
 	<key>com.apple.springboard.launchapplications</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 	<true/>
 	<key>com.apple.itunescloud.in-app-message-service</key>
 	<true/>
+	<key>com.apple.itunescloudd.private</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

 	</array>
 	<key>com.apple.private.associated-domains</key>
 	<true/>
+	<key>com.apple.private.attentionawareness</key>
+	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.coreidvd.proofing</string>
+		<string>com.apple.AttentionAwareness</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.amsaccountsd.security</string>
 		<string>com.apple.askpermissiond</string>

 		<string>com.apple.rtcreportingd</string>
 		<string>com.apple.watchlistd.xpc</string>
 		<string>com.apple.watchlistd.bulletin-server</string>
-		<string>com.apple.storebookkeeperd.xpc</string>
 		<string>com.apple.mediaartworkd.xpc</string>
 		<string>com.apple.atc.xpc</string>
 		<string>com.apple.atc.xpc.downloadprogress</string>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 	<array>
 		<string>com.apple.radios.plist</string>
 	</array>
+	<key>com.apple.accessibility.IDSServices</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>

 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.seeding.client</key>

 		<string>/AppleInternal/Library/NanoTimeKit/ComplicationBundles/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/mobile/tmp/DiagnosticLogs/</string>
+		<string>/private/var/db/os_eligibility/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+		<string>com.apple.madrid</string>
+	</array>
+	<key>com.apple.private.ids.messaging.urgent-priority</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+		<string>com.apple.madrid</string>
+	</array>
+	<key>com.apple.private.ids.registration</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+		<string>com.apple.madrid</string>
+	</array>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.findmy.findmylocate.settings</string>
 		<string>com.apple.findmy.findmylocate.locationservice</string>

```
### FaceTime

> `/private/var/staged_system_apps/FaceTime.app/FaceTime`

```diff

 	</array>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.accountsd.accountmanager</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.FaceTime</string>
+	<key>com.apple.authkit.client.internal</key>
+	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.bulletinboard.utilities</key>

 	<true/>
 	<key>com.apple.private.ids.idquery-cache</key>
 	<true/>
+	<key>com.apple.private.ids.messaging</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+		<string>com.apple.madrid</string>
+	</array>
+	<key>com.apple.private.ids.messaging.urgent-priority</key>
+	<array>
+		<string>com.apple.private.alloy.nameandphoto</string>
+	</array>
 	<key>com.apple.private.ids.registration</key>
 	<array>
 		<string>com.apple.ess</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.containermanagerd</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
+	<key>com.apple.private.healthkit.analytics-agreements.control</key>
+	<true/>
 	<key>com.apple.private.healthkit.attachments</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>App.Intent</string>
 		<string>HomeKitClientAccessoryControl</string>
 		<string>HomeKitClientActionSet</string>
 		<string>HomeKitClientMediaAccessoryControl</string>

 	<dict>
 		<key>com.apple.homekit.events</key>
 		<string>com.apple.homekit</string>
-		<key>com.apple.homekit.events.playground</key>
-		<string>com.apple.homekit</string>
 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.coordination.alarms</key>
 	<true/>
-	<key>com.apple.private.coordination.messaging</key>
-	<true/>
-	<key>com.apple.private.coordination.role</key>
-	<true/>
 	<key>com.apple.private.coordination.timers</key>
 	<true/>
 	<key>com.apple.private.corerecents</key>

 	<true/>
 	<key>com.apple.private.mobileinstall.xpc-services-enabled</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.persona.read</key>
 	<true/>
 	<key>com.apple.private.rtcreportingd</key>

 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.seeding.client</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceMediaLibrary</string>

 		<string>/private/var/MobileAsset/Assets/com_apple_MobileAsset_LinguisticData/</string>
 		<string>/private/var/containers/Bundle/</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/</string>
+		<string>/private/var/db/os_eligibility/</string>
 		<string>/private/var/preferences/SystemConfiguration/</string>
 		<string>/private/var/tmp/siriBC</string>
 	</array>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.coordination.alarms</string>
-		<string>com.apple.coordination.messaging</string>
-		<string>com.apple.coordination.role</string>
 		<string>com.apple.coordination.timers</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.datamigrator</string>

 		<string>com.apple.springboard</string>
 		<string>com.apple.sync.NanoHome</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 		<string>com.apple.wifi.ui</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

 		<string>/private/var/MobileAsset/Assets/com_apple_MobileAsset_LinguisticData/</string>
 		<string>/private/var/containers/Bundle/</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/</string>
+		<string>/private/var/db/os_eligibility/</string>
 		<string>/private/var/preferences/SystemConfiguration/</string>
 		<string>/private/var/tmp/siriBC</string>
 	</array>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.coordination.alarms</string>
-		<string>com.apple.coordination.messaging</string>
-		<string>com.apple.coordination.role</string>
 		<string>com.apple.coordination.timers</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.datamigrator</string>

 		<string>com.apple.springboard</string>
 		<string>com.apple.sync.NanoHome</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 		<string>com.apple.wifi.ui</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

```
### HomeWidget

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget`

```diff

 	<string>com.apple.Home.HomeWidget.Interactive</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>App.Intent</string>
 		<string>HomeKitClientAccessoryControl</string>
 		<string>HomeKitClientActionSet</string>
 		<string>HomeKitClientMediaAccessoryControl</string>

 		<string>com.apple.springboard</string>
 		<string>com.apple.sync.NanoHome</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 		<string>com.apple.wifi.ui</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

 		<string>com.apple.springboard</string>
 		<string>com.apple.sync.NanoHome</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 		<string>com.apple.wifi.ui</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

```
### HomeWidgetLockScreen

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetLockScreen.appex/HomeWidgetLockScreen`

```diff

 	<string>com.apple.Home.HomeWidget</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>App.Intent</string>
 		<string>HomeKitClientAccessoryControl</string>
 		<string>HomeKitClientActionSet</string>
 		<string>HomeKitClientMediaAccessoryControl</string>

 		<string>com.apple.springboard</string>
 		<string>com.apple.sync.NanoHome</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 		<string>com.apple.wifi.ui</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

 		<string>com.apple.springboard</string>
 		<string>com.apple.sync.NanoHome</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 		<string>com.apple.wifi.ui</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

```
### HomeWidgetSingleAccessoryIntent

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeWidgetSingleAccessoryIntent.appex/HomeWidgetSingleAccessoryIntent`

```diff

 	<string>com.apple.Home.HomeWidget</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>App.Intent</string>
 		<string>HomeKitClientAccessoryControl</string>
 		<string>HomeKitClientActionSet</string>
 		<string>HomeKitClientMediaAccessoryControl</string>

 		<string>com.apple.springboard</string>
 		<string>com.apple.sync.NanoHome</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 		<string>com.apple.wifi.ui</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

 		<string>com.apple.springboard</string>
 		<string>com.apple.sync.NanoHome</string>
 		<string>com.apple.voicetrigger</string>
+		<string>com.apple.voicetrigger.notbackedup</string>
 		<string>com.apple.wifi.ui</string>
 		<string>group.is.workflow.my.app</string>
 	</array>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.locationd.private_info</key>
 	<true/>
-	<key>com.apple.locationd.prompt_behavior</key>
-	<true/>
 	<key>com.apple.locationd.route_hint</key>
 	<true/>
 	<key>com.apple.locationd.simulation</key>

```
### GeneralMapsWidget

> `/private/var/staged_system_apps/Maps.app/PlugIns/GeneralMapsWidget.appex/GeneralMapsWidget`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
-	<key>com.apple.locationd.prompt_behavior</key>
-	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.systemNotesPresentation</key>
 	<true/>
 	<key>com.apple.springboard.systemNotesScreenshot</key>

```
### MobileTimer

> `/private/var/staged_system_apps/MobileTimer.app/MobileTimer`

```diff

 		<string>com.apple.MobileTimer.sleepmodeserver</string>
 		<string>com.apple.MobileTimer.timerserver</string>
 		<string>com.apple.MobileTimer.alarmserver</string>
+		<string>com.apple.MobileTimer.stopwatchserver</string>
 		<string>com.apple.tipsd</string>
 		<string>com.apple.MobileTimer.sessionserver</string>
 	</array>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>com.apple.SonicKit</string>
+	</array>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>

 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.Music</string>
+		<string>com.apple.SonicKit</string>
 	</array>
 	<key>com.apple.security.assets.music.read-write</key>
 	<true/>

```
### NewsTag

> `/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag`

```diff

 	<true/>
 	<key>com.apple.chrono.invalidatesOnStorefrontChange</key>
 	<true/>
+	<key>com.apple.chrono.open-urls-direct</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

```
### Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.apple-pay-trust.all-access</key>
 	<true/>
 	<key>com.apple.asd.allow</key>

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
-	<key>com.apple.private.LocalAuthentication.DTO</key>
-	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.RGBCapture</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.financed.service.bankconnect</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.seserviced.session</string>
 		<string>com.apple.SharingServices</string>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.mediaremote.device-info</key>
+	<true/>
+	<key>com.apple.mediaremote.remote-control-discovery</key>
+	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
 	<key>com.apple.mediaremote.set-playback-state</key>

 	<true/>
 	<key>com.apple.mobile.keybagd.UserManager.logout</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.payment.all-access</key>

 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.podcasts</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>MediaLibrary</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Podcasts.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.iosmac.unscaled</key>
 	<true/>
 	<key>com.apple.private.mobileinstall.upgrade-enabled</key>

 		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.xpc.amsengagementd</string>
+		<string>com.apple.passd.library</string>
+		<string>com.apple.passd.payment</string>
+		<string>com.apple.CarPlayApp.service</string>
+		<string>com.apple.SetStoreUpdateService</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.coreidvd.proofing</string>
 		<string>com.apple.xpc.amsengagementd</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
+		<string>com.apple.SetStoreUpdateService</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.temporary-exception.sbpl</key>
 	<array>

```
### RemindersIntentsExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsExtension.appex/RemindersIntentsExtension`

```diff

 		<true/>
 	</dict>
 	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceCalendar</string>
-	</array>
+	<array/>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### RemindersIntentsUIExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersIntentsUIExtension.appex/RemindersIntentsUIExtension`

```diff

 		<true/>
 	</dict>
 	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceCalendar</string>
-	</array>
+	<array/>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### RemindersSharingExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSharingExtension.appex/RemindersSharingExtension`

```diff

 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceCalendar</string>
-	</array>
+	<array/>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### RemindersWidgetExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension`

```diff

 	<key>com.apple.private.suggestions.contacts</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceCalendar</string>
-	</array>
+	<array/>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### Reminders

> `/private/var/staged_system_apps/Reminders.app/Reminders`

```diff

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
-		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceCamera</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceMotion</string>
 		<string>kTCCServicePhotos</string>
 		<string>kTCCServicePhotosAdd</string>
 		<string>kTCCServiceReminders</string>

```
### fsck_apfs

> `/sbin/fsck_apfs`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.apfs.sep.ramdisk</key>
+	<true/>
 	<key>com.apple.container.crypto.io</key>
 	<true/>
 	<key>com.apple.keystore.device</key>

```
### launchd

> `/sbin/launchd`

```diff

 	<true/>
 	<key>com.apple.private.security.disk-device-access</key>
 	<true/>
+	<key>com.apple.private.security.signal-critical-processes</key>
+	<true/>
+	<key>com.apple.private.security.signal-exempt</key>
+	<true/>
 	<key>com.apple.private.security.storage.driverkitd</key>
 	<true/>
 	<key>com.apple.private.security.storage.launchd</key>

```
### brctl

> `/usr/bin/brctl`

```diff

 	<key>com.apple.private.clouddocs.spi</key>
 	<array>
 		<string>setupInstanceWithDict:reply:</string>
-		<string>dumpDatabaseTo:containerID:personaID:includeAllItems:reply:</string>
+		<string>dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:</string>
 		<string>dumpFPFSMigrationStatusTo:personaID:includeNonMigratedItems:reply:</string>
 		<string>performSelfCheck:reply:</string>
 		<string>printStatus:containerID:reply:</string>

 		<string>healthStatusStringForContainer:reply:</string>
 		<string>zoneNameForContainer:reply:</string>
 		<string>dumpCoordinationInfoTo:reply:</string>
-		<string>backupDatabaseWithURLWrapper:forCiconia:reply:</string>
+		<string>backupDatabaseWithURLWrapper:reply:</string>
 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>

```
### fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
-	<key>com.apple.private.security.storage.ciconia</key>
-	<true/>
 	<key>com.apple.private.vfs.authorized-access</key>
 	<true/>
 	<key>com.apple.private.vfs.dataless-manipulation</key>

```
### footprint

> `/usr/bin/footprint`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.iosurfaceinfo</key>
+	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
 	<key>com.apple.system-task-ports.read</key>

```
### nfsstat

> `/usr/bin/nfsstat`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.system-nfssvc</key>
+	<true/>
+</dict>
+</plist>
 

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 		<string>AppleHDQGasGaugeControlUserClient</string>
 		<string>AppleNVMeUpdateUC</string>
 		<string>ApplePPMUserClient</string>
-		<string>IOAccelMemoryInfoUserClient</string>
 		<string>IOGPUMemoryInfoUserClient</string>
 		<string>IOMobileFramebufferUserClient</string>
 		<string>IOReportUserClient</string>

```
### ASPCarryLog

> `/usr/libexec/ASPCarryLog`

```diff

 		<string>AppleNVMeEANUC</string>
 		<string>ASPUserClient</string>
 		<string>AppleNVMePassThroughUC</string>
+		<string>IOUSBMassStorageResourceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 		<string>kTCCServiceFaceID</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceWebBrowserPublicKeyCredential</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.AuthenticationServices.CredentialSharingGroupsNotifications</string>

```
### DumpPanic

> `/usr/libexec/DumpPanic`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.DumpPanic</key>
 	<true/>
+	<key>com.apple.private.security.storage.spindump</key>
+	<true/>
 	<key>com.apple.rootless.volume.VM</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### IOMFB_bics_daemon

> `/usr/libexec/IOMFB_bics_daemon`

```diff

 <dict>
 	<key>com.apple.AppleNVMeEAN.allow</key>
 	<true/>
+	<key>com.apple.afk.user</key>
+	<true/>
 	<key>com.apple.private.applesepmanager.allow</key>
 	<true/>
 	<key>com.apple.private.iomfb.set-block</key>

 	<key>com.apple.private.xpc.launchd.ios-system-session</key>
 	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
-	<string>RootDomainUserClient</string>
+	<array>
+		<string>RootDomainUserClient</string>
+		<string>AFKEndpointInterfaceUserClient</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>IOMobileFramebufferUserClient</string>
 	<key>platform-application</key>

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 		<string>AppleHDQGasGaugeControlUserClient</string>
 		<string>AppleNVMeUpdateUC</string>
 		<string>ApplePPMUserClient</string>
-		<string>IOAccelMemoryInfoUserClient</string>
 		<string>IOGPUMemoryInfoUserClient</string>
 		<string>AppleMCCUserClient</string>
 		<string>AppleSMCClient</string>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 		<string>AppleHDQGasGaugeControlUserClient</string>
 		<string>AppleNVMeUpdateUC</string>
 		<string>ApplePPMUserClient</string>
-		<string>IOAccelMemoryInfoUserClient</string>
 		<string>IOGPUMemoryInfoUserClient</string>
 		<string>IOMobileFramebufferUserClient</string>
 		<string>IOReportUserClient</string>

```
### SensorKitALSHelper

> `/usr/libexec/SensorKitALSHelper`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.geod</string>
 		<string>com.apple.SensorKit.CHSupportService</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 	</array>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.vfs.allow-low-space-writes</key>

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 	<string>com.apple.iad-cloudkit</string>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-services</key>

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.InFocus</string>
+		<string>App.Install</string>
+	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>
 	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>

```
### announced

> `/usr/libexec/announced`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

```
### anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

 			<key>read</key>
 			<dict/>
 		</dict>
-		<key>DotFp</key>
+		<key>GpsFp</key>
 		<dict>
 			<key>read</key>
 			<dict/>
 		</dict>
-		<key>GpsFp</key>
+		<key>HertzFp</key>
 		<dict>
 			<key>read</key>
 			<dict/>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.inheritance.cryptoaccess</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```

### 🆕 appleh16camerad

> `/usr/libexec/appleh16camerad`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.driver.VADResource.user-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.photondetector.iokit-user-access</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.cmio.extension.configuration</key>
	<true/>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceCamera</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>AGXDeviceUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AppleH16CamInUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>H1xANELoadBalancerDirectPathClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelContext2</string>
		<string>IOAccelDevice</string>
		<string>IOAccelDevice2</string>
		<string>IOAccelSharedUserClient</string>
		<string>IOAccelSharedUserClient2</string>
		<string>IOAccelSubmitter2</string>
		<string>IOSurfaceRootUserClient</string>
		<string>VADResourceArbiterUserClient</string>
		<string>AppleH16PhotonDetectorUserClient</string>
		<string>IOUserClient</string>
	</array>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.systemstatus.publisher.domains</key>
	<array>
		<string>media</string>
	</array>
</dict>
</plist>

```
### asd

> `/usr/libexec/asd`

```diff

 		<key>asd-profile</key>
 		<dict>
 			<key>Databases</key>
-			<string>ApplePay.Security.Features</string>
+			<array>
+				<string>ApplePay.Security.Features</string>
+			</array>
 		</dict>
 	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### assessmentagent

> `/usr/libexec/assessmentagent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.assessmentagent</string>
+	<key>com.apple.Pasteboard.background-access</key>
+	<true/>
+	<key>com.apple.avfoundation.allow-system-wide-context</key>
+	<true/>
+	<key>com.apple.avfoundation.allows-access-to-device-list</key>
+	<true/>
+	<key>com.apple.avfoundation.allows-set-output-device</key>
+	<true/>
+	<key>com.apple.managedconfiguration.profiled-access</key>
+	<true/>
+	<key>com.apple.mediaremote.restrict-command-clients</key>
+	<true/>
+	<key>com.apple.private.neagent</key>
+	<true/>
+	<key>com.apple.private.necp.policies</key>
+	<true/>
+	<key>com.apple.private.nehelper.privileged</key>
+	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.runningboard.process-state</key>

 	<array>
 		<string>/Library/com.apple.assessmentagent/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.pasteboard.pasted</string>
+		<string>com.apple.coremedia.routingcontext.xpc</string>
+		<string>com.apple.coremedia.volumecontroller.xpc</string>
+		<string>com.apple.nehelper</string>
+		<string>com.apple.managedconfiguration.profiled</string>
+		<string>com.apple.mediaremoted.xpc</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mediaremote</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.assessmentmode</string>
+	</array>
 </dict>
 </plist>
 

```
### audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
-		<string>/var/root/Documents/AdaptiveVolumeLogs</string>
 		<string>/Library/Logs/DiagnosticReports/Audio</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 			<dict/>
 		</dict>
 	</dict>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>gesture</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.appleneuralengine.private.allow</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>

 	<true/>
 	<key>com.apple.managedassets.api.usermode</key>
 	<true/>
+	<key>com.apple.mediaremote.device-info</key>
+	<true/>
 	<key>com.apple.mediaremote.send-commands</key>
 	<true/>
 	<key>com.apple.multitasking.unlimitedassertions</key>

 	<array>
 		<string>com.apple.developer.driverkit.family.audio</string>
 	</array>
+	<key>com.apple.private.exclaves.conclave-host</key>
+	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 	</array>
 	<key>com.apple.private.master-sync-generator.user-access</key>
 	<true/>
+	<key>com.apple.private.mediaexperience.usesecuresession</key>
+	<true/>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
 	<true/>
 	<key>com.apple.private.network.interface-control</key>

 	<true/>
 	<key>com.apple.rapport.Client</key>
 	<true/>
+	<key>com.apple.realitysimulation.rendered-content-service</key>
+	<true/>
 	<key>com.apple.relatived.tempest</key>
 	<true/>
+	<key>com.apple.runningboard.endowment-originator</key>
+	<true/>
+	<key>com.apple.runningboard.listallassertions</key>
+	<true/>
 	<key>com.apple.runningboard.mediaexperience</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>SCodecUserClient</string>
 		<string>IOPAudioLPMicDeviceUserClient</string>
 		<string>IOPAudioIOBufferDeviceUserClient</string>
+		<string>IOPAudioIsolatedIOBufferDeviceUserClient</string>
 		<string>IOPAudioVoiceTriggerDeviceUserClient</string>
 		<string>IOPAudioClientManagerDeviceUserClient</string>
 		<string>AppleHapticsSupportUserClient</string>

 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
 		<string>kern.stackshot_stats</string>
+		<string>kern.exclaves_status</string>
+		<string>kern.task_conclave</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-write</key>
 	<array>

 		<string>311</string>
 		<string>312</string>
 	</array>
+	<key>com.apple.userexperiencemanager.source-for-recording-user-requested</key>
+	<true/>
 	<key>com.apple.videoconference.allow-conferencing</key>
 	<true/>
 	<key>com.apple.voiced.can-dump-audio</key>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.accessibility.BackBoard</key>
+	<true/>
+	<key>com.apple.accessibility.IDSServices</key>
+	<true/>
+	<key>com.apple.accessibility.SpeakThisServices</key>
+	<true/>
 	<key>com.apple.afk.user</key>
 	<true/>
 	<key>com.apple.aop.fastpath.user-client</key>

 		<string>WirelessBoardSnum</string>
 		<string>BatterySerialNumber</string>
 		<string>RoswellChipID</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.cecd.observer</key>
 	<true/>
+	<key>com.apple.private.exclaves.conclave-host</key>
+	<true/>
 	<key>com.apple.private.gain-map-access</key>
 	<true/>
 	<key>com.apple.private.graphics-restart-no-kill</key>

 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
+		<string>kern.exclaves_status</string>
+		<string>kern.task_conclave</string>
 		<string>machdep.wake_abstime</string>
 		<string>machdep.wake_conttime</string>
 	</array>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.intelligenceplatform.Coordination</key>
+	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

 		<string>com.apple.cloudd</string>
 		<string>com.apple.apsd</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.intelligenceplatform.Coordination</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### bluetoothuserd

> `/usr/libexec/bluetoothuserd`

```diff

 	<true/>
 	<key>com.apple.private.ids.registration</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 		<string>apple</string>
 		<string>InternetAccounts</string>
 	</array>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

```

### 🆕 caraccessoryd

> `/usr/libexec/caraccessoryd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.carp</key>
	<true/>
	<key>com.apple.private.CarPlayUIServices.cluster-theme</key>
	<true/>
	<key>com.apple.private.carp</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CarPlayApp.cluster-theme-service</string>
		<string>com.apple.caraccessoryframework.cardata</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.CarAccessoryFramework</string>
	</array>
</dict>
</plist>

```
### carkitd

> `/usr/libexec/carkitd`

```diff

 	<true/>
 	<key>com.apple.UIKit.status-bar-override-allow</key>
 	<true/>
+	<key>com.apple.airplay.endpoint.xpc</key>
+	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.coremedia.endpoint.xpc</key>
+	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.mediaexperience.endpoint.xpc</key>
+	<true/>
+	<key>com.apple.private.accessories.showallconnections</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.CarDDPAssets</string>

```
### ciphermld

> `/usr/libexec/ciphermld`

```diff

 	<string>com.apple.ciphermld</string>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.ciphermld</string>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.kvsd</string>
 		<string>com.apple.CipherMLService</string>
 		<string>com.apple.fairplayd.versioned</string>
 	</array>
+	<key>com.apple.security.exception.process-info</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.itunesstored</string>
+		<string>com.apple.jett.switch-itms</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### companiond

> `/usr/libexec/companiond`

```diff

 	<array>
 		<string>com.apple.private.alloy.companion.auth</string>
 	</array>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceFaceID</string>

 		<string>com.apple.watchnotificationsui.alertservice</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.tvremotecore.xpc</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.passd.in-app-payment</string>
 		<string>com.apple.passd.library</string>
 		<string>com.apple.xpc.amsaccountsd</string>
-		<string>com.apple.identityservicesd.embedded.auth</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	</array>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>temporary-sandbox</string>
-	</array>
 </dict>
 </plist>
 

```
### corecaptured

> `/usr/libexec/corecaptured`

```diff

 	<array>
 		<string>InverseDeviceID</string>
 	</array>
+	<key>com.apple.private.driverkit.driver-access</key>
+	<array>
+		<string>com.apple.private.wifi.driverkit</string>
+		<string>com.apple.private.corecaptureclient.driverkit</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOReportUserClient</string>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 		<string>IOAccelContext2</string>
 		<string>IOAccelDevice2</string>
 		<string>IOAccelSharedUserClient2</string>
+		<string>IOGPUDeviceUserClient</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### coreidvd

> `/usr/libexec/coreidvd`

```diff

 	<true/>
 	<key>com.apple.accounts.idms.fullaccess</key>
 	<true/>
+	<key>com.apple.app-distribution.private</key>
+	<true/>
 	<key>com.apple.asd.client</key>
 	<string>2665061694</string>
 	<key>com.apple.authkit.client.internal</key>

 		<string>com.apple.NPKCompanionAgent.library</string>
 		<string>com.apple.nfcd.hwmanager</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### countryd

> `/usr/libexec/countryd`

```diff

 <dict>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.setInput</key>
+	<true/>
 	<key>com.apple.rapport.StatusUpdates</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.eligibilityd</string>
 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.rapport.StatusUpdates</string>
 	</array>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.commcenter.carrierspace.xpc</string>

 		<string>com.apple.coremedia.cameraviewfinder</string>
 		<string>com.apple.coreservices.launchservicesd</string>
 		<string>com.apple.coreservices.quarantine-resolver</string>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.ExposureNotification</string>
 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.gizmoappd.appmanager</string>

 		<string>com.apple.nanobuddy</string>
 		<string>com.apple.purplebuddy</string>
 		<string>com.apple.cloudphotod</string>
+		<string>com.apple.mobileslideshow</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### demod

> `/usr/libexec/demod`

```diff

 		<string>EthernetMacAddress</string>
 		<string>IntegratedCircuitCardIdentifier</string>
 		<string>InternationalMobileEquipmentIdentity</string>
+		<string>InternationalMobileEquipmentIdentity2</string>
 		<string>MLBSerialNumber</string>
 		<string>MobileEquipmentIdentifier</string>
 		<string>PintoMacAddress</string>

 	<true/>
 	<key>com.apple.private.photos.service.demo</key>
 	<true/>
-	<key>com.apple.private.security.storage-exempt.heritable</key>
+	<key>com.apple.private.security.datavault.controller</key>
 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>

```
### demod_helper

> `/usr/libexec/demod_helper`

```diff

 	<true/>
 	<key>com.apple.private.iokit.ddl-write</key>
 	<true/>
-	<key>com.apple.private.security.disk-device-access</key>
+	<key>com.apple.private.security.datavault.controller</key>
 	<true/>
-	<key>com.apple.private.security.storage-exempt.heritable</key>
+	<key>com.apple.private.security.disk-device-access</key>
 	<true/>
 	<key>com.apple.private.security.storage.CallHistory</key>
 	<true/>

```

### 🆕 dietapplecamerad

> `/usr/libexec/dietapplecamerad`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.driver.VADResource.user-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.private.tcc.manager</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>AGXDeviceUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AppleH10CamInUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelContext2</string>
		<string>IOAccelDevice</string>
		<string>IOAccelDevice2</string>
		<string>IOAccelSharedUserClient</string>
		<string>IOAccelSharedUserClient2</string>
		<string>IOAccelSubmitter2</string>
		<string>IOSurfaceRootUserClient</string>
		<string>VADResourceArbiterUserClient</string>
	</array>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
</dict>
</plist>

```

### 🆕 dietappleh16camerad

> `/usr/libexec/dietappleh16camerad`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.driver.VADResource.user-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.pearl.iokit-user-access</key>
	<true/>
	<key>com.apple.photondetector.iokit-user-access</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AGXCommandQueue</string>
		<string>AGXDevice</string>
		<string>AGXDeviceUserClient</string>
		<string>AGXSharedUserClient</string>
		<string>AppleH16CamInUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>H1xANELoadBalancerDirectPathClient</string>
		<string>IOAccelContext</string>
		<string>IOAccelContext2</string>
		<string>IOAccelDevice</string>
		<string>IOAccelDevice2</string>
		<string>IOAccelSharedUserClient</string>
		<string>IOAccelSharedUserClient2</string>
		<string>IOAccelSubmitter2</string>
		<string>IOSurfaceRootUserClient</string>
		<string>VADResourceArbiterUserClient</string>
		<string>AppleH16PhotonDetectorUserClient</string>
		<string>IOUserClient</string>
	</array>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>com.apple.systemstatus.publisher.domains</key>
	<array>
		<string>media</string>
	</array>
</dict>
</plist>

```
### dockaccessoryd

> `/usr/libexec/dockaccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.allow-background-haptics</key>
 	<true/>
+	<key>com.apple.private.hid.client.event-dispatch</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothAlways</string>

```

### 🆕 eligibilityd

> `/usr/libexec/eligibilityd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.allowed</key>
	<false/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.os_eligibility_parameters</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readwrite</key>
	<true/>
	<key>com.apple.security.system-container</key>
	<true/>
</dict>
</plist>

```
### fairplaydeviceidentityd

> `/usr/libexec/fairplaydeviceidentityd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>AvpFairPlayUserClient.access</key>
+	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.fairplaydeviceidentityd</string>
 	<key>com.apple.keystore.fairplay</key>

 	<true/>
 	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>TF31PAB6aO8KAbPyNKSxKA</string>
+	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>AvpFairPlayUserClient</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.mobileactivationd</string>

 	<array>
 		<string>com_apple_driver_FairPlayIOKitUserClient</string>
 		<string>com_apple_driver_TestIOKitUserClient</string>
+		<string>AvpFairPlayUserClient</string>
 	</array>
+	<key>com.apple.system.diagnostics.iokit-properties</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 	<key>user-preference-write</key>

```
### fseventsd

> `/usr/libexec/fseventsd`

```diff

 <dict>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
-	<key>com.apple.private.vfs.fsevents-watcher</key>
+	<key>com.apple.private.vfs.fsevents-activity-watcher</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### gamecontrollerd

> `/usr/libexec/gamecontrollerd`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.game-center</key>
+	<true/>
 	<key>com.apple.hid.manager.user-access</key>
 	<true/>
 	<key>com.apple.hid.manager.user-access-interface-rematch</key>

 	</array>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.game-center</key>
+	<array>
+		<string>Account</string>
+	</array>
 	<key>com.apple.private.gamecontroller.config.client</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>

```
### gputoolsserviced

> `/usr/libexec/gputoolsserviced`

```diff

 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/GPUTools/</string>

```

### 🆕 init_exclavekit

> `/usr/libexec/init_exclavekit`

- No entitlements *(yet)*
### installd

> `/usr/libexec/installd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.AppBundles</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.uninstall.deletion</key>
 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>

```
### keybagd

> `/usr/libexec/keybagd`

```diff

 	<true/>
 	<key>com.apple.private.security.container-manager</key>
 	<true/>
+	<key>com.apple.private.security.datavault.controller</key>
+	<true/>
 	<key>com.apple.private.security.disk-device-access</key>
 	<true/>
 	<key>com.apple.private.security.install</key>
 	<true/>
-	<key>com.apple.private.security.storage-exempt.heritable</key>
-	<true/>
 	<key>com.apple.private.syncbubble-keychain</key>
 	<true/>
 	<key>com.apple.private.usermanagerhelper</key>

```
### linkd

> `/usr/libexec/linkd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.linkd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>AppIntentsTranscript</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>App.Intents.SafetyCriticalTranscript</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.Intents.Transcript</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+		<key>AppShortcuts</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.Shortcut.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.Shortcut.Phrase</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.daemon-container</key>

 		<string>com.apple.chronoservices</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.linkd.extension</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
+		<string>com.apple.SetStoreUpdateService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.linkd</string>
 		<string>com.apple.assistant.backedup</string>
 	</array>
 	<key>com.apple.security.system-container</key>

```
### locationd

> `/usr/libexec/locationd`

```diff

 		<key>com.apple.vo2max</key>
 		<string>com.apple.vo2max</string>
 	</dict>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
 	<key>com.apple.private.cloudkit.spi</key>
 	<true/>
 	<key>com.apple.private.corelocation.map-helper-service</key>

 	<array>
 		<string>com.apple.SafetyKit</string>
 		<string>com.apple.momentsd</string>
+		<string>com.apple.nanolifestyle.privacy</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### lockdownd

> `/usr/libexec/lockdownd`

```diff

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.CoreRepairCore.repairInfo</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>IceFallID</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CoreRepairCoreXPCService</string>
 		<string>com.apple.remoted</string>
 		<string>com.apple.pcapd</string>
 		<string>com.apple.nearbyd.xpc.diagnostics</string>

```
### lsd

> `/usr/libexec/lsd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage-exempt.heritable</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceUserTracking</string>

```
### lskdd

> `/usr/libexec/lskdd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>AvpFairPlayUserClient.access</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.AppleKeyServicesCRL2</string>

 	<array>
 		<string>com_apple_driver_KeyDeliveryIOKitUserClient</string>
 		<string>com_apple_driver_FairPlayIOKitUserClient</string>
+		<string>AvpFairPlayUserClient</string>
 	</array>
+    <key>com.apple.security.exception.iokit-user-client-class</key>
+    <array>
+        <string>AvpFairPlayUserClient</string>
+        <string>com_apple_driver_FairPlayIOKitUserClient</string>
+        <string>com_apple_driver_TestIOKitUserClient</string>
+    </array>
 	<key>com.apple.rootless.storage.fpsd</key>
 	<true/>
 	<key>com.apple.private.security.storage.fpsd</key>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<true/>
 	<key>com.apple.keystore.escrow.create</key>
 	<true/>
+	<key>com.apple.locationd.authorizeapplications</key>
+	<true/>
+	<key>com.apple.locationd.effective_bundle</key>
+	<true/>
+	<key>com.apple.locationd.emergency_enabler</key>
+	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.managedconfiguration.mdmd-access</key>

 	</array>
 	<key>com.apple.private.remotemanagement.enrollment</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
 	<key>com.apple.private.security.storage.ManagedConfiguration</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

 	<true/>
 	<key>com.apple.usermanagerd.persona.background</key>
 	<true/>
+	<key>com.apple.usermanagerd.persona.fetch</key>
+	<true/>
 	<key>com.apple.wipedevice</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### mlhostd

> `/usr/libexec/mlhostd`

```diff

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.mlhostd</string>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.mlhost.worker-host-entitlement</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.MLHostTask</string>
+	</array>
 	<key>com.apple.private.biome.pruner</key>
 	<array>
 		<string>Lighthouse.Ledger.TaskCustomEvent</string>

 		<string>/System/Library/MLHost/</string>
 		<string>/AppleInternal/Library/MLHost/</string>
 		<string>/AppleInternal/System/Library/MLHost/</string>
+		<string>/private/var/MobileAsset/AssetV2/com_apple_MobileAsset_MLHostTask/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.apsd</string>
+		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### mobile_diagnostics_relay

> `/usr/libexec/mobile_diagnostics_relay`

```diff

 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>
 	<true/>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>RootDomainUserClient</string>
+	</array>
 </dict>
 </plist>
 

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	</array>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.networkd.allow_bootstrap_cellular_service_request</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>

 	<true/>
 	<key>com.apple.private.mobileassetd.use-download-dir</key>
 	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.networkextension.configuration</key>
 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>

 	<true/>
 	<key>com.apple.private.security.bootpolicy.readonly</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.updatetransparency.client</key>
 	<true/>
 	<key>com.apple.private.vfs.graftdmg</key>

 	<true/>
 	<key>com.apple.rootless.volume.Update</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<string>/private/var/code_coverage/</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.installcoordinationd</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>
+		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>

 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.mobileassetd</string>
+		<string>lockdown-identities</string>
+		<string>apple</string>
+	</array>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>mobileassetd</string>

```
### momentsd

> `/usr/libexec/momentsd`

```diff

 	<array>
 		<string>MODataExportService</string>
 		<string>MOFetchEventBundles</string>
+		<string>MOPromptManagerTest</string>
+		<string>MOOnboardingAndSettings</string>
 	</array>
 	<key>com.apple.photoanalysisd</key>
 	<true/>

 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Topic.readOnly</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.Journal</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.momentsd/</string>

 		<string>com.apple.momentsd</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.private.intelligenceplatform.views.read-only</string>
+		<string>com.apple.usernotifications.listener</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### nanomediaremotelinkagent

> `/usr/libexec/nanomediaremotelinkagent`

```diff

 		<string>com.apple.private.alloy.audiocontrol.music</string>
 		<string>com.apple.private.alloy.mediaremote</string>
 	</array>
+	<key>com.apple.private.mediaexperience.setsilentmode.allow</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceMediaLibrary</string>

```
### nearbyd

> `/usr/libexec/nearbyd`

```diff

 	</array>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.aop.hid-driver.hid-service.pdr</key>
+	<true/>
 	<key>com.apple.aop.rose.controller.admin</key>
 	<true/>
 	<key>com.apple.aop.user-client</key>

 	<true/>
 	<key>com.apple.locationd.spectator</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
 	<key>com.apple.nfcd.session.se</key>

```
### nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.runningboard.dontterminate</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>

```
### networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmapbundleidtouuid</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.neagent</key>

```
### nexusd

> `/usr/libexec/nexusd`

```diff

 	<string>com.apple.nexusd</string>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.PairingManager.HomeKit</key>
+	<true/>
+	<key>com.apple.PairingManager.Read</key>
+	<true/>
+	<key>com.apple.PairingManager.Write</key>
+	<true/>
 	<key>com.apple.SiriVOXService.client</key>
 	<true/>
 	<key>com.apple.SystemConfiguration.SCDynamicStore-write-access</key>
 	<true/>
+	<key>com.apple.appletv.pbs.mediaremote</key>
+	<true/>
+	<key>com.apple.appletv.pbs.user-presentation-service-access</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.developer.driverkit.userclient-access</key>

 	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
+	<key>com.apple.private.homekit.pairing-identity</key>
+	<true/>
+	<key>com.apple.private.homekit.pairing-identity.private</key>
+	<true/>
+	<key>com.apple.private.ids.session</key>
+	<array/>
+	<key>com.apple.private.ids.session-private</key>
+	<true/>
+	<key>com.apple.private.network.socket-delegate</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.HomeKit</key>
+	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceWillow</string>

 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.coordination.capability</string>
 		<string>com.apple.homed.xpc</string>
+		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.locationd.registration</string>
+		<string>com.apple.PairingManager</string>
+		<string>com.apple.PineBoardServices</string>
 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.SiriVOXService.client</string>
 		<string>com.apple.soundboardservices.server</string>

 	<true/>
 	<key>com.apple.wifip2pd</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+		<string>com.apple.hap.pairing</string>
+		<string>com.apple.pairing</string>
+		<string>com.apple.rapport</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### nfcd

> `/usr/libexec/nfcd`

```diff

 	<array>
 		<string>UniqueChipID</string>
 		<string>SerialNumber</string>
+		<string>UniqueDeviceID</string>
 	</array>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>nfcd</string>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.smcsensor.user-access</key>
 	<true/>
 	<key>com.apple.private.stockholm.allow</key>
 	<true/>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceContactlessAccess</string>
+	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/hardware/FactoryData/System/Library/Caches/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.accessoryd.nf-events</string>
+		<string>com.apple.stockholm.services.NFRestoreService</string>
+		<string>com.apple.stockholm.services.NFRadioPowerSwitch</string>
+		<string>com.apple.stockholm.services.NFUIService</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.seserviced.contactlessCredential.settings</string>
+		<string>com.apple.passd.class-d</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.stockholm.analytics</string>
 		<string>com.apple.ControlCenter</string>
 		<string>com.apple.homed</string>
+		<string>com.apple.stockholm.wallet.presentation</string>
 	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>

```
### online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.online-auth-agent</string>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>

 	<true/>
 	<key>com.apple.private.amfi.garbage-collect-profiles</key>
 	<true/>
+	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MobileIdentityService.DenyList</string>
 	</array>
+	<key>com.apple.private.cloudkit.setEnvironment</key>
+	<true/>
+	<key>com.apple.private.cloudkit.systemService</key>
+	<true/>
 	<key>com.apple.private.mis.online_auth_agent</key>
 	<true/>
 	<key>com.apple.private.mis.profiles.write</key>
 	<true/>
 	<key>com.apple.private.mis.trust.set</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>SetLaunchWarning</string>
+	</array>
 	<key>com.apple.private.pvappidentity.spi</key>
 	<true/>
 	<key>com.apple.private.security.storage.MobileIdentityService</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceLiverpool</string>
+	</array>
+	<key>com.apple.runningboard.terminateprocess</key>
+	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobile.installd</string>
 		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.cloudd</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### profiled

> `/usr/libexec/profiled`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceFaceID</string>
 	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>
 	<array>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.appstored</key>
+	<array>
+		<string>AppCapabilities</string>
+	</array>
 	<key>com.apple.private.calendar.has-adopted-modern-request-access-methods</key>
 	<true/>
 	<key>com.apple.private.fairplay.FPDI</key>

 		<string>com.apple.ap.adprivacyd.idmanager</string>
 		<string>com.apple.adid</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.appstored.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
-	<key>com.apple.coreduetd.allow</key>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>

 	<true/>
 	<key>com.apple.rapport.Client</key>
 	<true/>
-	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
-	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>com.apple.coordination.alarms</string>
 		<string>com.apple.coordination.timers</string>
 		<string>com.apple.coreaudio.device</string>
-		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.coremedia.admin</string>
 		<string>com.apple.coremedia.asset.xpc</string>
 		<string>com.apple.coremedia.customurlloader.xpc</string>

 		<string>com.apple.soundboardservices.server</string>
 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.springboard.services</string>
+		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.SystemConfiguration.configd</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callstatecontroller</string>

 		<string>com.apple.coreanimation</string>
 		<string>com.apple.coreaudio</string>
 		<string>com.apple.coreaudio.device</string>
-		<string>com.apple.CoreDuet</string>
 		<string>com.apple.coremedia</string>
 		<string>com.apple.duetexpertd</string>
 		<string>com.apple.frontboardservices.device_emulation</string>

```
### rapportd

> `/usr/libexec/rapportd`

```diff

 	<true/>
 	<key>com.apple.icloud.fmfd.access</key>
 	<true/>
+	<key>com.apple.mediaremote.device-info</key>
+	<true/>
 	<key>com.apple.nearbyd.beacon</key>
 	<true/>
 	<key>com.apple.nearbyd.diagnostics</key>
 	<true/>
 	<key>com.apple.nearbyd.xpc</key>
 	<true/>
+	<key>com.apple.nearbyinteraction.background</key>
+	<true/>
 	<key>com.apple.networkd_privileged</key>
 	<true/>
 	<key>com.apple.nfcd.hce</key>

 	<true/>
 	<key>com.apple.private.nearbyinteraction.device-presence</key>
 	<true/>
+	<key>com.apple.private.nearbyinteraction.privileged</key>
+	<true/>
 	<key>com.apple.private.necp.policies</key>
 	<true/>
 	<key>com.apple.private.nehelper.privileged</key>

 	</array>
 	<key>com.apple.rapport.Client</key>
 	<true/>
+	<key>com.apple.rapport.NearbyInvitation</key>
+	<true/>
 	<key>com.apple.rapport.siri-audio</key>
 	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.CompanionLink</string>
 		<string>com.apple.rapport</string>
+		<string>com.apple.rapport.NearbyInvitation</string>
 		<string>com.apple.securityd.ckks</string>
 		<string>com.apple.SharedWebCredentials</string>
 		<string>com.apple.SiriVOXService.client</string>

```
### remindd

> `/usr/libexec/remindd`

```diff

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<key>value</key>
 		<string>com.apple.reminders</string>
 	</dict>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>Reminders.Grocery.MiscategorizedGroceryItem</string>
+	</array>
 	<key>com.apple.private.calendar.changeIdTrackingOverride</key>
 	<true/>
 	<key>com.apple.private.calendar.has-adopted-modern-request-access-methods</key>

 	</array>
 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
-		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.private.tcc.kill-on-assumed-identity-authorization-change</key>

 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### remotepairingdeviced

> `/usr/libexec/remotepairingdeviced`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.CoreDevice.remotepairingdeviced</string>
 	<key>com.apple.CompanionLink</key>
 	<true/>
 	<key>com.apple.PairingManager.Read</key>

 		<string>BluetoothAddress</string>
 		<string>UniqueChipID</string>
 		<string>UniqueDeviceID</string>
+		<string>SerialNumber</string>
 	</array>
 	<key>com.apple.private.corewifi</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.skywalk.register-kernel-pipe</key>
+	<true/>
+	<key>com.apple.private.skywalk.register-user-pipe</key>
+	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
 	<key>com.apple.rapport.Client</key>

```
### replayd

> `/usr/libexec/replayd`

```diff

 	<true/>
 	<key>com.apple.private.SkyLight.contentstream</key>
 	<true/>
+	<key>com.apple.private.SkyLight.screencaptureproxying</key>
+	<true/>
 	<key>com.apple.private.audio.interprocess-tap</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceRemoteDesktop</string>
+		<string>kTCCServiceScreenCapture</string>
 	</array>
 	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
 	<true/>

```
### routined

> `/usr/libexec/routined`

```diff

 	<true/>
 	<key>com.apple.corelocation.map-helper-service</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.extension-host.widget-extension</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.routined</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppLaunch</string>
 		<string>AppIntent</string>
+		<string>Device.Power.PluggedIn</string>
+		<string>Device.ScreenLocked</string>
+		<string>Device.Wireless.WiFiAvailabilityStatus</string>
+		<string>Motion.Activity</string>
 	</array>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>

 	<array>
 		<string>com.apple.private.alloy.safetymonitor.ownaccount</string>
 		<string>com.apple.private.alloy.safetymonitor</string>
-		<string>com.apple.private.alloy.multiplex1</string>
+		<string>com.apple.private.alloy.safetymonitor.multiplex</string>
 	</array>
 	<key>com.apple.private.ids.messaging.urgent-priority</key>
 	<array>

 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.safetyalerts</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.managed-preference.read-only</key>
 	<array>

```
### rtcreportingd

> `/usr/libexec/rtcreportingd`

```diff

 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/</string>
+		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-writ</key>
 	<array>
 		<string>/tmp</string>

```
### runningboardd

> `/usr/libexec/runningboardd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.driverkitd</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.spawn-driver</key>
 	<true/>
 	<key>com.apple.private.task_policy</key>

 	<true/>
 	<key>com.apple.security.enterprise-volume-access</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.spd.anypidmonitoring</key>
 	<true/>
 	<key>com.apple.tailspin.dump-output</key>

```
### safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

 	<true/>
 	<key>com.apple.apsd.ios-device-push-token</key>
 	<true/>
+	<key>com.apple.bluetooth.safetyalerts</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.driver.AppleConvergedIPCBB.user-access</key>

 	<string>com.apple.safetyalertsd</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>Device.Wireless.APSDInterfaceStatus</string>
 		<string>Device.Wireless.CellularQualityStatus</string>
 		<string>Device.Wireless.WiFi</string>
 		<string>Device.Wireless.WiFiAvailabilityStatus</string>

```
### securityd

> `/usr/libexec/securityd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.authkit.devicelist.server-only</key>
+	<true/>
 	<key>com.apple.developer.aps-environment</key>
 	<string>serverPreferred</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

```
### sensorkitd

> `/usr/libexec/sensorkitd`

```diff

 	<true/>
 	<key>com.apple.private.tcc.manager.access.delete</key>
 	<array>
+		<string>kTCCServiceSensorKitHistoricalMobilityMetrics</string>
+		<string>kTCCServiceSensorKitHistoricalCardioMetrics</string>
 		<string>kTCCServiceSensorKitKeyboardMetrics</string>
 		<string>kTCCServiceSensorKitOdometer</string>
 		<string>kTCCServiceSensorKitFacialMetrics</string>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>
 	<true/>
 	<key>com.apple.keystore.access-keychain-keys</key>

 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
+	<key>com.apple.nfcd.session.credential.manager</key>
+	<true/>
 	<key>com.apple.nfcd.session.fieldOperations</key>
 	<true/>
 	<key>com.apple.nfcd.session.lpemConfig</key>

 	<true/>
 	<key>com.apple.nfcd.session.trust</key>
 	<true/>
+	<key>com.apple.payment.all-access</key>
+	<true/>
+	<key>com.apple.peerpayment.all-access</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>BootManifestHash</string>

 	<true/>
 	<key>com.apple.private.security.storage.SecureElementService</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
+	<key>com.apple.private.seserviced.sereservation.client</key>
+	<true/>
+	<key>com.apple.private.tcc.manager.access.read</key>
+	<array>
+		<string>kTCCServiceAll</string>
+	</array>
+	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
+	<array>
+		<string>kTCCServiceSecureElementAccess</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.secureelementservice.aapp</string>
 	</array>
+	<key>com.apple.runningboard.private.se.credential</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/System/AppleInternal/Library/</string>
 		<string>/System/Library/Preferences/Logging/</string>
 		<string>/AppleInternal/Library/Preferences/Logging/</string>
 		<string>/Library/Preferences/Logging/</string>

 		<string>/usr/libexec/</string>
 		<string>/usr/standalone/firmware/SLAM/</string>
 		<string>/private/preboot/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.security.octagon</string>
 		<string>com.apple.nearbyd.xpc.diagnostics</string>
 		<string>com.apple.secureelementservice.test.events</string>
+		<string>com.apple.seservicexctests.credential-events</string>
 		<string>com.apple.passd.nf-events</string>
+		<string>com.apple.nfcd.credential-events</string>
 		<string>com.apple.seld.tsmmanager</string>
 		<string>com.apple.passd.payment</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>

 		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.carousel.connectionstatusservice</string>
+		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.wallet.application-authorization</string>
+		<string>com.apple.duet.activityscheduler</string>
+		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.SESAngel.mach</string>
+		<string>com.apple.passd.device-registration</string>
+		<string>com.apple.mobileactivationd</string>
+		<string>com.apple.seserviced.sereservation.client</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>com.apple.seserviced</string>
 		<string>com.apple.secureelementservice</string>
 		<string>com.apple.secureelementservice.aapp</string>
+		<string>com.apple.seserviced.contactlessCredential.settings</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

 	<true/>
 	<key>com.apple.seserviced.seendpoints.certificateauthorities</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
+	<key>com.apple.wallet.application-authorization</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.internal.seserviced.keysync.recoveryblobs</string>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.backboard.requestHapticFeedback</key>
+	<true/>
 	<key>com.apple.backboardd.lastUserEventTime</key>
 	<true/>
 	<key>com.apple.bluetooth.internal</key>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corewifi</key>
+	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
 	<key>com.apple.private.familycircle</key>

 		<string>com.apple.networking.captivenetworksupport</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.rapport.people</string>
 		<string>com.apple.rapport</string>
 		<string>com.apple.RemoteDisplay</string>

 		<string>com.apple.airplay</string>
 		<string>com.apple.communicationSafetySettings</string>
 		<string>com.apple.Wallet.public</string>
+		<string>com.apple.preferences.sounds</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### siriknowledged

> `/usr/libexec/siriknowledged`

```diff

 	<true/>
 	<key>com.apple.private.homekit.assistant-identifiers</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.siriknowledged</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>__Koa__</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.InstalledApp</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomCarName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomCarProfileName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomContactGroupName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomContactName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaAudiobookAuthorName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaAudiobookTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaMusicArtistName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaPlaylistTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomMediaShowTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomNotebookItemGroupName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomNotebookItemTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomPaymentsAccountNickname</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomPaymentsOrganizationName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomPhotoAlbumName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomPhotoTag</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomVoiceCommandName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.CustomWorkoutActivityName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaAudiobookAuthor</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaAudiobookTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaMusicArtistName</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaPlaylistTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.IntentVocabulary.GlobalMediaShowTitle</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.Shortcut.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>App.Shortcut.Phrase</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Calendar.Event</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>CarPlay.RadioStation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Contacts.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>FindMy.Device</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Fitness.Guest</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Health.Medication</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>HomeKit.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Location.SignificantLocation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Media.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Podcasts.Entity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Siri.PrivateLearning.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Siri.PrivateLearning.MediaEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>UserAccount.Identity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.link.vocabulary.index</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 		<string>/var/mobile/Library/com.apple.internal.ck/</string>
 		<string>/var/mobile/Library/Caches/com.apple.HomeKit.configurations</string>
 		<string>/private/var/mobile/Library/Assistant/</string>
+		<string>/var/mobile/Library/Biome/sets/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.assistant.analytics</string>
 		<string>com.apple.carpd.xpc</string>
 		<string>com.apple.caraccessoryframework.gatekeeper</string>
+		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.icloud.searchparty.locationfetch.items</string>
 		<string>com.apple.icloud.searchpartyd.ownersession</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.medialibraryd.xpc</string>
 		<string>com.apple.calaccessd</string>
 		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.SetStoreUpdateService</string>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.access.system</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.triald</string>
 		<string>com.apple.assistant.backedup</string>
 		<string>com.apple.assistant.support</string>
+		<string>com.apple.mobilecal</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### softposreaderd

> `/usr/libexec/softposreaderd`

```diff

 		<string>NDEF</string>
 		<string>TAG</string>
 	</array>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
 	<key>com.apple.nfcd.session.reader.internal</key>

 	<true/>
 	<key>com.apple.private.applesse.allow</key>
 	<true/>
+	<key>com.apple.private.applesse.baa</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>Library/Application Support/com.apple.softposreader/</string>

 	<array>
 		<string>com.apple.coremedia.systemcontroller.xpc</string>
 		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.seld.tsmmanager</string>
 		<string>com.apple.timed.xpc</string>
+		<string>com.apple.mobileactivationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.softposreaderd</string>
+	<key>com.apple.seld.tsmmanager</key>
+	<true/>
 	<key>com.apple.seserviced.key</key>
 	<true/>
 	<key>keychain-access-groups</key>

```

### 🆕 soundanalysisd

> `/usr/libexec/soundanalysisd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.CompanionLink</key>
	<true/>
	<key>com.apple.SoundAnalysis.CanHostDaemon</key>
	<true/>
	<key>com.apple.aned.private.ANEAccess.allow</key>
	<true/>
	<key>com.apple.aned.private.allow</key>
	<true/>
	<key>com.apple.coreaudio.CanRecordPastData</key>
	<true/>
	<key>com.apple.coreaudio.CanRecordWithoutSessionActivation</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.hid.manager.user-access-protected</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.soundanalysisd</string>
	<key>com.apple.private.biome.read-only</key>
	<array/>
	<key>com.apple.private.biome.read-write</key>
	<array/>
	<key>com.apple.private.coreaudio.rpbserver</key>
	<true/>
	<key>com.apple.private.exclaves.conclave-host</key>
	<true/>
	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMicrophone</string>
	</array>
	<key>com.apple.rapport.Client</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Audio/Tunings/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.soundanalysisd/</string>
		<string>/exclave/catalogue</string>
		<string>/exclave/com.apple.SoundAnalysis</string>
	</array>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>RootDomainUserClient</string>
		<string>AppleSPUUserClient</string>
		<string>IOHIDLibUserClient</string>
		<string>IOSurfaceRootUserClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>AGXDeviceUserClient</string>
		<string>AppleSMCClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.audio.isolated.client.service</string>
		<string>com.apple.audio.AudioQueueServer</string>
		<string>com.apple.audio.AudioSession</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.CompanionLink</string>
		<string>com.apple.appleneuralengine</string>
		<string>com.apple.appleneuralengine.private</string>
		<string>com.apple.tuningtargetd</string>
		<string>com.apple.remoted</string>
		<string>com.apple.symptom_diagnostics</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SoundAnalysis</string>
		<string>com.apple.rapport</string>
		<string>com.apple.coreaudio</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>kern.exclaves_status</string>
		<string>kern.task_conclave</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### spindump_fileparser

> `/usr/libexec/spindump_fileparser`

```diff

 	<true/>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>
+	<key>com.apple.trial.status.deployment-environment.allow</key>
+	<array>
+		<integer>0</integer>
+	</array>
 </dict>
 </plist>
 

```
### sportsd

> `/usr/libexec/sportsd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>Production</string>
+	<key>com.apple.private.activitykit.activityAuthorizationListener</key>
+	<true/>
 	<key>com.apple.private.activitykit.activityAuthorizer</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

```
### srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.mDNSResponder.dns-service-registration</key>
+	<true/>
 	<key>com.apple.mDNSResponder_Helper</key>
 	<true/>
 	<key>com.apple.networkd_privileged</key>

 		<string>com.apple.network.IPConfiguration</string>
 		<string>com.apple.pfd</string>
 		<string>com.apple.mDNSResponder_Helper</string>
+		<string>com.apple.mDNSResponder.control</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### symptomsd

> `/usr/libexec/symptomsd`

```diff

 	<true/>
 	<key>com.apple.awdd.manager-access</key>
 	<true/>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
-	<key>com.apple.coreduetd.context</key>
-	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

```
### symptomsd-helper

> `/usr/libexec/symptomsd-helper`

```diff

 	<true/>
 	<key>com.apple.awdd.manager-access</key>
 	<true/>
-	<key>com.apple.coreduetd.allow</key>
-	<true/>
-	<key>com.apple.coreduetd.context</key>
-	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	<true/>
 	<key>com.apple.polaris.client</key>
 	<true/>
+	<key>com.apple.private.CoreRepairCore.repairInfo</key>
+	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.dumpSysdiagnoseDataToDir</key>
+	<true/>
 	<key>com.apple.private.endpoint-security.xpc</key>
 	<true/>
 	<key>com.apple.private.eyecandy.sysdiagnose</key>

 		<string>systemgroup.com.apple.powerlog</string>
 		<string>systemgroup.com.apple.ReportMemoryException</string>
 	</array>
+	<key>com.apple.springboard.statedump</key>
+	<true/>
 	<key>com.apple.sysmond.client</key>
 	<true/>
 	<key>com.apple.tailspin.dump-output</key>

```
### sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

 	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
+	<key>com.apple.private.clouddocs.read-diagnostic-metadata</key>
+	<true/>
 	<key>com.apple.private.coreservices.cangetcurrentactivityinfo</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	<true/>
 	<key>com.apple.private.diagnostics</key>
 	<true/>
+	<key>com.apple.private.fileprovider.read-diagnostic-metadata</key>
+	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.sysdiagnose</string>

 		<string>systemgroup.com.apple.mobile.installationhelperlogs</string>
 		<string>systemgroup.com.apple.powerlog</string>
 	</array>
-	<key>com.apple.soundboard.sysdiagnose</key>
-	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### sysstatuscheck

> `/usr/libexec/sysstatuscheck`

```diff

 	<true/>
 	<key>com.apple.private.kernel.get-kext-info</key>
 	<true/>
+	<key>com.apple.private.memoryinfo</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOWatchdogUserClient</string>

```
### tailspind

> `/usr/libexec/tailspind`

```diff

 	<true/>
 	<key>com.apple.private.roots-installed-read-only</key>
 	<true/>
+	<key>com.apple.private.security.storage.spindump</key>
+	<true/>
 	<key>com.apple.private.stackshot</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 	<true/>
 	<key>com.apple.tailspin.symbolication</key>
 	<true/>
+	<key>com.apple.trial.status.deployment-environment.allow</key>
+	<array>
+		<integer>0</integer>
+	</array>
 </dict>
 </plist>
 

```
### terminusd

> `/usr/libexec/terminusd`

```diff

 	<true/>
 	<key>com.apple.developer.networking.multipath_extended</key>
 	<true/>
+	<key>com.apple.mDNSResponder.dnsproxy</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.paireddeviceregistry</key>

 		<string>com.apple.nano.nanoregistry.paireddeviceregistry</string>
 		<string>com.apple.FileCoordination</string>
 		<string>com.apple.wifip2pd</string>
+		<string>com.apple.mDNSResponder.control</string>
 	</array>
 	<key>com.apple.security.exception.nano-preference.read-only</key>
 	<array>

```
### thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

 	<true/>
 	<key>com.apple.private.clpc.seeding</key>
 	<true/>
+	<key>com.apple.private.getprivatesysid</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-monitor</key>
 	<true/>
 	<key>com.apple.private.iomfb.set-block</key>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.powerlogHelperd.XPCService.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### transparencyd

> `/usr/libexec/transparencyd`

```diff

 	</dict>
 	<key>com.apple.private.cloudkit.setEnvironment</key>
 	<true/>
+	<key>com.apple.private.cloudkit.spi</key>
+	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<array>
 		<string>com.apple.madrid</string>
 	</array>
+	<key>com.apple.private.ids.remotecredentials</key>
+	<true/>
 	<key>com.apple.private.ids.remoteurlconnection</key>
 	<true/>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.AppleMediaServices</string>
+		<string>com.apple.itunescloud</string>
 		<string>com.apple.mediaremote</string>
 		<string>com.apple.tvremoted</string>
 		<string>com.apple.TVRemoteMediaServices</string>

```
### usermanagerd

> `/usr/libexec/usermanagerd`

```diff

 	<true/>
 	<key>com.apple.private.vfs.dataless-resolver</key>
 	<true/>
+	<key>com.apple.private.vfs.exclave-fs-register</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.userspace-reboot</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.userspace-reboot-now</key>

```
### watchdogd

> `/usr/libexec/watchdogd`

```diff

 	<true/>
 	<key>com.apple.private.iowatchdog.user-access</key>
 	<true/>
+	<key>com.apple.private.security.storage.spindump</key>
+	<true/>
 	<key>com.apple.private.security.waitquiet-panics</key>
 	<true/>
 	<key>com.apple.private.stackshot</key>

```
### wifip2pd

> `/usr/libexec/wifip2pd`

```diff

 		<string>com.apple.WirelessCoexManager</string>
 		<string>com.apple.PineBoardServices</string>
 		<string>com.apple.CARenderServer</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
+	<key>com.apple.springboard.launchapplications</key>
+	<true/>
 	<key>com.apple.wifi_awdl.event_monitor</key>
 	<true/>
 	<key>com.apple.wifi_nan.event_monitor</key>

```
### wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

 	<true/>
 	<key>com.apple.private.logging.admin</key>
 	<true/>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.wifi.logs</string>
+	</array>
 	<key>com.apple.private.sysdiagnose</key>
 	<true/>
 	<key>com.apple.private.wifianalytics</key>

```
### BTLEServer

> `/usr/sbin/BTLEServer`

```diff

 	<true/>
 	<key>com.apple.accessoryupdater.uarp</key>
 	<true/>
+	<key>com.apple.bluetooth.pairedInfoSecurity</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.bulletinboard.observer</key>

```
### BlueTool

> `/usr/sbin/BlueTool`

```diff

 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>BlueTool</string>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleBTHciUC</string>

 		<string>AppleBluetoothModuleUserClient</string>
 		<string>AppleConvergedIPCUserClient</string>
 	</array>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>BlueTool</string>
-	</array>
 </dict>
 </plist>
 

```
### absd

> `/usr/sbin/absd`

```diff

 	<array>
 		<string>UniqueDeviceID</string>
 		<string>SerialNumber</string>
-	</array>
+    </array>
+    <key>com.apple.security.ts.system-info</key>
+    <array>
+        <string>net.link.addr</string>
+    </array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/usr/sbin</string>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>BTServer</string>
 	<key>com.apple.private.security.storage.ExposureNotification</key>
 	<true/>
 	<key>com.apple.private.skywalk.register-user-pipe</key>

 	</array>
 	<key>platform-application</key>
 	<true/>
-	<key>seatbelt-profiles</key>
-	<array>
-		<string>BTServer</string>
-	</array>
 </dict>
 </plist>
 

```
### mediaserverd

> `/usr/sbin/mediaserverd`

```diff

 			<dict/>
 		</dict>
 	</dict>
+	<key>com.apple.aop.hid-driver.user-client</key>
+	<dict>
+		<key>gesture</key>
+		<dict>
+			<key>send-command</key>
+			<dict/>
+		</dict>
+	</dict>
 	<key>com.apple.appleneuralengine.private.allow</key>
 	<true/>
 	<key>com.apple.appletv.pbs.av-effects</key>

 	<array>
 		<string>SysCfgDict</string>
 	</array>
+	<key>com.apple.private.ReplayKitAngel.client</key>
+	<true/>
 	<key>com.apple.private.accessories.showallconnections</key>
 	<true/>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>

 	<array>
 		<string>com.apple.developer.driverkit.family.audio</string>
 	</array>
+	<key>com.apple.private.exclaves.conclave-host</key>
+	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 	<true/>
 	<key>com.apple.rapport.Client</key>
 	<true/>
+	<key>com.apple.realitysimulation.rendered-content-service</key>
+	<true/>
 	<key>com.apple.relatived.tempest</key>
 	<true/>
 	<key>com.apple.rootless.storage.facekit</key>

 	<true/>
 	<key>com.apple.runningboard.cameracapture</key>
 	<true/>
+	<key>com.apple.runningboard.endowment-originator</key>
+	<true/>
+	<key>com.apple.runningboard.listallassertions</key>
+	<true/>
 	<key>com.apple.runningboard.mediaexperience</key>
 	<true/>
 	<key>com.apple.runningboard.process-state</key>

 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
 		<string>com.apple.coremedia.nerotransportconnectionxpc</string>
 		<string>com.apple.UXMAssertionService</string>
+		<string>com.apple.ReplayKitAngel.mach</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 		<string>311</string>
 		<string>312</string>
 	</array>
+	<key>com.apple.userexperiencemanager.source-for-recording-user-requested</key>
+	<true/>
 	<key>com.apple.userexperiencemanager.source-for-video-playback</key>
 	<true/>
 	<key>com.apple.videoconference.allow-conferencing</key>

```
### nvram

> `/usr/sbin/nvram`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.private.amfi.version-restriction</key>
+	<integer>1</integer>
 	<key>com.apple.private.iokit.system-nvram-internal-allow</key>
 	<true/>
 </dict>

```
### spindump

> `/usr/sbin/spindump`

```diff

 	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
+	<key>com.apple.trial.status.deployment-environment.allow</key>
+	<array>
+		<integer>0</integer>
+	</array>
 </dict>
 </plist>
 

```
### wifid

> `/usr/sbin/wifid`

```diff

 	<true/>
 	<key>com.apple.sharing.Services</key>
 	<true/>
+	<key>com.apple.springboard.launchapplications</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.smartCoverObserving</key>

```
