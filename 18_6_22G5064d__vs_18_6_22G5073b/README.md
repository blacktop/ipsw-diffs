# 18.6 (22G5064d) .vs 18.6 (22G5073b)

## IPSWs

- `iPhone17,1_18.6_22G5064d_Restore.ipsw`
- `iPhone17,1_18.6_22G5073b_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.6 *(22G5064d)* | 24.6.0 | 11417.140.64.0.1~33 | Tue, 17Jun2025 20:58:13 PDT |
| 18.6 *(22G5073b)* | 24.6.0 | 11417.140.66~43 | Thu, 03Jul2025 02:18:09 PDT |

### Kexts

### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.AppleARMWatchdogTimer

>  `com.apple.driver.AppleARMWatchdogTimer`

```diff

-299.140.4.0.0
+299.140.5.0.0
   __TEXT.__cstring: 0x135a
-  __TEXT_EXEC.__text: 0x57d8
+  __TEXT_EXEC.__text: 0x57e4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x118
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x14c8
   __DATA_CONST.__kalloc_type: 0x100
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: FC27240F-C013-3B9A-8013-CF8537F2C996
+  UUID: 82AB5180-52A9-390D-8820-9B85EFCB473C
   Functions: 187
   Symbols:   0
   CStrings:  126

```

#### com.apple.driver.AppleAVE2

>  `com.apple.driver.AppleAVE2`

```diff

-803.71.1.0.0
+803.73.1.0.0
   __TEXT.__const: 0x2ef60
-  __TEXT.__cstring: 0x3567a
-  __TEXT.__os_log: 0x40bb0
-  __TEXT_EXEC.__text: 0x14789c
+  __TEXT.__cstring: 0x356cd
+  __TEXT.__os_log: 0x40bec
+  __TEXT_EXEC.__text: 0x14795c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x290
   __DATA.__common: 0x130

   __DATA_CONST.__const: 0x6318
   __DATA_CONST.__kalloc_type: 0x3f80
   __DATA_CONST.__kalloc_var: 0x1b80
-  UUID: 1A267019-73F2-3BFD-88E0-4679CB63EDF6
+  UUID: 7BAAED0E-6221-3926-83FE-0E6A5358DE9E
   Functions: 2450
   Symbols:   0
-  CStrings:  6981
+  CStrings:  6983
 
Functions (modified):
~ __ZN7AVE_HwC18ProcessIntr_CmdAckEmi : 808 -> 1048
~ __ZN7AVE_HwC15ProcessIntr_CmdEmij : 6516 -> 6476

Functions (added):
+ sub_fffffff008cd7304

Functions (removed):
- sub_fffffff008cd722c
CStrings:
+ "%lld %d AVE %s: %s::%s:%d %s | wrong command %p 0x%lx %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong command %p 0x%lx %d %d\n"
+ "(cmd > AVE_Cmd_None && cmd < AVE_Cmd_Max)"
+ "19:07:25"
+ "803.73.1"
+ "Jul  6 2025"
- "21:59:47"
- "803.71.1"
- "Jun 17 2025"
- "cmd != AVE_Cmd_None"

```

#### com.apple.driver.AppleT8140CLPC

>  `com.apple.driver.AppleT8140CLPC`

```diff

-1175.140.9.0.2
-  __TEXT.__cstring: 0x2c19
+1175.140.11.0.0
+  __TEXT.__cstring: 0x2c16
   __TEXT.__const: 0xbd4
   __TEXT_EXEC.__text: 0x52c64
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x55f8
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__kalloc_var: 0x370
-  UUID: 63F03FFC-08CB-366A-BD38-5CC7B52BE2D4
+  UUID: 4D663533-E4D9-3B40-9642-08F6A57E966B
   Functions: 1197
   Symbols:   0
   CStrings:  468
CStrings:
+ "2025-07-03T02:13:40-07:00"
+ "AppleCLPC-1175.140.11"
- "2025-06-22T21:49:52-07:00"
- "AppleCLPC-1175.140.9.0.2"

```

#### com.apple.driver.IOHIDPowerSource

>  `com.apple.driver.IOHIDPowerSource`

```diff

-2115.140.2.0.0
+2115.140.3.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x7e4
   __TEXT.__os_log: 0x433
-  __TEXT_EXEC.__text: 0x95ec
+  __TEXT_EXEC.__text: 0x9624
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x138

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x1a78
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 3F2AEB96-9759-35AE-9350-72A23623819D
+  UUID: CC83F68E-5E93-3D0B-8775-06A4D7553F81
   Functions: 234
   Symbols:   0
   CStrings:  107
Functions (modified):
~ __ZN21IOHIDTranslationEvent14transformValueEP12OSDictionaryx : 300 -> 356

