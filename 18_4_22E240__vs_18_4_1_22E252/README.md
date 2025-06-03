# 18.4 (22E240) .vs 18.4.1 (22E252)

## IPSWs

- `iPhone17,1_18.4_22E240_Restore.ipsw`
- `iPhone17,1_18.4.1_22E252_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.4 *(22E240)* | 24.4.0 | 11417.102.9~20 | Sat, 15Mar2025 18:26:55 PDT |
| 18.4.1 *(22E252)* | 24.4.0 | 11417.102.9~20 | Sat, 15Mar2025 18:26:55 PDT |

### Kexts

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 440.4.0.0.0
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2c29
+  __TEXT.__cstring: 0x2c32
   __TEXT.__os_log: 0x16f1
   __TEXT_EXEC.__text: 0xafb0
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1780
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: D62E89CF-D5DA-3591-B99C-63DE4DCB9D61
+  UUID: 01E1D500-5F49-3503-8949-033F73FE85FF
   Functions: 258
   Symbols:   0
-  CStrings:  232
+  CStrings:  233
 
CStrings:
+ "18:44:27"
+ "18:44:28"
+ "Apr  7 2025"
- "19:48:02"
- "Mar 17 2025"

```

</details>

## MachO

### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### Siri

>  `/Applications/Siri.app/Siri`

```diff

-3404.71.4.11.4
-  __TEXT.__text: 0xbc098
+3404.71.4.11.5
+  __TEXT.__text: 0xbc0a0
   __TEXT.__auth_stubs: 0x24f0
   __TEXT.__objc_stubs: 0x173a0
   __TEXT.__objc_methlist: 0xca08

   __TEXT.__eh_frame: 0x950
   __DATA_CONST.__auth_got: 0x1288
   __DATA_CONST.__got: 0x1450
-  __DATA_CONST.__auth_ptr: 0x648
+  __DATA_CONST.__auth_ptr: 0x610
   __DATA_CONST.__const: 0x35d8
   __DATA_CONST.__cfstring: 0x2fe0
   __DATA_CONST.__objc_classlist: 0x348

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D9DAB53F-F6DB-31D3-87E8-107E62677F54
+  UUID: 71D7470F-E04A-3CE9-A294-13321F391F6D
   Functions: 4043
   Symbols:   1515
   CStrings:  8298
Functions:
~ sub_100031310 : 164 -> 172

```

#### AssistantSettingsControlsExtension

>  `/System/Library/ExtensionKit/Extensions/AssistantSettingsControlsExtension.appex/AssistantSettingsControlsExtension`

```diff

-3404.71.4.11.4
+3404.71.4.11.5
   __TEXT.__text: 0x5f2e4
   __TEXT.__auth_stubs: 0xd30
   __TEXT.__cstring: 0x4b12

   __TEXT.__eh_frame: 0x2eb0
   __DATA_CONST.__auth_got: 0x698
   __DATA_CONST.__got: 0x388
-  __DATA_CONST.__auth_ptr: 0x9e8
+  __DATA_CONST.__auth_ptr: 0xa08
   __DATA_CONST.__const: 0x1bc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: CC6818BA-E8FA-3A0F-B168-EED486A3641F
+  UUID: 26FF86A8-F55B-33CF-9155-FFE4961823DD
   Functions: 2795
   Symbols:   115
   CStrings:  441

```

#### WiFiSettingsControlsExtension

>  `/System/Library/ExtensionKit/Extensions/WiFiSettingsControlsExtension.appex/WiFiSettingsControlsExtension`

```diff

   __TEXT.__eh_frame: 0xd04
   __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__auth_ptr: 0x790
+  __DATA_CONST.__auth_ptr: 0x780
   __DATA_CONST.__const: 0xc90
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B3194829-88BF-3F2C-A25F-CBB5E9B3ECC6
+  UUID: A81ED803-3B46-38E8-82CC-74C0FE394EB1
   Functions: 940
   Symbols:   121
   CStrings:  148

```

