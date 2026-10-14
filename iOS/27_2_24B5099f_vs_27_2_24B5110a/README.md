# 27.2 (24B5099f) .vs 27.2 (24B5110a)

## Inputs

- `iPhone19,2,iPhone19,3,iPhone19,7_27.2_24B5099f_Restore.ipsw`
- `iPhone19,2,iPhone19,3,iPhone19,7_27.2_24B5110a_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 27.2 *(24B5099f)* | 27.2.0 | 13432.40.177.0.3~16 | Sun, 27Sep2026 21:01:09 PDT |
| 27.2 *(24B5110a)* | 27.2.0 | 13432.42.3~13 | Sat, 10Oct2026 01:30:59 PDT |

### Kexts

#### ⬆️ Updated (25)

- [com.apple.AGXG19P](KEXTS/com.apple.AGXG19P.md)
- [com.apple.driver.AppleARMPlatform](KEXTS/com.apple.driver.AppleARMPlatform.md)
- [com.apple.driver.AppleAVE2](KEXTS/com.apple.driver.AppleAVE2.md)
- [com.apple.driver.AppleCamera](KEXTS/com.apple.driver.AppleCamera.md)
- [com.apple.driver.AppleCentauriManager](KEXTS/com.apple.driver.AppleCentauriManager.md)
- [com.apple.driver.AppleFirmwareKit](KEXTS/com.apple.driver.AppleFirmwareKit.md)
- [com.apple.driver.AppleH16ANEInterface](KEXTS/com.apple.driver.AppleH16ANEInterface.md)
- [com.apple.driver.AppleIDV](KEXTS/com.apple.driver.AppleIDV.md)
- [com.apple.driver.AppleM2ScalerCSCDriver](KEXTS/com.apple.driver.AppleM2ScalerCSCDriver.md)
- [com.apple.driver.AppleMesaSEPDriver](KEXTS/com.apple.driver.AppleMesaSEPDriver.md)
- [com.apple.driver.AppleMobileDispH19P-DCP](KEXTS/com.apple.driver.AppleMobileDispH19P-DCP.md)
- [com.apple.driver.AppleSPMIPMU](KEXTS/com.apple.driver.AppleSPMIPMU.md)
- [com.apple.driver.AppleT8160CLPC](KEXTS/com.apple.driver.AppleT8160CLPC.md)
- [com.apple.driver.corecapture](KEXTS/com.apple.driver.corecapture.md)
- [com.apple.filesystems.apfs](KEXTS/com.apple.filesystems.apfs.md)
- [com.apple.iokit.IOBiometricFamily](KEXTS/com.apple.iokit.IOBiometricFamily.md)
- [com.apple.iokit.IOHIDFamily](KEXTS/com.apple.iokit.IOHIDFamily.md)
- [com.apple.iokit.IOPCIFamily](KEXTS/com.apple.iokit.IOPCIFamily.md)
- [com.apple.iokit.IOSkywalkFamily](KEXTS/com.apple.iokit.IOSkywalkFamily.md)
- [com.apple.iokit.IOStorageFamily](KEXTS/com.apple.iokit.IOStorageFamily.md)
- [com.apple.iokit.IOTimeSyncFamily](KEXTS/com.apple.iokit.IOTimeSyncFamily.md)
- [com.apple.iokit.IOUSBHostFamily](KEXTS/com.apple.iokit.IOUSBHostFamily.md)
- [com.apple.kernel](KEXTS/com.apple.kernel.md)
- [com.apple.security.AppleImage4](KEXTS/com.apple.security.AppleImage4.md)
- [com.apple.security.sandbox](KEXTS/com.apple.security.sandbox.md)

## MachO

### filesystem

#### 🆕 NEW (7)

- `/Applications/HomeProximityDynamicIslandUIService.app/HomeProximityDynamicIslandUIService`
- `/System/Library/CoreServices/CoreTypes.bundle/Contents/Library/MobileDevices-0004.bundle/MobileDevices-0004`
- `/System/Library/ExtensionKit/Extensions/HomeDeveloperSettingsIntents.appex/HomeDeveloperSettingsIntents`
- `/System/Library/PreferenceBundles/HomeDeveloperSettings.bundle/HomeDeveloperSettings`
- `/System/Library/PrivateFrameworks/HealthAppSupport.framework/PlugIns/MedicalIDFollowUpExtension.appex/MedicalIDFollowUpExtension`
- `/System/Library/PrivateFrameworks/PebblePlayDaemon.framework/pebbleplayd`
- `/private/var/staged_system_apps/Home.app/PlugIns/HomeAppMessagesExtension.appex/HomeAppMessagesExtension`

#### ❌ Removed (1)

- `/private/var/staged_system_apps/Health.app/PlugIns/MedicalIDFollowUpExtension.appex/MedicalIDFollowUpExtension`

#### ⬆️ Updated (1083)

- [View 1083 updated files](MACHOS/filesystem.Updated.md)

### SystemOS

#### ⬆️ Updated (3)

- [/System/Library/PrivateFrameworks/NodesUI.framework/NodesUI](MACHOS/SystemOS/System/Library/PrivateFrameworks/NodesUI.framework/NodesUI.md)
- [/usr/lib/libramrod.dylib](MACHOS/SystemOS/usr/lib/libramrod.dylib.md)
- [/usr/libexec/Moments.framework/Moments](MACHOS/SystemOS/usr/libexec/Moments.framework/Moments.md)

### AppOS

#### ⬆️ Updated (5)

- [/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari](MACHOS/AppOS/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari.md)
- [/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings](MACHOS/AppOS/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings.md)
- [/usr/libexec/SafariBookmarksSyncAgent](MACHOS/AppOS/usr/libexec/SafariBookmarksSyncAgent.md)
- [/usr/libexec/browserkitd](MACHOS/AppOS/usr/libexec/browserkitd.md)
- [/usr/libexec/webbookmarksd](MACHOS/AppOS/usr/libexec/webbookmarksd.md)

### ExclaveOS

#### ⬆️ Updated (3)

- [/System/ExclaveKit/System/Library/Frameworks/CodeCoverageDelegate.framework/CodeCoverageDelegate](MACHOS/ExclaveOS/System/ExclaveKit/System/Library/Frameworks/CodeCoverageDelegate.framework/CodeCoverageDelegate.md)
- [/System/ExclaveKit/System/Library/Frameworks/IISAudioOutputStreamClientNotifierComponent.framework/IISAudioOutputStreamClientNotifierComponent](MACHOS/ExclaveOS/System/ExclaveKit/System/Library/Frameworks/IISAudioOutputStreamClientNotifierComponent.framework/IISAudioOutputStreamClientNotifierComponent.md)
- [/System/ExclaveKit/usr/bin/tightbeam_stub](MACHOS/ExclaveOS/System/ExclaveKit/usr/bin/tightbeam_stub.md)

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Sandbox Profiles

### Collection (1)

#### ⬆️ Updated (1)

- [com.apple.driverkitd](SANDBOX/Collection/com.apple.driverkitd.md)

### Protobox/Autobox (47)

#### ⬆️ Updated (47)

<details>
  <summary><i>View Updated</i></summary>

- [AppleQEMUGuestAgent](SANDBOX/Protobox-Autobox/AppleQEMUGuestAgent.md)
- [Campo](SANDBOX/Protobox-Autobox/Campo.md)
- [CheckerBoard](SANDBOX/Protobox-Autobox/CheckerBoard.md)
- [DumpBasebandCrash](SANDBOX/Protobox-Autobox/DumpBasebandCrash.md)
- [ManagedStatusSubscriber](SANDBOX/Protobox-Autobox/ManagedStatusSubscriber.md)
- [ManagementTestSubscriber](SANDBOX/Protobox-Autobox/ManagementTestSubscriber.md)
- [MobileGestaltHelper](SANDBOX/Protobox-Autobox/MobileGestaltHelper.md)
- [SpringBoard](SANDBOX/Protobox-Autobox/SpringBoard.md)
- [StocksKitService](SANDBOX/Protobox-Autobox/StocksKitService.md)
- [anomalydetectiond](SANDBOX/Protobox-Autobox/anomalydetectiond.md)
- [appleidsetupd](SANDBOX/Protobox-Autobox/appleidsetupd.md)
- [audioaccessoryd](SANDBOX/Protobox-Autobox/audioaccessoryd.md)
- [audiomxd](SANDBOX/Protobox-Autobox/audiomxd.md)
- [avconferenced](SANDBOX/Protobox-Autobox/avconferenced.md)
- [axassetsd](SANDBOX/Protobox-Autobox/axassetsd.md)
- [com.apple.VideoSubscriberAccount.PrivacyService](SANDBOX/Protobox-Autobox/com.apple.VideoSubscriberAccount.PrivacyService.md)
- [com.apple.corelocation.locationUI](SANDBOX/Protobox-Autobox/com.apple.corelocation.locationUI.md)
- [dbtelemetryd](SANDBOX/Protobox-Autobox/dbtelemetryd.md)
- [deviceconfigurationd](SANDBOX/Protobox-Autobox/deviceconfigurationd.md)
- [donotdisturbd](SANDBOX/Protobox-Autobox/donotdisturbd.md)
- [enhancedloggingd](SANDBOX/Protobox-Autobox/enhancedloggingd.md)
- [familycircled](SANDBOX/Protobox-Autobox/familycircled.md)
- [fileindexerd](SANDBOX/Protobox-Autobox/fileindexerd.md)
- [geod](SANDBOX/Protobox-Autobox/geod.md)
- [healthappd](SANDBOX/Protobox-Autobox/healthappd.md)
- [installcoordination_proxy](SANDBOX/Protobox-Autobox/installcoordination_proxy.md)
- [intelligencecontextd](SANDBOX/Protobox-Autobox/intelligencecontextd.md)
- [intelligenceflowd](SANDBOX/Protobox-Autobox/intelligenceflowd.md)
- [linkd](SANDBOX/Protobox-Autobox/linkd.md)
- [lskdd](SANDBOX/Protobox-Autobox/lskdd.md)
- [manageddeviced](SANDBOX/Protobox-Autobox/manageddeviced.md)
- [mediaartworkd](SANDBOX/Protobox-Autobox/mediaartworkd.md)
- [medialibraryd](SANDBOX/Protobox-Autobox/medialibraryd.md)
- [mediaremoted](SANDBOX/Protobox-Autobox/mediaremoted.md)
- [mobilerepaird](SANDBOX/Protobox-Autobox/mobilerepaird.md)
- [mobiletimerd](SANDBOX/Protobox-Autobox/mobiletimerd.md)
- [nsattributedstringagent](SANDBOX/Protobox-Autobox/nsattributedstringagent.md)
- [searchd](SANDBOX/Protobox-Autobox/searchd.md)
- [searchtoold](SANDBOX/Protobox-Autobox/searchtoold.md)
- [seserviced](SANDBOX/Protobox-Autobox/seserviced.md)
- [sirittsd](SANDBOX/Protobox-Autobox/sirittsd.md)
- [sociallayerd](SANDBOX/Protobox-Autobox/sociallayerd.md)
- [speechmaintenanced](SANDBOX/Protobox-Autobox/speechmaintenanced.md)
- [symptomsd-distributed](SANDBOX/Protobox-Autobox/symptomsd-distributed.md)
- [usernotificationsd](SANDBOX/Protobox-Autobox/usernotificationsd.md)
- [voicememod](SANDBOX/Protobox-Autobox/voicememod.md)
- [webprivacyd](SANDBOX/Protobox-Autobox/webprivacyd.md)

</details>

## Firmware

### ⬆️ Updated (18)

- [Firmware/M3/bin/securem3fw-v6x.im4p](FIRMWARE/Firmware/M3/bin/securem3fw-v6x.im4p.md)
- [Firmware/agx/armfw_g19p.im4p/agx_a000](FIRMWARE/Firmware/agx/armfw_g19p.im4p/agx_a000.md)
- [Firmware/agx/armfw_g19p.im4p/agx_a010](FIRMWARE/Firmware/agx/armfw_g19p.im4p/agx_a010.md)
- [Firmware/agx/armfw_g19p.im4p/agx_b000](FIRMWARE/Firmware/agx/armfw_g19p.im4p/agx_b000.md)
- [Firmware/ane/h19_ane0_fw_perses_v6x.im4p](FIRMWARE/Firmware/ane/h19_ane0_fw_perses_v6x.im4p.md)
- [Firmware/ane/h19_ane1_fw_perses_v6x.im4p](FIRMWARE/Firmware/ane/h19_ane1_fw_perses_v6x.im4p.md)
- [Firmware/ansf.t8160.release.im4p](FIRMWARE/Firmware/ansf.t8160.release.im4p.md)
- [Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_kernel](FIRMWARE/Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_kernel.md)
- [Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_sharedcache](FIRMWARE/Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_sharedcache.md)
- [Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_kernel](FIRMWARE/Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_kernel.md)
- [Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_sharedcache](FIRMWARE/Firmware/image4/exclavecore_bundle.t8160.RELEASE.restore.im4p/exclave_sharedcache.md)
- [Firmware/isp_bni/adc-boreas-v6x.im4p](FIRMWARE/Firmware/isp_bni/adc-boreas-v6x.im4p.md)
- [Firmware/msr/t8160.msrf.im4p](FIRMWARE/Firmware/msr/t8160.msrf.im4p.md)
- [Firmware/msr/t8160.rmsr.im4p](FIRMWARE/Firmware/msr/t8160.rmsr.im4p.md)
- [Firmware/rans.t8160.release.im4p](FIRMWARE/Firmware/rans.t8160.release.im4p.md)
- [Firmware/sptm.t8160.release.im4p](FIRMWARE/Firmware/sptm.t8160.release.im4p.md)
- [Firmware/txm.iphoneos.release.im4p](FIRMWARE/Firmware/txm.iphoneos.release.im4p.md)
- [Firmware/txm.iphoneos.research.im4p](FIRMWARE/Firmware/txm.iphoneos.research.im4p.md)

### iBoot

| iOS | Version |
| :-- | :------ |
| 27.2 *(24B5099f)* | mBoot-20457.40.172.502.1 |
| 27.2 *(24B5110a)* | mBoot-20457.42.4 |

#### 🆕 NEW (9)

- [AppleSMCFirmware.bin](IBOOT/NEW/AppleSMCFirmware.bin.md)
- [RTKit.bin](IBOOT/NEW/RTKit.bin.md)
- [iboot_blob04.bin](IBOOT/NEW/iboot_blob04.bin.md)
- [iboot_blob08.bin](IBOOT/NEW/iboot_blob08.bin.md)
- [iboot_blob11.bin](IBOOT/NEW/iboot_blob11.bin.md)
- [iboot_blob31.bin](IBOOT/NEW/iboot_blob31.bin.md)
- [iboot_blob32.bin](IBOOT/NEW/iboot_blob32.bin.md)
- [iboot_blob34.bin](IBOOT/NEW/iboot_blob34.bin.md)
- [iboot_blob35.bin](IBOOT/NEW/iboot_blob35.bin.md)

#### ❌ Removed (5)

- [AppleSMCFirmware.bin](IBOOT/Removed/AppleSMCFirmware.bin.md)
- [iboot_blob31.bin](IBOOT/Removed/iboot_blob31.bin.md)
- [iboot_blob32.bin](IBOOT/Removed/iboot_blob32.bin.md)
- [iboot_blob34.bin](IBOOT/Removed/iboot_blob34.bin.md)
- [iboot_blob35.bin](IBOOT/Removed/iboot_blob35.bin.md)

### launchd Config

<details>
  <summary><i>View Updated</i></summary>

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
-	<key>IgnoreCache</key>
-	<true/>
 	<key>SIGTERMTimeout</key>
 	<integer>3</integer>
 	<key>CrashOnSIGTERMTimeout</key>

```

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 27.2 *(24B5099f)* | 625.2.7.1.0 |
| 27.2 *(24B5110a)* | 625.2.8.10.4 |

