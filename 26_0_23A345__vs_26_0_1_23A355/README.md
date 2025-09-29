# 26.0 (23A345) .vs 26.0.1 (23A355)

## IPSWs

- `iPhone18,1_26.0_23A345_Restore.ipsw`
- `iPhone18,1_26.0.1_23A355_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.0 *(23A345)* | 25.0.0 | 12377.2.8~1 | Tue, 26Aug2025 20:30:19 PDT |
| 26.0.1 *(23A355)* | 25.0.0 | 12377.2.9~1 | Thu, 25Sep2025 15:05:47 PDT |

### Kexts

### ⬆️ Updated (3)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.AppleMobileFileIntegrity

>  `com.apple.driver.AppleMobileFileIntegrity`

```diff

-1045.2.1.0.0
-  __TEXT.__cstring: 0xbca3
+1045.2.2.0.0
+  __TEXT.__cstring: 0xbcd8
   __TEXT.__const: 0x1570
   __TEXT.__os_log: 0x32d
   __TEXT_EXEC.__text: 0x28780
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x6f2
+  __DATA.__data: 0x702
   __DATA.__common: 0xb0
   __DATA.__bss: 0x81
   __DATA_CONST.__auth_got: 0x7f8

   __DATA_CONST.__kalloc_type: 0xf00
   __DATA_CONST.__kalloc_var: 0x1400
   __DATA_CONST.__assert: 0xf0
-  UUID: 13BD7B69-63FE-37A7-8F78-AABE2B1FAB73
+  UUID: C146C590-FDD7-3958-8244-F3ED1F990CD2
   Functions: 888
   Symbols:   0
-  CStrings:  1204
+  CStrings:  1206
 
CStrings:
+ "14:46:18"
+ "Sep 25 2025"
+ "com.apple.TelephonyUtilities"
+ "com.apple.coretelephony"
- "20:15:38"
- "Aug 26 2025"

```

#### com.apple.driver.IOPAudioVoiceTriggerDevice

>  `com.apple.driver.IOPAudioVoiceTriggerDevice`

```diff

 500.14.0.0.0
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x2d80
+  __TEXT.__cstring: 0x2d89
   __TEXT.__os_log: 0x1726
   __TEXT_EXEC.__text: 0xb108
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1750
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 1CCC882C-A8A3-3FE6-8635-CDFE897118B1
+  UUID: B4E806A8-E409-3A41-83C4-21EE3218CD04
   Functions: 260
   Symbols:   0
-  CStrings:  235
+  CStrings:  236
 
CStrings:
+ "14:59:06"
+ "14:59:07"
+ "Sep 25 2025"
- "20:27:28"
- "Aug 26 2025"

```

#### com.apple.security.sandbox

>  `com.apple.security.sandbox`

```diff

 2680.0.50.0.0
   __TEXT.__os_log: 0x225c
-  __TEXT.__const: 0x1d32a9
+  __TEXT.__const: 0x1d32b9
   __TEXT.__cstring: 0x7137
   __TEXT_EXEC.__text: 0x37a4c
   __TEXT_EXEC.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x3810
   __DATA_CONST.__kalloc_type: 0xac0
   __DATA_CONST.__kalloc_var: 0x4b0
-  UUID: 20E68335-F842-3885-A360-C854A44199CF
+  UUID: CB54FC50-F6CE-3EA3-AA43-3E82AEE04119
   Functions: 657
   Symbols:   0
   CStrings:  1326

```


</details>

## MachO

### ⬆️ Updated (18)

<details>
  <summary><i>View Updated</i></summary>

#### Setup

>  `/Applications/Setup.app/Setup`

```diff

-5374.106.0.0.0
-  __TEXT.__text: 0x244140
+5374.107.0.0.0
+  __TEXT.__text: 0x244918
   __TEXT.__auth_stubs: 0x2660
