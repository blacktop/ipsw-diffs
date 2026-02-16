## footprint

> `/usr/bin/footprint`

```diff

-310.0.0.0.0
-  __TEXT.__text: 0x1aef4
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x22e0
-  __TEXT.__objc_methlist: 0x115c
-  __TEXT.__cstring: 0x3440
+314.100.8.0.0
+  __TEXT.__text: 0x1c154
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_stubs: 0x2360
+  __TEXT.__objc_methlist: 0x11ac
+  __TEXT.__const: 0x200
+  __TEXT.__objc_methname: 0x23ab
+  __TEXT.__cstring: 0x351a
   __TEXT.__objc_classname: 0x206
-  __TEXT.__objc_methtype: 0x7bb
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x3d4
-  __TEXT.__objc_methname: 0x2356
+  __TEXT.__objc_methtype: 0x7b8
+  __TEXT.__gcc_except_tab: 0x3d0
   __TEXT.__ustring: 0xd0
   __TEXT.__oslogstring: 0x21
-  __TEXT.__unwind_info: 0x488
-  __DATA_CONST.__auth_got: 0x638
+  __TEXT.__unwind_info: 0x4f0
+  __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x17a8
-  __DATA_CONST.__cfstring: 0x2240
+  __DATA_CONST.__const: 0x17f0
+  __DATA_CONST.__cfstring: 0x22c0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2eb8
-  __DATA.__objc_selrefs: 0x9e0
-  __DATA.__objc_ivar: 0x290
+  __DATA.__objc_const: 0x2f40
+  __DATA.__objc_selrefs: 0xa00
+  __DATA.__objc_ivar: 0x29c
   __DATA.__objc_data: 0x780
   __DATA.__data: 0x250
   __DATA.__bss: 0x4140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: EB1E1A34-6111-3854-9C71-9E6435A484B4
-  Functions: 412
-  Symbols:   274
-  CStrings:  1448
+  UUID: 3FD4E65B-533F-3EA1-BEBE-8DB9DB4E7E42
+  Functions: 419
+  Symbols:   3479
+  CStrings:  1463
 
Symbols:
+ 
+ +[FPFootprint _totalForCategories:outTotal:]
+ +[FPFootprint breakDownPhysFootprint]
+ +[FPFootprint installCancelHandler:]
+ +[FPFootprint ioAccelMemoryInfoAvailable]
+ +[FPFootprint setBreakDownPhysFootprint:]
+ +[FPFootprint setVmRegionInfoFlags:]
+ +[FPKernelProcess _nameForWiredInfo:withKexts:andSymbolicator:zoneNames:zoneCount:]
+ +[FPMemgraphProcess processWithMemgraph:error:]
+ +[FPMemoryRegion categoryNameForTag:]
+ +[FPMemoryRegion vmLedgerNameForTag:]
+ +[FPProcess _nameForBsdInfo:]
+ +[FPProcess _nameForBsdInfoCommName:]
+ +[FPProcess allProcessesExcludingPids:]
+ +[FPProcess childPidsForPids:]
+ +[FPProcess pidsForStringDescriptions:errors:]
+ +[FPProcess processWithBsdInfo:]
+ +[FPProcess processWithPid:]
+ +[FPProcess removeIdleExitCleanProcessesFrom:]
+ +[FPSharedCache instanceCache]
+ +[FPSharedCache sharedCacheForDyldSnapshot:]
+ +[FPSystemMem getBootCarveoutSize]
+ +[FPTime now]
+ +[FPUserProcess _dirtyFlagsFromEntryState:]
+ -[FPAuxData .cxx_destruct]
+ -[FPAuxData description]
+ -[FPAuxData formattedValue]
+ -[FPAuxData formatter]
+ -[FPAuxData fp_isContainer]
+ -[FPAuxData fp_jsonRepresentation]
+ -[FPAuxData initWithValue:shouldAggregate:]
+ -[FPAuxData isEqual:]
+ -[FPAuxData setFormatter:]
+ -[FPAuxData shouldAggregate]
+ -[FPAuxData supportsFormattedValue]
+ -[FPAuxData value]
+ -[FPAuxDataInfo .cxx_destruct]
+ -[FPCorpseProcess _gatherProcessState]
+ -[FPCorpseProcess _isAlive]
+ -[FPCorpseProcess _populateTask]
+ -[FPCorpseProcess initWithCorpse:]
+ -[FPFootprint .cxx_destruct]
+ -[FPFootprint _categoriesForObjects:viewedByProcess:hasProcessView:summarize:]
+ -[FPFootprint _destroyMemoryObjectMaps]
+ -[FPFootprint _finalizeAndCompactMap:withName:]
+ -[FPFootprint _notHiddenProcesses]
+ -[FPFootprint analyzeData]
+ -[FPFootprint dealloc]
+ -[FPFootprint gatherData:]
+ -[FPFootprint initWithProcesses:]
+ -[FPFootprint ioAccelMemoryInfoDetailsAtAddress:for:error:]
+ -[FPFootprint ioSurfaceExtendedInfoDetailsAtAddress:for:]
+ -[FPFootprint printOutputVerbose:summarize:noCategories:]
+ -[FPFootprintArgs .cxx_destruct]
+ -[FPFootprintArgs targetProcessesAndError:]
+ -[FPImage .cxx_destruct]
+ -[FPImage setName:]
+ -[FPImageEnumerator .cxx_destruct]
+ -[FPImageEnumerator initWithImages:]
+ -[FPImageEnumerator nextImageForStart:end:]
+ -[FPKernelProcess .cxx_destruct]
+ -[FPKernelProcess _gatherPageSize]
+ -[FPKernelProcess _isAlive]
+ -[FPKernelProcess _populateTask]
+ -[FPKernelProcess auxData]
+ -[FPKernelProcess gatherData:extendedInfoProvider:]
+ -[FPKernelProcess initWithBsdInfo:]
+ -[FPMemgraphProcess .cxx_destruct]
+ -[FPMemgraphProcess _addSubrangesForRegion:purgeState:]
+ -[FPMemgraphProcess _configurePageSize]
+ -[FPMemgraphProcess _gatherImageData]
+ -[FPMemgraphProcess _gatherIsTranslated]
+ -[FPMemgraphProcess _gatherLedgers]
+ -[FPMemgraphProcess _gatherOwnedVmObjects]
+ -[FPMemgraphProcess _gatherPageSize]
+ -[FPMemgraphProcess _gatherProcessState]
+ -[FPMemgraphProcess _isAlive]
+ -[FPMemgraphProcess _populateMemoryRegionWithPageQueries:regionInfo:]
+ -[FPMemgraphProcess _populateTask]
+ -[FPMemgraphProcess breakDownPhysFootprint]
+ -[FPMemgraphProcess doOwnedAccountingAdjustments]
+ -[FPMemgraphProcess enumerateRegions:]
+ -[FPMemgraphProcess extendedInfoForRegionType:at:extendedInfoProvider:]
+ -[FPMemoryCategory .cxx_destruct]
+ -[FPMemoryCategory addMemoryObject:]
+ -[FPMemoryCategory auxDataFullName]
+ -[FPMemoryCategory auxData]
+ -[FPMemoryCategory detailedName]
+ -[FPMemoryCategory fullName]
+ -[FPMemoryCategory initSummary:]
+ -[FPMemoryCategory init]
+ -[FPMemoryCategory name]
+ -[FPMemoryCategory setTotalCleanSize:]
+ -[FPMemoryCategory setTotalDirtySize:]
+ -[FPMemoryCategory setTotalReclaimableSize:]
+ -[FPMemoryCategory setTotalRegions:]
+ -[FPMemoryCategory setTotalSwappedSize:]
+ -[FPMemoryCategory setTotalWiredSize:]
+ -[FPMemoryCategory totalCleanSize]
+ -[FPMemoryCategory totalDirtySize]
+ -[FPMemoryCategory totalReclaimableSize]
+ -[FPMemoryCategory totalRegions]
+ -[FPMemoryCategory totalSwappedSize]
+ -[FPMemoryCategory totalWiredSize]
+ -[FPMemoryMultiRegion .cxx_destruct]
+ -[FPMemoryMultiRegion auxDataName]
+ -[FPMemoryMultiRegion auxData]
+ -[FPMemoryMultiRegion regionSize]
+ -[FPMemoryMultiRegion setAuxDataName:]
+ -[FPMemoryMultiRegion setRegionSize:]
+ -[FPMemoryMultiRegion setTotalRegions:]
+ -[FPMemoryMultiRegion totalRegions]
+ -[FPMemoryObject .cxx_destruct]
+ -[FPMemoryObject _addRegion:forProcess:]
+ -[FPMemoryObject _canonicalRegion]
+ -[FPMemoryObject addRegion:forProcess:]
+ -[FPMemoryObject auxDataName]
+ -[FPMemoryObject auxData]
+ -[FPMemoryObject cleanSize]
+ -[FPMemoryObject containsFakeRegion]
+ -[FPMemoryObject copyWithZone:]
+ -[FPMemoryObject couldHaveProcessView]
+ -[FPMemoryObject detailedAuxDataName]
+ -[FPMemoryObject detailedAuxData]
+ -[FPMemoryObject detailedName]
+ -[FPMemoryObject dirtySize]
+ -[FPMemoryObject ensureMemoryObject]
+ -[FPMemoryObject finalizeObject]
+ -[FPMemoryObject finalizeUsingRegionDirtySize:]
+ -[FPMemoryObject fullName]
+ -[FPMemoryObject hasNoFootprint]
+ -[FPMemoryObject init]
+ -[FPMemoryObject name]
+ -[FPMemoryObject ownerPid]
+ -[FPMemoryObject reclaimableSize]
+ -[FPMemoryObject setOwnerPid:]
+ -[FPMemoryObject swappedSize]
+ -[FPMemoryObject totalRegions]
+ -[FPMemoryObject verbose]
+ -[FPMemoryObject viewForProcess:]
+ -[FPMemoryObject wiredSize]
+ -[FPMemoryRegion .cxx_destruct]
+ -[FPMemoryRegion addSubrange:memoryTotal:]
+ -[FPMemoryRegion auxDataName]
+ -[FPMemoryRegion auxData]
+ -[FPMemoryRegion cleanSize]
+ -[FPMemoryRegion containsFakeRegion]
+ -[FPMemoryRegion copyWithZone:]
+ -[FPMemoryRegion couldHaveProcessView]
+ -[FPMemoryRegion description]
+ -[FPMemoryRegion detailedAuxDataName]
+ -[FPMemoryRegion detailedAuxData]
+ -[FPMemoryRegion detailedName]
+ -[FPMemoryRegion dirtySize]
+ -[FPMemoryRegion eligibleForSubrangesUsingPageSize:]
+ -[FPMemoryRegion ensureMemoryObject]
+ -[FPMemoryRegion extendedInfo]
+ -[FPMemoryRegion finalizeObject]
+ -[FPMemoryRegion fullName]
+ -[FPMemoryRegion hasNoFootprint]
+ -[FPMemoryRegion name]
+ -[FPMemoryRegion ownerPid]
+ -[FPMemoryRegion privateSharedCacheRegion]
+ -[FPMemoryRegion reclaimableSize]
+ -[FPMemoryRegion setCleanSize:]
+ -[FPMemoryRegion setDetailedName:]
+ -[FPMemoryRegion setDirtySize:]
+ -[FPMemoryRegion setEnd:]
+ -[FPMemoryRegion setExtendedInfo:]
+ -[FPMemoryRegion setHasNoFootprint:]
+ -[FPMemoryRegion setName:]
+ -[FPMemoryRegion setReclaimableSize:]
+ -[FPMemoryRegion setSwappedSize:]
+ -[FPMemoryRegion setVerbose:]
+ -[FPMemoryRegion swappedSize]
+ -[FPMemoryRegion totalRegions]
+ -[FPMemoryRegion verbose]
+ -[FPMemoryRegion viewForProcess:]
+ -[FPMemoryRegion wiredSize]
+ -[FPOutputFormatterJSON .cxx_destruct]
+ -[FPOutputFormatterJSON JSONForAuxData:]
+ -[FPOutputFormatterJSON JSONForCategories:]
+ -[FPOutputFormatterJSON _emitTimeObjectForTime:label:]
+ -[FPOutputFormatterJSON close]
+ -[FPOutputFormatterJSON configureForMultipleOutputs]
+ -[FPOutputFormatterJSON dealloc]
+ -[FPOutputFormatterJSON endAtTime:]
+ -[FPOutputFormatterJSON endProcessHeader:]
+ -[FPOutputFormatterJSON initWithPath:]
+ -[FPOutputFormatterJSON printGlobalAuxData:]
+ -[FPOutputFormatterJSON printProcessAuxData:forProcess:]
+ -[FPOutputFormatterJSON printProcessCategories:total:forProcess:]
+ -[FPOutputFormatterJSON printProcessHeader:]
+ -[FPOutputFormatterJSON printProcessTotal:forProcess:]
+ -[FPOutputFormatterJSON printProcessesWithWarnings:processesWithErrors:globalErrors:]
+ -[FPOutputFormatterJSON printSharedCache:categories:sharedWith:total:]
+ -[FPOutputFormatterJSON printSharedCategories:sharedWith:forProcess:hasProcessView:total:]
+ -[FPOutputFormatterJSON printSummaryCategories:total:hadErrors:]
+ -[FPOutputFormatterJSON printVmmapLikeOutputForProcess:regions:]
+ -[FPOutputFormatterJSON startAtTime:]
+ -[FPOutputFormatterPerfdata .cxx_destruct]
+ -[FPOutputFormatterPerfdata _addCategories:]
+ -[FPOutputFormatterPerfdata _emitAuxData:parentMetric:processName:summaryTag:]
+ -[FPOutputFormatterPerfdata _emitCategoryAuxDataVariables:name:]
+ -[FPOutputFormatterPerfdata close]
+ -[FPOutputFormatterPerfdata configureForMultipleOutputs]
+ -[FPOutputFormatterPerfdata endAtTime:]
+ -[FPOutputFormatterPerfdata endProcessHeader:]
+ -[FPOutputFormatterPerfdata initWithPath:]
+ -[FPOutputFormatterPerfdata printGlobalAuxData:]
+ -[FPOutputFormatterPerfdata printProcessAuxData:forProcess:]
+ -[FPOutputFormatterPerfdata printProcessCategories:total:forProcess:]
+ -[FPOutputFormatterPerfdata printProcessHeader:]
+ -[FPOutputFormatterPerfdata printProcessTotal:forProcess:]
+ -[FPOutputFormatterPerfdata printProcessesWithWarnings:processesWithErrors:globalErrors:]
+ -[FPOutputFormatterPerfdata printSharedCache:categories:sharedWith:total:]
+ -[FPOutputFormatterPerfdata printSharedCategories:sharedWith:forProcess:hasProcessView:total:]
+ -[FPOutputFormatterPerfdata printSummaryCategories:total:hadErrors:]
+ -[FPOutputFormatterPerfdata startAtTime:]
+ -[FPOutputFormatterText .cxx_destruct]
+ -[FPOutputFormatterText _print:]
+ -[FPOutputFormatterText _printAuxData:withIndent:forProcess:]
+ -[FPOutputFormatterText _printCategories:forProcess:]
+ -[FPOutputFormatterText _printForProcess:verticalAlignment:format:]
+ -[FPOutputFormatterText _printHorizontallyForProcess:verticalAlignment:string:]
+ -[FPOutputFormatterText _printTotalFooter:forProcess:]
+ -[FPOutputFormatterText _truncatedNameForString:]
+ -[FPOutputFormatterText configureForMultipleOutputs]
+ -[FPOutputFormatterText endAtTime:]
+ -[FPOutputFormatterText endProcessHeader:]
+ -[FPOutputFormatterText formattedStringForSize:]
+ -[FPOutputFormatterText initWithSummaryFormat:options:sort:layoutStyle:]
+ -[FPOutputFormatterText printGlobalAuxData:]
+ -[FPOutputFormatterText printHeader]
+ -[FPOutputFormatterText printProcessAuxData:forProcess:]
+ -[FPOutputFormatterText printProcessCategories:total:forProcess:]
+ -[FPOutputFormatterText printProcessHeader:]
+ -[FPOutputFormatterText printProcessTotal:forProcess:]
+ -[FPOutputFormatterText printProcessesWithWarnings:processesWithErrors:globalErrors:]
+ -[FPOutputFormatterText printSharedCache:categories:sharedWith:total:]
+ -[FPOutputFormatterText printSharedCategories:sharedWith:forProcess:hasProcessView:total:]
+ -[FPOutputFormatterText printSummaryCategories:total:hadErrors:]
+ -[FPOutputFormatterText printVmmapLikeOutputForProcess:regions:]
+ -[FPOutputFormatterText startAtTime:]
+ -[FPProcess .cxx_destruct]
+ -[FPProcess _addGlobalError:]
+ -[FPProcess _gatherPageSize]
+ -[FPProcess _isAlive]
+ -[FPProcess _populateTask]
+ -[FPProcess asNumber]
+ -[FPProcess auxData]
+ -[FPProcess breakDownPhysFootprint]
+ -[FPProcess description]
+ -[FPProcess displayString]
+ -[FPProcess errors]
+ -[FPProcess extendedInfoForRegionType:at:extendedInfoProvider:]
+ -[FPProcess gatherData:extendedInfoProvider:]
+ -[FPProcess gatherData]
+ -[FPProcess globalErrors]
+ -[FPProcess hash]
+ -[FPProcess hiddenFromDisplay]
+ -[FPProcess idleExitStatus]
+ -[FPProcess initWithBsdInfo:]
+ -[FPProcess init]
+ -[FPProcess is64bit]
+ -[FPProcess isEqual:]
+ -[FPProcess isTranslated]
+ -[FPProcess memoryRegions]
+ -[FPProcess name]
+ -[FPProcess pageSize]
+ -[FPProcess pid]
+ -[FPProcess priority]
+ -[FPProcess setDisplayString:]
+ -[FPProcess setHiddenFromDisplay:]
+ -[FPProcess setIs64bit:]
+ -[FPProcess setIsTranslated:]
+ -[FPProcess setMemoryRegions:]
+ -[FPProcess setName:]
+ -[FPProcess setPageSize:]
+ -[FPProcess setPid:]
+ -[FPProcess setSharedCache:]
+ -[FPProcess sharedCache]
+ -[FPProcess warnings]
+ -[FPProcessGroup .cxx_destruct]
+ -[FPProcessGroup addObject:]
+ -[FPProcessGroup addProcess:]
+ -[FPProcessGroup attachCachedCategories:refcount:]
+ -[FPProcessGroup categoriesRefcount]
+ -[FPProcessGroup categories]
+ -[FPProcessGroup consumeCachedCategories]
+ -[FPProcessGroup copyWithZone:]
+ -[FPProcessGroup isEqual:]
+ -[FPProcessGroup setCategories:]
+ -[FPProcessGroup setCategoriesRefcount:]
+ -[FPProcessGroup setObjects:]
+ -[FPProcessGroupMinimal .cxx_destruct]
+ -[FPProcessGroupMinimal addProcess:]
+ -[FPProcessGroupMinimal description]
+ -[FPProcessGroupMinimal hash]
+ -[FPProcessGroupMinimal immutableCopy]
+ -[FPProcessGroupMinimal initUniqueProcessGroup]
+ -[FPProcessGroupMinimal initWithHashValue:]
+ -[FPProcessGroupMinimal init]
+ -[FPProcessGroupMinimal isEqual:]
+ -[FPProcessGroupMinimal processes]
+ -[FPProcessGroupMinimal setProcesses:]
+ -[FPRangeList _addRangeList:]
+ -[FPRangeList addRange:memoryTotal:]
+ -[FPRangeList addRegion:]
+ -[FPRangeList dealloc]
+ -[FPRangeList enumerateUsingBlock:]
+ -[FPRangeList sum]
+ -[FPSharedCache .cxx_destruct]
+ -[FPSharedCache copyWithZone:]
+ -[FPSharedCache initWithUUID:baseAddress:mappedSize:slide:]
+ -[FPSystemMem gatherData:]
+ -[FPSystemMem init]
+ -[FPTime date]
+ -[FPTime init]
+ -[FPTime machAbsoluteTimeNsec]
+ -[FPTime machContinuousTimeNsec]
+ -[FPUserProcess .cxx_destruct]
+ -[FPUserProcess _addErrnoWarningWithDescription:]
+ -[FPUserProcess _addSubrangesForRegion:purgeState:]
+ -[FPUserProcess _configurePageSize]
+ -[FPUserProcess _drainDeferredReclaim]
+ -[FPUserProcess _enumerateDispositionChunksWithStartAddr:pagesToQuery:block:]
+ -[FPUserProcess _gatherImageData]
+ -[FPUserProcess _gatherIsTranslated]
+ -[FPUserProcess _gatherLedgers]
+ -[FPUserProcess _gatherOwnedVmObjects]
+ -[FPUserProcess _gatherProcessState]
+ -[FPUserProcess _gatherSharedCacheFromDyldSnapshot:]
+ -[FPUserProcess _isAlive]
+ -[FPUserProcess _populateMemoryRegionWithPageQueries:regionInfo:]
+ -[FPUserProcess _populateTask]
+ -[FPUserProcess _processMachVMError:withDescription:]
+ -[FPUserProcess _setIdleExitStatusFromDirtyFlags:]
+ -[FPUserProcess _setPriority:]
+ -[FPUserProcess addLedgerData:count:]
+ -[FPUserProcess auxData]
+ -[FPUserProcess dealloc]
+ -[FPUserProcess doOwnedAccountingAdjustments]
+ -[FPUserProcess enumerateRegions:]
+ -[FPUserProcess extendedInfoForRegionType:at:extendedInfoProvider:]
+ -[FPUserProcess gatherData:extendedInfoProvider:]
+ -[FPUserProcess initWithBsdInfo:]
+ -[FPUserProcess physFootprint]
+ -[FPUserProcess task]
+ -[NSArray(FastBatchEnumeration) fp_enumerateObjectsWithBatchSize:usingBlock:]
+ -[NSDictionary(FPAuxData) fp_isContainer]
+ -[NSDictionary(FPAuxData) fp_jsonRepresentation]
+ -[NSDictionary(FPAuxData) fp_mergeAuxDatum:withDatum:forceAggregate:]
+ -[NSDictionary(FPAuxData) fp_mergeWithData:]
+ -[NSDictionary(FPAuxData) fp_mergeWithData:forceAggregate:]
+ -[NSEnumerator(FastBatchEnumeration) fp_enumerateObjectsWithBatchSize:usingBlock:]
+ .str
+ .str.1
+ .str.2
+ .str.244
+ .str.245
+ .str.3
+ .str.4
+ .str.5
+ .str.6
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/0.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/1.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/10.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/11.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/12.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/13.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/14.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/15.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/16.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/17.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/18.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/19.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/2.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/20.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/21.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/22.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/23.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/24.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/25.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/3.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/4.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/5.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/6.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/7.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/8.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Sources/footprint_darwinOS/footprint/
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Sources/footprint_darwinOS/footprint/Import Hacks/
+ /Library/Caches/com.apple.xbs/C8C57B89-3F7E-45C0-8AE0-E808FC2B7509/TemporaryDirectory.MbYxAb/Sources/footprint_darwinOS/shared/
+ FPAuxData.m
+ FPCorpseProcess.m
+ FPCorpseUtils.m
+ FPFootprint.m
+ FPImage.m
+ FPKernelProcess.m
+ FPLedgerIndexForLedger.ledgerIndexMap
+ FPLedgerIndexForLedger.onceToken
+ FPMemgraphProcess.m
+ FPMemoryCategory.m
+ FPMemoryObject.m
+ FPMemoryRegion.m
+ FPOutputFormatterJSON.m
+ FPOutputFormatterPerfdata.m
+ FPOutputFormatterText.m
+ FPProcess.m
+ FPProcessGroup.m
+ FPRangeList.m
+ FPSharedCache.m
+ FPSystemMem.m
+ FPTime.m
+ FPUserProcess.m
+ FastBatchEnumeration.m
+ GCC_except_table0
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table2
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table3
+ GCC_except_table4
+ GCC_except_table8
+ Kernel-arm-cpu_capabilities.c
+ LedgerSupport.m
+ OBJC_IVAR_$_FPAuxData._aggregate
+ OBJC_IVAR_$_FPAuxData._formatter
+ OBJC_IVAR_$_FPAuxData._value
+ OBJC_IVAR_$_FPAuxDataInfo._dictionary
+ OBJC_IVAR_$_FPAuxDataInfo._fullName
+ OBJC_IVAR_$_FPFootprint._allPIDsIOAccelMemoryInfos
+ OBJC_IVAR_$_FPFootprint._allPIDsIOAccelMemoryInfosLock
+ OBJC_IVAR_$_FPFootprint._allPIDsIOSurfaceDescriptions
+ OBJC_IVAR_$_FPFootprint._allPIDsIOSurfaceDescriptionsLock
+ OBJC_IVAR_$_FPFootprint._earlyExit
+ OBJC_IVAR_$_FPFootprint._gatherEndTime
+ OBJC_IVAR_$_FPFootprint._gatherStartTime
+ OBJC_IVAR_$_FPFootprint._linkeditMemoryObjects
+ OBJC_IVAR_$_FPFootprint._memoryObjectMapsInitialized
+ OBJC_IVAR_$_FPFootprint._memoryObjects
+ OBJC_IVAR_$_FPFootprint._outputFormatters
+ OBJC_IVAR_$_FPFootprint._pidToFootprint
+ OBJC_IVAR_$_FPFootprint._processes
+ OBJC_IVAR_$_FPFootprint._qualityOfService
+ OBJC_IVAR_$_FPFootprint._sharedCacheMemoryObjectsTable
+ OBJC_IVAR_$_FPFootprint._sysData
+ OBJC_IVAR_$_FPFootprint._textMemoryObjects
+ OBJC_IVAR_$_FPFootprint.sysMemData
+ OBJC_IVAR_$_FPFootprintArgs._JSONOutputFile
+ OBJC_IVAR_$_FPFootprintArgs._didSetShouldGetPhysFootprintBreakdown
+ OBJC_IVAR_$_FPFootprintArgs._drainDeferredReclaim
+ OBJC_IVAR_$_FPFootprintArgs._excludeSelf
+ OBJC_IVAR_$_FPFootprintArgs._excludedPidsOrProcesses
+ OBJC_IVAR_$_FPFootprintArgs._forkCorpse
+ OBJC_IVAR_$_FPFootprintArgs._includeSysFootprint
+ OBJC_IVAR_$_FPFootprintArgs._minFootprintMB
+ OBJC_IVAR_$_FPFootprintArgs._noCategories
+ OBJC_IVAR_$_FPFootprintArgs._perfdataOutputFile
+ OBJC_IVAR_$_FPFootprintArgs._potentialTargetProcesses
+ OBJC_IVAR_$_FPFootprintArgs._printingOptions
+ OBJC_IVAR_$_FPFootprintArgs._sampleDuration
+ OBJC_IVAR_$_FPFootprintArgs._sampleInterval
+ OBJC_IVAR_$_FPFootprintArgs._searchForUnmapped
+ OBJC_IVAR_$_FPFootprintArgs._shouldGetPhysFootprintBreakdown
+ OBJC_IVAR_$_FPFootprintArgs._skipIdleExitClean
+ OBJC_IVAR_$_FPFootprintArgs._summaryFormat
+ OBJC_IVAR_$_FPFootprintArgs._targetAll
+ OBJC_IVAR_$_FPFootprintArgs._targetChildren
+ OBJC_IVAR_$_FPFootprintArgs._targetPids
+ OBJC_IVAR_$_FPFootprintArgs._textLayoutStyle
+ OBJC_IVAR_$_FPFootprintArgs._textOptions
+ OBJC_IVAR_$_FPFootprintArgs._textSort
+ OBJC_IVAR_$_FPImage._name
+ OBJC_IVAR_$_FPImage._ownerPath
+ OBJC_IVAR_$_FPImage._segment
+ OBJC_IVAR_$_FPImage._size
+ OBJC_IVAR_$_FPImage._start
+ OBJC_IVAR_$_FPImageEnumerator._images
+ OBJC_IVAR_$_FPImageEnumerator._index
+ OBJC_IVAR_$_FPMemgraphProcess._graph
+ OBJC_IVAR_$_FPMemoryCategory._firstMemoryObject
+ OBJC_IVAR_$_FPMemoryCategory._isSummary
+ OBJC_IVAR_$_FPMemoryCategory._name
+ OBJC_IVAR_$_FPMemoryCategory._totalCleanSize
+ OBJC_IVAR_$_FPMemoryCategory._totalDirtySize
+ OBJC_IVAR_$_FPMemoryCategory._totalReclaimableSize
+ OBJC_IVAR_$_FPMemoryCategory._totalRegions
+ OBJC_IVAR_$_FPMemoryCategory._totalSwappedSize
+ OBJC_IVAR_$_FPMemoryCategory._totalWiredSize
+ OBJC_IVAR_$_FPMemoryMultiRegion._auxDataName
+ OBJC_IVAR_$_FPMemoryMultiRegion._regionSize
+ OBJC_IVAR_$_FPMemoryMultiRegion._totalRegions
+ OBJC_IVAR_$_FPMemoryObject._accurateSizes
+ OBJC_IVAR_$_FPMemoryObject._cleanSize
+ OBJC_IVAR_$_FPMemoryObject._dirtySize
+ OBJC_IVAR_$_FPMemoryObject._hasNoFootprint
+ OBJC_IVAR_$_FPMemoryObject._hasProcessViewForSingleTotalRegions
+ OBJC_IVAR_$_FPMemoryObject._isProcessViewForSingleTotalRegions
+ OBJC_IVAR_$_FPMemoryObject._memoryRegions
+ OBJC_IVAR_$_FPMemoryObject._ownerPid
+ OBJC_IVAR_$_FPMemoryObject._processMemoryRegions
+ OBJC_IVAR_$_FPMemoryObject._reclaimableSize
+ OBJC_IVAR_$_FPMemoryObject._swappedSize
+ OBJC_IVAR_$_FPMemoryObject._wiredSize
+ OBJC_IVAR_$_FPMemoryRegion._cleanSize
+ OBJC_IVAR_$_FPMemoryRegion._detailedName
+ OBJC_IVAR_$_FPMemoryRegion._dirtySize
+ OBJC_IVAR_$_FPMemoryRegion._hasNoFootprint
+ OBJC_IVAR_$_FPMemoryRegion._inSharedCache
+ OBJC_IVAR_$_FPMemoryRegion._memoryObject
+ OBJC_IVAR_$_FPMemoryRegion._name
+ OBJC_IVAR_$_FPMemoryRegion._object_id
+ OBJC_IVAR_$_FPMemoryRegion._offset
+ OBJC_IVAR_$_FPMemoryRegion._ownedExclusivelyByParentProcess
+ OBJC_IVAR_$_FPMemoryRegion._reclaimableSize
+ OBJC_IVAR_$_FPMemoryRegion._segment
+ OBJC_IVAR_$_FPMemoryRegion._share_mode
+ OBJC_IVAR_$_FPMemoryRegion._size
+ OBJC_IVAR_$_FPMemoryRegion._start
+ OBJC_IVAR_$_FPMemoryRegion._subrangeList
+ OBJC_IVAR_$_FPMemoryRegion._swappedSize
+ OBJC_IVAR_$_FPMemoryRegion._unusedSharedCacheRegion
+ OBJC_IVAR_$_FPMemoryRegion._user_tag
+ OBJC_IVAR_$_FPMemoryRegion._verbose
+ OBJC_IVAR_$_FPMemoryRegion._wired
+ OBJC_IVAR_$_FPOutputFormatterJSON._addedProcessGroups
+ OBJC_IVAR_$_FPOutputFormatterJSON._dateFormatter
+ OBJC_IVAR_$_FPOutputFormatterJSON._json
+ OBJC_IVAR_$_FPOutputFormatterJSON._multipleOutputs
+ OBJC_IVAR_$_FPOutputFormatterJSON._pageSize
+ OBJC_IVAR_$_FPOutputFormatterJSON._shared
+ OBJC_IVAR_$_FPOutputFormatterJSON._verbose
+ OBJC_IVAR_$_FPOutputFormatterPerfdata._currentProcessAuxDatas
+ OBJC_IVAR_$_FPOutputFormatterPerfdata._currentProcessTotals
+ OBJC_IVAR_$_FPOutputFormatterPerfdata._startTime
+ OBJC_IVAR_$_FPOutputFormatterPerfdata._writer
+ OBJC_IVAR_$_FPOutputFormatterText._dateFormatter
+ OBJC_IVAR_$_FPOutputFormatterText._layoutStyle
+ OBJC_IVAR_$_FPOutputFormatterText._maxTextLengthByPID
+ OBJC_IVAR_$_FPOutputFormatterText._multipleOutputs
+ OBJC_IVAR_$_FPOutputFormatterText._options
+ OBJC_IVAR_$_FPOutputFormatterText._orderedProcesses
+ OBJC_IVAR_$_FPOutputFormatterText._output
+ OBJC_IVAR_$_FPOutputFormatterText._outputLinesByPID
+ OBJC_IVAR_$_FPOutputFormatterText._pageSize
+ OBJC_IVAR_$_FPOutputFormatterText._prefix
+ OBJC_IVAR_$_FPOutputFormatterText._processCount
+ OBJC_IVAR_$_FPOutputFormatterText._sort
+ OBJC_IVAR_$_FPOutputFormatterText._suffix
+ OBJC_IVAR_$_FPOutputFormatterText._summaryFormat
+ OBJC_IVAR_$_FPOutputFormatterText._swappedColumnName
+ OBJC_IVAR_$_FPOutputFormatterText._verbose
+ OBJC_IVAR_$_FPOutputFormatterText._wiredColumnName
+ OBJC_IVAR_$_FPProcess._displayString
+ OBJC_IVAR_$_FPProcess._errors
+ OBJC_IVAR_$_FPProcess._globalErrors
+ OBJC_IVAR_$_FPProcess._hiddenFromDisplay
+ OBJC_IVAR_$_FPProcess._idleExitStatus
+ OBJC_IVAR_$_FPProcess._is64bit
+ OBJC_IVAR_$_FPProcess._isTranslated
+ OBJC_IVAR_$_FPProcess._memoryRegions
+ OBJC_IVAR_$_FPProcess._name
+ OBJC_IVAR_$_FPProcess._pageSize
+ OBJC_IVAR_$_FPProcess._pid
+ OBJC_IVAR_$_FPProcess._priority
+ OBJC_IVAR_$_FPProcess._sharedCache
+ OBJC_IVAR_$_FPProcess._warnings
+ OBJC_IVAR_$_FPProcessGroup._categories
+ OBJC_IVAR_$_FPProcessGroup._categoriesRefcount
+ OBJC_IVAR_$_FPProcessGroup._objects
+ OBJC_IVAR_$_FPProcessGroupMinimal._hashValue
+ OBJC_IVAR_$_FPProcessGroupMinimal._processes
+ OBJC_IVAR_$_FPRangeList._rangeListHead
+ OBJC_IVAR_$_FPSharedCache._alignment
+ OBJC_IVAR_$_FPSharedCache._baseAddress
+ OBJC_IVAR_$_FPSharedCache._mappedSize
+ OBJC_IVAR_$_FPSharedCache._slide
+ OBJC_IVAR_$_FPSharedCache._uuid
+ OBJC_IVAR_$_FPSystemMem._bootCarveoutSize
+ OBJC_IVAR_$_FPTime._machAbsoluteTime
+ OBJC_IVAR_$_FPTime._machContinuousTime
+ OBJC_IVAR_$_FPTime._wallTime
+ OBJC_IVAR_$_FPUserProcess._bailedOut
+ OBJC_IVAR_$_FPUserProcess._images
+ OBJC_IVAR_$_FPUserProcess._ledgers
+ OBJC_IVAR_$_FPUserProcess._ownedVmObjects
+ OBJC_IVAR_$_FPUserProcess._task
+ System-mach-arm-vm_param.c
+ _FPExtractCorpseInfoWithBlock
+ _FPFootprintBreakDownPhysFootprint
+ _FPFootprintErrorDomain
+ _FPFootprintSharingAnalysisDisabled
+ _FPIOAccelMemoryInfoCachedCopyKey
+ _FPIOAccelMemoryInfoDescriptionsKey
+ _FPIOAccelMemoryInfoDirtySizeKey
+ _FPIOAccelMemoryInfoIsPurgeableKey
+ _FPIOAccelMemoryInfoIsWiredKey
+ _FPIOAccelMemoryInfoMemoryPoolKey
+ _FPIOAccelMemoryInfoResidentSizeKey
+ _FPIOAccelMemoryInfoSizeKey
+ _FPIOAccelMemoryInfoSurfaceIDKey
+ _FPIOSurfaceInfoHeightKey
+ _FPIOSurfaceInfoNameKey
+ _FPIOSurfaceInfoPixelFormatKey
+ _FPIOSurfaceInfoSizeKey
+ _FPIOSurfaceInfoSurfaceIDKey
+ _FPIOSurfaceInfoWidthKey
+ _FPLedgerCreateInfoForPid
+ _FPLedgerNameForLedger
+ _FPLedgerValueForId
+ _FPTextAllColumns
+ _FPTextColumnCategory
+ _FPTextColumnClean
+ _FPTextColumnDirty
+ _FPTextColumnReclaimable
+ _FPTextColumnRegions
+ _FPTextColumnSwapped
+ _FPTextColumnWired
+ _KERNEL_COMM_PAGE64_NESTING_SIZE
+ _KERNEL_COMM_PAGE64_NESTING_START
+ _OBJC_$_PROP_LIST_FPMemoryObject.130
+ _OBJC_CLASS_$_FPAuxData
+ _OBJC_CLASS_$_FPAuxDataInfo
+ _OBJC_CLASS_$_FPCorpseProcess
+ _OBJC_CLASS_$_FPFootprint
+ _OBJC_CLASS_$_FPFootprintArgs
+ _OBJC_CLASS_$_FPImage
+ _OBJC_CLASS_$_FPImageEnumerator
+ _OBJC_CLASS_$_FPKernelProcess
+ _OBJC_CLASS_$_FPMemgraphProcess
+ _OBJC_CLASS_$_FPMemoryCategory
+ _OBJC_CLASS_$_FPMemoryMultiRegion
+ _OBJC_CLASS_$_FPMemoryObject
+ _OBJC_CLASS_$_FPMemoryRegion
+ _OBJC_CLASS_$_FPOutputFormatterJSON
+ _OBJC_CLASS_$_FPOutputFormatterPerfdata
+ _OBJC_CLASS_$_FPOutputFormatterText
+ _OBJC_CLASS_$_FPProcess
+ _OBJC_CLASS_$_FPProcessGroup
+ _OBJC_CLASS_$_FPProcessGroupMinimal
+ _OBJC_CLASS_$_FPRangeList
+ _OBJC_CLASS_$_FPSharedCache
+ _OBJC_CLASS_$_FPSystemMem
+ _OBJC_CLASS_$_FPTime
+ _OBJC_CLASS_$_FPUserProcess
+ _OBJC_METACLASS_$_FPAuxData
+ _OBJC_METACLASS_$_FPAuxDataInfo
+ _OBJC_METACLASS_$_FPCorpseProcess
+ _OBJC_METACLASS_$_FPFootprint
+ _OBJC_METACLASS_$_FPFootprintArgs
+ _OBJC_METACLASS_$_FPImage
+ _OBJC_METACLASS_$_FPImageEnumerator
+ _OBJC_METACLASS_$_FPKernelProcess
+ _OBJC_METACLASS_$_FPMemgraphProcess
+ _OBJC_METACLASS_$_FPMemoryCategory
+ _OBJC_METACLASS_$_FPMemoryMultiRegion
+ _OBJC_METACLASS_$_FPMemoryObject
+ _OBJC_METACLASS_$_FPMemoryRegion
+ _OBJC_METACLASS_$_FPOutputFormatterJSON
+ _OBJC_METACLASS_$_FPOutputFormatterPerfdata
+ _OBJC_METACLASS_$_FPOutputFormatterText
+ _OBJC_METACLASS_$_FPProcess
+ _OBJC_METACLASS_$_FPProcessGroup
+ _OBJC_METACLASS_$_FPProcessGroupMinimal
+ _OBJC_METACLASS_$_FPRangeList
+ _OBJC_METACLASS_$_FPSharedCache
+ _OBJC_METACLASS_$_FPSystemMem
+ _OBJC_METACLASS_$_FPTime
+ _OBJC_METACLASS_$_FPUserProcess
+ _SYSTEM_MACH_VM_MAX_GPU_CARVEOUT_ADDRESS
+ _SYSTEM_MACH_VM_MIN_GPU_CARVEOUT_ADDRESS
+ __Block_byref_object_copy_.181
+ __Block_byref_object_dispose_.182
+ __FPRangeListAddNode
+ __FPRangeListSplitNodeAtIntersection
+ __MergedGlobals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_FastBatchEnumeration
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_FPAuxData
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSEnumerator_$_FastBatchEnumeration
+ __OBJC_$_CATEGORY_NSArray_$_FastBatchEnumeration
+ __OBJC_$_CATEGORY_NSDictionary_$_FPAuxData
+ __OBJC_$_CATEGORY_NSEnumerator_$_FastBatchEnumeration
+ __OBJC_$_CLASS_METHODS_FPMemgraphProcess
+ __OBJC_$_CLASS_METHODS_FPProcess
+ __OBJC_$_CLASS_METHODS_FPSystemMem
+ __OBJC_$_CLASS_METHODS_FPUserProcess
+ __OBJC_$_INSTANCE_METHODS_FPAuxData
+ __OBJC_$_INSTANCE_METHODS_FPAuxDataInfo
+ __OBJC_$_INSTANCE_METHODS_FPCorpseProcess
+ __OBJC_$_INSTANCE_METHODS_FPFootprint
+ __OBJC_$_INSTANCE_METHODS_FPFootprintArgs
+ __OBJC_$_INSTANCE_METHODS_FPImage
+ __OBJC_$_INSTANCE_METHODS_FPImageEnumerator
+ __OBJC_$_INSTANCE_METHODS_FPKernelProcess
+ __OBJC_$_INSTANCE_METHODS_FPMemgraphProcess
+ __OBJC_$_INSTANCE_METHODS_FPMemoryCategory
+ __OBJC_$_INSTANCE_METHODS_FPMemoryMultiRegion
+ __OBJC_$_INSTANCE_METHODS_FPMemoryObject
+ __OBJC_$_INSTANCE_METHODS_FPMemoryRegion
+ __OBJC_$_INSTANCE_METHODS_FPOutputFormatterJSON
+ __OBJC_$_INSTANCE_METHODS_FPOutputFormatterPerfdata
+ __OBJC_$_INSTANCE_METHODS_FPOutputFormatterText
+ __OBJC_$_INSTANCE_METHODS_FPProcess
+ __OBJC_$_INSTANCE_METHODS_FPProcessGroup
+ __OBJC_$_INSTANCE_METHODS_FPProcessGroupMinimal
+ __OBJC_$_INSTANCE_METHODS_FPRangeList
+ __OBJC_$_INSTANCE_METHODS_FPSharedCache
+ __OBJC_$_INSTANCE_METHODS_FPSystemMem
+ __OBJC_$_INSTANCE_METHODS_FPTime
+ __OBJC_$_INSTANCE_METHODS_FPUserProcess
+ __OBJC_$_INSTANCE_VARIABLES_FPAuxData
+ __OBJC_$_INSTANCE_VARIABLES_FPAuxDataInfo
+ __OBJC_$_INSTANCE_VARIABLES_FPFootprint
+ __OBJC_$_INSTANCE_VARIABLES_FPFootprintArgs
+ __OBJC_$_INSTANCE_VARIABLES_FPImage
+ __OBJC_$_INSTANCE_VARIABLES_FPImageEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_FPKernelProcess
+ __OBJC_$_INSTANCE_VARIABLES_FPMemgraphProcess
+ __OBJC_$_INSTANCE_VARIABLES_FPMemoryCategory
+ __OBJC_$_INSTANCE_VARIABLES_FPMemoryMultiRegion
+ __OBJC_$_INSTANCE_VARIABLES_FPMemoryObject
+ __OBJC_$_INSTANCE_VARIABLES_FPMemoryRegion
+ __OBJC_$_INSTANCE_VARIABLES_FPOutputFormatterJSON
+ __OBJC_$_INSTANCE_VARIABLES_FPOutputFormatterPerfdata
+ __OBJC_$_INSTANCE_VARIABLES_FPOutputFormatterText
+ __OBJC_$_INSTANCE_VARIABLES_FPProcess
+ __OBJC_$_INSTANCE_VARIABLES_FPProcessGroup
+ __OBJC_$_INSTANCE_VARIABLES_FPProcessGroupMinimal
+ __OBJC_$_INSTANCE_VARIABLES_FPRangeList
+ __OBJC_$_INSTANCE_VARIABLES_FPSharedCache
+ __OBJC_$_INSTANCE_VARIABLES_FPSystemMem
+ __OBJC_$_INSTANCE_VARIABLES_FPTime
+ __OBJC_$_INSTANCE_VARIABLES_FPUserProcess
+ __OBJC_$_PROP_LIST_FPAuxData
+ __OBJC_$_PROP_LIST_FPAuxDataType
+ __OBJC_$_PROP_LIST_FPFootprint
+ __OBJC_$_PROP_LIST_FPMemoryCategory
+ __OBJC_$_PROP_LIST_FPMemoryMultiRegion
+ __OBJC_$_PROP_LIST_FPMemoryObject
+ __OBJC_$_PROP_LIST_FPMemoryRegion
+ __OBJC_$_PROP_LIST_FPOutputFormatterJSON
+ __OBJC_$_PROP_LIST_FPOutputFormatterPerfdata
+ __OBJC_$_PROP_LIST_FPOutputFormatterText
+ __OBJC_$_PROP_LIST_FPProcess
+ __OBJC_$_PROP_LIST_FPProcessGroup
+ __OBJC_$_PROP_LIST_FPProcessGroupMinimal
+ __OBJC_$_PROP_LIST_FPUserProcess
+ __OBJC_$_PROP_LIST_NSDictionary_$_FPAuxData
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPAuxDataType
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPFootprintExtendedInfoProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPMemoryObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FPOutputFormatter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FPOutputFormatter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPAuxDataType
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPFootprintExtendedInfoProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPMemoryObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FPOutputFormatter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_FPFootprintExtendedInfoProvider
+ __OBJC_$_PROTOCOL_REFS_FPMemoryObject
+ __OBJC_$_PROTOCOL_REFS_FPOutputFormatter
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDictionary_$_FPAuxData
+ __OBJC_CLASS_PROTOCOLS_$_FPAuxData
+ __OBJC_CLASS_PROTOCOLS_$_FPFootprint
+ __OBJC_CLASS_PROTOCOLS_$_FPMemoryObject
+ __OBJC_CLASS_PROTOCOLS_$_FPMemoryRegion
+ __OBJC_CLASS_PROTOCOLS_$_FPOutputFormatterJSON
+ __OBJC_CLASS_PROTOCOLS_$_FPOutputFormatterPerfdata
+ __OBJC_CLASS_PROTOCOLS_$_FPOutputFormatterText
+ __OBJC_CLASS_PROTOCOLS_$_FPProcessGroup
+ __OBJC_CLASS_PROTOCOLS_$_FPSharedCache
+ __OBJC_CLASS_RO_$_FPAuxData
+ __OBJC_CLASS_RO_$_FPAuxDataInfo
+ __OBJC_CLASS_RO_$_FPCorpseProcess
+ __OBJC_CLASS_RO_$_FPFootprint
+ __OBJC_CLASS_RO_$_FPFootprintArgs
+ __OBJC_CLASS_RO_$_FPImage
+ __OBJC_CLASS_RO_$_FPImageEnumerator
+ __OBJC_CLASS_RO_$_FPKernelProcess
+ __OBJC_CLASS_RO_$_FPMemgraphProcess
+ __OBJC_CLASS_RO_$_FPMemoryCategory
+ __OBJC_CLASS_RO_$_FPMemoryMultiRegion
+ __OBJC_CLASS_RO_$_FPMemoryObject
+ __OBJC_CLASS_RO_$_FPMemoryRegion
+ __OBJC_CLASS_RO_$_FPOutputFormatterJSON
+ __OBJC_CLASS_RO_$_FPOutputFormatterPerfdata
+ __OBJC_CLASS_RO_$_FPOutputFormatterText
+ __OBJC_CLASS_RO_$_FPProcess
+ __OBJC_CLASS_RO_$_FPProcessGroup
+ __OBJC_CLASS_RO_$_FPProcessGroupMinimal
+ __OBJC_CLASS_RO_$_FPRangeList
+ __OBJC_CLASS_RO_$_FPSharedCache
+ __OBJC_CLASS_RO_$_FPSystemMem
+ __OBJC_CLASS_RO_$_FPTime
+ __OBJC_CLASS_RO_$_FPUserProcess
+ __OBJC_LABEL_PROTOCOL_$_FPAuxDataType
+ __OBJC_LABEL_PROTOCOL_$_FPFootprintExtendedInfoProvider
+ __OBJC_LABEL_PROTOCOL_$_FPMemoryObject
+ __OBJC_LABEL_PROTOCOL_$_FPOutputFormatter
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_FPAuxData
+ __OBJC_METACLASS_RO_$_FPAuxDataInfo
+ __OBJC_METACLASS_RO_$_FPCorpseProcess
+ __OBJC_METACLASS_RO_$_FPFootprint
+ __OBJC_METACLASS_RO_$_FPFootprintArgs
+ __OBJC_METACLASS_RO_$_FPImage
+ __OBJC_METACLASS_RO_$_FPImageEnumerator
+ __OBJC_METACLASS_RO_$_FPKernelProcess
+ __OBJC_METACLASS_RO_$_FPMemgraphProcess
+ __OBJC_METACLASS_RO_$_FPMemoryCategory
+ __OBJC_METACLASS_RO_$_FPMemoryMultiRegion
+ __OBJC_METACLASS_RO_$_FPMemoryObject
+ __OBJC_METACLASS_RO_$_FPMemoryRegion
+ __OBJC_METACLASS_RO_$_FPOutputFormatterJSON
+ __OBJC_METACLASS_RO_$_FPOutputFormatterPerfdata
+ __OBJC_METACLASS_RO_$_FPOutputFormatterText
+ __OBJC_METACLASS_RO_$_FPProcess
+ __OBJC_METACLASS_RO_$_FPProcessGroup
+ __OBJC_METACLASS_RO_$_FPProcessGroupMinimal
+ __OBJC_METACLASS_RO_$_FPRangeList
+ __OBJC_METACLASS_RO_$_FPSharedCache
+ __OBJC_METACLASS_RO_$_FPSystemMem
+ __OBJC_METACLASS_RO_$_FPTime
+ __OBJC_METACLASS_RO_$_FPUserProcess
+ __OBJC_PROTOCOL_$_FPAuxDataType
+ __OBJC_PROTOCOL_$_FPFootprintExtendedInfoProvider
+ __OBJC_PROTOCOL_$_FPMemoryObject
+ __OBJC_PROTOCOL_$_FPOutputFormatter
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSObject
+ ___24-[FPUserProcess auxData]_block_invoke
+ ___24-[FPUserProcess auxData]_block_invoke_2
+ ___26-[FPFootprint gatherData:]_block_invoke
+ ___33-[FPUserProcess _gatherImageData]_block_invoke
+ ___33-[FPUserProcess _gatherImageData]_block_invoke_2
+ ___33-[FPUserProcess _gatherImageData]_block_invoke_3
+ ___34-[FPCorpseProcess initWithCorpse:]_block_invoke
+ ___37+[FPMemoryRegion categoryNameForTag:]_block_invoke
+ ___38-[FPMemgraphProcess enumerateRegions:]_block_invoke
+ ___42+[FPFootprint _processesBySortingPidDesc:]_block_invoke
+ ___43-[FPOutputFormatterJSON JSONForCategories:]_block_invoke
+ ___44+[FPSharedCache sharedCacheForDyldSnapshot:]_block_invoke
+ ___44+[FPSharedCache sharedCacheForDyldSnapshot:]_block_invoke_2
+ ___44-[FPFootprint _processesBySortingFootprint:]_block_invoke
+ ___44-[FPOutputFormatterJSON printProcessHeader:]_block_invoke
+ ___44-[FPOutputFormatterJSON printProcessHeader:]_block_invoke_2
+ ___47-[FPFootprint _finalizeAndCompactMap:withName:]_block_invoke
+ ___50-[FPOutputFormatterText _sortedKeysForCategories:]_block_invoke
+ ___50-[FPOutputFormatterText _sortedKeysForCategories:]_block_invoke_2
+ ___51-[FPUserProcess _addSubrangesForRegion:purgeState:]_block_invoke
+ ___53-[FPOutputFormatterText _printCategories:forProcess:]_block_invoke
+ ___56-[FPUserProcess _gatherMemoryData:extendedInfoProvider:]_block_invoke
+ ___57-[FPFootprint ioSurfaceExtendedInfoDetailsAtAddress:for:]_block_invoke
+ ___59-[FPFootprint ioAccelMemoryInfoDetailsAtAddress:for:error:]_block_invoke
+ ___64-[FPOutputFormatterText printVmmapLikeOutputForProcess:regions:]_block_invoke
+ ___65-[FPUserProcess _populateMemoryRegionWithPageQueries:regionInfo:]_block_invoke
+ ___75-[FPFootprint _generateProcessToProcessGroupsWithSharedCacheProcessGroups:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___FPLedgerIndexForLedger_block_invoke
+ ____extendedInfoStorage_block_invoke
+ ___block_descriptor_102_e8_32s40s48s56s64r72r_e93_B56?0Q8Q16^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQ}24i32"NSString"36"NSString"44B52ls32l8s40l8s48l8r64l8s56l8r72l8
+ ___block_descriptor_120_e8_32s40s48s56s64r72r80r88r96r104r_e5_v8?0ls32l8r64l8r72l8r80l8r88l8s40l8r96l8r104l8s48l8s56l8
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e12_B24?0Q8^v16l
+ ___block_descriptor_32_e33_q24?0"FPProcess"8"FPProcess"16l
+ ___block_descriptor_32_e47_q24?0"FPMemoryCategory"8"FPMemoryCategory"16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_32_e9_r*16?0q8l
+ ___block_descriptor_40_e12_B24?0Q8^v16l
+ ___block_descriptor_40_e52_B24?0"IOSurfaceDebugDescription"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32r_e30_v16?0^{dyld_shared_cache_s=}8lr32l8
+ ___block_descriptor_40_e8_32r_e9_v16?0r*8lr32l8
+ ___block_descriptor_40_e8_32s_e11_q24?0816ls32l8
+ ___block_descriptor_40_e8_32s_e12_v24?0^8Q16ls32l8
+ ___block_descriptor_40_e8_32s_e52_v16?0r^{FPRangeListNode=QQQQQQQ^{FPRangeListNode}}8ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e47_q24?0"FPMemoryCategory"8"FPMemoryCategory"16l
+ ___block_descriptor_56_e8_32s40bs48r_e25_v24?0"VMUVMRegion"8^B16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e23_v16?0^{dyld_image_s=}8ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSArray"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e12_v24?0^8Q16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s_e12_v24?0^8Q16ls32l8
+ ___block_descriptor_64_e8_32s40r48r_e18_v36?0r*8Q16Q24i32ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e8_v16?0Q8ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8r64l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40r48r_e18_v40?0^i8Q16Q24Q32lr40l8r48l8s32l8
+ ___block_descriptor_73_e8_32s40s48s56s64s_e12_v24?0^8Q16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40r48r56r64r_e37_v24?0{kcdata_iter=^{kcdata_item}^v}8lr40l8r48l8r56l8r64l8s32l8
+ ___block_descriptor_83_e8_32s40s48r56r_e18_v40?0^i8Q16Q24Q32ls32l8r48l8r56l8s40l8
+ ___block_literal_global
+ ___fp_map_destroy_block_invoke
+ ___machToNsec_block_invoke
+ ___main_block_invoke
+ ___runFootprint_block_invoke
+ ___sampleFootprint_block_invoke
+ ___sampleFootprint_block_invoke_2
+ ___sampleFootprint_block_invoke_3
+ ___sampleFootprint_block_invoke_4
+ ___sampleFootprint_block_invoke_5
+ __block_literal_global.102
+ __block_literal_global.107
+ __block_literal_global.182
+ __block_literal_global.188
+ __block_literal_global.194
+ __block_literal_global.427
+ __func__.-[FPMemoryRegion setEnd:]
+ __instanceCache
+ __instanceCacheLock
+ _enumerateObjects
+ _footprintForVmObject
+ _gLedgerCount
+ _gRegionLabels
+ _gVMLedgerNames
+ _kFPSampleIntervalDisabled
+ _kernCounterLabels
+ _kernMemoryLabels
+ _ledgerForId
+ _main
+ _newProcessStructures
+ _objc_initWeak
+ _objc_msgSend$UTF8String
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_addGlobalError:
+ _objc_msgSend$_addSubrangesForRegion:purgeState:
+ _objc_msgSend$_configurePageSize
+ _objc_msgSend$_dirtyFlagsFromEntryState:
+ _objc_msgSend$_drainDeferredReclaim
+ _objc_msgSend$_gatherImageData
+ _objc_msgSend$_gatherIsTranslated
+ _objc_msgSend$_gatherLedgers
+ _objc_msgSend$_gatherOwnedVmObjects
+ _objc_msgSend$_gatherPageSize
+ _objc_msgSend$_gatherProcessState
+ _objc_msgSend$_gatherSharedCacheFromDyldSnapshot:
+ _objc_msgSend$_isAlive
+ _objc_msgSend$_nameForBsdInfo:
+ _objc_msgSend$_populateMemoryRegionWithPageQueries:regionInfo:
+ _objc_msgSend$_populateTask
+ _objc_msgSend$_setIdleExitStatusFromDirtyFlags:
+ _objc_msgSend$_setPriority:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addLedgerData:count:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addProcess:
+ _objc_msgSend$address
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$allProcessesExcludingPids:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$asNumber
+ _objc_msgSend$auxData
+ _objc_msgSend$auxDataName
+ _objc_msgSend$binaryImagesDescription
+ _objc_msgSend$boolValue
+ _objc_msgSend$breakDownPhysFootprint
+ _objc_msgSend$cachedCopy
+ _objc_msgSend$childPidsForPids:
+ _objc_msgSend$cleanSize
+ _objc_msgSend$close
+ _objc_msgSend$code
+ _objc_msgSend$collectDataWithCompletionQueue:completionBlock:
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$configureForMultipleOutputs
+ _objc_msgSend$containsFakeRegion
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$copy
+ _objc_msgSend$couldHaveProcessView
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$description
+ _objc_msgSend$detailedAuxData
+ _objc_msgSend$detailedAuxDataName
+ _objc_msgSend$detailedName
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$didPhysFootprintDirtyAccounting
+ _objc_msgSend$directedGraphWithData:error:
+ _objc_msgSend$dirtyLength
+ _objc_msgSend$dirtySize
+ _objc_msgSend$displayString
+ _objc_msgSend$doOwnedAccountingAdjustments
+ _objc_msgSend$domain
+ _objc_msgSend$doubleValue
+ _objc_msgSend$dyldSharedCacheRange
+ _objc_msgSend$endAtTime:
+ _objc_msgSend$endProcessHeader:
+ _objc_msgSend$ensureMemoryObject
+ _objc_msgSend$enumerateRegions:
+ _objc_msgSend$enumerateRegionsWithBlock:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$errors
+ _objc_msgSend$extendedInfo
+ _objc_msgSend$extendedInfoForRegionType:at:extendedInfoProvider:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$finalizeObject
+ _objc_msgSend$firstObject
+ _objc_msgSend$formattedDescriptions
+ _objc_msgSend$formattedValue
+ _objc_msgSend$formatter
+ _objc_msgSend$fp_enumerateObjectsWithBatchSize:usingBlock:
+ _objc_msgSend$fp_isContainer
+ _objc_msgSend$fp_jsonRepresentation
+ _objc_msgSend$fp_mergeAuxDatum:withDatum:forceAggregate:
+ _objc_msgSend$fp_mergeWithData:
+ _objc_msgSend$fp_mergeWithData:forceAggregate:
+ _objc_msgSend$fullName
+ _objc_msgSend$gatherData:
+ _objc_msgSend$gatherData:extendedInfoProvider:
+ _objc_msgSend$getBootCarveoutSize
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getCString:maxLength:encoding:
+ _objc_msgSend$globalErrors
+ _objc_msgSend$hasNoFootprint
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hash
+ _objc_msgSend$height
+ _objc_msgSend$hiddenFromDisplay
+ _objc_msgSend$idleExitStatus
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$init
+ _objc_msgSend$initUniqueProcessGroup
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithBsdInfo:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithCString:encoding:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initWithValue:shouldAggregate:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$instanceMethodForSelector:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$ioAccelMemoryInfoDetailsAtAddress:for:error:
+ _objc_msgSend$ioSurfaceExtendedInfoDetailsAtAddress:for:
+ _objc_msgSend$is64bit
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isKernelPageTableMemory
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$isTranslated
+ _objc_msgSend$isTranslatedByRosetta
+ _objc_msgSend$kernelPageSize
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$lastObject
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$ledgerValueForKey:keyExists:
+ _objc_msgSend$length
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$mappings
+ _objc_msgSend$member:
+ _objc_msgSend$memoryPool
+ _objc_msgSend$memoryRegions
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$newlineCharacterSet
+ _objc_msgSend$nonretainedObjectValue
+ _objc_msgSend$null
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$ownerPid
+ _objc_msgSend$pageSize
+ _objc_msgSend$path
+ _objc_msgSend$physFootprint
+ _objc_msgSend$physicalFootprint
+ _objc_msgSend$physicalFootprintPeak
+ _objc_msgSend$pid
+ _objc_msgSend$pidsForStringDescriptions:errors:
+ _objc_msgSend$pixelFormat
+ _objc_msgSend$pointerValue
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$printGlobalAuxData:
+ _objc_msgSend$printHeader
+ _objc_msgSend$printProcessAuxData:forProcess:
+ _objc_msgSend$printProcessCategories:total:forProcess:
+ _objc_msgSend$printProcessHeader:
+ _objc_msgSend$printProcessTotal:forProcess:
+ _objc_msgSend$printProcessesWithWarnings:processesWithErrors:globalErrors:
+ _objc_msgSend$printSharedCache:categories:sharedWith:total:
+ _objc_msgSend$printSharedCategories:sharedWith:forProcess:hasProcessView:total:
+ _objc_msgSend$printSummaryCategories:total:hadErrors:
+ _objc_msgSend$printVmmapLikeOutputForProcess:regions:
+ _objc_msgSend$priority
+ _objc_msgSend$processDescriptionString
+ _objc_msgSend$processIDs
+ _objc_msgSend$processName
+ _objc_msgSend$processWithBsdInfo:
+ _objc_msgSend$processWithMemgraph:error:
+ _objc_msgSend$processWithPid:
+ _objc_msgSend$processes
+ _objc_msgSend$purgeable
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$reclaimableSize
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeIdleExitCleanProcessesFrom:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$residentLength
+ _objc_msgSend$scanInt:
+ _objc_msgSend$set
+ _objc_msgSend$setAuxDataName:
+ _objc_msgSend$setCleanSize:
+ _objc_msgSend$setDetailedName:
+ _objc_msgSend$setDirtySize:
+ _objc_msgSend$setDisplayString:
+ _objc_msgSend$setExtendedInfo:
+ _objc_msgSend$setFormatOptions:
+ _objc_msgSend$setFormatter:
+ _objc_msgSend$setHasNoFootprint:
+ _objc_msgSend$setHiddenFromDisplay:
+ _objc_msgSend$setMemoryRegions:
+ _objc_msgSend$setName:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOwnerPid:
+ _objc_msgSend$setPid:
+ _objc_msgSend$setReclaimableSize:
+ _objc_msgSend$setRegionSize:
+ _objc_msgSend$setSwappedSize:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$setTotalRegions:
+ _objc_msgSend$setVerbose:
+ _objc_msgSend$sharedCache
+ _objc_msgSend$shouldAggregate
+ _objc_msgSend$showsPhysFootprint
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$startAtTime:
+ _objc_msgSend$string
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$strongToStrongObjectsMapTable
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$supportsFormattedValue
+ _objc_msgSend$surfaceDescriptions
+ _objc_msgSend$surfaceID
+ _objc_msgSend$swappedSize
+ _objc_msgSend$systemTimeZone
+ _objc_msgSend$task
+ _objc_msgSend$totalCleanSize
+ _objc_msgSend$totalDirtySize
+ _objc_msgSend$totalReclaimableSize
+ _objc_msgSend$totalRegions
+ _objc_msgSend$totalSwappedSize
+ _objc_msgSend$totalWiredSize
+ _objc_msgSend$type
+ _objc_msgSend$unionSet:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$userInfo
+ _objc_msgSend$value
+ _objc_msgSend$valueWithNonretainedObject:
+ _objc_msgSend$valueWithPointer:
+ _objc_msgSend$verbose
+ _objc_msgSend$viewForProcess:
+ _objc_msgSend$virtualAddress
+ _objc_msgSend$vmPageSize
+ _objc_msgSend$warnings
+ _objc_msgSend$weakToStrongObjectsMapTable
+ _objc_msgSend$width
+ _objc_msgSend$wired
+ _objc_msgSend$wiredSize
+ _objc_retainAutoreleasedReturnValue
+ _usage
+ footprint.m
+ internForSegmentName.internPool
+ internForSymbolOwnerPath.internPool
+ main.onceToken
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- radr://5614542
CStrings:
+ "    -w, --wide                show wide output with all columns and full paths (implies --swapped --wired)\n    --swapped                 show swapped/compressed column\n    --wired                   show wired column\n    --vmObjectDirty           interpret dirty memory as viewed by VM objects in the kernel\n    --unmapped                search all processes for unmapped memory owned by the target processes\n    --sample <interval>       repeatedly gather footprint at the given sampling interval in seconds\n                              (can be fractional — e.g. 0.5)\n    --sample-duration <secs>  how long to sample in seconds (default: 0 / unlimited)\n    --noCategories            print only total footprint and auxiliary data\n    --sysFootprint            print system memory footprint data (boot_carveout, sys_wired, sys_unwired, sys_footprint)\n"
+ " (nofootprint)"
+ "%.0f MB"
+ "("
+ ")"
+ "@24@0:8^@16"
+ "NOTICE: '--sysFootprint' is redundant when using -a/--all"
+ "_hasNoFootprint"
+ "_includeSysFootprint"
+ "gatherData:"
+ "getBootCarveoutSize"
+ "hasNoFootprint"
+ "rangeOfString:options:"
+ "setHasNoFootprint:"
+ "substringWithRange:"
+ "sysFootprint"
- "    -w, --wide                show wide output with all columns and full paths (implies --swapped --wired)\n    --swapped                 show swapped/compressed column\n    --wired                   show wired column\n    --vmObjectDirty           interpret dirty memory as viewed by VM objects in the kernel\n    --unmapped                search all processes for unmapped memory owned by the target processes\n    --sample <interval>       repeatedly gather footprint at the given sampling interval in seconds\n                              (can be fractional — e.g. 0.5)\n    --sample-duration <secs>  how long to sample in seconds (default: 0 / unlimited)\n    --noCategories            print only total footprint and auxiliary data\n"
- "@32@0:8Q16^@24"
- "TQ,R,N,V_bootCarveoutSize"
- "bootCarveoutSize"
- "gatherData:error:"

```
