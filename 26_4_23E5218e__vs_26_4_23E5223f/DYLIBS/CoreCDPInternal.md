## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-416.475.10.0.0
-  __TEXT.__text: 0x954b4
-  __TEXT.__auth_stubs: 0x1150
-  __TEXT.__objc_methlist: 0x55ec
+416.475.11.0.0
+  __TEXT.__text: 0x95948
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_methlist: 0x5634
   __TEXT.__const: 0x830
-  __TEXT.__oslogstring: 0x1460e
+  __TEXT.__oslogstring: 0x1468e
   __TEXT.__cstring: 0xd5c5
-  __TEXT.__gcc_except_tab: 0xc5c
+  __TEXT.__gcc_except_tab: 0xc70
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x385
   __TEXT.__swift5_fieldmd: 0x80

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1f48
+  __TEXT.__unwind_info: 0x1f68
   __TEXT.__eh_frame: 0x958
   __TEXT.__objc_classname: 0xdbd
-  __TEXT.__objc_methname: 0xf90f
+  __TEXT.__objc_methname: 0xf9cf
   __TEXT.__objc_methtype: 0x2a77
-  __TEXT.__objc_stubs: 0xcb60
+  __TEXT.__objc_stubs: 0xcc00
   __DATA_CONST.__got: 0x1088
-  __DATA_CONST.__const: 0x2548
+  __DATA_CONST.__const: 0x2570
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3878
+  __DATA_CONST.__objc_selrefs: 0x38a0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x8b8
+  __AUTH_CONST.__auth_got: 0x8c0
   __AUTH_CONST.__const: 0xab0
   __AUTH_CONST.__cfstring: 0x8da0
-  __AUTH_CONST.__objc_const: 0x10070
+  __AUTH_CONST.__objc_const: 0x100b0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x1070
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x3ac
+  __DATA.__objc_ivar: 0x3b0
   __DATA.__data: 0x1230
-  __DATA.__bss: 0x4c0
+  __DATA.__bss: 0x4d0
   __DATA_DIRTY.__objc_data: 0xa60
   __DATA_DIRTY.__data: 0x180
   __DATA_DIRTY.__bss: 0x178

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5207F033-AD33-35EB-87FC-FC8081C7FD87
-  Functions: 3128
-  Symbols:   10328
-  CStrings:  6470
+  UUID: 41C5EE0E-B7B3-33F5-AE6F-4F77E320C207
+  Functions: 3142
+  Symbols:   10372
+  CStrings:  6481
 
Symbols:
+ -[CDPDTTRController .cxx_destruct]
+ -[CDPDTTRController _handleFetchedTTRConfig:error:forEvent:]
+ -[CDPDTTRController _handleFetchedTTRConfig:error:forEvent:].cold.1
+ -[CDPDTTRController _processTTRConfig:forEvent:]
+ -[CDPDTTRController _readCachedTTRConfig]
+ -[CDPDTTRController cachedTTRConfig]
+ -[CDPDTTRController requestTTRIfSupportedForEvent:].cold.2
+ -[CDPDTTRController requestTTRIfSupportedForEvent:].cold.3
+ -[CDPDTTRController setCachedTTRConfig:]
+ _OBJC_IVAR_$_CDPDTTRController._cachedTTRConfig
+ __OBJC_$_INSTANCE_VARIABLES_CDPDTTRController
+ __OBJC_$_PROP_LIST_CDPDTTRController
+ ___41-[CDPDTTRController _readCachedTTRConfig]_block_invoke
+ ___51-[CDPDTTRController requestTTRIfSupportedForEvent:]_block_invoke.cold.1
+ ___60-[CDPDTTRController _handleFetchedTTRConfig:error:forEvent:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e20_v24?08"NSError"16lw48l8s32l8s40l8
+ __ttrCacheLock
+ _objc_msgSend$_handleFetchedTTRConfig:error:forEvent:
+ _objc_msgSend$_processTTRConfig:forEvent:
+ _objc_msgSend$_readCachedTTRConfig
+ _objc_msgSend$cachedTTRConfig
+ _objc_msgSend$setCachedTTRConfig:
+ _objc_retain_x9
- ___block_descriptor_64_e8_32s40s48s56w_e20_v24?08"NSError"16ls32l8s40l8w56l8s48l8
CStrings:
+ "CDPDTTRController is missing."
+ "Cached TTR config NOT available...fetching."
+ "Cached TTR config available."
+ "Failed to fetch TTR config: %@"
+ "T@\"NSDictionary\",C,N,V_cachedTTRConfig"
+ "_cachedTTRConfig"
+ "_handleFetchedTTRConfig:error:forEvent:"
+ "_processTTRConfig:forEvent:"
+ "_readCachedTTRConfig"
+ "cachedTTRConfig"
+ "setCachedTTRConfig:"

```