-  __TEXT.__objc_stubs: 0x27f00
-  __TEXT.__objc_methlist: 0x1cfe0
+  __TEXT.__objc_stubs: 0x27fe0
+  __TEXT.__objc_methlist: 0x1d0c8
   __TEXT.__dlopen_cstrs: 0x1252
-  __TEXT.__cstring: 0x11c95
-  __TEXT.__const: 0x2298
+  __TEXT.__const: 0x22a8
+  __TEXT.__cstring: 0x11cd4
+  __TEXT.__objc_methname: 0x3ce3f
   __TEXT.__constg_swiftt: 0x2b24
   __TEXT.__swift5_typeref: 0x1cb4
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x15dc
+  __TEXT.__swift5_reflstr: 0x15cc
   __TEXT.__swift5_fieldmd: 0x12c4
+  __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_assocty: 0x168
+  __TEXT.__swift5_capture: 0xf7c
+  __TEXT.__oslogstring: 0x11d68
   __TEXT.__swift5_proto: 0xcc
   __TEXT.__swift5_types: 0x148
-  __TEXT.__objc_classname: 0x3dfe
-  __TEXT.__objc_methname: 0x3cc46
-  __TEXT.__objc_methtype: 0xb797
-  __TEXT.__swift5_capture: 0xf7c
-  __TEXT.__oslogstring: 0x11d17
+  __TEXT.__objc_classname: 0x3e4f
+  __TEXT.__objc_methtype: 0xb7c5
   __TEXT.__swift_as_entry: 0x118
   __TEXT.__swift_as_ret: 0xf8
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x57fc
   __TEXT.__ustring: 0x90
-  __TEXT.__unwind_info: 0x91a0
+  __TEXT.__unwind_info: 0x91e8
   __TEXT.__eh_frame: 0x29d0
   __DATA_CONST.__auth_got: 0x1348
-  __DATA_CONST.__got: 0x1ef0
+  __DATA_CONST.__got: 0x1ef8
   __DATA_CONST.__auth_ptr: 0x490
   __DATA_CONST.__const: 0x8070
-  __DATA_CONST.__cfstring: 0xb620
-  __DATA_CONST.__objc_classlist: 0xcc0
+  __DATA_CONST.__cfstring: 0xb660
+  __DATA_CONST.__objc_classlist: 0xcd0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x698
+  __DATA_CONST.__objc_protolist: 0x6a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1d0
-  __DATA_CONST.__objc_superrefs: 0x838
+  __DATA_CONST.__objc_superrefs: 0x840
   __DATA_CONST.__objc_intobj: 0x5b8
   __DATA_CONST.__objc_arraydata: 0x330
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x45640
-  __DATA.__objc_selrefs: 0xcb80
-  __DATA.__objc_ivar: 0x1d8c
-  __DATA.__objc_data: 0xac90
-  __DATA.__data: 0x5f28
+  __DATA.__objc_const: 0x458e8
+  __DATA.__objc_selrefs: 0xcbd8
+  __DATA.__objc_ivar: 0x1d94
+  __DATA.__objc_data: 0xad30
+  __DATA.__data: 0x5fd8
   __DATA.__bss: 0x1890
   __DATA.__common: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 01EC5B00-24A4-35DF-BF32-2725908AE722
-  Functions: 11560
+  UUID: 37D75E91-962B-3644-9787-A4E9C65D4B7D
+  Functions: 11574
   Symbols:   1511
