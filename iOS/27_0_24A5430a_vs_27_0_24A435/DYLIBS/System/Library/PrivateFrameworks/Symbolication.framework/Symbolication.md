## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

 64578.100.1.0.0
-  __TEXT.__text: 0xbc230
+  __TEXT.__text: 0xbc2cc
   __TEXT.__objc_methlist: 0x6a00
   __TEXT.__const: 0x316
-  __TEXT.__gcc_except_tab: 0x596c
+  __TEXT.__gcc_except_tab: 0x5990
   __TEXT.__cstring: 0x11308
   __TEXT.__oslogstring: 0x199c
   __TEXT.__ustring: 0x24

   __TEXT.__swift5_reflstr: 0x311
   __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x2db8
+  __TEXT.__unwind_info: 0x2dc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x8f8
   __DATA_CONST.__got: 0x4a0
   __AUTH_CONST.__const: 0x12f8
-  __AUTH_CONST.__cfstring: 0xdba0
+  __AUTH_CONST.__cfstring: 0xdbc0
   __AUTH_CONST.__objc_const: 0xcc20
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x120

   - /usr/lib/swift/libswiftos.dylib
   Functions: 3381
   Symbols:   7500
-  CStrings:  2906
+  CStrings:  2907
 
Functions:
~ _OUTLINED_FUNCTION_2 : 32 -> 16
~ _OUTLINED_FUNCTION_4 -> _OUTLINED_FUNCTION_3 : 24 -> 32
~ -[VMUTaskMemoryScanner setDyldSharedCacheMemoryMappingOverridesWithRegions:] : 1164 -> 1172
~ ___59-[VMUTaskMemoryScanner _withReaderBlockForHeapEnumeration:]_block_invoke : 1840 -> 1844
~ -[VMUTaskMemoryScanner _identifySwiftAsyncTaskSlabs] : 1404 -> 1408
~ -[VMUTaskMemoryScanner zoneNameForNode:] : 532 -> 536
~ -[VMUTaskMemoryScanner withContentForNode:block:] : 1868 -> 1860
~ _OUTLINED_FUNCTION_5 : 20 -> 24
~ _OUTLINED_FUNCTION_10 -> _OUTLINED_FUNCTION_6 : 16 -> 20
~ _OUTLINED_FUNCTION_11 -> _OUTLINED_FUNCTION_7 : 16 -> 20
~ _OUTLINED_FUNCTION_19 : 12 -> 16
~ _OUTLINED_FUNCTION_20 : 20 -> 12
~ ___53-[VMUKernelCoreMemoryScanner _withMemoryReaderBlock:]_block_invoke : 1732 -> 1720
~ -[VMUKernelCoreMemoryScanner _enumerateZallocZones:blocks:] : 1808 -> 1816
~ -[VMUKernelCoreMemoryScanner zoneNameForNode:] : 532 -> 536
~ -[VMUKernelCoreMemoryScanner withContentForNode:block:] : 1788 -> 1800
~ _OUTLINED_FUNCTION_6 -> _OUTLINED_FUNCTION_9 : 12 -> 16
~ -[VMULeakDetector printContents:size:] : 380 -> 384
~ -[VMUProcessDescription _cpuTypeDescription] : 416 -> 504
~ -[VMUProcessObjectGraph parseMacOSArchitectureFromProcessDescription] : 604 -> 672
~ -[VMUMallocZoneAggregate modifySize:count:forClassInfo:] : 660 -> 656
~ -[VMUDirectedGraph removeMarkedNodes:] : 800 -> 804
~ -[VMUDirectedGraph _adjustAdjacencyMap] : 1156 -> 1164
~ -[VMUObjectGraph addEdgeFromNode:sourceOffset:withScanType:toNode:destinationOffset:] : 564 -> 568
~ -[VMUObjectGraph _refineTypesWithOverlay:] : 704 -> 708
~ -[VMUObjectGraph _compareWithGraph:andMarkOnMatch:] : 1144 -> 1148
~ -[VMUKernelCoreMemoryScanner scanLocalMemory:atOffset:node:length:isa:scanCaches:fieldInfo:stride:recorder:] : 3148 -> 3096
CStrings:
+ ".X1"
```
