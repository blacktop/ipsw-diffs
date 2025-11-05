## QuickLookThumbnailingDaemon

> `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/Versions/A/QuickLookThumbnailingDaemon`

```diff

-199.4.3.0.0
-  __TEXT.__text: 0x58a48
-  __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0x2e5c
-  __TEXT.__const: 0xb68
-  __TEXT.__gcc_except_tab: 0xd5c
-  __TEXT.__cstring: 0x4686
+199.5.3.0.0
+  __TEXT.__text: 0x58990
+  __TEXT.__auth_stubs: 0x1a90
+  __TEXT.__objc_methlist: 0x30a4
+  __TEXT.__const: 0xb38
+  __TEXT.__gcc_except_tab: 0xd64
+  __TEXT.__cstring: 0x43b6
   __TEXT.__oslogstring: 0x5236
   __TEXT.__constg_swiftt: 0x308
-  __TEXT.__swift5_typeref: 0x517
+  __TEXT.__swift5_typeref: 0x539
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x293
   __TEXT.__swift5_fieldmd: 0x1d4
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_capture: 0xf8
+  __TEXT.__swift5_capture: 0x108
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x24
   __TEXT.__dof_QuickLook: 0xb22
-  __TEXT.__unwind_info: 0x13d8
-  __TEXT.__eh_frame: 0x6c0
+  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__eh_frame: 0x730
   __TEXT.__objc_classname: 0x4d2
   __TEXT.__objc_methname: 0x99f7
   __TEXT.__objc_methtype: 0x1b17
   __TEXT.__objc_stubs: 0x76c0
   __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x338
+  __DATA_CONST.__const: 0x300
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23d8
+  __DATA_CONST.__objc_selrefs: 0x2468
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0xd80
-  __AUTH_CONST.__const: 0x17a0
+  __AUTH_CONST.__auth_got: 0xd58
+  __AUTH_CONST.__const: 0x17f0
   __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x5468
+  __AUTH_CONST.__objc_const: 0x5060
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xea8

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7CB94FB8-57E3-357C-9647-6ED056B26464
-  Functions: 1940
-  Symbols:   4057
-  CStrings:  2985
+  UUID: 6956ED3A-84FE-3F9A-B34E-16E7DB1936F9
+  Functions: 1947
+  Symbols:   4062
+  CStrings:  2969
 
Symbols:
+ +[QLCacheFragHandler initialize].cold.1
+ +[QLTAnalyticsManager sharedManager].cold.1
+ +[QLThumbnailIOSurfaceGenerator sharedInstance].cold.1
+ +[_QLCacheThread defaultCacheSize].cold.1
+ -[QLTAnalyticsManager _eventsQueue].cold.1
+ GCC_except_table100
+ GCC_except_table108
+ GCC_except_table80
+ GCC_except_table85
+ GCC_except_table91
+ GCC_except_table98
+ QLCacheInDebugMode.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_project_boxed_opaque_existential_0
+ _stringForCacheMode
+ _symbolic SccySo15QLPlatformImageC______pG s5ErrorP
+ block_copy_helper.37
+ block_descriptor.39
+ block_destroy_helper.38
+ objectdestroy.19Tm
- GCC_except_table105
- GCC_except_table53
- GCC_except_table73
- GCC_except_table79
- GCC_except_table84
- GCC_except_table90
- GCC_except_table97
- GCC_except_table99
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_QuickLookThumbnailingDaemon
- _strcmp
- block_descriptor.34
- objectdestroy.16Tm
CStrings:
- "Can't construct Array with count < 0"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
