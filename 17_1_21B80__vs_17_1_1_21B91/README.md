# 17.1 (21B80) .vs 17.1.1 (21B91)

## IPSWs

- `iPhone16,1_17.1_21B80_Restore.ipsw`
- `iPhone16,1_17.1.1_21B91_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.1 *(21B80)* | 23.1.0 | 10002.42.9~2 | Tue, 10Oct2023 02:21:19 PDT |
| 17.1.1 *(21B91)* | 23.1.0 | 10002.42.9~2 | Tue, 10Oct2023 02:21:19 PDT |

## MachO

### ⬆️ Updated (4)

<details>
  <summary><i>View Updated</i></summary>

#### BTAudioHALPlugin

>  `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

-171.11.1.1.1
-  __TEXT.__text: 0x62514
+171.11.1.1.4
+  __TEXT.__text: 0x62518
   __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_stubs: 0x1260
   __TEXT.__init_offsets: 0x9c

```

#### WeatherWidget

>  `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherWidget.appex/WeatherWidget`

```diff

-484.0.0.0.0
-  __TEXT.__text: 0x187408
+484.1.0.0.0
+  __TEXT.__text: 0x1873fc
   __TEXT.__auth_stubs: 0x4230
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__objc_methlist: 0x170

```

#### nfcd

>  `/usr/libexec/nfcd`

```diff

-341.9.0.0.0
+341.10.0.0.0
   __TEXT.__text: 0x21867c
   __TEXT.__auth_stubs: 0x16d0
   __TEXT.__objc_stubs: 0xddc0
   __TEXT.__objc_methlist: 0x78f0
   __TEXT.__const: 0xfc0
   __TEXT.__oslogstring: 0x20756
-  __TEXT.__cstring: 0x29c51
+  __TEXT.__cstring: 0x29c52
   __TEXT.__objc_classname: 0x1782
   __TEXT.__objc_methname: 0x15e72
   __TEXT.__objc_methtype: 0x4cc9
CStrings:
+ "NFCD built from (B&I) Stockholm_Base-341.10 at 20:16:51 on Oct 30 2023"
- "NFCD built from (B&I) Stockholm_Base-341.9 at 22:14:25 on Oct  4 2023"

```

#### sharingd

>  `/usr/libexec/sharingd`

```diff

-1936.20.66.2.11
-  __TEXT.__text: 0x583634
+1936.20.66.2.12
+  __TEXT.__text: 0x5836a8
   __TEXT.__auth_stubs: 0x8700
   __TEXT.__objc_stubs: 0x330c0
-  __TEXT.__objc_methlist: 0x1b87c
+  __TEXT.__objc_methlist: 0x1b884
   __TEXT.__cstring: 0x554b6
   __TEXT.__objc_methname: 0x46cc0
-  __TEXT.__oslogstring: 0x1e9bd
+  __TEXT.__oslogstring: 0x1ea3f
   __TEXT.__objc_classname: 0x2bff
   __TEXT.__objc_methtype: 0x9735
   __TEXT.__const: 0xbb48

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arrayobj: 0x6d8
   __DATA.__objc_const: 0x3ae80
-  __DATA.__objc_selrefs: 0xffc8
+  __DATA.__objc_selrefs: 0xffd0
   __DATA.__objc_protorefs: 0x220
   __DATA.__objc_classrefs: 0x1408
   __DATA.__objc_superrefs: 0x770

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24007
+  Functions: 24008
   Symbols:   3889
-  CStrings:  26269
+  CStrings:  26270
 
CStrings:
+ "sessionSuspensionEnded attempting to resume"
+ "sessionWasSuspended waiting for ended suspension to resume. This should happen when bt is toggled back on"
- "sessionWasSuspended"

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.1 *(21B80)* | 616.2.9.10.10 |
| 17.1.1 *(21B91)* | 616.2.9.10.11 |

### Dylibs

#### ⬆️ Updated (9)

