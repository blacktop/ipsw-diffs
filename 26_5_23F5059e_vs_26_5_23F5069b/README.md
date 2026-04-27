# 26.5 (23F5059e) .vs 26.5 (23F5069b)

## Inputs

- `iPhone18,1_26.5_23F5059e_Restore.ipsw`
- `iPhone18,1_26.5_23F5069b_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.5 *(23F5059e)* | 25.5.0 | 12377.120.99.0.7~26 | Tue, 14Apr2026 22:07:12 PDT |
| 26.5 *(23F5069b)* | 25.5.0 | 12377.122.4~2 | Thu, 23Apr2026 21:27:42 PDT |

### Kexts

### ⬆️ Updated (9)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.AGXG18P

>  `com.apple.AGXG18P`

```diff

-350.40.0.0.0
+351.1.0.0.0
   __TEXT.__const: 0x42f4
   __TEXT.__os_log: 0xfff
-  __TEXT.__cstring: 0x123ba
-  __TEXT_EXEC.__text: 0xd48fc
+  __TEXT.__cstring: 0x1213f
+  __TEXT_EXEC.__text: 0xd4920
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1594
   __DATA.__common: 0x10

   __DATA_CONST.__const: 0x117c8
   __DATA_CONST.__kalloc_type: 0x2580
   __DATA_CONST.__kalloc_var: 0x3bb0
-  UUID: BA6E2679-9541-3E29-BDB9-28F184B0D108
+  UUID: A752C2B4-27A0-3B93-BB24-F0C32C19CB8C
   Functions: 3470
   Symbols:   0
-  CStrings:  2099
+  CStrings:  2096
 
Functions:
~ sub_fffffe0008305230 : 3700 -> 3908
~ sub_fffffe0008313d70 -> sub_fffffe0008313e40 : 2016 -> 2068
~ sub_fffffe0008321fb0 -> sub_fffffe00083220b4 : 4712 -> 4528
~ sub_fffffe000832474c -> sub_fffffe0008324798 : 792 -> 776
~ sub_fffffe000839ca84 -> sub_fffffe000839cac0 : 5820 -> 5796
CStrings:
+ "AGXk: %s:%d:%s: !!! AGXCLChannelSKSM::submitBuffer: context_id is negative (%d)\n"
+ "AGXk: %s:%d:%s: !!! AGXCLChannelSKSM::submitBuffer: context_id is out of range (%d)\n"
+ "AGXk: %s:%d:%s: !!! AGXCLChannelSKSM::submitBuffer: event_flag_idx out of bounds (priority_type=%u, context_id=%u)\n"
+ "AGXk: %s:%d:%s: !!! AGXCLChannelSKSM::submitBuffer: priority_type out of bounds (%u)\n"
+ "Apr 23 2026 21:10:49"
+ "void _expectInner(bool, const char *, const int, const char *, ...)"
- "Apr 14 2026 21:56:40"
- "void _expect(bool, T, const char *, U, const char *, const char *, const char *, const int) [T = AGFIFirmwareChannelErrorType, U = AGFIFirmwareChannelErrorType]"
- "void _expect(bool, T, const char *, U, const char *, const char *, const char *, const int) [T = _AGFIDataMasterType, U = _AGFIDataMasterType]"
- "void _expect(bool, T, const char *, U, const char *, const char *, const char *, const int) [T = int, U = int]"
- "void _expect(bool, T, const char *, U, const char *, const char *, const char *, const int) [T = unsigned int, U = AGFIPowerPIControllerType]"
- "void _expect(bool, T, const char *, U, const char *, const char *, const char *, const int) [T = unsigned int, U = _AGFIDataMasterType]"
- "void _expect(bool, T, const char *, U, const char *, const char *, const char *, const int) [T = unsigned int, U = int]"
- "void _expect(bool, T, const char *, U, const char *, const char *, const char *, const int) [T = unsigned long long, U = int]"
- "void _expect(bool, T, const char *, U, const char *, const char *, const char *, const int) [T = unsigned short, U = unsigned long]"

```

#### com.apple.driver.AppleSEPKeyStore

>  `com.apple.driver.AppleSEPKeyStore`

```diff

-2155.120.3.0.0
-  __TEXT.__cstring: 0x44ff
+2155.122.1.0.0
+  __TEXT.__cstring: 0x452f
   __TEXT.__const: 0x96c
-  __TEXT_EXEC.__text: 0x3c938
+  __TEXT_EXEC.__text: 0x3c958
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3a4
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x3ac8
   __DATA_CONST.__kalloc_type: 0xd80
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 91913DBD-62FF-3C38-84CC-B3A736C28A14
+  UUID: 93002446-51B9-3F83-9457-6ED02E003808
   Functions: 1014
   Symbols:   0
-  CStrings:  369
+  CStrings:  370
 
Functions:
~ __ZN23AppleKeyStoreUserClient24handleUserClientSelectorEjP25IOExternalMethodArguments : 33748 -> 33780
CStrings:
+ "2155.122.1"
+ "21:13:39"
+ "Apr 23 2026"
+ "com.apple.keystore.config.set.inactivity_reboot"
- "2155.120.3"
- "21:55:53"
- "Apr 14 2026"

```

#### com.apple.driver.IOPAudioVoiceTriggerDevice

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 540.3.0.0.0
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x2ed9
+  __TEXT.__cstring: 0x2ed0
   __TEXT.__os_log: 0x1726
   __TEXT_EXEC.__text: 0xad44
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1720
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 620429FB-5789-3921-95A6-DC6CD74862C0
+  UUID: 9F979996-8C8E-3294-92B1-BE393CE26A59
   Functions: 275
   Symbols:   0
-  CStrings:  240
+  CStrings:  239
 
CStrings:
+ "21:25:00"
+ "Apr 23 2026"
- "21:50:24"
- "21:50:25"
- "Apr 14 2026"

```

#### com.apple.filesystems.apfs

>  `com.apple.filesystems.apfs`

```diff

-2811.120.11.0.0
+2811.120.14.0.1
   __TEXT.__const: 0x9a8
-  __TEXT.__cstring: 0x4d4b0
-  __TEXT_EXEC.__text: 0x148314
+  __TEXT.__cstring: 0x4d4b8
+  __TEXT_EXEC.__text: 0x148324
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x70c
   __DATA.__bss: 0xd48
-  __DATA_CONST.__auth_got: 0x1178
+  __DATA_CONST.__auth_got: 0x1180
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__kalloc_type: 0x5080
   __DATA_CONST.__kalloc_var: 0x2990
   __DATA_CONST.__assert: 0x14
-  UUID: 7D621795-CF59-3CF5-9137-2B55FCA4FC19
+  UUID: 951C49ED-1762-3AE6-8594-FD5F36431280
   Functions: 2334
   Symbols:   0
   CStrings:  6692
Functions:
~ _handle_snapshot_mount : 2748 -> 2764
CStrings:
+ "2026/04/23"
+ "21:04:12"
+ "2811.120.14.0.1"
+ "Apr 23 2026"
+ "apfs-2811.120.14.0.1"
- "2026/04/14"
- "21:20:38"
- "2811.120.11"
- "Apr 14 2026"
- "apfs-2811.120.11"

```

#### com.apple.iokit.IOTimeSyncFamily

>  `com.apple.iokit.IOTimeSyncFamily`

```diff

-1450.1.0.0.0
+1450.2.0.0.0
   __TEXT.__cstring: 0x3e62
   __TEXT.__os_log: 0x89ce
   __TEXT.__const: 0x1d8
-  __TEXT_EXEC.__text: 0x30c24
+  __TEXT_EXEC.__text: 0x30ca0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd4
   __DATA.__common: 0x688
   __DATA.__bss: 0x41
-  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x100

   __DATA_CONST.__const: 0xc550
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: AC2ECF7E-9AED-3A1E-BC12-68DAF87CDE80
+  UUID: DAC6C54E-015D-3DCE-ABE7-3D9B3A7710F9
   Functions: 1483
   Symbols:   0
   CStrings:  721
Functions:
~ sub_fffffe000a0d56a4 -> sub_fffffe000a0d56e4 : 968 -> 972
~ __ZN12IOUserClient21copyClientEntitlementEP4taskPKc : 1212 -> 1268
~ sub_fffffe000a0d605c -> sub_fffffe000a0d60d8 : 240 -> 248
~ sub_fffffe000a0d614c -> sub_fffffe000a0d61d0 : 356 -> 360
~ sub_fffffe000a0d62b0 -> sub_fffffe000a0d6338 : 240 -> 248
~ sub_fffffe000a0d63a0 -> sub_fffffe000a0d6430 : 356 -> 364
~ __ZN32IOTimeSyncClockManagerUserClient20addUserFilteredClockEyyhbPy : 304 -> 328
~ sub_fffffe000a0d6634 -> sub_fffffe000a0d66e4 : 300 -> 312

```

#### com.apple.kec.corecrypto

>  `com.apple.kec.corecrypto`

