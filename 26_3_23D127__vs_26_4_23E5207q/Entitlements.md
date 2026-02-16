## 🔑 Entitlements


### 🆕 AccessoryNotificationsSourceSelection

> `/Applications/AccessoryNotificationsSourceSelection.app/AccessoryNotificationsSourceSelection`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.usernotifications.settings</key>
	<array>
		<string>read</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.usernotifications.accessorynotifications</string>
		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
	</array>
</dict>
</plist>

```

### 🆕 AccessoryNotificationsSetupExtension

> `/Applications/AccessoryNotificationsSourceSelection.app/PlugIns/AccessoryNotificationsSetupExtension.appex/AccessoryNotificationsSetupExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.usernotifications.settings</key>
	<array>
		<string>read</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
	</array>
</dict>
</plist>

```

### 🆕 AdaptiveMusicWidget

> `/Applications/AdaptiveMusicApp.app/PlugIns/AdaptiveMusicWidget.appex/AdaptiveMusicWidget`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>adi-client</key>
	<string>628765583</string>
	<key>application-identifier</key>
	<string>com.apple.AdaptiveMusicApp.AdaptiveMusicWidget</string>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
	</array>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.AdaptiveMusicApp</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/com.apple.PrivacyDisclosure/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Logs/MediaServices/</string>
		<string>/var/mobile/Library/Application Support/com.apple.iTunesCloud/URLBags</string>
		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
		<string>/Library/com.apple.iTunesCloud/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.itunescloud.remote-request-execution-service</string>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.xpc.amsaccountsd</string>
	</array>
	<key>com.apple.symptoms.NetworkOfInterest</key>
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
### AppDistributionLaunchAngel

> `/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel`

```diff

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.ScreenTimeAgent.ask</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.springboard.remote-alert</key>

```
### AppleIDSetupUIService

> `/Applications/AppleIDSetupUIService.app/AppleIDSetupUIService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.fetchNewestPolicies</key>
+	<true/>
+	<key>com.apple.private.eligibilityd.internalState</key>
+	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<true/>
 	<key>com.apple.private.screentime-setup</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.swc.system-app</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>

```

### 🆕 BrowserKitViewService

> `/Applications/BrowserKitViewService.app/BrowserKitViewService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.browser-kit.browserkitd-client</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO</key>
	<true/>
	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceFaceID</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.iconservices</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
</dict>
</plist>

```

### 🆕 BusinessActionSheet

> `/Applications/BusinessActionSheet.app/BusinessActionSheet`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.businessservicesd</string>
	</array>
	<key>com.apple.springboard.allowallcallurls</key>
	<true/>
</dict>
</plist>

```
### CheckerBoard

> `/Applications/CheckerBoard.app/CheckerBoard`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.tzlink</string>
 		<string>com.apple.systemstatus.activityattribution</string>
 		<string>com.apple.systemstatus.publisher</string>
 		<string>com.apple.systemstatus</string>

 	<array>
 		<string>status-items</string>
 	</array>
+	<key>com.apple.tzlink.allow</key>
+	<true/>
 	<key>com.apple.wifi.awdl</key>
 	<true/>
 	<key>com.apple.wifi.eap-nearby-device-setup-config-copy</key>

```
### Climate

> `/Applications/Climate.app/Climate`

```diff

 		<string>PositionTracker</string>
 		<string>Climate</string>
 	</array>
+	<key>com.apple.private.airplay.overlays</key>
+	<true/>
 	<key>com.apple.private.carkit</key>
 	<true/>
 	<key>com.apple.private.carp</key>

 		<string>com.apple.caraccessoryframework.cardata</string>
 		<string>com.apple.CarAssetUtils.variants</string>
 		<string>com.apple.carkit.service</string>
+		<string>com.apple.airplay.overlays.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### ClockAngel

> `/Applications/ClockAngel.app/ClockAngel`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.ClockAngel</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
 	<key>com.apple.bannerkit.post</key>

```

### 🆕 CompanionSetup

> `/Applications/CompanionSetup.app/CompanionSetup`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>AMSDeviceOfferRegistrationTask</key>
	<true/>
	<key>adi-client</key>
	<string>559326803</string>
	<key>application-identifier</key>
	<string>com.apple.CompanionSetup</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CompanionLink</key>
	<true/>
	<key>com.apple.PairingManager.HomeKit</key>
	<true/>
	<key>com.apple.PairingManager.Read</key>
	<true/>
	<key>com.apple.PairingManager.Write</key>
	<true/>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.TextInput.user-directory-trader</key>
	<true/>
	<key>com.apple.UIKit.vends-view-services</key>
	<true/>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>
	<true/>
	<key>com.apple.accounts.idms.fullaccess</key>
	<true/>
	<key>com.apple.appleaccount.custodian</key>
	<true/>
	<key>com.apple.appleaccount.identity.read</key>
	<true/>
	<key>com.apple.appleidsetup.repair.client</key>
	<true/>
	<key>com.apple.appprotectiond.guard.access</key>
	<true/>
	<key>com.apple.appprotectiond.read.access</key>
	<true/>
	<key>com.apple.appstored.install-apps</key>
	<true/>
	<key>com.apple.appstored.install-system-apps</key>
	<true/>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.authkit.client.internal</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.bluetooth.discovery</key>
	<dict>
		<key>AppleTVSetup</key>
		<dict>
			<key>bleRSSIThresholdHint</key>
			<integer>-45</integer>
			<key>discoveryFlags</key>
			<array>
				<string>AppleTVSetup</string>
			</array>
			<key>osFeatureFlag</key>
			<string>CompanionServices/TVSetupV2</string>
			<key>sceneIdentifier</key>
			<string>AppleTVSetup</string>
			<key>screenLocked</key>
			<true/>
			<key>systemUnlocked</key>
			<true/>
		</dict>
		<key>CompanionSetup</key>
		<dict>
			<key>bleRSSIThresholdHint</key>
			<integer>-45</integer>
			<key>discoveryTypes</key>
			<array>
				<string>CompanionSetup</string>
			</array>
			<key>sceneIdentifier</key>
			<string>CompanionSetup</string>
			<key>screenLocked</key>
			<true/>
			<key>systemUnlocked</key>
			<true/>
		</dict>
		<key>HomePodSetup</key>
		<dict>
			<key>bleRSSIThresholdHint</key>
			<integer>-45</integer>
			<key>discoveryFlags</key>
			<array>
				<string>HomePodSetup</string>
			</array>
			<key>discoveryTypes</key>
			<array>
				<string>HomePodSetupV2</string>
			</array>
			<key>osFeatureFlag</key>
			<string>CompanionServices/HomePodSetupV2</string>
			<key>sceneIdentifier</key>
			<string>HomePodSetup</string>
		</dict>
	</dict>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.cdp.recoverykey</key>
	<true/>
	<key>com.apple.cdp.statemachine</key>
	<true/>
	<key>com.apple.cdp.utility</key>
	<true/>
	<key>com.apple.cdp.walrus</key>
	<true/>
	<key>com.apple.chronoservices</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.driverkit.userclient-access</key>
	<array>
		<string>com.apple.DriverKit-AppleBCMWLAN</string>
	</array>
	<key>com.apple.developer.homekit</key>
	<true/>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.pass-type-identifiers</key>
	<array>
		<string>*.pass.com.apple.itunes.storecredit</string>
	</array>
	<key>com.apple.findmy.findmylocate.fenceservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.friendshipservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.locationservice</key>
	<true/>
	<key>com.apple.findmy.findmylocate.settings</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.homekit.private-spi-access</key>
	<true/>
	<key>com.apple.idle-timer-services</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.locationd.authorizeapplications</key>
	<true/>
	<key>com.apple.locationd.status</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled-access</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.networkrelay.deviceMonitor</key>
	<true/>
	<key>com.apple.networkrelay.devices.read</key>
	<true/>
	<key>com.apple.networkrelay.devices.write</key>
	<true/>
	<key>com.apple.nexus</key>
	<true/>
	<key>com.apple.payment.card-on-file</key>
	<true/>
	<key>com.apple.private.CoreAuthentication.SPI</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.applemediaservices.multiuser</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
		<string>com.apple.MobileAsset.SoftwareUpdate</string>
		<string>com.apple.MobileAsset.SoftwareUpdateDocumentation</string>
		<string>com.apple.MobileAsset.VoiceTriggerAssetsTV</string>
	</array>
	<key>com.apple.private.assets.change-daemon-config</key>
	<true/>
	<key>com.apple.private.biometrickit.allow-default</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.tvos.userprofiles</key>
		<string>com.apple.tvos.userprofiles</string>
	</dict>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.corewifi.keychain</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.game-center</key>
	<array>
		<string>Account</string>
	</array>
	<key>com.apple.private.game-center.bypass-authentication</key>
	<true/>
	<key>com.apple.private.homekit</key>
	<true/>
	<key>com.apple.private.homekit.home-location</key>
	<true/>
	<key>com.apple.private.homekit.location</key>
	<true/>
	<key>com.apple.private.homekit.pairing-identity</key>
	<true/>
	<key>com.apple.private.homekit.pairing-identity.private</key>
	<true/>
	<key>com.apple.private.ids.messaging</key>
	<array>
		<string>com.apple.private.alloy.willow</string>
	</array>
	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>
	<true/>
	<key>com.apple.private.mobileinstall.allowedSPI</key>
	<array>
		<string>InstallForLaunchServices</string>
	</array>
	<key>com.apple.private.octagon</key>
	<true/>
	<key>com.apple.private.security.storage.DuetExpertCenter</key>
	<true/>
	<key>com.apple.private.security.storage.HomeKit</key>
	<true/>
	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
	<true/>
	<key>com.apple.private.systempreferences</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceAddressBook</string>
		<string>kTCCServiceBluetoothAlways</string>
		<string>kTCCServiceBluetoothPeripheral</string>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceFaceID</string>
		<string>kTCCServiceMediaLibrary</string>
		<string>kTCCServiceMicrophone</string>
		<string>kTCCServicePhotos</string>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.proactive.AppPrediction.predictions</key>
	<true/>
	<key>com.apple.proactive.DefaultWidgetSuggester</key>
	<true/>
	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
	<true/>
	<key>com.apple.rootless.storage.proactivepredictions</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/os_eligibility/eligibility.plist</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Media/PhotoData/</string>
		<string>/private/var/mobile/tmp/</string>
		<string>/private/var/tmp/APCCaptures/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/DuetExpertCenter/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/VoiceTrigger/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.aa.daemon.xpc</string>
		<string>com.apple.aa.identity.xpc</string>
		<string>com.apple.adid</string>
		<string>com.apple.ak.authorizationservices.xpc</string>
		<string>com.apple.amsaccountsd.multiuser</string>
		<string>com.apple.appleidsetupd.repair.xpc</string>
		<string>com.apple.appleidsetupd.setup.xpc</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.appstored.xpc.request</string>
		<string>com.apple.assistant.multiuser.service</string>
		<string>com.apple.audio.AudioSession</string>
		<string>com.apple.audio.SystemSoundServer-iOS</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.bluetooth.xpc</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.chronoservices</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.findmy.findmylocate.fenceservice</string>
		<string>com.apple.findmy.findmylocate.friendshipservice</string>
		<string>com.apple.findmy.findmylocate.locationservice</string>
		<string>com.apple.findmy.findmylocate.settings</string>
		<string>com.apple.homed.xpc</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.iphone.axserver</string>
		<string>com.apple.itunescloud.music-subscription-status-service</string>
		<string>com.apple.lsd.installation</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.nexus</string>
		<string>com.apple.PairingManager</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.ScreenTimeAgent.persistence</string>
		<string>com.apple.security.octagon</string>
		<string>com.apple.SharingServices</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.sucontrollerd</string>
		<string>com.apple.systemstatus.activityattribution</string>
		<string>com.apple.TextInput.user-directory-trader-server</string>
		<string>com.apple.timed.xpc</string>
		<string>com.apple.wifi.manager</string>
		<string>com.apple.wifip2pd</string>
		<string>com.apple.xpc.amsaccountsd</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.da</string>
		<string>com.apple.nexus</string>
		<string>com.apple.rapport</string>
		<string>com.apple.speakerrecognition</string>
		<string>com.apple.voicetrigger</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.CompanionSetupKit</string>
		<string>com.apple.coreaudio</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.appleidsetupd.repair.xpc</string>
		<string>com.apple.appleidsetupd.setup.xpc</string>
		<string>com.apple.AppleMediaServicesUIDynamicService</string>
		<string>com.apple.appprotectiond.guard</string>
		<string>com.apple.appprotectiond.read</string>
		<string>com.apple.askpermissiond</string>
		<string>com.apple.bluetooth.xpc</string>
		<string>com.apple.cdp.daemon</string>
		<string>com.apple.homed.xpc</string>
		<string>com.apple.identityservicesd.embedded.auth</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.nexus</string>
		<string>com.apple.PairingManager</string>
		<string>com.apple.passd.in-app-payment</string>
		<string>com.apple.passd.library</string>
		<string>com.apple.passd.payment</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.ScreenTimeAgent.persistence</string>
		<string>com.apple.security.octagon</string>
		<string>com.apple.SharingServices</string>
		<string>com.apple.sucontrollerd</string>
		<string>com.apple.SystemConfiguration.configd</string>
		<string>com.apple.TextInput.user-directory-trader-server</string>
		<string>com.apple.wifip2pd</string>
		<string>com.apple.xpc.amsaccountsd</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.CompanionSetupKit</string>
		<string>com.apple.coreaudio</string>
	</array>
	<key>com.apple.security.ts.play-audio</key>
	<true/>
	<key>com.apple.security.ts.play-media</key>
	<true/>
	<key>com.apple.sharing.Client</key>
	<true/>
	<key>com.apple.springboard-ui.client</key>
	<true/>
	<key>com.apple.springboard.activateRemoteAlert</key>
	<true/>
	<key>com.apple.springboard.capture-button-restriction</key>
	<true/>
	<key>com.apple.springboard.hardware-button-service.event-consumption</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.private.capture-button-events</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.springboard.requestScene-daemon</key>
	<true/>
	<key>com.apple.system.diagnostics.iokit-properties</key>
	<true/>
	<key>com.apple.systemstatus.activityattribution</key>
	<true/>
	<key>com.apple.timed</key>
	<true/>
	<key>com.apple.wifip2pd</key>
	<true/>
	<key>com.apple.wlan.authentication</key>
	<true/>
	<key>fairplay-client</key>
	<string>1445028844</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>appleaccount</string>
		<string>com.apple.hap.pairing</string>
		<string>com.apple.pairing</string>
		<string>com.apple.preferences</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

 	<true/>
 	<key>com.apple.coretelephony.Identity.get</key>
 	<true/>
+	<key>com.apple.frontboard</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
 	<key>com.apple.mkb.usersession.keybagopaquedata</key>
 	<true/>
+	<key>com.apple.private.corewifi.bssid</key>
+	<true/>
+	<key>com.apple.private.corewifi.countrycode</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.iokit.rootdomain-set-property</key>

 	<true/>
 	<key>com.apple.runningboard.UIKitKeyboardManagement</key>
 	<true/>
+	<key>com.apple.runningboard.assertions.angeltarget</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
 	<key>com.apple.runningboard.primitiveattribute</key>

```

### 🆕 Diagnostic-6010

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6010.appex/Diagnostic-6010`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticsKit.extension</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.Diagnostics</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.DiagnosticsKit</string>
	</array>
</dict>
</plist>

```
### Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

```diff

 	<true/>
 	<key>com.apple.DiagnosticsSupport.HardwareButtonAccess</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.private.corerepair.attestation</key>
 	<true/>
 	<key>com.apple.private.corerepair.xpc</key>

```
### EventViewService

> `/Applications/EventViewService.app/EventViewService`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
-	<key>com.apple.appprotectiond.read.access</key>
-	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.developer.associated-domains</key>

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.private.corewifi-xpc</string>
-		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 </dict>
 </plist>
 

```
### FTMInternal

> `/Applications/FTMInternal.app/FTMInternal`

```diff

 	</array>
 	<key>com.apple.private.nsurlsession.impersonate</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.basebandd.xpc</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.FTMInternal</string>
+	</array>
 	<key>com.apple.security.files.user-selected.read-write</key>
 	<true/>
 	<key>com.apple.springboard.allowIconVisibilityChanges</key>

```
### FamilyControlsAuthenticationUI

> `/Applications/FamilyControlsAuthenticationUI.app/FamilyControlsAuthenticationUI`

```diff

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.screen-time</key>
+	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.runningboard.screentimeunlock</key>
+	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.ScreenTimeAgent.communication</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.FamilyControlsAgent.permissions-requirement.overrides</string>

```
### Feedback Assistant iOS

> `/Applications/Feedback Assistant iOS.app/Feedback Assistant iOS`

```diff

 	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
+	<key>com.apple.developer.associated-domains</key>
+	<array/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.siri</key>

 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>
 	<true/>
+	<key>com.apple.private.swc.system-app</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### FinanceUIService

> `/Applications/FinanceUIService.app/FinanceUIService`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.rtcreportingd</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.financed.service.bankconnect</string>

```
### FindMyRemoteUIService

> `/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService`

```diff

 		<string>com.apple.findmy.findmylocate.friendshipservice</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.findmy.findmylocate.fenceservice</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.icloud.searchpartyd.ownersession</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FMDCFUTheftAndLossReminderExtension

> `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/FMDCFUTheftAndLossReminderExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.icloud.FindMyDevice.FindMyDeviceSharedConfiguration.access</key>
 	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
+	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>SerialNumber</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.icloud.findmydeviced</string>
+		<string>com.apple.icloud.searchpartyd.beaconmanager.simplebeacon</string>
+		<string>com.apple.ak.auth.xpc</string>
 	</array>
 </dict>
 </plist>

```
### LocalAuthenticationUIService

> `/Applications/LocalAuthenticationUIService.app/LocalAuthenticationUIService`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.LocalAuthentication.RemoteUIHost</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.sharingd.nsxpc</string>

```
### MXUIServiceApp

> `/Applications/MXUIServiceApp.app/MXUIServiceApp`

```diff

 	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>
 	<true/>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.systemstatus.publisher</string>
+	</array>
 	<key>com.apple.springboard.requestScene-daemon</key>
 	<true/>
+	<key>com.apple.systemstatus.publisher.domains</key>
+	<array>
+		<string>background-activities</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### MagnifierAngel

> `/Applications/MagnifierAngel.app/MagnifierAngel`

```diff

 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>
 	<true/>
+	<key>com.apple.microlocation.connection</key>
+	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
 	<key>com.apple.private.activitykit.ephemeralActivityRequester</key>

 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VideoIntelligence/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/Accessibility/LiveOn/</string>
+	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.milod.xpc.service</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.accessibility.AXSpringBoardServer</string>
 		<string>com.apple.modelmanager</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
+		<string>com.apple.perceptiond.peripheralSensing</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### Media

> `/Applications/Media.app/Media`

```diff

 	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.biome.read-only</key>
+	<array>
+		<string>App.Intent</string>
+		<string>App.Intents.Transcript</string>
+	</array>
 	<key>com.apple.private.caraccessoryframework.nowplaying</key>
 	<true/>
 	<key>com.apple.private.carkit</key>

 		<string>com.apple.carkit.service</string>
 		<string>com.apple.caraccessoryframework.nowplaying</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
+		<string>com.apple.appprotectiond.read</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.CoreDuet</string>
+		<string>com.apple.spotlightui</string>
 	</array>
 	<key>keychain-access-groups</key>
 	<array>

```
### MediaRemoteUI

> `/Applications/MediaRemoteUI.app/MediaRemoteUI`

```diff

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.mediacontrols</string>
 		<string>com.apple.mediacontrol</string>
 		<string>com.apple.CoreDuet</string>
 		<string>com.apple.lockscreen.shared</string>

```
### SpotlightIndexExtension

> `/Applications/MobilePhone.app/PlugIns/SpotlightIndexExtension.appex/SpotlightIndexExtension`

```diff

 	</array>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### MusicRecognition

> `/Applications/MusicRecognition.app/MusicRecognition`

```diff

 	<true/>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>1445028844</string>
 </dict>
 </plist>
 

```
### NFCUISceneService

> `/Applications/NFCUISceneService.app/NFCUISceneService`

```diff

 	<true/>
 	<key>com.apple.nfcd.background.tag.reading.extension</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.runningboard.assertions.angeltarget</key>

```
### PDUIApp

> `/Applications/PDUIApp.app/PDUIApp`

```diff

 	<array>
 		<string>com.apple.datamigrator</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.videos-preferences</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.PrivacyDisclosure</string>

```
### PassbookUISceneService

> `/Applications/PassbookUISceneService.app/PassbookUISceneService`

```diff

 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>
-	<key>com.apple.private.applemediaservices</key>
-	<true/>
 	<key>com.apple.private.appstorecomponents</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
-		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.wallet.features.all-access</key>
 	<true/>
-	<key>fairplay-client</key>
-	<integer>87750944</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.PassbookUIService</string>

```
### PassbookUIService

> `/Applications/PassbookUIService.app/PassbookUIService`

```diff

 	<true/>
 	<key>com.apple.nfcd.radio.powertoggle</key>
 	<true/>
+	<key>com.apple.nfcd.session.cardmigration</key>
+	<true/>
 	<key>com.apple.nfcd.session.ecommerce</key>
 	<true/>
 	<key>com.apple.nfcd.session.fieldOperations</key>

 		<string>com.apple.businessservicesd</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.private.corewifi.internal-xpc</string>
-		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### PeerPaymentMessagesExtension

> `/Applications/PassbookUIService.app/PlugIns/PeerPaymentMessagesExtension.appex/PeerPaymentMessagesExtension`

```diff

 	<array>
 		<string>spi</string>
 	</array>
-	<key>com.apple.Contacts.database-allow</key>
-	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.accounts.appleidauthentication.defaultaccess</key>

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
-	<key>com.apple.private.tcc.allow</key>
-	<array>
-		<string>kTCCServiceAddressBook</string>
-	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

```
### PeopleMessageService

> `/Applications/PeopleMessageService.app/PeopleMessageService`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2132707621</string>
 	<key>application-identifier</key>
 	<string>com.apple.PeopleMessageService</string>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.ams.bag</key>
+	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array>
 		<string>peoplewidget.apple.com</string>

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.keystore.absinthe</key>
+	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+		<string>SerialNumber</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AskToBuy</string>

 	<array>
 		<string>group.com.apple.people</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/HTTPStorages/</string>
+		<string>/Library/Caches/com.apple.peopled/</string>
+		<string>/Library/com.apple.AppleMediaServices/PersistedBags/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.askpermissiond</string>

 		<string>com.apple.ScreenTimeAgent.ask</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.coreduetd.people</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.fairplayd.versioned</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
+	<key>com.apple.store.ams.bag</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>406</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 </dict>
 </plist>
 

```
### PeopleMessagesAskToBuy

> `/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesAskToBuy.appex/PeopleMessagesAskToBuy`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 </dict>
 </plist>
 

```
### PeopleMessagesScreenTime

> `/Applications/PeopleMessageService.app/PlugIns/PeopleMessagesScreenTime.appex/PeopleMessagesScreenTime`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2132707621</string>
 	<key>application-identifier</key>
 	<string>com.apple.PeopleMessageService.ScreenTime</string>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.ams.bag</key>
+	<true/>
 	<key>com.apple.authkit.client.internal</key>
 	<true/>
 	<key>com.apple.authkit.client.private</key>

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.keystore.absinthe</key>
+	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.messages.private.AllowAlertPresentation</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+		<string>SerialNumber</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	<array>
 		<string>group.com.apple.people</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/HTTPStorages/</string>
+		<string>/Library/Caches/com.apple.peopled/</string>
+		<string>/Library/com.apple.AppleMediaServices/PersistedBags/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ScreenTimeAgent.ask</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.contactsd.persistence</string>
 		<string>com.apple.AddressBook.ContactsAccountsService</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.fairplayd.versioned</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.store.ams.bag</key>
+	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 </dict>
 </plist>
 

```
### PhotosUIService

> `/Applications/PhotosUIService.app/PhotosUIService`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.user</string>
+		<string>com.apple.biome.compute.source</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>com.apple.communicationSafetySettings</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### PosterBoard

> `/Applications/PosterBoard.app/PosterBoard`

```diff

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.appstored.xpc</string>
 		<string>com.apple.installcoordinationd</string>
 		<string>com.apple.PosterPlatformSupportBundleService</string>

```
### Preferences

> `/Applications/Preferences.app/Preferences`

```diff

 	<true/>
 	<key>com.apple.private.ClipServices</key>
 	<true/>
+	<key>com.apple.private.CoreAnalytics.ManagementCommands.allow</key>
+	<true/>
+	<key>com.apple.private.CoreAnalytics.RolloverEvents.allow</key>
+	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>

 	<true/>
 	<key>com.apple.private.clouddocs.account-access</key>
 	<true/>
+	<key>com.apple.private.clouddocs.rfa-email-setting</key>
+	<true/>
 	<key>com.apple.private.cloudkit.customAccounts</key>
 	<true/>
 	<key>com.apple.private.cloudkit.displaysSystemAcceptPrompt</key>

 	<true/>
 	<key>com.apple.private.corewifi.internal</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.Preferences.ResetPrivacyWarningsNotification</key>
+	<true/>
 	<key>com.apple.private.darwin-notification.restrict-post.settings.userchangedpasscode</key>
 	<true/>
 	<key>com.apple.private.dmd.emergency-mode</key>

 	<true/>
 	<key>com.apple.private.icloudinboxd.client</key>
 	<true/>
+	<key>com.apple.private.icloudweb</key>
+	<true/>
+	<key>com.apple.private.icloudweb.settings</key>
+	<true/>
 	<key>com.apple.private.ids.idquery-cache-clear</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>AppleIntelligenceReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.Buddy</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>ProactiveAppPrediction</key>
 		<dict>
 			<key>Streams</key>

 	<true/>
 	<key>com.apple.private.iokit.charging-iconography</key>
 	<true/>
+	<key>com.apple.private.iokit.soc-limit</key>
+	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
 	<key>com.apple.private.keychain.sysbound</key>

 	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.osanalytics.SubmitLogs.allow</key>
+	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
 	<key>com.apple.private.persona.read</key>

```
### SafariViewService

> `/Applications/SafariViewService.app/SafariViewService`

```diff

 	<true/>
 	<key>com.apple.appattest.spi</key>
 	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.authentication-services.access-credential-identities</key>
 	<true/>
 	<key>com.apple.authentication-services.allow-authentication-request-any-rpid</key>

 	<true/>
 	<key>com.apple.developer.WebKit.ServiceWorkers</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.identity-document-services.web-presentment-controller</key>
 	<true/>
 	<key>com.apple.developer.networking.HotspotConfiguration</key>

 	<true/>
 	<key>com.apple.private.in-app-payments</key>
 	<true/>
+	<key>com.apple.private.keychain.inet_expansion_fields</key>
+	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
 	<key>com.apple.private.launchservices.changedefaulthandlers</key>

 		<string>com.apple.webprivacyd</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.lsd.modifydb</string>
+		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.Safari.PasswordBreachHelper</string>
 		<string>com.apple.ind.cloudfeatures</string>
 		<string>com.apple.ak.privateemail.xpc</string>

 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.BrowserKit</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.mobileactivationd</string>

 		<string>com.apple.safari.credit-cards</string>
 		<string>com.apple.webkit.webauthn</string>
 		<string>lockdown-identities</string>
+		<string>com.apple.Passwords.LocalState</string>
 		<string>com.apple.password-manager</string>
 		<string>com.apple.password-manager.personal</string>
 		<string>com.apple.cfnetwork-recently-deleted</string>

```
### ScreenshotServicesService

> `/Applications/ScreenshotServicesService.app/ScreenshotServicesService`

```diff

 		<string>Discoverability.Signals</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>VisualIntelligenceCamera.DetectedLabels</string>
+		<string>VisualIntelligenceCamera.Lookup.Event</string>
 	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>

```
### Setup

> `/Applications/Setup.app/Setup`

```diff

 		<string>OSThermalStatus.plist</string>
 		<string>com.apple.jetsam.plist</string>
 	</array>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.TextInput.lexicon-source</key>
 	<true/>
 	<key>com.apple.VideoSubscriberAccount.DeveloperService</key>

 	<true/>
 	<key>com.apple.private.CoreAuthentication.SPI</key>
 	<true/>
+	<key>com.apple.private.InstallCoordination.allowed</key>
+	<true/>
+	<key>com.apple.private.InstallCoordination.uninstall</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.PasscodeServices</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage</key>
+	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage.BiometricLivenessFlag</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.Storage.SetDSLModeEnabled</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.controlcenter.service.moduleidentifiers</key>
+	<array>
+		<string>com.apple.devicemanagementclient.DMCRRTSControlCenterModule</string>
+	</array>
 	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
 	<true/>
 	<key>com.apple.private.corewifi.internal</key>

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>AppleIntelligenceReporting</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>AppleIntelligence.Reporting.Buddy</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>ProactiveAppPrediction</key>
 		<dict>
 			<key>Streams</key>

 	<array>
 		<string>com.apple.AppleAccountUI.CustodianInviteMessageExtension</string>
 	</array>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>InstallForLaunchServices</string>
+		<string>UninstallForLaunchServices</string>
+		<string>FetchListOfAppsRequiringPreInstallConsent</string>
+	</array>
 	<key>com.apple.private.mobilestoredemo.enabledemo</key>
 	<array>
 		<string>Enroll</string>

 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.tips.allow</key>
+	<true/>
 	<key>com.apple.private.usage-tracking</key>
 	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>

 		<string>systemgroup.com.apple.powerlog</string>
 		<string>systemgroup.com.apple.DeviceActivity</string>
 	</array>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.TapToRadarKit.service</string>
+	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.optIn</string>

```
### ShazamEventsApp

> `/Applications/ShazamEventsApp.app/ShazamEventsApp`

```diff

 	</array>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
-	<key>com.apple.appprotectiond.read.access</key>
-	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.itunescloud.remote-request-execution-service</string>
 		<string>com.apple.private.corewifi-xpc</string>
-		<string>com.apple.appprotectiond.read</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.symptoms.NetworkOfInterest</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>apple</string>
+	</array>
 </dict>
 </plist>
 

```
### ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.alarmkit.bundleIdentifier</key>
+	<string>com.apple.reminders</string>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### ShortcutsViewService

> `/Applications/ShortcutsViewService.app/ShortcutsViewService`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.alarmkit.bundleIdentifier</key>
+	<string>com.apple.reminders</string>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

```
### Siri

> `/Applications/Siri.app/Siri`

```diff

 	<true/>
 	<key>com.apple.assistant.analytics-observation</key>
 	<true/>
+	<key>com.apple.assistant.cdm.client</key>
+	<true/>
 	<key>com.apple.assistant.client</key>
 	<true/>
 	<key>com.apple.assistant.security</key>

 	<true/>
 	<key>com.apple.intelligenceflow.context</key>
 	<true/>
+	<key>com.apple.intelligenceplatform.EntityResolution</key>
+	<true/>
+	<key>com.apple.intelligenceplatform.View</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.intents-image-service</key>

 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.private.appintents-bundle-absolute-paths</key>
+	<array>
+		<string>/System/Library/PrivateFrameworks/SiriSharedUI.framework/</string>
+	</array>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
 	<key>com.apple.private.donotdisturb.mode.assertion.client-identifiers</key>

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.views.read-only</key>
+	<array>
+		<string>visualIdentifier</string>
+		<string>entityAliasECR</string>
+		<string>inferenceFeaturesECR</string>
+		<string>entitySubgraph</string>
+		<string>entitySummary</string>
+		<string>peopleSubgraph</string>
+		<string>appEntityRelevanceRanking</string>
+		<string>personEntityRelevanceRanking</string>
+		<string>loiEntityRelevanceRanking</string>
+	</array>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
+	<key>com.apple.private.logging.stream</key>
+	<true/>
 	<key>com.apple.private.mobiletimerd</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
+	<key>com.apple.private.security.storage.Spotlight</key>
+	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sessionkit.presentationObserver</key>
 	<true/>
 	<key>com.apple.private.sessionkit.prominentPresentationAssertionRequester</key>

 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.runningboard.assertions.frontboard</key>
 	<true/>
 	<key>com.apple.runningboard.endowment-originator</key>

 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist</string>
 		<string>/private/var/mobile/Library/Assistant/AssistantSampled/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/tmp/SiriMessages/</string>
 		<string>/Library/SMS/</string>
+		<string>/Library/Spotlight/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/TrimmedAudio/</string>
+		<string>/Library/Shortcuts/</string>
 		<string>/Library/Notes/</string>
 		<string>/Library/Caches/com.apple.notes.autoincrement.lock</string>
 		<string>/Library/Caches/com.apple.notes.objectcreation.lock</string>

 		<string>com.apple.ClipServices.clipserviced</string>
 		<string>com.apple.carkit.dnd.service</string>
 		<string>com.apple.CarPlayApp.non-launching-service</string>
+		<string>com.apple.CarPlayApp.service</string>
+		<string>com.apple.carkit.service</string>
 		<string>com.apple.siri.activation.service</string>
 		<string>com.apple.coreduetd.context</string>
 		<string>com.apple.corespeech.corespeechd.attsiri.service</string>

 		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.generativeexperiences.ExternalPartnerCredentialStorage</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.assistant.cdm</string>
+		<string>com.apple.intelligenceplatform.EntityResolution</string>
+		<string>com.apple.intelligenceplatform.View</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.familycircle.agent</string>
 	</array>
+	<key>com.apple.shortcuts.stepwise-execution</key>
+	<true/>
+	<key>com.apple.shortcuts.variable-injection</key>
+	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
 	<key>com.apple.siri.activation.service</key>

 	<true/>
 	<key>com.apple.sirisuggestions.application-id</key>
 	<string>com.apple.siri</string>
+	<key>com.apple.spotlight.photos.entitledattributes</key>
+	<true/>
 	<key>com.apple.springboard-ui.client</key>
 	<true/>
 	<key>com.apple.springboard.deliveropenurlusingworkspace</key>

```
### Spotlight

> `/Applications/Spotlight.app/Spotlight`

```diff

 		<string>com.apple.DataDeliveryServices</string>
 		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### StickerPickerService

> `/Applications/StickerPickerService.app/StickerPickerService`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageGeneration</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
+		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServicePhotos</string>
 	</array>

```
### SystemActions

> `/Applications/SystemActions.app/SystemActions`

```diff

 		<string>com.apple.nesessionmanager</string>
 		<string>com.apple.posterboardservices.dataModel</string>
 		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.sessionservices</string>
 		<string>com.apple.sharing.airdrop.service</string>

 		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.springboard</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### Web

> `/Applications/Web.app/Web`

```diff

 	<array>
 		<string>com.apple.installcoordinationd</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.springboard.webClipService</key>
 	<true/>
 </dict>

```
### WebSheet

> `/Applications/WebSheet.app/WebSheet`

```diff

 		<string>com.apple.Passwords</string>
 		<string>com.apple.musebuddy</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<array>
 		<string>prefs:root=WIFI</string>

```
### WorkoutRemoteViewService

> `/Applications/WorkoutRemoteViewService.app/WorkoutRemoteViewService`

```diff

 	<true/>
 	<key>com.apple.UIKit.vends-view-services</key>
 	<true/>
+	<key>com.apple.backlight.backlightaccess</key>
+	<true/>
+	<key>com.apple.backlight.performrequest</key>
+	<true/>
+	<key>com.apple.companionappd.connect.allow</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
+	<key>com.apple.fitcore</key>
+	<true/>
+	<key>com.apple.fitcore.session</key>
+	<true/>
+	<key>com.apple.fitnessintelligenced</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
 	<key>com.apple.private.healthkit</key>

 	<true/>
 	<key>com.apple.private.workoutkit</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/mobile/Library/DeviceRegistry/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CompanionLink</string>
+		<string>com.apple.appconduitd.device-connection</string>
+		<string>com.apple.AudioAccessoryServices</string>
+		<string>com.apple.fitnessintelligenced</string>
+		<string>com.apple.heartratecoordinatord.observer</string>
 		<string>com.apple.WorkoutKitXPCService</string>
+		<string>com.apple.seymour</string>
+		<string>com.apple.seymour.session</string>
+		<string>com.apple.private.corewifi-xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.FitnessIntelligence</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.nanolifestyle</string>
+		<string>com.apple.nanolifestyle.sessiontrackerapp</string>
+		<string>com.apple.nanolifestyle.connectedgym</string>
+	</array>
+	<key>com.apple.security.ts.nano-preference.read-write</key>
+	<array>
+		<string>com.apple.nanolifestyle.sessiontrackerapp</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

 	<array>
 		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.gms.availability</string>
+		<string>com.apple.anvil</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### iCloud+

> `/Applications/iCloud+.app/iCloud+`

```diff

 	</array>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 ExpressiveEmbedded

> `/System/ExclaveKit/System/Library/Frameworks/ExpressiveEmbedded.framework/ExpressiveEmbedded`

- No entitlements *(yet)*

### 🆕 IISAudioOutputStreamClientNotifierComponent

> `/System/ExclaveKit/System/Library/Frameworks/IISAudioOutputStreamClientNotifierComponent.framework/IISAudioOutputStreamClientNotifierComponent`

- No entitlements *(yet)*

### 🆕 SystemGraphEmbedded

> `/System/ExclaveKit/System/Library/Frameworks/SystemGraphEmbedded.framework/SystemGraphEmbedded`

- No entitlements *(yet)*

### 🆕 SecureAudioPasscodeComponent

> `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureAudioPasscodeComponent.framework/SecureAudioPasscodeComponent`

- No entitlements *(yet)*

### 🆕 AppleMIDINetworkDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDINetworkDriver.plugin/AppleMIDINetworkDriver`

- No entitlements *(yet)*
### BluetoothUIService

> `/System/Library/CoreServices/BluetoothUIService.app/BluetoothUIService`

```diff

 	<true/>
 	<key>com.apple.bannerkit.post</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.coremedia.asset.xpc</string>
 		<string>com.apple.coremedia.mediaplaybackd.asset.xpc</string>
 		<string>com.apple.audio.AudioSession</string>

 		<string>com.apple.iconservices</string>
 		<string>com.apple.TVSystemUIService.banners</string>
 		<string>com.apple.coremedia.endpoint.xpc</string>
+		<string>com.apple.extensionkitservice</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 		<string>IOMobileFramebufferUserClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.requestScene-daemon</key>
 	<true/>
 	<key>platform-application</key>

```
### CarPlay

> `/System/Library/CoreServices/CarPlay.app/CarPlay`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.airplay.overlays</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowcarplayapps</key>
+	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.dmd.policy</key>

 		<string>com.apple.caraccessoryframework.applinks</string>
 		<string>com.apple.CarPlayApp.punch-through-service</string>
 		<string>com.apple.CarAssetUtils.variants</string>
+		<string>com.apple.airplay.overlays.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### CarPlayTemplateUIHost

> `/System/Library/CoreServices/CarPlayTemplateUIHost.app/CarPlayTemplateUIHost`

```diff

 	<true/>
 	<key>com.apple.private.carp</key>
 	<true/>
+	<key>com.apple.private.externalaccessory.showallaccessories</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.runningboard.carplay</key>

```
### HangHUD

> `/System/Library/CoreServices/HangHUD.app/HangHUD`

```diff

 	<true/>
 	<key>com.apple.multitasking.termination</key>
 	<true/>
+	<key>com.apple.private.clpc.internal</key>
+	<true/>
+	<key>com.apple.private.clpc.reporting</key>
+	<true/>
 	<key>com.apple.private.fpsd.client</key>
 	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
+	<key>com.apple.private.ioreporting.access</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.rtcreportingd</key>

 		<string>NBCoreUserClient</string>
 		<string>NBTimesyncUserClient</string>
 		<string>IOReportUserClient</string>
+		<string>AppleCLPCUserClient</string>
 		<string>IOSurfaceAcceleratorClient</string>
 		<string>H11ANEInDirectPathClient</string>
 	</array>

```
### ReportCrash

> `/System/Library/CoreServices/ReportCrash`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.keystore.info</key>
+	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.osanalytics.otatasking-service-access</key>

 	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
+	<key>com.apple.private.stackshot</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceSystemPolicyAllFiles</string>

```
### ShortcutsActions

> `/System/Library/CoreServices/ShortcutsActions.app/ShortcutsActions`

```diff

 	<true/>
 	<key>com.apple.private.appshortcuts-allow-omit-appname</key>
 	<true/>
-	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
+	<key>com.apple.private.attribution.usage-reporting-only.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>
 		<string>bundleID</string>

```
### SpringBoard

> `/System/Library/CoreServices/SpringBoard.app/SpringBoard`

```diff

 	</array>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.UserAlerts.destinations</key>
+	<array>
+		<string>com.apple.CarPlay.UserAlerts</string>
+	</array>
 	<key>com.apple.abm.helper.mobile.allow</key>
 	<true/>
 	<key>com.apple.accessibility.IDSServices</key>

 	<true/>
 	<key>com.apple.runningboard.listallassertions</key>
 	<true/>
+	<key>com.apple.runningboard.pagein-prefetching</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
 	<key>com.apple.runningboard.primitiveattribute</key>

 		<string>com.apple.PerformanceTrace.ptpassivecollectiond.collectionconfig</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.CarPlayApp.user-alerts-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.suggestions</string>
 		<string>com.apple.assistant.domain.preferences</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.posterboardservices.data-store</key>
+	<true/>
+	<key>com.apple.posterboardservices.data-store.accessSwitcherConfiguration</key>
+	<true/>
 	<key>com.apple.private.sandbox.container-query.all-users</key>
 	<true/>
 	<key>com.apple.security.enterprise-volume-access</key>

 		<string>/private/var/mobile/Library/Caches/com.apple.metal/</string>
 		<string>/private/var/mobile/Library/Caches/com.apple.metalfe/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.posterboardservices.services</string>
+	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>

```
### com.apple.AppleUserHIDDrivers

> `/System/Library/DriverExtensions/com.apple.AppleUserHIDDrivers.dext/com.apple.AppleUserHIDDrivers`

```diff

 			<integer>1452</integer>
 		</dict>
 	</array>
+	<key>com.apple.private.enable-coredump-on-panic</key>
+	<true/>
 </dict>
 </plist>
 

```
### ADAskForExceptionExtension

> `/System/Library/ExtensionKit/Extensions/ADAskForExceptionExtension.appex/ADAskForExceptionExtension`

```diff

 		<string>com.apple.asktod</string>
 		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 </dict>
 </plist>
 

```
### ADFollowUpExtension

> `/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension`

```diff

 	<array>
 		<string>com.apple.managedappdistributiond</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 </dict>
 </plist>
 

```
### ASDAgeAssuranceExtension

> `/System/Library/ExtensionKit/Extensions/ASDAgeAssuranceExtension.appex/ASDAgeAssuranceExtension`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.AppDistributionLaunchAngel</string>
 		<string>com.apple.asktod</string>
 		<string>com.apple.managedappdistributiond.xpc</string>
 		<string>com.apple.familycircle.agent</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### ATXThumbnail

> `/System/Library/ExtensionKit/Extensions/ATXThumbnail.appex/ATXThumbnail`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### AppStoreSettingsAppIntents

> `/System/Library/ExtensionKit/Extensions/AppStoreSettingsAppIntents.appex/AppStoreSettingsAppIntents`

```diff

 <dict>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 </dict>
 </plist>
 

```

### 🆕 AppleIntelligenceReportingSELFIngestor

> `/System/Library/ExtensionKit/Extensions/AppleIntelligenceReportingSELFIngestor.appex/AppleIntelligenceReportingSELFIngestor`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>AssetDelivery.UAF.DailyStatus</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>com.apple.AppleIntelligence.Reporting.AssetBringUp</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AssetDelivery.UAF.DailyStatus</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.AppleIntelligence.Reporting.AssetDeliveryLog</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.Availability</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.MobileAsset</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.MobileAssetVerbose</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.ModelCatalog</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.SoftwareUpdateController</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.UnifiedAssetFramework</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.AppleIntelligence.Reporting.Buddy</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.Buddy</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.AppleIntelligence.Reporting.Invocation.Step</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.Invocation.Step</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.AppleIntelligence.Reporting.ModelIO</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.ModelIO</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.xpc.domain-extension</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
		<string>/private/var/MobileAsset/AssetsV2/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.siri.uaf.subscription.service</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.appleintelligencereporting</string>
		<string>com.apple.appleintelligencereporting.processing</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
		<string>/System/Library/AssetsV2/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.TapToRadarKit.service</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.appleintelligencereporting</string>
		<string>com.apple.appleintelligencereporting.processing</string>
	</array>
</dict>
</plist>

```
### AssistantSettingsControlsExtension

> `/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension`

```diff

 	</array>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/assetsubscriptiond/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.assistant.settings</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
+		<string>com.apple.siri.uaf.service</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 AudioAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/AudioAppIntentsExtension.appex/AudioAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.AudioAppIntentsExtension</string>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
</dict>
</plist>

```
### AudiovisualThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/AudiovisualThumbnailExtension.appex/AudiovisualThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.runningboard</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### CalendarThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/CalendarThumbnailExtension.appex/CalendarThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.runningboard</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### ClockAppIntents

> `/System/Library/ExtensionKit/Extensions/ClockAppIntents.appex/ClockAppIntents`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.private.appintents-attribution-override</key>
 	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>

```
### ContactThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ContactThumbnailExtension.appex/ContactThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.runningboard</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### CoreMotionFoundationModelExtension

> `/System/Library/ExtensionKit/Extensions/CoreMotionFoundationModelExtension.appex/CoreMotionFoundationModelExtension`

```diff

 <?xml version="1.0" encoding="UTF-8"?>
-<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>com.apple.aned.private.ANEAccess.allow</key>
-	<true/>
+    <key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>H11ANEInDirectPathClient</string>
+		<string>AGXDeviceUserClient</string>
+		<string>IOSurfaceRootUserClient</string>
+	</array>
 	<key>com.apple.aned.private.allow</key>
 	<true/>
-	<key>com.apple.modelcatalog.full-access</key>
+	<key>com.apple.aned.private.ANEAccess.allow</key>
+	<true/>
+	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
+
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
+		<!-- Grants access to model assets -->
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
-		<string>com.apple.MobileAsset.UAF.CoreMotion.IMUFoundationModel</string>
+        <string>com.apple.MobileAsset.UAF.CoreMotion.IMUFoundationModel</string>
+		<!-- Grants access to override assets - deny lists and disabled use case list -->
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
-		<string>com.apple.MobileAsset.UAF.CoreMotion.Overrides</string>
+        <string>com.apple.MobileAsset.UAF.CoreMotion.Overrides</string>
 	</array>
-	<key>com.apple.private.security.no-sandbox</key>
-	<true/>
+
+
+	<!--                Section 2            -->
+	<!-- If the calling process is sandboxed -->
+	<!-- - - - - - - - - - - - - - - - - - - -->
+
+	<!-- See Sandbox Rules section below for more information -->
+	<!-- Many of the MobileAsset exceptions are not required if your sandbox has (asset-access). See this document for more information: https://confluence.sd.apple.com/pages/viewpage.action?spaceKey=MASSET&title=Learning+MobileAsset#LearningMobileAsset-Whatifmyprocessisadaemonthatissandboxed?  -->
+
+	<!-- File System -->
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<!-- Grants the sandboxed client process access to create a short term lock on the asset set -->
+		<!--
+			let resource: any AssetBackedResource = ...
+			let lock = try AssetLock()  // <- This initializes a UAFAssetSet which under the hood will take a short term lock on
+										// /private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/com.apple.modelcatalog/shared_locks/atomic_instance_latest.locker
+										// The underlying MobileAsset call is open with the O_SHLOCK flag.
+			let asset = try resource.fetchLockedAsset(with: lock)
+		-->
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		
+		<!-- Grants the sandboxed client process access to read the asset -->
+		<!--
+			let asset = try resource.fetchAsset() // <- At this point the asset metadata.json file is read and parsed
+			let data = Data(contentsOf: asset.contents.baseURL.appending(path: "myFile.dat")) // <- other contents are read
+		-->
+		<!-- Grants access to model assets -->
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/purpose_auto/</string>
+		<!-- Grants access to override assets - deny lists and disabled use case list -->
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel_Overrides/purpose_auto/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		
+		<!-- Access to read preinstalled assets -->
+		<!-- This is needed for asset roots to work. We need both the /var (InstallWithOs) and /System (RequiredByOs) paths. More info here: https://quip-apple.com/I7g3APbmJOdY -->
+		<!-- Grants access to model assets -->
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_CoreMotion_IMUFoundationModel/</string>
+		
+		<!-- Grants access to override assets - deny lists and disabled use case list -->
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 	</array>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.modelcatalog.catalog</string>
-		<string>com.apple.siri.uaf.service</string>
-		<string>com.apple.mobileasset.autoasset</string>
-		<string>com.apple.mobileassetd.v2</string>
-	</array>
+
+	<!-- UserDefaults -->
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<!-- Access to UAF UserDefaults -->
+		<!-- Is this actually needed by the client directly? Probably don't need today, but would be good to add for future proofing. -->
 		<string>com.apple.UnifiedAssetFramework</string>
+		
+		<!-- Access to AJAX override UserDefaults -->
+		<!--
+			let configuration = AJAXConfiguration(url: url, modelName: modelName, endPromptToken: endPromptToken)
+			overrideAJAX(configuration: configuration, forResource: identifier) // <- this currently sets user default
+		-->
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
-	<key>com.apple.security.iokit-user-client-class</key>
+
+	<!-- XPC -->
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>H11ANEInDirectPathClient</string>
-		<string>AGXDeviceUserClient</string>
-		<string>IOSurfaceRootUserClient</string>
+
+		<string>com.apple.modelmanager</string>
+		<!-- Grants access to XPC with modelcatalogd -->
+		<!-- See com.apple.modelcatalog.full-access above -->
+		<string>com.apple.modelcatalog.catalog</string>
+		
+		<!-- Grants access to XPC with siriknowledged? -->
+		<!-- Needed to talk to UAF to do subscribe and unsubscribe (needed for update assets for subscriber) -->
+		<!-- Catalog.requestDownload(...) needs this -->
+		<string>com.apple.siri.uaf.service</string>
+
+		<!-- Grants access to XPC with mobileassetd -->
+		<string>com.apple.mobileasset.autoasset</string>
+
+		<!-- Grants access to XPC with mobileassetd -->
+		<!-- This is needed by clients that fetch assets for asset roots to work. UAF uses V2 APIs to get the asset path direct if it looks like there is an asset root installed (stat directory). -->
+		<string>com.apple.mobileassetd.v2</string>
 	</array>
 </dict>
 </plist>
-

```
### FedAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/FedAutoEvalPlugin.appex/FedAutoEvalPlugin`

```diff

 	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
+		<string>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</string>
+		<string>GenerativeExperiences.GeneratedImageFeatures.ImageInteraction</string>
 		<string>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</string>
+		<string>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</string>
 		<string>GenerativeExperiences.Proactive.UseModelShortcuts</string>
 		<string>GenerativeExperiences.Proactive.UseModelShortcutsProd</string>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
+		<string>GenerativeExperiences.PromptTags</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### FedStatsMLHostPlugin

> `/System/Library/ExtensionKit/Extensions/FedStatsMLHostPlugin.appex/FedStatsMLHostPlugin`

```diff

 		<string>CommApps.CallIntelligence.HoldAssistFedStats</string>
 		<string>Device.Networking.TLS</string>
 		<string>App.EventEngagement</string>
+		<string>AdPlatforms.PolicyInstrumentation.Opportunity</string>
+		<string>AdPlatforms.PolicyInstrumentation.Candidate</string>
+		<string>Mail.Search.Query</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

```
### FontThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/FontThumbnailExtension.appex/FontThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.runningboard</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### GPNonUIExtension

> `/System/Library/ExtensionKit/Extensions/GPNonUIExtension.appex/GPNonUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageGeneration</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### GPUIExtension

> `/System/Library/ExtensionKit/Extensions/GPUIExtension.appex/GPUIExtension`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageGeneration</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### ImageThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/ImageThumbnailExtension.appex/ImageThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.runningboard</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### InferenceProviderService

> `/System/Library/ExtensionKit/Extensions/InferenceProviderService.appex/InferenceProviderService`

```diff

 	</array>
 	<key>com.apple.system.diagnostics.iokit-properties</key>
 	<true/>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>SIML_ADM_PERSONALIZATION</string>
+		<string>UAF_AB_MODELCATALOG</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.modelmanager.inferenceproviderservice</string>

```

### 🆕 KonaSynthesizer

> `/System/Library/ExtensionKit/Extensions/KonaSynthesizer.appex/KonaSynthesizer`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accessibility.systemvoiceprovider</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.accessibility.voices</string>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SpeakSelection</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.accessibility.voices</string>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SpeakSelection</string>
	</array>
	<key>com.apple.security.ts.ipc-posix-shm</key>
	<array>
		<string>apple.shm.notification_center</string>
	</array>
</dict>
</plist>

```

### 🆕 LoadingPoster

> `/System/Library/ExtensionKit/Extensions/LoadingPoster.appex/LoadingPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Library</string>
		<string>Install</string>
	</array>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.appstored.xpc</string>
		<string>com.apple.installcoordinationd</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
</dict>
</plist>

```

### 🆕 MacinTalkAUSP

> `/System/Library/ExtensionKit/Extensions/MacinTalkAUSP.appex/MacinTalkAUSP`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accessibility.systemvoiceprovider</key>
	<true/>
	<key>com.apple.coreaudio.allow-opus-codec</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.TTSAXResourceModelAssets</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_TTSAXResourceModelAssets/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.voiceservices</string>
		<string>com.apple.SpeakSelection</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Caches/TTSResourceCache.plist</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SpeakSelection</string>
		<string>com.apple.voiceservices</string>
	</array>
	<key>com.apple.security.ts.ipc-posix-shm</key>
	<array>
		<string>apple.shm.notification_center</string>
	</array>
</dict>
</plist>

```

### 🆕 MatterAccessoriesSettingsIntents

> `/System/Library/ExtensionKit/Extensions/MatterAccessoriesSettingsIntents.appex/MatterAccessoriesSettingsIntents`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.matter.support.xpc.device-pairing</key>
	<true/>
	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
	<string>com.apple.Preferences</string>
</dict>
</plist>

```

### 🆕 MauiAUSP

> `/System/Library/ExtensionKit/Extensions/MauiAUSP.appex/MauiAUSP`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accessibility.systemvoiceprovider</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.VoiceServices.VoiceResources</string>
		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
		<string>com.apple.MobileAsset.TTSAXResourceModelAssets</string>
	</array>
	<key>com.apple.private.sirittsservice.modify-proxy-assets</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/locks/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_TextToSpeech/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Trial_Siri_SiriTextToSpeech/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Trial_Siri_SiriTextToSpeech/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VoiceServices_CustomVoice/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_TTSAXResourceModelAssets/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VoiceServices_VoiceResources/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VoiceServices_CombinedVocalizerVoices/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SpeakSelection</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/System/Library/AssetsV2/</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.SpeakSelection</string>
	</array>
	<key>com.apple.security.ts.ipc-posix-shm</key>
	<array>
		<string>apple.shm.notification_center</string>
	</array>
</dict>
</plist>

```
### MessagesSettingsWidgetKitExtension

> `/System/Library/ExtensionKit/Extensions/MessagesSettingsWidgetKitExtension.appex/MessagesSettingsWidgetKitExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.CommCenter.StormBreaker</key>
+	<true/>
+	<key>com.apple.CommCenter.fine-grained</key>
+	<array>
+		<string>spi</string>
+	</array>
 	<key>com.apple.chrono.effectiveContainerBundleIdentifier</key>
 	<string>com.apple.Preferences</string>
 	<key>com.apple.default-app.carrier-messaging</key>

 	<true/>
 	<key>com.apple.private.appintents.attribution.bundle-identifier</key>
 	<string>com.apple.Preferences</string>
+	<key>com.apple.private.imcore.imagent</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.madrid</string>
 		<string>com.apple.imessage</string>
+		<string>com.apple.messages</string>
 	</array>
 </dict>
 </plist>

```
### Notification

> `/System/Library/ExtensionKit/Extensions/Notification.appex/Notification`

```diff

 	<true/>
 	<key>com.apple.security.hardened-process.hardened-heap</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### ODDIMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIMetricsExtension.appex/ODDIMetricsExtension`

```diff

 	<array>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
 		<string>Siri.ODDI.ScorecardMetrics</string>
+		<string>Siri.ODDI.ThirdPartyGenAiEngagementInference</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

```

### 🆕 ODDIPoirotExperimentationExtension

> `/System/Library/ExtensionKit/Extensions/ODDIPoirotExperimentationExtension.appex/ODDIPoirotExperimentationExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.siri.ODDIPoirotExperimentationExtension</string>
	<key>com.apple.assistant.settings</key>
	<true/>
	<key>com.apple.private.assistant.settings</key>
	<true/>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.siri.ODDIPoirotExperimentationExtension</string>
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
	<key>com.apple.private.logging.diagnostic</key>
	<true/>
	<key>com.apple.private.logging.stream</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>com.apple.siri.ODDExperimentationExtension</string>
		<string>com.apple.poirot.poirot_tool</string>
	</array>
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
		<string>com.apple.siri.ODDI.PoirotExperimentationWorker</string>
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
		<string>com.apple.siri.ODDI.PoirotExperimentationWorker</string>
	</array>
</dict>
</plist>

```
### ODDIPoirotMetricsExtension

> `/System/Library/ExtensionKit/Extensions/ODDIPoirotMetricsExtension.appex/ODDIPoirotMetricsExtension`

```diff

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Lighthouse.Ledger.LighthousePluginEvent</string>
+		<string>Siri.ODDI.ThirdPartyGenAiEngagementInference</string>
 	</array>
 	<key>com.apple.private.biome.writer</key>
 	<array>

```
### OfficeThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/OfficeThumbnailExtension.appex/OfficeThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.runningboard</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 PCCAgentClientExtension

> `/System/Library/ExtensionKit/Extensions/PCCAgentClientExtension.appex/PCCAgentClientExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.cloudos.PCCAgentClientExtension</string>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.modelcatalog.full-access</key>
	<true/>
	<key>com.apple.modelmanager.inference</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
		<string></string>
	</array>
	<key>com.apple.private.biome.client-identifier</key>
	<string>com.apple.privatemlclient.inferenceproviderservice</string>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
		<string>GenerativeExperiences.TransparencyLog</string>
	</array>
	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
	<true/>
	<key>com.apple.privatecloudcompute.bundleIdentifierOverride</key>
	<true/>
	<key>com.apple.privatecloudcompute.prefetchRequest</key>
	<true/>
	<key>com.apple.privatecloudcompute.requests</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.privatecloudcompute</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.tokengeneration</string>
		<string>com.apple.privatecloudcompute</string>
		<string>com.apple.modelcatalog.multiBaseModel</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.privatemlclient</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/Library/Preferences/com.apple.tokengeneration.plist</string>
		<string>/Library/Preferences/com.apple.privatemlclient.plist</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.privatecloudcompute</string>
		<string>com.apple.modelcatalog.catalog</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.tokengeneration</string>
		<string>com.apple.privatecloudcompute</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.privatemlclient</string>
	</array>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
</dict>
</plist>

```
### PasswordsDataMigration

> `/System/Library/ExtensionKit/Extensions/PasswordsDataMigration.appex/PasswordsDataMigration`

```diff

 		<string>com.apple.private.email</string>
 		<string>com.apple.imagent.embedded.auth</string>
 		<string>com.apple.ak.privateemail.xpc</string>
+		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>

 		<string>com.apple.password-manager.personal-recently-deleted.testing</string>
 		<string>com.apple.password-manager.generated-passwords</string>
 		<string>com.apple.password-manager.generated-passwords.testing</string>
+		<string>com.apple.password-manager.password-evaluations</string>
+		<string>com.apple.password-manager.password-evaluations.testing</string>
 	</array>
 </dict>
 </plist>

```
### PhotoPicker

> `/System/Library/ExtensionKit/Extensions/PhotoPicker.appex/PhotoPicker`

```diff

 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ScreenTimeAgent</string>
 		<string>com.apple.photoanalysisd</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### PhotosMessagesApp

> `/System/Library/ExtensionKit/Extensions/PhotosMessagesApp.appex/PhotosMessagesApp`

```diff

 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.ManagedSettingsAgent</string>
+		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.ScreenTimeAgent.communication</string>
 	</array>

```
### PhotosPicker

> `/System/Library/ExtensionKit/Extensions/PhotosPicker.appex/PhotosPicker`

```diff

 		<string>com.apple.photoanalysisd</string>
 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.mediaanalysisd-generation</string>
+		<string>com.apple.familycircle.agent</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### PrivateMLClientInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/PrivateMLClientInferenceProviderService.appex/PrivateMLClientInferenceProviderService`

```diff

 	<string>com.apple.privatemlclient.inferenceproviderservice</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>TokenGeneration.Inference.Requests</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeExperiences.TransparencyLog</string>
 	</array>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/tmp/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.privatecloudcompute</string>

```
### ProductPageExtension

> `/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.cdp.recoverykey</key>

 	<key>com.apple.private.storekit</key>
 	<array>
 		<string>AdvancedPurchase</string>
+		<string>RemoteDownloadIdentifiers</string>
+		<string>Articles</string>
 	</array>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>

```
### SCARemoteView Appex

> `/System/Library/ExtensionKit/Extensions/SCARemoteView Appex.appex/SCARemoteView Appex`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.SensitiveContentAnalysis.SCARemoteView.Extension</string>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.developer.icloud-container-environment</key>
+	<string>Production</string>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>SensitiveContentAnalysis.UIInteraction</string>

 	<true/>
 	<key>com.apple.private.screentime-communication</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sensitivecontentanalysis.client</key>
 	<array>
 		<string>analyze</string>

 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
+		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.runningboard.screentimeunlock</key>
 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.compute.source</string>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.communicationSafetySettings</string>
+		<string>com.apple.messages</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.ManagedSettingsAgent</string>
 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 	</array>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
+	<key>com.apple.trustkit.orca</key>
+	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>trustkit</string>
+	</array>
 </dict>
 </plist>
 

```

### 🆕 SafariBrowsingAssistantWorker

> `/System/Library/ExtensionKit/Extensions/SafariBrowsingAssistantWorker.appex/SafariBrowsingAssistantWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1821501079</string>
	<key>application-identifier</key>
	<string>com.apple.parsec.SafariBrowsingAssistantWorker</string>
	<key>com.apple.developer.networking.multipath_extended</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>SafariBrowsingAssistantUploader</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Safari.Browsing.Assistant</string>
			</array>
		</dict>
		<key>com.apple.aiml.unilog.healthTelemetry</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.HealthTelemetry</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.parsecd</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.parsecd</string>
	</array>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.siri.osprey</string>
	</array>
</dict>
</plist>

```
### SearchToolDiagnosticExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolDiagnosticExtension.appex/SearchToolDiagnosticExtension`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>application-identifier</key>
+	<string>com.apple.omniSearch.SearchToolDiagnosticExtension</string>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.omniSearch.SearchToolDiagnosticExtension</string>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/tmp/</string>
+	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.internal.xctestinternalangel.sessions</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.OmniSearch</string>
+	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/.com.apple.omniSearch.SearchToolDiagnosticExtension/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.internal.xctestinternalangel.sessions</string>
 	</array>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 </dict>
 </plist>
 

```
### SearchToolExtension

> `/System/Library/ExtensionKit/Extensions/SearchToolExtension.appex/SearchToolExtension`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
+		<string>com.apple.MobileAsset.UAF.Siri.AnswerSynthesis</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>
 		<string>photos.person</string>

 	<array>
 		<string>group.com.apple.siri.referenceResolution</string>
 	</array>
+	<key>com.apple.private.security.storage.IntelligencePlatform</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_AnswerSynthesis/purpose_auto/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>

 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_SpotlightResources/</string>
+		<string>/private/var/mobile/Library/WebClips/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/Library/Containers/com.apple.managedcorespotlightd/EnabledIndexes</string>
 		<string>/Library/Trial/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/DuetExpertCenter/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Shortcuts/</string>
 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>

 		<string>com.apple.siriknowledged</string>
 		<string>com.apple.siriknowledged.vocabulary.admin</string>
 		<string>com.apple.diagnosticpipeline.service</string>
+		<string>com.apple.proactive.appDirectory</string>
+		<string>com.apple.proactive.PersonalizationPortrait.Contact</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>AGXCommandQueue</string>
 		<string>AGXDevice</string>
 		<string>H11ANEInDirectPathClient</string>
+		<string>RootDomainUserClient</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

 		<string>com.apple.UnifiedAssetFramework</string>
 		<string>com.apple.modelcatalog.ajax</string>
 	</array>
+	<key>com.apple.shortcuts.stepwise-execution</key>
+	<true/>
+	<key>com.apple.shortcuts.variable-injection</key>
+	<true/>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 	<key>com.apple.siri.pommes_search_xpc_service</key>
 	<true/>
 	<key>com.apple.siri.vocabulary.admin</key>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>UAF_AB_ANSWER_SYNTHESIS</string>
 		<string>SEARCH_TOOL_ANSWER_SYNTHESIS</string>
 		<string>337</string>
 		<string>755</string>

```

### 🆕 SearchUploadWorker

> `/System/Library/ExtensionKit/Extensions/SearchUploadWorker.appex/SearchUploadWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1821501079</string>
	<key>application-identifier</key>
	<string>com.apple.unilog.SearchUploadWorker</string>
	<key>com.apple.developer.networking.multipath_extended</key>
	<true/>
	<key>com.apple.internal.intelligenceplatform.use-cases</key>
	<dict>
		<key>UnilogMailSearchProcessed</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Unilog.MailSearch.Processed</string>
			</array>
		</dict>
		<key>com.apple.aiml.unilog.healthTelemetry</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Unilog.HealthTelemetry</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Unilog.MailSearch.Processed</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.siri.osprey</string>
	</array>
</dict>
</plist>

```

### 🆕 SignificantChangeAckExtension

> `/System/Library/ExtensionKit/Extensions/SignificantChangeAckExtension.appex/SignificantChangeAckExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accounts.appleaccount.fullaccess</key>
	<true/>
	<key>com.apple.app-distribution.private</key>
	<true/>
	<key>com.apple.family.ageRange</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.family.ageRange.xpc</string>
		<string>com.apple.managedappdistributiond.xpc</string>
	</array>
	<key>com.apple.security.files.user-selected.read-only</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.family.ageRange.xpc</string>
		<string>com.apple.managedappdistributiond.xpc</string>
	</array>
</dict>
</plist>

```

### 🆕 SiriAUSP

> `/System/Library/ExtensionKit/Extensions/SiriAUSP.appex/SiriAUSP`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.accessibility.AXSpringBoardServerAccess</key>
	<true/>
	<key>com.apple.accessibility.systemvoiceprovider</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>SiriAUSP</string>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.VoiceServices.VoiceResources</string>
		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
	</array>
	<key>com.apple.private.sirittsservice.modify-proxy-assets</key>
	<true/>
	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
	<array>
		<string>kTCCServiceVoiceBanking</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.accessibility.voicebanking</string>
		<string>group.com.apple.SiriTTS</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/tmp/</string>
		<string>/private/var/tmp/</string>
		<string>/private/tmp/</string>
		<string>/tmp</string>
		<string>/private/var/tmp</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
		<string>/Library/Caches/SiriTTS/</string>
		<string>/Library/Logs/SiriTTSService/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.tccd</string>
		<string>com.apple.accessibility.AXSpringBoardServer</string>
		<string>com.apple.accessibility.AXBackBoardServer</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
		<string>com.apple.voicebanking.services</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Accessibility</string>
		<string>com.apple.Accessibility.Assets</string>
		<string>com.apple.accessibility.livespeech</string>
		<string>com.apple.accessibility.voicebanking</string>
		<string>com.apple.SpeakSelection</string>
		<string>com.apple.Accessibility.Assets</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
	<array>
		<string>/tmp/</string>
		<string>/private/tmp/</string>
		<string>/private/var/tmp/</string>
		<string>/tmp</string>
		<string>/private/var/tmp</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Group Containers/group.com.apple.accessibility.voicebanking/</string>
	</array>
	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Accessibility/</string>
		<string>/Library/Group Containers/group.com.apple.SiriTTS/</string>
		<string>/Library/Caches/SiriTTS/</string>
		<string>/Library/Logs/SiriTTSService/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.audio.AudioConverterService</string>
		<string>com.apple.logd</string>
		<string>com.apple.tccd</string>
		<string>com.apple.system.notification_center</string>
		<string>com.apple.audio.AudioComponentRegistrar</string>
		<string>com.apple.audio.AudioUnitServer</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.SiriTTSService.TrialProxy</string>
		<string>com.apple.voicebanking.services</string>
	</array>
	<key>com.apple.security.temporary-exception.process-info</key>
	<true/>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.Accessibility</string>
		<string>com.apple.Accessibility.Assets</string>
		<string>com.apple.accessibility.livespeech</string>
		<string>com.apple.accessibility.voicebanking</string>
		<string>com.apple.SpeakSelection</string>
		<string>com.apple.Accessibility.Assets</string>
	</array>
	<key>com.apple.security.ts.ipc-posix-shm</key>
	<array>
		<string>apple.shm.notification_center</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>406</string>
	</array>
	<key>com.apple.voicebanking.services</key>
	<true/>
</dict>
</plist>

```
### SiriAttentionAndInvocationExtension

> `/System/Library/ExtensionKit/Extensions/SiriAttentionAndInvocationExtension.appex/SiriAttentionAndInvocationExtension`

```diff

 					<key>mode</key>
 					<string>read-write</string>
 				</dict>
+				<key>Siri.VoiceTriggerStatistics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
 			</dict>
 		</dict>
 		<key>MLHostTelemetry</key>

 	<array>
 		<string>/Library/Assistant/AssistantSampled/</string>
 		<string>/Library/Caches/com.apple.feedbacklogger/</string>
+		<string>/Library/VoiceTrigger/nearmiss/audio/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.assistant.multiuser.service</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
 		<string>com.apple.siri.location</string>
+		<string>com.apple.ssr.rpisamplingservice</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.userprofiles</string>
 		<string>com.apple.assistant.multiuser.service</string>
 		<string>com.apple.siri.location</string>
+		<string>com.apple.ssr.rpisamplingservice</string>
 	</array>
 	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.siri.location</key>
 	<true/>
+	<key>com.apple.ssr.rpisamplingservice</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 SiriAutoEvalPlugin

> `/System/Library/ExtensionKit/Extensions/SiriAutoEvalPlugin.appex/SiriAutoEvalPlugin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.priml.PFLMLHostPlugins.SiriAutoEvalPlugin</string>
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
	<key>com.apple.priml.allowed-server-model-bundles</key>
	<dict>
		<key>com.apple.fm.language.instruct_server_v1.autograder</key>
		<array/>
	</dict>
	<key>com.apple.priml.pfl.Morpheus.allowed</key>
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
		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
		<string>GenerativeExperiences.PromptTags</string>
		<string>Siri.SELFProcessedEvent</string>
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
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>MLHostTelemetry</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Lighthouse.Ledger.TaskCustomEvent</string>
			</array>
		</dict>
		<key>SiriAutoEvalPlugin</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>IntelligenceFlow.Transcript.Datastream</string>
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

### 🆕 SiriInferenceRuntimeDiagnostics

> `/System/Library/ExtensionKit/Extensions/SiriInferenceRuntimeDiagnostics.appex/SiriInferenceRuntimeDiagnostics`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.application-identifier</key>
	<string>com.apple.siri.inference.SiriInference.SiriInferenceRuntimeDiagnostics</string>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>App.Intents.Transcript</string>
		<string>IntelligenceEngine.Interaction.Donation</string>
		<string>Siri.Remembers.MessageHistory</string>
		<string>Siri.Remembers.CallHistory</string>
		<string>Siri.Remembers.AudioHistory</string>
		<string>App.Intent</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>com.apple.siri.inference.SiriInferenceRuntimeDiagnostics</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>App.Intents.Transcript</string>
				<string>IntelligenceEngine.Interaction.Donation</string>
				<string>Siri.Remembers.MessageHistory</string>
				<string>Siri.Remembers.CallHistory</string>
				<string>Siri.Remembers.AudioHistory</string>
				<string>App.Intent</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Application Support</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
</dict>
</plist>

```

### 🆕 SiriPhoneAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/SiriPhoneAppIntentsExtension.appex/SiriPhoneAppIntentsExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.appintents-attribution-override</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
</dict>
</plist>

```

### 🆕 SiriUploadWorker

> `/System/Library/ExtensionKit/Extensions/SiriUploadWorker.appex/SiriUploadWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>abs-client</key>
	<string>1821501079</string>
	<key>application-identifier</key>
	<string>com.apple.unilog.SiriUploadWorker</string>
	<key>com.apple.developer.networking.multipath_extended</key>
	<true/>
	<key>com.apple.internal.intelligenceplatform.use-cases</key>
	<dict>
		<key>UnilogSiriProcessed</key>
		<dict>
			<key>Streams</key>
			<array>
				<string>Unilog.Siri.Processed</string>
			</array>
		</dict>
	</dict>
	<key>com.apple.private.biome.read-only</key>
	<array>
		<string>Unilog.Siri.Processed</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.siri.osprey</string>
	</array>
</dict>
</plist>

```

### 🆕 SiriVideoAppIntents

> `/System/Library/ExtensionKit/Extensions/SiriVideoAppIntents.appex/SiriVideoAppIntents`

- No entitlements *(yet)*
### SubscribePageExtension

> `/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.cdp.recoverykey</key>

 	<key>com.apple.private.storekit</key>
 	<array>
 		<string>AdvancedPurchase</string>
+		<string>RemoteDownloadIdentifiers</string>
+		<string>Articles</string>
 	</array>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>

```
### TGOnDeviceInferenceProviderService

> `/System/Library/ExtensionKit/Extensions/TGOnDeviceInferenceProviderService.appex/TGOnDeviceInferenceProviderService`

```diff

 	<string>com.apple.tgondeviceinferenceproviderservice</string>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
+		<string>TokenGeneration.Inference.Requests</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
 		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
 		<string>GenerativeExperiences.TransparencyLog</string>

```
### TVAppExtension

> `/System/Library/ExtensionKit/Extensions/TVAppExtension.appex/TVAppExtension`

```diff

 	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>
 	<true/>
-	<key>com.apple.locationd.effective_bundle</key>
-	<true/>
 	<key>com.apple.locationd.prompt_behavior</key>
 	<true/>
 	<key>com.apple.payment.all-access</key>

```
### TextThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/TextThumbnailExtension.appex/TextThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.runningboard</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 UnilogTelemetryWorker

> `/System/Library/ExtensionKit/Extensions/UnilogTelemetryWorker.appex/UnilogTelemetryWorker`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.aiml.UnilogTelemetryWorker</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>com.apple.aiml.unilog.healthTelemetry</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Device.Metadata</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
				<key>Unilog.HealthAggregatedSummary</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>Unilog.HealthTelemetry</key>
				<dict>
					<key>mode</key>
					<string>read-only</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.security.app-sandbox</key>
	<true/>
</dict>
</plist>

```

### 🆕 VideosUIEngagementExtension

> `/System/Library/ExtensionKit/Extensions/VideosUIEngagementExtension.appex/VideosUIEngagementExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.tv</string>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.appstored</key>
	<array>
		<string>Library</string>
	</array>
	<key>com.apple.private.security.restricted-application-groups</key>
	<array>
		<string>group.com.apple.tv.sharedcontainer</string>
		<string>group.tvappservices.container</string>
	</array>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.tvappservices.container</string>
		<string>group.com.apple.sports</string>
		<string>group.com.apple.tv.sharedcontainer</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.tv.engagement</string>
	</array>
</dict>
</plist>

```
### com.apple.WebKit.WebContent.CaptivePortal

> `/System/Library/ExtensionKit/Extensions/WebContentCaptivePortalExtension.appex/com.apple.WebKit.WebContent.CaptivePortal`

```diff

 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>
 		<string>com.apple.WebKit.showLegacyFlexReasons</string>
+		<string>com.apple.WebKit.showLegacyGridReasons</string>
 		<string>com.apple.WebKit.showMemoryCache</string>
 		<string>com.apple.WebKit.showPaintOrderTree</string>
 		<string>com.apple.WebKit.showRenderTree</string>

 	</array>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
+	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>
+	<integer>1</integer>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### com.apple.WebKit.WebContent.EnhancedSecurity

> `/System/Library/ExtensionKit/Extensions/WebContentEnhancedSecurityExtension.appex/com.apple.WebKit.WebContent.EnhancedSecurity`

```diff

 	<true/>
 	<key>com.apple.developer.coremedia.allow-alternate-video-decoder-selection</key>
 	<true/>
+	<key>com.apple.developer.gpu-restricted</key>
+	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
 	<key>com.apple.developer.kernel.extended-virtual-addressing</key>
 	<true/>
 	<key>com.apple.developer.web-browser-engine.restrict.notifyd</key>
 	<true/>
+	<key>com.apple.developer.web-browser-engine.webcontent</key>
+	<true/>
 	<key>com.apple.mediaremote.set-playback-state</key>
 	<true/>
 	<key>com.apple.pac.shared_region_id</key>

 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>
 		<string>com.apple.WebKit.showLegacyFlexReasons</string>
+		<string>com.apple.WebKit.showLegacyGridReasons</string>
 		<string>com.apple.WebKit.showMemoryCache</string>
 		<string>com.apple.WebKit.showPaintOrderTree</string>
 		<string>com.apple.WebKit.showRenderTree</string>

 	</array>
 	<key>com.apple.private.disable-log-mach-ports</key>
 	<true/>
+	<key>com.apple.private.extensionkit.host-requirement-exemption</key>
+	<true/>
 	<key>com.apple.private.memorystatus</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 		<string>WebProcessDidNotInjectStoreBundle</string>
 		<string>BlockUserInstalledFonts</string>
 	</array>
+	<key>com.apple.private.web-browser-engine.webcontent</key>
+	<true/>
 	<key>com.apple.private.webinspector.allow-remote-inspection</key>
 	<true/>
 	<key>com.apple.private.webinspector.proxy-application</key>

 	</array>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
+	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>
+	<integer>1</integer>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### com.apple.WebKit.WebContent

> `/System/Library/ExtensionKit/Extensions/WebContentExtension.appex/com.apple.WebKit.WebContent`

```diff

 		<string>com.apple.WebKit.showLayerTree</string>
 		<string>com.apple.WebKit.showLayoutTree</string>
 		<string>com.apple.WebKit.showLegacyFlexReasons</string>
+		<string>com.apple.WebKit.showLegacyGridReasons</string>
 		<string>com.apple.WebKit.showMemoryCache</string>
 		<string>com.apple.WebKit.showPaintOrderTree</string>
 		<string>com.apple.WebKit.showRenderTree</string>

 	</array>
 	<key>com.apple.security.hardened-process.containment.ipc</key>
 	<true/>
+	<key>com.apple.security.hardened-process.containment.vm.cow-defeatured</key>
+	<integer>1</integer>
 	<key>com.apple.sqlite.defensive</key>
 	<integer>1</integer>
 </dict>

```
### WebThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/WebThumbnailExtension.appex/WebThumbnailExtension`

```diff

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.runningboard</string>
+		<string>com.apple.WebKit.WebContent.EnhancedSecurity</string>
 	</array>
 </dict>
 </plist>

```
### iWorkThumbnailExtension

> `/System/Library/ExtensionKit/Extensions/iWorkThumbnailExtension.appex/iWorkThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.runningboard</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### apfs_checkdigest

> `/System/Library/Filesystems/apfs.fs/apfs_checkdigest`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.lock-container-load</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.lock-container-load</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```

### 🆕 apfs_computedigest

> `/System/Library/Filesystems/apfs.fs/apfs_computedigest`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.apfs.sep.ramdisk</key>
	<true/>
	<key>com.apple.container.crypto.io</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.keystore.devicebackup</key>
	<true/>
	<key>com.apple.private.apfs.create-sealed-snapshot</key>
	<true/>
	<key>com.apple.private.apfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.apfs.lock-container-load</key>
	<true/>
	<key>com.apple.private.apfs.revert-to-snapshot</key>
	<true/>
	<key>com.apple.private.iopol.case_sensitivity</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.security.system-async-io</key>
	<true/>
	<key>com.apple.private.vfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.vfs.move-data-extents</key>
	<true/>
	<key>com.apple.private.vfs.snapshot</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>AppleAPFSUserClient</string>
</dict>
</plist>

```
### apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

 	<true/>
 	<key>com.apple.private.apfs.omm.ctl</key>
 	<true/>
-	<key>com.apple.private.apfs.purgeable.extents</key>
-	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.security.disk-device-access</key>

```
### apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.lock-container-load</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.lock-container-load</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.lock-container-load</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### fsck_apfs

> `/System/Library/Filesystems/apfs_userfs.fs/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.lock-container-load</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### accountsd

> `/System/Library/Frameworks/Accounts.framework/accountsd`

```diff

 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
+	<key>com.apple.private.keychain.allow-delete-internal-on-sign-out</key>
+	<true/>
 	<key>com.apple.private.lockdown.finegrained-get</key>
 	<array>
 		<string>NULL/DevicePrivateKey</string>

 		<string>com.apple.asd.scoring</string>
 		<string>com.apple.aa.ageMigration.xpc</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```
### assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

```diff

 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.assetsd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>PhotosIDCard</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Photos.Extracted.IDCard</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.link.donate-dynamicterms-as</key>

 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.cache_delete.public</string>
 	</array>
-	<key>com.apple.security.temporary-exception.shared-preference.read-only</key>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.communicationSafetySettings</string>
+		<string>com.apple.suggestions</string>
 	</array>
 	<key>com.apple.siri.koa.donate.internal</key>
 	<true/>

```
### AudioConverterHardenedService

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AudioConverterHardenedService.xpc/AudioConverterHardenedService`

```diff

 	<key>com.apple.private.memory.ownership_transfer</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
-	<string>autobox</string>
+	<string>AudioConverterService</string>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Preferences/com.apple.coreaudio.plist</string>

```
### ContactsCoreSpotlightExtension

> `/System/Library/Frameworks/Contacts.framework/PlugIns/ContactsCoreSpotlightExtension.appex/ContactsCoreSpotlightExtension`

```diff

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### contactsd

> `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

 	<array>
 		<string>com.apple.TelephonyUtilities</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-call-providers</string>

```
### CoreSpotlightTestImporter

> `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTestImporter.appex/CoreSpotlightTestImporter`

```diff

 	<string>com.apple.CoreSpotlight.TestImporter</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### CoreSpotlightTextImporter

> `/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTextImporter.appex/CoreSpotlightTextImporter`

```diff

 	<string>com.apple.CoreSpotlight.TextImporter</string>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

 	<true/>
 	<key>com.apple.mobileassetd.v2</key>
 	<true/>
+	<key>com.apple.private.CacheDelete</key>
+	<array>
+		<string>CLIENT_ENTITLEMENT</string>
+	</array>
 	<key>com.apple.private.ciphermld.allow</key>
 	<true/>
 	<key>com.apple.private.corespotlight.allownotifications</key>

 				</dict>
 			</dict>
 		</dict>
+		<key>PowerHUD</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Spotlight.Operations</key>
+				<string>read-write</string>
+			</dict>
+		</dict>
 	</dict>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>
 	<array>

 	<array>
 		<string>com.apple.spotlightknowledged</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.spotlight.entitledattributes</key>
 	<true/>
 	<key>com.apple.tailspin.dump-output</key>

```
### CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

 		<string>kTCCServiceAddressBook</string>
 		<string>kTCCServiceFaceID</string>
 	</array>
+	<key>com.apple.private.translation</key>
+	<true/>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.tipsd</string>

 	<array>
 		<string>/private/var/Managed Preferences/mobile/com.apple.commcenter.managed.plist</string>
 		<string>/usr/local/bin/</string>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/private/var/db/MobileIdentityData/LaunchWarning.db</string>
+		<string>/private/var/db/MobileIdentityData/LaunchWarning.db-wal</string>
+		<string>/private/var/db/MobileIdentityData/LaunchWarning.db-shm</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

```
### CommCenterMobileHelper

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenterMobileHelper`

```diff

 		<string>Library/HTTPStorages</string>
 		<string>Library/HTTPStorages/com.apple.commcentermobilehelper/</string>
 		<string>Library/Preferences/com.apple.lasd.plist</string>
+		<string>Library/Preferences/com.apple.commcenter.shared.plist</string>
 		<string>Library/CallHistoryDB/</string>
 		<string>Library/LASD/</string>
 		<string>Library/Logs/CrashReporter/</string>

 		<string>com.apple.softwareupdateservicesd</string>
 		<string>com.apple.Bridge</string>
 		<string>com.apple.bridgecarriersettings</string>
-		<string>com.apple.system.prefs</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### FamilyControlsAgent

> `/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screen-time</key>
+	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDM.plist</string>
 		<string>/private/var/preferences/com.apple.networkd.plist</string>
 	</array>

```
### fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

 		<string>NOTIFICATION_ENTITLEMENT</string>
 		<string>ITEMIZED_PURGEABLE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.CoreAuthentication.SPI</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.CallerName</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.unrestrictedPersona</key>

```
### healthd

> `/System/Library/Frameworks/HealthKit.framework/healthd`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.health.RemoteHeartRateStreamService</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.SetStoreUpdateService</string>

 		<string>com.apple.Mobility.notifications</string>
 		<string>com.apple.FitnessCoaching</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.siri.external_request</key>
 	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>

```
### com.apple.imageimporter

> `/System/Library/Frameworks/ImageIO.framework/PlugIns/com.apple.imageimporter.appex/com.apple.imageimporter`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.private.corespotlight.bundleid</key>
+	<string>com.apple.CoreSpotlight.ImportExtension</string>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+</dict>
+</plist>
 

```
### coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

 	<true/>
 	<key>com.apple.keystore.device.verify</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
+	<key>com.apple.networkrelay.deviceMonitor</key>
+	<true/>
+	<key>com.apple.networkrelay.devices.read</key>
+	<true/>
 	<key>com.apple.private.CoreRepairCore.repairInfo</key>
 	<true/>
 	<key>com.apple.private.LocalAuthentication.LaunchAngel</key>

 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
-		<string>com.apple.CoreAuthUI</string>
 		<string>com.apple.LocalAuthenticationUIService</string>
 	</array>
 	<key>com.apple.runningboard.process-state</key>

 		<string>com.apple.CoreRepairCoreXPCService</string>
 		<string>com.apple.LocalAuthenticationUIService.authentication-methods</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.terminusd</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>kCFPreferencesAnyApplication</string>
 		<string>com.apple.coreauthd</string>
 	</array>
+	<key>com.apple.security.network.client</key>
+	<true/>
 	<key>com.apple.security.ts.ipc-posix-sem</key>
 	<string>purplebuddy.sentinel</string>
 	<key>com.apple.security.ts.nvram-read</key>

```
### applicensedeliveryd

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/applicensedeliveryd`

```diff

 	<array>
 		<string>com.apple.managedappdistributiond.xpc</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.applicensedelivery</string>

```
### managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.keystore.absinthe</key>
+	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.get</key>

 	<true/>
 	<key>com.apple.private.marketplace-extension-host</key>
 	<true/>
+	<key>com.apple.private.mobileinstall.allowedSPI</key>
+	<array>
+		<string>CheckCapabilitiesMatch</string>
+	</array>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.nsurlsession.impersonate</key>

 		<string>com.apple.managedappdistributiond</string>
 		<string>com.apple.appstored</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>com_apple_driver_FairPlayIOKitUserClient</string>

```
### PDFImporter

> `/System/Library/Frameworks/PDFKit.framework/PlugIns/PDFImporter.appex/PDFImporter`

```diff

 	<string>com.apple.CoreSpotlight.ImportExtension</string>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### PassKitSpotlightIndexExtension

> `/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitSpotlightIndexExtension.appex/PassKitSpotlightIndexExtension`

```diff

 	</dict>
 	<key>com.apple.private.corespotlight.bundleid</key>
 	<string>com.apple.Passbook</string>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### PassKitThumbnailExtension

> `/System/Library/Frameworks/PassKit.framework/PlugIns/PassKitThumbnailExtension.appex/PassKitThumbnailExtension`

```diff

 	<array>
 		<string>com.apple.trustd</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### PassKitWrapperXPCServiceUI

> `/System/Library/Frameworks/PassKit.framework/XPCServices/PassKitWrapperXPCServiceUI.xpc/PassKitWrapperXPCServiceUI`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
-		<string>Library/Caches/com.apple.PassKitWrapperXPCServiceUI/</string>
+		<string>/Library/Caches/PassKit/</string>
+		<string>/Library/Caches/com.apple.PassKitWrapperXPCServiceUI/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.UIKit</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXDeviceUserClient</string>

```
### com.apple.quicklook.ThumbnailsAgent

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent`

```diff

 	<array>
 		<string>com.apple.CoreGraphics.CGPDFService</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

 		<string>com.apple.TrustedPeersHelper</string>
 		<string>com.apple.security</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>

```
### shazamd

> `/System/Library/Frameworks/ShazamKit.framework/shazamd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>

 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.tcc.manager.access.modify</key>
+	<array>
+		<string>kTCCServiceLiverpool</string>
+	</array>
 	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
 	<array>
 		<string>kTCCServiceMicrophone</string>

 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

 		<string>com.apple.MobileAsset.UAF.Siri.UnderstandingAsrHammer</string>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+		<string>com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>

 	</array>
 	<key>com.apple.uservault</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.icl</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

 	<string>com.apple.storekit</string>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
 	<key>com.apple.symptom_analytics.query</key>

```
### TelephonyTransferService

> `/System/Library/Frameworks/TelephonyMessagingKit.framework/XPCServices/TelephonyTransferService.xpc/TelephonyTransferService`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.runningboard.assertions.TelephonyTransferService</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/var/containers/Bundle/Application/</string>
+		<string>/private/var/db/MobileIdentityData/LaunchWarning.db</string>
+		<string>/private/var/db/MobileIdentityData/LaunchWarning.db-wal</string>
+		<string>/private/var/db/MobileIdentityData/LaunchWarning.db-shm</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.TelephonyBlastDoorService</string>

```
### translationd

> `/System/Library/Frameworks/Translation.framework/translationd`

```diff

 	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.VoiceServicesVocalizerVoice</string>

 		<string>com.apple.MobileAsset.SpeechTranslationAssets5</string>
 		<string>com.apple.MobileAsset.SpeechTranslationAssets6</string>
 		<string>com.apple.MobileAsset.SpeechTranslationAssets7</string>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Translation.Assets</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>

 	<array>
 		<string>group.com.apple.private.translation</string>
 	</array>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.speech.synthesis.custom.voices.allow</key>
 	<true/>
 	<key>com.apple.security.application-groups</key>

 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.modelmanager</string>
+		<string>com.apple.spotlight.IndexAgent</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.coremedia</string>
 		<string>com.apple.assistant.support</string>
 		<string>com.apple.UnifiedAssetFramework</string>
+		<string>kCFPreferencesAnyApplication</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

 	<string>com.apple.wirelessinsightsd</string>
 	<key>com.apple.basebandd.xpc.allow</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
+	<key>com.apple.frontboardservices.display-layout-monitor</key>
+	<true/>
 	<key>com.apple.geoservices.navigation_info</key>
 	<true/>
 	<key>com.apple.geoservices.restricted-tiles</key>

 	<array>
 		<string>/private/var/wireless/wirelessinsightsd/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Caches/com.apple.wirelessinsightsd/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.private.corewifi-xpc</string>

 	<key>com.apple.trial.client</key>
 	<array>
 		<string>862</string>
+		<string>WIRELESS_DATA_ANALYTICS_SATELLITE_CLASSIFIER</string>
+		<string>WIRELESS_DATA_ANALYTICS_ML_ATD</string>
+		<string>WIRELESS_DATA_ANALYTICS_WIFI_TO_CELL_WALKOUT_PREDICTOR</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```

### 🆕 AppleMagicKeyboardSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/AppleMagicKeyboardSessionFilter.plugin/AppleMagicKeyboardSessionFilter`

- No entitlements *(yet)*

### 🆕 MedicationsHealthAppPluginBundle

> `/System/Library/Health/FeedItemPlugins/MedicationsHealthAppPluginBundle.healthplugin/MedicationsHealthAppPluginBundle`

- No entitlements *(yet)*

### 🆕 HealthDaemonControlsPlugin

> `/System/Library/Health/Plugins/HealthDaemonControlsPlugin.bundle/HealthDaemonControlsPlugin`

- No entitlements *(yet)*

### 🆕 HealthOntologyDaemonPluginBundle

> `/System/Library/Health/Plugins/HealthOntologyDaemonPluginBundle.bundle/HealthOntologyDaemonPluginBundle`

- No entitlements *(yet)*

### 🆕 HealthRecordsPluginBundle

> `/System/Library/Health/Plugins/HealthRecordsPluginBundle.bundle/HealthRecordsPluginBundle`

- No entitlements *(yet)*

### 🆕 MatterAccessoriesSettings

> `/System/Library/PreferenceBundles/MatterAccessoriesSettings.bundle/MatterAccessoriesSettings`

- No entitlements *(yet)*

### 🆕 MetalHUDDeveloperSettings

> `/System/Library/PreferenceBundles/MetalHUDDeveloperSettings.bundle/MetalHUDDeveloperSettings`

- No entitlements *(yet)*
### activityawardsd

> `/System/Library/PrivateFrameworks/ActivityAwardsServices.framework/activityawardsd`

```diff

 		<string>com.apple.ActivitySharing</string>
 		<string>com.apple.nanolifestyle</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.ts.nano-preference.read-only</key>
 	<array>
 		<string>.GlobalPreferences</string>

```
### AppIntentsRunnerXPCService

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/XPCServices/AppIntentsRunnerXPCService.xpc/AppIntentsRunnerXPCService`

```diff

 <plist version="1.0">
 <dict>
 	<key>application-identifier</key>
-	<string>com.apple.AppIntentsServices.Runner</string>
+	<string>com.apple.testmanagerd.appintentsservices</string>
 	<key>com.apple.appintents.assistantaccess</key>
 	<true/>
 	<key>com.apple.appprotectiond.guard.access</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
+	<key>com.apple.intelligenceflow.uiContext</key>
+	<true/>
 	<key>com.apple.linkd.registry</key>
 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.no-container</key>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.frontboard.systemappservices</string>
+		<string>com.apple.intelligenceflow.uiContext</string>
 		<string>com.apple.linkd.extension</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.linkd.registry</string>

```
### appstorecomponentsd

> `/System/Library/PrivateFrameworks/AppStoreComponents.framework/Support/appstorecomponentsd`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.jetpackassetd</key>
+	<true/>
 	<key>com.apple.private.logging.diagnostic</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	<array>
 		<string>/Library/Application Support/CrashReporter/DiagnosticMessagesHistory.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.extension</string>
+		<string>com.apple.jetpackassetd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

```
### ASDFollowUpExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDFollowUpExtension.appex/ASDFollowUpExtension`

```diff

 	<array>
 		<string>com.apple.corefollowup.agent</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 </dict>
 </plist>
 

```
### ASDUserNotificationExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDUserNotificationExtension.appex/ASDUserNotificationExtension`

```diff

 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 		<string>/Library/UserNotifications/</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

 	<string>9824938448</string>
 	<key>com.apple.attributionkitd.token-handoff</key>
 	<true/>
+	<key>com.apple.authentication-services-core.allow-querying-credential-providers</key>
+	<true/>
 	<key>com.apple.authkit.authorization-bundle-identifier-proxy</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 		<string>com.apple.apsd</string>
 		<string>com.apple.askpermissiond</string>
 		<string>com.apple.ak.authorizationservices.xpc</string>
+		<string>com.apple.AuthenticationServicesCore.AuthenticationServicesAgent</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>

 		<string>com.apple.imessage.bag</string>
 		<string>com.apple.AppStore</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 	<key>com.apple.security.system-container</key>
 	<true/>
 	<key>com.apple.security.system-groups</key>

```
### CustodianInviteMessageExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/CustodianInviteMessageExtension.appex/CustodianInviteMessageExtension`

```diff

 		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.security.octagon</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### LegacyContactMessageExtention

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/LegacyContactMessageExtention.appex/LegacyContactMessageExtention`

```diff

 		<string>com.apple.hsa-authentication-server</string>
 		<string>com.apple.security.octagon</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.springboard.activateRemoteAlert</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### AppleDeviceQueryService

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/XPCServices/AppleDeviceQueryService.xpc/AppleDeviceQueryService`

```diff

 	<true/>
 	<key>com.apple.private.security.bootpolicy</key>
 	<true/>
+	<key>com.apple.private.set-exception-port</key>
+	<true/>
 	<key>com.apple.private.xpc.domain-extension</key>
 	<true/>
 	<key>com.apple.security.exception.iokit-user-client-class</key>

```

### 🆕 AppleIntelligenceReportingProcessingService

> `/System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/XPCServices/AppleIntelligenceReportingProcessingService.xpc/AppleIntelligenceReportingProcessingService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>AssetDelivery.UAF.DailyStatus</string>
	</array>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>com.apple.AppleIntelligence.Reporting.AssetBringUp</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AssetDelivery.UAF.DailyStatus</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.AppleIntelligence.Reporting.AssetDeliveryLog</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.Availability</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.MobileAsset</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.MobileAssetVerbose</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.ModelCatalog</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.SoftwareUpdateController</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.UnifiedAssetFramework</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.AppleIntelligence.Reporting.Buddy</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.Buddy</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.AppleIntelligence.Reporting.Invocation.Step</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.Invocation.Step</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>com.apple.AppleIntelligence.Reporting.ModelIO</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.ModelIO</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.xpc.domain-extension</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
		<string>/private/var/MobileAsset/AssetsV2/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.siri.uaf.subscription.service</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.appleintelligencereporting</string>
		<string>com.apple.appleintelligencereporting.processing</string>
	</array>
	<key>com.apple.security.temporary-exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
		<string>/System/Library/AssetsV2/</string>
	</array>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.siri.analytics.assistant</string>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.TapToRadarKit.service</string>
	</array>
	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.appleintelligencereporting</string>
		<string>com.apple.appleintelligencereporting.processing</string>
	</array>
</dict>
</plist>

```
### askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond`

```diff

 	<true/>
 	<key>com.apple.private.appstored</key>
 	<array>
-		<string>Library</string>
 		<string>Install</string>
+		<string>Library</string>
 	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>

 	<true/>
 	<key>com.apple.private.screen-time</key>
 	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceFaceID</string>

 	<array>
 		<string>com.apple.askpermission.notifications</string>
 	</array>
+	<key>com.apple.runningboard.screentimeunlock</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/tmp/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>com.apple.xpc.amsaccountsd</string>
-		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.AskPermissionUI</string>
+		<string>com.apple.ScreenTimeAgent.exception</string>
+		<string>com.apple.appstored.xpc.request</string>
+		<string>com.apple.asktod</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biome.compute.source</string>
-		<string>com.apple.people.agent</string>
 		<string>com.apple.familycircle.agent</string>
-		<string>com.apple.ScreenTimeAgent.exception</string>
-		<string>com.apple.asktod</string>
-		<string>com.apple.appstored.xpc.request</string>
-		<string>com.apple.managedappdistributiond.xpc</string>
-		<string>com.apple.lsd.xpc</string>
 		<string>com.apple.lsd.open</string>
+		<string>com.apple.lsd.xpc</string>
+		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.people.agent</string>
+		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>

```
### assistant_service

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistant_service`

```diff

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.corespeech.corespeechd.xpc</key>
+	<true/>
 	<key>com.apple.developer.carp</key>
 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>

 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
+	<key>com.apple.intelligentrouting.recommendationservice</key>
+	<true/>
 	<key>com.apple.intents.extension.discovery</key>
 	<true/>
 	<key>com.apple.intents.intents-helper</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
+		<string>com.apple.intelligentroutingd.xpc.media</string>
 		<string>com.apple.siri.orchestration.configuration</string>
 		<string>com.apple.intelligenceflow.uiContext</string>
 		<string>com.apple.intelligenceflow.context</string>

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.fitnessintelligenced</string>
+		<string>com.apple.siri.audio_message_service.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.intelligentroutingd.xpc.media</string>
+	</array>
 	<key>com.apple.seserviced.key</key>
 	<true/>
 	<key>com.apple.seserviced.kmlXpcService</key>

 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
+		<string>access-call-providers</string>
 		<string>access-calls</string>
 		<string>modify-calls</string>
 		<string>access-call-capabilities</string>

```
### assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allows-set-output-device</key>
 	<true/>
+	<key>com.apple.backboardd.eventAuthenticationKey</key>
+	<true/>
+	<key>com.apple.backboardd.setAuthenticatedTouches</key>
+	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.bulletinboard.dataprovider</key>

 	</array>
 	<key>com.apple.intelligenceflow.querydecoration</key>
 	<true/>
+	<key>com.apple.intelligenceflow.toolbox</key>
+	<true/>
 	<key>com.apple.intelligenceflow.transcript-entity-querying</key>
 	<true/>
 	<key>com.apple.intelligenceflow.transcript-entity-querying.query-all-groups</key>

 		<string>Siri.OnDeviceAnalytics.SpeakerIdSampling</string>
 		<string>Siri.PostSiriEngagement</string>
 		<string>Siri.SELFProcessedEvent</string>
+		<string>Siri.SELFProcessedRemote</string>
 		<string>Siri.VoiceTriggerStatistics</string>
 		<string>SiriPrivateLearningSELFEvent</string>
 	</array>

 				</dict>
 			</dict>
 		</dict>
+		<key>SpeechDatasetSampling</key>
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
+				<key>App.Intents.ExtractedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
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
+				<key>HomeKit.Home</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>HomeKit.HomeServiceArea</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Location.SignificantLocation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>MediaLibrary.Media</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Podcasts.Podcast</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Siri.PrivateLearning.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Siri.PrivateLearning.Media</key>
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
 		<key>com.apple.AppleIntelligence.Reporting.AssetDeliveryLog</key>
 		<dict>
 			<key>Streams</key>

 	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
+	<key>com.apple.private.sessionkit.listener</key>
+	<true/>
 	<key>com.apple.private.siri-morphunassetsupdaterd</key>
 	<true/>
 	<key>com.apple.private.sirittsservice.impersonate-clients</key>

 		<string>kTCCServiceSiri</string>
 		<string>kTCCServiceSpeechRecognition</string>
 	</array>
+	<key>com.apple.private.tipsd.assistant</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.crossdevicearbitration.feedback.notification</string>

 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.avfoundation.allow-system-wide-context</string>
 		<string>com.apple.awdd</string>
+		<string>com.apple.backboard.hid-services.xpc</string>
 		<string>com.apple.backboard.hid.services</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.biome.access.user</string>

 		<string>com.apple.corespeech.speechmodeltraining.xpc</string>
 		<string>com.apple.corespeech.voicetriggerservice</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.fairplayd</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.familycircle.agent</string>
 		<string>com.apple.feedbacklogger</string>
 		<string>com.apple.FileCoordination</string>
+		<string>com.apple.fpsd</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.generativeexperiences.availability.internal</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>

 		<string>com.apple.intelligenceflow.context</string>
 		<string>com.apple.intelligenceflow.orchestrator</string>
 		<string>com.apple.intelligenceflow.querydecoration</string>
+		<string>com.apple.intelligenceflow.toolbox</string>
 		<string>com.apple.intelligenceflow.transcript-entity-querying</string>
 		<string>com.apple.intelligenceflow.uiContext</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>

 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.itunescloudd.xpc</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.linkd.autoShortcut</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.locationd.registration</string>
 		<string>com.apple.locationd.synchronous</string>
 		<string>com.apple.managedappdistributiond.xpc</string>
+		<string>com.apple.Maps.xpc.connectionBroker.endpointRecorder</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.mediaremoted.xpc</string>

 		<string>com.apple.PairingManager</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.passd.library</string>
+		<string>com.apple.perceptiond.sceneClassification</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.powerlog.plxpclogger.xpc</string>

 		<string>com.apple.routined.registration</string>
 		<string>com.apple.SBUserNotification</string>
 		<string>com.apple.securityd.systemkeychain</string>
+		<string>com.apple.sensornetd.transport</string>
 		<string>com.apple.server.bluetooth</string>
 		<string>com.apple.server.bluetooth.le.att.xpc</string>
+		<string>com.apple.sessionservices</string>
 		<string>com.apple.shazamd.ui</string>
 		<string>com.apple.siri.activation</string>
 		<string>com.apple.siri.activation.application</string>

 		<string>com.apple.siri.audio_message_service.xpc</string>
 		<string>com.apple.siri.client_lite</string>
 		<string>com.apple.siri.context.service</string>
+		<string>com.apple.siri.deviceselection</string>
+		<string>com.apple.siri.deviceselectiond</string>
 		<string>com.apple.siri.execution_service</string>
 		<string>com.apple.siri.external_request</string>
 		<string>com.apple.siri.localspeechrecognitionbridge.xpc</string>
+		<string>com.apple.siri.location</string>
 		<string>com.apple.siri.morphunassetsupdaterd</string>
 		<string>com.apple.siri.reference_resolution_module</string>
 		<string>com.apple.siri.shared_flow_plugin_service</string>

 		<string>com.apple.timesync.expositor</string>
 		<string>com.apple.timesync.manager</string>
 		<string>com.apple.timesync.ptp.manager</string>
+		<string>com.apple.tipsd.assistant</string>
 		<string>com.apple.trial.status</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.usernotifications.listener</string>

 		<string>com.apple.HeadGestures</string>
 		<string>com.apple.homed</string>
 		<string>com.apple.homed.notbackedup</string>
+		<string>com.apple.intelligenceflow</string>
 		<string>com.apple.itunescloud</string>
 		<string>com.apple.itunescloud.internal</string>
 		<string>com.apple.keyboard.preferences</string>

 		<string>com.apple.pommes</string>
 		<string>com.apple.preferences.sounds</string>
 		<string>com.apple.raisetospeak</string>
+		<string>com.apple.rapport</string>
 		<string>com.apple.siri.analytics.assistant</string>
 		<string>com.apple.siri.cdm</string>
 		<string>com.apple.siri.crossdevicearbitration</string>
+		<string>com.apple.siri.deviceselection</string>
 		<string>com.apple.siri.DialogEngine</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.siri.morphun</string>

 	<true/>
 	<key>com.apple.siri.client_lite</key>
 	<true/>
+	<key>com.apple.siri.deviceselection.allow</key>
+	<true/>
 	<key>com.apple.siri.embeddedspeech</key>
 	<true/>
 	<key>com.apple.siri.execution_service</key>

 	<true/>
 	<key>com.apple.siri.flow-extension-discovery</key>
 	<true/>
+	<key>com.apple.siri.location</key>
+	<true/>
 	<key>com.apple.siri.opportune_speaking_model_service</key>
 	<true/>
 	<key>com.apple.siri.siriaudio-helper</key>

 		<string>SIRI_REFERENCE_RESOLUTION_LIGHTHOUSE_PLUGIN_FOR_SHADOW_LOGGING</string>
 		<string>SIRI_SELF_REFLECTION_ASK_REPEAT</string>
 		<string>SIRI_SELF_REFLECTION_TAP_TO_EDIT</string>
+		<string>SIRI_SPEECH_DATASET_SAMPLING</string>
 		<string>SIRI_SPEECH_SV_SPEECH_PROFILE</string>
 		<string>SIRI_SUGGESTIONS_DOMAIN_GROUP_A</string>
 		<string>SIRI_SUGGESTIONS_DOMAIN_GROUP_B</string>

```
### AudioAccessoryAssetManagementXPCService

> `/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/XPCServices/AudioAccessoryAssetManagementXPCService.xpc/AudioAccessoryAssetManagementXPCService`

```diff

 	<array>
 		<string>com.apple.toolbox.indexing-service</string>
 		<string>com.apple.translationd</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.SetStoreUpdateService</string>
+	</array>
+	<key>com.apple.security.exception.syscall-mach.machtrap-number</key>
+	<array>
+		<string>MCS_semaphore_siganl_trap</string>
 	</array>
 	<key>com.apple.shortcuts.background-running</key>
 	<true/>

```
### akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

 		<string>com.apple.appstorecomponentsd.xpc</string>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.managedconfiguration.mdmdservice</string>
+		<string>com.apple.AuthenticationServices.AuthenticationServicesAgent.CredentialUpdate</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

 	</dict>
 	<key>com.apple.private.MobileContainerManager.userManagedAssets</key>
 	<true/>
-	<key>com.apple.private.apfs.get_free_queue_info</key>
-	<true/>
 	<key>com.apple.private.apfs.set_purgeable_notification_threshold</key>
 	<true/>
 	<key>com.apple.private.apfs.space-attribution</key>

```
### calaccessd

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/Support/calaccessd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.mobilecal</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	<array>
 		<string>group.com.apple.calendar</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.linkd.application-service</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>RootDomainUserClient</string>

```
### CallHistorySyncHelper

> `/System/Library/PrivateFrameworks/CallHistory.framework/Support/CallHistorySyncHelper`

```diff

 	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.calls.PhoneAppIntentsExtension</string>
+	</array>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.aps-environment</key>

 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.corerecents.recentsd</string>
+		<string>com.apple.linkd.application-service</string>
 	</array>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>

```
### SetStoreUpdateService

> `/System/Library/PrivateFrameworks/CascadeSets.framework/XPCServices/SetStoreUpdateService.xpc/SetStoreUpdateService`

```diff

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-write</key>
-	<array>
-		<string>/private/var/mobile/tmp/com.apple.biomesyncd/</string>
-	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.cascade.SetChangeRelayService</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
-		<string>com.apple.biome.compute.source.user</string>
-		<string>com.apple.biome.compute.source</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
-	<key>com.apple.security.ts.mobile-keybag-access</key>
-	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.SetStoreUpdateService</string>
 	<key>platform-application</key>

```
### chronod

> `/System/Library/PrivateFrameworks/ChronoCore.framework/Support/chronod`

```diff

 	</array>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.DeviceAccess.private</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.QuartzCore.secure-mode</key>

 	<true/>
 	<key>com.apple.private.security.storage.chronod</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.sessionkit.listener</key>
 	<true/>
 	<key>com.apple.private.sessionkit.sessionFinisher</key>

 		<string>/AppleInternal/Applications/</string>
 		<string>/private/var/containers/Bundle/Application/</string>
 		<string>/private/var/mobile/Library/SpringBoard/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
+		<string>com.apple.DeviceAccess.xpc</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### com.apple.Photos.CPLDiagnose

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/XPCServices/com.apple.Photos.CPLDiagnose.xpc/com.apple.Photos.CPLDiagnose`

```diff

 		<string>com.apple.accountsd.accountmanager</string>
 		<string>com.apple.cache_delete.public</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

```diff

 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.kvsd</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.sbd</string>

```

### 🆕 CSDetectionService

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/XPCServices/CSDetectionService.xpc/CSDetectionService`

- No entitlements *(yet)*
### assistant_cdmd

> `/System/Library/PrivateFrameworks/ContinuousDialogManagerService.framework/assistant_cdmd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.assistant_cdmd</string>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>

 	<true/>
 	<key>com.apple.private.e5rt.sharing-e5-bundles-allowed</key>
 	<true/>
+	<key>com.apple.private.familycircle</key>
+	<true/>
 	<key>com.apple.private.imcore.spi.database-access</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
 	<key>com.apple.private.suggestions.contacts</key>

 		<string>/private/var/mobile/Library/Trial/</string>
 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### CDPProximityPairingService

> `/System/Library/PrivateFrameworks/CoreCDP.framework/XPCServices/CDPProximityPairingService.xpc/CDPProximityPairingService`

```diff

 	<true/>
 	<key>com.apple.cdp.statemachine</key>
 	<true/>
+	<key>com.apple.keystore.lockassertion</key>
+	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.octagon</key>

```
### contextstored

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/Resources/contextstored`

```diff

 		<string>com.apple.rapport.people</string>
 		<string>com.apple.private.corewifi.readonly-xpc</string>
 		<string>com.apple.milod.xpc.service</string>
+		<string>com.apple.perceptiond.entitykit</string>
+		<string>com.apple.perceptiond.physicalContext</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```

### 🆕 SpeechAudioDiagnostic

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/PlugIns/SpeechAudioDiagnostic.appex/SpeechAudioDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/Assistant/TTRAudio/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Logs/CrashReporter/Assistant/TTRAudio/</string>
	</array>
</dict>
</plist>

```

### 🆕 SpeechProfileDiagnostic

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/PlugIns/SpeechProfileDiagnostic.appex/SpeechProfileDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.private.security.storage.SiriVocabulary</key>
	<true/>
	<key>com.apple.private.userprofiles.read</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Assistant/SiriVocabulary/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.uservault</string>
	</array>
	<key>com.apple.uservault</key>
	<true/>
</dict>
</plist>

```

### 🆕 TTRAssistantSpeechAudioDiagnostic

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/PlugIns/TTRAssistantSpeechAudioDiagnostic.appex/TTRAssistantSpeechAudioDiagnostic`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Logs/Assistant/TTRAudio/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Logs/CrashReporter/Assistant/TTRAudio/</string>
	</array>
</dict>
</plist>

```

### 🆕 speechmaintenanced

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/speechmaintenanced`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.speechmaintenanced</string>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrAssistant</string>
		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
	</array>
	<key>com.apple.private.assets.bypass-asset-types-check</key>
	<true/>
	<key>com.apple.private.biome.read-write</key>
	<array>
		<string>IntelligenceFlow.JointResolverTelemetry</string>
	</array>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.speechmaintenanced</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>ASRAppEntityRanking</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>App.Intents.IndexedEntity</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>entitySimilarityFeatures</string>
		<string>defaultResolverInteractions</string>
		<string>personEntityRelevanceRanking</string>
		<string>personEntityLongTermRanking</string>
		<string>loiEntityRelevanceRanking</string>
		<string>appEntityRelevanceRanking</string>
		<string>visualIdentifier</string>
	</array>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.storage.triald</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Biome/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.speechmaintenanced/</string>
		<string>/Library/Assistant/SpeechMaintenance/</string>
		<string>/Library/ASRAssetOverrides/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.SetStoreUpdateService</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.speech.localspeechrecognition</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.siri.analytics.assistant</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.assistant.backedup</string>
		<string>com.apple.assistant</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<array>
		<string>com.apple.speech.localspeechrecognition</string>
		<string>SpeechModelCache</string>
	</array>
	<key>com.apple.trial.client</key>
	<array>
		<string>1441</string>
		<string>1760</string>
		<string>INTELLIGENCE_FLOW_PLAN_RESOLUTION</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### parsecd

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd`

```diff

 	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.networkserviceproxy</key>
 	<true/>
 	<key>com.apple.private.power.notifications</key>

```
### com.apple.CoreSVG.thumbnail

> `/System/Library/PrivateFrameworks/CoreSVG.framework/PlugIns/com.apple.CoreSVG.thumbnail.appex/com.apple.CoreSVG.thumbnail`

```diff

 	<true/>
 	<key>com.apple.security.files.user-selected.read-only</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

 	<true/>
 	<key>com.apple.intelligenceflow.context</key>
 	<true/>
+	<key>com.apple.intelligenceflow.contextTool</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
 	<key>com.apple.locationd.activity</key>

 	<string>com.apple.corespeechd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>EuclidProfile</key>
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
+				<key>App.Intents.ExtractedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
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
+				<key>HomeKit.Home</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>HomeKit.HomeServiceArea</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Location.SignificantLocation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>MediaLibrary.Media</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Podcasts.Podcast</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Siri.PrivateLearning.Contact</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+				<key>Siri.PrivateLearning.Media</key>
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
+			<key>Streams</key>
+			<dict>
+				<key>CarPlay.Connected</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>PeopleSuggesterContactPriors</key>
 		<dict>
 			<key>Sets</key>

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/dev/exfiltration-adc-corespeechd</string>
+		<string>/tmp/SiriMessages/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.intelligenceflow.context</string>
 		<string>com.apple.intelligenceflow.querydecoration</string>
+		<string>com.apple.intelligenceflow.contextTool</string>
 		<string>com.apple.assistant.domain.validation.service</string>
 		<string>com.apple.assistant.domain.system.settings.service</string>
 		<string>com.apple.feedbacklogger</string>

 		<string>757</string>
 		<string>1701</string>
 		<string>1441</string>
+		<string>SIRI_SPEECH_DATASET_SAMPLING</string>
 	</array>
 	<key>com.apple.trial.status.namespace-name.allow</key>
 	<array>

```
### suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

 		<string>/Library/Mail/AttachmentData/</string>
 		<string>/Library/UserNotifications/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/SearchManager/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fpsd</string>
 		<string>com.apple.financed.service.financestore</string>
 		<string>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</string>
 		<string>com.apple.generativeexperiences.summarization</string>

 		<string>com.apple.donotdisturb.service.non-launching</string>
 		<string>com.apple.ciphermld</string>
 		<string>com.apple.usernotifications.usernotificationsettingsservice</string>
+		<string>com.apple.mediaanalysisd.service.public</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.generativesearch</string>
 		<string>com.apple.gms.availability</string>
 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.SiriViewService</string>

```
### dataaccessd

> `/System/Library/PrivateFrameworks/DataAccess.framework/Support/dataaccessd`

```diff

 	<array>
 		<string>CloudKit</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.mobile.keybagd.UserManager.logout</key>

```
### com.apple.migrationpluginwrapper

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.migrationpluginwrapper.xpc/com.apple.migrationpluginwrapper`

```diff

 	<true/>
 	<key>com.apple.private.LocalAuthentication.DTO</key>
 	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage</key>
+	<true/>
+	<key>com.apple.private.LocalAuthentication.Storage.BiometricLivenessFlag</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
 	<key>com.apple.private.Safari.History</key>

 		<string>LookupSystemAppState</string>
 		<string>UpdateSystemAppState</string>
 		<string>SetSystemAppMigrationComplete</string>
+		<string>StoreListOfAppsRequiringPreInstallConsent</string>
+		<string>FetchListOfAppsRequiringPreInstallConsent</string>
 	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>

```
### ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>ArchiveService</string>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.desktopservices.ArchiveService.AppGroupContainer</string>
+	</array>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.desktopservices.ArchiveService.AppGroupContainer</string>
+	</array>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.aea.cli</string>

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

### 🆕 CoreSensingDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/CoreSensingDiagnosticExtension.appex/CoreSensingDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/tmp/com.apple.AccessorySensorManager/</string>
	</array>
</dict>
</plist>

```
### IMDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/IMDiagnosticExtension.appex/IMDiagnosticExtension`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imdpersistence.database-access</key>
 	<true/>
+	<key>com.apple.security.app-sandbox</key>
+	<true/>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.IMCoreSpotlight</string>

```
### MiLoDiagnostic

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/MiLoDiagnostic.appex/MiLoDiagnostic`

```diff

 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Logs/milod/miloexport/</string>
+		<string>/Library/Logs/milod/visualloggerexport/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```
### ToolKitDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ToolKitDiagnosticExtension.appex/ToolKitDiagnosticExtension`

```diff

 	<array>
 		<string>/Library/Shortcuts/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.toolkitd.xpc</string>
+	</array>
 	<key>com.apple.toolkit.request-reindex.allow</key>
 	<true/>
 </dict>

```
### diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

 	<true/>
 	<key>com.apple.diskimages.creator-uc</key>
 	<true/>
+	<key>com.apple.private.amber.client</key>
+	<true/>
 	<key>com.apple.private.amfi.version-restriction</key>
 	<integer>2</integer>
 	<key>com.apple.private.apfs.no-padding</key>

```
### maild

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/maild`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.mobilemail</string>
+		<string>com.apple.mail</string>
+	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.duetactivityscheduler</string>

```
### facetimemessagestored

> `/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/facetimemessagestored`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.calls.PhoneAppIntentsExtension</string>
+	</array>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.suggestd.contacts</string>
 		<string>com.apple.corerecents.recentsd</string>
+		<string>com.apple.linkd.application-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### familycircled

> `/System/Library/PrivateFrameworks/FamilyCircle.framework/familycircled`

```diff

 	<array>
 		<string>com.apple.appleaccount</string>
 		<string>com.apple.familycircled</string>
+		<string>com.apple.FamilyCircle</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### generativeexperiencesd

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/generativeexperiencesd`

```diff

 	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.appleintelligencereporting.processing</key>
+	<true/>
 	<key>com.apple.appstored.install-system-apps</key>
 	<true/>
 	<key>com.apple.assistant.settings</key>

 		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.timed.xpc</string>
 		<string>com.apple.securityd</string>
+		<string>com.apple.appleintelligencereporting.processing</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 healtheventsd

> `/System/Library/PrivateFrameworks/HealthEventsDaemonImplementation.framework/healtheventsd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.healtheventsd</string>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Caches/com.apple.healtheventsd/</string>
	</array>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.healtheventsd</string>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.healtheventsd</string>
		<string>com.apple.Health</string>
	</array>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

 	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
-		<string>com.apple.MobileAsset.Health</string>
+		<string>com.apple.MobileAsset.VideoIntelligence</string>
 	</array>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>

 		<key>value</key>
 		<string>com.apple.Health</string>
 	</dict>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.Events</string>
+		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>
+		<string>GenerativeModels.GenerativeFunctions.SystemInstrumentation</string>
+		<string>AppleIntelligence.Reporting.Invocation.Step</string>
+	</array>
 	<key>com.apple.private.contacts</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 	</array>
 	<key>com.apple.private.followup</key>
 	<true/>
+	<key>com.apple.private.healthcontentd</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.authorization_bypass</key>

 		<string>cloud-participant</string>
 		<string>context-sync</string>
 	</array>
+	<key>com.apple.private.healthrecordsd</key>
+	<true/>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>HealthDonation</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>Health.CategorySample</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Health.Characteristics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Health.Classification</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+				<key>Health.Statistics</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.security.storage.Health</key>
 	<true/>
 	<key>com.apple.private.sleepd</key>

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VideoIntelligence/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.healthcontentd</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.backboard.hid.services</string>

 		<string>com.apple.sleepd.sleepserver</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.private.health.HearingTest</string>
 		<string>com.apple.private.health.mental-health</string>
 		<string>com.apple.private.health.health-actions</string>
-		<string>com.apple.private.health.HealthReport</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.biome.access.user</string>
+	</array>
 	<key>com.apple.security.ts.geoservices</key>
 	<true/>
 	<key>com.apple.security.ts.mobile-keybag-access</key>

```
### homeenergyd

> `/System/Library/PrivateFrameworks/HomeEnergyDaemon.framework/Support/homeenergyd`

```diff

 	</array>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.homeenergyd</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.homeenergy.utilityonboarding</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### homed

> `/System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed`

```diff

 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
+	<key>com.apple.DiagnosticExtensions.extensionHost</key>
+	<true/>
 	<key>com.apple.MFAAuthentication</key>
 	<array>
 		<string>token-auth</string>

 	<array>
 		<string>com.apple.DriverKit-AppleBCMWLAN</string>
 	</array>
+	<key>com.apple.developer.energykit</key>
+	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	<true/>
 	<key>com.apple.keystore.info</key>
 	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.place_inference</key>

 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
+	<key>com.apple.nfcd.session.reader.internal</key>
+	<true/>
 	<key>com.apple.osintelligence.inactivity</key>
 	<true/>
 	<key>com.apple.passes.add-silently</key>

 	<true/>
 	<key>com.apple.payment.all-access</key>
 	<true/>
+	<key>com.apple.private.AppleMediaServices</key>
+	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
+		<string>com.apple.private.alloy.homepod.topcap</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.ids.messaging.high-priority</key>

 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
+		<string>com.apple.private.alloy.homepod.topcap</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.ids.remotecredentials</key>

 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
+		<string>com.apple.private.alloy.homepod.topcap</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.ids.session</key>

 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
+		<string>com.apple.private.alloy.homepod.topcap</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.ids.session-private</key>

 		<string>com.apple.private.alloy.home</string>
 		<string>com.apple.private.alloy.alarms-timers</string>
 		<string>com.apple.private.alloy.energykit</string>
+		<string>com.apple.private.alloy.homepod.topcap</string>
 		<string>com.apple.private.alloy.home.invite</string>
 	</array>
 	<key>com.apple.private.imcore.imremoteurlconnection</key>

 		<string>com.apple.symptom_analytics</string>
 		<string>com.apple.homecommsd.xpc</string>
 		<string>com.apple.uarp.endpoint.transport</string>
+		<string>com.apple.nfcd.hwmanager</string>
+		<string>com.apple.NetworkInfo.DiagnosticExtension.apple-extension-service</string>
+		<string>com.apple.linkd.transcript</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.Home</string>
 		<string>com.apple.CommunicationTrust</string>
 		<string>com.apple.MobileStoreDemo.test</string>
+		<string>com.apple.bluetooth</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 	<key>com.apple.wlan.authentication</key>
 	<true/>
 	<key>fairplay-client</key>
-	<string>509276493</string>
+	<string>511712240</string>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>

```
### IDSBlastDoorService

> `/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/XPCServices/IDSBlastDoorService.xpc/IDSBlastDoorService`

```diff

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.fileprovider.share</key>
+        <true/>
+	<key>com.apple.private.cloudkit.masquerade</key>
+	<true/>
+	<key>com.apple.private.cloudkit.customAccounts</key>
+	<true/>
 	<key>com.apple.timed</key>
 	<true/>
 	<key>com.apple.trustkit.debug.ui</key>

 	<true/>
 	<key>com.apple.developer.icloud-extended-share-access</key>
 	<array>
+		<string>InProcessOneTimeLinks</string>
 		<string>InProcessShareOwnerParticipantInfo</string>
 	</array>
 	<key>com.apple.private.communicationsfilter</key>

```
### IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.MobileSMS</string>
+	</array>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.*</string>

 		<string>com.apple.compass.cellular-waypoints</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.kvsd</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.contacts.poster.api</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 	<true/>
 	<key>com.apple.spotlight.photos.entitledattributes</key>
 	<true/>
+	<key>com.apple.springboard.CFUserNotification</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

```
### installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.screen-time</key>
+	<true/>
+	<key>com.apple.private.screentime-ask</key>
+	<true/>
+	<key>com.apple.private.screentime-communication</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotos</string>
 	</array>
+	<key>com.apple.runningboard.screentimeunlock</key>
+	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
 	<key>com.apple.security.enterprise-volume-access</key>

 		<string>/private/var/mobile/Library/UserConfigurationProfiles/EffectiveUserSettings.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/mobile/Library/com.apple.FamilyControlsAgent/Authorizations.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<string>/private/var/mobile/Library/com.apple.PrivacyDisclosure/</string>

 		<string>com.apple.accountsd</string>
 		<string>com.apple.MobileInstallationHelperService</string>
 		<string>com.apple.migrationd.install-coordination</string>
+		<string>com.apple.ScreenTimeAgent.ask</string>
+		<string>com.apple.ScreenTimeAgent.communication</string>
+		<string>com.apple.ScreenTimeAgent.private</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### intelligencecontextd

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/intelligencecontextd`

```diff

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.assertiond.system-shell</key>
 	<true/>
+	<key>com.apple.assistant.settings</key>
+	<true/>
 	<key>com.apple.callkit</key>
 	<array>
 		<string>private-controller-api</string>

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.perceptiond.peripheralSensing</key>
+	<true/>
+	<key>com.apple.private.appintents.live-entities.read</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MorphunData</string>

 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 		<string>com.apple.MobileAsset.UAF.Siri.Understanding</string>
 	</array>
+	<key>com.apple.private.assistant.settings</key>
+	<true/>
 	<key>com.apple.private.biome.client-identifier</key>
 	<string>com.apple.intelligenceflow.intelligencecontextd</string>
 	<key>com.apple.private.biome.read-only</key>

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>Context.Tool.Telemetry</string>
 	</array>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.assistant.settings</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.TextInput.rdt</string>
 		<string>com.apple.calaccessd</string>

 		<string>com.apple.CalendarAgent</string>
 		<string>com.apple.callkit.callcontrollerhost</string>
 		<string>com.apple.linkd.extension</string>
+		<string>com.apple.perceptiond.peripheralSensing</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.mediaremote</string>
 		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
 		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.TelephonyUtilities</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

```
### IntelligenceFlowDiagnostics

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlugIns/IntelligenceFlowDiagnostics.appex/IntelligenceFlowDiagnostics`

```diff

 			</array>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.restricted-application-groups</key>
+	<array>
+		<string>group.com.apple.intelligenceflow</string>
+	</array>
 	<key>com.apple.private.security.storage.SiriFeatureStore</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.security.app-sandbox</key>
 	<true/>
+	<key>com.apple.security.application-groups</key>
+	<array>
+		<string>group.com.apple.intelligenceflow</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Shortcuts/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.biome.access.user</string>

```
### intelligenceflowd

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/intelligenceflowd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>Outgoing Network Connections</key>
+	<true/>
 	<key>application-identifier</key>
 	<string>com.apple.intelligenceflow.intelligenceflowd</string>
+	<key>com.apple.Contacts.database-allow</key>
+	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>
 	<true/>
 	<key>com.apple.CoreRoutine.Visit</key>

 	<true/>
 	<key>com.apple.QuartzCore.global-capture</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
+	<key>com.apple.accounts.idms.fullaccess</key>
+	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>
 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.intelligenceflow.intelligenceflowd</string>
+	<key>com.apple.assistant.audio-session-event</key>
+	<true/>
 	<key>com.apple.assistant.cdm.client</key>
 	<true/>
 	<key>com.apple.assistant.dictation.prerecorded</key>
 	<true/>
+	<key>com.apple.authkit.client.private</key>
+	<true/>
 	<key>com.apple.avfoundation.allow-identifying-output-device-details</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<true/>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.callkit</key>
+	<array>
+		<string>private-controller-api</string>
+	</array>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.coreduetd.allow</key>

 	<true/>
 	<key>com.apple.coreduetd.people</key>
 	<true/>
+	<key>com.apple.corespeech.corespeechd.attending.service</key>
+	<true/>
 	<key>com.apple.corespeech.corespeechd.xpc</key>
 	<true/>
 	<key>com.apple.corespotlight.privateindex.unsandboxed</key>

 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>
 	<true/>
+	<key>com.apple.developer.networking.multicast</key>
+	<true/>
 	<key>com.apple.developer.siri</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-write</key>

 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
+	<true/>
 	<key>com.apple.intelligenceflow.context</key>
 	<true/>
+	<key>com.apple.intelligenceflow.contextTool</key>
+	<true/>
+	<key>com.apple.intelligenceflow.orchestrator</key>
+	<true/>
+	<key>com.apple.intelligenceflow.orchestrator.features</key>
+	<array>
+		<string>executable-session</string>
+	</array>
 	<key>com.apple.intelligenceflow.querydecoration</key>
 	<true/>
 	<key>com.apple.intelligenceflow.uiContext</key>

 	<true/>
 	<key>com.apple.pegasus.context</key>
 	<true/>
+	<key>com.apple.perceptiond.access</key>
+	<dict>
+		<key>peripheralsensing</key>
+		<true/>
+	</dict>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>

 	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
+	<key>com.apple.private.application-service-browse</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.MorphunData</string>

 		<string>Sage.Transcript</string>
 		<string>IntelligenceFlow.Transcript.Datastream</string>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.Events</string>
+		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>
 		<string>IntelligenceFlow.ExecutorTelemetry</string>
+		<string>AppleIntelligence.Reporting.Invocation.Step</string>
+	</array>
+	<key>com.apple.private.biome.writer</key>
+	<array>
+		<string>Discoverability.Signals</string>
 	</array>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<true/>
 	<key>com.apple.private.familycircle</key>
 	<true/>
+	<key>com.apple.private.healthkit.medicaliddata</key>
+	<true/>
 	<key>com.apple.private.homekit</key>
 	<true/>
 	<key>com.apple.private.ids.messaging</key>

 	<key>com.apple.private.security.restricted-application-groups</key>
 	<array>
 		<string>group.com.apple.intelligenceflow</string>
+		<string>group.com.apple.siri.inference</string>
 	</array>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriFeatureStore</key>
 	<true/>
+	<key>com.apple.private.security.storage.SiriInference</key>
+	<true/>
 	<key>com.apple.private.security.storage.SiriReferenceResolution</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriVocabulary</key>

 	<array>
 		<string>kTCCServiceAll</string>
 	</array>
+	<key>com.apple.private.tipsd.assistant</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Location.readOnly</key>

 		<string>group.com.apple.intelligenceflow</string>
 		<string>group.is.workflow.my.app</string>
 		<string>group.is.workflow.shortcuts</string>
+		<string>group.com.apple.siri.inference</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>

 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/db/com.apple.countryd/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>

 		<string>/Library/Shortcuts/QuarantineAsset/</string>
 		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/UnifiedAssetFramework</string>
+		<string>/Library/Assistant/RecordedAudio/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/SiriReferenceResolution/</string>
 		<string>/Library/IntelligencePlatform/</string>
 		<string>/Library/IntelligenceFlow/</string>
+		<string>/Library/Application Support/IntelligenceFlow/</string>
 		<string>/Library/Caches/com.apple.intelligenceflow.intelligenceflowd/</string>
 		<string>/Library/IdentityServices/files/</string>
 		<string>/Media/</string>

 		<string>/Library/Logs/com.apple.FeatureStore/</string>
 		<string>/Library/Assistant/SiriVocabulary/</string>
 		<string>/Library/Assistant/PrivateLearning/</string>
+		<string>/Library/com.apple.siri.inference/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.generativeexperiences.generativeexperiencessession</string>
 		<string>com.apple.TextInput.rdt</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.remindd</string>

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
+		<string>com.apple.intelligenceflow.contextTool</string>
 		<string>com.apple.nehelper</string>
 		<string>com.apple.nesessionmanager</string>
 		<string>com.apple.posterboardservices.dataModel</string>

 		<string>com.apple.sessionservices</string>
 		<string>com.apple.sharingd</string>
 		<string>com.apple.shortcuts.view-service</string>
+		<string>com.apple.siri.attendingstates.xpc</string>
 		<string>com.apple.siri.location</string>
 		<string>com.apple.siri.vocabularyupdates</string>
 		<string>com.apple.sirittsd</string>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.intelligenceplatform.View</string>
 		<string>com.apple.intelligenceflow.context</string>
+		<string>com.apple.intelligenceflow.orchestrator</string>
 		<string>com.apple.intelligenceflow.uiContext</string>
 		<string>com.apple.intelligenceflow.querydecoration</string>
 		<string>com.apple.intelligenceplatform.Knosis</string>

 		<string>com.apple.searchd</string>
 		<string>com.apple.omniSearch.search</string>
 		<string>com.apple.omniSearch.answerSynthesis</string>
-		<string>com.apple.siri.flowtools_xpc_service</string>
+		<string>com.apple.siri.orchestration.sirix</string>
 		<string>com.apple.corespeech.corespeechd.xpc</string>
 		<string>com.apple.siri.localspeechrecognitionbridge.xpc</string>
+		<string>com.apple.linkd.autoShortcut</string>
+		<string>com.apple.callkit.callcontrollerhost</string>
+		<string>com.apple.tipsd.assistant</string>
+		<string>com.apple.assistant.audio-session-event</string>
+		<string>com.apple.siri.audio.stream.provider.service.xpc</string>
+		<string>com.apple.siri.audio.stream.consumer.service.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.siri.audio</string>
 		<string>com.apple.intelligenceflow</string>
 		<string>com.apple.humanunderstanding</string>
 		<string>com.apple.siri.shortcuts</string>

 		<string>group.is.workflow.my.app</string>
 		<string>com.apple.siri.PostSiriEngagement</string>
 		<string>com.apple.siri.DialogEngine</string>
+		<string>com.apple.siri.generativeassistantsettings</string>
+		<string>com.apple.generativepartnerservicesettings</string>
+		<string>com.apple.siri</string>
+		<string>com.apple.generativeassistanttools.GenerativeAssistantExtension</string>
+		<string>com.apple.siri.identityprovider</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.network.server</key>
+	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.personal-information.calendars</key>

 	<array>
 		<string>systemgroup.com.apple.configurationprofiles</string>
 	</array>
+	<key>com.apple.security.ts.addressbook</key>
+	<true/>
 	<key>com.apple.security.ts.ane-client</key>
 	<true/>
 	<key>com.apple.security.ts.asset-access</key>

 	<true/>
 	<key>com.apple.siri.VoiceShortcuts.xpc</key>
 	<true/>
-	<key>com.apple.siri.flowtools_xpc_service</key>
-	<true/>
 	<key>com.apple.siri.localspeechrecognitionbridge.xpc</key>
 	<true/>
 	<key>com.apple.siri.location</key>
 	<true/>
+	<key>com.apple.siri.orchestration.sirix</key>
+	<true/>
 	<key>com.apple.siriknowledged.koa.donate.internal</key>
 	<true/>
 	<key>com.apple.spotlight.entitledattributes</key>

 	<true/>
 	<key>com.apple.spotlight.search</key>
 	<true/>
+	<key>com.apple.symptoms.NetworkDiagnostics</key>
+	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
 		<string>1150</string>

 		<string>1180</string>
 		<string>1760</string>
 		<string>INTELLIGENCE_FLOW_QUERY_DECORATOR</string>
+		<string>SIRI_SECURITY_IPI</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### IntelligencePlatformComputeService

> `/System/Library/PrivateFrameworks/IntelligencePlatformCompute.framework/XPCServices/IntelligencePlatformComputeService.xpc/IntelligencePlatformComputeService`

```diff

 	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>
+	<key>com.apple.private.contacts</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<key>com.apple.private.tcc.allow.overridable</key>
 	<array>
 		<string>kTCCServicePhotos</string>
+		<string>kTCCServiceAddressBook</string>
 	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.Location.readOnly</key>
 	<true/>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.accountsd.accountmanager</string>
+		<string>com.apple.contactsd</string>
 		<string>com.apple.biome.compute.source</string>
 		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.calaccessd</string>

```
### intelligencetasksd

> `/System/Library/PrivateFrameworks/IntelligenceTasksEngine.framework/Support/intelligencetasksd`

```diff

 	<string>com.apple.intelligencetasksd</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.intelligencetasksd</string>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.intelligencetasksd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>AppEntityDonation</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.Intents.IndexedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>

```

### 🆕 IntelligentRoutingDaemonLLMService

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/XPCServices/IntelligentRoutingDaemonLLMService.xpc/IntelligentRoutingDaemonLLMService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```
### intentrecommendd

> `/System/Library/PrivateFrameworks/IntentRecommendRuntime.framework/intentrecommendd`

```diff

 	<array>
 		<string>HKWorkoutTypeIdentifier</string>
 	</array>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>IntentRecommendEvent</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.Intents.SuggestedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.restricted-application-groups</key>

```
### lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded`

```diff

 	<true/>
 	<key>com.apple.private.applecredentialmanager.transportrestrictedmode.configurewhilelocked.allow</key>
 	<true/>
-	<key>com.apple.private.followup</key>
-	<true/>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.lockdownmode</string>

 		<string>com.apple.coremedia</string>
 		<string>com.apple.controlcenter</string>
 		<string>kCFPreferencesAnyApplication</string>
-		<string>com.apple.ThreatNotificationUI.FollowUpExtension</string>
 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>

```
### MFAANetwork

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/XPCServices/MFAANetwork.xpc/MFAANetwork`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>FairPlay-Classic-Client</key>
+	<true/>
 	<key>fairplay-client</key>
 	<string>441247889</string>
 </dict>

```
### destinationd

> `/System/Library/PrivateFrameworks/MapsSuggestions.framework/destinationd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<string>kTCCServiceCalendar</string>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
+	<array>
+		<string>com.apple.weather</string>
+	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.Connections</key>
 	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.Location.readOnly</key>

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
+		<string>group.com.apple.weather.internal</string>
 		<string>group.com.apple.Maps</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>/AppleInternal/Library/Preferences/Logging/</string>
 		<string>/Library/Preferences/Logging/</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/mobile/Library/Weather/</string>
+	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Caches/com.apple.Maps.Suggestions/</string>

 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>
+	<key>com.apple.security.exception.shared-preference.read</key>
+	<array>
+		<string>com.apple.weather.internal</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.coremedia</string>

 	<array>
 		<string>/Library/Trial/</string>
 	</array>
+	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
+	<array>
+		<string>/Library/Weather/</string>
+	</array>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.Maps.mapspushd</string>

 		<string>1660</string>
 		<string>MAPS_SUGGESTIONS</string>
 	</array>
+	<key>fairplay-client</key>
+	<string>1445028844</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### mediaanalysisd

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.TextUnderstanding.process</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.TextUnderstanding.process</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### mediaanalysisd-service

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service`

```diff

 	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.TextUnderstanding.process</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.aned.private.ANEAccess.allow</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.TextUnderstanding.process</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MediaAnalysisBlastDoorService

> `/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/XPCServices/MediaAnalysisBlastDoorService.xpc/MediaAnalysisBlastDoorService`

```diff

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

 	<true/>
 	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
 	<true/>
+	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.appintents.live-entities.write</key>
+	<array>
+		<string>nowPlaying.localPausedMedia</string>
+		<string>nowPlaying.localPlayingMedia</string>
+	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.associated-domains</key>

 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.symptom_diagnostics</string>
+		<string>com.apple.appintents.LiveEntityService</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.appprotectiond.read</string>
 		<string>com.apple.linkd.extension</string>

 		<string>com.apple.da</string>
 		<string>com.apple.Accessibility</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleJPEGDriverUserClient</string>

```
### SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

 	<array>
 		<string>com.apple.mobilemail</string>
 	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.mobilemail</string>
+		<string>com.apple.mail</string>
+	</array>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<array>
 		<string>/Library/Mail/</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.linkd.application-service</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
 		<string>com.apple.email.SearchIndexer</string>

```

### 🆕 com.apple.MessageSecurity.MSTimestampXPCService

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/XPCServices/com.apple.MessageSecurity.MSTimestampXPCService.xpc/com.apple.MessageSecurity.MSTimestampXPCService`

- No entitlements *(yet)*
### HubbleBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/HubbleBlastDoorService.xpc/HubbleBlastDoorService`

```diff

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### MessagesAirlockService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesAirlockService.xpc/MessagesAirlockService`

```diff

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### MessagesBlastDoorService

> `/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService`

```diff

 	</array>
 	<key>com.apple.private.security.storage.PassKit</key>
 	<true/>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### MetricMeasurementHelper

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/XPCServices/MetricMeasurementHelper.xpc/MetricMeasurementHelper`

```diff

 	<array>
 		<string>com.apple.sysmond</string>
 		<string>com.apple.FunctionCoverageHelper</string>
+		<string>com.apple.PerfPowerMetricMonitor.xpc</string>
 	</array>
 	<key>com.apple.sysmond.client</key>
 	<true/>

```
### migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

 	<true/>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.USBCEntitlement</key>
+	<true/>
 	<key>com.apple.accessibility.AXSpringBoardServerAccess</key>
 	<true/>
 	<key>com.apple.appprotectiond.read</key>

 	<array>
 		<string>com.apple.accounts.sync.suggestion</string>
 	</array>
+	<key>com.apple.private.usbdevice.setdescription</key>
+	<true/>
 	<key>com.apple.private.voicememod.client</key>
 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>

 	<array>
 		<string>AppleJPEGDriverUserClient</string>
 		<string>AGXDeviceUserClient</string>
+		<string>AppleHPMARM</string>
+		<string>IOUSBDeviceInterfaceUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 com.apple.MobileAsset.DownloadService.Builtin

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/XPCServices/com.apple.MobileAsset.DownloadService.Builtin.xpc/com.apple.MobileAsset.DownloadService.Builtin`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.MobileAsset.DownloadService.Builtin</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>cellular-plan</string>
	</array>
	<key>com.apple.PerfPowerServices.data-donation</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.dsme_access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.mobileactivationd.device-identifiers</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.networkd.allow_bootstrap_cellular_service_request</key>
	<true/>
	<key>com.apple.nsurlsession.private.session-bundle-id</key>
	<string>com.apple.MobileAsset.DownloadService</string>
	<key>com.apple.private.AppleVirtualPlatformHostInfo</key>
	<true/>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>PURGE_ENTITLEMENT</string>
		<string>CLIENT_ENTITLEMENT</string>
		<string>PURGEABLE_ENTITLEMENT</string>
		<string>PURGE_SPECIAL_CASE_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.private.MobileAsset.ManifestStorageService</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>SerialNumber</string>
	</array>
	<key>com.apple.private.STRemoteExtractor.privileged</key>
	<true/>
	<key>com.apple.private.allow-nsurlsession-proxy</key>
	<true/>
	<key>com.apple.private.apfs.get-graft-info</key>
	<true/>
	<key>com.apple.private.aps-connection-initiate</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.MobileAssetBrain</string>
	</array>
	<key>com.apple.private.diskimages.kext.user-client-access</key>
	<true/>
	<key>com.apple.private.exclaves.conclave-host</key>
	<true/>
	<key>com.apple.private.image4.nonce.propose.mobile-asset</key>
	<true/>
	<key>com.apple.private.img4.nonce.cryptex1.asset</key>
	<true/>
	<key>com.apple.private.img4.nonce.pdi</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.mobileasset</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>AppleIntelligenceReporting.AssetDelivery</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.Availability</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.MobileAsset</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>AppleIntelligence.Reporting.AssetDeliveryLog.ModelCatalog</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
				<key>MobileAsset.LifeCycle.InstrumentationEvent</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.iokit.system-nvram-allow</key>
	<true/>
	<key>com.apple.private.kernel.override-cpumon</key>
	<true/>
	<key>com.apple.private.mobileassetd.use-daemon-preference-logic</key>
	<true/>
	<key>com.apple.private.mobileassetd.use-download-dir</key>
	<true/>
	<key>com.apple.private.mobileinboxupdater.xpc</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.networkextension.configuration</key>
	<true/>
	<key>com.apple.private.nsurlsession.impersonate</key>
	<true/>
	<key>com.apple.private.nsurlsession.set-discretionary-override-value</key>
	<true/>
	<key>com.apple.private.nsurlsession.set-task-priority</key>
	<true/>
	<key>com.apple.private.pmap.load-trust-cache</key>
	<array>
		<string>personalized.mobile-asset-brain</string>
	</array>
	<key>com.apple.private.security.AppleImage4.user-client</key>
	<true/>
	<key>com.apple.private.security.bootpolicy.readonly</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
	<true/>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.updatetransparency.client</key>
	<true/>
	<key>com.apple.private.vfs.entitled-reserve-access</key>
	<true/>
	<key>com.apple.private.vfs.exclave-fs-register</key>
	<true/>
	<key>com.apple.private.vfs.graftdmg</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.CarPlayAppBlacklist</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.DeviceCheck</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.DictionaryServices.dictionary2</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.DuetExpertCenterAsset</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.EmbeddedNL</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Font5</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Font6</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.HealthKit.FeatureAvailability</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.HomeKit</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.MXLongFormVideoApps</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.MacinTalkVoiceAssets</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.MailDynamicData</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.PKITrustSupplementals</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.SharingDeviceAssets</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.SiriShortcutsMobileAsset</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.TimeZoneUpdate</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriDialogAssets</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriExperienceCam</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriFindMyConfigurationFiles</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriInferredHelpfulness</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriTextToSpeech</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrAssistant</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrHammer</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAsrUaap</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriUnderstandingAttentionAssets</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNL</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.Trial.Siri.SiriUnderstandingNLOverrides</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.VoiceServices.CombinedVocalizerVoices</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.VoiceServices.CustomVoice</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.VoiceServices.GryphonVoice</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.VoiceServices.VoiceResources</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.VoiceServicesVocalizerVoice</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.VoiceTriggerAssets</key>
	<true/>
	<key>com.apple.rootless.storage.com.apple.MobileAsset.network.networknomicon</key>
	<true/>
	<key>com.apple.rootless.volume.Update</key>
	<true/>
	<key>com.apple.security.attestation.access</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/</string>
		<string>/private/var/run/bootSessionMA.txt</string>
		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
		<string>/private/var/run/MobileAssetCriticalDomainsUpdated.plist</string>
		<string>/private/var/run/MobileAssetSuspendSystemOptionalForSoftwareUpdate.nonce</string>
		<string>/private/var/code_coverage/</string>
		<string>/private/var/run/com.apple.mobileassetd-AutoAsset-DeviceBoot-UUID</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.inboxupdaterd</string>
		<string>com.apple.springboard.blockableservices</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.spaceattributiond</string>
		<string>com.apple.commcenter.coretelephony.xpc</string>
		<string>com.apple.installcoordinationd</string>
		<string>com.apple.remoted</string>
		<string>com.apple.apsd</string>
		<string>com.apple.cache_delete</string>
		<string>com.apple.cache_delete.public</string>
		<string>com.apple.powerlog.plxpclogger.xpc</string>
		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>
		<string>com.apple.biome.access.system</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.local-name</key>
	<array>
		<string>com.apple.springboard.blockableservices</string>
		<string>com.apple.inboxupdaterd</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.commcenter.coretelephony.xpc</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleImage4UserClient</string>
		<string>IOHDIXControllerUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.softwareupdatesso.tokenaccessallowed</key>
	<true/>
	<key>com.apple.spaceattribution.private</key>
	<true/>
	<key>com.apple.symptom_diagnostics.report</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.mobileassetd</string>
		<string>lockdown-identities</string>
		<string>apple</string>
	</array>
	<key>seatbelt-profiles</key>
	<array>
		<string>mobileassetd</string>
	</array>
</dict>
</plist>

```
### backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.fairplayd.xpc</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOAESAcceleratorUserClient</string>

```
### mobiletimerd

> `/System/Library/PrivateFrameworks/MobileTimer.framework/Executables/mobiletimerd`

```diff

 	<true/>
 	<key>com.apple.private.alarmkit.bundleIdentifier</key>
 	<string>com.apple.mobiletimer</string>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
+	<true/>
+	<key>com.apple.private.appintents.live-entities.write</key>
+	<array>
+		<string>clock.alarms</string>
+		<string>clock.stopwatch</string>
+		<string>clock.timers</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>Alarm</string>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.alarmkitservices</string>
+		<string>com.apple.appintents.LiveEntityService</string>
+		<string>com.apple.linkd.application-service</string>
+		<string>com.apple.linkd.registry</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/modelcatalogd`

```diff

 	<array>
 		<string>SIML_ADM_PERSONALIZATION_GP</string>
 		<string>SIML_ADM_PERSONALIZATION</string>
+		<string>UAF_AB_MODELCATALOG</string>
+		<string>SIRI_TTS_AB_PCC</string>
 	</array>
 </dict>
 </plist>

```
### medialibraryd

> `/System/Library/PrivateFrameworks/MusicLibrary.framework/Support/medialibraryd`

```diff

 	<array>
 		<string>UniqueDeviceID</string>
 	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.Music</string>
+	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.internal</key>

 		<string>com.apple.duetactivityscheduler</string>
 		<string>com.apple.userprofiles</string>
 		<string>com.apple.fairplayd.xpc</string>
+		<string>com.apple.linkd.application-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### com.apple.SharePlay.NearbyInvitationsService

> `/System/Library/PrivateFrameworks/NearbySessions.framework/XPCServices/com.apple.SharePlay.NearbyInvitationsService.xpc/com.apple.SharePlay.NearbyInvitationsService`

```diff

 	<array>
 		<string>com.apple.SharePlay.NearbyInvitationsService</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### newsd

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/newsd`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
+	<true/>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```
### OfficeSpotlightImporter

> `/System/Library/PrivateFrameworks/OfficeImport.framework/PlugIns/OfficeSpotlightImporter.appex/OfficeSpotlightImporter`

```diff

 <dict>
 	<key>com.apple.private.corespotlight.bundleid</key>
 	<string>com.apple.CoreSpotlight.ImportExtension</string>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
 </dict>
 </plist>
 

```
### searchtoold

> `/System/Library/PrivateFrameworks/OmniSearch.framework/searchtoold`

```diff

 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
 		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
 		<string>com.apple.MobileAsset.UAF.Sage.IFPlannerOverrides</string>
+		<string>com.apple.MobileAsset.UAF.Siri.AnswerSynthesis</string>
 		<string>com.apple.MobileAsset.Trial.Siri.SiriUnderstandingMorphun</string>
 	</array>
+	<key>com.apple.private.assets.bypass-asset-types-check</key>
+	<true/>
 	<key>com.apple.private.assetsd.xpcstore_restricted.access</key>
 	<array>
 		<string>photos.person</string>
 		<string>photos.face</string>
 	</array>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.omniSearch.searchtoold</string>
 	<key>com.apple.private.biome.read-only</key>
 	<array>
 		<string>AppIntent</string>

 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.Events</string>
+		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>
+		<string>AppleIntelligence.Reporting.Invocation.Step</string>
 	</array>
 	<key>com.apple.private.calendar.allow-suggestions</key>
 	<true/>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.corespotlight.allowcarplayapps</key>
+	<true/>
+	<key>com.apple.private.corespotlight.allownotifications</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.corespotlight.search.internal</key>

 	<array>
 		<string>group.com.apple.siri.referenceResolution</string>
 	</array>
+	<key>com.apple.private.security.storage.IntelligencePlatform</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>

 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_IF_PlannerOverrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_AnswerSynthesis/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
 		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>

 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
 		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_Siri_Understanding/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_SpotlightResources/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/private/var/mobile/Library/IntelligencePlatform/</string>
 		<string>/private/var/mobile/Library/IntelligenceFlow/</string>
 		<string>/private/var/mobile/Library/Assistant/SiriVocabulary/</string>
+		<string>/private/var/mobile/tmp/com.apple.omniSearch.searchtoold/</string>
 		<string>/Library/Shortcuts/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/Assistant/SiriVocabulary/</string>
 		<string>/Library/Containers/com.apple.managedcorespotlightd/EnabledIndexes</string>
 		<string>/Library/Trial/</string>
 		<string>/Library/UnifiedAssetFramework/</string>
+		<string>/Library/com.apple.ManagedSettings/</string>
+		<string>/Library/Spotlight/Resources.update_V3/</string>
+		<string>/Library/Caches/GeoServices/</string>
+		<string>/Library/DuetExpertCenter/</string>
+		<string>/Library/Spotlight/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Shortcuts/</string>
 		<string>/Library/Logs/com.apple.FeatureStore/</string>
+		<string>/Library/Application Support/com.apple.omniSearch.searchtoold/</string>
+		<string>/Library/Caches/com.apple.omniSearch.searchtoold/</string>
+		<string>/Library/Spotlight/CorrectionInputFiles/</string>
+		<string>/Library/Spotlight/parsecResources.plist</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.Maps.xpc.connectionBroker.endpointRecorder</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.photos.service</string>
 		<string>com.apple.photoanalysisd</string>

 		<string>com.apple.dmd.policy</string>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
-		<string>com.apple.mobileassetd.v2</string>
-		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.managedcorespotlightd</string>
 		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.diagnosticpipeline.service</string>

 		<string>com.apple.modelcatalog.ajax</string>
 		<string>com.apple.SpotlightResources.Defaults</string>
 		<string>com.apple.siri.morphun</string>
+		<string>com.apple.assistant.backedup</string>
+		<string>com.apple.assistant.support</string>
+		<string>com.apple.itunescloud</string>
+		<string>com.apple.springboard</string>
+		<string>com.apple.searchd</string>
+		<string>com.apple.pommes</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.tokengeneration</string>
+		<string>com.apple.itunescloud</string>
+		<string>com.apple.searchd</string>
+		<string>com.apple.omniSearch.searchtoold</string>
+		<string>com.apple.spotlightui</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<array>
 		<string>/Library/Shortcuts/</string>
 		<string>/Library/Logs/com.apple.FeatureStore/</string>
+		<string>/Library/Application Support/com.apple.omniSearch.searchtoold/</string>
 	</array>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.email.maild</string>
 		<string>com.apple.parsecd</string>
 		<string>com.apple.modelmanager</string>
+		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.mediaanalysisd.service.public</string>
 		<string>com.apple.searchd</string>
 		<string>com.apple.searchd.background</string>

 	<true/>
 	<key>com.apple.trial.client</key>
 	<array>
+		<string>UAF_AB_ANSWER_SYNTHESIS</string>
 		<string>337</string>
 		<string>755</string>
 	</array>

```
### passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

 	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
-		<string>om.apple.CoreODI</string>
+		<string>com.apple.CoreODI</string>
 	</array>
 	<key>com.apple.security.attestation.access</key>
 	<true/>

```
### peopled

> `/System/Library/PrivateFrameworks/People.framework/peopled`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>adi-client</key>
+	<string>2132707621</string>
 	<key>application-identifier</key>
 	<string>com.apple.peopled</string>
 	<key>com.apple.CallHistory.sync.allow</key>

 	</array>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
+	<key>com.apple.ams.bag</key>
+	<true/>
 	<key>com.apple.appprotectiond.read.access</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 	<true/>
 	<key>com.apple.imagent</key>
 	<true/>
+	<key>com.apple.itunesstored.private</key>
+	<true/>
+	<key>com.apple.keystore.absinthe</key>
+	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.private.CallHistory.read-write</key>
 	<true/>
+	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
+	<array>
+		<string>UniqueDeviceID</string>
+		<string>SerialNumber</string>
+	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
 	<key>com.apple.private.appintents.relevant.custom-identifier-allowed</key>
 	<true/>
+	<key>com.apple.private.applemediaservices</key>
+	<true/>
 	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
 	<dict>
 		<key>type</key>

 		<string>/tmp/com.apple.peopled</string>
 		<string>/Library/CallHistoryDB/</string>
 		<string>/Library/Logs/CallHistory</string>
+		<string>/Library/HTTPStorages/</string>
+		<string>/Library/Caches/com.apple.peopled/</string>
+		<string>/Library/com.apple.AppleMediaServices/PersistedBags/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.icloud.findmydeviced.app-support</string>
 		<string>com.apple.imagent.embedded.auth</string>
+		<string>com.apple.mobile.keybagd.xpc</string>
+		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.ScreenTimeAgent.downtime</string>
 		<string>com.apple.linkd.autoShortcut</string>

 	<string>com.apple.peopled</string>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.store.ams.bag</key>
+	<true/>
+	<key>fairplay-client</key>
+	<string>511712240</string>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### privatecloudcomputed

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/privatecloudcomputed.app/privatecloudcomputed`

```diff

 	<true/>
 	<key>com.apple.private.security.daemon-container</key>
 	<true/>
-	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
-		<string>/private/var/db/com.apple.countryd/</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
+	<key>com.apple.springboard.CFUserNotification</key>
+	<true/>
+	<key>com.apple.springboard.opensensitiveurl</key>
+	<true/>
 	<key>com.apple.transparency.privateCloudCompute</key>
 	<true/>
 </dict>

```

### 🆕 ProductKitService

> `/System/Library/PrivateFrameworks/ProductKitCore.framework/XPCServices/ProductKitService.xpc/ProductKitService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.ProductKitService</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Development</string>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>com.apple.productkit.b389personalization</string>
		<string>com.apple.accessorysetup</string>
		<string>com.apple.accessorysetup-staging</string>
		<string>com.apple.accessorysetup.homekit</string>
		<string>com.apple.accessorysetup.homekit-staging</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
</dict>
</plist>

```

### 🆕 SESDiagnosticExtension

> `/System/Library/PrivateFrameworks/SEService.framework/PlugIns/SESDiagnosticExtension.appex/SESDiagnosticExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.DiagnosticExtensions.extension</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Passes/</string>
		<string>/private/var/mobile/Library/Logs/</string>
		<string>/private/var/mobile/Library/Preferences/</string>
	</array>
</dict>
</plist>

```
### com.apple.Safari.SafeBrowsing.Service

> `/System/Library/PrivateFrameworks/SafariSafeBrowsing.framework/com.apple.Safari.SafeBrowsing.Service`

```diff

 	<array>
 		<string>carrier-space</string>
 	</array>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.security.storage.Safari</key>

```
### ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

 	<true/>
 	<key>com.apple.private.people</key>
 	<true/>
+	<key>com.apple.private.screen-time-settings</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

 		<string>com.apple.fairplayd.versioned</string>
 		<string>com.apple.xpc.amsaccountsd</string>
 		<string>com.apple.xpc.amsengagementd</string>
+		<string>com.apple.ScreenTimeSettingsAgent.private</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 ScreenTimeSettingsAgent

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsFoundation.framework/ScreenTimeSettingsAgent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.ScreenTimeSettingsAgent</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>aps-environment</key>
	<string>development</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Development</string>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.ScreenTimeSettings</key>
		<string>com.apple.ScreenTimeSettings</string>
	</dict>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.familycircle</key>
	<true/>
	<key>com.apple.private.managed-settings.apply</key>
	<true/>
	<key>com.apple.rootless.storage.remotemanagementd</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Application Support/com.apple.remotemanagementd/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.apsd</string>
		<string>com.apple.cloudd</string>
		<string>com.apple.familycircle.agent</string>
		<string>com.apple.ManagedSettingsAgent</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.springboard</string>
		<string>com.apple.ScreenTimeSettingsAgent</string>
		<string>com.apple.CloudKit</string>
	</array>
	<key>seatbelt-profiles</key>
	<array>
		<string>temporary-sandbox</string>
	</array>
</dict>
</plist>

```
### searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>PowerHUD</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Spotlight.Operations</key>
+				<string>read-write</string>
+			</dict>
+		</dict>
+		<key>SpotlightDonationProgressObservability</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>Spotlight.DonationProgress</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>SpotlightEngagementData</key>
 		<dict>
 			<key>Streams</key>

 	<true/>
 	<key>com.apple.private.librarian.container-proxy</key>
 	<true/>
+	<key>com.apple.private.logging.diagnostic</key>
+	<true/>
 	<key>com.apple.private.metadata.exattrs</key>
 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.assistant.cdm</string>
 		<string>com.apple.calaccessd</string>

 	<array>
 		<string>com.apple.DataDeliveryServices</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```
### fitcored

> `/System/Library/PrivateFrameworks/SeymourServices.framework/fitcored`

```diff

 	<true/>
 	<key>com.apple.coremedia.allow-protected-content-playback</key>
 	<true/>
+	<key>com.apple.developer.healthkit.background-delivery</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-identifiers</key>
 	<array>
 		<string>com.apple.seymour</string>

```

### 🆕 SidebarFileDispatcherService

> `/System/Library/PrivateFrameworks/SidebarFileDispatcher.framework/XPCServices/SidebarFileDispatcherService.xpc/SidebarFileDispatcherService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.AppleNVMeEAN.allow</key>
	<true/>
	<key>com.apple.AppleNVMeNamespaceDevice.allow</key>
	<true/>
	<key>com.apple.AppleNVMeSideBar.allow</key>
	<true/>
	<key>com.apple.nvmetunnel.allow</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>ASPUserClient</string>
		<string>AppleNVMeUpdateUC</string>
		<string>AppleNVMeNamespaceUC</string>
	</array>
</dict>
</plist>

```
### siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.siriinferenced</string>
+	<key>com.apple.CallHistory.sync.allow</key>
+	<true/>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>

 	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.siriinferenced</string>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.assistant.settings</key>
 	<true/>
 	<key>com.apple.authkit.client.internal</key>

 	<array>
 		<string>com.apple.SiriTasksEvaluation.SiriTasksEvaluationPlugin</string>
 	</array>
+	<key>com.apple.private.CallHistory.read</key>
+	<true/>
 	<key>com.apple.private.DistributedEvaluation.RecordAccess-com.apple.siriinference-dodml-plugin</key>
 	<true/>
 	<key>com.apple.private.SiriSuggestionsBookkeepingService.xpc</key>

 	<array>
 		<string>group.com.apple.siri.userfeedbacklearning</string>
 	</array>
+	<key>com.apple.private.security.storage.CallHistory</key>
+	<true/>
 	<key>com.apple.private.security.storage.HomeKit</key>
 	<true/>
 	<key>com.apple.private.security.storage.SiriInference</key>

 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/mobile/Library/DuetExpertCenter/UICaches/</string>
+		<string>/private/var/mobile/Library/Logs/CallHistory/</string>
+		<string>/private/var/mobile/Library/CallHistoryDB/</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>com.apple.linkd.transcript</string>
 		<string>com.apple.linkd.registry</string>
 		<string>com.apple.mobileasset.autoasset</string>
+		<string>com.apple.CallHistorySyncHelper</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>1342</string>
 		<string>1343</string>
 		<string>1710</string>
+		<string>SIRI_VIDEO_APP_SELECTION_LP</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### com.apple.SiriTTSService.TrialProxy

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/com.apple.SiriTTSService.TrialProxy`

```diff

 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
-		<string>com.apple.MobileAsset.Trial.Siri.SiriTextToSpeech</string>
 		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 	</array>
 	<key>com.apple.private.assets.bypass-asset-types-check</key>
 	<true/>
-	<key>com.apple.proactive.eventtracker</key>
-	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
-		<string>/private/var/mobile/Library/Trial/</string>
 		<string>/private/var/MobileAsset/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.siri.uaf.service</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
-		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.mobileasset.autoasset</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>

 		<string>com.apple.voiceservices</string>
 		<string>com.apple.gms.availability</string>
 	</array>
-	<key>com.apple.trial.client</key>
-	<array>
-		<string>406</string>
-	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### sirittsd

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/sirittsd`

```diff

 		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.sirittsd</string>
 		<string>com.apple.symptom_diagnostics</string>
-		<string>com.apple.triald.namespace-management</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.modelcatalog.catalog</string>

 		<string>com.apple.voiceservices</string>
 		<string>com.apple.internal.ck</string>
 		<string>com.apple.coremedia</string>
-		<string>com.apple.triald</string>
 		<string>com.apple.siri.audio</string>
 		<string>com.apple.SpeakSelection</string>
 		<string>com.apple.internal.testplatform</string>

 	<string>com.apple.sirittsd</string>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
-	<key>com.apple.trial.client</key>
-	<array>
-		<string>406</string>
-	</array>
 	<key>fairplay-client</key>
 	<string>511712240</string>
 	<key>keychain-access-groups</key>

```
### SiriHeadlessService

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriHeadlessService`

```diff

 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.deviceselection</string>
 		<string>com.apple.biome.PublicStreamAccessService</string>
 		<string>com.apple.biomesyncd.realTimeSession</string>
 		<string>com.apple.coordination.alarms</string>

 	<true/>
 	<key>com.apple.siri.client_lite</key>
 	<true/>
+	<key>com.apple.siri.deviceselection.allow</key>
+	<true/>
 	<key>com.apple.soundboard.system</key>
 	<true/>
 	<key>com.apple.trial.client</key>

```
### sleepd

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/sleepd`

```diff

 		<string>com.apple.Carousel</string>
 		<string>com.apple.springboard</string>
 		<string>com.apple.rootrobot</string>
+		<string>com.apple.health.shared</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.FileProvider</key>
 	<true/>
+	<key>com.apple.rootless.datavault.metadata</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.springboard.backgroundappservices</string>

```
### StatusKitAgent

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent`

```diff

 	</array>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.hardened-process</key>
 	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>

```
### TelephonyBlastDoorService

> `/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/XPCServices/TelephonyBlastDoorService.xpc/TelephonyBlastDoorService`

```diff

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### PhoneIntentHandler

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler`

```diff

 	<array>
 		<string>com.apple.TelephonyUtilities</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### com.apple.FTLivePhotoService

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService`

```diff

 		<string>com.apple.TelephonyUtilities</string>
 		<string>com.apple.facetime.bag</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.lockdownmode.read</key>
 	<true/>
 	<key>com.apple.security.network.client</key>

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
 	<key>com.apple.intelligentrouting.recommendationservice</key>
 	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.messages.nicknames</key>
 	<true/>
+	<key>com.apple.mkb.usersession.info</key>
+	<true/>
 	<key>com.apple.multitasking.termination</key>
 	<true/>
 	<key>com.apple.multitasking.voipassertions</key>

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
+	<key>com.apple.private.appintents.live-entities.write</key>
+	<array>
+		<string>calls.incoming</string>
+		<string>calls.ongoing</string>
+	</array>
 	<key>com.apple.private.aps-client-cert-access</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

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

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/mobile/Library/Trial/</string>
 		<string>/private/var/MobileAsset/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.lsd.modifydb</string>
+		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.appintents.LiveEntityService</string>
+		<string>com.apple.audioanalyticsd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### ThumbnailsBlastDoorService

> `/System/Library/PrivateFrameworks/ThumbnailsBlastDoorSupport.framework/XPCServices/ThumbnailsBlastDoorService.xpc/ThumbnailsBlastDoorService`

```diff

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 UnilogConfigXPCService

> `/System/Library/PrivateFrameworks/UnilogConfig.framework/XPCServices/UnilogConfigXPCService.xpc/UnilogConfigXPCService`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.UAF.UnilogConfig</string>
		<string>com.apple.MobileAsset.MLHostTask</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.mobileasset.autoasset</string>
		<string>com.apple.mobileassetd.v2</string>
		<string>com.apple.siri.uaf.service</string>
		<string>com.apple.siri.uaf.subscription.service</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
		<string>com.apple.mobile.usermanagerd.xpc</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.UnifiedAssetFramework</string>
	</array>
</dict>
</plist>

```
### usernotificationsd

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd`

```diff

 	<string>com.apple.usernotificationsd</string>
 	<key>aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.DeviceAccess</key>
+	<true/>
 	<key>com.apple.DeviceAccess.private</key>
 	<true/>
 	<key>com.apple.UserNotifications.RemoteNotifications.Replicator</key>

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.private.corerecents</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

 		<string>com.apple.DeviceAccess.xpc</string>
 		<string>com.apple.contactsd</string>
 		<string>com.apple.apsd</string>
+		<string>com.apple.FileCoordination</string>
 	</array>
 	<key>com.apple.security.exception.mach-register.global-name</key>
 	<array>

 	<true/>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>nano-preferences-read-write</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### TVProductPageExtension

> `/System/Library/PrivateFrameworks/VideosUI.framework/PlugIns/TVProductPageExtension.appex/TVProductPageExtension`

```diff

 	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>
 	<true/>
-	<key>com.apple.locationd.effective_bundle</key>
-	<true/>
 	<key>com.apple.locationd.prompt_behavior</key>
 	<true/>
 	<key>com.apple.payment.all-access</key>

```
### siriactionsd

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/Support/siriactionsd`

```diff

 	</array>
 	<key>com.apple.security.files.bookmarks.app-scope</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### WalletBlastDoorService

> `/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/XPCServices/WalletBlastDoorService.xpc/WalletBlastDoorService`

```diff

 	<array>
 		<string>blastdoor-post-launch</string>
 	</array>
+	<key>com.apple.security.hardened-process.containment.ipc</key>
+	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```

### 🆕 WeaveReplay

> `/System/Library/PrivateFrameworks/WeaveReplay.framework/WeaveReplay`

- No entitlements *(yet)*
### ShortcutsIntents

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/PlugIns/ShortcutsIntents.appex/ShortcutsIntents`

```diff

 		<string>com.apple.pasteboard.pasted</string>
 		<string>com.apple.posterboardservices.dataModel</string>
 		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.routined.registration</string>

 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.siri.shortcuts</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.springboard</string>
 		<string>group.is.workflow.my.app</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleJPEGDriverUserClient</string>

```
### BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

 	<array>
 		<string>iCloud.is.workflow.my.workflows</string>
 	</array>
+	<key>com.apple.developer.web-browser-engine.host</key>
+	<true/>
 	<key>com.apple.fileprovider.acl-write</key>
 	<true/>
 	<key>com.apple.fileprovider.enumerate</key>

 		<string>Accessibility.VoiceOver</string>
 		<string>Accessibility.WhitePoint</string>
 		<string>Accessibility.Zoom</string>
+		<string>AppleIntelligence.Reporting.SafetyGuardrails</string>
 		<string>Device.Display.AlwaysOn</string>
 		<string>Device.Display.AlwaysOn</string>
 		<string>Device.Display.Appearance</string>

 		<string>com.apple.nesessionmanager</string>
 		<string>com.apple.posterboardservices.dataModel</string>
 		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.remindd</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.sessionservices</string>

 		<string>com.apple.sirittsd</string>
 		<string>com.apple.speech.localspeechrecognition</string>
 		<string>com.apple.translationd</string>
+		<string>com.apple.webprivacyd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.generativepartnerservicesettings</string>
 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.springboard</string>
+		<string>com.apple.springboard</string>
 		<string>com.apple.weather.internal</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleJPEGDriverUserClient</string>

```
### AddShortcutExtension

> `/System/Library/PrivateFrameworks/WorkflowUI.framework/PlugIns/AddShortcutExtension.appex/AddShortcutExtension`

```diff

 		<string>com.apple.mediaexperience.endpoint.xpc</string>
 		<string>com.apple.posterboardservices.dataModel</string>
 		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.proactive.AppPrediction.predictions</string>
 		<string>com.apple.siri.VoiceShortcuts.xpc</string>

```

### 🆕 libos-brain.dylib

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/Frameworks/libos-brain.dylib`

- No entitlements *(yet)*
### bird

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/bird`

```diff

 	<string>serverPreferred</string>
 	<key>com.apple.developer.default-data-protection</key>
 	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
+	<key>com.apple.developer.device-information.user-assigned-device-name</key>
+	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>production</string>
 	<key>com.apple.developer.icloud-extended-share-access</key>

```
### ICQFollowup

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/PlugIns/ICQFollowup.appex/ICQFollowup`

```diff

 	<true/>
 	<key>com.apple.springboard.openurlinbackground</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
 	<key>fairplay-client</key>

```
### itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

 	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.developer.networking.multipath</key>
 	<true/>
+	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
+	<string>com.apple.Music</string>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.homekit.private-spi-access</key>

 	</array>
 	<key>com.apple.private.tcc.manager.get-identity-for-credential</key>
 	<true/>
+	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
+	<array>
+		<string>com.apple.music.concerts</string>
+	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.Music</string>

 		<string>com.apple.appprotectiond.guard</string>
 		<string>com.apple.linkd.mediator</string>
 		<string>com.apple.userprofiles</string>
+		<string>com.apple.kvsd</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```

### 🆕 SiriVideoUIPluginV2

> `/System/Library/Snippets/UIPlugins/SiriVideoUIPluginV2.bundle/SiriVideoUIPluginV2`

- No entitlements *(yet)*
### eapolclient

> `/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient`

```diff

 	<true/>
 	<key>com.apple.private.system-keychain</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```

### 🆕 MXUIBackgroundActivities

> `/System/Library/SystemStatus/Bundles/BackgroundActivities/MXUIBackgroundActivities.bundle/MXUIBackgroundActivities`

- No entitlements *(yet)*

### 🆕 com.apple.askpermission.notifications

> `/System/Library/UserNotifications/Bundles/com.apple.askpermission.notifications.bundle/com.apple.askpermission.notifications`

- No entitlements *(yet)*

### 🆕 AegirProxyApp

> `/private/var/staged_system_apps/AegirProxyApp.app/AegirProxyApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.NanoUniverse.AegirProxyApp</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/System/Library/CoreServices/AegirProxyApp.app/AegirProxyApp</string>
	</dict>
	<key>com.apple.private.data-usage-classification-override</key>
	<string>app</string>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 AegirPoster

> `/private/var/staged_system_apps/AegirProxyApp.app/Extensions/AegirPoster.appex/AegirPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.locationd.prompt_from_background</key>
	<true/>
	<key>com.apple.locationd.slc_configurer</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.NanoUniverse.AegirProxyApp.AegirPoster</string>
	</array>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```
### AppStore

> `/private/var/staged_system_apps/AppStore.app/AppStore`

```diff

 	<true/>
 	<key>com.apple.authkit.client.private</key>
 	<true/>
+	<key>com.apple.bluetooth.system</key>
+	<true/>
 	<key>com.apple.cards.all-access</key>
 	<true/>
 	<key>com.apple.cdp.recoverykey</key>

 	<key>com.apple.private.storekit</key>
 	<array>
 		<string>AdvancedPurchase</string>
+		<string>RemoteDownloadIdentifiers</string>
+		<string>Articles</string>
 	</array>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>

```
### AppleTV

> `/private/var/staged_system_apps/AppleTV.app/AppleTV`

```diff

 	</array>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.asd.client</key>
 	<string>9824938448</string>
 	<key>com.apple.authkit.client.private</key>

 	<true/>
 	<key>com.apple.developer.associated-domains</key>
 	<array/>
+	<key>com.apple.developer.carplay-video</key>
+	<true/>
 	<key>com.apple.developer.group-session</key>
 	<true/>
 	<key>com.apple.developer.networking.multicast</key>

 	<true/>
 	<key>com.apple.launchservices.receivereferrerrurl</key>
 	<true/>
-	<key>com.apple.locationd.effective_bundle</key>
-	<true/>
 	<key>com.apple.locationd.prompt_behavior</key>
 	<true/>
 	<key>com.apple.passes.add-silently</key>

 	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
+		<string>/System/Library/PrivateFrameworks/TVAppServices.framework</string>
 		<string>/System/Library/PrivateFrameworks/VideosUI.framework</string>
 	</array>
 	<key>com.apple.private.applemediaservices</key>

 		<string>com.apple.appstored.xpc.storequeue</string>
 		<string>com.apple.appstoreagent.xpc</string>
 		<string>com.apple.biome.access.user</string>
+		<string>com.apple.CarPlayApp.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

 		<string>com.apple.homesharing</string>
 		<string>com.apple.SocialLayer</string>
 		<string>com.apple.AppStoreComponents</string>
+		<string>com.apple.tv.engagement</string>
 	</array>
 	<key>com.apple.springboard.CFUserNotification</key>
 	<true/>

```
### TVCoreSpotlightExtension

> `/private/var/staged_system_apps/AppleTV.app/PlugIns/TVCoreSpotlightExtension.appex/TVCoreSpotlightExtension`

```diff

+<?xml version="1.0" encoding="UTF-8"?>
+<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
+<plist version="1.0">
+<dict>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+</dict>
+</plist>
 

```
### BooksSpotlightExtension

> `/private/var/staged_system_apps/Books.app/PlugIns/BooksSpotlightExtension.appex/BooksSpotlightExtension`

```diff

 		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.spotlight.SearchAgent</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 </dict>

```
### Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

```diff

 		<string>com.apple.ManagedSettingsAgent.publisher</string>
 		<string>com.apple.seserviced.storage-management-presentation</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.usernotifications.accessorynotifications</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### GreenfieldThumbnailExtension

> `/private/var/staged_system_apps/Bridge.app/PlugIns/GreenfieldThumbnailExtension.appex/GreenfieldThumbnailExtension`

```diff

 		<string>com.apple.nano.nanoregistry.pairunpairobliterate</string>
 		<string>com.apple.nano.nanoregistry</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>container</string>

```
### Contacts

> `/private/var/staged_system_apps/Contacts.app/Contacts`

```diff

 	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
+	<key>com.apple.symptom_diagnostics.report</key>
+	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>
 	<array>
 		<string>access-call-providers</string>

```

### 🆕 EmojiPoster

> `/private/var/staged_system_apps/EmojiPoster.app/EmojiPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.EmojiPoster</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 EmojiPosterExtension

> `/private/var/staged_system_apps/EmojiPoster.app/Extensions/EmojiPosterExtension.appex/EmojiPosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
</dict>
</plist>

```
### Files

> `/private/var/staged_system_apps/Files.app/Files`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.associated-domains</key>
+	<array/>
 	<key>com.apple.developer.icloud-extended-share-access</key>
 	<array>
 		<string>InProcessShareOwnerParticipantInfo</string>

 	<array>
 		<string>ContextualActions</string>
 	</array>
+	<key>com.apple.private.clouddocs.rfa-notification-handling</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corespotlight.bundleid</key>

 	<true/>
 	<key>com.apple.private.storagekitd.statuschange</key>
 	<true/>
+	<key>com.apple.private.swc.system-app</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServicePhotosAdd</string>

```
### Fitness

> `/private/var/staged_system_apps/Fitness.app/Fitness`

```diff

 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>
 	<true/>
+	<key>com.apple.mediaremote.remote-control-discovery</key>
+	<true/>
 	<key>com.apple.mediaremote.set-playback-state</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.fitnessintelligenced</string>
+		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.activityawardsd</string>
 		<string>com.apple.activitysharingd</string>
 		<string>com.apple.AppleMediaServicesUIDynamicService</string>

 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
+	<key>com.apple.springboard.remote-alert</key>
+	<true/>
 	<key>com.apple.springboard.topButtonFrames</key>
 	<true/>
 	<key>com.apple.symptom_analytics.query</key>

```

### 🆕 AppsGen

> `/private/var/staged_system_apps/Freeform.app/Frameworks/AppsGen.framework/AppsGen`

- No entitlements *(yet)*

### 🆕 TSAccessibility

> `/private/var/staged_system_apps/Freeform.app/Frameworks/TSAccessibility.framework/TSAccessibility`

- No entitlements *(yet)*

### 🆕 TSImageGeneration

> `/private/var/staged_system_apps/Freeform.app/Frameworks/TSImageGeneration.framework/TSImageGeneration`

- No entitlements *(yet)*

### 🆕 TSMediaLibrary

> `/private/var/staged_system_apps/Freeform.app/Frameworks/TSMediaLibrary.framework/TSMediaLibrary`

- No entitlements *(yet)*

### 🆕 TSUtility

> `/private/var/staged_system_apps/Freeform.app/Frameworks/TSUtility.framework/TSUtility`

- No entitlements *(yet)*
### Freeform

> `/private/var/staged_system_apps/Freeform.app/Freeform`

```diff

 	</array>
 	<key>com.apple.excludes-extensions</key>
 	<true/>
+	<key>com.apple.feedbackd.remote-evaluation</key>
+	<true/>
 	<key>com.apple.freeform.USD-renderer-remote-UI-entitlement</key>
 	<true/>
 	<key>com.apple.frontboard.debugapplications</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.ind.client</key>
 	<true/>
 	<key>com.apple.private.metadata.exattrs</key>
 	<true/>
+	<key>com.apple.private.network.system-token-fetch</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.security.system-application</key>

 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceLiverpool</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.LinkPresentation.LinkSnapshotGeneratorService</string>
 		<string>com.apple.SharePlay.GroupSessionService</string>
 		<string>com.apple.CloudSharing.SPIHelper-iOS</string>
 		<string>com.apple.ind.xpc</string>
+		<string>com.apple.networkserviceproxy.fetch-token</string>
 		<string>com.apple.spotlight.CSExattrCryptoService</string>
 		<string>com.apple.synapse.DocumentWorkflowsService</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.callprovidermanager</string>
+		<string>com.apple.xpc.amsaccountsd</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

 	</array>
 	<key>fairplay-client</key>
 	<string>511712240</string>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>L6VBL6N964.com.apple.freeform</string>
+		<string>CXZ9PY4T4T.group.com.analytics.shared.teams</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 GradientPosterExtension

> `/private/var/staged_system_apps/GradientPoster.app/Extensions/GradientPosterExtension.appex/GradientPosterExtension`

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

### 🆕 GradientPoster

> `/private/var/staged_system_apps/GradientPoster.app/GradientPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.GradientPoster</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### Health

> `/private/var/staged_system_apps/Health.app/Health`

```diff

 	<array>
 		<string>spi</string>
 	</array>
+	<key>com.apple.CompanionLink</key>
+	<true/>
 	<key>com.apple.Contacts.database-allow</key>
 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.fairplay-streaming</key>
+	<true/>
 	<key>com.apple.developer.healthkit</key>
 	<true/>
 	<key>com.apple.developer.homekit</key>

 	<true/>
 	<key>com.apple.fitcore</key>
 	<true/>
+	<key>com.apple.fitnessintelligenced</key>
+	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.heartratecoordinator.spi.heartrate</key>
+	<true/>
 	<key>com.apple.itunesstored.lookup</key>
 	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
+	<key>com.apple.locationd.cardiohealthdata-read</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.usage_oracle</key>

 	</array>
 	<key>com.apple.media.ringtones.read-only</key>
 	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.nano.nanoresourcegrabber</key>
 	<true/>
+	<key>com.apple.pairedunlock.xpc.authorized</key>
+	<true/>
 	<key>com.apple.passes.add-unsigned</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
+		<string>SerialNumber</string>
 		<string>UniqueDeviceID</string>
 		<string>VasUgeSzVyHdB27g2XpN0g</string>
 		<string>re6Zb+zwFKJNlkQTUeT+/w</string>

 		<string>com.apple.MobileAsset.Health</string>
 		<string>com.apple.MobileAsset.SharingDeviceAssets</string>
 		<string>com.apple.MobileAsset.AudiogramAssets</string>
+		<string>com.apple.MobileAsset.VideoIntelligence</string>
+		<string>com.apple.MobileAsset.UAF.Siri.TextToSpeech</string>
 	</array>
 	<key>com.apple.private.assets.change-daemon-config</key>
 	<true/>

 	<array>
 		<string>com.apple.sleep.sleep-mode</string>
 	</array>
+	<key>com.apple.private.fairplay.FPDI</key>
+	<dict>
+		<key>capabilities</key>
+		<array>
+			<integer>4014732562</integer>
+		</array>
+		<key>client-identifier</key>
+		<string>com.apple.Health</string>
+	</dict>
 	<key>com.apple.private.familycircle</key>
 	<true/>
 	<key>com.apple.private.followup</key>

 	<true/>
 	<key>com.apple.private.health.records.allow-account-login</key>
 	<true/>
+	<key>com.apple.private.healthcontentd</key>
+	<true/>
 	<key>com.apple.private.healthkit</key>
 	<true/>
 	<key>com.apple.private.healthkit.analytics-agreements.control</key>

 	<true/>
 	<key>com.apple.private.security.storage.Photos</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.sleepd</key>

 		<string>/Applications/MobileTimer.app/</string>
 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_VideoIntelligence/</string>
+		<string>/private/var/MobileAsset/</string>
+		<string>/private/var/db/assetsubscriptiond/UAFAssetSubscriptions.db</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

 		<string>/Library/UserConfigurationProfile/</string>
 		<string>/Library/Health/</string>
 		<string>/Library/DeviceRegistry/</string>
+		<string>/tmp/</string>
+		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.CompanionLink</string>
+		<string>com.apple.fitnessintelligenced</string>
+		<string>com.apple.healthcontentd</string>
+		<string>com.apple.heartratecoordinatord</string>
+		<string>com.apple.heartratecoordinatord.requestor</string>
+		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.sirittsd</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 		<string>com.apple.aa.daemon.xpc</string>
 		<string>com.apple.locationd.synchronous</string>
 		<string>com.apple.locationd.registration</string>

 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.AudioAccessorySystemStateService</string>
 		<string>com.apple.controlcenter.remoteservice</string>
+		<string>com.apple.fairplaydeviceidentityd</string>
+		<string>com.apple.SharingServices</string>
+		<string>com.apple.paired-unlock</string>
+		<string>com.apple.heartratecoordinatord.observer</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.private.health.HeartRateStream</string>
 		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.nanolifestyle.privacy</string>
 		<string>com.apple.healthappd</string>

 		<string>com.apple.private.HearingTestFramework</string>
 		<string>com.apple.private.health.blood-pressure-best-practices</string>
 		<string>com.apple.private.health.health-actions</string>
+		<string>com.apple.MotionHealthAlgorithms</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.sharing.Client</key>
+	<true/>
 	<key>com.apple.shortcuts.health-access</key>
 	<true/>
 	<key>com.apple.sos.contacts</key>

```

### 🆕 HealthPlansWidgetExtension

> `/private/var/staged_system_apps/Health.app/PlugIns/HealthPlansWidgetExtension.appex/HealthPlansWidgetExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.chrono.open-urls-direct</key>
	<true/>
	<key>com.apple.developer.default-data-protection</key>
	<string>NSFileProtectionComplete</string>
</dict>
</plist>

```
### Home

> `/private/var/staged_system_apps/Home.app/Home`

```diff

 	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
+	<key>com.apple.developer.energykit</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.developer.homekit.background-mode</key>

 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>
 	<true/>
-	<key>com.apple.home.home-extension</key>
-	<true/>
 	<key>com.apple.homekit.private-spi-access</key>
 	<true/>
 	<key>com.apple.intelligentrouting.recommendationservice</key>

 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
-	<key>com.apple.private.tcc.manager.access.modify</key>
-	<array>
-		<string>kTCCServiceWillow</string>
-	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
 		<string>kTCCServiceEnergyKitGuidance</string>
 	</array>
-	<key>com.apple.private.tcc.manager.check-by-audit-token</key>
-	<array>
-		<string>kTCCServiceWillow</string>
-	</array>
 	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
 	<array>
 		<string>com.apple.tipsd</string>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>apple</string>
+		<string>com.apple.homeenergy.utilityonboarding</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```

### 🆕 HomeAppMessagesExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeAppMessagesExtension.appex/HomeAppMessagesExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Home.HomeAppMessagesExtension</string>
	<key>com.apple.developer.homekit</key>
	<true/>
	<key>com.apple.developer.homekit.background-mode</key>
	<true/>
	<key>com.apple.private.homekit</key>
	<true/>
	<key>com.apple.private.homekit.diagnostics</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceWillow</string>
	</array>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/Caches/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.matter.native.xpc</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.matter.native.xpc</string>
	</array>
</dict>
</plist>

```
### HomeEnergyWidgetsExtension

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeEnergyWidgetsExtension.appex/HomeEnergyWidgetsExtension`

```diff

 	<string>com.apple.Home.HomeEnergyWidgetsExtension</string>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.Home.HomeEnergyWidgetsExtension</string>
+	<key>com.apple.developer.energykit</key>
+	<true/>
 	<key>com.apple.developer.homekit</key>
 	<true/>
 	<key>com.apple.energykit.client</key>

```
### GenerativePlaygroundAppIntents

> `/private/var/staged_system_apps/Image Playground.app/Extensions/GenerativePlaygroundAppIntents.appex/GenerativePlaygroundAppIntents`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageGeneration</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### Image Playground

> `/private/var/staged_system_apps/Image Playground.app/Image Playground`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageGeneration</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

```
### GenerativePlaygroundMessagesAppExtension

> `/private/var/staged_system_apps/Image Playground.app/PlugIns/GenerativePlaygroundMessagesAppExtension.appex/GenerativePlaygroundMessagesAppExtension`

```diff

 	<true/>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageGeneration</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageGeneration</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.anvil</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>IOSurfaceRootUserClient</string>

```

### 🆕 KaleidoscopePoster

> `/private/var/staged_system_apps/KaleidoscopePosterApp.app/Extensions/KaleidoscopePoster.appex/KaleidoscopePoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.WallClockPosters.KaleidoscopePoster</string>
	</array>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```

### 🆕 NTKKaleidoscopeShaders.metallib

> `/private/var/staged_system_apps/KaleidoscopePosterApp.app/Extensions/KaleidoscopePoster.appex/NTKKaleidoscopeShaders.metallib`

- No entitlements *(yet)*

### 🆕 KaleidoscopePosterApp

> `/private/var/staged_system_apps/KaleidoscopePosterApp.app/KaleidoscopePosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Posters.KaleidoscopePosterApp</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

 	<true/>
 	<key>com.apple.private.allow-explicit-graphics-priority</key>
 	<true/>
+	<key>com.apple.private.appintents.live-entities.read</key>
+	<true/>
+	<key>com.apple.private.appintents.live-entities.write</key>
+	<array>
+		<string>maps.parkedCar</string>
+		<string>maps.currentNavigation</string>
+	</array>
 	<key>com.apple.private.appleaccount.icloud-app-switch-hidden</key>
 	<true/>
 	<key>com.apple.private.applemediaservices</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.appintents.LiveEntityService</string>
 		<string>com.apple.extensionkitservice</string>
 		<string>com.apple.misagent</string>
 		<string>com.apple.appprotectiond.read</string>

```
### MobileCal

> `/private/var/staged_system_apps/MobileCal.app/MobileCal`

```diff

 	<array>
 		<string>/System/Library/PrivateFrameworks/CalendarLink.framework</string>
 	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.mobilecal</string>
+	</array>
 	<key>com.apple.private.applemediaservices</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch</key>
 	<true/>
 	<key>com.apple.private.intelligenceplatform.views.read-only</key>

 		<string>com.apple.realitysystemsupport.hid_server_backboard</string>
 		<string>com.apple.intelligenceplatform.EntityResolution</string>
 		<string>com.apple.intelligenceplatform.View</string>
+		<string>com.apple.linkd.application-service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### MobileMail

> `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 		<string>com.apple.generativeexperiences.availabilityService</string>
 		<string>com.apple.TextUnderstanding.process</string>
 		<string>com.apple.familycircle.agent</string>
+		<string>com.apple.internal.SpotlightAutomationTester</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.local-name</key>
 	<array>

```
### MobileNotes

> `/private/var/staged_system_apps/MobileNotes.app/MobileNotes`

```diff

 	<true/>
 	<key>com.apple.mkb.usersession.info</key>
 	<true/>
+	<key>com.apple.mobilemail.mailservices</key>
+	<true/>
 	<key>com.apple.modelcatalog.full-access</key>
 	<true/>
 	<key>com.apple.modelmanager.assertion</key>

 	</array>
 	<key>com.apple.private.avatar.store</key>
 	<true/>
+	<key>com.apple.private.biome.client-identifier</key>
+	<string>com.apple.mobilenotes</string>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+		<string>GenerativeModels.GenerativeFunctions.Events</string>
+		<string>GenerativeModels.GenerativeFunctions.ModelIO</string>
+	</array>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.canModifyAppLinkPermissions</key>

 	</array>
 	<key>com.apple.proactive.PersonalizationPortrait.Contact</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
 	<key>com.apple.sage.summarization</key>
 	<true/>
 	<key>com.apple.sage.textcomposition</key>

 		<string>IOSurfaceRootUserClient</string>
 		<string>AGXDeviceUserClient</string>
 	</array>
+	<key>com.apple.shortcuts.stepwise-execution</key>
+	<true/>
+	<key>com.apple.shortcuts.variable-injection</key>
+	<true/>
+	<key>com.apple.siri.VoiceShortcuts.xpc</key>
+	<true/>
 	<key>com.apple.siri.koa.donate.internal</key>
 	<true/>
 	<key>com.apple.spotlight.documentunderstanding.entitledattributes</key>

```
### com.apple.mobilenotes.SpotlightIndexExtension

> `/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SpotlightIndexExtension.appex/com.apple.mobilenotes.SpotlightIndexExtension`

```diff

 	<array>
 		<string>com.apple.mobilenotes</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```
### MobileSMS

> `/private/var/staged_system_apps/MobileSMS.app/MobileSMS`

```diff

 	<key>com.apple.private.appintents-bundle-absolute-paths</key>
 	<array>
 		<string>/System/Library/PrivateFrameworks/ChatKit.framework</string>
-		<string>/System/Library/PrivateFrameworks/VisualIntelligenceUI.framework/</string>
 	</array>
 	<key>com.apple.private.appleaccount.app-hidden-from-icloud-settings</key>
 	<true/>

 		<string>SensitiveContentAnalysis.ResourcesInteraction</string>
 		<string>MLSE.ShareSheet.ConversationUserInteraction</string>
 	</array>
+	<key>com.apple.private.calendar.watchos-mutable-database</key>
+	<true/>
 	<key>com.apple.private.canGetAppLinkInfo</key>
 	<true/>
 	<key>com.apple.private.clouddocs.sharing-proxy</key>

 	<true/>
 	<key>com.apple.private.security.storage.PhotosLibraries</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
 	<key>com.apple.private.shared-with-you.on-screen-content</key>

 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
 		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
### MessagesAssistantExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesAssistantExtension.appex/MessagesAssistantExtension`

```diff

 		<string>com.apple.MobileSMS</string>
 		<string>com.apple.messages</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>

```
### MessagesNotificationExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesNotificationExtension.appex/MessagesNotificationExtension`

```diff

 		<string>com.apple.mobilephone</string>
 		<string>UITextInputContextIdentifiers</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.surfboard.scenesession-updates</key>

```
### MessagesTranscriptExtension

> `/private/var/staged_system_apps/MobileSMS.app/PlugIns/MessagesTranscriptExtension.appex/MessagesTranscriptExtension`

```diff

 		<string>com.apple.mobilephone</string>
 		<string>UITextInputContextIdentifiers</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<true/>
 	<key>com.apple.surfboard.scenesession-updates</key>

```
### MobileSafari

> `/private/var/staged_system_apps/MobileSafari.app/MobileSafari`

```diff

 	<string>NSFileProtectionCompleteUntilFirstUserAuthentication</string>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
-	<key>com.apple.developer.hardened-process</key>
-	<true/>
 	<key>com.apple.developer.icloud-container-environment</key>
 	<string>Production</string>
 	<key>com.apple.developer.icloud-container-identifiers</key>

 	<true/>
 	<key>com.apple.private.interstellar.data-access</key>
 	<string>*</string>
+	<key>com.apple.private.keychain.inet_expansion_fields</key>
+	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
 	<key>com.apple.private.launchservices.suppresscustomschemeprompt</key>

 	<array>
 		<string>otc</string>
 	</array>
+	<key>com.apple.private.webbookmarks.browserdataexchange</key>
+	<true/>
 	<key>com.apple.proactive.PersonalizationPortrait.NamedEntity.readOnly</key>
 	<true/>
 	<key>com.apple.proactive.eventtracker</key>

 		<string>com.apple.siri.generativeassistantsettings</string>
 		<string>com.apple.Passwords</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.mobileactivationd</string>

 		<string>apple</string>
 		<string>lockdown-identities</string>
 		<string>com.apple.Safari.WBSDevice</string>
+		<string>com.apple.Passwords.LocalState</string>
 		<string>com.apple.password-manager</string>
 		<string>com.apple.password-manager.personal</string>
 		<string>com.apple.cfnetwork-recently-deleted</string>

```
### com.apple.mobilesafari.SafariDiagnosticExtension

> `/private/var/staged_system_apps/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension`

```diff

 <dict>
 	<key>com.apple.DiagnosticExtensions.extension</key>
 	<true/>
+	<key>com.apple.private.Safari.History</key>
+	<true/>
 	<key>com.apple.private.can-load-any-content-blocker</key>
 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>

```
### MobileTimer

> `/private/var/staged_system_apps/MobileTimer.app/MobileTimer`

```diff

 	<array/>
 	<key>com.apple.developer.siri</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.media.ringtones.read-only</key>

```
### Music

> `/private/var/staged_system_apps/Music.app/Music`

```diff

 		<string>kTCCServiceMediaLibrary</string>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceFaceID</string>
+		<string>kTCCServicePhotos</string>
 	</array>
 	<key>com.apple.private.tcc.allow-or-regional-prompt</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>
 	</array>
+	<key>com.apple.private.ubiquity-additional-kvstore-identifiers</key>
+	<array>
+		<string>com.apple.music.concerts</string>
+	</array>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
 	<key>com.apple.rootless.storage.MusicApp</key>

```
### MusicCoreSpotlightExtension

> `/private/var/staged_system_apps/Music.app/PlugIns/MusicCoreSpotlightExtension.appex/MusicCoreSpotlightExtension`

```diff

 	<array>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 </dict>
 </plist>
 

```
### News

> `/private/var/staged_system_apps/News.app/News`

```diff

 	</array>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.activitykit.unboundedActivityRequester</key>
+	<true/>
 	<key>com.apple.private.ad.analytics</key>
 	<true/>
 	<key>com.apple.private.appintents-bundle-absolute-paths</key>

 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>
 	<true/>
+	<key>com.apple.private.news-push-notification</key>
+	<true/>
 	<key>com.apple.private.safari.can-use-launch-agent</key>
 	<true/>
 	<key>com.apple.private.security.container-required</key>

 	<true/>
 	<key>com.apple.private.security.system-application</key>
 	<true/>
+	<key>com.apple.private.sessionkit.listener</key>
+	<true/>
 	<key>com.apple.private.sessionkit.permitMultipleProcessInputs</key>
 	<true/>
 	<key>com.apple.private.sessionkit.sessionRequest</key>
 	<true/>
 	<key>com.apple.private.sociallayer.highlights</key>
 	<true/>
+	<key>com.apple.private.sportskit.client</key>
+	<true/>
 	<key>com.apple.private.swc.additional-service-details-consumer</key>
 	<true/>
 	<key>com.apple.private.swc.system-app</key>

 		<string>com.apple.newsd.analytics</string>
 		<string>com.apple.newsd.download</string>
 		<string>com.apple.newsd.live-activity</string>
+		<string>com.apple.newsd.push-notification</string>
 		<string>com.apple.newsd.today-feed</string>
 		<string>com.apple.routined.registration</string>
 		<string>com.apple.routined.internal</string>

 		<string>com.apple.news.ScoringService</string>
 		<string>com.apple.MobileTimer.timerserver</string>
 		<string>com.apple.identityservicesd.embedded.auth</string>
+		<string>com.apple.sportsd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### NewsArticleQuickLook

> `/private/var/staged_system_apps/News.app/PlugIns/NewsArticleQuickLook.appex/NewsArticleQuickLook`

```diff

 	<array>
 		<string>com.apple.newscore</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.no-tagged-receive</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.hardened-heap</key>
+	<true/>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 </dict>
 </plist>
 

```
### PassbookQuicklookPreviewExtension

> `/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookQuicklookPreviewExtension.appex/PassbookQuicklookPreviewExtension`

```diff

 		<string>com.apple.passd.library</string>
 		<string>com.apple.financed.service.coredatastore</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### Passwords

> `/private/var/staged_system_apps/Passwords.app/Passwords`

```diff

 	<true/>
 	<key>com.apple.private.imcore.imagent</key>
 	<true/>
+	<key>com.apple.private.keychain.inet_expansion_fields</key>
+	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
 	<key>com.apple.private.launchservices.changedefaulthandlers</key>

 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.cdp.daemon</string>
 		<string>com.apple.ak.privateemail.xpc</string>
+		<string>com.apple.sharing.airdrop.service</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```

### 🆕 PodcastsAppEntities

> `/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsAppEntities.framework/PodcastsAppEntities`

- No entitlements *(yet)*

### 🆕 PodcastsAppIntents

> `/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsAppIntents.framework/PodcastsAppIntents`

- No entitlements *(yet)*

### 🆕 PodcastsPlaybackUI

> `/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsPlaybackUI.framework/PodcastsPlaybackUI`

- No entitlements *(yet)*

### 🆕 PodcastsSuggestedDonations

> `/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsSuggestedDonations.framework/PodcastsSuggestedDonations`

- No entitlements *(yet)*

### 🆕 PodcastsWidgetKit

> `/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsWidgetKit.framework/PodcastsWidgetKit`

- No entitlements *(yet)*

### 🆕 SWAIPodcastsAppIntents

> `/private/var/staged_system_apps/Podcasts.app/Frameworks/SWAIPodcastsAppIntents.framework/SWAIPodcastsAppIntents`

- No entitlements *(yet)*
### com.apple.podcasts.SpotlightIndexExtension

> `/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/com.apple.podcasts.SpotlightIndexExtension`

```diff

 	<array>
 		<string>243LU875E5.groups.com.apple.podcasts</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 </dict>

```
### Podcasts

> `/private/var/staged_system_apps/Podcasts.app/Podcasts`

```diff

 		<string>/Library/Caches/com.apple.AppleMediaServices/</string>
 		<string>/Media/ContentKeys/</string>
 		<string>/Media/iTunes_Control/Music/</string>
+		<string>/Media/MotionAssets/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

```

### 🆕 PridePosterExtension

> `/private/var/staged_system_apps/PridePosterApp.app/Extensions/PridePosterExtension.appex/PridePosterExtension`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
</dict>
</plist>

```

### 🆕 PridePosterApp

> `/private/var/staged_system_apps/PridePosterApp.app/PridePosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.PridePoster</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### RemindersSpotlightIndexExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersSpotlightIndexExtension.appex/RemindersSpotlightIndexExtension`

```diff

 	<array>
 		<string>com.apple.remindd</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 </dict>
 </plist>
 

```
### Reminders

> `/private/var/staged_system_apps/Reminders.app/Reminders`

```diff

 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
 	<key>com.apple.locationd.prompt_behavior</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 		<key>userInteractive</key>
 		<true/>
 	</dict>
+	<key>com.apple.private.replicator.dataProvider</key>
+	<true/>
 	<key>com.apple.private.security.container-required</key>
 	<true/>
 	<key>com.apple.private.security.storage.MessagesMetaData</key>

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.reminders.replicatorclient.entitlement</key>
+	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
 	<key>com.apple.runningboard.posterkit.host</key>
 	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.reminders</string>

 		<string>com.apple.chrono.widgetcenterconnection</string>
 		<string>com.apple.tipsd</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.perceptiond.entitykit</string>
 		<string>com.apple.alarmkitservices</string>
 		<string>com.apple.sessionservices</string>
+		<string>com.apple.replicatorservices</string>
+		<string>com.apple.perceptiond.peripheralSensing</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### SequoiaTranslator

> `/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator`

```diff

 	<true/>
 	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
 	<true/>
+	<key>com.apple.private.feedback.drafting</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.mobileinstall.xpc-services-enabled</key>

```
### Shortcuts

> `/private/var/staged_system_apps/Shortcuts.app/Shortcuts`

```diff

 		<string>com.apple.passd.payment</string>
 		<string>com.apple.posterboardservices.dataModel</string>
 		<string>com.apple.posterboardservices.services</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 		<string>com.apple.proactive.ActionPrediction.predictions</string>
 		<string>com.apple.proactive.AppPrediction.predictions</string>
 		<string>com.apple.proactive.ProactiveSuggestionClientModel.xpc</string>

```
### TipsSpotlightIndex

> `/private/var/staged_system_apps/Tips.app/PlugIns/TipsSpotlightIndex.appex/TipsSpotlightIndex`

```diff

 	<array>
 		<string>com.apple.tipsd</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.tipsd.access</key>
 	<true/>
 </dict>

```

### 🆕 ExtragalacticPoster

> `/private/var/staged_system_apps/UnityPosterApp.app/Extensions/ExtragalacticPoster.appex/ExtragalacticPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.WatchFacesWallpaperSupport.ExtragalacticPoster</string>
	</array>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```

### 🆕 RhizomePoster

> `/private/var/staged_system_apps/UnityPosterApp.app/Extensions/RhizomePoster.appex/RhizomePoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.WatchFacesWallpaperSupport.RhizomePoster</string>
	</array>
	<key>com.apple.security.ts.opengl-or-metal</key>
	<true/>
</dict>
</plist>

```

### 🆕 Unity2025Poster

> `/private/var/staged_system_apps/UnityPosterApp.app/Extensions/Unity2025Poster.appex/Unity2025Poster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.springboard</string>
	</array>
</dict>
</plist>

```

### 🆕 UnityPoster

> `/private/var/staged_system_apps/UnityPosterApp.app/Extensions/UnityPoster.appex/UnityPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.CARenderServer</string>
		<string>com.apple.coremedia.compressionsession</string>
		<string>com.apple.coremedia.decompressionsession</string>
		<string>com.apple.coremedia.videocodecd.compressionsession</string>
		<string>com.apple.coremedia.videocodecd.compressionsession.xpc</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession</string>
		<string>com.apple.coremedia.videocodecd.decompressionsession.xpc</string>
	</array>
</dict>
</plist>

```

### 🆕 UnityPosterApp

> `/private/var/staged_system_apps/UnityPosterApp.app/UnityPosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Posters.UnityPosterApp</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### VoiceMemosIntentsExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosIntentsExtension.appex/VoiceMemosIntentsExtension`

```diff

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>

```
### VoiceMemosShareExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/VoiceMemosShareExtension.appex/VoiceMemosShareExtension`

```diff

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>

```
### com.apple.VoiceMemos.SpotlightIndexExtension

> `/private/var/staged_system_apps/VoiceMemos.app/PlugIns/com.apple.VoiceMemos.SpotlightIndexExtension.appex/com.apple.VoiceMemos.SpotlightIndexExtension`

```diff

 	<array>
 		<string>com.apple.VoiceMemos</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.dyld-ro</key>
+	<true/>
+	<key>com.apple.security.hardened-process.enhanced-security-version</key>
+	<integer>1</integer>
+	<key>com.apple.security.hardened-process.platform-restrictions</key>
+	<integer>2</integer>
 </dict>
 </plist>
 

```
### VoiceMemos

> `/private/var/staged_system_apps/VoiceMemos.app/VoiceMemos`

```diff

 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>
 	<true/>
+	<key>com.apple.private.coreaudio.borrowaudiosession.allow</key>
+	<true/>
 	<key>com.apple.private.hid.client.event-dispatch.internal</key>
 	<true/>
 	<key>com.apple.private.mediaexperience.startrecordinginthebackground.allow</key>

```

### 🆕 WeatherPoster

> `/private/var/staged_system_apps/WeatherPosterApp.app/Extensions/WeatherPoster.appex/WeatherPoster`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.QuartzCore.secure-mode</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.weather</string>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.prompt_behavior</key>
	<true/>
	<key>com.apple.locationd.prompt_from_background</key>
	<true/>
	<key>com.apple.posterkit.enhanced-memory-limits</key>
	<true/>
	<key>com.apple.posterkit.provider</key>
	<true/>
	<key>com.apple.private.applemediaservices</key>
	<true/>
	<key>com.apple.private.network.socket-delegate</key>
	<true/>
	<key>com.apple.private.security.storage.Weather</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.weather</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private/var/db/com.apple.countryd/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Weather/</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>kCFPreferencesAnyApplication</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.weather</string>
		<string>com.apple.weather.internal</string>
		<string>com.apple.weather.sensitive</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>fairplay-client</key>
	<string>511712240</string>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
	</array>
</dict>
</plist>

```

### 🆕 WeatherPosterApp

> `/private/var/staged_system_apps/WeatherPosterApp.app/WeatherPosterApp`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.Posters.WeatherPosterApp</string>
	<key>com.apple.developer.app-management-domain</key>
	<string>com.apple.Posters</string>
	<key>com.apple.developer.not-executable</key>
	<true/>
	<key>com.apple.private.attribution.implicitly-assumed-identity</key>
	<dict>
		<key>type</key>
		<string>path</string>
		<key>value</key>
		<string>/private/var/staged_system_apps/WeatherPosterApp.app/WeatherPosterApp</string>
	</dict>
	<key>com.apple.private.security.no-container</key>
	<true/>
	<key>com.apple.private.security.system-application</key>
	<true/>
	<key>com.apple.security.app-sandbox</key>
	<true/>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### fsck_apfs

> `/sbin/fsck_apfs`

```diff

 	<true/>
 	<key>com.apple.private.apfs.dataless-manipulation</key>
 	<true/>
+	<key>com.apple.private.apfs.lock-container-load</key>
+	<true/>
 	<key>com.apple.private.apfs.revert-to-snapshot</key>
 	<true/>
 	<key>com.apple.private.iopol.case_sensitivity</key>

```
### launchd

> `/sbin/launchd`

```diff

 	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 </dict>
 </plist>
 

```
### IOMFB_FDR_Loader

> `/usr/bin/IOMFB_FDR_Loader`

```diff

 <dict>
 	<key>com.apple.AppleNVMeEAN.allow</key>
 	<true/>
+	<key>com.apple.keystore.fdr-access</key>
+	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
+	<true/>
 	<key>com.apple.private.iomfb.set-block</key>
 	<true/>
 	<key>com.apple.private.iomfb.set-block-client-profile</key>

```
### brctl

> `/usr/bin/brctl`

```diff

 		<string>gatherInformationForPath:reply:</string>
 		<string>log:function:source:line:message:</string>
 		<string>forceSyncContainerID:reply:</string>
-		<string>computePurgeableSpaceForAllUrgenciesWithReply:</string>
-		<string>purgeAmount:withUrgency:reply:</string>
-		<string>reclaimAmount:withUrgency:reply:</string>
+		<string>computePurgeableSpaceWithReply:</string>
+		<string>reclaimDiskSpaceWithReply:</string>
 		<string>waitForFileSystemChangeProcessingWithReply:</string>
 		<string>resetBudgets:reply:</string>
 		<string>createContainerWithID:ownerName:reply:</string>

 		<string>healthStatusStringForContainer:reply:</string>
 		<string>zoneNameForContainer:reply:</string>
 		<string>dumpCoordinationInfoTo:reply:</string>
-		<string>backupDatabaseWithURLWrapper:reply:</string>
+		<string>backupDatabaseWithURLWrapper:doNotObfuscate:reply:</string>
 	</array>
 	<key>com.apple.private.cloudkit.masquerade</key>
 	<true/>

```
### modelcatalogdump

> `/usr/bin/modelcatalogdump`

```diff

 	<true/>
 	<key>com.apple.modelcatalog.subscriptions</key>
 	<true/>
+	<key>com.apple.modelmanager.forceAssetVersionSwitch</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/mobile/Library/UnifiedAssetFramework/</string>

 	<array>
 		<string>SIML_ADM_PERSONALIZATION</string>
 		<string>SIRI_TTS_UAF_AB_DEVICE</string>
+		<string>UAF_AB_MODELCATALOG</string>
+		<string>SIRI_TTS_AB_PCC</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### perfpowermetricd

> `/usr/bin/perfpowermetricd`

```diff

 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
+	<key>com.apple.private.kernel.read-write-trial-experiment-factors</key>
+	<true/>
 	<key>com.apple.private.kernel.userspacereboot-info-read-only</key>
 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>

```
### powerlogHelperd

> `/usr/bin/powerlogHelperd`

```diff

 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
+	<key>com.apple.private.kernel.read-write-trial-experiment-factors</key>
+	<true/>
 	<key>com.apple.private.kernel.userspacereboot-info-read-only</key>
 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>

```

### 🆕 searchdiagnose

> `/usr/bin/searchdiagnose`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.searchdiagnose</string>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.security.storage.Spotlight</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```

### 🆕 libaxis.dylib

> `/usr/lib/libaxis.dylib`

- No entitlements *(yet)*
### ASPCarryLog

> `/usr/libexec/ASPCarryLog`

```diff

 	</array>
 	<key>com.apple.security.exception.sysctl.read-only</key>
 	<array>
+		<string>kern.hibernatestatistics</string>
 		<string>kern.memorystatus_freeze_pageouts</string>
 		<string>vm.compressor_swapouts_under_30s</string>
 		<string>vm.compressor_swapouts_under_60s</string>

```
### AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

 	</array>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.keychain.inet_expansion_fields</key>
+	<true/>
 	<key>com.apple.private.keychain.kcsharing.client</key>
 	<true/>
 	<key>com.apple.private.octagon</key>

 		<string>com.apple.cfnetwork.testing</string>
 		<string>com.apple.webkit.webauthn.testing</string>
 		<string>com.apple.password-manager.testing</string>
+		<string>com.apple.Passwords.LocalState</string>
+		<string>com.apple.Passwords.LocalState.testing</string>
 		<string>com.apple.password-manager.personal</string>
 		<string>com.apple.password-manager.personal.testing</string>
 		<string>com.apple.cfnetwork-recently-deleted</string>

```
### BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

 	<array>
 		<string>com.apple.fairplayd.xpc</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.icloud.findmydevice.managed</string>

```
### FinishRestoreFromBackup

> `/usr/libexec/FinishRestoreFromBackup`

```diff

 		<string>/Media/Recordings/</string>
 		<string>/Library/Recordings/</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 </dict>
 </plist>
 

```
### MobileGestaltHelper

> `/usr/libexec/MobileGestaltHelper`

```diff

 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.mobilegestaltcache</string>
+		<string>systemgroup.com.apple.mobileactivationd</string>
 	</array>
 	<key>com.apple.wifi.manager-access</key>
 	<true/>

```
### MobileStorageMounter

> `/usr/libexec/MobileStorageMounter`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.MobileStorageMounter</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.allow-submit-launch-angels</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>
 	<string>com.apple.mobile.storage_mounter</string>
 	<key>com.apple.private.xpc.launchd.storage-mounter</key>

```
### NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

 	<true/>
 	<key>com.apple.nvmetunnel.allow</key>
 	<true/>
+	<key>com.apple.private.apfs.purgeable.extents</key>
+	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.storage.SidebarFileDispatcherService</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>ASPUserClient</string>
 		<string>AppleNVMeUpdateUC</string>
 	</array>
+	<key>com.apple.storage.SidebarFileDispatcherService</key>
+	<true/>
 </dict>
 </plist>
 

```
### PerfPowerServices

> `/usr/libexec/PerfPowerServices`

```diff

 	<true/>
 	<key>com.apple.private.iokit.powerlogging</key>
 	<true/>
+	<key>com.apple.private.iokit.soc-limit</key>
+	<true/>
 	<key>com.apple.private.ioreporting.access</key>
 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
 	<key>com.apple.private.kernel.jetsam</key>
 	<true/>
+	<key>com.apple.private.kernel.read-write-trial-experiment-factors</key>
+	<true/>
 	<key>com.apple.private.kernel.userspacereboot-info-read-only</key>
 	<true/>
 	<key>com.apple.private.mako.status</key>

```
### PerfPowerServicesExtended

> `/usr/libexec/PerfPowerServicesExtended`

```diff

 	<true/>
 	<key>com.apple.private.kernel.global-proc-info</key>
 	<true/>
+	<key>com.apple.private.kernel.read-write-trial-experiment-factors</key>
+	<true/>
 	<key>com.apple.private.kernel.userspacereboot-info-read-only</key>
 	<true/>
 	<key>com.apple.private.logging.diagnostic</key>

```

### 🆕 SafariBookmarksSyncAgent

> `/usr/libexec/SafariBookmarksSyncAgent`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.mobilesafari</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>aps-environment</key>
	<string>production</string>
	<key>com.apple.application-identifier</key>
	<string>com.apple.Safari</string>
	<key>com.apple.developer.icloud-container-environment</key>
	<string>Production</string>
	<key>com.apple.developer.icloud-extended-share-access</key>
	<array>
		<string>InProcessShareOwnerParticipantInfo</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>UniqueDeviceID</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.aps-connection-initiate</key>
	<true/>
	<key>com.apple.private.cloudkit.masquerade</key>
	<true/>
	<key>com.apple.private.cloudkit.serviceNameForContainerMap</key>
	<dict>
		<key>com.apple.SafariShared.CloudTabs</key>
		<string>com.apple.SafariShared.CloudTabs</string>
		<key>com.apple.SafariShared.Settings</key>
		<string>com.apple.SafariShared.CloudTabs</string>
	</dict>
	<key>com.apple.private.cloudkit.setEnvironment</key>
	<true/>
	<key>com.apple.private.cloudkit.spi</key>
	<true/>
	<key>com.apple.private.cloudkit.systemService</key>
	<true/>
	<key>com.apple.private.interstellar.data-access</key>
	<string>*</string>
	<key>com.apple.private.security.container-required</key>
	<string>com.apple.mobilesafari</string>
	<key>com.apple.private.security.storage.Safari</key>
	<true/>
	<key>com.apple.private.sociallayer.highlights</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceLiverpool</string>
	</array>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<array>
		<string>group.com.apple.safari</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.spotlight.IndexAgent</string>
		<string>com.apple.securityd</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.mobilesafarishared</string>
	</array>
	<key>keychain-access-groups</key>
	<array>
		<string>com.apple.Safari.WBSDevice</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>SafariBookmarksSyncAgent</string>
	</array>
</dict>
</plist>

```
### UserEventAgent

> `/usr/libexec/UserEventAgent`

```diff

 	<array>
 		<string>/Library/Logs/AppleSupport/</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleCredentialManagerUserClient</string>

```
### accessorysensormgrd

> `/usr/libexec/accessorysensormgrd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>aop2.asen-motion</key>
+	<true/>
 	<key>com.apple.AudioAccessoryServices</key>
 	<true/>
+	<key>com.apple.afk.shmem-user</key>
+	<true/>
+	<key>com.apple.afk.user</key>
+	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.accessorysensormgrd</string>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
+	<key>com.apple.keystore.access-keychain-keys</key>
+	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
 	<key>com.apple.polaris.client</key>
 	<true/>
 	<key>com.apple.polaris.producer.all-streams</key>

 	<array>
 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.polaris.systemgraph_v2</string>
+		<string>com.apple.alwaysonexclaves</string>
+		<string>com.apple.perceptiond.peripheralCoordinator</string>
+		<string>com.apple.perceptiond.peripheralSensorCrop</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.AccessorySensorManager</string>
+		<string>com.apple.SecurePairingClientControl</string>
+	</array>
+	<key>com.apple.security.iokit-user-client-class</key>
+	<array>
+		<string>AFKSharedMemoryUserClient</string>
+		<string>AFKMemoryDescriptorManagerUserClient</string>
+		<string>AFKEndpointInterfaceUserClient</string>
 	</array>
 	<key>com.apple.security.temporary-exception.files.absolute-path.read-write</key>
 	<array>

```
### adprivacyd

> `/usr/libexec/adprivacyd`

```diff

 	<array>
 		<string>com.apple.ak.auth.xpc</string>
 		<string>com.apple.ap.promotedcontent.supportinterface</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>com.apple.AdPlatforms</string>
 		<string>com.apple.AppStore</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.ak.auth.xpc</string>

```
### airplayd

> `/usr/libexec/airplayd`

```diff

 		<string>com.apple.airplay</string>
 		<string>com.apple.coremedia.bag.airplay</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.network.server</key>

```
### announced

> `/usr/libexec/announced`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
 	<key>com.apple.private.homehubd</key>
 	<array>
 		<string>endpoint-read</string>

 		<string>com.apple.contactsd</string>
 		<string>com.apple.homed.xpc</string>
 		<string>com.apple.geod</string>
+		<string>com.apple.spotlight.IndexAgent</string>
 		<string>com.apple.PairingManager</string>
 		<string>com.apple.SystemConfiguration.configd</string>
 		<string>com.apple.idsremoteurlconnectionagent.embedded.auth</string>

 		<string>com.apple.telephonyutilities.callservicesdaemon.callcapabilities</string>
 		<string>com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager</string>
 		<string>com.apple.trustd</string>
+		<string>com.apple.SetStoreUpdateService</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.audio.AudioComponentRegistrar</string>

 	<array>
 		<string>hw.osenvironment</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.files.home-relative-path.read-write</key>
 	<array>
 		<string>/Library/Assistant/</string>

```
### anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.private.aop-audio.user-access</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.mobileactivationd</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### aonsensed

> `/usr/libexec/aonsensed`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>aop2.asen-motion</key>
+	<true/>
 	<key>aop2.gps-data.ent</key>
 	<true/>
 	<key>aop2.gps-debug</key>

 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.locationd.private_info</key>
+	<true/>
+	<key>com.apple.locationd.spectator</key>
+	<true/>
+	<key>com.apple.locationd.trusted_ARKit_hinter</key>
+	<true/>
 	<key>com.apple.nearbyd.xpc</key>
 	<true/>
 	<key>com.apple.nearbyinteraction.background</key>

 	<string>/Library/UnifiedAssetFramework</string>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.polaris.daemon_default</string>
+		<string>com.apple.polaris.systemgraph_v2</string>
 		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.private.corewifi-xpc</string>
 		<string>com.apple.mobileasset.autoasset</string>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.alwaysonexclaves</string>
+		<string>com.apple.perceptiond.peripheralSensing</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
+		<string>IOSurfaceRootUserClient</string>
+		<string>H11ANEInDirectPathClient</string>
+		<string>AppleKeyStoreUserClient</string>
+		<string>AGXDeviceUserClient</string>
+		<string>IOSurfaceAcceleratorClient</string>
+		<string>AFKSharedMemoryUserClient</string>
 		<string>RootDomainUserClient</string>
+		<string>AFKMemoryDescriptorManagerUserClient</string>
+		<string>AFKEndpointInterfaceUserClient</string>
+		<string>AppleAOPAudioUserClient</string>
 		<string>IOHIDLibUserClient</string>
-		<string>RootDomainUserClient</string>
-		<string>AppleSPUUserClient</string>
-		<string>RootDomainUserClient</string>
 		<string>AppleSPUFastpathDriverUserClient</string>
+		<string>AppleSPUUserClient</string>
 	</array>
 	<key>com.apple.security.ts.mobile-keybag-access</key>
 	<true/>

```
### appleaccountd

> `/usr/libexec/appleaccountd`

```diff

 	</array>
 	<key>com.apple.private.octagon</key>
 	<true/>
+	<key>com.apple.private.sandbox.profile:embedded</key>
+	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.appleaccountd</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<true/>
 	<key>com.apple.security.personal-information.addressbook</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.nsurlstoragedresources</string>

 	</array>
 	<key>com.apple.security.ts.cloudkit-client</key>
 	<true/>
+	<key>com.apple.security.ts.daemon-container</key>
+	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.appleaccountd</string>
 	<key>com.apple.springboard.CFUserNotification</key>

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
### appleidsetupd

> `/usr/libexec/appleidsetupd`

```diff

 	</dict>
 	<key>com.apple.private.eligibilityd.fetchNewestPolicies</key>
 	<true/>
+	<key>com.apple.private.eligibilityd.internalState</key>
+	<true/>
 	<key>com.apple.private.followup</key>
 	<true/>
 	<key>com.apple.private.game-center</key>

```
### asktod

> `/usr/libexec/asktod`

```diff

 	<true/>
 	<key>com.apple.private.screentime-ask</key>
 	<true/>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 		<string>com.apple.frontboard.systemappservices</string>
 		<string>com.apple.usernotifications.listener</string>
 	</array>
+	<key>com.apple.security.ts.daemon-container</key>
+	<true/>
 	<key>com.apple.security.ts.identity-services-client</key>
 	<true/>
 	<key>com.apple.security.ts.mobile-keybag-access</key>

```
### assetsubscriptiond

> `/usr/libexec/assetsubscriptiond`

```diff

 	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>

 		<string>1701</string>
 		<string>SIRI_TTS_UAF_AB_DEVICE</string>
 		<string>SIML_ADM_PERSONALIZATION</string>
+		<string>UAF_AB_MODELCATALOG</string>
+		<string>UAF_AB_ANSWER_SYNTHESIS</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

 	<true/>
 	<key>aps-environment</key>
 	<string>production</string>
+	<key>com.apple.AccessorySensorManager</key>
+	<true/>
 	<key>com.apple.AudioAccessoryServices</key>
 	<true/>
 	<key>com.apple.AudioAccessorySystemStateService</key>

 	<true/>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.DeviceAccess</key>
+	<true/>
+	<key>com.apple.DeviceAccess.private</key>
+	<true/>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
 	<key>com.apple.SensingPredict</key>

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.developer.accessory-transport-extension</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.healthkit</key>

 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>
 	<true/>
+	<key>com.apple.nearbyd.xpc</key>
+	<true/>
+	<key>com.apple.nearbyinteraction.background</key>
+	<true/>
+	<key>com.apple.powerui.smartcharging</key>
+	<true/>
 	<key>com.apple.powerui.smartcharging.AudioAccessory</key>
 	<true/>
+	<key>com.apple.private.AccessorySensorManager</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>BluetoothAddress</string>

 	<true/>
 	<key>com.apple.private.attentionawareness</key>
 	<true/>
+	<key>com.apple.private.attentionawareness.poll</key>
+	<true/>
+	<key>com.apple.private.attentionawareness.samplewhileabsent</key>
+	<true/>
 	<key>com.apple.private.biome.writer</key>
 	<array>
 		<string>Discoverability.Signals</string>

 	</array>
 	<key>com.apple.private.ids.registration</key>
 	<true/>
+	<key>com.apple.private.nearbyinteraction.device-presence</key>
+	<true/>
+	<key>com.apple.private.nearbyinteraction.privileged</key>
+	<true/>
 	<key>com.apple.private.power.notifications</key>
 	<true/>
 	<key>com.apple.private.security.storage.SoundProfileAsset</key>
 	<true/>
+	<key>com.apple.private.security.storage.os_eligibility.readonly</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceBluetoothPeripheral</string>

 		<string>kTCCServiceBluetoothAlways</string>
 		<string>kTCCServiceListenEvent</string>
 		<string>kTCCServiceCalendar</string>
+		<string>kTTCServiceBluetoothPeripheral</string>
 	</array>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>

 		<string>com.apple.MuteControlUserNotifications</string>
 		<string>com.apple.ShareAudioNotifications</string>
 		<string>com.apple.AudioAccessoryUserNotifications</string>
+		<string>com.apple.AudioAccessoryInteractiveNotifications</string>
 		<string>com.apple.HearingModeUserNotifications</string>
 		<string>com.apple.SleepDetectionUserNotification</string>
 		<string>com.apple.AssetManagementUserNotification</string>

 		<string>/usr/libexec</string>
 		<string>/private/var/mobile/Library/Preferences/com.apple.mediaremote.plist</string>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.AudioAccessoryServices</string>
+		<string>com.apple.AudioAccessoryKit</string>
 		<string>com.apple.feedbackd.xpc</string>
 		<string>com.apple.aps.cloudpaird</string>
 		<string>com.apple.apsd</string>

 		<string>com.apple.relatived.public</string>
 		<string>com.apple.healthd.server</string>
 		<string>com.apple.BTAudioHALPluginAccessories</string>
+		<string>com.apple.AudioAccessoryCommunication.xpc</string>
 		<string>com.apple.iohideventsystem</string>
 		<string>com.apple.toolbox.indexing-service</string>
 		<string>com.apple.PerfPowerTelemetryClientRegistrationService</string>

 		<string>com.apple.powerui.audioAccessorySmartChargeManager</string>
 		<string>com.apple.AttentionAwareness</string>
 		<string>com.apple.SBUserNotification</string>
+		<string>com.apple.perceptiond.entitykit</string>
+		<string>com.apple.nearbyd.xpc.nearbyinteraction</string>
+		<string>com.apple.perceptiond.physicalContext</string>
+		<string>com.apple.minilab.local_res_fact</string>
+		<string>com.apple.perceptiond.anst</string>
+		<string>com.apple.perceptiond.featureDetection</string>
+		<string>com.apple.perceptiond.histogram</string>
+		<string>com.apple.perceptiond.daemonWake</string>
+		<string>com.apple.perceptiond.api</string>
+		<string>com.apple.perceptiond.sceneClassification</string>
+		<string>com.apple.perceptiond.peripheralSensing</string>
+		<string>com.apple.DeviceAccess.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### audioanalyticsd

> `/usr/libexec/audioanalyticsd`

```diff

 <dict>
 	<key>com.apple.TapToRadarKit.service-access</key>
 	<true/>
+	<key>com.apple.accounts.appleaccount.fullaccess</key>
+	<true/>
 	<key>com.apple.audioanalytics.helper.service</key>
 	<true/>
 	<key>com.apple.bluetooth.internal</key>

 		<string>com.apple.lsd.open</string>
 		<string>com.apple.bluetooth.xpc</string>
 		<string>com.apple.usernotifications.usernotificationservice</string>
+		<string>com.apple.account.AppleAccount</string>
 	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>

 	<array>
 		<string>/Library/Logs/SiriTTSService/</string>
 	</array>
+	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
+	<string>IOHIDLibUserClient</string>
 	<key>com.apple.security.temporary-exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.server.bluetooth.general.xpc</string>
 	</array>
+	<key>com.apple.security.temporary-exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.CloudSubscriptionFeatures.optIn</string>
+		<string>com.apple.CloudSubscriptionFeatures.gm.bypass</string>
+	</array>
 	<key>com.apple.security.ts.springboard-services</key>
 	<true/>
 	<key>com.apple.springboard.CFUserNotification</key>

```
### audiomxd

> `/usr/libexec/audiomxd`

```diff

 	<string>com.apple.lskdd</string>
 	<key>checklessPersistentURLTranslation</key>
 	<true/>
+	<key>com.apple.AudioAccessoryCommunication.xpc</key>
+	<true/>
 	<key>com.apple.AudioAccessoryServices</key>
 	<true/>
 	<key>com.apple.BTAudioHALPluginAccessories</key>

 		<string>com.apple.backboard.hid-services.xpc</string>
 		<string>com.apple.BluetoothUIService</string>
 		<string>com.apple.BTAudioHALPlugin.xpc</string>
+		<string>com.apple.AudioAccessoryCommunication.xpc</string>
 		<string>com.apple.callkit.callcontrollerhost</string>
 		<string>com.apple.CARenderServer</string>
 		<string>com.apple.Carousel.contextuallock</string>

```
### backboardd

> `/usr/libexec/backboardd`

```diff

 	<true/>
 	<key>com.apple.hid.manager.user-access-keyboard</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-protected</key>
+	<true/>
 	<key>com.apple.hid.multitouch.user-access</key>
 	<true/>
 	<key>com.apple.hid.peppytouch.set-touch</key>

 		<string>Device.Display.TrueTone</string>
 		<string>Device.Display.NightShift</string>
 	</array>
+	<key>com.apple.private.biometrickit.allow-default</key>
+	<true/>
 	<key>com.apple.private.bmk.allow</key>
 	<true/>
 	<key>com.apple.private.cecd.control</key>

 		<string>kern.task_conclave</string>
 		<string>kern.bootargs</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleSMCClient</string>

```
### batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

 	<true/>
 	<key>com.apple.coreduetd.context</key>
 	<true/>
+	<key>com.apple.powerui.smartcharging</key>
+	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
 	<key>com.apple.private.iokit.charging-iconography</key>

 		<string>com.apple.powerlog.plxpclogger.xpc</string>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.appleneuralengine.private</string>
+		<string>com.apple.powerui.smartChargeManager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### biomesyncd

> `/usr/libexec/biomesyncd`

```diff

 	<true/>
 	<key>com.apple.security.ts.tmpdir</key>
 	<string>com.apple.biomesyncd</string>
+	<key>com.apple.trial.client</key>
+	<array>
+		<string>INTELLIGENCE_PLATFORM_BIOME_SYNC_CONFIG</string>
+	</array>
 	<key>com.apple.uservault</key>
 	<true/>
 	<key>com.apple.wifi.manager-access</key>

```

### 🆕 browserkitd

> `/usr/libexec/browserkitd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.private.coreservices.canopenactivity</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.security.daemon-container</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/tmp/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.frontboard.systemappservices</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.ts.daemon-container</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<array>
		<string>settings-navigation://com.apple.Settings.Apps/com.apple.mobilesafari</string>
	</array>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
</dict>
</plist>

```
### bulletindistributord

> `/usr/libexec/bulletindistributord`

```diff

 	<true/>
 	<key>com.apple.private.dmd.policy</key>
 	<true/>
+	<key>com.apple.private.donotdisturb.settings.request.client-identifiers</key>
+	<array>
+		<string>com.apple.bulletindistributor</string>
+	</array>
+	<key>com.apple.private.donotdisturb.settings.updates.client-identifiers</key>
+	<array>
+		<string>com.apple.bulletindistributor</string>
+	</array>
 	<key>com.apple.private.ids.messaging</key>
 	<array>
 		<string>com.apple.private.alloy.bulletindistributor</string>

 		<string>com.apple.private.alloy.bulletindistributor</string>
 		<string>com.apple.private.alloy.bulletindistributor.settings</string>
 	</array>
+	<key>com.apple.security.exception.mach-lookup.global-name</key>
+	<array>
+		<string>com.apple.donotdisturb.service</string>
+		<string>com.apple.donotdisturb.service.non-launching</string>
+		<string>com.apple.usernotifications.accessorynotifications</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.sharedpclogging</string>

```
### captiveagent

> `/usr/libexec/captiveagent`

```diff

 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>com.apple.captiveagent</string>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 </dict>

```
### caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

 	<true/>
 	<key>com.apple.private.CarPlayUIServices.cluster-theme</key>
 	<true/>
+	<key>com.apple.private.appintents-attribution-override</key>
+	<true/>
 	<key>com.apple.private.carkit.sessionBoost</key>
 	<true/>
 	<key>com.apple.private.carp</key>
 	<true/>
+	<key>com.apple.private.corespotlight.internal</key>
+	<true/>
+	<key>com.apple.private.corespotlight.search.internal</key>
+	<true/>
 	<key>com.apple.private.externalaccessory.showallaccessories</key>
 	<true/>
+	<key>com.apple.private.intelligenceplatform.client-identifier</key>
+	<string>com.apple.caraccessoryd</string>
+	<key>com.apple.private.intelligenceplatform.use-cases</key>
+	<dict>
+		<key>CarPlayMedia</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>CarPlay.RadioStation</key>
+				<dict>
+					<key>mode</key>
+					<string>read-only</string>
+				</dict>
+			</dict>
+		</dict>
+	</dict>
 	<key>com.apple.runningboard.caraccessoryd</key>
 	<true/>
 	<key>com.apple.runningboard.launchprocess</key>
 	<true/>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.carkit.app.service</string>
+		<string>com.apple.biome.access.system</string>
 		<string>com.apple.CarPlayApp.cluster-theme-service</string>
 		<string>com.apple.caraccessoryframework.cardata</string>
+		<string>com.apple.biome.access.user</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>

```
### com.apple.Safari.History

> `/usr/libexec/com.apple.Safari.History`

```diff

 	<array>
 		<string>com.apple.SafariCloudHistoryPushAgent</string>
 	</array>
+	<key>com.apple.security.exception.shared-preference.read-only</key>
+	<array>
+		<string>com.apple.mobilesafari</string>
+	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
 		<string>com.apple.SafariCloudHistoryPushAgent</string>

 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.safari.history</string>
+		<string>com.apple.Safari.WBSDevice</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### coreduetd

> `/usr/libexec/coreduetd`

```diff

 	<array>
 		<string>visualIdentifier</string>
 		<string>photosAutonamingView</string>
+		<string>entityTagging</string>
+		<string>hasAssociationSubgraph</string>
 	</array>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>

 	<array>
 		<string>com.apple.RelevanceEngine</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```
### coreidvd

> `/usr/libexec/coreidvd`

```diff

 	<true/>
 	<key>com.apple.mobileactivationd.spi</key>
 	<true/>
+	<key>com.apple.nano.nanoregistry.generalaccess</key>
+	<true/>
 	<key>com.apple.nanopassd.connect</key>
 	<true/>
 	<key>com.apple.nfcd.hce</key>

```
### cryptexd

> `/usr/libexec/cryptexd`

```diff

 	<true/>
 	<key>com.apple.runningboard.terminateprocess</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleImage4UserClient</string>

```
### dasd

> `/usr/libexec/dasd`

```diff

 	</array>
 	<key>com.apple.private.write-kr-experiment-factors</key>
 	<true/>
+	<key>com.apple.private.xpc.allowed-get-service-name</key>
+	<true/>
 	<key>com.apple.purplebuddy.budd.access</key>
 	<true/>
 	<key>com.apple.rootless.storage.coreduet_knowledge_store</key>

```
### demod

> `/usr/libexec/demod`

```diff

 	<true/>
 	<key>com.apple.springboard.allHomeScreenApplicationBundleIdentifiers</key>
 	<true/>
+	<key>com.apple.springboard.homeScreenIconStyle</key>
+	<true/>
+	<key>com.apple.springboard.homeScreenLayout</key>
+	<true/>
 	<key>com.apple.springboard.iconState</key>
 	<true/>
 	<key>com.apple.springboard.iconState.mutate</key>
 	<true/>
+	<key>com.apple.springboard.largeIconLayout</key>
+	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>
 	<array>
 		<string>demoloop-demod</string>
 	</array>
 	<key>com.apple.springboard.remote-alert</key>
 	<true/>
+	<key>com.apple.springboard.resetHomeScreenLayout</key>
+	<true/>
 	<key>com.apple.springboard.testautomation</key>
 	<true/>
 	<key>com.apple.timed</key>

```
### deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.deviceaccessd</string>
+	<key>aps-connection-initiate</key>
+	<true/>
+	<key>aps-environment</key>
+	<string>production</string>
 	<key>com.apple.DeviceAccess.private</key>
 	<true/>
 	<key>com.apple.bluetooth.custom.properties.writable</key>

 	<true/>
 	<key>com.apple.companionappd.connect.allow</key>
 	<true/>
+	<key>com.apple.developer.accessory-data-provider</key>
+	<true/>
 	<key>com.apple.developer.accessory-setup-discovery-extension</key>
 	<true/>
 	<key>com.apple.developer.accessory-transport-extension</key>
 	<true/>
+	<key>com.apple.developer.accessory-transport-security</key>
+	<true/>
 	<key>com.apple.developer.device-information.user-assigned-device-name</key>
 	<true/>
 	<key>com.apple.developer.media-device-discovery-extension</key>
 	<true/>
+	<key>com.apple.private.appstorecomponents</key>
+	<true/>
+	<key>com.apple.private.appstorecomponents.media-client-id</key>
+	<string>com.apple.deviceaccessd</string>
+	<key>com.apple.private.appstorecomponents.media-client-version</key>
+	<string>1</string>
+	<key>com.apple.private.aps-connection-initiate</key>
+	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>

 	</array>
 	<key>com.apple.private.tcc.manager.access.modify</key>
 	<array>
+		<string>kTCCServiceAccessoryAutomaticAudioSwitching</string>
+		<string>kTCCServiceAccessoryLiveActivities</string>
+		<string>kTCCServiceAccessoryNotifications</string>
 		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
-		<string>kTCCServiceAccessoryNotifications</string>
 	</array>
 	<key>com.apple.private.tcc.manager.access.read</key>
 	<array>
+		<string>kTCCServiceAll</string>
+		<string>kTCCServiceAccessoryAutomaticAudioSwitching</string>
+		<string>kTCCServiceAccessoryLiveActivities</string>
+		<string>kTCCServiceAccessoryNotifications</string>
 		<string>kTCCServiceAccessoryWiFiNetworkSharing</string>
 		<string>kTCCServiceBluetoothAlways</string>
-		<string>kTCCServiceAccessoryNotifications</string>
-		<string>kTCCServiceAll</string>
 	</array>
 	<key>com.apple.private.tcc.manager.service-override.modify</key>
 	<array>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.aps.deviceaccessd</string>
+		<string>com.apple.apsd</string>
 		<string>com.apple.nehelper</string>
 		<string>com.apple.server.bluetooth.le.att.xpc</string>
 		<string>com.apple.private.corewifi-xpc</string>

 		<string>com.apple.wifip2pd</string>
 		<string>com.apple.AccessorySetupUI</string>
 		<string>com.apple.AccessorySetupUI.services.presenter</string>
+		<string>com.apple.appstorecomponentsd.xpc</string>
+		<string>com.apple.ProductKitService</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	</array>
 	<key>com.apple.security.exception.shared-preference.read-write</key>
 	<array>
+		<string>com.apple.AppStoreComponents</string>
 		<string>com.apple.DeviceAccess</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```
### diskimagesiod

> `/usr/libexec/diskimagesiod`

```diff

 <dict>
 	<key>com.apple.diskimages.io-uc</key>
 	<true/>
+	<key>com.apple.private.amber.client</key>
+	<true/>
 	<key>com.apple.private.apfs.no-padding</key>
 	<true/>
 	<key>com.apple.private.diskarbitrationd.access</key>

```
### dmd

> `/usr/libexec/dmd`

```diff

 	<true/>
 	<key>com.apple.private.security.storage.AppDataContainers</key>
 	<true/>
+	<key>com.apple.private.security.storage.ManagedConfiguration</key>
+	<true/>
 	<key>com.apple.private.sysdiagnose</key>
 	<true/>
 	<key>com.apple.private.system-keychain</key>

```
### fairplaydeviceidentityd

> `/usr/libexec/fairplaydeviceidentityd`

```diff

 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>TF31PAB6aO8KAbPyNKSxKA</string>
+		<string>re6Zb+zwFKJNlkQTUeT+/w</string>
+		<string>VasUgeSzVyHdB27g2XpN0g</string>
+		<string>nFRqKto/RuQAV1P+0/qkBA</string>
 	</array>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>

```
### findmydeviced

> `/usr/libexec/findmydeviced`

```diff

 	<true/>
 	<key>com.apple.private.iokit.system-nvram-internal-allow</key>
 	<true/>
-	<key>com.apple.private.ndoagent</key>
-	<true/>
 	<key>com.apple.private.octagon</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 		<string>com.apple.nanoprefsyncd</string>
 		<string>systemgroup.com.apple.icloud.searchpartyd.sharedsettings</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<string>com_apple_driver_FairPlayIOKitUserClient</string>
 	<key>com.apple.security.network.client</key>

```
### findmylocated

> `/usr/libexec/findmylocated`

```diff

 		<string>UserAssignedDeviceName</string>
 		<string>SerialNumber</string>
 	</array>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.findmy</string>
+	</array>
 	<key>com.apple.private.biome.read-write</key>
 	<array>
 		<string>FindMy.ContactActivity</string>

```
### finish_demo_restore

> `/usr/libexec/finish_demo_restore`

```diff

 </dict>
 </plist>
 
+<!-- Launch Constraints (Parent) -->
+{
+  "appl": 1,
+  "ccat": 0,
+  "comp": 1,
+  "reqs": {
+    "is-init-proc": true
+  },
+  "vers": 1
+}
+

```
### frauddefensed

> `/usr/libexec/frauddefensed`

```diff

 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
+		<string>/private/var/mobile/Library/Caches/com.apple.frauddefensed/</string>
 		<string>/private/var/mobile/tmp/</string>
 		<string>/private/var/mobile/Containers/Data/InternalDaemon/</string>
 	</array>

 	<array>
 		<string>AGXDeviceUserClient</string>
 		<string>H11ANEInDirectPathClient</string>
+		<string>H1xANELoadBalancerDirectPathClient</string>
+		<string>IOAccelContext2</string>
+		<string>IOAccelDevice2</string>
+		<string>IOAccelSharedUserClient2</string>
+		<string>IOAccelSubmitter2</string>
+		<string>IOGPUDeviceUserClient</string>
+		<string>IOMobileFramebufferUserClient</string>
+		<string>IOSurfaceAcceleratorClient</string>
 		<string>IOSurfaceRootUserClient</string>
 	</array>
 	<key>com.apple.security.network.client</key>

```

### 🆕 icloudwebd

> `/usr/libexec/icloudwebd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.authkit.client.private</key>
	<true/>
	<key>com.apple.cdp.walrus</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>com.apple.icloudweb</string>
	<key>com.apple.fileprovider.acl-read</key>
	<true/>
	<key>com.apple.fileprovider.enumerate</key>
	<true/>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.aps-connection-initiate</key>
	<true/>
	<key>com.apple.private.clouddocs.can-get-ckrecordid</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.ids.messaging</key>
	<array>
		<string>com.apple.private.alloy.icloudweb</string>
	</array>
	<key>com.apple.private.ids.messaging.urgent-priority</key>
	<array>
		<string>com.apple.private.alloy.icloudweb</string>
	</array>
	<key>com.apple.private.ids.registration</key>
	<array>
		<string>com.apple.private.alloy.icloudweb</string>
	</array>
	<key>com.apple.private.ids.remoteurlconnection</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>temporary-sandbox</string>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServicePhotos</string>
	</array>
	<key>com.apple.private.usernotifications.bundle-identifiers</key>
	<array>
		<string>com.apple.icloudwebd</string>
	</array>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.application-groups</key>
	<string>com.apple.icloudwebd</string>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Containers/Shared/AppGroup/</string>
		<string>/Library/Mobile Documents/</string>
		<string>/Library/Application Support/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.imfoundation.IMRemoteURLConnectionAgent</string>
		<string>com.apple.ak.symmetrickey.xpc</string>
		<string>com.apple.apsd</string>
		<string>com.apple.identityservicesd.idquery.embedded.auth</string>
		<string>com.apple.usernotifications.listener</string>
		<string>com.apple.usernotifications.usernotificationservice</string>
		<string>com.apple.photos.service</string>
		<string>com.apple.FileProvider</string>
		<string>com.apple.bird</string>
		<string>com.apple.kvsd</string>
		<string>com.apple.cdp.daemon</string>
	</array>
	<key>com.apple.security.exception.process-info</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.icloudwebd</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.ts.identity-services-client</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<string>com.apple.icloudwebd</string>
	<key>com.apple.spotlight.photos.entitledattributes</key>
	<true/>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>platform-application</key>
	<true/>
</dict>
</plist>

```
### inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

 	<true/>
 	<key>com.apple.nfcd.hwmanager</key>
 	<true/>
+	<key>com.apple.private.SoftwareUpdate.Client.DisableBackgroundScan</key>
+	<true/>
+	<key>com.apple.private.SoftwareUpdate.Client.InBoxUpdater</key>
+	<true/>
 	<key>com.apple.private.applesmc.user-access</key>
 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
 	<key>com.apple.private.corewifi.bssid</key>
 	<true/>
+	<key>com.apple.private.iokit.limitedpower-wakerequest</key>
+	<true/>
 	<key>com.apple.private.iokit.soc-limit</key>
 	<true/>
 	<key>com.apple.private.mobileinboxupdater.loopback-server</key>
 	<true/>
+	<key>com.apple.private.security.daemon-container</key>
+	<true/>
 	<key>com.apple.private.security.no-sandbox</key>
 	<true/>
 	<key>com.apple.private.softwareupdated.OSUpdate</key>

```
### inputanalyticsd

> `/usr/libexec/inputanalyticsd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.inputanalyticsd</string>
+	<key>aps-connection-initiate</key>
+	<true/>
+	<key>com.apple.QuartzCore.global-capture</key>
+	<true/>
+	<key>com.apple.QuartzCore.secure-capture</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.feedbackd.remote-evaluation</key>
 	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
+	<key>com.apple.intelligenceflow.uiContext</key>
+	<true/>
 	<key>com.apple.private.intelligenceplatform.client-identifier</key>
 	<string>com.apple.inputanalyticsd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>GeneratedImageImageInteraction</key>
+		<dict>
+			<key>Streams</key>
+			<dict>
+				<key>GenerativeExperiences.GeneratedImageFeatures.ImageInteraction</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>GeneratedImageUserInteraction</key>
 		<dict>
 			<key>Streams</key>

 	</dict>
 	<key>com.apple.private.sandbox.profile:embedded</key>
 	<string>temporary-sandbox</string>
+	<key>com.apple.private.stickers</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>private/var/db/eligibilityd/eligibility.plist</string>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.siri.context.service</string>
+		<string>com.apple.ctcategories.service</string>
+		<string>com.apple.intelligenceflow.uiContext</string>
+		<string>com.apple.stickers.api</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.feedbackd.centralized-feedback</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.SBUserNotification</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<string>com.apple.inputanalyticsd</string>
 	<key>com.apple.security.ts.xpc-service-name</key>
 	<string>com.apple.duetactivityscheduler</string>
+	<key>com.apple.springboard.CFUserNotification</key>
+	<true/>
 	<key>keychain-access-groups</key>
 	<array>
 		<string>com.apple.openai</string>

```
### intelligentroutingd

> `/usr/libexec/intelligentroutingd`

```diff

 	<true/>
 	<key>com.apple.avfoundation.allows-access-to-device-list</key>
 	<true/>
+	<key>com.apple.developer.homekit</key>
+	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 		<string>App.InFocus</string>
 		<string>Media.Route</string>
 		<string>FrontBoard.DisplayLayout</string>
-		<string>Device.Metadata</string>
+		<string>HomeKit.Client.AccessoryControl</string>
+		<string>HomeKit.Client.ActionSet</string>
+		<string>HomeKit.Client.MediaAccessoryControl</string>
 	</array>
+	<key>com.apple.private.homekit</key>
+	<true/>
 	<key>com.apple.private.nearbyinteraction.device-presence</key>
 	<true/>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
 	<true/>
+	<key>com.apple.private.tcc.allow</key>
+	<array>
+		<string>kTCCServiceWillow</string>
+	</array>
 	<key>com.apple.proximitycontrol</key>
 	<true/>
 	<key>com.apple.proximitycontrol.lockscreenControls</key>

 		<string>com.apple.lsd.mapdb</string>
 		<string>com.apple.milod.xpc.service</string>
 		<string>com.apple.duetactivityscheduler</string>
+		<string>com.apple.homed.xpc</string>
+		<string>com.apple.tccd</string>
+		<string>com.apple.SystemConfiguration.configd</string>
+		<string>com.apple.IntelligentRoutingDaemonLLMService</string>
 	</array>
 </dict>
 </plist>

```
### linkd

> `/usr/libexec/linkd`

```diff

 	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
+	<key>com.apple.private.appintents.exception.allow-foreign-bundle-identifiers</key>
+	<true/>
 	<key>com.apple.private.appintents.extension-host</key>
 	<true/>
+	<key>com.apple.private.appintents.live-entities.admin</key>
+	<true/>
+	<key>com.apple.private.appintents.live-entities.write</key>
+	<array>
+		<string>maps.currentNavigation.3p</string>
+	</array>
 	<key>com.apple.private.biome.read-only</key>
 	<true/>
 	<key>com.apple.private.biome.read-write</key>

 	<string>com.apple.linkd</string>
 	<key>com.apple.private.intelligenceplatform.use-cases</key>
 	<dict>
+		<key>AppIntentsSuggestedEntity</key>
+		<dict>
+			<key>Sets</key>
+			<dict>
+				<key>App.Intents.SuggestedEntity</key>
+				<dict>
+					<key>mode</key>
+					<string>read-write</string>
+				</dict>
+			</dict>
+		</dict>
 		<key>AppIntentsTranscript</key>
 		<dict>
 			<key>Streams</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.linkd.suggestedentities</string>
 		<string>com.apple.mobile.installd</string>
 		<string>com.apple.siriknowledged.koa.donate</string>
 		<string>com.apple.extensionkitservice</string>

```
### locationd

> `/usr/libexec/locationd`

```diff

 	<true/>
 	<key>com.apple.6cc862169404427cfc3cbc40099ce681</key>
 	<true/>
+	<key>com.apple.AccessorySensorManager</key>
+	<true/>
 	<key>com.apple.AudioAccessoryServices</key>
 	<true/>
 	<key>com.apple.AudioAccessorySystemStateService</key>

 		<string>com.apple.mobileasset.autoasset</string>
 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.siri.uaf.subscription.service</string>
+		<string>com.apple.AccessorySensorManager</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<array>
 		<string>kern.sleeptime</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleBasebandPCIUserClient</string>

```

### 🆕 lskdP7d

> `/usr/libexec/lskdP7d`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>AvpFairPlayUserClient.access</key>
	<true/>
	<key>com.apple.private.assets.accessible-asset-types</key>
	<array>
		<string>com.apple.MobileAsset.AppleKeyServicesCRL2</string>
	</array>
	<key>com.apple.private.security.no-sandbox</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.lskdd</string>
	<key>fairplay-client</key>
	<string>1705639473</string>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.security.system-group-containers</key>
	<array>
		<string>systemgroup.com.apple.lskdrl</string>
	</array>
	<key>com.apple.keystore.fairplay</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>com_apple_driver_KeyDeliveryIOKitUserClient</string>
		<string>com_apple_driver_FairPlayIOKitUserClient</string>
		<string>AvpFairPlayUserClient</string>
	</array>
    <key>com.apple.security.exception.iokit-user-client-class</key>
    <array>
        <string>AvpFairPlayUserClient</string>
        <string>com_apple_driver_FairPlayIOKitUserClient</string>
        <string>com_apple_driver_TestIOKitUserClient</string>
    </array>
	<key>com.apple.rootless.storage.fpsd</key>
	<true/>
	<key>com.apple.private.security.storage.fpsd</key>
	<true/>
	<key>com.apple.private.fpsd.client</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.private.FairPlayIOKitUserClient.access</key>
	<true/>
</dict>
</plist>

```

### 🆕 manageddeviced

> `/usr/libexec/manageddeviced`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>allow-obliterate-device</key>
	<true/>
	<key>application-identifier</key>
	<string>com.apple.manageddeviced</string>
	<key>aps-connection-initiate</key>
	<true/>
	<key>com.apple.BTServer.allowRestrictedServices</key>
	<true/>
	<key>com.apple.CommCenter.fine-grained</key>
	<array>
		<string>spi</string>
		<string>identity</string>
		<string>vinyl-standalone</string>
	</array>
	<key>com.apple.Contacts.database-allow</key>
	<true/>
	<key>com.apple.GAX.SPI</key>
	<true/>
	<key>com.apple.MobileInternetSharing.allow</key>
	<true/>
	<key>com.apple.SystemConfiguration.SCPreferences-write-access</key>
	<array>
		<string>com.apple.AutoWake.xml</string>
		<string>preferences.plist</string>
	</array>
	<key>com.apple.appletv.pbs.allow-active-application</key>
	<true/>
	<key>com.apple.appletv.pbs.osupdate-service-access</key>
	<true/>
	<key>com.apple.appstored.install-apps</key>
	<true/>
	<key>com.apple.appstored.private</key>
	<true/>
	<key>com.apple.appstored.xpc.updates</key>
	<true/>
	<key>com.apple.apsd.ios-device-push-token</key>
	<true/>
	<key>com.apple.avfoundation.allow-system-wide-context</key>
	<true/>
	<key>com.apple.avfoundation.allows-access-to-device-list</key>
	<true/>
	<key>com.apple.avfoundation.allows-set-output-device</key>
	<true/>
	<key>com.apple.bluetooth.system</key>
	<true/>
	<key>com.apple.bulletinboard.settings</key>
	<true/>
	<key>com.apple.developer.device-information.user-assigned-device-name</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.frontboard.shutdown</key>
	<true/>
	<key>com.apple.frontboardservices.display-layout-monitor</key>
	<true/>
	<key>com.apple.ibooks.BLService.private</key>
	<true/>
	<key>com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService.access</key>
	<true/>
	<key>com.apple.icloud.findmydeviced.access</key>
	<true/>
	<key>com.apple.itunesstored.metrics</key>
	<true/>
	<key>com.apple.itunesstored.private</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.keystore.escrow.create</key>
	<true/>
	<key>com.apple.locationd.authorizeapplications</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.locationd.emergency_enabler</key>
	<true/>
	<key>com.apple.lsapplicationproxy.deviceidentifierforvendor</key>
	<true/>
	<key>com.apple.managedconfiguration.mdmd-access</key>
	<true/>
	<key>com.apple.managedconfiguration.mdmuserd-access</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled-access</key>
	<true/>
	<key>com.apple.managedconfiguration.profiled.configurationprofiles</key>
	<array>
		<string>Inspection</string>
		<string>PopInstallationQueue</string>
		<string>Removal</string>
		<string>SilentNonUIInstallation</string>
		<string>UIInstallation</string>
		<string>CloudLockedRemoval</string>
	</array>
	<key>com.apple.managedconfiguration.profiled.get</key>
	<array>
		<string>MachineInfo</string>
		<string>ManagedApplications</string>
		<string>NetworkExtension</string>
		<string>WiFiNetworks</string>
	</array>
	<key>com.apple.managedconfiguration.profiled.provisioningprofiles</key>
	<array>
		<string>Installation</string>
		<string>PopInstallationQueue</string>
		<string>Removal</string>
		<string>Validation</string>
	</array>
	<key>com.apple.managedconfiguration.profiled.set</key>
	<array>
		<string>ActivationLock</string>
		<string>ActivationRecord</string>
		<string>Certificates</string>
		<string>ClientRestrictions</string>
		<string>CloudConfiguration</string>
		<string>Passcode</string>
		<string>Safari</string>
		<string>UserSettings</string>
	</array>
	<key>com.apple.managedconfiguration.profiled.usercompliance</key>
	<true/>
	<key>com.apple.managedconfiguration.teslad-access</key>
	<true/>
	<key>com.apple.mkb.usersession.delete</key>
	<true/>
	<key>com.apple.mkb.usersession.info</key>
	<true/>
	<key>com.apple.mkb.usersession.keybagopaquedata</key>
	<true/>
	<key>com.apple.mkb.usersession.loginwindow</key>
	<true/>
	<key>com.apple.mobile.keybagd.UserManager.bubblepop</key>
	<true/>
	<key>com.apple.multitasking.termination</key>
	<true/>
	<key>com.apple.nano.nanoregistry.generalaccess</key>
	<true/>
	<key>com.apple.private.InstallCoordination.allowed</key>
	<true/>
	<key>com.apple.private.InstallCoordination.ignoreAppProtection</key>
	<true/>
	<key>com.apple.private.InstallCoordination.ignoreRemovability</key>
	<true/>
	<key>com.apple.private.InstallCoordination.ignoreRestrictions</key>
	<true/>
	<key>com.apple.private.MobileContainerManager.otherIdLookup</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>DeviceClass</string>
		<string>ProductType</string>
		<string>ProductVersion</string>
		<string>BuildVersion</string>
		<string>SerialNumber</string>
		<string>ModelNumber</string>
		<string>UniqueDeviceID</string>
		<string>UserAssignedDeviceName</string>
		<string>DiskUsage</string>
		<string>TelephonyCapability</string>
		<string>CellularDataCapability</string>
		<string>PersonalHotspotCapability</string>
		<string>PhoneNumber</string>
		<string>EthernetMacAddress</string>
		<string>BluetoothAddress</string>
		<string>WifiAddress</string>
		<string>WifiAddressData</string>
		<string>MobileSubscriberCountryCode</string>
		<string>MobileSubscriberNetworkCode</string>
	</array>
	<key>com.apple.private.accounts.allaccounts</key>
	<true/>
	<key>com.apple.private.coreservices.canmaplsdatabase</key>
	<true/>
	<key>com.apple.private.darwin-notification.restrict-post.fmip.lostmode.enable</key>
	<true/>
	<key>com.apple.private.donotdisturb.state.request.client-identifiers</key>
	<string>com.apple.manageddeviced</string>
	<key>com.apple.private.lockdown.finegrained-get</key>
	<array>
		<string>NULL/ActivationPrivateKey</string>
		<string>NULL/DevicePrivateKey</string>
		<string>NULL/DeviceCertificate</string>
		<string>NULL/DeviceName</string>
		<string>com.apple.mobile.backup/LastCloudBackupDate</string>
	</array>
	<key>com.apple.private.lockdown.finegrained-set</key>
	<array>
		<string>NULL/DeviceName</string>
	</array>
	<key>com.apple.private.mobileinstall.allowedSPI</key>
	<array>
		<string>Uninstall</string>
		<string>Lookup</string>
		<string>CopyDiskUsageForLaunchServices</string>
		<string>UninstallForLaunchServices</string>
		<string>InstallForLaunchServices</string>
	</array>
	<key>com.apple.private.screen-time</key>
	<true/>
	<key>com.apple.private.security.storage.AppDataContainers</key>
	<true/>
	<key>com.apple.private.sysdiagnose</key>
	<true/>
	<key>com.apple.private.system-keychain</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceMediaLibrary</string>
	</array>
	<key>com.apple.private.usage-tracking</key>
	<true/>
	<key>com.apple.rootless.storage.dmd</key>
	<true/>
	<key>com.apple.security.exception.carrier-bundle.read</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-only</key>
	<array>
		<string>/private</string>
		<string>/private/var</string>
		<string>/private/var/containers/Bundle/Application/</string>
		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.installcoordinationd/Library/InstallCoordination/Removability/</string>
		<string>/private/var/db/MobileIdentityData/</string>
		<string>/private/var/MobileAsset/</string>
		<string>/private/var/MobileDevice/ProvisioningProfiles/</string>
		<string>/private/var/MobileSoftwareUpdate/</string>
		<string>/usr</string>
		<string>/usr/libexec</string>
		<string>/System</string>
	</array>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/mobile/Library/manageddeviced/</string>
		<string>/private/var/mobile/Library/Preferences/com.apple.springboard.plist</string>
		<string>/private/var/tmp/com.apple.manageddeviced/</string>
		<string>/private/var/Managed Preferences/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
	<array>
		<string>/Library/Caches/com.apple.itunesstored/url-resolution.plist</string>
		<string>/Library/com.apple.ManagedSettings/EffectiveSettings.plist</string>
		<string>/Library/InstallCoordination/removability.plist</string>
		<string>/Library/UserConfigurationProfiles/</string>
		<string>/Library/Logs/CrashReporter/</string>
	</array>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/tmp/com.apple.manageddeviced/</string>
		<string>/Library/Caches/com.apple.manageddeviced/</string>
		<string>/Library/manageddeviced/</string>
		<string>/Media/Books/Purchases/</string>
	</array>
	<key>com.apple.security.exception.framebuffer-access</key>
	<true/>
	<key>com.apple.security.exception.iokit-user-client-class</key>
	<array>
		<string>IOUSBDeviceInterfaceUserClient</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.AppSSO.service-xpc</string>
		<string>com.apple.CARenderServer</string>
		<string>com.apple.FileCoordination</string>
		<string>com.apple.GSSCred</string>
		<string>com.apple.MTLCompilerService</string>
		<string>com.apple.MobileInternetSharing</string>
		<string>com.apple.PineBoardServices</string>
		<string>com.apple.PowerManagement.control</string>
		<string>com.apple.ProgressReporting</string>
		<string>com.apple.SBUserNotification</string>
		<string>com.apple.ScreenTimeAgent.organization-status</string>
		<string>com.apple.SystemConfiguration.configd</string>
		<string>com.apple.UsageTrackingAgent</string>
		<string>com.apple.UsageTrackingAgent.private</string>
		<string>com.apple.WebKit.Networking</string>
		<string>com.apple.WebKit.WebContent</string>
		<string>com.apple.accessibility.AXBackBoardServer</string>
		<string>com.apple.accessibility.gax.backboard</string>
		<string>com.apple.accountsd.accountmanager</string>
		<string>com.apple.appstored.xpc.storequeue</string>
		<string>com.apple.cfnetwork.AuthBrokerAgent</string>
		<string>com.apple.commcenter.coretelephony.xpc</string>
		<string>com.apple.commcenter.xpc</string>
		<string>com.apple.donotdisturb.service</string>
		<string>com.apple.exchangesyncd</string>
		<string>com.apple.icloud.findmydeviced</string>
		<string>com.apple.imfoundation.IMRemoteURLConnectionAgent</string>
		<string>com.apple.installcoordinationd</string>
		<string>com.apple.iokit.powerdxpc</string>
		<string>com.apple.itunescloudd.xpc</string>
		<string>com.apple.locationd.registration</string>
		<string>com.apple.locationd.synchronous</string>
		<string>com.apple.lsd.mapdb</string>
		<string>com.apple.lsd.xpc</string>
		<string>com.apple.managedconfiguration.profiled</string>
		<string>com.apple.misagent</string>
		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
		<string>com.apple.mobile.usermanagerd.xpc</string>
		<string>com.apple.mobile.keybagd.xpc</string>
		<string>com.apple.mobileactivationd</string>
		<string>com.apple.securityd</string>
		<string>com.apple.softwareupdateservicesd</string>
		<string>com.apple.springboard.services</string>
		<string>com.apple.sysdiagnose.service.xpc</string>
		<string>com.apple.trustd</string>
		<string>com.apple.coremedia.routediscoverer.xpc</string>
		<string>com.apple.coremedia.routingcontext.xpc</string>
		<string>com.apple.coremedia.volumecontroller.xpc</string>
		<string>com.apple.airplay.apsynccontroller.xpc</string>
		<string>com.apple.mediaremoted.xpc</string>
		<string>com.apple.server.bluetooth</string>
		<string>com.apple.appstored.xpc</string>
	</array>
	<key>com.apple.security.exception.mobile-keybag-access</key>
	<true/>
	<key>com.apple.security.exception.shared-preference.read-only</key>
	<array>
		<string>com.apple.ist.AppleDirectory</string>
		<string>com.apple.purplebuddy</string>
		<string>com.apple.mobileipod</string>
		<string>com.apple.nanobuddy</string>
	</array>
	<key>com.apple.security.exception.shared-preference.read-write</key>
	<array>
		<string>com.apple.manageddeviced</string>
		<string>com.apple.softwareupdateservicesd</string>
		<string>com.apple.carrier</string>
		<string>com.apple.itunescloud</string>
		<string>com.apple.merchantd</string>
	</array>
	<key>com.apple.security.exception.sysctl.read-only</key>
	<array>
		<string>net.routetable</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.configurationprofiles</string>
		<string>systemgroup.com.apple.installcoordinationd</string>
		<string>systemgroup.com.apple.media.books.managed</string>
	</array>
	<key>com.apple.security.ts.lockdown-client</key>
	<true/>
	<key>com.apple.security.ts.mach-task-name</key>
	<true/>
	<key>com.apple.security.ts.tmpdir</key>
	<array>
		<string>com.apple.manageddeviced</string>
	</array>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.application-removability.proxy</key>
	<true/>
	<key>com.apple.springboard.opensensitiveurl</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
	<key>com.apple.surfboard.lock-screen-client</key>
	<true/>
	<key>com.apple.usermanagerd.persona.fetch</key>
	<true/>
	<key>com.apple.usermanagerd.persona.setbundle</key>
	<true/>
	<key>keychain-access-groups</key>
	<array>
		<string>apple</string>
		<string>com.apple.certificates</string>
		<string>com.apple.identities</string>
		<string>com.apple.preferences</string>
		<string>com.apple.managed.vpn.shared</string>
		<string>lockdown-identities</string>
	</array>
	<key>platform-application</key>
	<true/>
	<key>seatbelt-profiles</key>
	<array>
		<string>temporary-sandbox</string>
	</array>
</dict>
</plist>

```
### mdmd

> `/usr/libexec/mdmd`

```diff

 	<array>
 		<string>kTCCServiceMediaLibrary</string>
 	</array>
+	<key>com.apple.private.xpc.launchd.reboot</key>
+	<true/>
+	<key>com.apple.private.xpc.launchd.userspace-reboot</key>
+	<true/>
 	<key>com.apple.runningboard.process-state</key>
 	<true/>
 	<key>com.apple.security.attestation.access</key>

```
### mediaparserd

> `/usr/libexec/mediaparserd`

```diff

 		<string>com.apple.coremedia</string>
 		<string>com.apple.coreaudio</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.tailspin.dump-output</key>
 	<true/>
 	<key>platform-application</key>

```
### mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

 		<string>com.apple.UXMAssertionService</string>
 		<string>com.apple.litehudd.xpc</string>
 		<string>com.apple.carousel.connectionstatusservice</string>
+		<string>com.apple.coremedia.figvirtualcapturecard.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.security.ts.play-audio</key>
 	<true/>
 	<key>com.apple.security.ts.springboard-services</key>

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
### milod

> `/usr/libexec/milod`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.AccessorySensorManager</key>
+	<true/>
+	<key>com.apple.AudioAccessoryServices</key>
+	<true/>
 	<key>com.apple.CompanionLink</key>
 	<true/>
 	<key>com.apple.CoreRoutine.LocationOfInterest</key>

 	<true/>
 	<key>com.apple.polaris.producer.all-streams</key>
 	<true/>
+	<key>com.apple.private.AccessorySensorManager</key>
+	<true/>
 	<key>com.apple.private.avfoundation.capture.nonstandard-client.allow</key>
 	<true/>
 	<key>com.apple.private.biome.client-identifier</key>

 	<key>com.apple.private.hid.client.service-protected</key>
 	<true/>
 	<key>com.apple.private.nearbyinteraction.privileged</key>
-	<string></string>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceCamera</string>
 		<string>kTCCServiceMicrophone</string>
+		<string>kTCCServiceMotion</string>
 	</array>
 	<key>com.apple.rapport.Client</key>
 	<true/>

 		<string>com.apple.TapToRadarKit.service</string>
 		<string>com.apple.spaceattributiond</string>
 		<string>com.apple.PowerManagement.control</string>
+		<string>com.apple.polaris.systemgraph_v2</string>
+		<string>com.apple.AudioAccessoryServices</string>
+		<string>com.apple.AccessorySensorManager</string>
+		<string>com.apple.perceptiond.peripheralSensing</string>
+	</array>
+	<key>com.apple.security.exception.sysctl.read-only</key>
+	<array>
+		<string>kern.exclaves_status</string>
+		<string>kern.task_conclave</string>
+		<string>kern.bootargs</string>
 	</array>
 	<key>com.apple.spaceattribution.private</key>
 	<true/>

```
### mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

 	<true/>
 	<key>com.apple.keystore.device</key>
 	<true/>
+	<key>com.apple.keystore.fdr-access</key>
+	<true/>
 	<key>com.apple.keystore.obliterate-d-key</key>
 	<true/>
+	<key>com.apple.keystore.sik.access</key>
+	<true/>
+	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
+	<true/>
 	<key>com.apple.private.WebClips.read-write</key>
 	<true/>
 	<key>com.apple.private.admin.writeconfig</key>

 	<true/>
 	<key>com.apple.rootless.volume.iSCPreboot</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-only</key>
+	<array>
+		<string>/private/preboot/</string>
+	</array>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleSEPUserClient</string>

```
### mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

 	<true/>
 	<key>com.apple.security.attestation.access</key>
 	<true/>
-	<key>com.apple.security.exception.mach-lookup.global-name</key>
-	<array>
-		<string>com.apple.iokit.powerdxpc</string>
-		<string>com.apple.fairplayd.xpc</string>
-	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.security.system-container</key>

```
### mobileassetd

> `/usr/libexec/mobileassetd`

```diff

 	</array>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.itunesstored.private</key>
 	<true/>
 	<key>com.apple.keystore.dsme_access</key>

 	<true/>
 	<key>com.apple.networkd.allow_bootstrap_cellular_service_request</key>
 	<true/>
+	<key>com.apple.private.AppleVirtualPlatformHostInfo</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>PURGE_ENTITLEMENT</string>

 	<true/>
 	<key>com.apple.private.InstallCoordination.allowed</key>
 	<true/>
+	<key>com.apple.private.MADownloadService.Client</key>
+	<true/>
 	<key>com.apple.private.MobileAsset.ManifestStorageService</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	</array>
 	<key>com.apple.private.diskimages.kext.user-client-access</key>
 	<true/>
+	<key>com.apple.private.domain-extension</key>
+	<true/>
 	<key>com.apple.private.exclaves.conclave-host</key>
 	<true/>
 	<key>com.apple.private.image4.nonce.propose.mobile-asset</key>

 	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
+	<key>com.apple.private.mobileassetd.use-daemon-preference-logic</key>
+	<true/>
 	<key>com.apple.private.mobileassetd.use-download-dir</key>
 	<true/>
 	<key>com.apple.private.mobileinboxupdater.xpc</key>

 	<true/>
 	<key>com.apple.private.updatetransparency.client</key>
 	<true/>
+	<key>com.apple.private.vfs.entitled-reserve-access</key>
+	<true/>
 	<key>com.apple.private.vfs.exclave-fs-register</key>
 	<true/>
 	<key>com.apple.private.vfs.graftdmg</key>

 	<array>
 		<string>/private/var/run/bootSessionMA.txt</string>
 		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
-		<string>/private/var/run/MobileAssetCritialDomainsUpdated.plist</string>
+		<string>/private/var/run/MobileAssetCriticalDomainsUpdated.plist</string>
 		<string>/private/var/run/MobileAssetSuspendSystemOptionalForSoftwareUpdate.nonce</string>
 		<string>/private/var/code_coverage/</string>
 		<string>/private/var/run/com.apple.mobileassetd-AutoAsset-DeviceBoot-UUID</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.MobileAsset.DownloadService.Builtin</string>
+		<string>com.apple.MobileAsset.DownloadService.Backported</string>
 		<string>com.apple.inboxupdaterd</string>
 		<string>com.apple.springboard.blockableservices</string>
 		<string>com.apple.mobileactivationd</string>

 		<string>com.apple.mobileactivationd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleKeyStoreUserClient</string>

```
### mobilerepaird

> `/usr/libexec/mobilerepaird`

```diff

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
 	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>

```
### modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

 	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
+		<string>/private/var/db/assetsubscriptiond/</string>
 		<string>/private/var/db/com.apple.countryd/</string>
 		<string>/private/var/db/eligibilityd/eligibility.plist</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>

 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.biome.access.system</string>
 		<string>com.apple.PowerManagement.control</string>
+		<string>com.apple.siri.uaf.subscription.service</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

 		<string>1690</string>
 		<string>SIML_ADM_PERSONALIZATION_GP</string>
 		<string>SIML_ADM_PERSONALIZATION</string>
+		<string>UAF_AB_MODELCATALOG</string>
 	</array>
 	<key>platform-application</key>
 	<true/>

```
### nehelper

> `/usr/libexec/nehelper`

```diff

 	<true/>
 	<key>com.apple.private.corewifi</key>
 	<true/>
+	<key>com.apple.private.corewifi.bssid</key>
+	<true/>
 	<key>com.apple.private.neagent-client</key>
 	<true/>
 	<key>com.apple.private.neconfiguration-write-access</key>

```
### networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.osanalytics.defaults.allow</key>
+	<true/>
 	<key>com.apple.private.rtcreportingd</key>
 	<true/>
 	<key>com.apple.private.skywalk.observe-stats</key>

 	<key>com.apple.security.exception.shared-preference.read</key>
 	<array>
 		<string>com.apple.CloudSubscriptionFeatures.gmCache</string>
+		<string>com.apple.CloudSubscriptionFeatures.cache</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

```
### nsurlsessiond

> `/usr/libexec/nsurlsessiond`

```diff

 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.nsurlstoragedresources</string>
+		<string>systemgroup.com.apple.osanalytics</string>
 	</array>
 	<key>com.apple.telephony.cupolicy-monitor-access</key>
 	<true/>

```
### powerexceptionsd

> `/usr/libexec/powerexceptionsd`

```diff

 <dict>
 	<key>com.apple.PerfPowerServices.data-donation</key>
 	<true/>
+	<key>com.apple.powerui.smartcharging</key>
+	<true/>
+	<key>com.apple.private.applegraphicsdevicecontrol</key>
+	<true/>
+	<key>com.apple.private.applesmc.user-access</key>
+	<true/>
+	<key>com.apple.private.iokit.batterydata</key>
+	<true/>
 	<key>com.apple.private.kernel.override-cpumon</key>
 	<true/>
 	<key>com.apple.private.runaway-mitigation</key>
 	<true/>
+	<key>com.apple.security.exception.iokit-user-client-class</key>
+	<array>
+		<string>RootDomainUserClient</string>
+		<string>ApplePMPThermalUserClient</string>
+		<string>ApplePPMUserClient</string>
+		<string>AppleSMCClient</string>
+		<string>AppleSMCSensorDispatcherUserClient</string>
+	</array>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.powerlog</string>
 		<string>systemgroup.com.apple.osanalytics</string>
+		<string>systemgroup.com.apple.powerexceptions</string>
 	</array>
 	<key>com.apple.trial.client</key>
 	<array>

```
### promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

 	<true/>
 	<key>com.apple.private.iad.opt-in-control</key>
 	<true/>
+	<key>com.apple.private.keychain.sysbound</key>
+	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
 	<key>com.apple.private.tcc.allow</key>

 	<array>
 		<string>/usr/libexec</string>
 		<string>/private/var/containers/Bundle/Application/</string>
+	</array>
+	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
+	<array>
 		<string>/Library/Trial/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>

 		<string>com.apple.fairplaydeviceidentityd</string>
 		<string>com.apple.commcenter.coretelephony.xpc</string>
 		<string>com.apple.fairplayd.versioned</string>
+		<string>com.apple.fpsd</string>
+		<string>com.apple.fairplayd</string>
+		<string>com.apple.fairplayd.xpc</string>
 		<string>com.apple.ap.adprivacyd.opt-out</string>
 		<string>com.apple.ap.adprivacyd.idmanager</string>
 		<string>com.apple.adid</string>

```
### proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

 	<true/>
 	<key>com.apple.private.coreservices.canmaplsdatabase</key>
 	<true/>
+	<key>com.apple.private.coreservices.canopenactivity</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.homekit</key>

 		<string>com.apple.uikitservices.userInterfaceStyleMode</string>
 		<string>com.apple.UIKit</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AppleKeyStoreUserClient</string>

```
### relatived

> `/usr/libexec/relatived`

```diff

 	<true/>
 	<key>com.apple.hid.system.user-access-fast-path</key>
 	<true/>
+	<key>com.apple.locationd.accessory-vl</key>
+	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
+	<key>com.apple.polaris.client</key>
+	<true/>
 	<key>com.apple.private.attentionawareness</key>
 	<true/>
 	<key>com.apple.private.avfoundation.capture.allow</key>

 		<string>com.apple.timesync.ptp.manager</string>
 		<string>com.apple.airplay.endpoint.xpc</string>
 		<string>com.apple.mediaexperience.endpoint.xpc</string>
+		<string>com.apple.perceptiond.anst</string>
+		<string>com.apple.perceptiond.featureDetection</string>
+		<string>com.apple.perceptiond.histogram</string>
+		<string>com.apple.perceptiond.daemonWake</string>
+		<string>com.apple.perceptiond.api</string>
+		<string>com.apple.perceptiond.entitykit</string>
+		<string>com.apple.perceptiond.sceneClassification</string>
+		<string>com.apple.polaris.daemon_default</string>
+		<string>com.apple.polaris.systemgraph</string>
+		<string>com.apple.polaris.graphstore</string>
+		<string>com.apple.polaris.system</string>
+		<string>com.apple.polaris.graphexecutor</string>
+		<string>com.apple.polaris.replay</string>
+		<string>com.apple.polaris.systemtransitionservice</string>
+		<string>com.apple.polaris.systemgraph_v2</string>
+		<string>com.apple.minilab.local_res_fact</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### remindd

> `/usr/libexec/remindd`

```diff

 	</array>
 	<key>com.apple.findmy.findmylocate.settings</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.generativeexperiences.availabilityService</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.locationd.effective_bundle</key>
 	<true/>
 	<key>com.apple.locationd.region_proxy_service</key>
 	<true/>
+	<key>com.apple.locationd.usage_oracle</key>
+	<true/>
 	<key>com.apple.managedconfiguration.profiled-access</key>
 	<true/>
 	<key>com.apple.mkb.usersession.info</key>

 	<true/>
 	<key>com.apple.private.alarmkit.bundleIdentifier</key>
 	<string>com.apple.reminders</string>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.reminders</string>
+	</array>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.appintents.relevant.custom-identifier-allowed</key>
 	<true/>
 	<key>com.apple.private.aps-client-cert-access</key>

 	<true/>
 	<key>com.apple.private.cloudkit.systemService</key>
 	<true/>
+	<key>com.apple.private.coreservices.canmaplsdatabase</key>
+	<true/>
 	<key>com.apple.private.corespotlight.internal</key>
 	<true/>
 	<key>com.apple.private.dark-wake-push</key>

 	<true/>
 	<key>com.apple.private.push-to-wake</key>
 	<true/>
+	<key>com.apple.private.replicator.dataProvider</key>
+	<true/>
 	<key>com.apple.private.secure-apsclientv2</key>
 	<true/>
 	<key>com.apple.private.security.restricted-application-groups</key>

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.reminders.replicatorclient.entitlement</key>
+	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.application-groups</key>
 	<array>
 		<string>group.com.apple.reminders</string>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
-		<string>Library/Reminders/</string>
-		<string>Library/Caches/com.apple.remindd/</string>
-		<string>Library/Logs/CrashReporter/Reminders/</string>
-		<string>Library/HTTPStorages/com.apple.remindd/</string>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
 	</array>
 	<key>com.apple.security.exception.iokit-user-client-class</key>
 	<array>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.biome.access.user</string>
 		<string>com.apple.alarmkitservices</string>
+		<string>com.apple.replicatorservices</string>
+		<string>com.apple.linkd.registry</string>
+		<string>com.apple.linkd.extension</string>
+		<string>com.apple.linkd.transcript</string>
+		<string>com.apple.linkd.application-service</string>
 		<string>com.apple.appleneuralengine</string>
 		<string>com.apple.usernotifications.listener</string>
 		<string>com.apple.mobile.keybagd.xpc</string>

 		<string>com.apple.mobileassetd.v2</string>
 		<string>com.apple.modelmanager</string>
 		<string>com.apple.generativeexperiences.availabilityService</string>
+		<string>com.apple.linkd.autoShortcut</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```

### 🆕 royacaptured

> `/usr/libexec/royacaptured`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.royad.royacaptured</string>
	<key>com.apple.AccessorySensorManager</key>
	<true/>
	<key>com.apple.AudioAccessoryServices</key>
	<true/>
	<key>com.apple.VE.CVCalibration.client</key>
	<true/>
	<key>com.apple.bluetooth.doap</key>
	<true/>
	<key>com.apple.camera.iokit-user-access</key>
	<true/>
	<key>com.apple.coreaudio.CanRecordPastData</key>
	<true/>
	<key>com.apple.coreaudio.CanRecordWithoutSessionActivation</key>
	<true/>
	<key>com.apple.coreaudio.CanTapTelephony</key>
	<true/>
	<key>com.apple.coreaudio.app-tap</key>
	<true/>
	<key>com.apple.coreaudio.private.SystemWideTap</key>
	<true/>
	<key>com.apple.coreaudio.register-internal-aus</key>
	<true/>
	<key>com.apple.corespeech.supportheysiriwhenrecord</key>
	<true/>
	<key>com.apple.locationd.activity</key>
	<true/>
	<key>com.apple.locationd.effective_bundle</key>
	<true/>
	<key>com.apple.managedassets.api.serialize</key>
	<true/>
	<key>com.apple.managedassets.api.usermode</key>
	<true/>
	<key>com.apple.polaris.client</key>
	<true/>
	<key>com.apple.polaris.consumer.all-streams</key>
	<true/>
	<key>com.apple.private.AccessorySensorManager</key>
	<true/>
	<key>com.apple.private.IOSurface.protected-access</key>
	<true/>
	<key>com.apple.private.PolarisSystemTransition.access</key>
	<true/>
	<key>com.apple.private.avfoundation.background-camera-access</key>
	<true/>
	<key>com.apple.private.avfoundation.capture.allow</key>
	<true/>
	<key>com.apple.private.coreaudio.mxsessionPropertyPipe</key>
	<true/>
	<key>com.apple.private.corewifi</key>
	<true/>
	<key>com.apple.private.master-sync-generator.user-access</key>
	<true/>
	<key>com.apple.private.mediaexperience.allowrecordingduringcall</key>
	<true/>
	<key>com.apple.private.mediaexperience.prefersnointerruptions.allow</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceCamera</string>
		<string>kTCCServiceMicrophone</string>
	</array>
	<key>com.apple.roya.royacaptured.camera.allow_xpc</key>
	<true/>
	<key>com.apple.roya.royacaptured.system.allow_xpc</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.AccessorySensorManager</string>
		<string>com.apple.AudioAccessoryServices</string>
		<string>com.apple.private.corewifi-xpc</string>
		<string>com.apple.wifip2pd</string>
		<string>com.apple.roya.royacaptured.camera</string>
		<string>com.apple.roya.royacaptured.system</string>
		<string>com.apple.BTLEAudioController.xpc</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>SCodecUserClient</string>
		<string>AppleDashboardUserClient</string>
		<string>AGXDeviceUserClient</string>
		<string>AppleAVE2UserClient</string>
		<string>AppleMSGKextUserClient</string>
		<string>NBDisplayControlUserClient</string>
		<string>NBCoreUserClient</string>
		<string>NBTimesyncUserClient</string>
		<string>IOReportUserClient</string>
		<string>IOSurfaceAcceleratorClient</string>
		<string>IOSurfaceRootUserClient</string>
		<string>H11ANEInDirectPathClient</string>
		<string>IOTimeSyncClockManagerUserClient</string>
		<string>IOTimeSyncDomainUserClient</string>
		<string>IOTimeSyncgPTPManagerUserClient</string>
		<string>IOTimeSyncNetworkPortUserClient</string>
		<string>AFKEndpointInterfaceUserClient</string>
		<string>iokit-open-user-client</string>
		<string>RootDomainUserClient</string>
		<string>AppleSPUFastpathDriverUserClient</string>
		<string>VDKDriverUserClient</string>
		<string>PSTDriverServerUserClient</string>
		<string>AppleMSGKextEPICUserClient</string>
		<string>IOHIDLibUserClient</string>
	</array>
	<key>com.apple.security.ts.play-audio</key>
	<true/>
	<key>com.apple.security.ts.play-media</key>
	<true/>
	<key>com.apple.wifi.manager-access</key>
	<true/>
	<key>com.apple.wifi.peer_traffic_registration</key>
	<true/>
	<key>com.apple.wifip2pd</key>
	<true/>
</dict>
</plist>

```
### runningboardd

> `/usr/libexec/runningboardd`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>com.apple.PerfPowerServices.data-donation</key>
+	<true/>
 	<key>com.apple.agx.gpurole</key>
 	<true/>
 	<key>com.apple.frontboardservices.display-layout-monitor</key>

 	</array>
 	<key>com.apple.private.xpc.domain-extension.proxy</key>
 	<true/>
+	<key>com.apple.private.xpc.launchd.allow-posixspawn-telemetry</key>
+	<true/>
 	<key>com.apple.private.xpc.launchd.app-server</key>
 	<true/>
 	<key>com.apple.private.xpc.launchd.job-manager</key>

 	<array>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
 	</array>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/root/Library/Caches/com.apple.runningboardd/</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.runningboardd</string>
+		<string>com.apple.coreos.fast</string>
+	</array>
 	<key>com.apple.spd.anypidmonitoring</key>
 	<true/>
 	<key>com.apple.tailspin.dump-output</key>

```
### searchpartyd

> `/usr/libexec/searchpartyd`

```diff

 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.appintents.allowed-bundle-identifiers</key>
+	<array>
+		<string>com.apple.findmy</string>
+	</array>
 	<key>com.apple.private.applecredentialmanager.allow</key>
 	<true/>
 	<key>com.apple.private.aps-connection-initiate</key>

```

### 🆕 securepairingd

> `/usr/libexec/securepairingd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.keystore.access-keychain-keys</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.private.exclaves.conclave-host</key>
	<true/>
	<key>com.apple.private.isolated.audio.coreaudioclient</key>
	<true/>
	<key>com.apple.private.mediaexperience.usesecuresession</key>
	<true/>
	<key>com.apple.security.exception.files.absolute-path.read-write</key>
	<array>
		<string>/private/var/tmp/</string>
		<string>/private/var/mobile/tmp/AudioCapture/</string>
		<string>/dev/exfiltration-adc-securepairi</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
</dict>
</plist>

```
### securityd

> `/usr/libexec/securityd`

```diff

 		<string>com.apple.AuthenticationServices.CredentialSharingGroups</string>
 		<string>com.apple.security.KeychainDBMover</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.network.client</key>
 	<true/>
 	<key>com.apple.springboard.opensensitiveurl</key>

```
### sensingpredictd

> `/usr/libexec/sensingpredictd`

```diff

 <dict>
 	<key>com.apple.AudioAccessoryServices</key>
 	<true/>
-	<key>com.apple.afk.shmem-user</key>
-	<true/>
-	<key>com.apple.afk.user</key>
-	<true/>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.sensingpredictd</string>
 	<key>com.apple.bluetooth.system</key>
 	<true/>
 	<key>com.apple.polaris.client</key>
 	<true/>
-	<key>com.apple.private.exclaves.conclave-host</key>
-	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTTCServiceBluetoothPeripheral</string>

```
### seserviced

> `/usr/libexec/seserviced`

```diff

 	<true/>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.feedbackd.client-forms</key>
+	<array>
+		<string>framework-car-key</string>
+	</array>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
 	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>

 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
+		<string>com.apple.symptom_diagnostics</string>
 		<string>com.apple.NPKCompanionAgent.Server</string>
 		<string>com.apple.softposreaderd</string>
 		<string>com.apple.SBUserNotification</string>

 		<string>com.apple.surfboard.applicationservice</string>
 		<string>com.apple.surfboard.scenesessionservice</string>
 		<string>com.apple.spotlight.IndexAgent</string>
+		<string>com.apple.feedbackd.xpc</string>
 	</array>
 	<key>com.apple.security.exception.process-info</key>
 	<true/>

```
### sharingd

> `/usr/libexec/sharingd`

```diff

 	</array>
 	<key>com.apple.CompanionLink</key>
 	<true/>
+	<key>com.apple.DeviceAccess</key>
+	<true/>
+	<key>com.apple.DeviceAccess.private</key>
+	<true/>
 	<key>com.apple.HearingModeService</key>
 	<true/>
 	<key>com.apple.MobileInternetSharing.allow</key>

 	<array>
 		<string>SensitiveContentAnalysis.MediaAnalysis</string>
 		<string>SensitiveContentAnalysis.UIInteraction</string>
+		<string>MLSE.ShareSheet.Metrics.SystemResourceUsage</string>
 	</array>
 	<key>com.apple.private.biometrickit.allow-connect</key>
 	<true/>

 		<string>com.apple.corecaptured</string>
 		<string>com.apple.coreduetd.knowledge</string>
 		<string>com.apple.corefollowup.agent</string>
+		<string>com.apple.DeviceAccess.xpc</string>
 		<string>com.apple.mediaanalysisd.analysis</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.DocumentManagerCore.Downloads</string>

```
### splashboardd

> `/usr/libexec/splashboardd`

```diff

 <dict>
 	<key>com.apple.QuartzCore.secure-mode</key>
 	<true/>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
 	<key>com.apple.security.iokit-user-client-class</key>
 	<array>
 		<string>AGXCommandQueue</string>

```

### 🆕 spotlightknowledged.graph

> `/usr/libexec/spotlightknowledged.graph`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.spotlightknowledged</string>
	<key>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</key>
	<true/>
	<key>com.apple.apfs.unlock</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.keystore.allow.background-processing-assertions</key>
	<true/>
	<key>com.apple.mobileassetd.v2</key>
	<true/>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>CLIENT_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.ciphermld.allow</key>
	<true/>
	<key>com.apple.private.corespotlight.allownotifications</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.sender</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.spotlightknowledge</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>AppEntityDonation</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>App.Intents.IndexedEntity</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>PowerHUD</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Spotlight.Operations</key>
				<string>read-write</string>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
	</array>
	<key>com.apple.private.iokit.powersource-control</key>
	<true/>
	<key>com.apple.private.security.storage.Spotlight</key>
	<true/>
	<key>com.apple.private.spotlight.openjournal</key>
	<true/>
	<key>com.apple.private.suggestions.spotlightknowledged</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ciphermld</string>
		<string>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.SetStoreUpdateService</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.linkd.registry</string>
	</array>
	<key>com.apple.security.exception.mach-register.global-name</key>
	<array>
		<string>com.apple.spotlightknowledged</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.spotlight.entitledattributes</key>
	<true/>
	<key>com.apple.tailspin.dump-output</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>333</string>
	</array>
</dict>
</plist>

```

### 🆕 spotlightknowledged.updater

> `/usr/libexec/spotlightknowledged.updater`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.spotlightknowledged</string>
	<key>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</key>
	<true/>
	<key>com.apple.apfs.unlock</key>
	<true/>
	<key>com.apple.coreduetd.allow</key>
	<true/>
	<key>com.apple.coreduetd.context</key>
	<true/>
	<key>com.apple.duet.activityscheduler.allow</key>
	<true/>
	<key>com.apple.intelligenceplatform.View</key>
	<true/>
	<key>com.apple.keystore.allow.background-processing-assertions</key>
	<true/>
	<key>com.apple.mobileassetd.v2</key>
	<true/>
	<key>com.apple.private.CacheDelete</key>
	<array>
		<string>CLIENT_ENTITLEMENT</string>
	</array>
	<key>com.apple.private.ciphermld.allow</key>
	<true/>
	<key>com.apple.private.corespotlight.allownotifications</key>
	<true/>
	<key>com.apple.private.corespotlight.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.search.internal</key>
	<true/>
	<key>com.apple.private.corespotlight.sender</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.spotlightknowledge</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>AppEntityDonation</key>
		<dict>
			<key>Sets</key>
			<dict>
				<key>App.Intents.IndexedEntity</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
		<key>PowerHUD</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Spotlight.Operations</key>
				<string>read-write</string>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.intelligenceplatform.views.read-only</key>
	<array>
		<string>visualIdentifier</string>
	</array>
	<key>com.apple.private.iokit.powersource-control</key>
	<true/>
	<key>com.apple.private.security.storage.Spotlight</key>
	<true/>
	<key>com.apple.private.spotlight.openjournal</key>
	<true/>
	<key>com.apple.private.suggestions.spotlightknowledged</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.ciphermld</string>
		<string>com.apple.TextUnderstanding.DocumentUnderstandingHarvesting</string>
		<string>com.apple.duetactivityscheduler</string>
		<string>com.apple.intelligenceplatform.View</string>
		<string>com.apple.SetStoreUpdateService</string>
		<string>com.apple.biome.access.user</string>
		<string>com.apple.biome.access.system</string>
		<string>com.apple.mediaanalysisd.service.public</string>
		<string>com.apple.linkd.registry</string>
	</array>
	<key>com.apple.security.exception.mach-register.global-name</key>
	<array>
		<string>com.apple.spotlightknowledged</string>
	</array>
	<key>com.apple.security.hardened-process</key>
	<true/>
	<key>com.apple.security.hardened-process.checked-allocations</key>
	<true/>
	<key>com.apple.spotlight.entitledattributes</key>
	<true/>
	<key>com.apple.tailspin.dump-output</key>
	<true/>
	<key>com.apple.trial.client</key>
	<array>
		<string>333</string>
	</array>
</dict>
</plist>

```
### storagekitd

> `/usr/libexec/storagekitd`

```diff

 		<string>CLIENT_ENTITLEMENT</string>
 		<string>PURGEABLE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.LiveFS.connection</key>
+	<true/>
 	<key>com.apple.private.diskarbitrationd.access</key>
 	<true/>
 	<key>com.apple.private.sandbox.profile:embedded</key>

```
### symptomsd

> `/usr/libexec/symptomsd`

```diff

 	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### symptomsd-distributed

> `/usr/libexec/symptomsd-distributed`

```diff

 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.symptoms.NetworkDiagnostics</key>
 	<true/>
 </dict>

```
### symptomsd-helper

> `/usr/libexec/symptomsd-helper`

```diff

 	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.osanalytics</string>

```
### sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

 	<true/>
 	<key>com.apple.hid.AppleDeviceManagementHIDFilter.entitlement</key>
 	<true/>
+	<key>com.apple.hid.manager.user-access-protected</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.Sysdiagnose</key>
 	<true/>
 	<key>com.apple.managedconfiguration.profiled.profile</key>

 		<integer>1</integer>
 		<integer>2</integer>
 		<integer>3</integer>
+		<integer>4</integer>
+		<integer>5</integer>
 	</array>
 	<key>com.apple.triald.internal</key>
 	<true/>

```
### terminusd

> `/usr/libexec/terminusd`

```diff

 	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.srp-mdns-proxy.proxy</key>
 	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>

```
### textunderstandingd

> `/usr/libexec/textunderstandingd`

```diff

 <dict>
 	<key>application-identifier</key>
 	<string>com.apple.textunderstandingd</string>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
+	<key>com.apple.appprotectiond.guard.access</key>
+	<true/>
+	<key>com.apple.appprotectiond.read.access</key>
+	<true/>
 	<key>com.apple.corespotlight.privateindex.unsandboxed</key>
 	<true/>
 	<key>com.apple.fileprovider.acl-read</key>

 	<true/>
 	<key>com.apple.finance.private</key>
 	<true/>
+	<key>com.apple.frontboard.launchapplications</key>
+	<true/>
 	<key>com.apple.intelligenceplatform.EntityResolution</key>
 	<true/>
 	<key>com.apple.intelligenceplatform.View</key>
 	<true/>
+	<key>com.apple.linkd.registry</key>
+	<true/>
+	<key>com.apple.linkd.transcript.privileged</key>
+	<true/>
 	<key>com.apple.mediaanalysisd.analysis</key>
 	<true/>
 	<key>com.apple.mediaanalysisd.client</key>

 	<true/>
 	<key>com.apple.modelmanager.inference</key>
 	<true/>
+	<key>com.apple.private.appintents.extension-host</key>
+	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>
 	<array>
 		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>

 	<string>temporary-sandbox</string>
 	<key>com.apple.private.security.storage.Mail</key>
 	<true/>
+	<key>com.apple.private.security.storage.Messages</key>
+	<true/>
 	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
 	<true/>
 	<key>com.apple.private.security.storage.Suggestions</key>

 	<true/>
 	<key>com.apple.proactive.experiments.responses</key>
 	<true/>
+	<key>com.apple.rootless.storage.shortcuts</key>
+	<true/>
+	<key>com.apple.runningboard.launchprocess</key>
+	<true/>
+	<key>com.apple.runningboard.process-state</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>

 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-only</key>
 	<array>
+		<string>/Library/com.apple.PrivacyDisclosure/</string>
 		<string>/Library/Mail/AttachmentData/</string>
+		<string>/Library/Messages/Attachments/</string>
+		<string>/Library/SMS/Attachments/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>
+		<string>/Library/Shortcuts/</string>
 		<string>/Library/TextUnderstanding/</string>
 		<string>/Library/Suggestions/</string>
 		<string>/Library/PersonalizationPortrait/</string>

 		<string>com.apple.biome.compute.source.user</string>
 		<string>com.apple.cache_delete.public</string>
 		<string>com.apple.proactive.PersonalizationPortrait.TextUnderstanding</string>
+		<string>com.apple.FileProvider</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

```
### thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

 	<array>
 		<string>kern.wake_abs_time</string>
 	</array>
+	<key>com.apple.security.hardened-process</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations</key>
+	<true/>
+	<key>com.apple.security.hardened-process.checked-allocations.soft-mode</key>
+	<true/>
 	<key>com.apple.security.ts.power-assertions</key>
 	<true/>
 	<key>com.apple.systemapp.allowsShutdown</key>

```
### tipsd

> `/usr/libexec/tipsd`

```diff

 	<array>
 		<string>com.apple.tipsd</string>
 	</array>
+	<key>com.apple.developer.icloud-services</key>
+	<array>
+		<string>CloudKit</string>
+	</array>
 	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
 	<string>com.apple.tipsd</string>
 	<key>com.apple.developer.usernotifications.time-sensitive</key>
 	<true/>
 	<key>com.apple.frontboard.launchapplications</key>
 	<true/>
+	<key>com.apple.generativeexperiences.generativeexperiencessession</key>
+	<true/>
 	<key>com.apple.icloud.findmydeviced.access</key>
 	<true/>
 	<key>com.apple.icloud.searchpartyd.beaconmanager</key>
 	<true/>
 	<key>com.apple.linkd.transcript.privileged</key>
 	<true/>
+	<key>com.apple.modelcatalog.full-access</key>
+	<true/>
+	<key>com.apple.modelmanager.inference</key>
+	<true/>
 	<key>com.apple.nano.nanoregistry</key>
 	<true/>
 	<key>com.apple.nano.nanoregistry.generalaccess</key>

 	<array>
 		<string>IAPHistory</string>
 	</array>
+	<key>com.apple.private.assets.accessible-asset-types</key>
+	<array>
+		<string>com.apple.MobileAsset.UAF.FM.GenerativeModels</string>
+		<string>com.apple.MobileAsset.UAF.FM.Overrides</string>
+	</array>
 	<key>com.apple.private.biome.pruner</key>
 	<array>
 		<string>Discoverability.Signals</string>

 		<string>AppLaunch</string>
 		<string>Device.Wireless.Bluetooth</string>
 		<string>Discoverability.Signals</string>
+		<string>SpringBoard.WindowManagement.StageManagerMode</string>
 		<string>UserFocusComputedMode</string>
 	</array>
+	<key>com.apple.private.biome.read-write</key>
+	<array>
+		<string>App.Intent</string>
+		<string>GenerativeModels.GenerativeFunctions.Instrumentation</string>
+	</array>
 	<key>com.apple.private.biome.sync</key>
 	<true/>
 	<key>com.apple.private.biome.writer</key>

 				</dict>
 				<key>GenerativeExperiences.GeneratedImageFeatures.UserInteraction</key>
 				<dict/>
+				<key>SpringBoard.WindowManagement.StageManagerMode</key>
+				<dict/>
 				<key>UserFocusComputedMode</key>
 				<dict/>
 			</dict>

 		<string>group.com.apple.tips</string>
 		<string>group.com.apple.tipsnext</string>
 	</array>
+	<key>com.apple.private.security.storage.MobileAssetGenerativeModels</key>
+	<true/>
 	<key>com.apple.private.security.storage.Spotlight</key>
 	<true/>
 	<key>com.apple.private.sleepd</key>

 	</array>
 	<key>com.apple.private.tips.allow</key>
 	<true/>
+	<key>com.apple.private.tipsd.assistant</key>
+	<true/>
 	<key>com.apple.private.usernotifications.bundle-identifiers</key>
 	<array>
 		<string>com.apple.tips</string>

 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/db/com.apple.countryd/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_GenerativeModels/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_UAF_FM_Overrides/purpose_auto/</string>
+		<string>/private/var/MobileAsset/AssetsV2/locks/com.apple.UnifiedAssetFramework/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
+		<string>/private/var/mobile/Library/com.apple.modelcatalog/sideload/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_GenerativeModels/</string>
+		<string>/System/Library/PreinstalledAssetsV2/RequiredByOs/com_apple_MobileAsset_UAF_FM_Overrides/</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.appconduitd.device-connection</string>
 		<string>com.apple.biomesyncd.sync</string>
 		<string>com.apple.CellularPlanDaemon.xpc</string>
+		<string>com.apple.cloudd</string>
 		<string>com.apple.contactsd</string>
+		<string>com.apple.controlcenter.remoteservice</string>
 		<string>com.apple.enroll.state</string>
 		<string>com.apple.itunescloud.music-subscription-status-service</string>
 		<string>com.apple.mobile.keybagd.UserManager.xpc</string>
 		<string>com.apple.mobile.keybagd.xpc</string>
 		<string>com.apple.mobile.usermanagerd.xpc</string>
+		<string>com.apple.modelcatalog.catalog</string>
+		<string>com.apple.modelmanager</string>
 		<string>com.apple.parsecd</string>
+		<string>com.apple.tipsd.assistant</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>
+		<string>com.apple.GenerativeFunctions.GenerativeFunctionsInstrumentation</string>
+		<string>com.apple.gms.availability</string>
+		<string>com.apple.modelcatalog.ajax</string>
+		<string>com.apple.modelcatalog.catalog</string>
 		<string>com.apple.parsecd</string>
+		<string>com.apple.UnifiedAssetFramework</string>
+		<string>kCFPreferencesAnyApplication</string>
+	</array>
+	<key>com.apple.security.exception.shared-preference.read-write</key>
+	<array>
+		<string>com.apple.siri.DialogEngine</string>
 	</array>
 	<key>com.apple.security.network.client</key>
 	<true/>

 	<true/>
 	<key>com.apple.usermanagerd.persona.fetch</key>
 	<true/>
+	<key>com.apple.wifi.manager-access</key>
+	<true/>
 	<key>platform-application</key>
 	<true/>
 </dict>

```

### 🆕 toolkitd

> `/usr/libexec/toolkitd`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.linkd.registry</key>
	<true/>
	<key>com.apple.linkd.transcript.privileged</key>
	<true/>
	<key>com.apple.private.appintents.extension-host</key>
	<true/>
	<key>com.apple.rootless.storage.shortcuts</key>
	<true/>
	<key>com.apple.runningboard.assertions.siri</key>
	<true/>
	<key>com.apple.runningboard.launchprocess</key>
	<true/>
	<key>com.apple.runningboard.process-state</key>
	<true/>
	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
	<array>
		<string>/Library/Shortcuts/</string>
	</array>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.linkd.autoShortcut</string>
		<string>com.apple.linkd.extension</string>
		<string>com.apple.linkd.registry</string>
		<string>com.apple.linkd.transcript</string>
	</array>
	<key>com.apple.shortcuts.toolkitd</key>
	<true/>
</dict>
</plist>

```

### 🆕 triageControllerD

> `/usr/libexec/triageControllerD`

- No entitlements *(yet)*
### triald

> `/usr/libexec/triald`

```diff

 	</array>
 	<key>com.apple.managedconfiguration.profiled.profile-list-read</key>
 	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
 	<key>com.apple.private.CacheDelete</key>
 	<array>
 		<string>CLIENT_ENTITLEMENT</string>
 		<string>PURGEABLE_ENTITLEMENT</string>
 		<string>PURGE_ENTITLEMENT</string>
 	</array>
+	<key>com.apple.private.DeviceIdentity.access</key>
+	<true/>
 	<key>com.apple.private.MobileContainerManager.allowed</key>
 	<true/>
 	<key>com.apple.private.MobileContainerManager.lookup</key>

 	<true/>
 	<key>com.apple.private.kernel.read-write-trial-experiment-factors</key>
 	<true/>
+	<key>com.apple.private.mobileactivationd.attestation</key>
+	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>

 	<true/>
 	<key>com.apple.proactive.eventtracker</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
 	<key>com.apple.security.exception.files.absolute-path.read-only</key>
 	<array>
 		<string>/private/var/MobileAsset/</string>

 	<true/>
 	<key>com.apple.triald.system.from-agent</key>
 	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.triald</string>
+		<string>lockdown-identities</string>
+		<string>apple</string>
+	</array>
 	<key>platform-application</key>
 	<true/>
 	<key>seatbelt-profiles</key>

```
### triald_system

> `/usr/libexec/triald_system`

```diff

 	</array>
 	<key>com.apple.duet.activityscheduler.allow</key>
 	<true/>
+	<key>com.apple.mobileactivationd.device-identifiers</key>
+	<true/>
+	<key>com.apple.mobileactivationd.spi</key>
+	<true/>
+	<key>com.apple.private.DeviceIdentity.access</key>
+	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
 	<array>
 		<string>UniqueDeviceID</string>

 			</dict>
 		</dict>
 	</dict>
+	<key>com.apple.private.mobileactivationd.attestation</key>
+	<true/>
 	<key>com.apple.private.osanalytics.defaults.allow</key>
 	<true/>
 	<key>com.apple.private.security.storage.triald</key>
 	<true/>
+	<key>com.apple.private.system-keychain</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceLiverpool</string>
 	</array>
 	<key>com.apple.private.xpc.launchd.allowed-manage-trial-factors</key>
 	<true/>
+	<key>com.apple.security.attestation.access</key>
+	<true/>
+	<key>keychain-access-groups</key>
+	<array>
+		<string>com.apple.triald</string>
+		<string>lockdown-identities</string>
+		<string>apple</string>
+	</array>
 	<key>seatbelt-profiles</key>
 	<array>
 		<string>triald_system</string>

```
### tvremoted

> `/usr/libexec/tvremoted`

```diff

 	<true/>
 	<key>com.apple.appletv.pbs.profile-picker-service-access.read</key>
 	<true/>
+	<key>com.apple.appletv.pbs.profile-picker-service-access.selectUser</key>
+	<true/>
 	<key>com.apple.appletv.pbs.user-profiles</key>
 	<true/>
 	<key>com.apple.appletv.pbs.user-profiles.select</key>

```
### uarpd

> `/usr/libexec/uarpd`

```diff

 	</array>
 	<key>com.apple.application-identifier</key>
 	<string>com.apple.uarpd</string>
+	<key>com.apple.corespeech.corespeechservices</key>
+	<true/>
 	<key>com.apple.corespeech.xpc</key>
 	<true/>
 	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>

 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.AppSSO.service-xpc</string>
+		<string>com.apple.corespeech.corespeechservices</string>
+		<string>com.apple.corespeech.xpc</string>
 		<string>com.apple.geod</string>
 		<string>com.apple.installerauthagent</string>
 		<string>com.apple.SBUserNotification</string>

```
### uarphidd

> `/usr/libexec/uarphidd`

```diff

 	</array>
 	<key>com.apple.private.xpc.launchd.per-user-lookup</key>
 	<true/>
+	<key>com.apple.security.exception.files.absolute-path.read-write</key>
+	<array>
+		<string>/private/var/db/accessoryupdater/</string>
+	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>
 		<string>com.apple.uarp.endpoint.transport</string>

```
### videocodecd

> `/usr/libexec/videocodecd`

```diff

 		<string>com.apple.coremedia</string>
 		<string>com.apple.VideoProcessing</string>
 	</array>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.security.temporary-exception.iokit-user-client-class</key>
 	<array>
 		<string>AppleAVDUserClient</string>

```
### BTLEServer

> `/usr/sbin/BTLEServer`

```diff

 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>
 		<string>/private/var/db/accessoryupdater/uarp/</string>
+		<string>/private/var/db/accessoryupdater/uarpd/</string>
 	</array>
 	<key>com.apple.security.exception.files.home-relative-path.read-write</key>
 	<array>

 		<string>com.apple.AudioAccessoryServices</string>
 		<string>com.apple.devicesharing.guestusermodeservice</string>
 		<string>com.apple.heartratecoordinatord.blecollectionobserver</string>
+		<string>com.apple.uarp.endpoint.transport</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 		<string>access-calls</string>
 		<string>modify-calls</string>
 	</array>
+	<key>com.apple.uarp.endpoint.transport</key>
+	<true/>
 	<key>com.apple.visualvoicemail.client</key>
 	<true/>
 	<key>keychain-access-groups</key>

```
### bluetoothaudiod

> `/usr/sbin/bluetoothaudiod`

```diff

 	<array>
 		<string>com.apple.BTLEServer.ANCS</string>
 	</array>
+	<key>com.apple.private.siri.activation</key>
+	<true/>
 	<key>com.apple.private.tcc.allow</key>
 	<array>
 		<string>kTCCServiceAddressBook</string>

 	<array>
 		<string>RootDomainUserClient</string>
 	</array>
+	<key>com.apple.siri.activation</key>
+	<true/>
+	<key>com.apple.siri.external_request</key>
+	<true/>
 	<key>com.apple.symptom_diagnostics.report</key>
 	<true/>
 	<key>com.apple.telephonyutilities.callservicesd</key>

```
### bluetoothd

> `/usr/sbin/bluetoothd`

```diff

 	<true/>
 	<key>com.apple.powerui.smartcharging.AudioAccessory</key>
 	<true/>
+	<key>com.apple.private.SkyLight.displaycontrol</key>
+	<true/>
 	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
 	<true/>
 	<key>com.apple.private.accounts.allaccounts</key>
 	<true/>
+	<key>com.apple.private.applecredentialmanager.allow</key>
+	<true/>
 	<key>com.apple.private.appletamanager.allow</key>
 	<true/>
 	<key>com.apple.private.assets.accessible-asset-types</key>

 	<true/>
 	<key>com.apple.private.coreservices.canopenactivity</key>
 	<true/>
+	<key>com.apple.private.darwin-notification.restrict-post.audioaccessoryd.MuteState</key>
+	<true/>
 	<key>com.apple.private.dprivacyd.allow</key>
 	<true/>
 	<key>com.apple.private.dprivacyd.metadata.allow</key>

 		<string>AppleSPUUserClient</string>
 		<string>IOHIDLibUserClient</string>
 		<string>IOUserClient</string>
+		<string>AppleCredentialManagerUserClient</string>
 	</array>
 	<key>com.apple.security.exception.mach-lookup.global-name</key>
 	<array>

 		<string>com.apple.matter.support.xpc</string>
 		<string>com.apple.UXMAssertionService</string>
 		<string>com.apple.appprotectiond.read</string>
+		<string>com.apple.ProductKitService</string>
 	</array>
 	<key>com.apple.security.exception.shared-preference.read-only</key>
 	<array>

 	<true/>
 	<key>com.apple.security.network.server</key>
 	<true/>
+	<key>com.apple.security.script-restrictions</key>
+	<true/>
 	<key>com.apple.security.system-groups</key>
 	<array>
 		<string>systemgroup.com.apple.logd_helper.FTABHarvest</string>

```
### mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

 	<true/>
 	<key>com.apple.developer.hardened-process.hardened-heap</key>
 	<true/>
+	<key>com.apple.duet.activityscheduler.allow</key>
+	<true/>
 	<key>com.apple.iokit.wakerequest</key>
 	<true/>
 	<key>com.apple.mDNSResponder_Helper</key>

 	<true/>
 	<key>com.apple.private.network.socket-delegate</key>
 	<true/>
+	<key>com.apple.private.network.tcp.info</key>
+	<true/>
 	<key>com.apple.private.network.ultraconstrained</key>
 	<true/>
 	<key>com.apple.private.networkextension.configuration</key>

```
### wifid

> `/usr/sbin/wifid`

```diff

 		<string>com.apple.wifi-class-d-private-mac-networks.plist</string>
 		<string>preferences.plist</string>
 	</array>
+	<key>com.apple.TapToRadarKit.service-access</key>
+	<true/>
 	<key>com.apple.accounts.appleaccount.fullaccess</key>
 	<true/>
 	<key>com.apple.avfoundation.allow-system-wide-context</key>

 	<true/>
 	<key>com.apple.keystore.sik.access</key>
 	<true/>
+	<key>com.apple.locationd.absolute_altimeter</key>
+	<true/>
 	<key>com.apple.locationd.activity</key>
 	<true/>
 	<key>com.apple.locationd.effective_bundle</key>

 		<string>/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PayloadManifest.plist</string>
 		<string>/private/var/mobile/Library/Trial/NamespaceDescriptors/</string>
 		<string>/private/var/db/os_eligibility/eligibility.plist</string>
+		<string>/private/var/run/MobileAssetStartupActivation.doneThisBoot</string>
 	</array>
 	<key>com.apple.security.exception.files.absolute-path.read-write</key>
 	<array>

```
