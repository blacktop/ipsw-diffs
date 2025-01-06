# 18.2 (22C152) .vs 18.2.1 (22C161)

## IPSWs

- `iPhone17,1_18.2_22C152_Restore.ipsw`
- `iPhone17,1_18.2.1_22C161_Restore.ipsw`

## Kernel

### Version

| iOS               | Version | Build        | Date                        |
| :---------------- | :------ | :----------- | :-------------------------- |
| 18.2 *(22C152)*   | 24.2.0  | 11215.62.3~1 | Thu, 14Nov2024 22:55:26 PST |
| 18.2.1 *(22C161)* | 24.2.0  | 11215.62.3~1 | Thu, 14Nov2024 22:55:26 PST |

## MachO

### ⬆️ Updated (6)

<details>
  <summary><i>View Updated</i></summary>

#### DiagnosticsReporter

>  `/Applications/DiagnosticsReporter.app/DiagnosticsReporter`

```diff

-727.60.31.0.0
+727.62.1.0.0
   __TEXT.__text: 0xe0f8
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_methlist: 0x180

   __TEXT.__eh_frame: 0x3f8
   __DATA_CONST.__auth_got: 0x670
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__auth_ptr: 0x210
+  __DATA_CONST.__auth_ptr: 0x1d0
   __DATA_CONST.__const: 0x5a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38

```

#### osanalyticshelper

>  `/System/Library/CoreServices/osanalyticshelper`

```diff

-727.60.31.0.0
-  __TEXT.__text: 0x11c80
-  __TEXT.__auth_stubs: 0xcc0
+727.62.1.0.0
+  __TEXT.__text: 0x11cd8
+  __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_stubs: 0x2420
   __TEXT.__objc_methlist: 0x664
   __TEXT.__const: 0x1ba

   __TEXT.__cstring: 0x1c31
   __TEXT.__objc_classname: 0x14c
   __TEXT.__objc_methtype: 0x3c6
-  __TEXT.__gcc_except_tab: 0x794
+  __TEXT.__gcc_except_tab: 0x79c
   __TEXT.__objc_methname: 0x1e01
   __TEXT.__constg_swiftt: 0x94
   __TEXT.__swift5_typeref: 0x78

   __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x430
-  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__auth_got: 0x680
   __DATA_CONST.__got: 0x480
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0x8e0

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 272
-  Symbols:   379
+  Symbols:   380
   CStrings:  900
 
Symbols:
+ _arc4random_uniform

```

#### TrustedPeersHelper

>  `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61439.62.1.0.0
+61439.62.2.0.0
   __TEXT.__text: 0x21f38c
   __TEXT.__auth_stubs: 0x1e70
   __TEXT.__objc_stubs: 0x2860

   __TEXT.__eh_frame: 0x7050
   __DATA_CONST.__auth_got: 0xf48
   __DATA_CONST.__got: 0x848
-  __DATA_CONST.__auth_ptr: 0x658
+  __DATA_CONST.__auth_ptr: 0x648
   __DATA_CONST.__const: 0xfb30
   __DATA_CONST.__cfstring: 0x1f20
   __DATA_CONST.__objc_classlist: 0x270

```

#### cdpd

>  `/System/Library/PrivateFrameworks/CoreCDP.framework/cdpd`

```diff

-386.231.0.0.0
-  __TEXT.__text: 0x24c
-  __TEXT.__auth_stubs: 0xe0
+386.231.1.0.0
+  __TEXT.__text: 0x214
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0xd
   __TEXT.__objc_methname: 0x5e
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x78
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__auth_got: 0x70
+  __DATA_CONST.__got: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2
-  Symbols:   27
+  Symbols:   25
   CStrings:  8
 
Symbols:
- _OBJC_CLASS_$_CDPDUnlockObserver
- _objc_release_x23

```

#### imagent

>  `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

-1402.300.181.2.20
+1402.300.181.2.21
   __TEXT.__text: 0x47424
   __TEXT.__auth_stubs: 0x1550
   __TEXT.__objc_stubs: 0x5800

   __TEXT.__eh_frame: 0x500
   __DATA_CONST.__auth_got: 0xab8
   __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__auth_ptr: 0x2d0
+  __DATA_CONST.__auth_ptr: 0x2d8
   __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x100
CStrings:
+ "16:36:36"
+ "Dec 18 2024"
- "19:20:06"
- "Dec  6 2024"

```

#### securityd

>  `/usr/libexec/securityd`

