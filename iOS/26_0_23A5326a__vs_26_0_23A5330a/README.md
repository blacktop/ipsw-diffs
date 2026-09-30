# 26.0 (23A5326a) .vs 26.0 (23A5330a)

## IPSWs

- `iPhone17,1_26.0_23A5326a_Restore.ipsw`
- `iPhone17,1_26.0_23A5330a_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.0 *(23A5326a)* | 25.0.0 | 12377.2.7~9 | Fri, 15Aug2025 00:02:28 PDT |
| 26.0 *(23A5330a)* | 25.0.0 | 12377.2.7~9 | Fri, 15Aug2025 00:02:28 PDT |

## MachO

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### InCallService

>  `/Applications/InCallService.app/InCallService`

```diff

-3025.100.1.2.22
-  __TEXT.__text: 0x24f20c
+3025.100.1.2.24
+  __TEXT.__text: 0x24f39c
   __TEXT.__auth_stubs: 0x6370
   __TEXT.__objc_stubs: 0x28340
   __TEXT.__objc_methlist: 0x182f8

   __TEXT.__swift_as_ret: 0x22c
   __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x92f8
+  __TEXT.__unwind_info: 0x9300
   __TEXT.__eh_frame: 0x71b0
   __DATA_CONST.__auth_got: 0x31c8
   __DATA_CONST.__got: 0x2100

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3B1FDADD-A160-3F53-A68A-1D32AAD21C0F
-  Functions: 14422
+  UUID: A9D886CA-9BB1-3C99-9FF3-64390AB6C55E
+  Functions: 14425
   Symbols:   3171
   CStrings:  15262
 

```

#### VirtualAudio

>  `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.124.34.0.0
-  __TEXT.__text: 0x5054e0
+1364.124.35.0.0
+  __TEXT.__text: 0x504e64
   __TEXT.__auth_stubs: 0x26f0
   __TEXT.__objc_stubs: 0x9e0
   __TEXT.__init_offsets: 0x4dc
   __TEXT.__objc_methlist: 0x124
   __TEXT.__const: 0xb0b12
-  __TEXT.__gcc_except_tab: 0x5dbf4
-  __TEXT.__cstring: 0x287a1
+  __TEXT.__gcc_except_tab: 0x5dc00
+  __TEXT.__cstring: 0x2878f
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x178

   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x11348
+  __TEXT.__unwind_info: 0x11330
   __TEXT.__eh_frame: 0x7a0
   __DATA_CONST.__auth_got: 0x1390
   __DATA_CONST.__got: 0x4d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FE1199AA-4D0F-3B52-9C48-2A1A4ED18A3B
-  Functions: 11496
+  UUID: EA57F43D-C983-3288-80BB-D45D28152B5B
+  Functions: 11493
   Symbols:   773
-  CStrings:  11286
+  CStrings:  11285
 
CStrings:
+ "@@ Strips Aug 20 2025 21:03:40"
- "@@ Strips Aug 12 2025 22:59:21"
- "PortManager mutex"

```

#### archive.metallib

>  `/System/Library/PrivateFrameworks/RenderBox.framework/archive.metallib`

```diff

   __TEXT.__descriptor: 0x1140
   __TEXT.__fragment: 0xa6ea0
   __TEXT.__visible: 0x19e0
-  __TEXT.__vertex: 0xb7a0
+  __TEXT.__vertex: 0xbf70
   __TEXT.__reflection: 0x12240
-  UUID: CB369D29-7629-3529-93E8-22B968D2FBB8
+  UUID: 23F6700E-9920-3DFF-B9B5-B281043E454B
   Functions: 0
   Symbols:   0
   CStrings:  0

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A5326a)* | iBoot-13822.2.12 |
| 26.0 *(23A5330a)* | iBoot-13822.2.13 |

#### 🆕 NEW (1)

<details>
  <summary><i>View NEW</i></summary>

##### `iboot`
  - `iBoot-13822.2.13`