### Dylibs

#### 🆕 NEW (5)

- `/System/Library/Frameworks/HomeExtensions.framework/HomeExtensions`
- `/System/Library/PrivateFrameworks/PebblePlayCore.framework/PebblePlayCore`
- `/System/Library/PrivateFrameworks/PebblePlayDaemon.framework/PebblePlayDaemon`
- `/System/Library/PrivateFrameworks/PebblePlayFeatures.framework/PebblePlayFeatures`
- `/System/Library/PrivateFrameworks/PebblePlayKit.framework/PebblePlayKit`

#### ⬆️ Updated (1013)

- [View 1013 updated files](DYLIBS/Dylibs.Updated.md)

## Files

### 🆕 New

#### filesystem (725)

- [View 725 new files](FILES/filesystem.NEW.md)

#### SystemOS (60)

- [View 60 new files](FILES/SystemOS.NEW.md)

#### ExclaveOS (6)

- `/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision_internal.framework/Resources/facelivelinessfull_ek_fp16.bundle/H19.bundle/H19.e5`
- `/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision_internal.framework/Resources/facelivelinessfull_ek_fp16.bundle/H19.bundle/main/main_ane/model.hwx`
- `/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision_internal.framework/Resources/faceprint_ek_fp16.bundle/H19.bundle/H19.e5`
- `/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision_internal.framework/Resources/faceprint_ek_fp16.bundle/H19.bundle/main/main_ane/model.hwx`
- `/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision_internal.framework/Resources/faceprint_uc_ek_fp16.bundle/H19.bundle/H19.e5`
- `/System/ExclaveKit/System/Library/Frameworks/Vision.framework/Vision_internal.framework/Resources/faceprint_uc_ek_fp16.bundle/H19.bundle/main/main_ane/model.hwx`

