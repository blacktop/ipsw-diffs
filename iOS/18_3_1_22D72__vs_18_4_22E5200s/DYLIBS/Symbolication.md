## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64567.3.3.0.0
-  __TEXT.__text: 0xa79bc
-  __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0x5d4c
+64570.53.1.0.0
+  __TEXT.__text: 0xa9d20
+  __TEXT.__auth_stubs: 0x1f70
+  __TEXT.__objc_methlist: 0x6398
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xf136
-  __TEXT.__gcc_except_tab: 0x4c5c
-  __TEXT.__oslogstring: 0x160a
+  __TEXT.__cstring: 0xf5be
+  __TEXT.__gcc_except_tab: 0x4f1c
+  __TEXT.__oslogstring: 0x1614
   __TEXT.__ustring: 0x24
-  __TEXT.__unwind_info: 0x26e0
-  __TEXT.__objc_classname: 0x7df
-  __TEXT.__objc_methname: 0xe8f5
-  __TEXT.__objc_methtype: 0x82f9
-  __TEXT.__objc_stubs: 0x9500
+  __TEXT.__unwind_info: 0x27c8
+  __TEXT.__objc_classname: 0x81d
+  __TEXT.__objc_methname: 0xf011
+  __TEXT.__objc_methtype: 0x8597
+  __TEXT.__objc_stubs: 0x9680
   __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x3398
-  __DATA_CONST.__objc_classlist: 0x2a8
+  __DATA_CONST.__const: 0x3588
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32f0
-  __DATA_CONST.__objc_superrefs: 0x1e8
-  __DATA_CONST.__objc_arraydata: 0x718
-  __AUTH_CONST.__auth_got: 0xff8
-  __AUTH_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__objc_selrefs: 0x3440
+  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_arraydata: 0x700
+  __AUTH_CONST.__auth_got: 0xfd0
+  __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0xaa8
-  __AUTH_CONST.__cfstring: 0xc6a0
-  __AUTH_CONST.__objc_const: 0xbf38
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__cfstring: 0xcc80
+  __AUTH_CONST.__objc_const: 0xb9b0
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x2d0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc24
+  __DATA.__objc_ivar: 0xc54
   __DATA.__data: 0xce8
-  __DATA.__bss: 0x530
-  __DATA.__common: 0x9
+  __DATA.__bss: 0x520
+  __DATA.__common: 0xd9
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2869
-  Symbols:   3745
-  CStrings:  5748
+  Functions: 2961
+  Symbols:   3895
+  CStrings:  5852
 