```diff

-1922.120.7.0.0
+1922.122.1.0.0
   __TEXT.__cstring: 0x4c7d
   __TEXT.__const: 0x196e0
   __TEXT.__fips_hmacs: 0x20
-  __TEXT_EXEC.__text: 0x69f94
+  __TEXT_EXEC.__text: 0x6a6ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x9340
   __DATA.__bss: 0x29e0

   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x178
   __DATA_CONST.__const: 0x3fc8
-  UUID: 90CE7597-4E5A-343C-82D4-DF472682D892
+  UUID: FE36ADEC-348B-3C8A-BE6D-2D60A910526E
   Functions: 1847
   Symbols:   0
   CStrings:  463

```

#### com.apple.kernel

>  `com.apple.kernel`

```diff

-12377.120.99.0.7
-  __TEXT.__const: 0x363e0
+12377.122.4.0.0
+  __TEXT.__const: 0x363d0
   __TEXT.__copyio_vectors: 0x2c0
   __TEXT.__cstring: 0x88592
-  __TEXT.__os_log: 0x3df0f
+  __TEXT.__os_log: 0x3ded0
   __TEXT.__eh_frame: 0x7e0
   __DATA_CONST.__hib_const: 0x120
   __DATA_CONST.__const: 0x119da0

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_SPTM.__const: 0x3c000
   __TEXT_EXEC.__hib_text: 0xed8
-  __TEXT_EXEC.__text: 0x8b6cdc
+  __TEXT_EXEC.__text: 0x8b6be8
   __TEXT_BOOT_EXEC.__bootcode: 0x5250
   __KLD.__text: 0x1460
   __LASTDATA_CONST.__mod_init_func: 0x8

   __PLK_LLVM_COV.__llvm_covmap: 0x0
   __PLK_LINKEDIT.__data: 0x0
   __LINKINFO.__symbolsets: 0x4804e
-  UUID: E9066B72-405C-314B-82C9-C674B6CA3355
+  UUID: 14DEDADF-FDEF-33B3-BB62-CD57869A86A4
   Functions: 21334
   Symbols:   0
-  CStrings:  20748
+  CStrings:  20747
 
Functions:
~ vm_object_update : 4044 -> 3928
~ sub_fffffe000a78ebd0 -> sub_fffffe000a78eb5c : 812 -> 808
~ vm_map_copy_overwrite_impl : 2692 -> 2656
~ flow_divert_token_set : 948 -> 860
~ sub_fffffe000aef7c18 -> sub_fffffe000aef7b24 : 33768 -> 34012
CStrings:
- "(%u): Token contains a signing identifier and HMAC is missing\n"

```

#### com.apple.nke.l2tp

>  `com.apple.nke.l2tp`

```diff

-1025.0.0.0.0
+1027.0.0.0.0
   __TEXT.__cstring: 0xa63
   __TEXT.__const: 0x58
-  __TEXT_EXEC.__text: 0x3e9c
+  __TEXT_EXEC.__text: 0x3ea8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x130
   __DATA.__common: 0x150

   __DATA_CONST.__got: 0x88
   __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 60276AF8-FDC9-3C61-8B95-B73E3CBB538A
+  UUID: 55D4DBE5-2227-3B37-BE03-FA2045C64742
   Functions: 61
   Symbols:   0
   CStrings:  69
Functions:
~ sub_fffffe000a3a1100 -> sub_fffffe000a3a11b0 : 948 -> 960

```

#### com.apple.security.sandbox

>  `com.apple.security.sandbox`

```diff

-2680.120.11.0.0
+2680.120.12.0.0
   __TEXT.__os_log: 0x2272
-  __TEXT.__const: 0x1caae9
+  __TEXT.__const: 0x1cab91
   __TEXT.__cstring: 0x72d6
   __TEXT_EXEC.__text: 0x38ab8
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x3858
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: B5A4D233-D0CD-370E-B20A-38CB023B42F7
+  UUID: 0FCEC51F-B242-3930-B4FA-071E06C62FED
   Functions: 652
   Symbols:   0
   CStrings:  1344

```


</details>

## MachO

### ⬆️ Updated (143)

<details>
  <summary><i>View Updated</i></summary>