</details>

#### ❌ Removed (1)

<details>
  <summary><i>View Removed</i></summary>

##### `iboot`
  - `iBoot-13822.2.12`

</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A5326a)* | 622.1.22.10.8 |
| 26.0 *(23A5330a)* | 622.1.22.10.8 |

### Dylibs

#### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### ConversationKit

>  `/System/Library/PrivateFrameworks/ConversationKit.framework/ConversationKit`

```diff

-574.100.1.2.5
-  __TEXT.__text: 0x81f240
-  __TEXT.__auth_stubs: 0xa590
+574.100.1.2.9
+  __TEXT.__text: 0x81f258
+  __TEXT.__auth_stubs: 0xa5a0
   __TEXT.__objc_methlist: 0xa200
   __TEXT.__const: 0x34c84
   __TEXT.__cstring: 0x36410

   __TEXT.__swift5_types: 0x14b8
   __TEXT.__swift_as_entry: 0x628
   __TEXT.__swift_as_ret: 0x534
-  __TEXT.__unwind_info: 0x1f898
+  __TEXT.__unwind_info: 0x1f8a0
   __TEXT.__eh_frame: 0x18d80
   __TEXT.__objc_classname: 0xf28
   __TEXT.__objc_methname: 0x1881f

   __DATA_CONST.__objc_selrefs: 0x6fa0
   __DATA_CONST.__objc_protorefs: 0x3d8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x52d0
+  __AUTH_CONST.__auth_got: 0x52d8
   __AUTH_CONST.__const: 0x334f0
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x286f0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7ABFC3E3-C531-3BCC-982C-038C188D5F8E
-  Functions: 59548
-  Symbols:   158385
+  UUID: B796F1F0-6234-3C62-A9E0-CB7955DC2433
+  Functions: 59550
+  Symbols:   158388
   CStrings:  11663
 
Symbols:
+ _$s7SwiftUI19UIHostingControllerC15safeAreaRegionsAA04SafefG0VvM
+ _$ss9OptionSetPs7ElementQzRszrlE6removeyxSgxF15ConversationKit27PeoplePickerRecipientsState33_7F96793E744B7F0A87FC1CE2B39EA70BLLV_Tg5
Functions:
~ sub_1bb086d74 : 44 -> 36
+ sub_1bb086d98
- sub_1bb0b3298
~ _$s15ConversationKit26ButtonsStackViewControllerC23isFrontFacingOrExternal17updateVideoLayersACSbSo15AVCaptureDeviceCc_ySo0oP8PositionVctcfc : 424 -> 488
+ _$ss9OptionSetPs7ElementQzRszrlE6removeyxSgxFSo30UIFontDescriptorSymbolicTraitsV_Tgq5
+ _$s15ConversationKit21ButtonsStackViewModelC7buttonsSayAC16LocalVideoButtonCGvi
+ _$s15ConversationKit26ScreenSharingContentLayoutV7SwiftUI0F0AadEP16layoutPropertiesAD0fJ0VvgZTW
+ _$s15ConversationKit26ScreenSharingContentLayoutV7SwiftUI0F0AadEP05_makeF4View4root6inputs4bodyAD01_J7OutputsVAD11_GraphValueVyxG_AD01_J6InputsVAD01_j4ListN0VAD01_O0V_AQtXEtFZTW
+ _$s15ConversationKit26ScreenSharingContentLayoutV7SwiftUI10AnimatableAadEP05_makeI05value6inputsyAD11_GraphValueVyxGz_AD01_M6InputsVtFZTW
- _$ss9OptionSetPs7ElementQzRszrlE6removeyxSgxFSo30UIFontDescriptorSymbolicTraitsV_Tgq5
- _$s15ConversationKit27PeoplePickerRecipientsState33_7F96793E744B7F0A87FC1CE2B39EA70BLLVs10SetAlgebraAAsAEP6update4with7ElementQzSgAJn_tFTW
- _$ss10SetAlgebraPs7ElementQz012ArrayLiteralC0RtzrlE05arrayE0xAFd_tcfCSo36TUConversationBroadcastingAttributesV_Tgq5

```