Symbols:
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_VMUAutoreleasePoolsAnalyzer
+ _OBJC_METACLASS_$_VMUAutoreleasePoolsAnalyzer
+ _VMUCallMallocEnumeratorWithAttributeGraphWorkaround
+ _VMUGraphNodeIsRoot
+ _VMUGraphNodeIsSpecialMallocNode
+ __dyld_shared_cache_real_path
+ _csops_audittoken
+ _objc_opt_self
+ _objc_retain_x11
+ _objc_retain_x13
- _OBJC_CLASS_$_NSValue
- _OBJC_CLASS_$_NSXPCInterface
- _access
- _class_getInstanceSize
- _closedir
- _csops
- _dyld_process_is_restricted
- _getsectiondata
- _getsegmentdata
- _object_getClass
- _opendir
- _readdir
CStrings:
+ "\x01\x113cA\x11!Q2q\x14!\"\x11\x121"
+ "\x0113cA\x11!Q\x12a\x14!\"\x11\x12\x13"
+ "\x012\x11\xa5\x14\x12"
+ "\x01ASB\x11%a$#\xa3"
+ "\x021"
+ "\x12"
+ "        %u:  "
+ "        Empty\n"
+ "      POOL BOUNDARY\n"
+ "     ** %u:  "
+ "    %s\n"
+ "    no autorelease pool\n"
+ "   COALESCED AUTORELEASES: %u"
+ "%s gave { .name = \"%s\", .Offset = %u, .Kind = %s, .TR = { .Typeref = %p (type %s) } }\n"
+ "%s%s\n"
+ "%u block%s  %s bytes"
+ "+ 960"
+ "-[VMUObjectIdentifier setupIsaTranslator]"
+ "/usr/lib/swift/libswiftRemoteMirror.dylib"
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
+ "OS_xpc_connection"
+ "Process:         %@ [%@]\nPath:            %@\nLoad Address:    %#qx\nIdentifier:      %@\nVersion:         %@\n%@Code Type:       %@\n%@Parent Process:  %@ [%@]\nTarget Type:     %@\n"
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
+ "^{_VMURegionNode=@^IIIQQb1b63^v^{_VMURegionNode}}"
+ "^{_VMURegionNode=@^IIIQQb1b63^v^{_VMURegionNode}}16@0:8"
+ "^{_VMURegionNode=@^IIIQQb1b63^v^{_VMURegionNode}}36@0:8{_VMURange=QQ}16B32"
+ "^{libSwiftRemoteMirrorWrapper=^{_DummyVMUSwiftReflectionContext}QQ}"
+ "^{libSwiftRemoteMirrorWrapper=^{_DummyVMUSwiftReflectionContext}QQ}16@0:8"
+ "_AGMallocZoneGetCurrentSwiftMetadata"
+ "_TtCs12_SwiftObject"
+ "__objc_empty_cache"
+ "_attributeGraphFakeRootNode"
+ "_attributeGraphSwiftMetadataToClassInfo"
+ "_attributeGraphZoneIndex"
+ "_autoreleasePoolChain"
+ "_autoreleasePoolNodesByThreadIndex"
+ "_autoreleasePoolsStatsInfo"
+ "_detector"
+ "_identifyAttributeGraphAllocationsIfPreciseIdentificationIsUnavailable"
+ "_isUnrealizedObjCClass:recursionDepth:"
+ "_isaPointerRefersToVTable:remoteAddress:symbol:symbolNameOut:"
+ "_lastClassInfoForMemoryClassInfo"
+ "_lastClassInfoForMemoryIsa"
+ "_leafField"
+ "_leafOffsetInRootField"
+ "_objc"
+ "_objcEmptyCacheAddress"
+ "_offsets"
+ "_rangeOfClassStructureForPossibleUnrealizedSwiftClassWithIsa:"
+ "_reachableOutsideOfAutoreleasePoolsMap"
+ "_rootField"
+ "_swiftValueInAttributeGraphAddressesToTypeMetadata"
+ "_threadNamesByThreadIndex"
+ "_unreferencedAutoreleasePoolNodes"
+ "_validVMRange"
+ "_withReaderBlockForHeapEnumeration:"
+ "a"
+ "autoreleasePoolChain"
+ "autoreleasePoolNodesByThreadIndex"
+ "autoreleasePoolsStatsInfo"
+ "bmalloc_allocate..."
+ "cameracaptured"
+ "classInfoForDriverKitMemory:length:atOffset:translatedIsa:symbol:remoteAddress:"
+ "configd"
+ "core file"
+ "corpse"
+ "createWithTask:error:"
+ "detector"
+ "environment"
+ "failed to create mapped memory cache: %s"
+ "failed to resolve canonical path for % in dyld shared cache."
+ "findHottestEmptyAutoreleasePoolPage:"
+ "getCachedScanInfoForClassWithIsa:classInfo:scanCaches:"
+ "i24@0:8^{_DummyVMUSwiftReflectionContext=}16"
+ "initWithCallGraphFile:fileHeader:topFunctionsList:binaryImagesList:error:"
+ "initWithRootField:leafField:leafOffsetInRootField:"
+ "iterateAutoreleasePoolsInThreadsGroupingByType:showVirtualSize:extraReleasesCount:withBlock:"
+ "iterateThroughPoolsPerThread:withBlock:"
+ "labelForSwiftContiguousArrayStorage:length:remoteAddress:"
+ "labelForSwiftDictionaryStorage:length:remoteAddress:"
+ "labelForSwiftSetStorage:length:remoteAddress:"
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
+ "v32@0:8{?=BB^I}16"
+ "v40@0:8B16B20^I24@?32"
+ "v48@0:8@16r*24I32I36Q40"
+ "validVMRange"
+ "xctest"
+ "{?=\"groupByType\"B\"referenceTreeShowRegionVirtualSize\"B\"autoreleasePoolsExtraReleasesCount\"^I}"
+ "{?=\"parentPageOffset\"I\"childPageOffset\"I\"firstEntryOffset\"I}"
+ "{?=\"totalEntriesInAutoreleasePools\"I\"uniqueEntriesInAutoreleasePools\"I\"autoreleasePoolContentPageCount\"I\"autoreleasePoolContentPageTotalSize\"I\"directlyHeldOnlyInAutoreleasePoolsCount\"I\"directlyHeldOnlyInAutoreleasePoolsSize\"Q\"reachableOnlyFromAutoreleasePoolsCount\"I\"reachableOnlyFromAutoreleasePoolsSize\"Q}"
+ "{?=BB^I}16@0:8"
+ "{?=IIIIIQIQ}16@0:8"
- "\x01\x113cA\x11!QBq\x14!\"\x11\x121"
- "\x01\x12\x11\xa5\x14\x12"
- "\x0113cA\x11!Q2a\x14!\"\x11\x12\x13"
- "\x01ASC\x16a$$\x91"
- " (Key Storage)"
- " (Value Storage)"
- "%s gave { .name = \"%s\", .Offset = %u, .Kind = %s, .TR = { .Typeref = %p (type %s), .Library = %d } }\n"
- "-[VMUTaskMemoryScanner _initWithTask:options:]: region identifier detected no regions, so returning nil VMUTaskMemoryScanner"
- ".fields"
- "/Developer/usr/lib/swift"
- "/System/Cryptexes/OS/"
- "/System/Library/Frameworks/WebKit.framework/Versions/A/WebKit"
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
- "Resources"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Failed to dlopen %@"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Loaded Swift Remote Mirror from %@"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Successfully dlopened %@"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: Unable to access %@ with errno: %d"
- "SYMBOLICATION_DEBUG_SWIFT_REMOTE_MIRROR: libswiftCore is in App bundle. Its corresponding remote mirror may not be in the trust cache. Skipping."
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
- "{NSSliceFields}"

```