<details>
  <summary><i>View Updated</i></summary>

#### AuthenticationServices

>  `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-616.2.9.10.10
-  __TEXT.__text: 0x54c80
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0x5518
+616.2.9.10.11
+  __TEXT.__text: 0x54d68
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x5528
   __TEXT.__cstring: 0x4996
   __TEXT.__const: 0x714
   __TEXT.__oslogstring: 0x22ec

   __TEXT.__unwind_info: 0x1c50
   __TEXT.__eh_frame: 0x1d8
   __TEXT.__objc_classname: 0x1c25
-  __TEXT.__objc_methname: 0x1454f
+  __TEXT.__objc_methname: 0x145af
   __TEXT.__objc_methtype: 0x4263
-  __TEXT.__objc_stubs: 0xd7e0
+  __TEXT.__objc_stubs: 0xd840
   __DATA_CONST.__got: 0x390
   __DATA_CONST.__const: 0x1550
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xafc0
-  __DATA_CONST.__objc_selrefs: 0x4048
+  __DATA_CONST.__objc_const: 0xafe0
+  __DATA_CONST.__objc_selrefs: 0x4060
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__cfstring: 0x3f80
   __AUTH_CONST.__objc_const: 0x3050

   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH.__objc_data: 0x23f0
   __AUTH.__data: 0x98
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x838
+  __DATA.__objc_classrefs: 0x840
   __DATA.__objc_superrefs: 0x2f8
-  __DATA.__objc_ivar: 0x66c
+  __DATA.__objc_ivar: 0x670
   __DATA.__data: 0x15e8
   __DATA.__bss: 0x6c0
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2485
-  Symbols:   8711
-  CStrings:  3968
+  Functions: 2486
+  Symbols:   8719
+  CStrings:  3972
 
Symbols:
+ -[ASPasswordAuthenticationPaneViewController viewDidDisappear:]
+ _OBJC_CLASS_$_UIKeyboardImpl
+ _OBJC_IVAR_$_ASPasswordAuthenticationPaneViewController._didForceSoftwareKeyboardOn
+ _UIKeyboardAutomaticIsOnScreen
+ _objc_msgSend$activeInstance
+ _objc_msgSend$ejectKeyDown
+ _objc_msgSend$hardwareKeyboardAvailabilityChanged
CStrings:
+ "_didForceSoftwareKeyboardOn"
+ "activeInstance"
+ "ejectKeyDown"
+ "hardwareKeyboardAvailabilityChanged"
+ "\xa1"
- "\x91"

```

#### WeatherKit

>  `/System/Library/Frameworks/WeatherKit.framework/WeatherKit`

```diff

-484.0.0.0.0
-  __TEXT.__text: 0x239188
-  __TEXT.__auth_stubs: 0x2b70
+484.1.0.0.0
+  __TEXT.__text: 0x23918c
+  __TEXT.__auth_stubs: 0x2b80
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x17890
   __TEXT.__swift5_typeref: 0x5a81

   __AUTH_CONST.__const: 0xec98
   __AUTH_CONST.__auth_ptr: 0x300
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x15b8
+  __AUTH_CONST.__auth_got: 0x15c0
   __AUTH.__data: 0x470
   __AUTH.__objc_data: 0x0
   __DATA.__objc_protorefs: 0x10

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 14137
-  Symbols:   7971
+  Symbols:   7972
   CStrings:  2104
 
Symbols:
+ _swift_initStackObject

```

#### HomeDeviceSetup