```

#### com.apple.driver.IOPAudioVoiceTriggerDevice

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 440.4.0.0.0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2c32
+  __TEXT.__cstring: 0x2c29
   __TEXT.__os_log: 0x16f1
   __TEXT_EXEC.__text: 0xafb0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1780
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 578FCCA3-5376-3057-8A20-3C16EE08B207
+  UUID: 35AB6DD8-9218-3A49-A323-4B223FAB562F
   Functions: 258
   Symbols:   0
-  CStrings:  233
+  CStrings:  232
 
CStrings:
+ "02:22:02"
+ "Jul  3 2025"
- "21:53:17"
- "21:53:18"
- "Jun 22 2025"

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

-2332.140.11.0.0
+2332.140.12.0.0
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x49f0d
+  __TEXT.__cstring: 0x49f16
   __TEXT_EXEC.__text: 0x140320
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x6a0

   __DATA_CONST.__kalloc_type: 0x4e00
   __DATA_CONST.__kalloc_var: 0x2b20
   __DATA_CONST.__assert: 0x14
-  UUID: 1D958DC7-7C9E-3CEB-B1E8-35AB4D88474E
+  UUID: 5F334502-32EB-38F5-BDD9-CB8962BE2AF6
   Functions: 2268
   Symbols:   0
-  CStrings:  6426
+  CStrings:  6427
 
Functions (modified):
~ _wrapping_keybag_setup : 176 -> 368
~ _nx_is_removable : 132 -> 308
~ __ZN19AppleAPFSUserClient24methodVolumeMakeMultikeyEPS_PvP25IOExternalMethodArguments : 748 -> 1268
~ _pfkur_thread_start : 180 -> 216
~ _pfkur_roll_ino : 932 -> 600

Functions (added):
+ sub_fffffff00aa19de0
+ sub_fffffff00aa2cd28
+ sub_fffffff00aa369ac
+ sub_fffffff00aa6f110
+ sub_fffffff00aa70104

Functions (removed):
- sub_fffffff00aa38cb4
- sub_fffffff00ab2993c
- sub_fffffff00ab3ae90
- sub_fffffff00ab3bd94
- sub_fffffff00ab3c148
CStrings:
+ "02:02:21"
+ "02:02:22"
+ "2025/07/03"
+ "2332.140.12"
+ "Jul  3 2025"
+ "apfs-2332.140.12"
- "2025/06/17"
- "20:53:07"
- "2332.140.11"
- "Jun 17 2025"
- "apfs-2332.140.11"

```

#### com.apple.kernel

>  `com.apple.kernel`

```diff

-11417.140.64.0.1
-  __TEXT.__const: 0x348c0
+11417.140.66.0.0
+  __TEXT.__const: 0x348b0
   __TEXT.__copyio_vectors: 0xf0
-  __TEXT.__cstring: 0x76a33
-  __TEXT.__os_log: 0x2a6fb
+  __TEXT.__cstring: 0x76a7a
+  __TEXT.__os_log: 0x2a76b
   __TEXT.__eh_frame: 0x610
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x2d8

   __DATA_CONST.__kern_brk_desc: 0x78
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xcc8
-  __TEXT_EXEC.__text: 0x82e344
+  __TEXT_EXEC.__text: 0x82e594
   __TEXT_BOOT_EXEC.__bootcode: 0x514c
   __KLD.__text: 0x1638
   __LASTDATA_CONST.__mod_init_func: 0x8

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x466fd
-  UUID: B484DA6F-E5CF-394D-837B-8C5632FA49D1
-  Functions: 20197
+  UUID: BE79611C-05EB-33C0-A8BC-E14C214994F1
+  Functions: 20198
   Symbols:   0
-  CStrings:  17896
+  CStrings:  17900
 
Functions (modified):
~ _proc_set_task_spawnpolicy : 1552 -> 288
~ ___stack_chk_fail : 1100 -> 308
~ _bridge_clone_destroy : 808 -> 820
~ _bridge_clone_create : 2744 -> 2908
~ _bridge_ioctl : 2908 -> 2640
~ _memorystatus_control : 176 -> 764
~ __ZN6OSKext15considerUnloadsEb : 348 -> 2200
~ _sleh_synchronous : 52 -> 60

Functions (added):
+ sub_fffffff0081cb714
+ _handle_kernel_abort
+ sub_fffffff008373704
+ sub_fffffff008658f94
+ sub_fffffff0087937ac
+ sub_fffffff0088f3f28

Functions (removed):
- sub_fffffff0087b5988
- sub_fffffff008928604
- sub_fffffff008930880
- sub_fffffff00893122c
- sub_fffffff008931508
CStrings:
+ "%s: %s: clearing SCF_PROTO_ATTACHED"
+ "%s: %s: proto count %d"
+ "%s: %s: setting SCF_PROTO_ATTACHED"
+ "bridge_interface_attach_protocol"
+ "bridge_interface_proto_attach_changed"
- "%s: ifp %s has address"

```

#### com.apple.security.sandbox