-  CStrings:  16097
+  CStrings:  16126
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B-gfugBtAGJx97bWc7wC_8ngP4nAHMb2iEcdmZQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:407: assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~B-gfugBtAGJx97bWc7wC_8ngP4nAHMb2iEcdmZQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:426: assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~B-gfugBtAGJx97bWc7wC_8ngP4nAHMb2iEcdmZQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:434: assertion !empty() failed: back() called on an empty vector\n"
+ "@\"<BYCPUAssertion>\""
+ "@\"<BYCPUAssertion>\"16@0:8"
+ "BYCPUAssertion"
+ "BYCPUAssertionProvider"
+ "BYRBSCPUAssertion"
+ "BYRBSCPUAssertionProvider"
+ "Did acquire cpu assertion with success %d, error %@"
+ "Did invalidate cpu assertion"
+ "ForegroundRuntime"
+ "Sep 23 2025"
+ "Setup launch needs foreground runtime even when backgrounded"
+ "T@\"<BYCPUAssertion>\",&,N,V_cpuAssertion"
+ "T@\"RBSAssertion\",&,N,V_underlyingAssertion"
+ "TB,N,V_inMiniBuddyFromBreadcrumb"
+ "TB,N,V_inMiniBuddyFromPostDemoRestoreBreadcrumb"
+ "_cpuAssertion"
+ "_underlyingAssertion"
+ "acquireAssertion"
+ "cpuAssertion"
+ "inMiniBuddyFromBreadcrumb"
+ "inMiniBuddyFromPostDemoRestoreBreadcrumb"
+ "initWithUnderlyingAssertion:"
+ "invalidateAssertionIfNeededForStartUpCause:"
+ "setCpuAssertion:"
+ "setInMiniBuddyFromBreadcrumb:"
+ "setInMiniBuddyFromPostDemoRestoreBreadcrumb:"
+ "setUnderlyingAssertion:"
+ "underlyingAssertion"
+ "\xf0\xf0\xd1"
- "/AppleInternal/Library/BuildRoots/4~B7IpugD1kN5t7t5OjecjaEY-ZqavQNVPx-pk3qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:407: assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~B7IpugD1kN5t7t5OjecjaEY-ZqavQNVPx-pk3qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:426: assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~B7IpugD1kN5t7t5OjecjaEY-ZqavQNVPx-pk3qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:434: assertion !empty() failed: back() called on an empty vector\n"
- "Aug  8 2025"
- "\xf0\xf0\xe1"

```

#### contactsd

>  `/System/Library/Frameworks/Contacts.framework/Support/contactsd`

```diff

-3804.100.1.2.4
-  __TEXT.__text: 0x2ab24
+3804.100.1.2.5
+  __TEXT.__text: 0x2b58c
   __TEXT.__auth_stubs: 0x1410
   __TEXT.__objc_stubs: 0x3600
   __TEXT.__objc_methlist: 0x1b54
-  __TEXT.__const: 0x76c
+  __TEXT.__const: 0x784
   __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__objc_methname: 0x51c5
-  __TEXT.__cstring: 0x1872
+  __TEXT.__objc_methname: 0x52a8
+  __TEXT.__cstring: 0x1882
   __TEXT.__objc_classname: 0x3dc
   __TEXT.__objc_methtype: 0x1149
   __TEXT.__dlopen_cstrs: 0x116
-  __TEXT.__oslogstring: 0x21d9
+  __TEXT.__oslogstring: 0x2209
   __TEXT.__swift5_typeref: 0x4ad
-  __TEXT.__constg_swiftt: 0x49c
-  __TEXT.__swift5_reflstr: 0x294
-  __TEXT.__swift5_fieldmd: 0x268
+  __TEXT.__constg_swiftt: 0x4bc
+  __TEXT.__swift5_reflstr: 0x2a4
+  __TEXT.__swift5_fieldmd: 0x274
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_capture: 0xf4

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xb20
+  __TEXT.__unwind_info: 0xb28
   __TEXT.__eh_frame: 0x668
   __DATA_CONST.__auth_got: 0xa18
-  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__got: 0x508
   __DATA_CONST.__auth_ptr: 0x160
   __DATA_CONST.__const: 0x12f8
   __DATA_CONST.__cfstring: 0x840

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2fd0
-  __DATA.__objc_selrefs: 0x1458
+  __DATA.__objc_const: 0x2ff0
+  __DATA.__objc_selrefs: 0x1498
   __DATA.__objc_ivar: 0x130
   __DATA.__objc_data: 0xac8