>  `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-217.10.10.0.0
-  __TEXT.__text: 0x4bb94
+217.11.1.0.0
+  __TEXT.__text: 0x4bb88
   __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_methlist: 0x1c70
   __TEXT.__const: 0x258

   __TEXT.__oslogstring: 0x3bc
   __TEXT.__unwind_info: 0xb50
   __TEXT.__objc_classname: 0x21e
-  __TEXT.__objc_methname: 0x983e
+  __TEXT.__objc_methname: 0x9826
   __TEXT.__objc_methtype: 0xe52
-  __TEXT.__objc_stubs: 0x6340
+  __TEXT.__objc_stubs: 0x6320
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x11b8
   __DATA_CONST.__objc_classlist: 0x58

   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5888
-  __DATA_CONST.__objc_selrefs: 0x1eb0
+  __DATA_CONST.__objc_selrefs: 0x1ea8
   __DATA_CONST.__objc_arraydata: 0x1c8
   __AUTH_CONST.__cfstring: 0x3900
   __AUTH_CONST.__objc_const: 0x540

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   Functions: 1116
-  Symbols:   4292
-  CStrings:  4162
+  Symbols:   4291
+  CStrings:  4161
 
Symbols:
- _objc_msgSend$setShouldSetupHomePod:
CStrings:
- "setShouldSetupHomePod:"

```

#### MediaExperience

>  `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-125.13.1.1.0
-  __TEXT.__text: 0x18cef0
+125.13.1.2.0
+  __TEXT.__text: 0x18ceec
   __TEXT.__auth_stubs: 0x1db0
   __TEXT.__objc_methlist: 0x36a4
-  __TEXT.__cstring: 0x23934
+  __TEXT.__cstring: 0x2395d
   __TEXT.__const: 0x1930
   __TEXT.__gcc_except_tab: 0x1650
   __TEXT.__oslogstring: 0x2afd7
   __TEXT.__dlopen_cstrs: 0x503
-  __TEXT.__unwind_info: 0x3870
+  __TEXT.__unwind_info: 0x386c
   __TEXT.__objc_classname: 0x388
   __TEXT.__objc_methname: 0xf13e
   __TEXT.__objc_methtype: 0x18bc

   __DATA_CONST.__objc_const: 0x5970
   __DATA_CONST.__objc_selrefs: 0x2800
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x14dc0
+  __AUTH_CONST.__cfstring: 0x14e00
   __AUTH_CONST.__const: 0x32a8
   __AUTH_CONST.__objc_const: 0xca0
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libobjc.A.dylib
   Functions: 4768
   Symbols:   15417
-  CStrings:  8524
+  CStrings:  8526
 
Symbols:
+ ___57-[MXSessionManager(Utilities) updateMuteState:muteValue:]_block_invoke.22
- ___57-[MXSessionManager(Utilities) updateMuteState:muteValue:]_block_invoke.16
CStrings:
+ "20:15:44"
+ "Oct 30 2023"
+ "com.apple.facetime"
+ "com.apple.mobilephone"
- "22:12:26"
- "Oct  4 2023"

```

#### UIKitCore

>  `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-7115.1.109.0.0
-  __TEXT.__text: 0x1301a9c
+7115.1.110.0.0
+  __TEXT.__text: 0x1301a68
   __TEXT.__auth_stubs: 0x7750
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x13e14c

   __TEXT.__oslogstring: 0x39e1f
   __TEXT.__ustring: 0x15a0
   __TEXT.__objc_const_ax: 0xa68
-  __TEXT.__unwind_info: 0x50f44
+  __TEXT.__unwind_info: 0x50f54
   __TEXT.__eh_frame: 0xe38
   __TEXT.__objc_classname: 0x2e591
   __TEXT.__objc_methname: 0x2ad40f
Symbols:
+ _block_copy_helper.83
+ _block_descriptor.85
+ _block_destroy_helper.84
- _block_copy_helper.58
- _block_copy_helper.62
- _block_copy_helper.71
- _block_copy_helper.81
- _block_descriptor.60
- _block_descriptor.64
- _block_descriptor.73
- _block_descriptor.83
- _block_destroy_helper.59
- _block_destroy_helper.63
- _block_destroy_helper.72
- _block_destroy_helper.82

```

#### WeatherCore

>  `/System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore`