- [/Applications/AccessorySetupUI.app/AccessorySetupUI](MACHOS/AccessorySetupUI.md)
- [/Applications/CarPlayWallpaper.app/CarPlayWallpaper](MACHOS/CarPlayWallpaper.md)
- [/Applications/InCallService.app/InCallService](MACHOS/InCallService.md)
- [/Applications/Media.app/Media](MACHOS/Media.md)
- [/Applications/ScreenshotServicesService.app/ScreenshotServicesService](MACHOS/ScreenshotServicesService.md)
- [/Applications/Siri.app/Siri](MACHOS/Siri.md)
- [/Applications/iCloud.app/iCloud](MACHOS/iCloud.md)
- [/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio](MACHOS/VirtualAudio.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8150_IR_ISP_EK_Component.framework/T8150_IR_ISP_EK_Component_asan](MACHOS/T8150_IR_ISP_EK_Component_asan.md)
- [/System/ExclaveKit/System/Library/Frameworks/T8150_RGB_ISP_EK_Component.framework/T8150_RGB_ISP_EK_Component_asan](MACHOS/T8150_RGB_ISP_EK_Component_asan.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8150_CoreAAClientKit.framework/T8150_CoreAAClientKit_asan](MACHOS/T8150_CoreAAClientKit_asan.md)
- [/System/ExclaveKit/System/Library/PrivateFrameworks/T8150_ExclaveISPSharedLib_exclavekit.framework/T8150_ExclaveISPSharedLib_exclavekit_asan](MACHOS/T8150_ExclaveISPSharedLib_exclavekit_asan.md)
- [/System/ExclaveKit/usr/lib/dyld](MACHOS/dyld.md)
- [/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin](MACHOS/CarCommandsFlowDelegatePlugin.md)
- [/System/Library/CoreServices/AssistiveTouch.app/assistivetouchd](MACHOS/assistivetouchd.md)
- [/System/Library/CoreServices/VoiceOverTouch.app/vot](MACHOS/vot.md)
- [/System/Library/ExtensionKit/Extensions/ProductPageExtension.appex/ProductPageExtension](MACHOS/ProductPageExtension.md)
- [/System/Library/ExtensionKit/Extensions/SubscribePageExtension.appex/SubscribePageExtension](MACHOS/SubscribePageExtension.md)
- [/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs](MACHOS/com.apple.fskit.apfs.md)
- [/System/Library/Filesystems/apfs.fs/apfs_condenser](MACHOS/apfs_condenser.md)
- [/System/Library/Filesystems/apfs.fs/apfs_vol_converter](MACHOS/apfs_vol_converter.md)
- [/System/Library/Filesystems/apfs.fs/fsck_apfs](MACHOS/fsck_apfs.md)
- [/System/Library/Filesystems/apfs.fs/newfs_apfs](MACHOS/newfs_apfs.md)
- [/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd](MACHOS/assetsd.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectory.xpc/com.apple.CallKit.CallDirectory](MACHOS/com.apple.CallKit.CallDirectory.md)
- [/System/Library/Frameworks/CallKit.framework/XPCServices/com.apple.CallKit.CallDirectoryMaintenance.xpc/com.apple.CallKit.CallDirectoryMaintenance](MACHOS/com.apple.CallKit.CallDirectoryMaintenance.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTestImporter.appex/CoreSpotlightTestImporter](MACHOS/CoreSpotlightTestImporter.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/PlugIns/CoreSpotlightTextImporter.appex/CoreSpotlightTextImporter](MACHOS/CoreSpotlightTextImporter.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/Support/com.apple.spotlight.IndexAgent](MACHOS/com.apple.spotlight.IndexAgent.md)
- [/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent](MACHOS/ManagedSettingsAgent.md)
- [/System/Library/Frameworks/Metal.framework/XPCServices/MTLCompilerService.xpc/MTLCompilerService](MACHOS/MTLCompilerService.md)
- [/System/Library/Frameworks/Security.framework/CircleJoinRequested/CircleJoinRequested](MACHOS/CircleJoinRequested.md)
- [/System/Library/Frameworks/Security.framework/CloudKeychainProxy.bundle/CloudKeychainProxy](MACHOS/CloudKeychainProxy.md)
- [/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper](MACHOS/TrustedPeersHelper.md)
- [/System/Library/Frameworks/Security.framework/swcagent](MACHOS/swcagent.md)
- [/System/Library/Frameworks/UIKit.framework/PlugIns/com.apple.UIKit.ShareUI.appex/com.apple.UIKit.ShareUI](MACHOS/com.apple.UIKit.ShareUI.md)
- [/System/Library/Messages/PlugIns/RCS.imservice/RCS](MACHOS/RCS.md)
- [/System/Library/Messages/PlugIns/iMessage.imservice/iMessage](MACHOS/iMessage.md)
- [/System/Library/Messages/iMessageBalloons/ASMessagesProvider.bundle/ASMessagesProvider](MACHOS/ASMessagesProvider.md)
- [/System/Library/NanoPreferenceBundles/SetupBundles/HealthFeaturesBridgeSetupPlugin.bundle/HealthFeaturesBridgeSetupPlugin](MACHOS/HealthFeaturesBridgeSetupPlugin.md)
- [/System/Library/NanoTimeKit/FaceBundles/KaleidoscopeFaceBundle.bundle/NTKKaleidoscopeShaders.metallib](MACHOS/NTKKaleidoscopeShaders.metallib.md)
- [/System/Library/NanoTimeKit/FaceBundles/NTKWarlockFaceBundle.bundle/warlock.metallib](MACHOS/warlock.metallib.md)
- [/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings](MACHOS/AppleAccountSettings.md)
- [/System/Library/PreferenceBundles/AccountSettings/CloudKitSettings.bundle/CloudKitSettings](MACHOS/CloudKitSettings.md)
- [/System/Library/PreferenceBundles/BackgroundSecurityImprovement.bundle/BackgroundSecurityImprovement](MACHOS/BackgroundSecurityImprovement.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/deflicker-binary-applegpu_g18p.metallib](MACHOS/deflicker-binary-applegpu_g18p.metallib.md)
- [/System/Library/PrivateFrameworks/ARKitCore.framework/deflicker-binary.metallib](MACHOS/deflicker-binary.metallib.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/XPCServices/HeuristicInterpreter.xpc/HeuristicInterpreter](MACHOS/HeuristicInterpreter.md)
- [/System/Library/PrivateFrameworks/AppInstallationMetrics.framework/Support/appinstallationmetricsd](MACHOS/appinstallationmetricsd.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/XPCServices/AppPredictionIntentsHelperService.xpc/AppPredictionIntentsHelperService](MACHOS/AppPredictionIntentsHelperService.md)
- [/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored](MACHOS/appstored.md)
- [/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/appleaccounttransparencyd](MACHOS/appleaccounttransparencyd.md)
- [/System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/XPCServices/AppleIntelligenceReportingProcessingService.xpc/AppleIntelligenceReportingProcessingService](MACHOS/AppleIntelligenceReportingProcessingService.md)
- [/System/Library/PrivateFrameworks/ApplePushService.framework/apsd](MACHOS/apsd.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd](MACHOS/assistantd.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/akd](MACHOS/akd.md)
- [/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKAppSSOExtension.appex/AKAppSSOExtension](MACHOS/AKAppSSOExtension.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/XPCServices/CSExattrCryptoService.xpc/CSExattrCryptoService](MACHOS/CSExattrCryptoService.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/ckdiscretionaryd](MACHOS/ckdiscretionaryd.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Support/cloudd](MACHOS/cloudd.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf](MACHOS/parsec-fbf.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/parsecd](MACHOS/parsecd.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/default-binaryarchive.metallib](MACHOS/default-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreRE.framework/mxi-binaryarchive.metallib](MACHOS/mxi-binaryarchive.metallib.md)
- [/System/Library/PrivateFrameworks/CoreRE3DGSFoundation.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.Microstackshot.appex/com.apple.DiagnosticExtensions.Microstackshot](MACHOS/com.apple.DiagnosticExtensions.Microstackshot.md)
- [/System/Library/PrivateFrameworks/EmailDaemon.framework/maild](MACHOS/maild.md)
- [/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd](MACHOS/identityservicesd.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent](MACHOS/imagent.md)
- [/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted](MACHOS/mediaremoted.md)
- [/System/Library/PrivateFrameworks/MentalHealthUI.framework/archive.metallib](MACHOS/archive.metallib.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd](MACHOS/migrationd.md)
- [/System/Library/PrivateFrameworks/NanoUniverse.framework/NUNICalliopeShadersCompanion.metallib](MACHOS/NUNICalliopeShadersCompanion.metallib.md)
- [/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/ndoagent](MACHOS/ndoagent.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/NewsScoringService.xpc/NewsScoringService](MACHOS/NewsScoringService.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PlugIns/DEPowerlogEPL.appex/DEPowerlogEPL](MACHOS/DEPowerlogEPL.md)
- [/System/Library/PrivateFrameworks/Search.framework/PlugIns/SpotlightDiagnostic.appex/SpotlightDiagnostic](MACHOS/SpotlightDiagnostic.md)
- [/System/Library/PrivateFrameworks/Search.framework/searchd](MACHOS/searchd.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd](MACHOS/callservicesd.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/Artwork.bundle/Artwork](MACHOS/Artwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/BoundingPathData.bundle/BoundingPathData](MACHOS/BoundingPathData.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/CarPlayArtwork.bundle/CarPlayArtwork](MACHOS/CarPlayArtwork.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/TextEffectsCatalog.bundle/TextEffectsCatalog](MACHOS/TextEffectsCatalog.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/XPCServices/com.apple.UIKit.KeyboardManagement.xpc/com.apple.UIKit.KeyboardManagement](MACHOS/com.apple.UIKit.KeyboardManagement.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/Support/usernotificationsd](MACHOS/usernotificationsd.md)
- [/System/Library/PrivateFrameworks/VectorKit.framework/metal_libraries/binary.metallib](MACHOS/binary.metallib.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/bird](MACHOS/bird.md)
- [/System/Library/SystemConfiguration/EAPOLController.bundle/eapolclient](MACHOS/eapolclient.md)
- [/System/Library/UserNotifications/Bundles/com.apple.Siri.ActionPredictionNotifications.bundle/com.apple.Siri.ActionPredictionNotifications](MACHOS/com.apple.Siri.ActionPredictionNotifications.md)
- [/System/Library/VideoProcessors/ColourConstancyV1.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/DepthProcessorV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/STF.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/SuperResolutionV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoDeghostingV1.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoDeghostingV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p](MACHOS/binaryArchive.g18p.md)
- [/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p_a0](MACHOS/binaryArchive.g18p_a0.md)
- [/private/var/staged_system_apps/AppStore.app/AppStore](MACHOS/AppStore.md)
- [/private/var/staged_system_apps/Freeform.app/Frameworks/TSMediaLibrary.framework/TSMediaLibrary](MACHOS/TSMediaLibrary.md)
- [/private/var/staged_system_apps/Home.app/PlugIns/HomeWidget.appex/HomeWidget](MACHOS/HomeWidget.md)
- [/private/var/staged_system_apps/KaleidoscopePosterApp.app/Extensions/KaleidoscopePoster.appex/NTKKaleidoscopeShaders.metallib](MACHOS/NTKKaleidoscopeShaders.metallib.md)
- [/private/var/staged_system_apps/Maps.app/Maps](MACHOS/Maps.md)
- [/private/var/staged_system_apps/MobileMail.app/MobileMail](MACHOS/MobileMail.md)
- [/private/var/staged_system_apps/MobileNotes.app/PlugIns/com.apple.mobilenotes.SpotlightIndexExtension.appex/com.apple.mobilenotes.SpotlightIndexExtension](MACHOS/com.apple.mobilenotes.SpotlightIndexExtension.md)
- [/private/var/staged_system_apps/Photos.app/Photos](MACHOS/Photos.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/NowPlayingUI.framework/NowPlayingUI](MACHOS/NowPlayingUI.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKit.framework/ShelfKit](MACHOS/ShelfKit.md)
- [/private/var/staged_system_apps/Podcasts.app/Frameworks/ShelfKitCollectionViews.framework/ShelfKitCollectionViews](MACHOS/ShelfKitCollectionViews.md)
- [/private/var/staged_system_apps/Podcasts.app/Podcasts](MACHOS/Podcasts.md)
- [/private/var/staged_system_apps/PridePosterApp.app/Extensions/PridePosterExtension.appex/PridePosterExtension](MACHOS/PridePosterExtension.md)
- [/private/var/staged_system_apps/SequoiaTranslator.app/SequoiaTranslator](MACHOS/SequoiaTranslator.md)
- [/private/var/staged_system_apps/Shortcuts.app/Shortcuts](MACHOS/Shortcuts.md)
- [/usr/bin/searchdiagnose](MACHOS/searchdiagnose.md)
- [/usr/lib/dyld](MACHOS/dyld.md)
- [/usr/libexec/ASPCarryLog](MACHOS/ASPCarryLog.md)
- [/usr/libexec/appleaccountd](MACHOS/appleaccountd.md)
- [/usr/libexec/deviceaccessd](MACHOS/deviceaccessd.md)
- [/usr/libexec/duetexpertd](MACHOS/duetexpertd.md)
- [/usr/libexec/eligibilityd](MACHOS/eligibilityd.md)
- [/usr/libexec/icloudwebd](MACHOS/icloudwebd.md)
- [/usr/libexec/inboxupdaterd](MACHOS/inboxupdaterd.md)
- [/usr/libexec/keychainsharingmessagingd](MACHOS/keychainsharingmessagingd.md)
- [/usr/libexec/languageassetd](MACHOS/languageassetd.md)
- [/usr/libexec/locationd](MACHOS/locationd.md)
- [/usr/libexec/misd](MACHOS/misd.md)
- [/usr/libexec/safetycheckd](MACHOS/safetycheckd.md)
- [/usr/libexec/securityd](MACHOS/securityd.md)
- [/usr/libexec/securityuploadd](MACHOS/securityuploadd.md)
- [/usr/libexec/spotlightknowledged.graph](MACHOS/spotlightknowledged.graph.md)
- [/usr/libexec/srp-mdns-proxy](MACHOS/srp-mdns-proxy.md)
- [/usr/libexec/sysdiagnose_helper](MACHOS/sysdiagnose_helper.md)
- [/usr/libexec/transparencyd](MACHOS/transparencyd.md)
- [/usr/libexec/trustd](MACHOS/trustd.md)
- [/usr/libexec/tvremoted](MACHOS/tvremoted.md)
- [/usr/sbin/bluetoothd](MACHOS/bluetoothd.md)
- [/usr/sbin/cfprefsd](MACHOS/cfprefsd.md)
- [/usr/sbin/distnoted](MACHOS/distnoted.md)
- [/usr/sbin/mDNSResponder](MACHOS/mDNSResponder.md)