-  __DATA.__data: 0xf58
+  __DATA.__data: 0xf88
   __DATA.__bss: 0x6e0
   __DATA.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4B140F04-A580-3135-9B79-18113377E1D0
-  Functions: 991
-  Symbols:   541
-  CStrings:  1371
+  UUID: F2733A2A-3969-3CE5-8739-26D306E96DA4
+  Functions: 992
+  Symbols:   542
+  CStrings:  1381
 
Symbols:
+ _OBJC_CLASS_$_NSUUID
CStrings:
+ "Fixed entry with duplicate identifier: %s"
+ "UUIDString"
+ "actionChannel"
+ "actionType"
+ "contactIdentifier"
+ "initWithIdentifier:name:value:label:propertyKey:actionType:bundleIdentifier:actionChannel:contactIdentifier:labeledValueIdentifier:"
+ "label"
+ "labeledValueIdentifier"
+ "needsSave"
+ "propertyKey"

```

#### BWVideoPIPOverlayNodeCoreImageArchive_bin.metallib

>  `/System/Library/PrivateFrameworks/CMCapture.framework/BWVideoPIPOverlayNodeCoreImageArchive_bin.metallib`

```diff

 
   __TEXT.__reflection: 0x1e90
-  __TEXT.__compute: 0xd590
+  __TEXT.__compute: 0xd5a0
   __TEXT.__descriptor: 0x8b0
   __TEXT.__metallib: 0x18d060
-  UUID: 7EF76FFD-9AA8-39F3-BE64-82C73F4A267C
+  UUID: B2B4252B-2041-3644-8AE2-3E2D4F6772A4
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### CMFSyncAgent

>  `/System/Library/PrivateFrameworks/CommunicationsFilter.framework/CMFSyncAgent`