### ❌ Removed

#### filesystem (131)

- [View 131 removed files](FILES/filesystem.Removed.md)

## Localizations

### SystemOS

#### 🆕 NEW (1)

<details>
  <summary><i>View New</i></summary>

##### MobileSafari

>  `SystemOS/System/Library/PrivateFrameworks/MobileSafari.framework/en.lproj/PebbleAppIntents.strings`

```text
%d Cloud Tabs = "%d Cloud Tabs"
%d Per-Site Settings = "%d Per-Site Settings"
%d URL Autocomplete Entity = "%d URL Autocomplete Entity"
Asks Siri to begin reading the current page aloud. = "Asks Siri to begin reading the current page aloud."
Change Reader Mode = "Change Reader Mode"
Changes Reader Mode of the current page. = "Changes Reader Mode of the current page."
Cloud Tab = "Cloud Tab"
Dismiss (App Intent) = "Dismiss"
Dismisses Pebble Safari Sheet = "Dismisses Pebble Safari Sheet"
Domain = "Domain"
Fetch Recommended Cloud Tabs = "Fetch Recommended Cloud Tabs"
Fetches a set of recommended cloud tabs = "Fetches a set of recommended cloud tabs"
Font Name = "Font Name"
Is Pinned (Cloud Tab Entity) = "Is Pinned"
Is Showing Reader (Cloud Tab Entity) = "Is Showing Reader"
Is Top Hit (PebbleURLAutocomplete Entity) = "Is Top Hit"
Language Tag = "Language Tag"
Last Viewed Time (Cloud Tab Entity) = "Last Viewed Time"
Listen to Page (App Intent) = "Listen to Page"
Navigate Webpage (App Intent) = "Navigate Webpage (App Intent)"
Navigates to the previous or next webpage in the navigation stack = "Navigates to the previous or next webpage in the navigation stack"
Navigation Direction = "Navigation Direction"
Per-Site Settings = "Per-Site Settings"
Reader Configuration = "Reader Configuration"
Reader Mode Toggle = "Reader Mode Toggle"
Reload Current Page (App Intent) = "Reload Current Page"
Reloads currently displayed webpage = "Reloads currently displayed webpage"
Scroll Direction = "Scroll Direction"
Scroll Webpage (App Intent) = "Scroll Webpage"
Scrolls down or up the current webpage = "Scrolls down or up the current webpage"
Theme Color = "Theme Color"
Title (Cloud Tab Entity) = "Title"
Title (PebbleURLAutocomplete Entity) = "Title"
URL (Cloud Tab Entity) = "URL"
URL (PebbleURLAutocomplete Entity) = "URL"
URL Autocomplete Entity = "URL Autocomplete Entity"
UUID String (Cloud Tab Entity) = "UUID String"
Use Reader Automatically = "Use Reader Automatically"
```

