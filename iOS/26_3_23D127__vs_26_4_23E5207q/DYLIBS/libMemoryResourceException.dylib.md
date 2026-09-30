## libMemoryResourceException.dylib

> `/usr/lib/libMemoryResourceException.dylib`

```diff

-310.0.0.0.0
-  __TEXT.__text: 0x19094
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x154c
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x1ea4
-  __TEXT.__oslogstring: 0xa7b
-  __TEXT.__gcc_except_tab: 0x3cc
+314.100.8.0.0
+  __TEXT.__text: 0x1aaa0
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x1594
+  __TEXT.__const: 0x178
+  __TEXT.__cstring: 0x1f0e
+  __TEXT.__oslogstring: 0xb7b
+  __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__ustring: 0xd0
-  __TEXT.__unwind_info: 0x460
+  __TEXT.__unwind_info: 0x500
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x3855
+  __TEXT.__objc_methname: 0x3887
   __TEXT.__objc_methtype: 0x82b
-  __TEXT.__objc_stubs: 0x2c00
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0xe40
+  __TEXT.__objc_stubs: 0x2c40
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0xe58
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf28
+  __DATA_CONST.__objc_selrefs: 0xf38
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x688
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x2740
-  __AUTH_CONST.__objc_const: 0x2ec0
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x27c0
+  __AUTH_CONST.__objc_const: 0x2f48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x25c
-  __DATA.__data: 0x448
+  __DATA.__objc_ivar: 0x274
+  __DATA.__data: 0x4e8
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_ivar: 0x1c
+  __DATA_DIRTY.__objc_ivar: 0xc
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x4171
+  __DATA_DIRTY.__bss: 0x4189
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C29BF4F1-BF33-3C19-8E9E-244E4C443242
-  Functions: 470
-  Symbols:   312
-  CStrings:  1651
+  UUID: 9FB77609-8391-3F22-B589-B667EAD26CD3
+  Functions: 490
+  Symbols:   2112
+  CStrings:  1672
 
Symbols:
+ +[FPFootprint _totalForCategories:outTotal:]
+ +[FPFootprint breakDownPhysFootprint]
+ +[FPFootprint installCancelHandler:]
+ +[FPFootprint isSharingAnalysisDisabled]
+ +[FPFootprint setBreakDownPhysFootprint:]
+ +[FPFootprint setSharingAnalysisDisabled:]
+ +[FPFootprint setVmRegionInfoFlags:]
+ +[FPFootprint vmRegionInfoFlags]
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
+ +[FPSharedCache clearInstanceCache]
+ +[FPSharedCache instanceCache]
+ +[FPSharedCache sharedCacheForDyldSnapshot:]
+ +[FPTime now]
+ +[FPUserProcess _dirtyFlagsFromEntryState:]
+ +[MemoryResourceException extractExecNameAndBundleIDMinimal:execNameOut:bundleIDOut:]
+ +[MemoryResourceException resourceExceptionFromLogFileHandle:error:]
+ +[MemoryResourceException resourceExceptionFromTask:error:]
+ +[RMECacheEnumerator getGcoreSpoolWithCreateIfNecessary:]
+ +[RMECacheEnumerator getLogPathsForSystemDiagnostic]
+ +[RMECacheEnumerator getLogPathsSortedByProcessFrequency]
+ +[RMECacheEnumerator getLogPathsSortedByTime]
+ +[RMECacheEnumerator(ContainerSupport) getEPLProfilePath]
+ +[RMECacheEnumerator(ContainerSupport) getLogContainer:]
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
+ -[FPCorpseProcess _gatherProcessState]
+ -[FPCorpseProcess _isAlive]
+ -[FPCorpseProcess _populateTask]
+ -[FPCorpseProcess initWithCorpse:pid:name:dirtyFlags:procFlags:]
+ -[FPFootprint .cxx_destruct]
+ -[FPFootprint _categoriesForAllProcessesShouldSummarize:]
+ -[FPFootprint _categoriesForObjects:viewedByProcess:hasProcessView:summarize:]
+ -[FPFootprint _destroyMemoryObjectMaps]
+ -[FPFootprint _finalizeAndCompactMap:withName:]
+ -[FPFootprint _notHiddenProcesses]
+ -[FPFootprint addOutputFormatter:]
+ -[FPFootprint analyzeData]
+ -[FPFootprint cancel]
+ -[FPFootprint dealloc]
+ -[FPFootprint gatherData:]
+ -[FPFootprint gatherData]
+ -[FPFootprint gatherEndTime]
+ -[FPFootprint gatherStartTime]
+ -[FPFootprint initWithProcesses:]
+ -[FPFootprint ioAccelMemoryInfoDetailsAtAddress:for:error:]
+ -[FPFootprint ioSurfaceExtendedInfoDetailsAtAddress:for:]
+ -[FPFootprint printOutputVerbose:summarize:noCategories:]
+ -[FPFootprint processes]
+ -[FPFootprint qualityOfService]
+ -[FPFootprint setQualityOfService:]
+ -[FPImage .cxx_destruct]
+ -[FPImage setName:]
+ -[FPImageEnumerator .cxx_destruct]
+ -[FPImageEnumerator initWithImages:]
+ -[FPImageEnumerator nextImageForStart:end:]
+ -[FPMemoryCategory .cxx_destruct]
+ -[FPMemoryCategory addMemoryObject:]
+ -[FPMemoryCategory auxDataFullName]
+ -[FPMemoryCategory auxData]
+ -[FPMemoryCategory detailedName]
+ -[FPMemoryCategory fullName]
+ -[FPMemoryCategory hasNoFootprint]
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
+ -[FPMemoryCategory verbose]
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
+ -[FPMemoryRegion eligibleForProcessView]
+ -[FPMemoryRegion eligibleForSubrangesUsingPageSize:]
+ -[FPMemoryRegion end]
+ -[FPMemoryRegion ensureMemoryObject]
+ -[FPMemoryRegion extendedInfo]
+ -[FPMemoryRegion finalizeObject]
+ -[FPMemoryRegion fullName]
+ -[FPMemoryRegion hasNoFootprint]
+ -[FPMemoryRegion inSharedCache]
+ -[FPMemoryRegion isFake]
+ -[FPMemoryRegion memoryObject]
+ -[FPMemoryRegion name]
+ -[FPMemoryRegion object_id]
+ -[FPMemoryRegion offset]
+ -[FPMemoryRegion ownedExclusivelyByParentProcess]
+ -[FPMemoryRegion ownerPid]
+ -[FPMemoryRegion privateSharedCacheRegion]
+ -[FPMemoryRegion reclaimableSize]
+ -[FPMemoryRegion segment]
+ -[FPMemoryRegion setCleanSize:]
+ -[FPMemoryRegion setDetailedName:]
+ -[FPMemoryRegion setDirtySize:]
+ -[FPMemoryRegion setEnd:]
+ -[FPMemoryRegion setExtendedInfo:]
+ -[FPMemoryRegion setHasNoFootprint:]
+ -[FPMemoryRegion setInSharedCache:]
+ -[FPMemoryRegion setMemoryObject:]
+ -[FPMemoryRegion setName:]
+ -[FPMemoryRegion setObject_id:]
+ -[FPMemoryRegion setOffset:]
+ -[FPMemoryRegion setOwnedExclusivelyByParentProcess:]
+ -[FPMemoryRegion setReclaimableSize:]
+ -[FPMemoryRegion setSegment:]
+ -[FPMemoryRegion setShare_mode:]
+ -[FPMemoryRegion setSize:]
+ -[FPMemoryRegion setStart:]
+ -[FPMemoryRegion setSwappedSize:]
+ -[FPMemoryRegion setUnusedSharedCacheRegion:]
+ -[FPMemoryRegion setUser_tag:]
+ -[FPMemoryRegion setVerbose:]
+ -[FPMemoryRegion setWired:]
+ -[FPMemoryRegion share_mode]
+ -[FPMemoryRegion size]
+ -[FPMemoryRegion start]
+ -[FPMemoryRegion subrangeList]
+ -[FPMemoryRegion swappedSize]
+ -[FPMemoryRegion totalRegions]
+ -[FPMemoryRegion unusedSharedCacheRegion]
+ -[FPMemoryRegion user_tag]
+ -[FPMemoryRegion verbose]
+ -[FPMemoryRegion viewForProcess:]
+ -[FPMemoryRegion wiredSize]
+ -[FPMemoryRegion wired]
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
+ -[FPRangeList sum]
+ -[FPSharedCache .cxx_destruct]
+ -[FPSharedCache alignment]
+ -[FPSharedCache baseAddress]
+ -[FPSharedCache containsAddress:]
+ -[FPSharedCache copyWithZone:]
+ -[FPSharedCache mappedSize]
+ -[FPSharedCache slide]
+ -[FPSharedCache uuid]
+ -[FPTime date]
+ -[FPTime init]
+ -[FPTime machAbsoluteTimeNsec]
+ -[FPTime machAbsoluteTime]
+ -[FPTime machContinuousTimeNsec]
+ -[FPTime machContinuousTime]
+ -[FPTime wallTime]
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
+ -[MREOutputFormatterInMemory .cxx_destruct]
+ -[MREOutputFormatterInMemory dataForCategories:]
+ -[MREOutputFormatterInMemory endAtTime:]
+ -[MREOutputFormatterInMemory endProcessHeader:]
+ -[MREOutputFormatterInMemory init]
+ -[MREOutputFormatterInMemory printGlobalAuxData:]
+ -[MREOutputFormatterInMemory printProcessAuxData:forProcess:]
+ -[MREOutputFormatterInMemory printProcessCategories:total:forProcess:]
+ -[MREOutputFormatterInMemory printProcessHeader:]
+ -[MREOutputFormatterInMemory printProcessTotal:forProcess:]
+ -[MREOutputFormatterInMemory printProcessesWithWarnings:processesWithErrors:globalErrors:]
+ -[MREOutputFormatterInMemory printSharedCache:categories:sharedWith:total:]
+ -[MREOutputFormatterInMemory printSharedCategories:sharedWith:forProcess:hasProcessView:total:]
+ -[MREOutputFormatterInMemory printSummaryCategories:total:hadErrors:]
+ -[MREOutputFormatterInMemory printVmmapLikeOutputForProcess:regions:]
+ -[MemoryResourceException .cxx_destruct]
+ -[MemoryResourceException _generateMemgraphWithContentLevel:timeoutSecs:memgraphFailedReasonOut:]
+ -[MemoryResourceException _populateAddtionalMetadataWithOptions:timeoutSecs:]
+ -[MemoryResourceException _saveLogFileWithHandle:error:]
+ -[MemoryResourceException _symbolOwners]
+ -[MemoryResourceException bundleID]
+ -[MemoryResourceException cachedMetaDataDict]
+ -[MemoryResourceException cid]
+ -[MemoryResourceException coalitionBundleID]
+ -[MemoryResourceException copyWithZone:]
+ -[MemoryResourceException crashedThreadId]
+ -[MemoryResourceException createLiteMetaDataDict]
+ -[MemoryResourceException createMetaDataDict]
+ -[MemoryResourceException currentTime]
+ -[MemoryResourceException dealloc]
+ -[MemoryResourceException dirtyFlags]
+ -[MemoryResourceException exceptionCode0]
+ -[MemoryResourceException exceptionType]
+ -[MemoryResourceException execName]
+ -[MemoryResourceException execPath]
+ -[MemoryResourceException executionStack]
+ -[MemoryResourceException footprintOutput]
+ -[MemoryResourceException gcoreCapture]
+ -[MemoryResourceException gcoreFilePath]
+ -[MemoryResourceException generateMemoryGraphWithContentLevel:memgraphFailedReasonOut:]
+ -[MemoryResourceException hwModel]
+ -[MemoryResourceException initWithMetaDataDict:andMemoryGraph:withError:]
+ -[MemoryResourceException ioAccelMemoryInfoErrors]
+ -[MemoryResourceException ioAccelMemoryInfo]
+ -[MemoryResourceException ioSurfaceInfo]
+ -[MemoryResourceException is64Bit]
+ -[MemoryResourceException isFirstParty]
+ -[MemoryResourceException isMSLEnabled]
+ -[MemoryResourceException ledgerAlternateAccountingCompressed]
+ -[MemoryResourceException ledgerAlternateAccounting]
+ -[MemoryResourceException ledgerIOKitMapped]
+ -[MemoryResourceException ledgerInternalCompressed]
+ -[MemoryResourceException ledgerInternal]
+ -[MemoryResourceException ledgerNetworkNonvolatileCompressed]
+ -[MemoryResourceException ledgerNetworkNonvolatile]
+ -[MemoryResourceException ledgerPageTable]
+ -[MemoryResourceException ledgerPhysFootprintPeak]
+ -[MemoryResourceException ledgerPhysFootprint]
+ -[MemoryResourceException ledgerPurgeableNonvolatileCompressed]
+ -[MemoryResourceException ledgerPurgeableNonvolatile]
+ -[MemoryResourceException ledgerWiredMem]
+ -[MemoryResourceException limitValue]
+ -[MemoryResourceException liteDiagFilePath]
+ -[MemoryResourceException memgraphError]
+ -[MemoryResourceException memoryGraph]
+ -[MemoryResourceException osLogs]
+ -[MemoryResourceException osVersion]
+ -[MemoryResourceException pid]
+ -[MemoryResourceException populateAdditionalMetadataWithDiagnostics:]
+ -[MemoryResourceException ppid]
+ -[MemoryResourceException prettyPrintBacktrace:]
+ -[MemoryResourceException prettyPrintBinaryImages]
+ -[MemoryResourceException prettyPrintIOAccelMemoryInfo]
+ -[MemoryResourceException prettyPrintIOSurfaceInfo]
+ -[MemoryResourceException procFlags]
+ -[MemoryResourceException processPidString]
+ -[MemoryResourceException releaseAnalyzedTask]
+ -[MemoryResourceException saveLogFileWithHandle:error:]
+ -[MemoryResourceException setGcoreCapture:]
+ -[MemoryResourceException setGcoreFilePath:]
+ -[MemoryResourceException setIsMSLEnabled:]
+ -[MemoryResourceException setLiteDiagFilePath:]
+ -[MemoryResourceException setMemgraphError:]
+ -[MemoryResourceException startTime]
+ -[MemoryResourceException suspensionToken]
+ -[MemoryResourceException task]
+ -[MemoryResourceException upTime]
+ -[MemoryResourceException version]
+ -[NSDictionary(FPAuxData) fp_isContainer]
+ -[NSDictionary(FPAuxData) fp_jsonRepresentation]
+ -[NSDictionary(FPAuxData) fp_mergeAuxDatum:withDatum:forceAggregate:]
+ -[NSDictionary(FPAuxData) fp_mergeWithData:]
+ -[NSDictionary(FPAuxData) fp_mergeWithData:forceAggregate:]
+ -[RMECacheEnumerator .cxx_destruct]
+ -[RMECacheEnumerator initCacheEnumeratorWithVolume:]
+ -[RMECacheEnumerator initCacheEnumerator]
+ -[RMECacheEnumerator nextValidURL]
+ <redacted>
+ GCC_except_table0
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table22
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table3
+ GCC_except_table8
+ OBJC_IVAR_$_FPUserProcess._images
+ OBJC_IVAR_$_FPUserProcess._ledgers
+ OBJC_IVAR_$_FPUserProcess._ownedVmObjects
+ OBJC_IVAR_$_FPUserProcess._task
+ _.str
+ _.str.1
+ _.str.2
+ _.str.3
+ _.str.4
+ _.str.5
+ _DiagnosticLogSubmissionEnabled
+ _FPExtractCorpseInfoWithBlock
+ _FPFootprintBreakDownPhysFootprint
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
+ _FPLedgerIndexForLedger.ledgerIndexMap
+ _FPLedgerIndexForLedger.onceToken
+ _FPLedgerNameForLedger
+ _FPLedgerValueForId
+ _KERNEL_COMM_PAGE64_NESTING_SIZE
+ _KERNEL_COMM_PAGE64_NESTING_START
+ _MRECRBinaryInfoArchitectureKey
+ _MRECRStackFrameAddressKey
+ _MRECRStackFrameSourceFilenameKey
+ _MRECRStackFrameSourceLineKey
+ _MRECRStackFrameSymbolAddressRangeLocationKey
+ _MRECRStackFrameSymbolKey
+ _MRECRStackFrameUUIDKey
+ _MREExecutionStackBacktracesKey
+ _MREExecutionStackBinaryImagesKey
+ _MREExecutionStackCrashedThreadKey
+ _MREExecutionStackThreadNamesKey
+ _MREIOAccelMemoryInfoCachedCopyKey
+ _MREIOAccelMemoryInfoDescriptionsKey
+ _MREIOAccelMemoryInfoDirtySizeKey
+ _MREIOAccelMemoryInfoIsPurgeableKey
+ _MREIOAccelMemoryInfoIsWiredKey
+ _MREIOAccelMemoryInfoMemoryPoolKey
+ _MREIOAccelMemoryInfoResidentSizeKey
+ _MREIOAccelMemoryInfoSizeKey
+ _MREIOAccelMemoryInfoSurfaceIDKey
+ _MREIOSurfaceInfoHeightKey
+ _MREIOSurfaceInfoNameKey
+ _MREIOSurfaceInfoPixelFormatKey
+ _MREIOSurfaceInfoSizeKey
+ _MREIOSurfaceInfoSurfaceIDKey
+ _MREIOSurfaceInfoWidthKey
+ _MREMetaDataBundleIDKey
+ _MREMetaDataCoalitionBundleIDKey
+ _MREMetaDataDirtyFlagsKey
+ _MREMetaDataExceptionTypeKey
+ _MREMetaDataExecNameKey
+ _MREMetaDataExecPathKey
+ _MREMetaDataExecutionStackKey
+ _MREMetaDataFootprintToolKey
+ _MREMetaDataHWModelKey
+ _MREMetaDataIOAccelMemoryInfoErrorsKey
+ _MREMetaDataIOAccelMemoryInfoKey
+ _MREMetaDataIOSurfaceInfoKey
+ _MREMetaDataIs64BitKey
+ _MREMetaDataLedgerAlternateAccountingCompressedKey
+ _MREMetaDataLedgerAlternateAccountingKey
+ _MREMetaDataLedgerIOKitMappedKey
+ _MREMetaDataLedgerInternalCompressedKey
+ _MREMetaDataLedgerInternalKey
+ _MREMetaDataLedgerNetworkNonvolatileCompressedKey
+ _MREMetaDataLedgerNetworkNonvolatileKey
+ _MREMetaDataLedgerPageTableKey
+ _MREMetaDataLedgerPhysFootprintKey
+ _MREMetaDataLedgerPhysFootprintPeakKey
+ _MREMetaDataLedgerPurgeableNonvolatileCompressedKey
+ _MREMetaDataLedgerPurgeableNonvolatileKey
+ _MREMetaDataLedgerWiredMemKey
+ _MREMetaDataLimitValueKey
+ _MREMetaDataMSLEnabledKey
+ _MREMetaDataMemgraphErrorKey
+ _MREMetaDataName
+ _MREMetaDataOSLogsKey
+ _MREMetaDataOSVersionKey
+ _MREMetaDataPIDKey
+ _MREMetaDataPPIDKey
+ _MREMetaDataUpTimeKey
+ _MREMetaDataVersionKey
+ _OBJC_CLASS_$_FPAuxData
+ _OBJC_CLASS_$_FPCorpseProcess
+ _OBJC_CLASS_$_FPImage
+ _OBJC_CLASS_$_FPImageEnumerator
+ _OBJC_CLASS_$_FPMemoryObject
+ _OBJC_CLASS_$_FPMemoryRegion
+ _OBJC_CLASS_$_FPProcessGroup
+ _OBJC_CLASS_$_FPProcessGroupMinimal
+ _OBJC_CLASS_$_FPRangeList
+ _OBJC_CLASS_$_FPSharedCache
+ _OBJC_CLASS_$_FPUserProcess
+ _OBJC_CLASS_$_MREOutputFormatterInMemory
+ _OBJC_IVAR_$_FPAuxData._aggregate
+ _OBJC_IVAR_$_FPAuxData._formatter
+ _OBJC_IVAR_$_FPAuxData._value
+ _OBJC_IVAR_$_FPFootprint._allPIDsIOAccelMemoryInfos
+ _OBJC_IVAR_$_FPFootprint._allPIDsIOAccelMemoryInfosLock
+ _OBJC_IVAR_$_FPFootprint._allPIDsIOSurfaceDescriptions
+ _OBJC_IVAR_$_FPFootprint._allPIDsIOSurfaceDescriptionsLock
+ _OBJC_IVAR_$_FPFootprint._earlyExit
+ _OBJC_IVAR_$_FPFootprint._gatherEndTime
+ _OBJC_IVAR_$_FPFootprint._gatherStartTime
+ _OBJC_IVAR_$_FPFootprint._linkeditMemoryObjects
+ _OBJC_IVAR_$_FPFootprint._memoryObjectMapsInitialized
+ _OBJC_IVAR_$_FPFootprint._memoryObjects
+ _OBJC_IVAR_$_FPFootprint._outputFormatters
+ _OBJC_IVAR_$_FPFootprint._pidToFootprint
+ _OBJC_IVAR_$_FPFootprint._processes
+ _OBJC_IVAR_$_FPFootprint._qualityOfService
+ _OBJC_IVAR_$_FPFootprint._sharedCacheMemoryObjectsTable
+ _OBJC_IVAR_$_FPFootprint._textMemoryObjects
+ _OBJC_IVAR_$_FPImage._name
+ _OBJC_IVAR_$_FPImage._ownerPath
+ _OBJC_IVAR_$_FPImage._segment
+ _OBJC_IVAR_$_FPImage._size
+ _OBJC_IVAR_$_FPImage._start
+ _OBJC_IVAR_$_FPImageEnumerator._images
+ _OBJC_IVAR_$_FPImageEnumerator._index
+ _OBJC_IVAR_$_FPMemoryCategory._firstMemoryObject
+ _OBJC_IVAR_$_FPMemoryCategory._isSummary
+ _OBJC_IVAR_$_FPMemoryCategory._name
+ _OBJC_IVAR_$_FPMemoryCategory._totalCleanSize
+ _OBJC_IVAR_$_FPMemoryCategory._totalDirtySize
+ _OBJC_IVAR_$_FPMemoryCategory._totalReclaimableSize
+ _OBJC_IVAR_$_FPMemoryCategory._totalRegions
+ _OBJC_IVAR_$_FPMemoryCategory._totalSwappedSize
+ _OBJC_IVAR_$_FPMemoryCategory._totalWiredSize
+ _OBJC_IVAR_$_FPMemoryObject._accurateSizes
+ _OBJC_IVAR_$_FPMemoryObject._cleanSize
+ _OBJC_IVAR_$_FPMemoryObject._dirtySize
+ _OBJC_IVAR_$_FPMemoryObject._hasNoFootprint
+ _OBJC_IVAR_$_FPMemoryObject._hasProcessViewForSingleTotalRegions
+ _OBJC_IVAR_$_FPMemoryObject._isProcessViewForSingleTotalRegions
+ _OBJC_IVAR_$_FPMemoryObject._memoryRegions
+ _OBJC_IVAR_$_FPMemoryObject._ownerPid
+ _OBJC_IVAR_$_FPMemoryObject._processMemoryRegions
+ _OBJC_IVAR_$_FPMemoryObject._reclaimableSize
+ _OBJC_IVAR_$_FPMemoryObject._swappedSize
+ _OBJC_IVAR_$_FPMemoryObject._wiredSize
+ _OBJC_IVAR_$_FPMemoryRegion._cleanSize
+ _OBJC_IVAR_$_FPMemoryRegion._detailedName
+ _OBJC_IVAR_$_FPMemoryRegion._dirtySize
+ _OBJC_IVAR_$_FPMemoryRegion._hasNoFootprint
+ _OBJC_IVAR_$_FPMemoryRegion._inSharedCache
+ _OBJC_IVAR_$_FPMemoryRegion._memoryObject
+ _OBJC_IVAR_$_FPMemoryRegion._name
+ _OBJC_IVAR_$_FPMemoryRegion._object_id
+ _OBJC_IVAR_$_FPMemoryRegion._offset
+ _OBJC_IVAR_$_FPMemoryRegion._ownedExclusivelyByParentProcess
+ _OBJC_IVAR_$_FPMemoryRegion._reclaimableSize
+ _OBJC_IVAR_$_FPMemoryRegion._segment
+ _OBJC_IVAR_$_FPMemoryRegion._share_mode
+ _OBJC_IVAR_$_FPMemoryRegion._size
+ _OBJC_IVAR_$_FPMemoryRegion._start
+ _OBJC_IVAR_$_FPMemoryRegion._subrangeList
+ _OBJC_IVAR_$_FPMemoryRegion._swappedSize
+ _OBJC_IVAR_$_FPMemoryRegion._unusedSharedCacheRegion
+ _OBJC_IVAR_$_FPMemoryRegion._user_tag
+ _OBJC_IVAR_$_FPMemoryRegion._verbose
+ _OBJC_IVAR_$_FPMemoryRegion._wired
+ _OBJC_IVAR_$_FPProcess._displayString
+ _OBJC_IVAR_$_FPProcess._hiddenFromDisplay
+ _OBJC_IVAR_$_FPProcess._memoryRegions
+ _OBJC_IVAR_$_FPProcess._name
+ _OBJC_IVAR_$_FPProcess._pageSize
+ _OBJC_IVAR_$_FPProcessGroup._categories
+ _OBJC_IVAR_$_FPProcessGroup._categoriesRefcount
+ _OBJC_IVAR_$_FPProcessGroup._objects
+ _OBJC_IVAR_$_FPProcessGroupMinimal._hashValue
+ _OBJC_IVAR_$_FPProcessGroupMinimal._processes
+ _OBJC_IVAR_$_FPRangeList._rangeListHead
+ _OBJC_IVAR_$_FPSharedCache._alignment
+ _OBJC_IVAR_$_FPSharedCache._baseAddress
+ _OBJC_IVAR_$_FPSharedCache._mappedSize
+ _OBJC_IVAR_$_FPSharedCache._slide
+ _OBJC_IVAR_$_FPSharedCache._uuid
+ _OBJC_IVAR_$_FPTime._machAbsoluteTime
+ _OBJC_IVAR_$_FPTime._machContinuousTime
+ _OBJC_IVAR_$_FPTime._wallTime
+ _OBJC_IVAR_$_FPUserProcess._bailedOut
+ _OBJC_IVAR_$_MREOutputFormatterInMemory._addedProcessGroups
+ _OBJC_IVAR_$_MREOutputFormatterInMemory._data
+ _OBJC_IVAR_$_MREOutputFormatterInMemory._isPageSizeSet
+ _OBJC_IVAR_$_MREOutputFormatterInMemory._processes
+ _OBJC_IVAR_$_MREOutputFormatterInMemory._verbose
+ _OBJC_IVAR_$_MemoryResourceException._bundleID
+ _OBJC_IVAR_$_MemoryResourceException._cachedMetaDataDict
+ _OBJC_IVAR_$_MemoryResourceException._cid
+ _OBJC_IVAR_$_MemoryResourceException._coalitionBundleID
+ _OBJC_IVAR_$_MemoryResourceException._crashedThreadId
+ _OBJC_IVAR_$_MemoryResourceException._currentTime
+ _OBJC_IVAR_$_MemoryResourceException._dirtyFlags
+ _OBJC_IVAR_$_MemoryResourceException._exceptionCode0
+ _OBJC_IVAR_$_MemoryResourceException._exceptionType
+ _OBJC_IVAR_$_MemoryResourceException._execName
+ _OBJC_IVAR_$_MemoryResourceException._execPath
+ _OBJC_IVAR_$_MemoryResourceException._executionStack
+ _OBJC_IVAR_$_MemoryResourceException._footprintOutput
+ _OBJC_IVAR_$_MemoryResourceException._gcoreCapture
+ _OBJC_IVAR_$_MemoryResourceException._gcoreFilePath
+ _OBJC_IVAR_$_MemoryResourceException._hwModel
+ _OBJC_IVAR_$_MemoryResourceException._ioAccelDirtySwappedSize
+ _OBJC_IVAR_$_MemoryResourceException._ioAccelMemoryInfo
+ _OBJC_IVAR_$_MemoryResourceException._ioAccelMemoryInfoErrors
+ _OBJC_IVAR_$_MemoryResourceException._ioSurfaceInfo
+ _OBJC_IVAR_$_MemoryResourceException._is64Bit
+ _OBJC_IVAR_$_MemoryResourceException._isMSLEnabled
+ _OBJC_IVAR_$_MemoryResourceException._ledgerAlternateAccounting
+ _OBJC_IVAR_$_MemoryResourceException._ledgerAlternateAccountingCompressed
+ _OBJC_IVAR_$_MemoryResourceException._ledgerIOKitMapped
+ _OBJC_IVAR_$_MemoryResourceException._ledgerInternal
+ _OBJC_IVAR_$_MemoryResourceException._ledgerInternalCompressed
+ _OBJC_IVAR_$_MemoryResourceException._ledgerNetworkNonvolatile
+ _OBJC_IVAR_$_MemoryResourceException._ledgerNetworkNonvolatileCompressed
+ _OBJC_IVAR_$_MemoryResourceException._ledgerPageTable
+ _OBJC_IVAR_$_MemoryResourceException._ledgerPhysFootprint
+ _OBJC_IVAR_$_MemoryResourceException._ledgerPhysFootprintPeak
+ _OBJC_IVAR_$_MemoryResourceException._ledgerPurgeableNonvolatile
+ _OBJC_IVAR_$_MemoryResourceException._ledgerPurgeableNonvolatileCompressed
+ _OBJC_IVAR_$_MemoryResourceException._ledgerWiredMem
+ _OBJC_IVAR_$_MemoryResourceException._limitValue
+ _OBJC_IVAR_$_MemoryResourceException._liteDiagFilePath
+ _OBJC_IVAR_$_MemoryResourceException._memgraphError
+ _OBJC_IVAR_$_MemoryResourceException._memoryGraph
+ _OBJC_IVAR_$_MemoryResourceException._osLogs
+ _OBJC_IVAR_$_MemoryResourceException._osVersion
+ _OBJC_IVAR_$_MemoryResourceException._pid
+ _OBJC_IVAR_$_MemoryResourceException._ppid
+ _OBJC_IVAR_$_MemoryResourceException._procFlags
+ _OBJC_IVAR_$_MemoryResourceException._startTime
+ _OBJC_IVAR_$_MemoryResourceException._suspensionToken
+ _OBJC_IVAR_$_MemoryResourceException._task
+ _OBJC_IVAR_$_MemoryResourceException._upTime
+ _OBJC_IVAR_$_MemoryResourceException._version
+ _OBJC_IVAR_$_RMECacheEnumerator._internalEnumerator
+ _OBJC_IVAR_$_RMECacheEnumerator._volume
+ _OBJC_METACLASS_$_FPAuxData
+ _OBJC_METACLASS_$_FPCorpseProcess
+ _OBJC_METACLASS_$_FPImage
+ _OBJC_METACLASS_$_FPImageEnumerator
+ _OBJC_METACLASS_$_FPMemoryObject
+ _OBJC_METACLASS_$_FPMemoryRegion
+ _OBJC_METACLASS_$_FPProcessGroup
+ _OBJC_METACLASS_$_FPProcessGroupMinimal
+ _OBJC_METACLASS_$_FPRangeList
+ _OBJC_METACLASS_$_FPSharedCache
+ _OBJC_METACLASS_$_FPUserProcess
+ _OBJC_METACLASS_$_MREOutputFormatterInMemory
+ _RMEExtractExecNameForFilename
+ _RMEGCoreDiagFilenameIndicator
+ _RMEGetCriticalProcesses
+ _RMEGetDefaultCriticalProcesses
+ _RMEGetDefaultLargeExemptedProcesses
+ _RMEGetLiteLimitForExecName
+ _RMEGetMemgraphLimitForExecName
+ _RMEGetPrefs
+ _RMEGetPrefsWithProfileDicts
+ _RMEGetTimeOrderedLogPathsMatchingPrefs
+ _RMEGetXPCConnection
+ _RMEHandleAnalyzeReply
+ _RMEIsAutoSubmitEnabled
+ _RMEIsCriticalProcess
+ _RMEMSLFullDiagFileSuffix
+ _RMEPopulateDefaultPrefs
+ _RMEPrefAllowInSysdiagnoseKey
+ _RMEPrefBoostCriticalProcessKey
+ _RMEPrefCollectIOAccelMemInfoKey
+ _RMEPrefCriticalProcessesKey
+ _RMEPrefExecNamesKey
+ _RMEPrefExpirationDateKey
+ _RMEPrefFullContentExecNamesListKey
+ _RMEPrefFullDiagLimitKey
+ _RMEPrefFullPerProcessLimitKey
+ _RMEPrefGCoreDiagLimitKey
+ _RMEPrefLargeExemptedProcessesKey
+ _RMEPrefLiteDiagLimitKey
+ _RMEPrefLitePerProcessLimitKey
+ _RMEPrefMSLFullDiagLimitKey
+ _RMEPrefPerCriticalProcessLimitKey
+ _RMEPrefProcessSpecificLimitsKey
+ _RMEPrefSysdiagnoseListKey
+ _RMEPrefThresholdFullDiagLimitKey
+ _RMEShouldIncludeDiagInSysdiagnose
+ _RMEShouldLogThirdPartyProcesses
+ _SYSTEM_MACH_VM_MAX_GPU_CARVEOUT_ADDRESS
+ _SYSTEM_MACH_VM_MIN_GPU_CARVEOUT_ADDRESS
+ __FPRangeListAddNode
+ __FPRangeListSplitNodeAtIntersection
+ __MergedGlobals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_FPAuxData
+ __OBJC_$_CATEGORY_NSDictionary_$_FPAuxData
+ __OBJC_$_CLASS_METHODS_FPFootprint
+ __OBJC_$_CLASS_METHODS_FPMemoryRegion
+ __OBJC_$_CLASS_METHODS_FPProcess
+ __OBJC_$_CLASS_METHODS_FPSharedCache
+ __OBJC_$_CLASS_METHODS_FPTime
+ __OBJC_$_CLASS_METHODS_FPUserProcess
+ __OBJC_$_CLASS_METHODS_MemoryResourceException
+ __OBJC_$_CLASS_METHODS_RMECacheEnumerator(ContainerSupport)
+ __OBJC_$_CLASS_PROP_LIST_FPFootprint
+ __OBJC_$_CLASS_PROP_LIST_FPTime
+ __OBJC_$_INSTANCE_METHODS_FPAuxData
+ __OBJC_$_INSTANCE_METHODS_FPCorpseProcess
+ __OBJC_$_INSTANCE_METHODS_FPFootprint
+ __OBJC_$_INSTANCE_METHODS_FPImage
+ __OBJC_$_INSTANCE_METHODS_FPImageEnumerator
+ __OBJC_$_INSTANCE_METHODS_FPMemoryCategory
+ __OBJC_$_INSTANCE_METHODS_FPMemoryObject
+ __OBJC_$_INSTANCE_METHODS_FPMemoryRegion
+ __OBJC_$_INSTANCE_METHODS_FPProcess
+ __OBJC_$_INSTANCE_METHODS_FPProcessGroup
+ __OBJC_$_INSTANCE_METHODS_FPProcessGroupMinimal
+ __OBJC_$_INSTANCE_METHODS_FPRangeList
+ __OBJC_$_INSTANCE_METHODS_FPSharedCache
+ __OBJC_$_INSTANCE_METHODS_FPTime
+ __OBJC_$_INSTANCE_METHODS_FPUserProcess
+ __OBJC_$_INSTANCE_METHODS_MREOutputFormatterInMemory
+ __OBJC_$_INSTANCE_METHODS_MemoryResourceException
+ __OBJC_$_INSTANCE_METHODS_RMECacheEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_FPAuxData
+ __OBJC_$_INSTANCE_VARIABLES_FPFootprint
+ __OBJC_$_INSTANCE_VARIABLES_FPImage
+ __OBJC_$_INSTANCE_VARIABLES_FPImageEnumerator
+ __OBJC_$_INSTANCE_VARIABLES_FPMemoryCategory
+ __OBJC_$_INSTANCE_VARIABLES_FPMemoryObject
+ __OBJC_$_INSTANCE_VARIABLES_FPMemoryRegion
+ __OBJC_$_INSTANCE_VARIABLES_FPProcess
+ __OBJC_$_INSTANCE_VARIABLES_FPProcessGroup
+ __OBJC_$_INSTANCE_VARIABLES_FPProcessGroupMinimal
+ __OBJC_$_INSTANCE_VARIABLES_FPRangeList
+ __OBJC_$_INSTANCE_VARIABLES_FPSharedCache
+ __OBJC_$_INSTANCE_VARIABLES_FPTime
+ __OBJC_$_INSTANCE_VARIABLES_FPUserProcess
+ __OBJC_$_INSTANCE_VARIABLES_MREOutputFormatterInMemory
+ __OBJC_$_INSTANCE_VARIABLES_MemoryResourceException
+ __OBJC_$_INSTANCE_VARIABLES_RMECacheEnumerator
+ __OBJC_$_PROP_LIST_FPAuxData
+ __OBJC_$_PROP_LIST_FPAuxDataType
+ __OBJC_$_PROP_LIST_FPFootprint
+ __OBJC_$_PROP_LIST_FPMemoryCategory
+ __OBJC_$_PROP_LIST_FPMemoryObject
+ __OBJC_$_PROP_LIST_FPMemoryObject.130
+ __OBJC_$_PROP_LIST_FPMemoryRegion
+ __OBJC_$_PROP_LIST_FPProcess
+ __OBJC_$_PROP_LIST_FPProcessGroup
+ __OBJC_$_PROP_LIST_FPProcessGroupMinimal
+ __OBJC_$_PROP_LIST_FPSharedCache
+ __OBJC_$_PROP_LIST_FPTime
+ __OBJC_$_PROP_LIST_FPUserProcess
+ __OBJC_$_PROP_LIST_MREOutputFormatterInMemory
+ __OBJC_$_PROP_LIST_MemoryResourceException
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
+ __OBJC_CLASS_PROTOCOLS_$_FPProcessGroup
+ __OBJC_CLASS_PROTOCOLS_$_FPSharedCache
+ __OBJC_CLASS_PROTOCOLS_$_MREOutputFormatterInMemory
+ __OBJC_CLASS_PROTOCOLS_$_MemoryResourceException
+ __OBJC_CLASS_RO_$_FPAuxData
+ __OBJC_CLASS_RO_$_FPCorpseProcess
+ __OBJC_CLASS_RO_$_FPFootprint
+ __OBJC_CLASS_RO_$_FPImage
+ __OBJC_CLASS_RO_$_FPImageEnumerator
+ __OBJC_CLASS_RO_$_FPMemoryCategory
+ __OBJC_CLASS_RO_$_FPMemoryObject
+ __OBJC_CLASS_RO_$_FPMemoryRegion
+ __OBJC_CLASS_RO_$_FPProcess
+ __OBJC_CLASS_RO_$_FPProcessGroup
+ __OBJC_CLASS_RO_$_FPProcessGroupMinimal
+ __OBJC_CLASS_RO_$_FPRangeList
+ __OBJC_CLASS_RO_$_FPSharedCache
+ __OBJC_CLASS_RO_$_FPTime
+ __OBJC_CLASS_RO_$_FPUserProcess
+ __OBJC_CLASS_RO_$_MREOutputFormatterInMemory
+ __OBJC_CLASS_RO_$_MemoryResourceException
+ __OBJC_CLASS_RO_$_RMECacheEnumerator
+ __OBJC_LABEL_PROTOCOL_$_FPAuxDataType
+ __OBJC_LABEL_PROTOCOL_$_FPFootprintExtendedInfoProvider
+ __OBJC_LABEL_PROTOCOL_$_FPMemoryObject
+ __OBJC_LABEL_PROTOCOL_$_FPOutputFormatter
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_FPAuxData
+ __OBJC_METACLASS_RO_$_FPCorpseProcess
+ __OBJC_METACLASS_RO_$_FPFootprint
+ __OBJC_METACLASS_RO_$_FPImage
+ __OBJC_METACLASS_RO_$_FPImageEnumerator
+ __OBJC_METACLASS_RO_$_FPMemoryCategory
+ __OBJC_METACLASS_RO_$_FPMemoryObject
+ __OBJC_METACLASS_RO_$_FPMemoryRegion
+ __OBJC_METACLASS_RO_$_FPProcess
+ __OBJC_METACLASS_RO_$_FPProcessGroup
+ __OBJC_METACLASS_RO_$_FPProcessGroupMinimal
+ __OBJC_METACLASS_RO_$_FPRangeList
+ __OBJC_METACLASS_RO_$_FPSharedCache
+ __OBJC_METACLASS_RO_$_FPTime
+ __OBJC_METACLASS_RO_$_FPUserProcess
+ __OBJC_METACLASS_RO_$_MREOutputFormatterInMemory
+ __OBJC_METACLASS_RO_$_MemoryResourceException
+ __OBJC_METACLASS_RO_$_RMECacheEnumerator
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
+ ___37+[FPMemoryRegion categoryNameForTag:]_block_invoke
+ ___40-[MemoryResourceException _symbolOwners]_block_invoke
+ ___40-[MemoryResourceException _symbolOwners]_block_invoke_2
+ ___42+[FPFootprint _processesBySortingPidDesc:]_block_invoke
+ ___44+[FPSharedCache sharedCacheForDyldSnapshot:]_block_invoke
+ ___44+[FPSharedCache sharedCacheForDyldSnapshot:]_block_invoke_2
+ ___44-[FPFootprint _processesBySortingFootprint:]_block_invoke
+ ___44-[MemoryResourceException extractCorpseInfo]_block_invoke
+ ___47-[FPFootprint _finalizeAndCompactMap:withName:]_block_invoke
+ ___51-[FPUserProcess _addSubrangesForRegion:purgeState:]_block_invoke
+ ___52-[RMECacheEnumerator initCacheEnumeratorWithVolume:]_block_invoke
+ ___55-[MemoryResourceException prettyPrintIOAccelMemoryInfo]_block_invoke
+ ___56+[RMECacheEnumerator(ContainerSupport) getLogContainer:]_block_invoke
+ ___56-[FPUserProcess _gatherMemoryData:extendedInfoProvider:]_block_invoke
+ ___57+[RMECacheEnumerator(ContainerSupport) getEPLProfilePath]_block_invoke
+ ___57-[FPFootprint ioSurfaceExtendedInfoDetailsAtAddress:for:]_block_invoke
+ ___59-[FPFootprint ioAccelMemoryInfoDetailsAtAddress:for:error:]_block_invoke
+ ___65-[FPUserProcess _populateMemoryRegionWithPageQueries:regionInfo:]_block_invoke
+ ___75-[FPFootprint _generateProcessToProcessGroupsWithSharedCacheProcessGroups:]_block_invoke
+ ___77-[MemoryResourceException _populateAddtionalMetadataWithOptions:timeoutSecs:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___FPLedgerIndexForLedger_block_invoke
+ ___RMEGetTimeOrderedLogPathsMatchingPrefs_block_invoke
+ ___RMEGetXPCConnection_block_invoke
+ ___RMEGetXPCConnection_block_invoke_2
+ ___RMEIsAutoSubmitEnabled_block_invoke
+ ___RMEShouldLogThirdPartyProcesses_block_invoke
+ ___ReportMemoryExceptionFromTask_block_invoke
+ ___ReportMemoryExceptionFromTask_block_invoke.19
+ ____extendedInfoStorage_block_invoke
+ ___block_descriptor_102_e8_32s40s48s56s64r72r_e93_B56?0Q8Q16^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQ}24i32"NSString"36"NSString"44B52ls32l8s40l8s48l8r64l8s56l8r72l8
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_32_e12_B24?0Q8^v16l
+ ___block_descriptor_32_e12_v24?0^v8Q16l
+ ___block_descriptor_32_e25_q24?0"NSURL"8"NSURL"16l
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___block_descriptor_32_e33_q24?0"FPProcess"8"FPProcess"16l
+ ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_32_e9_r*16?0q8l
+ ___block_descriptor_40_e12_B24?0Q8^v16l
+ ___block_descriptor_40_e52_B24?0"IOSurfaceDebugDescription"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_40_e8_32r_e30_v16?0^{dyld_shared_cache_s=}8lr32l8
+ ___block_descriptor_40_e8_32r_e37_v24?0{kcdata_iter=^{kcdata_item}^v}8lr32l8
+ ___block_descriptor_40_e8_32r_e9_v16?0r*8lr32l8
+ ___block_descriptor_40_e8_32s_e11_q24?0816ls32l8
+ ___block_descriptor_40_e8_32s_e37_v24?0{kcdata_iter=^{kcdata_item}^v}8ls32l8
+ ___block_descriptor_48_e22_v24?0{_CSTypeRef=QQ}8l
+ ___block_descriptor_48_e8_32r40r_e22_v24?0{_CSTypeRef=QQ}8lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e27_B24?0"NSURL"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSArray"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e23_v16?0^{dyld_image_s=}8ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSArray"16lr40l8r48l8s32l8
+ ___block_descriptor_61_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r_e18_v36?0r*8Q16Q24i32ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e8_v16?0Q8ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40r48r_e18_v40?0^i8Q16Q24Q32lr40l8r48l8s32l8
+ ___block_descriptor_73_e8_32s40s48s56s64s_e12_v24?0^8Q16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_83_e8_32s40s48r56r_e18_v40?0^i8Q16Q24Q32ls32l8r48l8r56l8s40l8
+ ___block_literal_global
+ ___block_literal_global.102
+ ___block_literal_global.104
+ ___block_literal_global.107
+ ___block_literal_global.11
+ ___block_literal_global.220
+ ___block_literal_global.470
+ ___block_literal_global.496
+ ___block_literal_global.5
+ ___block_literal_global.91
+ ___block_literal_global.96
+ ___extractBinaryImageInfo_block_invoke
+ ___fp_map_destroy_block_invoke
+ ___getLogPathsSortedByProcessFrequencyForLogs_block_invoke
+ ___getLogPathsSortedByProcessFrequencyForLogs_block_invoke_2
+ ___isNotCircularException_block_invoke
+ ___machToNsec_block_invoke
+ ___populateSystemVersionFromHost_block_invoke
+ __instanceCache
+ __instanceCacheLock
+ _coalition_id_for_pid
+ _copyCoalitionDict
+ _dateFromSecondsAndMicroSeconds
+ _execPathForPid
+ _extractBundleId
+ _extractCoalitionBundleId
+ _filesWithinAgeThreshold
+ _filesWithinSizeThreshold
+ _footprintForVmObject
+ _gLedgerCount
+ _gRegionLabels
+ _gVMLedgerNames
+ _getKinfoProcForPid
+ _getLogPathsSortedByProcessFrequencyForLogs
+ _internForSegmentName.internPool
+ _internForSymbolOwnerPath.internPool
+ _isMSLEnabledForTask
+ _isValidLimitVal
+ _ledgerForId
+ _mergePrefsFromInput
+ _mergePrefsFromInputProcessList
+ _newProcessStructures
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$UTF8String
+ _objc_msgSend$UUID
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
+ _objc_msgSend$_generateMemgraphWithContentLevel:timeoutSecs:memgraphFailedReasonOut:
+ _objc_msgSend$_isAlive
+ _objc_msgSend$_nameForBsdInfo:
+ _objc_msgSend$_populateAddtionalMetadataWithOptions:timeoutSecs:
+ _objc_msgSend$_populateMemoryRegionWithPageQueries:regionInfo:
+ _objc_msgSend$_populateTask
+ _objc_msgSend$_saveLogFileWithHandle:error:
+ _objc_msgSend$_setIdleExitStatusFromDirtyFlags:
+ _objc_msgSend$_setPriority:
+ _objc_msgSend$_symbolOwners
+ _objc_msgSend$addAllNodesFromTaskWithError:
+ _objc_msgSend$addLedgerData:count:
+ _objc_msgSend$addMemoryObject:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addProcess:
+ _objc_msgSend$addSubrange:memoryTotal:
+ _objc_msgSend$address
+ _objc_msgSend$alignment
+ _objc_msgSend$allKeys
+ _objc_msgSend$allValues
+ _objc_msgSend$allocationSize
+ _objc_msgSend$analyzeData
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$asNumber
+ _objc_msgSend$auxData
+ _objc_msgSend$auxDataName
+ _objc_msgSend$backtrace
+ _objc_msgSend$backtraceLength
+ _objc_msgSend$baseAddress
+ _objc_msgSend$boolValue
+ _objc_msgSend$breakDownPhysFootprint
+ _objc_msgSend$bytes
+ _objc_msgSend$cachedCopy
+ _objc_msgSend$categoryNameForTag:
+ _objc_msgSend$cleanSize
+ _objc_msgSend$code
+ _objc_msgSend$collectDataWithCompletionQueue:completionBlock:
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$containsAddress:
+ _objc_msgSend$containsFakeRegion
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$copy
+ _objc_msgSend$couldHaveProcessView
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createMetaDataDict
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$date
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$description
+ _objc_msgSend$detachFromTask
+ _objc_msgSend$detailedAuxData
+ _objc_msgSend$detailedAuxDataName
+ _objc_msgSend$detailedName
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dirtyLength
+ _objc_msgSend$dirtySize
+ _objc_msgSend$dispatchQueueNameForSerialNumber:
+ _objc_msgSend$dispatchQueueSerialNumber
+ _objc_msgSend$displayString
+ _objc_msgSend$doOwnedAccountingAdjustments
+ _objc_msgSend$domain
+ _objc_msgSend$eligibleForProcessView
+ _objc_msgSend$eligibleForSubrangesUsingPageSize:
+ _objc_msgSend$end
+ _objc_msgSend$endAtTime:
+ _objc_msgSend$endProcessHeader:
+ _objc_msgSend$ensureMemoryObject
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$enumerateRegions:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$errors
+ _objc_msgSend$executablePath
+ _objc_msgSend$extendedInfoForRegionType:at:extendedInfoProvider:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$fileURLWithPath:isDirectory:
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
+ _objc_msgSend$generateMemoryGraphWithContentLevel:memgraphFailedReasonOut:
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getCString:maxLength:encoding:
+ _objc_msgSend$getEPLProfilePath
+ _objc_msgSend$getLogContainer:
+ _objc_msgSend$getLogPathsSortedByTime
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$globalErrors
+ _objc_msgSend$hasNoFootprint
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hash
+ _objc_msgSend$height
+ _objc_msgSend$hiddenFromDisplay
+ _objc_msgSend$idleExitStatus
+ _objc_msgSend$inSharedCache
+ _objc_msgSend$init
+ _objc_msgSend$initCacheEnumeratorWithVolume:
+ _objc_msgSend$initFileURLWithPath:
+ _objc_msgSend$initSummary:
+ _objc_msgSend$initUniqueProcessGroup
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithBsdInfo:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithBytesNoCopy:length:deallocator:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithCorePath:originalBinaryPaths:error:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithObjectsAndKeys:
+ _objc_msgSend$initWithPID:task:processName:is64Bit:options:
+ _objc_msgSend$initWithPlistRepresentation:
+ _objc_msgSend$initWithProcesses:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$initWithTask:
+ _objc_msgSend$initWithTask:options:
+ _objc_msgSend$initWithTimeIntervalSince1970:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initWithVMUTask:options:
+ _objc_msgSend$initWithValue:shouldAggregate:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$ioAccelMemoryInfoDetailsAtAddress:for:error:
+ _objc_msgSend$ioSurfaceExtendedInfoDetailsAtAddress:for:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isFake
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$isSharingAnalysisDisabled
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$lastObject
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$length
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$mappedSize
+ _objc_msgSend$mappings
+ _objc_msgSend$member:
+ _objc_msgSend$memoryObject
+ _objc_msgSend$memoryPool
+ _objc_msgSend$memoryRegions
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$nextObject
+ _objc_msgSend$nextValidURL
+ _objc_msgSend$nonretainedObjectValue
+ _objc_msgSend$now
+ _objc_msgSend$null
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$object_id
+ _objc_msgSend$offset
+ _objc_msgSend$ownedExclusivelyByParentProcess
+ _objc_msgSend$ownerPid
+ _objc_msgSend$pageSize
+ _objc_msgSend$path
+ _objc_msgSend$pathExtension
+ _objc_msgSend$physicalFootprint
+ _objc_msgSend$physicalFootprintPeak
+ _objc_msgSend$pid
+ _objc_msgSend$pixelFormat
+ _objc_msgSend$plistRepresentationWithOptions:
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
+ _objc_msgSend$privateSharedCacheRegion
+ _objc_msgSend$processIDs
+ _objc_msgSend$processName
+ _objc_msgSend$processSnapshotGraphWithOptions:
+ _objc_msgSend$processWithBsdInfo:
+ _objc_msgSend$processes
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$purgeable
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$readDataToEndOfFileAndReturnError:
+ _objc_msgSend$reason
+ _objc_msgSend$reclaimableSize
+ _objc_msgSend$releaseAnalyzedTask
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$residentLength
+ _objc_msgSend$sampleAllThreadsOnce
+ _objc_msgSend$scanInt:
+ _objc_msgSend$segment
+ _objc_msgSend$set
+ _objc_msgSend$setAbandonedMarkingEnabled:
+ _objc_msgSend$setBreakDownPhysFootprint:
+ _objc_msgSend$setCleanSize:
+ _objc_msgSend$setDetailedName:
+ _objc_msgSend$setDirtySize:
+ _objc_msgSend$setDisplayString:
+ _objc_msgSend$setEnd:
+ _objc_msgSend$setExactScanningEnabled:
+ _objc_msgSend$setExtendedInfo:
+ _objc_msgSend$setFormatter:
+ _objc_msgSend$setHasNoFootprint:
+ _objc_msgSend$setInSharedCache:
+ _objc_msgSend$setMaxInteriorOffset:
+ _objc_msgSend$setMemoryObject:
+ _objc_msgSend$setMemoryRegions:
+ _objc_msgSend$setName:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setObjectContentLevel:
+ _objc_msgSend$setObject_id:
+ _objc_msgSend$setOffset:
+ _objc_msgSend$setOwnedExclusivelyByParentProcess:
+ _objc_msgSend$setOwnerPid:
+ _objc_msgSend$setPid:
+ _objc_msgSend$setReclaimableSize:
+ _objc_msgSend$setResourceValue:forKey:error:
+ _objc_msgSend$setScanningMask:
+ _objc_msgSend$setSegment:
+ _objc_msgSend$setShare_mode:
+ _objc_msgSend$setSharingAnalysisDisabled:
+ _objc_msgSend$setSize:
+ _objc_msgSend$setStart:
+ _objc_msgSend$setSwappedSize:
+ _objc_msgSend$setUnusedSharedCacheRegion:
+ _objc_msgSend$setUser_tag:
+ _objc_msgSend$setVerbose:
+ _objc_msgSend$setVmRegionInfoFlags:
+ _objc_msgSend$setWired:
+ _objc_msgSend$sharedCache
+ _objc_msgSend$sharedCacheForDyldSnapshot:
+ _objc_msgSend$shouldAggregate
+ _objc_msgSend$size
+ _objc_msgSend$slide
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$start
+ _objc_msgSend$startAtTime:
+ _objc_msgSend$string
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByPaddingToLength:withString:startingAtIndex:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$stringByStandardizingPath
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$strongToStrongObjectsMapTable
+ _objc_msgSend$subrangeList
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$supportsFormattedValue
+ _objc_msgSend$surfaceDescriptions
+ _objc_msgSend$surfaceID
+ _objc_msgSend$swappedSize
+ _objc_msgSend$symbolicator
+ _objc_msgSend$thread
+ _objc_msgSend$threadNameForThread:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$totalCleanSize
+ _objc_msgSend$totalDirtySize
+ _objc_msgSend$totalReclaimableSize
+ _objc_msgSend$totalRegions
+ _objc_msgSend$totalSwappedSize
+ _objc_msgSend$totalWiredSize
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unusedSharedCacheRegion
+ _objc_msgSend$userInfo
+ _objc_msgSend$uuid
+ _objc_msgSend$value
+ _objc_msgSend$valueWithNonretainedObject:
+ _objc_msgSend$valueWithPointer:
+ _objc_msgSend$verbose
+ _objc_msgSend$viewForProcess:
+ _objc_msgSend$virtualAddress
+ _objc_msgSend$vmLedgerNameForTag:
+ _objc_msgSend$warnings
+ _objc_msgSend$weakToStrongObjectsMapTable
+ _objc_msgSend$width
+ _objc_msgSend$wired
+ _objc_msgSend$wiredSize
+ _objc_msgSend$writeData:
+ _shouldBoostCriticalProcesses
+ _uniqueLogsArray
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ " (nofootprint)"
+ "%s - exceptionSpecificLimit: %ld"
+ "%s - final limit: %ld"
+ "%s - fullDiagPerProcessLimit: %ld"
+ "%s - isCriticalProcess: %d, dailyCriticalProcessLimit: %ld"
+ "%s - isLargeExemptProcess: %d"
+ "%s - liteDiagPerProcessLimit: %ld"
+ "%s - specificLimit: %ld"
+ "%s - typeLimit: %ld"
+ "RMEGetLiteLimitForExecName"
+ "RMEGetMemgraphLimitForExecName"
+ "SourceFilename"
+ "SourceLine"
+ "_gcore"
+ "_hasNoFootprint"
+ "hasNoFootprint"
+ "setHasNoFootprint:"

```
