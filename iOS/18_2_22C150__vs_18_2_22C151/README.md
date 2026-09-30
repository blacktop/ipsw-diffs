# 18.2 (22C150) .vs 18.2 (22C151)

## IPSWs

- `iPhone17,1_18.2_22C150_Restore.ipsw`
- `iPhone17,1_18.2_22C151_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.2 *(22C150)* | 24.2.0 | 11215.62.3~1 | Thu, 14Nov2024 22:55:26 PST |
| 18.2 *(22C151)* | 24.2.0 | 11215.62.3~1 | Thu, 14Nov2024 22:55:26 PST |

## MachO

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### SearchIndexer

>  `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3826.300.87.2.16
-  __TEXT.__text: 0x5da594
+3826.300.87.2.17
+  __TEXT.__text: 0x5daf8c
   __TEXT.__auth_stubs: 0x4390
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x198
   __TEXT.__cstring: 0x8e89
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0x42e90
-  __TEXT.__swift5_typeref: 0xe1c3
+  __TEXT.__swift5_typeref: 0xe1c9
   __TEXT.__swift5_capture: 0x7ecc
   __TEXT.__constg_swiftt: 0xb8b4
-  __TEXT.__swift5_reflstr: 0xd439
-  __TEXT.__swift5_fieldmd: 0x1203c
+  __TEXT.__swift5_reflstr: 0xd469
+  __TEXT.__swift5_fieldmd: 0x12048
   __TEXT.__swift5_proto: 0x2388
   __TEXT.__swift5_types: 0x1424
   __TEXT.__swift5_assocty: 0x1620

   __TEXT.__objc_methname: 0x174f
   __TEXT.__objc_methtype: 0x3e5
   __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__unwind_info: 0x13020
-  __TEXT.__eh_frame: 0x19398
+  __TEXT.__unwind_info: 0x13058
+  __TEXT.__eh_frame: 0x193a0
   __DATA_CONST.__auth_got: 0x21d8
   __DATA_CONST.__got: 0xb40
   __DATA_CONST.__auth_ptr: 0x3058

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 29322
+  Functions: 29328
   Symbols:   446
   CStrings:  2980


```

#### MobileMail

>  `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

-3826.300.87.2.16
+3826.300.87.2.17
   __TEXT.__text: 0x459e50
   __TEXT.__auth_stubs: 0x6120
   __TEXT.__objc_stubs: 0x405c0

   __TEXT.__eh_frame: 0x28d8
   __DATA_CONST.__auth_got: 0x30a0
   __DATA_CONST.__got: 0x3740
-  __DATA_CONST.__auth_ptr: 0x1eb8
+  __DATA_CONST.__auth_ptr: 0x1ec8
   __DATA_CONST.__const: 0x15490
   __DATA_CONST.__cfstring: 0xe4e0
   __DATA_CONST.__objc_classlist: 0xdf8

```

#### MailWidgetExtension

>  `/private/var/staged_system_apps/MobileMail.app/PlugIns/MailWidgetExtension.appex/MailWidgetExtension`

```diff

-3826.300.87.2.16
+3826.300.87.2.17
   __TEXT.__text: 0x864c0
   __TEXT.__auth_stubs: 0x1710
   __TEXT.__objc_methlist: 0x3dc

   __TEXT.__eh_frame: 0x3ac
   __DATA_CONST.__auth_got: 0xb88
   __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__auth_ptr: 0x640
+  __DATA_CONST.__auth_ptr: 0x638
   __DATA_CONST.__const: 0x2fa0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.2 *(22C150)* | 620.1.16.10.11 |
| 18.2 *(22C151)* | 620.1.16.10.11 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### Message

>  `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3826.300.87.2.16
-  __TEXT.__text: 0xb70ed4
+3826.300.87.2.17
+  __TEXT.__text: 0xb716bc
   __TEXT.__auth_stubs: 0x7de0
   __TEXT.__objc_methlist: 0x11a74
   __TEXT.__gcc_except_tab: 0x38664

   __TEXT.__cstring: 0x3019e
   __TEXT.__oslogstring: 0x23f20
   __TEXT.__ustring: 0x23c6
-  __TEXT.__swift5_typeref: 0x1228b
+  __TEXT.__swift5_typeref: 0x12291
   __TEXT.__swift5_capture: 0x30d04
   __TEXT.__constg_swiftt: 0xd620
   __TEXT.__swift5_builtin: 0xd98
-  __TEXT.__swift5_reflstr: 0xe8a9
-  __TEXT.__swift5_fieldmd: 0x146ac
+  __TEXT.__swift5_reflstr: 0xe8d9
+  __TEXT.__swift5_fieldmd: 0x146b8
   __TEXT.__swift5_assocty: 0x1b10
   __TEXT.__swift5_proto: 0x2780
   __TEXT.__swift5_types: 0x176c
   __TEXT.__swift5_protos: 0x74
   __TEXT.__swift5_mpenum: 0x7e8
-  __TEXT.__unwind_info: 0x238b8
-  __TEXT.__eh_frame: 0x1e5a0
+  __TEXT.__unwind_info: 0x238f8
+  __TEXT.__eh_frame: 0x1e5a8
   __TEXT.__objc_classname: 0x2a4e
   __TEXT.__objc_methname: 0x2e45a
   __TEXT.__objc_methtype: 0x67c4

   __DATA_CONST.__objc_superrefs: 0x680
   __DATA_CONST.__objc_arraydata: 0xf58
   __AUTH_CONST.__auth_got: 0x3f08
-  __AUTH_CONST.__auth_ptr: 0x3180
+  __AUTH_CONST.__auth_ptr: 0x3158
   __AUTH_CONST.__const: 0xa4aa0
   __AUTH_CONST.__cfstring: 0x184e0
   __AUTH_CONST.__objc_const: 0x26e50

   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x5298
-  __AUTH.__data: 0xaf90
+  __AUTH.__data: 0xaf70
   __DATA.__objc_ivar: 0x13a0
-  __DATA.__data: 0xe828
+  __DATA.__data: 0xe878
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x4e118
   __DATA.__common: 0xf40

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 54764
+  Functions: 54769
   Symbols:   13896
   CStrings:  17246


```


</details>

## EOF