</details>

#### ⬆️ Updated (1)

- [SystemOS/System/Library/PrivateFrameworks/SafariSharedUI.framework/en.lproj/Localizable.strings](LOCALIZATIONS/SystemOS/System/Library/PrivateFrameworks/SafariSharedUI.framework/en.lproj/Localizable.strings.md)

### FileSystem

#### 🆕 NEW (65)

<details>
  <summary><i>View New</i></summary>

- [FileSystem/Applications/CompanionSetup.app/Localizable-Linwood.loctable](LOCALIZATIONS/FileSystem/Applications/CompanionSetup.app/Localizable-Linwood.loctable.md)
- [FileSystem/Applications/CompanionSetup.app/Localizable-Pebble.loctable](LOCALIZATIONS/FileSystem/Applications/CompanionSetup.app/Localizable-Pebble.loctable.md)
- [FileSystem/Applications/Diagnostics.app/Localizable-J490.loctable](LOCALIZATIONS/FileSystem/Applications/Diagnostics.app/Localizable-J490.loctable.md)
- [FileSystem/Applications/HDSViewService.app/Localizable-TOPCAP.loctable](LOCALIZATIONS/FileSystem/Applications/HDSViewService.app/Localizable-TOPCAP.loctable.md)
- [FileSystem/Applications/HomeProximityDynamicIslandUIService.app/HUSensitiveStrings-AccessorySetup.loctable](LOCALIZATIONS/FileSystem/Applications/HomeProximityDynamicIslandUIService.app/HUSensitiveStrings-AccessorySetup.loctable.md)
- [FileSystem/Applications/HomeProximityDynamicIslandUIService.app/HUSensitiveStrings-MarqueeTroubleshooting.loctable](LOCALIZATIONS/FileSystem/Applications/HomeProximityDynamicIslandUIService.app/HUSensitiveStrings-MarqueeTroubleshooting.loctable.md)
- [FileSystem/Applications/HomeProximityDynamicIslandUIService.app/InfoPlist.loctable](LOCALIZATIONS/FileSystem/Applications/HomeProximityDynamicIslandUIService.app/InfoPlist.loctable.md)
- [FileSystem/Applications/RecoverDeviceUI.app/Localizable-J490.loctable](LOCALIZATIONS/FileSystem/Applications/RecoverDeviceUI.app/Localizable-J490.loctable.md)
- [FileSystem/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/Accessibility-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/Accessibility-J490.loctable.md)
- [FileSystem/System/Library/AppPlaceholders/Home.app/PlugIns/HomeAppMessagesExtension.appex/InfoPlist.loctable](LOCALIZATIONS/FileSystem/System/Library/AppPlaceholders/Home.app/PlugIns/HomeAppMessagesExtension.appex/InfoPlist.loctable.md)
- [FileSystem/System/Library/CoreServices/VoiceOverTouch.app/VOTElementInstructions-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/CoreServices/VoiceOverTouch.app/VOTElementInstructions-J490.loctable.md)
- [FileSystem/System/Library/CoreServices/VoiceOverTouch.app/VOTLocalizedStrings-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/CoreServices/VoiceOverTouch.app/VOTLocalizedStrings-J490.loctable.md)
- [FileSystem/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/HomeDevices-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/ExtensionKit/Extensions/GeneralSettingsIntents.appex/HomeDevices-J490.loctable.md)
- [FileSystem/System/Library/ExtensionKit/Extensions/HomeDeveloperSettingsIntents.appex/InfoPlist.loctable](LOCALIZATIONS/FileSystem/System/Library/ExtensionKit/Extensions/HomeDeveloperSettingsIntents.appex/InfoPlist.loctable.md)
- [FileSystem/System/Library/ExtensionKit/Extensions/HomeDeveloperSettingsIntents.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/ExtensionKit/Extensions/HomeDeveloperSettingsIntents.appex/Localizable.loctable.md)
- [FileSystem/System/Library/ExtensionKit/Extensions/MediaRemoteAppIntentsExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/ExtensionKit/Extensions/MediaRemoteAppIntentsExtension.appex/Localizable.loctable.md)
- [FileSystem/System/Library/ExtensionKit/Extensions/WallpaperSettingsIntents.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/ExtensionKit/Extensions/WallpaperSettingsIntents.appex/Localizable.loctable.md)
- [FileSystem/System/Library/Frameworks/HomeExtensions.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/Frameworks/HomeExtensions.framework/Localizable.loctable.md)
- [FileSystem/System/Library/Frameworks/HomeKit.framework/en.lproj/HMAccessoryCategory-J490.strings](LOCALIZATIONS/FileSystem/System/Library/Frameworks/HomeKit.framework/en.lproj/HMAccessoryCategory-J490.strings.md)
- [FileSystem/System/Library/Frameworks/HomeKit.framework/en.lproj/HomeKit-Extensibility.strings](LOCALIZATIONS/FileSystem/System/Library/Frameworks/HomeKit.framework/en.lproj/HomeKit-Extensibility.strings.md)
- [FileSystem/System/Library/Frameworks/HomeKit.framework/en.lproj/HomeKit-VCS.strings](LOCALIZATIONS/FileSystem/System/Library/Frameworks/HomeKit.framework/en.lproj/HomeKit-VCS.strings.md)
- [FileSystem/System/Library/PreferenceBundles/AccessibilitySettings.bundle/Accessibility-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PreferenceBundles/AccessibilitySettings.bundle/Accessibility-J490.loctable.md)
- [FileSystem/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/HomeDevices-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PreferenceBundles/AirPlayAndHandoffSettings.bundle/HomeDevices-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AXPIStrings-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AccessibilityPhysicalInteraction.framework/AXPIStrings-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AXUILocalizedStrings-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AXUILocalizedStrings-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AXWallpaperDescriptions-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AXWallpaperDescriptions-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/SwitchControl-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/SwitchControl-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AlarmUIFramework.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AlarmUIFramework.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettings-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettings-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettings-LinwoodTVOS.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AssistantSettingsSupport.framework/AssistantSettings-LinwoodTVOS.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/CompanionSetupKit.framework/Localizable-J265.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/CompanionSetupKit.framework/Localizable-J265.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/CompanionSetupKit.framework/Localizable-Linwood.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/CompanionSetupKit.framework/Localizable-Linwood.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/DisembarkUI.framework/PlugIns/DKFollowUpExtension.appex/InfoPlist.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/DisembarkUI.framework/PlugIns/DKFollowUpExtension.appex/InfoPlist.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/Pumpkin.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/Pumpkin.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/FindMyCore.framework/Intelligence+TVRemote.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/FindMyCore.framework/Intelligence+TVRemote.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/Home.framework/HFSensitiveStrings-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/Home.framework/HFSensitiveStrings-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/Home.framework/HFSensitiveStrings-Linwood.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/Home.framework/HFSensitiveStrings-Linwood.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/Home.framework/HFSensitiveStrings-LockDPS.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/Home.framework/HFSensitiveStrings-LockDPS.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/Home.framework/HFSensitiveStrings-TopCapNight.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/Home.framework/HFSensitiveStrings-TopCapNight.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-LockDPS.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-LockDPS.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-MarqueeExtensibility.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-MarqueeExtensibility.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-MarqueeThermostat.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-MarqueeThermostat.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-MarqueeTroubleshooting.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeDataModel.framework/HFSensitiveStrings-MarqueeTroubleshooting.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon-Thermostat.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon-Thermostat.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemon-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemon-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemon-Thermostat.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemon-Thermostat.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeUI.framework/HUSensitiveStrings-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeUI.framework/HUSensitiveStrings-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeUI.framework/HUSensitiveStrings-MarqueeCameras.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeUI.framework/HUSensitiveStrings-MarqueeCameras.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeUI.framework/HUSensitiveStrings-MarqueeTroubleshooting.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeUI.framework/HUSensitiveStrings-MarqueeTroubleshooting.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/ManagedConfiguration.framework/Localizable-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/ManagedConfiguration.framework/Localizable-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/MediaRemote.framework/Localizable-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/MediaRemote.framework/Localizable-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosClockPoster.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosClockPoster.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PUPosterSetup.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PUPosterSetup.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/ProximityControl.framework/Localizable-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/ProximityControl.framework/Localizable-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/SiriSetup.framework/Localizable-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/SiriSetup.framework/Localizable-J490.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/en.lproj/CommandDescriptions-J490.strings](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/en.lproj/CommandDescriptions-J490.strings.md)
- [FileSystem/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/en.lproj/CommandStrings-J490.strings](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/en.lproj/CommandStrings-J490.strings.md)
- [FileSystem/System/Library/PrivateFrameworks/UserNotificationsServer.framework/Localizable-J490.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/UserNotificationsServer.framework/Localizable-J490.loctable.md)
- [FileSystem/private/var/staged_system_apps/FindMy.app/Localizable-TVREMOTE.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/FindMy.app/Localizable-TVREMOTE.loctable.md)
- [FileSystem/private/var/staged_system_apps/Home.app/HOSensitiveStrings-J490.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Home.app/HOSensitiveStrings-J490.loctable.md)
- [FileSystem/private/var/staged_system_apps/Home.app/PlugIns/HomeAppMessagesExtension.appex/InfoPlist.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Home.app/PlugIns/HomeAppMessagesExtension.appex/InfoPlist.loctable.md)
- [FileSystem/private/var/staged_system_apps/Home.app/PlugIns/HomeAppMessagesExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Home.app/PlugIns/HomeAppMessagesExtension.appex/Localizable.loctable.md)