```diff

-181.100.1.2.4
-  __TEXT.__text: 0x118bc
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_stubs: 0x880
+181.100.1.2.5
+  __TEXT.__text: 0x10650
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_stubs: 0x8a0
   __TEXT.__objc_methlist: 0x31c
-  __TEXT.__cstring: 0x815
-  __TEXT.__const: 0x4c6
-  __TEXT.__oslogstring: 0x962
-  __TEXT.__objc_methname: 0xc18
+  __TEXT.__cstring: 0x7a5
+  __TEXT.__const: 0x4d6
+  __TEXT.__oslogstring: 0x90f
+  __TEXT.__objc_methname: 0xc34
   __TEXT.__objc_classname: 0x5f
   __TEXT.__objc_methtype: 0x19c
   __TEXT.__constg_swiftt: 0x218
-  __TEXT.__swift5_typeref: 0x40f
-  __TEXT.__swift5_reflstr: 0x173
+  __TEXT.__swift5_typeref: 0x469
+  __TEXT.__swift5_reflstr: 0x183
   __TEXT.__swift5_fieldmd: 0x18c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x24
-  __TEXT.__swift5_capture: 0x20
+  __TEXT.__swift5_capture: 0xb8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x410
-  __TEXT.__eh_frame: 0x400
-  __DATA_CONST.__auth_got: 0x6f8
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__auth_ptr: 0xf8
-  __DATA_CONST.__const: 0x600
+  __TEXT.__unwind_info: 0x420
+  __TEXT.__eh_frame: 0x348
+  __DATA_CONST.__auth_got: 0x708
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__auth_ptr: 0x128
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x900
-  __DATA.__objc_selrefs: 0x428
+  __DATA.__objc_selrefs: 0x430
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x258
-  __DATA.__data: 0x4d8
+  __DATA.__data: 0x4b8
   __DATA.__bss: 0x350
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D8A5B843-81A6-3BE9-80E8-F50308C38070
-  Functions: 317
-  Symbols:   351
-  CStrings:  325
+  UUID: 3DF16F2A-1F98-329D-9D0D-BD4ADBA741C9
+  Functions: 321
+  Symbols:   356
+  CStrings:  321
 
Symbols:
+ _$sSa5countSivg
+ _$sSays10ArraySliceVyxGSnySiGcig
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$ss10ArraySliceVMa
+ _$ss10ArraySliceVMn
+ _$ss11AnyIteratorVMa
+ _$ss11AnyIteratorVMn
+ _$ss11AnyIteratorVyAByxGxSgyccfC
+ _$ss11AnyIteratorVyxGStsMc
+ _$ss11AnySequenceVyAByxGqd__ycc7ElementQyd__RszStRd__lufC
+ _$ss12_ArrayBufferV18_typeCheckSlowPathyySiF
+ _$ss12_IteratorBoxCMn
+ _$ss12_SequenceBoxCMn
+ _$ss18_CocoaArrayWrapperVys12_SliceBufferVyyXlGSnySiGcig
+ _$ss19_AnyIteratorBoxBaseC4nextxSgyFTj
+ _$ss21_ClosureBasedIteratorVMn
+ _$ss21_ClosureBasedSequenceVMn
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
- _$sSD11descriptionSSvg
- _$sSS6appendyySSF
- _$sSa11descriptionSSvg
- _$ss11_MergeErrorON
- _$ss11_MergeErrorOs0B0sWP
- _$ss11_StringGutsV4growyySiF
- _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_SSAHSus6UInt32VtF
- _$ss26DefaultStringInterpolationVN
- _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
- _swift_allocError
- _swift_release_n
- _swift_stdlib_isStackAllocationSafe
- _swift_unexpectedError
CStrings:
+ "@\"NSArray\"8@?0"
+ "@24@0:8@?16"
+ "Failed to convert the contacts fetchResult: %@"
+ "Generating cache from blocklist: %ld"
+ "arrayByAddingObjectsFromArray:"
+ "blocklistGetter"
+ "updateCacheWithBlocklist:"
- "Cache after clearing associated handles %s"
- "Contact fetch failed with the following error: %@ Returning nil"
- "Duplicate values for key: '"
- "Fatal error"
- "Generating cache from blocklist: %s"
- "No contact found for %s"
- "No contact found, returning nil"
- "Swift/Dictionary.swift"
- "Swift/NativeDictionary.swift"
- "blocklist"
- "generateCachesFromBlocklist:"

```

#### AppleVideoEncoder

>  `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

```diff

   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x22528
-  __TEXT.__cstring: 0x52375
+  __TEXT.__cstring: 0x5237e
   __TEXT.__gcc_except_tab: 0x720
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x8a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65A59C3B-E587-3267-A0DF-A4528136A5F8
+  UUID: 9DFB1C27-20EF-37EC-81BC-7C7845E5CC7F
   Functions: 1578
   Symbols:   511
-  CStrings:  6981
+  CStrings:  6982
 
CStrings:
+ "15:02:47"
+ "15:02:49"
+ "15:02:50"
+ "15:02:51"
+ "Sep 25 2025"
- "20:31:18"
- "20:31:19"
- "20:31:21"
- "Aug 26 2025"

```

#### binaryArchive.g18p

>  `/System/Library/VideoProcessors/ColourConstancyV1.bundle/binaryArchive.g18p`

```diff

 
   __TEXT.__metallib: 0x1fe0
   __TEXT.__descriptor: 0xdb0
-  __TEXT.__compute: 0x153b0
+  __TEXT.__compute: 0x153c0
   __TEXT.__reflection: 0x60b0
-  UUID: F2E7A480-C6F2-37EC-9599-4394F3E188D0
+  UUID: 51C94CAE-9F8E-316B-B54F-26D172CD65F5
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p_a0

>  `/System/Library/VideoProcessors/DepthProcessorV2.bundle/binaryArchive.g18p_a0`