</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (6)

<details>
  <summary><i>View Updated</i></summary>

#### AppleAVE2FW_H18.im4p

>  `AppleAVE2FW_H18.im4p`

```diff

 
-  __TEXT.__text: 0x10aedc
+  __TEXT.__text: 0x10aeb8
   __TEXT.__const: 0x2069c
   __TEXT.__cstring: 0x17219
   __TEXT.__init_offsets: 0x0

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc6840
-  UUID: 2ED43E83-BB3B-3570-9A50-35114919AED9
+  UUID: 5FABEFE6-492F-342A-9453-2F3BDBE88DCA
   Functions: 1218
   Symbols:   1704
   CStrings:  2645
Functions:
~ __rtk_arm_start_bootstrap_area : 2696 -> 2660
CStrings:
+ "Caller is /Library/Caches/com.apple.xbs/006E2569-CC16-4140-9564-FFE86B4BB636/TemporaryDirectory.MkvXuW/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:751"
+ "Caller is /Library/Caches/com.apple.xbs/006E2569-CC16-4140-9564-FFE86B4BB636/TemporaryDirectory.MkvXuW/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:756"
- "Caller is /Library/Caches/com.apple.xbs/2732BBF3-751E-4111-810B-9B3FCC6FBA56/TemporaryDirectory.jn6vEv/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:751"
- "Caller is /Library/Caches/com.apple.xbs/2732BBF3-751E-4111-810B-9B3FCC6FBA56/TemporaryDirectory.jn6vEv/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:756"

```

#### adc-silenus-v5x.im4p

>  `adc-silenus-v5x.im4p`

```diff

 
-  __TEXT.__text: 0xb2f90c
+  __TEXT.__text: 0xb2f910
   __TEXT.__const: 0x8522ac
   __TEXT.__cstring: 0xab2ae
   __TEXT.text_env: 0x57888

   __DATA.__mod_init_func: 0x8
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x5eeaf8
-  UUID: 4DB4FEE2-CAF5-37E7-A038-1C9DDA3C1993
+  UUID: 28414802-F50A-3ABF-AC38-B4A3342C4968
   Functions: 9851
   Symbols:   0
   CStrings:  18760
Functions:
~ sub_32e18 : 22152 -> 22156
~ sub_b2f7d0 -> sub_b2f7d4 : 324 -> 316
CStrings:
+ "22:10:46"
- "21:46:12"

```

#### agx_a000

>  `agx_a000`

```diff

 
-  __TEXT.__text: 0x39b20
+  __TEXT.__text: 0x39b14
   __TEXT.__gxf_code: 0x4e28
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__const: 0x1052
+  __TEXT.__const: 0x1062
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x228b

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x59cd8
-  UUID: 714B5B0C-83BB-3453-8C69-C0843F2BE84E
-  Functions: 402
+  UUID: A2AC290B-0007-38AF-BAC6-D0D63BFC027D
+  Functions: 404
   Symbols:   166
   CStrings:  227
 
CStrings:
+ "Apr 23 2026 21:07:05"
- "Apr 14 2026 21:57:01"

```

#### agx_a010

>  `agx_a010`

```diff

 
-  __TEXT.__text: 0x39768
+  __TEXT.__text: 0x3975c
   __TEXT.__gxf_code: 0x4e28
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__const: 0x1052
+  __TEXT.__const: 0x1062
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x2341

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x59cd8
-  UUID: 5450485C-9D25-3C78-BF4E-7D2BDA6DF426
-  Functions: 401
+  UUID: 1E1E89BE-3274-3863-8845-968C78685C3F
+  Functions: 403
   Symbols:   166
   CStrings:  229
 
CStrings:
+ "Apr 23 2026 21:13:42"
- "Apr 14 2026 22:05:22"

```

#### agx_b000

>  `agx_b000`

```diff

 
-  __TEXT.__text: 0x39768
+  __TEXT.__text: 0x3975c
   __TEXT.__gxf_code: 0x4e28
   __TEXT.__gxf_code_pad: 0x0
   __TEXT.__gxf_shr_code: 0x558
-  __TEXT.__const: 0x1052
+  __TEXT.__const: 0x1062
   __TEXT._rtk_tunables: 0x740
   __TEXT._rtk_patchbay: 0x231
   __TEXT.__cstring: 0x2341

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x59cd8
-  UUID: 9FA42B4E-097C-3015-AC8F-45F03FBAA96F
-  Functions: 401
+  UUID: 67E0702A-342E-3E59-912B-675E3C6C2882
+  Functions: 403
   Symbols:   166
   CStrings:  229
 
CStrings:
+ "Apr 23 2026 21:11:42"
- "Apr 14 2026 22:02:43"

```

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 1148.120.6.0.0
-  __TEXT.__text: 0x5d5ad4
+  __TEXT.__text: 0x5d5bc4
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x48ed1
   __TEXT.__const: 0x112ee4

   __PDATA.__common: 0x2520
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  UUID: 3F9C3F8A-2356-358F-8C23-5687567C386A
-  Functions: 23500
+  UUID: FB3DEDF5-CBEA-3162-9088-DF9AC3C4E6EC
+  Functions: 23506
   Symbols:   1
   CStrings:  6796
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CNmaugCh0lE8N4uCgL28jvA81EaKLexEHacC0_Y/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CNmcugAqkCeqfyg5AJ2JsMT74qyQjC9UflCD6OU/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CNmdugD_iTWR82e-oH4aNiminZou4isq0Dx8jD4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
+ "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
+ "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
+ "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
+ "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
+ "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
+ "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
+ "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
+ "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
+ "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
+ "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
+ "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
+ "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
+ "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
+ "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
+ "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
+ "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/33ABC8E2-C2DD-42E5-87F0-E056B4C28F0A/TemporaryDirectory.0PnIJb/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"
- "/AppleInternal/Library/BuildRoots/4~CNHaugBXuBL-XHDtOPWz_INyFaEMU0dGeFIU5fg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CNHbugD4BOXjOBh4Bq-Aszw8X8T8DxIOpx3Hoa4/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CNXsugAMiQPZde1wk6gAs4Rcg14Ua9Gf37y3Neg/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.iPhoneOS.platform/Developer/SDKs/ExclaveCore.iPhoneOS26.5.Internal.sdk/System/ExclaveCore/usr/local/standalone/RTKit/usr/include/protocols/mbi_tightbeam_protocol.h"
- "malloc assertion \"!(zone->xzz_memtag_config.enabled && zone->xzz_memtag_config.max_block_size > XZM_SMALL_BLOCK_SIZE_MAX)\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:912)"
- "malloc assertion \"!memtag_config.tag_data\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:8144)"
- "malloc assertion \"((uintptr_t)segment >> XZM_METAPOOL_SEGMENT_BLOCK_SHIFT) < XZM_SEGMENT_TABLE_LIMIT_ENTRY\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/../xzone_malloc/xzone_inline_internal.h:187)"
- "malloc assertion \"(chunk_capacity & 1) == 0 || chunk_padding != 0\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7613)"
- "malloc assertion \"(quarantine && chunk->xzc_empty_count) || (!quarantine && chunk->xzc_guard_count > gc->xxgc_density)\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:677)"
- "malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2574)"
- "malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:2688)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:7225)"
- "malloc assertion \"allocation_front_count == 2\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:866)"
- "malloc assertion \"chunk->xzc_empty_count\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:432)"
- "malloc assertion \"middle_pte % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:892)"
- "malloc assertion \"middle_pte_middle < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:932)"
- "malloc assertion \"old_size\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:6243)"
- "malloc assertion \"range_count == 2\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:887)"
- "malloc assertion \"ranges[0].min_address < middle_pte_middle\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:931)"
- "malloc assertion \"ranges[0].min_address < ranges[0].max_address\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_segment.c:868)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:2106)"
- "malloc assertion \"success\" failed (/Library/Caches/com.apple.xbs/2958E06E-B8A5-4DE0-984D-45A9B5C54972/TemporaryDirectory.ntfYeE/Sources/libmalloc_exclavecore/src/xzone_malloc/xzone_malloc.c:5125)"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.5 *(23F5059e)* | mBoot-18000.120.33.0.1 |
| 26.5 *(23F5069b)* | mBoot-18000.120.36 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.5 *(23F5059e)* | 624.2.4.10.1 |
| 26.5 *(23F5069b)* | 624.2.5.10.4 |

### Dylibs

