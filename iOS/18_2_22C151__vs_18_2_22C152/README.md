# 18.2 (22C151) .vs 18.2 (22C152)

## IPSWs

- `iPhone17,1_18.2_22C151_Restore.ipsw`
- `iPhone17,1_18.2_22C152_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.2 *(22C151)* | 24.2.0 | 11215.62.3~1 | Thu, 14Nov2024 22:55:26 PST |
| 18.2 *(22C152)* | 24.2.0 | 11215.62.3~1 | Thu, 14Nov2024 22:55:26 PST |

## MachO

### ⬆️ Updated (4)

<details>
  <summary><i>View Updated</i></summary>

#### iMessage

>  `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1402.300.181.2.19
-  __TEXT.__text: 0x91e28
+1402.300.181.2.20
+  __TEXT.__text: 0x91d10
   __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_stubs: 0xb1a0
+  __TEXT.__objc_stubs: 0xb180
   __TEXT.__objc_methlist: 0x2164
   __TEXT.__const: 0x37e
   __TEXT.__gcc_except_tab: 0xa668
   __TEXT.__cstring: 0x2fad
   __TEXT.__oslogstring: 0x13ea6
   __TEXT.__objc_classname: 0x4e2
-  __TEXT.__objc_methname: 0x10308
+  __TEXT.__objc_methname: 0x102f2
   __TEXT.__objc_methtype: 0x2779
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x168

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d98
+  __TEXT.__unwind_info: 0x1d90
   __TEXT.__eh_frame: 0x2b8
   __DATA_CONST.__auth_got: 0x9d0
   __DATA_CONST.__got: 0xda0

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x3570
-  __DATA.__objc_selrefs: 0x31d0
+  __DATA.__objc_selrefs: 0x31c8
   __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x380
   __DATA.__data: 0x790

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1176
+  Functions: 1175
   Symbols:   778
-  CStrings:  4159
+  CStrings:  4158

CStrings:
- "activeiMessageAliases"

```

#### imagent

>  `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

-1402.300.181.2.19
+1402.300.181.2.20
   __TEXT.__text: 0x47424
   __TEXT.__auth_stubs: 0x1550
   __TEXT.__objc_stubs: 0x5800

   __TEXT.__eh_frame: 0x500
   __DATA_CONST.__auth_got: 0xab8
   __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__auth_ptr: 0x2d8
+  __DATA_CONST.__auth_ptr: 0x2d0
   __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x100
CStrings:
+ "19:20:06"
+ "Dec  6 2024"
- "20:58:27"
- "Nov 21 2024"

```

#### MobileMail

>  `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

-3826.300.87.2.17
+3826.300.87.2.22
   __TEXT.__text: 0x459e50
   __TEXT.__auth_stubs: 0x6120
   __TEXT.__objc_stubs: 0x405c0

   __TEXT.__eh_frame: 0x28d8
   __DATA_CONST.__auth_got: 0x30a0
   __DATA_CONST.__got: 0x3740
-  __DATA_CONST.__auth_ptr: 0x1ec8
+  __DATA_CONST.__auth_ptr: 0x1c98
   __DATA_CONST.__const: 0x15490
   __DATA_CONST.__cfstring: 0xe4e0
   __DATA_CONST.__objc_classlist: 0xdf8

```

#### MailWidgetExtension

>  `/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension`

```diff

-3826.300.87.2.17
+3826.300.87.2.22
   __TEXT.__text: 0x864c0
   __TEXT.__auth_stubs: 0x1710
   __TEXT.__objc_methlist: 0x3dc

   __TEXT.__eh_frame: 0x3ac
   __DATA_CONST.__auth_got: 0xb88
   __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__auth_ptr: 0x638
+  __DATA_CONST.__auth_ptr: 0x660
   __DATA_CONST.__const: 0x2fa0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.2 *(22C151)* | 620.1.16.10.11 |
| 18.2 *(22C152)* | 620.1.16.10.11 |

### Dylibs

#### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### ChatKit

>  `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1402.300.181.2.19
+1402.300.181.2.20
   __TEXT.__text: 0x8977e8
   __TEXT.__auth_stubs: 0x8b80
   __TEXT.__delay_helper: 0x190

   __DATA_CONST.__objc_superrefs: 0x19a0
   __DATA_CONST.__objc_arraydata: 0x1040
   __AUTH_CONST.__auth_got: 0x45d0
-  __AUTH_CONST.__auth_ptr: 0x3798
+  __AUTH_CONST.__auth_ptr: 0x33d8
   __AUTH_CONST.__const: 0x264f0
   __AUTH_CONST.__cfstring: 0x24300
   __AUTH_CONST.__objc_const: 0xa43c8

```

#### EmailDaemon

>  `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3826.300.87.2.17
-  __TEXT.__text: 0x2422b8
+3826.300.87.2.22
+  __TEXT.__text: 0x2423a0
   __TEXT.__auth_stubs: 0x2400
   __TEXT.__objc_methlist: 0x12f54
-  __TEXT.__gcc_except_tab: 0x49b6c
+  __TEXT.__gcc_except_tab: 0x49b80
   __TEXT.__const: 0x1d08
   __TEXT.__cstring: 0x201e7
   __TEXT.__oslogstring: 0x17bc6

   __TEXT.__swift5_types: 0xbc
   __TEXT.__swift5_capture: 0x128
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xfe88
+  __TEXT.__unwind_info: 0xfe98
   __TEXT.__eh_frame: 0x860
   __TEXT.__objc_classname: 0x2d18
   __TEXT.__objc_methname: 0x382e3

   __DATA_CONST.__objc_superrefs: 0x670
   __DATA_CONST.__objc_arraydata: 0x680
   __AUTH_CONST.__auth_got: 0x1210
-  __AUTH_CONST.__auth_ptr: 0x340
+  __AUTH_CONST.__auth_ptr: 0x338
   __AUTH_CONST.__const: 0x3ca8
   __AUTH_CONST.__cfstring: 0x10860
   __AUTH_CONST.__objc_const: 0x26c38

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10368
-  Symbols:   11218
+  Functions: 10369
+  Symbols:   11219
   CStrings:  14107


```