#### MobileStoreSettings

>  `/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings`

```diff

-11.4.24.2.2
+11.4.24.2.4
   __TEXT.__text: 0x2b4a0
   __TEXT.__auth_stubs: 0x1400
   __TEXT.__objc_stubs: 0x600

   __TEXT.__eh_frame: 0xc08
   __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__auth_ptr: 0x520
+  __DATA_CONST.__auth_ptr: 0x508
   __DATA_CONST.__const: 0xd10
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x30

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 834A8AF4-1408-3D7B-B396-27AF977E96D4
+  UUID: 2230C3CD-A580-3B8F-8CB3-F3E7EF28432A
   Functions: 747
   Symbols:   253
   CStrings:  404

```

#### appstored

>  `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

-11.4.24.2.2
-  __TEXT.__text: 0x43d8e8
+11.4.24.2.4
+  __TEXT.__text: 0x43d300
   __TEXT.__auth_stubs: 0x3f50
-  __TEXT.__objc_stubs: 0x12820
+  __TEXT.__objc_stubs: 0x12840
   __TEXT.__objc_methlist: 0xdcc8
   __TEXT.__dlopen_cstrs: 0x45e
   __TEXT.__const: 0x1aca8
-  __TEXT.__cstring: 0x21fda
-  __TEXT.__objc_methname: 0x1acc9
+  __TEXT.__cstring: 0x21f97
+  __TEXT.__objc_methname: 0x1acd8
   __TEXT.__constg_swiftt: 0x2194
   __TEXT.__swift5_typeref: 0x3806
   __TEXT.__swift5_fieldmd: 0x232c

   __TEXT.__swift5_capture: 0x1cbc
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift_as_entry: 0x36c
-  __TEXT.__oslogstring: 0x38ab7
+  __TEXT.__oslogstring: 0x38a41
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift_as_ret: 0x424
   __TEXT.__swift5_protos: 0x18
   __TEXT.__gcc_except_tab: 0xabf8
-  __TEXT.__unwind_info: 0xa810
+  __TEXT.__unwind_info: 0xa7f0
   __TEXT.__eh_frame: 0xb06c
   __DATA_CONST.__auth_got: 0x1fb8
   __DATA_CONST.__got: 0x18c0
-  __DATA_CONST.__auth_ptr: 0x8f0
-  __DATA_CONST.__const: 0x1f638
-  __DATA_CONST.__cfstring: 0x1b380
+  __DATA_CONST.__auth_ptr: 0x8e8
+  __DATA_CONST.__const: 0x1f5e8
+  __DATA_CONST.__cfstring: 0x1b320
   __DATA_CONST.__objc_classlist: 0x1650
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x538

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA.__objc_const: 0x35738
-  __DATA.__objc_selrefs: 0x62c0
+  __DATA.__objc_selrefs: 0x62c8
   __DATA.__objc_ivar: 0x2494
   __DATA.__objc_data: 0xff80
   __DATA.__data: 0x7580

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5F760438-346E-3E2D-A0D3-E97735810D9B
-  Functions: 12584
+  UUID: 4D4EBECE-6B02-3A0A-8028-AEC02D2A8FD2
+  Functions: 12573
   Symbols:   2036
-  CStrings:  18428
+  CStrings:  18421
 
CStrings:
+ "17:59:21"
+ "Apr  4 2025"
+ "addDependency:"
- "22:07:10"
- "Completed store queue checks on reboot"
- "Failed to complete store queue checks on reboot; will retry next daemon launch"
- "Mar 11 2025"
- "Reboot"
- "checkStoreQueues"
- "com.apple.appstored.TaskQueue.barrierBlock"

```

#### IPConfiguration

>  `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

```diff

