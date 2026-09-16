## PeriodicSystemMetricsCore

> `/System/Library/PrivateFrameworks/PeriodicSystemMetricsCore.framework/PeriodicSystemMetricsCore`

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
-  __TEXT.__text: 0xf880
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x1360
-  __TEXT.__objc_methlist: 0x147c
+9.0.0.0.0
+  __TEXT.__text: 0xfc94
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x1520
+  __TEXT.__objc_methlist: 0x15cc
   __TEXT.__const: 0x960
   __TEXT.__gcc_except_tab: 0x1308
-  __TEXT.__cstring: 0x6c0
-  __TEXT.__objc_methname: 0x1c6a
+  __TEXT.__cstring: 0x6a4
+  __TEXT.__objc_methname: 0x1e0d
   __TEXT.__objc_classname: 0x3de
-  __TEXT.__objc_methtype: 0x806
-  __TEXT.__oslogstring: 0x439
-  __TEXT.__unwind_info: 0xb38
-  __DATA_CONST.__const: 0x738
+  __TEXT.__objc_methtype: 0x830
+  __TEXT.__oslogstring: 0x3f3
+  __TEXT.__unwind_info: 0xb58
+  __DATA_CONST.__const: 0x758
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
-  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__auth_got: 0x368
   __DATA_CONST.__got: 0xf8
-  __DATA.__objc_const: 0x2ed8
+  __DATA.__objc_const: 0x2fb8
   __DATA.__objc_ivar: 0x1d4
   __DATA.__objc_data: 0xc80
-  __DATA.__data: 0x1d0
+  __DATA.__data: 0x1d8
   - /AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 689
-  Symbols:   1573
-  CStrings:  572
+  Functions: 717
+  Symbols:   1619
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
+ GCC_except_table148
+ GCC_except_table167
+ GCC_except_table184
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table211
+ GCC_except_table220
+ GCC_except_table240
+ GCC_except_table247
+ GCC_except_table256
+ GCC_except_table274
+ GCC_except_table276
+ GCC_except_table283
+ GCC_except_table365
+ GCC_except_table385
+ GCC_except_table405
+ GCC_except_table95
+ GCC_except_table96
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
- GCC_except_table127
- GCC_except_table139
- GCC_except_table146
- GCC_except_table155
- GCC_except_table156
- GCC_except_table176
- GCC_except_table191
- GCC_except_table192
- GCC_except_table210
- GCC_except_table212
- GCC_except_table227
- GCC_except_table228
- GCC_except_table246
- GCC_except_table337
- GCC_except_table357
- GCC_except_table88
- _OUTLINED_FUNCTION_10
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
