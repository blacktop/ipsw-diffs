# 18.6 (22G84) .vs 18.6 (22G86)

## IPSWs

- `iPhone17,1_18.6_22G84_Restore.ipsw`
- `iPhone17,1_18.6_22G86_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.6 *(22G84)* | 24.6.0 | 11417.140.69~16 | Tue, 15Jul2025 21:54:57 PDT |
| 18.6 *(22G86)* | 24.6.0 | 11417.140.69~16 | Tue, 15Jul2025 21:54:57 PDT |

## MachO

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### AppDistributionLaunchAngel

>  `/Applications/AppDistributionLaunchAngel.app/AppDistributionLaunchAngel`

```diff

-2.5.15.0.0
-  __TEXT.__text: 0x514ac
-  __TEXT.__auth_stubs: 0x2210
+2.5.16.0.0
+  __TEXT.__text: 0x516dc
+  __TEXT.__auth_stubs: 0x2220
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x108c
   __TEXT.__const: 0x1838
-  __TEXT.__cstring: 0x2a9d
+  __TEXT.__cstring: 0x2abd
   __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__objc_methname: 0x3159
   __TEXT.__oslogstring: 0xe0b

   __TEXT.__swift5_protos: 0x8
   __TEXT.__unwind_info: 0x1228
   __TEXT.__eh_frame: 0x2c10
-  __DATA_CONST.__auth_got: 0x1118
+  __DATA_CONST.__auth_got: 0x1120
   __DATA_CONST.__got: 0x640
-  __DATA_CONST.__auth_ptr: 0x568
+  __DATA_CONST.__auth_ptr: 0x570
   __DATA_CONST.__const: 0x1810
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x150

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 2A03425C-BD4E-3911-9EEC-8E324CE0D14C
+  UUID: 0E40E057-D7DE-3834-B42A-8BD536C79AED
   Functions: 1286
-  Symbols:   940
-  CStrings:  924
+  Symbols:   941
+  CStrings:  925
 
Symbols:
+ _$s14MarketplaceKit19InstallSheetContextV6SourceO011DistributorE0V2idSSvg
Functions:
~ sub_100036d78 : 1752 -> 2312
CStrings:
+ "Unhandled distribution source"

```

#### AppInstallationSettings

>  `/System/Library/PreferenceBundles/AppInstallationSettings.bundle/AppInstallationSettings`

```diff

-2.5.15.0.0
+2.5.16.0.0
   __TEXT.__text: 0x1c0bc
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x94

   __TEXT.__eh_frame: 0x808
   __DATA_CONST.__auth_got: 0x7e0
   __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__auth_ptr: 0x358
+  __DATA_CONST.__auth_ptr: 0x368
   __DATA_CONST.__const: 0x950
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 866400C5-07E8-3F4C-B275-C0E83C2AD6D0
+  UUID: DE7094C6-E347-319B-AA01-E1F767861A5A
   Functions: 465
   Symbols:   178
   CStrings:  149

```

#### MobileMail

>  `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

-3826.700.81.0.0
-  __TEXT.__text: 0x45bb44
-  __TEXT.__auth_stubs: 0x5f70
-  __TEXT.__objc_stubs: 0x40c20
-  __TEXT.__objc_methlist: 0x24c0c
-  __TEXT.__gcc_except_tab: 0x52664
-  __TEXT.__objc_methname: 0x5fdd9
+3826.700.81.2.1
+  __TEXT.__text: 0x45d184
+  __TEXT.__auth_stubs: 0x5f90
+  __TEXT.__objc_stubs: 0x40c40
+  __TEXT.__objc_methlist: 0x24c04
+  __TEXT.__gcc_except_tab: 0x52620
+  __TEXT.__objc_methname: 0x5fe0f
   __TEXT.__cstring: 0x1cd4d
   __TEXT.__objc_classname: 0x4f81
   __TEXT.__objc_methtype: 0x114f8
   __TEXT.__const: 0xed50
-  __TEXT.__oslogstring: 0x129f3
+  __TEXT.__oslogstring: 0x12a93
   __TEXT.__ustring: 0x896
-  __TEXT.__swift5_typeref: 0x954a
-  __TEXT.__swift5_capture: 0x33c8
-  __TEXT.__swift5_reflstr: 0x2d14
+  __TEXT.__swift5_typeref: 0x957c
+  __TEXT.__swift5_capture: 0x3478
+  __TEXT.__swift5_reflstr: 0x2d24
   __TEXT.__swift5_assocty: 0x13f0
   __TEXT.__constg_swiftt: 0x3448
   __TEXT.__swift5_fieldmd: 0x2618

   __TEXT.__swift_as_ret: 0x308
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x17688
+  __TEXT.__unwind_info: 0x17658
   __TEXT.__eh_frame: 0x2978
-  __DATA_CONST.__auth_got: 0x2fc8
-  __DATA_CONST.__got: 0x3790
-  __DATA_CONST.__auth_ptr: 0x1e78
-  __DATA_CONST.__const: 0x15770
+  __DATA_CONST.__auth_got: 0x2fd8
+  __DATA_CONST.__got: 0x3798
+  __DATA_CONST.__auth_ptr: 0x1cc0
+  __DATA_CONST.__const: 0x158a8
   __DATA_CONST.__cfstring: 0xe620
   __DATA_CONST.__objc_classlist: 0xdf8
   __DATA_CONST.__objc_catlist: 0xf0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 758C9067-51DA-3DB3-B678-48D72C3F0D70
-  Functions: 20908
-  Symbols:   4049
-  CStrings:  23058
+  UUID: 5FA9D5CD-FCE6-3C44-97E4-BDB9024F4057
+  Functions: 20914
+  Symbols:   4052
+  CStrings:  23061
 
Symbols:
+ _$sSh6insertySb8inserted_x17memberAfterInserttxnF
+ _$sSh9formUnionyyqd__n7ElementQyd__RszSTRd__lF
+ _$sShyxGs23CustomStringConvertiblesMc
CStrings:
+ "<%@: %p> Unexpectedly received exclusion mailboxes: %@ for smart mailbox: %@"
+ "Unexpectedly received exclusion mailboxes: %s for smart mailbox: %@"
+ "_mailboxObjectIDsOfInterest"
+ "mailboxesIfAvailableForObjectIDs:"
+ "setMailboxesOfInterest:mailboxTypeResolver:"
- "_mailboxesOfInterest"
- "setMailboxesOfInterest:"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.6 *(22G84)* | iBoot-11881.140.96 |
| 18.6 *(22G86)* | iBoot-11881.140.96 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.6 *(22G84)* | 621.3.11.10.3 |
| 18.6 *(22G86)* | 621.3.11.10.3 |

## EOF
