## PeriodicSystemMetricsCore

> `/System/Library/PrivateFrameworks/PeriodicSystemMetricsCore.framework/Versions/A/PeriodicSystemMetricsCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-8.0.0.0.0
-  __TEXT.__text: 0x10490
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x1360
-  __TEXT.__objc_methlist: 0x147c
+9.0.0.0.0
+  __TEXT.__text: 0x10890
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0x1520
+  __TEXT.__objc_methlist: 0x15cc
   __TEXT.__const: 0x968
   __TEXT.__gcc_except_tab: 0x1334
-  __TEXT.__cstring: 0x6c0
-  __TEXT.__objc_methname: 0x1c6a
+  __TEXT.__cstring: 0x6a4
+  __TEXT.__objc_methname: 0x1e0d
   __TEXT.__objc_classname: 0x3de
-  __TEXT.__objc_methtype: 0x806
-  __TEXT.__oslogstring: 0x439
-  __TEXT.__unwind_info: 0xb68
-  __DATA_CONST.__const: 0x778
+  __TEXT.__objc_methtype: 0x830
+  __TEXT.__oslogstring: 0x3f3
+  __TEXT.__unwind_info: 0xb80
+  __DATA_CONST.__const: 0x798
   __DATA_CONST.__cfstring: 0x7e0
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x648
+  __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_intobj: 0x3a8
   __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__auth_got: 0x2c0
   __DATA_CONST.__got: 0xf8
-  __DATA.__objc_const: 0x2ed8
+  __DATA.__objc_const: 0x2fb8
   __DATA.__objc_ivar: 0x1d4
   __DATA.__objc_data: 0xc80
-  __DATA.__data: 0x1d0
+  __DATA.__data: 0x1d8
   - /AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/Versions/A/PerformanceControlKitInternal
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 708
-  Symbols:   1568
-  CStrings:  572
+  Functions: 736
+  Symbols:   1611
+  CStrings:  584
 
Symbols:
+ -[PSMImmutableVMStats activeInternalCount]
+ -[PSMImmutableVMStats executableCount]
+ -[PSMImmutableVMStats inactiveInternalCount]
+ -[PSMImmutableVMStats pageinsDelta]
+ -[PSMImmutableVMStats purgeablePageableCount]
+ -[PSMImmutableVMStats purgeableWiredCount]
+ -[PSMImmutableVMStats realtimeCount]
+ -[PSMMutableVMStats activeInternalCount]
+ -[PSMMutableVMStats executableCount]
+ -[PSMMutableVMStats inactiveInternalCount]
+ -[PSMMutableVMStats initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:pageinsDelta:executableCount:purgeablePageableCount:purgeableWiredCount:activeInternalCount:inactiveInternalCount:realtimeCount:]
+ -[PSMMutableVMStats pageinsDelta]
+ -[PSMMutableVMStats purgeablePageableCount]
+ -[PSMMutableVMStats purgeableWiredCount]
+ -[PSMMutableVMStats realtimeCount]
+ -[PSMMutableVMStats setActiveInternalCount:]
+ -[PSMMutableVMStats setExecutableCount:]
+ -[PSMMutableVMStats setInactiveInternalCount:]
+ -[PSMMutableVMStats setPageinsDelta:]
+ -[PSMMutableVMStats setPurgeablePageableCount:]
+ -[PSMMutableVMStats setPurgeableWiredCount:]
+ -[PSMMutableVMStats setRealtimeCount:]
+ -[PSMVMStats activeInternalCount]
+ -[PSMVMStats executableCount]
+ -[PSMVMStats inactiveInternalCount]
+ -[PSMVMStats initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:pageinsDelta:executableCount:purgeablePageableCount:purgeableWiredCount:activeInternalCount:inactiveInternalCount:realtimeCount:]
+ -[PSMVMStats pageinsDelta]
+ -[PSMVMStats purgeablePageableCount]
+ -[PSMVMStats purgeableWiredCount]
+ -[PSMVMStats realtimeCount]
+ GCC_except_table152
+ GCC_except_table171
+ GCC_except_table188
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table215
+ GCC_except_table224
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table260
+ GCC_except_table278
+ GCC_except_table280
+ GCC_except_table287
+ GCC_except_table389
+ GCC_except_table99
+ _OUTLINED_FUNCTION_11
+ ____vmStats_block_invoke_2
+ _objc_msgSend$activeInternalCount
+ _objc_msgSend$executableCount
+ _objc_msgSend$inactiveInternalCount
+ _objc_msgSend$initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:pageinsDelta:executableCount:purgeablePageableCount:purgeableWiredCount:activeInternalCount:inactiveInternalCount:realtimeCount:
+ _objc_msgSend$pageinsDelta
+ _objc_msgSend$purgeablePageableCount
+ _objc_msgSend$purgeableWiredCount
+ _objc_msgSend$realtimeCount
+ _objc_msgSend$setActiveInternalCount:
+ _objc_msgSend$setExecutableCount:
+ _objc_msgSend$setInactiveInternalCount:
+ _objc_msgSend$setPageinsDelta:
+ _objc_msgSend$setPurgeablePageableCount:
+ _objc_msgSend$setPurgeableWiredCount:
+ _objc_msgSend$setRealtimeCount:
+ _vmStats.hostOnceToken
+ _vmStats.myHost
+ _vmStats.sPrevPageins
- -[PSMMutableVMStats initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:]
- -[PSMVMStats initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:]
- GCC_except_table131
- GCC_except_table143
- GCC_except_table150
- GCC_except_table159
- GCC_except_table160
- GCC_except_table180
- GCC_except_table195
- GCC_except_table196
- GCC_except_table214
- GCC_except_table216
- GCC_except_table231
- GCC_except_table232
- GCC_except_table250
- GCC_except_table252
- GCC_except_table341
- GCC_except_table361
- GCC_except_table381
- GCC_except_table92
- _objc_msgSend$initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:
- _sysctlbyname
CStrings:
+ "@92@0:8I16I20I24I28I32I36I40I44I48I52I56I60I64I68I72I76I80I84I88"
+ "Tr^{VMStats=IIIIIIIIIIIIIIIIIII},R,N"
+ "^{VMStats=IIIIIIIIIIIIIIIIIII}"
+ "activeInternalCount"
+ "executableCount"
+ "inactiveInternalCount"
+ "initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:pageinsDelta:executableCount:purgeablePageableCount:purgeableWiredCount:activeInternalCount:inactiveInternalCount:realtimeCount:"
+ "pageinsDelta"
+ "purgeablePageableCount"
+ "purgeableWiredCount"
+ "r^{VMStats=IIIIIIIIIIIIIIIIIII}"
+ "r^{VMStats=IIIIIIIIIIIIIIIIIII}16@0:8"
+ "realtimeCount"
+ "setActiveInternalCount:"
+ "setExecutableCount:"
+ "setInactiveInternalCount:"
+ "setPageinsDelta:"
+ "setPurgeablePageableCount:"
+ "setPurgeableWiredCount:"
+ "setRealtimeCount:"
- "@64@0:8I16I20I24I28I32I36I40I44I48I52I56I60"
- "Failed to fetch `vm.page_shared_region_count` sysctl due to error: %d"
- "Tr^{VMStats=IIIIIIIIIIII},R,N"
- "^{VMStats=IIIIIIIIIIII}"
- "initWithActiveCount:speculativeCount:inactiveCount:freeCount:wireCount:compressorPageCount:internalPageCount:externalPageCount:totalUncompressedPagesInCompressor:swappedCount:swapCount:pageSharedRegionCount:"
- "r^{VMStats=IIIIIIIIIIII}"
- "r^{VMStats=IIIIIIIIIIII}16@0:8"
- "vm.page_shared_region_count"
```
