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
Functions:
~ sub_fffffff008b34298 : 124 -> 136

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
 
Functions:
~ __ZN7AVE_HwC18ProcessIntr_CmdAckEmi : 808 -> 1048
~ __ZN7AVE_HwC15ProcessIntr_CmdEmij : 6516 -> 6476
~ sub_fffffff008cd722c -> sub_fffffff008cd7304 : 52 -> 44
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
Functions:
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

## EOF
