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

   __DATA_CONST.__kalloc_type: 0xc0
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
-  Functions: 12584
+  Functions: 12573
   Symbols:   2036
-  CStrings:  15038
+  CStrings:  15034
 
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
-  Functions: 985
+  Functions: 987
   Symbols:   466
   CStrings:  1670
 
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
-  Functions: 277
-  Symbols:   732
-  CStrings:  635
+  Functions: 279
+  Symbols:   730
+  CStrings:  633
 
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

#### ⬆️ Updated (9)

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
-  Functions: 8263
-  Symbols:   10047
+  Functions: 8264
+  Symbols:   10048
   CStrings:  10301
 

```

#### _MapKit_SwiftUI

>  `/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI`

```diff

   __DATA_CONST.__objc_selrefs: 0x9f0
   __DATA_CONST.__objc_protorefs: 0x48
   __AUTH_CONST.__auth_got: 0x10b0
-  __AUTH_CONST.__auth_ptr: 0x10c8
+  __AUTH_CONST.__auth_ptr: 0xeb8
   __AUTH_CONST.__const: 0x6fe0
   __AUTH_CONST.__objc_const: 0x14e0
   __AUTH.__objc_data: 0x7a0

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

   __DATA_CONST.__objc_arraydata: 0x2090
   __AUTH_CONST.__auth_got: 0xab8
   __AUTH_CONST.__auth_ptr: 0x8
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
-  Functions: 11758
-  Symbols:   14043
-  CStrings:  19242
+  Functions: 11759
+  Symbols:   14044
+  CStrings:  19245
 
CStrings:
+ "%s AFDeviceSupportsDisablingServerFallbackWhenMissingAsset returns true as locale is nil"
+ "%s AFDeviceSupportsDisablingServerFallbackWhenMissingAsset returns true for unsupported server locale: %@"
+ "hi_IN"

```

#### SiriSharedUI

>  `/System/Library/PrivateFrameworks/SiriSharedUI.framework/SiriSharedUI`

```diff

-3404.71.4.11.4
+3404.71.4.11.5
   __TEXT.__text: 0xc0d5c
   __TEXT.__auth_stubs: 0x2b50
   __TEXT.__objc_methlist: 0x6064

   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x15b8
-  __AUTH_CONST.__auth_ptr: 0xb50
+  __AUTH_CONST.__auth_ptr: 0xba0
   __AUTH_CONST.__const: 0x2d80
   __AUTH_CONST.__cfstring: 0xc40
   __AUTH_CONST.__objc_const: 0xac70

```

#### UserNotificationsKit

>  `/System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit`

```diff

-941.5.3.106.0
+941.5.3.107.0
   __TEXT.__text: 0x58c38
   __TEXT.__auth_stubs: 0x1bb0
   __TEXT.__objc_methlist: 0x2c0c

   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0xde8
-  __AUTH_CONST.__auth_ptr: 0x5c0
+  __AUTH_CONST.__auth_ptr: 0x5c8
   __AUTH_CONST.__const: 0x1a20
   __AUTH_CONST.__cfstring: 0x18e0
   __AUTH_CONST.__objc_const: 0x53d0

```

#### UserNotificationsUIKit

>  `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-941.5.3.106.0
+941.5.3.107.0
   __TEXT.__text: 0x19c080
   __TEXT.__auth_stubs: 0x24f0
   __TEXT.__objc_methlist: 0x196a4

   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0x158
   __AUTH_CONST.__auth_got: 0x1288
-  __AUTH_CONST.__auth_ptr: 0x798
+  __AUTH_CONST.__auth_ptr: 0x740
   __AUTH_CONST.__const: 0x5168
   __AUTH_CONST.__cfstring: 0x7d00
   __AUTH_CONST.__objc_const: 0x24738
CStrings:
+ "addAttributes:range:"
- "setAttributes:range:"

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

```

#### WiFiKitUI

>  `/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`

```diff

   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x150
   __AUTH_CONST.__auth_got: 0xc98
-  __AUTH_CONST.__auth_ptr: 0x708
+  __AUTH_CONST.__auth_ptr: 0x750
   __AUTH_CONST.__const: 0x1c40
   __AUTH_CONST.__cfstring: 0x67e0
   __AUTH_CONST.__objc_const: 0x13330

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
