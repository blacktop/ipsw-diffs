## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Versions/A/Symbolication`

```diff

-64567.3.3.0.0
-  __TEXT.__text: 0xb4144
-  __TEXT.__auth_stubs: 0x1df0
-  __TEXT.__objc_methlist: 0x5ea4
+64570.58.1.0.0
+  __TEXT.__text: 0xb7a60
+  __TEXT.__auth_stubs: 0x1fd0
+  __TEXT.__objc_methlist: 0x6658
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xf664
-  __TEXT.__gcc_except_tab: 0x507c
-  __TEXT.__oslogstring: 0x160a
+  __TEXT.__cstring: 0xff7f
+  __TEXT.__gcc_except_tab: 0x5348
+  __TEXT.__oslogstring: 0x1614
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x2860
-  __TEXT.__objc_classname: 0x84f
-  __TEXT.__objc_methname: 0xeeef
-  __TEXT.__objc_methtype: 0x853e
-  __TEXT.__objc_stubs: 0x9860
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0xcf8
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __TEXT.__unwind_info: 0x2990
+  __TEXT.__objc_classname: 0x88d
+  __TEXT.__objc_methname: 0xf75a
+  __TEXT.__objc_methtype: 0x882a
+  __TEXT.__objc_stubs: 0x9a60
+  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__const: 0xe30
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33e0
-  __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_arraydata: 0x718
-  __AUTH_CONST.__auth_got: 0xf10
-  __AUTH_CONST.__const: 0x39e0
-  __AUTH_CONST.__cfstring: 0xca00
-  __AUTH_CONST.__objc_const: 0xc658
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_selrefs: 0x35f0
+  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_arraydata: 0x870
+  __AUTH_CONST.__auth_got: 0x1000
+  __AUTH_CONST.__const: 0x3c70
+  __AUTH_CONST.__cfstring: 0xd760
+  __AUTH_CONST.__objc_const: 0xbf18
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1c20
+  __AUTH.__objc_data: 0x1cc0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc48
+  __DATA.__objc_ivar: 0xc7c
   __DATA.__data: 0xd58
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x608
-  __DATA.__common: 0x9
+  __DATA.__bss: 0x630
+  __DATA.__common: 0xf1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
+  - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MallocStackLogging.framework/Versions/A/MallocStackLogging

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 81116151-EC8C-3F0D-B0FC-CA815F946D31
-  Functions: 3000
-  Symbols:   7199
-  CStrings:  7457
+  UUID: CA0F33A1-95E2-3F8D-BF9D-E544A772A69C
+  Functions: 3112
+  Symbols:   7499
+  CStrings:  7746
 
Symbols:
+ +[VMUClassInfo _genericBlockByrefInfo].cold.1
+ +[VMUClassInfo swiftValueWithMetadata:objectIdentifier:]
+ +[VMUClassInfo swiftValueWithMetadata:objectIdentifier:].cold.1
+ +[VMUClassInfo swiftValueWithMetadata:objectIdentifier:].cold.2
+ +[VMUClassInfo swiftValueWithMetadata:objectIdentifier:].cold.3
+ +[VMUClassInfo swiftValueWithMetadata:objectIdentifier:].cold.4
+ +[VMULeakDetector _consolidatedRootLeakDescriptionsForTree:].cold.1
+ +[VMUProcessObjectGraph createWithTask:error:]
+ -[VMUAutoreleasePoolsAnalyzer .cxx_destruct]
+ -[VMUAutoreleasePoolsAnalyzer analysisSummaryWithError:]
+ -[VMUAutoreleasePoolsAnalyzer analyzerName]
+ -[VMUAutoreleasePoolsAnalyzer autoreleasePoolChain]
+ -[VMUAutoreleasePoolsAnalyzer autoreleasePoolNodesByThreadIndex]
+ -[VMUAutoreleasePoolsAnalyzer autoreleasePoolsStatsInfo]
+ -[VMUAutoreleasePoolsAnalyzer dealloc]
+ -[VMUAutoreleasePoolsAnalyzer detector]
+ -[VMUAutoreleasePoolsAnalyzer findHottestEmptyAutoreleasePoolPage:]
+ -[VMUAutoreleasePoolsAnalyzer initWithGraph:regionIdentifier:debugTimer:]
+ -[VMUAutoreleasePoolsAnalyzer iterateAutoreleasePoolsInThreadsGroupingByType:showVirtualSize:extraReleasesCount:withBlock:]
+ -[VMUAutoreleasePoolsAnalyzer iterateThroughPoolsPerThread:withBlock:]
+ -[VMUAutoreleasePoolsAnalyzer memoryTreeHeldByAutoreleasedNode:node:]
+ -[VMUAutoreleasePoolsAnalyzer offsets]
+ -[VMUAutoreleasePoolsAnalyzer options]
+ -[VMUAutoreleasePoolsAnalyzer populateAutoreleasePoolsDetails]
+ -[VMUAutoreleasePoolsAnalyzer reachableOutsideOfAutoreleasePoolsMap]
+ -[VMUAutoreleasePoolsAnalyzer reattachAutoreleasePoolsChainFromHottestToColdest:]
+ -[VMUAutoreleasePoolsAnalyzer setAutoreleasePoolChain:]
+ -[VMUAutoreleasePoolsAnalyzer setAutoreleasePoolNodesByThreadIndex:]
+ -[VMUAutoreleasePoolsAnalyzer setOptions:]
+ -[VMUAutoreleasePoolsAnalyzer setReachableOutsideOfAutoreleasePoolsMap:]
+ -[VMUAutoreleasePoolsAnalyzer setThreadNamesByThreadIndex:]
+ -[VMUAutoreleasePoolsAnalyzer setUnreferencedAutoreleasePoolNodes:]
+ -[VMUAutoreleasePoolsAnalyzer threadNamesByThreadIndex]
+ -[VMUAutoreleasePoolsAnalyzer unreferencedAutoreleasePoolNodes]
+ -[VMUCachedPointerFieldInfo .cxx_destruct]
+ -[VMUCachedPointerFieldInfo initWithRootField:leafField:leafOffsetInRootField:]
+ -[VMUCallTreeRoot initWithCallGraphFile:fileHeader:topFunctionsList:binaryImagesList:error:]
+ -[VMUClassInfo _objcABIFromObjectIdentifier:].cold.1
+ -[VMUClassInfo _setSuperclassOffset:]
+ -[VMUClassInfo initWithClosureContext:typeInfo:infoMap:swiftFieldMetadataContext:].cold.1
+ -[VMUClassInfo initWithClosureContext:typeInfo:infoMap:swiftFieldMetadataContext:].cold.2
+ -[VMUClassInfo initWithClosureContext:typeInfo:infoMap:swiftFieldMetadataContext:].cold.3
+ -[VMUClassInfo initWithClosureContext:typeInfo:infoMap:swiftFieldMetadataContext:].cold.4
+ -[VMUClassPatternMatcher matchesNodeDetails:orNodeDescription:].cold.1
+ -[VMUFieldInfo _fullIvarNameAtOffset:leafOffset:depth:].cold.1
+ -[VMUKernelCoreMemoryScanner _shouldScanVMregion:]
+ -[VMUKernelCoreMemoryScanner addRootNodesFromTaskWithError:].cold.1
+ -[VMUKernelCoreMemoryScanner getCachedScanInfoForClassWithIsa:classInfo:scanCaches:]
+ -[VMUKernelCoreMemoryScanner scanLocalMemory:atOffset:node:length:isa:scanCaches:fieldInfo:stride:recorder:]
+ -[VMUMutableClassInfo setSuperclassOffset:]
+ -[VMUObjectIdentifier _classInfoForMemory:length:atOffset:remoteAddress:].cold.1
+ -[VMUObjectIdentifier _isUnrealizedObjCClass:recursionDepth:]
+ -[VMUObjectIdentifier _isaPointerRefersToVTable:remoteAddress:symbol:symbolNameOut:]
+ -[VMUObjectIdentifier findCFTypes].cold.1
+ -[VMUObjectIdentifier isValidPointer:]
+ -[VMUObjectIdentifier labelForCStructureWithMemory:length:remoteAddress:classInfo:]
+ -[VMUObjectIdentifier labelForMemory:length:remoteAddress:classInfo:usingHandlerBlock:].cold.1
+ -[VMUObjectIdentifier labelForNSXPCConnection:length:remoteAddress:].cold.1
+ -[VMUObjectIdentifier labelForNSXPCInterface:length:remoteAddress:].cold.1
+ -[VMUObjectIdentifier labelForOSTransaction:length:remoteAddress:].cold.1
+ -[VMUObjectIdentifier labelForOSXPCDictionary:length:remoteAddress:].cold.1
+ -[VMUObjectIdentifier labelForOSXPCDictionaryStorageNode:length:remoteAddress:]
+ -[VMUObjectIdentifier labelForOSXPCString:length:remoteAddress:]
+ -[VMUObjectIdentifier labelForSwiftContiguousArrayStorage:length:remoteAddress:]
+ -[VMUObjectIdentifier labelForSwiftDictionaryStorage:length:remoteAddress:]
+ -[VMUObjectIdentifier labelForSwiftSetStorage:length:remoteAddress:]
+ -[VMUObjectIdentifier locateSwiftValuesInAttributeGraph]
+ -[VMUObjectIdentifier noLabelForOSXPCObject:length:remoteAddress:].cold.1
+ -[VMUObjectIdentifier setValidVMRange:]
+ -[VMUObjectIdentifier setupIsaTranslator].cold.1
+ -[VMUObjectIdentifier validVMRange]
+ -[VMUObjectIdentifierDriverKitSupport classInfoForDriverKitMemory:length:atOffset:translatedIsa:symbol:remoteAddress:]
+ -[VMUProcInfo isSemiCriticalProcess].cold.1
+ -[VMUProcInfo shouldAnalyzeWithCorpse].cold.1
+ -[VMUProcessDescription _bundleLock].cold.1
+ -[VMUProcessDescription launchTime]
+ -[VMUProcessDescription taskIsCorpse]
+ -[VMUSampler initWithPID:task:processName:is64Bit:options:].cold.1
+ -[VMUStackLogReaderBase shouldIgnoreSymbolWithName:binaryPath:].cold.1
+ -[VMUTask stripExtraPointerBits:]
+ -[VMUTaskMemoryScanner _addSpecialNodesFromTask].cold.1
+ -[VMUTaskMemoryScanner _identifyAttributeGraphAllocationsIfPreciseIdentificationIsUnavailable]
+ -[VMUTaskMemoryScanner _identifySwiftAsyncTaskSlabs].cold.1
+ -[VMUTaskMemoryScanner _identifySwiftAsyncTaskSlabs].cold.2
+ -[VMUTaskMemoryScanner _identifySwiftAsyncTaskSlabs].cold.3
+ -[VMUTaskMemoryScanner _identifySwiftAsyncTaskSlabs].cold.4
+ -[VMUTaskMemoryScanner _identifySwiftAsyncTaskSlabs].cold.5
+ -[VMUTaskMemoryScanner _identifyXPCDictionaryStorageReferencedByBlock:]
+ -[VMUTaskMemoryScanner _rangeOfClassStructureForPossibleUnrealizedSwiftClassWithIsa:]
+ -[VMUTaskMemoryScanner _recursivelyIdentifySwiftAsyncTaskSlabs:containerRange:remoteBlock:mappedBlock:asyncTaskSlabMetadataIsa:nestingLevel:].cold.1
+ -[VMUTaskMemoryScanner _recursivelyIdentifySwiftAsyncTaskSlabs:containerRange:remoteBlock:mappedBlock:asyncTaskSlabMetadataIsa:nestingLevel:].cold.2
+ -[VMUTaskMemoryScanner _recursivelyIdentifySwiftAsyncTaskSlabs:containerRange:remoteBlock:mappedBlock:asyncTaskSlabMetadataIsa:nestingLevel:].cold.3
+ -[VMUTaskMemoryScanner _recursivelyIdentifySwiftAsyncTaskSlabs:containerRange:remoteBlock:mappedBlock:asyncTaskSlabMetadataIsa:nestingLevel:].cold.4
+ -[VMUTaskMemoryScanner _untypedMallocBlockNodeReferencedFromAddress:]
+ -[VMUTaskMemoryScanner _withReaderBlockForHeapEnumeration:]
+ -[VMUTaskMemoryScanner _withReaderBlockForHeapEnumeration:].cold.1
+ -[VMUTaskMemoryScanner getCachedScanInfoForClassWithIsa:classInfo:scanCaches:]
+ -[VMUTaskMemoryScanner scanLocalMemory:atOffset:node:length:isa:scanCaches:fieldInfo:stride:recorder:]
+ -[VMUVMRegionIdentifier _recordRegionsAroundAddress:regionDescriptionOptions:].cold.1
+ GCC_except_table100
+ GCC_except_table103
+ GCC_except_table107
+ GCC_except_table112
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table129
+ GCC_except_table138
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table148
+ GCC_except_table150
+ GCC_except_table162
+ GCC_except_table167
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table191
+ GCC_except_table201
+ GCC_except_table84
+ GCC_except_table99
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._autoreleasePoolChain
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._autoreleasePoolNodesByThreadIndex
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._autoreleasePoolsStatsInfo
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._detector
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._offsets
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._options
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._reachableOutsideOfAutoreleasePoolsMap
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._threadNamesByThreadIndex
+ OBJC_IVAR_$_VMUAutoreleasePoolsAnalyzer._unreferencedAutoreleasePoolNodes
+ OBJC_IVAR_$_VMUCachedPointerFieldInfo._leafField
+ OBJC_IVAR_$_VMUCachedPointerFieldInfo._leafOffsetInRootField
+ OBJC_IVAR_$_VMUCachedPointerFieldInfo._rootField
+ OBJC_IVAR_$_VMUObjectIdentifier._attributeGraphSwiftMetadataToClassInfo
+ OBJC_IVAR_$_VMUObjectIdentifier._lastClassInfoForMemoryClassInfo
+ OBJC_IVAR_$_VMUObjectIdentifier._lastClassInfoForMemoryIsa
+ OBJC_IVAR_$_VMUObjectIdentifier._objcEmptyCacheAddress
+ OBJC_IVAR_$_VMUObjectIdentifier._swiftValueInAttributeGraphAddressesToTypeMetadata
+ OBJC_IVAR_$_VMUObjectIdentifier._validVMRange
+ OBJC_IVAR_$_VMUProcessDescription._taskType
+ OBJC_IVAR_$_VMUTaskMemoryScanner._attributeGraphFakeRootNode
+ OBJC_IVAR_$_VMUTaskMemoryScanner._attributeGraphZoneIndex
+ OBJC_IVAR_$_VMUTaskMemoryScanner._xpcDictionaryStorageClassInfoIndex
+ VMUMarkObject.cold.1
+ VMUOAHRuntimeLocation.cold.1
+ VMUSanitizePath.cold.1
+ VMUTask_foreach_malloc_zone.cold.1
+ VMUTask_foreach_malloc_zone.cold.2
+ _CRGetOSVersionDictionary.cold.1
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_VMUAutoreleasePoolsAnalyzer
+ _OBJC_CLASS_$_VMUCachedPointerFieldInfo
+ _OBJC_METACLASS_$_VMUAutoreleasePoolsAnalyzer
+ _OBJC_METACLASS_$_VMUCachedPointerFieldInfo
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _VMUCallMallocEnumeratorWithAttributeGraphWorkaround
+ _VMUGraphNodeIsRoot
+ _VMUGraphNodeIsSpecialMallocNode
+ _ZL19serializerLogHandlev.cold.1
+ _ZL20_swiftFieldsForClassyP8NSStringP27libSwiftRemoteMirrorWrapperP15VMUClassInfoMapj.cold.1
+ _ZL20_swiftFieldsForClassyP8NSStringP27libSwiftRemoteMirrorWrapperP15VMUClassInfoMapj.cold.2
+ _ZL20_swiftFieldsForClassyP8NSStringP27libSwiftRemoteMirrorWrapperP15VMUClassInfoMapj.cold.3
+ _ZL20_swiftFieldsForClassyP8NSStringP27libSwiftRemoteMirrorWrapperP15VMUClassInfoMapj.cold.4
+ _ZL20_swiftFieldsForClassyP8NSStringP27libSwiftRemoteMirrorWrapperP15VMUClassInfoMapj.cold.5
+ _ZL22demangleSwiftClassNamePKc.cold.1
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.1
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.2
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.3
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.4
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.5
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.6
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.7
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.8
+ _ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj.cold.9
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke.447
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke.590
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_10.670
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_11.688
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_12.694
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_13.700
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_14.709
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_15.751
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_2.480
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_2.591
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_3.484
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_3.595
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_4.604
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_5.619
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_6.628
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_7.637
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_8.646
+ __34-[VMUScanOverlay initWithScanner:]_block_invoke_9.661
+ __39-[VMUTaskMemoryScanner _fixupBlockIsas]_block_invoke.216
+ __39-[VMUTaskMemoryScanner _fixupBlockIsas]_block_invoke.225
+ __41-[VMUObjectIdentifier setupIsaTranslator]_block_invoke.177
+ __41-[VMUObjectIdentifier setupIsaTranslator]_block_invoke.180
+ __43-[VMUObjectIdentifier findCFTypes_version2]_block_invoke.119
+ __45-[VMUKernelCoreMemoryScanner _fixupBlockIsas]_block_invoke.121
+ __45-[VMUKernelCoreMemoryScanner _fixupBlockIsas]_block_invoke.130
+ __46-[VMUClassInfo _applyExtendedLayout:withSize:]_block_invoke.109
+ __47-[VMUVMRegionIdentifier initWithGraph:options:]_block_invoke.137
+ __48-[VMUTaskMemoryScanner initWithVMUTask:options:]_block_invoke.66
+ __48-[VMUTaskMemoryScanner initWithVMUTask:options:]_block_invoke.79
+ __54-[VMUObjectIdentifier buildIsaToObjectLabelHandlerMap]_block_invoke.228
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.313
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.319
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.322
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2.320
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2.323
+ __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_3.321
+ __56-[VMUTaskMemoryScanner addMallocNodesFromTaskWithError:]_block_invoke.cold.1
+ __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.352
+ __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.367
+ __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.384
+ __59-[VMUTaskMemoryScanner _withReaderBlockForHeapEnumeration:]_block_invoke.112
+ __61-[VMUKernelCoreMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.166
+ __61-[VMUKernelCoreMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.172
+ __61-[VMUKernelCoreMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.173
+ __61-[VMUKernelCoreMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2.174
+ __62-[VMUAutoreleasePoolsAnalyzer populateAutoreleasePoolsDetails]_block_invoke.63
+ __62-[VMUAutoreleasePoolsAnalyzer populateAutoreleasePoolsDetails]_block_invoke.80
+ __62-[VMUAutoreleasePoolsAnalyzer populateAutoreleasePoolsDetails]_block_invoke.83
+ __62-[VMUAutoreleasePoolsAnalyzer populateAutoreleasePoolsDetails]_block_invoke_2.84
+ __62-[VMUKernelCoreMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.203
+ __62-[VMUKernelCoreMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.224
+ __68-[VMUProcessDescription initWithVMUTaskMemoryCache:getBinariesList:]_block_invoke.46
+ __69-[VMUAutoreleasePoolsAnalyzer memoryTreeHeldByAutoreleasedNode:node:]_block_invoke.4
+ __78-[VMUClassInfo instanceSpecificInfoForObject:ofSize:withScanner:memoryReader:]_block_invoke.127
+ __78-[VMUClassInfo instanceSpecificInfoForObject:ofSize:withScanner:memoryReader:]_block_invoke.134
+ __78-[VMUClassInfo instanceSpecificInfoForObject:ofSize:withScanner:memoryReader:]_block_invoke_2.130
+ __98-[VMUStackLogReaderBase identifyNonObjectsUsingStackBacktraces:classInfoMap:classInfoSetterBlock:]_block_invoke.371
+ __Block_byref_object_copy_.16
+ __Block_byref_object_copy_.67
+ __Block_byref_object_dispose_.17
+ __Block_byref_object_dispose_.68
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS_VMUAutoreleasePoolsAnalyzer
+ __OBJC_$_INSTANCE_METHODS_VMUCachedPointerFieldInfo
+ __OBJC_$_INSTANCE_VARIABLES_VMUAutoreleasePoolsAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_VMUCachedPointerFieldInfo
+ __OBJC_$_PROP_LIST_VMUAutoreleasePoolsAnalyzer
+ __OBJC_CLASS_RO_$_VMUAutoreleasePoolsAnalyzer
+ __OBJC_CLASS_RO_$_VMUCachedPointerFieldInfo
+ __OBJC_METACLASS_RO_$_VMUAutoreleasePoolsAnalyzer
+ __OBJC_METACLASS_RO_$_VMUCachedPointerFieldInfo
+ __ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj
+ __ZL31determineBinaryPathForSwiftTypeP8NSStringyP19VMUObjectIdentifier10_CSTypeRef
+ __ZL34_debugEnvironmentVariableIsEnabledP8NSStringb
+ __ZL37_debugSwiftSubfieldDumpSwiftChildInfojPKc15swift_childinfoP31_DummyVMUSwiftReflectionContext
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne190102EPKvm
+ __ZNKSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI14RangeAndStringNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI25_CSBinaryImageInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI30_CSBinaryRelocationInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS6_IyEEEEEEPvEENS_22__hash_node_destructorINS6_ISI_EEEEE5resetB8ne190102EPSI_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUClassInfojEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUFieldInfojEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringjEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__111__sift_downB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_OT0_NS_15iterator_traitsIS9_E15difference_typeES9_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS5_IyEEEEEELi0EEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIS5_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_prepareB8ne190102EmRS5_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__116__insertion_sortB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
+ __ZNSt3__119__partial_sort_implB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_S8_EET1_S9_S9_T2_OT0_
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne190102EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne190102EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne190102EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI13SwiftFieldKeyjEEPvEEEEEclB8ne190102EPS7_
+ __ZNSt3__126__insertion_sort_unguardedB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEbT1_S9_T0_
+ __ZNSt3__131__partition_with_equals_on_leftB8ne190102INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEET0_S9_S9_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8ne190102INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEENS_4pairIT0_bEESA_SA_T1_
+ __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEjT1_S9_S9_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_S9_S9_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_S9_S9_S9_T0_
+ __ZNSt3__19__sift_upB8ne190102INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZNSt3__19allocatorI10_CSTypeRefE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorI14RangeAndStringE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorI25_CSBinaryImageInformationE17allocate_at_leastB8ne190102Em
+ __ZNSt3__19allocatorI30_CSBinaryRelocationInformationE17allocate_at_leastB8ne190102Em
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZZ15VMUSanitizePathE20cachedSanitizedPaths
+ __ZZ15VMUSanitizePathE9onceToken
+ __ZZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbjE27dispatchEnumConfigOnceToken
+ __ZZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbjE30preciselyScanMultiPayloadEnums
+ __ZZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbjE31preciselyScanSinglePayloadEnums
+ ___50-[VMUKernelCoreMemoryScanner _shouldScanVMregion:]_block_invoke
+ ___56-[VMUObjectIdentifier locateSwiftValuesInAttributeGraph]_block_invoke
+ ___56-[VMUObjectIdentifier locateSwiftValuesInAttributeGraph]_block_invoke_2
+ ___59-[VMUTaskMemoryScanner _withReaderBlockForHeapEnumeration:]_block_invoke
+ ___62-[VMUAutoreleasePoolsAnalyzer populateAutoreleasePoolsDetails]_block_invoke
+ ___62-[VMUAutoreleasePoolsAnalyzer populateAutoreleasePoolsDetails]_block_invoke_2
+ ___67-[VMUAutoreleasePoolsAnalyzer findHottestEmptyAutoreleasePoolPage:]_block_invoke
+ ___67-[VMUObjectIdentifier labelForNSXPCInterface:length:remoteAddress:]_block_invoke
+ ___69-[VMUAutoreleasePoolsAnalyzer memoryTreeHeldByAutoreleasedNode:node:]_block_invoke
+ ___70-[VMUAutoreleasePoolsAnalyzer iterateThroughPoolsPerThread:withBlock:]_block_invoke
+ ___78-[VMUTaskMemoryScanner getCachedScanInfoForClassWithIsa:classInfo:scanCaches:]_block_invoke
+ ___81-[VMUAutoreleasePoolsAnalyzer reattachAutoreleasePoolsChainFromHottestToColdest:]_block_invoke
+ ___84-[VMUKernelCoreMemoryScanner getCachedScanInfoForClassWithIsa:classInfo:scanCaches:]_block_invoke
+ ___94-[VMUTaskMemoryScanner _identifyAttributeGraphAllocationsIfPreciseIdentificationIsUnavailable]_block_invoke
+ ___VMUSanitizePath_block_invoke
+ ____ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kindyP15VMUClassInfoMapjP8NSStringPbj_block_invoke
+ ____ZL31determineBinaryPathForSwiftTypeP8NSStringyP19VMUObjectIdentifier10_CSTypeRef_block_invoke
+ ____recursivelyCreateSwiftVariant_block_invoke_3
+ ____variantForNSSlice_block_invoke
+ ___block_descriptor_100_e8_32s40s48bs56r64r_e9_v16?0^v8l
+ ___block_descriptor_112_e8_32s40s48s56s64r_e22_v24?0{_CSTypeRef=QQ}8l
+ ___block_descriptor_123_e8_32s40s48s56s64r72r_e22_v24?0{_CSTypeRef=QQ}8l
+ ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_32_e46_v28?0Q8"NSObject<OS_dispatch_mach_msg>"16i24l
+ ___block_descriptor_40_e8_32s_e21_v20?0I8"NSString"12l
+ ___block_descriptor_40_e8_32s_e42_v28?0"VMUFieldInfo"8"VMUFieldInfo"16I24l
+ ___block_descriptor_40_e8_32s_e8_Q16?0Q8l
+ ___block_descriptor_40_e8_32s_e8_v16?08l
+ ___block_descriptor_48_e26_"VMUMutableFieldInfo"8?0lu32l8u40l8
+ ___block_descriptor_48_e8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_48_e8_32s40s_e39_v68?0I8I12I16{?=^{?}{?=QIQ}^{?}}20^B60l
+ ___block_descriptor_48_e8_32s40s_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24l
+ ___block_descriptor_48_e8_32s_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24l
+ ___block_descriptor_56_e8_32s40r_e39_v68?0I8I12I16{?=^{?}{?=QIQ}^{?}}20^B60l
+ ___block_descriptor_56_e8_32s40s48r_e25_v44?0I8{?=Qb60b4}12^B36l
+ ___block_descriptor_56_e8_32s40s_e39_v68?0I8I12I16{?=^{?}{?=QIQ}^{?}}20^B60l
+ ___block_descriptor_60_e8_32r40r_e28_v24?0"VMUFieldInfo"8I16I20l
+ ___block_descriptor_60_e8_32s40bs48r_e12_v24?0^Q8Q16l
+ ___block_descriptor_60_e8_32s40bs_e25_v16?0?<v?Ii?<v?^v>>8l
+ ___block_descriptor_64_e5_B8?0lu32l8u40l8
+ ___block_descriptor_64_e8_32s40bs48r_e39_v68?0I8I12I16{?=^{?}{?=QIQ}^{?}}20^B60l
+ ___block_descriptor_64_e8_32s40r48r56r_e8_v12?0I8l
+ ___block_descriptor_64_e8_32s40s48s56s_e32_v36?0Q8"VMUClassInfo"16I24^B28l
+ ___block_descriptor_64_e8_32s_e8_Q16?0Q8l
+ ___block_descriptor_68_e8_32s40bs48r56r_e25_v24?0"VMUVMRegion"8^B16l
+ ___block_descriptor_68_e8_32s40bs_e28_v24?0"VMUFieldInfo"8I16I20l
+ ___block_descriptor_68_e8_32s40s48s_e25_v16?0?<v?Ii?<v?^v>>8l
+ ___block_descriptor_72_ea8_32s40s48s56s64r_e35_v32?0"NSString"8"NSString"16^B24l
+ ___block_descriptor_80_e8_32s40s48s56bs64r_e39_v68?0I8I12I16{?=^{?}{?=QIQ}^{?}}20^B60l
+ ___block_descriptor_80_e8_32s40s48s56r_e9_v16?0^?8l
+ ___block_descriptor_80_ea8_32s40s48s56s64s72s_e16_v16?0"NSTask"8l
+ ___block_descriptor_88_e8_32s40s48s56r_e9_v16?0^?8l
+ ___block_descriptor_88_e8_32s40s48s56s_e22_v24?0{_CSTypeRef=QQ}8l
+ ___block_descriptor_96_e8_32bs_e8_Q16?0Q8l
+ ___block_descriptor_98_e8_32s40s48s56s64r_e22_v24?0{_CSTypeRef=QQ}8l
+ ___copy_helper_block_ea8_32s40s48s56s64r
+ ___copy_helper_block_ea8_32s40s48s56s64s72s
+ ___destroy_helper_block_ea8_32s40s48s56s64r
+ ___determineConnectionRequestReplySizes_block_invoke
+ ___determineConnectionRequestReplySizes_block_invoke_2
+ ___determineConnectionRequestReplySizes_block_invoke_3
+ ___determineConnectionRequestReplySizes_block_invoke_4
+ ___determineOSClassInstanceSize_block_invoke
+ ___determineOSClassInstanceSize_block_invoke_2
+ ___determineOSClassInstanceSize_block_invoke_3
+ ___markOthers_block_invoke
+ ___markOthers_block_invoke_2
+ ___markRegionsForMallocZones_block_invoke.458
+ ___markRegionsForMallocZones_block_invoke.458.cold.1
+ ___markRegionsForMallocZones_block_invoke.458.cold.2
+ ___variantForSwiftClass_block_invoke.782
+ ___variantForSwiftClass_block_invoke.783
+ ___variantForSwiftClass_block_invoke.787
+ ___variantForSwiftClass_block_invoke.791
+ ___variantForSwiftClass_block_invoke_2.784
+ ___vmu_swift_reflection_createReflectionContextWithDataLayout_block_invoke
+ __block_literal_global.100
+ __block_literal_global.106
+ __block_literal_global.123
+ __block_literal_global.125
+ __block_literal_global.132
+ __block_literal_global.133
+ __block_literal_global.139
+ __block_literal_global.160
+ __block_literal_global.187
+ __block_literal_global.227
+ __block_literal_global.261
+ __block_literal_global.283
+ __block_literal_global.308
+ __block_literal_global.381
+ __block_literal_global.401
+ __block_literal_global.425
+ __block_literal_global.435
+ __block_literal_global.467
+ __block_literal_global.482
+ __block_literal_global.486
+ __block_literal_global.509
+ __block_literal_global.514
+ __block_literal_global.517
+ __block_literal_global.519
+ __block_literal_global.539
+ __block_literal_global.54
+ __block_literal_global.554
+ __block_literal_global.562
+ __block_literal_global.57
+ __block_literal_global.578
+ __block_literal_global.580
+ __block_literal_global.597
+ __block_literal_global.598
+ __block_literal_global.606
+ __block_literal_global.621
+ __block_literal_global.630
+ __block_literal_global.639
+ __block_literal_global.648
+ __block_literal_global.663
+ __block_literal_global.672
+ __block_literal_global.690
+ __block_literal_global.696
+ __block_literal_global.702
+ __block_literal_global.711
+ __block_literal_global.753
+ __block_literal_global.830
+ __block_literal_global.86
+ __block_literal_global.875
+ __block_literal_global.891
+ __block_literal_global.893
+ __block_literal_global.895
+ __block_literal_global.897
+ __block_literal_global.910
+ __debugSwiftSubfieldIsEnabled_block_invoke.cold.1
+ __determineOSClassInstanceSize_block_invoke.836
+ __determineOSClassInstanceSize_block_invoke.873
+ __dyld_shared_cache_real_path
+ __listKernelCoreRegions_block_invoke.410
+ __listKernelCoreRegions_block_invoke.415
+ __makeStorageFieldClassInfo
+ __markMachOLibraries_block_invoke.441
+ __markMachOLibraries_block_invoke_2.442
+ __remoteZoneIntrospection_block_invoke.84
+ __remoteZoneIntrospection_block_invoke.87
+ __remoteZoneIntrospection_block_invoke.98
+ __remoteZoneIntrospection_block_invoke_2.88
+ __remoteZoneIntrospection_block_invoke_2.88.cold.1
+ __warnIfIntrospectionSymbolOwnersDiffer
+ __xpc_error_connection_invalid
+ __xpc_type_connection
+ _addImage
+ _asyncTaskSlabAllocations
+ _asyncTaskSlabPointer
+ _attributeGraphVMRegionsStartRecorder
+ _childOfInstance
+ _childOfMetadata
+ _childOfTypeRef
+ _classIsSwiftMask
+ _copyDemangledNameForTypeRef
+ _createReflectionContextWithDataLayout
+ _csops_audittoken
+ _debugSwiftAsyncPrintfIsEnabled.cold.1
+ _destroyReflectionContext
+ _determineOSClassInstanceSize
+ _dispatch_activate
+ _dispatch_data_create
+ _dispatch_group_create
+ _dispatch_mach_create
+ _dispatch_mach_msg_create
+ _dumpInfoForInstance
+ _dumpInfoForMetadata
+ _dumpInfoForTypeRef
+ _dumpTypeRef
+ _global_xpcDictionaryStorageClassInfo
+ _global_xpc_connection_size
+ _global_xpc_received_dictionary_size
+ _global_xpc_reply_dictionary_size
+ _infoForInstance
+ _infoForMetadata
+ _infoForTypeRef
+ _isSafeToLoadLibrary
+ _mapped_memory_pointer_to_local_mapping_updated_with_extra_bits
+ _metadataForObject
+ _metadataNominalTypeDescriptor
+ _nw_array_create
+ _nw_frame_create
+ _objc_allocateProtocol
+ _objc_msgSend$_identifyAttributeGraphAllocationsIfPreciseIdentificationIsUnavailable
+ _objc_msgSend$_identifyXPCDictionaryStorageReferencedByBlock:
+ _objc_msgSend$_isUnrealizedObjCClass:recursionDepth:
+ _objc_msgSend$_isaPointerRefersToVTable:remoteAddress:symbol:symbolNameOut:
+ _objc_msgSend$_rangeOfClassStructureForPossibleUnrealizedSwiftClassWithIsa:
+ _objc_msgSend$_untypedMallocBlockNodeReferencedFromAddress:
+ _objc_msgSend$_withReaderBlockForHeapEnumeration:
+ _objc_msgSend$autoreleasePoolOffsets
+ _objc_msgSend$classInfoForDriverKitMemory:length:atOffset:translatedIsa:symbol:remoteAddress:
+ _objc_msgSend$environment
+ _objc_msgSend$findHottestEmptyAutoreleasePoolPage:
+ _objc_msgSend$getCachedScanInfoForClassWithIsa:classInfo:scanCaches:
+ _objc_msgSend$initWithCallGraphFile:fileHeader:topFunctionsList:binaryImagesList:error:
+ _objc_msgSend$initWithRootField:leafField:leafOffsetInRootField:
+ _objc_msgSend$iterateThroughPoolsPerThread:withBlock:
+ _objc_msgSend$labelForCStructureWithMemory:length:remoteAddress:classInfo:
+ _objc_msgSend$labelForOSXPCDictionaryStorageNode:length:remoteAddress:
+ _objc_msgSend$launchTime
+ _objc_msgSend$locateSwiftValuesInAttributeGraph
+ _objc_msgSend$markReachableNodesFromRoots:inMap:
+ _objc_msgSend$memoryTreeHeldByAutoreleasedNode:node:
+ _objc_msgSend$nodeDescription:withDestinationNode:referenceInfo:
+ _objc_msgSend$populateAutoreleasePoolsDetails
+ _objc_msgSend$processInfo
+ _objc_msgSend$reattachAutoreleasePoolsChainFromHottestToColdest:
+ _objc_msgSend$setInstanceSize:
+ _objc_msgSend$setSuperclassOffset:
+ _objc_msgSend$setValidVMRange:
+ _objc_msgSend$srcAddressToExtraAutoreleaseCountDict
+ _objc_opt_self
+ _os_transaction_create
+ _ownsAddress
+ _ownsObject
+ _printCPlusPlusNameSimplification.cold.1
+ _projectEnumValue
+ _projectExistential
+ _singleThreadedMarking.cold.1
+ _typeRefForInstance
+ _typeRefForMangledTypeName
+ _typeRefForMetadata
+ _vmu_swift_reflection_asyncTaskSlabAllocations
+ _vmu_swift_reflection_copyDemangledNameForTypeRef
+ _vmu_swift_reflection_createReflectionContextWithDataLayout
+ _vmu_swift_reflection_metadataForObject
+ _vmu_swift_reflection_metadataNominalTypeDescriptor
+ _vmu_swift_reflection_ownsAddress
+ _vmu_swift_reflection_ownsObject
+ _vmu_swift_reflection_setClassIsSwiftMask
+ _vmu_swift_reflection_typeRefForMangledTypeName
+ _vmu_swift_reflection_typeRefForMetadata
+ _withPeekTransformerFunctionForMemoryReader.cold.1
+ _xpc_array_create
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_create
+ _xpc_connection_create_from_endpoint
+ _xpc_connection_send_message_with_reply_sync
+ _xpc_connection_set_event_handler
+ _xpc_data_create
+ _xpc_date_create
+ _xpc_dictionary_create
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_send_reply
+ _xpc_dictionary_set_string
+ _xpc_double_create
+ _xpc_endpoint_create
+ _xpc_fd_create
+ _xpc_get_type
+ _xpc_int64_create
+ _xpc_pointer_create
+ _xpc_string_create
+ _xpc_uint64_create
+ _xpc_uuid_create
+ _zoneEnumeratorRangeRecorder
+ debugSwiftSubfieldIsEnabled.cold.1
+ determineOSClassInstanceSize.cold.1
+ determineOSClassInstanceSize.globalDispatchMach
+ determineOSClassInstanceSize.globalLog
+ determineOSClassInstanceSize.globalProtocol
+ determineOSClassInstanceSize.onceToken
+ labelForNSXPCInterface:length:remoteAddress:.offsetOfProtocol
+ labelForNSXPCInterface:length:remoteAddress:.onceToken
+ shortenString.cold.1
+ stringFromMappedNSCFData.cold.1
+ vmu_swift_reflection_createReflectionContextWithDataLayout.onceToken
- +[VMUProcessObjectGraph createWithTask:]
- +[VMUScanOverlay foundationHasNSSliceMemoryOptimization]
- -[VMUKernelCoreMemoryScanner scanLocalMemory:atOffset:node:length:isa:fieldInfo:stride:recorder:]
- -[VMUObjectIdentifier _dlopenLibSwiftRemoteMirrorFromDir:]
- -[VMUObjectIdentifier _dlopenLibSwiftRemoteMirrorNearExecutable]
- -[VMUObjectIdentifier _dlopenLibSwiftRemoteMirrorNearLibSwiftCore]
- -[VMUObjectIdentifier _dlopenLibSwiftRemoteMirror]
- -[VMUObjectIdentifier vmRegionRangeForAddress:]
- -[VMUObjectIdentifierDriverKitSupport classInfoForDriverKitMemory:length:atOffset:translatedIsa:symbol:]
- -[VMUTaskMemoryCache getOwnedVMObjectsIntoBuffer:byteCount:].cold.1
- -[VMUTaskMemoryScanner _identifyAttributeGraphAllocations]
- -[VMUTaskMemoryScanner _withMemoryReaderBlock:]
- -[VMUTaskMemoryScanner getCachedScanInfoForClassWithIsa:classInfo:returnedShouldApplySwiftPointerMaskingToIsa:]
- -[VMUTaskMemoryScanner initFullyWithTask:]
- -[VMUTaskMemoryScanner initWithVMUTask:options:].cold.2
- -[VMUTaskMemoryScanner scanLocalMemory:atOffset:node:length:isa:fieldInfo:stride:recorder:]
- GCC_except_table101
- GCC_except_table104
- GCC_except_table108
- GCC_except_table114
- GCC_except_table123
- GCC_except_table124
- GCC_except_table135
- GCC_except_table140
- GCC_except_table147
- GCC_except_table152
- GCC_except_table170
- GCC_except_table171
- GCC_except_table174
- GCC_except_table179
- GCC_except_table180
- GCC_except_table184
- GCC_except_table188
- GCC_except_table197
- GCC_except_table27
- GCC_except_table33
- GCC_except_table45
- GCC_except_table63
- GCC_except_table64
- GCC_except_table92
- OBJC_IVAR_$_VMUKernelCoreMemoryScanner._applySwiftMaskingToIsa
- OBJC_IVAR_$_VMUKernelCoreMemoryScanner._scanCaches
- OBJC_IVAR_$_VMUObjectIdentifier._lastCPlusPlusClassInfo
- OBJC_IVAR_$_VMUObjectIdentifier._lastCPlusPlusIsa
- OBJC_IVAR_$_VMUObjectIdentifier._libSwiftRemoteMirrors
- OBJC_IVAR_$_VMUObjectIdentifier._targetProcessVMranges
- OBJC_IVAR_$_VMUProcessDescription._taskIsCorpseOrCore
- OBJC_IVAR_$_VMUTaskMemoryScanner._applySwiftMaskingToIsa
- OBJC_IVAR_$_VMUTaskMemoryScanner._scanCaches
- _OBJC_CLASS_$_NSValue
- __34-[VMUScanOverlay initWithScanner:]_block_invoke.313
- __34-[VMUScanOverlay initWithScanner:]_block_invoke.461
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_10.553
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_11.571
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_12.577
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_13.583
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_14.592
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_15.634
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_2.346
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_2.474
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_3.350
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_3.478
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_4.487
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_5.502
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_6.511
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_7.520
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_8.529
- __34-[VMUScanOverlay initWithScanner:]_block_invoke_9.544
- __39-[VMUTaskMemoryScanner _fixupBlockIsas]_block_invoke.186
- __39-[VMUTaskMemoryScanner _fixupBlockIsas]_block_invoke.195
- __41-[VMUObjectIdentifier setupIsaTranslator]_block_invoke.167
- __43-[VMUObjectIdentifier findCFTypes_version2]_block_invoke.116
- __45-[VMUKernelCoreMemoryScanner _fixupBlockIsas]_block_invoke.117
- __45-[VMUKernelCoreMemoryScanner _fixupBlockIsas]_block_invoke.126
- __46-[VMUClassInfo _applyExtendedLayout:withSize:]_block_invoke.111
- __47-[VMUVMRegionIdentifier initWithGraph:options:]_block_invoke.139
- __48-[VMUTaskMemoryScanner initWithVMUTask:options:]_block_invoke.48
- __48-[VMUTaskMemoryScanner initWithVMUTask:options:]_block_invoke.58
- __51-[VMUObjectIdentifier loadSwiftReflectionLibraries]_block_invoke.497
- __54-[VMUObjectIdentifier buildIsaToObjectLabelHandlerMap]_block_invoke.209
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.281
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.287
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.290
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.292
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2.291
- __55-[VMUTaskMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2.293
- __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.322
- __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.337
- __56-[VMUTaskMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.354
- __61-[VMUKernelCoreMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.162
- __61-[VMUKernelCoreMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.168
- __61-[VMUKernelCoreMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke.169
- __61-[VMUKernelCoreMemoryScanner scanNodesWithReferenceRecorder:]_block_invoke_2.170
- __62-[VMUKernelCoreMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.199
- __62-[VMUKernelCoreMemoryScanner processSnapshotGraphWithOptions:]_block_invoke.216
- __68-[VMUProcessDescription initWithVMUTaskMemoryCache:getBinariesList:]_block_invoke.56
- __78-[VMUClassInfo instanceSpecificInfoForObject:ofSize:withScanner:memoryReader:]_block_invoke.136
- __78-[VMUClassInfo instanceSpecificInfoForObject:ofSize:withScanner:memoryReader:]_block_invoke_2.131
- __78-[VMUClassInfo instanceSpecificInfoForObject:ofSize:withScanner:memoryReader:]_block_invoke_3.132
- __98-[VMUStackLogReaderBase identifyNonObjectsUsingStackBacktraces:classInfoMap:classInfoSetterBlock:]_block_invoke.311
- __Block_byref_object_copy_.26
- __Block_byref_object_copy_.77
- __Block_byref_object_dispose_.27
- __Block_byref_object_dispose_.78
- __ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kind21swift_typeref_interopP15VMUClassInfoMapjP8NSStringPbj
- __ZL37_debugSwiftSubfieldDumpSwiftChildInfojPKc23swift_childinfo_interopP29SwiftReflectionInteropContext
- __ZL47_debugSwiftSubfieldEnvironmentVariableIsEnabledPKc
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne180100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne180100EPKvm
- __ZNKSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI14RangeAndStringNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI25_CSBinaryImageInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI30_CSBinaryRelocationInformationNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100ERKS6_S9_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS6_IyEEEEEEPvEENS_22__hash_node_destructorINS6_ISI_EEEEE5resetB8ne180100EPSI_
- __ZNSt3__111__sift_downB8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_OT0_NS_15iterator_traitsIS9_E15difference_typeES9_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS5_IyEEEEEELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_performB8ne180100EPNS_11__hash_nodeIS5_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP12VMUClassInfojEENS_22__unordered_map_hasherIS4_S5_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_SA_S8_Lb1EEENS_9allocatorIS5_EEE28__node_insert_unique_prepareB8ne180100EmRS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__116__insertion_sortB8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI10_CSTypeRefEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI14RangeAndStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI25_CSBinaryImageInformationEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI30_CSBinaryRelocationInformationEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__partial_sort_implB8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_S8_EET1_S9_S9_T2_OT0_
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne180100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne180100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne180100EPKcm
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI13SwiftFieldKeyjEEPvEEEEEclB8ne180100EPS7_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUClassInfojEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP12VMUFieldInfojEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringjEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIjU8__strongP8NSStringEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__126__insertion_sort_unguardedB8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEbT1_S9_T0_
- __ZNSt3__131__partition_with_equals_on_leftB8ne180100INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEET0_S9_S9_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8ne180100INS_17_ClassicAlgPolicyEP14RangeAndStringRPFbRKS2_S5_EEENS_4pairIT0_bEESA_SA_T1_
- __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI10_CSTypeRefNS_9allocatorIS1_EEE16__init_with_sizeB8ne180100IPS1_S6_EEvT_T0_m
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEjT1_S9_S9_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_S9_S9_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_S9_S9_S9_T0_
- __ZNSt3__19__sift_upB8ne180100INS_17_ClassicAlgPolicyERPFbRK14RangeAndStringS4_EPS2_EEvT1_S9_OT0_NS_15iterator_traitsIS9_E15difference_typeE
- __ZNSt3__1L19piecewise_constructE
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kind21swift_typeref_interopP15VMUClassInfoMapjP8NSStringPbjE27dispatchEnumConfigOnceToken
- __ZZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kind21swift_typeref_interopP15VMUClassInfoMapjP8NSStringPbjE30preciselyScanMultiPayloadEnums
- __ZZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kind21swift_typeref_interopP15VMUClassInfoMapjP8NSStringPbjE31preciselyScanSinglePayloadEnums
- ___111-[VMUTaskMemoryScanner getCachedScanInfoForClassWithIsa:classInfo:returnedShouldApplySwiftPointerMaskingToIsa:]_block_invoke
- ___41-[VMUObjectIdentifier setupIsaTranslator]_block_invoke_2
- ___47-[VMUTaskMemoryScanner _withMemoryReaderBlock:]_block_invoke
- ___48-[VMUTaskMemoryScanner _addSpecialNodesFromTask]_block_invoke_2
- ___56+[VMUScanOverlay foundationHasNSSliceMemoryOptimization]_block_invoke
- ___58-[VMUTaskMemoryScanner _identifyAttributeGraphAllocations]_block_invoke
- ___66-[VMUObjectIdentifier _dlopenLibSwiftRemoteMirrorNearLibSwiftCore]_block_invoke
- ___77-[VMUClassInfo _determineBinaryPathUsingObjectIdentifier:remoteClassNameLoc:]_block_invoke
- ___97-[VMUKernelCoreMemoryScanner scanLocalMemory:atOffset:node:length:isa:fieldInfo:stride:recorder:]_block_invoke
- ___VMUTask_enumerate_malloc_blocks_block_invoke
- ___VMUTask_enumerate_malloc_blocks_block_invoke_2
- ____ZL25_createFieldInfoFromChildP27libSwiftRemoteMirrorWrapperPKcj17swift_layout_kind21swift_typeref_interopP15VMUClassInfoMapjP8NSStringPbj_block_invoke
- ____shouldScanVMregion_block_invoke
- ____variantForNSSlice_Version1_block_invoke
- ____variantForNSSlice_Version2_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64r_e22_v24?0{_CSTypeRef=QQ}8l
- ___block_descriptor_115_e8_32s40s48s56s64r72r_e22_v24?0{_CSTypeRef=QQ}8l
- ___block_descriptor_40_e8_32s_e20_Q24?0?<^v?QQ>8Q16l
- ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24l
- ___block_descriptor_48_e8_32s40s_e26_"VMUMutableFieldInfo"8?0l
- ___block_descriptor_48_e8_32s40s_e32_v36?0Q8"VMUClassInfo"16I24^B28l
- ___block_descriptor_52_e8_32s40bs_e25_v16?0?<v?Ii?<v?^v>>8l
- ___block_descriptor_52_e8_32s40bs_e9_v16?0^v8l
- ___block_descriptor_56_e8_32s40r48r_e22_v24?0{_CSTypeRef=QQ}8l
- ___block_descriptor_56_e8_32s40r_e34_v32?0"NSString"8"NSValue"16^B24l
- ___block_descriptor_60_e8_32s40bs48r_e25_v24?0"VMUVMRegion"8^B16l
- ___block_descriptor_60_e8_32s40bs_e28_v24?0"VMUFieldInfo"8I16I20l
- ___block_descriptor_60_e8_32s40r48r_e28_v24?0"VMUFieldInfo"8I16I20l
- ___block_descriptor_60_e8_32s40s_e9_v16?0^v8l
- ___block_descriptor_60_e8_32s_e9_v16?0^?8l
- ___block_descriptor_64_e8_32s40bs_e5_B8?0l
- ___block_descriptor_64_e8_32s_e20_Q24?0?<^v?QQ>8Q16l
- ___block_descriptor_64_ea8_32s40s48s56r_e35_v32?0"NSString"8"NSString"16^B24l
- ___block_descriptor_68_e8_32s_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24l
- ___block_descriptor_72_ea8_32s40s48s56s64s_e16_v16?0"NSTask"8l
- ___block_descriptor_80_e8_32s40s48s56s_e22_v24?0{_CSTypeRef=QQ}8l
- ___block_descriptor_88_e20_Q24?0?<^v?QQ>8Q16l
- ___block_descriptor_90_e8_32s40s48s56s64r_e22_v24?0{_CSTypeRef=QQ}8l
- ___block_descriptor_92_e8_32s40s48bs56r64r_e9_v16?0^v8l
- ___copy_helper_block_ea8_32s40s48s56r
- ___copy_helper_block_ea8_32s40s48s56s64s
- ___destroy_helper_block_ea8_32s40s48s56r
- ___destroy_helper_block_ea8_32s40s48s56s64s
- ___markRegionsForMallocZones_block_invoke.457
- ___markRegionsForMallocZones_block_invoke.457.cold.1
- ___markRegionsForMallocZones_block_invoke.457.cold.2
- ___recursivelyCreateSwiftVariant_block_invoke.685
- ___variantForSwiftClass_block_invoke.663
- ___variantForSwiftClass_block_invoke.664
- ___variantForSwiftClass_block_invoke.668
- ___variantForSwiftClass_block_invoke.672
- ___variantForSwiftClass_block_invoke_2.665
- __block_literal_global.105
- __block_literal_global.111
- __block_literal_global.120
- __block_literal_global.122
- __block_literal_global.128
- __block_literal_global.156
- __block_literal_global.157
- __block_literal_global.197
- __block_literal_global.229
- __block_literal_global.251
- __block_literal_global.276
- __block_literal_global.352
- __block_literal_global.354
- __block_literal_global.358
- __block_literal_global.361
- __block_literal_global.377
- __block_literal_global.382
- __block_literal_global.387
- __block_literal_global.398
- __block_literal_global.406
- __block_literal_global.414
- __block_literal_global.422
- __block_literal_global.430
- __block_literal_global.441
- __block_literal_global.444
- __block_literal_global.446
- __block_literal_global.448
- __block_literal_global.46
- __block_literal_global.464
- __block_literal_global.480
- __block_literal_global.484
- __block_literal_global.489
- __block_literal_global.504
- __block_literal_global.513
- __block_literal_global.522
- __block_literal_global.531
- __block_literal_global.555
- __block_literal_global.579
- __block_literal_global.585
- __block_literal_global.594
- __block_literal_global.613
- __block_literal_global.636
- __block_literal_global.718
- __block_literal_global.82
- __listKernelCoreRegions_block_invoke.409
- __listKernelCoreRegions_block_invoke.414
- __markMachOLibraries_block_invoke.440
- __markMachOLibraries_block_invoke_2.441
- __remoteZoneIntrospection_block_invoke.66
- __remoteZoneIntrospection_block_invoke.69
- __remoteZoneIntrospection_block_invoke.80
- __remoteZoneIntrospection_block_invoke_2.70
- __remoteZoneIntrospection_block_invoke_2.70.cold.1
- _access
- _addSpecialNodesFromTask.onceToken.120
- _addSpecialNodesFromTask.webKitMallocFakeRootClassInfo
- _csops
- _dyld_process_is_restricted
- _getsectiondata
- _getsegmentdata
- _objc_msgSend$_dlopenLibSwiftRemoteMirror
- _objc_msgSend$_dlopenLibSwiftRemoteMirrorFromDir:
- _objc_msgSend$_dlopenLibSwiftRemoteMirrorNearExecutable
- _objc_msgSend$_dlopenLibSwiftRemoteMirrorNearLibSwiftCore
- _objc_msgSend$_identifyAttributeGraphAllocations
- _objc_msgSend$classInfoForDriverKitMemory:length:atOffset:translatedIsa:symbol:
- _objc_msgSend$foundationHasNSSliceMemoryOptimization
- _objc_msgSend$initFullyWithTask:
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$pointerValue
- _objc_msgSend$protocol
- _objc_msgSend$rangeForLocation:
- _objc_msgSend$valueWithPointer:
- _object_getClass
- _shouldScanVMregion.onceToken
- _shouldScanVMregion.scanVMRegionWithUnknownPathsEnvVar
- _shouldScanVMregion:.onceToken
- _shouldScanVMregion:.scanVMRegionWithUnknownPathsEnvVar
- _swift_reflection_interop_GetStringLengthAdapter
- _swift_reflection_interop_GetSymbolAddressAdapter
- _swift_reflection_interop_getSizeAdapter
- _swift_reflection_interop_libraryForObject
- _swift_reflection_interop_readBytesAdapter
- _task_find_all_malloc_regions
- _vmu_reflection_interop_asyncTaskSlabAllocations
- _vmu_swift_reflection_createReflectionContext
- _vmu_swift_reflection_interop_addLibrary
- _vmu_swift_reflection_interop_copyDemangledNameForTypeRef
- _vmu_swift_reflection_interop_lookupMetadata
- _vmu_swift_reflection_interop_metadataForObject
- _vmu_swift_reflection_interop_ownsObject
- _vmu_swift_reflection_interop_setClassIsSwiftMask
- _vmu_swift_reflection_interop_typeRefForMangledTypeName
- _vmu_swift_reflection_interop_typeRefForMetadata
- foundationHasNSSliceMemoryOptimization.foundationHasNSSliceMemoryOptimization
- foundationHasNSSliceMemoryOptimization.onceToken
CStrings:
+ "        %u:  "
+ "        Empty\n"
+ "      POOL BOUNDARY\n"
+ "     ** %u:  "
+ "    %s\n"
+ "    no autorelease pool\n"
+ "   COALESCED AUTORELEASES: %u"
+ " for ACTIVE TRANSACTION with"
+ "%s gave { .name = \"%s\", .Offset = %u, .Kind = %s, .TR = { .Typeref = %p (type %s) } }\n"
+ "%s%s\n"
+ "%u block%s  %s bytes"
+ "*** Symbolication:  malloc zone address %#llx is invalid\n"
+ "+ 960"
+ "-[VMUObjectIdentifier setupIsaTranslator]"
+ "/usr/lib/swift/libswiftRemoteMirror.dylib"
+ "<"
+ "<deduplicated_symbol>"
+ "@\"VMULeakDetector\""
+ "@28@0:8^@16I24"
+ "@40@0:8r*16I24I28Q32"
+ "@56@0:8@16^@24^@32^@40^@48"
+ "@60@0:8Q16{swift_typeinfo=iIIII}24@44^{libSwiftRemoteMirrorWrapper=^{_DummyVMUSwiftReflectionContext}QQ}52"
+ "@68@0:8@16@24I32I36I40I44I48@52^Q60"
+ "@72@0:8^v16Q24Q32Q40{_CSTypeRef=QQ}48Q64"
+ "AGMallocZoneGetCurrentSwiftMetadata"
+ "AUTORELEASEPOOLS"
+ "AttributeGraph Data (old mapping)"
+ "AttributeGraph Owned"
+ "AttributeGraph_0x"
+ "Autorelease pool pages not associated with a thread\n"
+ "B28@0:8Q16I24"
+ "B56@0:8Q16Q24{_CSTypeRef=QQ}32r^*48"
+ "Block pointed to by TypeNameCache has non-malloc type \"%s\" (%d)\n"
+ "Bootstrap Dictionary"
+ "Couldn't create task memory cache"
+ "Error occured while printing autoreleasePools per thread.\n"
+ "Failed to create VMUTaskMemoryCache for exclave heap enumeration: %@\n"
+ "Field is single-payload enum containing a pointer (with a nil representation of NULL). Treating as a struct and not varianting.\n"
+ "Found no VM regions in target process"
+ "Found no malloc zones in target process"
+ "Getting fields for Swift value type %s\n"
+ "INCORRECT CHAIN OF @autoreleasepool content BLOCKS -- TRUNCATING THE CHAIN (autoreleasePoolChainCount %u, autoreleasePoolChainMax %u\n"
+ "Invalid minRegionAddress %#llx and/or maxRegionAddress %#llx\n"
+ "JSC::CompleteSubspace::allocatorForSlow"
+ "JSC::CompleteSubspace::tryAllocateSlow"
+ "JSC::FastMallocAlignedMemoryAllocator"
+ "JSC::IsoMemoryAllocatorBase::tryAllocateAlignedMemory"
+ "JSC::LocalAllocator::allocateSlowCase"
+ "Memory directly held only by autorelease pools"
+ "Memory indirectly held only by autorelease pools"
+ "Memory size of autoreleasepool content blocks"
+ "NSXPCInterface"
+ "No autorelease pools"
+ "Not creating classinfo for zero-sized AttributeGraph value\n\n"
+ "OS_dispatch_"
+ "OS_dispatch_data"
+ "OS_dispatch_group"
+ "OS_dispatch_mach_msg"
+ "OS_dispatch_semaphore"
+ "OS_dispatch_source"
+ "OS_nw_array"
+ "OS_nw_frame"
+ "OS_object"
+ "OS_os_log"
+ "OS_xpc_"
+ "OS_xpc_activity"
+ "OS_xpc_array"
+ "OS_xpc_connection"
+ "OS_xpc_data"
+ "OS_xpc_date"
+ "OS_xpc_dictionary"
+ "OS_xpc_double"
+ "OS_xpc_endpoint"
+ "OS_xpc_fd"
+ "OS_xpc_int64"
+ "OS_xpc_pipe"
+ "OS_xpc_pointer"
+ "OS_xpc_serializer"
+ "OS_xpc_session"
+ "OS_xpc_string"
+ "OS_xpc_uint64"
+ "OS_xpc_uuid"
+ "Process:         %@ [%@]\nPath:            %@\nLoad Address:    %#qx\nIdentifier:      %@\nVersion:         %@\n%@Code Type:       %@\n%@Parent Process:  %@ [%@]\nTarget Type:     %@\n"
+ "Protocol"
+ "Reply Message"
+ "Request Message"
+ "SwiftObject"
+ "T@\"NSMutableArray\",&,N,V_threadNamesByThreadIndex"
+ "T@\"NSMutableSet\",&,N,V_unreferencedAutoreleasePoolNodes"
+ "T@\"VMULeakDetector\",R,N,V_detector"
+ "T^I,N,V_autoreleasePoolChain"
+ "T^I,N,V_autoreleasePoolNodesByThreadIndex"
+ "T^Q,R,N,V_swiftTyperef"
+ "T^v,N,V_reachableOutsideOfAutoreleasePoolsMap"
+ "T^{_VMURegionNode=@^IIIQQb1b63^v^{_VMURegionNode}},R,N,V_regions"
+ "T^{libSwiftRemoteMirrorWrapper=^{_DummyVMUSwiftReflectionContext}QQ},R,N,V_swiftMirror"
+ "Thread %u  %s\n"
+ "Total entries in autoreleasepools"
+ "Total memory of autorelease pools and content blocks"
+ "T{?=BB^I},N,V_options"
+ "T{?=IIIIIQIQ},R,N,V_autoreleasePoolsStatsInfo"
+ "T{?=III},R,N,V_offsets"
+ "T{_VMURange=QQ},N,V_validVMRange"
+ "Unable to verify csops flags"
+ "Unique entries in autoreleasepools"
+ "VMUAutoreleasePoolsAnalyzer"
+ "VMUCachedPointerFieldInfo"
+ "VMUObjectIdentifier.m"
+ "VMUScanOverlay.m"
+ "Value has size %llu, but Remote Mirror reports a size of %u.  Ignoring Remote Mirror output and scanning conservatively.\n"
+ "WTF::fastCompactAlignedMalloc"
+ "WTF::fastCompactCalloc"
+ "WTF::fastCompactMalloc"
+ "WTF::fastCompactMemDup"
+ "WTF::fastCompactRealloc"
+ "WTF::fastCompactStrDup"
+ "WTF::fastCompactZeroedMalloc"
+ "WTF::tryFastCompactAlignedMalloc"
+ "WTF::tryFastCompactCalloc"
+ "WTF::tryFastCompactMalloc"
+ "WTF::tryFastCompactRealloc"
+ "WTF::tryFastCompactZeroedMalloc"
+ "WebKit"
+ "WebKit Owned"
+ "^{_VMUBlockNode=Qb3b2b36b23}24@0:8r^v16"
+ "^{_VMURegionNode=@^IIIQQb1b63^v^{_VMURegionNode}}"
+ "^{_VMURegionNode=@^IIIQQb1b63^v^{_VMURegionNode}}16@0:8"
+ "^{_VMURegionNode=@^IIIQQb1b63^v^{_VMURegionNode}}36@0:8{_VMURange=QQ}16B32"
+ "^{libSwiftRemoteMirrorWrapper=^{_DummyVMUSwiftReflectionContext}QQ}"
+ "^{libSwiftRemoteMirrorWrapper=^{_DummyVMUSwiftReflectionContext}QQ}16@0:8"
+ "_AGMallocZoneGetCurrentSwiftMetadata"
+ "_TtCs12_SwiftObject"
+ "__IncompleteProtocol"
+ "__objc_empty_cache"
+ "_arr"
+ "_attributeGraphFakeRootNode"
+ "_attributeGraphSwiftMetadataToClassInfo"
+ "_attributeGraphZoneIndex"
+ "_autoreleasePoolChain"
+ "_autoreleasePoolNodesByThreadIndex"
+ "_autoreleasePoolsStatsInfo"
+ "_buff"
+ "_detector"
+ "_identifyAttributeGraphAllocationsIfPreciseIdentificationIsUnavailable"
+ "_identifyXPCDictionaryStorageReferencedByBlock:"
+ "_isUnrealizedObjCClass:recursionDepth:"
+ "_isaPointerRefersToVTable:remoteAddress:symbol:symbolNameOut:"
+ "_lastClassInfoForMemoryClassInfo"
+ "_lastClassInfoForMemoryIsa"
+ "_leafField"
+ "_leafOffsetInRootField"
+ "_objc"
+ "_objcEmptyCacheAddress"
+ "_offsets"
+ "_protocol"
+ "_rangeOfClassStructureForPossibleUnrealizedSwiftClassWithIsa:"
+ "_reachableOutsideOfAutoreleasePoolsMap"
+ "_rootField"
+ "_setSuperclassOffset:"
+ "_swiftValueInAttributeGraphAddressesToTypeMetadata"
+ "_table[%u]"
+ "_threadNamesByThreadIndex"
+ "_unreferencedAutoreleasePoolNodes"
+ "_untypedMallocBlockNodeReferencedFromAddress:"
+ "_validVMRange"
+ "_withReaderBlockForHeapEnumeration:"
+ "_xpcDictionaryStorageClassInfoIndex"
+ "a"
+ "autoreleasePoolChain"
+ "autoreleasePoolNodesByThreadIndex"
+ "autoreleasePoolsStatsInfo"
+ "bmalloc_allocate..."
+ "cameracaptured"
+ "classInfo.instanceSize >= tableOffset + tableSize"
+ "classInfoForDriverKitMemory:length:atOffset:translatedIsa:symbol:remoteAddress:"
+ "configd"
+ "core file"
+ "corpse"
+ "createWithTask:error:"
+ "detector"
+ "determineOSClassInstanceSize"
+ "dispatch_data_t"
+ "dispatch_group_t"
+ "dispatch_mach_msg_t"
+ "dispatch_mach_t"
+ "dispatch_semaphore_t"
+ "dispatch_source_t"
+ "environment"
+ "failed to create mapped memory cache: %s"
+ "failed to resolve canonical path for % in dyld shared cache."
+ "findHottestEmptyAutoreleasePoolPage:"
+ "getCachedScanInfoForClassWithIsa:classInfo:scanCaches:"
+ "i24@0:8^{_DummyVMUSwiftReflectionContext=}16"
+ "identifier"
+ "initWithCallGraphFile:fileHeader:topFunctionsList:binaryImagesList:error:"
+ "initWithRootField:leafField:leafOffsetInRootField:"
+ "invalid zone pointer"
+ "iterateAutoreleasePoolsInThreadsGroupingByType:showVirtualSize:extraReleasesCount:withBlock:"
+ "iterateThroughPoolsPerThread:withBlock:"
+ "key: \"%@\""
+ "labelForCStructureWithMemory:length:remoteAddress:classInfo:"
+ "labelForOSXPCDictionaryStorageNode:length:remoteAddress:"
+ "labelForOSXPCString:length:remoteAddress:"
+ "labelForSwiftContiguousArrayStorage:length:remoteAddress:"
+ "labelForSwiftDictionaryStorage:length:remoteAddress:"
+ "labelForSwiftSetStorage:length:remoteAddress:"
+ "launchTime"
+ "live task"
+ "locateSwiftValuesInAttributeGraph"
+ "memoryTreeHeldByAutoreleasedNode:node:"
+ "no posix thread"
+ "offsets"
+ "pas_msl_malloc_logging_slow"
+ "populateAutoreleasePoolsDetails"
+ "processInfo"
+ "r^{_VMUScanLocationCache=b24b6b1b1}36@0:8I16@20^^{_VMUScanLocationCache}28"
+ "reachableOutsideOfAutoreleasePoolsMap"
+ "reattachAutoreleasePoolsChainFromHottestToColdest:"
+ "setAutoreleasePoolChain:"
+ "setAutoreleasePoolNodesByThreadIndex:"
+ "setOptions:"
+ "setReachableOutsideOfAutoreleasePoolsMap:"
+ "setSuperclassOffset:"
+ "setThreadNamesByThreadIndex:"
+ "setUnreferencedAutoreleasePoolNodes:"
+ "setValidVMRange:"
+ "swift_reflection_asyncTaskSlabAllocations unavailable on bridgeOS"
+ "swift_reflection_metadataNominalTypeDescriptor"
+ "taskIsCorpse"
+ "the provided call tree file %s contains non-UTF8 data\n"
+ "threadNamesByThreadIndex"
+ "unexpected configuration. leaks is expected to either run with library validation or to be debuggable"
+ "unreferencedAutoreleasePoolNodes"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v16@?0@8"
+ "v20@?0I8@\"NSString\"12"
+ "v24@0:8^{_VMUBlockNode=Qb3b2b36b23}16"
+ "v28@?0Q8@\"NSObject<OS_dispatch_mach_msg>\"16i24"
+ "v32@0:8{?=BB^I}16"
+ "v40@0:8B16B20^I24@?32"
+ "v48@0:8@16r*24I32I36Q40"
+ "validVMRange"
+ "xctest"
+ "xpc_activity_t"
+ "xpc_array_t"
+ "xpc_connection_t"
+ "xpc_data_t"
+ "xpc_date_t"
+ "xpc_dictionary_t"
+ "xpc_double_t"
+ "xpc_endpoint_t"
+ "xpc_fd_t"
+ "xpc_int64_t"
+ "xpc_pipe_t"
+ "xpc_pointer_t"
+ "xpc_serializer_t"
+ "xpc_session_t"
+ "xpc_string_t"
+ "xpc_uint64_t"
+ "xpc_uuid_t"
+ "{?=\"groupByType\"B\"referenceTreeShowRegionVirtualSize\"B\"autoreleasePoolsExtraReleasesCount\"^I}"
+ "{?=\"parentPageOffset\"I\"childPageOffset\"I\"firstEntryOffset\"I}"
+ "{?=\"totalEntriesInAutoreleasePools\"I\"uniqueEntriesInAutoreleasePools\"I\"autoreleasePoolContentPageCount\"I\"autoreleasePoolContentPageTotalSize\"I\"directlyHeldOnlyInAutoreleasePoolsCount\"I\"directlyHeldOnlyInAutoreleasePoolsSize\"Q\"reachableOnlyFromAutoreleasePoolsCount\"I\"reachableOnlyFromAutoreleasePoolsSize\"Q}"
+ "{?=BB^I}16@0:8"
+ "{?=IIIIIQIQ}16@0:8"
- " (Key Storage)"
- " (Value Storage)"
- "%s gave { .name = \"%s\", .Offset = %u, .Kind = %s, .TR = { .Typeref = %p (type %s), .Library = %d } }\n"
- "%s/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/macosx"
- "-[VMUTaskMemoryScanner _initWithTask:options:]: region identifier detected no regions, so returning nil VMUTaskMemoryScanner"
- ".fields"
- "/System/Cryptexes/OS/"
- "/System/Library/Frameworks/WebKit.framework/Versions/A/WebKit"
- "/usr/lib/libxcselect.dylib"
- "/usr/lib/swift"
- "1"
- "@48@0:8r*16I24I28{swift_typeref_interop=Qi}32"
- "@60@0:8Q16{swift_typeinfo=iIIII}24@44^{libSwiftRemoteMirrorWrapper=^{SwiftReflectionInteropContext}QQ}52"
- "@64@0:8^v16Q24Q32Q40{_CSTypeRef=QQ}48"
- "@68@0:8@16@24I32I36I40I44I48@52^v60"
- "Failed to create mapped memory cache."
- "Failed to find Remote Mirror function asyncTaskSlabAllocations"
- "Failed to find Remote Mirror function asyncTaskSlabPointer"
- "Process:         %@ [%@]\nPath:            %@\nLoad Address:    %#qx\nIdentifier:      %@\nVersion:         %@\n%@Code Type:       %@\n%@Parent Process:  %@ [%@]\n"
- "Q24@?0@?<^v@?QQ>8Q16"
- "Request/Reply message for active transaction with "
- "Resources"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Failed to dlopen %@"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Loaded Swift Remote Mirror from %@"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Successfully dlopened %@"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Unable to access %@ with errno: %d"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: swift_reflection_interop_addLibrary failed for %@"
- "T^v,R,V_swiftTyperef"
- "T^{_VMURegionNode=@^IIIQQQ^v^{_VMURegionNode}},R,N,V_regions"
- "T^{libSwiftRemoteMirrorWrapper=^{SwiftReflectionInteropContext}QQ},R,N,V_swiftMirror"
- "WebKit Malloc Fake Root"
- "^^{_VMUScanLocationCache}"
- "^{_VMURegionNode=@^IIIQQQ^v^{_VMURegionNode}}"
- "^{_VMURegionNode=@^IIIQQQ^v^{_VMURegionNode}}16@0:8"
- "^{_VMURegionNode=@^IIIQQQ^v^{_VMURegionNode}}36@0:8{_VMURange=QQ}16B32"
- "^{libSwiftRemoteMirrorWrapper=^{SwiftReflectionInteropContext}QQ}"
- "^{libSwiftRemoteMirrorWrapper=^{SwiftReflectionInteropContext}QQ}16@0:8"
- "_Tt"
- "__swift3_assocty"
- "__swift3_builtin"
- "__swift3_capture"
- "__swift3_fieldmd"
- "__swift3_reflstr"
- "__swift3_typeref"
- "_applySwiftMaskingToIsa"
- "_dlopenLibSwiftRemoteMirror"
- "_dlopenLibSwiftRemoteMirrorFromDir:"
- "_dlopenLibSwiftRemoteMirrorNearExecutable"
- "_dlopenLibSwiftRemoteMirrorNearLibSwiftCore"
- "_identifyAttributeGraphAllocations"
- "_lastCPlusPlusClassInfo"
- "_lastCPlusPlusIsa"
- "_libSwiftRemoteMirrors"
- "_list"
- "_objs"
- "_scanCaches"
- "_targetProcessVMranges"
- "_taskIsCorpseOrCore"
- "_xconnection"
- "acquisitionProps"
- "classInfoForDriverKitMemory:length:atOffset:translatedIsa:symbol:"
- "createWithTask:"
- "for security, cannot load non-system library %s"
- "for security, cannot load non-system library %s from unsafe path into ReportCrash"
- "foundationHasNSSliceMemoryOptimization"
- "i24@0:8^{SwiftReflectionInteropContext=}16"
- "initFullyWithTask:"
- "libclang_rt.asan"
- "libclang_rt.tsan"
- "libswiftRemoteMirror42.dylib"
- "libswiftRemoteMirrorLegacy.dylib"
- "pathWithComponents:"
- "pointerValue"
- "protocol"
- "swift_reflection_addReflectionInfo"
- "swift_reflection_createReflectionContext"
- "swift_reflection_genericArgumentCountOfTypeRef"
- "swift_reflection_genericArgumentOfTypeRef"
- "swift_reflection_getSupportedMetadataVersion"
- "swift_reflection_readIsaMask"
- "usbd"
- "v32@?0@\"NSString\"8@\"NSValue\"16^B24"
- "v56@0:8@16r*24I32I36{swift_typeref_interop=Qi}40"
- "valueWithPointer:"
- "vmRegionRangeForAddress:"
- "xcselect_get_developer_dir_path"
- "{NSSliceFields}"

```