>  `com.apple.security.sandbox`

```diff

 2401.140.15.0.0
   __TEXT.__os_log: 0x2092
-  __TEXT.__const: 0x1baf99
+  __TEXT.__const: 0x1bb019
   __TEXT.__cstring: 0x71cc
   __TEXT_EXEC.__text: 0x31634
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x35f0
   __DATA_CONST.__kalloc_type: 0xb40
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 38D19D8D-BD61-3CDD-A762-FD97B999E847
+  UUID: 100D6FB8-9106-3BD3-8BAD-203CDB5B5B52
   Functions: 639
   Symbols:   0
   CStrings:  1322

```


</details>

## MachO

### 🆕 NEW (1)

- `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/FMDCFUTheftAndLossReminderExtension`

### ⬆️ Updated (114)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AirDropUI.app/AirDropUI](MACHOS/AirDropUI.md)
- [/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel](MACHOS/AppDistributionLaunchAngel.md)
- [/Applications/ClarityCamera.app/ClarityCamera](MACHOS/ClarityCamera.md)
- [/Applications/ColorPickerUIService.app/ColorPickerUIService](MACHOS/ColorPickerUIService.md)
- [/Applications/Diagnostics.app/Diagnostics](MACHOS/Diagnostics.md)
- [/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004](MACHOS/Diagnostic-6004.md)
- [/Applications/FindMyRemoteUIService.app/FindMyRemoteUIService](MACHOS/FindMyRemoteUIService.md)
- [/Applications/GameCenterUIService.app/PlugIns/GameCenterMessageExtension.appex/GameCenterMessageExtension](MACHOS/GameCenterMessageExtension.md)
- [/Applications/GameOverlayUI.app/GameOverlayUI](MACHOS/GameOverlayUI.md)
- [/Applications/Preferences.app/Preferences](MACHOS/Preferences.md)
- [/Applications/SharingUIService.app/SharingUIService](MACHOS/SharingUIService.md)
- [/Applications/SharingViewService.app/SharingViewService](MACHOS/SharingViewService.md)
- [/Applications/Tamale.app/Tamale](MACHOS/Tamale.md)
- [/System/Library/Accounts/ServiceOwners/AMSMediaServiceOwner.bundle/AMSMediaServiceOwner](MACHOS/AMSMediaServiceOwner.md)
- [/System/Library/AppleMediaServices/DynamicUI/PlugIns/StoreDynamicUIPlugin.bundle/StoreDynamicUIPlugin](MACHOS/StoreDynamicUIPlugin.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant](MACHOS/PreferencesAssistant.md)
- [/System/Library/Audio/Plug-Ins/AVC/AVCHalogen.driver/AVCHalogen](MACHOS/AVCHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/AirPlayHalogen.driver/AirPlayHalogen](MACHOS/AirPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/CarPlayHalogen.driver/CarPlayHalogen](MACHOS/CarPlayHalogen.md)
- [/System/Library/Audio/Plug-Ins/HAL/OctaviaHalogen.driver/OctaviaHalogen](MACHOS/OctaviaHalogen.md)
- [/System/Library/CoreServices/ClarityBoard.app/ClarityBoard](MACHOS/ClarityBoard.md)
- [/System/Library/CoreServices/powerd.bundle/powerd](MACHOS/powerd.md)
- [/System/Library/ExtensionKit/Extensions/ADFollowUpExtension.appex/ADFollowUpExtension](MACHOS/ADFollowUpExtension.md)
- [/System/Library/ExtensionKit/Extensions/GenerativeAssistantExtension.appex/GenerativeAssistantExtension](MACHOS/GenerativeAssistantExtension.md)
- [/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond](MACHOS/managedappdistributiond.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/Frameworks/StoreKit.framework/Support/storekitd](MACHOS/storekitd.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ColorPicker.appex/com.apple.UIKit.ColorPicker](MACHOS/com.apple.UIKit.ColorPicker.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings](MACHOS/AppInstallationSettings.md)
- [/System/Library/PreferenceBundles/PasswordsSettings.bundle/PasswordsSettings](MACHOS/PasswordsSettings.md)
- [/System/Library/PreferenceBundles/WallpaperSettings.bundle/WallpaperSettings](MACHOS/WallpaperSettings.md)
- [/System/Library/PrivateFrameworks/ASOctaneSupport.framework/XPCServices/ASOctaneSupportXPCService.xpc/ASOctaneSupportXPCService](MACHOS/ASOctaneSupportXPCService.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd](MACHOS/amsaccountsd.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension](MACHOS/UtilityExtension.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd](MACHOS/amsengagementd.md)
- [/System/Library/PrivateFrameworks/BookDataStore.framework/Support/bookdatastored](MACHOS/bookdatastored.md)
- [/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.DTMLModelRunnerService.xpc/com.apple.dt.DTMLModelRunnerService](MACHOS/com.apple.dt.DTMLModelRunnerService.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller](MACHOS/diskimagescontroller.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService](MACHOS/FindMyDeviceSharedConfigurationXPCService.md)
- [/System/Library/PrivateFrameworks/GameCenterUI.framework/PlugIns/GameCenterMatchmakerExtension.appex/GameCenterMatchmakerExtension](MACHOS/GameCenterMatchmakerExtension.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd](MACHOS/mediaanalysisd.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/mediaanalysisd-service](MACHOS/mediaanalysisd-service.md)
- [/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer](MACHOS/SearchIndexer.md)
- [/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service](MACHOS/Accessory_Updater_Service.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated](MACHOS/softwareupdated.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService](MACHOS/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/Support/amsondevicestoraged](MACHOS/amsondevicestoraged.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/passd](MACHOS/passd.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/Plugins/SoftwareUpdateServicesUIPlugin.servicebundle/SoftwareUpdateServicesUIPlugin](MACHOS/SoftwareUpdateServicesUIPlugin.md)
- [/System/Library/PrivateFrameworks/SonicKit.framework/PlugIns/SonicDiagnostics.appex/SonicDiagnostics](MACHOS/SonicDiagnostics.md)
- [/System/Library/UserEventPlugins/com.apple.cts.plugin/com.apple.cts](MACHOS/com.apple.cts.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2](MACHOS/VideoStabilizationV2.md)
- [/private/var/staged_system_apps/AppleTV.app/PlugIns/TVWidgetExtension.appex/TVWidgetExtension](MACHOS/TVWidgetExtension.md)
- [/private/var/staged_system_apps/AppleVisionProApp.app/AppleVisionProApp](MACHOS/AppleVisionProApp.md)
- [/private/var/staged_system_apps/Books.app/Books](MACHOS/Books.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore](MACHOS/BookCore.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookEPUB.framework/BookEPUB](MACHOS/BookEPUB.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BookStoreUI.framework/BookStoreUI](MACHOS/BookStoreUI.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksPersonalization.framework/BooksPersonalization](MACHOS/BooksPersonalization.md)
- [/private/var/staged_system_apps/Books.app/Frameworks/BooksUI.framework/BooksUI](MACHOS/BooksUI.md)
- [/private/var/staged_system_apps/FindMy.app/FindMy](MACHOS/FindMy.md)
- [/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/FindMyAppCore](MACHOS/FindMyAppCore.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyNotificationsService.appex/FindMyNotificationsService](MACHOS/FindMyNotificationsService.md)
- [/private/var/staged_system_apps/FindMy.app/PlugIns/FindMyWidgetPeople.appex/FindMyWidgetPeople](MACHOS/FindMyWidgetPeople.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension](MACHOS/MailWidgetExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/MobileNotes](MACHOS/MobileNotes.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SharingExtension.appex/com.apple.mobilenotes.SharingExtension](MACHOS/com.apple.mobilenotes.SharingExtension.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.WidgetExtension.appex/com.apple.mobilenotes.WidgetExtension](MACHOS/com.apple.mobilenotes.WidgetExtension.md)
- [/private/var/staged_system_apps/MobileSMS.app/MobileSMS](MACHOS/MobileSMS.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension](MACHOS/SafariWidgetExtension.md)
- [/private/var/staged_system_apps/MobileSafari.app/PlugIns/com.apple.mobilesafari.SafariDiagnosticExtension.appex/com.apple.mobilesafari.SafariDiagnosticExtension](MACHOS/com.apple.mobilesafari.SafariDiagnosticExtension.md)
- [/private/var/staged_system_apps/News.app/PlugIns/NewsTag.appex/NewsTag](MACHOS/NewsTag.md)
- [/private/var/staged_system_apps/Passbook.app/PlugIns/PassbookLockedWidgetsExtension.appex/PassbookLockedWidgetsExtension](MACHOS/PassbookLockedWidgetsExtension.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/PodcastsTranscripts.framework/PodcastsTranscripts](MACHOS/PodcastsTranscripts.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/sbin/launchd](MACHOS/launchd.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/bluetoothuserd](MACHOS/bluetoothuserd.md)
- [/usr/libexec/coreidvd](MACHOS/coreidvd.md)
- [/usr/libexec/cryptexd](MACHOS/cryptexd.md)
- [/usr/libexec/diskimagesiod](MACHOS/diskimagesiod.md)
- [/usr/libexec/driverkitd](MACHOS/driverkitd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/findmydeviced](MACHOS/findmydeviced.md)
- [/usr/libexec/fskitd](MACHOS/fskitd.md)
- [/usr/libexec/gamed](MACHOS/gamed.md)
- [/usr/libexec/idcredd](MACHOS/idcredd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/launchd_cache_loader](MACHOS/launchd_cache_loader.md)
- [/usr/libexec/mediaparserd](MACHOS/mediaparserd.md)
- [/usr/libexec/mediaplaybackd](MACHOS/mediaplaybackd.md)
- [/usr/libexec/nanoregistryd](MACHOS/nanoregistryd.md)
- [/usr/libexec/promotedcontentd](MACHOS/promotedcontentd.md)
- [/usr/libexec/searchpartyd](MACHOS/searchpartyd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/seserviced](MACHOS/seserviced.md)
- [/usr/libexec/swtransparencyd](MACHOS/swtransparencyd.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/videocodecd](MACHOS/videocodecd.md)
- [/usr/libexec/xpcproxy](MACHOS/xpcproxy.md)
- [/usr/libexec/xpcroleaccountd](MACHOS/xpcroleaccountd.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H17.im4p

>  `AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0xf3d38
+  __TEXT.__text: 0xf34d8
   __TEXT._rtk_mtab: 0x2d0
   __TEXT.__const: 0x22844
-  __TEXT.__cstring: 0x1417b
+  __TEXT.__cstring: 0x140ff
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0
   __DATA.__const: 0x2a20

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0xcbd58
-  UUID: F6B6FCE5-C471-3318-8FEC-89FCF9CFC551
+  UUID: 80123C74-2A29-395C-B892-E546918FBA85
   Functions: 0
   Symbols:   1538
-  CStrings:  2423
+  CStrings:  2421
 
Symbols:
+ __ZN16LinearRegression4initEffff
- __ZN16LinearRegression4initEfff
CStrings:
+ "%s::%s:%d wrong start point %d %d"
+ "8002.47.0"
- "%s::%s:%d BITBOX OVERFLOW (QPMODOFF) Frame# %d - ABR: %d HRD: %d"
- "%s::%s:%d BITBOX OVERFLOW (QPMODON) Frame# %d - ABR: %d HRD: %d qpModLevel %d"
- "8002.46.0"
- "start_pt < 128"

```

#### adc-rheia-d9x.im4p

>  `adc-rheia-d9x.im4p`

```diff

 
-  __TEXT.__text: 0x837018
+  __TEXT.__text: 0x837114
   __TEXT.__const: 0x9b59a0
   __TEXT.text_env: 0x4fda4
   __TEXT._rtk_mtab: 0x2b8
-  __TEXT.__cstring: 0xa37aa
+  __TEXT.__cstring: 0xa38c0
   __TEXT.__data_copy: 0x200000
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA._rtk_boot_l1: 0x80
   __DATA.__gxf_data: 0x10
   __DATA.__zerofill: 0x5bb620
-  UUID: 7FFF55B8-A0B6-375C-BA24-3D7EB9B554FE
+  UUID: 9FD7F568-B660-306D-B5EE-E11F585266C0
   Functions: 0
   Symbols:   0
-  CStrings:  17880
+  CStrings:  17882
 
CStrings:
+ "(bandwidthCtrl.scratchRegisterAddr >= PMC_BWR_AGENT_INTERFACE_START_ADDR && bandwidthCtrl.scratchRegisterAddr < PMC_BWR_AGENT_INTERFACE_END_ADDR)"
+ "(clockCtrl.scratchRegisterAddr >= PMS_PTD_UPDATE_SPACE_START_ADDR && clockCtrl.scratchRegisterAddr < PMS_PTD_UPDATE_SPACE_END_ADDR)"
+ "18:55:48"
- "21:24:54"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 543.140.10.0.0
-  __TEXT.__text: 0x4efdf4
+  __TEXT.__text: 0x4f0274
   __TEXT.__lcxx_override: 0x200
   __TEXT.__cstring: 0x3a03f
   __TEXT.__const: 0xfe6c8

   __TEXT.__term_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x40
-  __TEXT.__eh_frame: 0x27494
+  __TEXT.__eh_frame: 0x27454
   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x2a8
   __DATA.__mod_init_func: 0x38

   __PDATA.__common: 0x2530
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: C18C75E3-7531-377D-A375-D6BDB288D6A1
-  Functions: 19748
+  UUID: 1F115866-F18D-300B-BC27-914E706ABE31
+  Functions: 19754
   Symbols:   0
   CStrings:  5775
 
Functions (added):
+ sub_8072f50
+ sub_824e748
+ sub_83ad958
+ sub_842652c
+ sub_846fb3c
+ sub_84d8104
+ sub_84da5a4
+ sub_84da77c
+ sub_84da794
+ sub_84da8d0
+ sub_84e5614
+ sub_84e575c
+ sub_84e639c
+ sub_84e654c
+ sub_84e660c
+ sub_84e6754

Functions (removed):
- sub_84e7854
- sub_84e80e0
- sub_84e84ac
- sub_84eff14
- sub_84f0550
- sub_84f0870
- sub_84f0ba4
- [3 functions removed in block]
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B4b2ugBj-4W-xvnp5ji6oce7NbWgQMv9ccTMXoc/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.6.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~B4b3ugA1YoM5dFcznu453S5pX6jxgo3qghV3PM8/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.6.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~B4b4ugAsVIhbtfN7bhglAs1ptFJIKt8yPORzuqY/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.6.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "/AppleInternal/Library/BuildRoots/4~B2QSugDlp4jJdIpArgtmJmwKWCq0bVTSthSNPzs/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.6.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B2QTugAaOYSVLiPB9vjfqQHz-UmwVZQVULRdqYo/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.6.Internal.sdk/System/ExclaveCore/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/4~B2qVugAFIK2Xcm1K0dMCaZzwp709zLgORzOLKPw/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS18.6.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.6 *(22G5064d)* | iBoot-11881.140.90.0.1 |
| 18.6 *(22G5073b)* | iBoot-11881.140.95 |

#### 🆕 NEW (5)

<details>
  <summary><i>View NEW</i></summary>

##### `iboot`
  - `G56d0^(J[f`
  - `I4q%jTU;jT`
  - `ʂ)Ĺ"jF$N`
  - `5/JEDCF>d-%}`
  - `H)l90!:á<`
  - `x*9Ǧ[Çu#`
  - `l(G5LEoBARe$J>}z`
  - `i+dLEXWUZeaW`
  - `(42êqFHB?`
  - `root@qwdh2.p1l.plx.sd...2025/07/02@23:57:15`
  - `967e686f15e0c4707a92c01c75926aa2`
  - `iBoot-11881.140.95`
  - `Q}6ukR˴GR`
  - `rVdf iAib^`
  - `EplBSFtpT"e`
  - `uutrrxsqpsQ`
  - `O7uw(aMw~7n`
  - `d8,EC+D1TU[s`
  - `Q/S#/wvM"}9`
  - `~ȇ|ȇ|ȇ|`
  - `ǨmB?x%ʊB`
  - `}D,n9)IiNJO`
  - `5ŪKFYSb+DVh`
##### `RTKit.bin`
  - `SPMI Fatal Error: %s `
  - `drv_gg_veridian.cpp`
  - `Read Shelf life-  data=%d, return state=%d , rc = %d`
##### `iboot_blob28.bin`
  - `COFOROSOTO6h`
  - `TCAPACDLHDHPNIRNDVPUVilpslpVt`
  - `DAcKBcSBcSHcOIcDLcTRcSAmBDmCFmLFmCHmSMmkl<`
  - `!C#C?CRC]l`
##### `iboot_blob31.bin`
  - `HW Q Reset`
  - `Filter Modification`
##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-5204.140.29.d93.REL`

</details>

#### ❌ Removed (5)

<details>
  <summary><i>View Removed</i></summary>

##### `RTKit.bin`
  - `HW Q Reset`
  - `lf life-  data=%d, return state=%d , rc = %d`
  - `SPMI Fatal Error: %s Blocked`
##### `AppleSMCFirmware.bin`
  - `AppleSMCFirmware_H17-5204.140.28.d93.REL`
##### `iboot_blob31.bin`
  - `er Modification`
##### `iboot`
  - `5vT/jT/RGz4`
  - `uutsrwsqpsQ`
  - `Bd>Ww!KP q`
  - `kmTvh#[1jK`
  - `6.............`
  - `YO68v!&EY)`
  - `sIzꝣ,dgm`
  - `rlɃeV)@#%g"2`
  - `œcYɤw[$O`
  - `iBoot-11881.140.90.0.1`
  - `LvsY5^"/( `
  - `˸"M1lHGT]`
  - `,Op8y,p-63`
  - `!*9yG\ErV#Q`
  - `ki*T@:$L^AAb`
  - `-=?%iȿ6,H`
  - `%9Os¤E4-T7`
  - `Ty'R5:+'a;`
  - `root@89h6x.p1l.plx.sd...2025/06/10@19:32:25`
  - `2ea74dc3b99c4070b3f2f3a58af93d05`
  - `{U\\\\\\\\\\\`
  - `(C%ek4,ËC`
  - `}P-2Z5UiVMR`
  - `z<()%5ǥƔ`
  - `9~_ âʝk]`
##### `iboot_blob28.bin`
  - `TCAPACDLHDHPNIRNDVPUVilpslpVX`
  - `COFOROSOTO6P`
  - `1SB2SBTFCATCEPDPIHMPLrAPsDPfNPTPPpSPiW`
  - `DAcKBcSBcSHcOIcDLcTRcSAmBDmCFmLFmCHmSMmkP<`
  - `!C#C?CRC]T`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.6 *(22G5064d)* | 621.3.7.10.1 |
| 18.6 *(22G5073b)* | 621.3.8.0.0 |

### Dylibs

#### ⬆️ Updated (100)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/AccessibilityBundles/UserNotificationsUIKit.axbundle/UserNotificationsUIKit](DYLIBS/UserNotificationsUIKit.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Assignables.framework/Assignables](DYLIBS/Assignables.md)
- [/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices](DYLIBS/AuthenticationServices.md)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreML.framework/CoreML](DYLIBS/CoreML.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/FinanceKit.framework/FinanceKit](DYLIBS/FinanceKit.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit](DYLIBS/MarketplaceKit.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem](DYLIBS/APConfigurationSystem.md)
- [/System/Library/PrivateFrameworks/APTransport.framework/APTransport](DYLIBS/APTransport.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AppDistribution.framework/AppDistribution](DYLIBS/AppDistribution.md)
- [/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore](DYLIBS/AppSSOCore.md)
- [/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation](DYLIBS/CDMFoundation.md)
- [/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging](DYLIBS/CMImaging.md)
- [/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete](DYLIBS/CacheDelete.md)
- [/System/Library/PrivateFrameworks/Celestial.framework/Celestial](DYLIBS/Celestial.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/CoreIDVRGBLiveness.framework/CoreIDVRGBLiveness](DYLIBS/CoreIDVRGBLiveness.md)
- [/System/Library/PrivateFrameworks/CryptexServer.framework/CryptexServer](DYLIBS/CryptexServer.md)
- [/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy](DYLIBS/DifferentialPrivacy.md)
- [/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess](DYLIBS/DigitalAccess.md)
- [/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2](DYLIBS/DiskImages2.md)
- [/System/Library/PrivateFrameworks/Espresso.framework/Espresso](DYLIBS/Espresso.md)
- [/System/Library/PrivateFrameworks/FSKit.framework/FSKit](DYLIBS/FSKit.md)
- [/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon](DYLIBS/FinanceDaemon.md)
- [/System/Library/PrivateFrameworks/FindMyBluetooth.framework/FindMyBluetooth](DYLIBS/FindMyBluetooth.md)
- [/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice](DYLIBS/FindMyDevice.md)
- [/System/Library/PrivateFrameworks/FindMyUICore.framework/FindMyUICore](DYLIBS/FindMyUICore.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime](DYLIBS/GenerativeExperiencesRuntime.md)
- [/System/Library/PrivateFrameworks/Hands.framework/Hands](DYLIBS/Hands.md)
- [/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon](DYLIBS/HomeKitDaemon.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter](DYLIBS/KeyboardArbiter.md)
- [/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle](DYLIBS/KeychainCircle.md)
- [/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis](DYLIBS/MediaAnalysis.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework](DYLIBS/MetricsFramework.md)
- [/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate](DYLIBS/MobileInBoxUpdate.md)
- [/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer](DYLIBS/MobileMulticastTransfer.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate](DYLIBS/MobileSoftwareUpdate.md)
- [/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore](DYLIBS/NewsCore.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorage.framework/OnDeviceStorage](DYLIBS/OnDeviceStorage.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageCore.framework/OnDeviceStorageCore](DYLIBS/OnDeviceStorageCore.md)
- [/System/Library/PrivateFrameworks/OnDeviceStorageInternal.framework/OnDeviceStorageInternal](DYLIBS/OnDeviceStorageInternal.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO](DYLIBS/PlatformSSO.md)
- [/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit](DYLIBS/PodcastsKit.md)
- [/System/Library/PrivateFrameworks/PromotedContent.framework/PromotedContent](DYLIBS/PromotedContent.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/RapidResourceDelivery.framework/RapidResourceDelivery](DYLIBS/RapidResourceDelivery.md)
- [/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner](DYLIBS/SPOwner.md)
- [/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore](DYLIBS/SafariCore.md)
- [/System/Library/PrivateFrameworks/Sage.framework/Sage](DYLIBS/Sage.md)
- [/System/Library/PrivateFrameworks/SiriFindMy.framework/SiriFindMy](DYLIBS/SiriFindMy.md)
- [/System/Library/PrivateFrameworks/SiriInformationSearch.framework/SiriInformationSearch](DYLIBS/SiriInformationSearch.md)
- [/System/Library/PrivateFrameworks/SiriNLUTypes.framework/SiriNLUTypes](DYLIBS/SiriNLUTypes.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateServicesUI.framework/SoftwareUpdateServicesUI](DYLIBS/SoftwareUpdateServicesUI.md)
- [/System/Library/PrivateFrameworks/SonicFoundation.framework/SonicFoundation](DYLIBS/SonicFoundation.md)
- [/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit](DYLIBS/SummarizationKit.md)
- [/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks](DYLIBS/WebBookmarks.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/XCTTargetBootstrap](DYLIBS/XCTTargetBootstrap.md)
- [/System/Library/VideoCodecs/H264SW.videocodec](DYLIBS/H264SW.videocodec.md)
- [/System/Library/VideoDecoders/H264H8.videodecoder](DYLIBS/H264H8.videodecoder.md)
- [/System/Library/VideoDecoders/JPEGH1.videodecoder](DYLIBS/JPEGH1.videodecoder.md)
- [/System/Library/VideoEncoders/JPEGH1.videoencoder](DYLIBS/JPEGH1.videoencoder.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/usr/lib/libcryptex.dylib](DYLIBS/libcryptex.dylib.md)
- [/usr/lib/libcryptex_core.dylib](DYLIBS/libcryptex_core.dylib.md)
- [/usr/lib/libcryptex_interface.dylib](DYLIBS/libcryptex_interface.dylib.md)
- [/usr/lib/libcryptex_trampoline.dylib](DYLIBS/libcryptex_trampoline.dylib.md)
- [/usr/lib/libsqlite3.dylib](DYLIBS/libsqlite3.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/libxslt.1.dylib](DYLIBS/libxslt.1.dylib.md)
- [/usr/lib/system/liblaunch.dylib](DYLIBS/liblaunch.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)