#### ⬆️ Updated (260)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification](DYLIBS/KeychainSyncAccountNotification.md)
- [/System/Library/Extensions/AGXMetalG18P.bundle/AGXMetalG18P](DYLIBS/AGXMetalG18P.md)
- [/System/Library/Frameworks/AVKit.framework/AVKit](DYLIBS/AVKit.md)
- [/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBNNS.dylib](DYLIBS/libBNNS.dylib.md)
- [/System/Library/Frameworks/AccessoryLiveActivities.framework/AccessoryLiveActivities](DYLIBS/AccessoryLiveActivities.md)
- [/System/Library/Frameworks/AccessoryNotifications.framework/AccessoryNotifications](DYLIBS/AccessoryNotifications.md)
- [/System/Library/Frameworks/AccessoryTransportExtension.framework/AccessoryTransportExtension](DYLIBS/AccessoryTransportExtension.md)
- [/System/Library/Frameworks/ActivityKit.framework/ActivityKit](DYLIBS/ActivityKit.md)
- [/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies](DYLIBS/AACDependencies.md)
- [/System/Library/Frameworks/CloudKit.framework/CloudKit](DYLIBS/CloudKit.md)
- [/System/Library/Frameworks/Contacts.framework/Contacts](DYLIBS/Contacts.md)
- [/System/Library/Frameworks/ContactsUI.framework/ContactsUI](DYLIBS/ContactsUI.md)
- [/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth](DYLIBS/CoreBluetooth.md)
- [/System/Library/Frameworks/CoreImage.framework/CoreImage](DYLIBS/CoreImage.md)
- [/System/Library/Frameworks/CoreMedia.framework/CoreMedia](DYLIBS/CoreMedia.md)
- [/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight](DYLIBS/CoreSpotlight.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib](DYLIBS/libSystemDetermination.dylib.md)
- [/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation](DYLIBS/ExtensionFoundation.md)
- [/System/Library/Frameworks/FinanceKitUI.framework/FinanceKitUI](DYLIBS/FinanceKitUI.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/Frameworks/FoundationModels.framework/FoundationModels](DYLIBS/FoundationModels.md)
- [/System/Library/Frameworks/ImageIO.framework/ImageIO](DYLIBS/ImageIO.md)
- [/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore](DYLIBS/JavaScriptCore.md)
- [/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox](DYLIBS/MediaToolbox.md)
- [/System/Library/Frameworks/MessageUI.framework/MessageUI](DYLIBS/MessageUI.md)
- [/System/Library/Frameworks/Metal.framework/Metal](DYLIBS/Metal.md)
- [/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage](DYLIBS/NaturalLanguage.md)
- [/System/Library/Frameworks/Network.framework/Network](DYLIBS/Network.md)
- [/System/Library/Frameworks/PDFKit.framework/PDFKit](DYLIBS/PDFKit.md)
- [/System/Library/Frameworks/PencilKit.framework/PencilKit](DYLIBS/PencilKit.md)
- [/System/Library/Frameworks/Photos.framework/Photos](DYLIBS/Photos.md)
- [/System/Library/Frameworks/PhotosUI.framework/PhotosUI](DYLIBS/PhotosUI.md)
- [/System/Library/Frameworks/QuartzCore.framework/QuartzCore](DYLIBS/QuartzCore.md)
- [/System/Library/Frameworks/SafariServices.framework/SafariServices](DYLIBS/SafariServices.md)
- [/System/Library/Frameworks/Security.framework/Security](DYLIBS/Security.md)
- [/System/Library/Frameworks/StickerKit.framework/StickerKit](DYLIBS/StickerKit.md)
- [/System/Library/Frameworks/SwiftUI.framework/SwiftUI](DYLIBS/SwiftUI.md)
- [/System/Library/Frameworks/Translation.framework/Translation](DYLIBS/Translation.md)
- [/System/Library/Frameworks/UIKit.framework/UIKit](DYLIBS/UIKit.md)
- [/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox](DYLIBS/VideoToolbox.md)
- [/System/Library/Frameworks/WebKit.framework/WebKit](DYLIBS/WebKit.md)
- [/System/Library/Health/FeedItemPlugins/HighlightAlerts.healthplugin/HighlightAlerts](DYLIBS/HighlightAlerts.md)
- [/System/Library/Health/FeedItemPlugins/Highlights.healthplugin/Highlights](DYLIBS/Highlights.md)
- [/System/Library/Health/FeedItemPlugins/MenstrualCyclesAppPlugin.healthplugin/MenstrualCyclesAppPlugin](DYLIBS/MenstrualCyclesAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Profiles.healthplugin/Profiles](DYLIBS/Profiles.md)
- [/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety](DYLIBS/Safety.md)
- [/System/Library/Health/FeedItemPlugins/SleepHealthAppPlugin.healthplugin/SleepHealthAppPlugin](DYLIBS/SleepHealthAppPlugin.md)
- [/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries](DYLIBS/Summaries.md)
- [/System/Library/Health/FeedItemPlugins/VisionHealthAppPlugin.healthplugin/VisionHealthAppPlugin](DYLIBS/VisionHealthAppPlugin.md)
- [/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings](DYLIBS/BluetoothSettings.md)
- [/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation](DYLIBS/AAAFoundation.md)
- [/System/Library/PrivateFrameworks/AGXCompilerCore.framework/AGXCompilerCore](DYLIBS/AGXCompilerCore.md)
- [/System/Library/PrivateFrameworks/APFS.framework/APFS](DYLIBS/APFS.md)
- [/System/Library/PrivateFrameworks/AVConference.framework/AVConference](DYLIBS/AVConference.md)
- [/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore](DYLIBS/AVFCore.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristics.framework/ActionPredictionHeuristics](DYLIBS/ActionPredictionHeuristics.md)
- [/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal](DYLIBS/ActionPredictionHeuristicsInternal.md)
- [/System/Library/PrivateFrameworks/AdPlatformsCommon.framework/AdPlatformsCommon](DYLIBS/AdPlatformsCommon.md)
- [/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver](DYLIBS/AirPlayReceiver.md)
- [/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender](DYLIBS/AirPlaySender.md)
- [/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport](DYLIBS/AirPlaySupport.md)
- [/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient](DYLIBS/AppPredictionClient.md)
- [/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation](DYLIBS/AppPredictionFoundation.md)
- [/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal](DYLIBS/AppPredictionInternal.md)
- [/System/Library/PrivateFrameworks/AppPredictionUIFoundation.framework/AppPredictionUIFoundation](DYLIBS/AppPredictionUIFoundation.md)
- [/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents](DYLIBS/AppStoreComponents.md)
- [/System/Library/PrivateFrameworks/AppStoreKit.framework/AppStoreKit](DYLIBS/AppStoreKit.md)
- [/System/Library/PrivateFrameworks/AppleAccountTransparency.framework/AppleAccountTransparency](DYLIBS/AppleAccountTransparency.md)
- [/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup](DYLIBS/AppleIDSetup.md)
- [/System/Library/PrivateFrameworks/AppleIDSetupUI.framework/AppleIDSetupUI](DYLIBS/AppleIDSetupUI.md)
- [/System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/AppleIntelligenceReportingProcessing](DYLIBS/AppleIntelligenceReportingProcessing.md)
- [/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices](DYLIBS/AppleMediaServices.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal](DYLIBS/AppleMediaServicesKitInternal.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI](DYLIBS/AppleMediaServicesUI.md)
- [/System/Library/PrivateFrameworks/AppleMediaServicesUIKitInternal.framework/AppleMediaServicesUIKitInternal](DYLIBS/AppleMediaServicesUIKitInternal.md)
- [/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices](DYLIBS/AssistantServices.md)
- [/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession](DYLIBS/AudioSession.md)
- [/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore](DYLIBS/AudioToolboxCore.md)
- [/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit](DYLIBS/AuthKit.md)
- [/System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor](DYLIBS/BlastDoor.md)
- [/System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto](DYLIBS/CSExattrCrypto.md)
- [/System/Library/PrivateFrameworks/CTLazuliSupport.framework/CTLazuliSupport](DYLIBS/CTLazuliSupport.md)
- [/System/Library/PrivateFrameworks/CallsAppUI.framework/CallsAppUI](DYLIBS/CallsAppUI.md)
- [/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI](DYLIBS/CameraUI.md)
- [/System/Library/PrivateFrameworks/CentauriController.framework/CentauriController](DYLIBS/CentauriController.md)
- [/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit](DYLIBS/ChatKit.md)
- [/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore](DYLIBS/ChronoCore.md)
- [/System/Library/PrivateFrameworks/ChronoKit.framework/ChronoKit](DYLIBS/ChronoKit.md)
- [/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation](DYLIBS/CloudAttestation.md)
- [/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs](DYLIBS/CloudDocs.md)
- [/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon](DYLIBS/CloudKitDaemon.md)
- [/System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync](DYLIBS/CloudKitDistributedSync.md)
- [/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary](DYLIBS/CloudPhotoLibrary.md)
- [/System/Library/PrivateFrameworks/Coherence.framework/Coherence](DYLIBS/Coherence.md)
- [/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal](DYLIBS/CollectionsInternal.md)
- [/System/Library/PrivateFrameworks/CommunicationDetails.framework/CommunicationDetails](DYLIBS/CommunicationDetails.md)
- [/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI](DYLIBS/CommunicationsSetupUI.md)
- [/System/Library/PrivateFrameworks/CommunicationsUI.framework/CommunicationsUI](DYLIBS/CommunicationsUI.md)
- [/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync](DYLIBS/CompanionSync.md)
- [/System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore](DYLIBS/ContactsUICore.md)
- [/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP](DYLIBS/CoreCDP.md)
- [/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal](DYLIBS/CoreCDPInternal.md)
- [/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream](DYLIBS/CoreMediaStream.md)
- [/System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec](DYLIBS/CoreParsec.md)
- [/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition](DYLIBS/CoreRecognition.md)
- [/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet](DYLIBS/CoverSheet.md)
- [/System/Library/PrivateFrameworks/DashBoard.framework/DashBoard](DYLIBS/DashBoard.md)
- [/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess](DYLIBS/DeviceAccess.md)
- [/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation](DYLIBS/DigitalSeparation.md)
- [/System/Library/PrivateFrameworks/EAP8021X.framework/EAP8021X](DYLIBS/EAP8021X.md)
- [/System/Library/PrivateFrameworks/Email.framework/Email](DYLIBS/Email.md)
- [/System/Library/PrivateFrameworks/FTServices.framework/FTServices](DYLIBS/FTServices.md)
- [/System/Library/PrivateFrameworks/FaceTimeMessageStore.framework/FaceTimeMessageStore](DYLIBS/FaceTimeMessageStore.md)
- [/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation](DYLIBS/GameCenterFoundation.md)
- [/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore](DYLIBS/GameServicesCore.md)
- [/System/Library/PrivateFrameworks/GameStoreKit.framework/GameStoreKit](DYLIBS/GameStoreKit.md)
- [/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels](DYLIBS/GenerativeModels.md)
- [/System/Library/PrivateFrameworks/HeadphoneManager.framework/HeadphoneManager](DYLIBS/HeadphoneManager.md)
- [/System/Library/PrivateFrameworks/HeadphoneSettingsUI.framework/HeadphoneSettingsUI](DYLIBS/HeadphoneSettingsUI.md)
- [/System/Library/PrivateFrameworks/HealthMedicationsUI.framework/HealthMedicationsUI](DYLIBS/HealthMedicationsUI.md)
- [/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI](DYLIBS/HealthUI.md)
- [/System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization](DYLIBS/HealthVisualization.md)
- [/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities](DYLIBS/HearingUtilities.md)
- [/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon](DYLIBS/HeartHealthDaemon.md)
- [/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI](DYLIBS/HomeUI.md)
- [/System/Library/PrivateFrameworks/HomeWidgetIntents.framework/HomeWidgetIntents](DYLIBS/HomeWidgetIntents.md)
- [/System/Library/PrivateFrameworks/IDSBlastDoorSupport.framework/IDSBlastDoorSupport](DYLIBS/IDSBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation](DYLIBS/IDSFoundation.md)
- [/System/Library/PrivateFrameworks/IMCore.framework/IMCore](DYLIBS/IMCore.md)
- [/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence](DYLIBS/IMDPersistence.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities](DYLIBS/IMSharedUtilities.md)
- [/System/Library/PrivateFrameworks/IMTranscoderAgent.framework/IMTranscoderAgent](DYLIBS/IMTranscoderAgent.md)
- [/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib](DYLIBS/libIPTelephony.dylib.md)
- [/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore](DYLIBS/IntelligencePlatformCore.md)
- [/System/Library/PrivateFrameworks/MediaAnalysisBlastDoorSupport.framework/MediaAnalysisBlastDoorSupport](DYLIBS/MediaAnalysisBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI](DYLIBS/MediaCoreUI.md)
- [/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience](DYLIBS/MediaExperience.md)
- [/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore](DYLIBS/MediaPlaybackCore.md)
- [/System/Library/PrivateFrameworks/MedicalIDUI.framework/MedicalIDUI](DYLIBS/MedicalIDUI.md)
- [/System/Library/PrivateFrameworks/Message.framework/Message](DYLIBS/Message.md)
- [/System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport](DYLIBS/MessagesBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities](DYLIBS/MetadataUtilities.md)
- [/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools](DYLIBS/MetalTools.md)
- [/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit](DYLIBS/MigrationKit.md)
- [/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon](DYLIBS/MobileAssetDaemon.md)
- [/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI](DYLIBS/MobileMailUI.md)
- [/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari](DYLIBS/MobileSafari.md)
- [/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI](DYLIBS/MobileSafariUI.md)
- [/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport](DYLIBS/MultitouchSupport.md)
- [/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI](DYLIBS/MusicUI.md)
- [/System/Library/PrivateFrameworks/NDOAPI.framework/NDOAPI](DYLIBS/NDOAPI.md)
- [/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit](DYLIBS/NanoTimeKit.md)
- [/System/Library/PrivateFrameworks/NewsFeed.framework/NewsFeed](DYLIBS/NewsFeed.md)
- [/System/Library/PrivateFrameworks/NewsPersonalization.framework/NewsPersonalization](DYLIBS/NewsPersonalization.md)
- [/System/Library/PrivateFrameworks/NewsSubscription.framework/NewsSubscription](DYLIBS/NewsSubscription.md)
- [/System/Library/PrivateFrameworks/NewsUI2.framework/NewsUI2](DYLIBS/NewsUI2.md)
- [/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared](DYLIBS/NotesShared.md)
- [/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport](DYLIBS/NotesSupport.md)
- [/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility](DYLIBS/OSEligibility.md)
- [/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore](DYLIBS/PassKitCore.md)
- [/System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI](DYLIBS/PassKitUI.md)
- [/System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI](DYLIBS/PegasusAPI.md)
- [/System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration](DYLIBS/PegasusConfiguration.md)
- [/System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit](DYLIBS/PegasusKit.md)
- [/System/Library/PrivateFrameworks/PegasusPersistence.framework/PegasusPersistence](DYLIBS/PegasusPersistence.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices](DYLIBS/PhotoLibraryServices.md)
- [/System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore](DYLIBS/PhotoLibraryServicesCore.md)
- [/System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore](DYLIBS/PhotosUICore.md)
- [/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate](DYLIBS/PhotosUIPrivate.md)
- [/System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation](DYLIBS/PodcastsFoundation.md)
- [/System/Library/PrivateFrameworks/PodcastsUI.framework/PodcastsUI](DYLIBS/PodcastsUI.md)
- [/System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit](DYLIBS/PosterFuturesKit.md)
- [/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit](DYLIBS/PosterKit.md)
- [/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI](DYLIBS/PowerUI.md)
- [/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore](DYLIBS/PowerlogCore.md)
- [/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators](DYLIBS/PowerlogFullOperators.md)
- [/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators](DYLIBS/PowerlogLiteOperators.md)
- [/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction](DYLIBS/PromotedContentPrediction.md)
- [/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI](DYLIBS/PromotedContentUI.md)
- [/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage](DYLIBS/ProtectedCloudStorage.md)
- [/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal](DYLIBS/ReflectionInternal.md)
- [/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal](DYLIBS/RuntimeInternal.md)
- [/System/Library/PrivateFrameworks/Search.framework/Search](DYLIBS/Search.md)
- [/System/Library/PrivateFrameworks/SearchAssets.framework/SearchAssets](DYLIBS/SearchAssets.md)
- [/System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics](DYLIBS/SearchOnDeviceAnalytics.md)
- [/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI](DYLIBS/SearchUI.md)
- [/System/Library/PrivateFrameworks/SecureMessaging.framework/SecureMessaging](DYLIBS/SecureMessaging.md)
- [/System/Library/PrivateFrameworks/SecureMessagingAgentCore.framework/SecureMessagingAgentCore](DYLIBS/SecureMessagingAgentCore.md)
- [/System/Library/PrivateFrameworks/SessionAlert.framework/SessionAlert](DYLIBS/SessionAlert.md)
- [/System/Library/PrivateFrameworks/SessionCore.framework/SessionCore](DYLIBS/SessionCore.md)
- [/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation](DYLIBS/SettingsFoundation.md)
- [/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI](DYLIBS/SiriSharedUI.md)
- [/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon](DYLIBS/SleepHealthDaemon.md)
- [/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile](DYLIBS/SoftwareUpdateUIMobile.md)
- [/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon](DYLIBS/SpotlightDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics](DYLIBS/SpotlightDiagnostics.md)
- [/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation](DYLIBS/SpotlightFoundation.md)
- [/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex](DYLIBS/SpotlightIndex.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge](DYLIBS/SpotlightKnowledge.md)
- [/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon](DYLIBS/SpotlightKnowledgeDaemon.md)
- [/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver](DYLIBS/SpotlightReceiver.md)
- [/System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation](DYLIBS/SpotlightRecommendation.md)
- [/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources](DYLIBS/SpotlightResources.md)
- [/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices](DYLIBS/SpotlightServices.md)
- [/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard](DYLIBS/SpringBoard.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices](DYLIBS/SpringBoardUIServices.md)
- [/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS](DYLIBS/SwiftMLS.md)
- [/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore](DYLIBS/TVRemoteCore.md)
- [/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI](DYLIBS/TVRemoteUI.md)
- [/System/Library/PrivateFrameworks/TelephonyBlastDoorSupport.framework/TelephonyBlastDoorSupport](DYLIBS/TelephonyBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences](DYLIBS/TelephonyPreferences.md)
- [/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities](DYLIBS/TelephonyUtilities.md)
- [/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer](DYLIBS/TextComposer.md)
- [/System/Library/PrivateFrameworks/TextFormattingUI.framework/TextFormattingUI](DYLIBS/TextFormattingUI.md)
- [/System/Library/PrivateFrameworks/TextInput.framework/TextInput](DYLIBS/TextInput.md)
- [/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI](DYLIBS/TextInputUI.md)
- [/System/Library/PrivateFrameworks/ThumbnailsBlastDoorSupport.framework/ThumbnailsBlastDoorSupport](DYLIBS/ThumbnailsBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon](DYLIBS/TipsDaemon.md)
- [/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon](DYLIBS/TranslationDaemon.md)
- [/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore](DYLIBS/UIKitCore.md)
- [/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices](DYLIBS/UIKitServices.md)
- [/System/Library/PrivateFrameworks/UnifiedMessagingKit.framework/UnifiedMessagingKit](DYLIBS/UnifiedMessagingKit.md)
- [/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib](DYLIBS/livefiles_apfs.dylib.md)
- [/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore](DYLIBS/UserNotificationsCore.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer](DYLIBS/UserNotificationsServer.md)
- [/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices](DYLIBS/UserNotificationsServices.md)
- [/System/Library/PrivateFrameworks/VideosUI.framework/VideosUI](DYLIBS/VideosUI.md)
- [/System/Library/PrivateFrameworks/VisualActionPredictionCore.framework/VisualActionPredictionCore](DYLIBS/VisualActionPredictionCore.md)
- [/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient](DYLIBS/VoiceShortcutClient.md)
- [/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts](DYLIBS/VoiceShortcuts.md)
- [/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon](DYLIBS/WPDaemon.md)
- [/System/Library/PrivateFrameworks/WalletBlastDoorSupport.framework/WalletBlastDoorSupport](DYLIBS/WalletBlastDoorSupport.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib](DYLIBS/libANGLE-shared.dylib.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy](DYLIBS/WebKitLegacy.md)
- [/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit](DYLIBS/WiFiKit.md)
- [/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit](DYLIBS/WorkflowKit.md)
- [/System/Library/PrivateFrameworks/WorkflowUI.framework/WorkflowUI](DYLIBS/WorkflowUI.md)
- [/System/Library/PrivateFrameworks/WorkoutCore.framework/WorkoutCore](DYLIBS/WorkoutCore.md)
- [/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore](DYLIBS/iCloudDriveCore.md)
- [/System/Library/PrivateFrameworks/iCloudWebData.framework/iCloudWebData](DYLIBS/iCloudWebData.md)
- [/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics](DYLIBS/iOSDiagnostics.md)
- [/System/Library/TextInput/TextInput_cs.bundle/TextInput_cs](DYLIBS/TextInput_cs.md)
- [/System/Library/TextInput/TextInput_sk.bundle/TextInput_sk](DYLIBS/TextInput_sk.md)
- [/usr/lib/dyld](DYLIBS/dyld.md)
- [/usr/lib/libauthinstall.dylib](DYLIBS/libauthinstall.dylib.md)
- [/usr/lib/libswiftPrespecialized.dylib](DYLIBS/libswiftPrespecialized.dylib.md)
- [/usr/lib/swift/libswiftUIKit.dylib](DYLIBS/libswiftUIKit.dylib.md)
- [/usr/lib/system/libcorecrypto.dylib](DYLIBS/libcorecrypto.dylib.md)
- [/usr/lib/system/libcorecrypto_noasm.dylib](DYLIBS/libcorecrypto_noasm.dylib.md)
- [/usr/lib/system/libcorecrypto_trace.dylib](DYLIBS/libcorecrypto_trace.dylib.md)
- [/usr/lib/system/libdyld.dylib](DYLIBS/libdyld.dylib.md)
- [/usr/lib/system/libsystem_dnssd.dylib](DYLIBS/libsystem_dnssd.dylib.md)
- [/usr/lib/system/libsystem_eligibility.dylib](DYLIBS/libsystem_eligibility.dylib.md)
- [/usr/lib/system/libsystem_kernel.dylib](DYLIBS/libsystem_kernel.dylib.md)
- [/usr/lib/updaters/libVinylUpdater.dylib](DYLIBS/libVinylUpdater.dylib.md)
- [/usr/lib/usd/libusd_ms.dylib](DYLIBS/libusd_ms.dylib.md)

