## NanoMusicSync

> `/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2024.100.46.0.0
-  __TEXT.__text: 0x4de74
-  __TEXT.__objc_methlist: 0x4104
+2024.100.50.0.0
+  __TEXT.__text: 0x4e6ac
+  __TEXT.__objc_methlist: 0x414c
   __TEXT.__const: 0x332
-  __TEXT.__gcc_except_tab: 0x9e4
+  __TEXT.__gcc_except_tab: 0xa10
   __TEXT.__cstring: 0x33c3
   __TEXT.__oslogstring: 0x7981
   __TEXT.__constg_swiftt: 0xb8

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x4
-  __TEXT.__unwind_info: 0x1358
+  __TEXT.__unwind_info: 0x1388
   __TEXT.__eh_frame: 0x168
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x12e0
-  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__const: 0x1308
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b80
-  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_selrefs: 0x2ba0
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x98
   __DATA_CONST.__got: 0x990
   __AUTH_CONST.__const: 0x388
   __AUTH_CONST.__cfstring: 0x33c0
-  __AUTH_CONST.__objc_const: 0x6968
+  __AUTH_CONST.__objc_const: 0x6b58
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH.__objc_data: 0x12e8
+  __AUTH.__objc_data: 0x1338
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x458
+  __DATA.__objc_ivar: 0x480
   __DATA.__data: 0x568
   __DATA.__bss: 0x100
   __DATA.__common: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1738
-  Symbols:   4216
+  Functions: 1747
+  Symbols:   4245
   CStrings:  903
 
Symbols:
+ +[NMSPodcastsFetchRequests stationFetchRequestsForStationUUID:downloadedOnly:ctx:]
+ -[NMSStationFetchRequestItemEnumerator .cxx_destruct]
+ -[NMSStationFetchRequestItemEnumerator _getNextItem]
+ -[NMSStationFetchRequestItemEnumerator initWithStationUUID:downloadSettings:downloadedOnly:ctx:]
+ -[NMSStationFetchRequestItemEnumerator nextItem]
+ GCC_except_table2
+ GCC_except_table7
+ _OBJC_CLASS_$_NMSStationFetchRequestItemEnumerator
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._ctx
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._didLoadSegmentRequests
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._downloadSettings
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._downloadedOnly
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._episodesRemaining
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._segmentIndex
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._segmentItemIndex
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._segmentItems
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._segmentRequests
+ _OBJC_IVAR_$_NMSStationFetchRequestItemEnumerator._stationUUID
+ _OBJC_METACLASS_$_NMSStationFetchRequestItemEnumerator
+ __OBJC_$_INSTANCE_METHODS_NMSStationFetchRequestItemEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_NMSStationFetchRequestItemEnumerator
+ __OBJC_CLASS_PROTOCOLS_$_NMSStationFetchRequestItemEnumerator
+ __OBJC_CLASS_RO_$_NMSStationFetchRequestItemEnumerator
+ __OBJC_METACLASS_RO_$_NMSStationFetchRequestItemEnumerator
+ ___48-[NMSStationFetchRequestItemEnumerator nextItem]_block_invoke
+ ___82+[NMSPodcastsFetchRequests stationFetchRequestsForStationUUID:downloadedOnly:ctx:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ _objc_msgSend$predicate
+ _objc_msgSend$stationFetchRequests
+ _objc_msgSend$stationFetchRequestsForStationUUID:downloadedOnly:ctx:
- GCC_except_table3
```
