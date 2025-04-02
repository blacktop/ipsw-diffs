## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics`

```diff

-758.100.43.0.0
-  __TEXT.__text: 0x41a08
+758.120.5.0.0
+  __TEXT.__text: 0x41dbc
   __TEXT.__auth_stubs: 0x1250
-  __TEXT.__objc_methlist: 0x1a48
+  __TEXT.__objc_methlist: 0x1a90
   __TEXT.__oslogstring: 0x2e98
-  __TEXT.__cstring: 0x8dbe
+  __TEXT.__cstring: 0x8df4
   __TEXT.__const: 0x5b0
   __TEXT.__gcc_except_tab: 0x10bc
   __TEXT.__dlopen_cstrs: 0xed
-  __TEXT.__unwind_info: 0xa68
+  __TEXT.__unwind_info: 0xa78
   __TEXT.__eh_frame: 0x40
-  __TEXT.__objc_classname: 0x328
-  __TEXT.__objc_methname: 0x4bad
+  __TEXT.__objc_classname: 0x32a
+  __TEXT.__objc_methname: 0x4cbe
   __TEXT.__objc_methtype: 0xc6e
-  __TEXT.__objc_stubs: 0x42c0
+  __TEXT.__objc_stubs: 0x4360
   __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x7e0
+  __DATA_CONST.__const: 0x828
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1490
+  __DATA_CONST.__objc_selrefs: 0x14c8
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xbd0
   __AUTH_CONST.__auth_got: 0x938
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__const: 0xf00
-  __AUTH_CONST.__cfstring: 0x9ca0
-  __AUTH_CONST.__objc_const: 0x36a0
+  __AUTH_CONST.__const: 0xf30
+  __AUTH_CONST.__cfstring: 0x9ce0
+  __AUTH_CONST.__objc_const: 0x3720
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x2bc
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x168
   __DATA.__bss: 0x388
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 970
-  Symbols:   2670
-  CStrings:  2860
+  Functions: 977
+  Symbols:   2686
+  CStrings:  2876
 
Symbols:
+ -[ExclaveLayout setSharedCacheIndex:]
+ -[ExclaveLayout sharedCacheIndex]
+ -[OSABinaryImageCatalog addExclaveSharedCache:]
+ -[OSABinaryImageCatalog clearExclaveSharedCaches]
+ -[OSAExclaveContainer setSharedCaches:]
+ -[OSAExclaveContainer sharedCaches]
+ GCC_except_table49
+ OBJC_IVAR_$_ExclaveLayout._sharedCacheIndex
+ OBJC_IVAR_$_OSABinaryImageCatalog._exclave_shared_caches
+ OBJC_IVAR_$_OSAExclaveContainer._sharedCaches
+ __35-[OSAExclaveContainer parseKCdata:]_block_invoke.86
+ __37-[OSASystemConfiguration internalKey]_block_invoke.328
+ __37-[OSASystemConfiguration internalKey]_block_invoke.328.cold.1
+ __37-[OSASystemConfiguration internalKey]_block_invoke.328.cold.2
+ __37-[OSASystemConfiguration internalKey]_block_invoke.328.cold.3
+ __55-[OSABinaryImageCatalog searchFrame:in:regions:result:]_block_invoke.140
+ __61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.392
+ ___block_descriptor_48_e8_32s40s_e47_v20?0I8r^{exclave_textlayout_segment=[16C]Q}12l
+ ___block_descriptor_64_e8_32s40r48r_e38_v32?0"OSABinaryImageSegment"8Q16^B24l
+ __block_literal_global.269
+ __block_literal_global.39
+ __block_literal_global.60
+ __rtc_internal_block_invoke.63
+ __rtc_internal_block_invoke.63.cold.1
+ __rtc_internal_block_invoke.63.cold.2
+ __rtc_internal_block_invoke.63.cold.3
+ __rtc_internal_block_invoke.65
+ __rtc_internal_block_invoke.66.cold.1
+ _objc_msgSend$addExclaveSharedCache:
+ _objc_msgSend$clearExclaveSharedCaches
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$setSharedCacheIndex:
+ _objc_msgSend$sharedCacheIndex
- GCC_except_table47
- __35-[OSAExclaveContainer parseKCdata:]_block_invoke.81
- __37-[OSASystemConfiguration internalKey]_block_invoke.322
- __37-[OSASystemConfiguration internalKey]_block_invoke.322.cold.1
- __37-[OSASystemConfiguration internalKey]_block_invoke.322.cold.2
- __37-[OSASystemConfiguration internalKey]_block_invoke.322.cold.3
- __61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.386
- ___block_descriptor_40_e8_32s_e47_v20?0I8r^{exclave_textlayout_segment=[16C]Q}12l
- __block_literal_global.266
- __block_literal_global.40
- __block_literal_global.61
- __rtc_internal_block_invoke.64
- __rtc_internal_block_invoke.64.cold.1
- __rtc_internal_block_invoke.64.cold.2
- __rtc_internal_block_invoke.64.cold.3
- __rtc_internal_block_invoke.67
- __rtc_internal_block_invoke.67.cold.1
CStrings:
+ "\x06\x14"
+ "\x16"
+ "%@-seed"
+ "Seed"
+ "T@\"NSMutableArray\",&,N,V_sharedCaches"
+ "T@\"NSNumber\",&,N,V_sharedCacheIndex"
+ "_exclave_shared_caches"
+ "_sharedCacheIndex"
+ "_sharedCaches"
+ "addExclaveSharedCache:"
+ "clearExclaveSharedCaches"
+ "enumerateObjectsUsingBlock:"
+ "seed"
+ "setSharedCacheIndex:"
+ "setSharedCaches:"
+ "sharedCacheIndex"
+ "sharedCaches"
+ "v32@?0@\"OSABinaryImageSegment\"8Q16^B24"
- "\x06\x13"
- "GM"

```