</details>

## Files

### 🆕 New

#### filesystem (57)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/PrivateFrameworks/ChronoCore.framework/Localizable.loctable`
- `/System/Library/PrivateFrameworks/GameStoreKit.framework/ChicletVFX_AllPlacements_V6.vfx/assets/script.js`
- `/System/Library/UserNotifications/Bundles/com.apple.icloudwebd.bundle/Localizable.loctable`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/119f15b8ec5040d6a0f0b6bbc32f5036.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/674d6e82b6ef395e0b1ef8a7f42b53e2.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/28b6b5fe865e83d71004920bf59a96c1.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/abaa3eaeb9c2c83507aa72808cbc5ac9.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/c346abb47f39bdf5ea74c783db797c56.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/ca4b7fc3cb8942fe7cf706a5d8d725fa.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/4ee37489e3dc6e1495e47f92922bc474.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/47ed763d4da852053d3e0df403a32a15.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/e5ef47b714388efe15152efd0470d448.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/5c3a49cf0895c034c54be0b2934c516f.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/6bbf19e88f32263e9312eddb48411583.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/816af27423827af6c4b139fb9dc9934c.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/4674653c311ed103b62d1fb2c5cb47a2.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/f3fff939a8ea74c791518394e0ee8d47.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/3f4b911a5f15b5dee8fef84bb57f5765.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/d90ba7b3643280c39a0ef43dea75c243.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/6d599761a63725c06e50b113ffe89d45.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/4c913fe73b4302a65f8117aeda254b57.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/138ae3944360cf092d85ea0d4b1845b3.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/65a12114e41d4102b645f601cb41801f.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/ee72c4cad7f169364ca30afa7d1709e5.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/1aaa69a8d25940d633bf54a74616b43f.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/ade35c6dda359d3a30200572cdc6fc44.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/314da147ebfddde4b88b39e289cd1e9d.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/d5d2787c3a84a262b0a277da3cc8db59.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/46bc602cd95d6422a51cf178627114a3.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/f4e180cf08e15ab62b40c3251b632014.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/106a4997ced9ee975584f34b4ce5c645.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/a984c8f1520cb1d0d82a066b3533dcb7.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/dbf6be933bcf5665a9d975ff071e8f4b.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/eb87051541ba0bb4b907b5e8e3b825b2.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/69017177c45949dc449294a7c30c89f3.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/27c95577d32070c96de13deb24413994.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/54563cdd1d70f77d61cd8a27b7b52f40.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/8872a5da903f0a5ecc6d2a8008048a3a.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/0fb81a6558c785eeb8585807f596fa59.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/50945890aef7aaad97a83c5c13165e06.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/06cf9f84e81731ec98071094304d3805.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/b39a62b5afa9fa54a9acacab907c8916.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/f66f61897cf8cf662dfbdba21e7ee44c.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/c3b916396d857413d9ee273cc6c8e8e6.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/8f8d6c818f472f4eb5f33fb1be5da975.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/cbd0adb5d57d33a33e848f0a47d111bb.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/a7a39369cfe19c6eb11e82db9e542c5b.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/dc9ff4f6ec87c7366e35c1db5196be45.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/8119c8109e96bd28eff912624a0a116d.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/31a3e0939fcd5a5f3d4087e4bda2fe71.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/6cf585ca4df73c84a2cfe4da25deca37.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/a845a21c25a58174ea6fbb39435de759.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/b6f722ce771f33e8b076df87590b0445.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/85a0540beafe5adea1896c3975f76a9a.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/2420725c6a61086c83bb2ff2d13e431b.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Base.lproj/nlu.appintents/fe200a7bea670fc523de9e407efda68c.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/26c57d3b7dce55efc469fcdf238b389e.version`

</details>

### ❌ Removed

#### filesystem (63)

<details>
  <summary><i>View Files</i></summary>

- `/System/Library/PreferenceBundles/SMSPreferences.bundle/SMSPreferences-Entitlements.plist`
- `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/ca.lproj/IDSLocalizable.stringsdict`
- `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/es.lproj/IdentityServicesLocalizable.stringsdict`
- `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/hr.lproj/IDSLocalizable.stringsdict`
- `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/hr.lproj/IdentityServicesLocalizable.stringsdict`
- `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/pl.lproj/IDSFirewallLocalizable.stringsdict`
- `/System/Library/PrivateFrameworks/MigrationKit.framework/InternalDefaults.md`
- `/System/Library/PrivateFrameworks/iCloudWebSupport.framework/Localizable.loctable`
- `/System/Library/UserNotifications/Bundles/com.apple.icloudwebd.bundle/Localizable.strings`
- `/private/var/staged_system_apps/Tips.app/ar.lproj/nlu.appintents/632a304f58a5a9911d13dba2d167c413.version`
- `/private/var/staged_system_apps/Tips.app/bg.lproj/nlu.appintents/396208498e6c2e0180b79e46defb36f8.version`
- `/private/var/staged_system_apps/Tips.app/bn.lproj/nlu.appintents/ca90789f47a0a94c872905282023b573.version`
- `/private/var/staged_system_apps/Tips.app/ca.lproj/nlu.appintents/0af1a87dc525e55ce44cbddd5838a665.version`
- `/private/var/staged_system_apps/Tips.app/cs.lproj/nlu.appintents/ee184378eabc3a2dbbf913089ed818de.version`
- `/private/var/staged_system_apps/Tips.app/da.lproj/nlu.appintents/ec1415baa0db37ec6a9a4d390088ccf6.version`
- `/private/var/staged_system_apps/Tips.app/de.lproj/nlu.appintents/807fffb63d199139e2c8157b31ec324b.version`
- `/private/var/staged_system_apps/Tips.app/el.lproj/nlu.appintents/3b1b489deb0c4cc6983fb6c9a805a066.version`
- `/private/var/staged_system_apps/Tips.app/en.lproj/nlu.appintents/c78ad7d690e48d1eba1c0c4331f4d6a2.version`
- `/private/var/staged_system_apps/Tips.app/en_AU.lproj/nlu.appintents/7245265b47c04b8b272e6408e7ea2c94.version`
- `/private/var/staged_system_apps/Tips.app/en_GB.lproj/nlu.appintents/9ef50a25faf349ea7728ce137a19d6db.version`
- `/private/var/staged_system_apps/Tips.app/es.lproj/nlu.appintents/489bdb8c77376b31aaf271c6db868c15.version`
- `/private/var/staged_system_apps/Tips.app/es_419.lproj/nlu.appintents/25369dd72fb2d4a45178a4520f9e9f57.version`
- `/private/var/staged_system_apps/Tips.app/es_US.lproj/nlu.appintents/05720895bd313120c595bb5b940e3dce.version`
- `/private/var/staged_system_apps/Tips.app/fi.lproj/nlu.appintents/aabcdf595e307e480fc2fbe94ec43658.version`
- `/private/var/staged_system_apps/Tips.app/fr.lproj/nlu.appintents/0e996d440f26289494ba56451b67120f.version`
- `/private/var/staged_system_apps/Tips.app/fr_CA.lproj/nlu.appintents/edcdb97b8a8aa63791f20de207392d46.version`
- `/private/var/staged_system_apps/Tips.app/gu.lproj/nlu.appintents/09e1ed8dcf99fab68b5639661816f5bd.version`
- `/private/var/staged_system_apps/Tips.app/he.lproj/nlu.appintents/2a978b4bfddbe3381b6542841b9baa9f.version`
- `/private/var/staged_system_apps/Tips.app/hi.lproj/nlu.appintents/70eb17113de25342793c6e2b64a3e254.version`
- `/private/var/staged_system_apps/Tips.app/hr.lproj/nlu.appintents/67e02da7c6a5f6f96efb5030102101cb.version`
- `/private/var/staged_system_apps/Tips.app/hu.lproj/nlu.appintents/de66dc8c388c8464452a1a57a577573b.version`
- `/private/var/staged_system_apps/Tips.app/id.lproj/nlu.appintents/a2c23053d55e5d07032b5d70d7941f18.version`
- `/private/var/staged_system_apps/Tips.app/it.lproj/nlu.appintents/9af94a96d93904c13be7f514b6ac3ce7.version`
- `/private/var/staged_system_apps/Tips.app/ja.lproj/nlu.appintents/ef7803fd8217a0a6ea263bba5820568b.version`
- `/private/var/staged_system_apps/Tips.app/kk.lproj/nlu.appintents/8aa8f897943a86d9add4106f9d0ad273.version`
- `/private/var/staged_system_apps/Tips.app/kn.lproj/nlu.appintents/ff443aa6a4bcf57438b659e3497d49a0.version`
- `/private/var/staged_system_apps/Tips.app/ko.lproj/nlu.appintents/ae0f13b34ab8a7d3d6b028b00ab7048c.version`
- `/private/var/staged_system_apps/Tips.app/lt.lproj/nlu.appintents/c86e02dcab9da8e528b62631263b814d.version`
- `/private/var/staged_system_apps/Tips.app/ml.lproj/nlu.appintents/4b9c95ce99b37eb1fc13eaaa656ce44f.version`
- `/private/var/staged_system_apps/Tips.app/mr.lproj/nlu.appintents/7fbef2f35655660f19748bc36938eae5.version`
- `/private/var/staged_system_apps/Tips.app/ms.lproj/nlu.appintents/453e9997265e8bf85ec6b2c49905e7c5.version`
- `/private/var/staged_system_apps/Tips.app/nl.lproj/nlu.appintents/d07dc8f55e846a87b09f2a3dcad95ce5.version`
- `/private/var/staged_system_apps/Tips.app/no.lproj/nlu.appintents/9dcb6f8afdf823c866a06c1b93bf0050.version`
- `/private/var/staged_system_apps/Tips.app/or.lproj/nlu.appintents/7089e1b750e39849c8b3fb881ec4add5.version`
- `/private/var/staged_system_apps/Tips.app/pa.lproj/nlu.appintents/fb95e400dd3ecb9fe42fbcb3c7684168.version`
- `/private/var/staged_system_apps/Tips.app/pl.lproj/nlu.appintents/b85bfb5c40146ed1aa2de078e78005ce.version`
- `/private/var/staged_system_apps/Tips.app/pt_BR.lproj/nlu.appintents/01252493a62d9f6c94990ba692c5d617.version`
- `/private/var/staged_system_apps/Tips.app/ro.lproj/nlu.appintents/65eba4a2f95728ec1bc168972fb5ed01.version`
- `/private/var/staged_system_apps/Tips.app/ru.lproj/nlu.appintents/64903cde02327e8f650380ba5925951e.version`
- `/private/var/staged_system_apps/Tips.app/sk.lproj/nlu.appintents/6e50be38499d39239218870432a4630d.version`
- `/private/var/staged_system_apps/Tips.app/sl.lproj/nlu.appintents/fa3f86f050591aa1891d7a0235031a60.version`
- `/private/var/staged_system_apps/Tips.app/sv.lproj/nlu.appintents/bea6078a2f8976ccd6c55e67cec76a6b.version`
- `/private/var/staged_system_apps/Tips.app/ta.lproj/nlu.appintents/677c56c1d309994b0162aa5dc5e77576.version`
- `/private/var/staged_system_apps/Tips.app/th.lproj/nlu.appintents/dad7cf04d0798ff79273c84a0676565b.version`
- `/private/var/staged_system_apps/Tips.app/tr.lproj/nlu.appintents/c32f8387ddecafbd5d309dfd56e89e5a.version`
- `/private/var/staged_system_apps/Tips.app/uk.lproj/nlu.appintents/5fff46e04788902c24fbec12ae99cc2d.version`
- `/private/var/staged_system_apps/Tips.app/ur.lproj/nlu.appintents/4e39ac90ac42977d8fc368f658760790.version`
- `/private/var/staged_system_apps/Tips.app/vi.lproj/nlu.appintents/238273abfe2306ebf4ca21ee4a608f28.version`
- `/private/var/staged_system_apps/Tips.app/zh_CN.lproj/nlu.appintents/4454d5d4cb34dec1d5791c7890c49bb2.version`
- `/private/var/staged_system_apps/Tips.app/zh_HK.lproj/nlu.appintents/6d0d842d4d69fcac27de17a09fb7493e.version`
- `/private/var/staged_system_apps/Tips.app/zh_TW.lproj/nlu.appintents/6441b9ab23004fac50bb3c720e61c6fe.version`
- `/private/var/staged_system_apps/VoiceMemos.app/Base.lproj/nlu.appintents/6148a4bd03a935c4f3f6c0e92f5e6c9f.version`
- `/private/var/staged_system_apps/VoiceMemos.app/en.lproj/nlu.appintents/dd1fe5d7daca517a2cce21b646b2474a.version`

</details>

## Feature Flags

### ⬆️ Updated (2)

<details>
  <summary><i>View Updated</i></summary>

#### CoreTelephony.plist

>  `Domain/CoreTelephony.plist`

```diff

 		<key>DisclosureRequired</key>
 		<string>2d56a039-da9d-9afc-c249-0e18d5492708</string>
 	</dict>
+	<key>RCSCompression</key>
+	<dict>
+		<key>DevelopmentPhase</key>
+		<string>FeatureComplete</string>
+	</dict>
 	<key>RCSPush</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```

#### Siri.plist

>  `Domain/Siri.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>dictation_secure_touch</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
 	<key>dictation_user_edit_classification</key>
 	<dict>
 		<key>DevelopmentPhase</key>

```


</details>

## EOF