```diff

 
   __TEXT.__metallib: 0x2420
   __TEXT.__descriptor: 0x1010
-  __TEXT.__compute: 0x19e50
+  __TEXT.__compute: 0x19e40
   __TEXT.__reflection: 0xb0d0
-  UUID: 54D70BC9-DFBD-39AA-98C2-66EAE93DF9AE
+  UUID: 6EAA503D-CCED-3221-90A6-E3DB9255460A
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p

>  `/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p`

```diff

   __TEXT.__metallib: 0x4380
   __TEXT.__descriptor: 0x280
   __TEXT.__fragment: 0xfa80
-  __TEXT.__vertex: 0x7b90
+  __TEXT.__vertex: 0x7480
   __TEXT.__reflection: 0x14f0
-  UUID: 56EAB4C0-93A9-3E1C-81CA-9A413ED8B620
+  UUID: 2E8752FA-3583-37A1-9BE6-85C011C52BA8
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p_a0

>  `/System/Library/VideoProcessors/MetalFilter.bundle/binaryArchive.g18p_a0`

```diff

   __TEXT.__metallib: 0x4380
   __TEXT.__descriptor: 0x280
   __TEXT.__fragment: 0xfa80
-  __TEXT.__vertex: 0x82a0
+  __TEXT.__vertex: 0x7b90
   __TEXT.__reflection: 0x14f0
-  UUID: 8F7DFF34-F090-3914-AE4E-11ADB50C64F6
+  UUID: 6C2A6351-3D97-3628-841D-0A8D298CC201
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p

>  `/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p`

```diff

   __TEXT.__metallib: 0x477e0
   __TEXT.__descriptor: 0x117e0
   __TEXT.__fragment: 0x1faf90
-  __TEXT.__compute: 0x32bd90
-  __TEXT.__vertex: 0x2f7e0
-  __TEXT.__reflection: 0x13efa0
-  UUID: 818DBDB2-8660-3638-882D-E78A33E70B83
+  __TEXT.__compute: 0x32b8c0
+  __TEXT.__vertex: 0x30190
+  __TEXT.__reflection: 0x13f010
+  UUID: E50920C2-7944-3A45-8C37-DA49C1096039
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p_a0

>  `/System/Library/VideoProcessors/NRFV4.bundle/binaryArchive.g18p_a0`

```diff

   __TEXT.__metallib: 0x477e0
   __TEXT.__descriptor: 0x117e0
   __TEXT.__fragment: 0x1faf90
-  __TEXT.__compute: 0x32bd90
-  __TEXT.__vertex: 0x2e480
-  __TEXT.__reflection: 0x13efa0
-  UUID: C0EC9F49-1553-3597-BA3A-8323E67EB5B7
+  __TEXT.__compute: 0x32c220
+  __TEXT.__vertex: 0x2fd10
+  __TEXT.__reflection: 0x13f010
+  UUID: 4B02137A-057A-381B-A28D-C8F303739E6C
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p_a0

>  `/System/Library/VideoProcessors/SuperResolutionV2.bundle/binaryArchive.g18p_a0`

```diff

 
   __TEXT.__metallib: 0x2510
   __TEXT.__descriptor: 0x18a0
-  __TEXT.__compute: 0x20e30
+  __TEXT.__compute: 0x20e20
   __TEXT.__reflection: 0x96e0
-  UUID: 6130075B-0431-3D0D-87B7-12A90679ED95
+  UUID: A3A10691-B919-365D-A7D2-0C0C6C62BF9F
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p

>  `/System/Library/VideoProcessors/VideoDeghostingV3.bundle/binaryArchive.g18p`

```diff

 
   __TEXT.__metallib: 0x2170
   __TEXT.__descriptor: 0x15f0
-  __TEXT.__compute: 0x35610
+  __TEXT.__compute: 0x35600
   __TEXT.__reflection: 0x46e60
-  UUID: 9D3447A8-A2AC-3FCC-8B80-1E07FBEF5E5F
+  UUID: A0D2B740-00C7-3A0B-AE28-2C8D4E31F936
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p_a0

>  `/System/Library/VideoProcessors/VideoDeghostingV3.bundle/binaryArchive.g18p_a0`

```diff

 
   __TEXT.__metallib: 0x2170
   __TEXT.__descriptor: 0x15f0