-494.102.1.0.0
-  __TEXT.__text: 0x59cf0
+494.102.2.0.0
+  __TEXT.__text: 0x59d50
   __TEXT.__auth_stubs: 0xf90
   __TEXT.__const: 0x300
   __TEXT.__oslogstring: 0x63a5
   __TEXT.__cstring: 0x3c92
-  __TEXT.__unwind_info: 0xb80
+  __TEXT.__unwind_info: 0xb90
   __DATA_CONST.__auth_got: 0x7c8
   __DATA_CONST.__got: 0x370
   __DATA_CONST.__auth_ptr: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: AA4D7092-7655-3419-842B-FC368774724D
-  Functions: 985
+  UUID: 2F8E78A7-42B7-3C96-9B34-4A69D7A1CBEF
+  Functions: 987
   Symbols:   466
   CStrings:  1988
 
CStrings:
+ "IPv6.Prefix=%s/%d;IPv6.RouterHardwareAddress="
- "IPv6.Prefix=%@/%@;IPv6.RouterHardwareAddress="

```

#### libRPAC.dylib

>  `/usr/lib/libRPAC.dylib`

```diff

-84.0.0.0.0
-  __TEXT.__text: 0x9245c
-  __TEXT.__auth_stubs: 0xad0
+88.0.0.0.0
+  __TEXT.__text: 0x92424
+  __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x5190
+  __TEXT.__cstring: 0x5140
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__const: 0x1d58
   __TEXT.__objc_methname: 0x13b
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x320
-  __DATA_CONST.__auth_got: 0x580
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x330
+  __DATA_CONST.__auth_got: 0x578
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__interpose: 0x230
+  __AUTH_CONST.__interpose: 0x220
   __DATA.__objc_selrefs: 0x88
-  __DATA.__data: 0x7c8
+  __DATA.__data: 0x7c4
   __DATA.__common: 0x800e8
-  __DATA.__bss: 0x5809e0
+  __DATA.__bss: 0x5807d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 484E4D90-56E9-3A4E-84D4-EC82121D79D8
-  Functions: 277
-  Symbols:   732
-  CStrings:  654
+  UUID: 952FD03E-567F-3E2D-A26A-8748FF1471AD
+  Functions: 279
+  Symbols:   730
+  CStrings:  652
 
Symbols:
+ _lockLockInDispatchLockMap
+ _lockLockInNSCondtionLockMap
+ _unlockLockInDispatchLockMap
+ _unlockLockInNSConditionLockMap
- __ZL18max_primitive_maps
- __interpose_dlsym
- _dlsym
- _interposed_dlsym
- deletePrimitiveEntry.cold.1
- interposed_dlsym.dlsym_count
CStrings:
+ "Inversion detection for %s\n"
+ "SemaphoreWaitingAGPCLogType"
+ "semaphorewaitingagpclogtype"
- "DispatchSemaphoreWaitingOnMainThreadAGPCLogType"
- "deletePrimitiveEntry"
- "dispatchsemaphorewaitingonmainthreadagpclogtype"
- "dlsym"
- "libRPAC.dylib: interposed_dlsym invoked\n"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.4 *(22E240)* | iBoot-11881.100.993 |
| 18.4.1 *(22E252)* | iBoot-11881.100.993 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.4 *(22E240)* | 621.1.15.10.7 |
| 18.4.1 *(22E252)* | 621.1.15.10.7 |

### Dylibs

#### ⬆️ Updated (4)

<details>
  <summary><i>View Updated</i></summary>

#### AudioCodecs

>  `/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs`

```diff

-746.5.10.0.0
-  __TEXT.__text: 0x598514
+746.5.11.0.0
+  __TEXT.__text: 0x598534
   __TEXT.__auth_stubs: 0x1540
   __TEXT.__const: 0x3028cc
   __TEXT.__cstring: 0xa204

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: C37282EE-EF5F-323D-BA9B-C5B820271773
+  UUID: 2D3D1ECD-D220-30F0-91EF-9EE201C5EAA9
   Functions: 8800
   Symbols:   25768
   CStrings:  3578
Functions:
~ __ZN4apac3hoa11CodecConfig11DeserializeER16TBitstreamReaderIjE : 4156 -> 4188
CStrings:
+ "17:49:08"
+ "Apr  4 2025"
- "21:23:18"
- "Mar  7 2025"

```