#### MigrationKit

>  `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-829.2.2.0.0
-  __TEXT.__text: 0x4b06fc
-  __TEXT.__auth_stubs: 0x5520
+829.2.4.0.0
+  __TEXT.__text: 0x4b0738
+  __TEXT.__auth_stubs: 0x5530
   __TEXT.__objc_methlist: 0x6b40
   __TEXT.__const: 0x290e8
   __TEXT.__cstring: 0x1bf07
-  __TEXT.__oslogstring: 0xc532
+  __TEXT.__oslogstring: 0xc562
   __TEXT.__gcc_except_tab: 0x1404
   __TEXT.__swift5_typeref: 0x9970
   __TEXT.__swift5_fieldmd: 0xb950

   __TEXT.__swift_as_entry: 0xefc
   __TEXT.__swift_as_ret: 0x11d0
   __TEXT.__swift5_mpenum: 0xac
-  __TEXT.__unwind_info: 0x117e8
+  __TEXT.__unwind_info: 0x117f0
   __TEXT.__eh_frame: 0x2e1ec
   __TEXT.__objc_classname: 0xdfc
   __TEXT.__objc_methname: 0xfe2c
   __TEXT.__objc_methtype: 0x3639
-  __TEXT.__objc_stubs: 0x97a0
+  __TEXT.__objc_stubs: 0x9780
   __DATA_CONST.__got: 0x1898
-  __DATA_CONST.__const: 0x9d0
+  __DATA_CONST.__const: 0x9a8
   __DATA_CONST.__objc_classlist: 0xb78
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x268

   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x488
-  __AUTH_CONST.__auth_got: 0x2aa8
+  __AUTH_CONST.__auth_got: 0x2ab0
   __AUTH_CONST.__const: 0x12ea8
   __AUTH_CONST.__cfstring: 0x5100
   __AUTH_CONST.__objc_const: 0x19a98

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B895DDA2-201B-323C-B60A-BA90D4994009
-  Functions: 19106
-  Symbols:   13521
-  CStrings:  9053
+  UUID: 9D3FFBD1-D1AA-33DD-81E9-CA0459276FBA
+  Functions: 19105
+  Symbols:   13518
+  CStrings:  9054
 
Symbols:
+ _IMDSMSRecordStoreGetSchemaVersion
- ___27-[MKMessageMigrator import]_block_invoke
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$importWithCompletion:
Functions:
~ -[MKMessageMigrator open] : 180 -> 344
~ -[MKMessageMigrator close] : 156 -> 164
~ -[MKMessageMigrator import] : 124 -> 72
- ___27-[MKMessageMigrator import]_block_invoke
CStrings:
+ "fetched the current sms.db version. version=%ld"

```

#### PhotosUIPrivate

>  `/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate`

