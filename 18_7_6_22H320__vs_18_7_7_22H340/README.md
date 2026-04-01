# 18.7.6 (22H320) .vs 18.7.7 (22H340)

## Inputs

- `iPhone11,8_18.7.6_22H320_Restore.ipsw`
- `iPhone11,8_18.7.7_22H340_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.7.6 *(22H320)* | 24.6.0 | 11417.140.69.706.3~1 | Mon, 19Jan2026 22:05:19 PST |
| 18.7.7 *(22H340)* | 24.6.0 | 11417.140.69.706.9~1 | Wed, 04Mar2026 22:11:45 PST |

### Kexts

### ⬆️ Updated (4)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.AppleJPEGDriver

>  `com.apple.driver.AppleJPEGDriver`

```diff

-7.6.9.0.0
+7.6.10.0.0
   __TEXT.__cstring: 0x26fd
-  __TEXT.__os_log: 0x8506
+  __TEXT.__os_log: 0x84b7
   __TEXT.__const: 0x34b4
-  __TEXT_EXEC.__text: 0x29174
+  __TEXT_EXEC.__text: 0x29184
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2108
   __DATA.__common: 0x358

   __DATA_CONST.__mod_term_func: 0xa8
   __DATA_CONST.__const: 0x4578
   __DATA_CONST.__kalloc_type: 0xbc0
-  UUID: FE832E35-B392-31DE-BD14-C2DF2EA5B424
+  UUID: C023116A-28A1-3DFD-B2A3-824C14F37096
   Functions: 1590
   Symbols:   0
-  CStrings:  465
+  CStrings:  464
 
Functions:
~ __ZN15AppleJPEGDriver14queue_io_gatedEP11JpegRequest : 1516 -> 1480
~ __ZN15AppleJPEGDriver16sleepCommandGateEPvj : 284 -> 336
CStrings:
- "AppleJPEGDriver: %s, ERROR: failed to wait request successfully return 0x%x !\n"

```

#### com.apple.driver.AppleSEPKeyStore

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-1827.120.2.0.0
-  __TEXT.__cstring: 0x3acb
+1827.120.2.700.1
+  __TEXT.__cstring: 0x3ad1
   __TEXT.__const: 0x874
-  __TEXT_EXEC.__text: 0x3bdfc
+  __TEXT_EXEC.__text: 0x3be3c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3a4
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x3a88
   __DATA_CONST.__kalloc_type: 0xd80
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 17D789A9-4C8D-3EC6-9974-57B2BBD51340
-  Functions: 952
+  UUID: 659A9B77-DACF-32F7-9731-6063A8A1D0E1
+  Functions: 953
   Symbols:   0
   CStrings:  340
 
Functions:
~ sub_fffffff00923e0dc : 324 -> 264
+ sub_fffffff00923e1e4
CStrings:
+ "1827.120.2.700.1"
+ "22:24:16"
+ "Mar  4 2026"
- "1827.120.2"
- "21:56:34"
- "Jan 19 2026"

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

 2332.140.13.0.0
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x49f96
+  __TEXT.__cstring: 0x49f8d
   __TEXT_EXEC.__text: 0x140810
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x698

   __DATA_CONST.__kalloc_type: 0x4e00
   __DATA_CONST.__kalloc_var: 0x2b20
   __DATA_CONST.__assert: 0x14
-  UUID: 2710D0F3-85B3-369C-844D-98AD9091D123
+  UUID: 44A404DB-48D1-35A1-9B3B-246A0DC1BF8F
   Functions: 2269
   Symbols:   0
-  CStrings:  6430
+  CStrings:  6429
 
CStrings:
+ "2026/03/04"
+ "22:07:36"
+ "Mar  4 2026"
- "2026/01/19"
- "21:50:19"
- "21:50:20"
- "Jan 19 2026"

```

#### com.apple.kernel

>  `com.apple.kernel`