#### CoreServices

>  `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1378.17.0.0.0
-  __TEXT.__text: 0x199688
+1378.18.0.0.0
+  __TEXT.__text: 0x199700
   __TEXT.__auth_stubs: 0x3210
   __TEXT.__objc_methlist: 0xc3ec
   __TEXT.__const: 0x920

   __TEXT.__oslogstring: 0x12f56
   __TEXT.__gcc_except_tab: 0x24424
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xa710
+  __TEXT.__unwind_info: 0xa718
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x1d52
   __TEXT.__objc_methname: 0x1be4b

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A14CBB38-86E6-3807-9738-A00B19AA4ED7
-  Functions: 8263
-  Symbols:   26933
+  UUID: 0E9DF97F-96AA-3C2D-A5AD-3A764A0C4330
+  Functions: 8264
+  Symbols:   26936
   CStrings:  13085
 
Symbols:
+ GCC_except_table128
+ GCC_except_table142
+ GCC_except_table164
+ __ZN14LaunchServices17BindingEvaluation25BindingEligibilityChecker36isDefaultAppCategoryBindingEligibileERKNS0_5StateEPK24LSDefaultAppCategoryInfoRKNS0_15ExtendedBindingE
- GCC_except_table162
Functions:
~ __ZN14LaunchServices17BindingEvaluation25BindingEligibilityChecker23checkBindingIsEligibileERKNS0_5StateERKNS0_15ExtendedBindingE : 816 -> 720
+ __ZN14LaunchServices17BindingEvaluation25BindingEligibilityChecker36isDefaultAppCategoryBindingEligibileERKNS0_5StateEPK24LSDefaultAppCategoryInfoRKNS0_15ExtendedBindingE

```

#### AssistantServices