```diff

-61439.62.1.0.0
-  __TEXT.__text: 0x23075c
+61439.62.2.0.0
+  __TEXT.__text: 0x230754
   __TEXT.__auth_stubs: 0x38c0
   __TEXT.__objc_stubs: 0x1a4c0
   __TEXT.__objc_methlist: 0x128e4

```


</details>

## DSC

### WebKit

| iOS               | Version        |
| :---------------- | :------------- |
| 18.2 *(22C152)*   | 620.1.16.10.11 |
| 18.2.1 *(22C161)* | 620.1.16.10.11 |

### Dylibs

#### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

#### QuickLook

>  `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-969.3.4.0.0
+969.3.5.0.0
   __TEXT.__text: 0xd31c8
   __TEXT.__auth_stubs: 0x2420
   __TEXT.__delay_stubs: 0x2c

   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x1228
-  __AUTH_CONST.__auth_ptr: 0x640
+  __AUTH_CONST.__auth_ptr: 0x600
   __AUTH_CONST.__const: 0x3048
   __AUTH_CONST.__cfstring: 0x2f80
   __AUTH_CONST.__objc_const: 0x15420

```

#### ChatKit

>  `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1402.300.181.2.20
-  __TEXT.__text: 0x8977e8
+1402.300.181.2.21
+  __TEXT.__text: 0x897694
   __TEXT.__auth_stubs: 0x8b80
   __TEXT.__delay_helper: 0x190
   __TEXT.__objc_methlist: 0x5c760
   __TEXT.__const: 0x1b674
-  __TEXT.__gcc_except_tab: 0x26184
+  __TEXT.__gcc_except_tab: 0x2613c
   __TEXT.__cstring: 0x41909
   __TEXT.__oslogstring: 0x3d96b
   __TEXT.__dlopen_cstrs: 0xa79

   __TEXT.__swift5_types: 0x9c8
   __TEXT.__swift5_protos: 0x80
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x24728
+  __TEXT.__unwind_info: 0x24720
   __TEXT.__eh_frame: 0x62f0
   __TEXT.__objc_classname: 0xb197
   __TEXT.__objc_methname: 0xfa3d5

   __DATA_CONST.__objc_superrefs: 0x19a0
   __DATA_CONST.__objc_arraydata: 0x1040
   __AUTH_CONST.__auth_got: 0x45d0
-  __AUTH_CONST.__auth_ptr: 0x33d8
+  __AUTH_CONST.__auth_ptr: 0x3380
   __AUTH_CONST.__const: 0x264f0
   __AUTH_CONST.__cfstring: 0x24300
   __AUTH_CONST.__objc_const: 0xa43c8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 53368
-  Symbols:   41113
+  Functions: 53367
+  Symbols:   41112
   CStrings:  50942
 

```

#### CoreCDPInternal

>  `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-386.231.0.0.0
-  __TEXT.__text: 0x8ec04
-  __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__objc_methlist: 0x44cc
-  __TEXT.__const: 0x730
-  __TEXT.__oslogstring: 0x13768
-  __TEXT.__cstring: 0x7705
+386.231.1.0.0
+  __TEXT.__text: 0x8dacc
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_methlist: 0x4474
+  __TEXT.__const: 0x720
+  __TEXT.__oslogstring: 0x13538
+  __TEXT.__cstring: 0x7675
   __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x301

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__unwind_info: 0x1cb8
+  __TEXT.__unwind_info: 0x1c90
   __TEXT.__eh_frame: 0x8e0
-  __TEXT.__objc_classname: 0xc8c
-  __TEXT.__objc_methname: 0xeb7e
+  __TEXT.__objc_classname: 0xc79
+  __TEXT.__objc_methname: 0xeb56
   __TEXT.__objc_methtype: 0x28e1
   __TEXT.__objc_stubs: 0xbea0
-  __DATA_CONST.__got: 0x1008
+  __DATA_CONST.__got: 0x1000
   __DATA_CONST.__const: 0x2588
-  __DATA_CONST.__objc_classlist: 0x288
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x178
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3530
-  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_selrefs: 0x3520
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x8f8
+  __AUTH_CONST.__auth_got: 0x8a8
   __AUTH_CONST.__auth_ptr: 0x1d8
   __AUTH_CONST.__const: 0x9e8
   __AUTH_CONST.__cfstring: 0x4e60
-  __AUTH_CONST.__objc_const: 0x11af8
+  __AUTH_CONST.__objc_const: 0x116c8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1110
-  __AUTH.__data: 0x78
+  __AUTH.__objc_data: 0x10a0
+  __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x3a0
-  __DATA.__data: 0x1308
+  __DATA.__data: 0x1288
   __DATA.__bss: 0x840
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x920

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3027
-  Symbols:   3838
-  CStrings:  4738
+  Functions: 3015
+  Symbols:   3831
+  CStrings:  4720
 
Symbols:
- _MKBGetDeviceLockState
- _OBJC_CLASS_$_CDPDUnlockObserver
- _OBJC_METACLASS_$_CDPDUnlockObserver
- _swift_endAccess
- _swift_unknownObjectRelease_n
- _swift_unknownObjectRetain_n
CStrings:
- "%{public}s device is not unlocked. Found lock state %{public}d."
- "%{public}s ignoring event %{public}s because device is not unlocked"
- "%{public}s ignoring notification event %{public}s"
- "%{public}s received a nil eventName"
- "%{public}s recognizes event name %{public}s as unlocked. Notifying %{public}ld listeners."
- "CDPDUnlockListener"
- "CDPDUnlockObserver"
- "Fetched manatee status after device unlock with altDSID=%@, isPrimaryAccount=%{BOOL}d"
- "Fetching manatee status after device unlock with altDSID=%@, isPrimaryAccount=%{BOOL}d"
- "Notifying listener %{public}s"
- "com.apple.mobile.keybagd.lock_status"
- "currentDeviceIsUnlocked"
- "deviceDidUnlock"

```

