## leaks

> `/usr/bin/leaks`

```diff

-64566.82.1.0.0
-  __TEXT.__text: 0x19278
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x3380
-  __TEXT.__objc_methlist: 0x704
-  __TEXT.__const: 0x11c
-  __TEXT.__gcc_except_tab: 0xcf8
-  __TEXT.__cstring: 0x5320
-  __TEXT.__objc_methname: 0x3024
-  __TEXT.__objc_classname: 0x35
-  __TEXT.__objc_methtype: 0x219
+64570.34.1.0.0
+  __TEXT.__text: 0x171d0
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_stubs: 0x3260
+  __TEXT.__objc_methlist: 0x74c
+  __TEXT.__const: 0x138
+  __TEXT.__gcc_except_tab: 0xbe0
+  __TEXT.__cstring: 0x4f75
+  __TEXT.__objc_methname: 0x3015
+  __TEXT.__objc_classname: 0x4f
+  __TEXT.__objc_methtype: 0x256
   __TEXT.__oslogstring: 0xe96
-  __TEXT.__unwind_info: 0x488
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0xfe0
-  __DATA_CONST.__cfstring: 0x19a0
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x478
+  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0xe10
+  __DATA_CONST.__cfstring: 0x1900
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xee0
-  __DATA.__objc_selrefs: 0xd18
-  __DATA.__objc_ivar: 0x118
-  __DATA.__objc_data: 0xf0
+  __DATA.__objc_const: 0xff0
+  __DATA.__objc_selrefs: 0xce0
+  __DATA.__objc_ivar: 0x124
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x18
   __DATA.__crash_info: 0x40
   __DATA.__allow_alt_plat: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxcselect.dylib
-  UUID: 839D2DA2-68E9-3048-8606-A9A13C162871
-  Functions: 424
-  Symbols:   283
-  CStrings:  1380
+  UUID: ED671329-FEE0-37EC-BE27-318B6E4A0B83
+  Functions: 409
+  Symbols:   278
+  CStrings:  1359
 
Symbols:
+ _OBJC_CLASS_$_VMUAutoreleasePoolsAnalyzer
+ _VMUGraphNodeIsRoot
+ _VMUGraphNodeIsSpecialMallocNode
- OBJC_IVAR_$_VMUVMRegion.path
- _OBJC_CLASS_$_VMUProcessDescription
- _VMUCreateRootNodeMarkingMap
- _VMUGraphNodeType_IsRoot
- _kVMUAutoreleasePoolBoundaryClassName
- _kVMUAutoreleasePoolThreadSpecificDataKeyString
- _malloc_type_realloc
- _strtol
CStrings:
+ "@\"LeaksGlobals\""
+ "@\"VMUAutoreleasePoolsAnalyzer\""
+ "@32@0:8@16@24"
+ "AutoreleasePoolsPrinter"
+ "Number of autoreleases coalesced into previous entries: %d\n"
+ "Regular malloc blocks should not be root nodes of reference graph"
+ "SKIPPING PROCESS %5d: %s\n"
+ "SKIPPING PROCESS OF WRONG ARCHITECTURE:  %d %s\n"
+ "SKIP_WEBCONTENT"
+ "TI,R,N,V_totalEntriesInAutoreleasePools"
+ "Target process:  %@ [%u] (%@)\n"
+ "WebKit"
+ "_analyzer"
+ "_leaksGlobals"
+ "_totalEntriesInAutoreleasePools"
+ "autoreleasePoolsStatsInfo"
+ "core file"
+ "corpse"
+ "initWithGraph:options:"
+ "initWithGraph:regionIdentifier:debugTimer:"
+ "iterateAutoreleasePoolsInThreadsGroupingByType:showVirtualSize:extraReleasesCount:withBlock:"
+ "live task"
+ "printAutoreleasePoolsDetails"
+ "printAutoreleasePoolsPerThread"
+ "taskIsCorpse"
+ "totalEntriesInAutoreleasePools"
+ "v16@?0@\"NSString\"8"
- "        %u:  "
- "        Empty"
- "      POOL BOUNDARY"
- "     ** %u:  "
- "    %s\n"
- "    no autorelease pool"
- "   COALESCED AUTORELEASES: %u"
- "%*s"
- "%s%s\n"
- "--"
- "-al"
- "Autorelease pool pages not associated with a thread"
- "Expected non-nil srcCallTreeNode"
- "INCORRECT CHAIN OF @autoreleasepool content BLOCKS -- TRUNCATING THE CHAIN (autoreleasePoolChainCount %u, autoreleasePoolChainMax %u\n"
- "Malloc blocks should not be root nodes of reference graph"
- "NSString *memoryTreeHeldByAutoreleasedNode(LeakDetector *__strong, VMUMarkingMap *, VMUCallTreeNode *__unsafe_unretained *, uint32_t)"
- "NSString *memoryTreeHeldByAutoreleasedNode(LeakDetector *__strong, VMUMarkingMap *, VMUCallTreeNode *__unsafe_unretained *, uint32_t)_block_invoke"
- "No autorelease pools.\n"
- "Number of autoreleases coalesced into previous entries: %u\n"
- "Skipping process of wrong architecture:  %d %s\n"
- "Target process:  %@ [%u]\n"
- "Thread %u  %s\n"
- "_main_thread"
- "autoreleasePoolOffsets"
- "dyld"
- "expected autoreleasePoolChainCount %u to be less than autoreleasePoolChainMax %u\n"
- "graph"
- "initWithTask:getBinariesList:"
- "isStack"
- "markReachableNodesFromRoots:inMap:"
- "markReachableNodesFromRoots:inMap:options:"
- "no posix thread"
- "nodeDescription:usingDetails:"
- "nodeDetailIsAutoreleasePoolContentPage:"
- "nodeIsAutoreleasePoolContentPage:"
- "rangeForSymbolName:inRegion:"
- "removeObject:"
- "srcAddressToExtraAutoreleaseCountDict"
- "stringFromCallTreeWithOptions:"
- "threadNameForAddress:"
- "unsigned int printAutoreleasePools(VMUProcessObjectGraph *__strong, VMUTaskMemoryScanner *__strong, __strong id<VMUStackLogReader>)_block_invoke"
- "unsignedIntValue"
- "void printThreadAutoreleasePool(LeakDetector *__strong, uint32_t, NSMutableSet *__strong, VMUMarkingMap *)"

```