```diff

-802.43.240.0.0
-  __TEXT.__text: 0x59dd90
-  __TEXT.__auth_stubs: 0x9da0
-  __TEXT.__objc_methlist: 0x5530c
+802.43.252.0.0
+  __TEXT.__text: 0x59de38
+  __TEXT.__auth_stubs: 0x9db0
+  __TEXT.__objc_methlist: 0x5531c
   __TEXT.__const: 0x15098
   __TEXT.__dlopen_cstrs: 0x6ff
-  __TEXT.__cstring: 0x40c06
+  __TEXT.__cstring: 0x40bee
   __TEXT.__swift5_typeref: 0x13f28
   __TEXT.__swift5_capture: 0x34d8
   __TEXT.__constg_swiftt: 0xa40c

   __TEXT.__swift_as_ret: 0x214
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x9998
+  __TEXT.__gcc_except_tab: 0x99b4
   __TEXT.__ustring: 0x1c0
   __TEXT.__unwind_info: 0x17a90
   __TEXT.__eh_frame: 0x5bdc
   __TEXT.__objc_classname: 0xa972
-  __TEXT.__objc_methname: 0xf53be
+  __TEXT.__objc_methname: 0xf5407
   __TEXT.__objc_methtype: 0x2146c
-  __TEXT.__objc_stubs: 0x92b40
-  __DATA_CONST.__got: 0x5630
+  __TEXT.__objc_stubs: 0x92ba0
+  __DATA_CONST.__got: 0x5638
   __DATA_CONST.__const: 0xd970
   __DATA_CONST.__objc_classlist: 0x1f40
   __DATA_CONST.__objc_catlist: 0x1e0
   __DATA_CONST.__objc_catlist2: 0x10
   __DATA_CONST.__objc_protolist: 0x13d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2cd98
+  __DATA_CONST.__objc_selrefs: 0x2cdb0
   __DATA_CONST.__objc_protorefs: 0x480
   __DATA_CONST.__objc_superrefs: 0x1318
   __DATA_CONST.__vfx_script_tbl: 0x10
   __DATA_CONST.__objc_arraydata: 0x14f0
-  __AUTH_CONST.__auth_got: 0x4ee0
-  __AUTH_CONST.__const: 0x13b60
+  __AUTH_CONST.__auth_got: 0x4ee8
+  __AUTH_CONST.__const: 0x13b40
   __AUTH_CONST.__cfstring: 0x292a0
   __AUTH_CONST.__objc_const: 0x8dd98
   __AUTH_CONST.__objc_arrayobj: 0xd80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C96AA193-4229-3981-8760-2F84BBB990C7
-  Functions: 40767
-  Symbols:   103946
-  CStrings:  52750
+  UUID: 48B3B3CA-962B-38A6-B15F-BE9D84327650
+  Functions: 40768
+  Symbols:   103953
+  CStrings:  52753
 
Symbols:
+ -[PUWhatsNewWelcomeViewController _presentPrivacyOverview]
+ GCC_except_table26571
+ GCC_except_table26680
+ GCC_except_table26749
+ GCC_except_table26759
+ GCC_except_table26763
+ GCC_except_table26909
+ GCC_except_table27005
+ _OBJC_CLASS_$_OBPrivacyPresenter
+ _PLIsChinaSKU
+ ___Block_byref_object_copy_.97213
+ ___Block_byref_object_copy_.98391
+ ___Block_byref_object_dispose_.97214
+ ___Block_byref_object_dispose_.98392
+ ___block_literal_global.13.98396
+ ___block_literal_global.17.98394
+ ___block_literal_global.95999
+ ___block_literal_global.96504
+ ___block_literal_global.97204
+ ___block_literal_global.97459
+ ___block_literal_global.97475
+ ___block_literal_global.97890
+ ___block_literal_global.97939
+ ___block_literal_global.98244
+ ___block_literal_global.98398
+ ___block_literal_global.98423
+ ___block_literal_global.98500
+ ___block_literal_global.99001
+ ___block_literal_global.99099
+ _objc_msgSend$_presentPrivacyOverview
+ _objc_msgSend$present
+ _objc_msgSend$presenterForPrivacySplashWithIdentifier:
+ _sharedInstance.onceToken.95998
+ _sharedInstance.sharedInstance.96000
- GCC_except_table26679
- GCC_except_table26748
- GCC_except_table26758
- GCC_except_table26762
- GCC_except_table26908
- GCC_except_table27004
- ___Block_byref_object_copy_.97216
- ___Block_byref_object_copy_.98394
- ___Block_byref_object_dispose_.97217
- ___Block_byref_object_dispose_.98395
- ___block_literal_global.13.98399
- ___block_literal_global.17.98397
- ___block_literal_global.95868
- ___block_literal_global.96002
- ___block_literal_global.96507
- ___block_literal_global.97207
- ___block_literal_global.97462
- ___block_literal_global.97478
- ___block_literal_global.97893
- ___block_literal_global.97942
- ___block_literal_global.98247
- ___block_literal_global.98401
- ___block_literal_global.98426
- ___block_literal_global.98503
- ___block_literal_global.99003
- ___block_literal_global.99101
- _sharedInstance.onceToken.96001
- _sharedInstance.sharedInstance.96003
CStrings:
+ "_presentPrivacyOverview"
+ "com.apple.onboarding.photos"
+ "present"
+ "presenterForPrivacySplashWithIdentifier:"
- "https://www.apple.com/legal/privacy/data/en/photos/"

```