>  `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3404.80.4.11.3
-  __TEXT.__text: 0x1ac3f8
+3404.80.4.11.4
+  __TEXT.__text: 0x1ac720
   __TEXT.__auth_stubs: 0x1550
   __TEXT.__objc_methlist: 0x1dbfc
   __TEXT.__const: 0x458
   __TEXT.__dlopen_cstrs: 0x484
   __TEXT.__gcc_except_tab: 0x2adc
-  __TEXT.__cstring: 0x3d2cb
-  __TEXT.__oslogstring: 0x10ea8
+  __TEXT.__cstring: 0x3d2d1
+  __TEXT.__oslogstring: 0x10f6b
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x7d10
+  __TEXT.__unwind_info: 0x7d18
   __TEXT.__objc_classname: 0x4f0c
   __TEXT.__objc_methname: 0x3b165
   __TEXT.__objc_methtype: 0xaaf0

   __DATA_CONST.__objc_superrefs: 0xdf0
   __DATA_CONST.__objc_arraydata: 0x2090
   __AUTH_CONST.__auth_got: 0xab8
-  __AUTH_CONST.__const: 0x3a60
-  __AUTH_CONST.__cfstring: 0x27080
+  __AUTH_CONST.__const: 0x3a80
+  __AUTH_CONST.__cfstring: 0x270a0
   __AUTH_CONST.__objc_const: 0x33638
   __AUTH_CONST.__objc_intobj: 0x2328
   __AUTH_CONST.__objc_dictobj: 0xb90

   __AUTH.__data: 0x2b0
   __DATA.__objc_ivar: 0x255c
   __DATA.__data: 0x4178
-  __DATA.__bss: 0x1330
+  __DATA.__bss: 0x1340
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1158
   __DATA_DIRTY.__common: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48240B46-2E2A-332B-9ADC-DF6123EB6CD7
-  Functions: 11758
-  Symbols:   37463
-  CStrings:  24143
+  UUID: 7A44BD8F-2535-3644-9869-340513E68BB9
+  Functions: 11759
+  Symbols:   37468
+  CStrings:  24147
 
Symbols:
+ GCC_except_table11507
+ GCC_except_table11652
+ GCC_except_table11671
+ GCC_except_table11674
+ GCC_except_table11676
+ _AFIsLocaleSupportedForSirClassic.once
+ _AFIsLocaleSupportedForSirClassic.supportedSiriClassicLocales
+ ___AFIsLocaleSupportedForSirClassic_block_invoke
+ ___Block_byref_object_copy_.47686
+ ___Block_byref_object_copy_.48414
+ ___Block_byref_object_copy_.48696
+ ___Block_byref_object_dispose_.47687
+ ___Block_byref_object_dispose_.48415
+ ___Block_byref_object_dispose_.48697
+ ___block_literal_global.1089
+ ___block_literal_global.22.47192
+ ___block_literal_global.25.47186
+ ___block_literal_global.46852
+ ___block_literal_global.46878
+ ___block_literal_global.47.48709
+ ___block_literal_global.47032
+ ___block_literal_global.47180
+ ___block_literal_global.47706
+ ___block_literal_global.48370
+ ___block_literal_global.48717
+ ___block_literal_global.5.48702
+ _sharedObserver.onceToken.48716
+ _sharedObserver.sharedObserver.48718
- GCC_except_table11506
- GCC_except_table11651
- GCC_except_table11670
- GCC_except_table11673
- GCC_except_table11675
- ___Block_byref_object_copy_.47681
- ___Block_byref_object_copy_.48409
- ___Block_byref_object_copy_.48691
- ___Block_byref_object_dispose_.47682
- ___Block_byref_object_dispose_.48410
- ___Block_byref_object_dispose_.48692
- ___block_literal_global.22.47187
- ___block_literal_global.25.47181
- ___block_literal_global.46847
- ___block_literal_global.46873
- ___block_literal_global.47.48704
- ___block_literal_global.47027
- ___block_literal_global.47175
- ___block_literal_global.47701
- ___block_literal_global.48365
- ___block_literal_global.48712
- ___block_literal_global.5.48697
- _sharedObserver.onceToken.48711
- _sharedObserver.sharedObserver.48713
Functions:
~ _AFDeviceSupportsDisablingServerFallbackWhenMissingAsset : 240 -> 556
+ ___AFIsLocaleSupportedForSirClassic_block_invoke
CStrings:
+ "%s AFDeviceSupportsDisablingServerFallbackWhenMissingAsset returns true as locale is nil"
+ "%s AFDeviceSupportsDisablingServerFallbackWhenMissingAsset returns true for unsupported server locale: %@"
+ "hi_IN"

```

#### WatchListKit

>  `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-850.40.40.0.0
-  __TEXT.__text: 0x65a34
+850.41.1.0.0
+  __TEXT.__text: 0x65a0c
   __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_methlist: 0x6e94
   __TEXT.__const: 0x1ac

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D7309F5-E55C-35B1-8328-8249AF818FDC
+  UUID: 594CC431-7F49-3E95-90EA-9C1822C52506
   Functions: 2713
   Symbols:   9992
   CStrings:  6350
Functions:
~ +[NSURL(WLKAdditions) wlk_URLWithServerConfig:endpoint:relativeToBaseURL:queryParameters:suppressParameterEncoding:] : 748 -> 708

```


</details>

## Feature Flags

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### WiFiManager.plist

>  `Domain/WiFiManager.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
-	<key>EnableCarPlayJoinAfterInCar</key>
-	<dict>
-		<key>Enabled</key>
-		<true/>
-	</dict>
 	<key>EnableNANPHS</key>
 	<dict>
 		<key>Enabled</key>

```


</details>

## EOF