-  __TEXT.__compute: 0x35600
+  __TEXT.__compute: 0x35610
   __TEXT.__reflection: 0x46e60
-  UUID: 5F00D1F8-7B50-3517-B747-ADC0706D5632
+  UUID: 779138EB-EE1B-38B5-9A2C-F597FEC8FA0A
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p

>  `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p`

```diff

 
   __TEXT.__metallib: 0x37f0
   __TEXT.__descriptor: 0x3b90
-  __TEXT.__fragment: 0x42be0
+  __TEXT.__fragment: 0x41370
   __TEXT.__compute: 0x1940
   __TEXT.__vertex: 0xfd70
   __TEXT.__reflection: 0x9ea0
-  UUID: 00E5E0F5-F2D2-3BFB-A074-73E72569C4B3
+  UUID: 7696E6C1-1CC5-3A4E-BD09-72A800091550
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### binaryArchive.g18p_a0

>  `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/binaryArchive.g18p_a0`

```diff

 
   __TEXT.__metallib: 0x37f0
   __TEXT.__descriptor: 0x3b90
-  __TEXT.__fragment: 0x43e00
+  __TEXT.__fragment: 0x41370
   __TEXT.__compute: 0x1940
   __TEXT.__vertex: 0xfd70
   __TEXT.__reflection: 0x9ea0
-  UUID: 2B9A6846-D68C-3520-96E9-7C742C803CAC
+  UUID: B15807FD-F476-391B-A38F-34C06DFDDAA6
   Functions: 0
   Symbols:   0
   CStrings:  0

```

#### ospredictiond

>  `/usr/libexec/ospredictiond`

```diff

-222.2.2.0.0
+222.2.3.0.0
   __TEXT.__text: 0x5b6b0
   __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_stubs: 0x8660
   __TEXT.__objc_methlist: 0x8650
-  __TEXT.__const: 0x2f8
+  __TEXT.__const: 0x308
   __TEXT.__cstring: 0x48b7
   __TEXT.__objc_methname: 0x1358b
-  __TEXT.__oslogstring: 0x5445
+  __TEXT.__oslogstring: 0x5465
   __TEXT.__objc_classname: 0xcfa
   __TEXT.__objc_methtype: 0x221a
   __TEXT.__gcc_except_tab: 0xa74

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36A106E4-908D-32B5-8C54-872C38044902
+  UUID: 183FD9AB-01BA-3CE5-96A1-D01B780AA77E
   Functions: 2982
   Symbols:   255
   CStrings:  5041
CStrings:
+ "Not enough history to make prediction : %{public}lf days"
+ "Prediction input %{public}@ : %{public}lf"
+ "Prev12Next12Drain result  %{public}@"
- "Not enough history to make prediction : %lf days"
- "Prediction input %@ : %lf"
- "Prev12Next12Drain result  %@"

```

#### bluetoothd

>  `/usr/sbin/bluetoothd`

```diff

-190.51.1.6.0
-  __TEXT.__text: 0x874108
+190.51.1.7.0
+  __TEXT.__text: 0x874638
   __TEXT.__auth_stubs: 0x4990
   __TEXT.__objc_stubs: 0x17280
   __TEXT.__init_offsets: 0x54
   __TEXT.__objc_methlist: 0x8b34
   __TEXT.__const: 0x24f7c
-  __TEXT.__gcc_except_tab: 0x6c260
-  __TEXT.__cstring: 0xb3ee7
+  __TEXT.__gcc_except_tab: 0x6c348
+  __TEXT.__cstring: 0xb4056
   __TEXT.__objc_classname: 0xa07
   __TEXT.__objc_methname: 0x1bdba
   __TEXT.__objc_methtype: 0x496a

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0E9CADCD-E121-34B0-B639-C1714C7DD2A6
-  Functions: 33322
+  UUID: 3626717E-36AD-30EF-9BEE-FEF0840A79DC
+  Functions: 33323
   Symbols:   1639