#### PosterFoundation

>  `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

```diff

-290.108.0.0.0
-  __TEXT.__text: 0x43230
+290.109.0.0.0
+  __TEXT.__text: 0x433d8
   __TEXT.__auth_stubs: 0x1040
   __TEXT.__objc_methlist: 0x3158
   __TEXT.__const: 0x196
   __TEXT.__cstring: 0x3cf9
-  __TEXT.__oslogstring: 0x30d1
+  __TEXT.__oslogstring: 0x316f
   __TEXT.__gcc_except_tab: 0x10f8
   __TEXT.__unwind_info: 0x1258
   __TEXT.__objc_classname: 0x720

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 17C1A593-261E-3405-BDA4-36752B643F4B
-  Functions: 1587
-  Symbols:   5567
-  CStrings:  2831
+  UUID: 822D40D8-1BCF-3AF7-B8EC-C15352BFDDC3
+  Functions: 1589
+  Symbols:   5569
+  CStrings:  2833
 
Symbols:
+ -[PFPosterArchiver _unarchiveWithHandler:manifest:error:].cold.12
+ ___65-[PFPosterArchiver unarchivePathAppleArchiveData:manifest:error:]_block_invoke_2.cold.1
CStrings:
+ "Error writing archive data to pipe: %{public}@"
+ "Failed to create tempDirectory %@ : %{public}@"
+ "Manifest data failed to load from URL %@, error: %{public}@"
+ "Unable to copy contents for poster configuration: %{public}@"
+ "Unable to create directory for poster configuration: %{public}@"
+ "Unable to create finalURL: %{public}@"
+ "Unable to create incoming poster path: %{public}@"
+ "Unable to create placement URL: %{public}@"
+ "Unable to move item at provider URL to finalURL: %{public}@"
+ "unarchivingContainerURL %@ is not reachable URL : %{public}@"
- "Manifest data failed to load from URL %@, error: %@"
- "Unable to copy contents for poster configuration: %@"
- "Unable to create directory for poster configuration: %@"
- "Unable to create finalURL: %@"
- "Unable to create incoming poster path: %@"
- "Unable to create placement URL: %@"
- "Unable to move item at provider URL to finalURL: %@"
- "unarchivingContainerURL %@ is not reachable URL : %@"

```

#### RenderBox

>  `/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox`

```diff

-7.0.84.1.101
-  __TEXT.__text: 0x14eebc
+7.0.84.1.108
+  __TEXT.__text: 0x14eff0
   __TEXT.__auth_stubs: 0x2920
   __TEXT.__objc_methlist: 0x2a90
   __TEXT.__const: 0x5f88
-  __TEXT.__gcc_except_tab: 0x74d4
+  __TEXT.__gcc_except_tab: 0x74dc
   __TEXT.__cstring: 0x5d29
   __TEXT.__oslogstring: 0xf7d
   __TEXT.__unwind_info: 0x6200

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4877E0DB-55C0-3E9B-856A-0727C421368C
+  UUID: 5BBA335D-7200-3B8F-936C-BC3F2BCB7393
   Functions: 6873
   Symbols:   18084
   CStrings:  3633
Functions:
~ __ZN2RB9CGContext10apply_blurEfjRNS_6cf_ptrIP9CGContextEE : 1768 -> 1804
~ __ZNK2RB11DisplayList5Layer12make_cgimageERNS_9CGContextERNS_4RectENS1_6EffectEbPv : 1968 -> 2240
CStrings:
+ "7.0.84.1.108"
- "7.0.84.1.101"