#### IMSharedUtilities

>  `/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities`

```diff

-1402.300.181.2.20
+1402.300.181.2.21
   __TEXT.__text: 0x27d2e4
   __TEXT.__auth_stubs: 0x3e40
   __TEXT.__objc_methlist: 0x109d8

   __DATA_CONST.__objc_superrefs: 0x530
   __DATA_CONST.__objc_arraydata: 0x6b0
   __AUTH_CONST.__auth_got: 0x1f30
-  __AUTH_CONST.__auth_ptr: 0x1380
+  __AUTH_CONST.__auth_ptr: 0x1398
   __AUTH_CONST.__const: 0xd310
   __AUTH_CONST.__cfstring: 0x19ce0
   __AUTH_CONST.__objc_const: 0x20f80

```

#### MessagesCloudSync

>  `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-1402.300.181.2.20
+1402.300.181.2.21
   __TEXT.__text: 0x111e78
   __TEXT.__auth_stubs: 0x1f20
   __TEXT.__objc_methlist: 0x610

   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0xf98
-  __AUTH_CONST.__auth_ptr: 0xa90
+  __AUTH_CONST.__auth_ptr: 0xaf8
   __AUTH_CONST.__const: 0x8678
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x2db8

```

#### MessagesSettingsUI

>  `/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI`

```diff

-1402.300.181.2.20
+1402.300.181.2.21
   __TEXT.__text: 0x2e594
   __TEXT.__auth_stubs: 0x1200
   __TEXT.__objc_methlist: 0x11d8

   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x910
-  __AUTH_CONST.__auth_ptr: 0x560
+  __AUTH_CONST.__auth_ptr: 0x578
   __AUTH_CONST.__const: 0xd70
   __AUTH_CONST.__cfstring: 0x15c0
   __AUTH_CONST.__objc_const: 0x3ab8

```

#### MessagesSupport

>  `/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport`

```diff

-1402.300.181.2.20
+1402.300.181.2.21
   __TEXT.__text: 0xca8c
   __TEXT.__auth_stubs: 0xba0
   __TEXT.__objc_methlist: 0x5c4

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH_CONST.__auth_ptr: 0x290
+  __AUTH_CONST.__auth_ptr: 0x298
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x1350

```

#### SettingsFoundation

>  `/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation`

```diff

-1080.2.3.0.0
-  __TEXT.__text: 0x10ce0
+1080.2.6.0.0
+  __TEXT.__text: 0x10d30
   __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_methlist: 0x604
   __TEXT.__const: 0x7f8
-  __TEXT.__cstring: 0x199b
+  __TEXT.__cstring: 0x19a7
   __TEXT.__ustring: 0x78
   __TEXT.__oslogstring: 0x158c
   __TEXT.__gcc_except_tab: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x890
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0x3c0
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x2040
+  __AUTH_CONST.__cfstring: 0x20c0
   __AUTH_CONST.__objc_const: 0x8b0
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x48
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x28

   - /usr/lib/libobjc.A.dylib
   Functions: 286
   Symbols:   521
-  CStrings:  720
+  CStrings:  724
 
CStrings:
+ "CI"
+ "LL"
+ "LZ"
+ "VC"

```


</details>

## EOF