```diff

-11417.140.69.706.3
+11417.140.69.706.9
   __TEXT.__const: 0x349f0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x6e2b1
+  __TEXT.__cstring: 0x6e2e5
   __TEXT.__os_log: 0x2a645
   __TEXT.__thread_starts: 0x0
   __TEXT.__eh_frame: 0x4e0

   __DATA_CONST.__assert: 0x1cc
   __DATA_CONST.__kern_brk_desc: 0x60
   __TEXT_EXEC.__hib_text: 0xc88
-  __TEXT_EXEC.__text: 0x7e4380
+  __TEXT_EXEC.__text: 0x7e49bc
   __KLD.__text: 0x16d4
   __PPLTEXT.__text: 0x1c930
   __PPLTRAMP.__text: 0xc008

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x46722
-  UUID: EA1C3DF4-109C-30A2-8F3C-DDFD46BB4FAB
-  Functions: 19448
+  UUID: F5910B7F-4DD1-3B13-BD28-F980FAD5BECE
+  Functions: 19447
   Symbols:   0
-  CStrings:  17286
+  CStrings:  17288
 
CStrings:
+ "chmod_chown_busy"
+ "com.apple.private.network.tcp.info"

```


</details>

## MachO

### ⬆️ Updated (64)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/FMDMagSafeSetupRemoteUI.app/FMDMagSafeSetupRemoteUI](MACHOS/FMDMagSafeSetupRemoteUI.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FMDMagSafeExtension.appex/FMDMagSafeExtension](MACHOS/FMDMagSafeExtension.md)
- [/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension](MACHOS/FindMyDeviceBluetoothExtension.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/HeadphoneProxService.app/HeadphoneProxService](MACHOS/HeadphoneProxService.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/System/DriverKit/usr/lib/system/libsystem_c_debug.dylib](MACHOS/libsystem_c_debug.dylib.md)
- [/System/Library/Accounts/Notification/CloudDocsAccountNotificationPlugin.bundle/CloudDocsAccountNotificationPlugin](MACHOS/CloudDocsAccountNotificationPlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/CoreServices/ReportCrash](MACHOS/ReportCrash.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.app-launch.bundle/com.apple.donotdisturb.private.app-launch](MACHOS/com.apple.donotdisturb.private.app-launch.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.private.smart-trigger.bundle/com.apple.donotdisturb.private.smart-trigger](MACHOS/com.apple.donotdisturb.private.smart-trigger.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.donotdisturb.user-toggles.preload.bundle/com.apple.donotdisturb.user-toggles.preload](MACHOS/com.apple.donotdisturb.user-toggles.preload.md)
- [/System/Library/DoNotDisturb/ClientBundles/com.apple.private.SpringBoard.focus.intents.preload.bundle/com.apple.private.SpringBoard.focus.intents.preload](MACHOS/com.apple.private.SpringBoard.focus.intents.preload.md)
- [/System/Library/ExtensionKit/Extensions/PasscodeSettingsExtension.appex/PasscodeSettingsExtension](MACHOS/PasscodeSettingsExtension.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/LocationBundles/DoNotDisturb.bundle/DoNotDisturb](MACHOS/DoNotDisturb.md)
- [/System/Library/PreferenceBundles/PasswordsSettings.bundle/PasswordsSettings](MACHOS/PasswordsSettings.md)
- [/System/Library/PreferenceBundles/PrivacyAndSecuritySettings.bundle/PrivacyAndSecuritySettings](MACHOS/PrivacyAndSecuritySettings.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/PlugIns/DoNotDisturbIntents.appex/DoNotDisturbIntents](MACHOS/DoNotDisturbIntents.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceBTDiscoveryXPCService.xpc/FindMyDeviceBTDiscoveryXPCService](MACHOS/FindMyDeviceBTDiscoveryXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEmergencyCallInfoPublisherXPCService.xpc/FindMyDeviceEmergencyCallInfoPublisherXPCService](MACHOS/FindMyDeviceEmergencyCallInfoPublisherXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/FindMyDeviceEraseXPCService](MACHOS/FindMyDeviceEraseXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService](MACHOS/FindMyDeviceHelperXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceIdentityXPCService.xpc/FindMyDeviceIdentityXPCService](MACHOS/FindMyDeviceIdentityXPCService.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceUserNotificationsXPCService.xpc/FindMyDeviceUserNotificationsXPCService](MACHOS/FindMyDeviceUserNotificationsXPCService.md)
- [/System/Library/PrivateFrameworks/FocusSettingsUI.framework/PlugIns/UserNotificationExtension.appex/UserNotificationExtension](MACHOS/UserNotificationExtension.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService](MACHOS/MobileBackupCacheDeleteService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/PlugIns/MBDiagnosticExtension.appex/MBDiagnosticExtension](MACHOS/MBDiagnosticExtension.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService](MACHOS/MBHelperService.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/backupd](MACHOS/backupd.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/PlugIns/CloudDocsDiagnostic.appex/CloudDocsDiagnostic](MACHOS/CloudDocsDiagnostic.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/bird](MACHOS/bird.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/XPCServices/ContainerMetadataExtractor.xpc/ContainerMetadataExtractor](MACHOS/ContainerMetadataExtractor.md)
- [/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA](MACHOS/MobileBackupUEA.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/usr/libexec/BackupAgent2](MACHOS/BackupAgent2.md)
- [/usr/libexec/FinishRestoreFromBackup](MACHOS/FinishRestoreFromBackup.md)
- [/usr/libexec/audioaccessoryd](MACHOS/audioaccessoryd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/nehelper](MACHOS/nehelper.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/sharingd](MACHOS/sharingd.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)
- [/usr/sbin/otctl](MACHOS/otctl.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.7.6 *(22H320)* | iBoot-11881.140.96 |
| 18.7.7 *(22H340)* | iBoot-11881.140.96.700.1 |

#### 🆕 NEW (1)

<details>
  <summary><i>View NEW</i></summary>

##### `iboot`
  - `iBoot-11881.140.96.700.1`

</details>

#### ❌ Removed (1)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot`
  - `iBoot-11881.140.96`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.7.6 *(22H320)* | 621.7.1.10.1 |
| 18.7.7 *(22H340)* | 621.8.1.10.1 |

### Dylibs

#### ⬆️ Updated (35)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Notification/FindMyDeviceAccountNotificationPlugin.bundle/FindMyDeviceAccountNotificationPlugin](DYLIBS/FindMyDeviceAccountNotificationPlugin.md)
- [/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics](DYLIBS/CoreHaptics.md)
- [/System/Library/Frameworks/FileProvider.framework/OverrideBundles/iCloudDriveFileProviderOverride.bundle/iCloudDriveFileProviderOverride](DYLIBS/iCloudDriveFileProviderOverride.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/LiveCommunicationKit.framework/LiveCommunicationKit](DYLIBS/LiveCommunicationKit.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory](DYLIBS/CallHistory.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI](DYLIBS/CoreUI.md)
- [/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils](DYLIBS/CoreUtils.md)
- [/System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb](DYLIBS/DoNotDisturb.md)
- [/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer](DYLIBS/DoNotDisturbServer.md)
- [/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore](DYLIBS/FMIPCore.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/Focus.framework/Focus](DYLIBS/Focus.md)
- [/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices](DYLIBS/GeoServices.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/IconServices.framework/IconServices](DYLIBS/IconServices.md)
- [/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup](DYLIBS/MobileBackup.md)
- [/System/Library/PrivateFrameworks/MobileDeviceLink.framework/MobileDeviceLink](DYLIBS/MobileDeviceLink.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared](DYLIBS/SafariShared.md)
- [/System/Library/PrivateFrameworks/Settings/GeneralSettingsUI.framework/GeneralSettingsUI](DYLIBS/GeneralSettingsUI.md)
- [/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation](DYLIBS/UIFoundation.md)
- [/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity](DYLIBS/UserActivity.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudDriveService.framework/iCloudDriveService](DYLIBS/iCloudDriveService.md)
- [/usr/lib/libMobileGestalt.dylib](DYLIBS/libMobileGestalt.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/system/libsystem_c.dylib](DYLIBS/libsystem_c.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)

</details>

## EOF