```

#### WelcomeKitCore

>  `/System/Library/PrivateFrameworks/WelcomeKitCore.framework/WelcomeKitCore`

```diff

-829.2.2.0.0
-  __TEXT.__text: 0x3673c
+829.2.4.0.0
+  __TEXT.__text: 0x36744
   __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_methlist: 0x336c
   __TEXT.__const: 0x238

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 3D18C50A-51CE-33A2-B399-1AE0FAB5B1B6
+  UUID: CF332DE2-BCC8-3258-A23A-8660AF592AA5
   Functions: 1181
   Symbols:   4623
   CStrings:  3616
Functions:
~ -[WLWiFiController _networkRecordFromSSID:password:channel:] : 452 -> 460

```

#### _CommunicationsUICore_PosterBoardServices

>  `/System/Library/PrivateFrameworks/_CommunicationsUICore_PosterBoardServices.framework/_CommunicationsUICore_PosterBoardServices`

```diff

-104.100.1.2.24
-  __TEXT.__text: 0x10470
+104.100.1.2.26
+  __TEXT.__text: 0x103c4
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_methlist: 0x264
-  __TEXT.__const: 0xb70
+  __TEXT.__const: 0xb50
   __TEXT.__cstring: 0xa50
   __TEXT.__swift5_typeref: 0x49c
   __TEXT.__constg_swiftt: 0x44c

   __TEXT.__unwind_info: 0x490
   __TEXT.__eh_frame: 0x618
   __TEXT.__objc_classname: 0x3b
-  __TEXT.__objc_methname: 0xc8a
+  __TEXT.__objc_methname: 0xcb9
   __TEXT.__objc_methtype: 0x100
-  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c8
+  __DATA_CONST.__objc_selrefs: 0x4d8
   __DATA_CONST.__objc_protorefs: 0x28
   __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__const: 0xa58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C214BDDE-6071-36C9-8852-C20E22BC7700
+  UUID: 10A1ADAF-CEE1-3993-9BBB-4D5AE3AAE5A7
   Functions: 369
-  Symbols:   435
-  CStrings:  268
+  Symbols:   436
+  CStrings:  270
 
Symbols:
+ _OBJC_CLASS_$_UIApplication
+ _block_copy_helper.39
+ _block_copy_helper.48
+ _block_copy_helper.54
+ _block_copy_helper.60
+ _block_descriptor.41
+ _block_descriptor.50
+ _block_descriptor.56
+ _block_descriptor.62
+ _block_destroy_helper.40
+ _block_destroy_helper.49
+ _block_destroy_helper.55
+ _block_destroy_helper.61
- _block_copy_helper.41
- _block_copy_helper.50
- _block_copy_helper.56
- _block_copy_helper.62
- _block_descriptor.43
- _block_descriptor.52
- _block_descriptor.58
- _block_descriptor.64
- _block_destroy_helper.42
- _block_destroy_helper.51
- _block_destroy_helper.57
- _block_destroy_helper.63
Functions:
~ sub_271699794 : 804 -> 1012
~ sub_27169a2c0 -> sub_27169a390 : 116 -> 284
~ sub_27169a334 -> sub_27169a4ac : 92 -> 116
~ sub_27169a390 -> sub_27169a520 : 120 -> 92
~ sub_27169a408 -> sub_27169a57c : 12 -> 120
~ sub_27169a414 -> sub_27169a5f4 : 4 -> 12
~ sub_27169a418 -> sub_27169a600 : 84 -> 4
~ sub_27169a46c -> sub_27169a604 : 284 -> 84
~ sub_2716a559c -> sub_2716a566c : 2368 -> 1988
CStrings:
+ "sharedApplication"
+ "userInterfaceLayoutDirection"

```


</details>

## EOF
