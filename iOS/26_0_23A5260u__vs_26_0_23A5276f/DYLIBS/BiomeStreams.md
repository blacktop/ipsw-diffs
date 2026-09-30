## BiomeStreams

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams`

```diff

-192.0.0.0.0
-  __TEXT.__text: 0x40ebf4
+195.0.0.0.0
+  __TEXT.__text: 0x40edc4
   __TEXT.__auth_stubs: 0x23f0
   __TEXT.__objc_methlist: 0x15124
   __TEXT.__const: 0xabf84
   __TEXT.__cstring: 0x35119
   __TEXT.__gcc_except_tab: 0x14d8
-  __TEXT.__oslogstring: 0xbaa0
+  __TEXT.__oslogstring: 0xbae0
   __TEXT.__dlopen_cstrs: 0x632
   __TEXT.__constg_swiftt: 0xb2b8
   __TEXT.__swift5_typeref: 0x55b2

   __TEXT.__unwind_info: 0xc258
   __TEXT.__eh_frame: 0xde80
   __TEXT.__objc_classname: 0x26cd
-  __TEXT.__objc_methname: 0x1cf63
+  __TEXT.__objc_methname: 0x1cf75
   __TEXT.__objc_methtype: 0x3c99
-  __TEXT.__objc_stubs: 0x117a0
+  __TEXT.__objc_stubs: 0x117c0
   __DATA_CONST.__got: 0x10a8
-  __DATA_CONST.__const: 0x2a838
+  __DATA_CONST.__const: 0x2a7f8
   __DATA_CONST.__objc_classlist: 0xea0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6058
+  __DATA_CONST.__objc_selrefs: 0x6060
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x990
   __DATA_CONST.__objc_arraydata: 0x38

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DC60E7EF-4956-3D3A-A5A0-B857BE7D9BC2
-  Functions: 21814
-  Symbols:   74767
-  CStrings:  16588
+  UUID: AE2A4D12-3117-387F-973E-98536B337C09
+  Functions: 21815
+  Symbols:   74758
+  CStrings:  16590
 
Symbols:
+ ___55-[BMStorePublisherManager _streamReaderWithRemoteName:]_block_invoke.cold.1
+ _objc_msgSend$currentFrameStore
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_BiomeSQLParser
- __swift_FORCE_LOAD_$_swiftDarwin_$_BiomeStreams
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_BiomeSQLParser
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_BiomeStreams
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_BiomeSQLParser
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_BiomeStreams
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_BiomeSQLParser
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_BiomeStreams
Functions:
~ ___55-[BMStorePublisherManager _streamReaderWithRemoteName:]_block_invoke : 332 -> 408
~ _bmstream_vtab_destroy : 60 -> 80
~ -[BMPublisherVirtualTableCursor resetWithOptions:] : 196 -> 228
~ -[BMPublisherVirtualTableCursor advance] : 112 -> 128
~ -[BMPublisherVirtualTableCursor _resetWithPublisher:] : 4 -> 96
~ -[BMPublisherVirtualTableCursor requestNextEvents] : 96 -> 112
~ _bmstream_vtab_connect : 564 -> 584
~ _bmstream_vtab_bestindex : 1288 -> 1336
~ _bmstream_vtab_disconnect : 68 -> 84
~ _bmstream_vtab_open : 112 -> 132
~ _bmstream_vtab_close : 64 -> 80
~ _bmstream_vtab_filter : 616 -> 640
+ ___55-[BMStorePublisherManager _streamReaderWithRemoteName:]_block_invoke.cold.1
CStrings:
+ "BMStorePublisherManager: clearing localDatastore cache due to nil frame store"
+ "currentFrameStore"

```