</details>

## Files

### 🆕 New

#### IPSW (2)

- `Firmware/Mav24-1.70.02.Release.bbfw`
- `Firmware/Mav24-1.70.02.Release.plist`

#### filesystem (101)

<details>
  <summary><i>View Files</i></summary>

- `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/Entitlements.plist`
- `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/FMDCFUTheftAndLossReminderExtension`
- `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/Info.plist`
- `/Applications/FindMyRemoteUIService.app/PlugIns/FMDCFUTheftAndLossReminderExtension.appex/_CodeSignature/CodeResources`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/metadata/mediaType.dtag/pl.dtag.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Templates/metadata/musicGenre.dtag/pl.dtag.bin`
- `/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/Templates/metadata/dailyBriefingDomainNames.dtag/pl.dtag.bin`
- `/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APCS/APAMSNetworkFacade/ConfigurationNode.json`
- `/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APCS/Policy/AggregatedTimespent/ConfigurationNode.json`
- `/System/Library/PrivateFrameworks/IMDaemonCore.framework/MessageSendableUTIs.plist`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_CallContact.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/fr-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Contacts_FacetimeContact.cat/zh-tw.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/ar.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/da.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/de.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/en-au.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/en-ca.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/en-gb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/es-mx.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/es.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/fi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/fr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/he.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/hi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/it.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/ja.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/ko.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/ms.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/nb.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/nl.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/pt.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/ru.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/sv.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/th.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/tr.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/vi.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/yue.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/zh-cn.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/zh-hk.cat.bin`
- `/System/Library/PrivateFrameworks/SiriSuggestionsBaseModel.framework/Templates/dialog/BaseSuggestions.catfamily/Notes_CreateNote.cat/zh-tw.cat.bin`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/281779a4b5f38c348e28b6d402fafd4b0caeaa2d.asset`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/281779a4b5f38c348e28b6d402fafd4b0caeaa2d.asset/AssetData`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/281779a4b5f38c348e28b6d402fafd4b0caeaa2d.asset/AssetData/CarPlayAppDenylist.plist`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/281779a4b5f38c348e28b6d402fafd4b0caeaa2d.asset/AssetData/CarPlayCapabilities.plist`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/281779a4b5f38c348e28b6d402fafd4b0caeaa2d.asset/AssetData/CarPlayDisabledAssetIDs.plist`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/281779a4b5f38c348e28b6d402fafd4b0caeaa2d.asset/AssetData/CarPlayLiveActivitiesDenylist.plist`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/281779a4b5f38c348e28b6d402fafd4b0caeaa2d.asset/Info.plist`

</details>

### ❌ Removed

#### IPSW (2)

- `Firmware/Mav24-1.70.01.Release.bbfw`
- `Firmware/Mav24-1.70.01.Release.plist`

#### filesystem (7)

- `/System/Library/Messages/PlugIns/iMessage.imservice/MessageSendableUTIs.plist`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/ef74750324338ab23d16544744b1ef52ce4d3d8c.asset`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/ef74750324338ab23d16544744b1ef52ce4d3d8c.asset/AssetData`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/ef74750324338ab23d16544744b1ef52ce4d3d8c.asset/AssetData/CarPlayAppDenylist.plist`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/ef74750324338ab23d16544744b1ef52ce4d3d8c.asset/AssetData/CarPlayCapabilities.plist`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/ef74750324338ab23d16544744b1ef52ce4d3d8c.asset/AssetData/CarPlayDisabledAssetIDs.plist`
- `/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs/com_apple_MobileAsset_CarExperienceAssets/ef74750324338ab23d16544744b1ef52ce4d3d8c.asset/Info.plist`

## Feature Flags

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### MarketplaceKit.plist

>  `Domain/MarketplaceKit.plist`

```diff

 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
 <plist version="1.0">
 <dict>
+	<key>NewInstallSheetFlow</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>WebDistribution</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```


</details>

## EOF