</details>

#### ❌ Removed (4)

- `FileSystem/Applications/PosterBoard.app/InfoPlist.loctable`
- `FileSystem/System/Library/AppPlaceholders/AppleTV.app/PlugIns/TVWidgetExtension.appex/InfoPlist.loctable`
- `FileSystem/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/InfoPlist.loctable`
- `FileSystem/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/InfoPlist.loctable`

#### ⬆️ Updated (111)

<details>
  <summary><i>View Updated</i></summary>

- [FileSystem/Applications/ClockAngel.app/InfoPlist.loctable](LOCALIZATIONS/FileSystem/Applications/ClockAngel.app/InfoPlist.loctable.md)
- [FileSystem/Applications/CompanionSetup.app/Localizable.loctable](LOCALIZATIONS/FileSystem/Applications/CompanionSetup.app/Localizable.loctable.md)
- [FileSystem/Applications/SharingUIService.app/Localizable.loctable](LOCALIZATIONS/FileSystem/Applications/SharingUIService.app/Localizable.loctable.md)
- [FileSystem/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/Accessibility.loctable](LOCALIZATIONS/FileSystem/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/Accessibility.loctable.md)
- [FileSystem/System/Library/AccessibilityBundles/ProxCardKit.axbundle/Accessibility.loctable](LOCALIZATIONS/FileSystem/System/Library/AccessibilityBundles/ProxCardKit.axbundle/Accessibility.loctable.md)
- [FileSystem/System/Library/AccessibilityBundles/SpringBoard.axbundle/Accessibility.loctable](LOCALIZATIONS/FileSystem/System/Library/AccessibilityBundles/SpringBoard.axbundle/Accessibility.loctable.md)
- [FileSystem/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/Accessibility.loctable](LOCALIZATIONS/FileSystem/System/Library/AccessibilityBundles/SystemStatusUI.axbundle/Accessibility.loctable.md)
- [FileSystem/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOverSettings.loctable](LOCALIZATIONS/FileSystem/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOverSettings.loctable.md)
- [FileSystem/System/Library/AppRemovalServices/com.apple.podcasts.appremoval.xpc/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/AppRemovalServices/com.apple.podcasts.appremoval.xpc/Localizable.loctable.md)
- [FileSystem/System/Library/Assistant/Plugins/Podcasts.assistantBundle/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/Assistant/Plugins/Podcasts.assistantBundle/Localizable.loctable.md)
- [FileSystem/System/Library/CoreServices/CoreServicesUIAgent.app/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/CoreServices/CoreServicesUIAgent.app/Localizable.loctable.md)
- [FileSystem/System/Library/CoreServices/MobileCoreTypes.bundle/InfoPlist.loctable](LOCALIZATIONS/FileSystem/System/Library/CoreServices/MobileCoreTypes.bundle/InfoPlist.loctable.md)
- [FileSystem/System/Library/ExtensionKit/Extensions/AskToViewExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/ExtensionKit/Extensions/AskToViewExtension.appex/Localizable.loctable.md)
- [FileSystem/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/ExtensionKit/Extensions/DisplayAndBrightnessSettingsExtension.appex/Localizable.loctable.md)
- [FileSystem/System/Library/ExtensionKit/Extensions/PodcastsSettingsAppIntentsExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/ExtensionKit/Extensions/PodcastsSettingsAppIntentsExtension.appex/Localizable.loctable.md)
- [FileSystem/System/Library/Frameworks/AppManagedFeatures.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/Frameworks/AppManagedFeatures.framework/Localizable.loctable.md)
- [FileSystem/System/Library/Frameworks/CoreTelephony.framework/en.lproj/CBMessage~applewatch.strings](LOCALIZATIONS/FileSystem/System/Library/Frameworks/CoreTelephony.framework/en.lproj/CBMessage~applewatch.strings.md)
- [FileSystem/System/Library/Frameworks/CoreTelephony.framework/en.lproj/CBMessage~iphone.strings](LOCALIZATIONS/FileSystem/System/Library/Frameworks/CoreTelephony.framework/en.lproj/CBMessage~iphone.strings.md)
- [FileSystem/System/Library/Frameworks/FileProvider.framework/FileProvider.loctable](LOCALIZATIONS/FileSystem/System/Library/Frameworks/FileProvider.framework/FileProvider.loctable.md)
- [FileSystem/System/Library/Frameworks/LinkPresentation.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/Frameworks/LinkPresentation.framework/Localizable.loctable.md)
- [FileSystem/System/Library/Frameworks/ReplayKit.framework/Localizable-V68.loctable](LOCALIZATIONS/FileSystem/System/Library/Frameworks/ReplayKit.framework/Localizable-V68.loctable.md)
- [FileSystem/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/LocalizableProvenance.loctable](LOCALIZATIONS/FileSystem/System/Library/Frameworks/_PhotosUI_SwiftUI.framework/LocalizableProvenance.loctable.md)
- [FileSystem/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Localizable.loctable.md)
- [FileSystem/System/Library/NanoPreferenceBundles/General/CompanionStingSettings.bundle/LocalizableSettings-N199.loctable](LOCALIZATIONS/FileSystem/System/Library/NanoPreferenceBundles/General/CompanionStingSettings.bundle/LocalizableSettings-N199.loctable.md)
- [FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.appleid.bundle/AppleID.loctable](LOCALIZATIONS/FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.appleid.bundle/AppleID.loctable.md)
- [FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.improveintelligence.bundle/ImproveIntelligence.loctable](LOCALIZATIONS/FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.improveintelligence.bundle/ImproveIntelligence.loctable.md)
- [FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.improvesiridictation.bundle/ImproveSiriDictation.loctable](LOCALIZATIONS/FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.improvesiridictation.bundle/ImproveSiriDictation.loctable.md)
- [FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.podcasts.bundle/Podcasts.loctable](LOCALIZATIONS/FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.podcasts.bundle/Podcasts.loctable.md)
- [FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.siri.bundle/AskSiri.loctable](LOCALIZATIONS/FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.siri.bundle/AskSiri.loctable.md)
- [FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.trustinsights.bundle/TrustInsights.loctable](LOCALIZATIONS/FileSystem/System/Library/OnBoardingBundles/com.apple.onboarding.trustinsights.bundle/TrustInsights.loctable.md)
- [FileSystem/System/Library/PreferenceBundles/DeveloperSettings.bundle/DTSettings.loctable](LOCALIZATIONS/FileSystem/System/Library/PreferenceBundles/DeveloperSettings.bundle/DTSettings.loctable.md)
- [FileSystem/System/Library/PreferenceBundles/FilterSpamSettingsBundle.bundle/FilterSpamSettings.loctable](LOCALIZATIONS/FileSystem/System/Library/PreferenceBundles/FilterSpamSettingsBundle.bundle/FilterSpamSettings.loctable.md)
- [FileSystem/System/Library/PreferenceBundles/HearingSettings.bundle/HearingAidAudioSettings.loctable](LOCALIZATIONS/FileSystem/System/Library/PreferenceBundles/HearingSettings.bundle/HearingAidAudioSettings.loctable.md)
- [FileSystem/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PreferenceBundles/MultitaskingAndGesturesSettings.bundle/Localizable.loctable.md)
- [FileSystem/System/Library/PreferenceBundles/TVSettings.bundle/Localizable-SimpleProfilesPersonal.loctable](LOCALIZATIONS/FileSystem/System/Library/PreferenceBundles/TVSettings.bundle/Localizable-SimpleProfilesPersonal.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/TeachableMomentItems-27.0-iOS.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AccessibilityUtilities.framework/TeachableMomentItems-27.0-iOS.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AgentCanvasUICore.framework/Canvas.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AgentCanvasUICore.framework/Canvas.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AppIntentSchemas.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AppIntentSchemas.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/AskToCore.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/AskToCore.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/CallsAppUI.framework/CallsAppUI.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/CallsAppUI.framework/CallsAppUI.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI-Provenance.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI-Provenance.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/LocalizableSettings-N199.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/CarouselPreferenceServices.framework/LocalizableSettings-N199.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/ContentKit.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/ContentKit.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationControls.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationControls.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/CoreRepairCore.framework/Localizable-V68.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/CoreRepairCore.framework/Localizable-V68.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/CoreRepairKit.framework/Localizable-V68.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/CoreRepairKit.framework/Localizable-V68.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/CoreRepairKit.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/CoreRepairKit.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/DisembarkUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/DisembarkUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/FindMyCore.framework/Intelligence.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/FindMyCore.framework/Intelligence.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HealthIntelligence.framework/QuantityIntelligenceSemantics.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HealthIntelligence.framework/QuantityIntelligenceSemantics.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HealthPlansUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HealthPlansUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HealthReportCoreUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HealthReportCoreUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemon.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/HomeKitDaemonLegacy.framework/HomeKitDaemon.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/Human.framework/Alignment.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/Human.framework/Alignment.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/Human.framework/AlignmentMisc.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/Human.framework/AlignmentMisc.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/Human.framework/AlignmentVariants.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/Human.framework/AlignmentVariants.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/IntelligenceFlow.framework/DomainTopicDisclaimers.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/IntelligenceFlow.framework/DomainTopicDisclaimers.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/IntelligenceFlow.framework/PlannerModelFacingErrors.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/IntelligenceFlow.framework/PlannerModelFacingErrors.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/DomainTopicDisclaimers.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/DomainTopicDisclaimers.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/PlannerModelFacingErrors.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerRuntime.framework/PlannerModelFacingErrors.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/DomainTopicDisclaimers.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/DomainTopicDisclaimers.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/PlannerModelFacingErrors.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/PlannerModelFacingErrors.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/DomainTopicDisclaimers.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/DomainTopicDisclaimers.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlannerModelFacingErrors.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/PlannerModelFacingErrors.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/LabKitUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/LabKitUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/MedicalIDDaemon.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/MedicalIDDaemon.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/NewsUI2.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/NewsUI2.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/NowPlayingUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/NowPlayingUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/OmniSearch.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/OmniSearch.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/Passcode Lock.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/Passcode_Lock.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/ImageProvenance.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/ImageProvenance.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICoreProvenance.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICoreProvenance.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICoreSharedAlbums.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICoreSharedAlbums.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICoreSharedCollections.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICoreSharedCollections.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUI.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUI.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PodcastsFoundation.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PodcastsFoundation.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PodcastsKit.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PodcastsKit.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/PodcastsUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/PodcastsUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/SFSymbols.framework/CoreGlyphsPrivate.bundle/nofill_to_fill.strings](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/SFSymbols.framework/CoreGlyphsPrivate.bundle/nofill_to_fill.strings.md)
- [FileSystem/System/Library/PrivateFrameworks/ScreenTimeSettingsServicesUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/ScreenTimeSettingsServicesUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/TelephonyPreferences.framework/CallDirectorySettings.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/TelephonyPreferences.framework/CallDirectorySettings.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/VideosUI.framework/Localizable-SimpleProfilesPersonal.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/VideosUI.framework/Localizable-SimpleProfilesPersonal.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverCommands.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/VoiceOverServices.framework/VoiceOverCommands.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/WorkflowEditor.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/WorkflowEditor.framework/Localizable.loctable.md)
- [FileSystem/System/Library/PrivateFrameworks/WorkflowKit.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/PrivateFrameworks/WorkflowKit.framework/Localizable.loctable.md)
- [FileSystem/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/InfoPlist.loctable](LOCALIZATIONS/FileSystem/System/Library/ScreenReader/BrailleDrivers/GenericHID.brailledriver/InfoPlist.loctable.md)
- [FileSystem/System/Library/Settings/DefaultApps/CallFiltering.plugin/CallDirectorySettings.loctable](LOCALIZATIONS/FileSystem/System/Library/Settings/DefaultApps/CallFiltering.plugin/CallDirectorySettings.loctable.md)
- [FileSystem/System/Library/Settings/SuggestedActionsSettings.settings/SuggestedActionsSettings.loctable](LOCALIZATIONS/FileSystem/System/Library/Settings/SuggestedActionsSettings.settings/SuggestedActionsSettings.loctable.md)
- [FileSystem/System/Library/Snippets/UIPlugins/MusicSnippetsUI.bundle/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/Snippets/UIPlugins/MusicSnippetsUI.bundle/Localizable.loctable.md)
- [FileSystem/System/Library/UserNotifications/Bundles/com.apple.CompanionNotifications.bundle/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/UserNotifications/Bundles/com.apple.CompanionNotifications.bundle/Localizable.loctable.md)
- [FileSystem/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeNotifications.bundle/Localizable.loctable](LOCALIZATIONS/FileSystem/System/Library/UserNotifications/Bundles/com.apple.ScreenTimeNotifications.bundle/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Fitness.app/Localizable-Cobalt.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Fitness.app/Localizable-Cobalt.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsAppEntities.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsAppEntities.framework/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsAppIntents.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsAppIntents.framework/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsPlayback.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsPlayback.framework/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsWidgetKit.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsWidgetKit.framework/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/SWAIPodcastsAppIntents.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/SWAIPodcastsAppIntents.framework/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsAnnouncementsNotificationExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsAnnouncementsNotificationExtension.appex/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsClassKitExtension.appex/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsNotificationExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsNotificationExtension.appex/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/PodcastsWidget.appex/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.DiagnosticExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.DiagnosticExtension.appex/Localizable.loctable.md)
- [FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/Localizable.loctable](LOCALIZATIONS/FileSystem/private/var/staged_system_apps/Podcasts.app/PlugIns/com.apple.podcasts.SpotlightIndexExtension.appex/Localizable.loctable.md)

