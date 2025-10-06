## PodcastsKit

> `/System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit`

```diff

-4023.410.2.0.0
-  __TEXT.__text: 0x32090
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_methlist: 0x269c
+4023.510.2.0.0
+  __TEXT.__text: 0x32328
+  __TEXT.__auth_stubs: 0x1300
+  __TEXT.__objc_methlist: 0x26ac
   __TEXT.__const: 0x8d6
   __TEXT.__gcc_except_tab: 0x748
-  __TEXT.__cstring: 0x22f2
-  __TEXT.__oslogstring: 0x17ad
+  __TEXT.__cstring: 0x25c2
+  __TEXT.__oslogstring: 0x180a
   __TEXT.__ustring: 0x20
-  __TEXT.__swift5_typeref: 0x57c
+  __TEXT.__swift5_typeref: 0x57b
   __TEXT.__swift5_reflstr: 0x2fa
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0x764

   __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_capture: 0x368
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0xf78
+  __TEXT.__unwind_info: 0xf9c
   __TEXT.__objc_classname: 0x4e3
-  __TEXT.__objc_methname: 0x86fe
+  __TEXT.__objc_methname: 0x8734
   __TEXT.__objc_methtype: 0xf32
   __TEXT.__objc_stubs: 0x5be0
   __DATA_CONST.__got: 0x550
-  __DATA_CONST.__const: 0xcc8
+  __DATA_CONST.__const: 0xcd8
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4418
-  __DATA_CONST.__objc_selrefs: 0x20e0
+  __DATA_CONST.__objc_selrefs: 0x20e8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x328
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x12a0
+  __AUTH_CONST.__cfstring: 0x12c0
   __AUTH_CONST.__objc_const: 0x1100
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x980
+  __AUTH_CONST.__auth_got: 0x990
   __AUTH.__objc_data: 0x1820
   __AUTH.__data: 0x468
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x328
-  __DATA.__objc_superrefs: 0xc0
   __DATA.__objc_ivar: 0x1fc
   __DATA.__objc_data: 0x208
-  __DATA.__data: 0x7b0
+  __DATA.__data: 0x800
   __DATA.__bss: 0x590
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x230

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4B7EA164-1358-3BF6-BD99-0ABB53E86DAF
-  Functions: 1453
-  Symbols:   3842
-  CStrings:  2144
+  UUID: 1ED1CA04-E79C-369E-A272-EA7D7DDE9A34
+  Functions: 1452
+  Symbols:   3845
+  CStrings:  2164
 
Symbols:
+ +[MTPodcast(NSSortDescriptor) sortDescriptorsForRecentlyUnfollowed]
+ ___43-[MTAccountController _updateActiveAccount]_block_invoke.17
+ _block_copy_helper.112
+ _block_copy_helper.126
+ _block_copy_helper.34
+ _block_copy_helper.43
+ _block_copy_helper.61
+ _block_copy_helper.67
+ _block_copy_helper.74
+ _block_copy_helper.81
+ _block_copy_helper.87
+ _block_copy_helper.94
+ _block_descriptor.114
+ _block_descriptor.128
+ _block_descriptor.36
+ _block_descriptor.45
+ _block_descriptor.63
+ _block_descriptor.69
+ _block_descriptor.76
+ _block_descriptor.83
+ _block_descriptor.89
+ _block_descriptor.96
+ _block_destroy_helper.113
+ _block_destroy_helper.127
+ _block_destroy_helper.35
+ _block_destroy_helper.44
+ _block_destroy_helper.62
+ _block_destroy_helper.68
+ _block_destroy_helper.75
+ _block_destroy_helper.82
+ _block_destroy_helper.88
+ _block_destroy_helper.95
+ _kLastUnfollowedDate
+ _kMTShowsSortTypeRecentlyUnfollowed
+ _objc_msgSend$sortDescriptorsForRecentlyUnfollowed
+ _objectdestroy.32Tm
+ _objectdestroy.65Tm
- ___43-[MTAccountController _updateActiveAccount]_block_invoke_2
- _block_copy_helper.111
- _block_copy_helper.125
- _block_copy_helper.33
- _block_copy_helper.42
- _block_copy_helper.60
- _block_copy_helper.66
- _block_copy_helper.73
- _block_copy_helper.80
- _block_copy_helper.86
- _block_copy_helper.93
- _block_descriptor.113
- _block_descriptor.127
- _block_descriptor.35
- _block_descriptor.44
- _block_descriptor.62
- _block_descriptor.68
- _block_descriptor.75
- _block_descriptor.82
- _block_descriptor.88
- _block_descriptor.95
- _block_destroy_helper.112
- _block_destroy_helper.126
- _block_destroy_helper.34
- _block_destroy_helper.43
- _block_destroy_helper.61
- _block_destroy_helper.67
- _block_destroy_helper.74
- _block_destroy_helper.81
- _block_destroy_helper.87
- _block_destroy_helper.94
- _objc_msgSend$sortDescriptorsForRecentlyUpdatedAscending:
- _objectdestroy.31Tm
- _objectdestroy.64Tm
- _os_feature_enabled_use_first_time_available
CStrings:
+ "Insufficient space allocated to copy string contents"
+ "MTAccountController: Setting active account: %@"
+ "MTAccountController: updating active account"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"
+ "recentlyUnfollowed"
+ "sortDescriptorsForRecentlyUnfollowed"

```