#### IMDaemonCore

>  `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1402.300.181.2.19
-  __TEXT.__text: 0x288e24
+1402.300.181.2.20
+  __TEXT.__text: 0x288a3c
   __TEXT.__auth_stubs: 0x43b0
-  __TEXT.__objc_methlist: 0x1280c
+  __TEXT.__objc_methlist: 0x127fc
   __TEXT.__const: 0x2fc8
-  __TEXT.__cstring: 0x12aa1
-  __TEXT.__gcc_except_tab: 0x26a44
-  __TEXT.__oslogstring: 0x44e17
+  __TEXT.__cstring: 0x12a91
+  __TEXT.__gcc_except_tab: 0x269d8
+  __TEXT.__oslogstring: 0x44dd7
   __TEXT.__ustring: 0x37a
   __TEXT.__dlopen_cstrs: 0x128
   __TEXT.__constg_swiftt: 0x108c

   __TEXT.__swift5_proto: 0x1e8
   __TEXT.__swift5_types: 0x114
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0xabe8
+  __TEXT.__unwind_info: 0xabe0
   __TEXT.__eh_frame: 0x1fe8
-  __TEXT.__objc_classname: 0x2dfc
-  __TEXT.__objc_methname: 0x4502f
+  __TEXT.__objc_classname: 0x2deb
+  __TEXT.__objc_methname: 0x45019
   __TEXT.__objc_methtype: 0x914d
   __TEXT.__objc_stubs: 0x2c100
   __DATA_CONST.__got: 0x2a78

   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x600
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd278
+  __DATA_CONST.__objc_selrefs: 0xd270
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x4f0
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x21e8
-  __AUTH_CONST.__auth_ptr: 0x9c8
+  __AUTH_CONST.__auth_ptr: 0x9d0
   __AUTH_CONST.__const: 0x54d8
-  __AUTH_CONST.__cfstring: 0xe160
+  __AUTH_CONST.__cfstring: 0xe120
   __AUTH_CONST.__objc_const: 0x21cb0
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x120

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9848
+  Functions: 9847
   Symbols:   2677
-  CStrings:  17629
+  CStrings:  17623

CStrings:
+ "Fixing chat join state"
- ", "
- "<nil>"
- "Could not find a service for string: %@"
- "Fixed chat join states for chats with guids: %@"
- "GroupConvergence"
- "IMAccoutController"
- "activeiMessageAliases"

```

#### IMSharedUtilities

>  `/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities`

```diff

-1402.300.181.2.19
+1402.300.181.2.20
   __TEXT.__text: 0x27d2e4
   __TEXT.__auth_stubs: 0x3e40
   __TEXT.__objc_methlist: 0x109d8

   __DATA_CONST.__objc_superrefs: 0x530
   __DATA_CONST.__objc_arraydata: 0x6b0
   __AUTH_CONST.__auth_got: 0x1f30
-  __AUTH_CONST.__auth_ptr: 0x13d8
+  __AUTH_CONST.__auth_ptr: 0x1380
   __AUTH_CONST.__const: 0xd310
   __AUTH_CONST.__cfstring: 0x19ce0
   __AUTH_CONST.__objc_const: 0x20f80

```

#### MessagesCloudSync

>  `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-1402.300.181.2.19
+1402.300.181.2.20
   __TEXT.__text: 0x111e78
   __TEXT.__auth_stubs: 0x1f20
   __TEXT.__objc_methlist: 0x610

   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0xf98
-  __AUTH_CONST.__auth_ptr: 0xaa0
+  __AUTH_CONST.__auth_ptr: 0xa90
   __AUTH_CONST.__const: 0x8678
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x2db8

```

#### MessagesSettingsUI

>  `/System/Library/PrivateFrameworks/MessagesSettingsUI.framework/MessagesSettingsUI`

```diff

-1402.300.181.2.19
+1402.300.181.2.20
   __TEXT.__text: 0x2e594
   __TEXT.__auth_stubs: 0x1200
   __TEXT.__objc_methlist: 0x11d8

   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x910
-  __AUTH_CONST.__auth_ptr: 0x578
+  __AUTH_CONST.__auth_ptr: 0x560
   __AUTH_CONST.__const: 0xd70
   __AUTH_CONST.__cfstring: 0x15c0
   __AUTH_CONST.__objc_const: 0x3ab8

```

#### MessagesSupport

>  `/System/Library/PrivateFrameworks/MessagesSupport.framework/MessagesSupport`

```diff

-1402.300.181.2.19
+1402.300.181.2.20
   __TEXT.__text: 0xca8c
   __TEXT.__auth_stubs: 0xba0
   __TEXT.__objc_methlist: 0x5c4

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x5d8
-  __AUTH_CONST.__auth_ptr: 0x298
+  __AUTH_CONST.__auth_ptr: 0x290
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x1350

```


</details>

## EOF