</details>

## Feature Flags

### filesystem

#### 🆕 NEW (2)

<details>
  <summary><i>View New</i></summary>

##### FontServices.plist

>  `Domain/FontServices.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict/>
</plist>

```
##### PebblePlay.plist

>  `Domain/PebblePlay.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PebblePlay</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>ShowAssistantCell</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
	<key>TemplateImageExtraction</key>
	<dict>
		<key>DevelopmentPhase</key>
		<string>FeatureComplete</string>
	</dict>
</dict>
</plist>

```

</details>

#### ⬆️ Updated (12)

- [Domain/Accessibility.plist](FEATURES/filesystem/Domain/Accessibility.plist.md)
- [Domain/AppIntentsServices.plist](FEATURES/filesystem/Domain/AppIntentsServices.plist.md)
- [Domain/AppleMediaServices.plist](FEATURES/filesystem/Domain/AppleMediaServices.plist.md)
- [Domain/FileProvider.plist](FEATURES/filesystem/Domain/FileProvider.plist.md)
- [Domain/FindMy.plist](FEATURES/filesystem/Domain/FindMy.plist.md)
- [Domain/Health.plist](FEATURES/filesystem/Domain/Health.plist.md)
- [Domain/Home.plist](FEATURES/filesystem/Domain/Home.plist.md)
- [Domain/OmniSearch.plist](FEATURES/filesystem/Domain/OmniSearch.plist.md)
- [Domain/Photos.plist](FEATURES/filesystem/Domain/Photos.plist.md)
- [Domain/Rapport.plist](FEATURES/filesystem/Domain/Rapport.plist.md)
- [Domain/ReplayKit.plist](FEATURES/filesystem/Domain/ReplayKit.plist.md)
- [Domain/TelephonyUtilities.plist](FEATURES/filesystem/Domain/TelephonyUtilities.plist.md)

## EOF