```diff

-484.0.0.0.0
-  __TEXT.__text: 0x17a770
+484.1.0.0.0
+  __TEXT.__text: 0x17a808
   __TEXT.__auth_stubs: 0x3ab0
   __TEXT.__objc_methlist: 0x554
   __TEXT.__const: 0x115d4

   __TEXT.__swift5_types: 0x4dc
   __TEXT.__swift5_capture: 0xe6c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6e04
-  __TEXT.__eh_frame: 0x74e0
+  __TEXT.__unwind_info: 0x6e6c
+  __TEXT.__eh_frame: 0x7540
   __TEXT.__objc_classname: 0x10b
   __TEXT.__objc_methname: 0x51d8
   __TEXT.__objc_methtype: 0xc8d

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12386
-  Symbols:   7054
+  Functions: 12389
+  Symbols:   7056
   CStrings:  2550
 

```

#### WeatherDaemon

>  `/System/Library/PrivateFrameworks/WeatherDaemon.framework/WeatherDaemon`

```diff

-484.0.0.0.0
-  __TEXT.__text: 0x1e7f28
+484.1.0.0.0
+  __TEXT.__text: 0x1e8028
   __TEXT.__auth_stubs: 0x2a70
   __TEXT.__objc_methlist: 0x520
   __TEXT.__const: 0xe404

   __TEXT.__swift5_assocty: 0x5d0
   __TEXT.__swift5_capture: 0x1a04
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x8718
-  __TEXT.__eh_frame: 0xaf44
+  __TEXT.__unwind_info: 0x77dc
+  __TEXT.__eh_frame: 0xafc4
   __TEXT.__objc_classname: 0x8f
   __TEXT.__objc_methname: 0xe92
   __TEXT.__objc_methtype: 0x566

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12848
+  Functions: 12851
   Symbols:   6307
   CStrings:  1204
 

```

#### WeatherMaps

>  `/System/Library/PrivateFrameworks/WeatherMaps.framework/WeatherMaps`

```diff

-484.0.0.0.0
-  __TEXT.__text: 0x1d8c08
+484.1.0.0.0
+  __TEXT.__text: 0x1d8c1c
   __TEXT.__auth_stubs: 0x4a40
   __TEXT.__objc_methlist: 0x1208
   __TEXT.__const: 0xe574

   __TEXT.__swift5_types: 0x6bc
   __TEXT.__swift5_capture: 0x1868
   __TEXT.__swift5_protos: 0x19c
-  __TEXT.__unwind_info: 0x7488
+  __TEXT.__unwind_info: 0x747c
   __TEXT.__eh_frame: 0x902c
   __TEXT.__objc_classname: 0x1c8
   __TEXT.__objc_methname: 0x77d9

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12155
+  Functions: 12156
   Symbols:   7119
   CStrings:  3087
 

```

#### libPN548_API.dylib

>  `/usr/lib/libPN548_API.dylib`

```diff

-341.9.0.0.0
+341.10.0.0.0
   __TEXT.__text: 0x41174
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__cstring: 0x9c9b
-  __TEXT.__oslogstring: 0x6efb
+  __TEXT.__cstring: 0x9c9c
+  __TEXT.__oslogstring: 0x6efc
   __TEXT.__const: 0x732
   __TEXT.__unwind_info: 0x560
   __DATA_CONST.__got: 0x48
CStrings:
+ "%s:%i Running build from (B&I) Stockholm_Base-341.10 built at 20:15:21 on Oct 30 2023"
+ "%{public}s:%i Running build from (B&I) Stockholm_Base-341.10 built at 20:15:21 on Oct 30 2023"
- "%s:%i Running build from (B&I) Stockholm_Base-341.9 built at 22:12:42 on Oct  4 2023"
- "%{public}s:%i Running build from (B&I) Stockholm_Base-341.9 built at 22:12:42 on Oct  4 2023"

```


</details>

## EOF