-  CStrings:  43985
+  CStrings:  43993
 
CStrings:
+ "    HostAwakeVSC          Trigger Host Awake VSC for BD_VSC_REMOTE_AP_WRITE_LOCAL_STATE.\n"
+ "    HostSleptVSC          Trigger Host Slept VSC for BD_VSC_REMOTE_AP_WRITE_LOCAL_STATE.\n"
+ "    restart               Trigger bluetoothd restart manually.\n"
+ "15:13:01"
+ "Bluetooth FLR Transport hard reset done"
+ "Error: Bluetooth FLR Transport hard reset failed"
+ "HostAwakeVSC"
+ "HostSleptVSC"
+ "Sep 25 2025"
+ "restart"
- "20:37:38"
- "Aug 26 2025"

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A345)* | iBoot-13822.2.13 |
| 26.0.1 *(23A355)* | iBoot-13822.2.13 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.0 *(23A345)* | 622.1.22.10.9 |
| 26.0.1 *(23A355)* | 622.1.22.10.11 |

### Dylibs

#### ⬆️ Updated (25)

<details>
  <summary><i>View Updated</i></summary>

- [/System/Library/Frameworks/Accounts.framework/Accounts](DYLIBS/Accounts.md)
- [/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony](DYLIBS/CoreTelephony.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib](DYLIBS/libCommCenterBase.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterKCommandDrivers.dylib](DYLIBS/libCommCenterKCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib](DYLIBS/libCommCenterMCommandDrivers.dylib.md)
- [/System/Library/Frameworks/CoreText.framework/CoreText](DYLIBS/CoreText.md)
- [/System/Library/Frameworks/Foundation.framework/Foundation](DYLIBS/Foundation.md)
- [/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon](DYLIBS/AccountsDaemon.md)
- [/System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers](DYLIBS/CorePhoneNumbers.md)
- [/System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib](DYLIBS/libFontParser.dylib.md)
- [/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore](DYLIBS/IMDaemonCore.md)
- [/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation](DYLIBS/IconFoundation.md)
- [/System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI](DYLIBS/MobileStoreUI.md)
- [/System/Library/PrivateFrameworks/Navigation.framework/Navigation](DYLIBS/Navigation.md)
- [/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence](DYLIBS/OSIntelligence.md)
- [/System/Library/PrivateFrameworks/ReplicatorServices.framework/ReplicatorServices](DYLIBS/ReplicatorServices.md)
- [/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport](DYLIBS/SIMSetupSupport.md)
- [/System/Library/PrivateFrameworks/SignpostNotification.framework/SignpostNotification](DYLIBS/SignpostNotification.md)
- [/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport](DYLIBS/SignpostSupport.md)
- [/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome](DYLIBS/SpringBoardHome.md)
- [/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech](DYLIBS/TextToSpeech.md)
- [/System/Library/PrivateFrameworks/TextToSpeechVoiceBankingSupport.framework/TextToSpeechVoiceBankingSupport](DYLIBS/TextToSpeechVoiceBankingSupport.md)
- [/System/Library/PrivateFrameworks/WebCore.framework/WebCore](DYLIBS/WebCore.md)
- [/System/Library/VideoProcessors/NRFV4.bundle/NRFV4](DYLIBS/NRFV4.md)
- [/usr/lib/libcoreroutine.dylib](DYLIBS/libcoreroutine.dylib.md)

</details>

## Feature Flags

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### SIMSetupSupport.plist

>  `Domain/SIMSetupSupport.plist`

```diff

 		<key>Enabled</key>
 		<true/>
 	</dict>
+	<key>eSIMCountRestriction</key>
+	<dict>
+		<key>Enabled</key>
+		<true/>
+	</dict>
 	<key>eSIMTravelExperience</key>
 	<dict>
 		<key>Enabled</key>

```


</details>

## EOF
